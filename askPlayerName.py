import pygame
from player import Player

pygame.init()

# Couleurs utilisées
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialisation de la fenêtre
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enregistrement de joueurs")

# Police utilisée pour les textes
font = pygame.font.Font(None, 32)

# Variables pour stocker les noms entrés par le joueur
name1 = ""
name2 = ""

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
                if name1_active:
                    name1 = name1[:-1]
                else:
                    name2 = name2[:-1]
            elif event.key == pygame.K_RETURN:
                # Création des objets Player avec les noms entrés et fermeture de la fenêtre
                player1 = Player(name1)
                player2 = Player(name2)
                done = True
            else:
                if name1_active:
                    name1 += event.unicode
                else:
                    name2 += event.unicode

    # Affichage des éléments de la fenêtre
    screen.fill(WHITE)

    # Textes et zones de saisie pour les noms
    text1 = font.render("Nom joueur 1 :", True, BLACK)
    screen.blit(text1, (50, 50))
    text2 = font.render("Nom joueur 2 :", True, BLACK)
    screen.blit(text2, (50, 100))

    # Zone de saisie pour le nom du joueur 1
    rect1 = pygame.Rect(200, 50, 200, 30)
    pygame.draw.rect(screen, BLACK, rect1, 2)
    if name1_active:
        pygame.draw.rect(screen, BLACK, rect1, 1)
    text_surface1 = font.render(name1, True, BLACK)
    screen.blit(text_surface1, (205, 55))

    # Zone de saisie pour le nom du joueur 2
    rect2 = pygame.Rect(200, 100, 200, 30)
    pygame.draw.rect(screen, BLACK, rect2, 2)
    if not name1_active:
        pygame.draw.rect(screen, BLACK, rect2, 1)
    text_surface2 = font.render(name2, True, BLACK)
    screen.blit(text_surface2, (205, 105))

    # Changement de la zone de saisie active lorsque l'utilisateur clique sur l'une d'entre elles
    mouse_pos = pygame.mouse.get_pos()
    if rect1.collidepoint(mouse_pos):
        name1_active = True
        name2_active = False
    elif rect2.collidepoint(mouse_pos):
        name1_active = False
        name2_active = True

    pygame.display.flip()
    clock.tick(60)
