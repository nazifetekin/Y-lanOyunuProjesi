import pygame
import random
from settings import CELL_SIZE, WIDTH, HEIGHT, RED, INFO_PANEL_HEIGHT

class Food:
    def __init__(self, walls, snake):
        self.position = self.random_position(walls, snake)

    def random_position(self, walls, snake):
        while True:
            #y koordinatını info_panel_height'dan sonra başlatır yani skor,hedef ve levelin altında başlatır.
            pos = (
                random.randrange(0, WIDTH, CELL_SIZE), 
                random.randrange(INFO_PANEL_HEIGHT + CELL_SIZE, HEIGHT, CELL_SIZE)
            )
            if pos not in walls and pos not in snake.body:
                return pos

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))
