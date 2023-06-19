# fichier comprenant les fonctions de l'interface

import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame.event import get
from pygame.mouse import get_pos, get_pressed
from map import *
from base import *
from ship import *
from placement import *
from game import *
from player import *
pygame.init()

# def drawShips(win, ships, square_size, margin, space_size):
#     for ship in ships:
#         if ship.direction == 'N':
#             BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
#             BoatImg = pygame.transform.scale(BoatImg, (40, (square_size + space_size)*ship.size))

#             x = 80 + margin + ship.col * (square_size + space_size)
#             y = 20 + margin + ship.row * (square_size + space_size)

#             pygame.draw.rect(win, (0, 71, 255), (x, y, 4, 4))
#         # elif ship.direction == 'E':
#         #     BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
#         #     BoatImg = pygame.transform.scale(BoatImg, (50, 100))
#         #     BoatImg = pygame.transform.rotate(BoatImg, -90)

#         #     x = 80 + margin + space_size + ship.col * (square_size + space_size)
#         #     y = 20 + margin + space_size + ship.row * (square_size + space_size)

#         # elif ship.direction == 'W':
#         #     BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
#         #     BoatImg = pygame.transform.scale(BoatImg, (30, 100))
#         #     BoatImg = pygame.transform.rotate(BoatImg, 90)

#         #     x = 80 + margin + space_size + ship.col * (square_size + space_size)
#         #     y = 20 + margin + space_size + ship.row * (square_size + space_size)

#         # elif ship.direction == 'S':
#         #     BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
#         #     BoatImg = pygame.transform.scale(BoatImg, (50, 100))
#         #     BoatImg = pygame.transform.rotate(BoatImg, 180)

#         #     x = 80 + margin + space_size + ship.col * (square_size + space_size)
#         #     y = 20 + margin + space_size + ship.row * (square_size + space_size)

#         # Draw the ship image on the window
#             win.blit(BoatImg, (x, y))


def drawShips(win, ships, square_size, margin, space_size):
    # Parcourir chaque bateau dans la liste
    for ship in ships:
        if ship.direction == 'S':
            BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
            BoatImg = pygame.transform.scale(BoatImg, (square_size, (square_size + space_size) * ship.size))
            BoatImg = pygame.transform.rotate(BoatImg, 180)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)
        elif ship.direction == 'E':
            BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
            BoatImg = pygame.transform.scale(BoatImg, (square_size, (square_size + space_size) * ship.size))
            BoatImg = pygame.transform.rotate(BoatImg, -90)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)
        elif ship.direction == 'W':
            BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
            BoatImg = pygame.transform.scale(BoatImg, (square_size, (square_size + space_size) * ship.size))
            BoatImg = pygame.transform.rotate(BoatImg, 90)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + (ship.col + 1 - ship.size) * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)
        elif ship.direction == 'N':
            BoatImg = pygame.image.load("./assets/shipsImg/S1_" + str(ship.size) + ".png")
            BoatImg = pygame.transform.scale(BoatImg, (square_size, (square_size + space_size) * ship.size))
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + (ship.row + 1 - ship.size) * (square_size + space_size)

        # Dessiner le bateau à sa position calculée
        win.blit(BoatImg, (x, y))



            

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
            elif cell_value == "* ":
                pygame.draw.rect(win, (12, 171, 232), square_rect)
            else:
                pygame.draw.rect(win, (12, 171, 232), square_rect)
                drawShips(win, m1.ships, square_size, margin, space_size)


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
