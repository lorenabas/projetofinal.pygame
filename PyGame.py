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
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
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
                player_character.movimento(direction, self.height)
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


                # Termina o jogo se houver colisão entre o jogador e o carro ou diploma e chapeu
                # Feche o jogo se perder e reinicie o loop do jogo se vencer
                if player_character.verifica_colisao(carro_0):
                    game_over = True
                    ganhou = False
                    text = font.render('You Lose!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (275, 350))
                    pygame.display.update()
                    clock.tick(1)
                    break
                elif player_character.verifica_colisao(diploma, chapeu):
                    game_over = True
                    ganhou = True
                    text = font.render('You Win!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (275, 350))
                    pygame.display.update()
                    clock.tick(1)
                    break

            # atualizar todos os gráficos do jogo
            pygame.display.update()
            # Clique no relógio para atualizar tudo dentro do jogo
            clock.tick(self.TICK_RATE)

            # Recomeça o loop do jogo se o jogador ganhar
            # Termina o loop do jogo se o jogador perder
            if ganhou:
                self.run_game_loop(level_speed + 0.5)
            else:
                return

# Cria classe de elemento do jogo para definir outras classes dos outros elementos do jogo
class ElementoJogo:

    def __init__(self, image_path, x, y, width, height):
        # Importar a imagem e ajustar o tamanho da imagem
        imagem_elemento = pygame.image.load(image_path)
        self.imagem = pygame.transform.scale(imagem_elemento, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    #Desenha o elemento ao fazer blit no plano de fundo - game_screen
    def draw(self, background):
        background.blit(self.imagem, (self.x_pos, self.y_pos))

# Cria classe da personagem do jogador
class PlayerCharacter(ElementoJogo):

    # Quantos espaços/quadrados o personagem se mexe por segundo
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Função para mexer a personagem - vai para cima se a direção > 0, e para baixo se a direção for < 0
    def movimento(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Verifica que a personagem não sai da tela
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height -40
    
    # Retorna que não houve colisão (False) se as posições x e y não se sobrepuserem
    # Retorna que houve colisão (True) se as posições x e y se sobrepuserem
    def verifica_colisao(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True