---
title: Etapa 10: Conexión en paralelo, divisor de corriente y carga
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Corriente, resistencia y leyes de Kirchhoff
order: 1121100
summary: El segundo patrón básico: resistencias una junto a otra.
tags: conexión en paralelo, divisor de corriente, resistencia de carga
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
El segundo patrón básico: resistencias una junto a otra. Con él se puede responder qué ocurre con un divisor de tensión del que se extrae corriente.
:::

**La idea.** Todas las resistencias están conectadas a los mismos dos nudos, es decir, a la misma tensión. Cada resistencia adicional abre un camino adicional, y la ley de los nudos suma las corrientes. Por eso se suman las conductancias, igual que se suman las secciones de hilos colocados uno junto a otro.

:::satz Teorema 10.1 (Conexión en paralelo y divisor de corriente)
<span class="anker" id="satz-10-1"></span>

Para $N$ resistencias en __conexión en paralelo__ se cumple

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} U&=U_1=\dots=U_N,\qquad I=I_1+\dots+I_N,\qquad I_i=G_i\,U=\frac{U}{R_i},\\ G_\mathrm{tot}&=\frac{1}{R_\mathrm{tot}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i},\qquad R_\mathrm{tot}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}. \end{aligned} \tag{10.1|10.2}$$

Para dos resistencias se escribe $R_1\parallel R_2$:

<span class="anker" id="gl-10-3"></span>
$$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2},\qquad I_1=I_\mathrm{tot}\,\frac{G_1}{G_1+G_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2},\quad I_2=I_\mathrm{tot}\,\frac{G_2}{G_1+G_2}. \tag{10.3}$$
:::

⁠**Cómo leerlo:** Las corrientes se reparten en la relación de las conductancias: es el __divisor de corriente__. En la expresión de $I_1$ aparece arriba $R_2$: la corriente prefiere la resistencia menor. **Validez:** Ambas resistencias están entre los mismos dos nudos, y los conductores de conexión son ideales.

:::herleitung Conductancia total y divisor de corriente
La ley de los nudos da $I=\sum I_i$; con la misma $U$, por tanto, $I=(G_1+\dots+G_N)\,U$. Para dos ramas, $U=I_\mathrm{tot}/(G_1+G_2)$ y, con ello, $I_1=G_1\,U$. Con $G=1/R$ resulta

$$I_1=I_\mathrm{tot}\,\frac{1/R_1}{1/R_1+1/R_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2}.$$
:::

**Ejemplo.** $R_1$ y $R_2$ de la cadena en paralelo a 9 V: $G_\mathrm{tot}=0{,}5+1=1{,}5$ mS, es decir, $R_\mathrm{tot}=667\,\Omega$, menos que el valor menor, e $I=13{,}5$ mA. El divisor de corriente da $I_1=13{,}5\,\mathrm{mA}\cdot1/3=4{,}5$ mA, $I_2=9$ mA. Las redes mixtas se agrupan de dentro hacia fuera: $6\,\mathrm{k\Omega}$ en paralelo con $1\,\mathrm{k\Omega}+2\,\mathrm{k\Omega}$ da $6\parallel3=2\,\mathrm{k\Omega}$. **Casos límite:** $R_2\to\infty$ da $R_1$: la rama abierta no cuenta. $R_2\to0$ da 0: el cortocircuito se lleva toda la corriente. $R_1=R_2$ da $R_1/2$.

**El divisor de tensión con carga.** La tensión de un divisor debe alimentar otra etapa del circuito; la __resistencia de carga__ $R_\mathrm L$ queda en paralelo con $R_2$ (fig. [11](#abb-11)). El mecanismo: en el nudo central se abre un camino adicional, la resistencia total baja, la corriente por $R_1$ sube, en $R_1$ cae más tensión y el potencial central baja. Con $R_2'=R_2\parallel R_\mathrm L$ en [(9.3)](reihenschaltung-und-spannungsteiler.html#gl-9-3):

<span class="anker" id="gl-10-4"></span>
$$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}=\frac{R_2\,R_\mathrm L}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L},\quad I_\mathrm L=\frac{U_2}{R_\mathrm L}=\frac{U\,R_2}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}. \tag{10.4}$$

