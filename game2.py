import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
title_size = 64


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Adding Fonts')

custom_font = pygame.font.Font("Assests/Fonts/Black_Crayon.ttf", 128)

def draw_background(surf):
    water = pygame.image.load("Assests/Sprites/water.png").convert()
    sand = pygame.image.load("Assests/Sprites/sand_top.png").convert()
    seagrass = pygame.image.load("Assests/Sprites/seagrass.png").convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    for x in range(0, screen_width, title_size):
        for y in range(0, screen_height, title_size):
            surf.blit(water, (x,y))

    for x in range(0, screen_width, title_size):
        surf.blit(sand, (x, screen_height-title_size))

    for _ in range (4):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height-title_size*2+22))


    text = custom_font.render("Chomp", True, (225,29,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()/2))
def draw_fishes(surf):
    #load fish tiles onto the surface
    

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))


    pygame.display.flip()
pygame.quit()