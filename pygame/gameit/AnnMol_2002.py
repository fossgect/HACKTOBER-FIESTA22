#imported pygame and requests library
import pygame
import requests

#Here the implementation code begins
def sudoku():
    WIDTH=550#width of the window
    background_color=(251,247,245)#background color for the sudoku 
    original_grid_element_color=(52,31,151)
    buffer=5#to store buffer value

    response=requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")#take initialvalues to be set in the sudoku boxes
    grid=response.json()['board']
    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
    #inserting values into the game board
    def insert(win,position):
        i,j=position[1],position[0]
        myfont = pygame.font.SysFont('Comic Sans MS',35)

        while True:
            for event in pygame.event.get():
                #to close the game
                if event.type==pygame.QUIT:
                    return
                if event.type==pygame.KEYDOWN:
                    if(grid_original[i-1][j-1]!=0):
                        return
                    if(event.key == 48):#if the value entered is 0, then leave it blank
                        grid[i-1][j-1]=event.key - 48
                        pygame.draw.rect(win,background_color,(position[0]*50+buffer,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                        pygame.display.update()
                    if(0<event.key-48<10 ):#to allow only nos from 1-9
                        pygame.draw.rect(win,background_color,(position[0]*50+buffer,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                        value=myfont.render(str(event.key-48),True,(0,0,0))
                        win.blit(value,(position[0]*50+15,position[1]*50))
                        grid[i-1][j-1]=event.key-48
                        pygame.display.update()
                    return
                return

    def main():
        pygame.init()
        #creating the layout of the game how it looks
        win=pygame.display.set_mode((WIDTH,WIDTH))
        pygame.display.set_caption("Sudoku")
        win.fill(background_color)
        myfont = pygame.font.SysFont('Comic Sans MS',35)
        #drawing lines for the boxes
        for i in range(0,10):
            if(i%3 ==0):
                pygame.draw.line(win,(0,0,0),(50+50*i,50),(50+50*i,500),4)
                pygame.draw.line(win,(0,0,0),(50,50+50*i),(500,50+50*i),4)
            #drawing thicker lines in between after a square of 3X3
            pygame.draw.line(win,(0,0,0),(50+50*i,50),(50+50*i,500),2)
            pygame.draw.line(win,(0,0,0),(50,50+50*i),(500,50+50*i),2)
        pygame.display.update()
        #rendering the size of values entered and how it looks
        for i in range(0,len(grid[0])):
            for j in range(0,len(grid[0])):
                if(0<grid[i][j]<10):
                    value=myfont.render(str(grid[i][j]),True,original_grid_element_color)
                    win.blit(value,((j+1)*50+15,(i+1)*50))
        pygame.display.update()
        #mentioning what to do inorder to the actions of the player 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos=pygame.mouse.get_pos()
                    insert(win,(pos[0]//50,pos[1]//50))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


    main()