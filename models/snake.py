import pygame
from settings import CELL_SIZE, WIDTH, HEIGHT, GREEN, DARK_GREEN, INFO_PANEL_HEIGHT

class Snake:
    def __init__(self):
        #bilgi panelinin altında başlatır.yani skor,ievel ve hedefin altından başlatır.o kısmı dahil almaz.
        self.body = [(100, INFO_PANEL_HEIGHT + 60)] 
        self.direction = (CELL_SIZE, 0)
        self.grow_pending = False

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [head] + self.body
        
        #eğer büyüme beklemiyorsa son parçayı çıkar
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False  #büyüme işlemi tamamlandı

    def grow(self):
        self.grow_pending = True  #bir sonraki harekette yılan  büyüyecek

    def draw(self, screen):
        for i, part in enumerate(self.body):
            #yılanın baş kısmını daha koyu yeşil yapar.
            color = DARK_GREEN if i == 0 else GREEN
            pygame.draw.rect(screen, color, (*part, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        #kendine çarpma kontrolü yapar. kendine çarparsa ölür
        if head in self.body[1:]:
            return True
        #duvara çarpma kontrolü yapar. eğer duvara çarparsa yanar.
        if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
            return True
        return False
