---
title: Stufe 8: Das Rezept
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Vom Atom zum Band
order: 4181000
summary: Die letzten Rechnungen liefen immer gleich ab.
tags: 
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die letzten Rechnungen liefen immer gleich ab. Diese Stufe fasst sie in neun Schritte, die auch für Zellen mit mehreren Atomen und Orbitalen gelten.
:::

**Die Idee.** Jede Zelle sieht gleich aus, und die Koeffizienten der Nachbarzelle sind die der eigenen Zelle mal $\mathrm{e}^{\pm\mathrm{j} ka}$. Es reicht also, eine zentrale Zelle aufzuschreiben und ihre Kopplung an die Nachbarzellen. Statt einer riesigen Matrix bleibt eine $M\times M$-Matrix, $M$ ist die Zahl der Orbitale in der Zelle.

:::merke Rezept für die Tight-Binding-Rechnung
<ol>

<li>

Finde die Wigner-Seitz-Zelle des Kristalls ([Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)) und bestimme die primitiven Gittervektoren.

</li>

<li>

Wähle die Orbitale, die relevant sind oder sein sollen. Das ist nicht von vornherein klar und Teil der Modellbildung.

</li>

<li>

Die Dimension $M$ der Matrizen ist die Gesamtzahl der Orbitale in der Zelle, zum Beispiel $M=2$ für 2 Atome mal 1 Orbital.

</li>

<li>

Bestimme die Kopplung zu den Nachbarzellen. Mit Nächster-Nachbar-Näherung ist in 1D je eine Zelle links und rechts relevant, zusammen $\#=3$ Matrizen.

</li>

<li>

Schreibe $\#$ leere $M\times M$-Matrizen auf: zentrale Zelle, linke Zelle, rechte Zelle.

</li>

<li>

Schreibe in die Spalte vor jede Matrix die Orbitale der zentralen Zelle.

</li>

<li>

Schreibe als Zeile über jede Matrix die Orbitale der jeweiligen Zelle. Jeder Eintrag ist $\langle\text{Orbital vorn}|\hat H|\text{Orbital oben}\rangle$.

</li>

<li>

Multipliziere die Matrizen „links“ und „rechts“ mit $\mathrm{e}^{-\mathrm{j} ka}$ und $\mathrm{e}^{+\mathrm{j} ka}$.

</li>

<li>

Addiere alle Matrizen, ziehe $E\cdot\mathbf1$ ab und setze die Determinante null. Die Nullstellen dieses charakteristischen Polynoms sind die Bänder $E(k)$.

</li>

</ol>
:::

