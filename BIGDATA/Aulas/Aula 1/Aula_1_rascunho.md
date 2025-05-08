# Big Data

## 1. O que é Big Data
Como o nome ja diz, Big Data é um grande volume de dados de difícil manipulação e processamento. Anos atrás enfrentamos dificuldade em analisar uma grande quantidade de dados com rápido processamento, tanto pela quantidade absurda de dados quanto pela sua variedade e falta de padronização.


## 2. Possíveis soluções
Mas se temos muitos dados que precisam ser processados de maneira precisa e rápida, não podemos simplesmente desenvolver computadores mais potentes? Teóricamente sim, porém na prática não é tao simples assim. 

### 2.1
Em 1965 é formulado a Lei de Moore, que afirma que o número de transistores em um chip dobra aproximadamente a cada dois anos, mantendo o mesmo custo e espaço. Portanto, a potência de processamento poderia se beneficiar desse aumento de transitores e evoluir também. A lei de Moore ainda é relevante para algumas situações, porém a partir de 2000 o aumento na frequência de clocks da CPU deixou de acompanhar esse aumento. Isso porque existem limites fisícos para o desenvolvimento dos processadores que não podem ser desprezados, com o aumento da frequência de clocks a energia a ser dissipada também cresce, portanto estamos há 15 anos em aproximadamente processadores com 5Ghz. Esse problema da barreira fisíca para o avanço da velocidade do clock é conhecido como "PowerWall".
<moore_law.png>

### 2.2 
Com isso precisamos desenvolver métodos para lidar com todos esses dados sendo processados, que estão aproximadamente dobrando a cada dois anos que se passam. Pensando em um caso real, a Google, quando pesquisamos por algo na barra de pesquisa o sistema procura em toda a internet e retorna isso para o usuário. O usuário não pode esperar, então esse processo deve ser rápido, e todo site disponível é diferente um do outro, portanto é necessário lidar com um enorme volume de dados, com dados variados e retornar isso rápido.


## 3. Desafio
Para entendermos melhor como funciona vamos realizar um desafio. Faça uma busca por uma palavra específica dentro de páginas da Wikipédia e retorne as páginas onde a palavra mais aparece. Para isso devemos utilizar da Distância de Levenshtein

### 3.1 Distância de Levenshtein
A Distância de Levenshtein serve para conseguir saber a quantidade de operações, inserção, deleção ou substituição, uma palavra deve sofrer para se transformar em outra, por exemplo: banana para batata precisa sofrer duas alterações.

#### 3.1.1 Como funciona
