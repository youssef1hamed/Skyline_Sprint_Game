"""
Skyline Sprint — a Pygame Zero runner.
Run with: pgzrun game.py
"""
import math
import random
from pygame import Rect
import pgzrun

WIDTH = 900
HEIGHT = 560
TITLE = "Skyline Sprint"
GROUND_Y = 455
GOAL_SCORE = 12

state = "menu"
sound_on = True
score = 0
distance = 0
speed = 4.0
frame_timer = 0
obstacles = []
coins = []
enemies = []
player = None
game_over_reason = ""

class AnimatedCharacter:
    """Owns a sprite actor and cycles idle/movement frames."""
    def __init__(self, x, y, prefix, speed=0):
        self.actor = Actor(prefix + "_idle_0", (x, y))
        self.prefix = prefix
        self.speed = speed
        self.frame = 0
        self.timer = 0
        self.idle = True
        self.alive = True

    def animate(self, dt):
        self.timer += dt
        max_frames = 2 if self.idle else 4
        # Clamp frame if switching between idle and move to prevent out-of-range keys
        if self.frame >= max_frames:
            self.frame = 0
        if self.timer >= 0.12:
            self.timer = 0
            self.frame = (self.frame + 1) % max_frames
        mode = "idle" if self.idle else "move"
        self.actor.image = self.prefix + "_" + mode + "_" + str(self.frame)

    def draw(self):
        self.actor.draw()

class RunnerPlayer(AnimatedCharacter):
    def __init__(self):
        super().__init__(145, GROUND_Y - 25, "hero")
        self.y_ground = GROUND_Y - 25
        self.jump_velocity = 0
        self.sliding = False
        self.invulnerable = 0

    def update(self, dt):
        if keyboard.space and self.actor.y >= self.y_ground:
            self.jump_velocity = -570
            if sound_on:
                sounds.jump.play()
        self.jump_velocity += 1350 * dt
        self.actor.y += self.jump_velocity * dt
        if self.actor.y > self.y_ground:
            self.actor.y = self.y_ground
            self.jump_velocity = 0
        self.idle = abs(self.jump_velocity) < 1
        self.invulnerable = max(0, self.invulnerable - dt)
        self.animate(dt)

class PatrolHazard(AnimatedCharacter):
    """A dangerous enemy that charges and chases the runner."""
    def __init__(self, x, y, prefix, speed):
        super().__init__(x, y, prefix, speed)
        self.passed = False

    def update(self, dt):
        # Charge directly left toward the player
        self.actor.x -= self.speed * dt
        self.idle = False
        self.animate(dt)

def draw_button(rect, label):
    screen.draw.filled_rect(rect, (36, 54, 83))
    screen.draw.rect(rect, (125, 210, 255))
    screen.draw.text(label, center=rect.center, fontsize=27, color="white")

def start_game():
    global state, score, distance, speed, player, obstacles, coins, enemies, game_over_reason
    state = "playing"
    score = 0
    distance = 0
    speed = 4.0
    game_over_reason = ""
    player = RunnerPlayer()
    obstacles = []
    coins = []
    
    # Spawn a challenging charging rival
    enemies = [
        PatrolHazard(750, GROUND_Y - 25, "enemy_a", 220),
    ]
    
    if sound_on:
        music.play("subway-sound")
        music.set_volume(0.25)

def end_game(won, reason):
    global state, game_over_reason
    state = "won" if won else "lost"
    game_over_reason = reason
    music.stop()
    if sound_on:
        music.play("crowd-applause" if won else "sad-game-over")
        music.set_volume(0.3)

