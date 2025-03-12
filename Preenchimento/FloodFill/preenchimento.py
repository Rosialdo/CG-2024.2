import pygame
import sys

sys.setrecursionlimit(5000)

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BG_COLOR = WHITE  # Cor de fundo da tela

WIDTH, HEIGHT = 500, 500
xc = WIDTH // 2  # Coordenada x do centro da tela 
yc = HEIGHT // 2  # Coordenada y do centro da tela

# ------------------- Desenho Simétrico ------------------- #
def simetria(screen, xc, yc, x, y, color):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        screen.set_at((px, py), color)  # Desenha pixel diretamente

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

# ------------------- Desenho do Retângulo ------------------- #
def draw_rectangle(screen, x, y, width, height, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height), 1)



# ------------------- Flood Fill (Preenchimento) ------------------- #
def floodfill(screen, cor_nova, x, y):
   
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return

    cor_atual = screen.get_at((x, y))[:3]

    # Verifica se a cor já é a nova ou se não é a cor de fundo
    if cor_atual == cor_nova or cor_atual != BG_COLOR:
        return

    # Pinta o pixel
    screen.set_at((x, y), cor_nova)
    pygame.display.update()

    # Chama recursivamente para os pixels vizinhos
    floodfill(screen, cor_nova, x + 1, y)  # Direita
    floodfill(screen, cor_nova, x - 1, y)  # Esquerda
    floodfill(screen, cor_nova, x, y + 1)  # Baixo
    floodfill(screen, cor_nova, x, y - 1)  # Cima

# ------------------- Função Principal ------------------- #
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho e Preenchimento de Círculo")
    screen.fill(BG_COLOR)

    # Desenha o círculo no centro da tela

    #draw_circle(screen, xc, yc, 50, BLACK)
    draw_rectangle(screen, xc - 50, yc - 30, 100, 60, BLACK)
    
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
                    floodfill(screen, RED, xc, yc)  # Preenche o círculo a partir do centro
                    filled = True  # Evita múltiplas chamadas do preenchimento
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
