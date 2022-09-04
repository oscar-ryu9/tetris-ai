import pygame
import shapes

pygame.init()

(width, height) = (2560, 1440)
screen = pygame.display.set_mode((width, height))
pygame.display.toggle_fullscreen()

#background
background_color = (255, 255, 255)
screen.fill(background_color)

pygame.display.flip()

#tetris caption
pygame.display.set_caption('Tetris')

#tetris logo
logo = pygame.image.load('assets/tetris_logo.jpg')
pygame.display.set_icon(logo)



# click window x will quit pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()