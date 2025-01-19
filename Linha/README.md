# Trabalho de Rasterização de Linhas

## Objetivo do Programa

### Desenvolver um programa que permita desenhar retas utilizando os algoritmos:

- Analítico
- DDA (Digital Differential Analyzer)
- Bresenham

## Tecnologias Utilizadas

### Linguagem de Programação

Para a implementação deste trabalho, optei pela linguagem Python devido à minha familiaridade e à sua flexibilidade para desenvolvimento de aplicações gráficas.

### Bibliotecas Utilizadas

As seguintes bibliotecas foram utilizadas no projeto:

- `sys`: Utilizada para encerrar o programa corretamente.
- `pygame`: Escolhida para visualização gráfica das retas devido à sua facilidade de uso e capacidade de manipulação de gráficos em tempo real.

## Implementação dos Algoritmos

Os algoritmos foram implementados em um único arquivo chamado `linhas.py` para facilitar o gerenciamento e compreensão do código.

### Algoritmo Analítico

O algoritmo analítico é implementado pela função `analitico(x1, y1, x2, y2)`. Este método calcula os pixels ao longo de uma linha utilizando a equação da reta, como mostrado no slide da disciplina. No entanto, ele apresenta limitações quando `x2` é maior que `y2`, causando problemas na renderização dos pixels.

#### Referência para o Algoritimo Analítico: 

![Algoritimo Analítico](../assets/analitico.png)

### Algoritmo DDA 

O algoritmo DDA é implementado pela função `dda(x1, y1, x2, y2)`. Ele melhora a descontinuidade do método analítico ao utilizar aritmética de ponto flutuante para calcular os pixels da linha. Apesar de sua simplicidade, pode sofrer com erros de arredondamento em escalas maiores e ser relativamente lento para algumas aplicações.

#### Referência para o Algoritimo DDA: 

![Algoritimo DDA](../assets/DDA.png)

### Algoritmo de Bresenham

O algoritmo de Bresenham é implementado pela função `bresenham(x1, y1, x2, y2)`. Considerado o mais eficiente dos três métodos para rasterização de linhas, o algoritmo de Bresenham utiliza incrementos inteiros para calcular os pixels da linha, evitando operações de arredondamento. Isso resulta em um método rápido e preciso para desenhar linhas.

#### Referência para o Algoritmo de Bresenham: 

![Algoritimo Bresenham](../assets/BRESENHAM.png)

## Desenvolvimento

Durante a implementação, encontrei dificuldades significativas ao desenvolver os algoritmos DDA e Bresenham. Após estudar os pseudocódigos fornecidos em aula, consegui superar esses obstáculos. Também enfrentei desafios na visualização das linhas, inicialmente tentando usar a biblioteca matplotlib. Optei então pelo pygame, após considerar sua adequação para demonstrações gráficas em tempo real, conforme discutido com colegas.

A implementação da visualização das linhas não correspondeu completamente às minhas expectativas iniciais, mas acredito que tenha sido eficaz para exemplificar os cálculos dos algoritmos.

