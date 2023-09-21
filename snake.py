import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.dx = 20
        self.dy = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(window, green, [element[0], element[1], 20, 20])

    def move(self):
        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i] = [self.elements[i-1][0], self.elements[i-1][1]]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def add_element(self):
        self.size += 1
        self.elements.append([0, 0])

class Food:
    def __init__(self):
        self.x = random.randint(0, (window_width-20) // 20) * 20
        self.y = random.randint(0, (window_height-20) // 20) * 20

    def draw(self):
        pygame.draw.rect(window, red, [self.x, self.y, 20, 20])

snake = Snake()
food = Food()

clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -20
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 20
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dy = -20
                snake.dx = 0
            elif event.key == pygame.K_DOWN:
                snake.dy = 20
                snake.dx = 0

    snake.move()
    if snake.elements[0][0] < 0 or snake.elements[0][0] > window_width - 20 or snake.elements[0][1] < 0 or snake.elements[0][1] > window_height - 20:
        game_over = True
    for element in snake.elements[1:]:
        if snake.elements[0] == element:
            game_over = True

    if snake.elements[0] == [food.x, food.y]:
        snake.add_element()
        food = Food()

    window.fill(black)
    snake.draw()
    food.draw()
    pygame.display.update()

    clock.tick(10)

pygame.quit()
