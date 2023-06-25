import pygame
from player import Player

pygame.init()

def playerName(i):
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
                
        # Affichage des éléments de la fenêtre
        screen.fill(WHITE)

        # Textes et zones de saisie pour les noms
        message = f"Enter Player {i} Name:"
        text1 = font.render(message, True, BLACK)
        screen.blit(text1, (50, 50))

        # Zone de saisie pour le nom du joueur 1
        rect1 = pygame.Rect(300, 50, 300, 30)
        pygame.draw.rect(screen, BLACK, rect1, 2)
        pygame.draw.rect(screen, BLACK, rect1, 1)
        text_surface1 = font.render(name1, True, BLACK)
        screen.blit(text_surface1, (305, 55))

        pygame.display.flip()
        clock.tick(60)

    return player1

