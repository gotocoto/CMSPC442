def read_file(file):
    f = open(file, "r")
    print(f.read())
import numpy as np
import pygame
import heapq
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
#targetGrid = np.array([[0,1,2],[3,4,5],[6,7,8]])
targetGrid = [0,1,2,3,4,5,6,7,8]
#startingGrid = np.array([[1,0,2],[3,4,5],[6,7,8]])
#startingGrid = [np.array([[7,2,4],[5,0,6],[8,3,1]])]
startingGrid= [2,1,0,3,4,5,6,7,8]
#startingGrid = [7,2,4,5,0,6,8,3,1]
def getMd(grid,targetGrid):
    md = 0
    for y,row in enumerate(grid):
        for x,cell in enumerate(row):
            if(cell!=0):
                print(list(zip(*np.where(targetGrid==cell)))[0])
                goaly,goalx = list(zip(*np.where(targetGrid==cell)))[0]
                md += abs(x-goalx)+abs(y-goaly)
    return(md)
def getEmpty(grid):
    for i in range(9):
        if(grid[i]==0):
            return i
def moveUp(grid,path):
    path+='U'
    empty = getEmpty(grid)
    grid[empty]=grid[empty-3]
    grid[empty-3]=0
    return [grid,path]
def moveDown(grid,path):
    path+='D'
    empty = getEmpty(grid)
    grid[empty]=grid[empty+3]
    grid[empty+3]=0
    return [grid,path]
def moveLeft(grid,path):
    path+='L'
    empty = getEmpty(grid)
    grid[empty]=grid[empty-1]
    grid[empty-1]=0
    return [grid,path]
def moveRight(grid,path):
    path+='R'
    empty = getEmpty(grid)
    grid[empty]=grid[empty+1]
    grid[empty+1]=0
    return [grid,path]
def branch(grid,path):
    branches = []
    empty = getEmpty(grid)
    if(empty%3 != 2):
        branches.append(moveRight(list.copy(grid),path))
    if(empty%3 != 0 ):
        branches.append(moveLeft(list.copy(grid),path))
    if(empty>2):
        branches.append(moveUp(list.copy(grid),path))
    if(empty<6):
        branches.append(moveDown(list.copy(grid),path))
    return branches #Remove the None types
class gridPath:
    def __init__(self,combination):
        self.grid,self.path = combination
    def getGrid(self):
        return self.grid
    def __eq__(self, __value: object) -> bool:
        return False
        #return np.array_equal(self.grid,__value.getGrid())
    def __lt__(self, __value: object) -> bool:
        return False
        #return np.less(self.grid,__value.getGrid()).all()
    def data(self):
        return [self.grid,self.path]
#print(getMd(startingGrid,targetGrid))
print(startingGrid)
print(moveUp(startingGrid,[]))
print(branch(startingGrid,[]))
print(getEmpty(startingGrid))
queue =[]
heapq.heappush(queue,(0,gridPath([startingGrid,'S']))) 
print(queue)
i=0
while(True):
    i+=1
    if(i%10000==0): print(i)
    weight,temp = heapq.heappop(queue)
    grid,path =temp.data()
    if(grid==targetGrid):
        print(weight)
        print(path)
        print(grid)
        break
    #print(path)
    branches = branch(grid,path)
    for child in branches:
        heapq.heappush(queue,(weight+1,gridPath(child)))
    

read_file("input.txt")