from collide import *
from placement import *
from map import *
from player import *
from base import *
from ship import *

import random
    # Fonction pour faire baisser les PV du bateau attaqué en fonction des degats de l'arme attaquante
    # Si le bateau a plus de PV, il est détruit et enlever des class Player
def Attacked(s: Ship, w:Weapon, m: list[Ship]):
    print(s.health)
    s.health -= w.damages
    print(s.health)
    if(s.health <= 0):
        #m.matrix[s.row][s.col] = "* "
        m.remove(s)
        Ship.nb -= 1
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

def reconizeObject(m: map,coordX: int, coordY: int):
        Object = m.matrix[coordX][coordY]
        if(Object[0] != "B"):
            return find_ship_by_id(m, int(Object[0]))
        else: 
            return  None


    #FAIRE UNE FONCTION POUR RETROUVER UN BATEAU EN FONCTION DES COORDONNEES
def Shoot(s: Ship, w: Weapon, way, m: Map):
        
        #Coordonnée du front du bateau
        coordX = coordShooting(s)[0]
        coordY = coordShooting(s)[1]

        match way:
            case "N":
                for i in range(w.range+1):
                    if(coordX - i >= 0):
                        if(m.matrix[coordX - (i+1)][coordY] != "* "):
                            ship = reconizeObject(m,coordX - (i+1), coordY)
                            if(ship != None):
                                print("TOUCHE!")
                                Attacked(ship, w, m.ships)
                                m1.displayMap()
                                break
                        else:
                            print("RATE!")
                    else:
                        print("fin du tir")
                        break
                    
            case "E":
                for i in range(w.range+1):
                    if(coordY + i+1 <= m.size-1):
                        if(m.matrix[coordX][coordY + (i+1)] != "* "):
                            ship = reconizeObject(m, coordX, coordY + (i+1))
                            if(ship != None):
                                print(f"TOUCHE! {s.id}")
                                Attacked(ship, w, m.matrix)
                                m1.displayMap()
                                break
                        else:
                            print("RATE!")
                    else:
                        print("fin du tir")
                        break
            case "S":
                for i in range(w.range+1):
                    if(coordX + i+1 <= m.size-1):
                        if(m.matrix[coordX + (i+1)][coordY] != "* "):
                            ship = reconizeObject(m, coordX + (i+1), coordY)
                            if(ship != None):
                                print(f"TOUCHE! {s.id}")
                                Attacked(ship, w, m.matrix)
                                m1.displayMap()
                                break
                        else:
                            print("RATE!")
                    else:
                        break
            case "O":
                for i in range(w.range+1):
                    if(coordY - i >= 0):
                        if(m.matrix[coordX][coordY - (i+1)] != "* "):
                            ship = reconizeObject(m, coordX, coordY - (i+1))
                            if(ship != None):
                                print(f"TOUCHE! {s.id}")
                                Attacked(ship, w, m.matrix)
                                m1.displayMap()
                                break
                        else:
                            print("RATE!")
                    else:
                        break

m1 = Map(20)
m1.createMap()
w1 = Weapon(10, 10, 20)
m1.initializeShips()
for element in m1.ships:
    print(element.id)
m1.displayMap()

Shoot(find_ship_by_id(m1,0), w1, "E", m1)
#m1.displayMap()
s1 = Ship
s1 = find_ship_by_id(m1,0)

for element in m1.ships:
    print(element.id)
#print(s1.row)
#print(s1.col)
#print(coordShooting(s1)[0])
#print(coordShooting(s1)[1])

#print("1 FINI\n")


