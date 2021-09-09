import pygame
from random import randint

from constants import *

class Pillar:

    def __init__(self, color=(0, 0, 255)):

        self.x = WINDOW_WIDTH
        self.width = 100
        self.height1 = randint(50, WINDOW_HEIGHT - 100)
        self.height2 = randint(50, WINDOW_HEIGHT - self.height1 - 50)
        self.color = color

    def render(self):

        pygame.draw.rect(SCREEN, self.color, [self.x, 0, self.width, self.height1])
        pygame.draw.rect(SCREEN, self.color, [self.x, WINDOW_HEIGHT - self.height2, self.width, self.height2])

    def update(self):

        self.x -= 3

        self.render()