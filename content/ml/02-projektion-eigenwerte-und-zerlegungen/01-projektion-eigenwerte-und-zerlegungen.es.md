---
title: Visión general: Proyección, valores propios y descomposiciones
kurz: Visión general
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Capítulo 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220100
summary: Puntos más cercanos, direcciones naturales y los bloques de una matriz
tags: 
lang: es
---

## De qué trata

En el [capítulo 1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) quedó abierta una pregunta. Cuatro viviendas están descritas por su superficie y su número de habitaciones, y se conocen sus precios. Se buscan dos pesos con los que la suma ponderada acierte cada precio. Tales pesos no existen: cuatro ecuaciones con dos incógnitas se contradicen entre sí. Con datos medidos casi siempre ocurre lo mismo. Se tienen más mediciones que incógnitas, cada medición es un poco imprecisa, y el sistema de ecuaciones no tiene solución. Aun así se necesitan pesos, y precisamente los que se desvíen lo menos posible.

Este capítulo aborda esta pregunta y otras dos que resultan estar estrechamente emparentadas con ella. ¿Hay direcciones en las que una matriz solo alarga o acorta una flecha, sin girarla, y qué revelan esas direcciones sobre la matriz? ¿Y puede descomponerse toda matriz en unos pocos bloques sencillos, ordenados por su importancia, de modo que puedan omitirse los poco importantes? A ello se suma una pregunta práctica: ¿cuánto cambia el resultado de un cálculo si los datos son un poco erróneos?

La utilidad: con las respuestas se ajusta una recta u otra regla sencilla a unos valores medidos de modo que el error sea lo más pequeño posible. Se reconoce si una función de varias variables tiene una hondonada, una cresta o una silla. Se aproxima una imagen o una tabla grande con pocos números y se sabe cuánto se pierde al hacerlo. Y se puede juzgar si cabe fiarse de un resultado numérico. Las herramientas de este capítulo aparecen en casi todas las partes posteriores de la serie.

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué funciona un método y de dónde viene), deducciones y demostraciones; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta y ejecuta de verdad los programas; la solución se despliega justo debajo de cada ejercicio.
