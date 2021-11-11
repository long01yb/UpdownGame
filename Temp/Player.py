import pygame

COLLISION = 1
ISALIVE = 2
DEAD = 3
class Dinosaur:
    def __init__(self,characterList,type = 0):
        self.characterList = characterList # a surface
        self.character = self.characterList[type]
        self.position = self.character.get_rect()
        self.position.x = 50
        self.position.y = 380
        self.hp = 50
        self.state = ISALIVE
    def getState(self):
        return self.state
    def getPosition(self):
        return self.position
    def isAlive(self):
        return self.state == ISALIVE
    def isDead(self):
        return self.hp <= 0
    def isCollision(self,enemyPosition):
        return self.position.colliderect(enemyPosition)
    def update(self, userInput,speed,enemyPosition = None):
        if(enemyPosition != None and self.isCollision(enemyPosition) and self.state == ISALIVE):
            self.hp -= 10
            self.state = COLLISION
        if self.state == COLLISION:
            self.state = ISALIVE
        if self.isDead():
            self.state = DEAD
        if userInput[pygame.K_s]:
            self.position.y += 5 * speed
        elif userInput[pygame.K_w]:
            self.position.y -= 5 * speed
        elif userInput[pygame.K_d]:
            self.position.x += 5 * speed
        elif userInput[pygame.K_a]:
            self.position.x -= 5 * speed
    def draw(self, SCREEN):
        SCREEN.blit(self.character, (self.position.x, self.position.y))
