import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, obj_setting, screen, player, direction):
        super(Bullet, self).__init__()
        self.screen = screen
        self.obj_setting = obj_setting
        self.player = player
        self.direction = direction
        self.rect = pygame.Rect(0, 0, obj_setting.width_bullet, obj_setting.height_bullet)
        
        self.speed = obj_setting.speed_bullet
        if(direction == [1, 0, 0, 0]):
            self.rect.centerx = self.player.rect.left
            self.rect.centery = self.player.rect.centery -6
        elif(direction == [0, 1, 0, 0]):
            self.rect.centerx = self.player.rect.right
            self.rect.centery = self.player.rect.centery -6
        elif(direction == [0, 0, 0, 1]):
            self.rect.centerx = self.player.rect.centerx
            self.rect.bottom = self.player.rect.bottom
        elif(direction == [1, 0, 1, 0]):
            self.rect.centerx = self.player.rect.right
            self.rect.centery = self.player.rect.centery
        elif(direction == [0, 1, 1, 0]):
            self.rect.centerx = self.player.rect.left
            self.rect.centery = self.player.rect.top
        elif(direction == [0, 1, 0, 1]):
            self.rect.centerx = self.player.rect.left
            self.rect.centery = self.player.rect.bottom
        elif(direction == [1, 0, 0, 1]):
            self.rect.centerx = self.player.rect.right
            self.rect.bottom = self.player.rect.bottom
        else:
            self.rect.centerx = self.player.rect.centerx
            self.rect.bottom = self.player.rect.top
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        if(self.direction[0] == 1):
            self.x += self.speed
        if(self.direction[1] == 1):
            self.x -= self.speed
            
        if(self.direction[2] == 1):
            self.y -= self.speed
        if(self.direction[3] == 1):
            self.y += self.speed
            
        self.rect.x = self.x
        self.rect.y = self.y
    
        
    def draw_bullet(self):
        
        pygame.draw.rect(self.screen, (255,0,0), self.rect)  