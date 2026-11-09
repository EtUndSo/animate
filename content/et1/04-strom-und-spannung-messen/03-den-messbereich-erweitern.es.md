---
title: Etapa 2: Ampliar el rango de medida
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Medir corriente y tensión
order: 1140300
summary: El mecanismo de medida termina en 50 µ A y 100 mV.
tags: shunt, resistencia en serie
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
El mecanismo de medida termina en 50 µ A y 100 mV. Esta etapa lo convierte en un amperímetro hasta 10 mA y en un voltímetro hasta 10 V y muestra de dónde vienen $R_\mathrm{iA}$ y $R_\mathrm{iV}$.
:::

**La idea.** El mecanismo de medida solo soporta 50 µ A. Si debe mostrar 10 mA, el resto tiene que pasar de largo: un __shunt__ (resistencia en paralelo) se conecta en paralelo y asume 9,95 mA. Si debe mostrar 10 V, solo puede haber 100 mV en él: una __resistencia en serie__ asume 9,9 V (fig. [2](#abb-2)). A fondo de escala, el mecanismo ve lo mismo que antes; solo cambia la rotulación de la escala.

:::abbildung et1/k4bereich 2
El mismo mecanismo de medida dos veces. A la izquierda, el shunt divide la corriente en la relación 199 a 1; a la derecha, la resistencia en serie divide la tensión en la relación 99 a 1.
:::

:::satz Teorema 2.1 (Shunt y resistencia en serie)
<span class="anker" id="satz-2-1"></span>

Sea un instrumento con resistencia interna $R_\mathrm{viejo}$ y valor de fondo de escala $I_\mathrm{viejo}$ o $U_\mathrm{viejo}$, respectivamente. Para el nuevo valor de fondo de escala $I_\mathrm{nuevo}$ o $U_\mathrm{nuevo}=\alpha\,U_\mathrm{viejo}$ necesita

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{Shunt}=R_\mathrm{viejo}\,\frac{I_\mathrm{viejo}}{I_\mathrm{nuevo}-I_\mathrm{viejo}},\qquad R_\mathrm V=R_\mathrm{viejo}\,(\alpha-1). \tag{2.1}$$

La nueva resistencia interna es $R_\mathrm{viejo}\parallel R_\mathrm{Shunt}$ o $R_\mathrm{viejo}+R_\mathrm V$, respectivamente.
:::

⁠**Cómo leerlo:** $\alpha>1$ es el factor de ampliación, sin unidad. $\parallel$ significa en paralelo: $R_a\parallel R_b=R_aR_b/(R_a+R_b)$. El shunt es pequeño frente a $R_\mathrm{viejo}$; la resistencia en serie, grande. **Validez:** La desviación debe ser proporcional a la corriente, y las resistencias deben ser exactas, porque su error entra en la lectura.

:::herleitung Divisor de corriente y divisor de tensión
El shunt y el instrumento están en paralelo; $G=1/R$ es la conductancia. A fondo de escala vale el divisor de corriente

$$\frac{I_\mathrm{viejo}}{I_\mathrm{nuevo}}=\frac{R_\mathrm{Shunt}}{R_\mathrm{Shunt}+R_\mathrm{viejo}}=\frac{G_\mathrm{viejo}}{G_\mathrm{Shunt}+G_\mathrm{viejo}} \quad\Rightarrow\quad R_\mathrm{Shunt}=\frac{I_\mathrm{viejo}}{I_\mathrm{nuevo}}\,(R_\mathrm{Shunt}+R_\mathrm{viejo}).$$

Despejando $R_\mathrm{Shunt}$ se obtiene [(2.1)](#gl-2-1). La resistencia en serie y el instrumento están en serie. El divisor de tensión da

$$U_\mathrm{viejo}=U_\mathrm{nuevo}\,\frac{R_\mathrm{viejo}}{R_\mathrm{viejo}+R_\mathrm V} \quad\Rightarrow\quad \alpha=\frac{R_\mathrm{viejo}+R_\mathrm V}{R_\mathrm{viejo}}\quad\Rightarrow\quad R_\mathrm V=R_\mathrm{viejo}\,(\alpha-1).$$
:::

::::beispiel
Para 10 mA: $R_\mathrm{Shunt}=2\,\mathrm{k\Omega}\cdot\frac{50\,\mu\text{A}}{9{,}95\,\mathrm{mA}}=10{,}05\,\Omega$, en paralelo con 2 k$\Omega$ da $R_\mathrm{iA}=10\,\Omega$. Para 10 V: $\alpha=100$, $R_\mathrm V=2\,\mathrm{k\Omega}\cdot99=198$ k$\Omega$, es decir, $R_\mathrm{iV}=200$ k$\Omega$.
::::

⁠**En resumen:** a fondo de escala, en el amperímetro caen 100 mV en cualquier rango, y por el voltímetro circulan 50 µ A en cualquier rango. De ahí se deducen directamente las resistencias internas: $R_\mathrm{iA}=100\,\mathrm{mV}/10\,\mathrm{mA}=10\,\Omega$ y $R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200$ k$\Omega$. Así pues, un rango de corriente sensible tiene una resistencia interna grande, y un rango de tensión alto también. El inverso de 50 µ A, 20 k$\Omega$/V, figura como dato característico en los instrumentos de aguja.

⁠**Caso límite:** Para $I_\mathrm{nuevo}\to I_\mathrm{viejo}$, $R_\mathrm{Shunt}\to\infty$; para $\alpha=1$, $R_\mathrm V=0$. Sin ampliación no hace falta ningún componente.

**Varios rangos.** Un instrumento multirrango (aparato con varios rangos) conmuta entre ellos (fig. [3](#abb-3)). En el amperímetro, cada interruptor adicional pone un shunt en paralelo; en el voltímetro, cada interruptor adicional abierto incorpora una resistencia en serie. La ecuación [(2.1)](#gl-2-1) vale paso a paso: el conjunto anterior es el instrumento, y su resistencia interna se llama $R_\mathrm{viejo}$.

:::abbildung et1/k4stufen 3
Ampliación escalonada. A la izquierda, cada interruptor cerrado añade un shunt; a la derecha, cada interruptor abierto añade una resistencia en serie.
:::

:::frage ¿El shunt hace más sensible el instrumento?
No, menos sensible. El mecanismo de medida sigue necesitando 50 µ A para la desviación a fondo de escala, y el shunt hace que para ello hagan falta 10 mA.
:::

:::aufgabe Ejercicio 2 ★★ Conmutador de rangos
<span class="anker" id="aufg-2"></span>

El mecanismo de medida recibe los circuitos de la fig. [3](#abb-3). (a) Calcula $R_1$, $R_2$, $R_3$ para los rangos de corriente 250 µ A, 1 mA, 10 mA y la resistencia interna en cada caso. (b) Calcula $R_1$, $R_2$, $R_3$ para los rangos de tensión 1 V, 10 V, 100 V. (c) Comprueba ambas partes con la frase de «En resumen».

:::loesung
(a) Con [(2.1)](#gl-2-1) paso a paso:

$$\begin{aligned} R_1&=2\,\mathrm{k\Omega}\cdot\tfrac{50}{250-50}=500\,\Omega, & R^*&=2\,\mathrm{k\Omega}\parallel500\,\Omega=400\,\Omega,\\ R_2&=400\,\Omega\cdot\tfrac{250}{1000-250}=133{,}3\,\Omega, & R^{**}&=400\,\Omega\parallel133{,}3\,\Omega=100\,\Omega,\\ R_3&=100\,\Omega\cdot\tfrac{1}{10-1}=11{,}11\,\Omega, & R^{***}&=100\,\Omega\parallel11{,}11\,\Omega=10\,\Omega. \end{aligned}$$

En paralelo, los tres shunts dan 10,05 $\Omega$, como el shunt único del ejemplo.

(b) Cada paso tiene $\alpha=10$: $R_1=2\,\mathrm{k\Omega}\cdot9=18$ k$\Omega$ con $R^*=20$ k$\Omega$, $R_2=20\,\mathrm{k\Omega}\cdot9=180$ k$\Omega$ con $R^{**}=200$ k$\Omega$, $R_3=200\,\mathrm{k\Omega}\cdot9=1{,}8$ M$\Omega$ con $R^{***}=2$ M$\Omega$.

(c) $250\,\mu\text{A}\cdot400\,\Omega=1\,\mathrm{mA}\cdot100\,\Omega=10\,\mathrm{mA}\cdot10\,\Omega=100$ mV. En el voltímetro, $1\,\mathrm{V}/20\,\mathrm{k\Omega}=10\,\mathrm{V}/200\,\mathrm{k\Omega}=100\,\mathrm{V}/2\,\mathrm{M\Omega}=50$ µ A.
:::
:::
