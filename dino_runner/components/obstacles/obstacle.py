from turtle import width
from pygame.sprite import Sprite
from dino_runner.components import Obstacles
from dino_runner.utils.constants import SCREEN_WIDTH
GAME_SPEED=10
class Obstacle(Sprite):
    def __init__(self, images, type):
        self.images = images
        self.type = type
        self.rect = self.images[self.type].get_rect()
        self.rect.x= SCREEN_WIDTH
    def update(self, game_speed, obstacles):
        self.game_speed = GAME_SPEED        
        self.rect.x -= game_speed
        if self.rect.x <  -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
