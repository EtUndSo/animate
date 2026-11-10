---
title: Stufe 3: Silizium
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Bandstrukturen lesen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen
knoten: Kapitel 9: Bandstrukturen lesen
order: 4190500
summary: Graphen kam mit einem Orbital je Atom aus.
tags: Tal, Rotationsellipsoid
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Graphen kam mit einem Orbital je Atom aus. In Silizium binden alle vier Außenelektronen, und der Kristall ist dreidimensional. Diese Stufe zählt Elektronen und Orbitale und erklärt die Bandkanten und ihre Entartung.
:::

**Die Idee.** Zuerst wird gezählt. Silizium hat die Konfiguration 1s$^2$ 2s$^2$ 2p$^6$ 3s$^2$ 3p$^2$. Die inneren zehn Elektronen gehören zum Rumpfion Si$^{4+}$. Die vier äußeren sitzen im freien Atom nach der Hundschen Regel einzeln in den vier sp$^3$-Hybriden. Im Kristall teilt jedes Atom mit jedem der vier Nachbarn ein Paar. Jede Bindung spaltet in einen bindenden und einen antibindenden Zustand, und die Elektronen reichen genau für alle bindenden. Aus diesen werden Valenzbänder, aus den antibindenden Leitungsbänder.

:::satz Satz 3.1 (Zählen in der Diamantstruktur)
<span class="anker" id="satz-3-1"></span>

Die primitive Zelle enthält zwei Atome, also 8 Orbitale (s, p$_x$, p$_y$, p$_z$ je Atom), 8 Bänder und 8 Außenelektronen. Jedes Band fasst zwei Elektronen je Zelle. Bei $T=0$ sind die unteren vier Bänder voll und die oberen vier leer.
:::

⁠**So liest man das:** Kurz gesagt: Die Zahl der Bänder ist die Zahl der Orbitale in der Zelle. Die Zahl der vollen Bänder ist die halbe Elektronenzahl der Zelle, solange sich die Bänder nicht überlappen.

**Das Rezept.** Die Schritte laufen wie in Graphen, nur größer. Das Gitter ist FCC mit $\boldsymbol a_1=\frac a2(1,1,0)$, $\boldsymbol a_2=\frac a2(1,0,1)$, $\boldsymbol a_3=\frac a2(0,1,1)$, das zweite Atom sitzt bei $\boldsymbol d=\frac a4(1,1,1)$: zwei ineinander geschobene FCC-Gitter. Für brauchbare Leitungsbänder nimmt man fünf Orbitale je Atom, s, p$_x$, p$_y$, p$_z$ und ein höheres s-Orbital s$^*$. Das heißt sp$^3$s$^*$-Basis und ergibt $M=2\cdot5=10$. Jedes Atom hat vier Nachbarn, einen in der eigenen Zelle und drei in anderen, also $\#=1+6=7$. Die Summe ist eine $10\times10$-Matrix aus vier Blöcken:

<span class="anker" id="gl-3-1"></span>
$$\boldsymbol H_\mathrm{tot}(\boldsymbol k)=\begin{pmatrix}\boldsymbol H_\mathrm{AA}&\boldsymbol H_\mathrm{AB}(\boldsymbol k)\\\boldsymbol H_\mathrm{AB}^\dagger(\boldsymbol k)&\boldsymbol H_\mathrm{BB}\end{pmatrix}. \tag{3.1}$$

⁠**So liest man das:** $\boldsymbol H_\mathrm{AA}$ und $\boldsymbol H_\mathrm{BB}$ sind Diagonalmatrizen mit den fünf Orbitalenergien. $\boldsymbol H_\mathrm{AB}$ enthält die Kopplungen zwischen den Atomen, $\dagger$ bedeutet konjugiert transponiert. Oben links in $\boldsymbol H_\mathrm{AB}$ steht $-V_\mathrm{ss}g_0(\boldsymbol k)$ mit $g_0=1+\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_1}+\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_2}+\mathrm{e}^{-\mathrm{j}\boldsymbol k\cdot\boldsymbol a_3}$, genau wie $f$ in Graphen, nur mit vier Wegen. Die zehn Nullstellen findet ein Rechner für jedes $\boldsymbol k$ einzeln.

:::abbildung gemb1/k9silizium 3
Links: **qualitative Skizze** der Silizium-Bänder, nicht maßstäblich und nicht gerechnet. Nur Reihenfolge der Bänder und Lage der Extrema stimmen. Blau Valenzbänder, rot die untersten Leitungsbänder, grau die Lücke. Die obere blaue Linie besteht auf beiden Wegen aus zwei Bändern gleicher Energie. Rechts: Schnitt $k_z=0$ durch die Zone mit vier Tälern knapp über $E_\mathrm C$. Die beiden übrigen liegen auf der $k_z$-Achse vor und hinter der Zeichenebene (gestrichelt).
:::

