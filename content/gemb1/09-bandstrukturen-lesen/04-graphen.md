---
title: Stufe 2: Graphen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Bandstrukturen lesen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen
knoten: Kapitel 9: Bandstrukturen lesen
order: 4190400
summary: Bisher enthielt die Zelle ein Atom.
tags: Dirac-Punkt, Halbmetall
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bisher enthielt die Zelle ein Atom. Graphen hat zwei. Diese Stufe führt das Rezept für die Wabe durch. Das Ergebnis sind zwei Bänder, die sich an einzelnen Punkten berühren.
:::

**Die Idee.** Graphen ist eine Lage Kohlenstoff in Wabenform ([Kapitel 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)). Die Atome sind gleich, ihre Umgebungen nicht, deshalb enthält die primitive Zelle, eine Raute, die Atome A und B. Drei Elektronen je Atom bilden das Gerüst aus sp$^2$-Bindungen. Das vierte sitzt im p$_z$-Orbital senkrecht zur Lage. Dieses hat oben und unten verschiedene Vorzeichen, die sp$^2$-Orbitale nicht, also heben sich die Kopplungen zwischen beiden auf, und die p$_z$-Orbitale bilden ein System für sich. Jedes A hüpft zu drei B. Die drei Wege überlagern sich, und an besonderen $\boldsymbol k$ löschen sie sich aus.

**Das Rezept für die Wabe.** A sitzt im Ursprung, B bei $(a_\mathrm{CC},0)$ (Abb. [2](#abb-2)).

<ol>

<li>

Primitive Vektoren: $\boldsymbol a_1=a\,(\sqrt3/2,\ 1/2)$ und $\boldsymbol a_2=a\,(\sqrt3/2,\ -1/2)$ mit $a=\sqrt3\,a_\mathrm{CC}$. $a$ ist die Gitterkonstante, $a_\mathrm{CC}$ der Abstand benachbarter Atome.

</li>

<li>

Relevant ist das p$_z$-Orbital. Die Orbitale liegen seitlich nebeneinander, $\langle\mathrm A|\hat H|\mathrm B\rangle=-V_{\mathrm{pp}\pi}$.

</li>

<li>

$M=2\cdot1=2$.

</li>

<li>

A hat Nachbarn in der eigenen Zelle und in den Zellen $-\boldsymbol a_1$ und $-\boldsymbol a_2$, B in den Zellen $+\boldsymbol a_1$ und $+\boldsymbol a_2$, also $\#=5$.

</li>

<li>

⁠**5.–8.** Mit den Zeilen $\langle\mathrm A|$, $\langle\mathrm B|$ und den Spalten A, B der jeweiligen Zelle:

$$\underbrace{\begin{pmatrix}E_\mathrm p&-V_{\mathrm{pp}\pi}\\-V_{\mathrm{pp}\pi}&E_\mathrm p\end{pmatrix}}_{\text{Mitte}},\qquad\underbrace{\begin{pmatrix}0&0\\-V_{\mathrm{pp}\pi}&0\end{pmatrix}}_{+\boldsymbol a_{1,2}:\ \text{mal }\mathrm{e}^{+\mathrm{j}\boldsymbol k\cdot\boldsymbol a_{1,2}}},\qquad\underbrace{\begin{pmatrix}0&-V_{\mathrm{pp}\pi}\\0&0\end{pmatrix}}_{-\boldsymbol a_{1,2}:\ \text{mal }\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_{1,2}}}.$$

</li>

<li>

⁠**9.** Die Summe ist $\boldsymbol H_\mathrm{tot}$, die Bedingung lautet $\det|\boldsymbol H_\mathrm{tot}-E\mathbf1|=0$.

</li>

</ol>

:::satz Satz 2.1 (Bänder von Graphen)
<span class="anker" id="satz-2-1"></span>

Es gilt

<span class="anker" id="gl-2-1"></span>
$$\boldsymbol H_\mathrm{tot}=\begin{pmatrix}E_\mathrm p&-V_{\mathrm{pp}\pi}\bigl(1+\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_1}+\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_2}\bigr)\\-V_{\mathrm{pp}\pi}\bigl(1+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_1}+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_2}\bigr)&E_\mathrm p\end{pmatrix}. \tag{2.1}$$

Mit $f(\boldsymbol k)=1+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_1}+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_2}$ sind die Bänder

