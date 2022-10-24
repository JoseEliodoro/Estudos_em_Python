#Bibliotecas
from pygame.sprite import Group
import pygame
from bullet import Bullet

#importando classes
from setting import Settings
from player import Player

#Importando modolu
import functions as fun

def start(): #Função que start o jogo
    pygame.init() #Inicia a janela
    ai_setting = Settings() #Classe com as configurações do jogo
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height)) #Definindo dimensões iniciais da janela
    
    pygame.display.set_caption('JOGUINHO') #Definindo título da janela
    
    player = Player(ai_setting, screen) #instância do player
    
    bullets = Group()
    while True: #Laço para o jogo continuar rodando
        fun.check_events(ai_setting, screen, player, bullets)
        bullets.update()
        player.movings()
        
        fun.update_screen(player, screen,ai_setting, bullets)
        
            
start()