import pygame


class Board:
    def _init_(self):
        print("Board")

    def Draw(screen, size):
        for x in range(20):
            for y in range(20):
                if(x+y) % 2 == 0:
                    pygame.draw.rect(screen, (170,215,81), pygame.Rect(x * size, y * size, size, size))
                else:
                    pygame.draw.rect(screen, (162,209,73), pygame.Rect(x * size, y * size, size, size))