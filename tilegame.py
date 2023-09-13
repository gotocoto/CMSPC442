import numpy as np
import pygame

#p  from queue import PriorityQueue
targetGrid = np.array([[0,1,2],[3,4,5],[6,7,8]])
startingGrid = np.array([[1,0,2],[3,4,5],[6,7,8]])
#startingGrid = np.array([[4,2,5],[1,3,6],[0,8,7]])

def getMd(grid,targetGrid):
    md = 0
    for y,row in enumerate(grid):
        for x,cell in enumerate(row):
            if(cell!=0):
                print(list(zip(*np.where(targetGrid==cell)))[0])
                goaly,goalx = list(zip(*np.where(targetGrid==cell)))[0]
                md += abs(x-goalx)+abs(y-goaly)
    return(md)

def moveUp(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyY==0: return grid
    newY = emptyY-1
    grid[emptyY][emptyX]=grid[newY][emptyX]
    grid[newY][emptyX]=0
    return grid
def moveDown(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyY==2: return grid
    newY = emptyY+1
    grid[emptyY][emptyX]=grid[newY][emptyX]
    grid[newY][emptyX]=0
    return grid
def moveLeft(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyX==0: return grid
    newX = emptyX-1
    grid[emptyY][emptyX]=grid[emptyY][newX]
    grid[emptyY][newX]=0
    return grid
def moveRight(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyX==2: return grid
    newX = emptyX+1
    grid[emptyY][emptyX]=grid[emptyY][newX]
    grid[emptyY][newX]=0
    return grid
print(getMd(startingGrid,targetGrid))
print(startingGrid)
print(moveUp(startingGrid))
print(startingGrid)

'''
#Pygame
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Tile Game')
screen.fill(background_colour)
pygame.display.flip()'''
running = True

while running:
    '''
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
    if((startingGrid==targetGrid).all()):
        break'''
    print(startingGrid)
    direction = input("\n")
    match direction:
        case 'u':
            moveUp(startingGrid)
        case 'd':
            moveDown(startingGrid)
        case 'l':
            moveLeft(startingGrid)
        case 'r':
            moveRight(startingGrid)
    
