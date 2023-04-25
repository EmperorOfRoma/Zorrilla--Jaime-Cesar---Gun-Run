# File created by: Jaime Cesar Zorrilla


# screen dimentions
WIDTH = 800
HEIGHT = 600

# game settings
FPS = 30
RUNNING = True

# player attributes
PLAYER_ACC = 1
PLAYER_FRICTION = -0.9
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
MOB_ACC = 0.5
MOB_FRICTION = -0.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (50, 50, 255)

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (200,200,200), "normal")]