# interface graphique pour le projet Mastercamp

import pygame

pygame.init()

# créer la fenetre du jeu de couleur 
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Mastercamp")

#changer la couleur de la fenetre
win.fill((242, 251, 255))

# zone de jeu (rectangle)

def drawMapZone():
    pygame.draw.rect(win, (255, 255, 255), (80, 20, 1020, 1020), 10)


# zone d'action (rectangle à gauche)

def drawInfosZone():
    pygame.draw.rect(win, (0, 255, 0), (1920-540, 20, 500, 1020), 10)

#Affichier les bateaux avec les images 

def drawBoat():
    image = pygame.image.load("./assets/shipsImg/S1_5.png")

    win.blit(image, (0, 0))




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


