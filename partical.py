import pygame
from constants import *
from circleshape import CircleShape
from random import randint

class Partical(CircleShape):
    containers = ()
    def __init__(self, x, y, radious):
        super().__init__(x, y, radious)
        self.position.x += randint(1, 25)

    def update(self, dt):
        if self.position.y < FLOOR:
            self.position += self.gravity_effect() * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def gravity_effect(self):
        return pygame.Vector2(0, PARTICAL_GRAV)  # pixels per second downward
        
