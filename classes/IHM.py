#IHM

import pygame
from classes import Entity

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

screen_width = 640
screen_height = 480

class Pygame():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((screen_width, screen_height))
        self.background = pygame.Surface(self.fenetre.get_size())
        self.floor = pygame.image.load('images/dirt.png')
        
        #setup entity
        self.enemies = []
        self.players = []
        self.players.append( Entity.Entity(100,280,'images/red.png' ))
        self.enemies.append( Entity.Entity(340,280, 'images/Pedobear.png'))
        
        self.environment = []
        
        pass


    def start(self):
        self.loop = True
        self.run()

    def stop(self):
        self.loop = False

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

    

    def graphical(self):
        self.background.fill((0, 200, 255))
        self.fenetre.blit(self.background, (0, 0))
        for i in range(0, screen_width//16) : 
            self.fenetre.blit(self.floor, (i*16,screen_height-100))
            self.environment.append(pygame.Rect.Rect((i*16,screen_height-100), self.floor.get_width(), self.floor.get_height())

        for pl in self.players:
            #player = pygame.draw.rect(self.fenetre, red, pl.hitbox)
            player = self.fenetre.blit(pl.image, pl.hitbox)
        for en in self.enemies:
            #player = pygame.draw.rect(self.fenetre, red, pl.hitbox)
            enemie = self.fenetre.blit(en.image, en.hitbox)
    def work(self):

        for pl in self.players:

            enemie = self.enemies[0]
            collidlist = [enemie.hitbox]
            pl.move(collidlist)

            
            
        pass

    def run(self):
        while self.loop:
            #event
            self.eventHandler()

            #work
            self.work()

            #graphical
            self.graphical()

            #end
            pygame.display.flip()
            self.clock.tick(10)
