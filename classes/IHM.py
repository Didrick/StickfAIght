#IHM

import pygame


class Pygame():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((640, 480))
        self.background = pygame.Surface(self.fenetre.get_size())
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

    def run(self):
        while self.loop:
            #event
            self.eventHandler()

            #work

            #graphical
            self.graphical()

            #end
            pygame.display.flip()
            self.clock.tick(10)
