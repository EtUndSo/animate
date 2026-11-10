---
title: Desde cero: Fuentes controladas y matrices
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Cuadripolos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Capítulo 6: Cuadripolos
order: 1160200
summary: Por qué cuatro números sustituyen a toda una red y cada forma de parámetros es solo otra elección
tags: fuente controlada, matriz, determinante, matriz inversa, matriz identidad
lang: es
---

Una fuente ideal del [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) suministra un valor fijo. Una __fuente controlada__ suministra un valor proporcional a otra tensión u otra corriente en otro lugar del circuito. Su símbolo es un rombo. Las abreviaturas proceden del inglés (voltage o current controlled voltage o current source).

| Nombre | Sigla | Ley | Factor |
|---|---|---|---|
| fuente de tensión controlada por tensión | VCVS | $U=\mu\,U_\mathrm{s}$ | sin unidad |
| fuente de tensión controlada por corriente | CCVS | $U=r\,I_\mathrm{s}$ | en $\Omega$ |
| fuente de corriente controlada por tensión | VCCS | $I=g\,U_\mathrm{s}$ | en S |
| fuente de corriente controlada por corriente | CCCS | $I=\beta\,I_\mathrm{s}$ | sin unidad |

El índice s indica la magnitud de control. El ejemplo más conocido es el transistor bipolar ([capítulo 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)): una pequeña corriente de base controla una gran corriente de colector. La energía para ello procede de la tensión de alimentación; la señal de control solo aporta la información. La magnitud de control y la fuente están en lugares distintos; por eso, toda fuente controlada es por naturaleza un cuadripolo.

Una __matriz__ es un esquema rectangular de números, aquí casi siempre con dos filas y dos columnas. Las letras en negrita representan matrices y columnas de dos magnitudes. Al multiplicar, cada fila de la matriz izquierda se combina con cada columna de la derecha, elemento por elemento, y luego se suma:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix},\qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}.$$

Con dos matrices, el orden importa. Las matrices se suman elemento por elemento. El número $\det\mathbf M=a\,d-b\,c$ se llama __determinante__. Si no es cero, existe la __matriz inversa__, que despeja $\mathbf x$ de $\mathbf y=\mathbf M\,\mathbf x$:

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

El producto $\mathbf M\,\mathbf M^{-1}$ es la __matriz identidad__ $\mathbf 1$, con unos en la diagonal y ceros en el resto. No cambia nada de aquello por lo que se multiplica.
