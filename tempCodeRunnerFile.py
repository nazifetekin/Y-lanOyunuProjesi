import pygame
import random
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ekranı oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Yılan Oyunu')

# Saat
clock = pygame.time.Clock()

# Yılan Sınıfı
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (CELL_SIZE, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for part in self.body:
            pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        # Kendine çarpma
        if head in self.body[1:]:
            return True
        # Ekran dışı çıkma
        if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
            return True
        return False

# Yem Sınıfı
class Food:
    def __init__(self, walls):
        self.position = self.random_position(walls)

    def random_position(self, walls):
        while True:
            pos = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
            if pos not in walls:
                return pos

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Duvar Sınıfı
class Wall:
    def __init__(self, level):
        self.body = []
        if level >= 2:
            for i in range(100, 500, CELL_SIZE * 4):
                self.body.append((i, 200))
        if level == 3:
            for i in range(50, 550, CELL_SIZE * 6):
                self.body.append((i, 100))

    def draw(self):
        for part in self.body:
            pygame.draw.rect(screen, BLUE, (*part, CELL_SIZE, CELL_SIZE))

# Seviye Ayarları
levels = {
    1: {'speed': 10},
    2: {'speed': 15},
    3: {'speed': 20}
}

# Ana oyun fonksiyonu
def main():
    level = 1
    while level <= 3:
        snake = Snake()
        wall = Wall(level)
        food = Food(wall.body)
        running = True
        speed = levels[level]['speed']

        while running:
            clock.tick(speed)
            screen.fill(BLACK)

            # Etkinlikler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                        snake.direction = (0, -CELL_SIZE)
                    if event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                        snake.direction = (0, CELL_SIZE)
                    if event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                        snake.direction = (-CELL_SIZE, 0)
                    if event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                        snake.direction = (CELL_SIZE, 0)

            snake.move()

            # Yem Yeme
            if snake.body[0] == food.position:
                snake.grow()
                food = Food(wall.body)

            # Çarpışmalar
            if snake.check_collision() or snake.body[0] in wall.body:
                running = False

            # Çizimler
            snake.draw()
            food.draw()
            wall.draw()

            # Skor ve Level Yazısı
            font = pygame.font.SysFont(None, 24)
            score_text = font.render(f'Score: {len(snake.body) - 1}  Level: {level}', True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.update()

            # Seviye Atlama
            if len(snake.body) - 1 >= 5 * level:
                level += 1
                running = False

    # Oyun Bitti
    game_over()

def game_over():
    font = pygame.font.SysFont(None, 40)
    text = font.render('Tebrikler! Oyunu Bitirdin!', True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
