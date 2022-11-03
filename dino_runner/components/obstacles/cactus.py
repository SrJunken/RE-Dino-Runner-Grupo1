import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from .obstacle import Obstacle

SMALL_CACTUS_HEIGHT = 71
LARGE_CACTUS_HEIGHT = 95
class Cactus(Obstacle):
    def __init__(self, images):
        type = random.randint(0,5)

        super().__init__(images, type)
        # print(images[type].get_height())
        if images[type].get_height() == SMALL_CACTUS_HEIGHT:
            self.rect.y = 325

        if images[type].get_height() == LARGE_CACTUS_HEIGHT:
            self.rect.y = 301

            
