# 🏃‍♂️ Skyline Sprint! 🏙️

Welcome to **Skyline Sprint**, an exciting endless-runner arcade game built using Python and Pygame Zero!

Dash through the city skyline, leap over road barriers, dodge speedy rivals, and collect glowing energy orbs to win! 🌟

## 🎮 What's the Game About?

In **Skyline Sprint**, you control a heroic runner sprinting across the city. Your mission is simple but thrilling:

* 🪙 **Collect 12 Energy Orbs** scattered in the air to power up and win!

* 🚧 **Jump Over Road Barriers** to keep your run going.

* 🏃‍♂️💨 **Outsmart the Charging Rival!** Jump over the rival to dodge him. But watch out—every time you dodge him, he speeds up and comes charging back!

## 🚀 How to Get Started

### 1. Requirements 📋

Make sure you have installed on your computer:

* **Python 3** (Download from [python.org](https://www.python.org/))

* **Pygame Zero** (`pgzero`)

### 2. Installation 💻

Open your Command Prompt or Terminal and install Pygame Zero by running:

```
pip install pgzero

```

### 3. How to Play! 🎮

1. Open your terminal in this game's folder.

2. Type the following command and press **Enter**:

```
pgzrun game.py

```

*(Or run `python game.py` if your environment uses the Python launcher!)*

## 🕹️ Game Controls

| Action | Control | 
| ----- | ----- | 
| **Jump** | Press `SPACEBAR` ⌨️ | 
| **Navigate Menus** | Click buttons with your **Mouse** 🖱️ | 
| **Toggle Audio** | Click the **Sound: ON / OFF** button on the main menu 🔊 | 

## 🎨 Music, Sounds & Visuals

Everything you see and hear in Skyline Sprint comes right from the local assets folder:

* 🖼️ **`images/`**: Contains all character animation frames (running & idle cycles) and collectible orb sprites.

* 🔊 **`sounds/`**: Packed with fun action sound effects for jumping, picking up orbs, and taking hits!

* 🎵 **`music/`**: Features upbeat tracks like `subway-sound.mp3` for high-energy running, plus celebratory win tracks (`crowd-applause.mp3`) and game-over music (`sad-game-over.mp3`).

## 🛠️ Code Features (For Young Programmers!)

This game was crafted to be clean, beginner-friendly, and lightweight:

* 🧱 **Object-Oriented Design**: Characters and hazards use custom classes (`RunnerPlayer` and `PatrolHazard`) to handle movement, gravity, and animations smoothly.

* ⚡ **Standard Libraries Only**: The game logic imports only Python's standard `math` and `random` modules, keeping the code clean and fast.

* 🔁 **Dynamic Difficulty**: Features smart collision detection and increasing speed mechanics that test your reaction time!

