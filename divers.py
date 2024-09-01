#------------------------------------#
# Bibliothèque de fonctions diverses #
#------------------------------------#

import pygame
import variables as var


#----Fonction pour écrire à l'écran-------------------------------------------------------------------------------------
def ecrit(texte,col,size, x, y,police):

    if police == "":
        font = pygame.freetype.Font(None, size)
    else:
        font = pygame.freetype.Font("Assets/retro.ttf", size)

    text_surf2, text_rect2 = font.render(texte,col)     # font.render permet d'avoir une transparence
    var.ecran.blit(text_surf2, (x, y))
