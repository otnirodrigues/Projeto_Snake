import random
from webbrowser import get
import pygame
from pygame import *
from pyparsing import White


class Apllication():
    
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    snake_direction = LEFT
    cont = 0

    # Metodo que inicia o pygame e chama os outros metodos
    def __init__(self):
       pygame.init()
       self.criando_janela()
       self.criando_snake()
       self.criando_maca()
       self.game()

    def criando_janela(self):
        # Criando uma janela de tamanho 600x600, e alterando o nome da janela para 'Snake'
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')

    def criando_snake(self):
        # Setando a posição inicial da snake na matriz
        # Setando o tamanho da Snake
        # Setando a cor da snake
        self.snake = [(200,200), (210,200), (220,200)]
        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((0, 128, 0))
        
    def update_snake_matriz(self):
        # Atualizando a snake na matriz
        for pos in self.snake:
            self.screen.blit(self.snake_skin, pos)

    def criando_maca(self):
        # Setando um objeto maça, de tamanho 10x10
        # Setando a cor da Maça
        self.maca = pygame.Surface((10, 10))
        self.maca2 = pygame.Surface((10, 10))
        self.maca.fill((255, 0, 0))
        self.maca2.fill((255, 0, 0))
        self.pos_maca = self.setando_maca_grid()
        self.pos_maca2 = self.setando_maca_grid()
        
    def setando_maca_grid(self):
        # setando uma posição na matriz aleatoriamente, o escopo está dentro de 0 à 590, pois a matriz vai de 0 à 600
        # Tratando x e y, para que retorne um numero inteiro entre 0 e 590. // divide e arredonda para int
        x = random.randint(0, 590)
        y = random.randint(0, 590)
        return(x//10 * 10, y//10 * 10)
    
    
    def colisao(self, c1, c2):
        # Criando um metodo para colisão da snake com a maça
        return(c1[0] == c2[0] and c1[1] == c2[1])
        

    def movimento_snake(self):
        # Metodo para definir regras de movimento snake
        for i in range(len(self.snake) -1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])
        if self.snake_direction == self.UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] -10)
        if self.snake_direction == self.DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] +10)
        if self.snake_direction == self.LEFT:
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
        if self.snake_direction == self.RIGHT:
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])
       

    def fps_snake(self):
        # Limitando a velocidade do FPS da Snake
        self.clock = pygame.time.Clock()
        self.clock.tick(15)

    def game_over(self):
        # Definindo os limites da janela, caso ultrapasse, game over
        if self.snake[0][0] == 600 or self.snake[0][1] == 600 or self.snake[0][0] <0 or self.snake[0][1] < 0:
            
            # Criando a tela de game over, definindo fonte e texto
            screen_over = pygame.display.set_mode((600, 400))
            font = pygame.font.SysFont("comicsansms", 45)
            text = font.render("Game Over", True, (255, 0, 0))           
            pygame.display.set_caption("Snake - Game Over")  
            texto_pos = (300 - text.get_width() // 2, 200 - text.get_height() // 2)
            
            # Setando os objetos para o novo display
            while True:  
                screen_over.fill((255,255,255))  
                screen_over.blit(text, texto_pos)
                self.clock.tick(60)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                pygame.display.update()

    def game(self):
        
        while True:

            self.fps_snake()

            # Captura os eventos que seram realizados
            # Inicia uma varredura, ao localizar o evento QUIT, encerra o game
            # Evento do type.key, localiza evento no teclado.
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake_direction = self.UP
                    if event.key == K_DOWN:
                        self.snake_direction = self.DOWN
                    if event.key == K_LEFT:
                        self.snake_direction = self.LEFT
                    if event.key == K_RIGHT:
                        self.snake_direction = self.RIGHT

            self.movimento_snake()
            self.game_over()

            # Tratando a colisão entre snake e maça
            # Gera uma nova posição para maça1 e maça2
            if self.colisao(self.snake[0], self.pos_maca):
                self.pos_maca = self.setando_maca_grid()
                self.snake.append((0,0))
                self.cont += 1
            elif self.colisao(self.snake[0], self.pos_maca2):
                    self.pos_maca2 = self.setando_maca_grid()
                    self.snake.append((0,0))
                    self.cont += 1 
            
            # Limpando a tela
            # Protando a maça na matrix
            self.screen.fill((255,255,255))
            self.update_snake_matriz()
            self.screen.blit(self.maca, self.pos_maca)
            self.screen.blit(self.maca2, self.pos_maca2)
            

            # Atualiza o display a toda interação do while
            pygame.display.update()

Apllication()