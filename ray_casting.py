import pygame, math
from settings import *

class RayCast:
	def __init__(self, game):
		self.game = game

	def cast_rays(self):
		px, py = self.game.player.pos
		world_x, world_y = self.game.player.world_pos

		start_angle = self.game.player.p_angle - HALF_FOV + 0.0001 #To avoid zero error
		for ray in range(NUM_OF_RAYS):
			
			cos_a = math.cos(start_angle)
			sin_a = math.sin(start_angle)

			#Finding Depth to Wall/textures using Tiles
			#For Horizontals:
			hor_y = (world_y + 1) if sin_a > 0 else (world_y - 1e-6) #(hor_x, hor_y) are tile coordinates
			dy = 1 if sin_a > 0 else -1 #dy being the vertical distance to next tile

			depth_hor = (hor_y - py) / sin_a
			hor_x = (cos_a*depth_hor) + px

			hor_delta_depth = dy / sin_a
			dx = cos_a * hor_delta_depth

			for i in range(MAX_DEPTH):
				tile_hor = int(hor_x), int(hor_y)
				if tile_hor in self.game.map.world_map:
					break
				hor_x += dx #To check next tile
				hor_y += dy
				depth_hor += hor_delta_depth

			#For Verticals
			vert_x = (world_x + 1) if cos_a > 0 else (world_x - 1e-6)
			dx = 1 if cos_a > 0 else -1

			depth_vert = (vert_x - px) / cos_a
			vert_y = (depth_vert * sin_a) + py

			vert_delta_depth = dx / cos_a
			dy = vert_delta_depth * sin_a

			for i in range(MAX_DEPTH):
				tile_vert = int(vert_x), int(vert_y)
				if tile_vert in self.game.map.world_map:
					break
				vert_x += dx
				vert_y += dy
				depth_vert += vert_delta_depth

			#Chose the shortest depth.
			if depth_vert < depth_hor:
				depth = depth_vert
			else:
				depth = depth_hor
			# Draw Rays for Debug
			pygame.draw.line(self.game.screen, 'yellow', (px*TILE, py*TILE), (px*TILE+depth*cos_a*TILE, py*TILE+depth*sin_a*TILE), 2)


			start_angle += FOV / NUM_OF_RAYS

	def update(self):
		self.cast_rays() 