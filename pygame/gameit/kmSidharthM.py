# Space Invader
# Created by Sidharth Murali

#  =>The aim of the game is to kill all the enemies coming towards space to attack using a spaceship.

# How to play the game:
#   ->  Use the arrow keys to move the spaceship left and right
#   ->  Press spacebar to fire.

# Points to be noted:
#   ->  At a time 2 enemies are spawned at random horizontal position and are headed downwards, 
#       killing one of them creates a new enemy. 
#   ->  Even if one of the enemy enters the space,preventing the other enemy to enter can take the 
#       game forward. Once both the enemies enters the space the game gets over with a score same 
#       as number of enemies killed.
#   ->  When score is at every multiple of 15 the downward velocity of the enemies increases thus increasing difficulty.
#   ->  Only 1 bullet at a time that is you will not be able to fire until the fired bullet leaves the game window


import pygame
import time
import random
import math
from pygame import  K_ESCAPE, K_RETURN, mixer

def Space_Invader():
    pygame.init()


    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption('SPACE INVADER')
    icon=pygame.image.load('static/kmSidharthM/spaceship.png')
    pygame.display.set_icon(icon) 
    gameState=True
    value=random.randint(23,28)
    while(gameState):

        #player details
        playerimg=pygame.image.load('static/kmSidharthM/player.png')
        playerx=218
        playery=430
        playerchangex=0

        #multiple enemy details
        enemyimg=[]
        enemyx=[]
        enemyy=[]
        noofEnemy=2
        enemyspeed=0.05
        for i in range(2):
            enemyimg.append(pygame.image.load('static/kmSidharthM/enemy.png'))
            enemyx.append(random.randint(0,436))
            enemyy.append(100)

        #bullet details
        bulletimg=pygame.image.load('static/kmSidharthM/bullet.png')
        bulletx=playerx
        bullety=430
        bulletchange=0.4
        bulletstate="ready"


        score=0
        font=pygame.font.Font('static/kmSidharthM/BebasNeue-Regular.ttf',22)
        scorex=10
        scorey=10


        #gameover text
        gm='GAME OVER'
        restart='Press Esc to continue'
        gmtext=pygame.font.Font('static/kmSidharthM/Golden Age Shad.ttf',64)
        restarttext=pygame.font.Font('static/kmSidharthM/Golden Age Shad.ttf',26)

        running=True
        collision=False
        background=pygame.image.load('static/kmSidharthM/background.png')
        

        #funtion to display player
        def player(x,y):
            screen.blit(playerimg,(x,y))

        #funtion to display enemy
        def enemy(x,y,i):
            screen.blit(enemyimg[i],(x,y))

        #funtion to display bullets
        def bullet(x,y):
            global bulletstate
            bulletstate="fire"
            screen.blit(bulletimg,(x+25,y))

        #funtion to check for collision
        def iscollision(enemyx,enemyy,bulletx,bullety):
            distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
            if distance<27:
                return True
            else:
                return False
            
        #funtion to display score
        def scoreval(x,y):
            scorevalue=font.render("score : "+str(score),True,(255,255,255))
            screen.blit(scorevalue,(x,y))

        #funtion to display game over
        def gmfuntion():
            text=gmtext.render(gm,True,(255,255,255))
            restart_text=restarttext.render(restart,True,(255,255,255))
            screen.blit(text,(47,205))
            screen.blit(restart_text,(80,275 ))
            

        
        while running:
            screen.fill((200,200,255))
            screen.blit(background,(0,0))

            #reads all pressed key and check for required 
            for event in pygame.event.get():                            
                if(event.type==pygame.QUIT):
                    running=False
                    gameState=False
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_LEFT):
                        playerchangex=-0.15
                    if(event.key==pygame.K_RIGHT):
                        playerchangex=0.15
                    if(event.key==pygame.K_SPACE):
                        if bulletstate == "ready":
                            mixer.Sound('static/kmSidharthM/laser.wav').play()
                            bulletx=playerx 
                            bullet(bulletx,bullety)
                if(event.type==pygame.KEYUP):
                    playerchangex=0

            #edits player position
            playerx+=playerchangex

            #checks for ends of game window
            if(playerx>=436):
                playerx=436
            if(playerx<=0):
                playerx=0
            player(playerx,playery)
                        
            for i in range(2):
                enemyy[i]+=enemyspeed
                enemy(enemyx[i],enemyy[i],i) 
                collision=iscollision(enemyx[i]-16,enemyy[i]-16,bulletx-4,bullety-4)
                if collision:                                                               #checks for collision                  
                    mixer.Sound('static/kmSidharthM/explosion.wav').play()
                    bullety=430
                    bulletstate="ready"
                    score+=1
                    enemyx[i]=random.randint(0,436)
                    enemyy[i]=0
                    if(score%15==0):
                        enemyspeed+=0.05
    
            if(bullety<0):
                bullety=playery
                bulletstate="ready"
            if bulletstate == "fire":
                bullet(bulletx,bullety)
                bullety-=bulletchange
            
            #checks whether both the enemies have entered the space
            if(enemyy[0]>500 and enemyy[1]>500):
                    gameState=False
                    gmfuntion()
                    e=pygame.key.get_pressed()
                    if e[K_ESCAPE]:
                        running=False
                        gameState=True
        
            
            scoreval(scorex,scorey)
            pygame.display.update()
        

