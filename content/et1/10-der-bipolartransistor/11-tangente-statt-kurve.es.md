---
title: Etapa 9: Tangente en lugar de curva
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1201100
summary: Un amplificador trabaja alrededor de un punto fijo en la región activa.
tags: pequeña señal, derivada parcial, resistencia de entrada, resistencia de salida, tensión de Early, circuito equivalente ampliado, circuito equivalente de pequeña señal
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Un amplificador trabaja alrededor de un punto fijo en la región activa. Allí, las pequeñas variaciones no ven una función exponencial, sino una recta. Esta etapa lee sus pendientes y las dibuja como circuito equivalente.
:::

**La idea.** El modelo lineal de la etapa [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) tiene dos defectos. Convierte el tramo BE en una tensión fija, así que su resistencia de entrada es cero. Y hace horizontal la curva característica de salida, así que su conductancia es cero. En realidad, ambas pendientes son finitas. Para pequeñas variaciones alrededor del punto de trabajo basta lo que en el diodo ([Parte 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) fue la tangente: el terreno de la etapa [3](eine-flache-viele-kennlinien.html#stufe-3) se convierte allí en un plano inclinado, con una pendiente por dirección.

La descomposición se escribe así: magnitud total igual a componente continua más variación, $u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t)$, $i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$. Las letras minúsculas con índices minúsculos se llaman __pequeña señal__. El signo $\partial$ representa la __derivada parcial__: la derivada respecto a una variable manteniendo fijas las demás, es decir, la pendiente de una sección.

:::definition Definición 9.1 (Magnitudes de pequeña señal en el punto de trabajo)
<span class="anker" id="satz-9-1"></span>

<span class="anker" id="gl-9-1"></span>
$$S=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{I_\mathrm{C}}{U_T},\qquad r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S},\qquad G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}. \tag{9.1}$$

Para las variaciones se tiene entonces

<span class="anker" id="gl-9-2"></span>
$$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}},\qquad i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}. \tag{9.2}$$
:::

⁠**Cómo leerlo:** La transconductancia $S$ en A/V es la pendiente de la curva característica de control; $r_\mathrm{BE}$ es la __resistencia de entrada__, la pendiente de la curva característica de entrada leída a la inversa. $r_\mathrm{CE}$ es la __resistencia de salida__. Las rectas de las curvas características de salida, prolongadas hacia la izquierda, se encuentran en $-U_\mathrm{Early}$. La __tensión de Early__ $U_\mathrm{Early}$ está típicamente entre 50 V y 200 V; en T son 74 V. Mecanismo: más $U_\mathrm{CB}$ ensancha la zona de carga espacial hacia el interior de la base. La base se estrecha, el gradiente de densidad se hace más abrupto y la corriente aumenta. **Validez:** región activa y $|u_\mathrm{be}|\ll U_T$.

