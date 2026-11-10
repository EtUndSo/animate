---
title: Etapa 3: Ondas con excitación sinusoidal
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Desarrollo ortogonal y líneas de transmisión
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Capítulo 8: Desarrollo ortogonal y líneas de transmisión
order: 3280400
summary: Con fasores, las ecuaciones en derivadas parciales se convierten en una ecuación ordinaria en la posición.
tags: ecuación de onda, constante de propagación, impedancia característica, constante de atenuación, coeficiente de reflexión
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Con fasores, las ecuaciones en derivadas parciales se convierten en una ecuación ordinaria en la posición. Su solución son dos ondas que se propagan en sentidos opuestos.
:::

Con $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$, y lo mismo para $i$, $\frac{\partial}{\partial t}$ se convierte en $\mathrm{j}2\pi f$:

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

Derivando la primera ecuación y sustituyendo la segunda resulta la __ecuación de onda__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$.

:::satz Teorema 3.1 (Onda incidente y onda reflejada)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

con la __constante de propagación__ y la __impedancia característica__

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**Cómo leerlo:** con $\gamma=\alpha+\mathrm{j}\beta$, el primer sumando se convierte, en el dominio del tiempo, en $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$: una onda que se propaga en el sentido de $s$ creciente y que, al hacerlo, decae con la __constante de atenuación__ $\alpha$. Un paso por cero se desplaza con la velocidad $v=2\pi f/\beta$; la longitud de onda es $\lambda=2\pi/\beta$. El segundo sumando se propaga en sentido contrario. $Z$ es la razón entre tensión y corriente en una sola onda. Las condiciones de contorno fijan las constantes $\underline U_1$, $\underline U_2$, por ejemplo la tensión y la corriente al principio de la línea: $\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$.

**Reflexión en el extremo.** Si la línea está terminada en su extremo ($s=l$) con una resistencia $R_\mathrm E=\underline U_e/\underline I_e$, la tensión puede escribirse como

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

El primer sumando es la onda incidente; el segundo, la onda reflejada, que vuelve desde el extremo. Para $R_\mathrm E=Z$ desaparece la onda reflejada: una terminación (carga) con la impedancia característica absorbe por completo la onda que llega, como si la línea continuara indefinidamente. La razón entre las dos ondas en el extremo es el __coeficiente de reflexión__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$ (además: cortocircuito, $r=-1$; circuito abierto, $r=+1$).

:::frage ¿Por qué una terminación incorrecta no molesta en las líneas cortas?
Porque entonces la onda reflejada vuelve casi de inmediato. Si el tiempo de propagación a lo largo de la línea es pequeño frente a la duración de los cambios de la señal (línea corta frente a la longitud de onda), la onda incidente y la reflejada se superponen prácticamente a la vez, y solo se nota la resistencia de terminación. Solo cuando el tiempo de propagación se vuelve comparable, por ejemplo con señales digitales rápidas o en alta frecuencia, las reflexiones aparecen como ecos y distorsionan la señal.
:::