<span class="anker" id="gl-2-2"></span>
$$E_\pm(\boldsymbol k)=E_\mathrm p\pm V_{\mathrm{pp}\pi}\,|f(\boldsymbol k)|=E_\mathrm p\pm V_{\mathrm{pp}\pi}\sqrt{1+4\cos\bigl(\tfrac{\sqrt3}2k_xa\bigr)\cos\bigl(\tfrac{k_ya}2\bigr)+4\cos^2\bigl(\tfrac{k_ya}2\bigr)}. \tag{2.2}$$
:::

:::herleitung Von der Determinante zur Wurzel
Die Determinante ist $(E_\mathrm p-E)^2-V_{\mathrm{pp}\pi}^2|f|^2=0$. Mit $\boldsymbol k\cdot\boldsymbol a_{1,2}=\frac{\sqrt3}2k_xa\pm\frac12k_ya$ wird $f=1+2\,\mathrm{e}^{\mathrm{j} k_xa\sqrt3/2}\cos(k_ya/2)$, also

$$E=E_\mathrm p\pm\sqrt{V_{\mathrm{pp}\pi}\bigl(1+2\mathrm{e}^{\mathrm{j} k_xa\sqrt3/2}\cos(\tfrac{k_ya}2)\bigr)\,V_{\mathrm{pp}\pi}\bigl(1+2\mathrm{e}^{-\mathrm{j} k_xa\sqrt3/2}\cos(\tfrac{k_ya}2)\bigr)}.$$

