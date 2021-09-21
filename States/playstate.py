from constants import SCREEN
from classes.birdClass import Bird
import pygame

from States.basestate import Base

class Play(Base):

    def __init__(self):
        super().__init__()

        self.bird_sprite = pygame.sprite.Group()
        self.bird = Bird()
        self.bird_sprite.add(self.bird)
        self.speed = 0
        self.g = 0.5

    
    def render(self) :
        self.bird_sprite.draw(SCREEN)

    def update(self, params) : 

        self.speed += self.g
        self.bird.rect.y += self.speed

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.speed = -8

        self.render()