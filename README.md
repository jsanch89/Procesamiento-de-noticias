# News Analysis
Proyecto de Big Data para la materia Tópicos Especiales en Telemática de la Universidad Eafit.

## Integrantes
```
- Hamilton Tobón Mosquera - htobonm@eafit.edu.co
- Julian Andrés Sánchez Alzate - jsanch89@eafit.edu.co
- Anderson Daniel Grajales Alzate - agrajal7@eafit.edu.co
```

## Metodología CRISP-DM
Para resolver el problema en cuestión, se adoptó la metodología CRISP-DM que bien se resume en la siguiente figura:
![alt text](crisp-dm-4-problems-fig1.png)

## Etapa 1: Business Understanding

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


## Etapa 2: Data Understanding

En esta etapa se leyó el dataset en un data frame. Posteriormente se analizaron las columnas, es decir, sus tipos de datos y cuales eran las columnas útiles para nuestro caso (id, title, content). También se verificó la cantidad total de noticias y si habían campos nulos en el dataset.

## Etapa 3: Data Preparation

### Data Cleaning

Esta etapa consiste en la limpeza de cada noticia, es decir, en la eliminación de:
- Caracteres especiales
- Stop Words (is, of, on, the, ...)
- Palabras con longitud menor que 2.

En esta etapa de pre-procesamiento de datos se usaron las librerias y/o módulos:
- NLTK (https://www.nltk.org/)
- Sets (https://docs.python.org/2/library/sets.html)
- Stop Words (https://www.nltk.org/book/ch02.html)

## Etapa 4: Modeling

### Inverted Index
En esta etapa de modelamiento se usaron las siguientes librerias y/o módulos:
- PySpark (https://spark.apache.org/docs/0.9.0/python-programming-guide.html)
- RDDs (https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- DataFrames (https://spark.apache.org/docs/latest/sql-programming-guide.html)
- Sets (https://docs.python.org/2/library/sets.html)

### Similarity Analysis

## Etapa 5: Model Evaluation

### DataBricks
En el siguiente link se puede encontrar la solución al problema:
- Solucion: https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/8473593282024510/4263140825395790/6592235585723091/latest.html

### Visualization
En esta etapa de despliegue y finalización se usaron las siguientes librerias y/o módulos:
- Plotly (https://plot.ly/)
- Matplotlib (https://matplotlib.org/)
- WordCloud (https://github.com/amueller/word_cloud)

## Etapa 6: Cycle

Ir de nuevo a la etapa 1.

## Etapa 7: Deployment

