import pygame

#################################### FUNCTIONS ################################


def drawmap(map):
    
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 1:
                screen.blit(black, (col*50, row*50))
            if map[row][col] == 2:
                screen.blit(dirt, (col*50, row*50))
            if map[row][col] == 3:
                screen.blit(mtn, (col*50, row*50))
            if map[row][col] == 4:
                screen.blit(water, (col*50, row*50))
            if map[row][col] == 5:
                screen.blit(tree, (col*50, row*50))
            if map[row][col] == 6:
                screen.blit(REC, (col*50, row*50))
            if map[row][col] == 7:
                screen.blit(BEC, (col*50, row*50))
            if map[row][col] == 8:
                screen.blit(L, (col*50, row*50))
            if map[row][col] == 9:
                screen.blit(I, (col*50, row*50))
            if map[row][col] == 10:
                screen.blit(F, (col*50, row*50))
            if map[row][col] == 11:
                screen.blit(E, (col*50, row*50))
            if map[row][col] == 12:
                screen.blit(heart, (col*50, row*50))
            if map[row][col] == 13:
                screen.blit(dash, (col*50, row*50))
            if map[row][col] == 14:
                screen.blit(caveent, (col*50, row*50))
            if map[row][col] == 15:
                screen.blit(dirt, (col*50, row*50))
            if map[row][col] == 16:
                screen.blit(dirt, (col*50, row*50))

        

##################################### GLOBAL VARIABLES #########################
w = 1000
h = 800
rowpos = 0
colpos = 0
screen = pygame.display.set_mode([1000,800])
pygame.display.set_caption("ADVENTURE OF THE HERO")
black = pygame.image.load("caveent.png")
black = pygame.transform.scale(black, (50,50))
dirt = pygame.image.load("dirt.png")
dirt = pygame.transform.scale(dirt, (50,50))
mtn = pygame.image.load("mntn.png")
mtn = pygame.transform.scale(mtn, (50,50))
dash = pygame.image.load("-.png")
dash = pygame.transform.scale(dash, (50,50))
L = pygame.image.load("L.png")
L = pygame.transform.scale(L, (50,50))
I = pygame.image.load("I.png")
I = pygame.transform.scale(I, (50,50))
F = pygame.image.load("F.png")
F = pygame.transform.scale(F, (50,50))
E = pygame.image.load("E.png")
E = pygame.transform.scale(E, (50,50))
heart = pygame.image.load("hrt.png")
heart = pygame.transform.scale(heart, (50,50))
water = pygame.image.load("water.png")
water = pygame.transform.scale(water, (50,50))
tree = pygame.image.load("tree.png")
tree = pygame.transform.scale(tree, (50,50))
REC = pygame.image.load("REC.png")
REC = pygame.transform.scale(REC, (50,50))
BEC = pygame.image.load("BEC.png")
BEC = pygame.transform.scale(BEC, (50,50))
caveent = pygame.transform.scale(black, (50,50))
dude = pygame.image.load("dude.png")
dude = pygame.transform.scale(dude, (50,50))
dudex = 12
dudey = 10


counter = 0
up = False
right = False
left = False
down = False
space = False
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 8, 9, 10, 11, 13, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1],
       [4, 4, 6, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

#################################### GAME LOOP ################################
while True:
    done = False
    # ============================== HANDLE EVENTS  ========================= #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break
        
        #sets up to True when up arrow pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
        
        #sets up to False when up arrow is not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False  
        if event.type == pygame.KEYDOWN:      #KEYDOWN means a key is pressed
            if event.key == pygame.K_UP:      #UP arrow is pressed
                up = True
            if event.key == pygame.K_DOWN:      
                down = True
            if event.key == pygame.K_LEFT:      
                left = True
            if event.key == pygame.K_RIGHT:      
                right = True
            if event.key == pygame.K_SPACE:   #SPACE is pressed
                space = True
                            
        if event.type == pygame.KEYUP:        #KEYUP means a key is NOT pressed
            if event.key == pygame.K_UP:      #UP arrow is NOT pressed
                up = False
            if event.key == pygame.K_DOWN:      
                down = False
            if event.key == pygame.K_LEFT:      
                left = False
            if event.key == pygame.K_RIGHT:      
                right = False
            if event.key == pygame.K_SPACE:   #SPACE is NOT pressed
                space = False

                
    if done == True:
        break

 # ============================== MOVE STUFF ============================= #
 # Collision + movement
    if right:
        if map[dudey][dudex + 1] == 5 or map[dudey][dudex + 1] == 3 or map[dudey][dudex + 1] == 4 or map[dudey][dudex + 1] == 1:
            right = False
        else:
            dudex += 1
            right = False
            
    if left:
        if map[dudey][dudex - 1] == 5 or map[dudey][dudex - 1] == 3 or map[dudey][dudex - 1] == 4 or map[dudey][dudex - 1] == 1 or map[dudey][dudex - 1] == 6:
            right = False
        else:
            dudex -= 1
            left = False
    if up:
        if map[dudey - 1][dudex] == 5 or map[dudey - 1][dudex] == 3 or map[dudey - 1][dudex] == 4:
            up = False
        else:
            dudey -= 1
            up = False
        
        if map[dudey + 1][dudex] == 15:
            map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 8, 9, 10, 11, 13, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5],
                   [4, 4, 4, 4, 4, 4, 6, 16, 16, 16, 16, 16, 5, 5, 5, 5, 5, 5, 5, 5]]
            dudex = 9
            dudey = 15
            drawmap(map)
            
    if down:
        if map[dudey + 1][dudex] == 5 or map[dudey + 1][dudex] == 3 or map[dudey + 1][dudex] == 4 or map[dudey + 1][dudex] == 1 or map[dudey + 1][dudex] == 7 or map[dudey][dudex] == 16:
            down = False
        else:
            dudey += 1
            down = False

#     if map[dudey - 1][dudex] == 16:
#         map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 8, 9, 10, 11, 13, 1],
#                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1],
#                [4, 4, 6, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
#                [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
#         dudex = 9
#         dudey = 4
#         drawmap(map)

            


 # ============================== COLLISION ============================== #





 # ============================== DRAW STUFF ============================= #                               
    screen.fill((0, 0, 0))
    drawmap(map)
    screen.blit(dude, ((dudex*50, dudey*50)))    


    
    
    # ============================== PYGAME STUFF (DO NOT EDIT) ============= #
    pygame.display.flip()
    pygame.time.delay(20)
pygame.quit()