import pygame


class Obstacle:
    def __init__(self):
        self.image = pygame.image.load('assets/wall.jpg').convert_alpha()
        self.color = (170, 215, 81)
        print("Obstacle")

    def Draw(self, screen,array, size):
        self.image = pygame.transform.scale(self.image, (size, size))
        for x in array:
            screen.blit(self.image, (x[0], x[1]))
            pygame.draw.circle(screen, self.color, (x[0], x[1]), 1)
