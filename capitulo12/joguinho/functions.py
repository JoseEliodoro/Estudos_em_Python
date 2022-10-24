#Bibliotecas
import sys
import pygame
import os
from bullet import Bullet

def update_screen(player, screen, ai_setting, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.bitmap()
    pygame.display.flip()
    
def check_events(ai_setting, screen, player, bullets):
   
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
            if(event.type == pygame.KEYDOWN):
                check_keydown_events(event, ai_setting, screen, player, bullets)
            if(event.type == pygame.KEYUP):
                check_keyup_events(event, player)
                
            
                
def check_keydown_events(event, ai_setting, screen, player, bullets):
    
    if(event.key == pygame.K_RIGHT):
        player.moving_right = True
    elif(event.key == pygame.K_LEFT):
        player.moving_left = True
    elif(event.key == pygame.K_UP):
        player.moving_up = True
    elif(event.key == pygame.K_DOWN):
        player.moving_down = True
    
    if(event.key == pygame.K_a):
        direction = player.position[:]
        bullet = Bullet(ai_setting, screen, player, direction)  
        bullets.add(bullet)
        #print(direction)
    
    test(player)
      
def test(player):
    img = pygame.image.load('img/foguete.bmp')
    if(player.moving_right):
        player.img = pygame.transform.rotate(img, 270)
        player.position = [1, 0, 0, 0]
    elif(player.moving_left):
        player.img = pygame.transform.rotate(img, 90)
        player.position = [0, 1, 0, 0]
    if(player.moving_up):
        player.img = img
        player.position = [0, 0, 1, 0]
    elif(player.moving_down):
        player.img = pygame.transform.rotate(img, 180)
        player.position = [0, 0, 0, 1]
    
    if(player.moving_up and player.moving_left):      
        player.position = [0, 1, 1, 0]
        player.img = pygame.transform.rotate(img, 45)      
    elif(player.moving_up and player.moving_right):
        player.position = [1, 0, 1, 0]
        player.img = pygame.transform.rotate(img, 315)
    elif(player.moving_down and player.moving_left):
        player.position = [0, 1, 0, 1]
        player.img = pygame.transform.rotate(img, 135)
    elif(player.moving_down and player.moving_right):
        player.position = [1, 0, 0, 1]
        player.img = pygame.transform.rotate(img, 225)
    player.test()
    
        
def check_keyup_events(event, player):
    if(event.key == pygame.K_RIGHT):
        player.moving_right = False
    elif(event.key == pygame.K_LEFT):
        player.moving_left = False
    elif(event.key == pygame.K_UP):
        player.moving_up = False
    elif(event.key == pygame.K_DOWN):
        player.moving_down = False
    
    test(player)