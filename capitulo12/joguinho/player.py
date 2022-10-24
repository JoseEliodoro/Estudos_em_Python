#Bibliotecas
import pygame

class Player():
    def __init__(self, ai_setting, screen):
        
        self.ai_setting = ai_setting
        self.screen = screen
        self.img = pygame.image.load('img/foguete.bmp')
        
        self.rect = self.img.get_rect() #Intânci que possue as cordenadas interna da img
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        
        self.position = [0, 0, 1, 0]
        
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
    
    def test(self):
        self.rect = self.img.get_rect()
    
    def movings(self):
        if(self.moving_right and self.rect.right < self.ai_setting.width):
            self.x += self.ai_setting.speed_player
        if(self.moving_left and self.rect.left > 0):
            self.x -= self.ai_setting.speed_player
        self.rect.centerx = self.x
        
        if(self.moving_up and self.rect.top > 0):
            self.y -= self.ai_setting.speed_player
        if(self.moving_down and self.rect.bottom < self.ai_setting.height):
            self.y += self.ai_setting.speed_player
        self.rect.centery = self.y
        
    def bitmap(self):
        self.screen.blit(self.img, self.rect)
        
    