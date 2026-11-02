---
title: Etapa 1: Tres capas, dos tensiones
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1200300
summary: Un diodo tiene dos terminales y una curva característica.
tags: transistor npn, diodo BE, diodo CB, transistor pnp, símbolo eléctrico, corriente de colector, corriente de base, corriente de emisor
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Un diodo tiene dos terminales y una curva característica. El transistor tiene tres terminales. Esta etapa aclara su estructura y cuenta cuántas magnitudes son libres.
:::

**La idea.** Un __transistor npn__ consta de tres zonas del mismo semiconductor: emisor dopado n, base dopada p, colector dopado n (fig. [1](#abb-1)). El emisor es el más dopado, para que pueda ceder muchos electrones. El colector es el menos dopado, para que su zona de carga espacial sea ancha y soporte tensiones altas. La base está en medio y es muy estrecha, de alrededor de 1 µ m. Así se forman dos uniones pn que comparten la base: el __diodo BE__ y el __diodo CB__. En funcionamiento normal, el diodo BE conduce y el diodo CB bloquea. Si se intercambian n y p, se obtiene el __transistor pnp__ (etapa [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)). En el __símbolo eléctrico__, el símbolo del esquema, el emisor es el terminal con la flecha. La flecha indica el sentido de la corriente convencional.

:::abbildung et1/k10aufbau 1
Izquierda: transistor npn como secuencia de capas y como símbolo eléctrico con todas las flechas de referencia. Derecha: transistor pnp con la secuencia de capas invertida. Allí la flecha del emisor apunta hacia el interior del componente, y todas las corrientes y tensiones se invierten.
:::

:::definition Definición 1.1 (Corrientes y tensiones en el transistor npn)
<span class="anker" id="satz-1-1"></span>

$I_\mathrm{B}$ e $I_\mathrm{C}$ se cuentan hacia el interior del componente, $I_\mathrm{E}$ hacia fuera. Las tensiones son diferencias de potencial, y el primer índice es el polo positivo: $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$. Siempre se cumple

<span class="anker" id="gl-1-1"></span>
$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}. \tag{1.1}$$
:::

⁠**Cómo leerlo:** $I_\mathrm{C}$ es la __corriente de colector__, de microamperios a amperios según el tipo. $I_\mathrm{B}$ es la __corriente de base__, mucho menor, e $I_\mathrm{E}$ la __corriente de emisor__. $U_\mathrm{BE}$ cae en el diodo BE, alrededor de 0,6 V. $U_\mathrm{CE}$ va de unos 0,2 V hasta varias decenas de voltios. $U_\mathrm{CB}$ es la tensión inversa del diodo CB. **Validez:** las leyes de los nudos y de las mallas se cumplen en todo estado de funcionamiento.

:::herleitung Cuántas magnitudes son libres
Un componente con $n$ terminales tiene $n$ corrientes. No almacena carga, así que la ley de los nudos ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) elimina una corriente. Tiene $n$ potenciales, pero solo cuentan las diferencias, así que quedan $n-1$ tensiones. El diodo ($n=2$) tiene una tensión, una corriente y una curva. El transistor ($n=3$) tiene dos tensiones y dos corrientes. Su interior las relaciona mediante dos ecuaciones,

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE}).$$

Es, por tanto, un cuadripolo ([Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) cuyas dos puertas comparten el emisor.
:::

**Ejemplo.** En el modelo de referencia, $\varphi_\mathrm{E}=0$, $\varphi_\mathrm{B}=0{,}6$ V, $\varphi_\mathrm{C}=6$ V. Con ello, $U_\mathrm{BE}=0{,}6$ V, $U_\mathrm{CE}=6$ V y $U_\mathrm{CB}=5{,}4$ V. El diodo BE conduce porque su lado p está más alto. El diodo CB bloquea porque su lado n está 5,4 V más alto. De $I_\mathrm{C}=2$ mA e $I_\mathrm{B}=10$ µ A se deduce $I_\mathrm{E}=2{,}01$ mA. **Caso límite:** para $U_\mathrm{CB}=0$ es $U_\mathrm{CE}=U_\mathrm{BE}$. Ahí termina el funcionamiento normal.

:::frage ¿Puedo soldar un transistor con dos diodos?
No. La imagen equivalente de dos diodos solo muestra la polaridad de las fronteras. En dos diodos separados, cada electrón se recombina mucho antes de alcanzar la segunda capa de bloqueo, y el diodo bloqueado sigue bloqueado. El efecto transistor solo aparece porque las dos fronteras están más cerca entre sí que la distancia que un electrón sobrevive en la zona p.
:::

:::aufgabe Ejercicio 1 ★ Del potencial a la tensión
<span class="anker" id="aufg-1"></span>

Respecto a masa se miden $\varphi_\mathrm{E}=1{,}2$ V, $\varphi_\mathrm{B}=1{,}85$ V y $\varphi_\mathrm{C}=7$ V, además de $I_\mathrm{B}=15$ µ A e $I_\mathrm{C}=3$ mA. (a) Determina $U_\mathrm{BE}$, $U_\mathrm{CE}$, $U_\mathrm{CB}$ y comprueba [(1.1)](#gl-1-1). (b) ¿Cuánto vale $I_\mathrm{E}$? (c) ¿A qué valor debe bajar $\varphi_\mathrm{C}$ para que $U_\mathrm{CB}=0$?

:::loesung
(a) $U_\mathrm{BE}=0{,}65$ V, $U_\mathrm{CE}=5{,}8$ V, $U_\mathrm{CB}=5{,}15$ V. Comprobación: $5{,}15\,\mathrm{V}+0{,}65\,\mathrm{V}=5{,}8$ V. (b) $I_\mathrm{E}=3{,}015$ mA. (c) $U_\mathrm{CB}=0$ significa $\varphi_\mathrm{C}=\varphi_\mathrm{B}=1{,}85$ V.
:::
:::
