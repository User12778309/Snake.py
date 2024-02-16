import pygame
import sys
import random


ligne = ( 10 )
colonne = ( 15 )
cellule = ( 40 )

class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = random.randrange(0,10)
        self.y = random.randrange(0, 15)
    def draw_player(self):
        player = pygame.Rect(self.x * cellule,self.y * cellule,cellule,cellule)
        pygame.draw.rect(screen,pygame.Color("green"),player)
    def move_player(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.x -=1
        if pressed[pygame.K_RIGHT]:
            self.x +=1
        if pressed[pygame.K_UP]:
            self.y -=1
        if pressed[pygame.K_DOWN]:
            self.y +=1
        if pressed[pygame.K_a]:
            self.x -=1
        if pressed[pygame.K_d]:
            self.x +=1
        if pressed[pygame.K_w]:
            self.y -=1
        if pressed[pygame.K_s]:
            self.y +=1
