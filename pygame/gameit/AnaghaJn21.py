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

