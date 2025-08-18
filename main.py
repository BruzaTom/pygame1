import pygame, sys
from random import randint
from partical import Partical
from water import Water
from dirt import Dirt
from curser import Curser
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
partical_group = pygame.sprite.Group()
#containers
Curser.containers = (updatable_group, drawable_group)
Water.containers = (updatable_group, drawable_group, partical_group)
Partical.containers = (updatable_group, drawable_group, partical_group)
Dirt.containers = (updatable_group, drawable_group, partical_group)

#init curser
curser = Curser((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
while True:
    screen.fill('black')
    for item in updatable_group:
        item.update(dt)
    for item in drawable_group:
        item.draw(screen)
    for item in partical_group:
        for other_item in partical_group:
            if item.collisions(other_item):
                item.contact(other_item)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    dt = clock.tick(60) / 1000
    pygame.display.flip()
