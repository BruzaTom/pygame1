import pygame
from constants import *
from circleshape import CircleShape
from partical import Partical
from random import randint
import math

class Dirt(Partical):
    containers = ()
    def __init__(self, x, y, radius):
        # Use a soft water-blue color
        super().__init__(x, y, radius, color=DIRT)

    def contact(self, CircleShape):
        self.position.y = CircleShape.position.y + CircleShape.radius + self.radius
        self.velocity = pygame.Vector2(0, 0)
        self.stuck = True

