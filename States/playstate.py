from random import randint
from classes.pillarClass import Pillar
from constants import SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
from classes.birdClass import Bird
import pygame

from States.basestate import Base

class Play(Base):

    def __init__(self):
        super().__init__()

        self.pillar_sprite = pygame.sprite.Group()
        self.all_sprite = pygame.sprite.Group()
        self.bird = Bird()
        # self.bird_sprite.add(self.bird)
        self.all_sprite.add(self.bird)
        self.speed = 0
        self.g = 0.5

        pillar1, pillar2 = Pillar(), Pillar()
        pillar1.rect.y = randint(-150, 0)
        pillar2.rect.y = WINDOW_HEIGHT // 2 + (pillar1.rect.bottom - randint(100, 150))
        self.all_sprite.add(pillar1)
        self.pillar_sprite.add(pillar1)
        self.all_sprite.add(pillar2)
        self.pillar_sprite.add(pillar2)

        self.last = pillar1

    def render(self) :
        self.all_sprite.draw(SCREEN)

    def update(self, params) : 

        if (self.last.rect.x <= WINDOW_WIDTH - 300):
            pillar1, pillar2 = Pillar(), Pillar()
            pillar1.rect.y = randint(-150, 0)
            pillar2.rect.y = WINDOW_HEIGHT // 2 + (pillar1.rect.bottom - randint(100, 150))
            self.all_sprite.add(pillar1)
            self.pillar_sprite.add(pillar1)
            self.all_sprite.add(pillar2)
            self.pillar_sprite.add(pillar2)
            self.last = pillar1
        
        for pillar in self.pillar_sprite:
            if pillar.rect.x < - pillar.rect.width: 
                pillar.kill()

        self.speed += self.g
        self.bird.rect.y += self.speed

        for pillar in self.pillar_sprite:
            pillar.rect.x -= 3


        hit_list = pygame.sprite.spritecollide(self.bird, self.pillar_sprite, False)

        for pillar in hit_list:
            print("This is working")

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.speed = -8

        self.render()