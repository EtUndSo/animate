---
title: Etapa 5: Adónde va la potencia de una fuente
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170600
summary: También la fuente tiene una resistencia en su interior.
tags: 
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
También la fuente tiene una resistencia en su interior. Esta etapa establece el balance y define el rendimiento.
:::

**La idea.** En la fuente, cada culombio recibe la energía $U_\mathrm{q}$ en julios, porque la química lo empuja contra el campo hacia el potencial más alto. Una parte $U_\mathrm{Ri}$ la pierde en $R_\mathrm{i}$ como calor; el resto $U_\mathrm{L}$ lo cede en la carga (fig. [6](#abb-6)). Entonces está de nuevo en el punto de partida. Todos los culombios dan la misma vuelta, de modo que la relación entre las tensiones determina qué fracción de la potencia llega.

:::abbildung et1/k7kreis 6
A la izquierda, la fuente con la carga. A la derecha, el potencial de una carga eléctrica en la vuelta para $R_\mathrm{L}=16\,\Omega$, con B como punto de referencia. La fuente la eleva 9 V, $R_\mathrm{i}$ toma 1 V y la carga conectada 8 V.
:::

:::definition Definición 5.1 (Balance de potencia y rendimiento)
<span class="anker" id="satz-5-1"></span>

En el circuito con $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$ se cumple

<span class="anker" id="gl-5-1"></span>
$$P_\mathrm{q}=U_\mathrm{q}\,I,\qquad P_\mathrm{v}=U_\mathrm{Ri}\,I=I^2R_\mathrm{i},\qquad P_\mathrm{L}=U_\mathrm{L}\,I=I^2R_\mathrm{L},\qquad P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}. \tag{5.1}$$

El rendimiento es la potencia aprovechada referida a la potencia total empleada por la fuente:

<span class="anker" id="gl-5-2"></span>
$$\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac{I\,U_\mathrm{L}}{I\,U_\mathrm{q}}=\frac{U_\mathrm{L}}{U_\mathrm{q}}=\frac{R_\mathrm{L}}{R_\mathrm{L}+R_\mathrm{i}}=\frac{R_\mathrm{L}/R_\mathrm{i}}{1+R_\mathrm{L}/R_\mathrm{i}}. \tag{5.2}$$
:::

⁠**Cómo leerlo:** $P_\mathrm{q}$ es la potencia que genera la fuente; $P_\mathrm{v}$, la potencia de pérdidas en su resistencia interna; $P_\mathrm{L}$, la potencia útil. $U_\mathrm{Ri}=R_\mathrm{i}I$ es la tensión en $R_\mathrm{i}$. $\eta$ es un número puro entre 0 y 1 y solo depende de la relación $R_\mathrm{L}/R_\mathrm{i}$. **Validez:** Esto vale para la conexión en serie de fuente ideal, $R_\mathrm{i}$ y $R_\mathrm{L}$. En una fuente equivalente, las magnitudes internas no son correctas (etapa [7](warum-50-und-welches-ziel-gilt.html#stufe-7)).

:::herleitung El balance es la ley de las mallas multiplicada por la corriente
La ley de las mallas dice $U_\mathrm{q}=U_\mathrm{Ri}+U_\mathrm{L}$. Multiplicada por $I$ da $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$. En [(5.2)](#gl-5-2) se simplifica $I$, porque ambas resistencias llevan la misma corriente. El divisor de tensión ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) da $U_\mathrm{L}=U_\mathrm{q}\,R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$.
:::

::::beispiel
La batería con cuatro cargas:

| $R_\mathrm{L}$ en $\Omega$ | $I$ en A | $U_\mathrm{L}$ en V | $P_\mathrm{L}$ en W | $P_\mathrm{v}$ en W | $P_\mathrm{q}$ en W | $\eta$ |
|---|---|---|---|---|---|---|
| 0,5 | 3,6 | 1,8 | 6,48 | 25,92 | 32,4 | 20 % |
| 2 | 2,25 | 4,5 | 10,125 | 10,125 | 20,25 | 50 % |
| 8 | 0,9 | 7,2 | 6,48 | 1,62 | 8,1 | 80 % |
| 16 | 0,5 | 8 | 4 | 0,5 | 4,5 | 88,9 % |
::::

⁠**Casos límite:** En cortocircuito, $R_\mathrm{L}=0$, $\eta=0$: la carga se queda fría, y toda la potencia $P_\mathrm{q}=40{,}5$ W calienta $R_\mathrm{i}$. En circuito abierto, $R_\mathrm{L}\to\infty$, $\eta\to1$, pero $I\to0$ y, con ello, $P_\mathrm{L}\to0$.

:::frage El rendimiento sigue subiendo con $R_\mathrm{L}$. ¿Por qué no se hace la carga arbitrariamente grande?
Porque $\eta$ es una fracción y no una cantidad. Con $R_\mathrm{L}$ grande, cada culombio cede casi todo en la carga, pero apenas llegan culombios. La tabla lo muestra: de 8 $\Omega$ a 16 $\Omega$, $\eta$ sube y la potencia $P_\mathrm{L}$ baja.
:::

:::aufgabe Ejercicio 5 ★ Establecer el balance
<span class="anker" id="aufg-5"></span>

Una fuente tiene $U_\mathrm{q}=12$ V y $R_\mathrm{i}=3\,\Omega$. (a) Calcula para $R_\mathrm{L}=9\,\Omega$ todas las magnitudes de [(5.1)](#gl-5-1) y $\eta$. (b) ¿Qué carga da $\eta=90$ %, y qué llega entonces? (c) ¿Qué ocurre en cortocircuito?

:::loesung
(a) $I=12\,\mathrm{V}/12\,\Omega=1$ A, $U_\mathrm{Ri}=3$ V, $U_\mathrm{L}=9$ V, $P_\mathrm{q}=12$ W, $P_\mathrm{v}=3$ W, $P_\mathrm{L}=9$ W, $\eta=75$ %. (b) $R_\mathrm{L}/(R_\mathrm{L}+3\,\Omega)=0{,}9$ da $R_\mathrm{L}=27\,\Omega$, $I=0{,}4$ A, $P_\mathrm{L}=4{,}32$ W. (c) $I_\mathrm{CC}=4$ A, los 48 W se generan todos en $R_\mathrm{i}$, $\eta=0$.
:::
:::
