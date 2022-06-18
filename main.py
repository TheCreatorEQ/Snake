import pygame, random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_UP, K_DOWN, K_RIGHT, K_LEFT , K_SPACE

pygame.init()

WIDTH = 750
HEIGHT = 750
SIZE = (WIDTH, HEIGHT)
is_alive = True
framecount = 0
light_green = (0,225,0)
dark_green = (0,200,0)
red = (255,0,0)
grid = [[0 for i in range(15)] for i in range(15)] 
# 0 = empty tile
# 1 = snake
snake = [[5, 7], [6, 7], [7, 7]] # LEFT is tail, RIGHT is head
for i in snake:
    grid[i[1]][i[0]] = 1
direction = "E"
apple_x = 12
apple_y = 7
font = pygame.font.SysFont("Comic Sans MS", 20)
font2 = pygame.font.SysFont('Comic Sans MS', 75)
speed = 2
score = 0
surface = pygame.display.set_mode((WIDTH, HEIGHT))
myfont1 = pygame.font.SysFont('Comic Sans MS', 200 )
myfont2 = pygame.font.SysFont('Comic Sans MS', 50 )
textsurface = myfont1.render('Snake', False, (255, 255, 255))
slow1 = myfont2.render('Slow', False, (255, 0, 0))
medium1 = myfont2.render('Normal', False, (255, 0, 0))
fast1 = myfont2.render('Fast', False, (255, 0, 0))
slow2 = myfont2.render('Slow', False, (0, 255, 0))
medium2 = myfont2.render('Normal', False, (0, 255, 0))
fast2 = myfont2.render('Fast', False, (0, 255, 0))
startmenu = True
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

if startmenu == True: 
  
    def start():
        mpos = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        screen.blit(textsurface,(90,100))
        screen.blit(slow1,(100,420))
        screen.blit(medium1,(290,420))
        screen.blit(fast1,(540,420))
        if mpos[0] >= 100 and mpos[0] <= 210 and mpos[1] >= 430 and mpos[1] <= 480:
            screen.blit(slow2,(100,420))
        if mpos[0] >= 290 and mpos[0] <= 460 and mpos[1] >= 430 and mpos[1] <= 480:
            screen.blit(medium2,(290,420))
        if mpos[0] >= 540 and mpos[0] <= 644 and mpos[1] >= 430 and mpos[1] <= 480:
            screen.blit(fast2,(540,420))
    
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                mpos = pygame.mouse.get_pos()
                if mpos[0] >= 100 and mpos[0] <= 210 and mpos[1] >= 430 and mpos[1] <= 480:
                    startmenu = False
                    speed = 10
                    running = False
                if mpos[0] >= 290 and mpos[0] <= 460 and mpos[1] >= 430 and mpos[1] <= 480:
                    startmenu = False
                    speed = 4
                    running = False
                if mpos[0] >= 540 and mpos[0] <= 644 and mpos[1] >= 430 and mpos[1] <= 480:
                    startmenu = False
                    speed = 2
                    running = False

        screen.fill((255, 255, 255)) 
        start()
        pygame.display.flip()
        clock.tick(30)
