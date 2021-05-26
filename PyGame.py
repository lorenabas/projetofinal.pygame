#Acessar a biblioteca do pygame
import pygame

#Tamanho da tela
SCREEN_TITLE = 'Crossy RPG' 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#Cores
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
#Tempo
clock = pygame.time.Clock()
# Fonte para o texto do jogo
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)