from PyGame import Game
import pygame
import random
from os import path
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLUE_COLOR, FPS, QUIT, GAME

def init_screen(tela):
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                state = GAME
                running = False

        screen.fill(BLUE_COLOR)

        pygame.display.flip()
    
    return state