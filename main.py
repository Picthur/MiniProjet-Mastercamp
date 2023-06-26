# interface graphique pour le projet Mastercamp

import pygame

from Affichage import *
from InteractionPlayer import *
from gameAction import *
from ClassPlayer import *

window_initialized = False

def drawAll(player):
    win.fill((242, 251, 255))
    drawInfosZone(player)
    drawMapZone()
    drawMap(win, m, size, p1, p2)

size = 31
m, p1, p2 = loadGame(size)

#Attribution de leurs id
p1.set_id(1)
p2.set_id(2)
# print(p1.name + " dont l'id est: ", p1.get_id())
# print(p2.name + " dont l'id est: ", p2.get_id())

running = True
turn = 0
player = whoPlays(turn, p1, p2)

ship_selected = False
victoire = ''

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Initialisation de la fenêtre de jeu (choix des noms des joueurs)
    if not window_initialized:
        p1.name, p2.name = initWindow()
        window_initialized = True

    # Affichage de la fenêtre de jeu
    drawAll(player)
    
    # Passer le tour
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 1645 <= mouse[0] <= 1645 + 180 and 20 + 15 + 180 + 45 + 58 <= mouse[1] <= 20 + 15 + 180 + 45 + 58 + 40:
        if click[0] == 1:
            player.set_action(player.action - 5)

    # Déplacement du bateau
    if not ship_selected:
        # on selectionne un bateau
        selected_ship = selectShipClick(win, player)
        if selected_ship is not None:
            ship_selected = True

    # Choix de l'action
    if ship_selected:
        victoire = chooseActions(win, m, player, selected_ship, p1, p2, mouse, click)

    if victoire == "victoire":
        print("Fin de partie, victoire de " + player.name)
        running = False

    pygame.display.update()

    # Pemet de passer au joueur suivant
    if player.action <= 0 and victoire != "victoire":
        turn += 1
        player = whoPlays(turn, p1, p2)
        player.action = 5
        ship_selected = False

    selectedShip = None  # Réinitialiser la valeur de selectedShip à chaque tour de boucle

victoryRunning = True

if victoire == "victoire":
    while victoryRunning:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    victoryRunning = False

        victory(player)
        
pygame.quit()


#TODO:
# - faire en sorte que le joueur puisse choisir un weapon en cliquant dessus (pour l'instant c'est avec le terminale
# - faire mieux apparaitre le bateau sélectionné par le joueur (carré rouge autour)
# - faire un meilleur README
