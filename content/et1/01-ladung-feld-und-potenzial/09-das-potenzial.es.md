---
title: Etapa 7: El potencial
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Carga, campo y potencial
order: 1110900
summary: Si el trabajo solo depende del inicio y del final, basta un único número por lugar para calcularlo.
tags: superficies equipotenciales
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Si el trabajo solo depende del inicio y del final, basta un único número por lugar para calcularlo. Ese número es el potencial.
:::

**La idea.** Se elige un punto de referencia y se escribe en cada lugar el trabajo por unidad de carga que el campo cede en el camino desde allí hasta el punto de referencia. Dividir por la carga convierte ese número en una propiedad del lugar. El trabajo entre dos lugares es entonces una diferencia de dos de esos números.

:::analogie
El potencial es la altura de un paisaje; el campo, su pendiente; una carga positiva, una pelota que rueda cuesta abajo. La imagen deja de valer con las cargas negativas: en el mismo paisaje ruedan cuesta arriba.
:::

:::definition Definición 7.1 (Potencial)
<span class="anker" id="satz-7-1"></span>

En un campo electrostático con el punto de referencia $P_0$, el potencial de un punto $P$ es

<span class="anker" id="gl-7-1"></span>
$$\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s,\qquad[\varphi]=\frac{\mathrm J}{\mathrm C}=\mathrm V. \tag{7.1}$$

Una carga $Q$ tiene allí la energía potencial $W_\mathrm{pot}=Q\,\varphi(P)$.
:::

:::satz Teorema 7.2 (Trabajo como diferencia de potencial, dos perfiles)
<span class="anker" id="satz-7-2"></span>

<span class="anker" id="gl-7-2"></span>
$$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr). \tag{7.2}$$

En el campo uniforme en la dirección $x$ y en el campo de una carga puntual $Q_0$ (punto de referencia en el infinito) se cumple

<span class="anker" id="gl-7-3"></span>
$$\varphi(x)=\varphi(0)-E\,x,\qquad\varphi(r)=k\,\frac{Q_0}{r}. \tag{7.3}$$
:::

:::herleitung Trabajo como diferencia de potencial
Como el trabajo no depende del camino, se puede ir de $P_1$ a $P_2$ pasando por $P_0$:

$$\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\int_{P_1}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_2}\vec E\cdot\mathrm{d}\vec s=\varphi(P_1)-\varphi(P_2).$$

Sin independencia del camino, $\varphi$ ni siquiera estaría definido de forma única. Los perfiles [(7.3)](#gl-7-3) se deducen de [(7.1)](#gl-7-1) con $E$ constante y de la deducción de la etapa [6](arbeit-im-feld.html#stufe-6) con $r_2\to\infty$.
:::

⁠**Cómo leerlo:** $\varphi$ es un número por lugar, no un vector. En la dirección de $\vec E$, $\varphi$ disminuye; la intensidad de campo es la pendiente del potencial: $E_x=-\mathrm{d}\varphi/\mathrm{d} x$. Si $P_0$ se traslada a otro sitio, todos los potenciales cambian en la misma cantidad. **Validez:** El potencial presupone un campo electrostático.

**Superficies equipotenciales.** Los lugares de igual potencial forman __superficies equipotenciales__. Sobre ellas, una carga puede desplazarse sin trabajo. De ahí se sigue que las líneas de campo son perpendiculares a ellas; si no, habría trabajo a lo largo de la superficie. En el par de placas son planos paralelos a las placas; alrededor de una carga puntual, esferas. Un cuerpo metálico en reposo tiene, por ser $\vec E=0$, el mismo potencial en todas partes.

:::abbildung et1/k1potenzial 8
Izquierda: el par de placas con el punto de referencia en la placa B. Las líneas discontinuas son superficies equipotenciales en sección, separadas 3 V. Derecha: el potencial baja a lo largo de $x$ de 9 V a 0 V; su pendiente $-3$ V/mm es $-E$.
:::

::::beispiel
Con $\varphi=0$ en B, A está a 9 V, y $\varphi(x)=9\,\mathrm{V}-3\,\mathrm{kV/m}\cdot x$: 6 V en 1 mm, 3 V en 2 mm. La esfera A ($+10$ nC) tiene a 3 cm de distancia el potencial 3,0 kV, y a 6 cm, 1,5 kV. La diferencia por 1 nC da los 1,5 µ J de la etapa [6](arbeit-im-feld.html#stufe-6).
::::

⁠**En resumen:** el potencial es la energía por unidad de carga en un lugar, medida desde el punto de referencia.

⁠**Casos límite:** Para $r\to\infty$, $\varphi\to0$; ese es el punto de referencia elegido. Para $E=0$, $\varphi$ es constante, pero no tiene por qué ser cero.

:::frage Si $\varphi=0$, allí tampoco hay campo, ¿verdad?
No. El campo depende de la pendiente, no del valor. La placa B tiene $\varphi=0$, y justo delante de ella hay el campo completo de 3 kV/m. A la inversa, en el interior de una esfera metálica cargada $E=0$, pero su potencial no es cero.
:::

:::aufgabe Ejercicio 7 ★★ Separar potencial y campo
<span class="anker" id="aufg-7"></span>

En el eje $x$ están $Q_1=+4$ nC en $x=0$ y $Q_2=-1$ nC en $x=6$ cm; el punto de referencia está en el infinito.

<ol class="al">

<li>

Calcula el potencial en $x=3$ cm. ¿Por qué aquí se suma sin direcciones?

</li>

<li>

¿Dónde, entre las cargas, es $\varphi=0$? ¿Qué valor tiene $E$ allí?

</li>

</ol>

:::loesung
(a) Los potenciales son números y se suman con su signo: $\varphi=k\,(4\,\mathrm{nC}-1\,\mathrm{nC})/3\,\mathrm{cm}=899$ V. (b) $4/x-1/(6-x)=0$ con $x$ en cm da $x=4{,}8$ cm. Allí, ambos campos apuntan hacia la derecha: $E=k\cdot4\,\mathrm{nC}/(4{,}8\,\mathrm{cm})^2+k\cdot1\,\mathrm{nC}/(1{,}2\,\mathrm{cm})^2=15{,}6\,\mathrm{kV/m}+62{,}4\,\mathrm{kV/m}=78{,}0$ kV/m. Así pues, $\varphi=0$ no significa $E=0$.
:::
:::
