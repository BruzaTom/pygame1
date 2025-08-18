import pygame
from constants import *
from circleshape import CircleShape
from random import randint

class BodyPart(CircleShape):
    containers = ()
    def __init__(self, x, y, radious, color):
        super().__init__(x, y, radious)
        self.color = color

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=100)

