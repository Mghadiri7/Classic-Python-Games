import pygame


class Btn:
    def __init__(self, text, location, size, 
                 text_color, back_color, for_color, ch_state):
        self.font = pygame.font.Font(None, 28)
        self.text = self.font.render(text, True, text_color)
        self._text = text
        self.location = location
        self.width, self.height = size
        self.text_color = text_color
        self.b_color = back_color
        self.f_color = for_color
        self.ch_state = ch_state

        self.rect1 = pygame.Rect(*location, *size)
        self.rect2 = pygame.Rect(*[i+3 for i in location], 
                                 *[i-6 for i in size])
        
    def normal(self, Surface):
        self.text = self.font.render(self._text, True, self.text_color)
        pygame.draw.rect(Surface, self.b_color, self.rect1, border_radius=10)
        pygame.draw.rect(Surface, self.f_color, self.rect2, border_radius=10)
        Surface.blit(self.text, 
                     ((self.location[0]+(self.width-self.text.get_width())//2), 
                     (self.location[1]+(self.height-self.text.get_height())//2)))

    def hover(self, Surface):
        self.text = self.font.render(self._text, True, (0,122,204))
        pygame.draw.rect(Surface, (0,122,204), self.rect1, border_radius=10)
        pygame.draw.rect(Surface, self.f_color, self.rect2, border_radius=10)
        Surface.blit(self.text, 
                     ((self.location[0]+(self.width-self.text.get_width())//2), 
                     (self.location[1]+(self.height-self.text.get_height())//2)))
        
    def update(self, Surface ,pos, state, click=False):
        if self.rect1.collidepoint(pos) and click:
            return self.ch_state
        elif self. rect1.collidepoint(pos):
            self.hover(Surface)
        else:
            self.normal(Surface)
        return state