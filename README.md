## 3D Raycasting Engine in Python

This is a simple 3D raycasting built with Pygame, inspired by Wolfenstein 3D. It Currently implements the Digital Differential Analyser (DDA) algorithm for ray-casting.

## Features (so far)
- DDA-based raycasting to detect walls. Wall coordinates are stored in a dictionary.
- Basic player movement using WASD and rotation using q and e.
- Textured Walls(to be added)
- Sprites(enemies, items)
- Minimap

# How to Run
1. Clone the repository
2. Install Python 3.x and Pygame: "pip install pygame"
3. Run 'python main.py' (or your relevant entry file)

## Controls
- W/A/S/D: To move forward/back and strafe left/right
- q/e: To rotate view left/right

##Next steps
- Draw rect for each ray to create walls
- Find fixes for visual issues like Fisheye
- Add Textures to walls. 
- Impove performance by Optimisatio
- Add static and animated sprites
- Add Minimao

# Change log 
- 