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

class Player():
    def __init__(self):
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


ligne = ( 10 )
colonne = ( 15 )
cellule = ( 40 )

pygame.init()

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Snake de golmon")

FPS = pygame.time.Clock()

food = Food()
player = Player()

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
    pygame.display.flip()
    FPS.tick(10)