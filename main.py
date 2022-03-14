import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
width, height = 1000, 800
size = (width, height)

pygame.init()

pygame.display.set_caption("CONWAY'S GAME OF LIFE")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width, height, scaler, offset)

random_color = []
for i in range(100):
    random_color.append(np.random.choice(range(256), size=3))
Grid.random2d_array(random_color)
pause = False
Cell = False
run = True
while run:
    colorflag = 0
    clock.tick(fps)
    screen.fill(black)
    location = (-1 ,-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_c:
                colorflag = 1
            if event.key == pygame.K_z:
                colorflag = -1
            if event.key == pygame.K_r:
                Grid.random2d_array(random_color)
            if event.key == pygame.K_a:
                Cell = not Cell
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                location = (pos[0] // scaler, pos[1] // scaler)

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause, Rcolor = random_color, cflag= colorflag, Location = location, Cell=Cell)

    pygame.display.update()

pygame.quit()
