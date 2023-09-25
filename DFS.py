def read_file(file):
    f = open(file, "r")
    print(f.read())
import heapq
import queue
DEBUG =False
#p  from queue import PriorityQueue
#targetGrid = np.array([[0,1,2],[3,4,5],[6,7,8]])
targetGrid = '012345678'
#startingGrid = np.array([[1,0,2],[3,4,5],[6,7,8]])
#startingGrid = [np.array([[7,2,4],[5,0,6],[8,3,1]])]
#startingGrid= '724506831'
startingGrid = '123456078'
#startingGrid = [7,2,4,5,0,6,8,3,1]
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
class Grid(object):
    def __init__(self,grid,path):
        self.grid = grid
        self.nextNodeNumber = 0
        self.path = path
        self.empty = getEmpty(grid)
        self.options = []
        if(self.empty%3 != 2):
            self.options.append('R')
        if(self.empty%3 != 0 ):
            self.options.append('L')
        if(self.empty>2):
            self.options.append('U')
        if(self.empty<6):
            self.options.append('D')
        self.options.append(None)
    def next(self):
        nextDirection = self.options[self.nextNodeNumber]
        self.nextNodeNumber += 1
        if(nextDirection==None):
            return None
        if(nextDirection =='R'):
            return Grid(*moveRight(self.grid,self.path,self.empty))
        if(nextDirection =='L'):
            return Grid(*moveLeft(self.grid,self.path,self.empty))
        if(nextDirection =='U'):
            return Grid(*moveUp(self.grid,self.path,self.empty))
        if(nextDirection =='D'):
            return Grid(*moveDown(self.grid,self.path,self.empty))
        else:
            return 0/0
    def __str__(self):
        return str(self.grid)
print(startingGrid)
print(moveUp(startingGrid,'',getEmpty(startingGrid)))
print(branch(startingGrid,''),getEmpty(startingGrid))
print(getEmpty(startingGrid),getEmpty(startingGrid))   
def DFS(grid):
    queue =[]
    #print(queue)
    path = 'S'
    steps=0
    notDone = True
    depth =0
    running = True
    while(running):
        depth+=1
        queue.clear()
        queue.append(Grid(grid,''))
        print("Depth is now ",depth)
        notDone = True
        while(notDone):
            steps+=1
            if(not queue):
                break
            if(depth>len(queue)):
                next = queue[-1].next()
                if(next==targetGrid):
                    if(DEBUG):
                        print( True)
                        print(queue[-1])
                        print(queue[-1].path())
                    return queue[-1].path()
                if(next==None):
                    queue.pop()
                else:
                    queue.append(next)
            else:
                queue.pop()
            if(DEBUG and steps%100000000==0):
                print("\nSteps: "+str(steps))
                print("Queue Size: "+str(len(queue)))
                print("Depth: "+str(depth))
                print("Grid: " +str(queue[-1]))
                print(queue)
        

    

read_file("input.txt")