import math

RES = WIDTH, HEIGHT = 1280, 728
TILE = 50

#Colors
BLACK = (0, 0, 0)
GREY = (30, 30, 30)

#Player/Movable Character settings
PLAYER_POS = 1.4, 1.8 #On mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_ANGLE = 0.0028

#FPS
FPS = 60

#Ray Cast settings
NUM_OF_RAYS = WIDTH // 2
FOV = math.pi / 3 #60 degrees
HALF_FOV = FOV / 2
MAX_DEPTH = 20
DELTA_ANGLE =FOV / NUM_OF_RAYS


