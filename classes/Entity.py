import pygame
from copy import copy
from Const import *

class Entity():
    def __init__(self, x, y, img, width=40, height=80):
        self.hp = 10
        self.vitesse = 1
        self.attaque = 1
        self.defence = 0
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img, (width,height))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.velo_y = 0
        pass

    def move(self,collidlist):
        
        hitbox_back = copy(self.hitbox)
        self.hitbox.y += 16
        falling = True
        if(self.hitbox.collidelist(collidlist) != -1): 
            falling = False
            self.hitbox.y -= 16
        
        print (self.velo_y)

        if self.velo_y < 0:
            falling = False
        
        hitbox_back = copy(self.hitbox)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.hitbox.x -= 8 * self.vitesse
            if self.hitbox.x < 0:
                self.hitbox.x = 0 * self.vitesse
        if key[pygame.K_RIGHT]:
            self.hitbox.x += 8 * self.vitesse
            if self.hitbox.x > screen_width - self.hitbox.width : 
             self.hitbox.x -= 8  * self.vitesse


        if key[pygame.K_UP] and not falling and self.velo_y == 0:
            self.velo_y -= 80

        if self.velo_y < 0:
            self.hitbox.y = self.hitbox.y + self.velo_y + 16
            self.velo_y += 16
        if self.velo_y > 0:
            self.hitbox.y = self.hitbox.y + self.velo_y - 16
            self.velo_y -= 16
            
            if self.hitbox.y < 0: # a auto
                self.hitbox.y = 0
        
        if(self.hitbox.collidelist(collidlist) != -1): 
            self.hitbox = hitbox_back
            print (self.velo_y)
        
    
        #y = y-taille de case * vitesse

    def attack(self):
        pass

    def defence(self):
        pass
    #pdv = pdv  - degat * defense

