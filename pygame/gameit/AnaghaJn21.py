
#Apple Shooting
#Created by Anagha Jayan


#Rules of the game:
#the objective of the game is to help the archer to shoot apples using his bow and arrows.
#Apple will be moving randomly..use right and left arrow key to move the hunter and use up arrow key to shoot an arrow
#if arrow hit the apple, score will be incremented 
#if any of apple reaches near archer game will be over

#importing libraries
import pygame
import random
import math
def AppleShooting():
    # initialize the app
    pygame.init()
    # set window size
    screen=pygame.display.set_mode((800,600))
    #set window title
    pygame.display.set_caption("apple shooting")
    #set window icon
    icon=pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    #archer
    playerimg=pygame.image.load('archer.png')
    #initial position of archer
    playerx=370
    playery=480
    playerxchange=0

    #apple
    enemyimg=[]
    enemyx=[]
    enemyy=[]
    enemyxchange=[]
    enemyychange=[]

    numofenemy=5
    i=0
    for i in range(numofenemy):
        enemyimg.append(pygame.image.load('apple.png'))
        enemyx.append(random.randint(0,735))
        enemyy.append(random.randint(50,150))
        enemyxchange.append(0.1)
        enemyychange.append(30)
    
    #arrow
    bulletimg=pygame.image.load('arrow.png')
    bulletx=0
    bullety=480
    bulletxchange=0
    bulletychange=0.5
    # arrowstate=Ready - You can't see the arrow on the screen
    # arrowstate=Fire - The arrow is currently moving
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

     #function to display archer
    def player(x,y):
        screen.blit(playerimg,(x,y))

    #function to display apple
    def enemy(x,y,i):
        screen.blit(enemyimg[i],(x,y))

     #function to show arrow
    def firebullet(x,y):
        global bulletstate
        bulletstate="fire"
        screen.blit(bulletimg,(x+16,y+10))


     #function to check wheather arrow hit an apple
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
                #if left arrow key is pressed archer move towards left
                if event.key==pygame.K_LEFT:
                    print("left")
                    playerxchange=-0.5
                #if right arrow key is pressed archer move towards right
                if event.key==pygame.K_RIGHT:
                    print("right")
                    playerxchange=0.5
                 #if up arrow key is pressed archer shoot an arrow
                if event.key==pygame.K_UP:
                    
                    if bulletstate=="ready":
                         #get the current x coordinate of the archer
                        bulletx=playerx
                        firebullet(bulletx,bullety)
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    print("keystrole has been released")
                    playerxchange=0
            
        
        playerx+=playerxchange
        
        #restricting movement of hunter outside of the game window
        if playerx<=0:
            playerx=0
        if playerx>=736:
            playerx=736

        #apple movement
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

             # arrow movement
        if bullety<=0:
            bullety=480
            bulletstate="ready"

        if bulletstate=="fire":
            firebullet(bulletx,bullety)
            bullety-=bulletychange

    
    
        player(playerx,playery)
        showscore(textx,texty)
        #apply changes
`       pygame.display.update()`
=======
import pygame
import random
import math
def AppleShooting():
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("apple shooting")
    icon=pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    playerimg=pygame.image.load('archer.png')
    playerx=370
    playery=480
    playerxchange=0


    enemyimg=[]
    enemyx=[]
    enemyy=[]
    enemyxchange=[]
    enemyychange=[]

    numofenemy=5
    i=0
    for i in range(numofenemy):
        enemyimg.append(pygame.image.load('apple.png'))
        enemyx.append(random.randint(0,735))
        enemyy.append(random.randint(50,150))
        enemyxchange.append(0.1)
        enemyychange.append(30)
    
    bulletimg=pygame.image.load('arrow.png')
    bulletx=0
    bullety=480
    bulletxchange=0
    bulletychange=0.5
    global bulletstate
    bulletstate="ready"


    score=0
    font=pygame.font.Font('freesansbold.ttf',32)
    textx=10
    texty=10

    overfont=pygame.font.Font('freesansbold.ttf',64)

    def showscore(x,y):
        scores=font.render("score :"+str(score),True,(255,255,255))
        screen.blit(scores,(x,y))

    def gameover():
        over=overfont.render("GAME OVER",True,(255,255,255))
        screen.blit(over,(200,250))


    def player(x,y):
        screen.blit(playerimg,(x,y))

    def enemy(x,y,i):
        screen.blit(enemyimg[i],(x,y))

    def firebullet(x,y):
        global bulletstate
        bulletstate="fire"
        screen.blit(bulletimg,(x+16,y+10))


    def collision(enemyx,enemyy,bulletx,bullety):
        distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
        if distance<27:
            return True
        else:
            return False

    running=True
    while running:
        screen.fill((0,0,0))
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    print("left")
                    playerxchange=-0.5
                if event.key==pygame.K_RIGHT:
                    print("right")
                    playerxchange=0.5
                if event.key==pygame.K_UP:
                    if bulletstate=="ready":
                        bulletx=playerx
                        firebullet(bulletx,bullety)
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    print("keystrole has been released")
                    playerxchange=0
            
        
        playerx+=playerxchange

        if playerx<=0:
            playerx=0
        if playerx>=736:
            playerx=736

    
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


            col=collision(enemyx[i],enemyy[i],bulletx,bullety)
            if col:
                bullety=480
                bulletstate="ready"
                score+=1
                print(score)
                enemyx[i]=random.randint(0,735)
                enemyy[i]=random.randint(50,150)

            enemy(enemyx[i],enemyy[i],i)

        if bullety<=0:
            bullety=480
            bulletstate="ready"

        if bulletstate=="fire":
            firebullet(bulletx,bullety)
            bullety-=bulletychange

    
    
        player(playerx,playery)
        showscore(textx,texty)
        pygame.display.update()
