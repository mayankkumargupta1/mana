import pygame
screen = pygame.display.set_mode((500,500))
player = pygame.image.load('assets/player.png')
x = 250
y = 250
#enemy 1
enemy_x1 = 0
enemy_y1 = 0
#enemy 2
enemy_x2 = 250
enemy_y2 = 0
#enemy 3
enemy_x3 = 500
enemy_y3 = 0
#enemy 4
enemy_x4 = 0
enemy_y4 = 250
#enemy 5
enemy_x5 = 0
enemy_y5 = 500
#enemy 6
enemy_x6 = 500
enemy_y6 = 250
#enemy 7
enemy_x7 = 500
enemy_y7 = 500



width = 10
height = 10
runing = True 
WHITE   = (255,255,255)
fps = 60

game_state = True 

enemy_speed = 1
score = 0

    

def player_movement(keys,plt,game_state):
    
    global x
    global y
    global bullet_y3,bullet_y4,bullet_x1,bullet_x2,bullet_width,bullet_heigth,bullet_frame,bullet_y1,bullet_y2,bullet_x3,bullet_x4

    if game_state:
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            x -= 20
            y -= 20
        

def enemy_dead1():
    global enemy_x1 , enemy_y1   
    enemy_x1 = 0
    enemy_y1 = 0 
    
def enemy1(enemy_speed):
    global width , height , enemy_x1 , enemy_y1 , game_state
    
    enemy1 = pygame.draw.rect(screen,(0,0,255),(enemy_x1,enemy_y1,10,10))

    
    
    
    if enemy_x1 == x and enemy_y1 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x1 + 10 == x and  enemy_y1 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x1 - 10 == x and  enemy_y1 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y1 + 10 == y and enemy_x1 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y1 - 10 == y and enemy_x1 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x1 < x : 
        enemy_x1 += enemy_speed
    if enemy_y1 < y : 
        enemy_y1 += enemy_speed
    if enemy_x1 > x : 
        enemy_x1 -= enemy_speed
    if enemy_y1 > y : 
        enemy_y1 -= enemy_speed

def enemy2(enemy_speed):
    global width , height , enemy_x2 , enemy_y2 , game_state
    
    enemy2 = pygame.draw.rect(screen,(0,0,255),(enemy_x2,enemy_y2,10,10))

    
    
    
    if enemy_x2 == x and enemy_y2 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x2 + 10 == x and  enemy_y2 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x2 - 10 == x and  enemy_y2 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y2 + 10 == y and enemy_x2 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y2 - 10 == y and enemy_x2 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x2 < x : 
        enemy_x2 += enemy_speed
    if enemy_y2 < y : 
        enemy_y2 += enemy_speed
    if enemy_x2 > x : 
        enemy_x2 -= enemy_speed
    if enemy_y2 > y : 
        enemy_y2 -= enemy_speed
            

        
def enemy3(enemy_speed):
    global width , height , enemy_x3 , enemy_y3 , game_state
    
    enemy3 = pygame.draw.rect(screen,(0,0,255),(enemy_x3,enemy_y3,10,10))

    
    
    
    if enemy_x3 == x and enemy_y3 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x3 + 10 == x and  enemy_y3 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x3 - 10 == x and  enemy_y3 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y3 + 10 == y and enemy_x3 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y3 - 10 == y and enemy_x3 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x3 < x : 
        enemy_x3 += enemy_speed
    if enemy_y3 < y : 
        enemy_y3 += enemy_speed
    if enemy_x3 > x : 
        enemy_x3 -= enemy_speed
    if enemy_y3 > y : 
        enemy_y3 -= enemy_speed

def enemy4(enemy_speed):
    global width , height , enemy_x4 , enemy_y4 , game_state
    
    enemy4 = pygame.draw.rect(screen,(0,0,255),(enemy_x4,enemy_y4,10,10))

    
    
    
    if enemy_x4 == x and enemy_y4 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x4 + 10 == x and  enemy_y4 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x4 - 10 == x and  enemy_y4 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y4 + 10 == y and enemy_x4 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y4 - 10 == y and enemy_x4 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x4 < x : 
        enemy_x4 += enemy_speed
    if enemy_y4 < y : 
        enemy_y4 += enemy_speed
    if enemy_x4 > x : 
        enemy_x4 -= enemy_speed
    if enemy_y4 > y : 
        enemy_y4 -= enemy_speed

def enemy5(enemy_speed):
    global width , height , enemy_x5 , enemy_y5 , game_state
    
    enemy5 = pygame.draw.rect(screen,(0,0,255),(enemy_x5,enemy_y5,10,10))

    
    
    
    if enemy_x5 == x and enemy_y5 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x5 + 10 == x and  enemy_y5 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x5 - 10 == x and  enemy_y5 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y5 + 10 == y and enemy_x5 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y5 - 10 == y and enemy_x5 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x5 < x : 
        enemy_x5 += enemy_speed
    if enemy_y5 < y : 
        enemy_y5 += enemy_speed
    if enemy_x5 > x : 
        enemy_x5 -= enemy_speed
    if enemy_y5 > y : 
        enemy_y5 -= enemy_speed

