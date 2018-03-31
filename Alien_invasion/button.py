import pygame

class Rectangle():
	def __init__(self,screen,ai_settings):
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings=ai_settings

		self.width,self.height=self.ai_settings.button_width,self.ai_settings.button_height
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		
		
		# The button message needs to be prepped only once.
		self.prep_msg(self.ai_settings.button_msg)

	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.ai_settings.text_color,
		self.ai_settings	.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.ai_settings.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

