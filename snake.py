import pygame
import random

#Start of pygame

pygame.init

#Game window

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game For You :)")

#Colours

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

#Snake Class

class Snake:
