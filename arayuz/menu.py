import pygame
import sys
from settings import (
    WIDTH, HEIGHT, BLACK, WHITE, GREEN, RED, YELLOW, 
    thixel_font, thixel_font_medium, background_image, clock, FPS
)
from arayuz.button import Button

def start_menu(screen):
    title_text = thixel_font.render('Yılan Oyunu', True, WHITE)
    
    #BAŞLA butonu oluşturur
    start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 40, "BAŞLA", GREEN, (0, 200, 0))
    
    waiting = True
    while waiting:
        #arka plan resmini çiz veya siyah arka plan kullan
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BLACK)
        
        #fare pozisyonunu al
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    waiting = False
        
        #butonun hover durumunu kontrol edeer
        start_button.check_hover(mouse_pos)
        
        #buton tıklamasını kontrol eder
        if start_button.is_clicked(mouse_pos, mouse_click):
            waiting = False
        
        #başlık vebutonu çizer
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(title_text, title_rect)
        start_button.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)

def show_level_text(screen, level):
    level_text = thixel_font.render(f'Level {level}', True, WHITE)
    
    screen.fill(BLACK)
    
    level_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    screen.blit(level_text, level_rect)
    pygame.display.update()
    
    #sonraki levele geçerken 1.5 saniye bir bekleme olur ve otomatik olarak devam eder
    pygame.time.wait(1500)

def game_over_menu(screen, reason, score, restart_game):
    #oyun bitince veya ölünde tekrar otna be oyundan çıkış butonlarını oluşturur.
    restart_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 40, "TEKRAR OYNA", GREEN, (0, 200, 0))
    quit_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 40, "ÇIKIŞ", RED, (200, 0, 0))
    
    reason_text = thixel_font.render(reason, True, WHITE)
    score_text = thixel_font_medium.render(f'Toplam Skor: {score}', True, YELLOW)
    
    waiting = True
    while waiting:
        screen.fill(BLACK)
        
        #fare pozisyonunu alıre
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart_game()  #oyunu yeniden başlatır
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        #butonların görünürlük durumunu kontrol eder
        restart_button.check_hover(mouse_pos)
        quit_button.check_hover(mouse_pos)
        
        #buton tıklamalarını kontrol eder
        if restart_button.is_clicked(mouse_pos, mouse_click):
            restart_game()  # Oyunu yeniden başlat
            return
        if quit_button.is_clicked(mouse_pos, mouse_click):
            pygame.quit()
            sys.exit()
        
     
        reason_rect = reason_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        screen.blit(reason_text, reason_rect)
        screen.blit(score_text, score_rect)
        
        #
        restart_button.draw(screen)
        quit_button.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)
