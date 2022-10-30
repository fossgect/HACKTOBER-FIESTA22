#Pygame of Halloween theme 
#Created by AnjanaPR

#Game Objective shoot the ghosts with garlic in the short duration to score points
#To shoot click the space bar
#____Happy Gaming and Halloween____

import math
import random

import pygame
from pygame import mixer

def Spooky_Halloween():
    # Intialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load('background.png')

    # Sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Spooky Halloween")
    icon = pygame.image.load('pumpkin.png')
    pygame.display.set_icon(icon)

    # player
    playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # ghost
    ghostImg = []
    ghostX = []
    ghostY = []
    ghostX_change = []
    ghostY_change = []
    num_of_enemies = 6

    for i in range(num_of_enemies):
        ghostImg.append(pygame.image.load('ghost.png'))
        ghostX.append(random.randint(0, 736))
        ghostY.append(random.randint(50, 100))
        ghostX_change.append(4)
        ghostY_change.append(40)

    # garlic
    # Fire - The garlic is currently moving

    garlicImg = pygame.image.load('garlic.png')
    garlicX = 0
    garlicY = 480
    garlicX_change = 0
    garlicY_change = 10
    garlic_state = "ready"

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    testY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def ghost(x, y, i):
        screen.blit(ghostImg[i], (x, y))


    def fire_garlic(x, y):
        global garlic_state
        garlic_state = "fire"
        screen.blit(garlicImg, (x + 16, y + 10))


    def isCollision(ghostX, ghostY, garlicX, garlicY):
        distance = math.sqrt(math.pow(ghostX - garlicX, 2) + (math.pow(ghostY - garlicY, 2)))
        if distance < 27:
            return True
        else:
            return False


    # Game Loop
    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if garlic_state is "ready":
                        garlicSound = mixer.Sound("laser.wav")
                        garlicSound.play()
                        # Get the current x cordinate of the spaceship
                        garlicX = playerX
                        fire_garlic(garlicX, garlicY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # ghost Movement
        for i in range(num_of_enemies):

            # Game Over
            if ghostY[i] > 440:
                for j in range(num_of_enemies):
                    ghostY[j] = 2000
                game_over_text()
                break

            ghostX[i] += ghostX_change[i]
            if ghostX[i] <= 0:
                ghostX_change[i] = 4
                ghostY[i] += ghostY_change[i]
            elif ghostX[i] >= 736:
                ghostX_change[i] = -4
                ghostY[i] += ghostY_change[i]

            # Collision
            collision = isCollision(ghostX[i], ghostY[i], garlicX, garlicY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                garlicY = 480
                garlic_state = "ready"
                score_value += 1
                ghostX[i] = random.randint(0, 736)
                ghostY[i] = random.randint(50, 150)

            ghost(ghostX[i], ghostY[i], i)

        # garlic Movement
        if garlicY <= 0:
            garlicY = 480
            garlic_state = "ready"

        if garlic_state is "fire":
            fire_garlic(garlicX, garlicY)
            garlicY -= garlicY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()

