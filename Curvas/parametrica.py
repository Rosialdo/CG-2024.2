import pygame  
from math import factorial  

def binomio_newton(n, k):
    """
    Calcula o coeficiente binomial de Newton C(n, k) = n! / (k! * (n - k)!)
    Esse coeficiente é utilizado na equação da curva de Bézier.
    """
    return factorial(n) // (factorial(k) * factorial(n - k))  # Retorna o valor do coeficiente binomial

def bezier(t, points):
    """
    Calcula um ponto (x, y) na curva de Bézier de grau n para um valor t no intervalo [0,1].
    Usa a equação paramétrica baseada nos polinômios de Bernstein.
    """
    n = 3  # Define o grau da curva 
    x, y = 0, 0  

    for i in range(n + 1):  
        coef = binomio_newton(n, i) * ((1 - t) ** (n - i)) * (t ** i)  
        # Calcula o coeficiente de Bernstein para o ponto i

        x += coef * points[i][0]  # Multiplica a coordenada x do ponto de controle pelo coeficiente e acumula
        y += coef * points[i][1]  # Multiplica a coordenada y do ponto de controle pelo coeficiente e acumula

    return int(x), int(y)  

def draw_curve(screen, points, color):
    """
    Desenha a curva de Bézier na tela usando a equação paramétrica.
    """
    curve_points = [bezier(t / 100, points) for t in range(101)]  
    # Gera 101 pontos da curva (t varia de 0 a 1 em passos de 0.01)

    pygame.draw.lines(screen, color, False, curve_points, 2)  
    # Desenha a curva conectando os pontos gerados com linhas verdes

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True
    points = [(100, 300), (150, 200), (450, 200), (500, 300)]  # 3 pontos de controle
    
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Desenha os pontos de controle
        for p in points:
            pygame.draw.circle(screen, (255, 0, 0), p, 5)
        
        # Desenha a curva usando a equação paramétrica
        draw_curve(screen, points, (0, 255, 0)) 
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
