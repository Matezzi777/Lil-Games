import pygame
from menu import Menu
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('LilGames')

menu = Menu(screen)

menu.run()
pygame.quit()