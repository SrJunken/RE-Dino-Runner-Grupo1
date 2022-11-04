import pygame

from dino_runner.utils.constants import FONT_STYLE
from dino_runner.components import game

class You_win:

    def __init__(self):
        
        self.death_count = 0
        

    def add_death(self):

        self.death_count += 1

    def draw(self, screen):

        font = pygame.font.Font(FONT_STYLE, 17)
        text_death = font.render(f"Deaths: {self.death_count}", True, (255,0,0) )
        text_rect = text_death.get_rect()
        text_rect.center = (100 ,50)
        screen.blit(text_death, text_rect)
    
    def reset_death_count(self):
        self.death_count = 0
        