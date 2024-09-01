# This is a Bass tab Editor
# v0

import pygame

from variables import *
from divers import ecrit


# ----------------------------------------------------------------------------------------------------------------------
def affiche(tab):

    j = 0   # pour les retours à la ligne
    for i in range(0, len(section)):    # on affiche toutes les cases composant la section
        # on affiche les 4 cordes pour chaque case de la section
        pygame.draw.rect(ecran, WHITE, (bordure_x + i * long_case, bordure_y + j * larg_case, long_case, larg_case), 1)         # case G
        if section[i].G != 99:
            ecrit(str(section[i].G), WHITE, 10, bordure_x + i * long_case, bordure_y + (j) * larg_case, "")
        pygame.draw.rect(ecran, WHITE, (bordure_x + i * long_case, bordure_y + (j+1) * larg_case, long_case, larg_case), 1)     # case D
        if section[i].D != 99:
            ecrit(str(section[i].D), WHITE, 10, bordure_x + i * long_case, bordure_y + (j+1) * larg_case, "")
        pygame.draw.rect(ecran, WHITE, (bordure_x + i * long_case, bordure_y + (j+2) * larg_case, long_case, larg_case), 1)     # case A
        if section[i].A != 99:
            ecrit(str(section[i].A), WHITE, 10, bordure_x + i * long_case, bordure_y + (j+2) * larg_case, "")
        pygame.draw.rect(ecran, WHITE, (bordure_x + i * long_case, bordure_y + (j+3) * larg_case, long_case, larg_case), 1)     # case E
        if section[i].E != 99:
            ecrit(str(section[i].E), WHITE, 10, bordure_x + i * long_case, bordure_y + (j+3) * larg_case, "")


    ecrit("2", WHITE, 5, bordure_x + i * long_case, bordure_y + j * larg_case, "")
    # pygame.draw.line(ecran, WHITE, (15, 15), (50, 50), 1)


# ----------------------------------------------------------------------------------------------------------------------
#--Boucle affichage-----------------------------------------------------------------------------------------------------
def updateaffichage(tab):

    ecran.fill(BLACK)  # efface l'écran

    affiche(tab)

    pygame.display.flip()  # affichage à l'écran

# ---MENUS--------------------------------------------------------------------------------------------------------------
def menu(menu):
    match menu:
        case 0:  # Menu principal titre
            # on affiche le texte statique
            ecrit("TABLATOR", WHITE, 20, int(SCREEN_X/2)-60, 32, "")

            pygame.display.update()  # on affiche le tout


#-----GAME--------------------------------------------------------------------------------------------------------------
def run():

    # ----------------gestion des évènements hors interaction joueur--------------------------------


    # ----------------- affichage général du jeu ---------------------------------------------------
    updateaffichage(tab)



clock = pygame.time.Clock()

#-----------------------------------------------------------------------------------------------------------------------
# -------Boucle principale----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

continuer = True
while continuer:

    # Boucle qui tourne pendant le jeu en dehors de la gestion des évènements-------------------------------------------

    # On rafraichit l'affichage graphique des différents menus----------------------------------------------------------
    match Num_ecran:
        case 0:  # Ecran in game
            run()
        case 1:  # Ecran de menu
            menu(0) # 0 = menu principal
        case 2:  # Ecran Victoire Passage d'un level
            pass
        case 3:             # écran Game Over
            pass

    # captation des évènements-----------------------------------------------------------------
    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()          # captation des évèvements claviers sous forme de liste
                                                    # permet de capter la répétition des frappes de touches


        # Clic sur la croix fermeture de la fenetre
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()

        # Evènements clavier-------------------------------------------------------------------------
        # KEYDOWN permet de savoir si une touche a été pressée
        # moins rapide que get_pressed, permet de n'avoir qu'une seule touche pressée
        if event.type == pygame.KEYDOWN:  # Utilisateur presse une touche

            # Touche Escape
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()

            if (event.key == pygame.K_DOWN):           # flèche bas
                match Num_ecran:
                    case 1:                             # on est dans l'écran MENU et on change de mode de jeu
                        pass
            if (event.key == pygame.K_UP):           # flèche haut
                match Num_ecran:
                    case 1:                             # on est dans l'écran MENU et on change de mode de jeu
                        pass
            if (event.key == pygame.K_SPACE):           # Space
                match Num_ecran:
                    case 1:                             # on est dans l'écran MENU et on lance le jeu
                        pass