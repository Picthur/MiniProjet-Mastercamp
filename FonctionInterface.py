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
from gameAction import *

pygame.init()


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
            cell_value = m1.matrix[row][col]

            # Dessiner le carré avec la couleur appropriée en fonction de la valeur de la case
            if cell_value == "B1":
                # rectancgle bkanc autour du carré pour le mettre en valeur
                pygame.draw.rect(win, (242, 251, 255), (x-space_size, y-space_size, square_size+2*space_size, square_size+2*space_size))
                pygame.draw.rect(win, (0, 71, 255), square_rect)
            elif cell_value == "B2":
                pygame.draw.rect(win, (242, 251, 255), (x-space_size, y-space_size, square_size+2*space_size, square_size+2*space_size))
                pygame.draw.rect(win, (255, 97, 97), square_rect)
            elif cell_value == "* ":
                pygame.draw.rect(win, (242, 251, 255), (x-space_size, y-space_size, square_size+2*space_size, square_size+2*space_size))
                pygame.draw.rect(win, (12, 171, 232), square_rect)
            else:
                pygame.draw.rect(win, (242, 251, 255), (x-space_size, y-space_size, square_size+2*space_size, square_size+2*space_size))
                pygame.draw.rect(win, (12, 171, 232), square_rect)
                drawShips(win, m1.ships, square_size, margin, space_size)

def selectShip(win, player):
    print("##########")

    for ship in player.ships:
        print("Bateau n°", ship.id, ":", ship.size, "cases, en", ship.direction, "à la position (", ship.row, ",", ship.col, ")")

    print("##########")

def chooseAction(win, m, player):
    # DeplacerButton = pygame.image.load("./assets/DéplacerButton.png")
    # DeplacerButton = pygame.transform.scale(DeplacerButton, (200, 70))
    # win.blit(DeplacerButton, (1280, 375))

    # TirerButton = pygame.image.load("./assets/TirerButton.png")
    # TirerButton = pygame.transform.scale(TirerButton, (200, 70))
    # win.blit(TirerButton, (1570, 375))

    AvancerIcon = pygame.image.load("./assets/AvancerIcon.png")
    AvancerIcon = pygame.transform.scale(AvancerIcon, (80, 80))
    win.blit(AvancerIcon, (1340, 475))

    TournerIcon = pygame.image.load("./assets/TournerIcon.png")
    TournerIcon = pygame.transform.scale(TournerIcon, (80, 80))
    win.blit(TournerIcon, (1340, 575)) 

    ReculerIcon = pygame.image.load("./assets/ReculerIcon.png")
    ReculerIcon = pygame.transform.scale(ReculerIcon, (80, 80))
    win.blit(ReculerIcon, (1340, 675))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Bouton Avancé
    if 1340 <= mouse[0] <= 1420 and 475 <= mouse[1] <= 555:
        if click[0] == 1:
            print("Avancer")
            #afficher un rectagle blanc pour cacher le playerPA
            pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

            if(not willCollideForward(player.ships[0],m)):
                #Dans ce cas on avance
                moveShipForward(player.ships[0],m)
                #Coûte un point d'action
                player.set_PA(player.PA - 1)
            else:
                print("Action impossible : collision")

            pygame.display.update()  # Mettre à jour l'affichage après avoir cliqué sur le bouton

    #Bouton Tourner
    if 1340 <= mouse[0] <= 1420 and 575 <= mouse[1] <= 655:
        if click[0] == 1:
            print("Tourner")
            #afficher un rectagle blanc pour cacher le playerPA
            pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))
            player.set_PA(player.PA - 1)

            nextShipDirection = rotateShipLeft(player.ships[0])
            
            if(not willCollideRotation(player.ships[0],nextShipDirection,m)):

                eraseShip(player.ships[0],m.matrix)

                player.ships[0].direction = nextShipDirection
                placeShip(player.ships[0],m.matrix)

                player.set_PA(player.PA - 2)
            else:
                print("Collision détectée")

            pygame.display.update()

    #Bouton Reculer
    if 1340 <= mouse[0] <= 1420 and 675 <= mouse[1] <= 755:
        if click[0] == 1:
            print("Reculer")
            #afficher un rectagle blanc pour cacher le playerPA
            pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

            if(not willCollideBackward(player.ships[0],m)):
                moveShipBackward(player.ships[0],m)
                player.set_PA(player.PA - 1)
            else:
                print("Action impossible : collision")

            pygame.display.update()


