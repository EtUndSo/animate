---
title: Etapa 2: Electrones lentos, corriente inmediata
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120300
summary: La etapa 1 necesita una velocidad v .
tags: red cristalina, movilidad, recorrido libre medio
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
La etapa [1](strom-ist-bewegte-ladung.html#stufe-1) necesita una velocidad $v$. Esta etapa muestra por qué es constante y diminuta, y resuelve la contradicción con la lámpara que se enciende al instante.
:::

**La idea.** En un metal, al menos un electrón por átomo ya no está ligado a su átomo. Los iones positivos que quedan forman una __red cristalina__ regular. Si se aplica una tensión, hay un campo en el hilo. Este acelera cada electrón libre en contra del sentido del campo. Al poco tiempo, el electrón se dispersa y cede a la red cristalina la velocidad dirigida ganada; después empieza de nuevo (fig. [2](#abb-2)). En promedio queda una velocidad constante: las colisiones quitan exactamente lo que da el campo.

:::abbildung et1/k2drift 2
Izquierda: trayectoria de un electrón en la red cristalina (esquemática, sin escala). Derecha: modelo para la parte dirigida de la velocidad. Crece en el campo hasta $v_\mathrm{max}$ y cae a cero en la colisión. Su valor medio es la velocidad de deriva $v_\mathrm D=v_\mathrm{max}/2$.
:::

:::satz Teorema 2.1 (Velocidad de deriva)
<span class="anker" id="satz-2-1"></span>

Si cada vuelo entre dos colisiones dura el tiempo $T$, entonces

<span class="anker" id="gl-2-1"></span>
$$|\vec v_\mathrm{max}|=\frac{e\,|\vec E|}{m_\mathrm e}\,T,\qquad\vec v_\mathrm D=-\mu\,\vec E,\qquad\mu=\frac{e\,T}{2\,m_\mathrm e}. \tag{2.1}$$

Con la etapa [1](strom-ist-bewegte-ladung.html#stufe-1), de la corriente se obtiene $v_\mathrm D=j/(n\,e)=I/(n\,e\,A)$.
:::

⁠**Cómo leerlo:** $\vec v_\mathrm D$ es la velocidad de deriva en m/s. El signo menos dice: los electrones son negativos, avanzan en contra de $\vec E$. $\mu$ es la __movilidad__, la velocidad de deriva por unidad de intensidad de campo, en $\mathrm{m^2/(V\,s)}$. Es una constante del material, en el cobre $4{,}3\cdot10^{-3}\,\mathrm{m^2/(V\,s)}$. $T$ es el tiempo de vuelo, en el cobre unos 49 fs. En este tiempo, el electrón recorre en promedio el __recorrido libre medio__ $\lambda$. **Validez:** [(2.1)](#gl-2-1) es un modelo. Solo cuenta la parte de la velocidad producida por el campo. Además, los electrones vuelan desordenadamente en todas las direcciones a unos 1600 km/s. Este movimiento se anula en promedio, no transporta corriente y se mantiene en las colisiones.

:::herleitung Del campo a la deriva
De $F=m_\mathrm e\,a$ y $F=e\,E$ ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)) se obtiene la aceleración $a=e\,E/m_\mathrm e$. Un vuelo empieza con la parte dirigida en cero, así que $v(t)=a\,t$ y $v_\mathrm{max}=a\,T$. El diente de sierra tiene el valor medio $v_\mathrm{max}/2=e\,E\,T/(2\,m_\mathrm e)$. La velocidad no sigue creciendo, porque cada colisión la devuelve a cero.
:::

::::beispiel
En el hilo, $v_\mathrm D=j/(n\,e)=6\cdot10^3\,\mathrm{A/m^2}/(1{,}36\cdot10^{10}\,\mathrm{C/m^3})=4{,}4\cdot10^{-7}$ m/s, es decir, 0,44 µ m/s. Para recorrer un metro, un electrón necesitaría 26 días. El campo en el hilo es $E=v_\mathrm D/\mu=0{,}10$ mV/m. La deriva es tan pequeña porque el hilo contiene muchísimos portadores de carga: 6800 C por metro solo tienen que aportar 3 mC por segundo.
::::

⁠**En resumen:** La velocidad de deriva es la corriente dividida por la carga libre por metro. **Casos límite:** Sin campo, $v_\mathrm D=0$. El doble de corriente da el doble de deriva. Muchas colisiones ($T\to0$) dan $\mu\to0$: el material no conduce.

**Por qué, aun así, la corriente está ahí al instante.** En el hilo viajan dos cosas que no deben confundirse. Los electrones derivan lentamente. El campo, en cambio, se propaga a lo largo del hilo como onda electromagnética al cerrar el interruptor, en los cables a unos $2\cdot10^8$ m/s. Los electrones ya están en todo el hilo. Cada uno empieza a derivar en cuanto lo alcanza el frente de campo (fig. [3](#abb-3)). Tras unos pocos de estos tiempos de propagación circula en todo el circuito la corriente estacionaria. La energía viaja con el campo, no con los electrones. El frente tarda 5 ns en recorrer un metro. En estos 5 ns, un electrón deriva 2,2 fm, unas 100 000 veces menos que la distancia entre dos átomos de cobre. Las dos velocidades difieren en un factor de $4{,}5\cdot10^{14}$.

:::abbildung et1/k2sofort 3
Un metro de hilo en tres momentos después de cerrar el interruptor de la izquierda. El frente de campo lo recorre en 5 ns. Detrás del frente derivan todos los electrones; delante de él están, en promedio, en reposo. Los propios electrones prácticamente no han avanzado en este tiempo.
:::

:::analogie
Una cadena de bicicleta está llena de eslabones por todas partes. Si se pedalea delante, se mueve detrás en el mismo momento, aunque cada eslabón avanza despacio. La analogía termina en el mecanismo: los eslabones se empujan mecánicamente y el efecto recorre el metal a la velocidad del sonido. En el hilo viaja un campo, y su velocidad es cercana a la de la luz.
:::

:::frage El capítulo 1 dice que en el metal $\vec E=0$. ¿Por qué hay un campo en el hilo y cómo sigue las curvas?
$\vec E=0$ solo vale en estado de reposo, cuando todas las cargas se han detenido. La fuente no lo permite: extrae electrones por un extremo y los aporta por el otro, de modo que nunca se alcanza el reposo. Queda un pequeño campo, aquí 0,10 mV/m. En las curvas se acumulan cargas diminutas en la superficie del hilo. Su campo dirige $\vec E$ en todas partes a lo largo del hilo; de lo contrario, los electrones chocarían contra la pared y la carga allí seguiría creciendo.
:::

:::zusatz Qué velocidad tienen realmente los electrones
El movimiento desordenado es $3{,}6\cdot10^{12}$ veces más rápido que la deriva en el hilo. Es una consecuencia de la mecánica cuántica y se mantiene incluso cerca del cero absoluto. Los tiempos de vuelo varían, y con tiempos dispersos el factor $\frac12$ de $\mu$ desaparece si $T$ es el tiempo de vuelo medio. Entonces $T=25$ fs, y el recorrido libre $\lambda$ es de unos 39 nm, unas 150 distancias atómicas. La imagen «colisión con cada átomo» es, por tanto, demasiado burda: una red cristalina perfecta en reposo no dispersa electrones en absoluto. Chocan con vibraciones de la red cristalina, átomos extraños y defectos.
:::

:::aufgabe Ejercicio 2 ★★ Deriva y tiempo de propagación
<span class="anker" id="aufg-2"></span>

El cable del ejercicio [1](strom-ist-bewegte-ladung.html#aufg-1) es de cobre y mide 30 m.

<ol class="al">

<li>

Calcula $v_\mathrm D$ y el campo $E=\rho\,j$ en el cable.

</li>

<li>

¿Cuánto tardaría un electrón en recorrer los 30 m, y cuánto el frente de campo?

</li>

<li>

Predicción: ¿Cómo cambia $v_\mathrm D$ si la sección se duplica con la misma corriente?

</li>

</ol>

:::loesung
(a) $j=1{,}07\cdot10^7\,\mathrm{A/m^2}$, $v_\mathrm D=j/(n\,e)=0{,}78$ mm/s. $E=\rho\,j=0{,}18$ V/m.

(b) Electrón: $30\,\mathrm{m}/0{,}78\,\mathrm{mm/s}=3{,}8\cdot10^4$ s $=10{,}6$ h. Frente de campo: $30\,\mathrm{m}/(2\cdot10^8\,\mathrm{m/s})=150$ ns.

(c) Se reduce a la mitad: el doble de portadores de carga por metro se reparte la misma corriente, $v_\mathrm D=I/(n\,e\,A)$.
:::
:::
