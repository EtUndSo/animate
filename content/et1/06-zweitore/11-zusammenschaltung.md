---
title: Stufe 9: Zusammenschaltung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1161100
summary: Stufe 8 hat gezeigt, dass die Kette zur A-Form passt.
tags: 
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Stufe [8](kettenform.html#stufe-8) hat gezeigt, dass die Kette zur A-Form passt. Diese Stufe beantwortet die Frage allgemein: Welche Form passt zu welcher Zusammenschaltung?
:::

**Die Idee.** Verbindet man zwei Zweitore, teilen sie an jedem Tor entweder den Strom (Reihe) oder die Spannung (parallel). Die geteilte Größe ist für beide Teile gleich, die andere summiert sich. Das sagt, welche Form passt: Die gemeinsamen Größen gehören zu den Ursachen, die summierten zu den Wirkungen. Dann steht auf der rechten Seite für beide Teile dasselbe, und die Parameter addieren sich.

:::satz Satz 9.1 (Zusammenschaltung zweier Zweitore)
<span class="anker" id="satz-9-1"></span>

Bleibt in beiden Teilen die Torbedingung erhalten, gilt:

| Schaltung (Tor 1, Tor 2) | gleich für beide | summiert sich | Regel |
|---|---|---|---|
| Reihe, Reihe | $I_1$, $I_2$ | $U_1$, $U_2$ | $\mathbf Z=\mathbf Z'+\mathbf Z''$ |
| parallel, parallel | $U_1$, $U_2$ | $I_1$, $I_2$ | $\mathbf Y=\mathbf Y'+\mathbf Y''$ |
| Reihe, parallel | $I_1$, $U_2$ | $U_1$, $I_2$ | $\mathbf H=\mathbf H'+\mathbf H''$ |
| Kette | $U_2'=U_1''$, $-I_2'=I_1''$ | nichts | $\mathbf A=\mathbf A'\mathbf A''$ |
:::

⁠**So liest man das:** Das Schaltbild sagt, welche Größen gleich sind, die Tabelle sagt, welche Form sich addiert (Abb. [11](#abb-11)). Daher hat die H-Matrix ihren zweiten Namen Reihenparallelmatrix. Die Schaltung „parallel, Reihe“ ist der fehlende Fall. Zu ihr gehört die umgekehrte Hybridform mit $U_1$ und $I_2$ als Ursachen, die man mit der Inversen von $\mathbf H$ erhält.

:::herleitung Warum sich die Parameter addieren
In Reihe, Reihe führen beide Teile dieselben Ströme: $\mathbf I'=\mathbf I''=\mathbf I$. Also ist $\mathbf U=\mathbf U'+\mathbf U''=\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$. Parallel gilt dasselbe mit vertauschten Rollen. Bei Reihe, parallel ist die Ursachenspalte $(I_1,\,U_2)$ für beide gleich, die Wirkungsspalte $(U_1,\,I_2)$ ist die Summe beider Wirkungsspalten.
:::

:::abbildung et1/k6zusammen 11
Drei Zusammenschaltungen. Links Reihe, Reihe: gleiche Ströme, Z addiert sich. Mitte parallel, parallel: gleiche Spannungen, Y addiert sich. Rechts Reihe, parallel: gleiches $I_1$ und $U_2$, H addiert sich.
:::

::::beispiel
⁠**Reihe:** Das T-Zweitor selbst ist eine Reihenschaltung aus zwei getrennten Längswiderständen und einem Querwiderstand:

$$\mathbf Z=\begin{pmatrix}15&0\\0&20\end{pmatrix}\Omega+\begin{pmatrix}20&20\\20&20\end{pmatrix}\Omega=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**Parallel:** Legt man einen Widerstand von 100 $\Omega$ von Klemme 1 nach Klemme 2 über das T-Zweitor, kommt zu $\mathbf Y$ der Längsleitwert hinzu:

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}+\begin{pmatrix}10&-10\\-10&10\end{pmatrix}\mathrm{mS}=\begin{pmatrix}50&-30\\-30&45\end{pmatrix}\mathrm{mS}.$$

Kontrolle: Mit kurzgeschlossenem Tor 2 ist $1/Y_{11}=20\,\Omega$, und direkt ist das $25\,\Omega\parallel100\,\Omega=20\,\Omega$.

**Wann die Regel versagt.** Die Regeln setzen voraus, dass jedes Teil für sich die Torbedingung behält. Bei der Kette ist sie sicher, denn das hintere Teil samt Last ist für das vordere ein Zweipol. Zwei Dreipole mit gemeinsamer Masseleitung darf man ebenfalls parallel schalten: Bei ihnen fallen 1$'$ und 2$'$ in einem Punkt zusammen, es zählt nur die Summe der Rückströme. Bei der Reihe ist Vorsicht nötig. Setzt man zwei T-Zweitore mit ihren Masseleitungen übereinander, schließt die Masseleitung des oberen die beiden oberen Klemmen des unteren kurz. Ein Teil des Stroms von Tor 1 läuft dann im unteren T durch $R_\mathrm{c}$, die Torbedingung bricht. Statt $Z_{11}=70\,\Omega$ misst man $35\,\Omega+15\,\Omega\parallel20\,\Omega+20\,\Omega=63{,}6\,\Omega$. Abhilfe: Man spiegelt das untere T, sodass nur die beiden Masseleitungen verbunden sind. Dann bleiben beide Dreipole, und die Regel gibt die richtigen 70 $\Omega$.

⁠**Grenzfall:** Zwei gleiche Zweitore parallel haben die halbe Matrix $\mathbf Z$, gleiche Widerstände parallel ergeben den halben Widerstand. In Reihe verdoppelt sich $\mathbf Z$.

:::frage Warum addiert sich bei der Reihe nicht auch die Kettenmatrix?
Weil bei der Reihe $I_1$ für beide gleich ist, $U_1$ aber nicht. In der Kettenform steht $U_1$ zusammen mit $I_1$ auf der linken Seite, und rechts stünden die Ausgangsgrößen. Für beide Teile wäre die rechte Spalte verschieden, und nichts ließe sich zusammenfassen.
:::

:::aufgabe Aufgabe 9 ★★ Welche Form passt?
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Zwei gleiche T-Zweitore werden parallel, parallel verbunden. Wie groß ist $\mathbf Z$ der Schaltung? Warum ist die Rechnung hier zulässig?

</li>

<li>

Zwei gleiche T-Zweitore, das untere gespiegelt, liegen in Reihe, Reihe. Wie groß ist $\mathbf Z$?

</li>

<li>

Die Hybridmatrix des T-Zweitors ist bekannt. Wie groß ist $\mathbf H$ für zwei gleiche Zweitore in Reihe, parallel (Torbedingung vorausgesetzt)?

</li>

<li>

Zum T-Zweitor kommt ein Querwiderstand von 10 $\Omega$ in Reihe, Reihe. Welches $\mathbf Z$ ergibt sich, und welche T-Schaltung gehört dazu?

</li>

</ol>

:::loesung
(a) $\mathbf Y$ verdoppelt sich, also halbiert sich $\mathbf Z$: $Z_{11}=17{,}5\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=20\,\Omega$. Beide sind Dreipole mit gemeinsamer Masseleitung, die Tore bleiben Tore. (b) $\mathbf Z$ verdoppelt sich: 70, 40, 40, 80 $\Omega$. (c) $\mathbf H$ verdoppelt sich: $H_{11}=50\,\Omega$, $H_{12}=1$, $H_{21}=-1$, $H_{22}=50$ mS. (d) $Z_{11}=45\,\Omega$, $Z_{12}=Z_{21}=30\,\Omega$, $Z_{22}=50\,\Omega$. Das ist ein T mit $R_\mathrm{a}=15\,\Omega$, $R_\mathrm{b}=30\,\Omega$, $R_\mathrm{c}=20\,\Omega$: Der Querwiderstand liegt in Reihe zu $R_\mathrm{b}$, weil er denselben Summenstrom führt.
:::
:::
