# fichier comprenant les fonctions de l'interface

import pygame
import sys

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame.event import get
from pygame.mouse import get_pos, get_pressed
from ClassMap import *
from Classbase import *
from ClassShip import *
from placement import *
from Shooting import *
from ClassPlayer import *
from gameAction import *

pygame.init()

# Variables globales pour la gestion du délai
delay = 200  # Délai en millisecondes
last_update = pygame.time.get_ticks()  # Temps du dernier déplacement de la roquette

global getSelectWeapon

def drawShips(win, square_size, margin, space_size, player):
    if player.get_id() == 1:
        boatName = "S1_"
    else:
        boatName = "S2_"
    
    # Parcourir chaque bateau dans la liste
    for ship in player.ship:
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
            else :
                pygame.draw.rect(win, (242, 251, 255), (x-space_size, y-space_size, square_size+2*space_size, square_size+2*space_size))
                pygame.draw.rect(win, (12, 171, 232), square_rect)

    for row in range(size):
        for col in range(size):
            # Récupérer la valeur de la case dans la matrice map
            cell_value = m1.matrix[row][col]

            if cell_value != "B1" and cell_value != "B2" and cell_value != "* ":
                drawShips(win, square_size, margin, space_size, p1)
                drawShips(win, square_size, margin, space_size, p2)
    

