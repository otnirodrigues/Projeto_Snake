
import random
import pygame
from pygame import *


class Apllication():
    
    # Metodo que inicia o pygame e chama os outros metodos
    def __init__(self):
       pygame.init()
       self.criando_janela()
       self.criando_snake()
       self.criando_maca()
       self.fps_snake()
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
        
        
    
    def criando_maca(self):
        # Setando um objeto maça, de tamanho 10x10
        # Setando a cor da Maça
        self.maca = pygame.Surface((10, 10))
        self.maca.fill((255, 0, 0))

        #setando uma posição na matriz aleatoriamente, o escopo está dentro de 0 à 590, pois a matriz vai de 0 à 600
        self.maca_pos = (random.randint(0, 590), random.randint(0, 590))
     

    def fps_snake(self):

        # Limitando a velocidade do FPS da Snake
        clock = pygame.time.Clock()
        clock.tick(2)


    def mover_snake(self):

        # Importando o library turtle para capturar as ações
        # 'penup' == UP, 'right' == RIGHT, 'pendown' == DOWN, 'left' == LEFT
        # Setando a direção da Snake
        
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        

        if self.snake_direction == UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] -10)
        if self.snake_direction == DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] +10)
        if self.snake_direction == LEFT:
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
        if self.snake_direction == RIGHT:
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1] -10)
            
        for i in range(len(self.snake) -1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

    
    def game(self):
        self.snake_direction = 3
        while True:
            
            # Captura os eventos que seram realizados
            # Inicia uma varredura, ao localizar o evento QUIT, encerra o game
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            for event in pygame.event.get():
                if event.type == KEYUP:
                    self.snake_direction = self.mover_snake()
                if event.type == KEYDOWN:
                    self.snake_direction = self.mover_snake()
                if event.type == K_LEFT:
                    self.snake_direction = self.mover_snake
                if event.type == K_RIGHT:
                    self.snake_direction = self.mover_snake() 
                


            # Limpando a tela
            # Protando a maça na matrix
            self.screen.fill((0,0,0))
            self.screen.blit(self.maca, self.maca_pos)

            # Atualizando a snake na matriz
            for pos in self.snake:
                self.screen.blit(self.snake_skin, pos)


            # Atualiza o display a toda interação do while
            pygame.display.update()


Apllication()