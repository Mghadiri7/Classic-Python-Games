import pygame
from constants import *

sq_list = []
for i in range(3):
    for j in range(3):
        sq_list.append(pygame.Rect(10*(j+1)+(SIZE*j), 10*(i+1)+(SIZE*i), SIZE, SIZE))