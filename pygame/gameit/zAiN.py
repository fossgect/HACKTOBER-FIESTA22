#game "hallo"
#created by Zain
#Enjoy!!!!!


#it is a funny game in this halloween 
#the user have to kill all the pumpkins before gameover with the help of a ghost



#rules of game
#user can access the movements of ghost by left and right arrow keys
#user can shoot the pumpkin by using space key
#score will be displayed on the left top corner
#if any pumpkin reaches the ground the will end


#happy gaming
#all the best for the game


#importing library functions
import pygame
import random
import math
def hallo():
    #initialising step
    pygame.init()

    #setting screen
    screen=pygame.display.set_mode((800,600))

    

    #setting caption and icon 
    pygame.display.set_caption("hallo")
    icon=pygame.image.load('static/mimithamg/pumpkin.png')
    pygame.display.set_icon(icon)


    #setting player (ghost is our player)
    playerImg=pygame.image.load('ghost.png')

    
    playerImg=pygame.image.load('static/mimithamg/ghost.png')
    playerX=370
    playerY=480
    playerX_change =0


    #setting enemy(pumpkin is the enemy)
    enemyImg=[]
    enemyX=[]
    enemyY=[]
    enemyX_change =[]
    enemyY_change =[]
    num_of_enemies=6

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('static/mimithamg/pumpkin.png'))
        enemyX.append(random.randint(0,735))
        enemyY.append(random.randint(50,150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)




    #setting the shooting 
    bulletImg=pygame.image.load('fire.png')

    
    bulletImg=pygame.image.load('static/mimithamg/fire.png')

    bulletX= 0
    bulletY=480
    bulletX_change =0
    bulletY_change =.3
    

    #bulletstate=ready means you can not see bullet or fire
    #bullet state =Fire means fire currently moving
    global bullet_state
    bullet_state="ready"

    #score
    score_value=0
    font=pygame.font.Font('freesansbold.ttf',32)

    textX=10
    testY=10

    #game over
    over_font=pygame.font.Font('freesansbold.ttf',64)

    #function to display score

    def show_score(x,y):
        score=font.render("score:"+str(score_value),True,(255,255,255))
        screen.blit(score,(x,y))


    #function to display game over
    
    def game_over_text():
        over_text=over_font.render("GAME OVER",True,(255,255,255))
        screen.blit(over_text,(200,250))
    

    #function to display player
    def player(x,y):
     screen.blit(playerImg,(x,y))
    
    #function to display pumpkin
    def enemy(x,y,i):
     screen.blit(enemyImg[i],(x,y))
    
    #function to display fire or bullet
    def fire_bullet(x,y):
     global bullet_state
     bullet_state="fire"
     screen.blit(bulletImg,(x+16,y+10))
    

    #function to check whether collision happens
    def iscollision(enemyX,enemyY,bulletX,bulletY):
     distance= math.sqrt((math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2)))   
     if distance <27:
         return True
     else:
         return False


    #game loop     
    running=True
    while running:
       
       screen.fill((0,0,0))
       
      
       for event in pygame.event.get():
            if event.type==pygame.QUIT:
             running=False

            
            #if keystroke pressed 
            if event.type==pygame.KEYDOWN:

              #if left arrow pressed ghost move towards left
              if event.key==pygame.K_LEFT:
                playerX_change =-0.3

              #if right arrow pressed ghost move towards right
              if event.key==pygame.K_RIGHT:
                playerX_change =0.3


              #if space key pressed ghost shoot the fire  
              if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                  bulletX=playerX
                  fire_bullet(playerX,bulletY)

                
            if event.type==pygame.KEYUP:
              if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

                
       playerX+=playerX_change
       #restricting movement of ghost outside game window
       if playerX<=0:
           playerX =0
       elif playerX >= 736:
           playerX =736
        
       
       for i in range(num_of_enemies):
           
           if enemyY[i]>450:
               for j in range(num_of_enemies):
                   enemyY[j]=2000
               game_over_text()
               break

           
           enemyX[i]+=enemyX_change[i]

           if enemyX[i]<=0:
               enemyX_change[i]=0.3
               enemyY[i]+=enemyY_change[i]
           elif enemyX[i] >= 736:
               enemyX_change[i] =-0.3
               enemyY[i]+=enemyY_change[i]

           
           collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
           if collision:
               bulletY=480
               bullet_state="ready"
               score_value+=1
               print(score_value)
               enemyX[i]= random.randint(0,735)
               enemyY[i]=random.randint(50,150)
           enemy(enemyX[i],enemyY[i],i)

       
       if bulletY<=0:
           bulletY=480
           bullet_state="ready"
       if bullet_state is "fire":
           fire_bullet(bulletX,bulletY)
           bulletY -=bulletY_change

           
           
       player(playerX,playerY)
       show_score(textX,testY)

       #applying changes 
       pygame.display.update()

