import shelve
class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset()
		shelFile=shelve.open('highscore')
		self.highscore=int(shelFile['score'])
		shelFile.close()
		# with open("highscore.txt") as file_obj:
		# 	self.highscore=file_obj.read()
		# self.highscore=int(self.highscore)	
	def reset(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.game_active=False
		self.score=0
		self.level=1