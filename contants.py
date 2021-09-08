import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# C      R  G  B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)
GREEN = (0, 255, 0)
RED =   (255, 0, 0)

PILLARS = [
    pygame.image.load("./Images/1x/Asset 1.png"),
    pygame.image.load("./Images/1x/Asset 2.png"),
    pygame.image.load("./Images/1x/Asset 4.png")
]