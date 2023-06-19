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
        
        #Coordonnée du front du bateau
        coordX = coordShooting(s)[0]
        coordY = coordShooting(s)[1]

        #Match pour trouver la direction du tir
        i = 1
        match way:
            case "N":
                for i in range(w.range+1):
                    if(m.matrix[coordX - i][coordY] != "* "):
                        if(reconizeObject(m,coordX - i, coordY) != None):
                            print("TOUCHE!")
                            Attacked(reconizeObject(m, coordX - i,coordY), w)
                    else:
                        print("RATE!")
                    
            case "E":
                for i in range(w.range+1):
                    if(m.matrix[coordX][coordY + i] != "* "):
                        if(reconizeObject(m, coordX, coordY + i) != None):
                            print("TOUCHE!")
                            Attacked(reconizeObject(m, coordX,coordY + i), w)
                    else:
                        print("RATE!")
            case "S":
                for i in range(w.range+1):
                    if(m.matrix[coordX + i][coordY] != "* "):
                        if(reconizeObject(m, coordX + i, coordY) != None):
                            print("TOUCHE!")
                            Attacked(reconizeObject(m, coordX + i, coordY), w)
                    else:
                        print("RATE!")
            case "O":
                for i in range(w.range+1):
                    if(m.matrix[coordX][coordY - i] != "* "):
                        if(reconizeObject(m, coordX, coordY - i) != None):
                            print("TOUCHE!")
                            Attacked(reconizeObject(m, coordX, coordY - i), w)
                    else:
                        print("RATE!")

m1 = Map(20)
m1.createMap()
w1 = Weapon(2, 10, 10)
m1.initializeShips()
m1.displayMap()
Shoot(find_ship_by_id(m1,0), w1, "E", m1)
s1 = Ship
s1 = find_ship_by_id(m1,0)
print(s1.row)
print(s1.col)
print(coordShooting(s1)[0])
print(coordShooting(s1)[1])

#print("1 FINI\n")


