import pygame
import sys
from settings import (
    WIDTH, HEIGHT, BLACK, WHITE, levels, clock, thixel_font_small, 
    INFO_PANEL_HEIGHT, DARK_GRAY, FPS, CELL_SIZE
)
from models.snake import Snake
from models.food import Food
from models.wall import Wall
from arayuz.menu import start_menu, show_level_text, game_over_menu

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.snake = None
        self.wall = None
        self.food = None
        self.level = 1
        self.score = 0
        self.game_over_reason = ""
        
    def start_game(self):
        start_menu(self.screen)  #başlangıç menüsünü gösterir
        self.run_game()  #oyunu başlatır
        
    def run_game(self):
        #oyun nesnelerini oluşturur
        self.level = 1
        self.score = 0
        self.snake = Snake()
        self.wall = Wall(self.level)
        self.food = Food(self.wall.body, self.snake)
        
        #lvel 1 yazısını gösterir
        show_level_text(self.screen, self.level)
        
        base_speed = levels[self.level]['speed']
        current_speed = base_speed
        
        running = True
        while running:
            clock.tick(current_speed)
            
            #ekranı temizler
            self.screen.fill(BLACK)
            
            # Etkinlikler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_key_event(event)

            self.snake.move()

            #yılanın yemi yeme kontrolü yapılır
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food = Food(self.wall.body, self.snake)
                
                # yılan yemi yedikçe hızı*0.2  arttar
                current_speed = base_speed + (self.score * 0.2)

            #engele çarpma kontrolü
            if self.snake.check_collision():
                self.game_over_reason = "Duvara çarptın!"
                running = False
            
            #duvara çarpma kontrolü
            if self.snake.body[0] in self.wall.body:
                self.game_over_reason = "Engele çarptın!"
                running = False

            #çizim
            self._draw_game_elements()

            #yılan hedefe ulaştımı seviye atlar
            if self.score >= levels[self.level]["target_score"] and self.level < 3:
                self.level += 1
                show_level_text(self.screen, self.level)  # Level geçiş ekranı
                self.wall = Wall(self.level)
                base_speed = levels[self.level]['speed']
                current_speed = base_speed + (self.score * 0.2)

            #level üçte skor 15'e ulaştığı zman oyuncu oyunu kzanır
            if self.level == 3 and self.score >= levels[self.level]["target_score"]:
                self.game_over_reason = "Tebrikler! Tüm levelleri tamamladın!"
                running = False

        #ve oyun biter
        game_over_menu(self.screen, self.game_over_reason, self.score, self.run_game)
    
    def _handle_key_event(self, event):
        """Klavye olaylarını işle"""
        if event.key == pygame.K_UP and self.snake.direction != (0, CELL_SIZE):
            self.snake.direction = (0, -CELL_SIZE)
        if event.key == pygame.K_DOWN and self.snake.direction != (0, -CELL_SIZE):
            self.snake.direction = (0, CELL_SIZE)
        if event.key == pygame.K_LEFT and self.snake.direction != (CELL_SIZE, 0):
            self.snake.direction = (-CELL_SIZE, 0)
        if event.key == pygame.K_RIGHT and self.snake.direction != (-CELL_SIZE, 0):
            self.snake.direction = (CELL_SIZE, 0)
    
    def _draw_game_elements(self):
        """Oyun elemanlarını çiz"""
        #oyunda kullandığımız yılan ,food ve engelleri çizer
        self.wall.draw(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        #bilgi paneli ve oyun panelini ayoror.
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, WIDTH, INFO_PANEL_HEIGHT))
        pygame.draw.line(self.screen, WHITE, (0, INFO_PANEL_HEIGHT), (WIDTH, INFO_PANEL_HEIGHT), 2)

        #skor ve level yazısı
        score_text = thixel_font_small.render(f'Skor: {self.score}  Level: {self.level}', True, WHITE)
        target_text = thixel_font_small.render(f'Hedef: {levels[self.level]["target_score"]}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(target_text, (WIDTH - 120, 10))

        pygame.display.update()
