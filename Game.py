import pygame
import sys
import random
from Player import Player
from Food import Food

class Game():
    def __init__(self,screen):
        self.screen = screen
        self.player = Player()
        self.food = Food(screen)
    def collision(self):
        if player.x == food.x:
            if player.y == food.y:
                return True