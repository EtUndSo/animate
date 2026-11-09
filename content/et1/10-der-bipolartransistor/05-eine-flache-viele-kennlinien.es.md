---
title: Etapa 3: Una superficie, muchas curvas características
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1200500
summary: Las hojas de datos muestran varias curvas características con ejes distintos.
tags: curva característica, sección, familia de curvas, Curva característica de entrada, Curva característica de control, Curva característica de control por corriente, Curva característica de salida, curva característica de transferencia
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Las hojas de datos muestran varias curvas características con ejes distintos. Esta etapa las reduce a un solo objeto.
:::

**La idea.** $I_\mathrm{C}$ depende de dos tensiones. Una función de dos variables es una superficie, como un terreno sobre un mapa: el mapa tiene las direcciones $U_\mathrm{BE}$ y $U_\mathrm{CE}$, y la altura del terreno es $I_\mathrm{C}$ (fig. [3](#abb-3)). Una __curva característica__ (relación entre dos magnitudes, [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) aparece cuando se mantiene fija una tensión: una __sección__ del terreno. Varias secciones paralelas dan una __familia de curvas__. Así pues, no hay muchas dependencias, sino un solo terreno con varias vistas. En la dirección de $U_\mathrm{BE}$ es una ladera empinada (rojo); en la dirección de $U_\mathrm{CE}$, un borde y luego un plano casi horizontal (verde).

:::abbildung et1/k10flaeche 3
La superficie $I_\mathrm{C}(U_\mathrm{BE},U_\mathrm{CE})$ del modelo de referencia. Rojo: sección a $U_\mathrm{CE}=6$ V, exponencial. Verde: sección a $U_\mathrm{BE}=0{,}6$ V, primero abrupta y luego casi horizontal. Ambas se encuentran en el punto de trabajo.
:::

:::satz Teorema 3.1 (La superficie del modelo)
<span class="anker" id="satz-3-1"></span>

Para $U_\mathrm{BE}\gg U_T$ y $U_\mathrm{CE}\ge0$, en el modelo de referencia se cumple

<span class="anker" id="gl-3-1"></span>
$$I_\mathrm{C}=\underbrace{I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}}_{\text{inyección}}\cdot\underbrace{\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)}_{\text{recogida}}\cdot\underbrace{\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)}_{\text{pequeña pendiente}},\qquad I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}. \tag{3.1}$$
:::