⁠**So liest man das:** Der Phasenfaktor stammt aus [(5.1)](viele-atome.html#gl-5-1), $a$ ist hier die Länge der Zelle. Die Zahl der Bänder ist $M$. **Kontrolle:** Für ein Atom mit einem s-Orbital sind die drei Matrizen die Zahlen $-V_\mathrm{ss}$, $E_\mathrm s$, $-V_\mathrm{ss}$, und Schritt 9 ergibt [(5.2)](viele-atome.html#gl-5-2).

::::beispiel zwei Atome je Zelle
Eine Zickzack-Kette aus Kohlenstoffatomen wie im Polyacetylen (Abb. [8](#abb-8)) hat in jeder Zelle die Atome A und B, der primitive Gittervektor hat die Länge $a$ (Schritt 1). Für die Leitung zählt das p-Orbital senkrecht zur Ebene der Kette (Schritt 2), also $M=2\cdot1=2$ (Schritt 3), und mit nächsten Nachbarn $\#=3$ (Schritt 4). Benachbarte Orbitale überlappen seitlich mit gleichem Vorzeichen, die Kopplung ist $-V_{\mathrm{pp}\pi}$. A koppelt an B derselben Zelle und an B der linken Zelle, B an A der rechten Zelle. Mit den Zeilen A, B und den Spalten A, B der jeweiligen Zelle ergeben die Schritte 5 bis 7

$$\underbrace{\begin{pmatrix}E_\mathrm p&-V_{\mathrm{pp}\pi}\\-V_{\mathrm{pp}\pi}&E_\mathrm p\end{pmatrix}}_{\text{Mitte}},\qquad\underbrace{\begin{pmatrix}0&-V_{\mathrm{pp}\pi}\\0&0\end{pmatrix}}_{\text{links}},\qquad\underbrace{\begin{pmatrix}0&0\\-V_{\mathrm{pp}\pi}&0\end{pmatrix}}_{\text{rechts}}.$$

Oben rechts in der Matrix links steht $\int\phi_\mathrm A^*\hat H\phi_\mathrm B^\text{links}\,\mathrm{d} x=\langle\mathrm A|\hat H|\mathrm B^\text{links}\rangle$. Die Schritte 8 und 9 ergeben

<span class="anker" id="gl-8-1"></span>
$$\det\left|\begin{pmatrix}0&0\\-V_{\mathrm{pp}\pi}&0\end{pmatrix}\mathrm{e}^{\mathrm{j} ka}+\begin{pmatrix}E_\mathrm p-E&-V_{\mathrm{pp}\pi}\\-V_{\mathrm{pp}\pi}&E_\mathrm p-E\end{pmatrix}+\begin{pmatrix}0&-V_{\mathrm{pp}\pi}\\0&0\end{pmatrix}\mathrm{e}^{-\mathrm{j} ka}\right|\overset!=0. \tag{8.1}$$

Das ist $(E_\mathrm p-E)^2-V_{\mathrm{pp}\pi}^2(1+\mathrm{e}^{\mathrm{j} ka})(1+\mathrm{e}^{-\mathrm{j} ka})=0$, also

<span class="anker" id="gl-8-2"></span>
$$E-E_\mathrm p=\pm V_{\mathrm{pp}\pi}\sqrt{2\bigl(1+\cos(ka)\bigr)}. \tag{8.2}$$

:::abbildung gemb1/k8rezept 8
Links: Kette mit den Atomen A und B, die zentrale Zelle ist grau, $a$ die Länge der Zelle. Rechts: Die Bänder [(8.2)](#gl-8-2) für $V_{\mathrm{pp}\pi}=2{,}5$ eV. Bei $k=0$ spalten sie maximal auf, am Zonenrand berühren sie sich.
:::
::::

⁠**So liest man das:** Das $\pm$ ist bindend und antibindend, die Fortsetzung von [(3.2)](zwei-atome.html#gl-3-2) auf den Kristall. Mit $V_{\mathrm{pp}\pi}=2{,}5$ eV ist die Aufspaltung bei $k=0$ $\pm5$ eV, bei $ka=\pi/2$ noch $\pm3{,}54$ eV, und bei $ka=\pi$ null: Die beiden Beiträge zur Kopplung von A und B heben sich auf, $1+\mathrm{e}^{\mathrm{j}\pi}=0$. **Kontrolle:** Es gilt $\sqrt{2(1+\cos(ka))}=2|\cos(ka/2)|$. Das ist das Band [(5.2)](viele-atome.html#gl-5-2) einer Kette mit Atomabstand $a/2$, in die halb so breite Zone zurückgefaltet. Sind A und B gleichwertig, ändert die größere Zelle nur die Buchführung.

:::aufgabe Aufgabe 11 ★★★ Abwechselnd kurz und lang
<span class="anker" id="aufg-11"></span>

In einer realen Kette wechseln kurze und lange Bindungen, die Kopplung ist abwechselnd $V_\pi$ (in der Zelle) und $V_\pi'$ (zur Nachbarzelle).

<ol class="al">

<li>

Führe das Rezept durch und zeige $E-E_\mathrm p=\pm\sqrt{V_\pi^2+V_\pi'^2+2V_\pi V_\pi'\cos(ka)}$.

</li>

<li>

Berechne für $V_\pi=2{,}8$ eV und $V_\pi'=2{,}2$ eV die Energien bei $k=0$, $ka=\pi/2$ und $ka=\pi$ sowie die Bandlücke. Jedes Atom gibt ein Elektron ab: Welche Sorte Stoff entsteht?

</li>

<li>

Grenzfälle: Was ergibt sich für $V_\pi'=V_\pi$ und für $V_\pi'\to0$?

</li>

<li>

Sind die Kopplungen gleich ($V=2$ eV), aber die Atome verschieden, mit $E_\mathrm A=-3$ eV und $E_\mathrm B=-1$ eV: Wie groß ist die Lücke?

</li>

</ol>

:::loesung
(a) Wie [(8.1)](#gl-8-1), die Nebendiagonale ist $-(V_\pi+V_\pi'\mathrm{e}^{-\mathrm{j} ka})$, und $|V_\pi+V_\pi'\mathrm{e}^{\mathrm{j} ka}|^2=V_\pi^2+V_\pi'^2+2V_\pi V_\pi'\cos(ka)$. (b) $\pm5{,}0$ eV; $\pm3{,}56$ eV; $\pm0{,}6$ eV, also $E_\mathrm g=2|V_\pi-V_\pi'|=1{,}2$ eV. Zwei Elektronen je Zelle füllen das untere Band: ein Halbleiter. (c) $V_\pi'=V_\pi$ ergibt [(8.2)](#gl-8-2). $V_\pi'\to0$ ergibt getrennte Paare mit $E-E_\mathrm p=\pm V_\pi$ ohne Abhängigkeit von $k$. (d) Es ist $E=\frac12(E_\mathrm A+E_\mathrm B)\pm\sqrt{\frac14(E_\mathrm A-E_\mathrm B)^2+2V^2(1+\cos(ka))}$. Am Zonenrand bleibt $E_\mathrm g=|E_\mathrm A-E_\mathrm B|=2$ eV.
:::
:::
