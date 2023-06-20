# interface graphique pour le projet Mastercamp

import pygame
#importer les fonctions du fichier FonctionInterface.py
from FonctionInterface import *
from gameAction import *

pygame.init()

# créer la fenetre du jeu de couleur 
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Mastercamp")
#changer la couleur de la fenetre
win.fill((242, 251, 255))


# zone de jeu (rectangle avec bord rond)
def drawMapZone():
    pygame.draw.rect(win, (0, 0, 0), (80, 20, 1020, 1020), 5, border_radius=10)
    

# zone d'action (rectangle à gauche)
def drawInfosZone(player):
    pygame.draw.rect(win, (0, 0, 0), (1180, 20, 700, 1020), 5, border_radius=10)

    #réuire la taille de l'image
    TitleImg = pygame.image.load("./assets/TitleGame.png")
    TitleImg = pygame.transform.scale(TitleImg, (600, 180))
    win.blit(TitleImg, (1230, 35))

    #Infos du jouer 
    font = pygame.font.Font('freesansbold.ttf', 32)
    PlayerText = font.render('Joueur :', True, (0, 0, 0))
    PlayerName = font.render(player.name, True, (97, 143, 255))
    PlayerName = pygame.transform.scale(PlayerName, (80, 40)) 
    win.blit(PlayerText, (1230, 20+15+180+50))
    win.blit(PlayerName, (1230+150, 20+15+180+45))

    PlayerPAtext = font.render('Nbr de tour :', True, (0, 0, 0))
    PlayerPA = font.render(str(player.PA), True, (97, 143, 255))
    PlayerPA = pygame.transform.scale(PlayerPA, (25, 30))
    win.blit(PlayerPAtext, (1230, 20+15+180+50+50))
    win.blit(PlayerPA, (1445, 20+15+180+45+58)) 
   
# def drawMoveButton():
#     #Icon des déplacements
#     AvancerIcon = pygame.image.load("./assets/AvancerIcon.png")
#     AvancerIcon = pygame.transform.scale(AvancerIcon, (80, 80))
#     win.blit(AvancerIcon, (1340, 475))

#     TournerIcon = pygame.image.load("./assets/TournerIcon.png")
#     TournerIcon = pygame.transform.scale(TournerIcon, (80, 80))
#     win.blit(TournerIcon, (1340, 575)) 

#     ReculerIcon = pygame.image.load("./assets/ReculerIcon.png")
#     ReculerIcon = pygame.transform.scale(ReculerIcon, (80, 80))
#     win.blit(ReculerIcon, (1340, 675))

    # if 1340 <= mouse1[0] <= 1420 and 475 <= mouse1[1] <= 555:
    #     if click1[0] == 1:
    #         print("Avancer")
    #         moveShip(map, player)
    #         pygame.display.update()
            
    # elif 1340 <= mouse1[0] <= 1420 and 575 <= mouse1[1] <= 655:
    #     if click1[0] == 1:
    #         print("Tourner")

    # elif 1340 <= mouse1[0] <= 1420 and 675 <= mouse1[1] <= 755:
    #     if click1[0] == 1:
    #         print("Reculer")
                


def drawWeapon():
    #Icon des tirs
    Weapon1Icon = pygame.image.load("./assets/Weapon1.png")
    Weapon1Icon = pygame.transform.scale(Weapon1Icon, (80, 80))
    win.blit(Weapon1Icon, (1628, 475))

    Weapon2Icon = pygame.image.load("./assets/Weapon2.png")
    Weapon2Icon = pygame.transform.scale(Weapon2Icon, (80, 80))
    win.blit(Weapon2Icon, (1628, 575))

    TirerIcon = pygame.image.load("./assets/TirerIcon.png")
    TirerIcon = pygame.transform.scale(TirerIcon, (80, 80))
    win.blit(TirerIcon, (1630, 675))


#Appeler les fonctions d'affichage
def drawAll(player):
    drawInfosZone(player)
    drawMapZone()
    drawMap(win, m, size)
    drawWeapon()


# Initialisation de la carte et des bases 
size = 31 # taille de la carte (chsoisir un nombre impair)
m,p1,p2 = loadGame(size)
m.displayMap()

running = True # variable pour lancer le jeu
turn = 0 # variable pour savoir à quel tour on est

# Lancemenent du jeu (si echap, quitter le jeu)
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    player = whoPlays(turn,p1,p2)
    player.set_PA(6)

    drawAll(player)
    pygame.display.update()

    #Demande au joueur de choisir une action tant qu'il le peut (PA > 0)

    # while(player.PA > 0):
    #     chooseAction(win, player)
    
    # pygame.display.update()            
            
    #Passe au tour suivant
    # turn += 1

    chooseAction(win, m, player)
    drawAll(player)
    pygame.display.update()


