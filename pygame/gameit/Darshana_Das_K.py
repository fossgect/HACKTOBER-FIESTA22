#Snake game 
#Created by Darshana Das K(https://github.com/Darshana-Das-K)


#Use Arrow Keys to change direction of snake
#Eat the fruit ans score maximum points 
#Click on Quit to exit the game


#importing libraries
import pygame
import sys
import time
import random

def snakeGameWithMenu():
    #Button defined for the buttons in menu
    class Button():
        def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
            return False

        def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)


    # Defining colours
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(191, 38, 62)
    green = pygame.Color(93, 220,137)
    blue = pygame.Color(47, 76, 187)

    #initialising game
    pygame.init()

    #setting title bar caption
    pygame.display.set_caption("Menu")
    
    snake_speed = 10

    #creating font object get_font
    def get_font(size): 
        return pygame.font.Font("assets/font.ttf", size)

    #defining window size and initialising game window
    x = 720
    y = 480
    pygame.display.set_caption('SNAKE GAME')
    game_window = pygame.display.set_mode((x, y))
    #Frame per seconds
    fps = pygame.time.Clock()
    #initialising score
    score = 0
    
    #defining funstion to show score
    def show_score(choice, color, font, size,score):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)
    
    #defining game over screen
    def game_over(score):

        my_font = pygame.font.SysFont("assets/font.ttf", 50)
        
        if (score==0):
            game_over_surface = my_font.render(
                'Your Score is : ' + str(score), True, red)
        else:
            game_over_surface = my_font.render(
                'Your Score is : ' + str(score), True, blue)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (x/2, y/2)
        game_window.fill("black")
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        #Displaying menu after 2 seconds
        time.sleep(2)
        game_window.fill("black")
        main_menu()
    
   
    #defining the game conditions
    def play(score):
        pygame.display.set_caption("SNAKE GAME")
        #intialising position of snake
        snake_position = [100, 50]
        
        snake_body = [[100, 50],
                    [90, 50],
                    [80, 50]
                    ]
        #determining the fruit position randomly
        fruit_position = [random.randrange(1, (x//10)) * 10,
                        random.randrange(1, (y//10)) * 10]

        fruit_spawn = True

        direction = 'RIGHT'
        change_to = direction

        
        while True:
        
            #key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
            #if two keys pressed simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            
            #moving the snake
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            #snake growing mechanism
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                fruit_spawn = False
            else:
                snake_body.pop()
                
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (x//10)) * 10,
                                random.randrange(1, (y//10)) * 10]
                
            fruit_spawn = True
            game_window.fill(black)
            
            for pos in snake_body:
                pygame.draw.rect(game_window, green,
                                pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))
            
            #game over condition
            if snake_position[0] < 0 or snake_position[0] > x-10:
                game_over(score=score)
                
            if snake_position[1] < 0 or snake_position[1] > y-10:
                game_over(score= score)

            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over(score= score)

            show_score(1, white, 'times new roman', 20,score=score)

            pygame.display.update()

            fps.tick(snake_speed)
            
    #main menu
    def main_menu():
        pygame.display.set_caption("Menu")
        while True:
        

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            #title
            MENU_TEXT = get_font(50).render("SNAKE GAME", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))
            
            #defining buttons
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(360, 250), 
                                text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(360, 400), 
                                text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")



            game_window.blit(MENU_TEXT, MENU_RECT)
            
            #changing colour on hovering
            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(game_window)
            
            #key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play(score=score)
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit() #deactivating pygame library
                        sys.exit()

            pygame.display.update()
    #calling main menu
    main_menu()