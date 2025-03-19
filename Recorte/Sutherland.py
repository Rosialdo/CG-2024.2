import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definição da janela de recorte: limites mínimo e máximo em x e y
x_min, y_min, x_max, y_max = 100, 100, 400, 400

# Dicionário contendo quatro polígonos de teste, cada um como lista de vértices [x, y]
polygons = {
    'a': [[200, 200], [200, 500], [500, 200]],
    'b': [[90, 210], [230, 210], [280, 330], [160, 410], [40, 330]],
    'c': [[150, 100], [150, 150], [200, 150], [200, 200], [300, 200], [300, 150],
          [350, 150], [350, 100], [350, 50], [300, 50], [300, 0], [200, 0],
          [200, 50], [150, 50]],
    'd': [[120, 320], [120, 480], [380, 480], [380, 340], [300, 340],
          [300, 410], [200, 410], [200, 320]]
}

# Função para escalar (ampliar/reduzir) um polígono em torno do seu centroide
def escalar_poligono(poly, fator):
    cx = np.mean([p[0] for p in poly])  # coordenada x do centroide
    cy = np.mean([p[1] for p in poly])  # coordenada y do centroide
    # Aplica fator de escala mantendo o centro
    return [[(x - cx) * fator + cx, (y - cy) * fator + cy] for x, y in poly]

# Aplica escala ao polígono 'b' conforme especificado
polygons['b'] = escalar_poligono(polygons['b'], 1.5)

# Testa se um ponto está dentro de uma borda do retângulo de recorte
def dentro(pt, edge):
    x, y = pt
    ex1, ey1, ex2, ey2 = edge
    if ex1 == ex2:  # borda vertical
        # Se é a borda esquerda, ponto deve ter x >= x_min; se direita, x <= x_max
        if ex1 == x_min:
            return x >= x_min
        else:
            return x <= x_max
    # borda horizontal: se inferior, y >= y_min; se superior, y <= y_max
    if ey1 == y_min:
        return y >= y_min
    else:
        return y <= y_max

# Calcula interseção entre segmento p1-p2 e a borda edge
def calcular_intersecao(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    ex1, ey1, ex2, ey2 = edge
    if ex1 == ex2:  # borda vertical
        x_int = ex1
        m = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
        return (x_int, y1 + m * (x_int - x1))
    # borda horizontal
    y_int = ey1
    m = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
    return (x1 + (y_int - y1) / m if m != 0 else x1, y_int)

# Implementação do Algoritmo de Sutherland-Hodgman para recorte de polígono
def sutherland(poly, clip_rect):
    xmin, xmax, ymin, ymax = clip_rect
    # Define as 4 bordas do retângulo: esquerda, topo, direita, inferior
    edges = [
        (xmin, ymin, xmin, ymax),
        (xmin, ymax, xmax, ymax),
        (xmax, ymax, xmax, ymin),
        (xmax, ymin, xmin, ymin)
    ]

    result = poly[:]  # cópia inicial do polígono

    # Processa recorte contra cada borda sequencialmente
    for edge in edges:
        novo = []
        prev = result[-1]
        for current_point in result:
            if dentro(current_point, edge):
                if not dentro(prev, edge):
                    # Caso de transição de fora para dentro: adiciona interseção
                    novo.append(calcular_intersecao(prev, current_point, edge))
                novo.append(current_point)
            elif dentro(prev, edge):
                # Caso de transição de dentro para fora: adiciona interseção
                novo.append(calcular_intersecao(prev, current_point, edge))
            prev = current_point
        result = novo
    return result

# Executa recorte para todos os polígonos definidos
clipped_polygons = {k: sutherland(v, (x_min, x_max, y_min, y_max)) for k, v in polygons.items()}

# Lista para armazenar os polígonos recortados e impressão dos mesmos
print("\nPolígonos Recortados:")
for chave, poligono in clipped_polygons.items():
    print(f"\n * Polígono '{chave}':")
    for i, ponto in enumerate(poligono):
        print(f"  P{i}: {ponto}")

# Função de animação que desenha o polígono original e o recortado
def animar_poligono(key):
    original = polygons[key]
    clipped = clipped_polygons[key]
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.set_xlim(-50, 550)
        ax.set_ylim(-50, 550)
        ax.set_aspect('equal')
        # Desenha a região de recorte
        rect = plt.Polygon([(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)], fill=False, linewidth=2)
        ax.add_patch(rect)
        # Exibe o polígono original ou o recortado conforme o frame
        poly = original if frame == 0 else clipped
        if poly:
            ax.fill(*zip(*(poly + [poly[0]])), edgecolor='black', facecolor='none', linewidth=2,
                    label='Original' if frame == 0 else 'Recortado')
        ax.legend()

    ani = animation.FuncAnimation(fig, update, frames=2, interval=3000, repeat=False)
    plt.show()

# Executa animação para cada polígono
for key in polygons:
    animar_poligono(key)
