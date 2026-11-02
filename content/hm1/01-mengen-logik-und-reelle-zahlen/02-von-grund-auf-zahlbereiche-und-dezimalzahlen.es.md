---
title: Desde cero: Sistemas numéricos y números decimales
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210200
summary: Qué hay que suponer sobre los números y por qué la raíz cuadrada de 2 no es una fracción
tags: números naturales, números enteros, números racionales, número real, irracionales
lang: es
---

El signo $:=$ significa «se define como». Los __números naturales__ son $\mathbb{N}:=\{1,2,3,\dots\}$, los __números enteros__ $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$, los __números racionales__ (fracciones) $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$. Los dos puntos significan «para los que se cumple».

:::definition Definición 0.1 (Número real, provisional)
<span class="anker" id="satz-0-1"></span>

Un __número real__ es un número con representación decimal, es decir, con un signo, un $m\in\mathbb{N}\cup\{0\}$ y cifras $a_1,a_2,\ldots\in\{0,1,\dots,9\}$, en cantidad finita o infinita:

<span class="anker" id="gl-0-1"></span>
$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr). \tag{0.1}$$

$\mathbb{R}$ es el conjunto de los números reales. Los números de $\mathbb{R}$ que no son una fracción se llaman __irracionales__.
:::

⁠**Cómo leerlo:** $3/8=0{,}375$ termina, $5/11=0{,}4545\ldots$ es periódico, y toda fracción tiene una de estas dos formas. $\sqrt2=1{,}41421356\ldots$ nunca llega a ser periódico. Se cumple $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. Esta definición es una solución provisional: no explica qué es una suma infinita (Parte 4) y no es única: $1{,}000\ldots$ y $0{,}999\ldots$ son el mismo número. La etapa [6](das-vollstandigkeitsaxiom.html#stufe-6) la sustituye por axiomas.
