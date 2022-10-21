import pygame


class Fruit:
    def __init__(self):
        self.image = 0
        self.color = (170, 215, 81)
        self.square = 0
        print("Fruit")

    def Draw(self, screen, x, y, size):
        self.image = pygame.transform.scale(pygame.image.load('assets/apple.png').convert_alpha(), (size, size))
        screen.blit(self.image, (x, y))
        self.square = pygame.draw.circle(screen, self.color, (x, y), 1)
