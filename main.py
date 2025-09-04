import pygame
import numpy as np
import sys
from init import *
from constants import *
from objects import *
from function import show, circle, cross, check_state, restart


def show():
    for sq in sq_list:
        pygame.draw.rect(game_display, COLOR, sq)

turn = True
show()
allow = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and allow:
            position = pygame.mouse.get_pos()
            for sq in range(len(sq_list)):
                if sq_list[sq].collidepoint(position):
                    row, col = sq//3, sq%3
                    if Game_board[row][col]==0:
                        if turn:
                            circle(sq)
                            Game_board[row][col]=int(turn)
                            turn = not turn
                        else:
                            cross(sq)
                            Game_board[row][col]=int(turn)+2
                            turn = not turn
    pygame.display.update()
    if allow:
        state = check_state(Game_board)
        if state!="Continue":
            if state!="Tie":
                print(f"Player {state} Won!")
            else:
                print("Tie")
            
            if input("Do you want to play again? (y, n)") == "y":
                Game_board = restart()
                turn = True
                show()
            else:
                allow = False
