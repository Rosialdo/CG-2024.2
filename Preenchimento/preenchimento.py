import pygame
import sys

sys.setrecursionlimit(100000)
# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BG_COLOR = WHITE  # Cor de fundo da tela

WIDTH, HEIGHT = 500, 500

def draw_circle(surface, center, radius, color):
    pygame.draw.circle(surface, color, center, radius, 1)  # Desenha a borda da circunferência

def floodfill(screen, cor_nova, x, y):
    """Preenchimento totalmente recursivo (sem limite)."""
    
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return

    cor_atual = screen.get_at((x, y))[:3]
    
    if cor_atual == cor_nova or cor_atual != BG_COLOR:
        return

    # Pinta o pixel
    screen.set_at((x, y), cor_nova)
    pygame.display.update()

    floodfill(screen, cor_nova, x + 1, y)  # Direita
    floodfill(screen, cor_nova, x - 1, y)  # Esquerda
    floodfill(screen, cor_nova, x, y + 1)  # Baixo
    floodfill(screen, cor_nova, x, y - 1)  # Cima

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    center = (250, 250)
    radius = 100
    draw_circle(screen, center, radius, BLACK)
    
    # Criar botão
    button_rect = pygame.Rect(200, 400, 100, 40)
    font = pygame.font.Font(None, 30)
    text = font.render("Clique", True, WHITE)
    pygame.draw.rect(screen, BLACK, button_rect)
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))
    pygame.display.flip()

    running = True
    filled = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos) and not filled:
                    floodfill(screen, RED, center[0], center[1])
                    filled = True  # Evita múltiplas chamadas do preenchimento
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
