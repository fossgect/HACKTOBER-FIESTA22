#Hunting Birds
#Created by Urmila T Anilan


#Rules of the game:
#the objective of the game is to help the hunter to hunt birds using her bow and arrows.
#Birds will be moving randomly..use right and left arrow key to move the hunter and use up arrow key to shoot an arrow
#if arrow hit the bird, score will be incremented 
#if any of birds reaches near hunter game will be over

#importing libraries
import pygame
import random
import math
def HuntingBirds():
    # initialize the app
    pygame.init()
    # set window size
    screen=pygame.display.set_mode((800,600))
    #set window title
    pygame.display.set_caption("Hunting Birds")
    #set window icon
    icon=pygame.image.load('009-bow.png')
    pygame.display.set_icon(icon)

    #hunter
    hunterimg=pygame.image.load('huntergirl.png')
    #initial position of hunter
    hunterx=370
    huntery=480
    hunterxchange=0


    #bird
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
    
    #arrow
    arrowimg=pygame.image.load('arrow.png')
    arrowx=0
    arrowy=480
    arrowxchange=0
    arrowychange=0.5

    # arrowstate=Ready - You can't see the arrow on the screen
    # arrowstate=Fire - The arrow is currently moving
    global arrowstate
    arrowstate="ready"

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

    #function to display hunter
    def hunter(x,y):
        screen.blit(hunterimg,(x,y))

    #function to display birds
    def bird(x,y,i):
        screen.blit(birdimg[i],(x,y))

    #function to show arrow
    def firearrow(x,y):
        global arrowstate
        arrowstate="fire"
        screen.blit(arrowimg,(x+16,y+10))

    #function to check wheather arrow hit a bird
    def collision(birdx,birdy,bulletx,bullety):
        distance=math.sqrt((math.pow(birdx-arrowx,2))+(math.pow(birdy-arrowy,2)))
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
                #if left arrow key is pressed hunter move towards left
                if event.key==pygame.K_LEFT:
                    hunterxchange=-0.5
                #if right arrow key is pressed hunter move towards right
                if event.key==pygame.K_RIGHT:
                    hunterxchange=0.5
                #if up arrow key is pressed hunter shoot an arrow
                if event.key==pygame.K_UP:
                    if arrowstate=="ready":
                        #get the current x coordinate of the hunter
                        arrowx=hunterx
                        firearrow(arrowx,arrowy)
                        pygame.display.update()

                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    hunterxchange=0
            
        
        hunterx+=hunterxchange
        #restricting movement of hunter outside of the game window
        if hunterx<=0:
            hunterx=0
        if hunterx>=672:
            hunterx=672

        #bird movement
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

            #collision
            col=collision(birdx[i],birdy[i],arrowx,arrowy)
            if col:
                arrowy=480
                arrowstate="ready"
                score+=1
                birdx[i]=random.randint(0,735)
                birdy[i]=random.randint(50,150)

            bird(birdx[i],birdy[i],i)

        # arrow movement
        if arrowy<=0:
            arrowy=480
            arrowstate="ready"

        if arrowstate=="fire":
            firearrow(arrowx,arrowy)
            arrowy-=arrowychange

   
    
        hunter(hunterx,huntery)
        showscore(textx,texty)
        #apply chandes
        pygame.display.update()
