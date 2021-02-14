#IHM

import pygame


class IHM():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((640, 480))
        self.background = pygame.Surface(fenetre.get_size())
        pass

    def start(self):
        self.loop = True
    
    def stop(self):
        self.loop = False

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def run(self):
        while self.loop:
            #event
            self.eventHandler()

            #graphical
            self.background.fill((0, 200, 255))
            self.fenetre.blit(background, (0, 0))

            #end
            pygame.display.flip()
            self.clock.tick(10)