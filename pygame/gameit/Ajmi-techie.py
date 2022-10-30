import pygame
def racing_game():
    pygame.init() #initializes the Pygame
    from pygame import locals #import all modules from Pygame
    import random
    import math
    screen = pygame.display.set_mode((798,600))


    #changing title of the game window
    pygame.display.set_caption('Racing Beast')

    #changing the logo
    logo = pygame.image.load('car game/logo.jpeg')
    pygame.display.set_icon(logo)


    #defining our gameloop function

    def gameloop():

        #setting background image
        bg = pygame.image.load('car game/bg.png')

        
        # setting our player
        maincar = pygame.image.load('car game\car.png')
        maincarX = 350
        maincarY = 495
        maincarX_change = 0
        maincarY_change = 0

        #other cars
        car1 = pygame.image.load('car game\car1.jpeg')
        car1X = random.randint(178,490)
        car1Y = 100
        car1Ychange = 10

        car2 = pygame.image.load('car game\car2.png')
        car2X = random.randint(178,490)
        car2Y = 100
        car2Ychange = 10

        car3 = pygame.image.load('car game\car3.png')
        car3X = random.randint(178,490)
        car3Y = 100
        car3Ychange = 10
        
        


    
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                    #checking if any key has been pressed
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        maincarX_change += 5
                
                    if event.key == pygame.K_LEFT:
                        maincarX_change -= 5
                    
                    if event.key == pygame.K_UP:
                        maincarY_change -= 5
                        
                    if event.key == pygame.K_DOWN:
                        maincarY_change += 5

                    #checking if key has been lifted up
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_RIGHT:
                        maincarX_change = 0
                
                    if event.key == pygame.K_LEFT:
                        maincarX_change = 0
                    
                    if event.key == pygame.K_UP:
                        maincarY_change = 0
                        
                    if event.key == pygame.K_DOWN:
                        maincarY_change = 0            

            #setting boundary for our main car
            if maincarX < 178:
                maincarX = 178
            if maincarX > 490:
                maincarX = 490
            
            if maincarY < 0:
                maincarY = 0
            if maincarY > 495:
                maincarY = 495


            #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
            screen.fill((0,0,0))

            #displaying the background image
            screen.blit(bg,(0,0))

            #displaying our main car
            screen.blit(maincar,(maincarX,maincarY))

            #displaing other cars
            screen.blit(car1,(car1X,car1Y))
            screen.blit(car2,(car2X,car2Y))
            screen.blit(car3,(car3X,car3Y))
            
            #updating the values
            maincarX += maincarX_change
            maincarY +=maincarY_change

            #movement of the enemies
            car1Y += car1Ychange
            car2Y += car2Ychange
            car3Y += car3Ychange
            #moving enemies infinitely
            if car1Y > 670:
                car1Y = -100
            if car2Y > 670:
                car2Y = -150
            if car3Y > 670:
                car3Y = -200

            #DETECTING COLLISIONS BETWEEN THE CARS

            #getting distance between our main car and car1
            def iscollision(car1X,car1Y,maincarX,maincarY):
                distance = math.sqrt(math.pow(car1X-maincarX,2) + math.pow(car1Y - maincarY,2)) 

                #checking if distance is smaller than 50 after then collision will occur

                if distance < 50: 
                    return True
                else:
                    return False

            #getting distance between our main car and car2
            def iscollision(car2X,car2Y,maincarX,maincarY):
                distance = math.sqrt(math.pow(car2X-maincarX,2) + math.pow(car2Y - maincarY,2))

                #checking if distance is smaller than 50 after then collision will occur
                if distance < 50:
                    return True
                else:
                    return False

            #getting distance between our main car and car3
            def iscollision(car3X,car3Y,maincarX,maincarY):
                distance = math.sqrt(math.pow(car3X-maincarX,2) + math.pow(car3Y - maincarY,2))

                #checking if distance is smaller then 50 after then collision will occur
                if distance < 50:
                    return True
                else:
                    return False
            
            #giving collision a variable

            #collision between maincar and car1
            coll1 = iscollision(car1X,car1Y,maincarX,maincarY) 

            #collision between maincar and car2
            coll2 = iscollision(car2X,car2Y,maincarX,maincarY) 

            #collision between maincar and car3
            coll3 = iscollision(car3X,car3Y,maincarX,maincarY) 

            #if coll1 occur
            if coll1: 
                screen.fill((200,215,250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0
            
            #if coll2 occur
            if coll2:
                screen.fill((200,215,250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0

            #if coll3 occur    
            if coll3:
                screen.fill((200,215,250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0
            pygame.display.update()

    gameloop()