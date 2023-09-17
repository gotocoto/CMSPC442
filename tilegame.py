import numpy as np
import pygame

class Tile(object):
    
    def __init__(self,num):
        self.value = num
        self.font = pygame.font.SysFont('arial', 70)
        self.image = self.font.render(str(self.value), True, (0, 0, 0))
        self.center = [100, 200]

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        surf.blit(self.image, self.center)
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


#Pygame
class game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.background_colour = (234, 212, 252)
        self.title = pygame.display.set_caption('Tile Game')
        pygame.init()
        self.player = Tile(4)
    def run(self):
        running = 1
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                
                # Check for QUIT event      
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_w:
                            moveUp(startingGrid)
                        case pygame.K_s:
                            moveDown(startingGrid)
                        case pygame.K_a:
                            moveLeft(startingGrid)
                        case pygame.K_d:
                            moveRight(startingGrid)
                    print(startingGrid)
            if((startingGrid==targetGrid).all()):
                break
            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            self.player.move(move_x * 5, move_y * 5)
            self.screen.fill([50, 200, 0])
            self.player.draw(self.screen)
            pygame.display.update()
g= game()
g.run()
'''
    direction = input("\n")
    match direction:
        case 'u':
            moveUp(startingGrid)
        case 'd':
            moveDown(startingGrid)
        case 'l':
            moveLeft(startingGrid)
        case 'r':
            moveRight(startingGrid)'''
    
