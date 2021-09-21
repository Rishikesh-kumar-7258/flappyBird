from constants import WHITE, WINDOW_WIDTH
import pygame

class Pillar(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Images/green.png")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH + self.rect.width