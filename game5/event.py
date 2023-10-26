import pygame
import sys


from game_parameters import *
from background import draw_background

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Learning to get event types')

#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')


#draw backgrounf
    screen.blit(background, (0,0))
    pygame.display.flip()

pygame.quit()



