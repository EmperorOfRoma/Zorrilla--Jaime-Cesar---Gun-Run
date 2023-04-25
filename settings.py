# File created by: Jaime Cesar Zorrilla

# # import libs
# import pygame as pg
# import os
# # Allows for text to appear on screen
# import pygame.freetype

# screen dimentions
WIDTH = 800
HEIGHT = 600

# game settings
FPS = 30
RUNNING = True

# player attributes
PLAYER_ACC = 1
PLAYER_FRICTION = -0.5
PLAYER_GRAV = 2
PLAYER_JUMP = 35
PLAYER_PUSH = 200
MOB_ACC = 0.5
MOB_FRICTION = -0.5
 
SCORE = 0
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255,50)
LIGHTBLUE = (150, 150, 255)
LIGHTGREEN = (50, 255, 50)



# These are the platforms that the game can use
PLATFORM_LIST = [
                (0, HEIGHT - 40, WIDTH/3, 40, LIGHTGREEN, "normal"),
                 (WIDTH*2/3, HEIGHT - 40, WIDTH/3, 40, LIGHTGREEN, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, LIGHTBLUE, "bouncey"),
                #  (125, HEIGHT - 350, 100, 5, RED, "disappearing"),
                 (350, 200, 100, 20, YELLOW, "normal"),
                 #(175, 100, 50, 20, (200,200,200), "normal")
                 ]