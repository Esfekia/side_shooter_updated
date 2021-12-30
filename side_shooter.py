import sys
import pygame
from settings import Settings
from ship import Ship

class SideShooter:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game and create game resources."""

		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption ("Sideways Shooter!")

		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#Watch for keyboard and mouse events.
			self._check_events()

			#Update ship's position.
			self.ship.update()

			#Redraw the screen during each pass through the loop.
			self._update_screen()

	def _check_events(self):
		"""Respond to key presses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self,event):
		"""Respond to key presses."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self,event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
	
	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance, and run the game.
	ss = SideShooter()
	ss.run_game()