if startmenu == False:
    def create_background(): 
        screen.fill(dark_green) 
        flag = True
        for x in range(0, WIDTH, 50):
            for y in range(0, HEIGHT, 50):
                if flag:
                    pygame.draw.rect(screen, light_green, (x, y, 50, 50))
                flag = not flag

    def create_snake(): 
        for i in snake:
            pygame.draw.rect(screen, red, (i[0]*50, i[1]*50, 50, 50))
            pygame.draw.polygon(screen, (0 ,0 ,0), ((i[0]*50, i[1]*50), (i[0]*50 + 3, i[1]*50 + 3), (i[0]*50 + 50, i[1]*50), (i[0]*50 + 47, i[1]*50 + 3), (i[0]*50, i[1]*50 + 50), (i[0]*50 + 3, i[1]*50 + 47), (i[0]*50 + 47, i[1]*50 + 47), (i[0]*50 + 50, i[1]*50 + 50)))#kevin w
    
    def your_score(score):
        global surface
        value = myfont2.render("Your Score: " + str(score), True, (255, 255, 255))
        surface.blit(value, [20, 0])
    
    def game_over():
        screen.fill((0, 0, 0))
        gameover_msg = font2.render(("Game Over"), True, (255, 255, 255))
        surface.blit(gameover_msg, [200, 280])
        play_again = font.render(("Press SPACE to play again"), True, (255, 0, 0))
        surface.blit(play_again, [250, 400])
        
    def add_snake(): 
        snake.insert(0, ([snake[0][0], snake[0][1]]))

    def update(): 
        global score, is_alive
        for i in range(15):
            for j in range(15): 
                grid[i][j] = 0
        score = len(snake) - 3
        your_score(score)
        for i in snake:
            if i[0] < 0 or i[0] > 14 or i[1] < 0 or i[1] > 14:
                is_alive = False
            else:
                grid[i[1]][i[0]] = 1
        x, y = snake[-1][0], snake[-1][1]
        if direction == "E":
            if x+1 < 15 and grid[y][x+1] == 1:
                is_alive = False
        elif direction == "W":
            if x-1 >= 0 and grid[y][x-1] == 1:
                is_alive = False
        elif direction == "N":
            if y-1 >= 0 and grid[y-1][x] == 1:
                is_alive = False
        elif direction == "S":
            if y+1 < 15 and grid[y+1][x] == 1:
                is_alive = False
        
    def printGrid(): 
        for a in grid:
            print(a)

       
    def draw_head(headpos):
        if direction == 'N':
            pygame.draw.polygon(screen, (255,150,0), [(headpos[0]-15,headpos[1]+20),(headpos[0]+65,headpos[1]+20),(headpos[0]+25,headpos[1]-40)])
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+15,headpos[1]), 5)
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+35,headpos[1]), 5)
        elif direction == 'S':
            pygame.draw.polygon(screen, (255,150,0), [(headpos[0]-15,headpos[1]+30),(headpos[0]+65,headpos[1]+30),(headpos[0]+25,headpos[1]+90)])
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+15,headpos[1]+50), 5)
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+35,headpos[1]+50), 5)
        elif direction == 'W':
            pygame.draw.polygon(screen, (255,150,0), [(headpos[0]+20,headpos[1]-15),(headpos[0]+20,headpos[1]+65),(headpos[0]-40,headpos[1]+25)])
            pygame.draw.circle(screen, (255,0,255), (headpos[0],headpos[1]+15), 5)
            pygame.draw.circle(screen, (255,0,255), (headpos[0],headpos[1]+35), 5)
        elif direction == 'E':
            pygame.draw.polygon(screen, (255,150,0), [(headpos[0]+30,headpos[1]-15),(headpos[0]+30,headpos[1]+65),(headpos[0]+90,headpos[1]+25)])
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+50,headpos[1]+15), 5)
            pygame.draw.circle(screen, (255,0,255), (headpos[0]+50,headpos[1]+35), 5)


    running = True
    while running:
        #Leo Gao
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    if direction != 'S':
                        direction = 'N'
                elif event.key == K_DOWN:
                    if direction != 'N':
                        direction = 'S'
                elif event.key == K_RIGHT:
                    if direction != 'W':
                        direction = 'E'
                elif event.key == K_LEFT:
                    if direction != 'E':
                        direction = 'W'
                elif event.key == K_SPACE:
                    snake = [[5, 7], [6, 7], [7, 7]]
                    direction = "E"
                    is_alive = True
            elif event.type == QUIT:
                running = False
        
 
        if not is_alive:
            game_over()
            framecount += 1
            pygame.display.flip()
            clock.tick(30)
            continue
     
        create_background()
        if framecount % speed == 0:
            if direction == "E":
                snake.pop(0)
                snake.append([snake[-1][0]+1, snake[-1][1]])
            elif direction == "W":
                snake.pop(0)
                snake.append([snake[-1][0]-1, snake[-1][1]])
            elif direction == "N":
                snake.pop(0)
                snake.append([snake[-1][0], snake[-1][1]-1])
            elif direction == "S":
                snake.pop(0)
                snake.append([snake[-1][0], snake[-1][1]+1])
        
        if [apple_x, apple_y] == snake[-1]:
            add_snake()
            
            apple_x = random.randint(0,14)
            apple_y = random.randint(0,14)
            while grid[apple_y][apple_x] == 1:
                apple_x = random.randint(0,14)
                apple_y = random.randint(0,14)
        
        pygame.draw.rect(screen, (255, 255, 0), (apple_x * 50, apple_y * 50, 50, 50))
        create_snake()
        update()
        draw_head((snake[-1][0]*50,snake[-1][1]*50))

        framecount += 1


        pygame.display.flip()
        clock.tick(30)
        #---------------------------

pygame.quit() 
