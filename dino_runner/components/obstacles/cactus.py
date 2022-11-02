import random
from .obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, images):
        type = random.randint(0,5)

        super().__init__(images, type)
        print(images[type].get_height())
        if images[type].get_height() == 71:
            self.rect.y = 325

        if images[type].get_height() == 95:
            self.rect.y = 301
            
