import random
from tkinter import LEFT, RIGHT
import pygame
from pygame import *


class Apllication():
    
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    snake_direction = LEFT

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
        self.snake_skin.fill((255, 255, 255))
        
        
    
    def update_snake_matriz(self):
        # Atualizando a snake na matriz
        for pos in self.snake:
            self.screen.blit(self.snake_skin, pos)

    
    def criando_maca(self):
        # Setando um objeto maça, de tamanho 10x10
        # Setando a cor da Maça
        self.maca = pygame.Surface((10, 10))
        self.maca.fill((255, 0, 0))
        self.pos_maca = self.setando_maca_grid()
        
    def setando_maca_grid(self):
        #setando uma posição na matriz aleatoriamente, o escopo está dentro de 0 à 590, pois a matriz vai de 0 à 600
        
        x = random.randint(0, 590)
        y = random.randint(0, 590)
        return(x//10 * 10, y//10 * 10)
    
    def colisao(self, c1, c2):
        # Criando um metodo para colisão da snake com a maça
        return(c1[0] == c2[0] and c1[1] == c2[1])
        

    def movimento_snake(self):

        # Metodo para definir regras de movimento snake
        if self.snake_direction == self.UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] -10)
        if self.snake_direction == self.DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] +10)
        if self.snake_direction == self.LEFT:
            self.snake[0] = (self.snake[0][1] - 10, self.snake[0][0])
        if self.snake_direction == self.RIGHT:
            self.snake[0] = (self.snake[0][1] + 10, self.snake[0][0])
        for i in range(len(self.snake) -1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])


    def fps_snake(self):

        # Limitando a velocidade do FPS da Snake
        clock = pygame.time.Clock()
        clock.tick(5)
    
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

            # Tratando a colisão entre snake e maça
            # Gera uma nova posição para maça
            if self.colisao(self.snake[0], self.pos_maca):
                self.pos_maca = self.setando_maca_grid()
                self.snake.append((0,0))
            
            # Limpando a tela
            # Protando a maça na matrix
            self.screen.fill((0,0,0))
            self.update_snake_matriz()
            self.screen.blit(self.maca, self.pos_maca)

            # Atualiza o display a toda interação do while
            pygame.display.update()

Apllication()