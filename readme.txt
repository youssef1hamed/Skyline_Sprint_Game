PROJECT: Skyline Sprint

OVERVIEW
Runner game: jump over road barriers, avoid two patrolling rivals, and collect 12 energy orbs.

REQUIREMENTS
- Python 3
- Pygame Zero (pgzero)
- The project game code imports only math and random. Pygame itself is not imported.
- The assets are local image and sound files included in this project.

HOW TO RUN
1. Install Python 3 if it is not already installed.
2. Install Pygame Zero using your terminal:
   pip install pgzero
3. Open a terminal in this project folder.
4. Run:
   pgzrun game.py or python game.py

CONTROLS
- SPACE: jump
- Use the clickable menu buttons to start, toggle sound, or exit.
- Collect 12 energy orbs to win; hitting a barrier or rival causes a loss.

AUDIO AND VISUALS
- images/ contains cyclic idle and movement animation frames, plus the collectible coin image.
- sounds/ contains WAV sound effects.
- music/background.ogg contains the looping background music.

PROJECT NOTES
- Enemy movement is bounded by each enemy's assigned patrol area.
- Each character uses an object-oriented class for movement and animation.
- The source is intentionally compact for a beginner-friendly assessment project.
- Before submitting, test all menu buttons, collisions, sound toggling, win/loss screens, and restart behavior on the target machine.
