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
        
def getSLd(grid):
    total = 0
    for i in range(9):
        cur = int(grid[i])
        goalx,goaly = cur%3,cur//3
        curx,cury = i%3,i//3
        total += pow(pow((goalx-curx),2)+pow((goaly-cury),2),1/2)
    return total
        
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
def isGoal(grid):
    return grid==targetGrid
'''
def isGoal(grid):
    return sum(map(int,list(grid[:3])))==11
'''
#print(getMd(startingGrid,targetGrid))
'''
#Testing Functions
print(startingGrid)
print(moveUp(startingGrid,'',getEmpty(startingGrid)))
print(branch(startingGrid,''),getEmpty(startingGrid))
print(getEmpty(startingGrid),getEmpty(startingGrid))  
''' 
def BFS(grid):
    queue =[]
    heapq.heappush(queue,(0,(grid,''))) 
    print(queue)
    path = ''
    steps=0
    explored = set()
    while(True):
        steps+=1
        weight,(grid,path) = heapq.heappop(queue)
        if(DEBUG and steps%100000==0):
            print("\nSteps: "+str(steps))
            print("Queue Size: "+str(len(queue)))
            print("Depth: "+str(len(path)))
            print("Weight: "+str(weight))
            print("Path: "+str(path))
            print("Grid: " +str(grid))
        if(isGoal(grid)):
            if(DEBUG):
                print("\nSOLUTION")
                print("Queue Size: "+str(len(queue)))
                print("Depth: "+str(len(path)))
                print("Weight: "+str(weight))
                print("Path: "+str(path))
                print("Grid: " +str(grid))
            return path
        explored.add(grid)
        branches = branch(grid,path)
        for child in branches:
            if(child[0] not in explored):
                heapq.heappush(queue,(weight+1,child))
    
def testMovement(grid):
    while(True):
        direction = input("\n")
        empty = getEmpty(startingGrid)
        match direction:
            case 'u':
                grid,path = moveUp(grid,path,empty)   
            case 'd':
                grid,path = moveDown(grid,path,empty)
            case 'l':
                grid,path = moveLeft(grid,path,empty)
            case 'r':
                grid,path = moveRight(grid,path,empty)
        print(startingGrid,path)

read_file("input.txt")