---
title: Etapa 2: Aprovechar la simetría
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1150400
summary: Algunas redes no contienen grupos.
tags: semicircuito
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Algunas redes no contienen grupos. La simetría proporciona entonces nudos de igual potencial, y al unirlos surgen grupos.
:::

**La idea.** Si dos nudos están al mismo potencial, la tensión entre ellos es cero. Un cable entre ellos no conduce, por tanto, ninguna corriente, y no cambia nada si se añade. A la inversa, una rama sin corriente se puede cortar. La simetría revela qué nudos son esos sin necesidad de calcular nada.

:::satz Teorema 2.1 (Dos reglas de simetría)
<span class="anker" id="satz-2-1"></span>

Para una red de resistencias con los terminales A y B se cumple:

<ol>

<li>

Si la red coincide consigo misma al reflejarla o girarla y A y B permanecen en su sitio, los nudos que se superponen tienen el mismo potencial. Se pueden unir. Una resistencia entre ellos no conduce corriente.

</li>

<li>

Si la red coincide consigo misma al reflejarla y A y B intercambian sus puestos, todo punto del eje de simetría está en el valor medio $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$. Se pueden unir todos y se calcula solo un lado, el __semicircuito__:

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{AB}=2\,R_\mathrm{A,eje}. \tag{2.1}$$

</li>

</ol>
:::

⁠**Cómo leerlo:** $R_\mathrm{A,eje}$ es la resistencia entre A y el eje unido en un solo nudo. Una resistencia que cruza el eje se divide en dos resistencias mitad, y su centro está en el eje. Una resistencia a lo largo del eje tiene ambos extremos al mismo potencial y no conduce corriente. **Validez:** La simetría debe abarcar también los valores. Una sola resistencia distinta la rompe.

:::herleitung Los potenciales se deducen de la simetría
Regla 1: La red reflejada tiene los mismos componentes, los mismos terminales y la misma tensión, es decir, las mismas ecuaciones. Estas tienen exactamente una solución. Por tanto, dos nudos que se superponen deben tener el mismo potencial.

