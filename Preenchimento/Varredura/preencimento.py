import pygame
import sys
import time

sys.setrecursionlimit(5000)

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BG_COLOR = WHITE  # Cor de fundo da tela

WIDTH, HEIGHT = 500, 500
xc = WIDTH // 2  # Coordenada x do centro da tela 
yc = HEIGHT // 2  # Coordenada y do centro da tela

# ------------------- Algoritmo de Varredura com Análise Geométrica ------------------- #
def scanline_fill(screen, x_min, x_max, y_min, y_max, color):
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            screen.set_at((x, y), color)
            pygame.display.update()
            time.sleep(0.001)  # Pequeno delay para visualização

# ------------------- Desenho Simétrico ------------------- #
def simetria(screen, xc, yc, x, y, color):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        screen.set_at((px, py), color)

# ------------------- Algoritmo de Bresenham ------------------- #
def draw_circle(screen, xc, yc, raio, color):
    x = 0
    y = raio
    parametro = 1 - raio

    while x <= y:  
        simetria(screen, xc, yc, x, y, color)

        if parametro >= 0:
            y -= 1
            parametro += 2 * (x - y) + 5
        else:
            parametro += 2 * x + 3
        x += 1
    pygame.display.update()

# ------------------- Desenho do Retângulo ------------------- #
def draw_rectangle(screen, x, y, width, height, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height), 1)

# ------------------- Função Principal ------------------- #
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho e Preenchimento de Formas")
    screen.fill(BG_COLOR)

    # Desenha o retângulo
    rect_x, rect_y, rect_w, rect_h = xc - 50, yc - 30, 100, 60
    draw_rectangle(screen, rect_x, rect_y, rect_w, rect_h, BLACK)


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
                    scanline_fill(screen, rect_x + 1, rect_x + rect_w - 1, rect_y + 1, rect_y + rect_h - 1, RED)
                    filled = True  # Evita múltiplas chamadas do preenchimento
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
