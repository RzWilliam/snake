import pygame


class Obstacle:
    def _init_(self):
        print("Obstacle")

    def Draw(screen,array, size):
        img = pygame.image.load('assets/wall.jpg').convert_alpha()
        img = pygame.transform.scale(img, (size, size))

        for x in array:
            screen.blit(img, (x[0], x[1]))
            pygame.draw.circle(screen, (170, 215, 81), (x[0], x[1]), 1)
