import pygame
from init import game_display
from objects import FONT
from constants import *


def show_score(Surface, _str, color, which_p):
    str_obj = FONT.render(_str, True, color)
    position = list(str_obj.get_size())
    if which_p:
        position[0] = (WIDTH//2)-position[0]-20
    else:
        position[0] = (WIDTH//2)+20
    Surface.blit(str_obj, position)

def update_player(player, keys):
    if keys[pygame.K_UP] and player.top>5:
        player.y-=PADDLE_SPEED
    if keys[pygame.K_DOWN] and player.bottom<HEIGHT-5:
        player.y+=PADDLE_SPEED
    return player

def update_score(player, opponent, ball, player_score, opponent_score):
    if ball.center[0]>player.right or ball.x>WIDTH:
        opponent_score+=1
        ball.x, ball.y = WIDTH//2-BALL_SIZE[0]//2, HEIGHT//2-BALL_SIZE[1]//2    
    elif ball.center[0]<opponent.left or ball.x<0:
        player_score+=1
        ball.x, ball.y = WIDTH//2-BALL_SIZE[0]//2, HEIGHT//2-BALL_SIZE[1]//2
    return player_score, opponent_score, ball.x, ball.y

def opponent_paddle_update(opponent, ball):
    if opponent.center[1]<ball.center[1] and opponent.bottom<HEIGHT-5:
        opponent.y+=PADDLE_SPEED
    elif opponent.center[1]>ball.center[1] and opponent.top>5:
        opponent.y-=PADDLE_SPEED
    return opponent.y

def draw(player, opponent, ball, player_score, opponent_score):
    show_score(game_display, str(opponent_score), BLUE, True)
    show_score(game_display, str(player_score), BLUE, False)
    pygame.draw.ellipse(game_display, RED, ball)
    pygame.draw.rect(game_display, WHITE, player)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.line(game_display, WHITE, 
                     (WIDTH//2-1, 0), (WIDTH//2-1, HEIGHT), 2)
