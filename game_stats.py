class GameStats:
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, ss_game):
		"""Initialize statistics."""
		self.settings = ss_game.settings
		self.reset_stats()

		#Start Side Shooter in an active state.
		self.game_active = False
		
	def reset_stats(self):
		"""Initialize statistics that chan change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
