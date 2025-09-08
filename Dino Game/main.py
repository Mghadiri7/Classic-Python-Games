import pygame
import sys
from dino import Dino
from constants import *
from ground import GND
from day import Day_or_night
from obstacles import Obstacle, Obstacles

class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(GAME_NAME)
        self.font = pygame.font.Font(None, 24)
        self.hscore = self.load_highest_score()
        self.score = 0
        self.day = Day_or_night(self.fps, 7)
        self.ground = GND(5, WINDOW_SIZE[1]-150)
        self.obss = Obstacles(y=400, min_gap=450, speed=5)
        self.player = Dino((100,350), self.fps)
        self.clock = pygame.time.Clock()
        self.run()

    def load_highest_score(self):
        with open("save.txt", "r") as file:
            highest_score = file.read()
            return highest_score
    
    def show_score(self):
        score = str(self.score)
        _score = self.font.render("Your Score: "+(6-len(score))*"0"+score, True, RED, 1)
        _hscore = self.font.render("Highest Score:  "+self.hscore, True, BLUE, 1)
        self.game_display.blit(_score, (820, 75))
        self.game_display.blit(_hscore, (800, 50))

    def new_score(self):
        if int(self.hscore)<self.score:
            with open("save.txt", "w") as file:
                _str = (6-len(str(self.score)))*"0"+str(self.score)
                file.write(_str)

    def run(self):
        state = True
        while True:
            self.day.update(self.game_display, state)
            self.show_score()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
            self.ground.update(self.game_display, state)
            self.obss.update(self.game_display, state)
            state = self.player.update(self.game_display, self.obss, state)
            self.obss.check()
            if state:
                self.score+=1
            else:
                self.new_score()
            pygame.display.update() 
            self.clock.tick(self.fps)

new_game = Game()
