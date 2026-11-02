---
title: Etapa 4: Pérdidas en la línea
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170500
summary: Entre la fuente y la carga está la línea, y también ella es una resistencia.
tags: caída de tensión, potencia de pérdidas, potencia útil, tensión nominal
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Entre la fuente y la carga está la línea, y también ella es una resistencia. Esta etapa muestra por qué las grandes potencias se transportan a tensiones altas.
:::

**La idea.** La línea está en serie con la carga; toda la corriente debe atravesarla (fig. [5](#abb-5)). Cada culombio pierde en ella $R_\mathrm{cable}I$ julios antes de llegar a la carga. Una potencia fija se puede transmitir de dos maneras: con tensión alta y corriente pequeña, o al revés. Con tensión alta, cada culombio aporta mucha energía, así que bastan pocos. La corriente pequeña ayuda por partida doble: cada culombio pierde menos, y hay menos culombios.

:::abbildung et1/k7leitung 5
Fuente, línea y carga. $R_\mathrm{cable}$ agrupa los conductores de ida y de vuelta. A la derecha, los dos casos del ejemplo.
:::

:::satz Teorema 4.1 (Pérdidas en la línea)
<span class="anker" id="satz-4-1"></span>

Si la corriente $I$ circula hacia la carga por una línea con $R_\mathrm{cable}$, se cumple

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{cable}=R_\mathrm{cable}\,I,\qquad P_\mathrm{cable}=U_\mathrm{cable}\,I=R_\mathrm{cable}\,I^2,\qquad P_\text{útil}=(U_\mathrm{q}-U_\mathrm{cable})\,I \tag{4.1}$$

y, por tanto,

<span class="anker" id="gl-4-2"></span>
$$\frac{P_\text{útil}}{P_\mathrm{q}}=\frac{(U_\mathrm{q}-U_\mathrm{cable})\,I}{U_\mathrm{q}\,I}=1-\frac{U_\mathrm{cable}}{U_\mathrm{q}}. \tag{4.2}$$

Para dos tensiones con la misma potencia en la carga $P_\mathrm{L}=U_\mathrm{L1}I_1=U_\mathrm{L2}I_2$ se cumple

<span class="anker" id="gl-4-3"></span>
$$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}},\qquad\frac{P_\mathrm{cable,1}}{P_\mathrm{cable,2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}. \tag{4.3}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{cable}$ es la __caída de tensión__ a lo largo de la línea. $P_\mathrm{cable}$ es la __potencia de pérdidas__; $P_\text{útil}=P_\mathrm{L}$, la __potencia útil__ de la carga; $P_\mathrm{q}=U_\mathrm{q}I$, la potencia de la fuente. $U_\mathrm{L}$ es la tensión en la carga. **Validez:** Las fórmulas valen para magnitudes continuas y para la resistencia de la línea. Con tensión alterna y carga óhmica valen con valores eficaces.

**Ejemplo.** La carga necesita 40 kW, $R_\mathrm{cable}=1\,\Omega$. Con $U_\mathrm{L}=400$ V son $I=100$ A, $U_\mathrm{cable}=100$ V y $P_\mathrm{cable}=10$ kW. La fuente debe suministrar 500 V y, según [(4.2)](#gl-4-2), llega $1-100/500=80$ %. Con 20 kV son $I=2$ A, $U_\mathrm{cable}=2$ V y $P_\mathrm{cable}=4$ W, y llega el 99,99 %. La corriente baja en un factor 50; la pérdida, en $50^2=2500$. **Caso límite:** Para $R_\mathrm{cable}\to0$ se tiene $U_\mathrm{cable}=0$, y [(4.2)](#gl-4-2) da 1. A distancias largas, la energía solo se puede transmitir con tensión alta; por eso la red eléctrica se construye en niveles. La __tensión nominal__ es la tensión para la que está diseñada una red:

| Nivel | Tensión nominal | Alcance | Función |
|---|---|---|---|
| Baja tensión | 230/400 V | varios 100 m | Hogares y comercios de la localidad |
| Media tensión | 10 kV | hasta unos 10 km | Distribución en grandes ciudades |
| Media tensión | 20 kV | hasta unos 25 km | Distribución en zonas rurales y ciudades medianas |
| Alta tensión | 110 kV | hasta unos 100 km | Alimentación de las redes de media tensión |
| Muy alta tensión | 220 kV, 380 kV | de varios 100 a más de 1000 km | Interconexión en el país y en Europa |

La alta tensión no se puede llevar hasta la vivienda: el aire se perfora a unos 3 kV/mm ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), por lo que las líneas aéreas necesitan distancias de varios metros. Los transformadores elevan la tensión alterna para el transporte y la reducen de nuevo antes de los consumidores.

:::frage Según $P=U^2/R$, la potencia crece con la tensión. ¿No deberían las tensiones altas traer más pérdidas?
La fórmula es correcta, pero necesita la tensión en la misma resistencia. En el ejemplo, el cable no tiene 20 kV, sino $U_\mathrm{cable}=2$ V, y $(2\,\mathrm{V})^2/1\,\Omega$ son los 4 W. La tensión alta está en la carga. $U_\mathrm{cable}$ baja porque baja la corriente.
:::

:::aufgabe Ejercicio 4 ★★ La cabaña al borde del bosque
<span class="anker" id="aufg-4"></span>

Una cabaña absorbe 480 W a 48 V de tensión continua, y la línea de alimentación tiene $R_\mathrm{cable}=0{,}2\,\Omega$. (a) Calcula $I$, $U_\mathrm{cable}$, $P_\mathrm{cable}$, $U_\mathrm{q}$ y la fracción que llega. (b) Lo mismo para 480 W a 12 V. (c) ¿Qué tensión $U_\mathrm{L}$ limita la pérdida al 1 % de la potencia en la carga?

:::loesung
(a) $I=480\,\mathrm{W}/48\,\mathrm{V}=10$ A, $U_\mathrm{cable}=2$ V, $P_\mathrm{cable}=20$ W, $U_\mathrm{q}=50$ V. Llega $1-2/50=96$ %. (b) $I=40$ A, $U_\mathrm{cable}=8$ V, $P_\mathrm{cable}=320$ W, $U_\mathrm{q}=20$ V. Solo llega el 60 %. Cuatro veces la corriente da dieciséis veces la pérdida. (c) $R_\mathrm{cable}\,P_\mathrm{L}^2/U_\mathrm{L}^2\le0{,}01\,P_\mathrm{L}$ da $U_\mathrm{L}\ge\sqrt{R_\mathrm{cable}\,P_\mathrm{L}/0{,}01}=98$ V.
:::
:::
