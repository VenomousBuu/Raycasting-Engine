import pygame, math
from settings import *

class Player:
	def __init__(self, game):
		self.game = game
		self.px, self.py = PLAYER_POS
		self.p_angle = PLAYER_ANGLE

	def movement(self):
		#Make Player Face Forward, left, right, back based on Direction Faced
		cos_a = math.cos(self.p_angle)
		sin_a = math.sin(self.p_angle)
		speed = PLAYER_SPEED * self.game.delta_time
		dx, dy = 0, 0
		mov_cos = cos_a * speed
		mov_sin = sin_a * speed

		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			dx += mov_cos
			dy += mov_sin
		if keys[pygame.K_s]:
			dx -= mov_cos
			dy -= mov_sin

		slower_mov_sin = mov_sin*0.6
		slower_mov_cos = mov_cos*0.6
		if keys[pygame.K_d]:
			dx += -slower_mov_sin
			dy += slower_mov_cos
		if keys[pygame.K_a]:
			dx += slower_mov_sin
			dy += -slower_mov_cos

		if keys[pygame.K_e]:
			self.p_angle += PLAYER_ROT_ANGLE * self.game.delta_time
		if keys[pygame.K_q]:
			self.p_angle -= PLAYER_ROT_ANGLE * self.game.delta_time
		self.p_angle %= math.tau

		# #Add Movement
		# self.px += dx
		# self.py += dy

		#Check Collision with Walls
		self.check_wall_collisions(dx, dy)

	def check_wall_collisions(self, dx, dy):
		if self.check_player_location(int(self.px + dx), int(self.py)):
			self.px += dx
		if self.check_player_location(int(self.px), int(self.py + dy)):
			self.py += dy  

	def check_player_location(self, x, y):
		return (x, y) not in self.game.map.world_map

	def update(self):
		self.movement()

	def draw(self):
		pygame.draw.line(self.game.screen, 'yellow', (self.px*TILE, self.py*TILE), (self.px*TILE+WIDTH * math.cos(self.p_angle), self.py*TILE+HEIGHT * math.sin(self.p_angle)), 1)
		pygame.draw.circle(self.game.screen, 'red', (self.px*TILE, self.py*TILE), 5)


	@property
	def pos(self):
		return self.px, self.py

	@property
	def world_pos(self):
		return int(self.px), int(self.py)
