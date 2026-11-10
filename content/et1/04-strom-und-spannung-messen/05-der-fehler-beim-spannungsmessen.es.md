---
title: Etapa 4: El error al medir tensión
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Medir corriente y tensión
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Capítulo 4: Medir corriente y tensión
order: 1140500
summary: El voltímetro está fuera del circuito y, aun así, circula corriente por él.
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
El voltímetro está fuera del circuito y, aun así, circula corriente por él. Esta etapa muestra cuándo eso reduce la tensión que debe medir.
:::

**La idea.** El voltímetro abre un segundo camino para la corriente entre dos nudos. Su corriente tiene que venir de algún sitio. Si una fuente de corriente (mantiene fija su corriente, [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) alimenta la resistencia de carga $R_L$, la corriente fija se reparte: lo que circula por el voltímetro falta en $R_L$, y la tensión baja (fig. [5](#abb-5)). En cambio, si $R_L$ está conectada directamente a una fuente de tensión ideal, esta suministra la corriente adicional y nada cambia. Por tanto, los errores solo aparecen donde la corriente no puede afluir libremente. En el divisor de tensión, $R_1$ frena el suministro: la corriente total aumenta, en $R_1$ cae más tensión y el punto medio baja.

:::abbildung et1/k4spannung 5
El voltímetro (rango 10 V; en trazos, resistencia interna y aparato ideal) en dos circuitos equivalentes. En ambos desvía 13,6 µ A, y la lectura baja de 3 V a 2,727 V.
:::

:::satz Teorema 4.1 (Error del voltímetro)
<span class="anker" id="satz-4-1"></span>

En una fuente de corriente $I_\mathrm q$ con carga $R_L$, sin instrumento se cumple $U_L=I_\mathrm qR_L$, y con instrumento

<span class="anker" id="gl-4-1"></span>
$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}. \tag{4.1}$$

El error relativo es $f=-R_L/(R_L+R_\mathrm i)$; para $R_L\ll R_\mathrm i$, por tanto, $f\approx-R_L/R_\mathrm i$. En el divisor de tensión vale lo mismo con $R_L=R_1\parallel R_2$.
:::

⁠**Cómo leerlo:** La fracción es el factor de error. $R_L$ es la resistencia que el instrumento encuentra entre sus terminales. Para un error pequeño hace falta $R_\mathrm i\gg R_L$; lo ideal es $R_\mathrm i\to\infty$. **Validez:** fuentes ideales, resistencias independientes de la tensión.

:::herleitung Factor de error
Con la regla de los nudos $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$, la corriente se reparte entre dos resistencias en paralelo, y en ambas hay $U_L'$. Así pues, $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$, y simplificando $R_\mathrm i$ se obtiene [(4.1)](#gl-4-1). En el divisor, sin instrumento, $U_2=U\,R_2/(R_1+R_2)$. Con instrumento hay que sustituir $R_2$ por $R_2\parallel R_\mathrm i$ (divisor de tensión cargado, [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)):

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)} \quad\Rightarrow\quad \frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}.$$
:::

::::beispiel
En el divisor, $R_1\parallel R_2=20$ k$\Omega$ y $R_L/R_\mathrm i=0{,}1$. La lectura es $3\,\mathrm{V}/1{,}1=2{,}727$ V, es decir, $f=-9{,}1\,\%$. El mecanismo en números: la corriente por $R_1$ sube de 100 µ A a 104,5 µ A, de los cuales 90,9 µ A circulan por $R_2$ y 13,6 µ A por el voltímetro. Los mismos valores da $I_\mathrm q=150$ µ A con $R_L=20$ k$\Omega$. Un multímetro digital de 10 M$\Omega$ muestra 2,994 V, es decir, $f=-0{,}2\,\%$.
::::

⁠**Casos límite:** $R_\mathrm i\to\infty$ da $f\to0$. $R_L\to0$ (fuente directamente en el instrumento) también da $f\to0$. Con $R_\mathrm i=R_L$, la tensión se reduce a la mitad.

:::frage 200 k$\Omega$ parece mucho. ¿Por qué el instrumento perturba aun así el divisor?
Grande o pequeño solo existe en comparación con $R_L$. Por el divisor circulan solo 100 µ A. Al lado de eso, 13,6 µ A no son una parte pequeña.
:::

:::aufgabe Ejercicio 4 ★★ Divisor de alta resistencia
<span class="anker" id="aufg-4"></span>

$R_1=6$ M$\Omega$ y $R_2=3$ M$\Omega$ están conectadas a 9 V. (a) ¿Qué muestran en $R_2$ el voltímetro de 200 k$\Omega$ y el multímetro digital de 10 M$\Omega$? (b) ¿Cómo recuperas el valor verdadero a partir de la lectura 2,5 V? (c) ¿Qué $R_\mathrm i$ haría falta para un error del 1 %?

:::loesung
(a) $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$, el valor verdadero es 3 V. Con 200 k$\Omega$: $3\,\mathrm{V}/(1+10)=0{,}273$ V, $f=-91\,\%$. Con 10 M$\Omega$: $3\,\mathrm{V}/(1+0{,}2)=2{,}5$ V, $f=-16{,}7\,\%$.

(b) Despejando en [(4.1)](#gl-4-1): $U=U'(1+R_L/R_\mathrm i)=2{,}5\,\mathrm{V}\cdot1{,}2=3$ V. (c) $R_L/(R_L+R_\mathrm i)\le0{,}01$ da $R_\mathrm i\ge99\,R_L=198$ M$\Omega$.
:::
:::
