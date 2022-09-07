import pygame
import shapes
import random

pygame.init()

(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))

#tetris caption
pygame.display.set_caption('Tetris')

#tetris logo
logo = pygame.image.load('assets/tetris_logo.jpg')
pygame.display.set_icon(logo)

#initialize blocks
bag_of_shapes = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
Block = shapes.Tetromino(random.choice(bag_of_shapes), 1161, 120)


def draw_grid():
    grid_outer = pygame.Rect(977, 117, 606, 1206)
    grid_inner = pygame.Rect(982, 122, 596, 1196)

    pygame.draw.rect(screen, (255, 255, 255), grid_inner)

    for i in range(9):
        start_pos = (((i+1)*60) + 980, 120)
        end_pos = (((i+1)*60) + 980, 1320)
        pygame.draw.line(screen, (232, 232, 232), start_pos, end_pos, 2)

    for i in range(19):
        start_pos = (980, ((i+1)*60) + 120)
        end_pos = (1580, ((i+1)*60) + 120)
        pygame.draw.line(screen, (232, 232, 232), start_pos, end_pos, 2)

    pygame.draw.rect(screen, (0, 0, 0), grid_outer, 5)


def draw_background():
    background_color = (255, 255, 255)
    screen.fill(background_color)

    grey_rectangle1 = pygame.Rect(275, 15, 2010, 1410)
    grey_rectangle2 = pygame.Rect(280, 20, 2000, 1400)
    pygame.draw.rect(screen, (207, 207, 207), grey_rectangle1)
    pygame.draw.rect(screen, (232, 232, 232), grey_rectangle2)



#game


running = True
collision = False
Block = shapes.Tetromino(random.choice(bag_of_shapes), 1161, 120)
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # exit clause
            if event.key == pygame.K_ESCAPE:
                running = False
            #rotate shape clause
            if event.key == pygame.K_SPACE:
                Block.rotate()



    # block
    if collision:
        Block = shapes.Tetromino(random.choice(bag_of_shapes), 1161, 120)

    draw_background()
    draw_grid()
    collision = Block.draw()

    if Block.get_update():
        pygame.display.update()

pygame.quit()
