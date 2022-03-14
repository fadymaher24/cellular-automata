import pygame
import numpy as np
import random
i = 0
n = 0
cellcolor = []
class Grid:
    def __init__(self, width, height, scale, offset):
        # side of the square
        self.scale = scale
        self.columns = int((height // self.scale))
        self.rows = int((width // self.scale))

        # tuple for Example : (5, 10)
        self.size = (self.rows, self.columns)

        # cellular automata grid
        self.grid_array = np.ndarray(shape=(self.size))

        self.offset = offset

    # intialize the grid with a random values
    def random2d_array(self, Rcolor):
        global cellcolor
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)
        for i in range(100):
            cellcolor.append(Rcolor[i])

    def Conway(self, off_color, on_color, surface, pause, Rcolor,cflag, Location, Cell):
        global n,i, cellcolor
        if cflag == 1:
            if Cell == True:
                i +=1
            else:
                n+=1
        elif cflag == -1:
            if Cell == True:
                i -=1
            else:
                n-=1
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if Location == (x,y):
                    if self.grid_array[x][y] == 1:
                        self.grid_array[x][y] = 0
                    else:
                        self.grid_array[x][y] = 1
                if self.grid_array[x][y] == 1:
                    if Cell == True:
                        on_color = cellcolor[i%100]
                        i += 1
                    else:
                        on_color =Rcolor[n%100]
                    pygame.draw.ellipse(surface, on_color,
                                        [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.ellipse(surface, off_color,
                                        [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset], 20)

        next = np.ndarray(shape=(self.size))
        if pause == False:
            n += 1
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)

                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                            next[x][y] = 0
                    elif state ==1 and(neighbours < 2 or neighbours > 3):
                        next[x][y]=np.random.choice([0,1], p=[0.8,0.2])
                    else:
                        next[x][y] = state
            self.grid_array = next

    def Button_click(grid_array, mpos, x, y, n):
        if mpos[0]:
            n[int(x / 30)][int(y / 30)] = 1
        if mpos[1]:
            n[x][y] = 0

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n) % self.rows
                y_edge = (y + m) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total