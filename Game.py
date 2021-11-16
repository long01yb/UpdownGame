import random
import threading

import pygame
import os
import threading
from Window import  Window
import Player
import Obtacles
from Question import  Question
PLANE_ENEMY = [pygame.image.load(os.path.join("Assets/Obtacle", "Rocket_Enemy.png")),
                pygame.image.load(os.path.join("Assets/Obtacle", "Enemy.png"))]
BULLET = [pygame.image.load(os.path.join("Assets/Dino", "Bullet.png"))]
BULLET_ENEMY = [pygame.image.load(os.path.join("Assets/Obtacle", "Bullet_enemy.png"))]
class Game(Window):
    COLLISION = 10
    def __init__(self,background,height,width,windowStack,state,Player_sprite):
        super().__init__(background,height,width,windowStack,state)
        self.speed = 4
        self.player = Player.Dinosaur(self.screen,Player_sprite)
        self.obtacleList = Obtacles.ObtacleList()
        self.fps = 30
        self.points = 0
        self.event = None
        self.userInput = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.scroll = 0
        self.inc = 1
        self.ques = Question(self.screen)
        self.delay = False
    def initButtons(self):
        # add button of game here
        pass
    def generateObtacle(self):
        if self.obtacleList.isEmpty():
            for x in range(self.speed // 2):
                obs = Obtacles.EnemyPlane(self.screen,PLANE_ENEMY)
                self.obtacleList.add(obs)
                rand = random.choice([1, 2])
                if rand == 1:
                    self.obtacleList.add(Obtacles.BulletEnemy(self.screen, BULLET_ENEMY,obs.getRect() ))
    def getSpeed(self):
        return self.speed
    def getFPS(self):
        return self.fps
    def getPoint(self):
        return self.points
    def isQUIT(self):
        return self.state == self.QUIT
    def checkState(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.player.isDead():
                self.state = self.QUIT
                self.windowStack.pop()
        self.userInput = pygame.key.get_pressed()
        if self.userInput[pygame.K_SPACE] and self.state != self.COLLISION:
            if self.state == self.STOP:
                self.state = self.PLAYING
                self.inc = 1
            else:
                self.state = self.STOP
        if self.player.isCollision():
            self.state = self.COLLISION
        elif  not self.ques.isTHINKING():
            if self.ques.getAnswer():
                self.player.heal()
            self.ques.refresh()
            self.ques.updateContent()
            self.inc = 1
            self.state = self.PLAYING
    def updatePoints_Speed_userInput(self):
        if self.points % 200 == 0:
            self.speed += self.inc
        self.points += self.inc
    def updateUserInput(self):
        self.userInput = pygame.key.get_pressed()
    def updatePlayer(self):
        if pygame.mouse.get_pressed()[0]:
            self.player.shoot(self.speed,BULLET,self.screen)
        self.player.update(self.userInput,self.speed)
    def updateObtacleList(self):
        self.obtacleList.update(self.player,self.speed)
    def updateScroll(self):
        self.scroll += self.inc*4
    def updateState(self):
        self.checkState()
        if self.state == self.STOP:
            self.inc = 0
        elif self.state == self.COLLISION:
            self.player.updateState()
            self.obtacleList.updateCollsion(self.player)
            self.ques.update()
    def drawPoint(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Points: " + str(self.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        self.screen.blit(text, textRect)
    # update point,speed,input
    def runStuff(self):

        self.updatePoints_Speed_userInput()
        self.drawPoint()
    def runBackground(self):
        width = self.background.get_width()

        self.updateScroll()
        for x in range(4):
            self.screen.blit(self.background, (width*x - self.scroll,0))
    def runPlayer_Obtacle(self):
        self.updatePlayer()
        self.updateObtacleList()
    def draw(self):
        self.obtacleList.draw()
        self.player.draw()
        if self.state == self.COLLISION:
            self.ques.draw()
    def run(self):
        while self.state != self.QUIT:
            if self.state == self.PLAYING:
                threading.Thread(target=self.runBackground(), args=()).start() # thread background
                threading.Thread(target=self.runStuff(), args=()).start() # thread infomation
                threading.Thread(target=self.generateObtacle(), args=()).start() # thread generate
                threading.Thread(target=self.runPlayer_Obtacle(), args=()).start() # thread Player
            # thread state
            self.updateState()
            self.draw()
            self.clock.tick(self.fps)
            pygame.display.update()