def enemy6(enemy_speed):
    global width , height , enemy_x6 , enemy_y6 , game_state
    
    enemy6 = pygame.draw.rect(screen,(0,0,255),(enemy_x6,enemy_y6,10,10))

    
    
    
    if enemy_x6 == x and enemy_y6 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x6 + 10 == x and  enemy_y6 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x6 - 10 == x and  enemy_y6 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y6 + 10 == y and enemy_x6 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y6 - 10 == y and enemy_x6 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x6 < x : 
        enemy_x6 += enemy_speed
    if enemy_y6 < y : 
        enemy_y6 += enemy_speed
    if enemy_x6 > x : 
        enemy_x6 -= enemy_speed
    if enemy_y6 > y : 
        enemy_y6 -= enemy_speed

def enemy7(enemy_speed):
    global width , height , enemy_x7 , enemy_y7 , game_state
    
    enemy7 = pygame.draw.rect(screen,(0,0,255),(enemy_x7,enemy_y7,10,10))

    
    
    
    if enemy_x7 == x and enemy_y7 == y :
        game_state = False 
        width = 0
        height = 0
    if enemy_x7 + 10 == x and  enemy_y7 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_x7 - 10 == x and  enemy_y7 == y:
        game_state = False 
        width = 0
        height = 0
    if enemy_y7 + 10 == y and enemy_x7 == x :
        game_state = False 
        width = 0
        height = 0
    if enemy_y7 - 10 == y and enemy_x7 == x :
        game_state = False 
        width = 0
        height = 0
                                                                                    

    if enemy_x7 < x : 
        enemy_x7 += enemy_speed
    if enemy_y7 < y : 
        enemy_y7 += enemy_speed
    if enemy_x7 > x : 
        enemy_x7 -= enemy_speed
    if enemy_y7 > y : 
        enemy_y7 -= enemy_speed


i = 0

while runing :
    clock = pygame.time.Clock()
    clock.tick(fps)
    
    plt = pygame.Rect(x,y,width,height)
    artificial_player = pygame.transform.scale(player,(width,height))
    

    
    
    

    if x < 11 or y < 11 or x > 481 or y > 481:
        game_state = False 
        width = 0
        height = 0
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
        keys = pygame.key.get_pressed()
        player_movement(keys,plt,game_state)
    

        
        
        
    # enemy 
    i += 1
    screen.fill(WHITE)
    pygame.draw.rect(screen,(0, 0,0),(0,0,10,500))
    pygame.draw.rect(screen,(0, 0,0),(0,0,500,10))
    pygame.draw.rect(screen,(0, 0,0),(0,490,500,10))
    pygame.draw.rect(screen,(0, 0,0),(490,0,10,500))
    
    if enemy_x1 == enemy_x2 and enemy_y1 == enemy_y2:
        enemy_speed += 1
        score += 5
        enemy_x2 = 250
        enemy_y2 = 0 
    if enemy_x2 == enemy_x3 and enemy_y2 == enemy_y3:
        enemy_speed += 1
        score += 5
        enemy_x3 = 500
        enemy_y3 = 0
    if enemy_x3 == enemy_x4 and enemy_y3 == enemy_y4:
        enemy_speed += 1
        score += 5
        enemy_x4 = 0
        enemy_y4 = 250
    if enemy_x4 == enemy_x5 and enemy_y4 == enemy_y5:
        enemy_speed += 1
        score += 5
        enemy_x5 = 0
        enemy_y5 = 500
    if enemy_x5 == enemy_x6 and enemy_y5 == enemy_y6:
        enemy_speed += 1
        score += 5
        enemy_x6 = 500
        enemy_y6 = 250
    if enemy_x6 == enemy_x7 and enemy_y6 == enemy_y7:
        enemy_speed += 1
        score += 5
        enemy_x7 = 500
        enemy_y7 = 500

    
    if enemy_x1 == enemy_x7 and enemy_y1 == enemy_y7:
        enemy_speed += 1
        score += 5
        enemy_x7 = 500
        enemy_y7 = 500 
    if enemy_x2 == enemy_x6 and enemy_y2 == enemy_y6:
        enemy_speed += 1
        score += 5
        enemy_x6 = 500
        enemy_y6 = 250
    if enemy_x3 == enemy_x5 and enemy_y3 == enemy_y5:
        enemy_speed += 1
        score += 5
        enemy_x5 = 0
        enemy_y5 = 500
    if enemy_x4 == enemy_x1 and enemy_y4 == enemy_y1:
        enemy_speed += 1
        score += 5
        enemy_x1 = 0
        enemy_y1 = 0
    if enemy_x5 == enemy_x6 and enemy_y5 == enemy_y6:
        enemy_speed += 1
        score += 5
        enemy_x6 = 500
        enemy_y6 = 250
    if enemy_x6 == enemy_x7 and enemy_y6 == enemy_y7:
        enemy_speed += 1
        score += 5
        enemy_x7 = 500
        enemy_y7 = 500

    if enemy_speed == 4:
        enemy_speed = 1
    if i/10 == 60:
        enemy_speed = 1
    if i/10 == 30:
        enemy_speed = 6

    if i/10 == 90:
        enemy_speed = 4
        i = 0
        enemy_x7 = 500
        enemy_y7 = 500
        enemy_x6 = 500
        enemy_y6 = 250
        enemy_x1 = 0
        enemy_y1 = 0
        enemy_x5 = 0
        enemy_y5 = 500
        enemy_x2 = 250
        enemy_y2 = 0 
        enemy_x3 = 500
        enemy_y3 = 0


    enemy1(enemy_speed)
    enemy2(enemy_speed)
    enemy3(enemy_speed)
    enemy4(enemy_speed)
    enemy5(enemy_speed)
    enemy6(enemy_speed)
    enemy7(enemy_speed)


    screen.blit(artificial_player,(plt.x,plt.y))
    pygame.display.update()