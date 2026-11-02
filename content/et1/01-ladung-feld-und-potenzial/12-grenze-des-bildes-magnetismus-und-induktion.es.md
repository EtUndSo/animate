---
title: Etapa 10: Límite de la imagen: magnetismo e inducción
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Carga, campo y potencial
order: 1111200
summary: Todo lo anterior valía para cargas en reposo.
tags: campo magnético, bobina, inducción, electromagnetismo, campo rotacional, regla de la mano derecha, sentido técnico de la corriente, flujo magnético
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Todo lo anterior valía para cargas en reposo. Esta etapa muestra qué cambia cuando las cargas se mueven y los campos magnéticos varían, y dónde termina la independencia del camino.
:::

**La idea.** Durante mucho tiempo, la electricidad y el magnetismo se consideraron dos ámbitos separados. En 1820, Ørsted vio que una aguja de brújula se desviaba junto a un cable con corriente: la carga en movimiento crea un __campo magnético__ $H$. En 1831, Faraday invirtió la idea: un imán que movía dentro de una __bobina__, un cable enrollado en espiras, creaba una tensión en sus extremos. Esto se llama __inducción__. En 1864, Maxwell lo reunió todo en el __electromagnetismo__. El mecanismo de la inducción es un campo nuevo: un campo magnético variable crea un campo eléctrico con líneas cerradas, un __campo rotacional__. En una vuelta por él, una carga gana energía, y ahí termina la afirmación [(6.2)](arbeit-im-feld.html#gl-6-2).

:::abbildung et1/k1oersted 12
Izquierda: sección de un cable; la corriente $I$ fluye hacia el plano. El campo magnético $H$ describe círculos alrededor del cable, y las agujas de brújula orientan según él su punta roja. Derecha: un imán de barra en movimiento cambia el flujo magnético $\Phi$ a través de la bobina. Mientras se mueve, el instrumento muestra la tensión $u_\mathrm{ind}$.
:::

La dirección del campo magnético la da la __regla de la mano derecha__: el pulgar apunta en el sentido técnico de la corriente, y los dedos, en el sentido del campo. El __sentido técnico de la corriente__ va de positivo a negativo; los electrones del cable se mueven al revés ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::satz Teorema 10.1 (Ley de inducción)
<span class="anker" id="satz-10-1"></span>

Si varía el flujo magnético $\Phi$ a través de una bobina de $N$ espiras, entre sus extremos aparece la tensión

<span class="anker" id="gl-10-1"></span>
$$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}. \tag{10.1}$$
:::

⁠**Cómo leerlo:** El __flujo magnético__ $\Phi$ mide cuánto campo magnético atraviesa la superficie de la bobina, $[\Phi]=\mathrm{V\,s}=\mathrm{Wb}$ (weber). Las bobinas pequeñas abarcan de microwebers a miliwebers. Solo cuenta la variación, no el flujo en sí. La ley es un resultado de medida: a lo largo de una espira, el campo rotacional da la tensión $|\mathrm{d}\Phi/\mathrm{d} t|$; las $N$ espiras están en serie y sus tensiones se suman. La letra minúscula $u$ indica una tensión que depende del tiempo. El signo menos significa que una corriente impulsada por esta tensión se opone a la variación del flujo. **Validez:** Todas las espiras deben abarcar el mismo flujo.

Faraday también mostró la inducción sin imán: enrolló dos bobinas en un anillo y conectó una batería a una y un galvanómetro (un antiguo medidor de corriente) a la otra. Solo se desviaba al conectar y desconectar, porque solo entonces cambia el flujo.

**Las ecuaciones de Maxwell en palabras.** Las ecuaciones en sí requieren más matemáticas, pero su contenido cabe en cuatro frases. La __densidad de flujo__ es aquí la medida de la densidad de las líneas de campo. **Ley de Gauss para campos eléctricos:** Las cargas son fuentes y sumideros de la densidad de flujo eléctrico. **Ley de Gauss para el magnetismo:** La densidad de flujo magnético no tiene fuentes; sus líneas son cerradas. **Ley de inducción:** Las variaciones temporales del flujo magnético producen un campo eléctrico rotacional. **Ley de Ampère:** Las corrientes y las variaciones temporales del campo eléctrico producen un campo magnético rotacional.

**Ejemplo.** El imán de la fig. [12](#abb-12) cambia el flujo a través de la bobina con $N=500$ de manera uniforme en 0,2 mWb en 25 ms. La tensión es entonces constante: $|U_\mathrm{ind}|=500\cdot0{,}2\,\mathrm{mWb}/25\,\mathrm{ms}=4$ V. Durante ese tiempo, la integral de $\vec E$ alrededor del flujo no es cero, y la tensión entre dos puntos depende de por qué lado del flujo pasa el camino.

⁠**Casos límite:** Con flujo constante, $u_\mathrm{ind}=0$; un imán en reposo no crea tensión. En la mayoría de los circuitos, los flujos variables están casi por completo en las bobinas. Entre los componentes, el campo sigue siendo prácticamente irrotacional; por eso los potenciales y las tensiones siguen siendo allí la herramienta.

:::frage ¿Por qué no se puede dar un potencial en un campo rotacional?
El potencial de un lugar es el trabajo por unidad de carga hasta el punto de referencia. En un campo rotacional depende del camino. Dos caminos dan dos valores, y el lugar no tendría un potencial único.
:::

:::aufgabe Ejercicio 11 ★ Inducción
<span class="anker" id="aufg-11"></span>

Una bobina de 200 espiras abarca un flujo que aumenta uniformemente 0,5 mWb en 10 ms. (a) ¿Cuál es el módulo de la tensión inducida? (b) Después, el flujo permanece constante. ¿Qué tensión hay ahora?

:::loesung
(a) $|U_\mathrm{ind}|=200\cdot0{,}5\,\mathrm{mWb}/10\,\mathrm{ms}=10$ V. (b) Cero, porque $\mathrm{d}\Phi/\mathrm{d} t=0$.
:::
:::
