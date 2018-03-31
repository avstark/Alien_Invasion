"""settings class for the game"""

class Settings():
	def __init__(self):
		"""initializing settings"""
		#screen settings
		self.dimentions=(1000,800) 	#(width,height)
		self.bg_color=(230,230,230)		#(R,B,G)
	
		# ship settings
		self.ship_speed_factor=1.1
		self.ship_limit = 3

		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15	
		self.bullet_color = 60, 60, 60
		self.bullet_speed_factor=1.1
		self.limit_bullets=4

		# Alien settings
		self.alien_speed_factor=1.2
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#scoreing settings
		self.score_speed_factor=1.5

		self.reset()

		#play settings
		self.width,self.height,self.button_color,self.text_color=200,50,(0,255,0),(255,255,255)
		
	
	def reset(self):
		self.ship_speed=1.2
		self.bullet_speed=1.2
		self.alien_speed=.8
		self.score_speed=10
		
	def update_settings(self):
		self.ship_speed*=self.ship_speed_factor
		self.bullet_speed*=self.bullet_speed_factor
		self.alien_speed*=self.alien_speed_factor
		self.score_speed*=self.score_speed_factor
		


