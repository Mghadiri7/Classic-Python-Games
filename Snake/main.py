import pygame
import sys
from init import *
from constants import *
from functions import *

direction = "RIGHT"
clock = pygame.time.Clock()
food = generate_food(snake)
alive = True
speed = SPEED
while True:
    game_display.fill(BLACK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction!="LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_LEFT and direction!="RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_UP and direction!="DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction!="UP":
                direction = "DOWN"
            
    snake, food, alive, speed = update(snake, food, direction, alive, speed)
    if not alive:
        direction = ""
        if DELAY==0:
            DELAY = 10
            snake, food, direction, alive, speed = restart()
        DELAY-=1
    show(game_display, snake, food)
    pygame.display.update()
    clock.tick(speed)
