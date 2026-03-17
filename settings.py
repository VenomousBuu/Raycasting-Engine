import math

RES = WIDTH, HEIGHT = 1280, 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 80

#Colors
BLACK = (0, 0, 0)
GREY = (30, 30, 30)

#Player/Movable Character settings
PLAYER_POS = 1.5, 2 #On mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.003
PLAYER_ROT_ANGLE = 0.0015

#FPS
FPS = 60

#Ray Cast settings
NUM_OF_RAYS = WIDTH // 2
FOV = math.pi / 3 #60 degrees
HALF_FOV = FOV / 2
MAX_DEPTH = 30

#3D rendering settings
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_OF_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2


