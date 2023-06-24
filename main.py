from gameAction import *

def play():

    (map,p1,p2) = loadGame(31)

    gameContinue = True
    turn = 0
    

    while(gameContinue):

        #Défini quel joueur doit jouer en fonction du tour auquel on est (1 sur 2)
        player = whoPlays(turn,p1,p2)
    
        player.set_PA(5)
        #Demande au joueur de choisir une action tant qu'il le peut (PA > 0)
        while(player.PA > 0):
            map.displayMap()
            print("Tour de {}\n".format(player.name))
            print("PA disponibles {}".format(player.PA))
            if selectAction(map, player) == "victoire":
                map.displayMap()
                gameContinue = False
                print("Fin de partie, victoire de " + player.name)
                break    

        #Passe au tour suivant
        turn += 1


play()