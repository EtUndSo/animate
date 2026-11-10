---
title: Etapa 9: Interconexión
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Cuadripolos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Capítulo 6: Cuadripolos
order: 1161100
summary: La etapa 8 mostró que la cadena encaja con la forma A.
tags: 
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
La etapa [8](kettenform.html#stufe-8) mostró que la cadena encaja con la forma A. Esta etapa responde a la pregunta en general: ¿qué forma encaja con qué interconexión?
:::

**La idea.** Si se unen dos cuadripolos, en cada puerto comparten o bien la corriente (serie) o bien la tensión (paralelo). La magnitud compartida es igual para ambas partes, y la otra se suma. Eso dice qué forma encaja: las magnitudes comunes pertenecen a las causas; las sumadas, a los efectos. Entonces, a la derecha aparece lo mismo para ambas partes, y los parámetros se suman.

:::satz Teorema 9.1 (Interconexión de dos cuadripolos)
<span class="anker" id="satz-9-1"></span>

Si en ambas partes se mantiene la condición de puerto, se cumple:

| Conexión (puerto 1, puerto 2) | igual para ambas | se suma | Regla |
|---|---|---|---|
| serie, serie | $I_1$, $I_2$ | $U_1$, $U_2$ | $\mathbf Z=\mathbf Z'+\mathbf Z''$ |
| paralelo, paralelo | $U_1$, $U_2$ | $I_1$, $I_2$ | $\mathbf Y=\mathbf Y'+\mathbf Y''$ |
| serie, paralelo | $I_1$, $U_2$ | $U_1$, $I_2$ | $\mathbf H=\mathbf H'+\mathbf H''$ |
| cadena | $U_2'=U_1''$, $-I_2'=I_1''$ | nada | $\mathbf A=\mathbf A'\mathbf A''$ |
:::

⁠**Cómo leerlo:** El esquema dice qué magnitudes son iguales; la tabla dice qué forma se suma (fig. [11](#abb-11)). De ahí viene el segundo nombre de la matriz H, matriz serie-paralelo. La conexión «paralelo, serie» es el caso que falta. Le corresponde la forma híbrida inversa, con $U_1$ e $I_2$ como causas, que se obtiene con la inversa de $\mathbf H$.

:::herleitung Por qué se suman los parámetros
En serie, serie, ambas partes llevan las mismas corrientes: $\mathbf I'=\mathbf I''=\mathbf I$. Por tanto, $\mathbf U=\mathbf U'+\mathbf U''=\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$. En paralelo vale lo mismo con los papeles intercambiados. En serie, paralelo, la columna de causas $(I_1,\,U_2)$ es igual para ambas, y la columna de efectos $(U_1,\,I_2)$ es la suma de ambas columnas de efectos.
:::

:::abbildung et1/k6zusammen 11
Tres interconexiones. Izquierda, serie, serie: corrientes iguales, Z se suma. Centro, paralelo, paralelo: tensiones iguales, Y se suma. Derecha, serie, paralelo: $I_1$ y $U_2$ iguales, H se suma.
:::

::::beispiel
⁠**Serie:** El propio cuadripolo T es una conexión en serie de dos resistencias longitudinales separadas y una resistencia transversal:

$$\mathbf Z=\begin{pmatrix}15&0\\0&20\end{pmatrix}\Omega+\begin{pmatrix}20&20\\20&20\end{pmatrix}\Omega=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**Paralelo:** Si se coloca una resistencia de 100 $\Omega$ del terminal 1 al terminal 2 sobre el cuadripolo T, a $\mathbf Y$ se le añade la conductancia longitudinal:

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}+\begin{pmatrix}10&-10\\-10&10\end{pmatrix}\mathrm{mS}=\begin{pmatrix}50&-30\\-30&45\end{pmatrix}\mathrm{mS}.$$

Comprobación: con el puerto 2 en cortocircuito, $1/Y_{11}=20\,\Omega$, y directamente es $25\,\Omega\parallel100\,\Omega=20\,\Omega$.

**Cuándo falla la regla.** Las reglas suponen que cada parte conserva por sí sola la condición de puerto. En la cadena esto es seguro, porque para la parte delantera, la parte trasera junto con la carga es un dipolo. Dos tripolos con línea de masa común también se pueden conectar en paralelo: en ellos, 1$'$ y 2$'$ coinciden en un punto, y solo cuenta la suma de las corrientes de retorno. En serie hace falta precaución. Si se apilan dos cuadripolos T con sus líneas de masa, la línea de masa del superior cortocircuita los dos terminales superiores del inferior. Una parte de la corriente del puerto 1 pasa entonces en la T inferior por $R_\mathrm{c}$, y la condición de puerto se rompe. En lugar de $Z_{11}=70\,\Omega$ se mide $35\,\Omega+15\,\Omega\parallel20\,\Omega+20\,\Omega=63{,}6\,\Omega$. Remedio: se invierte en espejo la T inferior, de modo que solo queden unidas las dos líneas de masa. Entonces ambos siguen siendo tripolos, y la regla da los 70 $\Omega$ correctos.

⁠**Caso límite:** Dos cuadripolos iguales en paralelo tienen la mitad de la matriz $\mathbf Z$; resistencias iguales en paralelo dan la mitad de la resistencia. En serie, $\mathbf Z$ se duplica.

:::frage ¿Por qué en serie no se suma también la matriz de cadena?
Porque en serie $I_1$ es igual para ambas partes, pero $U_1$ no. En la forma en cadena, $U_1$ está junto con $I_1$ en el lado izquierdo, y a la derecha estarían las magnitudes de salida. La columna derecha sería distinta para ambas partes, y nada se podría agrupar.
:::

:::aufgabe Ejercicio 9 ★★ ¿Qué forma encaja?
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Dos cuadripolos T iguales se conectan en paralelo, paralelo. ¿Cuánto vale $\mathbf Z$ del circuito? ¿Por qué aquí es admisible el cálculo?

</li>

<li>

Dos cuadripolos T iguales, el inferior invertido en espejo, están en serie, serie. ¿Cuánto vale $\mathbf Z$?

</li>

<li>

Se conoce la matriz híbrida del cuadripolo T. ¿Cuánto vale $\mathbf H$ de dos cuadripolos iguales en serie, paralelo (suponiendo la condición de puerto)?

</li>

<li>

Al cuadripolo T se le añade una resistencia transversal de 10 $\Omega$ en serie, serie. ¿Qué $\mathbf Z$ resulta, y qué red en T le corresponde?

</li>

</ol>

:::loesung
(a) $\mathbf Y$ se duplica, así que $\mathbf Z$ se reduce a la mitad: $Z_{11}=17{,}5\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=20\,\Omega$. Ambos son tripolos con línea de masa común, y los puertos siguen siendo puertos. (b) $\mathbf Z$ se duplica: 70, 40, 40, 80 $\Omega$. (c) $\mathbf H$ se duplica: $H_{11}=50\,\Omega$, $H_{12}=1$, $H_{21}=-1$, $H_{22}=50$ mS. (d) $Z_{11}=45\,\Omega$, $Z_{12}=Z_{21}=30\,\Omega$, $Z_{22}=50\,\Omega$. Es una T con $R_\mathrm{a}=15\,\Omega$, $R_\mathrm{b}=30\,\Omega$, $R_\mathrm{c}=20\,\Omega$: la resistencia transversal queda en serie con $R_\mathrm{b}$, porque lleva la misma corriente suma.
:::
:::
