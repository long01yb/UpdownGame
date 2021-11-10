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

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
START = 1
PLAYING = 2
QUIT = 3
HOWTOPLAY = 4
STOP = 5
BGcolor = (204, 102, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacleList
    run = True
    clock = pygame.time.Clock()
    player = Player.Dinosaur(RUNNING)
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    death_count = 0
    obstacleList= Obtacles.ObtacleList()

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))


    while run:
        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(userInput)

        if obstacleList.isEmpty():
            if random.randint(0, 2) == 0:
                obstacleList.add(Obtacles.SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacleList.add(Obtacles.LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacleList.add(Obtacles.Bird(BIRD))

        obstacleList.update(player)
        obstacleList.draw(SCREEN)
        background()
        score()

        # set fps = 30
        clock.tick(30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #or player.isDead():
                run = False
    return 0
class Window:
    # SCREEN_HEIGHT = 600
    # SCREEN_WIDTH = 1100
    # SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self,background,height,width,windowStack,state):
        self.background = background #a variable surface ~ image of background window
        self.screen = pygame.display.set_mode((height,width))
        self.windowStack = windowStack
        self.state = state
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
        self.speed = 10
        self.player = Player.Dinosaur(RUNNING)
        self.obtacleList = 0
        self.fps = 30
        self.points = 0
        self.event = None
        self.userInput = None
        self.clock = pygame.time.Clock()
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
                self.speed = 10
            else:
                self.state = STOP
    def update(self):
        self.updateState()
        if self.state == STOP:
            self.speed = 0
        if self.state == PLAYING:
            self.userInput = pygame.key.get_pressed()
            self.points += 1
            if self.points % 150 == 0:
                self.speed += 1
            self.player.update(self.userInput)
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0,380))
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
        self.buttons = a.ButtonList()
    def initButtons(self):
        self.buttons.add("Start",a.Button(75, 360, 'Start'))
        self.buttons.add("Setting",a.Button(325, 360, 'Setting'))
        self.buttons.add("Quit",a.Button(200, 450, 'Quit'))
    # def initGame(self):
    #     SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #     pass
    def update(self):
        self.buttons.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.buttons.findButton("Quit").update():
                self.state = QUIT
                self.windowStack.pop()
            elif self.buttons.findButton("Start").update():
                self.state = START
                game = Game(BG,1200,600,self.windowStack,self.state)
                self.windowStack.append(game)

        return self.state
    def getState(self):
        return self.state
    def draw(self):
        SCREEN.fill((BGcolor))
        self.buttons.draw(self.screen)
    def run(self):
        self.initButtons()
        self.update()
        self.draw()
        pygame.display.update()
class GameState:
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
mainn = GameState()
mainn.run()
