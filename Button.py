import pygame, sys
from pygame.locals import *
import os
# define colours
pygame.init()
BG = (204, 102, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Constantia', 30)

# to Manage all Button as Dict { key = name of button , value = button }
class ButtonList():
    def __init__(self):
        self.List = {}
    def add(self,name,button):
        self.List.update({name: button})
    def findButton(self,name):
        for i in self.List.items():
            if name == i[0]:
                return i[1]
        return None
    def update(self):
        for button in self.List.values():
            button.update()
    def draw(self,screen):
        for button in self.List.values():
            button.draw(screen)
class Button():
    # colours for button and text
    button_col = (192, 192, 192)
    HOVER = (255, 225, 255)
    CLICK = (75, 225, 255)
    text_col = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.coor = [x,y]
        self.text = text
        self.clicked = False
        self.button_rect = Rect(x, y, self.width, self.height)

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(pos):  # check if the mouse cursor is in the button
            if pygame.mouse.get_pressed()[0] == 1:  # if the left mouse has been clicked to the button
                self.clicked = True
            else:
                self.clicked = False
        return self.clicked
    def draw(self,screen):
        pygame.draw.rect(screen, self.button_col, self.button_rect)
        if self.clicked == True:
            pygame.draw.rect(screen, self.HOVER, self.button_rect)
        else:
            pygame.draw.rect(screen, self.CLICK, self.button_rect)
        # add shading to button
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (
        self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))  # showing the text at the center 
