---
title: Stufe 6: Masse und Richtung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4190800
summary: Stufe 5 rechnete in einer Richtung.
tags: isotrop, anisotrop
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Stufe [5](die-effektive-masse-im-kristall.html#stufe-5) rechnete in einer Richtung. In drei Dimensionen kann die Krümmung von $E(\boldsymbol k)$ je Richtung verschieden sein. Diese Stufe zeigt, wie man das an den Flächen konstanter Energie erkennt und warum Silizium zwei Massen hat.
:::

**Die Idee.** Die Atome liegen nicht in allen Richtungen gleich, also hängt auch $E(\boldsymbol k)$ von der Richtung ab. Eine Mulde kann in einer Richtung steil sein, in der anderen flach, wie ein langes Tal in den Bergen. Die Fläche konstanter Energie zeigt das sofort: Wo die Mulde flach ist, muss man weit gehen, um dieselbe Energie zu erreichen. Lange Achse bedeutet kleine Krümmung, also große Masse.

:::definition Definition 6.1 (Isotrop und anisotrop)
<span class="anker" id="satz-6-1"></span>

Sind die Flächen konstanter Energie Kugeln, heißt die Dispersion, also die Beziehung $E(\boldsymbol k)$, __isotrop__: In allen Richtungen liegt dieselbe effektive Masse vor. Sonst heißt sie __anisotrop__.
:::

:::satz Satz 6.2 (Parabel in drei Richtungen)
<span class="anker" id="satz-6-2"></span>

Liegen die Hauptachsen eines Tals längs $x,y,z$, gilt um das Minimum bei $\boldsymbol k_0$ mit $\boldsymbol q=\boldsymbol k-\boldsymbol k_0$

<span class="anker" id="gl-6-1"></span>
$$E(\boldsymbol k)\approx E_\mathrm C+\frac{\hbar^2}2\Bigl(\frac{q_x^2}{m_x}+\frac{q_y^2}{m_y}+\frac{q_z^2}{m_z}\Bigr),\qquad\frac1{m_i}=\frac1{\hbar^2}\,\frac{\partial^2E}{\partial k_i^2}. \tag{6.1}$$

Die Fläche zur Energie $E$ ist ein Ellipsoid mit den Halbachsen $q_i=\sqrt{2m_i(E-E_\mathrm C)}/\hbar$. Je Richtung gilt $F_i=m_i\,\mathrm{d} v_i/\mathrm{d} t$.
:::

⁠**So liest man das:** $m_x,m_y,m_z$ sind die Richtungsmassen aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html), jede folgt aus [(5.1)](die-effektive-masse-im-kristall.html#gl-5-1) für ihre Achse. Das Verhältnis zweier Halbachsen ist $\sqrt{m_x/m_y}$. **Gültigkeit:** nahe dem Extremum und längs der Hauptachsen des Tals, sonst kommen gemischte Ableitungen hinzu.

**Silizium und GaAs.** Das $\Gamma$-Tal von GaAs ist isotrop, eine Zahl genügt: $m^*=0{,}067\,m_0$. Das Silizium-Leitungsband ist komplizierter. Jedes der sechs Täler ist ein Rotationsellipsoid mit einer Längsrichtung und zwei gleichen Querrichtungen, es gibt also zwei effektive Massen:

<span class="anker" id="gl-6-2"></span>
$$m_\mathrm h^*=0{,}92\,m_0\quad\text{(längs)},\qquad m_\mathrm l^*=0{,}19\,m_0\quad\text{(quer)}. \tag{6.2}$$

Dabei steht h für englisch heavy, l für light. Andere Bücher nennen die Längsmasse $m_\mathrm l$ wie longitudinal, entscheidend ist: längs schwer, quer leicht. Für das Tal auf der $k_x$-Achse ist $m_x=m_\mathrm h^*$ und $m_y=m_z=m_\mathrm l^*$. Abweichungen von der Kugel gibt es auch in Metallen: Natrium hat recht gute Kugelflächen, in Kupfer, Silber und Gold weichen sie bei höheren Energien deutlich ab, denn sie kommen der Zonengrenze nahe, wie im Quadrat aus Stufe [1](das-band-in-der-ebene.html#stufe-1).

:::abbildung gemb1/k9ellipse 6
Links: Schnitt durch die Flächen konstanter Energie bei $E-E_\mathrm C=26$ meV, vom Minimum des Tals aus, $q$ in 1/nm, im gleichen Maßstab. Rechts: Die zugehörigen Parabeln. Kleine Masse bedeutet starke Krümmung.
:::

::::beispiel
Bei $E-E_\mathrm C=26$ meV sind die Halbachsen im Silizium-Tal $0{,}79\,\mathrm{nm^{-1}}$ und $0{,}36\,\mathrm{nm^{-1}}$, das Verhältnis ist $\sqrt{0{,}92/0{,}19}=2{,}20$. GaAs hat den Radius $0{,}21\,\mathrm{nm^{-1}}$. Im Ellipsoid sind Kraft und Beschleunigung nicht parallel. Eine Kraft unter $45^\circ$ zur Längsachse ergibt $(\mathrm{d} v_x/\mathrm{d} t)/(\mathrm{d} v_y/\mathrm{d} t)=m_\mathrm l^*/m_\mathrm h^*=0{,}21$. Die Beschleunigung zeigt also unter $78{,}3^\circ$ zur Längsachse: Das Elektron weicht in die leichte Richtung aus.
::::

⁠**Grenzfall:** Für $m_\mathrm h^*=m_\mathrm l^*$ wird das Ellipsoid zur Kugel.

:::frage Silizium ist kubisch, alle drei Achsen sind gleichwertig. Wie kann die Masse da von der Richtung abhängen?
Ein einzelnes Tal ist nicht kubisch, alle sechs zusammen sind es: Bei einer Kraft längs $x$ antworten zwei Täler mit $m_\mathrm h^*$ und vier mit $m_\mathrm l^*$, für jede Achse gleich. Die Wirkung ist das Mittel der Kehrwerte, $3/(1/m_\mathrm h^*+2/m_\mathrm l^*)=0{,}26\,m_0$.
:::

:::aufgabe Aufgabe 7 ★★ Ein Tal vermessen
<span class="anker" id="aufg-7"></span>

Betrachte das Silizium-Tal auf der $k_x$-Achse.

<ol class="al">

<li>

Berechne die Halbachsen der Fläche bei $E-E_\mathrm C=50$ meV. Wie groß wäre der Radius der GaAs-Kugel?

</li>

<li>

Die Kraft zeigt unter $30^\circ$ zur Talachse. Unter welchem Winkel zeigt die Beschleunigung?

</li>

<li>

Warum zählt in der obigen Frage das Mittel der Kehrwerte und nicht das der Massen ($0{,}43\,m_0$)?

</li>

</ol>

:::loesung
(a) $q_\mathrm h=\sqrt{0{,}92\cdot0{,}05/0{,}0381}\,\mathrm{nm^{-1}}=1{,}10\,\mathrm{nm^{-1}}$, $q_\mathrm l=0{,}50\,\mathrm{nm^{-1}}$, GaAs $0{,}30\,\mathrm{nm^{-1}}$. (b) $\tan\alpha=(\sin30^\circ/m_\mathrm l^*)/(\cos30^\circ/m_\mathrm h^*)=2{,}80$, also $\alpha=70{,}3^\circ$. (c) Die Täler leiten nebeneinander, die Beschleunigungen $F/m$ addieren sich, also mittelt man $1/m$.
:::
:::
