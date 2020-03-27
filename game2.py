import pygame
import time
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("first game")


a = []
b = []



checkAlive = [[0 for i in range(100)] for j in range(100)]




for i in range(2, 498, 5):
    a.append(i)
    b.append(i)

def checkAlgoAlive(a,i,j):
    if i>1 and i<99 and j>1 and j<99:
        temp = []
        sum = 0
        temp.append(a[i+1][j])
        temp.append(a[i][j+1])
        temp.append(a[i][j-1])
        temp.append(a[i-1][j])
        temp.append(a[i+1][j+1])
        temp.append(a[i+1][j-1])
        temp.append(a[i-1][j+1])
        temp.append(a[i-1][j-1])
        for k in temp:  
            sum = sum + k
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0
    else:
        return 0


def checkAlgoDead(a,i,j):
    if i>1 and i<99 and j>1 and j<99:
        temp = []
        sum = 0
        temp.append(a[i+1][j])
        temp.append(a[i][j+1])
        temp.append(a[i][j-1])
        temp.append(a[i-1][j])
        temp.append(a[i+1][j+1])
        temp.append(a[i+1][j-1])
        temp.append(a[i-1][j+1])
        temp.append(a[i-1][j-1])
        for k in temp:
            sum = sum + k
        if sum == 3:
            return 1
        else:
            return 0
    else:
        return 0


def box(k,a,b):
    pygame.draw.rect(win, (255, k, 255),(a, b, 5, 5))





run = True
while run:
    
    pygame.time.delay(10) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            X = int(pos[0]/5)*5
            Y = int(pos[1]/5)*5
            box(150,X,Y)
            checkAlive[int(X/5)][int(Y/5)] = 1

            # color = win.get_at(pos)
            # print(color)
            # if win.get_at((X,Y)) == (255, 255, 255, 255):
            #     print("haha")
    
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:


        for i in range(100):
            for j in range(100):
                if checkAlive[i][j] == 1:
                    if checkAlgoAlive(checkAlive, i, j) == 0:
                        checkAlive[i][j] = 0
                if checkAlive[i][j] == 0: 
                    if checkAlgoDead(checkAlive, i, j) == 1:
                        checkAlive[i][j] = 1

        for i in range(100):
            for j in range(100):
                if checkAlive[i][j] == 0:
                    pygame.draw.rect(win, (0, 0, 0),(i*5, j*5, 5, 5))
                if checkAlive[i][j] == 1:
                    box(255,i*5,j*5)


    
    pygame.display.update()
pygame.quit()
