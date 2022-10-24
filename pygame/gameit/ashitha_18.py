import pygame
import random

def SudokoGame():
    pygame.font.init()

    # Load test fonts for future use
    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)

    screen = pygame.display.set_mode((500, 685))
    x = 0
    y = 0
    dif = 500 / 9
    val = 0
    score = 0


    grid1 =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    grid1_original = [[grid1[x][y] for y in range(len(grid1[0]))] for x in range(len(grid1))]

    grid2 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0] 
    ]
    grid2_original = [[grid2[x][y] for y in range(len(grid2[0]))] for x in range(len(grid2))]

    grid3 = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    grid3_original = [[grid3[x][y] for y in range(len(grid3[0]))] for x in range(len(grid3))]
    num = random.randint(0,2)

    grid_random = [grid1, grid2, grid3]
    grid_original = [grid1_original, grid2_original, grid3_original] 


    def get_cord(pos):
        global x
        x = pos[0]//dif
        global y
        y = pos[1]//dif

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (0, 0, 255), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 5)
            pygame.draw.line(screen, (0, 0, 255), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 5)

    
    def draw():
        for i in range (9):
            for j in range (9):
                if grid[i][j]!= 0:
                    # Fill yellow color in already numbered grid
                    pygame.draw.rect(screen, (255,255,153), (i * dif, j * dif, dif + 1, dif + 1))

                    # Fill grid with default numbers specified
                    text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                    screen.blit(text1, (i * dif + 12, j * dif + 5))
                                        
        # Draw lines horizontally and vertically to form grid 
        for i in range(10):
            if i % 3 == 0 :
                        thick = 7
            else:
                        thick = 1
                        
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    def draw_val(val):
        text1 = font1.render(str(val), 1, (0, 0, 0))
        screen.blit(text1, (x * dif + 15, y * dif + 15))

    def raise_error1():
        text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))
            
    def raise_error2():
        text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))

    def next_time():
        text1 = font1.render("better luck next time", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))
        score_text = font2.render("SCORE : " + str(score), 1, (0,0,0))
        screen.blit(score_text, (40, 610))
        
    def valid(m, i, j, val):
        for it in range(9):
                if m[i][it]== val:
                        return False
                if m[it][j]== val:
                        return False
                                
        it = i//3
        jt = j//3
        for i in range(it * 3, it * 3 + 3):
                for j in range (jt * 3, jt * 3 + 3):
                    if m[i][j]== val:
                        return False
        return True

    def find_empty(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return (i, j)  

        return False

    def solve(grid, i, j):

        while grid[i][j]!= 0:
            if i<8:
                i+= 1
            elif i == 8 and j<8:
                i = 0
                j+= 1
            elif i == 8 and j == 8:
                return True
        pygame.event.pump()
        
        for it in range(1, 10):
            if valid(grid, i, j, it)== True:
                grid[i][j]= it
                global x, y
                x = i
                y = j
                screen.fill((255, 255, 255))
                draw()
                draw_box()
                pygame.display.update()
                pygame.time.delay(20)
                if solve(grid, i, j)== 1:
                            return True
                else:
                            grid[i][j]= 0
                screen.fill((255, 255, 255))
                draw()
                draw_box()
                pygame.display.update()
                pygame.time.delay(50)
        return False


    def instruction():
        text1 = font2.render("PRESS N TO PLAY NEXT GAME", 1, (0, 0, 0))
        text2 = font2.render("ENTER VALUES AND PRESS ENTER ", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))
        screen.blit(text2, (20, 540))


    def result(score):
        score +=1
        score_text = font2.render("SCORE : " + str(score), 1, (0,0,0))
        text1 = font1.render("SOLVED", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))
        screen.blit(score_text, (40, 610))

    run = True
    flag1 = 0
    flag2 = 0
    rs = 0
    error = 0
    f = 1

    while run:
            grid = grid_random[num]

            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    flag1 = 1
                    pos = pygame.mouse.get_pos()
                    get_cord(pos)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x-= 1
                        flag1 = 1
                    if event.key == pygame.K_RIGHT:
                        x+= 1
                        flag1 = 1
                    if event.key == pygame.K_UP:
                        y-= 1
                        flag1 = 1
                    if event.key == pygame.K_DOWN:
                        y+= 1
                        flag1 = 1

                    if event.key == pygame.K_1:
                        val = 1
                    if event.key == pygame.K_2:
                        val = 2
                    if event.key == pygame.K_3:
                        val = 3
                    if event.key == pygame.K_4:
                        val = 4
                    if event.key == pygame.K_5:
                        val = 5
                    if event.key == pygame.K_6:
                        val = 6
                    if event.key == pygame.K_7:
                        val = 7
                    if event.key == pygame.K_8:
                        val = 8
                    if event.key == pygame.K_9:
                        val = 9
                    
                    if event.key == pygame.K_r:
                        grid = grid_original[num]

                    if event.key == pygame.K_RETURN:
                        flag2 = 1
                
                    if event.key == pygame.K_n:
                        num=random.randint(0,2)
                        grid_random = grid_original
                        continue

                if flag2 == 1:
                    find = find_empty(grid)
                    if find:
                        rs=0
                        f=0
                        solve(grid,0,0)
                    elif solve(grid, 0, 0)== True:
                        rs = 1
                        flag2 = 0
                    else:
                        error = 1
                draw()        
                if val != 0: 
                    if valid(grid, int(x), int(y), val)== True:
                        grid[int(x)][int(y)]= val
                        flag1 = 0
                        draw_val(val)
                        
                    elif grid[int(x)][int(y)]!=0:
                        raise_error2()
                    else:
                        raise_error2()
                    val = 0

                if error == 1:
                    raise_error1()
                
                if f == 0:
                    next_time()
                    
                elif rs == 1:
                    result(score)
                
                if flag1 == 1:
                    draw_box()
                instruction()

                pygame.display.update()


    pygame.quit()