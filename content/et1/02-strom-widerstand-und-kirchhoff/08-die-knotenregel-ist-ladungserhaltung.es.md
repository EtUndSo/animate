---
title: Etapa 7: La ley de los nudos es conservación de la carga
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Corriente, resistencia y leyes de Kirchhoff
order: 1120800
summary: El primer tipo de ecuación: ¿Qué exige la conservación de la carga en un nudo?
tags: 
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
El primer tipo de ecuación: ¿Qué exige la conservación de la carga en un nudo?
:::

**La idea.** Un nudo es un trozo de hilo. Si entra más de lo que sale, se acumula carga en él y su potencial sube. Con ello baja la tensión en las resistencias por las que entra corriente y sube en las resistencias por las que sale. La entrada disminuye y la salida aumenta hasta que ambas son iguales. Esta autorregulación transcurre en nanosegundos. Es el mecanismo detrás de la ley: el nudo se ajusta exactamente al potencial en el que nada queda retenido.

:::satz Teorema 7.1 (Ley de los nudos, primera ley de Kirchhoff)
<span class="anker" id="satz-7-1"></span>

La suma de todas las corrientes que entran en un nudo es cero en todo instante. De forma equivalente, la suma de las corrientes entrantes es igual a la suma de las salientes:

<span class="anker" id="gl-7-1"></span>
$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{(todas las flechas hacia el nudo)},\qquad\sum I_\mathrm{ent}=\sum I_\mathrm{sal}. \tag{7.1}$$

Para una red con $k$ nudos, $k-1$ de estas ecuaciones son independientes.
:::

⁠**Cómo leerlo:** Las flechas se eligen libremente. Si todas apuntan hacia el nudo, al menos una de las corrientes debe ser negativa, o todas son cero. Con flechas mixtas, las entrantes cuentan como positivas y las salientes como negativas. **Validez:** El nudo no debe almacenar una carga apreciable. Eso se cumple mientras las corrientes cambien lentamente en comparación con el tiempo de compensación. La deducción da un número para ello.

:::abbildung et1/k2knoten 8
Izquierda: nudo con dos corrientes entrantes y tres salientes, suma 7 mA en cada caso. Derecha: la ley también vale para una superficie alrededor de una parte de la red, aquí alrededor de $K_2$, $K_3$ y $R_\mathrm e$. La corriente en $R_\mathrm e$ queda dentro y no cuenta.
:::

:::herleitung La ley de los nudos a partir de la conservación de la carga
Para la carga $Q_\mathrm K$ del nudo se cumple $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$, porque la carga ni se crea ni desaparece. Una estimación con la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) muestra lo pequeña que queda $Q_\mathrm K$: una esfera metálica de 1 cm de radio tiene el potencial $\varphi=k_\mathrm C\,Q/r$ con la constante de Coulomb $k_\mathrm C=8{,}99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$. Para 9 V bastan $Q=10$ pC. Un exceso de 3 mA los aporta en 3,3 ns. Por eso $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ es despreciable frente a las corrientes, y queda $\sum I_\nu=0$.
:::

**Por qué sobra una ecuación.** Cada rama une dos nudos. Por eso su corriente aparece en exactamente dos ecuaciones de nudo, una vez con $+$ (entrante) y otra con $-$ (saliente). Si se suman las $k$ ecuaciones, todas las corrientes se cancelan. Una ecuación se deduce, pues, de las demás, y cualquier selección de $k-1$ ecuaciones es independiente.

**Ejemplo.** Todas las flechas de corriente de la red apuntan en el sentido de la corriente real: de $K_1$ hacia abajo a través de las resistencias, $I_\mathrm e$ de $K_2$ a $K_3$, $I_0$ a través de la fuente de $K_4$ a $K_1$. Las ecuaciones de nudo son

$$\begin{aligned} K_1:&\quad +I_0-I_\mathrm a-I_\mathrm c=0, & K_2:&\quad +I_\mathrm a-I_\mathrm b-I_\mathrm e=0,\\ K_3:&\quad +I_\mathrm c-I_\mathrm d+I_\mathrm e=0, & K_4:&\quad -I_0+I_\mathrm b+I_\mathrm d=0. \end{aligned}$$

La suma de las tres primeras es $I_0-I_\mathrm b-I_\mathrm d=0$, la cuarta ecuación con el signo contrario. Si solo se suman $K_2$ y $K_3$, desaparece $I_\mathrm e$ y queda la superficie de la fig. [8](#abb-8): $I_\mathrm a+I_\mathrm c=I_\mathrm b+I_\mathrm d$. **Comprobación:** En un punto con solo dos ramas se obtiene $I_1=I_2$. Por componentes en serie circula la misma corriente.

:::frage ¿Vale la ley también si en un nudo hay un condensador?
Sí. La corriente hacia la placa es una corriente de rama como cualquier otra; la carga no se acumula en el nudo, sino en la placa. La [Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) trata este caso.
:::

:::aufgabe Ejercicio 7 ★★ Aplicar la ley de los nudos
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Cuatro flechas de corriente apuntan hacia el nudo: $I_1=5$ mA, $I_2=-2$ mA, $I_3=-1$ mA. ¿Cuánto vale $I_4$ y en qué sentido circula realmente?

</li>

<li>

Demuestra a partir de las ecuaciones de nudo de la red que $I_0=I_\mathrm b+I_\mathrm d$. ¿Qué superficie corresponde a esto?

</li>

<li>

Predicción: Un exceso de solo 1 µ A se queda 1 s en la esfera de la deducción. ¿Qué potencial tendría? ¿Por qué no ocurre eso?

</li>

</ol>

:::loesung
(a) $5-2-1+I_4=0$, es decir, $I_4=-2$ mA: del nudo salen 2 mA.

(b) La suma de $K_1$, $K_2$, $K_3$ da $I_0-I_\mathrm b-I_\mathrm d=0$. Es la superficie alrededor de $K_1$, $K_2$, $K_3$ o, de forma equivalente, la ecuación de $K_4$. Con números: $4=1+3$.

(c) $Q=1\,\mu\text{C}$ da $\varphi=k_\mathrm C\,Q/r=0{,}9$ MV. Mucho antes de alcanzar este valor, el potencial creciente expulsa el exceso. Esa es la autorregulación.
:::
:::
