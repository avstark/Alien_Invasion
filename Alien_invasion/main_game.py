#!/usr/bin/env python
import pygame
import game_functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(ai_settings.dimentions)
	pygame.display.set_caption("ALIEN X")
	ship=Ship(ai_settings,screen)
	pygame.display.set_icon(ship.image)
	bullets=Group()
	aliens=Group()
	game_functions.create_aliens_fleet(aliens,screen,ai_settings)
	stats=GameStats(ai_settings)
	
	play=game_functions.Rectangle(screen,ai_settings,"Play")

	scoreboard=Scoreboard(ai_settings,screen,stats)
	
	"""Start the  main loop for the game."""
	while True:
		# game_control_loop 
		game_functions.check_events(ship,screen,ai_settings,bullets,aliens,stats,play,scoreboard)
		if stats.game_active:
			# moving the ship accordingly  
			ship.update_position()
			# updating  the group of aliens
			game_functions.update_aliens(ai_settings,aliens)
			# updating the group of bullets
			game_functions.update_bullets(bullets)
			# check for any collision
			game_functions.check_collisions(ship,screen,ai_settings,aliens,bullets,stats,scoreboard)
			# update screen with recent changes
		game_functions.update_screen(ship,screen,ai_settings,bullets,aliens,stats,play,scoreboard)


if __name__=='__main__':
	run_game()
	
 
