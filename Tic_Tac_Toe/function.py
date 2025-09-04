import pygame
import numpy as np
from init import *
from objects import *
from constants import *

def show():
    for sq in sq_list:
        pygame.draw.rect(game_display, COLOR, sq)

def circle(i):
    row, col = i//3, i%3
    pygame.draw.circle(game_display, RED, 
                       (10*(col+1)+(SIZE*col)+HALF, 10*(row+1)+(SIZE*row)+HALF), 35, 8)

def cross(i):
    row, col = i//3, i%3
    pygame.draw.line(game_display, BLUE, 
                     (10*(col+1)+(SIZE*col)+OFFSET, 10*(row+1)+(SIZE*row)+OFFSET), 
                     (10*(col+1)+(SIZE*col)+(SIZE-OFFSET), 10*(row+1)+(SIZE*row)+(SIZE-OFFSET)), 8)
    pygame.draw.line(game_display, BLUE, 
                     (10*(col+1)+(SIZE*col)+(SIZE-OFFSET), 10*(row+1)+(SIZE*row)+OFFSET), 
                     (10*(col+1)+(SIZE*col)+OFFSET, 10*(row+1)+(SIZE*row)+(SIZE-OFFSET)), 8)
    
def check_state(gb):
    for i in range(3):
        row = np.unique(gb[:,i])
        col = np.unique(gb[i,:])
        if len(row)==1 and row!=0:
            return row
        if len(col)==1 and col!=0:
            return col
    if gb[0][0]==gb[1][1] and gb[1][1]==gb[2][2] and gb[1][1]!=0:
        return gb[1][1]
    elif gb[2][0]==gb[1][1] and gb[1][1]==gb[0][2] and gb[1][1]!=0:
        return gb[1][1]
    
    if 0 not in np.unique(gb):
        return "Tie"
    return "Continue"

def restart():
    return np.array([[0,0,0], [0,0,0], [0,0,0]])