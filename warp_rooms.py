#Dean.k and Gary.L|2/25/30
import pygame
import math
pygame.init()
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800,800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

# CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
map = [True, False]

# MAP: 2 is brick
map1 = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]

map2 = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]


brick2 = pygame.image.load('brick2.png')
brick2 = pygame.transform.scale(brick2, (40,40))
door1 = pygame.image.load('door1.png')
door1 = pygame.transform.scale(door1, (40,40))
brick = pygame.image.load('brick.png')  # load your spritesheet
Link = pygame.image.load('link.png')  # load your spritesheet
Link.set_colorkey((255, 0, 255))  # this makes bright pink (255, 0, 255) transparent (sort of)

# player variables
xpos = 400  # xpos of player
ypos = 400  # ypos of player

# animation variables variables
frameWidth = 13
frameHeight = 20
RowNum = 0  # for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

def collide(mapnum, blocknum, xpos, ypos):
            #left collision
        if mapnum[int((ypos) / 40)][int((xpos - 5) / 40)] == blocknum:
            xpos+=3
            print("left collision!")
       
        #right collision
        if mapnum[int((ypos) / 40)][int((xpos + 15) / 40)] == blocknum:
            xpos-=3   
            print("right collision!")
    
        #UP collision
        if mapnum[int((ypos-3)/40)][int((xpos) / 40)] == blocknum:
            ypos+=3   
            print("up collision!")
    
        #down collision
        if mapnum[int((ypos+15)/40)][int((xpos) / 40)] == blocknum:
            ypos-=3   
            print("down collision!")

while not gameover:
    clock.tick(60)  # FPS

    for event in pygame.event.get():  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        #keyboard input---------------------------
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False




    #Left/right MOVEMENT-------------------------------------
    if keys[LEFT] == True:
        vx = -3
        RowNum = 0
        direction = LEFT

    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 1
        direction = RIGHT
    else:
        vx = 0
   
    if keys[UP] == True:
        vy = -3
        RowNum = 2
        direction = UP
    
    elif keys[DOWN] == True:
        vy = 3
        RowNum = 3
        direction = DOWN
        
    else:
        vy = 0

    #map collision---------------------
    if map[0] == True:
        #left collision
        if map1[int((ypos) / 40)][int((xpos - 5) / 40)] == 2:
            xpos+=3
            print("left collision!")
       
        #right collision
        if map1[int((ypos) / 40)][int((xpos + 15) / 40)] == 2:
            xpos-=3   
            print("right collision!")
    
        #UP collision
        if map1[int((ypos-3)/40)][int((xpos) / 40)] == 2:
            ypos+=3   
            print("up collision!")
    
        #down collision
        if map1[int((ypos+15)/40)][int((xpos) / 40)] == 2:
            ypos-=3   
            print("down collision!")
        ############################################################  MAP 2
            #right collision
        if map1[int((ypos) / 40)][int((xpos + 15) / 40)] == 4:
            map[0] = False
            map[1] = True
            xpos = 100 #update player xpos
            ypos = 325
            print("right collision!")
        collide(map1, 3, xpos, ypos)
    elif map[1] == True:
        if map2[int((ypos) / 40)][int((xpos - 5) / 40)] == 4:
            map[1] = False
            map[0] = True
            xpos = 750 #update player xpos
            ypos = 325
            print("go to ROOM 11111111")
        if map1[int((ypos) / 40)][int((xpos - 5) / 40)] == 2:
            xpos+=3
            print("left collision222222!")
       
        #right collision
        if map2[int((ypos) / 40)][int((xpos + 15) / 40)] == 2:
            xpos-=3   
            print("right collision22222!")
    
        #UP collision
        if map2[int((ypos-3)/40)][int((xpos) / 40)] == 2:
            ypos+=3   
            print("up collision22222!")
    
        #down collision
        if map2[int((ypos+15)/40)][int((xpos) / 40)] == 2:
            ypos-=3   
            print("down collision22222!")
        if map1[int((ypos) / 40)][int((xpos - 5) / 40)] == 3:
            xpos+=3
            print("left collision222222!")
       
        #right collision
        if map2[int((ypos) / 40)][int((xpos + 15) / 40)] == 3:
            xpos-=3   
            print("right collision22222!")
    
        #UP collision
        if map2[int((ypos-3)/40)][int((xpos) / 40)] == 3:
            ypos+=3   
            print("up collision22222!")
    
        #down collision
        if map2[int((ypos+15)/40)][int((xpos) / 40)] == 3:
            ypos-=3   
            print("down collision22222!")
        
        


    xpos+=vx #update player xpos
    ypos+=vy

    # Animation update
    ticker+=1
    if vx != 0: #only animate when moving
        if ticker % 10 == 0:  # only change frames every 10 ticks (make number smaller for faster running animation)
            frameNum += 1
    if vy != 0: #only animate when moving
        if ticker % 10 == 0:  # only change frames every 10 ticks (make number smaller for faster running animation)
            frameNum += 1
    if frameNum > 7:
        frameNum = 0

    # Render section--------------------------------------------------------
    screen.fill((0, 0, 0))  # wipe screen so it doesn't smear
    # draw map
    if map[0] == True:
        for i in range(20):
            for j in range(20):
                if map1[i][j] == 2:
                    screen.blit(brick, (j * 40, i * 40), (0, 0, 40, 40))
                
                elif map1[i][j] == 3:
                    screen.blit(brick2, (j * 40, i * 40), (0, 0, 40, 40))
                elif map1[i][j] == 4:
                    screen.blit(door1, (j * 40, i * 40), (0, 0, 40, 40))
    elif map[1] == True:
        for i in range(20):
            for j in range(20):
                if map2[i][j] == 2:
                    screen.blit(brick, (j * 40, i * 40), (0, 0, 40, 40))
                
                elif map2[i][j] == 3:
                    screen.blit(brick2, (j * 40, i * 40), (0, 0, 40, 40))
                elif map2[i][j] == 4:
                    screen.blit(door1, (j * 40, i * 40), (0, 0, 40, 40))

    # draw player
    screen.blit(Link, (xpos, ypos), (frameWidth * frameNum, RowNum * frameHeight, frameWidth, frameHeight))
    pygame.display.flip()  # this actually puts the pixel on the screen

# end game loop
pygame.quit()
