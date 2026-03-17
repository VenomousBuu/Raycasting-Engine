import pygame
from settings import*

_ = False
path = 'Level1.txt'
with open(path, 'r') as file:
	#We Extract the created text file as a list with multiple lines
	mini_map = file.read().splitlines()

class Map:
	def __init__(self, game):
		self.game = game
		self.mini_map = mini_map
		self.world_map = {}
		self.create_map()

	def create_map(self):
		for j, row in enumerate(self.mini_map):
			for i, value in enumerate(row):
				if value != '_':
					self.world_map[(i, j)] = value

	def draw(self):
		for pos in self.world_map:
			pygame.draw.rect(self.game.screen,BLACK, (pos[0] * TILE, pos[1] * TILE, TILE-1, TILE-1))