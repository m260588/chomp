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

for _ in range (10):
    fishes.add(Fish(random.randint(screen_width, screen_height*2), random.randint(0, screen_height-tile_size)))
# draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font for score
score = 0
score_font = pygame.font.Font("../Assests/Fonts/Black_Crayon.ttf", 48)

chomp = pygame.mixer.Sound("../Assests/sounds/chomp.wav")
bubbles = pygame.mixer.Sound("../Assests/sounds/bubbles.wav")
hurt = pygame.mixer.Sound("../Assests/sounds/hurt.wav")

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        player.stop() # the fish will keep going on key down without this playstop, you can also use keyup instead
        if event.type == pygame.KEYDOWN:
            pygame.mixer.Sound.play(bubbles)
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

    #check for collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result:
        score += len(result)
        pygame.mixer.Sound.play(chomp)


    for _ in range(len(result)):
        fishes.add(Fish(random.randint(screen_width, screen_height * 2), random.randint(0, screen_height - tile_size)))




    for fish in fishes:
        if fish.rect.x < -tile_size:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(0, screen_height-tile_size)))


    fishes.draw(screen)

    player.draw(screen)

    #update score on screen
    text = score_font.render(f"Score: {score}", True, (225, 29, 0))
    screen.blit(text, (screen_width - text.get_width() / 2 - 100, 0))

    pygame.display.flip()

    #set the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()