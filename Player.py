import pygame
import os
COLLISION = 1
ISALIVE = 2
DEAD = 3
SHOOTING = 4
class Bullet:
    def __init__(self, speed, bulletList, screen, x,y, type=0):
        self.speed = speed
        self.screen = screen
        self.bulletList = bulletList
        self.type = type
        self.bullet = self.bulletList[type]
        self.position = self.bullet.get_rect()
        self.position.x = x
        self.position.y = y
        self.state = ISALIVE
    def isCollision(self, enemyPosition):
        if self.position.colliderect(enemyPosition):
            self.state = DEAD
        return self.state == DEAD

    def isDead(self):
        return (self.position.x >= 1100 or self.state == DEAD)
    def update(self):
        self.position.x += (5*self.speed)
    def draw(self):
        self.screen.blit(self.bullet,(self.position))
class Dinosaur:
    def __init__(self,screen,characterList,type = 0):
        self.characterList = characterList # a surface
        self.character = self.characterList[type]
        self.position = self.character.get_rect()
        self.position.x = 50
        self.position.y = 380
        self.hp = 50
        self.state = ISALIVE
        self.screen = screen
        self.bullet = []
    def getState(self):
        return self.state
    def getPosition(self):
        return self.position
    def getBullet(self):
        return self.bullet
    def isAlive(self):
        return self.state == ISALIVE
    def isDead(self):
        return self.hp < 0
    def heal(self):
        self.hp += 10
    def isCollision(self,enemyPosition = None):
        if enemyPosition != None and self.position.colliderect(enemyPosition):
            self.state = COLLISION
        return self.state == COLLISION
    def shoot(self,speed,bulletList,screen):
        self.state = SHOOTING
        rect_x = self.position.x + self.character.get_width()//2
        rect_y = self.position.y + self.character.get_height() // 2
        if len(self.bullet) < 10:
            self.bullet.append(Bullet(speed,bulletList,screen,rect_x,rect_y))
    def updatePosition(self,userInput,speed):
        if userInput[pygame.K_s] and self.position.y <550:
            self.position.y += 4 * speed
        elif userInput[pygame.K_w] and self.position.y > -50:
            self.position.y -= 4 * speed
        elif userInput[pygame.K_d] and self.position.x <1100:
            self.position.x += 4 * speed
        elif userInput[pygame.K_a] and self.position.x > -50:
            self.position.x -= 4 * speed
    def updateState(self):
        if self.state == COLLISION:
            self.hp -= 10
            self.state = ISALIVE
        if self.state == SHOOTING:
            self.state = ISALIVE
        if self.isDead():
            self.state = DEAD
    def updateBullet(self):
        for i in self.bullet:
            i.update()
            if i.isDead():
                self.bullet.remove(i)
    def update(self, userInput,speed):
        self.updateBullet()
        self.updatePosition(userInput,speed)
        self.updateState()
    def draw(self):
        if self.state == DEAD:
            pass
        else:
            for i in self.bullet:
                i.draw()
            self.screen.blit(self.character, (self.position.x, self.position.y))
