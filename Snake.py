import random
import pygame
from pygame import *


class Apllication():
    
    # Metodo que inicia o pygame e chama os outros metodos
    def __init__(self):
       pygame.init()
       self.criando_janela()
       #self.criando_snake()
       #self.criando_maca()
       self.game()

    def criando_janela(self):
        
        # Criando uma janela de tamanho 600x600, e alterando o nome da janela para 'Snake'
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')

    def criando_snake(self):
        # Setando a posição inicial da snake na matriz
        # Setando o tamanho da Snake
        # Setando a cor da snake
        snake = [(200,200), (210,200)]
        snake_skin = pygame.Surface((10, 10))
        snake_skin.fill((255, 255, 255))
        #snake_direction = self.direcao(self.LEFT)
    
    def criando_maca(self):
        # Setando um objeto maça, de tamanho 10x10
        # Setando a cor da Maça
        self.maca = pygame.Surface((10, 10))
        self.maca.fill((255, 0, 0))

        #setando uma posição na matriz aleatoriamente, o escopo está dentro de 0 à 590, pois a matriz vai de 0 à 600
        self.maca_pos = (random.randint(0, 590), random.randint(0, 590))

    def direcao (self):
        self.UP = 0
        self.RIGHT = 1
        self.LEFT = 2
        self.DOWN = 3
        

    def game(self):

        while True:

            # Captura os eventos que seram realizados
            # Inicia uma varredura, ao localizar o evento QUIT, encerra o game
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            # Limpando a tela
            # Protando a maça na matrix
            self.screen.fill((0,0,0))
            self.screen.blit().criando_maca()

            # Atualizando a snake na matriz
            for pos in self.snake:
                self.screen.blit(pos).criando_snake()

            # Atualiza o display a toda interação do while
            pygame.display.update()


Apllication()