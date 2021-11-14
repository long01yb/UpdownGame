import random

import pygame
import os
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
        self.userInput = None
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
    def updateState(self):
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
    def updateSpeed(self):
        if self.points % 200 == 0:
            self.speed += self.inc
    def updatePoints(self):
        self.points += self.inc
    def updateUserInput(self):
        self.userInput = pygame.key.get_pressed()
    def updatePlayer(self):
        if self.userInput[pygame.K_o]:
            self.player.shoot(self.speed,BULLET,self.screen)
        self.player.update(self.userInput,self.speed)

    def updateObtacleList(self):
        self.obtacleList.update(self.player,self.speed)

    def updateScroll(self):
        self.scroll += self.inc*4
    def update(self):
        self.updateState()
        if  self.state == self.PLAYING:
            self.updatePoints()
            self.updateSpeed()
            self.updateUserInput()
            self.updatePlayer()
            self.updateScroll()
            self.generateObtacle()
            self.updateObtacleList()
        elif self.state == self.STOP:
            self.inc = 0
        elif self.state == self.COLLISION:
            self.player.updateState()
            self.obtacleList.updateCollsion(self.player)
            self.ques.update()
    def draw(self):
        width = self.background.get_width()
        for x in range(4):
            self.screen.blit(self.background, (width*x - self.scroll,0))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Points: " + str(self.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        self.screen.blit(text, textRect)
        self.obtacleList.draw()
        self.player.draw()

        if self.state == self.COLLISION:
            self.ques.draw()
    def run(self):
        self.update()
        self.draw()
        self.clock.tick(self.fps)
        pygame.display.update()