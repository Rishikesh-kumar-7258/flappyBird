import pygame

from constants import *

class Bird:

    def __init__(self):

        self.size = 40
        self.x = 200
        self.y = WINDOW_HEIGHT // 2 - self.size // 2
        self.color = BLUE
        self.bird = pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.size, self.size])

    def render(self):
        self.bird = pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.size, self.size])

    def update(self):

        self.render()
    
    def collides(self, obj):

        return ((self.x + self.size >= obj.x and self.x <= obj.x + obj.width) and 
                (self.y <= obj.height1 or self.y + self.size >= WINDOW_HEIGHT - obj.height2))