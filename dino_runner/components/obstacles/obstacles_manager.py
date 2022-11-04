import random
import pygame
from dino_runner.components.death_count import Death_count
from dino_runner.components.obstacles.bird import Birds
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, DEFAULT_TYPE, DIE_SOUND, HAMMER_TYPE, HAMMMMER_SOUND, SHIELD_SOUND, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS
from pygame import mixer


class ObstacleManager:
    def __init__ (self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            option = random.randint(0,2)
            if (option == 0):
                self.obstacles_list.append(Cactus(LARGE_CACTUS))
            elif (option == 1):
                self.obstacles_list.append(Cactus(SMALL_CACTUS))
            elif (option==2):
                print("bird")
                self.obstacles_list.append(Birds(BIRD))


        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)

            
            if game.player.dino_rect.colliderect(obstacle.rect) and game.player.type == DEFAULT_TYPE:
                DIE_SOUND.play()
                pygame.time.delay(500)
                game.playing = False
                break
            elif game.player.dino_rect.colliderect(obstacle.rect) and game.player.type == HAMMER_TYPE:
                mixer.music.set_volume(0.1)
                HAMMMMER_SOUND.play()
                self.obstacles_list.pop()
                mixer.music.set_volume(0.9)

                break
            elif game.player.dino_rect.colliderect(obstacle.rect) and game.player.type == SHIELD_TYPE:
                SHIELD_SOUND.play()



            

            



    def draw(self, game):
        for obstacle in self.obstacles_list:
            obstacle.draw(game.screen)

    def reset_obstacles(self):
        self.obstacles_list = []