import pygame
from collide import *
from placement import *
from map import *
from player import *
from base import *
from ship import *

import random
    # Fonction pour faire baisser les PV du bateau attaqué en fonction des degats de l'arme attaquante
    # Si le bateau a plus de PV, il est détruit et enlever des class Player
def Attacked(s: Ship, w:Weapon):
    s.health -= w.damages
    if(s.health <= 0):
        del s

def coordShooting(s: Ship):
        coordX = 0
        coordY = 0
        match s.direction:
            case "N":
                coordX = s.row - (s.size-1)
                coordY = s.col
            case "E":
                coordX = s.row
                coordY = s.col + (s.size-1)
            case "S":
                coordX = s.row + (s.size-1)
                coordY = s.col
            case "O":
                coordX = s.row
                coordY = s.col - (s.size-1)
        return coordX, coordY
    
def find_ship_by_id(m: Map, id):
        for ship in m.ships:
            if ship.get_id()-1 == id:
                print(ship.id)
                return ship
        return None

def reconizeObject(m: map,coordX, coordY):
        Object = m.matrix[coordX][coordY]
        if(Object is int):
            return find_ship_by_id(m, Object)
        else: 
            return  None


    #FAIRE UNE FONCTION POUR RETROUVER UN BATEAU EN FONCTION DES COORDONNEES
def Shoot(s: Ship, w: Weapon, way, m: Map):
        coordX = coordShooting(s)[0]
        coordY = coordShooting(s)[1]
        #print(coordShooting(s)[0])

        match way:
            case "N":
                for i in range(w.range):
                    if(m.matrix[coordX - i][coordY] != "* "):
                        if(reconizeObject(m,coordX - i, coordY) != None):
                            Attacked(reconizeObject(m, coordX - i,coordY), w)
                            print("TOUCHE!")
                    else:
                        print("RATE!")
            case "E":
                for i in range(w.range):
                    if(m.matrix[coordX][coordY + i] != "* "):
                        if(reconizeObject(m, coordX, coordY + i) != None):
                            Attacked(reconizeObject(m, coordX,coordY + i), w)
                            print("TOUCHE!")
                    else:
                        print("RATE!")
            case "S":
                for i in range(w.range):
                    if(m.matrix[coordX + i][coordY] != "* "):
                        if(reconizeObject(m, coordX + i, coordY) != None):
                            Attacked(reconizeObject(m, coordX + i, coordY), w)
                            print("TOUCHE!")
                    else:
                        print("RATE!")
            case "O":
                for i in range(w.range):
                    if(m.matrix[coordX][coordY - i] != "* "):
                        if(reconizeObject(m, coordX, coordY - i) != None):
                            Attacked(reconizeObject(m, coordX, coordY - i), w)
                            print("TOUCHE!")
                    else:
                        print("RATE!")

m1 = Map(41)
m1.createMap()
m1.initializeShips()
w1 = Weapon(2, 2, 3, 5)
Shoot(find_ship_by_id(m1,2), w1, "N", m1)
