import pygame


class Input_box:
    def __init__(self, location, size, b_c='black', f_c='white', p_h=''):
        self.font = pygame.font.Font(None, 28)
        self.location = location
        self.x_loc, self.y_loc = location
        self.size = size
        self.width, self.height = size
        self.b_c = b_c
        self.f_c = f_c
        self.place_holder = p_h
        self._text = ""
        self.max_length = 10
        self.rect1 = pygame.Rect(*location, *size)
        self.rect2 = pygame.Rect(*[i+3 for i in location], 
                                 *[i-6 for i in size])
        
    def show_placeholder(self, Surface):
        self.text = self.font.render(self.place_holder, True, (160,160,160))
        pygame.draw.rect(Surface, self.b_c, self.rect1, border_radius=10)
        pygame.draw.rect(Surface, self.f_c, self.rect2, border_radius=10)
        Surface.blit(self.text, (self.x_loc+8,self.y_loc+8))

    def show_value(self, Surface):
        self.text = self.font.render(self._text, True, 'black')
        pygame.draw.rect(Surface, self.b_c, self.rect1, border_radius=10)
        pygame.draw.rect(Surface, self.f_c, self.rect2, border_radius=10)
        Surface.blit(self.text, (self.x_loc+8,self.y_loc+8))

    def validate(self, _str):
        if _str == 'backspace':
            return self._text[:-1], True
        if len(self._text)<self.max_length:
            if _str == 'space':
                return " ", False
            elif len(_str)>1:
                return _str[1], False
            else:
                return _str, False
        else:
            return self._text, True

    def update(self, Surface, key_name, _key):
        if key_name != None and _key:
            _str, inplace = self.validate(key_name)
            if inplace:
                self._text = _str
            else:
                self._text+=_str
            _key = False
        if len(self._text):
            self.show_value(Surface)
        else:
            self.show_placeholder(Surface)
        return _key