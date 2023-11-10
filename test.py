import pygame
import random
#################################### CLASSES ##################################



#################################### FUNCTIONS ################################
 
def menu():
    gamestate = 0
    screen.fill ((0, 0, 0))
    text = font.render("The Legend of a Hero", True, colour4)
    screen.blit(text, [230,100])
    pygame.draw.rect(screen, (255, 255, 255), (300, 300, 400, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 500, 400, 100))
    text2 = font2.render("Play", True, blk)
    text3 = font2.render("How to play", True, blk)
    screen.blit(text2, [440,320])
    screen.blit(text3, [370,520])
def rungame():
    screen.fill((255,255,0))
    
def howto():
    screen.fill((0, 0, 0))
    text4 = font2.render("Controls and shit", True, (255, 255, 255,))
    text5 = font2.render("back", True, (0, 0, 0,))
    pygame.draw.rect(screen, (255, 255, 255), (300, 700, 400, 100))
    screen.blit(text5, [440,700])
    screen.blit(text4, [340,120])
#################################### GLOBAL VARIABLES #########################
pygame.init()
screen = pygame.display.set_mode([1000,800])
pygame.display.set_caption("")
colour1 = (0, 102, 255)
colour2 = (255, 0, 102)
colour3 = (0, 153, 51)
colour4 = (255, 0, 0)
colour4 = (0, 255, 0)
blk = (0, 0, 0)
font = pygame.font.SysFont("Aharoni", 70, bold=True, italic=True)
font2 = pygame.font.SysFont("Aharoni", 50, bold=False, italic=False)
gamestate = 0
click = False
gamestate = 0
timer = 0

#################################### GAME LOOP ################################
while True:
    done = False
    # ============================== HANDLE EVENTS  ========================= #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break
        x, y = pygame.mouse.get_pos()
        
        #check if mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
         #INSERT EVENTS HERE
                
    if done == True:
        break
    # ============================== MOVE STUFF ============================= #


    if gamestate == 0:
        menu()
    if gamestate == 1:
        rungame()
    if gamestate == 2:
        howto()
    # ============================== COLLISION ============================== #
    if click and gamestate == 0:
        if 300 <= x <= 700 and 300 <= y <= 400:
            gamestate = 1
            
        if 300 <= x <= 700 and 500 <= y <= 600:
            gamestate = 2
            
            
    if click and gamestate == 2:
        if 300 <= x <= 700 and 700 <= y <= 800:
            gamestate = 0
    
            
    
        
  
  
    # ============================== DRAW STUFF ============================= #                               
    
    
        
    



   
    
    # ============================== SOUND EFFECTS (OPTIONAL) =============== #

    # ============================== PYGAME STUFF =========================== #
    pygame.display.flip()
    pygame.time.delay(20)
