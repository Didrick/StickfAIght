import pygame

class Entity():
    def __init__(self, x, y):
        self.hp = 10
        self.vitesse = 100
        self.attaque = 1
        self.defence = 0
        #self.x = x
        #self.y = y
        #self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
        img = pygame.image.load('images/red.png')
        self.image = pygame.transform.scale(img, (40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pass

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 7
            if self.rect.x < 0:
                self.rect.x = 0
        if key[pygame.K_RIGHT]:
            self.rect.x += 7
            if self.rect.x > 430: # a auto
                self.rect.x = 430
        #self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
        #y = y-taille de case * vitesse

    def attack(self):
        pass

    def defence(self):
        pass
    #pdv = pdv  - degat * defense

