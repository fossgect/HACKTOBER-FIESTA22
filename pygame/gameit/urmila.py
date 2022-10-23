import pygame
import random
import math
def HuntingBirds():
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Hunting Birds")
    icon=pygame.image.load('009-bow.png')
    pygame.display.set_icon(icon)
    hunterimg=pygame.image.load('huntergirl.png')
    hunterx=370
    huntery=480
    hunterxchange=0


    birdimg=[]
    birdx=[]
    birdy=[]
    birdxchange=[]
    birdychange=[]

    numofbird=5
    i=0
    for i in range(numofbird):
        birdimg.append(pygame.image.load('bird.png'))
        birdx.append(random.randint(0,735))
        birdy.append(random.randint(50,150))
        birdxchange.append(0.1)
        birdychange.append(30)
    
    arrowimg=pygame.image.load('arrow.png')
    arrowx=0
    arrowy=480
    arrowxchange=0
    arrowychange=0.5
    global arrowstate
    arrowstate="ready"


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


    def hunter(x,y):
        screen.blit(hunterimg,(x,y))

    def bird(x,y,i):
        screen.blit(birdimg[i],(x,y))

    def firearrow(x,y):
        global arrowstate
        arrowstate="fire"
        screen.blit(arrowimg,(x+16,y+10))


    def collision(birdx,birdy,bulletx,bullety):
        distance=math.sqrt((math.pow(birdx-arrowx,2))+(math.pow(birdy-arrowy,2)))
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
                    hunterxchange=-0.5
                if event.key==pygame.K_RIGHT:
                    hunterxchange=0.5
                if event.key==pygame.K_UP:
                    if arrowstate=="ready":
                        arrowx=hunterx
                        firearrow(arrowx,arrowy)
                        pygame.display.update()

                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    hunterxchange=0
            
        
        hunterx+=hunterxchange

        if hunterx<=0:
            hunterx=0
        if hunterx>=672:
            hunterx=672

    
        for i in range(numofbird):

            if birdy[i]>=440:
                for j in range(numofbird):
                    birdy[j]=2000
                gameover()
                break

            birdx[i]+=birdxchange[i]

            if birdx[i]<=0:
                birdxchange[i]=0.2
                birdy[i]+=birdychange[i]
            elif birdx[i]>=736:
                birdxchange[i]=-0.2
                birdy[i]+=birdychange[i]


            col=collision(birdx[i],birdy[i],arrowx,arrowy)
            if col:
                arrowy=480
                arrowstate="ready"
                score+=1
                birdx[i]=random.randint(0,735)
                birdy[i]=random.randint(50,150)

            bird(birdx[i],birdy[i],i)

        if arrowy<=0:
            arrowy=480
            arrowstate="ready"

        if arrowstate=="fire":
            firearrow(arrowx,arrowy)
            arrowy-=arrowychange

   
    
        hunter(hunterx,huntery)
        showscore(textx,texty)
        pygame.display.update()

