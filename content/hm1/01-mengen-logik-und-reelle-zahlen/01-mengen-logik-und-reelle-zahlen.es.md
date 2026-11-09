---
title: Visión general: Conjuntos, lógica y números reales
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210100
summary: Qué hay que suponer sobre los números y por qué la raíz cuadrada de 2 no es una fracción
tags: conjunto, proposición, axioma, cuerpo, orden, completitud, inducción matemática, valor absoluto
lang: es
---

## De qué trata

En la escuela se aprenden reglas como $(-1)\cdot(-1)=1$ o «no se puede dividir por cero». ¿Por qué se cumplen? La costumbre como justificación no llega muy lejos: en los números complejos ([Parte 2](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) deja de valer la regla «los cuadrados no son negativos», y todos los límites (Parte 4) dependen de una propiedad de los números que en la escuela nunca se menciona. Se ve en un solo número: la diagonal de un cuadrado de lado 1 mide $\sqrt2$, y ninguna fracción tiene ese valor. La pregunta de este capítulo es: *¿Qué hay que suponer exactamente sobre los números para que todas las reglas de cálculo se puedan demostrar, y qué distingue a los números reales de las fracciones?*

La respuesta necesita dos herramientas y una lista breve de supuestos. Un __conjunto__ agrupa objetos; una __proposición__ es una oración que es verdadera o falsa. Un __axioma__ es un supuesto básico que se establece y no se demuestra. Bastan tres grupos de axiomas: un __cuerpo__ es un conjunto en el que la suma y el producto funcionan según las reglas conocidas. El __orden__ establece qué números son positivos. La __completitud__ dice que la recta numérica no tiene huecos. A esto se añaden la __inducción matemática__, el método de demostración para proposiciones sobre todos los números naturales, y el __valor absoluto__, la distancia de un número al cero.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Conjuntos:** $G=\{1,2,\dots,12\}$, y dentro de él $A=\{1,2,3,4,6,12\}$ (divisores de 12) y $B=\{2,3,5,7,11\}$ (números primos).

</li>

<li>

⁠**Proposición:** $\mathcal E(n):=(n\ge7\Rightarrow n>5)$ para números naturales $n$.

</li>

<li>

⁠**Conjunto con hueco:** $D=\{x\in\mathbb{Q}:x>0,\ x^2<2\}$, las fracciones positivas con cuadrado menor que 2.

</li>

<li>

⁠**Números para desigualdades:** $x=-3$, $y=5$ para el valor absoluto; $x=2$, $y=8$ para las medias; las listas $\vec x=(3,4)$, $\vec y=(1,2)$ para Cauchy-Schwarz. El script `rechnung_kap1.py` comprueba todos los números y tablas.

</li>

</ul>
:::
