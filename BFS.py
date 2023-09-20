import numpy as np
import pygame
size = 150
border = 5
background_color=[180,180,180]
margin = border
class Tile(object):
    
    def __init__(self,num,center):
        self.value = num
        self.font = pygame.font.SysFont('coper black', 90)
        self.image = self.font.render(str(self.value), True, (0, 0, 0))
        x,y = self.image.get_width()//2,self.image.get_height()//2
        self.tile = pygame.Surface((size, size))
        self.tile.fill(background_color)
        pygame.draw.rect(self.tile, [255,255,255], pygame.Rect(margin,margin,size-2*margin,size-2*margin),0,30)
        pygame.draw.rect(self.tile, [10,10,10], pygame.Rect(margin,margin,size-2*margin,size-2*margin),  border,30)
        
        self.tile.blit(self.image,(size//2-x,size//2-y))
        self.center = center

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        if(self.value!=0):
            surf.blit(self.tile, self.center)
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
    if emptyY==0: return None
    newY = emptyY-1
    grid[emptyY][emptyX]=grid[newY][emptyX]
    grid[newY][emptyX]=0
    return grid
def moveDown(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyY==2: return None
    newY = emptyY+1
    grid[emptyY][emptyX]=grid[newY][emptyX]
    grid[newY][emptyX]=0
    return grid
def moveLeft(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyX==0: return None
    newX = emptyX-1
    grid[emptyY][emptyX]=grid[emptyY][newX]
    grid[emptyY][newX]=0
    return grid
def moveRight(grid):
    emptyY,emptyX = list(zip(*np.where(grid==0)))[0]
    if emptyX==2: return None
    newX = emptyX+1
    grid[emptyY][emptyX]=grid[emptyY][newX]
    grid[emptyY][newX]=0
    return grid
def branch(grid):
    branches = []
    branches.append(moveRight(np.copy(grid)))
    branches.append(moveLeft(np.copy(grid)))
    branches.append(moveUp(np.copy(grid)))
    branches.append(moveDown(np.copy(grid)))
    return list(filter(lambda item: item is not None, branches)) #Remove the None types
print(getMd(startingGrid,targetGrid))
print(startingGrid)
print(moveUp(startingGrid))
print(startingGrid)

def read_file(file):
    f = open(file, "r")
    print(f.read())

#Pygame
class game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((size*3, size*3))
        self.clock = pygame.time.Clock()
        self.background_colour = (234, 212, 252)
        self.title = pygame.display.set_caption('Tile Game')
        pygame.init()
    def run(self):
        running = 1
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                
                # Check for QUIT event      
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if(event.key==pygame.K_w):
                            moveUp(startingGrid)
                    elif(event.key==pygame.K_s):
                            moveDown(startingGrid)
                    elif(event.key==pygame.K_a):
                            moveLeft(startingGrid)
                    elif(event.key==pygame.K_d):
                            moveRight(startingGrid)
                    print(startingGrid)
            if((startingGrid==targetGrid).all()):
                break
            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            #self.player.move(move_x * 5, move_y * 5)
            self.screen.fill(background_color)
            for i in range(3):
                for j in range(3):
                    Tile(startingGrid[j][i],(i*size,j*size)).draw(self.screen)
            #self.player.draw(self.screen)
            pygame.display.update()
g= game()
g.run()
