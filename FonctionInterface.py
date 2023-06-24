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


def drawShips(win, square_size, margin, space_size, player):
    # print("[drawShips()] player id: ", player.get_id())

    if player.get_id() == 1:
        boatName = "S1_"
    else:
        boatName = "S2_"
    
    # Parcourir chaque bateau dans la liste
    for ship in player.ships:
        BoatImg = pygame.image.load("./assets/shipsImg/" + boatName + str(ship.size) + ".png")
        BoatImg = pygame.transform.scale(BoatImg, (square_size, (square_size + space_size) * ship.size))

        if ship.direction == 'S':
            BoatImg = pygame.transform.rotate(BoatImg, 180)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)

        elif ship.direction == 'E':
            BoatImg = pygame.transform.rotate(BoatImg, -90)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)

        elif ship.direction == 'W': 
            BoatImg = pygame.transform.rotate(BoatImg, 90)
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + (ship.col + 1 - ship.size) * (square_size + space_size)
            y = 20 + margin + space_size + ship.row * (square_size + space_size)

        elif ship.direction == 'N':
            # Calculer les coordonnées de dessin du bateau en fonction de sa position dans la matrice
            x = 80 + margin + space_size + ship.col * (square_size + space_size)
            y = 20 + margin + space_size + (ship.row + 1 - ship.size) * (square_size + space_size)

        # Dessiner le bateau à sa position calculée
        win.blit(BoatImg, (x, y))
            

def drawMap(win, m1, size, p1, p2):
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
                drawShips(win, square_size, margin, space_size, p1)
                drawShips(win, square_size, margin, space_size, p2)

def selectShipClick(win, player):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0] == 1:
        #Bouton 5
        if 1400 <= mouse[0] <= 1440 and 400 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 5
            print("Bateau de taille 2 sélectionné")
            return player.ships[3]
            
        #Bouton 4
        if 1460 <= mouse[0] <= 1500 and 440 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 4
            print("Bateau de taille 3 sélectionné")
            return player.ships[2]
            
        #Bouton 3
        if 1520 <= mouse[0] <= 1560 and 460 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 3
            print("Bateau de taille 4 sélectionné")
            return player.ships[1]
            
        #Bouton 2
        if 1580 <= mouse[0] <= 1620 and 520 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 2
            print("Bateau de taille 5 sélectionné")
            return player.ships[0]
        

def chooseActions(win, m, player, selectedShip):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    print("Bateau sélectionné : " + str(selectedShip.size) + "\n")

    #Bouton Avancé
    if 1340 <= mouse[0] <= 1420 and 675 <= mouse[1] <= 755:
        if click[0] == 1:
            if selectedShip is not None:
                print("Avancer")
            
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                if(not willCollideForward(selectedShip,m)):
                    #Dans ce cas on avance
                    moveShipForward(selectedShip,m)
                    #Coûte un point d'action
                    player.set_PA(player.PA - 2)
                else:
                    print("Action impossible : collision")

                pygame.display.update()  # Mettre à jour l'affichage après avoir cliqué sur le bouton
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour avancer")

    #Bouton Tourner gauche
    if 1290 <= mouse[0] <= 1370 and 775 <= mouse[1] <= 855:
        if click[0] == 1:
            print("Tourner gauche")
            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                nextShipDirection = rotateShipLeft(selectedShip)
                
                if(not willCollideRotation(selectedShip,nextShipDirection,m)):
                    eraseShip(selectedShip,m.matrix)

                    selectedShip.direction = nextShipDirection
                    placeShip(selectedShip,m.matrix)

                    player.set_PA(player.PA - 1)
                else:
                    print("Collision détectée")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour tourner")

    #Bouton Tourner droite
    if 1390 <= mouse[0] <= 1470 and 775 <= mouse[1] <= 855:
        if click[0] == 1:
            print("Tourner droite")

            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                nextShipDirection = rotateShipRight(selectedShip)
                
                if(not willCollideRotation(selectedShip,nextShipDirection,m)):
                    eraseShip(selectedShip,m.matrix)

                    selectedShip.direction = nextShipDirection
                    placeShip(selectedShip,m.matrix)

                    player.set_PA(player.PA - 1)
                else:
                    print("Collision détectée")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour tourner")


    #Bouton Reculer
    if 1340 <= mouse[0] <= 1420 and 875 <= mouse[1] <= 955:
        if click[0] == 1:
            print("Reculer")

            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                if(not willCollideBackward(selectedShip,m)):
                    moveShipBackward(selectedShip,m)
                    player.set_PA(player.PA - 2)
                else:
                    print("Action impossible : collision")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour reculer")
        

