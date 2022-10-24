import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('capitulo12/mario2.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx 
        #Atributos do rect center, centerx, centery, top, bottom, left, right, x ou y
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self): #Desenha a espaçonave em sua posição atual.
        self.screen.blit(self.image, self.rect)