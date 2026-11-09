---
title: Etapa 7: Por qué el 50 %, y qué objetivo se aplica
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170800
summary: El máximo de potencia desperdicia la mitad.
tags: 
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
El máximo de potencia desperdicia la mitad. Esta etapa muestra por qué eso es inevitable y cuándo se quiere de todos modos.
:::

**La idea.** De $\eta=U_\mathrm{L}/U_\mathrm{q}$ y de la recta de la fuente se deduce: el rendimiento baja linealmente con la corriente, porque cuanta más corriente, más tensión se queda en $R_\mathrm{i}$. La potencia de la fuente $P_\mathrm{q}=U_\mathrm{q}I$, en cambio, sube linealmente con la corriente. A la carga llega el producto, $P_\mathrm{L}=P_\mathrm{q}\,\eta$. El producto de una recta ascendente y una descendente es una parábola con el vértice en el centro, y allí la recta descendente está a media altura (fig. [8](#abb-8)). El 50 % no es ni casualidad ni una cuestión de material.

:::satz Teorema 7.1 (Potencia y rendimiento)
<span class="anker" id="satz-7-1"></span>

Al dividir $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ por $U_\mathrm{q}$ se obtiene, con $x=I/I_\mathrm{CC}$,

<span class="anker" id="gl-7-1"></span>
$$\eta=1-x,\qquad\frac{P_\mathrm{L}}{P_\mathrm{CC}}=x\,\eta=x(1-x). \tag{7.1}$$

Con adaptación de potencia, $x=\frac12$ y, por tanto, $\eta=\frac12$.
:::

⁠**Cómo leerlo:** $x$ es la corriente como fracción de la corriente de cortocircuito; $\eta$, la fracción de la energía por culombio que llega a la carga. **En resumen:** En el máximo de potencia, cada carga cede una mitad de su energía en la fuente y la otra en la carga conectada. **Validez:** como en la etapa [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5). **Casos límite:** $x=0$ es el circuito abierto con $\eta=1$; $x=1$, el cortocircuito con $\eta=0$. En ambos, $P_\mathrm{L}=0$.

:::abbildung et1/k7kurven 8
A la izquierda: potencia en la carga y rendimiento frente a $R_\mathrm{L}/R_\mathrm{i}$. El máximo de potencia está en 1, donde $\eta=0{,}5$. A la derecha, las mismas curvas frente a la corriente: $\eta$ se convierte en una recta, la potencia en una parábola. La normalización es respecto a $P_\mathrm{L,max}=P_\mathrm{CC}/4$.
:::

**Tres objetivos.** Qué funcionamiento es el correcto depende de lo que cuente.

| Adaptación | Condición | Resultado | $\eta$ | Uso |
|---|---|---|---|---|
| Tensión | $R_\mathrm{L}\gg R_\mathrm{i}$ | $U_\mathrm{L}\approx U_\mathrm{q}$, casi independiente de la carga | cerca de 1 | Red eléctrica, batería, voltímetro |
| Corriente | $R_\mathrm{L}\ll R_\mathrm{i}$ | $I\approx I_\mathrm{CC}$, casi independiente de la carga | cerca de 0 | Amperímetro, fuentes de corriente |
| Potencia | $R_\mathrm{L}=R_\mathrm{i}$ | $P_\mathrm{L}$ máxima | $\frac12$ | Antenas, procesamiento de señales |

::::beispiel [Ejemplos]
En la batería, $R_\mathrm{L}=200\,\Omega$ da la tensión de 8,91 V, el 99 % de $U_\mathrm{q}$. Con $R_\mathrm{L}=0{,}02\,\Omega$ circulan 4,46 A, el 99 % de $I_\mathrm{CC}$. El paso de 2 $\Omega$ a 8 $\Omega$ cuesta el 36 % de la potencia y reduce el calor en la batería al 16 %.
::::

⁠**Ingeniería de potencia.** Las potencias están en el rango de los kW; todo calor en la fuente cuesta dinero y la pone en peligro. Se quiere un rendimiento alto, es decir, $R_\mathrm{i}\ll R_\mathrm{L}$. Una batería de herramienta eléctrica de 18 V y 60 m$\Omega$ alcanza en el arranque con 120 A todavía $\eta=1-7{,}2\,\mathrm{V}/18\,\mathrm{V}=60$ %, y en su interior se generan $(120\,\mathrm{A})^2\cdot60\,\mathrm{m\Omega}=864$ W. Una lámpara de trabajo de 1,8 W actúa como 180 $\Omega$, y $\eta=180/180{,}06=99{,}97$ %. La adaptación significaría aquí 1350 W de calor en la batería.

⁠**Ingeniería de comunicaciones.** Las potencias están en el rango de los µ W. Un receptor solo puede tomar lo que ofrece la antena. Cuenta la potencia absoluta, no la fracción, y el calor en la fuente no perjudica. Una antena de 10 mV y 50 $\Omega$ entrega a 50 $\Omega$ exactamente 0,5 µ W, y a 5 $\Omega$ o 500 $\Omega$ solo 0,165 µ W.

**Fuentes equivalentes: el máximo se mantiene, el 50 % no.** A menudo, la fuente es una red. La fig. [9](#abb-9) muestra una fuente con $R_\mathrm{q}$ y, en paralelo, $R$. Respecto a los terminales A, B es una fuente equivalente ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) con $R_\mathrm{i}=R_\mathrm{q}\parallel R$ y $U_\mathrm{CA}=U_\mathrm{q}R/(R_\mathrm{q}+R)$. Para la carga solo cuenta la recta en los terminales, de modo que el máximo está en $R_\mathrm{L}=R_\mathrm{i}$, con

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)},\qquad P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}. \tag{7.2}$$

