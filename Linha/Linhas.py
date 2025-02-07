import pygame
import sys


#------------------- Algoritmo Analítico -------------------#
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

#------------------- Algoritmo DDA -------------------#
def dda(x1, y1, x2, y2):
    pixels = []
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):  
        passo = abs(dx) # quantidade de passos
        inc_y = dy / abs(dx)
        inc_x = 1 if dx > 0 else -1 #direção

        x = x1
        y = y1

        for _ in range(passo + 1):
            pixels.append((x, round(y)))  
            x += inc_x
            y += inc_y
    else:  
        passo = abs(dy)
        inc_x = dx / abs(dy)
        inc_y = 1 if dy > 0 else -1

        x = x1
        y = y1

        for _ in range(passo + 1):
            pixels.append((round(x), y))  
            x += inc_x
            y += inc_y

    return pixels


    
#------------------- Algoritmo bresenham -------------------#

def bresenham(x1, y1, x2, y2):
    pixels = []

    # Se x2 < x1, trocar P1 com P2
    if x2 < x1:
        x1, y1, x2, y2 = x2, y2, x1, y1

    # Se y2 < y1, inverter y1 e y2 e pintar (x, -y)
    if y2 < y1:
        y1 = -y1
        y2 = -y2
        a = -1
    else: 
        a = 1

    # Se |y2 - y1| > |x2 - x1|, trocar x com y (espelhamento)
    if abs(y2 - y1) > abs(x2 - x1):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        troca_xy = True
    else:
        troca_xy = False

    # Cálculo do Δx e Δy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    p = 2 * dy - dx

    x, y = x1, y1
    for _ in range(dx + 1):
        if troca_xy:
            pixels.append((y, x))  # Inverte x e y se houve troca
        else:
            pixels.append((x, y))

        if p >= 0:
            y += sy
            p -= 2 * dx

        x += sx
        p += 2 * dy

    return pixels



def draw_line_pygame(screen, pixels, color=(255, 255, 255)):
    for px, py in pixels:
        pygame.draw.rect(screen, color, (px * 50, py * 50, 50, 50))  


def main():

    # Configurações iniciais do Pygame
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Algoritmo Bresenham")
    screen.fill((255, 255, 255))

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

        #draw_line_pygame(screen, pixels_analitico, color=(255, 0, 0))   # Vermelho - Analítico
        #draw_line_pygame(screen, pixels_dda, color=(0, 0, 255))        # Azul - DDA
        draw_line_pygame(screen, pixels_bresenham, color=(0, 255, 0))  # Verde - Bresenham

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()