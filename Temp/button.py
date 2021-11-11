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
                return i[1] # return a button ( not name )
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
    HOVER_COLOR = (255, 225, 255)
    CLICK_COLOR = (75, 225, 255)
    IDLE_COLOR =(160, 198, 245,255)
    FONT_COLOR = (181, 99, 202)
    IDLE = 1
    HOVER = 2
    CLICK = 3
    text_col = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.coor = [x,y]
        self.text = text
        self.state = self.IDLE
        self.button_rect = Rect(x, y, self.width, self.height)
    def isIDLE(self):
        return self.state == self.IDLE
    def isCLICK(self):
        return self.state == self.CLICK
    def isHOVER(self):
        return self.state == self.HOVER
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(pos):  # check if the mouse cursor is in the button
            if pygame.mouse.get_pressed()[0] == 1:  # if the left mouse has been clicked to the button
                self.state = self.CLICK
            else:
                self.state = self.HOVER
        elif self.state != self.IDLE:
            self.state = self.IDLE
    def draw(self,screen):
        if self.state == self.HOVER:
            pygame.draw.rect(screen, self.HOVER_COLOR, self.button_rect)
        elif self.state == self.CLICK:
            pygame.draw.rect(screen, self.CLICK_COLOR, self.button_rect)
        else:
            pygame.draw.rect(screen, self.IDLE_COLOR, self.button_rect)
            self.text_col = self.FONT_COLOR
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (
        self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
