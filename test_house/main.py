import pygame, sys
from random import randint
from body import Body
from constants import *


#class Partical(pygame.sprite.Sprite)
#class Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

#groups
updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
#containers
Body.containers = (updatable_group, drawable_group)
#Partical.containers = (updatable_group, drawable_group, partical_group)

#init body
body = Body((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
while True:
    screen.fill('#71ddee')
    for item in updatable_group:
        item.update(dt)
    for item in drawable_group:
        item.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    dt = clock.tick(60) / 1000
    pygame.display.flip()
