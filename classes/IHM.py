#IHM

import pygame
from classes import Entity
from Const import *

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
        self.environement = []
        self.players.append( Entity.Entity(128,256,'images/red.png' ))
        self.enemies.append( Entity.Entity(256,256+32, 'images/Pedobear.png'))

        
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
        for env in self.environement:
            environ = self.fenetre.blit(env.image, env.hitbox)

        for pl in self.players:
            #player = pygame.draw.rect(self.fenetre, red, pl.hitbox)
            player = self.fenetre.blit(pl.image, pl.hitbox)
        for en in self.enemies:
            #player = pygame.draw.rect(self.fenetre, red, pl.hitbox)
            enemie = self.fenetre.blit(en.image, en.hitbox)


    def work(self):



        for i in range(0, screen_width//16) : 
            self.environement.append(Entity.Entity(i*16, screen_height-124, 'images/dirt.png', 32, 32))

        for pl in self.players:
            enemie = self.enemies[0]
            collidlist = [enemie.hitbox]
            for env in self.environement:
                collidlist.append(env.hitbox)
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
            self.clock.tick(20)
