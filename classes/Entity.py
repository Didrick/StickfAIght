import pygame

class Entity():
    def __init__(self, x, y, img):
        self.hp = 10
        self.vitesse = 100
        self.attaque = 1
        self.defence = 0
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img, (40,80))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        pass

    def move(self,collidlist):
        if(self.hitbox.collidelist(collidlist) == 0): 
            print("COLLISION !!!")
        else : 
            print(" ")

        self.hitbox.y += 10
        if self.hitbox.y > 300 : 
            self.hitbox.y=300
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.hitbox.x -= 8
            if self.hitbox.x < 0:
                self.hitbox.x = 0
        if key[pygame.K_RIGHT]:
            self.hitbox.x += 8
            if self.hitbox.x > 480: # a auto
                self.hitbox.x = 480

        if key[pygame.K_UP]:
            self.hitbox.y -= 30
            if self.hitbox.y < 0: # a auto
                self.hitbox.y = 0
        #self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
        #y = y-taille de case * vitesse

    def attack(self):
        pass

    def defence(self):
        pass
    #pdv = pdv  - degat * defense

