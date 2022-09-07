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
        self.cooldown = 100
        self.update = False
        # matrix
        # 0   1   2   3
        # 4   5   6   7
        # 8   9   10  11
        # 12  13  14  15
        self.foundation = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.matrix = {
            'I': [2, 6, 10, 14],
            'J': [0, 4, 5, 6],
            'L': [2, 4, 5, 6],
            'O': [1, 2, 5, 6],
            'S': [1, 2, 4, 5],
            'T': [1, 4, 5, 6],
            'Z': [0, 1, 5, 6]
        }

        self.colors = {
            'I': (0, 182, 221),
            'J': (0, 71, 147),
            'L': (255, 166, 2),
            'O': (255, 229, 45),
            'S': (0, 186, 48),
            'T': (166, 25, 188),
            'Z': (226, 19, 0)
        }

    def draw(self):
        my_matrix = self.matrix[self.type]
        now = pygame.time.get_ticks()
        if self.y < 1320:
            if now - self.last >= self.cooldown:
                self.update = True
                for i in range(4):
                    blocki = pygame.Rect((self.x + ((my_matrix[i]%4)*60)), (self.y + ((my_matrix[i]//4)*60)), 61, 61)
                    pygame.draw.rect(screen, self.colors[self.type], blocki)
                    pygame.draw.rect(screen, (0, 0, 0), blocki, 3)
                self.last = pygame.time.get_ticks()
                self.y += 60
            else:
                self.update = False
            return False
        else:
            return True


    def rotate(self):
        print("ROTATE")

    def get_update(self):
        return self.update




