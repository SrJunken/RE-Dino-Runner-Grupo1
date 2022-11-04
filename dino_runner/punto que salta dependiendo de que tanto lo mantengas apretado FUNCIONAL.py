
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
ducking= False
jumping = False
air=0
ducking_in_the_middle_of_the_air=False
stop_jumping_in_the_middle_of_the_air=False
run = True

while run:
    user_input = pygame.key.get_pressed()
    if air>=20:
        air=0
        print("el aire se ha reseteado a", air)
    win.fill((255, 0, 0))
    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    #ducking
    if user_input[pygame.K_DOWN]:
        ducking= True
        print("Agachandose")
    if user_input[pygame.K_DOWN]== False:
        ducking= False
    
    #jumping
    
    if user_input[pygame.K_UP] and ducking== False and air==0:
        jumping=True
    if user_input[pygame.K_UP]==False:
        jumping=False

    #que pasa si jumping

    if jumping and not air >= 20:
        
        print("Input Up==True")
        y -= (vel_y_subida*4)
        vel_y_subida -= 1

        if vel_y_subida < -10:
            y = 250
            print("Velocidad reseteada")
            vel_y_subida = 10  
            jumping=False              
        else:
            air+=1
            print("el aire es", air)
    
    #que pasa si no jumping en el medio del aire (si caida lenta o caida rapida)
    

    elif jumping==False and not stop_jumping_in_the_middle_of_the_air:
        if air<20 and air>0 and not ducking:
            stop_jumping_in_the_middle_of_the_air=True
            print("dejaste de saltar")         
        if air<20 and air>0 and ducking:
            ducking_in_the_middle_of_the_air=True
            print("te estas agachando en el medio del aire")

# exactamente qué pasa si caida rapida

    if ducking_in_the_middle_of_the_air and air >0:
        print("caida rapida")
        y += (vel_y_bajada*8)
        vel_y_bajada -=1
        if y >= 250:
            y=250
            vel_y_bajada = 0
            print("velocidad de bajada seteada a 0")
            air=0
            print("aire seteado a ", air)
            ducking_in_the_middle_of_the_air=False
            print("parar de saltar en medio de el aire == Falso")

#exactamente que pasas si caida lenta

    if stop_jumping_in_the_middle_of_the_air and air>0:
        print("caida improvista")
        y += (vel_y_bajada*4)
        vel_y_bajada -=1
        if y >= 250:
            y=250
            vel_y_bajada = 0
            print("velocidad de bajada seteada a 0")
            air=0
            print("aire seteado a ", air)
            stop_jumping_in_the_middle_of_the_air=False
            print("parar de saltar en medio de el aire == Falso")

#reseteo para que todo siga igual


    if not stop_jumping_in_the_middle_of_the_air and not jumping and not ducking and not ducking_in_the_middle_of_the_air:
        vel_x = 10
        vel_y_subida = 10
        vel_y_bajada= 10
        y = 250
        print("todo reseteado y finalizado")     

    else:
        print("")



    pygame.time.delay(30)
    pygame.display.update()