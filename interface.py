# interface graphique pour le projet Mastercamp

import pygame

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
    pygame.draw.rect(win, (0, 0, 0), (1920-750, 20, 700, 1020), 5, border_radius=10)

    #réuire la taille de l'image
    TitleImg = pygame.image.load("./assets/TitleGame.png")
    TitleImg = pygame.transform.scale(TitleImg, (600, 180))
    win.blit(TitleImg, (1920-750+50, 20+15))

    #Infos du jouer 
    font = pygame.font.Font('freesansbold.ttf', 32)
    PlayerText = font.render('Joueur :', True, (0, 0, 0))
    Name = "Léo"
    PlayerName = font.render(Name, True, (0, 0, 0))
    PlayerName = pygame.transform.scale(PlayerName, (80, 50)) 
    
    win.blit(PlayerText, (1920-750+50, 20+15+180+50))
    win.blit(PlayerName, (1920-750+50+150, 20+15+180+40))
    




#Affichier les bateaux avec les images 
def drawBoat():
    BoaImg = pygame.image.load("./assets/shipsImg/S1_5.png")
    BoaImg = pygame.transform.scale(BoaImg, (50, 100))
    win.blit(BoaImg, (0, 0))




# Lancemenent du jeu (si echap, quitter le jeu)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    drawMapZone()
    drawInfosZone()
    drawBoat()
    pygame.display.update()


