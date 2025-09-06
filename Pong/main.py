import pygame
import sys
from init import *
from constants import *
from objects import *
from functions import update_player, update_score, opponent_paddle_update, draw


clock = pygame.time.Clock()
player_score = 0
opponent_score = 0
collision = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    player = update_player(player, keys)

    if ball.bottom>HEIGHT-5 or ball.top<5:
        ball_yd*=-1
    if (ball.colliderect(player) and not collision) or (
        ball.colliderect(opponent) and collision):
        ball_xd*=-1
        collision = not collision

    ball.x+=ball_xd
    ball.y+=ball_yd

    player_score, opponent_score, ball.x, ball.y = update_score(player, opponent,
                                                                ball, player_score, opponent_score)
    opponent.y = opponent_paddle_update(opponent, ball)
    game_display.fill(GREEN)
    draw(player, opponent, ball, player_score, opponent_score)
    pygame.display.update()
    clock.tick(50)
