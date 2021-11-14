import pygame
import random
from threading import Thread
class ObtacleList: #manage obtacle
    def __init__(self):
        self.obstacles = []
        self.total = 0
    def add(self, obstacle):
        self.total += 1
        self.obstacles.append(obstacle)
    def isEmpty(self):
        return self.total == 0

    def updateCollsion(self,player):
        for obs in self.obstacles:
            if player.isCollision(obs.getRect()):
                self.obstacles.remove(obs)
                self.total -= 1
            for bullet in player.getBullet():
                if self.total == 0:
                    break
                if bullet.isCollision(obs.getRect()) and (obs in self.obstacles):
                    self.obstacles.remove(obs)
                    self.total -= 1
    def update(self,player,speed):    #update with player too
        self.updateCollsion(player)
        for obs in self.obstacles:
            obs.update(speed)
            if obs.getX() <= 0:
                self.obstacles.remove(obs)
                self.total -= 1
    def draw(self):
        for obs in self.obstacles:
            obs.draw() #
class Obstacle: # things make noise
    def __init__(self,screen, image,type = 0):
        self.screen = screen
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1200
    # collison
    def isCollion(self,position):
        return self.image.get_rect.colliderect(position)
    def update(self,speed):
        self.rect.x -= 4*speed

    def draw(self):
        self.screen.blit(self.image[self.type], self.rect)
    def getRect(self):
        return self.rect
    def getX(self):
        return self.rect.x
    def getWidth(self):
        return self.rect.width
class EnemyPlane(Obstacle):
    def __init__(self,screen,image,type = 0):
        super().__init__(screen,image,type)
        rand = random.choice([100,200,300,400,500,600])
        self.rect.y = rand
        rand2 = random.choice([1200,1300,1400])
        self.rect.x = rand2
class BulletEnemy(Obstacle):
    def __init__(self,screen,image,position,type = 0):
        super().__init__(screen,image,type)
        rect_x = position.x + self.image[type].get_width()//2
        rect_y = position.y + self.image[type].get_height() // 2
        self.rect.x = rect_x
        self.rect.y = rect_y
    def update(self,speed):
        self.rect.x -= 6*speed



