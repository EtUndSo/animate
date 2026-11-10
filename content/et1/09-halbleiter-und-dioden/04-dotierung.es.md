---
title: Etapa 2: Dopado
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190400
summary: El silicio puro tiene muy pocos portadores de carga, y su número depende mucho de la temperatura.
tags: electrones de valencia, enlace covalente, donador, aceptor, región n, región p, portador mayoritario, portador minoritario
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
El silicio puro tiene muy pocos portadores de carga, y su número depende mucho de la temperatura. Esta etapa fija el tipo y el número de portadores con átomos de impureza.
:::

**La idea.** El silicio tiene cuatro __electrones de valencia__ (electrones de la capa más externa). Cada átomo comparte un par de electrones con cada uno de sus cuatro vecinos; eso es el __enlace covalente__. Si se sustituye un átomo por fósforo, con cinco electrones de valencia, cuatro se enlazan y el quinto sobra (fig. [3](#abb-3)). Está unido al resto del átomo de fósforo con solo 45 meV, que es 1,7 veces $k_\mathrm BT$. El calor casi siempre lo libera, se convierte en un electrón libre en la BC y queda un ion $\mathrm P^+$ fijo. El boro solo tiene tres electrones de valencia. Un enlace queda abierto, y un electrón vecino salta a él, también con 45 meV. El ion $\mathrm B^-$ fijo se queda, y el hueco se aleja.

:::abbildung et1/k9dotierung 3
Izquierda: cristal en el plano; cada línea doble es un enlace. Derecha: bandas a 300 K, sin escala. El nivel $W_\mathrm D$ del fósforo está 45 meV por debajo de la BC, el nivel $W_\mathrm A$ del boro 45 meV por encima de la BV. Flechas: el calor entrega los electrones a la BC (arriba) y los saca de la BV (abajo). La energía de Fermi se acerca a la banda de la mayoría.
:::

:::definition Definición 2.1 (Dopado n y p)
<span class="anker" id="satz-2-1"></span>

Un __donador__ (fósforo) cede un electrón, un __aceptor__ (boro) toma uno. Con $N_\mathrm D$ donadores por cm$^3$ se forma una __región n__, con $N_\mathrm A$ aceptores por cm$^3$ una __región p__:

<span class="anker" id="gl-2-1"></span>
$$\text{región n: }n\approx N_\mathrm D,\qquad\text{región p: }p\approx N_\mathrm A,\qquad\text{en todas partes: }n\,p=n_\mathrm i^2. \tag{2.1}$$
:::

⁠**Cómo leerlo:** $n$ y $p$ son las densidades de electrones y huecos en 1/cm$^3$. El tipo más frecuente se llama __portador mayoritario__, el más escaso __portador minoritario__. Lo habitual es $N=10^{15}$ a $10^{19}\,\mathrm{cm^{-3}}$. El dopado no carga el cristal: a cada electrón libre le corresponde un $\mathrm P^+$ fijo. En la región n, la energía de Fermi sube $k_\mathrm BT\ln(n/n_\mathrm i)$ por encima del centro de la brecha. **Validez:** temperatura ambiente (todos los átomos de impureza ionizados) y $N\gg n_\mathrm i$.

:::herleitung Por qué el producto es constante
El calor genera pares de electrón y hueco a un ritmo que solo depende de $T$ y del material. La recombinación requiere que ambos se encuentren; su ritmo es $c\,n\,p$. En equilibrio ambos ritmos son iguales, así que $n\,p$ es constante. En silicio puro $n=p=n_\mathrm i$, por tanto $n\,p=n_\mathrm i^2$. Más electrones significan más recombinación y menos huecos.
:::

::::beispiel
Con $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ hay un átomo de impureza por cada $5\cdot10^{6}$ átomos de silicio, y aun así $n$ sube a un millón de veces $n_\mathrm i$. Los huecos bajan a $p=10^{20}/10^{16}=10^{4}\,\mathrm{cm^{-3}}$. Mayoría y minoría están separadas por un factor $10^{12}$. $W_\mathrm F$ sube $25{,}85\,\mathrm{meV}\cdot\ln10^{6}=0{,}36$ eV.
::::

⁠**Caso límite:** Para $N_\mathrm D\to0$, [(2.1)](#gl-2-1) vuelve a dar $n=p=n_\mathrm i$.

:::frage ¿El silicio tipo n tiene carga negativa y el tipo p carga positiva?
No, ambos son neutros. «n» y «p» indican el signo de las cargas móviles, no el de la pieza. En la región n, cada electrón libre tiene enfrente un ion positivo fijo. Solo en la unión pn se separan ambos (etapa [3](die-raumladungszone.html#stufe-3)).
:::

:::aufgabe Ejercicio 2 ★★ Contar portadores
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

El silicio recibe $N_\mathrm D=5\cdot10^{15}\,\mathrm{cm^{-3}}$. ¿Cuántos átomos de silicio hay por átomo de impureza? ¿Cuánto valen $n$ y $p$?

</li>

<li>

¿Cuánto valen $n$ y $p$ con $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$?

</li>

<li>

Predicción: una pieza recibe tantos donadores como aceptores. ¿Qué ocurre con los portadores de carga?

</li>

</ol>

:::loesung
(a) $5\cdot10^{22}/5\cdot10^{15}=10^{7}$ átomos por átomo de impureza, $n=5\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=10^{20}/5\cdot10^{15}=2\cdot10^{4}\,\mathrm{cm^{-3}}$. (b) $p=2\cdot10^{17}\,\mathrm{cm^{-3}}$, $n=500\,\mathrm{cm^{-3}}$. (c) Cada electrón donador cae en un aceptor. No surgen portadores adicionales, $n=p=n_\mathrm i$. El cristal se comporta como silicio puro aunque está lleno de iones. Esto se llama __compensación__.
:::
:::
