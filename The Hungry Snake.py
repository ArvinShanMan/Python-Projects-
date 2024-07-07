import pygame
import sys
import time
import random


speed = 15
frames_Xaxis = 780
frames_Yaxis = 480
block_size = 50

check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Sorry Error found " + check_errors[1])
else:
    print("Game opened succesfully")


#game window making

pygame.display.set_caption("The Hungry Snake")
pygame.display.set_mode((frames_Xaxis, frames_Yaxis))

#color of game

green = pygame.Color(0, 255, 0)
Blue = pygame.Color(0, 0, 255)
Cyan = pygame.Color(0, 255, 255)
Yellow = pygame.Color(255, 255, 0)

fps_controller = pygame.time.Clock()

#snake size

def init_vars():
    global snake_body, hed_pos, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    hed_pos = [130,50]
    snake_body = [[130,50]]
    food_pos = [random.randrange(1,(frames_Xaxis // block_size)) * block_size,
                random.randrange(1,(frames_Yaxis // block_size)) * block_size]
    food_spawn = True
    score = 0

init_vars()

def show_score(choice, color, font, size):
    global game_window
    font_name = 'Arial' #font name
    font_size = 36 #font size
    score_font = pygame.font.SysFont(font_name, font_size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frames_Xaxis / 10, 15)
    else:
        score_rect.midtop = (frames_Xaxis/2, frames_Yaxis/1.25)

    game_window.blit(score_surface, score_rect)