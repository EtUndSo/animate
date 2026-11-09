---
title: Visión general: Serie de Fourier y transformada de Fourier
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230100
summary: Toda señal como superposición de oscilaciones
tags: espectro
lang: es
---

## De qué trata

La [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) ha mostrado que toda señal es una superposición de bloques $\mathrm{e}^{pt}$ y que un sistema LTI solo multiplica cada bloque por un número. La descripción de Fourier usa de ellos únicamente los bloques del eje imaginario, $p=\mathrm{j}2\pi f$: oscilaciones puras $\mathrm{e}^{\mathrm{j}2\pi ft}$, que ni crecen ni decaen. Esto tiene una gran ventaja. Una oscilación tiene una frecuencia que se puede oír, medir y filtrar. El __espectro__ $S(f)$ indica con qué amplitud y con qué fase está contenida cada frecuencia en la señal.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Onda cuadrada** entre 0 y 1 con periodo $T=2\pi$ s y ciclo de trabajo $\frac12$: 1 para $|t|\le T/4$, 0 para $T/4<|t|\le T/2$, prolongada periódicamente. Frecuencia fundamental $F=1/T=0{,}159$ Hz, es decir, $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**Paso bajo RC** con $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. En el $k$-ésimo armónico de la onda cuadrada (su componente de frecuencia $kF$), $2\pi kF\cdot RC=k$, es decir, $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Pulso rectangular** $\operatorname{rect}(t)$ y $\operatorname{si}(x)=\sin(x)/x$.

</li>

</ul>

El script `rechnung_kap3.py` recalcula los números y las curvas.
:::
