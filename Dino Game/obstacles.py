import pygame
from random import randint as rnd

prefix = "./Assets/"
def load_obj_rects_details(name):
    with open(prefix+name[:-3]+"txt") as file:
        content = file.readlines()
        content = [i.strip() for i in content]
        content = [i.split(",") for i in content]
        content = [[int(j) for j in i] for i in content]
    return content

class Obstacles:
    def __init__(self, y, min_gap, speed):
        self.obs_list = []
        self.y = y
        self.min_gap = min_gap
        self.speed = speed
        self.init_obss()

    def init_obss(self):
        self.obs_list.append(Obstacle((rnd(900, 1000), self.y), self.speed))
        self.obs_list.append(Obstacle((rnd(1350, 1500), self.y), self.speed))
        self.obs_list.append(Obstacle((rnd(2200, 2500), self.y), self.speed))    
    
    def generate_obs(self):
        self.obs_list.append(Obstacle((rnd(2000, 2300), self.y), self.speed))

    def remove(self):
        self.obs_list.pop(0)

    def check(self):
        if self.obs_list[0].x_loc+self.obs_list[0].width<0:
            self.remove()
        if self.obs_list[-1].x_loc+self.obs_list[-1].width+self.min_gap<2000:
            self.generate_obs()

    def update(self, Surface, state):
        for obs in self.obs_list:
            obs.update(Surface, state)

class Obstacle:
    img_list = [["tree1s3.png", load_obj_rects_details("tree1s3.png")],
                 ["tree2s3.png", load_obj_rects_details("tree1s3.png")], 
                 ["tree3s3.png", load_obj_rects_details("tree1s3.png")]]
    def __init__(self, location, speed):
        self.location = location
        self.x_loc, self.y_loc = location
        self.speed = speed
        self.type = rnd(0, len(self.img_list)-1)
        self.img = pygame.image.load(prefix+self.img_list[self.type][0])
        self.width = self.img.get_width()
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = self.x_loc, self.y_loc
        self.rects = self.create_rects()

    def create_rects(self):
        rects = []
        for rect_details in self.img_list[self.type][1:]:
            for rect in range(len(rect_details)):
                rects.append(pygame.Rect(rect_details[rect][0]+self.x_loc, 
                                         rect_details[rect][1]+self.y_loc, 
                                         *rect_details[rect][2:]))
        return rects

    def update(self, Surface, state):
        if state:
            self.x_loc-=self.speed
            self.rect.x-=self.speed
        Surface.blit(self.img, (self.x_loc, self.y_loc))
        if state:
            for i in range(len(self.rects)):
                self.rects[i].x -= self.speed
                # pygame.draw.rect(Surface, 'blue', self.rects[i], 1)
        