# fichier comprenant les fonctions de l'interface

import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame.event import get
from pygame.mouse import get_pos, get_pressed

pygame.init()

win = pygame.display.set_mode((1920, 1080))

def drawMap():
    # créer la fenetre du jeu de couleur
    size = 21

def chooseAction():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Bouton Déplacer
    if 1280 <= mouse[0] <= 1480 and 375 <= mouse[1] <= 445:
        if click[0] == 1:
            print("Déplacer")
    #Bouton Tirer
    if 1570 <= mouse[0] <= 1770 and 375 <= mouse[1] <= 445:
        if click[0] == 1:
            print("Tirer")
