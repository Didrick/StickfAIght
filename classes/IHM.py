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

class Pygame():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((640, 480))
        self.background = pygame.Surface(self.fenetre.get_size())
        
        #setup entity
        self.enemies = []
        self.players = []
        self.players.append( Entity.Entity(320,240) )
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

        for pl in self.players:
            player = pygame.draw.rect(self.fenetre, red, pl.hitbox)

    def work(self):
        for pl in self.players:
            pl.move()
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
