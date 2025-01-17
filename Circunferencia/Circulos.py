import pygame
import sys
import math

# Configurações da tela
WIDTH, HEIGHT = 600, 600
BG_COLOR = (255, 255, 255)  
COLORS = {
    "parametrica": (255, 0, 0),     # Vermelho
    "incremental": (0, 255, 0),     # Verde
    "bresenham": (0, 0, 255),       # Azul
}
xc = WIDTH // 2  # Coordenada x do centro da tela 
yc = HEIGHT // 2  # Coordenada y do centro da tela

#------------------- Desenho Paramétrico -------------------
def circulo_parametrico(screen, xc, yc, raio, color):
    x = xc + raio
    y = yc
    for t in range(360): 
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 1, 1))
        x = xc + raio * math.cos ((math.pi * t)/180)
        y = yc + raio * math.sin ((math.pi * t)/180)
        

#------------------- Desenho Simétrico ------------------- #
def simetria (screen, xc, yc, x, y, color):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        pygame.draw.rect(screen, color, pygame.Rect(px, py, 1, 1))

#------------------- Desenho Incremental -------------------#
def circulo_incremental(screen, xc, yc, raio, color):
    x = 0
    y = raio
    theta = 1 / raio
    sin_theta = math.sin(theta)
    cos_theta = math.cos(theta)

    while x <= y:
        simetria (screen, xc, yc, x, y, color)
        xn = x
        yn = y
        x = xn * cos_theta - yn * sin_theta
        y = y * cos_theta + xn * sin_theta

#------------------- Algoritmo de Bresenham -------------------#
def circulo_bresenham(screen, xc, yc, raio, color):
    x = 0
    y = raio
    parametro = 1 - raio

    while x <= y:  
        simetria (screen, xc, yc, x, y, color)

        if parametro >= 0:
            y -= 1
            parametro += 2 * (x - y) + 5
        else:
            parametro += 2 * x + 3
        x += 1

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Comparação de Algoritmos de Círculo")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # Desenho dos círculos usando diferentes algoritmos

        circulo_parametrico(screen, xc, yc, 100, COLORS["parametrica"])
        circulo_incremental(screen, xc, yc, 150, COLORS["incremental"])
        circulo_bresenham(screen, xc, yc, 200, COLORS["bresenham"])

        # Atualiza a tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
