import pygame
import random
class ObtacleList: #manage obtacle
    def __init__(self):
        self.obstacles = []
        self.total = 0
    def add(self, obstacle):
        self.total += 1
        self.obstacles.append(obstacle)
    def isEmpty(self):
        return self.total == 0
    def update(self,player):    #update with player too
        for obs in self.obstacles:
            obs.update()
            if obs.getX() < -obs.getWidth():
                self.obstacles.pop()
            if player.isCollision(obs):
                pygame.time.delay(100)
    def draw(self, SCREEN):
        for obs in self.obstacles:
            obs.draw(SCREEN) #
class Obstacle: # things make noise
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1000
    # collison
    def isCollion(self,x,y):
        return self.image.get_rect.colliderect([x,y])
    def update(self):
        self.rect.x -= 4
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
    def getRect(self):
        return self.rect
    def getX(self):
        return self.rect.x
    def getWidth(self):
        return self.rect.width
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):

        SCREEN.blit(self.image[0], self.rect)
