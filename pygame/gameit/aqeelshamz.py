# Treasure Hunt
# Created by aqeelshamz

# Will you be able to find the treasure?

# How to play:
# * Use keyboard arrow keys to move the circle
# * Try not to hit the blocks
# * Play the game and grab the treasure

import pygame

def treasureHunt():
    pygame.init()
    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Treasure Hunt by aqeelshamz")

    x = 25
    y = 25

    width = 20
    height = 20

    speed = 2

    run = True

    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= speed

        if keys[pygame.K_RIGHT] and x < 500 - width:
            x += speed

        if keys[pygame.K_UP] and y > 0:
            y -= speed

        if keys[pygame.K_DOWN] and y < 500 - height:
            y += speed

        win.fill((0, 0, 0))

        pygame.draw.circle(win, (0, 237, 138), [x, y], width, 2)
        pygame.draw.rect(win, (97, 97, 97), (80, 0, 50, 270))
        pygame.draw.rect(win, (97, 97, 97), (200, 250, 50, 270))
        pygame.draw.rect(win, (97, 97, 97), (300, 0, 50, 200))
        pygame.draw.rect(win, (97, 97, 97), (400, 300, 50, 200))

        pygame.draw.rect(win, (237, 213, 0), (390, 5, 80, 80))

        if x >= 390 and x <= 390 + 80 and y >= 5 and y <= 5 + 80:
            print("Treasure found! 🪙")
            pygame.quit()

        if (
            (x >= 80 and x <= 80 + 50 and y >= 0 and y <= 0 + 270)
            or (x >= 200 and x <= 200 + 50 and y >= 250 and y <= 250 + 270)
            or (x >= 300 and x <= 300 + 50 and y >= 0 and y <= 0 + 200)
            or (x >= 400 and x <= 400 + 50 and y >= 300 and y <= 300 + 200)
        ):
            print("Game Over 🥲")
            pygame.quit()

        pygame.display.update()

    pygame.quit()
