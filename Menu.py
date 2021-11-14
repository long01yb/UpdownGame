import pygame
import  os
from Window import  Window
from Game import  Game
import button as a
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "Rocket_Player.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png"))]
BG = pygame.image.load(os.path.join("Assets/Other", "Plano-10.png"))
BG1 = pygame.image.load(os.path.join("Assets/Other", "BG_Game.png"))
START = [pygame.image.load(os.path.join("Assets/Other", "StartIdle.png")),
         pygame.image.load(os.path.join("Assets/Other", "StartHover.png"))]
SETTING = [pygame.image.load(os.path.join("Assets/Other", "SettingIdle.png")),
         pygame.image.load(os.path.join("Assets/Other", "SettingHover.png"))]
QUIT = [pygame.image.load(os.path.join("Assets/Other", "QuitIdle.png")),
         pygame.image.load(os.path.join("Assets/Other", "QuitHover.png"))]
class Menu(Window):
    def __init__(self,height,width,windowStack,bg = BG):
        super().__init__(bg,height,width,windowStack)
        self.points = 0
    def initButtons(self):
        self.buttons.add("Start",a.Button(150,190,20,START[0],START[1]))
        self.buttons.add("Setting",a.Button(150, 255,20,SETTING[0],SETTING[1]))
        self.buttons.add("Quit",a.Button(150, 320,20,QUIT[0],QUIT[1]))
    def update(self):
        self.buttons.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.buttons.findButton("Quit").isCLICK():
                self.state = self.QUIT
                self.windowStack.pop()
            elif self.buttons.findButton("Start").isCLICK():
                self.state = self.PLAYING
                game = Game(BG1,1100,600,self.windowStack,self.state,RUNNING)
                self.windowStack.append(game)
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