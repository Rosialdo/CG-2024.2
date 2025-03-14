Aluno: Rosialdo Vicente

N° de Matricula: 2020018122

## Objetivo do Programa

### Desenvolver um programa para desenhar curvas aproximadas utilizando os algoritmos:

- **Bézier**
- **De Casteljau**

## Tecnologias Utilizadas

### Linguagem de Programação

Para a implementação deste trabalho, optei pela linguagem `Python` devido à sua flexibilidade e à minha familiaridade com seu uso no desenvolvimento de aplicações gráficas.

### Bibliotecas Utilizadas

As seguintes bibliotecas foram utilizadas no projeto:

- **`pygame`**: Escolhida por já ter sido utilizada em trabalhos anteriores, facilitando a implementação e visualização gráfica das curvas.
- **`math`**: Utilizada para cálculos matemáticos necessários no algoritmo de Bézier, incluindo o cálculo do fatorial para o Binômio de Newton.

## Implementação dos Algoritmos

Cada algoritmo foi implementado em arquivos separados para facilitar o entendimento e organização do código.

### Algoritmo Beziér:

No algoritmo de Bézier, o cálculo da curva é feito através do **Binômio de Newton** e dos **polinômios de Bernstein**, que determinam a influência de cada ponto de controle ao longo da curva. O coeficiente calculado é aplicado às coordenadas **X e Y**, sendo somado aos respectivos valores e retornado ao final do processamento.

Abaixo, um trecho do código:

![Bezier](../assets/Bezier.png)

### Algoritmo Casteljau:

O código implementa o algoritmo de De Casteljau para gerar uma curva de Bézier  por meio de subdivisão recursiva. A função subdivision calcula pontos intermediários entre os pontos de controle, refinando a curva progressivamente. A função casteljau aplica recursão para dividir a curva até atingir um critério de parada, armazenando os pontos na lista bezier_curve. 

Abaixo, um trecho do código:

![Casteljau](../assets/Casteljau.png)

## Desenvolvimento

A implementação dos dois algoritmos foi um desafio, principalmente devido à dificuldade em encontrar materiais de referência, especialmente para o algoritmo de De Casteljau. No entanto, através de discussões com colegas, consulta ao material da disciplina e pesquisas na internet, consegui desenvolver ambos os algoritmos corretamente.

Acredito que o programa atenda aos requisitos do trabalho. No entanto, um aspecto que poderia ser melhorado seria a **interatividade na definição dos pontos de controle**, pois, atualmente, os pontos precisam ser modificados manualmente no código.

## Testes

### Teste Beziér

O teste foi realizado utilizando os seguintes pontos:

```
points = [(100, 300), (150, 200), (450, 200), (500, 300)]
```

Resultado:

![teste_bezier](../assets/teste_bezier.png)

### Teste Casteljau

O teste foi realizado utilizando os seguintes pontos:

```
P0 = (100, 300)
P1 = (200, 100)
P2 = (400, 100)
P3 = (500, 300)
```

Resultado:

![teste_casteljau.png](../assets/teste_casteljau.png)

## Comparando os Algoritmos

| **Critério** | **Algoritmo de De Casteljau** | **Equação de Bézier (Polinômios de Bernstein)** |
| --- | --- | --- |
| **Método** | Baseado em subdivisão recursiva dos segmentos | Utiliza polinômios de Bernstein para calcular a curva diretamente |
| **Precisão Numérica** | Mais estável para valores altos de `n`, pois evita operações de potência sucessivas | Pode sofrer com erros numéricos devido à manipulação de fatoriais e potências elevadas |
| **Uso em Computação Gráfica** | Melhor para técnicas de subdivisão adaptativa, permitindo renderizações dinâmicas | Melhor para cálculos diretos, como animações baseadas em interpolação paramétrica |
| **Facilidade de Implementação** | Conceitualmente simples e intuitivo, baseado na interpolação sucessiva de pontos | Requer o cálculo explícito dos coeficientes binomiais, o que pode ser mais trabalhoso |
| **Flexibilidade** | Pode ser facilmente adaptado para algoritmos de refinamento progressivo | Melhor para cálculos precisos de posições intermediárias ao longo da curva |
| **Acurácia em Interpolação** | Garante que todos os pontos intermediários pertencem à curva original | Depende da precisão dos coeficientes binomiais e pode introduzir pequenos desvios |