Ausmultiplizieren ergibt [(2.2)](#gl-2-2).
:::

:::abbildung gemb1/k9graphen 2
Oben links: Wabe mit den Atomen A (blau) und B (grün), die zentrale Zelle dunkelgrau, ihre vier Nachbarzellen hellgrau. Oben rechts: Brillouin-Zone mit dem Weg $\Gamma\to M\to K\to\Gamma$, rot die sechs Ecken. Unten: Bänder [(2.2)](#gl-2-2) für $V_{\mathrm{pp}\pi}=2{,}8$ eV.
:::

⁠**So liest man das:** Zwei Orbitale ergeben zwei Bänder, das bindende $\pi$-Band und das antibindende $\pi^*$-Band. Die Zone ist ein Sechseck mit der Kantenmitte $M=(\frac{2\pi}{\sqrt3a},0)$ und der Ecke $K=(\frac{2\pi}{\sqrt3a},\frac{2\pi}{3a})$. Bei $\Gamma$ addieren sich die drei Wege, $|f|=3$. Bei $M$ ist $|f|=1$. Bei $K$ haben die drei Summanden von $f$ die Phasen $0$, $240^\circ$ und $120^\circ$, und ihre Summe ist null: A und B koppeln nicht mehr, beide Bänder bleiben bei $E_\mathrm p$.

:::definition Definition 2.2 (Dirac-Punkt)
<span class="anker" id="satz-2-2"></span>

Die Ecken der Zone, an denen sich $\pi$- und $\pi^*$-Band berühren, heißen __Dirac-Punkt__e. Nur zwei der sechs Ecken sind verschieden, $K$ und $K'$, die übrigen gehen durch reziproke Gittervektoren aus ihnen hervor. Dort ist $E_\mathrm g=0$. Nahe dem Punkt gilt mit $\boldsymbol q=\boldsymbol k-\boldsymbol K$ eine lineare Beziehung, ein Kegel:

<span class="anker" id="gl-2-3"></span>
$$E_\pm\approx E_\mathrm p\pm\hbar v_\mathrm{Dirac}|\boldsymbol q|,\qquad v_\mathrm{Dirac}=\frac{\sqrt3\,V_{\mathrm{pp}\pi}\,a}{2\hbar}. \tag{2.3}$$
:::

:::herleitung Die Steigung am Dirac-Punkt
Weil $f(\boldsymbol K)=0$ ist, bleibt in erster Ordnung $f\approx\mathrm{j} u\,\mathrm{e}^{\mathrm{j}4\pi/3}+\mathrm{j} w\,\mathrm{e}^{\mathrm{j}2\pi/3}$ mit $u=\boldsymbol q\cdot\boldsymbol a_1$ und $w=\boldsymbol q\cdot\boldsymbol a_2$. Das ergibt $|f|^2=u^2+w^2-uw=\frac34a^2|\boldsymbol q|^2$.
:::

⁠**Besetzung:** Jedes C-Atom gibt ein p$_z$-Elektron, zwei je Zelle. Das $\pi$-Band fasst genau zwei je Zelle, es ist voll, das $\pi^*$-Band leer. Graphen ist damit ein __Halbmetall__: Besetztes und leeres Band berühren sich, ohne Lücke und ohne Überlapp. **Gültigkeit:** nur nächste Nachbarn, nur p$_z$-Orbitale.

::::beispiel
Mit $E_\mathrm p$ als Nullpunkt ist $E_\pm(\Gamma)=\pm8{,}4$ eV, $E_\pm(M)=\pm2{,}8$ eV, $E_\pm(K)=0$. Die Breite beider Bänder zusammen ist $6V_{\mathrm{pp}\pi}=16{,}8$ eV, das Doppelte der Kopplungen an drei Nachbarn. Aus [(2.3)](#gl-2-3) folgt $\hbar v_\mathrm{Dirac}=0{,}596\,\mathrm{eV\,nm}$ und $v_\mathrm{Dirac}=9{,}1\cdot10^5$ m/s, ein 331stel der Lichtgeschwindigkeit. Sie hängt nicht von der Energie ab, ein Kegel hat überall dieselbe Steigung.
::::

⁠**Grenzfall:** Für $V_{\mathrm{pp}\pi}\to0$ fallen beide Bänder auf $E_\mathrm p$.

:::frage Wenn die Lücke null ist, warum ist Graphen dann kein gewöhnliches Metall?
In einem Metall grenzen besetzte und leere Zustände längs einer ganzen Fläche im $k$-Raum aneinander. In Graphen geschieht das nur an den Punkten $K$ und $K'$. Schon wenige zusätzliche Elektronen verschieben deshalb die Eigenschaften stark.
:::

:::aufgabe Aufgabe 2 ★★★ Zwei verschiedene Atome in der Wabe
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Zeige mit [(2.2)](#gl-2-2), dass auch $K'=(0,\frac{4\pi}{3a})$ ein Dirac-Punkt ist.

</li>

<li>

In hexagonalem Bornitrid wechseln sich Bor und Stickstoff ab, $E_\mathrm A=E_\mathrm p+\Delta$ und $E_\mathrm B=E_\mathrm p-\Delta$. Zeige: $E_\pm=E_\mathrm p\pm\sqrt{\Delta^2+V_{\mathrm{pp}\pi}^2|f|^2}$.

</li>

<li>

Berechne für $\Delta=2{,}9$ eV und $V_{\mathrm{pp}\pi}=2{,}4$ eV die Energien an $\Gamma$, $M$ und $K$. Wie groß ist die Bandlücke?

</li>

<li>

Zeige, dass aus dem Kegel bei $K$ eine Parabel wird, und bestimme $m^*$ für $a=0{,}25$ nm. Was geschieht für $\Delta\to0$?

</li>

</ol>

:::loesung
(a) $k_x=0$ ergibt $\cos(\frac{\sqrt3}2k_xa)=1$, $k_ya/2=2\pi/3$ ergibt $\cos=-\frac12$. Unter der Wurzel steht $1-2+1=0$. (b) Die Hauptdiagonale von [(2.1)](#gl-2-1) wird $E_\mathrm p\pm\Delta$, die Determinante $(E_\mathrm p-E)^2-\Delta^2-V_{\mathrm{pp}\pi}^2|f|^2=0$. (c) $\Gamma$: $\pm\sqrt{2{,}9^2+7{,}2^2}\,\mathrm{eV}=\pm7{,}76$ eV. $M$: $\pm3{,}76$ eV. $K$: $\pm2{,}9$ eV. Die Lücke liegt bei $K$ und ist $2\Delta=5{,}8$ eV. (d) Nahe $K$ ist $V_{\mathrm{pp}\pi}|f|=\hbar v_\mathrm{Dirac}|\boldsymbol q|$ mit $\hbar v_\mathrm{Dirac}=0{,}520\,\mathrm{eV\,nm}$. Für kleine $|\boldsymbol q|$ ist $\sqrt{\Delta^2+(\hbar v_\mathrm{Dirac}q)^2}\approx\Delta+(\hbar v_\mathrm{Dirac}q)^2/(2\Delta)$, eine Parabel. Der Vergleich mit $\hbar^2q^2/(2m^*)$ ergibt $m^*/m_0=0{,}0381\,\mathrm{eV\,nm^2}\cdot2\Delta/(\hbar v_\mathrm{Dirac})^2=0{,}82$. Für $\Delta\to0$ geht $m^*\to0$, der Kegel kehrt zurück.
:::
:::
