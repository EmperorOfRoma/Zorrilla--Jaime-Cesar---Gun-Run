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

Player health
When this reaches 0, game ends and restarts.

Bullet mob
A mob that moves across the screen ignoring platforms and damaging the player

Respawn
In the case the player falls off the screen

'''

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        SCORE = 0
        TIME = SCORE/FPS
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game causes the below to reset or spawn in the manner described
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # self.enemies = pg.sprite.Group()
        self.player = Player(self)
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.all_sprites.add(self.plat1)
        # self.platforms.add(self.plat1)        
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # for i in range(0,10):
        #     m = Mob(20,20,(0,255,0))
        #     self.all_sprites.add(m)
        #     self.enemies.add(m)
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
        # Timer to provide a score to the player ****************
        # while TIME < 600:
        #     SCORE =+ 1
        #     print(SCORE)
        # start_ticks=pg.time.get_ticks()
        # while RUNNING:
        #     seconds=(pg.time.get_ticks()-start_ticks)/1000
        #     print(seconds)
        # print(pg.time.Clock()) **********************************
        if self.player.pos.y > HEIGHT:
            self.player.pos.y = HEIGHT/2
            self.player.pos.x = WIDTH/2

    # makes visuals appear on screen
    def draw(self):
        self.screen.fill(BLUE)
        self.draw_text("Hello there", 24, WHITE, WIDTH/2, HEIGHT/10)
        self.draw_text("Blocky.", 24, WHITE, WIDTH/2, HEIGHT/10+30)
        self.draw_text("I know you're stuck", 24, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("so survive as long as you can.", 24, WHITE, WIDTH/2, HEIGHT/2+30)
        self.draw_text("I will try to help.", 24, WHITE, WIDTH/2, HEIGHT/2+60)
        self.all_sprites.draw(self.screen)
        if HEALTH == 3:
            pass

        pg.display.flip()
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