import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game of life")


def box(a,b):
    pygame.draw.rect(win, (225,225,225), (a, b, 5, 5))


state = [[0 for i in range(100)] for j in range(100)]  # i is alive and 0 is dead


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
            box(X,Y)
            state[int(X/5)][int(Y/5)] = 1

    for i in range(100):
        for j in range(100):
            if state[i][j] == 0:
                pygame.draw.rect(win, (0, 0, 0),(i*5, j*5, 5, 5))
            if state[i][j] == 1:
                box(i*5, j*5)

    
    pygame.display.update()
pygame.quit()
            