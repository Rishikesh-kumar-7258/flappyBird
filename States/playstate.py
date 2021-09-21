import pygame

from States.basestate import Base

from classes.pillarClass import Pillar
from classes.birdClass import Bird
from constants import *

class Play(Base):

    def __init__(self):
        super().__init__()

        self.pillars = []
        self.current = Pillar()
        self.pillars.append(self.current)
        self.bird = Bird()

        self.bird_sprite = pygame.sprite.Group()
        self.bird_sprite.add(self.bird)

        self.gap = 200

        #setting up background
        self.upper = pygame.image.load("./Images/upper.png")
        self.lower = pygame.image.load("./Images/lower.png")
        self.upper_rect = self.upper.get_rect()
        self.lower_rect = self.lower.get_rect()
        self.upper_rect2 = self.upper.get_rect()
        self.lower_rect2 = self.lower.get_rect()

        self.upper_rect.x = 0
        self.upper_rect.y = 0
        self.lower_rect.x = 0
        self.lower_rect.y = WINDOW_HEIGHT - 40
        self.upper_rect2.x = WINDOW_WIDTH
        self.upper_rect2.y = 0
        self.lower_rect2.x = WINDOW_WIDTH
        self.lower_rect2.y = WINDOW_HEIGHT - 40

        self.lower_speed = 5
        self.upper_speed = 3

        self.bird_speed = 0
        self.accel = 0.3

        self.score = 0
        self.add_score = False

    def render(self): 

        self.bird_sprite.draw(SCREEN)

        for pillar in self.pillars:
            pillar.render()

        SCREEN.blit(self.upper, self.upper_rect)
        SCREEN.blit(self.lower, self.lower_rect)
        SCREEN.blit(self.upper, self.upper_rect2)
        SCREEN.blit(self.lower, self.lower_rect2)

    def update(self, params):

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird_speed = -5
            
        self.bird_speed += self.accel
        self.bird.y += self.bird_speed

        self.lower_rect.x -= self.lower_speed
        self.lower_rect2.x -= self.lower_speed
        self.upper_rect.x -= self.upper_speed
        self.upper_rect2.x -= self.upper_speed

        if self.bird.y <= 0 or self.bird.y >= WINDOW_HEIGHT - 40: gStateMachine.change("gameover")
        
        self.re_render(self.upper_rect)
        self.re_render(self.upper_rect2)
        self.re_render(self.lower_rect)
        self.re_render(self.lower_rect2)


        if self.current.x <= WINDOW_WIDTH - self.gap - self.current.width:
            self.current = Pillar()
            self.pillars.append(self.current)
        
        for pillar in self.pillars:
            if self.bird.collides(pillar) :
                gStateMachine.change("gameover")
            # if self.bird.x + self.bird.size >= pillar.x and 
            if pillar.x < -pillar.width - self.gap : self.pillars = self.pillars[1:]
            pillar.update()

        self.render()
    
    def enter(self):
        self.pillars = []
        self.current = Pillar()
        self.pillars.append(self.current)
        self.bird_speed = 0
        self.bird = Bird()
        self.score = 0

    
    def re_render(self, img):
        if img.x <= -WINDOW_WIDTH :
            img.x = WINDOW_WIDTH