---
title: Etapa 10: Descarga y constante de tiempo
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El condensador
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Capítulo 3: El condensador
order: 1131100
summary: El condensador cargado devuelve su carga a través de una resistencia.
tags: 
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
El condensador cargado devuelve su carga a través de una resistencia. Es la misma ecuación con otro valor inicial. De ello se deduce una regla para todo proceso de conmutación en el circuito RC.
:::

**La idea.** El interruptor pasa de la posición 1 a la 2, y la batería queda desconectada. El condensador mantiene sus 9 V, porque no pueden saltar. Esta tensión está ahora en $R$. Los electrones de la placa negativa vuelven a través de $R$ a la positiva. Así pues, la corriente circula contra la flecha de referencia de la fig. [9](aufladen-uber-einen-widerstand.html#abb-9), y salta: hace un momento era cero, ahora es de $-0{,}9$ mA. Con cada carga que sale bajan la tensión y, con ella, la corriente. Al principio, el condensador actúa como una fuente cada vez más débil.

:::satz Teorema 10.1 (Descarga)
<span class="anker" id="satz-10-1"></span>

Sin batería, la ley de mallas dice $u_R+u_C=0$, es decir, $RC\,\mathrm{d} u_C/\mathrm{d} t+u_C=0$. Con $u_C(0)=U_0$ y $t\ge0$ se cumple

<span class="anker" id="gl-10-1"></span>
$$u_C(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad i(t)=-\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=-U_0\,\mathrm{e}^{-t/\tau}. \tag{10.1}$$
:::

En general, para todo proceso de conmutación en el circuito RC con fuente constante, la tensión va del valor inicial $u_C(0)$ al valor final $u_\infty$ según

<span class="anker" id="gl-10-2"></span>
$$u_C(t)=u_\infty+\bigl(u_C(0)-u_\infty\bigr)\,\mathrm{e}^{-t/\tau}. \tag{10.2}$$

⁠**Cómo leerlo:** El signo menos en $i$ indica: la corriente circula contra la flecha de referencia. $u_\infty$ es la tensión que el condensador alcanza tras mucho tiempo: $U_0$ al cargar, 0 al descargar. La diferencia respecto al valor final se reduce en cada tiempo $\tau$ al 36,8 %. **Validez:** $\tau$ se forma con la resistencia del camino de corriente correspondiente. Aquí, ambas posiciones tienen la misma $R$.

:::herleitung Regla general
Para la distancia $x=u_\infty-u_C$ se cumple, como en la etapa [9](aufladen-uber-einen-widerstand.html#stufe-9), $\mathrm{d} x/\mathrm{d} t=-x/\tau$. Los pasos 2 a 4 valen para cualquier signo de $x$ si se escribe $\ln|x|$, y dan $x(t)=x(0)\,\mathrm{e}^{-t/\tau}$. Sustituyendo $x(0)=u_\infty-u_C(0)$ se obtiene [(10.2)](#gl-10-2). Para $u_\infty=0$ resulta [(10.1)](#gl-10-1); para $u_\infty=U_0$ y $u_C(0)=0$ resulta [(9.3)](aufladen-uber-einen-widerstand.html#gl-9-3).
:::

**La constante de tiempo.** $\tau=RC$ es el tiempo tras el cual la corriente y la tensión restante han caído a $1/\mathrm{e}$. En la carga se ha alcanzado entonces el 63,2 %. La carga y la descarga se aceleran con una $C$ menor, porque hay que mover menos carga, y con una $R$ menor, porque circula más corriente. $U_0$ no aparece en $\tau$: el doble de tensión da el doble de corriente, pero también el doble de carga. La tabla vale para cualquier circuito RC; la última fila, para el modelo de referencia.

| Tiempo | $1\tau$ | $2\tau$ | $3\tau$ | $4\tau$ | $5\tau$ |
|---|---|---|---|---|---|
| Carga: $1-\mathrm{e}^{-t/\tau}$ en % | 63,2 | 86,5 | 95,0 | 98,2 | 99,3 |
| Descarga: $\mathrm{e}^{-t/\tau}$ en % | 36,8 | 13,5 | 5,0 | 1,8 | 0,7 |
| Carga: $u_C$ en V | 5,69 | 7,78 | 8,55 | 8,84 | 8,94 |

:::abbildung et1/k3entladen 12
Cinco segundos de carga, cinco segundos de descarga. La tensión es continua; los porcentajes se refieren al valor final en la carga y al valor inicial en la descarga. La corriente salta al conmutar y cambia de signo en la descarga; en trazo discontinuo, los saltos.
:::

::::beispiel
En el modelo de referencia, la descarga empieza en 9 V. En el primer instante, $u_R=-9$ V e $i=-0{,}9$ mA. Tras 1 s son $u_C=3{,}31$ V e $i=-0{,}331$ mA; tras 3 s quedan 0,448 V. Si solo se carga durante 5 s como en la fig. [12](#abb-12), la descarga empieza en 8,94 V.
::::

⁠**Comprobación:** La carga que pasa por $R$ en la descarga es $\int_0^\infty|i|\,\mathrm{d} t=\frac{U_0}{R}\,\tau=C\,U_0$, exactamente la carga almacenada. **Caso límite:** Para $u_C(0)=u_\infty$, el paréntesis de [(10.2)](#gl-10-2) es cero: no ocurre nada, el condensador ya está en su estado final.

:::frage ¿Por qué la corriente puede saltar al conmutar, pero la tensión no?
La tensión está ligada a la carga almacenada, y esta solo puede cambiar con corriente finita en un tiempo finito. La corriente no tiene ese almacén. Se deduce en cada instante de la tensión en $R$, y esta cambia al accionar el interruptor.
:::

:::ltspice Carga y descarga en el circuito RC
⁠**Esquema:** `voltage` de `in` a masa con `PULSE(0 9 0 1u 1u 5 10)`, `res` con `10k` de `in` a `out`, `cap` con `100u` de `out` a masa. La fuente sustituye al interruptor: 9 V durante 5 s, luego 0 V, es decir, un camino de vuelta a través de $R$.

⁠**Directivas:** `.tran 0 10 0 1m`, además de medidas como `.meas tran u1 FIND V(out) AT=1` para $t=1$, 2, 3, 5 y 6 s, así como `.meas tran i0 FIND I(R1) AT=10u`.

⁠**Lo que ves:** 5,69 V; 7,78 V; 8,55 V; 8,94 V en la carga, como en la tabla; en 6 s, 3,29 V, es decir, el 36,8 % de 8,94 V. Al inicio, `i0` $=0{,}90$ mA. Pon después 12 V, `4.7k` y `220u` y comprueba tus resultados del ejercicio [10](aufladen-uber-einen-widerstand.html#aufg-10).
:::

:::aufgabe Ejercicio 12 ★★ Valores iniciales y autodescarga
<span class="anker" id="aufg-12"></span>

Se tiene $R=10\,\mathrm{k\Omega}$, $C=100\,\mu\text{F}$ y $\tau=1$ s.

<ol class="al">

<li>

El condensador ya lleva 3 V cuando se conecta $U_0=9$ V. Indica $u_C(t)$ y calcula $u_C(1\,\mathrm{s})$.

</li>

<li>

¿Cuánto tarda en este caso $u_C$ en subir de 3 V a 6 V?

</li>

<li>

Descarga desde 9 V: ¿cuándo cae $u_C$ por debajo de 1 V?

</li>

<li>

El condensador cargado (9 V) está desconectado y solo lo descarga $R_\mathrm{I}=1\,\mathrm{M\Omega}$. ¿Cuánto vale $u_C$ tras un minuto?

</li>

</ol>

:::loesung
(a) Con [(10.2)](#gl-10-2), $u_\infty=9$ V y $u_C(0)=3$ V: $u_C(t)=9\,\mathrm{V}-6\,\mathrm{V}\cdot\mathrm{e}^{-t/\tau}$. Para $t=1$ s: 6,79 V.

(b) $6=9-6\,\mathrm{e}^{-t/\tau}$ da $\mathrm{e}^{-t/\tau}=\frac12$, es decir, $t=\tau\ln2=0{,}693$ s.

(c) $9\,\mathrm{e}^{-t/\tau}=1$ da $t=\tau\ln9=2{,}20$ s.

(d) La constante de tiempo es $R_\mathrm{I}\,C=100$ s, es decir, $u_C(60\,\mathrm{s})=9\,\mathrm{V}\cdot\mathrm{e}^{-0{,}6}=4{,}94$ V.
:::
:::
