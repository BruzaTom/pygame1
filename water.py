import pygame
from constants import *
from circleshape import CircleShape
from partical import Partical
from random import randint
import math

class Water(Partical):
    containers = ()
    def __init__(self, x, y, radius):
        # Use a soft water-blue color
        super().__init__(x, y, radius, color=AQUA)

