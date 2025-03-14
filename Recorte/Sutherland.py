import pygame
import time

def sutherland(app, poligono, recorte, velocidade=5):

    def dentro(ponto, aresta):
        
        (x1, y1), (x2, y2) = aresta
        return (x2 - x1) * (ponto[1] - y1) - (y2 - y1) * (ponto[0] - x1) >= 0

    def intersecao(ponto1, ponto2, aresta):
        (x1, y1), (x2, y2) = aresta
        dx, dy = ponto2[0] - ponto1[0], ponto2[1] - ponto1[1]
        dx_aresta, dy_aresta = x2 - x1, y2 - y1
        num = (x1 - ponto1[0]) * dy_aresta - (y1 - ponto1[1]) * dx_aresta
        den = dx * dy_aresta - dy * dx_aresta
        if den == 0:
            return ponto1  # Se as retas forem paralelas, retorna ponto1
        t = num / den
        return [int(ponto1[0] + t * dx), int(ponto1[1] + t * dy)]

    saida = poligono  # Inicializa o polígono para ser processado
    for i in range(len(recorte)):
        entrada = saida  # Define a entrada como o polígono atual
        saida = []  # A nova lista será construída com os pontos recortados
        aresta = (recorte[i], recorte[(i + 1) % len(recorte)])
        
        # Pausa para visualizar a animação do recorte
        time.sleep(1)
        app.limpar()
        desenhar_poligono(app, recorte, cor=(255, 0, 0))  # Janela de recorte em vermelho
        desenhar_poligono(app, saida, cor=(0, 0, 255))  # Polígono recortado em azul
        pygame.display.flip()
        
        for j in range(len(entrada)):

            ponto1, ponto2 = entrada[j], entrada[(j + 1) % len(entrada)]
            ponto1_dentro = dentro(ponto1, aresta)
            ponto2_dentro = dentro(ponto2, aresta)
            
            if ponto1_dentro and ponto2_dentro:
                saida.append(ponto2)  # CASO 1: Ambos os pontos dentro
            elif ponto1_dentro and not ponto2_dentro:
                saida.append(intersecao(ponto1, ponto2, aresta))  # CASO 2: Adiciona a interseção
            elif not ponto1_dentro and ponto2_dentro:
                saida.append(intersecao(ponto1, ponto2, aresta))  # CASO 4: Adiciona a interseção
                saida.append(ponto2)  # CASO 4: Adiciona ponto2 pois está dentro
            # CASO 3: Ambos fora, nenhum ponto é adicionado
        
        # Atualiza a tela com o novo polígono recortado
        app.limpar()
        desenhar_poligono(app, recorte, cor=(255, 0, 0))  # Janela de recorte
        desenhar_poligono(app, saida, cor=(0, 0, 255))  # Polígono recortado
        pygame.display.flip()
    
    return saida

def desenhar_poligono(app, pontos, cor):

    if len(pontos) > 1:
        for i in range(len(pontos)):
            ponto_inicial = pontos[i]
            ponto_final = pontos[(i + 1) % len(pontos)]  # Garante que o polígono feche
            pygame.draw.line(app.tela, cor, ponto_inicial, ponto_final, 2)

# Código de inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Algoritmo de Sutherland-Hodgman")
app = type('App', (object,), {'tela': tela, 'limpar': lambda: tela.fill((255, 255, 255))})


# Exemplo de polígono e janela de recorte
poligono = [(230, 150), (200, 170), (170, 150), (100, 150), (100, 200), (200, 270), (300, 200), (300, 150)] # Figura C

#poligono = [(160, 260), (140, 300), (300, 280), (310, 250), (210, 180), (100, 220)] # Figura A
recorte = [(150, 140), (280, 140), (280, 240), (150, 240)]


# Chama o algoritmo de recorte
poligono_recortado = sutherland(app, poligono, recorte, velocidade=5)

# Exibição final e loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
