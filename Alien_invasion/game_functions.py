"""stores game_functions encapsulation"""
import sys
import pygame
import shelve
from bullets import Bullet
from aliens import Alien
from time import sleep
from rectangles import Rectangle

#########################################################################################################
def check_keyUPs(event,ship):
	"""checks if the key is released"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=(False)
	elif event.key==pygame.K_LEFT:
		ship.moving_left=(False)	
	elif event.key==pygame.K_UP:
		ship.moving_up=(False)	
	elif event.key==pygame.K_DOWN:
		ship.moving_down=(False)

def check_mouse_button(button,coordinates,stats):
	if button.rect.collidepoint(*coordinates):
		stats.game_active=True
		pygame.mouse.set_visible(False)

def check_keyDOWNS(event,ship,screen,ai_settings,bullets,aliens,stats,scoreboard):
	"""checks if the key is pressed"""
	if event.key==pygame.K_r:
		update_highscore(stats.highscore)
		reset(ship,aliens, bullets, stats,ai_settings)
		scoreboard.prep_level()
		scoreboard.prep_ships()
		scoreboard.prep_score()
		stats.game_active=True
		create_aliens_fleet(aliens,screen,ai_settings)
		sleep(.7)
		pygame.mouse.set_visible(False)
	elif event.key == pygame.K_SPACE:
		if len(bullets)<ai_settings.limit_bullets :
				new_bullet = Bullet(ai_settings, screen, ship)
				bullets.add(new_bullet)

	elif event.key==pygame.K_p:
		if stats.game_active:
			stats.game_active=False
		else:
			stats.game_active=True
			sleep(.7)
	
	elif event.key==pygame.K_RIGHT:
		ship.moving_right=(True)
	elif event.key==pygame.K_LEFT:
		ship.moving_left=(True)	
	elif event.key==pygame.K_UP:
		ship.moving_up=(True)	
	elif event.key==pygame.K_DOWN:
		ship.moving_down=(True)	
	# Create a new bullet and add it to the bullets group.





def check_events(ship,screen,ai_settings,bullets,aliens,stats,button,scoreboard):
	"""Contains the main event check for loop"""
	for event in pygame.event.get():
		"""Listening to events"""
		if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
			update_highscore(stats.highscore)
			sys.exit()
		elif (not stats.game_active) and event.type==pygame.MOUSEBUTTONDOWN:
			check_mouse_button(button,pygame.mouse.get_pos(),stats)
		elif event.type==pygame.KEYDOWN:
			check_keyDOWNS(event,ship,screen,ai_settings,bullets,aliens,stats,scoreboard)
		elif event.type==pygame.KEYUP:
			check_keyUPs(event,ship)

#########################################################################################################

def get_number_aliens_x(screen,ai_settings):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = screen.get_rect().width - 2 * alien_width
	return int(available_space_x / (2 * alien_width))

def get_number_aliens_y(screen,ai_settings):
	alien = Alien(ai_settings, screen)
	alien_height = alien.rect.height
	available_space_y = screen.get_rect().height - 4 * alien.rect.height
	return int(available_space_y / (2 * alien_height))

def create_alien(screen,ai_settings,column,row):
	alien = Alien(ai_settings, screen)
	alien_width=alien.rect.width
	alien_height=alien.rect.height
	alien.x = alien_width + 2 * alien_width * column
	alien.y = alien_height + 2 * alien_height * row
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	return alien

def create_aliens_fleet(aliens,screen,ai_settings):
	number_aliens_x =get_number_aliens_x(screen,ai_settings)
	number_aliens_y =get_number_aliens_y(screen,ai_settings)
	# Create the first row of aliens.
	for row in range(number_aliens_y):
		for column in range(number_aliens_x):
			# Create an alien and place it in the row.
			alien=create_alien(screen,ai_settings,column,row)
			aliens.add(alien)

#########################################################################################################
	
def change_fleet_direction(ai_settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
	
def update_aliens(ai_settings, aliens):
	"""
	Check if the fleet is at an edge,
	and then update the postions of all aliens in the fleet.
	"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()


def update_bullets(bullets):
	"""Handles the motion and deletion of fired bullets"""
	# movement
	bullets.update()
	# removing the out of screen bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom<=bullet.screen.get_rect().top:
			bullets.remove(bullet)
def update_highscore(highscore):
	shelveFile=shelve.open("highscore")
	shelveFile['score']=str(highscore)
	shelveFile.close()

def check_for_highscore(stats,scoreboard):
	if stats.score>stats.highscore:
		stats.highscore=stats.score
		scoreboard.prep_high_score()
	return None

def level_up(ship,ai_settings,bullets,stats):
	bullets.empty()
	ship.reset()
	ai_settings.update_settings()
	stats.level+=1

def ship_loose(ship,screen,ai_settings,aliens, bullets, stats):
	# ship left reduce
	stats.ships_left-=1
	if stats.ships_left>=0:		#if still left
		ship.reset()
		aliens.empty()
		bullets.empty()
		# pause
		sleep(.5)
	else:
		update_highscore(stats.highscore)
		reset(ship,aliens,bullets,stats,ai_settings)
	create_aliens_fleet(aliens,screen,ai_settings)


def aliens_reach_bottom(screen,aliens):
	for alien in aliens:
		if alien.rect.bottom>=screen.get_rect().bottom:
			return True
	return False
		 
def check_collisions(ship,screen,ai_settings,aliens,bullets,stats,scoreboard):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for values in collisions.values():
			stats.score+=int(len(values)*ai_settings.score_speed)
		scoreboard.prep_score()
		check_for_highscore(stats,scoreboard)

	if pygame.sprite.spritecollideany(ship, aliens) or aliens_reach_bottom(screen,aliens):
		ship_loose(ship,screen,ai_settings,aliens, bullets, stats)
		scoreboard.prep_ships()

	if len(aliens)==0:
		create_aliens_fleet(aliens,screen,ai_settings)
		level_up(ship,ai_settings,bullets,stats)	
		scoreboard.prep_level()

def update_menu(scoreboard):
	scoreboard.show_score()

def update_screen(ship,screen,ai_settings,bullets,aliens,stats,play,scoreboard):
	"""every new frame it handles the making of screen with updated attributes"""
	if not stats.game_active:
		screen.fill((50,50,50))
		play.draw_rectangle()
	else:
		# fill the background
		screen.fill(ai_settings.bg_color)		
		# Redraw every bullets fired on the screen
		aliens.draw(screen)
		for bullet in bullets.sprites():
			bullet.draw()
		# Redraw the ship
		ship.blit_me()
		update_menu(scoreboard)	
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	

def reset(ship,aliens,bullets,stats,ai_settings):
	aliens.empty()
	bullets.empty()
	stats.reset()
	ship.reset()
	ai_settings.reset()
	pygame.mouse.set_visible(True)