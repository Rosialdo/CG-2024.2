import pygame  # Importa a biblioteca Pygame para renderizar a curva na tela

def casteljau(t, pontos_controle):
    """
    Calcula um ponto na curva de Bézier usando o algoritmo de De Casteljau.
    O método realiza interpolação sucessiva entre os pontos de controle.
    """

    pontos = pontos_controle[:]  # Copia a lista de pontos de controle para não modificar a original
    n = 3  # Define o grau da curva (cúbica, pois há 4 pontos de controle)

    # Algoritmo de De Casteljau: interpolação sucessiva
    for r in range(1, n + 1):  # Percorre os níveis da interpolação
        for i in range(n - r + 1):  # Itera sobre os pontos intermediários restantes
            x = (1 - t) * pontos[i][0] + t * pontos[i + 1][0]  # Interpolação linear no eixo X
            y = (1 - t) * pontos[i][1] + t * pontos[i + 1][1]  # Interpolação linear no eixo Y
            pontos[i] = [x, y]  # Atualiza o ponto na lista com o novo ponto interpolado

    return [int(pontos[0][0]), int(pontos[0][1])]  # Retorna o ponto final da interpolação, convertido para inteiros

def draw_curve(screen, points, color):
    """
    Desenha a curva de Bézier utilizando o algoritmo de De Casteljau.
    
    Parâmetros:
        screen (pygame.Surface): Tela onde a curva será desenhada.
        points (list): Lista de pontos de controle [(x1, y1), (x2, y2), ...].
        color (tuple): Cor da curva no formato (R, G, B).
    """

    curve_points = [casteljau(t / 100, points) for t in range(101)]  
    # Calcula 101 pontos da curva variando t de 0 a 1 em passos de 0.01

    pygame.draw.lines(screen, color, False, curve_points, 2)  
    # Desenha a curva ligando os pontos gerados

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True
    points = [(100, 300), (150, 200), (400, 200), (500, 300)]  # 3 pontos de controle
    
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Desenha os pontos de controle
        for p in points:
            pygame.draw.circle(screen, (0, 0, 255), p, 5)
        
        # Desenha a curva usando o algoritmo de De Casteljau
        draw_curve(screen, points, (0, 255, 0)) # Verde (Casteljau)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()