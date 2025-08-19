import pygame
from constants import *
from circleshape import CircleShape
from partical import Partical
from random import randint
import math

class Dirt(Partical):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, color=DIRT)


