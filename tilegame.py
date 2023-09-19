import numpy as np
import pygame
size = 150
border = 5
background_color=[180,180,180]
margin = border
pygame.init()
class Tile(object):
    tileMap = []
    font = pygame.font.SysFont('coper black', 90)
    for i in range(9):
        image = font.render(str(i), True, (0, 0, 0))
        x,y = image.get_width()//2,image.get_height()//2
        tile = pygame.Surface((size, size))
        tile.fill(background_color)
        pygame.draw.rect(tile, [255,255,255], pygame.Rect(margin,margin,size-2*margin,size-2*margin),0,30)
        pygame.draw.rect(tile, [10,10,10], pygame.Rect(margin,margin,size-2*margin,size-2*margin),  border,30)
        tile.blit(image,(size//2-x,size//2-y))
        tileMap.append(tile)

    def __init__(self,num,center):
        self.value = num
        self.center = center
    def getCenter(self):
        return self.center
    def setCenter(self,center):
        self.center= center
    def move(self, newTile):
        self.center = newTile.getCenter()
        return self
    def draw(self, surf):
        if(self.value!=0):
            surf.blit(self.tileMap[self.value], self.center)
    
    def __eq__(self, __value: object) -> bool:
        if(isinstance(__value,int)):
            return self.value == __value
        return self.value == __value.value
    def __str__(self):
        return str(self.value)
print(Tile(6,(10,50))==5)
#p  from queue import PriorityQueue

#startingGrid = np.array([[4,2,5],[1,3,6],[0,8,7]])
class Grid(object):
    def __init__(self,grid):
        newGrid = np.empty((3,3),Tile)
        for i in range(3):
            for j in range(3):
                newGrid[j][i]=Tile(grid[j][i],(i*size,j*size))
        self.grid = newGrid
    def getHole(self):
        return  list(zip(*np.where(self.grid==0)))[0]
    def findVal(self,num):
        return list(zip(*np.where(targetGrid==num)))[0]
    def getMd(self,targetGrid):
        md = 0
        for y,row in enumerate(self.grid):
            for x,cell in enumerate(row):
                if(cell!=0):
                    print(self.findVal(cell))
                    goaly,goalx = self.findVal(cell)
                    md += abs(x-goalx)+abs(y-goaly)
        return(md)
    def switch(self,tile1,tile2):
        tile1.move(tile2)
        tile2.move(tile1)
        temp = tile1
        tile1 = tile2
        tile2 = temp
    def moveUp(self):
        emptyY,emptyX = self.getHole()
        if emptyY==0: return self.grid
        newY = emptyY-1
        self.switch(self.grid[emptyY][emptyX],self.grid[newY][emptyX])
        return self.grid
    def moveDown(self):
        emptyY,emptyX = self.getHole()
        if emptyY==2: return self.grid
        newY = emptyY+1
        self.switch(self.grid[emptyY][emptyX],self.grid[newY][emptyX])
        return self.grid
    def moveLeft(self):
        emptyY,emptyX = self.getHole()
        if emptyX==0: return self.grid
        newX = emptyX-1
        self.switch(self.grid[emptyY][emptyX],self.grid[emptyY][newX])
        return self.grid
    def moveRight(self):
        emptyY,emptyX = self.getHole()
        if emptyX==2: return self.grid
        newX = emptyX+1
        self.switch(self.grid[emptyY][emptyX],self.grid[emptyY][newX])
        return self.grid
    def __str__(self):
        temp = np.empty((3,3),str)
        for i in range(3):
            for j in range(3):
                temp[j][i]=str(self.grid[j][i])
        return str(temp)
    def draw(self,surface):
        for i in range(3):
                for j in range(3):
                    self.grid[j][i].draw(surface)
    

targetGrid = np.array([[0,1,2],[3,4,5],[6,7,8]])
startingGrid = Grid(np.array([[1,0,2],[3,4,5],[6,7,8]]))
print(startingGrid.getMd(targetGrid))
print(startingGrid)
print(startingGrid.moveUp())
print(startingGrid)


#Pygame
class game(object):
    def __init__(self,grid):
        self.screen = pygame.display.set_mode((size*3, size*3))
        self.clock = pygame.time.Clock()
        self.background_colour = (234, 212, 252)
        self.title = pygame.display.set_caption('Tile Game')
        self.grid = grid
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
                            self.grid.moveUp()
                        case pygame.K_s:
                            self.grid.moveDown()
                        case pygame.K_a:
                            self.grid.moveLeft()
                        case pygame.K_d:
                            self.grid.moveRight()
                    print(startingGrid)
            if((startingGrid==targetGrid).all()):
                break
            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            #self.player.move(move_x * 5, move_y * 5)
            self.screen.fill(background_color)
            self.grid.draw(self.screen)
            
            #self.player.draw(self.screen)
            pygame.display.update()
g= game(startingGrid)
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
    
