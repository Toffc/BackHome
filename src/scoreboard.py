import pygame.font
from src.game_stats import * 

class Scoreboard():
    def __init__(self, ai_settings, stats):
        self.screen = ai_settings.screen
        self.screen_rect = ai_settings.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_life()

    
    def prep_score(self):
        score_str = str(self.stats.score)
        score_str = "score:" + score_str
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def prep_life(self):
        self.images = []
        for i in range(self.stats.life):
            self.images.append(pygame.image.load("material/image/hero_life.png"))

        self.life_rect = self.images[0].get_rect()
        self.life_rect.right = self.screen_rect.right + 20
        self.life_rect.top = 540

    def show_life(self):
        now_rect = self.life_rect
        for i in range(self.stats.life):
            now_rect.right -= 50
            self.screen.blit(self.images[i], now_rect)
