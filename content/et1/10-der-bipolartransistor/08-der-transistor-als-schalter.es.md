---
title: Etapa 6: El transistor como interruptor
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El transistor bipolar
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Capítulo 10: El transistor bipolar
order: 1200800
summary: Un interruptor debe estar del todo abierto o del todo cerrado.
tags: inversor, niveles lógicos, hipérbola de potencia
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Un interruptor debe estar del todo abierto o del todo cerrado. Esta etapa muestra por qué usa para ello los extremos de la recta de carga, construye con él el inversor y nombra los límites del componente.
:::

**La idea.** El transistor convierte en calor la potencia $P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$, en la práctica solo la primera parte. En la región de corte es $I_\mathrm{C}=0$; en la saturación, $U_\mathrm{CE}$ es pequeña. En ambos puntos el producto sigue siendo reducido. Es máximo en el centro de la recta de carga. Por eso un interruptor salta entre Z y S. Así, además, la distancia entre los dos niveles de salida es máxima, y no hay mecánica: el transistor conmuta muy deprisa y sin desgaste. Un amplificador, en cambio, trabaja en la región activa. Allí la curva característica es aproximadamente lineal, y la mayor potencia disipada cuenta menos que una señal sin distorsión.

El circuito lógico más pequeño es el __inversor__: el mismo circuito de la fig. [6](der-arbeitspunkt.html#abb-6), con $U_\mathrm{sal}=U_\mathrm{CE}$ como salida. Una tensión de entrada alta da una tensión de salida baja y viceversa. Como __niveles lógicos__, una tensión baja cuenta como 0 y una alta como 1.

:::satz Teorema 6.1 (Curva característica del inversor)
<span class="anker" id="satz-6-1"></span>

Con el modelo lineal se cumple

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{sal}= \begin{cases} U_\mathrm{CC} & U_\mathrm{ent}<U_\mathrm{BE},\\[2pt] U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{ent}-U_\mathrm{BE}}{R_\mathrm{B}} & U_\mathrm{BE}\le U_\mathrm{ent}\le U_\mathrm{ent,sat},\\[6pt] U_\mathrm{CE,sat} & U_\mathrm{ent}>U_\mathrm{ent,sat}, \end{cases} \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{ent,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}. \tag{6.2}$$
:::

⁠**Cómo leerlo:** La rama central es una recta de pendiente $-B\,R_\mathrm{C}/R_\mathrm{B}$. $U_\mathrm{ent,sat}$ es la tensión de entrada a la que el transistor alcanza la saturación. Por debajo de $U_\mathrm{BE}$ la entrada cuenta como 0, por encima de $U_\mathrm{ent,sat}$ como 1. Entre ambas, la señal no es unívoca. Por eso se elige $R_\mathrm{B}$ lo bastante pequeña para que $U_\mathrm{ent,sat}$ se acerque a $U_\mathrm{BE}$. La deducción es [(5.2)](der-arbeitspunkt.html#gl-5-2) con [(5.1)](der-arbeitspunkt.html#gl-5-1), despejando $U_\mathrm{ent}$ para $U_\mathrm{CE}=U_\mathrm{CE,sat}$. **Validez:** para señales lentas. Los cambios muy rápidos están limitados por la carga en la base.

:::abbildung et1/k10schalter 7
Izquierda, la curva característica del inversor con $R_\mathrm{B}=20$ k$\Omega$, codos en 0,6 V y 0,99 V. Centro, una señal rectangular entre 0 y 5 V en la entrada (gris) y la salida invertida entre 12 V y 0,2 V (azul). Derecha, los puntos de trabajo admisibles: por debajo de la hipérbola de potencia, $I_\mathrm{C,max}$ y $U_\mathrm{CE,max}$. El punto de trabajo A, con 12 mW, queda muy dentro de la zona permitida.
:::

::::beispiel
Con $R_\mathrm{B}=20$ k$\Omega$, la pendiente es $-30$ y $U_\mathrm{ent,sat}=0{,}99$ V. Una entrada lógica de 5 V da $I_\mathrm{B}=220$ µ A y $B\,I_\mathrm{B}=44$ mA, muy por encima de los 3,93 mA que permite $R_\mathrm{C}$. El transistor está, pues, sobreexcitado en un factor once, y sigue seguro en conducción incluso con un mal ejemplar. En él se producen $0{,}2\,\mathrm{V}\cdot3{,}93\,\mathrm{mA}+0{,}6\,\mathrm{V}\cdot0{,}22\,\mathrm{mA}=0{,}92$ mW, mientras conmuta una potencia de 46 mW en $R_\mathrm{C}$. En el punto A serían 12 mW en el transistor.
::::

⁠**Caso límite:** para $B\,R_\mathrm{C}/R_\mathrm{B}\to\infty$, la curva característica se convierte en un salto vertical en $U_\mathrm{BE}$.

**Límites de funcionamiento.** Tres valores limitan los puntos de trabajo permitidos (fig. [7](#abb-7), derecha). Por encima de $U_\mathrm{CE,max}$ se perfora la frontera CB. Por encima de $I_\mathrm{C,max}$ se sobrecargan la base y los hilos de conexión. Por encima de la __hipérbola de potencia__ $I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$ el componente se calienta demasiado. Fuera de estos límites, la vida útil cae rápidamente o el componente falla de inmediato. Para T, la hipérbola está a 40 V en 10 mA y a 4 V en 100 mA.

:::aufgabe Ejercicio 7 ★★ Inversor
<span class="anker" id="aufg-7"></span>

Un inversor con T funciona con $U_\mathrm{CC}=5$ V, $R_\mathrm{C}=1$ k$\Omega$ y $R_\mathrm{B}=10$ k$\Omega$. (a) Determina la pendiente y $U_\mathrm{ent,sat}$. (b) En la entrada hay 3,3 V. Determina $I_\mathrm{B}$, $I_\mathrm{C}$ y la potencia en el transistor. Compárala con el máximo sobre la recta de carga. (c) ¿Basta una entrada de 3,3 V también con $B=50$?

:::loesung
(a) Pendiente $-200\cdot1\,\text{k}\Omega/10\,\text{k}\Omega=-20$. $U_\mathrm{ent,sat}=4{,}8\,\mathrm{V}/20+0{,}6\,\mathrm{V}=0{,}84$ V.

(b) $I_\mathrm{B}=2{,}7\,\mathrm{V}/10\,\text{k}\Omega=270$ µ A, $B\,I_\mathrm{B}=54$ mA, muy por encima de $I_\mathrm{C}=4{,}8\,\mathrm{V}/1\,\text{k}\Omega=4{,}8$ mA, luego saturación. $P=0{,}2\,\mathrm{V}\cdot4{,}8\,\mathrm{mA}+0{,}6\,\mathrm{V}\cdot0{,}27\,\mathrm{mA}=1{,}12$ mW. Sobre la recta de carga, $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$. El máximo está en $U_\mathrm{CC}/2$ con $U_\mathrm{CC}^2/(4R_\mathrm{C})=6{,}25$ mW.

(c) $U_\mathrm{ent,sat}=4{,}8\,\mathrm{V}/5+0{,}6\,\mathrm{V}=1{,}56$ V $<3{,}3$ V: sí.
:::
:::
