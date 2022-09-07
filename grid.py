import pygame
pygame.init()

(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))

class Grid:
    def __init__(self, b1, b2, b3, b4, shape):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.shape = shape
        self.current_board = None



