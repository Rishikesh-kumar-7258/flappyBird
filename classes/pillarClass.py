import pygame
import random

from contants import *

class Pillar:

    def __init_(self, color="blue"):

        self.x = WINDOW_WIDTH
        self.y = random.randint(50, WINDOW_HEIGHT // 2 - 20)
        self.color = color

        self.img = pygame.image.load("../Images/1x/blue.png")


    def render(self) : 

        img_rect = self.img.get_rect()
        img_rect.x = self.x
        img_rect.y = self.y

        SCREEN.blit(self.img, img_rect)

        pygame.draw.rect(SCREEN, (255, 255, 255), [50, 50, 50, 50])

    def update(self) : 

        self.render()