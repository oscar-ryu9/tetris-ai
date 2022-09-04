import pygame
import shapes
import grid

pygame.init()

(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))

#tetris caption
pygame.display.set_caption('Tetris')

#tetris logo
logo = pygame.image.load('assets/tetris_logo.jpg')
pygame.display.set_icon(logo)



#click window x will quit pygame
running = True
while running:

    #exit clause
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #background
    background_color = (255, 255, 255)
    screen.fill(background_color)

    #background aesthetics
    grey_rectangle1 = pygame.Rect(275, 15, 2010, 1410)
    grey_rectangle2 = pygame.Rect(280, 20, 2000, 1400)
    pygame.draw.rect(screen, (207, 207, 207), grey_rectangle1)
    pygame.draw.rect(screen, (232, 232, 232), grey_rectangle2)
    pygame.display.update()





pygame.quit()