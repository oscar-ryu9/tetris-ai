import pygame
pygame.init()
(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))


class Grid:
    def __init__(self):
        self.dimensions = (1000, 2000)

    def draw(self):
        grid = pygame.Rect(980, 120, 600, 1200)
        pygame.draw.rect(screen, (255, 255, 255), grid)

