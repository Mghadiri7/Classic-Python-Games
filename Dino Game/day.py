import pygame


class Day_or_night:
    def __init__(self, fps, length):
        self.threshold = fps * length
        self.counter = 0
        self.state = True
        self.c = 0
        self.transition_speed = 1
        self.transition = False

    def update(self, Surface, state):
        if state:
            _max = 255-self.transition_speed
            _min = 0-self.transition_speed
            if self.transition:
                self.c+=self.transition_speed
            if self.c>=_max or self.c<_min:
                self.transition_speed*=-1
                self.threshold = False
            Surface.fill((self.c, self.c, self.c))
            self._update()
        # return (255,255,255) if self.transition_speed>0 else (0,0,0)

    def _update(self):
        if not self.transition:
            if self.counter>=self.threshold:
                self.transition = True
                self.counter = 0
            else:
                self.counter+=1