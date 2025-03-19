Aluno: Rosialdo Vicente
N° de Matrícula: 2020018122

Objetivo do Programa
Desenvolver um programa em Python que realiza o recorte de polígonos utilizando o algoritmo de Sutherland-Hodgman. O programa exibe tanto a forma original quanto a versão recortada dos polígonos em uma janela gráfica, utilizando animação para evidenciar a transição entre as duas representações.

Tecnologias Utilizadas
Linguagem de Programação
Para a implementação deste trabalho, optei pela linguagem Python. A escolha se deu pela clareza do código e pela robustez na manipulação de estruturas matemáticas e gráficos, essenciais para o desenvolvimento do algoritmo de recorte e da animação.

Bibliotecas Utilizadas
As seguintes bibliotecas foram empregadas no projeto:

numpy: Utilizada para operações matemáticas, como cálculo da média para determinar o centroide dos polígonos e operações aritméticas essenciais ao algoritmo.
matplotlib: Responsável pela criação dos gráficos e animações, permitindo visualizar tanto os polígonos originais quanto os recortados.
matplotlib.animation: Módulo do matplotlib que facilita a criação de animações, mostrando o processo de recorte aplicado aos polígonos.
Implementação dos Algoritmos
Recorte de Polígonos (Sutherland-Hodgman)
O algoritmo de Sutherland-Hodgman é aplicado para recortar os polígonos em relação a uma janela de recorte definida pelos limites 
𝑥
min
,
𝑦
min
,
𝑥
max
,
𝑦
max
x 
min
​
 ,y 
min
​
 ,x 
max
​
 ,y 
max
​
 .

Componentes do Algoritmo:
Definição da Janela de Recorte e dos Polígonos:
São definidos os limites da janela e um dicionário contendo os polígonos de teste. Cada polígono é representado como uma lista de vértices, onde cada vértice é uma lista com as coordenadas 
[
𝑥
,
𝑦
]
[x,y].

Escala do Polígono:
Uma função é definida para escalar (ampliar ou reduzir) um polígono em torno de seu centroide. Essa função é aplicada, por exemplo, ao polígono 'b', aumentando-o em 50%.

Testar se um Ponto Está Dentro de uma Borda:
A função dentro verifica se um ponto está dentro de uma determinada borda da janela de recorte. Essa função é essencial para determinar os casos de transição do polígono (de fora para dentro, de dentro para fora ou ambos fora).

Cálculo da Interseção:
A função calcular_intersecao determina o ponto onde o segmento entre dois pontos do polígono intersecta a borda de recorte. Ela trata separadamente o caso de bordas verticais e horizontais.

Aplicação do Algoritmo Sutherland-Hodgman:
A função sutherland recorta o polígono iterativamente contra cada uma das quatro bordas da janela (esquerda, topo, direita, inferior).
Para cada borda, o algoritmo percorre os vértices do polígono e aplica as seguintes regras:

Transição de Fora para Dentro: Adiciona o ponto de interseção e, em seguida, o vértice atual.
Transição de Dentro para Fora: Adiciona apenas o ponto de interseção.
Dentro para Dentro: Mantém o vértice.
Fora para Fora: Não adiciona nenhum ponto.
Ao final do processo, obtém-se o polígono recortado, que é armazenado em um dicionário que mantém a mesma chave do polígono original.

Um trecho importante do código é:

python
Copiar
clipped_polygons = {k: sutherland(v, (x_min, x_max, y_min, y_max)) for k, v in polygons.items()}
Esse comando percorre todos os polígonos, aplica a função sutherland a cada um e armazena o resultado no dicionário clipped_polygons.

Animação dos Polígonos
Após o recorte, o programa utiliza o módulo de animação do matplotlib para exibir os polígonos originais e os recortados. Em cada frame da animação, a região de recorte é desenhada, e dependendo do frame, é exibido o polígono original ou o polígono recortado. Essa visualização dinâmica facilita a compreensão do efeito do algoritmo de recorte.

Desenvolvimento
Durante o desenvolvimento deste trabalho, enfrentei o desafio de implementar o algoritmo de Sutherland-Hodgman, principalmente na definição correta dos casos de transição entre os pontos (dentro e fora da região de recorte). A implementação exigiu um cuidado especial na verificação de pontos e no cálculo das interseções, garantindo que os polígonos fossem recortados de forma precisa.

A utilização da biblioteca matplotlib para a animação possibilitou uma visualização clara do processo, facilitando a depuração e validação dos resultados. A integração entre o recorte dos polígonos e a exibição gráfica mostrou-se uma abordagem eficiente para demonstrar os conceitos estudados.

Testes
Teste de Recorte
Os testes foram realizados utilizando quatro polígonos de formatos variados para verificar a robustez do algoritmo. Após o processamento, os polígonos recortados são impressos no console, onde cada vértice resultante é listado. Essa verificação permite confirmar a exatidão dos cálculos de interseção e a correta aplicação dos casos de recorte.

Teste de Animação
A animação é executada para cada polígono individualmente. Durante a animação, o polígono original é exibido em um primeiro frame, e o polígono recortado é apresentado no segundo frame. Essa alternância visual ajuda a evidenciar o efeito do recorte na forma dos polígonos.

Comparação de Métodos de Recorte
Critério	Algoritmo Sutherland-Hodgman	Outros Métodos (ex: Weiler-Atherton)
Método	Recorte iterativo contra cada borda da região de recorte	Baseado em métodos de subdivisão e tratamento de casos
Complexidade	Relativamente simples, fácil de implementar para polígonos convexos	Pode ser mais complexo para polígonos côncavos
Precisão	Fornece resultados precisos para a maioria dos polígonos de teste	Pode lidar melhor com interseções complexas em polígonos côncavos
Uso em Computação Gráfica	Bastante utilizado em renderização de gráficos em 2D	Requer técnicas adicionais para casos especiais
Interatividade	Pode ser integrado facilmente a animações e visualizações dinâmicas	Geralmente utilizado em processamento offline
