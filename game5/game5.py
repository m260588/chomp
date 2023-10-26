import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

pygame.init()

#create the screen

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player fish')

clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

for _ in range (5):
    fishes.add(Fish(random.randint(screen_width, screen_height*2), random.randint(0, screen_height-tile_size)))
# draw player fish
player = Player(screen_width/2, screen_height/2)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        player.stop() # the fish will keep going on key down without this playstop, you can also use keyup instead
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
                player.move_up()
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')
                player.move_down()
            if event.key == pygame.K_LEFT:
                print('You pressed the left key')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('You pressed the right key')
                player.move_right()
            


    screen.blit(background, (0, 0))

    # update fish position
    fishes.update()

    player.update()


    for fish in fishes:
        if fish.rect.x < -tile_size:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(0, screen_height-tile_size)))


    fishes.draw(screen)

    player.draw(screen)

    pygame.display.flip()

    #set the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()