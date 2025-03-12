import pygame
from math import factorial

def binomial_coeff(n, k):
    """Calcula o coeficiente binomial C(n, k)."""
    return factorial(n) // (factorial(k) * factorial(n - k))

def bezier_equation(t, points):
    """Calcula um ponto da curva de Bézier quadrática (3 pontos de controle)."""
    n = 2  # Grau da curva (quadrática)
    x, y = 0, 0
    for i in range(n + 1):
        coef = binomial_coeff(n, i) * ((1 - t) ** (n - i)) * (t ** i)
        x += coef * points[i][0]
        y += coef * points[i][1]
    return int(x), int(y)

def draw_curve(screen, points, color):
    """Desenha a curva de Bézier usando a equação paramétrica."""
    curve_points = [bezier_equation(t / 100, points) for t in range(101)]
    pygame.draw.lines(screen, color, False, curve_points, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True
    points = [(100, 300), (150, 200), (500, 300)]  # 3 pontos de controle
    
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Desenha os pontos de controle
        for p in points:
            pygame.draw.circle(screen, (255, 0, 0), p, 5)
        
        # Desenha a curva usando a equação paramétrica
        draw_curve(screen, points, (0, 255, 0)) # Verde (Equação Paramétrica)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
