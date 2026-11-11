---
title: Visión general: La transformada de Laplace
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Transformada de Laplace
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Capítulo 2: Transformada de Laplace
order: 3220100
summary: Toda señal como superposición de $\mathrm{e}^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: 
lang: es
---

## De qué trata

**Cómo trabajar con este capítulo.** Cada etapa es un artículo breve con la idea, preguntas típicas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio. Termina una etapa antes de pasar a la siguiente.

:::merke El modelo de cálculo de este capítulo
Todos los ejemplos usan los mismos dos componentes:

<ul>

<li>

un **filtro paso bajo RC** con $RC=1$ s (por ejemplo, $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Su respuesta al impulso y su función de transferencia son

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

con $t$ en s y $p$ en $1/\mathrm{s}$;

</li>

<li>

el **escalón unitario** $s(t)=\varepsilon(t)$ con $S(p)=1/p$ para $\operatorname{Re} p>0$.

</li>

</ul>

:::
