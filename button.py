import pygame, sys
from pygame.locals import *
import os
# define colours
pygame.init()
BG = (204, 102, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Constantia', 20)

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
    IDLE = 1
    HOVER = 2
    CLICK = 3
    text_col = BLACK
    def __init__(self, x, y,sizeText = 30
                 ,img_idle = None,img_hover = None, text = None):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('Constantia', sizeText)
        self.coor = [x,y]
        self.text = text
        self.state = self.IDLE
        self.img_idle = img_idle
        self.img_hover = img_hover
        self.width = self.img_idle.get_width()
        self.height = self.img_idle.get_height()
        self.button_rect = Rect(x,y,img_idle.get_width(),img_idle.get_height())
    def isIDLE(self):
        return self.state == self.IDLE
    def isCLICK(self):
        return self.state == self.CLICK
    def isHOVER(self):
        return self.state == self.HOVER
    def changeContent(self,text):
        self.text = text
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
            screen.blit(self.img_hover,(self.x,self.y))
        else:
            screen.blit(self.img_idle,(self.x,self.y))
        if self.text != None:
            text_img = self.font.render(self.text, True, (0,0,0))
            text_len = text_img.get_width()
            screen.blit(text_img, (
            self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
    def draw1(self,screen,img):
        if self.state == self.HOVER:
            screen.blit(img,(self.x,self.y))
        else:
            screen.blit(img,(self.x,self.y))
        if self.text != None:
            text_img = self.font.render(self.text, True, (0,0,0))
            text_len = text_img.get_width()
            screen.blit(text_img, (
            self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
