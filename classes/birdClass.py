import pygame

from constants import *

class Bird:

    def __init__(self):

        self.size = 50
        self.x = 200
        self.y = WINDOW_HEIGHT // 2 - self.size // 2
        self.color = BLUE
        self.bird = pygame.draw.rect(SCREEN, self.color, [self.x])

    def render(self):
        self.bird = pygame.draw.rect(SCREEN, self.color, [self.x])

    def update(self):

        self.render()