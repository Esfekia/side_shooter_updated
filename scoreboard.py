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
		self.prep_high_score()

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

	def prep_high_score(self):
		"""Turn the high score into a rendered image at top center."""
		high_score = round (self.stats.high_score, -1)
		high_score_str = "{:}".format(high_score)
		self.high_score_image = self.font.render (f"High Score: " +high_score_str,True,
			self.text_color)

		#Position the high score below the score.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.score_rect.right
		self.high_score_rect.top = self.score_rect.bottom +10

	def check_high_score(self):
		"""Check to see if there is a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)

