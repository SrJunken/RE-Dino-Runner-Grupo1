import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


BIRD_HEIGHT = 68

class Birds (Obstacle):
    def __init__(self, images):
        type = 0
        print(images[type].get_height())
        super().__init__(images, type)
        if images[type].get_height() == BIRD_HEIGHT:
            position = random.randint(0,1)
            if position == 0:
                print("bird 325")
                self.rect.y = 325
            elif position == 1:
                print("bird 260")
                self.rect.y = 270



        self.index= 0


    def draw (self, screen):

        if self.index >= 9:
            self.index= 0
        screen.blit (self.images [self.index// 5], self.rect)
        self.index+= 1