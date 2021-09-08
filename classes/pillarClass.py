import pygame
import random

from contants import *

class Pillar(pygame.sprite.Sprite):

    def __init_(self, color="blue"):
        super().__init__()

        self.x = WINDOW_WIDTH
        self.y = random.randint(50, WINDOW_HEIGHT // 2 - 20)
        self.color = color

        # self.img = PILLARS[0]

        # self.image.fill(WHITE)
        # self.image.set_colorkey(WHITE)

        # pygame.draw.rect(self.image, color, [0, 0, width, height])
        # self.image.render()
        # if (color == "blue") :
        #     self.image = pygame.image.load("../Images/1x/Asset 1.png")
        # elif color == 'pink':
        #     self.image = pygame.image.load("../Images/1x/Asset 2.png")
        # else : self.image = pygame.image.load('../Images/1x/Asset 4.png')

    def render(self) : 

        # img_rect = self.img.get_rect()
        # img_rect.x = self.x
        # img_rect.y = self.y

        # SCREEN.blit(self.img, img_rect)

        pygame.draw.rect(SCREEN, (255, 255, 255), [50, 50, 50, 50])

    def update(self) : 

        self.render()