import pygame

class CampSite:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.built = False
        self.type = None
        self.menu_active = False
        self.font = pygame.font.SysFont("Arial", 18)

    def interact(self):
        if not self.built:
            self.menu_active = True

    def handle_choice(self, choice):
        self.built = True
        self.type = choice
        self.menu_active = False
        print(f"Camp built as: {choice}")

    def update(self, keys):
        if self.menu_active:
            if keys[pygame.K_1]:
                self.handle_choice("defense")
            elif keys[pygame.K_2]:
                self.handle_choice("hunt")
            elif keys[pygame.K_3]:
                self.handle_choice("build")

    def draw(self, screen, camera_x):
        screen_x = self.rect.x - camera_x
        if not self.built:
            pygame.draw.rect(screen, (100, 80, 50), (screen_x, self.rect.y, self.rect.width, self.rect.height))
        else:
            color = {"defense": (180, 50, 50), "hunt": (50, 180, 50), "build": (50, 50, 180)}[self.type]
            pygame.draw.rect(screen, color, (screen_x, self.rect.y, self.rect.width, self.rect.height))

        if self.menu_active:
            self.draw_menu(screen)

    def draw_menu(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (200, 100, 400, 180))
        pygame.draw.rect(screen, (255, 255, 255), (200, 100, 400, 180), 2)

        choices = ["defense", "hunt", "build"]
        for i, c in enumerate(choices):
            pygame.draw.rect(screen, (100, 100, 100), (220, 120 + i * 50, 360, 40))
            text = self.font.render(f"{c.title()} Camp (press {i+1})", True, (255, 255, 255))
            screen.blit(text, (230, 130 + i * 50))

