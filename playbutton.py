import pygame

class PlayButton:
	"""A class to manage the play button"""
	
	def __init__(self,ss_game):
		"""Initialize play button attributes."""

		self.screen = ss_game.screen
		self.screen_rect = self.screen.get_rect()

		#Load the play button image and get its rect.
		self.image = pygame.image.load('images/play.bmp')
		self.rect = self.image.get_rect()

		#Position the play button in the center of the screen.
		self.rect.center =self.screen_rect.center

		#Store a decimal value for the play button's positions:
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""Draw the play button at its current location."""
		self.screen.blit(self.image, self.rect)