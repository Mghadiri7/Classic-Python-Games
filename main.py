import pygame
import sys
from buttons import Btn

class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Menu")
        self.state = 1 #1=Main menu
        self.buttons = self.main_menu()
        self.click = False
        self.run()

    def main_menu(self):
        btns = [Btn("New Game", (125,80), (150,35), 'black', 'red', 'green', 2), 
                Btn("Option", (125,120), (150,35), 'black', 'red', 'green', 3), 
                Btn("Exit", (125,160), (150,35), 'black', 'red', 'green', 4)]
        return btns

    def run(self):
        while True:
            self.game_display.fill('white')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click = True
                else:
                    self.click = False
            if self.state==1:
                for btn in self.buttons:
                    position = pygame.mouse.get_pos()
                    self.state = btn.update(self.game_display, position, 
                                            self.state, self.click)
            elif self.state==4:
                pygame.quit()
                sys.exit()
            pygame.display.update()
    
new_game = Game()