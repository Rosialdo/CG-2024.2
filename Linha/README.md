# Trabalho de rasterização de linhas

## Objetivo do programa

### Desenvolver um programa que permita desenhar retas por meio dos algoritmos:

- Analítico;
- DDA;
- Bresenham.

## Tecnologias utilizadas

### Linguagem de programação: 

Escolhi como linguagem para realizar esse trabalho o ```python``` a escolha foi devido a maior familiaridade com a linguem visando uma melhor implementação do código.

### Blibiotecas utilizadas:

Para esse codigo utilizei duas blibiotecas: 

- ```sys```: Dentro do codigo foi utilizada para encerrar o programa corretamente;

- ```pygame```: Essa foi usada pra conseguir demonstrar graficamente a implementação. Estava na duvida dentre ela e a mathplot, mas ela foi a escolhida visando facilitar futuras implementações no decorrer da disciplina.

## Implementação

Para essa implementação eu coloquei todos os três algoritimos em um único arquivo chamado linhas para facilitar vamos falar sobre cada um deles agora.

### Analítico: 

É uma função no codigo chamada ```analitico```, essa função tem 4 entradas ```x1```, ```y1```, ```x2``` e ```y2```. Para a realização do algoritimo eu fiz com referencia ao Slide disponibilizado pelo Professor durante as aulas da disciplina: 

![Algoritimo Analítico](../assets/analitico.png)
