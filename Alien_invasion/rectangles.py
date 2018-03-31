import pygame

class Rectangle():
	def __init__(self,screen,settings,msg):
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings=settings

		self.rect = pygame.Rect(0, 0, settings.width, settings.height)
		self.font = pygame.font.SysFont(None, 48)
		self.msg=msg

		# Build the button's rect object and center it.
		self.rect.center=self.screen_rect.center
		
		# The button message needs to be prepped only once.
		self.prep_msg(self.msg)

	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.settings.text_color,self.settings.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_rectangle(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.settings.bg_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def get_rect(self):
		return self.rect

