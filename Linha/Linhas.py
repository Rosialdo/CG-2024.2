import pygame
import sys

def analitico(x1, y1, x2, y2):
    pixels = []
    if x1 == x2:
        for y in range(y1, y2 + 1):
            pixels.append((x1, y))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y2 - m * x2
        for x in range(x1, x2 + 1):
            y = m * x + b
            pixels.append((x, y))
    return pixels

def dda(x1, y1, x2, y2):
    pixels = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx > dy:
        incremento = (y2 - y1) / dx
        y = y1
        for x in range(x1, x2 + 1):
            pixels.append(x, y)
            y += incremento
    else:
        incremento = (x2 - x1) / dy
        x = x1
        for y in range(y1, y2 + 1):
            pixels.append(x, y)
            x += incremento

    return pixels

def bresenham(x1, y1, x2, y2):
    pixels = []
    dy = y2 - y1
    dx = x2 - x1
    y = y1

    p = 2 * dy - dx

    for x in range(x1, x2 + 1):
        pixels.append((x, y))  
        if p >= 0:
            y += 1
            p += 2 * (dy - dx)
        else:
            p += 2 * dy

    return pixels


def draw_line_pygame(screen, pixels, color=(255, 255, 255)):
    for px, py in pixels:
        pygame.draw.rect(screen, color, (px * 10, py * 10, 10, 10))  


def main():

    # Configurações iniciais do Pygame
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Algoritmos de Rasterização")
    screen.fill((0, 0, 0))

    x1 = int(input("Digite o valor de x1: "))
    y1 = int(input("Digite o valor de y1: "))
    x2 = int(input("Digite o valor de x2: "))
    y2 = int(input("Digite o valor de y2: "))

    # Definição dos pixels
    pixels_analitico = analitico(x1, y1, x2, y2)
    pixels_dda = dda(x1, y1, x2, y2)
    pixels_bresenham = bresenham(x1, y1, x2, y2)


    # Inicio da demonstração
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenha as linhas no grid

        draw_line_pygame(screen, pixels_analitico, color=(255, 0, 0))   # Vermelho - Analítico
        # draw_line_pygame(screen, pixels_bresenham, color=(0, 255, 0))  # Verde - Bresenham
        # draw_line_pygame(screen, pixels_dda, color=(0, 0, 255))        # Azul - DDA

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()