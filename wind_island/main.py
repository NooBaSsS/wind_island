import pygame
from player import Player
from campsite import CampSite

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(100, SCREEN_HEIGHT - 70)
camps = [CampSite(400, SCREEN_HEIGHT - 40), CampSite(900, SCREEN_HEIGHT - 40)]

running = True
camera_x = 0

while running:
    dt = clock.tick(60) / 1000  # delta time
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(keys, dt)

    # Интеракция с лагерем
    if keys[pygame.K_e]:
        for camp in camps:
            if player.rect.colliderect(camp.rect):
                camp.interact()

    for camp in camps:
        camp.update(keys)

    # Камера следует за игроком
    camera_x = player.rect.centerx - SCREEN_WIDTH // 2
    if camera_x < 0:
        camera_x = 0

    # Рисуем
    screen.fill((100, 150, 200))  # фон
    for camp in camps:
        camp.draw(screen, camera_x)

    player.draw(screen, camera_x)

    pygame.display.flip()

pygame.quit()

