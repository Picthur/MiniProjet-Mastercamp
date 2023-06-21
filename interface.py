# interface graphique pour le projet Mastercamp

import pygame
from FonctionInterface import *
from gameAction import *

pygame.init()

win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Mastercamp")
win.fill((242, 251, 255))


def drawMapZone():
    pygame.draw.rect(win, (0, 0, 0), (80, 20, 1020, 1020), 5, border_radius=10)


def drawInfosZone(player):
    pygame.draw.rect(win, (0, 0, 0), (1180, 20, 700, 1020), 5, border_radius=10)

    TitleImg = pygame.image.load("./assets/TitleGame.png")
    TitleImg = pygame.transform.scale(TitleImg, (600, 180))
    win.blit(TitleImg, (1230, 35))

    font = pygame.font.Font('freesansbold.ttf', 32)
    PlayerText = font.render('Joueur :', True, (0, 0, 0))
    win.blit(PlayerText, (1230, 20 + 15 + 180 + 50))

    PlayerPAtext = font.render('Nbr de tour :', True, (0, 0, 0))
    win.blit(PlayerPAtext, (1230, 20 + 15 + 180 + 50 + 50))

    if player.name == "Lucas": #TODO: changer la couleur en fonction de l'ID du joueur
        PlayerName = font.render(player.name, True, (224, 90, 12))
        PlayerPA = font.render(str(player.PA), True, (224, 90, 12))
    else:
        PlayerName = font.render(player.name, True, (97, 143, 255))
        PlayerPA = font.render(str(player.PA), True, (97, 143, 255))

    PlayerName = pygame.transform.scale(PlayerName, (80, 40))
    
    pygame.draw.rect(win, (242, 251, 255), (1230 + 150, 20 + 15 + 180 + 50, 80, 40)) #Affiche un rectangle blanc pour cacher le nom du joueur précédent
    win.blit(PlayerName, (1230 + 150, 20 + 15 + 180 + 45))
    
    PlayerPA = pygame.transform.scale(PlayerPA, (25, 30))
    win.blit(PlayerPA, (1445, 20 + 15 + 180 + 45 + 58))


def drawShips():
    #Affichier les bateaux du joueur dans l'ordre de taille

    #Afficher les bateaux du joueur 1
    for ship in p1.ships:
        ShipImg = pygame.image.load("./assets/ShipH.png")
        ShipImg = pygame.transform.scale(ShipImg, (ship.size * 40, 40))

def drawWeapon():
    Weapon1Icon = pygame.image.load("./assets/Weapon1.png")
    Weapon1Icon = pygame.transform.scale(Weapon1Icon, (80, 80))
    win.blit(Weapon1Icon, (1628, 675))

    Weapon2Icon = pygame.image.load("./assets/Weapon2.png")
    Weapon2Icon = pygame.transform.scale(Weapon2Icon, (80, 80))
    win.blit(Weapon2Icon, (1628, 775))

    TirerIcon = pygame.image.load("./assets/TirerIcon.png")
    TirerIcon = pygame.transform.scale(TirerIcon, (80, 80))
    win.blit(TirerIcon, (1630, 875))


def drawAll(player):
    drawInfosZone(player)
    drawMapZone()
    drawMap(win, m, size, p1, p2)
    drawWeapon()


size = 41
m, p1, p2 = loadGame(size)
m.displayMap()

running = True
turn = 0
player = whoPlays(turn, p1, p2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    
    drawAll(player)
    action = chooseAction(win, m, player)

    pygame.display.update()

    if player.PA <= 0:
        turn += 1
        player = whoPlays(turn, p1, p2)
        player.PA = 5

pygame.quit()

