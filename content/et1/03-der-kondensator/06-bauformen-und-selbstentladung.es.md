---
title: Etapa 5: Tipos constructivos y autodescarga
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El condensador
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Capítulo 3: El condensador
order: 1130600
summary: 100 µF como par de placas en aire ocuparían 3,4 hectáreas.
tags: electrolito, polarizado, Autorreparable, corriente de fuga, resistencia de aislamiento
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
100 µF como par de placas en aire ocuparían 3,4 hectáreas. Los condensadores reales lo resuelven mediante $A$, $d$ y $\varepsilon$. Cada tipo constructivo paga por ello su propio precio.
:::

**La idea.** La ecuación [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) tiene tres palancas de ajuste, y todos los tipos constructivos actúan sobre ellas (fig. [5](#abb-5)).

<ul>

<li>

⁠**Condensador de película:** Dos largas tiras metálicas, separadas por película de plástico o papel, se enrollan formando un bobinado. Así cabe una gran área en poco espacio.

</li>

<li>

⁠**Condensador cerámico:** Una cerámica de $\varepsilon_\mathrm{r}$ grande, a menudo en muchas capas finas superpuestas y conectadas en paralelo (etapa [7](parallel-und-reihenschaltung.html#stufe-7)). El precio: $\varepsilon_\mathrm{r}$ depende de la tensión y de la temperatura.

</li>

<li>

⁠**Condensador electrolítico:** El electrodo es una lámina de aluminio rugosa. Eso aumenta $A$. El dieléctrico es una capa de óxido de solo unas decenas de nanómetros, lo que hace pequeña $d$. El contraelectrodo es un líquido conductor, el __electrolito__, porque solo él sigue cada hendidura. El precio: el condensador electrolítico está __polarizado__; el óxido solo aguanta en un sentido. Mal conectado se degrada, circula corriente, el componente se calienta y puede reventar.

</li>

<li>

⁠**Supercap (también Goldcap):** En un electrodo de carbono poroso con una enorme superficie interna, los iones del electrolito se acumulan a una distancia de cerca de 1 nm. Eso da capacidades de hasta 100 F y más. El precio: solo unos pocos voltios, por encima de los cuales el electrolito se descompone, y una corriente de fuga comparativamente alta.

</li>

</ul>

:::abbildung et1/k3bauform 5
Cuatro caminos hacia una gran capacidad, secciones esquemáticas, sin escala. En rojo y azul, los dos electrodos; en el condensador electrolítico, en naranja el óxido sobre el aluminio y en azul claro el electrolito. En el supercap, los iones se sitúan muy cerca del carbono.
:::

| Tipo | Capacidad | Tensión | Tamaño | Polarizado | Autorreparable |
|---|---|---|---|---|---|
| Papel, papel metalizado | 100 pF a 50 µF | 125 V a 1 kV | grande | no | solo metalizado |
| Película de plástico | 2 pF a 200 µF | 50 V a 5 kV | mediano a muy pequeño | no | solo metalizado |
| Cerámica | 0,5 pF a 100 µF | 6 V a 1 kV | pequeño | no | no |
| Electrolítico | 0,5 µF a 10 mF | 3 V a 650 V | muy pequeño | sí | sí |
| Supercap | 0,1 F a más de 100 F | unos pocos voltios | muy pequeño | sí | no |

La tabla resume los rangos habituales. __Autorreparable__ significa: en una ruptura, la fina capa metálica se evapora alrededor del defecto, el cortocircuito desaparece y solo se pierde un área diminuta. En el condensador electrolítico, el óxido se forma de nuevo en el defecto.

**Autodescarga.** Ningún aislante es perfecto. El dieléctrico contiene unas pocas cargas móviles, por lo que circula una corriente diminuta de placa a placa, la __corriente de fuga__. En el circuito equivalente hay, en paralelo con el condensador ideal, una __resistencia de aislamiento__ $R_\mathrm{I}$. Idealmente, $R_\mathrm{I}\to\infty$ y un condensador desconectado conserva su carga para siempre. En la realidad la cede al ritmo $R_\mathrm{I}\,C$ (etapa [10](entladen-und-zeitkonstante.html#stufe-10)). Con la resistividad $\rho$ del material ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) es $R_\mathrm{I}=\rho\,d/A$, y junto con [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) resulta

<span class="anker" id="gl-5-1"></span>
$$R_\mathrm{I}\,C=\rho\,\varepsilon. \tag{5.1}$$

$A$ y $d$ se simplifican: la autodescarga solo depende del material, no del tamaño del componente.

::::beispiel
La película de plástico con $\rho\approx10^{16}\,\Omega\,$m y $\varepsilon_\mathrm{r}=2{,}2$ da unos dos días. Para un condensador electrolítico de 100 µF a 9 V, las hojas de datos indican como máximo unos 9 µA de corriente de fuga, es decir, $R_\mathrm{I}\approx1\,\mathrm{M\Omega}$. Eso es 100 veces más que $R$ en el circuito RC; la corriente de fuga es el 1 % de 0,9 mA y se desprecia en las etapas siguientes.
::::

⁠**Caso límite:** Para $\rho\to\infty$, $R_\mathrm{I}\,C$ crece sin límite; es el condensador ideal sin autodescarga.

:::frage ¿Por qué no se usa siempre el tipo con la mayor capacidad?
Porque cada tipo tiene su precio. Los condensadores electrolíticos están polarizados y tienen grandes tolerancias; los supercaps solo aguantan unos pocos voltios. Donde la tensión cambia de signo o la capacidad debe ser exacta, se usa película o cerámica.
:::

:::aufgabe Ejercicio 6 ★ Comprobar un condensador electrolítico
<span class="anker" id="aufg-6"></span>

Un condensador electrolítico de 100 µF y 16 V tiene una capa de óxido con $\varepsilon_\mathrm{r}=9$ y un grosor de 1,4 nm por voltio.

<ol class="al">

<li>

¿Qué grosor tiene el óxido y qué área hace falta?

</li>

<li>

En el vaso cabe una tira de 3 cm por 20 cm. ¿En qué factor debe aumentar la superficie el tratamiento de rugosidad?

</li>

<li>

¿Por qué un contraelectrodo metálico liso no daría esta ganancia?

</li>

</ol>

:::loesung
(a) $d=16\cdot1{,}4\,\mathrm{nm}=22{,}4$ nm. $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot22{,}4\cdot10^{-9}\,\mathrm{m}}{9\cdot8{,}854\cdot10^{-12}\,\mathrm{F/m}}=281\,\mathrm{cm^2}$.

(b) La tira tiene 60 cm$^2$, de modo que hace falta un factor $281/60=4{,}7$.

(c) Un contraelectrodo sólido solo tocaría las crestas de la superficie rugosa. Las hendiduras no aportarían nada, y allí la distancia sería mucho mayor que el grosor del óxido. Solo un líquido sigue la superficie a la distancia $d$.
:::
:::
