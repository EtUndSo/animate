---
title: Stufe 2: Die Kontinuitätsgleichung
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen
knoten: Kapitel 13: Diffusion, Rekombination und Grundgleichungen
order: 4230400
summary: Das Fick-Gesetz nennt den Strom zu einer bekannten Dichte.
tags: Quellenterm, Senkenterm, Sedimentation, Diffusionsgleichung
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Das Fick-Gesetz nennt den Strom zu einer bekannten Dichte. Der Strom ändert aber die Dichte. Diese Stufe verbindet beides zu einer Gleichung für den zeitlichen Verlauf.
:::

**Die Idee.** Solange keine Teilchen entstehen oder verschwinden, kann sich ihre Zahl in einem kleinen Volumen nur ändern, wenn auf einer Seite mehr hineinläuft, als auf der anderen herausläuft (Abb. [2](#abb-2)). Das ist reine Buchführung und gilt für jede Art von Strom. Mit dem Fick-Gesetz ergibt sie eine Gleichung für das Dichteprofil selbst.

:::abbildung gemb1/k13kontinuitaet 2
Links: Ein Volumen der Dicke $\Delta x$. Links strömt mehr hinein, als rechts herausströmt, also steigt die Dichte darin. Rechts: Eine Dichtestufe bei $x=0$ ebnet sich mit der Zeit ein ($t_0<t_1<t_2<t_3<t_4$).
:::

:::satz Satz 2.1 (Kontinuitätsgleichung)
<span class="anker" id="satz-2-1"></span>

Für Teilchen, die weder entstehen noch verschwinden, gilt

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial N}{\partial t}=-\frac{\partial\mathcal J}{\partial x}\quad\text{in einer Richtung},\qquad\dot N=\frac{\partial N}{\partial t}=-\operatorname{div}\boldsymbol{\mathcal J}\quad\text{allgemein}. \tag{2.1}$$

Mit Quellen und Senken kommen zwei Terme hinzu: $\dot N=-\operatorname{div}\boldsymbol{\mathcal J}+r_\mathrm Q-r_\mathrm S$.
:::

⁠**So liest man das:** $r_\mathrm Q$ ist der __Quellenterm__ (Teilchen, die je Volumen und Zeit entstehen, etwa durch eine chemische Reaktion), $r_\mathrm S$ der __Senkenterm__. Ist $\partial\mathcal J/\partial x>0$, läuft rechts mehr hinaus als links hinein, und $N$ sinkt. Woher $\boldsymbol{\mathcal J}$ kommt, ist gleich: Dichtegefälle (Diffusion), Feld (Drift), Schwerkraft (__Sedimentation__) oder Druck- und Dichteunterschiede (Konvektion).

:::herleitung Bilanz am Volumenelement
Das Volumen hat die Kanten $\Delta x,\Delta y,\Delta z$. In der Zeit $\Delta t$ kommen links $\mathcal J(x)\,\Delta y\,\Delta z\,\Delta t$ Teilchen hinein, rechts gehen $\mathcal J(x+\Delta x)\,\Delta y\,\Delta z\,\Delta t$ hinaus. Die Differenz, geteilt durch das Volumen, ist die Dichteänderung:

$$\Delta N=-\frac{\mathcal J(x+\Delta x)-\mathcal J(x)}{\Delta x}\,\Delta t\quad\Rightarrow\quad\frac{\partial N}{\partial t}=-\frac{\partial\mathcal J}{\partial x}.$$

In drei Dimensionen addieren sich die drei Richtungen zu $-\operatorname{div}\boldsymbol{\mathcal J}$.
:::

:::satz Satz 2.2 (Zweites Fick-Gesetz, zeitabhängige Diffusion)
<span class="anker" id="satz-2-2"></span>

Setzt man [(1.2)](warum-teilchen-ohne-kraft-stromen.html#gl-1-2) in [(2.1)](#gl-2-1) ein und ist $D$ konstant, folgt die __Diffusionsgleichung__

<span class="anker" id="gl-2-2"></span>
$$\frac{\partial^2N}{\partial x^2}=\frac1D\,\frac{\partial N}{\partial t}\quad\Leftrightarrow\quad\frac{\partial N}{\partial t}=D\,\frac{\partial^2N}{\partial x^2},\qquad\text{allgemein}\quad\frac{\partial N}{\partial t}=D\operatorname{div}\operatorname{grad}N=D\,\Delta N. \tag{2.2}$$
:::

⁠**So liest man das:** Das ist eine lineare partielle Differentialgleichung, zweiter Ordnung im Ort und erster in der Zeit, dieselbe Art wie die Wärmeleitungsgleichung. Links steht die Krümmung des Profils, rechts seine Änderung. Wo $N$ einen Berg bildet ($\partial^2N/\partial x^2<0$), sinkt die Dichte, in einem Tal steigt sie. Jedes Profil wird also glatter. Für eine Lösung braucht man eine Anfangsbedingung und zwei Randbedingungen. **Gültigkeit:** keine Quellen und Senken, $D$ unabhängig von Ort und Dichte.

::::beispiel
Die Gleichung verknüpft $t$ mit $x^2$, die einzige Länge aus $D$ und $t$ ist $\sqrt{Dt}$. Bor bei 1100 °C braucht für 1 µ m rund $x^2/(4D)=1{,}9$ h, für 2 µ m viermal so lange.
::::

⁠**Grenzfälle:** Eine gerade Strecke $N(x)$ hat keine Krümmung und ändert sich nicht. In einem geschlossenen Behälter wird für $t\to\infty$ $N$ überall gleich.

:::frage Im geradlinigen Profil fließt ein Strom. Warum ändert sich die Dichte dann nicht?
Weil der Strom überall gleich groß ist. Was in ein Volumen hineinläuft, läuft auf der anderen Seite wieder hinaus. Die Dichte ändert sich nur, wo sich der Strom ändert, und das verlangt ein gekrümmtes Profil.
:::

:::aufgabe Aufgabe 2 ★★ Ein Kosinusprofil zerfällt
<span class="anker" id="aufg-2"></span>

Bor liegt bei 1100 °C in einer Schicht der Dicke $b=2$ µ m, durch deren Ränder nichts entweicht, mit $N(x,0)=N_\mathrm m+N_\mathrm a\cos(\pi x/b)$.

<ol class="al">

<li>

Zeige, dass $N(x,t)=N_\mathrm m+N_\mathrm a\cos(\pi x/b)\,\mathrm{e}^{-t/t_\mathrm a}$ die Gleichung [(2.2)](#gl-2-2) löst, und bestimme $t_\mathrm a$.

</li>

<li>

Prüfe $\mathcal J=0$ an beiden Rändern. Wann ist die Schwankung auf 10 % gesunken?

</li>

<li>

Vorhersage: Wie ändert sich $t_\mathrm a$ bei doppelter Dicke?

</li>

</ol>

:::loesung
(a) Einsetzen gibt links den Faktor $-1/t_\mathrm a$, rechts $-D\pi^2/b^2$, also $t_\mathrm a=b^2/(\pi^2D)=1{,}1\cdot10^{4}\,\mathrm{s}=3{,}1$ h. (b) $\mathcal J\propto\sin(\pi x/b)$ ist an beiden Rändern null. 10 % nach $t_\mathrm a\ln10=7{,}0$ h. (c) Viermal so lang (12 h), weil die Krümmung viermal kleiner ist.
:::
:::
