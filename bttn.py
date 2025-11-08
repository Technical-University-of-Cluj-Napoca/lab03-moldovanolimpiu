import pygame
from utils import COLORS
pygame.init()
class Button:
    def __init__(self, x, y, width, height, text, callback,color, text_color, font = None):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.callback = callback
        self.font = pygame.font.SysFont("arial",20,True)


        self.indicator = pygame.Rect(x+width+10,y+15,20,20)
        self.indicatorcolor = COLORS['RED']

    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)

        text_surface = self.font.render(self.text,True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface,text_rect)
        pygame.draw.rect(win,self.indicatorcolor,self.indicator)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
    def setColorIndicatorRed(self):
        self.indicatorcolor = COLORS['RED']
    def setColorIndicatorGreen(self):
        self.indicatorcolor = COLORS['GREEN']
    
