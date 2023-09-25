def read_file(file):
    f = open(file, "r")
    print(f.read())
import heapq
import queue
size = 150
border = 5
background_color=[180,180,180]
margin = border
'''
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
            surf.blit(self.tile, self.center)'''
#p  from queue import PriorityQueue
#targetGrid = np.array([[0,1,2],[3,4,5],[6,7,8]])
targetGrid = '012345678'
#startingGrid = np.array([[1,0,2],[3,4,5],[6,7,8]])
#startingGrid = [np.array([[7,2,4],[5,0,6],[8,3,1]])]
startingGrid= '724506831'
#startingGrid = '123456078'
#startingGrid = [7,2,4,5,0,6,8,3,1]
def getMd(grid):
    total = 0
    for i in range(9):
        cur = int(grid[i])
        goalx,goaly = cur%3,cur//3
        curx,cury = i%3,i//3
        total += abs(goalx-curx)+abs(goaly-cury)
    return total
        
        
    return(md)
def getEmpty(grid):
    return grid.index('0')
def moveUp(grid,path,empty):
    path+='U'
    newGrid = "".join([grid[:empty-3],'0',grid[empty-2:empty],grid[empty-3],grid[empty+1:]])
    return [newGrid,path]
def moveDown(grid,path,empty):
    path+='D'
    newGrid = "".join([grid[:empty],grid[empty+3],grid[empty+1:empty+3],'0',grid[empty+4:]])
    return [newGrid,path]
def moveLeft(grid,path,empty):
    path+='L'
    newGrid = "".join([grid[:empty-1],'0',grid[empty-1],grid[empty+1:]])
    return [newGrid,path]
def moveRight(grid,path,empty):
    path+='R'
    newGrid = "".join([grid[:empty],grid[empty+1],'0',grid[empty+2:]])
    return [newGrid,path]
def branch(grid,path):
    branches = []
    empty = getEmpty(grid)
    if(empty%3 != 2):
        branches.append(moveRight(grid,path,empty))
    if(empty%3 != 0 ):
        branches.append(moveLeft(grid,path,empty))
    if(empty>2):
        branches.append(moveUp(grid,path,empty))
    if(empty<6):
        branches.append(moveDown(grid,path,empty))
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
print(moveUp(startingGrid,'',getEmpty(startingGrid)))
print(branch(startingGrid,''),getEmpty(startingGrid))
print(getEmpty(startingGrid),getEmpty(startingGrid))   
queue =[]
heapq.heappush(queue,(0,(startingGrid,''))) 
print(queue)
path = ''
steps=0
visited = set()
while(True):
    steps+=1
    weight,(grid,path) = heapq.heappop(queue)
    if(steps%100==0):
        print("\nSteps: "+str(steps))
        print("Queue Size: "+str(len(queue)))
        print("Depth: "+str(len(path)))
        print("Weight: "+str(weight))
        print("Path: "+str(path))
        print("Grid: " +str(grid))
    if(grid==targetGrid):
        print("\nSOLUTION")
        print("Queue Size: "+str(len(queue)))
        print("Depth: "+str(len(path)))
        print("Weight: "+str(weight))
        print("Path: "+str(path))
        print("Grid: " +str(grid))
        break
    #print(path)
    '''
    direction = input("\n")
    match direction:
        case 'u':
            startingGrid,path = moveUp(startingGrid,path)   
        case 'd':
            startingGrid,path = moveDown(startingGrid,path)
        case 'l':
            startingGrid,path = moveLeft(startingGrid,path)
        case 'r':
            startingGrid,path = moveRight(startingGrid,path)
    '''
    '''
    #Checking if in queue
    for i in queue:
            if(i[1][0]==child[0]):
                unique = False
                if(i[0]>len(child[1])):
                    i[0]=child[1]
                    update = True
        if(update):
            heapq.heapify(queue)
            '''
    visited.add(grid)
    branches = branch(grid,path)
    for child in branches:
        if(child[0] not in visited):
            heapq.heappush(queue,(len(child[1])+getMd(child[0]),child))
    

read_file("input.txt")