import pygame

class Entity():
    def __init__(self, x, y):
        self.hp = 10
        self.vitesse = 100
        self.attaque = 1
        self.defence = 0
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
        pass

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= 7
            if self.x < 0:
                self.x = 0
        if key[pygame.K_RIGHT]:
            self.x += 7
            if self.x > 430: # a auto
                self.x = 430
        self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
    #y = y-taille de case * vitesse

    def attack(self):
        pass

    def defence(self):
        pass
    #pdv = pdv  - degat * defense

