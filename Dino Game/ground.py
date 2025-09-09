import pygame

prefix = "./Assets/"

class GND:
    img = pygame.image.load(prefix+"new_desert.png")
    def __init__(self, speed, location):
        self.speed = speed
        self.locs = [[0,location], [2000,location]]

    def update(self, Surface, state):
        if state:
            #move
            self.locs[0][0]-=self.speed
            self.locs[1][0]-=self.speed
            if self.locs[0][0] == -2000:
                self.locs[0][0] = 2000
            if self.locs[1][0] == -2000:
                self.locs[1][0] = 2000
            #show
        Surface.blit(self.img, self.locs[0])
        Surface.blit(self.img, self.locs[1])