# File created by: Jaime Cesar Zorrilla
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# Sources: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

'''
My goal is:

Player health - Check
When this reaches 0, game ends and restarts.

Bullet mob
A mob that moves across the screen ignoring platforms and damaging the player

Respawn - check
In the case the player falls off the screen

Clock - check
Visible timer that will serve as a score

Randsom platforms
Each game start will pull from a pool of platforms in combinations that are all playable

'''

# import libs
from time import sleep
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from math import floor
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
# # Turns a visual saved in my folder into a variable to be used in the code
# heart_image = pg.image.load(os.path.join(img_folder, "pixel-heart.jpg")).convert()
# heart_image_rect = heart_image.get_rect()

class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
        # print(self.delta)
    def reset(self):
        self.event_time = floor((pg.time.get_ticks())/1000)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        # Turns a visual saved in my folder into a variable to be used in the code
        global heart_image1
        global heart_image1_rect
        global heart_image2
        global heart_image2_rect
        global heart_image3
        global heart_image3_rect
        heart_image1 = pg.image.load(os.path.join(img_folder, "pixel-heart.png")).convert()
        heart_image1_rect = heart_image1.get_rect()
        heart_image2 = pg.image.load(os.path.join(img_folder, "pixel-heart.png")).convert()
        heart_image2_rect = heart_image1.get_rect()
        heart_image3 = pg.image.load(os.path.join(img_folder, "pixel-heart.png")).convert()
        heart_image3_rect = heart_image1.get_rect()
        SCORE = 0
        TIME = SCORE/FPS
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game causes the below to reset or spawn in the manner described
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.cd = Cooldown()
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.all_sprites.add(self.plat1)
        # self.platforms.add(self.plat1)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,8):
            m = Mob(20,20,RED)
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    # Make the game play
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # Responses to different player inputs
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    # the system applies these once every 30 secs, updating the game as the concurrent condtions require
    def update(self):
        self.all_sprites.update()
        # Timer to provide a score to the player
        self.cd.ticking()
        # Enemies injure the player
        injure = pg.sprite.spritecollide(self.player, self.enemies, False)
        if self.cd.delta > 2:
            if injure:
                injure[0].kill()
                self.player.health -= 1
        # Causes platforms to work
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
        if self.player.pos.y > HEIGHT:
            self.player.pos.y = HEIGHT/2
            self.player.pos.x = WIDTH/2
            self.player.health -= 1

    # makes visuals appear on screen
    def draw(self):
        self.screen.fill(BLUE)
        self.draw_text(str(self.cd.delta), 24, WHITE, WIDTH - 50, 0)
        if self.cd.delta < 20:
            self.draw_text("Hello there", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("Blocky.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
            self.draw_text("I know you're stuck", 24, WHITE, WIDTH/2, HEIGHT/2)
            self.draw_text("so survive as long as you can.", 24, WHITE, WIDTH/2, HEIGHT/2+30)
            self.draw_text("I will try to help.", 24, WHITE, WIDTH/2, HEIGHT/2+60)
        if self.cd.delta > 19 and self.cd.delta < 25:
            self.draw_text("Give me 10 minutes.", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 24 and self.cd.delta < 40:
            self.draw_text("Don't forget:", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("It's hard to change directions", 24, WHITE, WIDTH/2, HEIGHT/10+30)
            self.draw_text("while moving.", 24, WHITE, WIDTH/2, HEIGHT/10+60)
            self.draw_text("Stop moving, then turn.", 24, WHITE, WIDTH/2, HEIGHT/2)
        if self.cd.delta > 59 and self.cd.delta < 70:
            self.draw_text("You know, you've been off the", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("radar for a while.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 69 and self.cd.delta < 75:
            self.draw_text("You're a hard person to find.", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 74 and self.cd.delta < 80:
            self.draw_text("Do you remember anything?", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 79 and self.cd.delta < 85:
            self.draw_text("No?", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 89 and self.cd.delta < 95:
            self.draw_text("Where to begin...?", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 109 and self.cd.delta < 130:
            self.draw_text("Sir Cular and his regiments", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("have laid siege to the world.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
            self.draw_text("Sir Cumference is leading his armies.", 24, WHITE, WIDTH/2, HEIGHT/10+60)
            self.draw_text("We have tried to fight back", 24, WHITE, WIDTH/2, HEIGHT/2)
            self.draw_text("but our soldiers are square.", 24, WHITE, WIDTH/2, HEIGHT/2+30)
            self.draw_text("Our Triangular allies are too edgy to help.", 24, WHITE, WIDTH/2, HEIGHT/2+60)
        if self.cd.delta > 129 and self.cd.delta < 140:
            self.draw_text("You were our only hope,", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("then you dissappeared.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 139 and self.cd.delta < 150:
            self.draw_text("Now I've found you in a", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("gun-geon of sorts.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 149 and self.cd.delta < 155:
            self.draw_text("Don't worry, friend.", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 154 and self.cd.delta < 160:
            self.draw_text("I'll get you out.", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 299 and self.cd.delta < 310:
            self.draw_text("ETA: 5 mins.", 24, WHITE, WIDTH/2, HEIGHT/10)
        if self.cd.delta > 539 and self.cd.delta < 550:
            self.draw_text("One more minute.", 24, WHITE, WIDTH/2, HEIGHT/10)
            self.draw_text("Just hold on.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 579 and self.cd.delta < 590:
            self.draw_text("HAHA! I made it!.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 589 and self.cd.delta < 600:
            self.draw_text("Hop on!", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        if self.cd.delta > 599:
            self.screen.fill(BLUE)
            self.draw_text("YOU", 100, GREEN, WIDTH/2, HEIGHT/2)
            pg.display.flip()
            sleep(2)
            self.screen.fill(BLUE)
            self.draw_text("YOU", 150, GREEN, WIDTH/2, HEIGHT/2-80)
            self.draw_text("SURVIVED", 150, GREEN, WIDTH/2, HEIGHT/2+70)
            pg.display.flip()
            sleep(5)
            pg.quit()
        self.all_sprites.draw(self.screen)
        # These provide visual feedback on player's health
        if self.player.health == 3:
            heart_image1_rect.y = -5
            heart_image2_rect.y = -5
            heart_image3_rect.y = -5
            heart_image2_rect.x = heart_image1_rect.width
            heart_image3_rect.x = heart_image1_rect.width*2
            self.screen.blit(heart_image1, heart_image1_rect)
            self.screen.blit(heart_image2, heart_image2_rect)
            self.screen.blit(heart_image3, heart_image3_rect)
        if self.player.health == 2:
            heart_image1_rect.y = -5
            heart_image2_rect.y = -5
            heart_image2_rect.x = heart_image1_rect.width
            self.screen.blit(heart_image1, heart_image1_rect)
            self.screen.blit(heart_image2, heart_image2_rect)
        if self.player.health == 1:
            heart_image1_rect.y = -5
            self.screen.blit(heart_image1, heart_image1_rect)
        pg.display.flip()
        if self.player.health < 1:
            self.screen.fill(BLUE)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 0)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 100)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 200)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 300)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 400)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 500)
            self.draw_text("YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD YOU ARE DEAD", 100, RED, -10, 600)
            pg.display.flip()
            sleep(5)
            self.screen.fill(BLUE)
            self.draw_text("You Survived " + str(self.cd.delta) + " seconds.", 70, RED, WIDTH/2, HEIGHT/2)
            pg.display.flip()
            sleep(5)
            pg.quit()

    # allows text to appear on screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    # this way, the game knows what the player has clicked on
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()