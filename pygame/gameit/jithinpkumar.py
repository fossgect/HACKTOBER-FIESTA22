#Killing Terrorists
#Created by Jithin P Kumar


#Rules of the game:
#the objective of the game is to help the soldier to kill terrorists using gun and bullet.
#Terrorists will be moving randomly..use right and left arrow key to move the soldier and use up arrow key to shoot a bullet
#if bullet hit the terrorist, score will be incremented 
#if any of terrorist reaches near soldier game will be over

#importing libraries
import pygame
import random
import math

def ArmyBase():
        # initialize the app
        pygame.init()
        # set window size
        screen=pygame.display.set_mode((800,600))
        #set window title
        pygame.display.set_caption("Army Base")
         #set window icon
        icon=pygame.image.load('003-sniper.png')
        pygame.display.set_icon(icon)

        #soldier
        playerimg=pygame.image.load('004-soldier.png')
        #initial position of hunter
        playerx=370
        playery=480
        playerxchange=0

        #terrorist
        enemyimg=[]
        enemyx=[]
        enemyy=[]
        enemyxchange=[]
        enemyychange=[]

        numofenemy=5
        i=0
        for i in range(numofenemy):
            enemyimg.append(pygame.image.load('terror.png'))
            enemyx.append(random.randint(0,735))
            enemyy.append(random.randint(50,150))
            enemyxchange.append(0.1)
            enemyychange.append(30)

        #bullet   
        bulletimg=pygame.image.load('bullet.png')
        bulletx=0
        bullety=480
        bulletxchange=0
        bulletychange=0.5

        # bulletstate=Ready - You can't see the bullet on the screen
        # bullettate=Fire - The bullet is currently moving
        global bulletstate
        bulletstate="ready"

        #score
        score=0
        font=pygame.font.Font('freesansbold.ttf',32)
        textx=10
        texty=10

        #Game over
        overfont=pygame.font.Font('freesansbold.ttf',64)

        #function to display score on screen
        def showscore(x,y):
            scores=font.render("score :"+str(score),True,(255,255,255))
            screen.blit(scores,(x,y))

        #fuction to display Game Over on screen
        def gameover():
            over=overfont.render("GAME OVER",True,(255,255,255))
            screen.blit(over,(200,250))

        #function to display soldier
        def player(x,y):
            screen.blit(playerimg,(x,y))

        #function to display terrorist
        def enemy(x,y,i):
            screen.blit(enemyimg[i],(x,y))

        #function to show bullet
        def firebullet(x,y):
            global bulletstate
            bulletstate="fire"
            screen.blit(bulletimg,(x+16,y+10))

        #function to check wheather bullet hit a terrorist
        def collision(enemyx,enemyy,bulletx,bullety):
            distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
            if distance<27:
                return True
            else:
                return False

        #Game loop
        running=True
        while running:
            screen.fill((0,0,0))
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False

                 #if keystroke is pressed check wheather its right,left or up
                if event.type==pygame.KEYDOWN:
                    #if left arrow key is pressed soldier move towards left
                    if event.key==pygame.K_LEFT:
                         playerxchange=-0.5
                    #if right arrow key is pressed soldier move towards right
                    if event.key==pygame.K_RIGHT:
                        
                        playerxchange=0.5
                    #if up arrow key is pressed soldier shoot an bullet
                    if event.key==pygame.K_UP:
                        if bulletstate=="ready":
                            #get the current x coordinate of the soldier
                            bulletx=playerx
                            firebullet(bulletx,bullety)
                       
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                      
                        playerxchange=0
                   
               
            playerx+=playerxchange
            #restricting movement of soldier outside of the game window
            if playerx<=0:
                playerx=0
            if playerx>=736:
                playerx=736

           #terrorist movement
            for i in range(numofenemy):

                if enemyy[i]>=440:
                    for j in range(numofenemy):
                        enemyy[j]=2000
                    gameover()
                    break

                enemyx[i]+=enemyxchange[i]

                if enemyx[i]<=0:
                    enemyxchange[i]=0.2
                    enemyy[i]+=enemyychange[i]
                elif enemyx[i]>=736:
                    enemyxchange[i]=-0.2
                    enemyy[i]+=enemyychange[i]

                #collision
                col=collision(enemyx[i],enemyy[i],bulletx,bullety)
                if col:
                    bullety=480
                    bulletstate="ready"
                    score+=1
                    print(score)
                    enemyx[i]=random.randint(0,735)
                    enemyy[i]=random.randint(50,150)

                enemy(enemyx[i],enemyy[i],i)

            # bullet movement
            if bullety<=0:
                bullety=480
                bulletstate="ready"

            if bulletstate=="fire":
                firebullet(bulletx,bullety)
                bullety-=bulletychange

           
           
            player(playerx,playery)
            showscore(textx,texty)
             #apply changes
            pygame.display.update()


