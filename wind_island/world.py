import pygame
from settings import DAY_DURATION, NIGHT_DURATION

class World:
    def __init__(self):
        self.time = 0
        self.day = True
        self.overlay = pygame.Surface((800, 480))
        self.overlay.set_alpha(100)

    def update(self, dt):
        self.time += dt
        if self.day and self.time > DAY_DURATION:
            self.time = 0
            self.day = False
        elif not self.day and self.time > NIGHT_DURATION:
            self.time = 0
            self.day = True

    def draw(self, screen):
        if not self.day:
            self.overlay.fill((20, 20, 50))  # затемнение
            screen.blit(self.overlay, (0, 0))