:::herleitung Las pendientes
De $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$ se deduce $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{1}{U_T}I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}=\frac{I_\mathrm{C}}{U_T}$. La derivada de una función exponencial es la propia función dividida por la escala del exponente. Del mismo modo, $\partial I_\mathrm{B}/\partial U_\mathrm{BE}=I_\mathrm{B}/U_T$. El valor inverso es $r_\mathrm{BE}$. Con $I_\mathrm{B}=I_\mathrm{C}/B$ se deduce $r_\mathrm{BE}=B/S$. El tercer factor de [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1) da $\partial I_\mathrm{C}/\partial U_\mathrm{CE}=I_\mathrm{C}/(74\,\mathrm{V}+U_\mathrm{CE})$. En el punto A son 80 V en el denominador. La suma en [(9.2)](#gl-9-2) es el plano tangente, que reúne ambas direcciones.
:::

:::abbildung et1/k10tangente 10
Izquierda, la curva característica de control con la tangente en el punto A (2 mA), pendiente $S=76{,}9$ mS. Derecha, curvas características de salida para dos valores de $U_\mathrm{BE}$. La distancia entre las curvas es el efecto de $S$. La pendiente de cada curva es $1/r_\mathrm{CE}$; prolongadas hacia la izquierda, alcanzan $-74$ V.
:::

::::beispiel
En el punto A, $S=2\,\mathrm{mA}/26\,\mathrm{mV}=76{,}9$ mS, es decir, $1/S=13\,\Omega$, y además $r_\mathrm{BE}=200/S=2{,}6$ k$\Omega$ y $r_\mathrm{CE}=80\,\mathrm{V}/2\,\mathrm{mA}=40$ k$\Omega$. Mecanismo de $S$: 1 mV más de $U_\mathrm{BE}$ reduce la barrera, y según la tangente la inyección sube un 3,85 %, es decir, 77 µ A. Para lograr lo mismo por la salida harían falta 3 V en $U_\mathrm{CE}$.
::::

⁠**En resumen:** la transconductancia es la corriente dividida por $U_T$, independiente de $B$ y de $I_\mathrm{S}$. **Casos límite:** $I_\mathrm{C}\to0$ da $S\to0$: sin corriente de reposo no hay efecto de control. $U_\mathrm{Early}\to\infty$ da $r_\mathrm{CE}\to\infty$, la fuente de corriente ideal.

**¿Cuánto es pequeño?** Exactamente, $i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$; la tangente dice $I_\mathrm{C}u_\mathrm{be}/U_T$. Con $u_\mathrm{be}=+1$ mV el error es del 2 %, con $+5$ mV es del 10 % ($+424$ µ A en lugar de $+385$ µ A), mientras que con $-5$ mV circulan solo $-350$ µ A. La semionda positiva se hace mayor que la negativa, y la señal se distorsiona. Con 26 mV, la tangente es inservible.

**Del modelo al circuito equivalente.** Las tangentes se convierten en componentes (fig. [11](#abb-11)). El __circuito equivalente ampliado__ contiene las componentes continuas. En la entrada hay una fuente $U_0$ y $r_\mathrm{BE}$ en serie. Aquí, $U_0=U_\mathrm{BE}-U_T=0{,}574$ V es el punto en el que la tangente a la curva característica de entrada corta el eje. En la salida hay una fuente de corriente controlada $I$ y $r_\mathrm{CE}$ en paralelo. En el punto A entrega $I=1{,}85$ mA, y por $r_\mathrm{CE}$ circulan los 0,15 mA restantes. Si se omiten las componentes continuas, queda el __circuito equivalente de pequeña señal__. Las fuentes constantes desaparecen en él: una tensión constante se convierte en un hilo, también $U_\mathrm{CC}$ (superposición, [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Para la traducción vale lo siguiente: si una corriente depende de la tensión en su propio par de terminales, es una resistencia. Si depende de otra tensión, es una fuente controlada, aquí una fuente de corriente controlada por tensión (VCCS, [Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Expresado como cuadripolo, son los parámetros Y $Y_{11}=1/r_\mathrm{BE}$, $Y_{12}=0$, $Y_{21}=S$, $Y_{22}=G_\mathrm{CE}$.

:::abbildung et1/k10kleinsignal 11
Izquierda, el circuito equivalente ampliado para magnitudes continuas en conducción. Derecha, el circuito equivalente de pequeña señal: las constantes han desaparecido y solo quedan las pendientes. La fuente $S\,u_\mathrm{be}$ es la tangente en la dirección de $U_\mathrm{BE}$, $r_\mathrm{CE}$ la de la dirección de $U_\mathrm{CE}$.
:::

:::frage ¿No es la transconductancia la pendiente en la familia de curvas características de salida?
No. Allí, $U_\mathrm{CE}$ es el eje horizontal, así que la pendiente es $1/r_\mathrm{CE}$. La transconductancia pertenece a la dirección de $U_\mathrm{BE}$ y aparece en la familia de salida como la distancia vertical entre dos curvas, dividida por su diferencia en $U_\mathrm{BE}$.
:::

:::frage ¿Por qué $1/S=13\,\Omega$, pero $r_\mathrm{BE}=2{,}6$ k$\Omega$? Ambas miden la misma tensión.
Ambas dividen la variación de tensión por una corriente, pero por corrientes distintas. $1/S$ divide por la variación de $I_\mathrm{C}$; $r_\mathrm{BE}$, por la variación $B$ veces menor de $I_\mathrm{B}$. Por eso la resistencia de entrada es $B$ veces mayor. La relación es aquí 200.
:::

:::aufgabe Ejercicio 11 ★★ Magnitudes de pequeña señal
<span class="anker" id="aufg-11"></span>

T trabaja con $I_\mathrm{C}=0{,}5$ mA y $U_\mathrm{CE}=6$ V. (a) Determina $S$, $1/S$, $r_\mathrm{BE}$ y $r_\mathrm{CE}$. (b) Para $u_\mathrm{be}=\pm5$ mV, compara la variación exacta de corriente con la tangente. (c) Predice: ¿cómo cambian los cuatro valores de (a) si la corriente se hace el doble?

:::loesung
(a) $S=19{,}2$ mS, $1/S=52\,\Omega$, $r_\mathrm{BE}=200/S=10{,}4$ k$\Omega$, $r_\mathrm{CE}=80\,\mathrm{V}/0{,}5\,\mathrm{mA}=160$ k$\Omega$.

(b) Tangente $\pm96$ µ A. Exacto: $+106$ µ A y $-87$ µ A.

(c) $S$ se duplica; $1/S$, $r_\mathrm{BE}$ y $r_\mathrm{CE}$ se reducen a la mitad. Los cuatro son proporcionales o inversamente proporcionales a la corriente.
:::
:::
