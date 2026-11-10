---
title: Etapa 5: El punto de trabajo
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El transistor bipolar
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Capítulo 10: El transistor bipolar
order: 1200700
summary: De antemano no se sabe qué región se aplica.
tags: recta de carga, tensión de alimentación
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
De antemano no se sabe qué región se aplica. Esta etapa determina el punto de trabajo suponiendo y comprobando, y lo dibuja como una intersección.
:::

**La idea.** El transistor aporta sus curvas características; el circuito, las ecuaciones de malla. Ambas deben cumplirse a la vez. El resultado es el punto de trabajo (PT), como en el [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) la intersección de una curva característica con una recta. Como cada región tiene otro circuito equivalente, se supone una región, se calcula linealmente y se comprueba. Una contradicción con las condiciones [(4.1)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-1) a [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) delata la suposición falsa.

:::abbildung et1/k10arbeit 6
Izquierda, el circuito del modelo de referencia. Derecha, las curvas características de salida linealizadas con la recta de carga de $(0;\,4\,\mathrm{mA})$ a $(12\,\mathrm{V};\,0)$. Corta la línea $I_\mathrm{B}=10$ µ A en el punto de trabajo A. S es el punto en la saturación, Z el punto en la región de corte.
:::

:::satz Teorema 5.1 (Punto de trabajo del circuito con resistencias de base y de colector)
<span class="anker" id="satz-5-1"></span>

La malla de entrada es $U_\mathrm{ent}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$; la malla de salida es la __recta de carga__ $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$. Para $U_\mathrm{ent}\le U_\mathrm{BE,on}$ el transistor bloquea y se cumple $U_\mathrm{BE}=U_\mathrm{ent}$. Para $U_\mathrm{ent}>U_\mathrm{BE,on}$, en las dos regiones de conducción se tiene

<span class="anker" id="gl-5-1"></span>
$$I_\mathrm{B}=\frac{U_\mathrm{ent}-U_\mathrm{BE,on}}{R_\mathrm{B}}. \tag{5.1}$$

Suponiendo la región activa resulta

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{C}=B\,I_\mathrm{B},\qquad U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}. \tag{5.2}$$

Si el resultado es $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$, la suposición es correcta. Si no, hay saturación, con

<span class="anker" id="gl-5-3"></span>
$$U_\mathrm{CE}=U_\mathrm{CE,sat},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}. \tag{5.3}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{CC}$ es la __tensión de alimentación__, $U_\mathrm{ent}$ la tensión de entrada respecto a masa. $R_\mathrm{B}$ fija la corriente de base, $R_\mathrm{C}$ convierte la corriente de colector en una tensión. **Validez:** emisor a masa, el modelo lineal de la etapa [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4). La ecuación [(5.1)](#gl-5-1) vale en las dos regiones de conducción porque allí hay la misma fuente de 0,6 V entre B y E.

::::beispiel
Modelo de referencia: $I_\mathrm{B}=(5\,\mathrm{V}-0{,}6\,\mathrm{V})/440\,\text{k}\Omega=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-6\,\mathrm{V}=6$ V. Es más de 0,2 V, luego activa (punto A). Una primera suposición falsa no hace daño: la saturación daría $I_\mathrm{C}=3{,}93$ mA, pero $B\,I_\mathrm{B}=2$ mA es menor, en contradicción con [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3). Para $U_\mathrm{ent}=12$ V es $I_\mathrm{B}=25{,}9$ µ A. Suponiendo la región activa saldría $U_\mathrm{CE}=-3{,}5$ V, es decir, una contradicción. En la saturación, $I_\mathrm{C}=3{,}93$ mA y $B\,I_\mathrm{B}=5{,}18$ mA (punto S).
::::

⁠**Casos límite:** $R_\mathrm{C}=0$ da $U_\mathrm{CE}=U_\mathrm{CC}$, y la salida queda rígida. $U_\mathrm{ent}<0{,}6$ V da $I_\mathrm{C}=0$ y $U_\mathrm{CE}=12$ V (punto Z).

**El centro de la región activa.** En la región activa, $U_\mathrm{CE}$ está entre 0,2 V y $U_\mathrm{CC}$. Para que una señal tenga el mismo margen a ambos lados, el punto se coloca en el centro. Con $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}=11{,}8$ V es

<span class="anker" id="gl-5-4"></span>
$$U_\mathrm{CE,PT}=U_\mathrm{CE,sat}+\frac{\Delta U}{2}=6{,}1\,\mathrm{V},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,PT}}{R_\mathrm{C}}=1{,}97\,\mathrm{mA}. \tag{5.4}$$

