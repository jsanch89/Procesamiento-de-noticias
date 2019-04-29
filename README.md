# News Analysis
Proyecto de Big Data para la materia Tópicos Especiales en Telemática de la Universidad Eafit.

## Integrantes
- Hamilton Tobón Mosquera - htobonm@eafit.edu.co
- Julian Andrés Sánchez Alzate - jsanch89@eafit.edu.co
- Anderson Daniel Grajales Alzate - agrajal7@eafit.edu.co

## Descripción del Problema
### Contexto
La minería o analítica de texto, son un conjunto de modelos, técnicas, algoritmos y
tecnologías que permiten procesar texto de naturaleza NO ESTRUCTURADA.
La minería de texto (text mining) permite transformar el texto en una forma
estructurada, de tal forma que facilite una serie de aplicaciones como Búsqueda en
texto, relevancia de documentos, entendimiento natural del lenguaje (NLP), traducción
automática entre idiomas, análisis de sentimientos, detección de tópicos entre muchas
otras aplicaciones.
Quizás el procesamiento más sencillo de todos, sea el wordcount, el cual consiste en
determinar la frecuencia de la palabra por documento o por todo el dataset.
### Problema
Se tiene un conjunto de noticias en texto libre, sobre el cual se desea realizar:
- PRIMERA PARTE: Preparación de Datos. Las noticias deben ser pre-procesadas para preparar los datos para la analítica, dentro de las sugerencias de preparación están:
  - Remover caracteres especiales (. , % ( ) ‘ “ ….
  - Remover stop-words
  - Remover palabras de longitud 1
- SEGUNDA PARTE: Un buscador sencillo basado en el índice invertido.
- TERCERA PARTE: Agrupamiento de noticias por similitud. Se recomienda usar la siguiente formula para determinar la similitud: <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\mathscr{F}(news_i,&space;news_j)&space;=&space;\sum\limits_{w^{*}&space;\in&space;{news_i}^{(1&space;\cdots&space;10)}&space;\cap&space;{news_j}^{(1&space;\cdots&space;10)}}&space;(\mathbb{F}_{wi}&space;&plus;&space;\mathbb{F}_{wj})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathscr{F}(news_i,&space;news_j)&space;=&space;\sum\limits_{w^{*}&space;\in&space;{news_i}^{(1&space;\cdots&space;10)}&space;\cap&space;{news_j}^{(1&space;\cdots&space;10)}}&space;(\mathbb{F}_{wi}&space;&plus;&space;\mathbb{F}_{wj})" title="\mathscr{F}(news_i, news_j) = \sum\limits_{w^{*} \in {news_i}^{(1 \cdots 10)} \cap {news_j}^{(1 \cdots 10)}} e\mathbb{F}_{wi} + \mathbb{F}_{wj})" /></a>
## Metodología CRISP-DM
Para resolver el problema en cuestión, se adoptó la metodología CRISP-DM que bien se resume en la siguiente figura:

