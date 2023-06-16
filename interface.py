# interface graphique pour le projet Mastercamp

import pygame
#importer les fonctions du fichier FonctionInterface.py
from FonctionInterface import *

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
def drawInfosZone():
    pygame.draw.rect(win, (0, 0, 0), (1180, 20, 700, 1020), 5, border_radius=10)

    #réuire la taille de l'image
    TitleImg = pygame.image.load("./assets/TitleGame.png")
    TitleImg = pygame.transform.scale(TitleImg, (600, 180))
    win.blit(TitleImg, (1230, 35))

    #Infos du jouer 
    font = pygame.font.Font('freesansbold.ttf', 32)
    PlayerText = font.render('Joueur :', True, (0, 0, 0))
    Name = "Léo"
    PlayerName = font.render(Name, True, (97, 143, 255))
    PlayerName = pygame.transform.scale(PlayerName, (80, 50)) 
    
    win.blit(PlayerText, (1230, 20+15+180+50))
    win.blit(PlayerName, (1370, 20+15+180+40))

    chooseAction()
    # Bouton Déplacer et Tirer (séparer les boutons de 80px et les centrer)
    DeplacerButton = pygame.image.load("./assets/DéplacerButton.png")
    DeplacerButton = pygame.transform.scale(DeplacerButton, (200, 70))
    win.blit(DeplacerButton, (1280, 375))

    TirerButton = pygame.image.load("./assets/TirerButton.png")
    TirerButton = pygame.transform.scale(TirerButton, (200, 70))
    win.blit(TirerButton, (1570, 375))

    #Icon des déplacements
    AvancerIcon = pygame.image.load("./assets/AvancerIcon.png")
    AvancerIcon = pygame.transform.scale(AvancerIcon, (80, 80))
    win.blit(AvancerIcon, (1340, 475))

    TournerIcon = pygame.image.load("./assets/TournerIcon.png")
    TournerIcon = pygame.transform.scale(TournerIcon, (80, 80))
    win.blit(TournerIcon, (1340, 575)) 

    ReculerIcon = pygame.image.load("./assets/ReculerIcon.png")
    ReculerIcon = pygame.transform.scale(ReculerIcon, (80, 80))
    win.blit(ReculerIcon, (1340, 675))

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




#Affichier les bateaux avec les images 
def drawBoat():
    BoaImg = pygame.image.load("./assets/shipsImg/S1_5.png")
    BoaImg = pygame.transform.scale(BoaImg, (50, 100))
    win.blit(BoaImg, (0, 0))

#Appeler les fonctions d'affichage
def drawAll():
    drawInfosZone()
    drawMapZone()
    drawBoat()


# Initialisation de la carte et des bases 
size = 31 # taille de la carte (chsoisir un nombre impair)
m1 = Map(size)
m1.createMap()
m1.initializeBase()
# m1.initializeShips()
m1.displayMap()

running = True # variable pour lancer le jeu

# Lancemenent du jeu (si echap, quitter le jeu)
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    
    drawAll()
    drawMap(win, m1, size)
    pygame.display.update()


