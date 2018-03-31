"""control structure of player's ship"""
import pygame
import os
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.image=pygame.image.load(os.path.join('images','ship.bmp'))
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		
		"""getting the rectangles right."""
		self.rect=self.image.get_rect()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings

		"""getting positions right."""
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom =self.screen_rect.bottom

		self.center_x=float(self.rect.centerx)
		self.bottom=float(self.rect.bottom)
		
		
	def blit_me(self):
		"""Draw the ship at its current location."""	
		self.screen.blit(self.image, self.rect)#self.screen  or screen pass kr ke screen.blit krun

	def update_position(self):
		
		if(self.moving_right and self.rect.right<=self.screen_rect.right):
			self.center_x+=float(self.ai_settings.ship_speed)
		if(self.moving_left and self.rect.left>=self.screen_rect.left):
			self.center_x-=float(self.ai_settings.ship_speed)
		if(self.moving_up and self.rect.top>=self.screen_rect.top):
			self.bottom-=float(self.ai_settings.ship_speed)
		if(self.moving_down and self.rect.bottom<=self.screen_rect.bottom):
			self.bottom+=float(self.ai_settings.ship_speed)

		self.rect.centerx=self.center_x
		self.rect.bottom=self.bottom

	def reset(self):
		self.center_x=self.screen_rect.centerx
		self.bottom=self.screen_rect.bottom		

		self.rect.centerx=self.center_x
		self.rect.bottom=self.bottom