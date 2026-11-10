---
title: Etapa 1: Por qué el silicio apenas conduce
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190300
summary: El metal conduce, el vidrio no, el silicio puro apenas.
tags: niveles de energía, banda, zona prohibida, banda de valencia, banda de conducción, brecha de banda, energía de Fermi, metal
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
El metal conduce, el vidrio no, el silicio puro apenas. La diferencia está en el número de electrones móviles. Esta etapa lo explica a partir de las energías permitidas en el cristal.
:::

**La idea.** En un átomo aislado, los electrones solo tienen determinadas energías, los __niveles de energía__. En un cristal (red regular de átomos) las capas se solapan y los electrones pertenecen a todo el cristal. Dos electrones no pueden ocupar el mismo estado. Por eso cada nivel se desdobla en tantos niveles muy próximos como átomos tiene el cristal. Así se forma una __banda__ de energías permitidas. Entre las bandas está la __zona prohibida__: allí no hay estados. Un campo solo puede acelerar a un electrón si justo por encima de él hay un estado libre. Por tanto, una banda llena no conduce, por muchos electrones que contenga.

:::abbildung et1/k9baender 2
Modelo de bandas, sin escala; $W$ es la energía de un electrón. En el metal, la banda superior está solo parcialmente llena. En el semiconductor, el calor eleva unos pocos electrones sobre la pequeña brecha y quedan huecos. En el aislante, la brecha es demasiado grande.
:::

:::definition Definición 1.1 (Bandas)
<span class="anker" id="satz-1-1"></span>

La __banda de valencia__ (BV) es la banda superior que a $T=0$ está completamente ocupada. La __banda de conducción__ (BC) está por encima y a $T=0$ está vacía. La __brecha de banda__ $W_\mathrm g$ es la menor energía que eleva un electrón de la BV a la BC. La __energía de Fermi__ $W_\mathrm F$ separa a $T=0$ los estados ocupados de los libres. A $T>0$ es la energía a la que un estado estaría ocupado la mitad del tiempo; puede estar dentro de la brecha aunque allí no haya ningún estado.
:::

⁠**Cómo leerlo:** El silicio tiene $W_\mathrm g=1{,}12$ eV, el germanio 0,67 eV, el diamante 5,5 eV. **Tres casos:** En el __metal__, la banda ocupada superior está solo parcialmente llena, hay estados libres justo por encima de los electrones y conduce a cualquier temperatura. En el __aislante__, $W_\mathrm g$ es tan grande que ningún electrón llega a pasar. Un semiconductor es un aislante con una brecha pequeña: a $T=0$ aísla; con excitación por calor, luz o campos intensos, los electrones llegan a la BC.

Un electrón que pasa a la BC deja un lugar libre en la BV. Un electrón vecino lo ocupa, y el lugar se desplaza. El __hueco__ (defecto de electrón) se comporta como una partícula móvil con carga $+e$. Ambos cuentan como portadores de carga: los electrones en la BC y los huecos en la BV. Si un electrón cae de nuevo en un hueco, ambos desaparecen; esto se llama __recombinación__.

:::satz Teorema 1.2 (Fracción de electrones en la banda de conducción)
<span class="anker" id="satz-1-2"></span>

En un semiconductor puro, $W_\mathrm F$ está en el centro de la brecha. Por eso, para los estados en el borde de la BC,

<span class="anker" id="gl-1-1"></span>
$$\text{ocupación}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}. \tag{1.1}$$
:::

:::herleitung Por qué cuenta media brecha
Cada electrón en la BC deja un hueco en la BV, así que el número de ambos es igual. Con un número similar de estados en ambas bandas, esto solo es posible si $W_\mathrm F$ está a la misma distancia $W_\mathrm g/2$ de los dos bordes de banda. En [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1) cuenta la energía por encima de $W_\mathrm F$, es decir, $W=W_\mathrm g/2$.
:::

::::beispiel
A 300 K, $W_\mathrm g/(k_\mathrm BT)=43{,}3$ y $\mathrm{e}^{-21{,}7}=3{,}9\cdot10^{-10}$. La densidad medida de electrones libres es $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$. Eso es uno por cada $5\cdot10^{12}$ átomos, porque el silicio tiene $5\cdot10^{22}$ átomos por cm$^3$. El cobre tiene $8{,}5\cdot10^{12}$ veces más electrones libres ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).
::::

⁠**Casos límite:** Para $T\to0$, [(1.1)](#gl-1-1) tiende a cero: el silicio aísla. Cada 10 K de calentamiento duplican la fracción. Por eso la resistencia de un semiconductor baja con la temperatura ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::frage ¿Por qué no conduce una banda llena, si está repleta de electrones?
Porque la corriente necesita un movimiento en una dirección preferente. Para ello, un electrón tendría que pasar a un estado con algo más de energía. En la banda llena, todos esos estados están ocupados. Dos electrones solo podrían intercambiarse, y eso no cambia nada. El primer hueco hace conductora la banda.
:::

:::aufgabe Ejercicio 1 ★ Comparar tres materiales
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Expresa $W_\mathrm g=1{,}12$ eV en julios. ¿Cuántas veces $k_\mathrm BT$ es eso a 300 K?

</li>

<li>

Calcula [(1.1)](#gl-1-1) para silicio, germanio y diamante. ¿Qué material puro conduce mejor?

</li>

<li>

El silicio se calienta de 300 K a 330 K. ¿En qué factor crece la fracción?

</li>

</ol>

:::loesung
(a) $1{,}12\cdot1{,}602\cdot10^{-19}\,\mathrm{J}=1{,}79\cdot10^{-19}$ J, es decir, $1{,}12\,\mathrm{eV}/25{,}85\,\mathrm{meV}=43{,}3$ veces $k_\mathrm BT$. (b) Silicio $3{,}9\cdot10^{-10}$, germanio $2{,}4\cdot10^{-6}$, diamante $6{,}3\cdot10^{-47}$. El germanio conduce mejor, con unas 6000 veces más ocupación que el silicio; el diamante prácticamente no tiene electrones libres. (c) Con $U_T=28{,}44$ mV a 330 K la fracción es $2{,}8\cdot10^{-9}$, 7,2 veces más.
:::
:::
