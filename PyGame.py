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

    def run_game_loop(self, level_speed):
        game_over = False
        ganhou = False
        direction = 0
        player_character = PlayerCharacter('personagem_m.png', 375, 700, 50, 50)
        carro_0 = Carro('carro_dp.png', 20, 600, 50, 50)

        # aumento de velocidade
        carro_0.SPEED *= level_speed

        # criação de outro carro
        carro_1 = Carro('carro_pf.png', self.width - 40, 400, 50, 50)
        carro_1.SPEED *= level_speed

        # criação de outro carro
        carro_2 = Carro('carro_pi.png', 20,200, 50, 50)
        carro_2.SPEED *= level_speed
      
        diploma = Diploma('diploma.png', 375, 50, 50, 50)
        chapeu = Chapeu('chapeu_formatura.png', 375, 50, 50)

        # Loop principal, atualiza o jogo até que is_game_over = True
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Verifica se a tecla está apertada
                elif event.type == pygame.KEYDOWN:
                    # Mexe para cima se a seta para cima está sendo apertada
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Mexe para baixo se a seta para baixo está sendo apertada
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Verifica quando a tecla deixa é solta
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

                # Refaz o plano de fundo
                self.game_screen.fill(WHITE_COLOR)
                self.game_screen.blit(self.image, (0, 0))

                # desenha o diploma e o chapeu
                diploma.draw(self.game_screen)
                chapeu.draw(self.game_screen)
            
                # muda a posição do jogador
                player_character.move(direction, self.height)
                # coloca o jogador na nova posição
                player_character.draw(self.game_screen)

                # move a posição do carro
                carro_0.move(self.width)
                carro_0.draw(self.game_screen)
            
                # adcionar novos carros
                if level_speed > 2:
                    carro_1.move(self.width)
                    carro_1.draw(self.game_screen)
                if level_speed > 4:
                    carro_2.move(self.width)
                    carro_2.draw(self.game_screen)