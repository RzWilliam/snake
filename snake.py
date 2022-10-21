import pygame


class Snake:
    def _init_(self):
        print("snake")

    def Draw(screen, array, size, deg):
        for x in array:

            if x == array[-1]:
                head = pygame.image.load('assets/snake_head.png').convert_alpha()
                head = pygame.transform.scale(head, (size, size))
                head = pygame.transform.rotate(head, deg)
                screen.blit(head, (x[0], x[1]))
                pygame.draw.circle(screen, (170, 215, 81), (x[0], x[1]), 1)
            else:
                pygame.draw.rect(screen, (193, 168, 65), pygame.Rect(x[0], x[1], size, size))

