---
title: Etapa 1: Clases de señales y muestreo ideal
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3240200
summary: ¿Qué tipos de señales hay y cómo se describe matemáticamente el muestreo?
tags: analógica, en tiempo discreto, digital, muestreador ideal
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
¿Qué tipos de señales hay y cómo se describe matemáticamente el muestreo?
:::

**Cuatro clases.** El tiempo y la amplitud pueden ser, cada uno, continuos o discretos. Una señal __analógica__ es continua en ambos. Una señal __en tiempo discreto__ solo tiene valores en los instantes $nT$, pero estos con precisión arbitraria. Una señal __digital__ está además escalonada en amplitud (cuantizada), porque un ordenador solo puede representar una cantidad finita de números. Este capítulo trata la discretización del tiempo. La cuantización de la amplitud es un tema aparte.

**Del muestreador real al ideal.** Un muestreador real cierra un interruptor en cada periodo de muestreo durante el breve tiempo $T_0$:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

Si $T_0$ se hace cada vez más corto, solo quedan los valores $s(nT)$. Matemáticamente, el rectángulo se sustituye por un impulso de Dirac. Este es el __muestreador ideal__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

La señal muestreada es un tren de impulsos de Dirac, cada uno con una muestra como peso. El segundo paso es la propiedad de muestreo (de criba) $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. De esta forma, las señales muestreadas pueden tratarse con todas las herramientas para señales continuas.
