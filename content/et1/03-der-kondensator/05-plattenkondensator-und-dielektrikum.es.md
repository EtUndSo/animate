---
title: Etapa 4: Condensador de placas y dieléctrico
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1130500
summary: ¿De dónde sale el valor de C ?
tags: polarización, carga ligada, permitividad, permitividad relativa, ruptura, corriente de desplazamiento
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
¿De dónde sale el valor de $C$? En dos placas planas se deduce del área, la separación y el material entre ellas. Esta etapa deduce la fórmula y explica qué hace el aislante.
:::

**La idea.** Con tensión fija $U$ y separación fija $d$, el campo $E=U/d$ queda fijado ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). El campo indica lo densas que son las líneas de campo, y cada línea empieza en una carga. Queda fijada, por tanto, la carga por unidad de área. Por eso, el doble de área significa el doble de carga. La mitad de separación significa el doble de campo y, con ello, el doble de carga por unidad de área.

El aislante aumenta además la capacidad. Sus electrones permanecen en sus átomos, pero el campo desplaza un poco, en cada átomo o molécula, la carga positiva respecto a la negativa. Este desplazamiento se llama __polarización__. En el interior se anulan los extremos vecinos; en las superficies queda una __carga ligada__, negativa frente a la placa positiva (fig. [4](#abb-4) derecha). En ella termina una parte de las líneas de campo, y el campo entre las placas se debilitaría. Pero la batería mantiene fija $U$ y, con ella, $E$, así que aporta carga hasta que el campo vuelve a ser el correcto. Con la misma tensión hay más carga en las placas.

:::abbildung et1/k3platte 4
Misma tensión, misma separación, mismo campo. Izquierda, aire: cada línea de campo va de placa a placa; $A$ es el área de una placa. Derecha, un dieléctrico con $\varepsilon_\mathrm{r}=2$: las moléculas están orientadas, en el interior se anulan los extremos y en el borde queda carga ligada. La mitad de las líneas termina allí. Por eso, la placa lleva el doble de carga.
:::

:::satz Teorema 4.1 (Condensador de placas)
<span class="anker" id="satz-4-1"></span>

Para dos placas planas de área $A$ separadas una distancia $d$, con un dieléctrico que llena el espacio, se cumple

<span class="anker" id="gl-4-1"></span>
$$C=\varepsilon\,\frac{A}{d},\qquad\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r},\qquad\varepsilon_0=8{,}854\cdot10^{-12}\,\frac{\mathrm{A\,s}}{\mathrm{V\,m}}. \tag{4.1}$$
:::

⁠**Cómo leerlo:** $C$ aumenta con un área $A$ mayor (en m$^2$; la $A$ en cursiva no es la placa A de la etapa [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)), una separación $d$ menor (en m) y un $\varepsilon$ mayor. $\varepsilon_0$ es la constante eléctrica de la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). $\varepsilon$ se llama __permitividad__; el número puro $\varepsilon_\mathrm{r}$ se llama __permitividad relativa__ e indica en qué factor aumenta el material la capacidad respecto al vacío. El aire cuenta con el valor 1; el error es del 0,06 %. **Validez:** $d$ debe ser pequeña frente a la anchura de las placas. Si no, cuenta el campo de borde ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)); en el par de placas con 3 mm de separación y 10 cm de anchura aumenta $C$ en un 10 % aproximadamente. Para estimaciones basta [(4.1)](#gl-4-1).

| Material | Aire | Papel | Mica | Porcelana | Agua | Cerámica de condensador |
|---|---|---|---|---|---|---|
| $\varepsilon_\mathrm{r}$ | 1 | $\approx2$ | $\approx5$ | $\approx6$ | $\approx81$ | 60 a 3000 |

:::herleitung De la imagen de las líneas de campo a la fórmula
Una carga puntual crea el campo $E=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$. En el denominador está la superficie esférica por la que pasan todas sus líneas de campo. Así pues, según la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): la intensidad de campo es la carga dividida por $\varepsilon_0$ y por el área que sus líneas atraviesan uniformemente. En el par de placas, todas las líneas de la carga $Q$ pasan en paralelo por el área $A$:

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}\quad\Longrightarrow\quad C=\frac QU=\varepsilon_0\,\frac Ad.$$

