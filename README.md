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
	<img width="1344" height="767" alt="Screenshot 2026-03-18 121544" src="https://github.com/user-attachments/assets/fb2b8513-8995-44c5-b424-3b30b7f77f08" />
- Basic player movement using WASD and rotation using q and e.
- Added Textured Walls
   	<img width="1365" height="767" alt="Screenshot 2026-03-18 121624" src="https://github.com/user-attachments/assets/45b92a09-1cc6-4471-a5ff-cfc822e190f2" />
  	<img width="1365" height="767" alt="Screenshot 2026-03-18 122354" src="https://github.com/user-attachments/assets/d244ebc0-0238-4664-873f-82d0a4666dc9" /> 
- Sprites(enemies, items)
- Minimap

## Controls
- W/A/S/D: To move forward/back and strafe left/right
- q/e: To rotate view left/right

## Next steps 
- Impove performance by Optimisation
- Add static and animated sprites
- Add Minimap
- Add Weapons
- Add Closing and Opening doors

## Technical Challenges
- FishEye - Walls appeared curved. Fixed this by implementing cosine correction, by multiplying the raw depth by cosine of the relative angle at the edges of the FOV
  <img width="1365" height="767" alt="Screenshot 2026-03-18 123204" src="https://github.com/user-attachments/assets/beb5e131-89a3-443b-beb9-496d2b1b04c6" />
<img width="1365" height="767" alt="Screenshot 2026-03-18 123222" src="https://github.com/user-attachments/assets/0f76a7f3-606d-49dd-8318-cb7451fde353" />

- Frame Rate would significantly suffer when player got Too close to the Wall. I fixed it by defining a fixed height for walls once the projected height was bigger than the window height

## Assets & Credits
Code: Original implementation of the Raycasting engine logic.

Textures: Third-party placeholder assets sourced from open-source GitHub repositories. While the original creators are currently unattributed due to the age of the assets, they are used here for educational and portfolio demonstration purposes only.

If you are the creator of any of these textures, please reach out so I can provide proper attribution or replace them.
