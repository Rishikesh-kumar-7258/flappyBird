import pygame

from constants import *

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = 40
        self.x = 200
        self.y = WINDOW_HEIGHT // 2 - self.size // 2
        self.color = BLUE

        self.image = pygame.image.load("../Images/Bird/Asset 1.png").convert()
        self.image2 = pygame.image.load("../Images/Bird/Asset 2.png").convert()
        self.image.set_colorkey(WHITE)
        self.image2.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.rect2 = self.image.get_rect()
        self.rect2.center = (self.x, self.y)
        # self.bird = pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.size, self.size])

    # def render(self):
    #     self.bird = pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.size, self.size])

    def update(self):  pass

        # self.render()
    
    # def collides(self, obj):

    #     return ((self.x + self.size >= obj.x and self.x <= obj.x + obj.width) and 
    #             (self.y <= obj.height1 or self.y + self.size >= WINDOW_HEIGHT - obj.height2))