Sin embargo, la fuente real trabaja sobre $R_\mathrm{tot}=R_\mathrm{q}+R\parallel R_\mathrm{L}$, y entonces resulta

<span class="anker" id="gl-7-3"></span>
$$P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{tot}}=\frac{U_\mathrm{q}^2\,(2R_\mathrm{q}+R)}{2R_\mathrm{q}(R_\mathrm{q}+R)},\qquad\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12\quad\text{para }R<\infty. \tag{7.3}$$

:::abbildung et1/k7netz 9
A la izquierda, la red con adaptación y las potencias reales. A la derecha, su fuente equivalente. Para la carga ambas son iguales; en la fuente, no.
:::

:::herleitung Las transformaciones hasta [(7.3)](#gl-7-3)
Con $R_\mathrm{L}=R_\mathrm{q}R/(R_\mathrm{q}+R)$ es $R\parallel R_\mathrm{L}=R^2R_\mathrm{q}/(R^2+2R_\mathrm{q}R)=R\,R_\mathrm{q}/(R+2R_\mathrm{q})$. Eso da $R_\mathrm{tot}=2R_\mathrm{q}(R_\mathrm{q}+R)/(2R_\mathrm{q}+R)$. En general, el divisor de tensión da $U_\mathrm{L}=U_\mathrm{q}(R\parallel R_\mathrm{L})/R_\mathrm{tot}=U_\mathrm{q}\,R\,R_\mathrm{L}/\bigl(R_\mathrm{q}(R+R_\mathrm{L})+R\,R_\mathrm{L}\bigr)$. Al sustituir se obtiene la fórmula de [(7.2)](#gl-7-2). Con ello, $P_\mathrm{L}=U_\mathrm{L}^2(R_\mathrm{q}+R)/(R_\mathrm{q}R)$. El cociente de $P_\mathrm{L}$ y $P_\mathrm{q}$ se simplifica en [(7.3)](#gl-7-3).
:::

::::beispiel
Para $U_\mathrm{q}=18$ V, $R_\mathrm{q}=6\,\Omega$ y $R=3\,\Omega$ son $R_\mathrm{i}=2\,\Omega$ y $U_\mathrm{CA}=6$ V. Con $R_\mathrm{L}=2\,\Omega$ hay 3 V en la carga, que recibe 4,5 W. Por $R_\mathrm{q}$ circulan 2,5 A, de los cuales 1 A pasa por $R$. Eso da 37,5 W en $R_\mathrm{q}$, 3 W en $R$ y, junto con la carga, $P_\mathrm{q}=45$ W y $\eta=10$ %. La fuente equivalente muestra aparentemente el 50 %, porque no dice nada sobre el interior. La corriente por $R$ circula también sin carga; ya en circuito abierto, la red calienta con 36 W.
::::

⁠**Caso límite:** Para $R\to\infty$ desaparece esta rama, y [(7.3)](#gl-7-3) vuelve a dar $\eta=\frac12$.

:::frage ¿Significa $\eta=50$ % en el máximo que con la adaptación «pierdo» la mitad de la energía?
En una fuente con resistencia interna real, sí; se calienta tanto como la carga. Con potencia pequeña es tolerable. Donde la energía es cara o la fuente es sensible, se trabaja muy a la derecha del máximo.
:::

:::aufgabe Ejercicio 7 ★ ¿Qué objetivo se aplica?
<span class="anker" id="aufg-7"></span>

Asigna y calcula: (a) Un voltímetro de 10 M$\Omega$ en la batería. ¿Cuánto se desvía la indicación de 9 V? (b) Un amperímetro de 0,1 $\Omega$ en un circuito de 5 V y 1 k$\Omega$. ¿En qué porcentaje cambia la corriente? (c) Una fuente de alimentación de 12 V y 50 m$\Omega$ con 6 $\Omega$. ¿Cuánto vale $\eta$? (d) ¿Qué daría la adaptación de potencia en la misma fuente de alimentación?

:::loesung
(a) Adaptación de tensión: $R_\mathrm{L}\gg R_\mathrm{i}$. Circulan 0,9 µ A, y dentro caen 1,8 µ V. (b) Adaptación de corriente: la fuente se comporta como de alta impedancia. La corriente baja de 5 mA en un 0,01 %. (c) Adaptación de tensión: $\eta=6/6{,}05=99{,}2$ %. (d) $R_\mathrm{L}=50$ m$\Omega$ daría 720 W en la carga y 720 W en la fuente de alimentación, lo que sería destructivo.
:::
:::

:::aufgabe Ejercicio 8 ★★★ La red con adaptación
<span class="anker" id="aufg-8"></span>

Una fuente con $U_\mathrm{q}=24$ V y $R_\mathrm{q}=4\,\Omega$ se carga con $R=12\,\Omega$, y la carga está en paralelo con $R$. (a) Determina $R_\mathrm{i}$ y $U_\mathrm{CA}$. (b) Calcula $U_\mathrm{L}$ y $P_\mathrm{L}$ con adaptación. (c) Calcula $P_\mathrm{q}$ y $\eta$, una vez a partir de las corrientes y otra con [(7.3)](#gl-7-3). (d) ¿Qué valor debe tener $R$ para que $\eta=45$ %?

:::loesung
(a) $R_\mathrm{i}=4\,\Omega\parallel12\,\Omega=3\,\Omega$, $U_\mathrm{CA}=24\,\mathrm{V}\cdot12/16=18$ V. (b) $U_\mathrm{L}=9$ V, $P_\mathrm{L}=(9\,\mathrm{V})^2/3\,\Omega=27$ W $=U_\mathrm{CA}^2/(4R_\mathrm{i})$. (c) 3 A por la carga, 0,75 A por $R$, es decir, 3,75 A desde la fuente. $P_\mathrm{q}=90$ W $=56{,}25\,\mathrm{W}+6{,}75\,\mathrm{W}+27\,\mathrm{W}$, $\eta=30$ %, igual que $\frac12\cdot12/20$. (d) $\frac12R/(8\,\Omega+R)=0{,}45$ da $R=72\,\Omega$.
:::
:::