Con dieléctrico, algunas líneas terminan en la carga ligada $Q_\mathrm{g}$, y por el espacio solo pasa la parte $Q-Q_\mathrm{g}$. En la mayoría de los aislantes, esta parte es una fracción fija de $Q$. Se escribe $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$, lo que da $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$ y, con ello, [(4.1)](#gl-4-1).
:::

**Ejemplo.** El par de placas tiene $C=8{,}854\cdot10^{-12}\,\mathrm{F/m}\cdot0{,}01\,\mathrm{m^2}/0{,}003\,\mathrm{m}=29{,}5$ pF. Con cerámica de $\varepsilon_\mathrm{r}=1000$ serían 29,5 nF. Para 100 µF con 3 mm de aire haría falta el área $A=C\,d/\varepsilon_0=33\,900\,\mathrm{m^2}$, es decir, 3,4 hectáreas. Por eso, los condensadores reales trabajan con capas finas (etapa [5](bauformen-und-selbstentladung.html#stufe-5)).

⁠**Comprobación:** La unidad es correcta: $\frac{\mathrm{A\,s}}{\mathrm{V\,m}}\cdot\frac{\mathrm{m^2}}{\mathrm{m}}=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$. **Caso límite:** Para $d\to0$, $C$ crecería sin límite. Lo impide la __ruptura__: con $E_\mathrm{max}$, el dieléctrico se vuelve conductor, en el aire con 3 MV/m ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Por eso, las capas finas necesitan un material sólido, y todo condensador tiene una tensión máxima $U_\mathrm{max}=E_\mathrm{max}\,d$.

:::zusatz La corriente de desplazamiento
Con $u=E\,d$ y [(4.1)](#gl-4-1), [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) se convierte en $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$. En el hueco no circula carga, pero allí cambia el campo, y este cambio tiene exactamente el tamaño de la corriente en los cables. Maxwell lo llamó __corriente de desplazamiento__. En el hueco crea el mismo campo magnético que la corriente en el cable (ley de Ampère, [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Para el campo magnético, por tanto, el circuito está cerrado.
:::

:::frage El agua tiene $\varepsilon_\mathrm{r}=81$. ¿Por qué nadie construye condensadores de agua?
Porque en la práctica el agua conduce: los iones disueltos llevan corriente entre las placas, y el condensador se descarga enseguida por sí solo. Un dieléctrico debe saber hacer dos cosas: polarizarse y aislar. El alto $\varepsilon_\mathrm{r}$ procede de las moléculas de agua, que tienen de por sí centros de carga separados y se orientan en el campo.
:::

:::aufgabe Ejercicio 4 ★★ Área y tensión máxima
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

¿Qué tamaño debe tener $A$ para 100 µF si, en lugar de 3 mm de aire, separa las placas una película de 10 µm de grosor con $\varepsilon_\mathrm{r}=3$?

</li>

<li>

¿Qué longitud tendría una tira de 5 cm de ancho con esta área?

</li>

<li>

¿Hasta qué tensión aguanta el par de placas en aire?

</li>

</ol>

:::loesung
(a) $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot10^{-5}\,\mathrm{m}}{3\cdot8{,}854\cdot10^{-12}\,\mathrm{F/m}}=37{,}6\,\mathrm{m^2}$.

(b) $37{,}6\,\mathrm{m^2}/0{,}05\,\mathrm{m}=753$ m. Los bobinados reales son más cortos porque usan película más fina y las dos caras de cada electrodo.

(c) $U_\mathrm{max}=E_\mathrm{max}\,d=3\,\mathrm{MV/m}\cdot3\,\mathrm{mm}=9$ kV.
:::
:::

:::aufgabe Ejercicio 5 ★★ Introducir un dieléctrico
<span class="anker" id="aufg-5"></span>

El par de placas está conectado a 9 V. Ahora el espacio se llena con un material de $\varepsilon_\mathrm{r}=4$. Predice primero qué se mantiene y calcula después.

<ol class="al">

<li>

La batería sigue conectada. ¿Cuánto valen $C$, $U$, $Q$ y $E$?

</li>

<li>

La batería se desconectó antes. ¿Cuánto valen ahora $C$, $U$, $Q$ y $E$?

</li>

<li>

¿Por qué difieren los dos casos, aunque $C$ sea igual?

</li>

</ol>

:::loesung
En ambos casos, $C=4\cdot29{,}5\,\mathrm{pF}=118$ pF.

(a) La batería mantiene fija $U=9$ V. Entonces $E=U/d=3$ kV/m no cambia, y $Q=C\,U=1{,}06$ nC. La batería aporta la carga adicional.

(b) Sin batería no puede llegar más carga, y $Q=266$ pC se mantiene. Entonces $U=Q/C=2{,}25$ V y $E=U/d=750$ V/m.

(c) En cada caso se mantiene fija una magnitud distinta: con batería, la tensión; sin batería, la carga. El dieléctrico cambia $C$, y la otra magnitud se ajusta según $Q=CU$.
:::
:::
