import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from playbutton import PlayButton
from game_stats import GameStats
from scoreboard import Scoreboard

from pygame.locals import *
from time import sleep
from random import random

class SideShooter:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()

		self.bg = pygame.image.load("images/space.bmp")
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption ("Sideways Shooter!")

		#Create an instance to store game statistics.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.ship = Ship(self)
		self.playbutton = PlayButton(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			
			#Loop the background.
			self._loop_bg()

			#Watch for keyboard and mouse events.
			self._check_events()

			#Check if the game is still active first!
			if self.stats.game_active:

				#Consider creating a new alien.
				self._create_alien()
			
				#Update ship's position.
				self.ship.update()

				#Update bullets.
				self._update_bullets()

				#Update aliens group
				self.aliens.update()

				#Look for alien-ship collisions.
				if pygame.sprite.spritecollideany(self.ship,self.aliens):
					self._ship_hit()
			
			#Redraw the screen during each pass through the loop.
			self._update_screen()

	def _loop_bg(self):
		"""Create a scrolling background event"""
		self.settings.bgX -= 0.1  # Move both background images back
		self.settings.bgX2 -= 0.1

		if self.settings.bgX < self.settings.screen_width * -1:  # If our bg is at the -width then reset its position
			self.settings.bgX = self.settings.screen_width
		if self.settings.bgX2 < self.settings.screen_width * -1:
			self.settings.bgX2 = self.settings.screen_width

	def _check_events(self):
		"""Respond to key presses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self,mouse_pos):
		"""Start a new game when the player clicks Play"""
		button_clicked = self.playbutton.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.start_game()

	def start_game(self):
		#Reset the game statistics and set active flag
		self.stats.reset_stats()
		self.stats.game_active =True

		#Hide the mouse cursor
		pygame.mouse.set_visible(False)

	def _check_keydown_events(self,event):
		"""Respond to key presses."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_p and not self.stats.game_active:	
			self.start_game()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
	
	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		#As long as the number of bullets is less than allowed:
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		self.bullets.update()

		#Get rid of the bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right>= self.settings.screen_width:
				self.bullets.remove(bullet)

		#Check for collisions.
		self._check_bullet_alien_collisions()

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""

		if self.stats.ships_left > 0 :
			#Decrement ships_eft.
			self.stats.ships_left -= 1

			#Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			#Create a new alien and center the ship.
			self._create_alien()
			self.ship.center_ship()

			#Pause.
			sleep(2)

		else:
			self.stats.game_active = False

	def _check_bullet_alien_collisions(self):
		"""Check whether any bullets have hit an alien."""
		collisions =pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

	def _create_alien(self):
		"""Create an alien, if conditions are right."""
		if random() < self.settings.alien_frequency:
			alien = Alien(self)
			self.aliens.add(alien)
			###print(len(self.aliens)) <= no longer needed.

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		
		#Add background picture
		self.screen.blit(self.bg, (self.settings.bgX, 0))  # draws our first bg image
		self.screen.blit(self.bg, (self.settings.bgX2, 0))  # draws the seconf bg image
		
		#Add ship picture
		self.ship.blitme()

		#Draw the bullets
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		#Draw the aliens
		self.aliens.draw(self.screen)
		
		#Draw the scoreinformation
		self.sb.show_score()

		#Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.playbutton.blitme()
		
		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance, and run the game.
	ss = SideShooter()
	ss.run_game()

