import pygame, math
from settings import *

class RayCast:
	def __init__(self, game):
		self.game = game
		self.raycasting_results = []
		self.textures = self.game.object_renderer.wall_textures
		self.objects_to_render = []

	def get_objects_to_render(self):
		self.objects_to_render = []
		for ray, values in enumerate(self.raycasting_results):
			depth, proj_height, texture, offset = values

			if proj_height < HEIGHT:
				wall_column = self.textures[texture].subsurface(
					(offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)
					)
				wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
				wall_pos = (ray*SCALE, HALF_HEIGHT - proj_height//2)
			else:
				texture_height = TEXTURE_SIZE * HEIGHT / proj_height
				wall_column = self.textures[texture].subsurface(
					offset*(TEXTURE_SIZE-SCALE), HALF_TEXTURE_SIZE - texture_height//2, SCALE, texture_height
					)
				wall_column = pygame.transform.scale(wall_column, (SCALE, HEIGHT))
				wall_pos = (ray*SCALE, 0)

			self.objects_to_render.append((depth, wall_column, wall_pos))


	def cast_rays(self):
		self.raycasting_results = []
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
					texture_hor = self.game.map.world_map[tile_hor]
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
					texture_vert = self.game.map.world_map[tile_vert]
					break
				vert_x += dx
				vert_y += dy
				depth_vert += vert_delta_depth

			#Chose the shortest depth.
			if depth_vert < depth_hor:
				depth, texture = depth_vert, texture_vert
				vert_y %= 1
				offset = vert_y if cos_a > 0 else (1 - vert_y)
			else:
				depth, texture = depth_hor, texture_hor
				hor_x %= 1
				offset = (1 - hor_x) if sin_a > 0 else hor_x

			# # Draw Rays for Debug
			# pygame.draw.line(self.game.screen, 'yellow', (px*TILE, py*TILE), (px*TILE+depth*cos_a*TILE, py*TILE+depth*sin_a*TILE), 2)

			#To Fix Fisheye
			depth *= math.cos(self.game.player.p_angle - start_angle)

			#Projection
			proj_height = SCREEN_DIST / (depth + 0.0001)

			# #Draw Walls
			# color = [256 / (1 + depth ** 5 * 0.00002)]*3
			# pygame.draw.rect(self.game.screen, color, (ray*SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

			#Add Ray_casting results
			self.raycasting_results.append((depth, proj_height, texture ,offset))

			start_angle += FOV / NUM_OF_RAYS

	def update(self):
		self.cast_rays()
		self.get_objects_to_render()

