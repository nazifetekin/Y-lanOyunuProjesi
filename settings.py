import pygame

#oyun ekran boyutu
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

#bilgi pabeli yüksekliği
INFO_PANEL_HEIGHT = 40

#renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (60, 179, 113)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (20, 20, 20)

#internetten bulduğum piksel fontunu kullandım(Thixel.ttf)
pygame.font.init()
try:
    #yazı boyutları
    thixel_font = pygame.font.Font('thixel.ttf', 90) 
    thixel_font_medium = pygame.font.Font('thixel.ttf', 36) 
    thixel_font_small = pygame.font.Font('thixel.ttf', 30)  
except pygame.error:
    print("Thixel fontu yüklenemedi. sistemde bulunan font kullanılıyor")
    thixel_font = pygame.font.SysFont(None, 48)
    thixel_font_medium = pygame.font.SysFont(None, 30)
    thixel_font_small = pygame.font.SysFont(None, 24)

#ana girişe arka plan resmini yüklendi
try:
    background_image = pygame.image.load('oyunarkaplan.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error:
    background_image = None
    print(".....arka plan resmi yüklenmedi.....")

# Saat
clock = pygame.time.Clock()

#seviye ayarları(hız, score,rnek)
levels = {
    1: {'speed': 6, 'target_score': 5, 'color': (100, 100, 255)},
    2: {'speed': 8, 'target_score': 10, 'color': (100, 255, 100)},
    3: {'speed': 10, 'target_score': 15, 'color': (255, 100, 100)}
}

#FPS değeri. saniyede 60 kare çizmesini hedefleiyor.
FPS = 60