⁠**Casos límite:** $R_\mathrm L\to\infty$ da $I_\mathrm L\to0$ y la regla sin carga. $R_\mathrm L=R_2$ da $U_2/U=R_2/(2R_1+R_2)=\frac12R_2/(R_1+\frac12R_2)$.

:::abbildung et1/k2belastung 11
Izquierda: divisor de tensión con carga. Derecha: $U_2$ frente a $R_\mathrm L$ para $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$, $U=9$ V, según [(10.4)](#gl-10-4). Con $R_\mathrm L=1\,\mathrm{k\Omega}$ quedan 1,8 V; con $10\,\mathrm{k\Omega}$ son 2,81 V. Solo muy por encima de $R_1\parallel R_2=667\,\Omega$ la carga es imperceptible.
:::

**Ejemplo.** Para la cadena, el error relativo $\delta=(U_{2,0}-U_2)/U_{2,0}$ respecto a los 3 V sin carga es: $R_\mathrm L=1\,\mathrm{k\Omega}$ da 40 %, $10\,\mathrm{k\Omega}$ da 6,3 %, $100\,\mathrm{k\Omega}$ da 0,66 %. El error es $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ con $R_\mathrm i=R_1\parallel R_2$ (ejercicio [11](#aufg-11)). El divisor actúa, pues, como una fuente con la resistencia interna $R_\mathrm i$ ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

:::ltspice Medir la carga
⁠**Esquema:** fuente `voltage` con `9` de `in` a masa, `res` `R1 2k` de `in` a `mid`, `R2 1k` de `mid` a masa, `RL` con valor `{RL}` de `mid` a masa.

⁠**Directivas:** `.step param RL list 1k 2k 6k 10k 100k`, `.tran 1m`, `.meas tran u2 FIND V(mid) AT=1m`.

⁠**Lo que ves:** El SPICE Error Log da $U_2$ para cada paso: 1,80 V; 2,25 V; 2,70 V; 2,81 V; 2,98 V. Compara el valor para $6\,\mathrm{k\Omega}$ con el ejercicio [11](#aufg-11)(b).
:::

**Aplicación: escalera R-2R.** El divisor de corriente sustenta un segundo convertidor D/A (fig. [12](#abb-12)). El truco es la autosemejanza: en el último nudo hay $2R\parallel2R=R$. Con la $R$ anterior, eso vuelve a dar $2R$. Así, cada nudo ve $2R$ hacia la derecha y $2R$ hacia abajo, su corriente se reparte 1:1, y de nudo a nudo la tensión se reduce a la mitad (divisor de $R$ y $2R\parallel2R$). La fuente entrega $I_\mathrm{ref}=U_\mathrm{ref}/R$, y surgen las corrientes con peso binario $I_\mathrm{ref}/2$, $I_\mathrm{ref}/4$, $I_\mathrm{ref}/8$, etc. Un circuito exterior ([Parte 11](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) mantiene la barra colectora al potencial de masa. Por eso, todas las $2R$ ven abajo el mismo potencial, tanto si conmutan a la barra como a masa, y las corrientes no cambian al conmutar. El bit cercano a la fuente es el más significativo (MSB, most significant bit); el del final, el menos significativo (LSB). $I_\mathrm{sal}$ es la suma de las corrientes conectadas.

:::abbildung et1/k2r2r 12
Escalera R-2R con $R=1\,\mathrm{k\Omega}$ a $U_\mathrm{ref}=8$ V. En rojo, las tensiones de nudo; en azul, las corrientes de rama. Los interruptores están en el número 1010: hacia la barra colectora van $4\,\mathrm{mA}+1\,\mathrm{mA}=5$ mA.
:::

:::frage ¿Cómo puede bajar la resistencia si se añade otra?
Aquí, «más resistencias» significa más caminos. La rama existente sigue llevando la misma corriente, y la nueva lleva corriente adicional. Con la misma tensión circula más en total, así que $U/I$ es menor.
:::

:::aufgabe Ejercicio 10 ★★ En paralelo y mixto
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calcula $R_\mathrm{tot}$ para $2$, $3$ y $6\,\mathrm{k\Omega}$ en paralelo, y todas las corrientes con 12 V.

</li>

<li>

10 mA se reparten entre $1\,\mathrm{k\Omega}$ y $9\,\mathrm{k\Omega}$. ¿Cuánto valen ambas corrientes?

</li>

<li>

$1\,\mathrm{k\Omega}$ está en serie con $4\,\mathrm{k\Omega}\parallel(1\,\mathrm{k\Omega}+3\,\mathrm{k\Omega})$ a 9 V. Determina $R_\mathrm{tot}$ y todas las corrientes.

</li>

</ol>

:::loesung
(a) $G_\mathrm{tot}=0{,}5+0{,}333+0{,}167=1$ mS, es decir, $R_\mathrm{tot}=1\,\mathrm{k\Omega}$. Corrientes 6, 4 y 2 mA, suma 12 mA. (b) $I_1=10\,\mathrm{mA}\cdot9/10=9$ mA, $I_2=1$ mA. La resistencia pequeña lleva nueve veces más. (c) $1+3=4\,\mathrm{k\Omega}$, $4\parallel4=2\,\mathrm{k\Omega}$, $R_\mathrm{tot}=3\,\mathrm{k\Omega}$. Corriente total 3 mA, 1,5 mA en cada una de las dos ramas iguales.
:::
:::

:::aufgabe Ejercicio 11 ★★★ Dominar la carga
<span class="anker" id="aufg-11"></span>

El divisor es $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$ a 9 V.

<ol class="al">

<li>

Demuestra a partir de [(10.4)](#gl-10-4) que $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ con $R_\mathrm i=R_1\parallel R_2$.

</li>

<li>

¿Qué $R_\mathrm L$ da $\delta=10\,\%$? ¿Cuánto vale entonces $U_2$?

</li>

<li>

Un divisor de $200\,\Omega$ y $100\,\Omega$ tiene la misma relación. Calcula $U_2$ con $R_\mathrm L=1\,\mathrm{k\Omega}$. ¿Qué cuesta la mejor tensión?

</li>

<li>

Caso límite: ¿Cuánto vale $I_\mathrm L$ para $R_\mathrm L\to0$ con el divisor original?

</li>

</ol>

:::loesung
(a) Sin carga, $U_{2,0}=U\,R_2/(R_1+R_2)$. De [(10.4)](#gl-10-4) se obtiene

$$\frac{U_2}{U_{2,0}}=\frac{R_\mathrm L\,(R_1+R_2)}{R_1R_2+R_\mathrm L\,(R_1+R_2)}=\frac{R_\mathrm L}{R_\mathrm i+R_\mathrm L},\qquad\delta=1-\frac{U_2}{U_{2,0}}=\frac{R_\mathrm i}{R_\mathrm i+R_\mathrm L}.$$

(b) $\delta=0{,}1$ da $R_\mathrm L=9\,R_\mathrm i=6\,\mathrm{k\Omega}$ y $U_2=2{,}7$ V.

(c) $R_\mathrm i=66{,}7\,\Omega$, $U_2=2{,}81$ V, el mismo error que antes con $10\,\mathrm{k\Omega}$. A cambio, por el divisor circulan 30 mA en lugar de 3 mA, y convierte 270 mW en lugar de 27 mW.

(d) $R_\mathrm L\to0$ cortocircuita $R_2$: $I_\mathrm L=9\,\mathrm{V}/2\,\mathrm{k\Omega}=4{,}5$ mA.
:::
:::

:::aufgabe Ejercicio 12 ★★★ Escalera R-2R
<span class="anker" id="aufg-12"></span>

Una escalera de cuatro nudos como la de la fig. [12](#abb-12) tiene $R=10\,\mathrm{k\Omega}$ y $U_\mathrm{ref}=5$ V.

<ol class="al">

<li>

¿Qué resistencia ve la fuente? ¿Cuánto valen $I_\mathrm{ref}$ y las tensiones de nudo?

</li>

<li>

¿Cuánto valen las cuatro corrientes por las $2R$ superiores?

</li>

<li>

¿Cuánto vale $I_\mathrm{sal}$ con el número 1001, y cuánto el escalón más pequeño?

</li>

</ol>

:::loesung
(a) La fuente ve $2R\parallel2R=R=10\,\mathrm{k\Omega}$, es decir, $I_\mathrm{ref}=0{,}5$ mA. Tensiones de nudo 5; 2,5; 1,25; 0,625 V. (b) 0,25; 0,125; 0,0625; 0,03125 mA. (c) Número 1001: $0{,}25+0{,}03125=0{,}281$ mA. El escalón más pequeño es de 31,25 µ A.
:::
:::
