import pygame
import classes
from classes import Case

# Define some colors
BLACK = (0, 0, 0)
LIGHT_GREY = (0,50,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0, 0)
PINK = (255,85,255)
CYAN = (85,255,255)

# Init écran graphique
SCREEN_X = 1024
SCREEN_Y = 768
pygame.init()
size = [SCREEN_X, SCREEN_Y]
ecran = pygame.display.set_mode(size)
pygame.display.set_caption("Tablator")

bordure_x = 100
bordure_y = 100

Num_ecran = 0   # on commence dans l'application

long_case = 15
larg_case = 15

# Déclaration d'une section de tablature pour test
tab = []
section = []
case = Case(0,99,99,99)
section.append(case)
case = Case(99,0,99,99)
section.append(case)
case = Case(99,99,0,99)
section.append(case)
case = Case(99,99,99,0)
section.append(case)

tab.append(section)

# tab.append(section)

print("longueur section : ",len(section))
print("section : ", section)
print("section[0] : ",section[0].E)
print("section[1] : ",section[1].E)
print("section[2] : ",section[2].E)
print("section[3] : ",section[3].E)