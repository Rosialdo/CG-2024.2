# Trabalho de Rasterização de Circunferências

## Objetivo do Programa

### Desenvolver um programa que permita desenhar circunferências utilizando os algoritmos:

- Paramétrico
- Incremental
- Bresenham

## Tecnologias Utilizadas

### Linguagem de Programação

Escolhi a linguagem Python para este projeto devido à minha familiaridade com ela e à sua flexibilidade, o que facilita a implementação e teste dos algoritmos.

### Bibliotecas Utilizadas

As seguintes bibliotecas foram utilizadas no desenvolvimento do programa:

- **`sys`**: Utilizada para encerrar o programa de forma adequada.
- **`pygame`**: Escolhida para demonstrar graficamente os algoritmos de rasterização. Considerei inicialmente o uso da biblioteca matplotlib, mas optei pelo pygame por facilitar futuras implementações e pela sua abordagem mais intuitiva para manipulação de gráficos em tempo real.
- **`math`**: Utilizada para cálculos matemáticos necessários nos algoritmos, como funções trigonométricas, otimizando os cálculos relacionados à construção de circunferências.

## Implementação dos Algoritmos

Os três algoritmos foram implementados em um único arquivo chamado `circunferencia.py`, facilitando a organização e apresentação do projeto.

### Algoritmo Paramétrico

A função `circulo_parametrico(screen, xc, yc, raio, color)` utiliza a equação paramétrica de uma circunferência para determinar os pontos. Suas entradas principais são:

- `xc` e `yc`: Coordenadas do centro da circunferência.
- `raio`: O raio da circunferência.

O algoritmo calcula os pontos da circunferência variando o ângulo de 0 a 360 graus. A cada iteração, utiliza funções trigonométricas para determinar as coordenadas \( x \) e \( y \). Essa abordagem, embora precisa, pode ser relativamente lenta devido ao uso intensivo de operações de ponto flutuante.

![Algoritmo Paramétrico](../assets/parametrico.png)

---

### Algoritmo Incremental

A função `circulo_incremental(screen, xc, yc, raio, color)` também recebe como entradas `xc`, `yc` e `raio`. Este método utiliza uma abordagem incremental para calcular os pontos da circunferência com base em pequenas variações angulares. O uso de seno e cosseno para calcular as novas coordenadas dos pontos, a cada incremento, facilita a construção da circunferência.

A função `simetria(screen, xc, yc, x, y, color)` é essencial para otimizar o algoritmo incremental, desenhando simultaneamente os pontos simétricos da circunferência em todas as oito regiões principais.

> *Nota*: A imagem do algoritmo incremental ainda precisa ser referenciada corretamente no local adequado.

---

### Algoritmo de Bresenham

A função `circulo_bresenham(screen, xc, yc, raio, color)` implementa o algoritmo de Bresenham para rasterização de circunferências. Este método utiliza aritmética de inteiros para calcular os pontos, eliminando a necessidade de operações de ponto flutuante, o que o torna mais rápido e eficiente.

Entradas principais:

- `xc` e `yc`: Coordenadas do centro da circunferência.
- `raio`: O raio da circunferência.

O algoritmo começa no ponto superior da circunferência e avança calculando os pixels de forma incremental, utilizando a função `simetria` para desenhar os pontos equivalentes em todas as regiões.

![Algoritmo de Bresenham](../assets/c_bresenham.png)

---

## Desenvolvimento

Durante a implementação, enfrentei desafios ao lidar com a visualização gráfica dos algoritmos. Inicialmente, tentei desenvolver os algoritmos de linha e circunferência juntos, mas essa abordagem se mostrou confusa. Resolvi priorizar a implementação das linhas, o que facilitou o desenvolvimento posterior das circunferências.

A função `simetria` foi particularmente desafiadora, pois organiza os pontos simétricos da circunferência em todas as regiões principais, garantindo que a forma seja desenhada corretamente. A implementação do algoritmo incremental foi a mais demorada, devido à necessidade de estudar referências adicionais para compreendê-lo completamente.

No geral, acredito que consegui implementar os tópicos solicitados de forma satisfatória, e o programa final atende aos requisitos propostos na atividade.
