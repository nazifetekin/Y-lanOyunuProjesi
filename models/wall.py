import pygame
from settings import CELL_SIZE, WIDTH, HEIGHT, BLUE

class Wall:
    def __init__(self, level):
        self.body = []
        
        #level 1: basit engel duvarlarından oluşuyor.
        if level == 1:
            #köşelerin hepsinde aşağıya doğru küçük engeller vardır
            for i in range(0, 100, CELL_SIZE):
                self.body.append((i, i))
                self.body.append((WIDTH - i - CELL_SIZE, i))
                self.body.append((i, HEIGHT - i - CELL_SIZE))  # Sol alt köşe
                self.body.append((WIDTH - i - CELL_SIZE, HEIGHT - i - CELL_SIZE))
        
        #level 2: level1'e göre daha zordur.
        elif level == 2:
            #orta kısmımda yatay engel duvarlarından oluşur. bir kare bir boşluk bir kare diye devam eder.
            for i in range(100, 500, CELL_SIZE * 2):
                self.body.append((i, 100))
                self.body.append((i, 300))
        
        #level 3: leve2'e göre daha zordur.
        elif level == 3:
            #orta kısımda artı işartindenm duvar engeli var.
            for i in range(WIDTH // 2 - 60, WIDTH // 2 + 80, CELL_SIZE):
                self.body.append((i, HEIGHT // 2))  #yatay çizgi
            
            for i in range(HEIGHT // 2 - 60, HEIGHT // 2 + 80, CELL_SIZE):
                self.body.append((WIDTH // 2, i))  #dikey çizgi
            
            # Köşelerde küçük engeller
            for i in range(0, 120, CELL_SIZE):
                self.body.append((i, i))
                self.body.append((WIDTH - i - CELL_SIZE, i))
                self.body.append((i, HEIGHT - i - CELL_SIZE))  # Sol alt köşe
                self.body.append((WIDTH - i - CELL_SIZE, HEIGHT - i - CELL_SIZE))  # Sağ alt köşe

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, BLUE, (*part, CELL_SIZE, CELL_SIZE))
