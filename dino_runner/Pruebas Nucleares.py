
##Esto lo hice para saber el alto de un sprite
#from utils.constants import *
#from pygame import *
#print(LARGE_CACTUS[2].get_height())

import pygame

pygame.init()



win = pygame.display.set_mode((500, 500))

x = 250
y = 250
radius = 15
vel_x = 10
vel_y_subida = 10
vel_y_bajada= 10
jumping = False
air=0
stop_jumping_in_the_middle_of_the_air=False
run = True
while run:
    user_input = pygame.key.get_pressed()
    if air>=20:
        air=0
        print("el aire se ha reseteado a", air)
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Movement




    #Jump
    if user_input[pygame.K_UP]:
        jumping=True
    if user_input[pygame.K_UP]==False:
        jumping=False

    if jumping and not air >= 20:
        
        print("Input Up==True")
        y -= (vel_y_subida*4)
        vel_y_subida -= 1

        if vel_y_subida < -10:
            print("Velocidad reseteada")
            vel_y_subida = 10  
            jumping=False              
        else:
            air+=1
            print("el aire es", air)
    elif jumping==False and not stop_jumping_in_the_middle_of_the_air:
        if air<20 and air>0:
            stop_jumping_in_the_middle_of_the_air=True
            print("dejaste de saltar")

    if stop_jumping_in_the_middle_of_the_air and air>0:
        print("caida improvista")
        y += (vel_y_bajada*4)
        vel_y_bajada -=1
        if y >= 250:
            vel_y_bajada = 0
            print("velocidad de bajada seteada a 0")
            air=0
            print("aire seteado a 0", air)
            stop_jumping_in_the_middle_of_the_air=False
            print("parar de saltar en medio de el aire == Falso")
    if not stop_jumping_in_the_middle_of_the_air and not jumping:
        vel_x = 10
        vel_y_subida = 10
        vel_y_bajada= 10
        x = 250
        y = 250
            
#        elif y < 250 and air!=0:
#            print("velocidad reseteada a 10")
#            vel_y = 10
#            "d Caida==Falso"
#            stop_jumping_in_the_middle_of_the_air=False


    else:
        print("d")

  #  else:
        #print("")

    pygame.time.delay(30)
    pygame.display.update()