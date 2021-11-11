from logging import exception

import pygame
import os
import random
import Obtacles
import Player
import button as a
from enum import Enum
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png"))]
BG = pygame.image.load(os.path.join("Assets/Other", "BG.jpg"))
BG1 = pygame.image.load(os.path.join("Assets/Other", "Track1.jpg"))
START = 1
PLAYING = 2
QUIT = 3
HOWTOPLAY = 4
STOP = 5
BGcolor = (204, 102, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Window:
    def __init__(self,background,height,width,windowStack,state):
        self.background = background #a variable surface ~ image of background window
        self.screen = pygame.display.set_mode((height,width))
        self.windowStack = windowStack
        self.state = state
        self.buttons = a.ButtonList()
    def initButtons(self): # abstract
        pass
    def getState(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def run(self):
        pass
class Game(Window):
    def __init__(self,background,height,width,windowStack,state):
        super().__init__(background,height,width,windowStack,state)
        self.speed = 3
        self.player = Player.Dinosaur(RUNNING)
        self.obtacleList = Obtacles.ObtacleList()
        self.fps = 30
        self.points = 0
        self.event = None
        self.userInput = None
        self.clock = pygame.time.Clock()
        self.scroll = 0
        self.inc = 1.0
    def initButtons(self):
        # add button of game when state is PLAYING
        pass
    def getSpeed(self):
        return self.speed
    def getFPS(self):
        return self.fps
    def getPoint(self):
        return self.points
    def updateState(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #or player.isDead():
                self.state = QUIT
                self.windowStack.pop()
        self.userInput = pygame.key.get_pressed()
        if self.userInput[pygame.K_SPACE]:
            if self.state == STOP:
                self.state = PLAYING
            else:
                self.state = STOP
    def updateSpeed(self):
        if self.points % 200 == 0:
            self.speed += self.inc
    def updatePoints(self):
        self.points += self.inc
    def updateUserInput(self):
        self.userInput = pygame.key.get_pressed()
    def updatePlayer(self,enemyPosition = None):
        self.player.update(self.userInput,self.speed,enemyPosition)
    def updateObtacle(self):

        pass
    def updateScroll(self):
        self.scroll += self.inc*4
    def update(self):
        self.updateState()
        if  self.state == PLAYING:
            self.inc = 1
            self.updatePoints()
            self.updateSpeed()
            self.updateUserInput()
            self.updatePlayer()
            self.updateScroll()
        else:
            self.inc = 0
    def draw(self):
        self.screen.fill((255, 255, 255))
        width = self.background.get_width()
        for x in range(4):
            self.screen.blit(self.background, (width*x - self.scroll,380))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Points: " + str(self.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        self.screen.blit(text, textRect)
        self.player.draw(self.screen)
    def run(self):
        self.update()
        self.draw()
        self.clock.tick(self.fps)
        pygame.display.update()
class Menu(Window):
    def __init__(self,bg,height,width,windowStack,state):
        super().__init__(bg,height,width,windowStack,state)
        self.points = 0
    def initButtons(self):
        self.buttons.add("Start",a.Button(75, 360, 'Start'))
        self.buttons.add("Setting",a.Button(325, 360, 'Setting'))
        self.buttons.add("Quit",a.Button(200, 450, 'Quit'))
    def update(self):
        self.buttons.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.buttons.findButton("Quit").isCLICK():
                self.state = QUIT
                self.windowStack.pop()
            elif self.buttons.findButton("Start").isCLICK():
                self.state = START
                game = Game(BG,1200,600,self.windowStack,self.state)
                self.windowStack.append(game)

        return self.state
    def getState(self):
        return self.state
    def draw(self):
        SCREEN.blit(BG,(0,0))
        self.buttons.draw(self.screen)
    def run(self):
        self.initButtons()
        self.update()
        self.draw()
        pygame.display.update()
class Control:
    def __init__(self):
        self.windowStack = []
    def addWindow(self,window):
        self.windowStack.append(window)
    def initWindow(self):
        menu = Menu(BG,1200,600,self.windowStack, START)
        self.addWindow(menu)
    def run(self):
        self.initWindow()
        while(len(self.windowStack) != 0):
            end = len(self.windowStack) - 1
            window = self.windowStack[end]
            window.run()
mainn = Control()
mainn.run()
