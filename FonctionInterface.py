# fichier comprenant les fonctions de l'interface

import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame.event import get
from pygame.mouse import get_pos, get_pressed
from map import *
from base import *
pygame.init()


def drawMap(win, m1, size):
    MapZoneSize = 1020

    # Calcul des dimensions des carrés et de l'espace entre eux
    space_size = 2
    square_size = (MapZoneSize - (size - 1) * space_size) // size # square_size correspond à la taille d'un carré en pixel 
    margin = (MapZoneSize - (square_size+space_size)*size)//2 # margin correspond à la marge entre le bord de la fenêtre et le carré

    # Parcourir chaque position de la carte et dessiner les carrés
    for row in range(size):
        for col in range(size):
            # Calcul des coordonnées de dessin du carré
            x = 80 + margin + space_size + col * (square_size + space_size)
            y = 20 + margin + space_size + row * (square_size + space_size)
            square_rect = pygame.Rect(x, y, square_size, square_size)

            # Récupérer la valeur de la case dans la matrice map
            cell_value = m1.map[row][col]
            
            # Dessiner le carré avec la couleur appropriée en fonction de la valeur de la case
            if cell_value == "B1":
                pygame.draw.rect(win, (0, 71, 255), square_rect)
            elif cell_value == "B2":
                pygame.draw.rect(win, (255, 97, 97), square_rect)
            else:
                pygame.draw.rect(win, (12, 171, 232), square_rect)


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
