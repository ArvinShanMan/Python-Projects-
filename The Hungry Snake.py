import pygame
import sys
import time
import random


speed = 10
frames_Xaxis = 600
frames_Yaxis = 400
block_size = 10

check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Sorry Error found " + check_errors[1])
else:
    print("Game opened succesfully")


#game window making

pygame.display.set_caption("The Hungry Snake")
game_wind = pygame.display.set_mode((frames_Xaxis, frames_Yaxis))

#color of game

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
Cyan = pygame.Color(0, 255, 255)
Yellow = pygame.Color(255, 255, 0)

fps_controller = pygame.time.Clock()

#snake size

def init_vars():
    global snake_body, hed_pos, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    hed_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [random.randrange(1,(frames_Xaxis // block_size)) * block_size,
                random.randrange(1,(frames_Yaxis // block_size)) * block_size]
    food_spawn = True
    score = 0

init_vars()

def show_score(choice, color, font, size):
    global game_wind
    font_name = 'Arial' #font name
    font_size = 36 #font size
    score_font = pygame.font.SysFont(font_name, font_size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frames_Xaxis / 10, 15)
    else:
        score_rect.midtop = (frames_Xaxis/2, frames_Yaxis/1.25)

    game_wind.blit(score_surface, score_rect)


#game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("W")
            and direction != "DOWN"):
                direction = "UP"
            elif ( event.key == pygame.K_DOWN or event.key == ord("s")
                  and direction != "UP"):
                direction = "DOWN"
            elif  ( event.key == pygame.K_LEFT or event.key == ord("a") 
                and direction != "RIGHT"):
                direction = "LEFT"
            elif  ( event.key == pygame.K_RIGHT or event.key == ord("d") 
                and direction != "LEFT"):
                direction = "RIGHT"
    
    if direction == "UP":
        hed_pos[1] -= block_size
    elif direction == "DOWN":
        hed_pos[1] += block_size
    elif direction == "LEFT":
        hed_pos[0] -= block_size
    else:
        hed_pos[0] += block_size
        
    if hed_pos[0] < 0:
        hed_pos[0] = frames_Xaxis - block_size
    elif hed_pos[0] > frames_Xaxis - block_size:
        hed_pos[0] = 0
    elif hed_pos[1] < 0:
        hed_pos[1] = frames_Yaxis - block_size
    elif hed_pos[1] > frames_Yaxis - block_size:
        hed_pos[1] = 0
        
    #eating apple
    snake_body.insert(0, list(hed_pos))
    if hed_pos[0] == food_pos[0] and hed_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # spawn food
    if not food_spawn:
        food_pos = [random.randrange(1,(frames_Xaxis // block_size)) * block_size, 
            random.randrange(1,(frames_Yaxis // block_size)) * block_size]
        food_spawn = True

    # GFX
    game_wind.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_wind, white, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            block_size -2, block_size -2 ))
        
    pygame.draw.rect(game_wind,red, pygame.Rect(food_pos[0], 
                    food_pos[1], block_size, block_size))
    
    # game over condiditons

    for block in snake_body[1:]:
        if hed_pos[0] == block[0] and hed_pos[1] == block[1]:
            init_vars()

    show_score(1,Cyan, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)
