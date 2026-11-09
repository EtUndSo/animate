---
title: Stufe 3: Leitungsband und Valenzband
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
order: 4200500
summary: Die Formeln gelten für eine Parabel mit einer Masse, die bei null beginnt.
tags: Ellipsoid, Zustandsdichtemasse
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Formeln gelten für eine Parabel mit einer Masse, die bei null beginnt. Echte Bänder beginnen bei $E_\mathrm C$, das Valenzband ist nach unten geöffnet, und Silizium hat mehrere Täler mit richtungsabhängiger Masse. Diese Stufe bringt alles in dieselbe Form.
:::

**Die Idee.** Wärme hebt Elektronen nur knapp über einen Bandrand, denn $k_\mathrm BT$ ist klein gegen die Breite eines Bands. Deshalb genügt die Umgebung des Rands, und dort ist jedes Band eine Parabel. Das Leitungsband ist die 3D-Formel, um $E_\mathrm C$ nach oben verschoben. Das Valenzband ist dieselbe Formel, an $E_\mathrm V$ gespiegelt, denn seine Plätze liegen unterhalb des Rands (Abb. [3](#abb-3)). In der Lücke gibt es keinen Zustand, dort ist $D=0$.

:::satz Satz 3.1 (Zustandsdichte an den Bandrändern)
<span class="anker" id="satz-3-1"></span>

Für $E\ge E_\mathrm C$ und für $E\le E_\mathrm V$ gilt

<span class="anker" id="gl-3-1"></span>
$$D_\mathrm C(E)=\frac{4\pi(2m_\mathrm C^*)^{3/2}}{h^3}\sqrt{E-E_\mathrm C},\qquad D_\mathrm V(E)=\frac{4\pi(2m_\mathrm V^*)^{3/2}}{h^3}\sqrt{E_\mathrm V-E}. \tag{3.1}$$
:::

⁠**So liest man das:** $m_\mathrm C^*$ und $m_\mathrm V^*$ sind die effektiven Massen fürs Zählen. Mit $h=2\pi\hbar$ ist der Vorfaktor $(2m^*)^{3/2}/(2\pi^2\hbar^3)$. **Gültigkeit:** Das Band muss in dem Bereich parabolisch sein, in dem Elektronen oder Löcher sitzen. Das sind wenige $k_\mathrm BT$ vom Rand.

:::abbildung gemb1/k10kante 3
Links ein Schnitt durch den $k$-Raum von Silizium: Flächen gleicher Energie im Leitungsband sind sechs Ellipsoide, vier davon liegen in der Schnittebene, zwei über und unter ihr, im Bild ein Kreis. Rechts die Zustandsdichte nach [(3.1)](#gl-3-1) für Silizium. Die Energie steht senkrecht, die Dichte läuft nach rechts.
:::

**Richtungsabhängige Masse.** Hängt die Krümmung von der Richtung ab ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)), gilt um ein Bandminimum

<span class="anker" id="gl-3-2"></span>
$$E-E_\mathrm C=\frac{\hbar^2k_x^2}{2m_x}+\frac{\hbar^2k_y^2}{2m_y}+\frac{\hbar^2k_z^2}{2m_z}. \tag{3.2}$$

Die Fläche gleicher Energie ist ein __Ellipsoid__ mit den Halbachsen $k_i=\sqrt{2m_i(E-E_\mathrm C)}/\hbar$. Sein Volumen ist $\frac43\pi k_xk_yk_z$. Eine Kugel mit derselben Energie hätte $\frac43\pi k^3$. Die Rechnung aus Stufe [2](kreisring-und-kugelschale.html#stufe-2) läuft also unverändert, wenn man $m^{*3}$ durch $m_xm_ym_z$ ersetzt. Gibt es $g$ gleichwertige Täler (Minima an verschiedenen Stellen des $k$-Raums, [Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)), zählt jedes für sich, und die Dichte wird $g$-mal so groß.

:::definition Definition 3.2 (Zustandsdichtemasse)
<span class="anker" id="satz-3-2"></span>

Die __Zustandsdichtemasse__ ist die Masse, die man in die Formel [(3.1)](#gl-3-1) einsetzt, damit sie dieselbe Zahl von Plätzen liefert wie alle Täler zusammen:

<span class="anker" id="gl-3-3"></span>
$$m^*_\mathrm{DOS}=\bigl(g^2\,m_xm_ym_z\bigr)^{1/3}\quad\text{(Raum)},\qquad m^*_\mathrm{DOS}=g\sqrt{m_xm_z}\quad\text{(Ebene)}. \tag{3.3}$$
:::

⁠**So liest man das:** $g$ ist der Entartungsfaktor der Täler. DOS steht für density of states, englisch für Zustandsdichte. Das $g^2$ entsteht so: $D$ wächst mit $m^{3/2}$, also verlangt ein Faktor $g$ in $D$ den Faktor $g^{2/3}$ in der Masse, und in der Klammer steht die dritte Potenz. Das Mittel ist geometrisch, denn ein Volumen ist ein Produkt.

::::beispiel
Silizium hat sechs Täler mit $m_\mathrm h^*=0{,}92\,m_0$ längs und $m_\mathrm l^*=0{,}19\,m_0$ in beiden Querrichtungen ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). Das ergibt $(36\cdot0{,}92\cdot0{,}19^2)^{1/3}m_0=1{,}06\,m_0$. Der Wert des Rechenmodells $1{,}08\,m_0$ ist der bei 300 K übliche, die Massen ändern sich mit der Temperatur leicht. Im Valenzband addieren sich die Bänder der schweren und der leichten Löcher, das ergäbe mit den Massen aus [Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html) $(m_\mathrm{hh}^{*3/2}+m_\mathrm{lh}^{*3/2})^{2/3}=0{,}55\,m_0$. Der bei 300 K übliche Wert $0{,}81\,m_0$ liegt höher, weil diese Bänder nicht exakt parabolisch sind. Bei $E_\mathrm C+k_\mathrm BT$ ist $D_\mathrm C=1{,}23\cdot10^{21}\,\mathrm{eV^{-1}\,cm^{-3}}$. GaAs hat um $\Gamma$ ein einziges Tal mit $0{,}067\,m_0$ und dort nur $1{,}9\cdot10^{19}\,\mathrm{eV^{-1}\,cm^{-3}}$, 65-mal weniger.
::::

⁠**Grenzfall:** Für $g=1$ und gleiche Massen ist $m^*_\mathrm{DOS}=m^*$.

:::frage Warum nicht das arithmetische Mittel $(m_x+m_y+m_z)/3$?
Gezählt wird ein Volumen, und das hängt vom Produkt der Halbachsen ab. Das arithmetische Mittel überschätzt es, besonders bei stark verschiedenen Massen. Für Silizium ohne Talzahl gibt es $0{,}43\,m_0$ statt $0{,}32\,m_0$.
:::

:::aufgabe Aufgabe 4 ★★ Eine Ellipse statt eines Kreises
<span class="anker" id="aufg-4"></span>

In der Ebene gelte $E=\hbar^2k_x^2/(2m_x)+\hbar^2k_z^2/(2m_z)$ mit $m_x=0{,}2\,m_0$ und $m_z=0{,}8\,m_0$.

<ol class="al">

<li>

Wie lang sind die Halbachsen der Linie $E=50$ meV?

</li>

<li>

Zeige mit der Ellipsenfläche $\pi k_xk_z$, dass $m^*_\mathrm{DOS}=\sqrt{m_xm_z}$ gilt. Berechne $D$.

</li>

<li>

Setze $k_x'=k_x\sqrt{\bar m/m_x}$ und $k_z'=k_z\sqrt{\bar m/m_z}$ mit einer beliebigen Masse $\bar m$. Welche Form hat $E(k_x',k_z')$? Um welchen Faktor ändert sich die Fläche je Rasterpunkt?

</li>

</ol>

:::loesung
(a) $k_x=\sqrt{m_xE/(m_0\cdot0{,}0381\,\mathrm{eV\,nm^2})}=0{,}512\,\mathrm{nm^{-1}}$, $k_z=1{,}025\,\mathrm{nm^{-1}}$. (b) Fläche $\pi k_xk_z=2\pi\sqrt{m_xm_z}\,E/\hbar^2$. Der Kreis hat $2\pi m^*E/\hbar^2$, also $m^*_\mathrm{DOS}=\sqrt{m_xm_z}=0{,}4\,m_0$ und $D=1{,}67\cdot10^{14}\,\mathrm{eV^{-1}\,cm^{-2}}$. Das arithmetische Mittel $0{,}5\,m_0$ läge 25 % zu hoch. (c) $E=\hbar^2(k_x'^2+k_z'^2)/(2\bar m)$, ein Kreis. Die Zelle wird um $\bar m/\sqrt{m_xm_z}$ größer, also zählt jeder Rasterpunkt im neuen Raum für $\sqrt{m_xm_z}/\bar m$. Das ergibt $D=(\sqrt{m_xm_z}/\bar m)\cdot\bar m/(\pi\hbar^2)$, und $\bar m$ fällt heraus.
:::
:::

:::aufgabe Aufgabe 5 ★★ Vier Täler
<span class="anker" id="aufg-5"></span>

Germanium hat vier Täler mit $m_\mathrm h^*=1{,}58\,m_0$ längs und $m_\mathrm l^*=0{,}082\,m_0$ in beiden Querrichtungen.

<ol class="al">

<li>

Berechne $m^*_\mathrm{DOS}$.

</li>

<li>

Berechne $D_\mathrm C(E_\mathrm C+50\,\mathrm{meV})$ und vergleiche mit Silizium.

</li>

<li>

Um welchen Faktor wäre die Dichte kleiner, wenn es nur ein Tal gäbe?

</li>

</ol>

:::loesung
(a) $(16\cdot1{,}58\cdot0{,}082^2)^{1/3}m_0=0{,}554\,m_0$. (b) $6{,}28\cdot10^{20}\,\mathrm{eV^{-1}\,cm^{-3}}$, Silizium mit $1{,}08\,m_0$ hat $1{,}71\cdot10^{21}$, Germanium also das 0,37-Fache. (c) Um den Faktor 4, denn $D\propto g$.
:::
:::
