---
title: Etapa 1: Agrupar resistencias
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Fuentes y fuentes equivalentes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Capítulo 5: Fuentes y fuentes equivalentes
order: 1150300
summary: Una red de resistencias sin fuente tiene en dos terminales una curva característica que pasa por el origen, así que basta un número.
tags: circuito serie-paralelo, resistencia total, conductancia
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Una red de resistencias sin fuente tiene en dos terminales una curva característica que pasa por el origen, así que basta un número. Esta etapa lo halla agrupando paso a paso.
:::

**La idea.** Un __circuito serie-paralelo__ se compone de grupos en serie y en paralelo encajados unos en otros. Dos resistencias están en serie si en su nudo común no hay nada más conectado. Entonces circula la misma corriente por ambas, porque la carga no puede desviarse a ningún sitio. Están en paralelo si están conectadas a los mismos dos nudos. Entonces hay la misma tensión en ambas. Cada uno de estos grupos es a su vez un pequeño monopuerto cuya curva característica es una resistencia. Se sustituye por esa resistencia, y el resto del circuito no nota nada. Esto se repite de dentro hacia fuera.

:::abbildung et1/k5gruppe 1
A la izquierda, una red de carga de seis resistencias. Las tres apiladas están en paralelo y dan 10 $\Omega$, y junto con $R_\mathrm{c}$ en serie, 15 $\Omega$. A la derecha, la red tras estos dos pasos.
:::

:::definition Definición 1.1 (Resistencia total)
<span class="anker" id="satz-1-1"></span>

La __resistencia total__ $R_\mathrm{AB}$ es el cociente $U_\mathrm{AB}/I_\mathrm{A}$ de un monopuerto sin fuente. Para la red de la fig. [1](#abb-1) se cumple

<span class="anker" id="gl-1-1"></span>
$$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr) =R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}. \tag{1.1}$$
:::

⁠**Cómo leerlo:** $R$ es una resistencia en $\Omega$, $G=1/R$ su __conductancia__ en siemens (S). En serie se suman resistencias; en paralelo se suman conductancias. Por eso, en la segunda forma cada grupo en paralelo aparece como una suma de conductancias. El corchete con el exponente $-1$ invierte de nuevo el resultado. **Validez:** El procedimiento necesita grupos auténticos. Si en un nudo intermedio hay conectada una tercera rama, las dos vecinas ya no están en serie (etapas [2](symmetrie-nutzen.html#stufe-2) y [3](stern-und-dreieck.html#stufe-3)).

::::beispiel
Con los valores de la fig. [1](#abb-1): $G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}=50+33{,}3+16{,}7$ mS $=100$ mS, es decir, 10 $\Omega$. Con $R_\mathrm{c}$ en serie: 15 $\Omega$. En paralelo con $R_\mathrm{b}$: $30\,\Omega\parallel15\,\Omega=10\,\Omega$. Con $R_\mathrm{a}$ en serie: $R_\mathrm{AB}=16\,\Omega$. El cálculo inverso da las corrientes: con 8 V entre A y B circulan 0,5 A. En $R_\mathrm{a}$ caen 3 V y quedan 5 V para el resto. Por $R_\mathrm{b}$ circulan $5\,\mathrm{V}/30\,\Omega=166{,}7$ mA, por $R_\mathrm{c}$ circulan $5\,\mathrm{V}/15\,\Omega=333{,}3$ mA. La suma es 500 mA.
::::

⁠**Caso límite:** Para $R_\mathrm{b}\to0$, [(1.1)](#gl-1-1) se convierte en $R_\mathrm{AB}=R_\mathrm{a}=6\,\Omega$. El cortocircuito puentea todo lo que hay detrás; la carga toma el cable.

:::frage ¿Puedo hacer los pasos en cualquier orden?
No. Un grupo suele surgir solo cuando el grupo interior ya está agrupado: en el esquema inicial, $R_\mathrm{c}$ y $R_\mathrm{b}$ no están en paralelo, porque entre ellas están las tres resistencias apiladas. Por eso se trabaja desde el grupo más alejado de los terminales hacia los terminales.
:::

:::aufgabe Ejercicio 1 ★ Modificar la red de carga
<span class="anker" id="aufg-1"></span>

Parte de la red de la fig. [1](#abb-1). ¿Qué $R_\mathrm{AB}$ resulta si (a) $R_\mathrm{b}$ desaparece por una rotura del cable, (b) se cortocircuita $R_\mathrm{c}$, (c) se cortocircuita $R_\mathrm{d}$, (d) desaparece $R_\mathrm{f}$? Antes de calcular, predice cuál de los cuatro cambios tiene menos efecto.

:::loesung
Predicción: el que menos efecto tiene es (d), porque $R_\mathrm{f}$ es la mayor resistencia de su grupo en paralelo y conduce la menor corriente.

(a) $R_\mathrm{AB}=6\,\Omega+15\,\Omega=21\,\Omega$. (b) $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel10\,\Omega=13{,}5\,\Omega$. (c) Todo el grupo en paralelo queda puenteado: $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel5\,\Omega=10{,}29\,\Omega$. (d) $20\,\Omega\parallel30\,\Omega=12\,\Omega$, es decir, $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel17\,\Omega=16{,}85\,\Omega$.
:::
:::
