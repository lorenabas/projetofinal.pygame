#Acessar a biblioteca do pygame
import pygame
import pygame.freetype
from config import SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE_COLOR, BLACK_COLOR, BLUE_COLOR 
from pathlib import Path

base = Path(__file__).parent

#Tempo
clock = pygame.time.Clock()
# Fonte para o texto do jogo
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)
pygame.mixer.init()

# Carrega os sons do jogo
pygame.mixer.music.load(f'{base}\Música inicial.mp3')
pygame.mixer.music.set_volume(0.4)
end_sound = pygame.mixer.Sound(f'{base}\Colisão.mp3')

class Game:  

    #Inicializador para classe de jogo para configurar largura, altura e título
    def __init__(self, image_path, título, largura, altura, FPS):
        self.FPS = FPS
        self.título = título
        self.altura = altura
        self.largura = largura

        #Cria a janela de tamanho especificado para exibir o jogo
        self.game_screen = pygame.display.set_mode((largura, altura))
        # definir a cor da janela do jogo para branco
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(título)

        # Carregar e definir a imagem de fundo
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (largura, altura))
        self.init_screen(self.game_screen)

    def init_screen(self, tela):
        running = True
        while running:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    self.run_game_loop(1)
                    running = False

            # Cria imagem do menu inicial
            inicial_image = pygame.image.load('CROSSY INSPER (1).png')
            self.game_screen.blit(inicial_image, (0, 0))

            pygame.display.flip()

    def run_game_loop(self, level_speed):
        game_over = False
        ganhou = False
        direction = 0
        direction2 = 0

        #nome da imagem, posicao no eixo x, posicao no eixo y, largura, altura
        player_character = PlayerCharacter('personagem_m.png', 375, 700, 50, 50)
        carro_0 = CarroCharacter('carro_pi.png', 20, 580, 140, 90)

        # aumento de velocidade
        carro_0.SPEED *= level_speed

        # criação de outro carro
        carro_1 = CarroCharacter2('carro_pf.png', self.largura - 40, 380, 140, 80)
        carro_1.SPEED *= level_speed

        # criação de outro carro
        carro_2 = CarroCharacter('carro_dp.png',20,160, 140, 90)
        carro_2.SPEED *= level_speed

        diploma = Elementojogo('diploma.png', 375, 50, 50, 50)
        chapeu = Elementojogo('chapeu_formatura.png', 375, 50, 50, 50)

        # posicao na tela, largura, altura do objeto
        arbusto1 = Elementojogo('arbusto1.png.png', 370, 300, 70, 70)
        arbusto2 = Elementojogo('arbusto1.png.png', 200, 510, 70, 70)
        arbusto3 = Elementojogo('arbusto1.png.png', 500, 90, 70, 70)

        pygame.mixer.music.play(loops=-1)

        # Loop principal, atualiza o jogo até que is_game_over = True
        while not game_over:
            print('1')
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
                    # Mexe para direira se a seta para cima está sendo apertada
                    if event.key == pygame.K_RIGHT:
                        direction2 = -1
                    # Mexe para esquerda se a seta para baixo está sendo apertada
                    elif event.key == pygame.K_LEFT:
                        direction2 = 1
                # Verifica quando a tecla deixa é solta
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        direction2 = 0
               
                
            # Refaz o plano de fundo
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            # desenha o diploma e o chapeu
            diploma.draw(self.game_screen)
            chapeu.draw(self.game_screen)
            arbusto1.draw(self.game_screen)
            arbusto2.draw(self.game_screen)
            arbusto3.draw(self.game_screen)
        
            # muda a posição do jogador
            player_character.movimento(direction, self.largura)
            player_character.movimento2(direction2, self.largura)
            # coloca o jogador na nova posição
            player_character.draw(self.game_screen)

            # move a posição do carro
            carro_0.move(self.largura)
            carro_0.draw(self.game_screen)
        
            # adcionar novos carros
            if level_speed > 2:
                carro_1.move(self.largura)
                carro_1.draw(self.game_screen)
            if level_speed > 4:
                carro_2.move(self.largura)
                carro_2.draw(self.game_screen)


            # Termina o jogo se houver colisão entre o jogador e o carro ou diploma e chapeu
            # Feche o jogo se perder e reinicie o loop do jogo se vencer
            if player_character.verifica_colisao(carro_0):
                game_over = True
                ganhou = False
                text = font.render('You Lost!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                self.end_sound.play() 
                break
            elif level_speed > 2 and level_speed < 4:
                if player_character.verifica_colisao(carro_1):
                    game_over = True
                    ganhou = False
                    text = font.render('You Lost!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (275, 350))
                    pygame.display.update()
                    clock.tick(1)
                    self.end_sound.play() 
                    break
            elif level_speed > 4:
                if player_character.verifica_colisao(carro_1):
                    game_over = True
                    ganhou = False
                    text = font.render('You Lost!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (275, 350))
                    pygame.display.update()
                    clock.tick(1)
                    self.end_sound.play() 
                    break
                elif player_character.verifica_colisao(carro_2):
                    game_over = True
                    ganhou = False
                    text = font.render('You Lost!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (275, 350))
                    pygame.display.update()
                    self.end_sound.play() 
                    clock.tick(1)
                    break
            if player_character.verifica_colisao(diploma):
                game_over = True
                ganhou = True
                text = font.render('You Won!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.verifica_colisao(chapeu):
                game_over = True
                ganhou = False
                text = font.render('You Won!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif any(player_character.verifica_colisoes([arbusto1, arbusto2, arbusto3])):
                i_arbusto = (player_character.verifica_colisoes([arbusto1, arbusto2, arbusto3])).index(True)
                print(player_character.SPEED)
                if i_arbusto == 0:
                    x = 370
                    y = 300
                elif i_arbusto == 1:
                    x = 200
                    y = 510
                elif i_arbusto == 2:
                    x = 500
                    y = 90

                if direction < 0:
                    player_character.y_pos = y-40
                elif direction > 0:
                    player_character.y_pos = y+40
                elif direction2 < 0:
                    player_character.x_pos = x-40
                elif direction2 > 0:
                    player_character.x_pos = x+40
                
              
            # atualizar todos os gráficos do jogo
            pygame.display.update()
            # Clique no relógio para atualizar tudo dentro do jogo
            clock.tick(self.FPS)

        # Recomeça o loop do jogo se o jogador ganhar
        # Termina o loop do jogo se o jogador perder
        if ganhou:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

# Cria classe de elemento do jogo para definir outras classes dos outros elementos do jogo
class Elementojogo:

    def __init__(self, image_path, x, y, largura, altura):
        # Importar a imagem e ajustar o tamanho da imagem
        imagem_elemento = pygame.image.load(image_path)
        self.imagem = pygame.transform.scale(imagem_elemento, (largura, altura))

        self.x_pos = x
        self.y_pos = y

        self.altura = altura
        self.largura = largura

    #Desenha o elemento ao fazer blit no plano de fundo - game_screen
    def draw(self, background):
        background.blit(self.imagem, (self.x_pos, self.y_pos))

# Cria classe da personagem do jogador
class PlayerCharacter(Elementojogo):

    # Quantos espaços/quadrados o personagem se mexe por segundo
    SPEED = 5

    def __init__(self, image_path, x, y, largura, altura):
        super().__init__(image_path, x, y, largura, altura)


    # Função para mexer a personagem - vai para cima se a direção > 0, e para baixo se a direção for < 0
    def movimento(self, direction, max_altura):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Verifica que a personagem não sai da tela
        if self.y_pos >= max_altura - 40:
            self.y_pos = max_altura -40
        elif self.y_pos <= 0:
            self.y_pos = 40
        
    # Função para mexer a personagem - vai para esquerda se a direção2 > 0, e para direita se a direção2 for < 0
    def movimento2(self, direction2, max_largura):
        if direction2 > 0:
            self.x_pos -= self.SPEED
        elif direction2 < 0:
            self.x_pos += self.SPEED

        # Verifica que a personagem não sai da tela
        if self.x_pos >= max_largura - 40:
            self.x_pos = max_largura -40
        elif self.x_pos <= 0:
            self.x_pos = 20
        
    
    # Retorna que não houve colisão (False) se as posições x e y não se sobrepuserem
    # Retorna que houve colisão (True) se as posições x e y se sobrepuserem
    def verifica_colisao(self, other_body):
        if self.y_pos > other_body.y_pos + ((3*other_body.altura)/4):
            return False
        elif self.y_pos + ((3*self.altura)/4) < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + ((3*other_body.largura)/4):
            return False
        elif self.x_pos + ((3*self.largura)/4) < other_body.x_pos:
            return False

        return True
    
    def verifica_colisao2(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.altura/2:
            return False
        elif self.y_pos + self.altura/2 < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.largura/2:
            return False
        elif self.x_pos + self.largura/2 < other_body.x_pos:
            return False

        return True

    def verifica_colisoes(self, lista_corpos):
        l_boolean = []
        for i in lista_corpos:
            l_boolean.append(self.verifica_colisao2(i))
        
        return l_boolean

# Classe para representar os carros não controlados pelo jogador
class CarroCharacter(Elementojogo):
    # Quantas peças o carro se move por segundo
    SPEED = 1
    def __init__(self, image_path, x, y, largura, altura):
        super().__init__(image_path, x, y, largura, altura)
    # A função Mover irá mover o carro para a direita e ao chegar no final da tela voltar para o começo
    def move(self, max_largura):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_largura - 40:
            self.SPEED = -abs(self.SPEED)
            self.x_pos = 20
        self.x_pos += self.SPEED

# Classe para representar os carros não controlados pelo jogador (carro 1)
class CarroCharacter2(Elementojogo):
    # Quantas peças o carro se move por segundo
    SPEED = 1
    def __init__(self, image_path, x, y, largura, altura):
        super().__init__(image_path, x, y, largura, altura)
    # A função Mover irá mover o carro para a esquerda automaticamente e ao chegar no final da tela voltar par o começo
    def move(self, max_largura):
        if self.x_pos >= max_largura - 40:
            self.SPEED = -abs(self.SPEED)
        elif self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
            self.x_pos = max_largura - 40
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('background1.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS) 
#new_game.run_game_loop(1)

pygame.quit()
quit()