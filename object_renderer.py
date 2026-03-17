import pygame
from settings import *

class Object_Renderer:
	def __init__(self, game):
		self.game = game
		self.wall_textures = self.load_textures()

	def render_images(self):
		list_objects = self.game.raycasting.objects_to_render
		for depth, image, pos in list_objects:
			self.game.screen.blit(image, pos)

	def draw(self):
		self.render_images()


	@staticmethod
	def get_textures(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
		texture = pygame.image.load(path).convert_alpha()
		return pygame.transform.scale(texture, res)

	def load_textures(self):
		return {
		1:self.get_textures("resources/textures/1.png"),
		2:self.get_textures("resources/textures/2.png"),
		3:self.get_textures("resources/textures/3.png"),
		4:self.get_textures("resources/textures/4.png"),
		5:self.get_textures("resources/textures/5.png")
		}


