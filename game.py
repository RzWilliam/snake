import pygame
import random
from board import Board
from snake import Snake
from fruit import Fruit
from obstacle import Obstacle

# Defaults settings
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
module_charge = pygame.init
print(module_charge)
timer = pygame.time.Clock()
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Declare variables
is_not_dead = True
score = 0
snake_size = 30
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_array = []
snake_length = 1
move_x = 0
move_y = 0
fruit_x = random.randrange(0, screen_width, snake_size)
fruit_y = random.randrange(0, screen_height, snake_size)
obstacles = []
direction = 0
deg = 0

while is_not_dead:
    screen.fill((125, 125, 125))
    Board.Draw(screen, snake_size)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:  # Touche J
                is_not_dead = False
            elif event.key == pygame.K_z and direction != 3:
                move_y = -snake_size
                move_x = 0
                direction = 1
                deg = 270

            elif event.key == pygame.K_s and direction != 1:
                move_y = snake_size
                move_x = 0
                direction = 3
                deg = 90

            elif event.key == pygame.K_d and direction != 2:
                move_x = snake_size
                move_y = 0
                direction = 4
                deg = 180

            elif event.key == pygame.K_q and direction != 4:
                move_x = -snake_size
                move_y = 0
                direction = 2
                deg = 0

        if event.type == pygame.QUIT:
            is_not_dead = False

    # Die if off screen
    if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
        is_not_dead = False

    # Movement of snake
    snake_x += move_x
    snake_y += move_y
    snake_head = [snake_x, snake_y]
    snake_array.append(snake_head)
    # Draw first fruit
    Fruit.Draw(screen, fruit_x, fruit_y, snake_size)

    # Maintain correct number of square
    if snake_length < len(snake_array):
        del snake_array[0]

    # Die if the head collide with the body
    for x in snake_array[:-1]:
        if x == snake_head:
            is_not_dead = False

    for x in obstacles:
        if x == snake_head:
            is_not_dead = False

    Snake.Draw(screen, snake_array, snake_size, deg)

    # Change position of fruit after being eaten
    if snake_x == fruit_x and snake_y == fruit_y:
        fruit_x = random.randrange(0, screen_width, snake_size)
        fruit_y = random.randrange(0, screen_height, snake_size)
        obstacle_x = random.randrange(0, screen_width, snake_size)
        obstacle_y = random.randrange(0, screen_height, snake_size)
        snake_length += 1
        score += 1

    # Create Obstacle
    if score % 4 == 0 and score > 1:
        obstacle_coord = [obstacle_x, obstacle_y]
        obstacles.append(obstacle_coord)

    Obstacle.Draw(screen, obstacles, snake_size)

    text = font.render("Score : " + str(score), True, (0, 128, 0))
    screen.blit(text, (300 - text.get_width() // 2, 50 - text.get_height() // 2))
    # Speed of game
    timer.tick(10)

    pygame.display.flip()

pygame.quit()