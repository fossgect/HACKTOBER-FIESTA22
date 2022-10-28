
import pygame

def upAndDown():
    pygame.init()
    win = pygame.display.set_mode((700, 500))

    pygame.display.set_caption("UpAndDown by Muhsin")

    x = 30 
    y = 500 

    width = 10             

    speed = 3         

    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_SPACE] and y > 0:  
            y -= speed

        if not keys[pygame.K_SPACE] and y < 495:
            y += speed

        if keys[pygame.K_RIGHT] and x < 700:
            x += speed

        if keys[pygame.K_LEFT] and x > 20:
            x -= speed

        win.fill((0, 0, 255))

        pygame.draw.circle(win, (255, 255, 0), [x, y], width, 2)
        pygame.draw.rect(win, (255, 0, 0), (0, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (70, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (140, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (210, 450, 40, 50))      
        pygame.draw.rect(win, (255, 0, 0), (280, 450, 80, 50))       
        pygame.draw.rect(win, (255, 0, 0), (400, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (470, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (550, 450, 40, 50))
        pygame.draw.rect(win, (255, 0, 0), (660, 450, 40, 50))

        if not keys[pygame.K_SPACE] and x >= 0 and x <= 40:
            y = 440

        if not keys[pygame.K_SPACE] and x >= 70 and x <= 110: 
            y = 440

        if not keys[pygame.K_SPACE] and x >= 140 and x <= 180: 
            y = 440
        
        if not keys[pygame.K_SPACE] and x >= 210 and x <= 250: 
            y = 440
        
        if not keys[pygame.K_SPACE] and x >= 280 and x <= 360: 
            y = 440

        if not keys[pygame.K_SPACE] and x >= 400 and x <= 440: 
            y = 440

        if not keys[pygame.K_SPACE] and x >= 470 and x <= 510: 
            y = 440

        if not keys[pygame.K_SPACE] and x >= 550 and x <= 590: 
            y = 440

        if not keys[pygame.K_SPACE] and x >= 660 and x <= 700: #? condition for character when it reached at the last block of the game
            y = 440
            print("You won the game !")
            pygame.quit()

        if y > 490: #? condition for character if doesnt't reach the last block or it fall from the block
            print("Game Over , Try Again!")
            pygame.quit()
        
        pygame.display.update()

    pygame.quit()

