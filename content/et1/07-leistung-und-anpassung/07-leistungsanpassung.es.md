---
title: Etapa 6: Adaptación de potencia
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170700
summary: La tabla muestra un máximo de P L .
tags: potencia de cortocircuito
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
La tabla muestra un máximo de $P_\mathrm{L}$. Esta etapa lo encuentra y explica por qué está justo en $R_\mathrm{L}=R_\mathrm{i}$.
:::

**La idea.** Dos influencias actúan en sentidos opuestos. Con $R_\mathrm{L}$ pequeña llegan muchos culombios, pero casi toda su energía se queda en $R_\mathrm{i}$. Con $R_\mathrm{L}$ grande, cada culombio cede casi todo en la carga, pero llegan pocos. La recta $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ de la [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) lo hace visible: $P_\mathrm{L}=U_\mathrm{L}I$ es el área del rectángulo bajo ella (fig. [7](#abb-7)). Es máxima cuando su esquina está en el centro de la recta, con la mitad de la corriente y la mitad de la tensión. Entonces, en $R_\mathrm{i}$ y en $R_\mathrm{L}$ cae la misma tensión con la misma corriente, de modo que ambas resistencias son iguales.

:::abbildung et1/k7rechteck 7
Recta de la fuente de la batería con tres puntos de trabajo. Azul: $P_\mathrm{L}$, rectángulo de $I$ y $U_\mathrm{L}$. Rojo: $P_\mathrm{v}$, rectángulo de $I$ y $U_\mathrm{Ri}$. Ambos juntos son $P_\mathrm{q}=U_\mathrm{q}I$. La esquina central da el mayor rectángulo azul.
:::

:::satz Teorema 6.1 (Adaptación de potencia)
<span class="anker" id="satz-6-1"></span>

Con $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$, la potencia en la carga es

<span class="anker" id="gl-6-1"></span>
$$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}=U_\mathrm{q}^2\,\frac{R_\mathrm{L}}{\bigl(R_\mathrm{i}(1+R_\mathrm{L}/R_\mathrm{i})\bigr)^2}=P_\mathrm{CC}\,\frac{\alpha}{(1+\alpha)^2}, \tag{6.1}$$

con $\alpha=R_\mathrm{L}/R_\mathrm{i}$ y $P_\mathrm{CC}=U_\mathrm{q}^2/R_\mathrm{i}$. Es máxima para

<span class="anker" id="gl-6-2"></span>
$$R_\mathrm{L}=R_\mathrm{i},\qquad P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{CC}}{4},\qquad I=\frac{I_\mathrm{CC}}{2},\qquad U_\mathrm{L}=\frac{U_\mathrm{q}}{2}. \tag{6.2}$$
:::

⁠**Cómo leerlo:** $P_\mathrm{CC}=U_\mathrm{q}I_\mathrm{CC}$ es la __potencia de cortocircuito__, la potencia de la fuente con $R_\mathrm{L}=0$. Acaba por completo en $R_\mathrm{i}$, y ninguna carga recibe más de una cuarta parte de ella. **Validez:** La fuente está fijada; solo se elige $R_\mathrm{L}$. En una fuente equivalente, $U_\mathrm{CA}$ ocupa el lugar de $U_\mathrm{q}$.

:::herleitung El máximo, por tres caminos
Según la regla del cociente, $\bigl(f/g\bigr)'=(f'g-f\,g')/g^2$, con $f=\alpha$ y $g=(1+\alpha)^2$, es

$$\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{CC}\,\frac{(1+\alpha)^2-2\alpha(1+\alpha)}{(1+\alpha)^4}=P_\mathrm{CC}\,\frac{1-\alpha}{(1+\alpha)^3}.$$

La derivada es cero en $\alpha=1$, positiva antes y negativa después. Ese es el máximo.

Sin derivada: con $x=I/I_\mathrm{CC}$ es $P_\mathrm{L}=P_\mathrm{CC}\,x(1-x)$. Esta parábola tiene los ceros 0 y 1, de modo que su máximo $\frac14$ está en $x=\frac12$.

