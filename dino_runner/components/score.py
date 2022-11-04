import pygame

from dino_runner.utils.constants import FONT_STYLE, HAMMER_TYPE, POINT_SOUND


class Score:
    x=254
    y=254
    z=254
    def __init__(self):
        self.score = 0
        self.x =254
        self.y =254
        self.z =254
    def update(self, game):
        self.score +=1
        if self.score % 100 == 0:
            POINT_SOUND.play()
            game.game_speed += 2


    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 17)
        text_component = font.render(f"Points: {self.score}", True, (0,255,0) )
        text_rect = text_component.get_rect()
        text_rect.center = (1000 ,50)
        screen.blit(text_component, text_rect)


    
    def reset_score(self):
        self.score = 0
    def turn_black_background(self, screen):
        self.screen = screen
        self.x-=15
        if self.x <= 4:
            self.x = 0
        self.y-=15
        if self.y <= 4:
            self.y = 0        
        self.z-=15
        if self.z <= 4:
            self.z = 0
        
        self.screen.fill((self.x, self.y, self.z))
    def turn_white_background(self,screen):
        self.screen = screen
        self.x+=15
        if self.x >= 230:
            self.x = 255
        self.y+=15
        if self.y >= 230:
            self.y = 255        
        self.z+=15
        if self.z >= 230:
            self.z = 255 

        self.screen.fill((self.x, self.y, self.z))  
            #def you_win_message(self,screen):
#        font = pygame.font.Font(FONT_STYLE, 30)
 #       text_component = font.render("Congratulations! You Win!", True, (0,255,0) )
  #      text_rect = text_component.get_rect()
   #     text_rect.center = (510 ,300)
    #    screen.blit(text_component, text_rect)
     #   self.player.type=HAMMER_TYPE