De ahí se deduce $R_\mathrm{B}=(U_\mathrm{ent}-U_\mathrm{BE})\,B/I_\mathrm{C}=447$ k$\Omega$. Los 440 k$\Omega$ del modelo de referencia están casi ahí.

**Con resistencia de emisor.** Si la base está directamente en $U_\mathrm{ent}$ y el emisor va a masa a través de $R_\mathrm{E}$, la malla de entrada es $U_\mathrm{ent}=U_\mathrm{BE,on}+R_\mathrm{E}I_\mathrm{E}$. Para $U_\mathrm{ent}>0{,}6$ V el transistor no bloquea, y

<span class="anker" id="gl-5-5"></span>
$$I_\mathrm{E}=\frac{U_\mathrm{ent}-U_\mathrm{BE,on}}{R_\mathrm{E}},\quad I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B},\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}. \tag{5.5}$$

Con $U_\mathrm{ent}=2{,}6$ V y $R_\mathrm{E}=1$ k$\Omega$ resultan $I_\mathrm{E}=2$ mA, $I_\mathrm{C}=1{,}99$ mA y $U_\mathrm{CE}=4{,}03$ V. Aquí $B$ entró en juego solo en el último paso y casi no cambia nada. La etapa [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7) aprovecha esto.

:::aufgabe Ejercicio 5 ★★ Calcular el punto de trabajo
<span class="anker" id="aufg-5"></span>

Se dan T, $U_\mathrm{CC}=10$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{B}=220$ k$\Omega$. (a) Determina el punto de trabajo para $U_\mathrm{ent}=3$ V. (b) Determínalo para $U_\mathrm{ent}=8$ V. (c) ¿Qué $R_\mathrm{B}$ coloca el punto en el centro de la región activa con $U_\mathrm{ent}=3$ V?

:::loesung
(a) $I_\mathrm{B}=2{,}4\,\mathrm{V}/220\,\text{k}\Omega=10{,}9$ µ A, $I_\mathrm{C}=2{,}18$ mA, $U_\mathrm{CE}=10\,\mathrm{V}-4{,}36\,\mathrm{V}=5{,}64$ V: activa.

(b) $I_\mathrm{B}=33{,}6$ µ A, $B\,I_\mathrm{B}=6{,}73$ mA. Suponiendo la región activa saldría $U_\mathrm{CE}=-3{,}45$ V, una contradicción. Por tanto, saturación: $U_\mathrm{CE}=0{,}2$ V, $I_\mathrm{C}=9{,}8\,\mathrm{V}/2\,\text{k}\Omega=4{,}9$ mA $<6{,}73$ mA.

(c) $U_\mathrm{CE,PT}=0{,}2\,\mathrm{V}+4{,}9\,\mathrm{V}=5{,}1$ V, $I_\mathrm{C}=4{,}9\,\mathrm{V}/2\,\text{k}\Omega=2{,}45$ mA, $I_\mathrm{B}=12{,}25$ µ A, $R_\mathrm{B}=2{,}4\,\mathrm{V}/12{,}25\,\mu\text{A}=196$ k$\Omega$.
:::
:::

:::aufgabe Ejercicio 6 ★★ Resistencia de emisor
<span class="anker" id="aufg-6"></span>

La base de T está directamente en $U_\mathrm{ent}=1{,}6$ V, con $U_\mathrm{CC}=12$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{E}=500\,\Omega$. (a) Determina $I_\mathrm{E}$, $I_\mathrm{B}$, $I_\mathrm{C}$ y $U_\mathrm{CE}$. (b) ¿Qué cambia si $B$ baja a 100?

:::loesung
(a) $I_\mathrm{E}=1\,\mathrm{V}/500\,\Omega=2$ mA, $I_\mathrm{B}=2\,\mathrm{mA}/201=9{,}95$ µ A, $I_\mathrm{C}=1{,}99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3{,}98\,\mathrm{V}-1\,\mathrm{V}=7{,}02$ V.

(b) $I_\mathrm{E}$ sigue siendo 2 mA, porque solo depende de $U_\mathrm{ent}$ y $R_\mathrm{E}$. $I_\mathrm{B}$ pasa a 19,8 µ A, $I_\mathrm{C}$ a 1,98 mA, $U_\mathrm{CE}$ a 7,04 V. La mitad de $B$, pero solo un 0,5 % menos de corriente de colector.
:::
:::
