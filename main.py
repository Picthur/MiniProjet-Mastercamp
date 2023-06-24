from gameAction import *
from game import *

def play():

    (map,p1,p2) = loadGame()

    gameContinue = True
    turn = 0
    

    while(gameContinue):

        #Défini quel joueur doit jouer en fonction du tour auquel on est (1 sur 2)
        player, player2 = whoPlays(turn,p1,p2)
        print("Tour de {}\n".format(player.name))

        player.set_PA(5)
        #Demande au joueur de choisir une action tant qu'il le peut (PA > 0)
        while(player.PA > 0):
            map.displayMap()
            print("PA disponibles {}".format(player.PA))
            selectAction(map, player, player2)    

        #Passe au tour suivant
        turn += 1


play()