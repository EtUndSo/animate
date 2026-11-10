---
title: Etapa 6: Distribución conjunta, independencia, incorrelación
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3270700
summary: Dos variables aleatorias a la vez: ¿cuándo están relacionadas y qué se deduce de ello para su suma?
tags: distribución conjunta, estadísticamente independientes, incorreladas
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Dos variables aleatorias a la vez: ¿cuándo están relacionadas y qué se deduce de ello para su suma?
:::

La __distribución conjunta__ de dos variables es $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{y}\ g\le y]$, y su densidad, $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. De ella se obtienen las distribuciones individuales ($P_{sg}(x,\infty)=P_s(x)$) y la correlación $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. En procesos conjuntamente estacionarios, todo depende solo del desplazamiento temporal $\tau$ entre $s(t)$ y $g(t+\tau)$.

:::definition Definición 6.1 (Independientes, incorreladas)
<span class="anker" id="satz-6-1"></span>

$s$ y $g$ son __estadísticamente independientes__ si $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Son __incorreladas__ si $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

De la independencia se deduce la incorrelación: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. Al revés, no: incorreladas solo significa que no existe una relación *lineal* (ejercicio [5](#aufg-5)).

**La suma de dos variables independientes.** La suma $s=f+g$ toma el valor $x$ cuando $f=u$ y $g=x-u$, para algún $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{independientes}). \tag{6.1}$$

Es la convolución del [capítulo 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), allí con el ejemplo de los dados. Dos variables con distribución uniforme dan una densidad triangular; tres, una que ya tiene casi forma de campana (fig. [2](#abb-2)).

:::abbildung et3/k7summen 2
Densidades de probabilidad de sumas de variables aleatorias independientes con distribución uniforme en $[-\frac12,\frac12]$. La suma de tres ya está cerca de la curva de Gauss con la misma varianza (en $x=0$: 0,75 frente a 0,80).
:::

:::aufgabe Ejercicio 5 ★★ Incorreladas, pero dependientes
<span class="anker" id="aufg-5"></span>

$s$ tiene distribución uniforme en $[-1,1]$ y $g=s^2$. Demuestra que $s$ y $g$ están incorreladas, aunque $g$ está completamente determinada por $s$.

:::loesung
$m_s=0$ y $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$; por tanto, $\mu_{sg}=0-0\cdot m_g=0$: incorreladas. Aun así, $s$ fija el valor de $g$. La relación es cuadrática, y una correlación solo capta relaciones lineales: para $s$ positivo, $g$ crece con $s$; para $s$ negativo, decrece; en promedio, ambas tendencias se compensan.
:::
:::
