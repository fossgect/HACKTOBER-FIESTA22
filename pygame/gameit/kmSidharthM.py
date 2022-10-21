import pygame
import time
import random
import math
from pygame import  K_ESCAPE, K_RETURN, mixer

def Space_Invader():
    pygame.init()


    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption('SPACE INVADER')
    # icon=pygame.image.load('static/spaceship.png')
    # pygame.display.set_icon(icon) 
    gameState=True
    value=random.randint(23,28)
    while(gameState):

        #player details
        playerimg=pygame.image.load('static/player.png')
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
            enemyimg.append(pygame.image.load('static/enemy.png'))
            enemyx.append(random.randint(0,436))
            enemyy.append(100)

        #bullet details
        bulletimg=pygame.image.load('static/bullet.png')
        bulletx=playerx
        bullety=430
        bulletchange=0.4
        bulletstate="ready"


        score=0
        font=pygame.font.Font('static/BebasNeue-Regular.ttf',22)
        scorex=10
        scorey=10


        #gameover text
        gm='GAME OVER'
        restart='Press Esc to continue'
        gmtext=pygame.font.Font('static/Golden Age Shad.ttf',64)
        restarttext=pygame.font.Font('static/Golden Age Shad.ttf',26)

        running=True
        collision=False
        background=pygame.image.load('static/background.png')
        

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
                            mixer.Sound('static/laser.wav').play()
                            bulletx=playerx 
                            bullet(bulletx,bullety)
                if(event.type==pygame.KEYUP):
                    playerchangex=0

            playerx+=playerchangex
            if(playerx>=436):
                playerx=436
            if(playerx<=0):
                playerx=0
            player(playerx,playery)
                        
            for i in range(2):
                enemyy[i]+=enemyspeed
                enemy(enemyx[i],enemyy[i],i) 
                collision=iscollision(enemyx[i]-16,enemyy[i]-16,bulletx-4,bullety-4)
                if collision:
                    mixer.Sound('static/explosion.wav').play()
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
            
            if(enemyy[0]>500 and enemyy[1]>500):
                    gameState=False
                    gmfuntion()
                    e=pygame.key.get_pressed()
                    if e[K_ESCAPE]:
                        running=False
                        gameState=True
        
            
            scoreval(scorex,scorey)
            pygame.display.update()
        

