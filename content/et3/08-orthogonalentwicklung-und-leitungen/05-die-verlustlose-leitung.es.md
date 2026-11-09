---
title: Etapa 4: La línea de transmisión sin pérdidas
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Desarrollo ortogonal y líneas de transmisión
order: 3280500
summary: Sin pérdidas ( R'=G'=0 ), la impedancia característica y la velocidad se vuelven independientes de la frecuencia.
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Sin pérdidas ($R'=G'=0$), la impedancia característica y la velocidad se vuelven independientes de la frecuencia. Entonces la solución en forma de ondas vale para señales cualesquiera, no solo para oscilaciones sinusoidales.
:::

Con $R'=G'=0$ se tiene $\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$: no hay atenuación ($\alpha=0$), y $\beta$ es proporcional a $f$. De ahí:

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz Teorema 4.1 (Solución de d'Alembert)
<span class="anker" id="satz-4-1"></span>

Toda solución de la ecuación de onda [(4.1)](#gl-4-1) tiene la forma

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{prog}(s-vt)+u_\mathrm{reg}(s+vt) \tag{4.2}$$

con funciones cualesquiera (dos veces derivables) $u_\mathrm{prog}$ (progresiva) y $u_\mathrm{reg}$ (regresiva).
:::

⁠**Cómo leerlo:** una forma de señal cualquiera se propaga sin cambios a lo largo de la línea con la velocidad $v$. Esto se debe a que todas las componentes de frecuencia son igual de rápidas y se atenúan igual de poco: la línea es un sistema sin distorsión en el sentido de la [parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), con el retardo $l/v$. La ecuación de onda para $u$ se obtiene de [(2.1)](die-leitungsgleichungen.html#gl-2-1) derivando la primera ecuación respecto a $s$ y la segunda respecto a $t$, y eliminando $i$.

::::beispiel cable coaxial
$Z=50\,\Omega$ y $C'=100$ pF/m dan $L'=Z^2C'=250$ nH/m y $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, dos tercios de la velocidad de la luz (debido al dieléctrico del cable). Una señal tarda 50 ns en recorrer 10 m de cable. Si el cable se termina con 75 $\Omega$ en lugar de 50 $\Omega$, $r=\frac{75-50}{75+50}=0{,}2$: el 20 % de la amplitud de tensión vuelve como eco.
::::

:::ltspice Reflexiones en una línea
⁠**Esquema:** fuente `voltage` con `PULSE(0 2 0 1n 1n 10n 1)` y una resistencia interna `res` con `50` hacia el nodo `in`. Desde `in`, una línea sin pérdidas `tline` con `Td=50n Z0=50` (el cable coaxial de 10 m del ejemplo) hasta el nodo `end`, y ahí `res` con `{RE}` a masa. Como la resistencia interna es igual a $Z$, sale una onda de 1 V, y el eco se absorbe por completo en la fuente.

⁠**Directivas:** `.param RE=75`, `.step param RE list 1m 50 75 1G` (casi cortocircuito, adaptación, 75 $\Omega$, casi circuito abierto), `.tran 0 200n 0 0.1n`.

⁠**Lo que ves:** en `in`, primero el pulso de 1 V. Al cabo de $2\cdot50\,\mathrm{ns}=100$ ns vuelve el eco con la altura $r\cdot1$ V: $-1$; $0$; $0{,}2$ y $+1$, exactamente $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. En `end` aparece, a partir de 50 ns, la suma de la onda incidente y la reflejada, $(1+r)\cdot1$ V. Ajusta `Td` y `Z0` a tus valores del ejercicio [4](#aufg-4)(a), pon `RE` a 100 y compara la altura del eco con tu resultado del ejercicio [4](#aufg-4)(b).
:::

:::aufgabe Ejercicio 3 ★★ Comprobar d'Alembert
<span class="anker" id="aufg-3"></span>

Demuestra por sustitución que $u(s,t)=u_\mathrm{prog}(s-vt)$ resuelve la ecuación de onda [(4.1)](#gl-4-1) con $v=1/\sqrt{L'C'}$. ¿Cómo se relaciona la corriente correspondiente con la tensión? Pista: primera ecuación de la línea con $R'=0$.

:::loesung
Con $x=s-vt$: $\frac{\partial^2u}{\partial s^2}=u_\mathrm{prog}''(x)$ y $\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{prog}''(x)$. La ecuación de onda exige $u''=L'C'v^2u''$, es decir, $v^2=\frac{1}{L'C'}$. Corriente: con $R'=0$ se tiene $\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$, es decir, $u_\mathrm{prog}'(x)=-L'\frac{\partial i}{\partial t}$. El planteamiento $i=u_\mathrm{prog}(x)/Z$ da $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{prog}$, y esto encaja, porque $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$. En la onda progresiva, la tensión y la corriente están en todas partes en la razón $Z$.
:::
:::

:::aufgabe Ejercicio 4 ★★ Cable y terminación
<span class="anker" id="aufg-4"></span>

Un cable sin pérdidas tiene $L'=300$ nH/m y $C'=120$ pF/m.

<ol class="al">

<li>

Calcula $Z$, $v$ y el tiempo de propagación para 5 m.

</li>

<li>

¿Con qué resistencia hay que terminarlo para que no se refleje nada? ¿Qué coeficiente de reflexión resulta con 100 $\Omega$?

</li>

<li>

¿Hasta qué frecuencia pueden tratarse todavía los 5 m como «cortos», si la línea debe medir como máximo una décima parte de la longitud de onda?

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2{,}5\cdot10^3}\,\Omega=50\,\Omega$. $v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3{,}6\cdot10^{-17}}}\,\mathrm{m/s}=1{,}67\cdot10^8$ m/s. Tiempo de propagación para 5 m: 30 ns.

(b) Con $Z=50\,\Omega$. Con 100 $\Omega$: $r=\frac{100-50}{150}=\frac13$.

(c) $\lambda=v/f\ge50$ m; por tanto, $f\le\frac{1{,}67\cdot10^8}{50}\,\mathrm{Hz}=3{,}3$ MHz.
:::
:::
