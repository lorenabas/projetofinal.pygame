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

class Game:
    #FPS
    FPS = 60    
    
    #Inicializador para classe de jogo para configurar largura, altura e título
    def __init__(self, image_path, título, altura, peso):
        self.título = título
        self.altura = altura
        self.peso = peso

        #Cria a janela de tamanho especificado para exibir o jogo
        self.game_screen = pygame.display.set_mode((altura, peso))
        #set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(título)

        # Carregar e definir a imagem de fundo
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (altura, peso))