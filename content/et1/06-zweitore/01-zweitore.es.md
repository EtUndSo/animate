---
title: Visión general: Cuadripolos
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160100
summary: Por qué cuatro números sustituyen a toda una red y cada forma de parámetros es solo otra elección
tags: cuadripolo, puerto
lang: es
---

## De qué trata

Entre la fuente y la carga suele haber otra red: un cable, un filtro, un atenuador o un amplificador. Tiene un lado de entrada y un lado de salida, y desde fuera solo cuenta lo que hace con la tensión y la corriente. Una red con dos pares de terminales así se llama __cuadripolo__, y cada par de terminales es un __puerto__. La [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) sustituyó una red en un par de terminales por dos números, la tensión equivalente y la resistencia interna. La pregunta de este capítulo es: *¿Cuántos números hacen falta con dos pares de terminales, y cómo se miden desde fuera?*



**Cómo trabajar con este capítulo.** Cada etapa es un artículo breve con la idea, preguntas típicas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio. Termina una etapa antes de pasar a la siguiente.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Cuadripolo T:** una red en T ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) con la resistencia longitudinal $R_\mathrm{a}=15\,\Omega$ en la entrada, la resistencia transversal $R_\mathrm{b}=20\,\Omega$ hacia la línea inferior continua y la resistencia longitudinal $R_\mathrm{c}=20\,\Omega$ en la salida.

</li>

<li>

⁠**Funcionamiento:** En el puerto 1 hay una fuente de tensión real con $U_\mathrm{q}=9$ V y $R_\mathrm{q}=5\,\Omega$; en el puerto 2, la carga $R_\mathrm{L}=60\,\Omega$.

</li>

<li>

⁠**Amplificador:** un modelo con 2 k$\Omega$ en la entrada, ganancia de corriente 100, 20 k$\Omega$ en la salida y carga de 5 k$\Omega$, mostrado en la etapa [7](hybridform.html#stufe-7).

</li>

<li>

Todas las magnitudes son continuas. El script `rechnung_kap6.py` comprueba todos los números.

</li>

</ul>
:::
