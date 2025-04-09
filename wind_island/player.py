import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 48))
        self.image.fill((255, 255, 0))
        self.rect = pygame.Rect(x, y, 32, 48)
        self.speed = 200

    def update(self, keys, dt):
        if keys[pygame.K_LEFT]:
            self.rect.x -= int(self.speed * dt)
        if keys[pygame.K_RIGHT]:
            self.rect.x += int(self.speed * dt)

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))

