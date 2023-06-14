from map import *

m1 = Map(41)
m1.createMap()
m1.initializeBase()
m1.initializeShips()
m1.displayMap()

gameContinue = True

while(gameContinue):

    possibleShips = []
    for ship in m1.ships:
        possibleShips.append(str(ship.id))
    
    choice = input("Choisir un bateau ou exit\n")
    if(choice == "exit"):
        gameContinue = False
        break
    
    if(choice not in possibleShips):
        print("no ship")
    else:
        ship = m1.ships[int(choice) - 1]
        