Como mecanismo: un incremento de corriente $\mathrm{d} I$ saca $U_\mathrm{q}\mathrm{d} I$ de la fuente, y las pérdidas crecen $2R_\mathrm{i}I\,\mathrm{d} I$. Con $I=I_\mathrm{CC}/2$, la pérdida se come el incremento: 9 V frente a $2\cdot2\,\Omega\cdot2{,}25\,\mathrm{A}=9$ V.
:::

::::beispiel
Para $R_\mathrm{L}=2\,\Omega$ son $I=2{,}25$ A, $U_\mathrm{L}=4{,}5$ V y $P_\mathrm{L}=10{,}125$ W, una cuarta parte de $P_\mathrm{CC}=40{,}5$ W. Las cargas de 0,5 $\Omega$ y 8 $\Omega$ dan ambas 6,48 W. En general, $\alpha$ y $1/\alpha$ dan la misma potencia, porque intercambian $x$ y $1-x$.
::::

⁠**Casos límite:** Para $\alpha\to0$, la corriente es fija y $P_\mathrm{L}\approx P_\mathrm{CC}\,\alpha$. Para $\alpha\to\infty$, la tensión es fija y $P_\mathrm{L}\approx P_\mathrm{CC}/\alpha$.

:::ltspice Parábola y recta
⁠**Esquema:** `voltage` con 9 de `q` a masa, `res` con 2 de `q` a `a`. Como carga, una fuente de corriente `current` llamada `I1` de `a` a masa.

⁠**Directivas:** `.dc I1 0 4.5 0.01` y `.meas dc Pmax MAX V(a)*I(I1)`

⁠**Lo que ves:** Representa `V(a)*I(I1)`: una parábola con el máximo de 10,125 W en 2,25 A. `V(a)/9` es el rendimiento, una recta descendente que allí alcanza 0,5. Con 3,6 A y 0,9 A hay 6,48 W en cada caso. Para el ejercicio [6](#aufg-6), introduce 12 y 4 y barre hasta 3 A: 9 W en 1,5 A, 8 W en 1 A y en 2 A.
:::

:::frage Tengo una carga fija. ¿Debo elegir la fuente de modo que $R_\mathrm{i}=R_\mathrm{L}$?
No. El teorema vale para una fuente fija y una carga elegible. Si la carga es fija y $R_\mathrm{i}$ se puede elegir, lo mejor es $R_\mathrm{i}=0$, porque $U_\mathrm{q}^2R_\mathrm{L}/(R_\mathrm{i}+R_\mathrm{L})^2$ disminuye con $R_\mathrm{i}$. La carga de 16 $\Omega$ recibe entonces 4 W con $R_\mathrm{i}=2\,\Omega$, y 5,06 W con $R_\mathrm{i}=0$.
:::

:::aufgabe Ejercicio 6 ★★ Altavoz en el amplificador
<span class="anker" id="aufg-6"></span>

La salida de un amplificador actúa como $U_\mathrm{q}=12$ V y $R_\mathrm{i}=4\,\Omega$. (a) ¿Qué altavoz extrae la mayor potencia, y cuánto vale? (b) ¿Qué da uno de 8 $\Omega$? Compara potencia y rendimiento. (c) ¿Qué segunda carga da la misma potencia que 8 $\Omega$? (d) ★★★ Demuestra con [(6.1)](#gl-6-1) que $\alpha$ y $1/\alpha$ siempre dan la misma potencia.

:::loesung
(a) $R_\mathrm{L}=4\,\Omega$, $P_\mathrm{L,max}=144\,\mathrm{V^2}/16\,\Omega=9$ W con $\eta=50$ %. (b) $I=1$ A, $P_\mathrm{L}=8$ W, $\eta=\frac23$. Solo se pierde el 11 % de la potencia, y las pérdidas bajan de 9 W a 4 W. (c) $\alpha=2$ corresponde a $\alpha=\frac12$, es decir, $R_\mathrm{L}=2\,\Omega$: 8 W, pero solo $\eta=\frac13$.

(d) $\dfrac{1/\alpha}{(1+1/\alpha)^2}=\dfrac{1/\alpha}{(\alpha+1)^2/\alpha^2}=\dfrac{\alpha}{(1+\alpha)^2}$.
:::
:::
