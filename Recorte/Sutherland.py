import pygame
import time

def sutherland_hodgman_clip(app, poligono, janela_recorte, velocidade=10):
    """
    Recorta um polígono arbitrário contra uma janela de recorte convexa usando o algoritmo Sutherland-Hodgman,
    desenhando progressivamente à medida que o recorte ocorre.

    :param app: Instância do aplicativo onde os pixels serão desenhados.
    :param poligono: Lista de vértices do polígono original. Cada vértice é representado por [x, y].
    :param janela_recorte: Lista de vértices que definem a janela de recorte convexa.
    :param velocidade: Velocidade do desenho (0-100). Padrão 100 (mais rápido).
    :return: Lista de vértices do polígono recortado.
    """
    def dentro(ponto, aresta):
        """ Verifica se um ponto está dentro da borda de recorte. """
        (x1, y1), (x2, y2) = aresta
        return (x2 - x1) * (ponto[1] - y1) - (y2 - y1) * (ponto[0] - x1) >= 0

    def intersecao(ponto1, ponto2, aresta):
        """ Calcula a interseção entre a aresta do polígono e a borda de recorte. """
        (x1, y1), (x2, y2) = aresta
        dx, dy = ponto2[0] - ponto1[0], ponto2[1] - ponto1[1]
        dx_aresta, dy_aresta = x2 - x1, y2 - y1
        num = (x1 - ponto1[0]) * dy_aresta - (y1 - ponto1[1]) * dx_aresta
        den = dx * dy_aresta - dy * dx_aresta
        if den == 0:
            return ponto1  # Se paralelo, retorna o próprio ponto
        t = num / den
        return [int(ponto1[0] + t * dx), int(ponto1[1] + t * dy)]

    lista_saida = poligono
    for i in range(len(janela_recorte)):
        lista_entrada = lista_saida
        lista_saida = []
        aresta = (janela_recorte[i], janela_recorte[(i + 1) % len(janela_recorte)])
        
        # Adiciona um atraso de 1 segundo entre as iterações para diminuir a velocidade
        time.sleep(1)  # Atraso de 1 segundo entre as iterações
        
        # Limpa a tela e desenha o polígono original e o polígono recortado
        app.limpar()
        desenhar_poligono(app, janela_recorte, cor=(255, 0, 0))  # Janela de recorte em vermelho
        desenhar_poligono(app, lista_saida, cor=(0, 0, 255))  # Polígono recortado em azul
        pygame.display.flip()
        
        for j in range(len(lista_entrada)):
            ponto1, ponto2 = lista_entrada[j], lista_entrada[(j + 1) % len(lista_entrada)]
            ponto1_dentro = dentro(ponto1, aresta)
            ponto2_dentro = dentro(ponto2, aresta)

            if ponto1_dentro and ponto2_dentro:
                lista_saida.append(ponto2)  # CASO 1: Ambos os pontos estão dentro, adiciona ponto2
            elif ponto1_dentro and not ponto2_dentro:
                lista_saida.append(intersecao(ponto1, ponto2, aresta))  # CASO 2: Adiciona a interseção
            elif not ponto1_dentro and ponto2_dentro:
                lista_saida.append(intersecao(ponto1, ponto2, aresta))  # CASO 4: Adiciona a interseção
                lista_saida.append(ponto2)  # CASO 4: Adiciona ponto2 pois está dentro
            # CASO 3: Ambos os pontos estão fora, nenhum é adicionado
        
        # Limpa e redesenha para a próxima iteração
        app.limpar()
        desenhar_poligono(app, janela_recorte, cor=(255, 0, 0))  # Janela de recorte
        desenhar_poligono(app, lista_saida, cor=(0, 0, 255))  # Polígono recortado
        pygame.display.flip()
    
    return lista_saida

def desenhar_poligono(app, pontos, cor):
    """
    Função para desenhar um polígono no Pygame.

    :param app: Instância do aplicativo Pygame.
    :param pontos: Lista de vértices do polígono.
    :param cor: Cor para desenhar o polígono.
    """
    if len(pontos) > 1:
        for i in range(len(pontos)):
            ponto_inicial = pontos[i]
            ponto_final = pontos[(i + 1) % len(pontos)]
            pygame.draw.line(app.tela, cor, ponto_inicial, ponto_final, 2)

# Código de inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Algoritmo de Sutherland-Hodgman")
app = type('App', (object,), {'tela': tela, 'limpar': lambda: tela.fill((255, 255, 255))})

# Exemplo de polígono e janela de recorte
poligono = [(230, 150), (200, 170), (170, 150), (100, 150), (100, 200), (200, 270), (300, 200), (300, 150)]
janela_recorte = [(150, 140), (350, 140), (350, 240), (150, 240)]


# Chama o algoritmo de recorte
poligono_recortado = sutherland_hodgman_clip(app, poligono, janela_recorte, velocidade=5)

# Exibição final e loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
