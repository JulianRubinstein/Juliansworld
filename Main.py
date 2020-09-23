import pygame, sys
from pygame.locals import *
import Sudoko_solver as ss

FPS = 10
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
LIGHTGRAY = (200, 200, 200)
BASICFONTSIZE = 50
WINDOWMULTIPLIER = 9 
WINDOWSIZE = 81
WINDOWWIDTH = int(WINDOWSIZE * WINDOWMULTIPLIER)
WINDOWHEIGHT = int(WINDOWSIZE * WINDOWMULTIPLIER)
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3)

def drawGrid():
    
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))

    return None

def settings():
    
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BASICFONTSIZE
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku')
    
    
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    FPSCLOCK.tick(FPS)
    DISPLAYSURF.fill(WHITE)
    
    return None

def populateCell(cellData, x, y):
    cellSurf = BASICFONT.render(cellData,True,BLACK)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)
 
def populateCells():
    for j in range (9):
        for i in range (9):
            pygame.draw.rect(DISPLAYSURF,WHITE,[WINDOWSIZE*(i+1/10),WINDOWSIZE*(j+1/10),70,70])
            populateCell(str(ss.s[j][i]),WINDOWSIZE*(i+1/3),WINDOWSIZE*(j+1/4))
            
def depopulateCells():
    for j in range (9):
        for i in range (9):
            pygame.draw.rect(DISPLAYSURF,WHITE,[WINDOWSIZE*(i+1/10),WINDOWSIZE*(j+1/10),70,70])

def solve():
    t=0
    i1 = 0
    j1 = 0
    k=0
    while(i1!=9):
        if ss.f[i1][j1]==0 and ss.p==1:
            ss.producenumber(i1,j1)  
            #print("\n got front in")
        if ss.f[i1][j1]==0 and ss.p==0:
            ss.backproducenumber(i1,j1)  
            #print("\n got back in")
        if ss.p==1:
            if j1==8:
                i1+=1
                j1=0
            else:
                j1+=1  
        if ss.p==0:        
            if j1==0:
                i1-=1
                j1=8
            else:
                j1-=1
        
        t=t+1
        populateCells()
        pygame.display.update()


def main():
    
    pygame.init()
    
    settings()
    
    drawGrid()
    
    ss.restart()
    depopulateCells()
    populateCells()
    pygame.display.update()
       
    while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        solve()
            
if __name__=='__main__':
    main()

    