def shootRocket(win, m, selectedShip, shipAttacked, weapon_selected):
    MapZoneSize = 1020

    # Calcul des dimensions des carrés et de l'espace entre eux
    space_size = 2
    square_size = (MapZoneSize - (m.size - 1) * space_size) // m.size # square_size correspond à la taille d'un carré en pixel 
    margin = (MapZoneSize - (square_size+space_size)*m.size)//2 # margin correspond à la marge entre le bord de la fenêtre et le carré

    waitTime = 300
    
    if weapon_selected == 0:
        rocketImg = pygame.image.load("./assets/Weapon1.png")
    elif weapon_selected == 1:
        rocketImg = pygame.image.load("./assets/Weapon2.png")

    print("selectedShip.direction = ", selectedShip.direction)
    print("weapon_selected = ", weapon_selected)
    print()
    
    if selectedShip is not None and shipAttacked is not None:
        rocketImg = pygame.transform.scale(rocketImg, (square_size+square_size/3, square_size + space_size * 2))

        if selectedShip.direction == 'S':
            rocketImg = pygame.transform.rotate(rocketImg, 180)
            x = 80 + margin + space_size + selectedShip.col * (square_size + space_size)
            y = 20 + margin + space_size + selectedShip.row * (square_size + space_size) + (square_size + space_size) * selectedShip.size

            rangeRocket = shipAttacked.row - selectedShip.row - selectedShip.size
            
            # Déplacer la roquette jusuq'à la case du bateau attaqué
            for i in range(rangeRocket-1):
                # Effacer la roquette de la case précédente
                if y > 20 + margin + space_size + selectedShip.row * (square_size + space_size) + (square_size + space_size) * selectedShip.size:
                    prev_x = x
                    prev_y = y - (square_size + space_size)
                    pygame.draw.rect(win, (242, 251, 255), (prev_x-space_size, prev_y-space_size, square_size+2*space_size, square_size+2*space_size))
                    pygame.draw.rect(win, (12, 171, 232), (prev_x, prev_y, square_size, square_size))
                    pygame.display.update()

                y += square_size + space_size
                win.blit(rocketImg, (x, y))
                pygame.display.update()
                pygame.time.wait(waitTime)

        elif selectedShip.direction == 'E':
            rocketImg = pygame.transform.rotate(rocketImg, -90)
            x = 80 + margin + space_size + selectedShip.col * (square_size + space_size) + (square_size + space_size) * selectedShip.size
            y = 20 + margin + space_size + selectedShip.row * (square_size + space_size)

            rangeRocket = shipAttacked.col - selectedShip.col - selectedShip.size 

            # Déplacer la roquette jusuq'à la case du bateau attaqué
            for i in range(rangeRocket-1):
                # Effacer la roquette de la case précédente
                if x > 80 + margin + space_size + selectedShip.col * (square_size + space_size) + (square_size + space_size) * selectedShip.size:
                    prev_x = x - (square_size + space_size)
                    prev_y = y
                    pygame.draw.rect(win, (242, 251, 255), (prev_x-space_size, prev_y-space_size, square_size+2*space_size, square_size+2*space_size))
                    pygame.draw.rect(win, (12, 171, 232), (prev_x, prev_y, square_size, square_size))
                    pygame.display.update()
                
                # permet de faire une pause entre chaque déplacement de la roquette
                x += square_size + space_size
                win.blit(rocketImg, (x, y))
                pygame.display.update()
                pygame.time.wait(waitTime)

        elif selectedShip.direction == 'W':
            rocketImg = pygame.transform.rotate(rocketImg, 90)
            x = 80 + margin + space_size + (selectedShip.col - selectedShip.size) * (square_size + space_size) - square_size - space_size
            y = 20 + margin + space_size + selectedShip.row * (square_size + space_size)


            if shipAttacked.direction == 'N' or shipAttacked.direction == 'S':
                rangeRocket = selectedShip.col - shipAttacked.col - 1
            elif shipAttacked.direction == 'E' or shipAttacked.direction == 'W':
                rangeRocket = selectedShip.col - shipAttacked.col - shipAttacked.size

            # Déplacer la roquette jusuq'à la case du bateau attaqué            
            for i in range(rangeRocket-1):
                print("i = ", i)
                # Effacer la roquette de la case précédente
                if x > 80 + margin + space_size + selectedShip.col * (square_size + space_size) + (square_size + space_size) * selectedShip.size:
                    prev_x = x - (square_size + space_size)
                    prev_y = y
                    pygame.draw.rect(win, (242, 251, 255), (prev_x-space_size, prev_y-space_size, square_size+2*space_size, square_size+2*space_size))
                    pygame.draw.rect(win, (12, 171, 232), (prev_x, prev_y, square_size, square_size))
                    pygame.display.update()

                x -= square_size + space_size
                win.blit(rocketImg, (x, y))
                pygame.display.update()
                pygame.time.wait(waitTime)

        elif selectedShip.direction == 'N':
            x = 80 + margin + space_size + selectedShip.col * (square_size + space_size)
            y = 20 + margin + space_size + (selectedShip.row + 1 - selectedShip.size) * (square_size + space_size) - square_size - space_size

            # Déplacer la roquette jusuq'à la case du bateau attaqué

            if shipAttacked.direction == 'N' or shipAttacked.direction == 'S':
                rangeRocket = selectedShip.row - shipAttacked.row - shipAttacked.size
            elif shipAttacked.direction == 'E' or shipAttacked.direction == 'W':
                rangeRocket = selectedShip.row - shipAttacked.row - 1

            for i in range(rangeRocket-1):
                # Effacer la roquette de la case précédente
                if y > 20 + margin + space_size + selectedShip.row * (square_size + space_size) + (square_size + space_size) * selectedShip.size:
                    prev_x = x
                    prev_y = y - (square_size + space_size)
                    pygame.draw.rect(win, (242, 251, 255), (prev_x-space_size, prev_y-space_size, square_size+2*space_size, square_size+2*space_size))
                    pygame.draw.rect(win, (12, 171, 232), (prev_x, prev_y, square_size, square_size))
                    pygame.display.update()

                y -= square_size + space_size
                win.blit(rocketImg, (x, y))
                pygame.display.update()
                pygame.time.wait(waitTime)

        # Effacer la roquette de la case précédente
        prev_x = x
        prev_y = y
        pygame.draw.rect(win, (242, 251, 255), (prev_x-space_size, prev_y-space_size, square_size+2*space_size, square_size+2*space_size))
        pygame.draw.rect(win, (12, 171, 232), (prev_x, prev_y, square_size, square_size))
        pygame.display.update()


def selectShip(win, player):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    x = 1400
    y = 675
    
    if click[0] == 1:
        #Bouton 5
        if 1400 <= mouse[0] <= 1440 and 400 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 5
            print("Bateau de taille 5 sélectionné")
            for ship in player.ship:
                if ((ship.id-1) %4 == 3):
                    print(ship.id)
                    return ship
            
        #Bouton 4
        if 1460 <= mouse[0] <= 1500 and 440 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 4
            print("Bateau de taille 4 sélectionné")
            for ship in player.ship:
                if ((ship.id-1) %4 == 2):
                    print(ship.id)
                    return ship
            
        #Bouton 3
        if 1520 <= mouse[0] <= 1560 and 460 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 3
            print("Bateau de taille 3 sélectionné")
            for ship in player.ship:
                if ((ship.id-1) %4 == 1):
                    print(ship.id)
                    return ship

            
        #Bouton 2
        if 1580 <= mouse[0] <= 1620 and 520 <= mouse[1] <= 600:
            #retourner le bateau dont la taille est 2
            print("Bateau de taille 2 sélectionné")
            for ship in player.ship:
                if ((ship.id-1) %4 == 0):
                    print(ship.id)
                    return ship


