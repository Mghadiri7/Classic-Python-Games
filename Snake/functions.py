import pygame
from random import randint as rnd
from constants import *

def show(Surface, snake, food):
    for sq in snake:
        pygame.draw.rect(Surface, WHITE, 
                         (sq[0]*TILE_SIZE, sq[1]*TILE_SIZE, 
                         TILE_SIZE, TILE_SIZE), 2)
    pygame.draw.rect(Surface, RED, 
                     (food[0]*TILE_SIZE, food[1]*TILE_SIZE, 
                      TILE_SIZE, TILE_SIZE))
        
def update(snake, food, direction, alive, speed):
    if direction=="RIGHT":
        if snake[-1][0]+1>W_T-1:
            snake.append([0, snake[-1][1]])
        else:
            snake.append([snake[-1][0]+1, snake[-1][1]])
    elif direction=="LEFT":
        if snake[-1][0]-1<0:
            snake.append([W_T-1, snake[-1][1]])
        else:
            snake.append([snake[-1][0]-1, snake[-1][1]])
    elif direction=="UP":
        if snake[-1][1]-1<0:
            snake.append([snake[-1][0], W_T-1])
        else:
            snake.append([snake[-1][0], snake[-1][1]-1])
    elif direction=="DOWN":
        if snake[-1][1]+1>W_T-1:
            snake.append([snake[-1][0], 0])
        else:
            snake.append([snake[-1][0], snake[-1][1]+1])
    if food not in snake and alive:
        snake.pop(0)
    else:
        if alive:
            food = generate_food(snake)
            if speed>10:
                pass
            else:
                speed+=1
    if snake[-1] in snake[:-1]:
        alive = False
    return snake, food, alive, speed

def generate_food(snake):
    food = [rnd(0, W_T-1), rnd(0, W_T-1)]
    while food in snake:
        food = [rnd(0, W_T-1), rnd(0, W_T-1)]
    return food

def restart():
    snake = [[0, W_T//2],
         [1, W_T//2],
         [2, W_T//2]]
    food = generate_food(snake)
    direction = "RIGHT"
    alive = True
    speed = SPEED
    return snake, food, direction, alive, speed