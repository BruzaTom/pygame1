import pygame
from constants import *
from partical import Partical

class Curser(pygame.sprite.Sprite):
    containers = ()
    def __init__(self, pos):
        super().__init__(*self.containers)
        #start pos
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        #for hollow curser
        #pygame.draw.rect(self.image, red, self.image.get_rect(), 2)
        #for soloid curser
        self.image.fill(red)
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = CURSER_SPEED 
        self.spawn_timer = 0
    def generate_object(self, object):
        self.spawn_timer = PARTICAL_COOL_DOWN
        object(self.rect.x, self.rect.y, radious = 4)

    def input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        #commands
        if keys[pygame.K_SPACE]:
            if self.spawn_timer < 0:
                self.generate_object(Partical)

    def update(self, dt):
        self.spawn_timer -= dt
        self.input(dt)
        self.rect.center += self.direction * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

