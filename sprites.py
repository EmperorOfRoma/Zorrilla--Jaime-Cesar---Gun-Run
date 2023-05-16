import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint


vec = pg.math.Vector2

# player class
class Player(Sprite): 
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties of the player class
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.health = 3
        # self.score = 0
        # self.time = self.score/FPS
        self.last_update = pg.time.get_ticks()
        self.canjump = False
    # These are the actions taken by the Player Character (PC) when certain inputs are given by the player
    def input(self):
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    # the system applies these once every 30 secs, updating the game as the concurrent condtions require
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.pos.y < 0:
            self.pos

# mob class
class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        # properties of the class
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(3,7),randint(3,7))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # keeps mobs on the screen
    def inbounds(self):
        if self.rect.x > WIDTH-self.width:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT-self.height:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    # the system applies these once every 30 secs, updating the game as the concurrent condtions require
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

# platform class
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        # properties of the class
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant