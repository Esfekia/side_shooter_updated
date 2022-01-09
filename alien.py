import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ss_game):
		"""Initialize the alien and set its starting position."""
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings

		#Load the alien image and set its rect attribute.
		self.image =pygame.image.load('images/alien.png')
		self.image =pygame.transform.scale(self.image, (100, 66))
		self.rect = self.image.get_rect()

		#Start each new alien on top right of the screen.
		self.rect.left = self.screen.get_rect().right
		#The farthest down the screen we'll place the alien is the height
		# of the screen, minus the height of the alien.
		alien_top_max = self.settings.screen_height - self.rect.height
		self.rect.top = randint(0, alien_top_max)

		#Store the alien's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move the alien steadily to the left."""
		self.x -= self.settings.alien_speed
		self.rect.x = self.x