**Was die Bandstruktur zeigt.** Wichtige Punkte der Zone sind $\Gamma$, $X=\frac{2\pi}a(1,0,0)$ (Mitte einer Quadratfläche) und $L=\frac\pi a(1,1,1)$ (Mitte einer Sechseckfläche).

<ul>

<li>

⁠**Valenzbandkante.** Das Maximum liegt bei $\Gamma$. Die obersten Zustände sind p-artig, und $x,y,z$ sind im Würfel gleichwertig. Deshalb treffen sich dort zwei Bänder mit verschiedener Krümmung, wie die Paare in der quadratischen Box aus [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html): Das Valenzband ist bei $\Gamma$ **2-fach entartet** (auch: degeneriert). Ein drittes liegt wegen einer kleinen magnetischen Wirkung des Spins 44 meV tiefer. Knapp unter $E_\mathrm V$ sind die Flächen konstanter Energie fast Kugeln um $\Gamma$.

</li>

<li>

⁠**Leitungsbandkante.** Das Minimum liegt längs $\Gamma\to X$ bei rund 85 % des Wegs. Warum gerade dort, ergibt erst die Rechnung. Weil der Würfel sechs gleichwertige Richtungen $\pm k_x,\pm k_y,\pm k_z$ hat, gibt es sechs solche Minima: Das Leitungsband ist **6-fach entartet**. Die Mulde um ein Minimum heißt __Tal__. Knapp über $E_\mathrm C$ sind die Flächen konstanter Energie sechs kleine __Rotationsellipsoid__e, längliche Körper um die Achse ihres Tals.

</li>

</ul>

::::beispiel
Es ist $2\pi/a=11{,}57\,\mathrm{nm^{-1}}$, das Minimum liegt bei $9{,}83\,\mathrm{nm^{-1}}$. Mit dem Zellvolumen $a^3/4$ gibt es $2{,}50\cdot10^{22}$ Zellen je cm$^3$. Die vier Valenzbänder fassen $2{,}0\cdot10^{23}\,\mathrm{cm^{-3}}$ Elektronen, genau die vier Außenelektronen der $5{,}0\cdot10^{22}$ Atome je cm$^3$. **Kontrolle:** Bei $\Gamma$ ist $g_0=4$. Zwei s-Orbitale ergeben dann $E_\mathrm s\mp4V_\mathrm{ss}$: dieselbe Aufspaltung wie $E_\sigma$ und $E_{\sigma^*}$ aus [Kapitel 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html), verstärkt durch vier Nachbarn.
::::

:::frage Im Atom ist jedes sp$^3$-Orbital halb voll, im Kristall ist das Valenzband ganz voll. Woher kommen die zusätzlichen Elektronen?
Es kommen keine hinzu. $N$ Atome bringen $4N$ Orbitale und $4N$ Elektronen. Die Kopplung macht daraus $2N$ bindende und $2N$ antibindende Zustände, und in die bindenden passen $4N$ Elektronen. Voll ist nur die untere Hälfte.
:::

:::aufgabe Aufgabe 3 ★ Elektronen und Bänder zählen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Germanium hat 32 Elektronen. Schreibe die Konfiguration auf. Wie viele Außenelektronen zählen?

</li>

<li>

Germanium hat die Diamantstruktur mit $a=0{,}5658$ nm. Wie viele Elektronen je cm$^3$ sitzen in den Valenzbändern?

</li>

<li>

Wie groß ist $M$ mit und ohne s$^*$-Orbital? Wie viele Bänder sind jeweils voll?

</li>

<li>

Vorhersage: Natrium ist BCC mit einem Atom je primitiver Zelle und einem Außenelektron. Wie weit ist das oberste Band gefüllt?

</li>

</ol>

:::loesung
(a) 1s$^2$ 2s$^2$ 2p$^6$ 3s$^2$ 3p$^6$ 3d$^{10}$ 4s$^2$ 4p$^2$, vier Außenelektronen. (b) Zelle $a^3/4=0{,}0453\,\mathrm{nm^3}$, also $2{,}21\cdot10^{22}$ Zellen und $1{,}77\cdot10^{23}$ Elektronen je cm$^3$. (c) Mit s$^*$ ist $M=10$, ohne $M=8$. Voll sind jedes Mal vier Bänder, die Elektronenzahl bleibt acht. (d) Ein Elektron je Zelle, zwei Plätze: Das Band ist halb voll, Natrium leitet.
:::
:::
