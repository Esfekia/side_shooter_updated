import pygame
from pygame.sprite import Sprite

class Explosion (Sprite):
	"""A class to manage explosions in the game."""

	def __init__(self, ss_game):
		"""Create an explosion object at the ship's current position."""
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.screen_rect = ss_game.screen.get_rect()
		
		#Load the explosion image and get its rect.
		self.image = pygame.image.load("images/fire.png")
		self.rect = self.image.get_rect()
		self.rect.center = ss_game.ship.rect.midright

		#Store the explosion's position as a decimal value.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	#def blitme(self):
		"""Draw the explosion to the screen."""
	#	self.screen.blit(self.image, self.rect)

