import pygame

screen_width = 640
screen_height = 480

class Entity():
    def __init__(self, x, y, img, width=40, height=80):
        self.hp = 10
        self.vitesse = 100
        self.attaque = 1
        self.defence = 0
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img, (width,height))
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
        if self.hitbox.y > screen_height - self.hitbox.height : 
             self.hitbox.y=screen_height - self.hitbox.height 
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.hitbox.x -= 8
            if self.hitbox.x < 0:
                self.hitbox.x = 0
        if key[pygame.K_RIGHT]:
            self.hitbox.x += 8
            if self.hitbox.x > screen_width - self.hitbox.width : 
             self.hitbox.x = screen_width - self.hitbox.width 

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

