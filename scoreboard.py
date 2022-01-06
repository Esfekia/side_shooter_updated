import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self,ss_game):
		"""Initialize scorekeeping attributes."""
		self.ss_game = ss_game
		self.screen = ss_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ss_game.settings
		self.stats = ss_game.stats

		#Font settings for scoring information.
		self.text_color = (215,183,64)
		self.font = pygame.font.SysFont(None,24)

		#Prepare the initial score image.
		self.prep_score()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		score_str = str(self.stats.score)
		rounded_score =round (self.stats.score, -1)
		score_str ="{:,}".format(rounded_score)
		self.score_image = self.font.render (f"Score: " +score_str,True,
			self.text_color)

		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)

