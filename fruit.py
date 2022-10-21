import pygame


class Fruit:
    def _init_(self):
        print("Fruit")

    def Draw(screen, x, y, size):
        img = pygame.image.load('assets/apple.png').convert_alpha()
        img = pygame.transform.scale(img, (size, size))
        screen.blit(img, (x, y))
        pygame.draw.circle(screen, (170, 215, 81), (x, y), 1)
