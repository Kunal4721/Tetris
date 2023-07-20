import pygame
import random

# 10 width X 20 height square blocks

#Some Global Variables
screen_width = 800
screen_height = 700

play_width = 300 #10 blocks of 30 width
play_height = 600 #20 blocks of 20 height

block_size = 30

top_left_x = (screen_width - play_width) // 2
top_left_y =  screen_height - play_height

# All Block Shapes
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S,Z,I,O,J,L,T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(10)]for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j,i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def get_shape():
    return random.choice(shapes)

def draw_grid(surface):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont('arial', 60)
    label  = font.render('Tetris', 1, (255,255,255))

    surface.blit(label, )