⁠**Cómo leerlo:** El primer factor es [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1). El segundo tiende a 1 en cuanto el colector está unos pocos $U_T$ por encima del emisor: cuenta cuántos electrones devuelve el colector, que son el 15 % con $U_\mathrm{CE}=0{,}05$ V, aún el 2 % con 0,1 V y solo el 0,05 % con 0,2 V. El tercer factor describe el ligero aumento con $U_\mathrm{CE}$ (etapa [9](tangente-statt-kurve.html#stufe-9)). $I_\mathrm{S}$ y $B$ valen para $U_\mathrm{CE}=6$ V. **Validez:** un modelo para corrientes pequeñas y medianas.

:::herleitung El factor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$
La corriente de electrones por la base es proporcional al gradiente de densidad entre sus dos bordes. Cada borde sigue la tensión de su frontera: $\mathrm{e}^{U_\mathrm{BE}/U_T}$ en el emisor, $\mathrm{e}^{U_\mathrm{BC}/U_T}$ en el colector, con $U_\mathrm{BC}=-U_\mathrm{CB}=U_\mathrm{BE}-U_\mathrm{CE}$ según [(1.1)](drei-schichten-zwei-spannungen.html#gl-1-1). Por tanto, $I_\mathrm{C}\sim\mathrm{e}^{U_\mathrm{BE}/U_T}-\mathrm{e}^{(U_\mathrm{BE}-U_\mathrm{CE})/U_T}=\mathrm{e}^{U_\mathrm{BE}/U_T}(1-\mathrm{e}^{-U_\mathrm{CE}/U_T})$. La función exponencial en $U_\mathrm{BE}$ y el borde en $U_\mathrm{CE}$ son dos caras de una misma diferencia.
:::

:::abbildung et1/k10schnitte 4
Cuatro secciones de la ecuación [(3.1)](#gl-3-1). Izquierda, curvas características de entrada y de control a $U_\mathrm{CE}=6$ V: la misma forma, con el eje $I_\mathrm{B}$ a una escala distinta en un factor 200. Centro, curvas características de salida para $I_\mathrm{B}=5$ a 20 µ A; en trazos, el límite $U_\mathrm{CE}=U_\mathrm{BE}$. Derecha, curva característica de control por corriente con pendiente $B$.
:::

| Curva característica | se fija | ejes | forma y motivo |
|---|---|---|---|
| __Curva característica de entrada__ | $U_\mathrm{CE}$ | $I_\mathrm{B}$ sobre $U_\mathrm{BE}$ | Diodo, codo hacia 0,6 V: la frontera BE es un diodo |
| __Curva característica de control__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ sobre $U_\mathrm{BE}$ | Misma forma, $B$ veces más alta: inyección |
| __Curva característica de control por corriente__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ sobre $I_\mathrm{B}$ | Recta de pendiente $B$: la función exponencial se cancela |
| __Curva característica de salida__ | $U_\mathrm{BE}$ o $I_\mathrm{B}$ | $I_\mathrm{C}$ sobre $U_\mathrm{CE}$ | Abrupta y luego casi plana como una fuente de corriente: recogida |

La curva característica de control por corriente se llama también __curva característica de transferencia__. Con corrientes muy grandes se aplana y $B$ disminuye: la base está entonces tan llena de electrones que el cálculo sencillo deja de valer. El límite $U_\mathrm{CE}=U_\mathrm{BE}$ de la fig. [4](#abb-4) es el lugar $U_\mathrm{CB}=0$. A su izquierda, el diodo CB ya conduce débilmente, pero la curva solo se dobla por debajo de unos 0,2 V.

::::beispiel
Sección a $U_\mathrm{CE}=6$ V: 0,582 V, 0,600 V y 0,618 V dan 1,0 mA, 2,0 mA y 4,0 mA. Sección a $U_\mathrm{BE}=0{,}6$ V: $U_\mathrm{CE}=0{,}05$ V; 0,2 V; 6 V; 14 V dan 1,58 mA; 1,85 mA; 2,00 mA; 2,20 mA.
::::

⁠**Caso límite:** para $U_\mathrm{CE}=0$ es $I_\mathrm{C}=0$: los dos bordes de la base están a la misma altura y no hay gradiente.

:::frage Entonces, ¿la corriente depende de $U_\mathrm{CE}$ o no?
Sí, pero con fuerza muy distinta. Mucho hasta 0,2 V, y después alrededor de un 1 % por voltio. Como comparación: 1 mV en $U_\mathrm{BE}$ produce un 3,9 %. «Depende» no significa «depende con la misma fuerza». El terreno tiene pendiente en ambas direcciones, solo que muy distinta.
:::

:::ltspice La familia de curvas características de salida
⁠**Esquema:** `npn` con el nombre de modelo `T`, emisor a masa, en el colector `voltage` llamada `VCE`, en la base `current` con `{IB0}` de masa a la base.

⁠**Directivas:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.param IB0=10u`, `.step param IB0 list 5u 10u 15u 20u`, `.dc VCE 0 12 0.02`. A 6 V y 27 °C, estos parámetros dan los valores de T, porque LTspice cuenta $B$ e $I_\mathrm{S}$ con $U_\mathrm{CB}=0$.

⁠**Lo que ves:** Cuatro curvas en `Ic(Q1)`, abruptas hasta 0,2 V y luego ligeramente crecientes. Con $I_\mathrm{B}=10$ µ A, LTspice muestra 1,996 mA a 6 V y 2,147 mA a 12 V; el cálculo da 2,00 mA y 2,15 mA. Compara con el ejercicio [3](#aufg-3).
:::

:::aufgabe Ejercicio 3 ★ Leer secciones
<span class="anker" id="aufg-3"></span>

(a) Determina con [(3.1)](#gl-3-1) $I_\mathrm{C}$ a $U_\mathrm{BE}=0{,}6$ V para $U_\mathrm{CE}=0{,}1$ V y 12 V. ¿Qué curva característica estás calculando? (b) Determina $I_\mathrm{C}$ a $U_\mathrm{CE}=6$ V para $U_\mathrm{BE}=0{,}56$ V y 0,62 V. ¿Qué curva característica es esta? (c) Predice: ¿qué aspecto tiene la curva $I_\mathrm{C}(I_\mathrm{B})$ a $U_\mathrm{CE}=0{,}05$ V, comparada con la de 6 V?

:::loesung
(a) $1{,}81$ mA y $2{,}15$ mA, una sección a $U_\mathrm{BE}$ fija: curva característica de salida. (b) 0,43 mA y 4,32 mA, una sección a $U_\mathrm{CE}$ fija: curva característica de control. 60 mV dan el factor 10. (c) De nuevo una recta que pasa por el origen, solo que más plana. $I_\mathrm{B}$ en [(3.1)](#gl-3-1) no depende de $U_\mathrm{CE}$, y los otros dos factores son constantes a $U_\mathrm{CE}$ fija: $0{,}854\cdot0{,}926=0{,}79$, la pendiente es 158 en lugar de 200.
:::
:::
