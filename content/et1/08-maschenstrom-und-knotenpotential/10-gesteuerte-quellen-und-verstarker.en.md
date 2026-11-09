---
title: Stage 8: Controlled sources and amplifiers
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Mesh Current and Node Voltage Analysis
order: 1181000
summary: Amplifiers contain controlled sources (Part 6).
tags: voltage-controlled current source, transconductance, voltage gain, negative feedback, transimpedance
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Amplifiers contain controlled sources ([Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). This stage gives them a stamp and shows what that means for the matrix.
:::

**The idea.** A __voltage-controlled current source__ ([Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) is a generalized conductance. With a conductance, its own voltage $U_{ik}$ controls the current from $i$ to $k$. With the source, a foreign voltage $U_{pq}$ controls it. The rows remain, because the current flows out of and into the same nodes. The columns move from $i$, $k$ to $p$, $q$, because they count the controlling potentials. The symmetry is lost in the process. That is physics: the input acts on the output, but not the other way around.

:::satz Theorem 8.1 (Stamp of the voltage-controlled current source)
<span class="anker" id="satz-8-1"></span>

A source with $I=g\,(U_p-U_q)$ from $i$ to $k$ adds $+g$ to $(i,p)$ and $(k,q)$ and $-g$ to $(i,q)$ and $(k,p)$.
:::

⁠**How to read it:** $g$ is the __transconductance__, current per control voltage in siemens, 50 mS in the model. **Validity:** The source must be linear. Transistors are linear only for small changes around an operating point ([Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).

::::beispiel without negative feedback
A current source $I_\mathrm q=20$ µ A with $G_\mathrm q=0.5$ mS feeds node 1. There, $G_\mathrm i=0.5$ mS lies to ground. The source $g\,U_1$ draws current from node 2 into ground; $G_\mathrm o=0.05$ mS and $G_\mathrm L=0.2$ mS are also connected there. The stamps give

<span class="anker" id="gl-8-1"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}. \tag{8.1}$$

$Y_{12}=0$, but $Y_{21}=g$. With $D=(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)$, $D_1=(G_\mathrm o+G_\mathrm L)\,I_\mathrm q$ and $D_2=-g\,I_\mathrm q$, this becomes

<span class="anker" id="gl-8-2"></span>
$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}. \tag{8.2}$$

In the model, $D=0.25$, $U_1=20$ mV, $U_2=-4$ V and the __voltage gain__ is $A_u=-200$, as in [Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). The minus arises because the controlled current flows out of node 2.
::::

**With negative feedback.** The common lower point of input and output is called the foot point. If you separate it from ground and insert $R_\mathrm S=1\,\mathrm{k\Omega}$ there, node 3 arises (Fig. [8](#abb-8)). The output current now runs through $R_\mathrm S$ and raises $U_3$. This lowers the control voltage $U_1-U_3$, and the output current decreases. This action of the output back on its own input is called __negative feedback__.

:::abbildung et1/k8verstaerker 8
Amplifier with negative feedback. The source $g\,(U_1-U_3)$ leads from node 2 to node 3, $G_\mathrm i$ and $G_\mathrm o$ end at node 3. The red path shows the output current: it raises node 3 and so reduces the control voltage. For $G_\mathrm S\to\infty$, node 3 falls to ground.
:::

The stamps of $G_\mathrm q$, $G_\mathrm i$, $G_\mathrm S$, $G_\mathrm o$, $G_\mathrm L$ and $g\,(U_1-U_3)$ from 2 to 3 give

<span class="anker" id="gl-8-3"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0&-G_\mathrm i\\g&G_\mathrm o+G_\mathrm L&-g-G_\mathrm o\\-g-G_\mathrm i&-G_\mathrm o&G_\mathrm S+g+G_\mathrm i+G_\mathrm o\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\\0\end{pmatrix}. \tag{8.3}$$

:::herleitung The determinants
With $A=G_\mathrm q+G_\mathrm i$ and $B=G_\mathrm o+G_\mathrm L$, expansion along the first row gives

$$\begin{aligned} D&=A\,[B\,(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]-G_\mathrm i\,[B\,G_\mathrm i+G_\mathrm L\,g]\\ &=B\,[A\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[A\,G_\mathrm o+G_\mathrm q\,g]. \end{aligned}$$

$D_2$ is expanded along column 2, in which only $I_\mathrm q$ stands: $D_2=-I_\mathrm q\,[g\,(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)(g+G_\mathrm i)]=(G_\mathrm iG_\mathrm o-g\,G_\mathrm S)\,I_\mathrm q$.
:::

This gives the __transimpedance__, the output voltage per input current,

<span class="anker" id="gl-8-4"></span>
$$\frac{U_2}{I_\mathrm q}=\frac{G_\mathrm iG_\mathrm o-g\,G_\mathrm S}{(G_\mathrm o+G_\mathrm L)\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm o+G_\mathrm q\,g]}. \tag{8.4}$$

In the model with $G_\mathrm S=1$ mS, $D=5.3225$ and $D_2/I_\mathrm q=-49.975$, so $U_2/I_\mathrm q=-9.39\,\mathrm{k\Omega}$. From 20 µ A come $U_1=39.0$ mV, $U_2=-188$ mV and $A_u=-4.81$. **Limiting case:** For $G_\mathrm S\to\infty$, only the terms with $G_\mathrm S$ remain, and [(8.4)](#gl-8-4) turns into $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]=-200\,\mathrm{k\Omega}$, the result from [(8.2)](#gl-8-2). The foot point is then at ground again.

:::ltspice Amplifier with negative feedback
⁠**Draw:** `current` with `20u` from ground to `1`, `Rq 2k` from `1` to ground, `Ri 2k` from `1` to `3`, `RS 1k` from `3` to ground. The controlled current source `g` with `50m`: output from `2` to `3`, control input from `1` to `3`. `Ro 20k` from `2` to `3`, `RL 5k` from `2` to ground.

⁠**Directives:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op au PARAM u2/u1`.

⁠**What you see:** $\mathtt{u1}=39.0$ mV, $\mathtt{u2}=-188$ mV, $\mathtt{au}=-4.81$. Set `RS` to `1u`: then $\mathtt{u2}=-4$ V and $\mathtt{au}=-200$. Check your result from Exercise [10](#aufg-10) with `V(3)`.
:::

:::frage Why would you reduce the gain voluntarily?
Because it then hardly depends on the transconductance any more, and $g$ varies widely in transistors. If you double $g$ in the model, $A_u$ only goes from $-4.81$ to $-4.90$. Without $R_\mathrm S$, by contrast, $-200$ would become $-400$. The result lies close to $-R_\mathrm L/R_\mathrm S=-5$, that is, it is set by two precise resistors. [Part 11](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html) uses this for the operational amplifier.
:::

:::aufgabe Exercise 10 ★★★ The input resistance rises
<span class="anker" id="aufg-10"></span>

Consider the amplifier from Fig. [8](#abb-8) with $G_\mathrm S=1$ mS.

<ol class="al">

<li>

Show $D_1=[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]\,I_\mathrm q$ and calculate $U_1/I_\mathrm q$.

</li>

<li>

The input conductance without $G_\mathrm q$ is $Y_\mathrm{in}=I_\mathrm q/U_1-G_\mathrm q$. How large is the input resistance $1/Y_\mathrm{in}$? Compare with 2 k$\Omega$ without $R_\mathrm S$.

</li>

<li>

Explain the mechanism: How large is $U_3$, and what current therefore still flows through $G_\mathrm i$?

</li>

</ol>

:::loesung
(a) Replacing column 1 by $(I_\mathrm q,0,0)$ leaves $D_1=I_\mathrm q\,[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)\,G_\mathrm o]$. Multiplied out, the bracket is the one given. Numbers: $0.25\cdot1.5+0.2\cdot50.05=10.385$. With $D=5.3225$, $U_1/I_\mathrm q=1.95\,\mathrm{k\Omega}$.

(b) $Y_\mathrm{in}=1/(1.951\,\mathrm{k\Omega})-0.5\,\mathrm{mS}=0.0125$ mS, so $R_\mathrm{in}=79.9\,\mathrm{k\Omega}$, forty times as much.

(c) $U_3=38.05$ mV lies only 0.98 mV below $U_1=39.02$ mV. The potential at the other end of $R_\mathrm i$ almost follows along. That is why just under 1 mV is across $R_\mathrm i$, and instead of 10 µ A, 0.49 µ A flow. Little current at the same voltage means a large input resistance.
:::
:::
