import pygame
import numpy as np

def subdivision(P0, P1, P2, P3):
    """
    Calcula os pontos intermediários da curva de Bézier usando o método de De Casteljau.
    Retorna os novos pontos para subdivisão.
    """
    # Primeira subdivisão | Cria três novos pontos intermediarios 
    P0xD1 = (P0 + P1) / 2
    P1xD1 = (P1 + P2) / 2
    P2xD1 = (P2 + P3) / 2
    
    # Segunda subdivisão | Cria a partir dos pontos intermediarios novos pontos intermediarios 
    P0xD2 = (P0xD1 + P1xD1) / 2
    P1xD2 = (P1xD1 + P2xD1) / 2
    
    # Terceira subdivisão (ponto na curva) | Realiza a ultima subdivisão com os resultados da anteriores
    P0xD3 = (P0xD2 + P1xD2) / 2
    
    return P0xD1, P2xD1, P0xD2, P1xD2, P0xD3

def casteljau(P0, P1, P2, P3, t, curve_points):
    """
    Algoritmo de De Casteljau recursivo para calcular pontos da curva de Bézier.
    """
    if t > 0.005:
        e = t / 2
        P0xD1, P2xD1, P0xD2, P1xD2, P0xD3 = subdivision(P0, P1, P2, P3)
        casteljau(P0, P0xD1, P0xD2, P0xD3, e, curve_points)
        casteljau(P0xD3, P1xD2, P2xD1, P3, e, curve_points)
    else:
        curve_points.append(P0)

def draw_curve(screen, points, color):
    """
    Desenha a curva de Bézier interpolada.
    """
    if len(points) > 1:
        pygame.draw.lines(screen, color, False, points, 2)

def draw_points(screen, points, color, radius=6):
    """
    Desenha os pontos de controle P0, P1, P2 e P3.
    """
    for point in points:
        pygame.draw.circle(screen, color, (int(point[0]), int(point[1])), radius)

def main():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Casteljau")
    clock = pygame.time.Clock()
    
    P0 = np.array([100, 300])
    P1 = np.array([200, 100])
    P2 = np.array([400, 100])
    P3 = np.array([500, 300])
    
    bezier_curve = []
    casteljau(P0, P1, P2, P3, 1, bezier_curve)
    bezier_curve.append(P3)
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        
        # Desenha o polígono de controle
        pygame.draw.lines(screen, (200, 0, 0), False, [P0, P1, P2, P3], 2)
        
        # Desenha os pontos de controle
        draw_points(screen, [P0, P1, P2, P3], (255, 255, 0))
        
        # Desenha a curva de Bézier
        draw_curve(screen, bezier_curve, (0, 0, 255))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
