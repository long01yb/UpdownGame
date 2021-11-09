import pygame


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    VEL = 4
    def __init__(self,RUNNING):
        self.vel = self.VEL
        self.run_img = RUNNING
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.hp = 50
    def update(self, userInput):
        if userInput[pygame.K_s]:
            self.dino_rect.y += 5*self.vel
        elif userInput[pygame.K_w]:
            self.dino_rect.y -= 5 * self.vel
        elif userInput[pygame.K_d]:
            self.dino_rect.x += 5 * self.vel
        elif userInput[pygame.K_a]:
            self.dino_rect.x -= 5 * self.vel
    def isDead(self):
        return self.hp <= 0
    def isCollision(self,z):
        self.hp -= 10
        return  self.dino_rect.colliderect(z.getRect())
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    def getRect(self):
        return self.dino_rect