Regla 2: Sea el punto de referencia el del centro, es decir, $\varphi_\mathrm{A}=+\frac12U$ y $\varphi_\mathrm{B}=-\frac12U$. La reflexión intercambia A y B, de modo que actúa como invertir la polaridad de la tensión. En una red lineal, invertir la polaridad invierte todo potencial (etapa [8](uberlagerung.html#stufe-8)). Para un punto $P$ y su imagen especular $P'$ se cumple, por tanto, $\varphi(P')=-\varphi(P)$. Un punto del eje es su propia imagen especular, así que $\varphi=-\varphi$ y con ello $\varphi=0$, el valor medio. Las dos mitades son iguales y están en serie, lo que da [(2.1)](#gl-2-1).
:::

:::abbildung et1/k5symmetrie 2
Siete resistencias iguales de 14 $\Omega$ cada una. A la izquierda, la red con los potenciales para 16 V en A. El eje de simetría pasa por L y por el centro de la resistencia entre E y F, que por eso se divide en dos veces 7 $\Omega$. A la derecha, el semicircuito.
:::

::::beispiel
En la fig. [2](#abb-2), la reflexión intercambia A y B, así como E y F, y se aplica la regla 2. En el semicircuito, entre E y el eje hay $14\,\Omega\parallel7\,\Omega=4{,}67\,\Omega$. Con el camino de A a E son 18,67 $\Omega$. En paralelo con la rama izquierda da $R_\mathrm{A,eje}=14\,\Omega\parallel18{,}67\,\Omega=8\,\Omega$, es decir, $R_\mathrm{AB}=16\,\Omega$, otra vez la carga del modelo de referencia. **Comprobación** con los potenciales de la figura: de A a L circulan $8\,\mathrm{V}/14\,\Omega=0{,}571$ A, de A a E circulan $6\,\mathrm{V}/14\,\Omega=0{,}429$ A. La suma es 1 A, como exige $16\,\mathrm{V}/16\,\Omega$.
::::

:::abbildung et1/k5wuerfel 3
Cubo de doce resistencias iguales con la tensión aplicada en la diagonal espacial. Un giro alrededor de esta diagonal transforma entre sí los tres vecinos de A, y lo mismo los tres vecinos de B. Al unirlos surge una cadena de tres grupos.
:::

**El cubo de resistencias.** Doce aristas de $R=12\,\Omega$ cada una, los terminales en vértices opuestos (fig. [3](#abb-3)). Por la regla 1, los tres vecinos de A están al mismo potencial, y también los tres vecinos de B. Entre estos dos tríos discurren seis aristas. Surge una cadena:

$$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R=10\,\Omega.$$

Con 5 V circulan 0,5 A. Se reparten en tres aristas con 167 mA cada una, luego en seis con 83 mA cada una y después otra vez en tres.

:::frage ¿Unir los nudos no es una intervención en el circuito?
En el dibujo sí, en las corrientes no. Por el cable nuevo solo podría circular corriente si hubiera tensión entre sus extremos. No la hay. Por eso no cambia ninguna corriente en el resto de la red. El procedimiento solo vale mientras los potenciales sean realmente iguales.
:::

:::aufgabe Ejercicio 2 ★ Predecir la ausencia de corriente
<span class="anker" id="aufg-2"></span>

De A salen 10 $\Omega$ hacia el nudo C y 30 $\Omega$ hacia el nudo D; de C salen 20 $\Omega$ y de D salen 60 $\Omega$ hacia B. Entre C y D hay una resistencia transversal $R_\mathrm{Q}$ (el puente de la [Parte 4](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). (a) Demuestra que C y D tienen el mismo potencial, incluso sin simetría. (b) Calcula $R_\mathrm{AB}$ para $R_\mathrm{Q}\to\infty$ y para $R_\mathrm{Q}\to0$. (c) ¿Qué se deduce para $R_\mathrm{Q}=47\,\Omega$?

:::loesung
(a) Sin corriente por $R_\mathrm{Q}$, ambas ramas son divisores de tensión con la misma relación: $\frac{20}{10+20}=\frac{60}{30+60}=\frac23$. C y D están entonces al mismo potencial, y por $R_\mathrm{Q}$ realmente no circula corriente. Esa es la única solución de la red (el equilibrio de la [Parte 4](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)).

(b) $R_\mathrm{Q}\to\infty$: $(10\,\Omega+20\,\Omega)\parallel(30\,\Omega+60\,\Omega)=22{,}5\,\Omega$. $R_\mathrm{Q}\to0$: $10\,\Omega\parallel30\,\Omega+20\,\Omega\parallel60\,\Omega=7{,}5\,\Omega+15\,\Omega=22{,}5\,\Omega$.

(c) Lo mismo: 22,5 $\Omega$. La resistencia transversal no conduce corriente, y su valor no influye.
:::
:::

:::aufgabe Ejercicio 3 ★★ El cubo por la diagonal de una cara
<span class="anker" id="aufg-3"></span>

Aplica la tensión a dos vértices de la misma cara del cubo que estén diagonalmente opuestos, $R=12\,\Omega$. Pista: ayudan las dos reglas. ¿Qué cuatro vértices están en el valor medio? Calcula $R_\mathrm{AB}$.

:::loesung
Sean A y B los terminales. C y D son los dos vértices que son vecinos de A y de B. Sobre C y D están, en la otra cara, E y F; sobre A está P, sobre B está Q. Si se refleja en el plano perpendicular a la unión AB que pasa por su punto medio, A y B intercambian sus puestos, y también P y Q. C, D, E, F están en este plano, luego por la regla 2 están en el valor medio.

Semicircuito de A al eje: por C y por D, $R$ cada uno, en conjunto $\frac R2$. Por P: $R$, luego de P a E y a F, $R$ cada uno, en conjunto $R+\frac R2=\frac32R$. En paralelo: $\frac R2\parallel\frac32R=\frac38R$. Con ello, $R_\mathrm{AB}=\frac34R=9\,\Omega$.
:::
:::
