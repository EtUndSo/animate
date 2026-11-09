---
title: Etapa 6: Trabajo en el campo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Carga, campo y potencial
order: 1110800
summary: Si una carga se mueve en un campo, la fuerza del campo realiza trabajo.
tags: irrotacional, electrostático
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Si una carga se mueve en un campo, la fuerza del campo realiza trabajo. Esta etapa lo calcula y muestra la propiedad en la que se basa todo lo demás: el trabajo no depende del camino.
:::

**La idea.** Una carga en un campo se comporta como la mochila de la etapa [1](groen-kraft-und-arbeit.html#stufe-1); la fuerza es ahora $Q\vec E$. Si una carga positiva avanza en el sentido del campo, el campo le cede energía. Si avanza en contra, otro debe aportar el trabajo, y la energía pasa al campo. Transversalmente al campo no ocurre nada.

:::satz Teorema 6.1 (Trabajo en el campo eléctrico)
<span class="anker" id="satz-6-1"></span>

Si una carga $Q$ va de $P_1$ a $P_2$, el campo realiza sobre ella el trabajo

<span class="anker" id="gl-6-1"></span>
$$W_{12}=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s,\qquad\text{en el campo uniforme}\quad W_{12}=Q\,E\,s\cos\alpha. \tag{6.1}$$

En el campo de cargas en reposo, $W_{12}$ solo depende de $P_1$ y $P_2$, no del camino. De forma equivalente, la integral a lo largo de cualquier camino cerrado es cero: el campo es __irrotacional__:

<span class="anker" id="gl-6-2"></span>
$$\oint_L\vec E\cdot\mathrm{d}\vec s=0. \tag{6.2}$$
:::

⁠**Cómo leerlo:** $Q$ es la carga que se mueve, con signo; $s$, la longitud de un camino recto que forma el ángulo $\alpha$ con $\vec E$. El círculo en la integral significa que el camino $L$ termina donde empezó. $W_{12}>0$ significa que el campo cede energía a la carga: la energía queda *liberada*. $W_{12}<0$ significa que hay que aportar desde fuera $W_\text{ext}=-W_{12}$, siempre que la carga no se acelere ni se frene. Con 1 nC y unos voltios se trata de nanojulios. **Validez:** [(6.2)](#gl-6-2) exige cargas en reposo y ningún campo magnético variable (etapa [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)). Un campo así se llama __electrostático__.

:::herleitung Por qué el trabajo no depende del camino
⁠**Una carga puntual.** Sea $Q$ moviéndose en el campo de $Q_0$ de $r_1$ a $r_2$. El camino se divide en tramos a lo largo del radio y transversales a él. En los tramos transversales, el campo es perpendicular al camino, y solo cuenta la variación de la distancia:

$$W_{12}=Q\int_{r_1}^{r_2}k\,\frac{Q_0}{r^2}\,\mathrm{d} r=k\,Q\,Q_0\Bigl(\frac{1}{r_1}-\frac{1}{r_2}\Bigr).$$

⁠**Cargas en reposo cualesquiera.** Todo campo de este tipo es una suma de campos de cargas puntuales, y el trabajo es la suma de los trabajos individuales.

⁠**Camino cerrado.** Si el camino $a$ lleva de $P_1$ a $P_2$ y el camino $b$ de vuelta, el camino de vuelta leído en sentido contrario cambia de signo: $\oint\vec E\cdot\mathrm{d}\vec s=\int_a\vec E\cdot\mathrm{d}\vec s-\int_{b,\,P_1\to P_2}\vec E\cdot\mathrm{d}\vec s=0$, porque ambos caminos dan el mismo valor.
:::

:::abbildung et1/k1feldarbeit 7
Detalle del par de placas, a escala. Una carga de prueba $+1$ nC recorre el triángulo. De 1 a 2 gana 9 nJ. De 2 a 3 va transversalmente al campo: ningún trabajo. De 3 a 1 pierde 9 nJ. La vuelta completa da cero.
:::

::::beispiel
En la fig. [7](#abb-7), $F=Q\,E=3$ µ N en la dirección $x$ y $W_{12}=10^{-9}\,\mathrm{C}\cdot3000\,\mathrm{V/m}\cdot3\,\mathrm{mm}=9$ nJ. Directamente de 1 a 3 el camino mide 5 mm, con $\cos\alpha=0{,}6$: de nuevo 9 nJ. En el campo de la esfera A ($Q_0=+10$ nC), $+1$ nC gana de 3 cm a 6 cm la energía $k\cdot1\,\mathrm{nC}\cdot10\,\mathrm{nC}\cdot(1/r_1-1/r_2)=1{,}5$ µ J.
::::

⁠**Casos límite:** Para $\alpha=90^\circ$ y para $P_2=P_1$, $W=0$. Con carga negativa, el signo se invierte: un electrón gana energía cuando avanza en contra de $\vec E$. Para $r_2\to\infty$, $W_{12}=kQQ_0/r_1$ sigue siendo finito.

:::frage Ida y vuelta siempre da cero. ¿Por qué es esto una afirmación especial?
Por el mismo camino de ida y vuelta, eso vale para cualquier campo de fuerzas. [(6.2)](#gl-6-2) es más fuerte: también vale si la vuelta va por otro camino. Si no, se podría hacer circular una carga y ganar energía en cada vuelta.
:::

:::aufgabe Ejercicio 6 ★★ Caminos en el campo
<span class="anker" id="aufg-6"></span>

En el campo uniforme $E=3$ kV/m en la dirección $x$, $Q=+2$ nC va de $P_1=(0;\,0)$ a $P_2=(2\,\mathrm{mm};\,1{,}5\,\mathrm{mm})$.

<ol class="al">

<li>

Calcula $W_{12}$ en el camino recto.

</li>

<li>

Calcula $W_{12}$ en el rodeo, primero en la dirección $y$ y luego en la dirección $x$.

</li>

<li>

¿Qué cambia para $Q=-2$ nC?

</li>

</ol>

:::loesung
(a) Longitud $s=\sqrt{2^2+1{,}5^2}\,\mathrm{mm}=2{,}5$ mm, $\cos\alpha=0{,}8$: $W_{12}=2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2{,}5\,\mathrm{mm}\cdot0{,}8=12$ nJ. (b) En la dirección $y$, el camino es perpendicular a $\vec E$: 0. En la dirección $x$: $2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2\,\mathrm{mm}=12$ nJ. (c) $W_{12}=-12$ nJ; hay que aportar 12 nJ desde fuera.
:::
:::
