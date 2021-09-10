import pygame
from random import randint

from constants import *

class Pillar:

    def __init__(self, color=(173, 40, 9)):

        self.x = WINDOW_WIDTH
        self.width = 100
        self.gap = 100
        self.height1 = randint(200, 400)
        self.height2 = WINDOW_HEIGHT - self.height1 - self.gap - randint(0, 100)
        self.color = color

    def render(self):

        pygame.draw.rect(SCREEN, self.color, [self.x, 0, self.width, self.height1])
        pygame.draw.rect(SCREEN, self.color, [self.x, WINDOW_HEIGHT - self.height2, self.width, self.height2])

    def update(self):

        self.x -= 3

        self.render()