import pygame as p
import random

WIDTH = 360
HEIGHT = 480
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

p.init()
p.mixer.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("MY_GAME")
clock = p.time.Clock()

running = True

while running:
    screen.fill(WHITE)

    p.display.flip()