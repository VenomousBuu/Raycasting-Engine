# 3D Raycasting Engine in Python

This is a simple 3D raycasting built with Pygame, inspired by Wolfenstein 3D.

## Mathematical Background
This engine demonstrates the application of trigonometry and linear algebra in real-time rendering. By utilizing the DDA algorithm, we achieve $O(n)$ complexity for ray-grid intersections, where $n$ is the maximum search depth, ensuring high performance even on low-end hardware.

## HOW TO RUN
Pre_Requisites

- Python 3.x
- pygame library

		pip install pygame
Installation
	- Clone the Repository


		git clone https://github.com/VenomousBuu/Raycasting-Engine.git
cd Raycasting-Engine
	Running
	- Run Main.py
	
		python main.py
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

## Next steps
- Draw rect for each ray to create walls
- Find fixes for visual issues like Fisheye
- Add Textures to walls. 
- Impove performance by Optimisation
- Add static and animated sprites
- Add Minimap
- Add Weapons
- Add Closing and Opening doors

## Technical Challenges
- FishEye - Walls appeared curved. Fixed this by implementing cosine correction, by multiplying the raw depth by cosine of the relative angle at the edges of the FOV
- Frame Rate would significantly suffer when player got Too close to the Wall. I fixed it by defining a fixed height for walls once the projected height was bigger than the window height

## Assets & Credits
Code: Original implementation of the Raycasting engine logic.

Textures: Third-party placeholder assets sourced from open-source GitHub repositories. While the original creators are currently unattributed due to the age of the assets, they are used here for educational and portfolio demonstration purposes only.

If you are the creator of any of these textures, please reach out so I can provide proper attribution or replace them.
