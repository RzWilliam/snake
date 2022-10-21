import pygame


class Snake:
    def __init__(self):
        print("snake")
        self.image = 0
        self.color1 = (170, 215, 81)
        self.color2 = (193, 168, 65)

    def Draw(self, screen, array, size, deg):
        for x in array:

            if x == array[-1]:
                self.image = pygame.transform.scale(pygame.image.load('assets/snake_head.png').convert_alpha(), (size, size))
                self.image = pygame.transform.rotate(self.image, deg)
                screen.blit(self.image, (x[0], x[1]))
                pygame.draw.circle(screen, self.color1, (x[0], x[1]), 1)
            else:
                pygame.draw.rect(screen, self.color2, pygame.Rect(x[0], x[1], size, size))

