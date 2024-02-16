import pygame
import sys
import random
from Food import Food
from Player import Player
from Game import Game


ligne = ( 10 )
colonne = ( 15 )
cellule = ( 40 )

pygame.init()

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Snake de golmon V1")

FPS = pygame.time.Clock()

food = Food(screen)
player = Player(screen)
game = Game(screen)

def show_grid():
    for i in range(0,ligne):
        for j in range(0,colonne):
            grille = pygame.Rect(i * cellule,j * cellule,cellule,cellule)
            pygame.draw.rect(screen,pygame.Color("black"),grille,width=0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")
    show_grid()
    food.draw_food()
    player.draw_player()
    player.move_player()
    game.collision()
    pygame.display.flip()
    FPS.tick(10)