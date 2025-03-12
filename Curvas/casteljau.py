import pygame

def casteljau(t, pontos_controle):
    """
    Calcula um ponto na curva de Bézier utilizando o algoritmo de De Casteljau.
    """
    pontos = pontos_controle[:]
    n = 1  # Grau da curva (quadrática, 3 pontos de controle)
    
    for r in range(1, n + 1):  # Percorre os níveis da interpolação
        for i in range(n - r + 1):  # Calcula os novos pontos intermediários
            x = (1 - t) * pontos[i][0] + t * pontos[i + 1][0]
            y = (1 - t) * pontos[i][1] + t * pontos[i + 1][1]
            pontos[i] = [x, y]
    
    return [int(pontos[0][0]), int(pontos[0][1])]

def draw_curve(screen, points, color):
    """Desenha a curva de Bézier usando o algoritmo de De Casteljau."""
    curve_points = [casteljau(t / 100, points) for t in range(101)]
    pygame.draw.lines(screen, color, False, curve_points, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True
    points = [(100, 300), (500, 300)]  # 3 pontos de controle
    
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Desenha os pontos de controle
        for p in points:
            pygame.draw.circle(screen, (255, 0, 0), p, 5)
        
        # Desenha a curva usando o algoritmo de De Casteljau
        draw_curve(screen, points, (0, 255, 0)) # Verde (Casteljau)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()