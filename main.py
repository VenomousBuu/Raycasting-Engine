import pygame, sys
from settings import*
from map import *
from player import *
from ray_casting import *

class Main:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(RES)
		pygame.display.set_caption("3D Rayscasting Engine")

		self.delta_time = 1
		self.clock = pygame.time.Clock()

		self.map = Map(self)
		self.player = Player(self)
		self.raycasting = RayCast(self)

	def run(self):
		while True:
			self.events()
			self.update()
			self.draw()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()

	def draw(self):
		self.screen.fill(GREY)
		# self.map.draw()
		# self.player.draw()

	def update(self):
		self.player.update()
		self.raycasting.update()
		pygame.display.flip()
		self.delta_time = self.clock.tick(FPS)


if __name__ == "__main__":
	game = Main()
	game.run()