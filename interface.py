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


def playerName(i):
    # Couleurs utilisées
    BLACK = (0, 0, 0)

    win.fill((242, 251, 255))
    logo = pygame.image.load("./assets/TitleGame.png")
    logo = pygame.transform.scale(logo, (600, 180))
    win.blit(logo, (660, 20))
    
    # Police utilisée pour les textes
    font = pygame.font.Font(None, 32)

    # Variables pour stocker les noms entrés par le joueur
    name1 = ""

    # Boucle principale
    done = False
    clock = pygame.time.Clock()

    while not done:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Ajout des caractères entrés par le joueur à la variable correspondante
                if event.key == pygame.K_BACKSPACE:
                    name1 = name1[:-1]

                elif event.key == pygame.K_RETURN:
                    # Création des objets Player avec les noms entrés et fermeture de la fenêtre
                    player1 = Player(name1)
                    done = True
                else:
                    name1 += event.unicode
                
        # Textes et zones de saisie pour les noms
        x = 600
        y = 300
        message = f"Enter Player {i} Name:"
        text1 = font.render(message, True, BLACK)
        win.blit(text1, (x, y))

        # Zone de saisie pour le nom du joueur 1
        
        rect1 = pygame.Rect(x + 250, y-5, 140, 32)
        pygame.draw.rect(win, BLACK, rect1, 2)
        pygame.draw.rect(win, BLACK, rect1, 1)
        if player.get_id() == 1:
            text_surface1 = font.render(name1, True, (224, 90, 12))
        else:
            text_surface1 = font.render(name1, True, (97, 143, 255))
        win.blit(text_surface1, (rect1.x + 5, rect1.y + 5))

        pygame.display.flip()
        clock.tick(60)

    return player1

def initWindow():
    player1 = playerName(1)
    player2 = playerName(2)

   
    
    print("name1: ", player1.name + "dont l'id est: ", player1.get_id())
    print("name2: ", player2.name + "dont l'id est: ", player2.get_id())

    return player1.name, player2.name

def drawShips(player):
    #Affichier les bateaux du joueur alignés l'ordre de taille

    print("[main] player id: ", player.get_id())

    if player.get_id() == 1:
        boatName = "S1_"
    else:
        boatName = "S2_"

    for ship in player.ships:
        BoatImg_5 = pygame.image.load("./assets/shipsImg/" + boatName + "5.png")
        BoatImg_5 = pygame.transform.scale(BoatImg_5, (40, 200))

        BoatImg_4 = pygame.image.load("./assets/shipsImg/" + boatName + "4.png")
        BoatImg_4 = pygame.transform.scale(BoatImg_4, (40, 160))

        BoatImg_3 = pygame.image.load("./assets/shipsImg/" + boatName + "3.png")
        BoatImg_3 = pygame.transform.scale(BoatImg_3, (40, 120))

        BoatImg_2 = pygame.image.load("./assets/shipsImg/" + boatName + "2.png")
        BoatImg_2 = pygame.transform.scale(BoatImg_2, (40, 80))

        x = 1400
        y = 400
        win.blit(BoatImg_5, (x, y))
        win.blit(BoatImg_4, (x + 60, y + 200 - 160))
        win.blit(BoatImg_3, (x + 60 + 60, y + 200 - 120))
        win.blit(BoatImg_2, (x + 60 + 60 + 60, y + 200 - 80))


def drawMoveButton():
    AvancerIcon = pygame.image.load("./assets/AvancerIcon.png")
    AvancerIcon = pygame.transform.scale(AvancerIcon, (80, 80))
    win.blit(AvancerIcon, (1340, 675))

    TournerGaucheIcon = pygame.image.load("./assets/TournerGaucheIcon.png")
    TournerGaucheIcon = pygame.transform.scale(TournerGaucheIcon, (80, 80))
    win.blit(TournerGaucheIcon, (1290, 775))

    TournerDroiteIcon = pygame.image.load("./assets/TournerDroiteIcon.png")
    TournerDroiteIcon = pygame.transform.scale(TournerDroiteIcon, (80, 80))
    win.blit(TournerDroiteIcon, (1390, 775))

    ReculerIcon = pygame.image.load("./assets/ReculerIcon.png")
    ReculerIcon = pygame.transform.scale(ReculerIcon, (80, 80))
    win.blit(ReculerIcon, (1340, 875))


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

    if player.get_id() == 1:
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

    drawShips(player)  
    drawMoveButton()   


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
    win.fill((242, 251, 255))
    drawInfosZone(player)
    drawMapZone()
    drawMap(win, m, size, p1, p2)
    drawWeapon()

window_initialized = False

size = 21
m, p1, p2 = loadGame(size)
 #Attribution de leurs id
p1.set_id(1)
p2.set_id(2)

m.displayMap()

running = True
turn = 0
player = whoPlays(turn, p1, p2)

ship_selected = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if not window_initialized:
        print("init 1st time")
        p1.name, p2.name = initWindow()
        window_initialized = True
        print("init done")

    drawAll(player)
    
    if not ship_selected:
        selected_ship = selectShipClick(win, player)
        if selected_ship is not None:
            ship_selected = True

    # Choix de l'action
    if ship_selected:
        chooseActions(win, m, player, selected_ship)

    pygame.display.update()

    if player.PA <= 0:
        turn += 1
        player = whoPlays(turn, p1, p2)
        player.PA = 5
        ship_selected = False

    selectedShip = None  # Réinitialiser la valeur de selectedShip à chaque tour de boucle
    
pygame.quit()

