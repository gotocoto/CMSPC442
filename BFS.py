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







read_file("input.txt")