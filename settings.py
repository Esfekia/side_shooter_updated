import random

class Settings:
	"""A Class to store all settings for Alien Invasion."""

	def __init__ (self):
		"""Initialize the game's settings."""
		
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (6,18,33)

		#Background Scroll Settings:
		self.bgX = 0
		self.bgX2 = self.screen_width
		#self.bg_speed = 0.1

		#Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 15
		self.bullet_height =3
		self.bullet_color = (224,231,34)
		self.bullets_allowed = 3

		#Alien settings
		#  alien_frequency controls how often a new alien appear.s
		#    Higher values -> more frequent aliens. Max = 1.0.
		self.alien_frequency = 0.0016
		
		#Randomize ship speed.
		self.alien_speed = 1 * random.random()

		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""

		#Ship settings
		self.ship_speed = 1
		self.ship_limit = 3

		#Bullet settings
		self.bullet_speed = 1.5

		#Scoring
		self.alien_points = 50