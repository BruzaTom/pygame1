import pygame
from constants import *
from circleshape import CircleShape
from random import randint
import math

class Partical(CircleShape):
    containers = ()
    def __init__(self, x, y, radius, color='white'):
        super().__init__(x, y, radius)
        self.position.x += randint(1, 25)
        self.color = color
        self.dead = False

    def update(self, dt):
        if self.position.y < FLOOR:
            self.velocity.y += PARTICAL_GRAV
        if not self.dead:
            self.position += self.velocity * dt
        if self.position.y > FLOOR:
            self.velocity.y = 0
            if self.position.y >= FLOOR:
                self.position.y = self.position.y - (2 * (self.position.y - FLOOR))
        self.check_stopped()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def contact(self, CircleShape):
        if not CircleShape.dead:
            return
        dx = self.position.x - CircleShape.position.x
        dy = self.position.y - CircleShape.position.y
        distance = math.sqrt(dx**2 + dy**2)
        min_distance = self.radius + CircleShape.radius

        if distance < min_distance:
            # Avoid division by zero
            if distance == 0:
                # Arbitrarily separate along x-axis
                dx, dy = 1.0, 0.0
                distance = 1.0
            # Normalize direction vector
            nx = dx / distance
            ny = dy / distance
            # Calculate overlap amount
            overlap = min_distance - distance
            # Push each circle away from the CircleShape by half the overlap
            self.position.x += nx * (overlap / 2)
            self.position.y += ny * (overlap / 2)
            CircleShape.position.x -= nx * (overlap / 2)
            CircleShape.position.y -= ny * (overlap / 2)

    def check_stopped(self, threshold=0.01):
        if abs(self.velocity.y) < threshold:
            self.dead = True
