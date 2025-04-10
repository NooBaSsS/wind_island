import pygame
from player import Player
from campsite import CampSite
from ui import UI

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480
WORLD_WIDTH = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
background_image = pygame.image.load('.//assets//images//bg_test2.jpg')
bg_width = background_image.get_width()
bg_height = background_image.get_height()

player = Player(100, SCREEN_HEIGHT - 70)
camps = [CampSite(400, SCREEN_HEIGHT - 40), CampSite(900, SCREEN_HEIGHT - 40)]
ui = UI(player)

running = True
camp_cost = 1
camera_x = 0
camera_x_min = 0
camera_x_max = WORLD_WIDTH - SCREEN_WIDTH
parallax_factor = 0.5

population_total = 5
population_max = 10
population_used = 0

while running:
    dt = clock.tick(60) / 1000  # delta time
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(keys, dt, WORLD_WIDTH)

    # Интеракция с лагерем
    if keys[pygame.K_e]:
        for camp in camps:
            if player.rect.colliderect(camp.rect):
                camp.interact()
    
    elif keys[pygame.K_f]:
        player_x = player.rect.centerx
        
        overlap = any(abs(camp.rect.centerx - player_x) < 40 for camp in camps)
        if not overlap and player.coins >= camp_cost:
            new_camp = CampSite(player_x, SCREEN_HEIGHT - 40)
            camps.append(new_camp)
            player.coins -= camp_cost
    
    for camp in camps:
        camp.update(keys)

    # Камера следует за игроком
    camera_x = player.rect.centerx - SCREEN_WIDTH // 2
    if camera_x < 0:
        camera_x = 0

    # Рисуем

    bg_scroll_x = int(camera_x * parallax_factor)
    
    for i in range(-1, WORLD_WIDTH // bg_width + 2):
        screen.blit(background_image, (i * bg_width - bg_scroll_x % bg_width, SCREEN_HEIGHT - bg_height))

    for camp in camps:
        camp.draw(screen, camera_x)
    
    player.draw(screen, camera_x)
    ui.draw(screen)

    pygame.display.flip()

pygame.quit()

