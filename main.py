import pygame, sys
from random import randint
from tree import Tree
from player import Player

#class Tree(pygame.sprite.Sprite)
#class Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#setup
camera_group = pygame.sprite.Group()
Player((640, 360), camera_group)

for i in range (20):
    random_x = randint(0,1000)
    random_y = randint(0,1000)
    Tree((random_x,random_y), camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#71ddee')
    camera_group.update()
    camera_group.draw(screen)

    pygame.display.update()