def update(dt):
    global frame_timer, distance, speed, score, obstacles, coins
    if state != "playing":
        return
    frame_timer += dt
    distance += speed * dt
    speed = min(7.0, 4.0 + distance / 450)
    player.update(dt)
    
    for enemy in enemies:
        enemy.update(dt)
        
        # Check if the player successfully jumped OVER the enemy
        if not enemy.passed and enemy.actor.x < player.actor.x:
            if player.actor.y < GROUND_Y - 40:  # Player is in the air!
                enemy.passed = True
                score += 1  # Bonus score for a clean dodge!
                if sound_on:
                    sounds.coin.play()
                # Reset enemy ahead with increased speed & difficulty!
                enemy.actor.x = WIDTH + random.randint(50, 200)
                enemy.speed += 45  # Gets faster every time you dodge him!
                enemy.passed = False

        # If enemy reaches the left side without being jumped over, reset them
        if enemy.actor.x < -30:
            enemy.actor.x = WIDTH + 100
            enemy.passed = False

    if frame_timer > 1.0:
        frame_timer = 0
        if random.random() < 0.78:
            obstacles.append(Rect((WIDTH + 20, GROUND_Y - 38, 28, 38)))
        if random.random() < 0.75:
            coins.append(Actor("coin", (WIDTH + 20, random.choice([GROUND_Y-95, GROUND_Y-150, GROUND_Y-210]))))
    for item in obstacles:
        item.x -= speed * 60 * dt
    for item in coins:
        item.x -= speed * 60 * dt
    obstacles = [item for item in obstacles if item.right > 0]
    coins = [item for item in coins if item.x > -30]
    for item in coins[:]:
        if player.actor.colliderect(item):
            coins.remove(item)
            score += 1
            if sound_on:
                sounds.coin.play()
    for enemy in enemies:
        # Collision: If you hit him while on the ground, game over!
        if player.actor.colliderect(enemy.actor) and player.actor.y >= GROUND_Y - 40 and player.invulnerable <= 0:
            end_game(False, "The rival caught you on the ground!")
            return
    for obstacle in obstacles:
        if player.actor.colliderect(obstacle) and player.actor.y > GROUND_Y - 70:
            end_game(False, "You hit a road barrier!")
            return
    if score >= GOAL_SCORE:
        end_game(True, "You survived and collected enough orbs!")

def draw():
    screen.fill((18, 28, 52))
    # layered skyline
    for i in range(12):
        x = i * 85 - int(distance * 13) % 85
        height = 80 + (i * 37 % 120)
        screen.draw.filled_rect(Rect((x, GROUND_Y-height, 55, height)), (28, 45, 75))
        for wy in range(GROUND_Y-height+12, GROUND_Y-8, 20):
            screen.draw.filled_rect(Rect((x+10,wy,6,7)), (95,150,190))
    screen.draw.filled_rect(Rect((0, GROUND_Y, WIDTH, HEIGHT-GROUND_Y)), (48, 60, 68))
    screen.draw.line((0, GROUND_Y), (WIDTH, GROUND_Y), (220, 220, 180))
    for x in range(-20, WIDTH, 70):
        screen.draw.filled_rect(Rect((x-int(distance*60)%70, GROUND_Y+65, 35, 5)), (210,210,190))
    if state == "menu":
        screen.draw.text("SKYLINE SPRINT", center=(WIDTH/2, 120), fontsize=56, color="white")
        screen.draw.text("Jump over the road barriers, watch out the Patrol, and collect orbs to win!", center=(WIDTH/2, 180), fontsize=23, color=(190,220,255))
        draw_button(Rect((330,240,240,55)), "Start Game")
        draw_button(Rect((330,310,240,55)), "Sound: " + ("ON" if sound_on else "OFF"))
        draw_button(Rect((330,380,240,55)), "Exit")
        return
    for obstacle in obstacles:
        screen.draw.filled_rect(obstacle, (240, 100, 65))
        screen.draw.line((obstacle.x, obstacle.y), (obstacle.right, obstacle.y), (255,220,180))
    for item in coins:
        screen.draw.filled_circle((item.x,item.y), 12, (255,215,50))
        screen.draw.circle((item.x,item.y), 12, (255,245,170))
    if player:
        player.draw()
    for enemy in enemies:
        enemy.draw()
    screen.draw.text("Score: " + str(score) + "/" + str(GOAL_SCORE), (20,20), fontsize=30, color="white")
    screen.draw.text("SPACE = jump", (20,55), fontsize=20, color=(210,220,240))
    if state in ("won", "lost"):
        screen.draw.filled_rect(Rect((170,175,560,190)), (20,30,50))
        screen.draw.rect(Rect((170,175,560,190)), "white")
        screen.draw.text("YOU WIN!" if state == "won" else "GAME OVER", center=(WIDTH/2,215), fontsize=42, color="yellow" if state == "won" else "red")
        screen.draw.text(game_over_reason, center=(WIDTH/2,265), fontsize=22, color="white")
        draw_button(Rect((245,300,190,45)), "Play Again")
        draw_button(Rect((465,300,190,45)), "Main Menu")

def on_mouse_down(pos):
    global sound_on, state
    if state == "menu":
        if Rect((330,240,240,55)).collidepoint(pos):
            start_game()
        elif Rect((330,310,240,55)).collidepoint(pos):
            sound_on = not sound_on
            if not sound_on:
                music.stop()
        elif Rect((330,380,240,55)).collidepoint(pos):
            music.stop()
            raise SystemExit
    elif state in ("won","lost"):
        if Rect((245,300,190,45)).collidepoint(pos):
            start_game()
        elif Rect((465,300,190,45)).collidepoint(pos):
            music.stop()
            state = "menu"

pgzrun.go()
