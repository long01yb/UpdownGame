from logging import exception

import pygame
import os
import Menu
pygame.init()
class Control:
    def __init__(self):
        self.windowStack = []
    def addWindow(self,window):
        self.windowStack.append(window)
    def initWindow(self):
        menu = Menu.Menu(1100,600,self.windowStack)
        self.addWindow(menu)
    def run(self):
        self.initWindow()
        while(len(self.windowStack) != 0):
            end = len(self.windowStack) - 1
            window = self.windowStack[end]
            window.run()
            # pos = pygame.mouse.get_pos()
            # print(f"{pos[0]} -d- {pos[1]}")
mainn = Control()
mainn.run()