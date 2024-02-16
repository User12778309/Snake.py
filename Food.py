import pygame
import sys
import random

class Food():
    def __init__(self):
        self.x = random.randrange(0,10)
        self.y = random.randrange(0,15)
    def draw_food(self):
        food = pygame.Rect(self.x * cellule,self.y * cellule,cellule,cellule)
        pygame.draw.rect(screen,pygame.Color("red"),food)