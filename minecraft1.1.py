import pygame
import sys

pygame.init()

# Fenêtre
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("minecraft1.1")
clock = pygame.time.Clock()

# Couleurs
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joueur
x = 100
y = 100
largeur_joueur = 50
hauteur_joueur = 50
joueur_rect = pygame.Rect(x, y, largeur_joueur, hauteur_joueur)

velocity = 0
gravity = 0.5
jump_power = -10

# Sol
floor = 430

# Plateforme
plateforme_rect = pygame.Rect(200, 350, 200, 20)

# Vie et texte
vie = 5
police = pygame.font.Font(None, 40)
game_over_text = police.render("votre ,vie,game over", True, (255, 0, 0))

# Temps
start_time = pygame.time.get_ticks()
game_over = False

# Boucle principale
running = True
while running:
    # ---- Événements ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    # ---- Déplacement horizontal ----
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5

    # ---- Saut ----
    if keys[pygame.K_SPACE] and y >= floor:
        velocity = jump_power

    # ---- Physique ----
    velocity += gravity
    y += velocity

    # ---- Collision avec le sol ----
    if y >= floor:
        y = floor
        velocity = 0

    # ---- Mise à jour du rectangle du joueur ----
    joueur_rect.x = x
    joueur_rect.y = y

    # ---- Collision avec la plateforme ----
    if joueur_rect.colliderect(plateforme_rect):
        joueur_rect.bottom = plateforme_rect.top
        y = joueur_rect.y
        velocity = 0

    # ---- Gestion du temps / fin de partie ----
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 10000:  # 10 secondes
        vie -= 1
        start_time = current_time  # reset du compteur
        if vie <= 0:
            game_over = True
            running = False

    # ---- Affichage ----
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, joueur_rect)
    pygame.draw.rect(screen, BLACK, plateforme_rect)

    # Afficher texte game over si mort
    if game_over:
        screen.blit(game_over_text, (220, 50))

    # Afficher vie
    vie_text = police.render(f"Vie: {vie}", True, (0,0,0))
    screen.blit(vie_text, (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

