import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = screen
		self.ai_settings=ai_settings
		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect=pygame.Rect(ship.rect.centerx,ship.rect.top,
			ai_settings.bullet_width,ai_settings.bullet_height)
		# self.rect.centerx = ship.rect.centerx
		# self.rect.top = ship.rect.top
		#Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.speed_factor = self.ai_settings.bullet_speed
		self.y -= self.speed_factor
		# Update the rect position.
		self.rect.y = self.y

	def draw(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)