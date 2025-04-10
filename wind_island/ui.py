import pygame

class UI:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.SysFont('Arial', 24)

    def draw(self, screen):
        coins_text = self.font.render(f'Coins: {self.player.coins}', True, (255, 255, 255))
        screen.blit(coins_text, (10, 10))
