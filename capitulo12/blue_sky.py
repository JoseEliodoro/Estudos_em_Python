import pygame
import sys

from player import Player

def blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    player = Player(screen)
    bg_color = (0, 190, 255)
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
        screen.fill(bg_color)
        player.blitme()
        pygame.display.flip()

        
        
blue_sky()