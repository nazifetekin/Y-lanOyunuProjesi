import pygame
import sys
from game_manager import GameManager
from settings import WIDTH, HEIGHT, BLACK, clock

#pygame'i başlat
pygame.init()

#ekranı oluştururuz
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Yılan Oyunu')

#oyun yöneticisini oluşturur
game_manager = GameManager(screen)

if __name__ == '__main__':
    game_manager.start_game()
