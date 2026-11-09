---
title: Etapa 2: Carga
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Carga, campo y potencial
order: 1110400
summary: Esta etapa aclara la primera pregunta: ¿qué es la carga, cómo se origina un cuerpo cargado y qué se conserva en el proceso?
tags: defecto de electrones, exceso de electrones, carga elemental, conservación de la carga, conductor, aislante
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Esta etapa aclara la primera pregunta: ¿qué es la carga, cómo se origina un cuerpo cargado y qué se conserva en el proceso?
:::

**La idea.** La electricidad por frotamiento, el rayo como descarga de cargas separadas a través del aire y el magnetismo no pueden explicarse con la mecánica. Si se frota una varilla de vidrio con un paño de seda y una varilla de ebonita con una piel, las dos varillas se atraen, mientras que dos varillas de ebonita se repelen (fig. [3](#abb-3)). Al frotar no se crea nada nuevo: los electrones cambian de cuerpo. Las distintas sustancias retienen sus electrones exteriores con distinta fuerza. En los puntos de contacto, los electrones pasan a la sustancia que los retiene con más fuerza, y el frotamiento crea muchos de esos puntos. Un cuerpo con __defecto de electrones__ está cargado positivamente; uno con __exceso de electrones__, negativamente.

:::abbildung et1/k1reibung 3
Arriba: el frotamiento separa carga. Los electrones ($\mathrm{e}^-$) pasan del vidrio a la seda y de la piel a la ebonita. Abajo: las varillas con carga de signo opuesto se atraen; las de mismo signo se repelen.
:::

:::definition Definición 2.1 (Carga)
<span class="anker" id="satz-2-1"></span>

Un cuerpo con $N_\mathrm{p}$ protones y $N_\mathrm{e}$ electrones tiene la carga

<span class="anker" id="gl-2-1"></span>
$$Q=(N_\mathrm{p}-N_\mathrm{e})\,e,\qquad e=1{,}602\cdot10^{-19}\,\mathrm{C},\qquad[Q]=\mathrm C=\mathrm{A\,s}. \tag{2.1}$$

La __carga elemental__ $e$ es la carga más pequeña que aparece libre. Un electrón tiene $-e$; un protón, $+e$. En un sistema cerrado, la suma de todas las cargas permanece constante (__conservación de la carga__).
:::

⁠**Cómo leerlo:** La carga solo aparece en múltiplos de $e$; un culombio son $6{,}24\cdot10^{18}$ cargas elementales. Las varillas frotadas tienen alrededor de 10 nC. **Validez:** Este escalonamiento solo se nota en partículas individuales; ya 1 nC son seis mil millones de electrones. Por eso, en los circuitos la carga se trata como una magnitud continua.

:::herleitung Por qué frotar no cambia la carga total
Dos cuerpos tienen juntos $Q_1+Q_2=\bigl[(N_\mathrm{p1}+N_\mathrm{p2})-(N_\mathrm{e1}+N_\mathrm{e2})\bigr]e$. Si un electrón pasa de 1 a 2, $N_\mathrm{e1}$ disminuye en uno y $N_\mathrm{e2}$ aumenta en uno; el corchete no cambia. Las cargas «generadas» al frotar siempre suman cero.
:::

Los nombres son más antiguos que el electrón. En 1733, DuFay distinguió entre electricidad vítrea y resinosa; hacia 1750, Franklin llamó positiva a la una y negativa a la otra. La palabra griega para ámbar, *elektron*, dio nombre a este ámbito.

**Conductores y aislantes.** En un __conductor__ como el metal, al menos un electrón por átomo puede desplazarse por todo el cuerpo. En un __aislante__ como el vidrio o la goma, los electrones permanecen en sus átomos. Por eso, en un aislante la carga se queda donde se produjo, mientras que en un metal se reparte de inmediato.

::::beispiel
A la esfera A ($+10$ nC) le faltan $N=Q/e=6{,}24\cdot10^{10}$ electrones. Una esfera de plástico de 1 g contiene unos $3{,}2\cdot10^{23}$ electrones, así que solo falta uno de cada $5\cdot10^{12}$.
::::

⁠**Caso límite:** Para $N_\mathrm{p}=N_\mathrm{e}$ es $Q=0$. Un cuerpo neutro no contiene poca carga, sino la misma cantidad de ambos signos.

:::frage ¿Por qué precisamente la falta de electrones se llama positiva?
Porque los signos se asignaron antes de que se conocieran los electrones. Franklin llamó positivo al vidrio frotado; mucho después se vio que al frotarlo pierde electrones. La convención se mantuvo, y por eso el electrón tiene carga negativa. Físicamente no tiene nada de especial.
:::

:::aufgabe Ejercicio 2 ★ Contar cargas
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Tras frotarla, una varilla de vidrio tiene $+8$ nC. ¿Cuántos electrones ha cedido? ¿Qué carga tiene el paño si antes ambos eran neutros?

</li>

<li>

Dos esferas metálicas iguales tienen $+8$ nC y $-2$ nC. Se tocan y se separan. ¿Qué carga tiene cada una? ¿Cuántos electrones han pasado, y en qué dirección?

</li>

</ol>

:::loesung
(a) $N=8\cdot10^{-9}\,\mathrm{C}/(1{,}602\cdot10^{-19}\,\mathrm{C})=4{,}99\cdot10^{10}$ electrones. El paño los ha recibido y tiene $-8$ nC. (b) La carga total $+6$ nC se conserva y se reparte por igual entre esferas iguales: $+3$ nC cada una. La esfera negativa cede, por tanto, $5\cdot10^{-9}\,\mathrm{C}/e=3{,}12\cdot10^{10}$ electrones a la positiva.
:::
:::
