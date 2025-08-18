import pygame
from constants import *
from bodypart import BodyPart

class Body(pygame.sprite.Sprite):
    containers = ()
    def __init__(self, pos):
        super().__init__(*self.containers)
        #start pos
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        #bodyparts 
        body = BodyPart(center_x, center_y, 40, YOSHI_GREEN)
        neck = BodyPart(center_x + 20, center_y - 45, 20, YOSHI_GREEN)
        head = BodyPart(center_x + 30, center_y - 70, 30, YOSHI_GREEN)
        nose = BodyPart(center_x + 50, center_y - 90, 30, YOSHI_GREEN)
        #list of body parts
        self.bodyparts = [body, neck, head, nose]

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

    def update(self, dt):
        for circle in self.bodyparts:
            circle.update(dt)

    def draw(self, surface):
        for circle in self.bodyparts:
            circle.draw(surface)
