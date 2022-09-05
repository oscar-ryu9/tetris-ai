import pygame
pygame.init()

(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))


class Tetromino:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.update = False

    def draw(self):
        if self.type == 'block':
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.update = True
                block = pygame.Rect(self.x, self.y, 61, 61)
                pygame.draw.rect(screen, (255, 0, 0), block)
                pygame.draw.rect(screen, (0, 0, 0), block, 4)
                self.last = pygame.time.get_ticks()
                self.y += 60
            else:
                self.update = False

    def get_update(self):
        return self.update