weaponSelected = False

def selectWeaponClick(player):
    weaponSelected = False

    while not weaponSelected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                
                if click[0] == 1:
                    if 1628 <= mouse[0] <= 1710 and 775 <= mouse[1] <= 855:
                        
                            print("Weapon 1 selected")
                            weaponSelected = True
                            return player.weapon[0]
                    
                    if 1628 <= mouse[0] <= 1710 and 875 <= mouse[1] <= 955:
                            print("Weapon 2 selected")
                            weaponSelected = True
                            return player.weapon[1]
                



weapon_selected = False

def chooseActions(win, m, player, selectedShip, p1, p2, mouse, click):
    # mouse = pygame.mouse.get_pos()
    # click = pygame.mouse.get_pressed()

    opponentBase = "B" + str(player.id %2 +1)
    weapon_selected = False

    if click[0] == 1:
        #Bouton Avancé
        if 1340 <= mouse[0] <= 1420 and 675 <= mouse[1] <= 755:
            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                if(not willCollideForward(selectedShip,m, opponentBase)):
                    #Dans ce cas on avance
                    if(moveShipForward(selectedShip,m) == "victoire"):
                        return "victoire"
                    #Coûte un point d'action
                    player.set_action(player.action - 1)
                else:
                    print("Action impossible : collision")

                pygame.display.update()  # Mettre à jour l'affichage après avoir cliqué sur le bouton
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour avancer")

        #Bouton Tourner gauche
        if 1290 <= mouse[0] <= 1370 and 775 <= mouse[1] <= 855:
            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                nextShipDirection = rotateShipLeft(selectedShip)
                
                #Si la rotation ne pose pas de pb de collisions
                if(not willCollideRotation(selectedShip,nextShipDirection,m, opponentBase)):

                    #On efface l'emplacement du bateau
                    eraseShip(selectedShip,m.matrix)

                    #On change sa direction et on le replace
                    selectedShip.direction = nextShipDirection
                    if(placeShip(selectedShip,m.matrix) == "victoire"):
                        print(placeShip(selectedShip,m.matrix), "ICI")
                        return "victoire"

                    #Cout de rotation : 2 PA
                    player.set_action(player.action - 2)
                else:
                    print("Collision détectée")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour tourner")

        #Bouton Tourner droite
        if 1390 <= mouse[0] <= 1470 and 775 <= mouse[1] <= 855:
            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                nextShipDirection = rotateShipRight(selectedShip)
                
                #Si la rotation ne pose pas de pb de collisions
                if(not willCollideRotation(selectedShip,nextShipDirection,m, opponentBase)):

                    #On efface l'emplacement du bateau
                    eraseShip(selectedShip,m.matrix)

                    #On change sa direction et on le replace
                    selectedShip.direction = nextShipDirection
                    if(placeShip(selectedShip,m.matrix) == "victoire"):
                        print(placeShip(selectedShip,m.matrix), "ICI")
                        return "victoire"

                    #Cout de rotation : 2 PA
                    player.set_action(player.action - 2)
                else:
                    print("Collision détectée")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour tourner")


        #Bouton Reculer
        if 1340 <= mouse[0] <= 1420 and 875 <= mouse[1] <= 955:
            
            if selectedShip is not None:
                #afficher un rectagle blanc pour cacher le playerPA
                pygame.draw.rect(win, (242, 251, 255), (1445, 20+15+180+45+58, 25, 30))

                if(not willCollideBackward(selectedShip,m,opponentBase)):
                    if(moveShipBackward(selectedShip,m) == "victoire"):
                        return "victoire"
                    player.set_action(player.action - 1)
                else:
                    print("Action impossible : collision")

                pygame.display.update()
                selectedShip = None
            else:
                print("Aucun bateau sélectionné pour reculer")

        #Bouton Tirer
        if 1630 <= mouse[0] <= 1710 and 675 <= mouse[1] <= 755:
            if selectedShip is not None:
                print("tirer")

                if not weapon_selected:
                    w = selectWeaponClick(player)
                    if w is not None:
                        weapon_selected = True
                        
                if w is not None:
                    
                    shipAttacked = Shoot(selectedShip, w, m, p1, p2)

                    if shipAttacked is not None:
                        shootRocket(win, m, selectedShip, shipAttacked, w.id)

                        if(checkWinByOponentShip(m, p1)):
                            return "victoire"
                        player.set_action(player.action - 2)

                        pygame.display.update()
                        selectedShip = None
                    else:
                        print("Aucun bateau à attaquer")
                        
                        
            else:
                print("Aucun bateau sélectionné pour tirer")