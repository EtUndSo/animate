---
title: Etapa 9: Qué hace la tensión con una carga
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1111100
summary: Esta etapa reúne campo, potencial y tensión en un solo electrón: ¿qué fuerza actúa, qué energía gana, a qué velocidad llega?
tags: electronvoltio
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Esta etapa reúne campo, potencial y tensión en un solo electrón: ¿qué fuerza actúa, qué energía gana, a qué velocidad llega?
:::

**La idea.** Un electrón se desprende de la placa B y parte del reposo. El campo apunta de A a B. Por $\vec F=Q\vec E$ y $Q=-e$, la fuerza actúa en sentido contrario al campo, hacia la placa A. Es igual en todas partes, así que la aceleración es constante y vale [(1.4)](groen-kraft-und-arbeit.html#gl-1-4). Por el camino, la energía potencial se convierte en energía cinética. El electrón va hacia el potencial alto, pero su energía $Q\varphi$ disminuye, porque $Q$ es negativa.

:::satz Teorema 9.1 (Carga en el campo)
<span class="anker" id="satz-9-1"></span>

En el campo electrostático, la suma de energía cinética y energía potencial permanece constante:

<span class="anker" id="gl-9-1"></span>
$$\tfrac12m\,v^2+Q\,\varphi=\text{constante}. \tag{9.1}$$

Una carga que recorre desde el reposo la tensión $U$ alcanza, en un campo uniforme de longitud $d$,

<span class="anker" id="gl-9-2"></span>
$$v=\sqrt{\frac{2\,|Q\,U|}{m}},\qquad a=\frac{|Q|\,E}{m},\qquad t=\frac{2\,d}{v}. \tag{9.2}$$
:::

:::herleitung Teorema de la energía y tiempo de vuelo
El trabajo del campo se convierte por completo en energía cinética: $\frac12mv_2^2-\frac12mv_1^2=W_{12}=Q(\varphi_1-\varphi_2)$. Reordenando se obtiene [(9.1)](#gl-9-1). Con $v_1=0$ resulta $|Q\,U|=\frac12m\,v^2$. Con aceleración constante, la velocidad media es $v/2$, así que $t=d/(v/2)$.
:::

⁠**Cómo leerlo:** $m$ es la masa en kg; $\varphi$, el potencial en el lugar. En $v$ no aparece el camino: solo la tensión determina la energía. **Validez y simplificaciones:** Las ecuaciones valen en el vacío. En el aire, un electrón choca con una molécula tras solo fracciones de micrómetro. El peso $m_\mathrm{e}g=8{,}9\cdot10^{-30}$ N se omite: es $5{,}4\cdot10^{13}$ veces menor que la fuerza del campo. Además debe cumplirse $v\ll c$. Aquí $v$ es solo el 0,6 % de la velocidad de la luz $c$, y la corrección de la energía cinética es del 0,003 %.

:::abbildung et1/k1elektron 11
Izquierda: el electrón parte de la placa B y va en contra del campo hacia la placa A. Derecha: de $x=3$ mm a $x=0$, la energía cinética crece hasta $1{,}44\cdot10^{-18}$ J y la energía potencial baja en la misma cantidad, punto de referencia B. La suma sigue siendo cero.
:::

::::beispiel
Para el electrón en el par de placas,

$$\begin{aligned} F&=e\,E=4{,}81\cdot10^{-16}\,\mathrm{N},\qquad a=\frac{F}{m_\mathrm{e}}=5{,}28\cdot10^{14}\,\mathrm{m/s^2},\qquad W=e\,U=1{,}44\cdot10^{-18}\,\mathrm{J},\\ v&=\sqrt{\frac{2\cdot1{,}44\cdot10^{-18}\,\mathrm{J}}{9{,}109\cdot10^{-31}\,\mathrm{kg}}}=1{,}78\cdot10^{6}\,\mathrm{m/s},\qquad t=\frac{2\cdot3\,\mathrm{mm}}{v}=3{,}37\,\mathrm{ns}. \end{aligned}$$

Un protón va de A a B. Gana la misma energía, pero es 1836 veces más pesado: $v=4{,}15\cdot10^4$ m/s, $\sqrt{1836}=42{,}9$ veces más lento, tiempo de vuelo 144 ns.
::::

⁠**En resumen:** si una carga recorre en el vacío una tensión, su energía cinética cambia en carga por tensión, independientemente del camino y de la distancia.

⁠**Casos límite:** Para $U\to0$, $v\to0$. El doble de separación entre placas con la misma tensión reduce $E$ y $a$ a la mitad, pero no cambia $v$: el electrón se acelera menos, pero durante más tiempo, y tarda 6,74 ns. Cuatro veces la tensión da el doble de velocidad.

:::frage ¿De verdad va el electrón en contra del campo? Un campo empuja a las cargas en su sentido, ¿no?
Empuja a las cargas *positivas* en su sentido; así se define el sentido de $\vec E$. Toda carga se mueve por sí sola hacia donde su energía potencial $Q\varphi$ se hace menor. Para el electrón, ese es el potencial más alto.
:::

:::zusatz El electronvoltio
La energía que gana una carga elemental al recorrer 1 V se llama __electronvoltio__: $1\,\mathrm{eV}=1{,}602\cdot10^{-19}$ J. El electrón del ejemplo gana 9 eV.
:::

:::aufgabe Ejercicio 10 ★★★ Electrón contra el campo
<span class="anker" id="aufg-10"></span>

Un electrón sale de la placa A del modelo de referencia con $v_0=1{,}0\cdot10^6$ m/s hacia la placa B.

<ol class="al">

<li>

¿Llega a la placa B? Compara su energía cinética con la energía necesaria.

</li>

<li>

¿En qué lugar $x$ da la vuelta? Calcula una vez con el teorema de la energía y otra con [(1.4)](groen-kraft-und-arbeit.html#gl-1-4).

</li>

<li>

¿Cuándo vuelve a estar en la placa A, y con qué velocidad?

</li>

<li>

¿Qué velocidad inicial necesitaría para llegar justo a B?

</li>

</ol>

:::loesung
(a) $W_\mathrm{kin}=\frac12m_\mathrm{e}v_0^2=4{,}55\cdot10^{-19}$ J. Hasta B harían falta $e\cdot9\,\mathrm{V}=1{,}44\cdot10^{-18}$ J. No llega a B. (b) Teorema de la energía: avanza hasta agotar $\Delta\varphi=W_\mathrm{kin}/e=2{,}84$ V. Con 3 V/mm, $x=0{,}948$ mm. Con [(1.4)](groen-kraft-und-arbeit.html#gl-1-4): frenado $a=5{,}28\cdot10^{14}\,\mathrm{m/s^2}$, inversión en $t=v_0/a$, es decir, $x=v_0^2/(2a)=0{,}948$ mm.

(c) Ida y vuelta: $t=2v_0/a=3{,}79$ ns. El potencial vuelve a ser el mismo, así que según [(9.1)](#gl-9-1) $v=v_0=1{,}0\cdot10^6$ m/s, en sentido contrario. (d) Justo la energía del ejemplo: $v_0=1{,}78\cdot10^6$ m/s.
:::
:::
