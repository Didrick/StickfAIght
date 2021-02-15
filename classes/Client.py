import pygame
import pygame.locals
import socket
import select
import random
import time


#on m appelle l'ovni

class GameClient(object):
    def __init__(self, addr="85.168.112.123", serverport=40000):
        self.clientport = random.randrange(8000, 8999)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind to localhost - set to external ip to connect from other computers
        self.conn.bind(("192.168.0.17", self.clientport))
        self.addr = addr
        self.serverport = serverport
        
        self.read_list = [self.conn]
        self.write_list = []
        
        self.setup_pygame()
      
    def setup_pygame(self, width=400, height=300):
        self.screen = pygame.display.set_mode((width, height))
        self.bg_surface = pygame.image.load("images/bg.png").convert()
        
        self.image = pygame.image.load("images/green.png").convert_alpha()
        
        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.locals.QUIT,
                                                            pygame.locals.KEYDOWN])
        pygame.key.set_repeat(50, 50)
        
    def run(self):
        running = True
        clock = pygame.time.Clock()
        tickspeed = 30
        
        try:
            self.conn.sendto("c".encode(), (self.addr, self.serverport))
            while running:
                clock.tick(tickspeed)
                
                readable, writable, exceptional = (
                        select.select(self.read_list, self.write_list, [], 0)
                )
                for f in readable:
                    if f is self.conn:
                        msg, addr = f.recvfrom(32)
                        msg = msg.decode()
                        self.screen.blit(self.bg_surface, (0,0))
                        for position in msg.split('|'):
                            x, sep, y = position.partition(',')
                            try:
                                self.screen.blit(self.image, (int(x), int(y)))
                            except:
                                pass 
                        

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.locals.QUIT:
                        running = False
                        break
                    elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_UP:
                            self.conn.sendto("uu".encode(), (self.addr, self.serverport))
                        if event.key == pygame.locals.K_DOWN:
                            self.conn.sendto("ud".encode(), (self.addr, self.serverport))
                        if event.key == pygame.locals.K_LEFT:
                            self.conn.sendto("ul".encode(), (self.addr, self.serverport))
                        if event.key == pygame.locals.K_RIGHT:
                            self.conn.sendto("ur".encode(), (self.addr, self.serverport))
                            
                        pygame.event.clear(pygame.locals.KEYDOWN)

                pygame.display.update()
        finally:
            self.conn.sendto("d".encode(), (self.addr, self.serverport))


if __name__ == "__main__":
    g = GameClient()
    g.run()