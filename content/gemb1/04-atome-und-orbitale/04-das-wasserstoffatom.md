---
title: Stufe 2: Das Wasserstoffatom
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140400
summary: Der Trichter steht.
tags: Grundzustand, Hauptquantenzahl, Ionisierungsenergie, Bohr-Radius, Bohrschen Atommodell, radiale Wahrscheinlichkeitsdichte
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Der Trichter steht. Diese Stufe findet den tiefsten Zustand, erklärt, warum das Elektron nicht in den Kern stürzt, und nennt alle erlaubten Energien.
:::

**Die Idee.** Zwei Beiträge arbeiten gegeneinander. Zieht sich die Welle auf einen Radius $a$ zusammen, sinkt die potentielle Energie wie $-1/a$. Zugleich wird die Welle stärker gekrümmt, und die kinetische Energie steigt wie $1/a^2$, denn Einsperren kostet Energie ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)). Für die Wellenform $\psi\propto\mathrm{e}^{-r/a}$ gilt genau

<span class="anker" id="gl-2-1"></span>
$$E(a)=\frac{\hbar^2}{2m_0a^2}-\frac{e^2}{4\pi\varepsilon_0a}. \tag{2.1}$$

Bei kleinem $a$ gewinnt der Term $1/a^2$. Deshalb stürzt das Elektron nicht in den Kern: Der Weg dorthin kostet mehr, als er bringt. Bei großem $a$ gewinnt $-1/a$. Dazwischen liegt ein Minimum, und das ist der Grundzustand.

:::satz Satz 2.1 (Wasserstoffatom)
<span class="anker" id="satz-2-1"></span>

Die gebundenen Zustände haben die Energien

<span class="anker" id="gl-2-2"></span>
$$E_n=-\frac{m_0e^4}{8\varepsilon_0^2h^2}\,\frac{1}{n^2}=\frac{E_1}{n^2},\qquad E_1=-13{,}6\,\mathrm{eV},\qquad n=1,2,3,\dots \tag{2.2}$$

Im __Grundzustand__ $n=1$ gilt

<span class="anker" id="gl-2-3"></span>
$$|\psi_1(r)|^2=\frac{1}{\pi r_1^3}\,\exp\Bigl(-\frac{2r}{r_1}\Bigr),\qquad r_1=\frac{\varepsilon_0h^2}{\pi m_0e^2}=0{,}0529\,\mathrm{nm}. \tag{2.3}$$
:::

⁠**So liest man das:** $n$ heißt __Hauptquantenzahl__. Die Energie ist negativ, weil der Nullpunkt beim freien Elektron liegt: Man muss Energie aufwenden, um das Elektron vom Kern zu lösen. Dieser Aufwand heißt __Ionisierungsenergie__, hier $|E_1|=13{,}6$ eV. $r_1$ ist der __Bohr-Radius__, zugleich der Radius der Kreisbahn im __Bohrschen Atommodell__, einem Vorläufer der Quantenmechanik. Aus dieser Zeit stammt der Name Orbital, obwohl es keine Bahn gibt. $|\psi_1|^2$ ist die Dichte an einem Punkt in 1/m$^3$, und $|\psi_1|^2\,\mathrm{d} V$ die Wahrscheinlichkeit im Volumen $\mathrm{d} V$. Für die Kugelschale mit $\mathrm{d} V=4\pi r^2\,\mathrm{d} r$ folgt

<span class="anker" id="gl-2-4"></span>
$$P(r)=4\pi r^2\,|\psi_1(r)|^2, \tag{2.4}$$

die __radiale Wahrscheinlichkeitsdichte__: $P(r)\,\mathrm{d} r$ ist die Wahrscheinlichkeit, das Elektron in der Schale zu finden. **Gültigkeit:** ein Elektron, gebundene Zustände. Für freie Zustände mit $E>0$ gilt [(2.2)](#gl-2-2) nicht.

:::abbildung gemb1/k4radial 2
Grundzustand des Wasserstoffatoms. Links: Die Dichte an einem Punkt ist am Kern am größten. Rechts: Die Wahrscheinlichkeit je Radius ist bei $r=r_1$ am größten, weil die Kugelschalen mit $r^2$ wachsen. Die Fläche unter der Kurve ist 1, innerhalb von $r_1$ liegen 32 %.
:::

:::herleitung Grundzustand durch Einsetzen
Der Grundzustand hängt nicht von den Winkeln ab. Von [(1.2)](der-kern-als-kasten-ohne-wande.html#gl-1-2) bleibt dann $\frac{1}{r^2}(r^2\psi')'=\psi''+\frac2r\psi'$. Mit $\psi=A\,\mathrm{e}^{-r/a}$ ist $\psi'=-\psi/a$ und $\psi''=\psi/a^2$. Einsetzen und Teilen durch $\psi$ ergibt

$$-\frac{\hbar^2}{2m_0}\Bigl(\frac1{a^2}-\frac{2}{a\,r}\Bigr)-\frac{e^2}{4\pi\varepsilon_0\,r}=E.$$

Das muss für jedes $r$ gelten, die beiden Terme mit $1/r$ müssen sich also aufheben:

$$\frac{\hbar^2}{m_0a}=\frac{e^2}{4\pi\varepsilon_0}\quad\Rightarrow\quad a=r_1=\frac{4\pi\varepsilon_0\hbar^2}{m_0e^2}=\frac{\varepsilon_0h^2}{\pi m_0e^2},\qquad E_1=-\frac{\hbar^2}{2m_0r_1^2}=-\frac{m_0e^4}{8\varepsilon_0^2h^2}.$$

Die Normierung verlangt $1=A^2\int_0^\infty\mathrm{e}^{-2r/r_1}\,4\pi r^2\,\mathrm{d} r=A^2\pi r_1^3$. Das ist [(2.3)](#gl-2-3). Für $n\ge2$ hat die Welle Knoten, die Rechnung wird länger und liefert den Faktor $1/n^2$.
:::

**Beispiel.** Es ist $E_2=-3{,}40$ eV und $E_3=-1{,}51$ eV. Fällt das Elektron von $n=3$ auf $n=2$, nimmt ein Photon die Differenz 1,89 eV mit. Das ergibt $\lambda=h\,c/\Delta E=656$ nm, die rote Linie im Licht von Wasserstoff. Die Wärmeenergie bei 300 K ist $k_\mathrm BT=25{,}85$ meV ($k_\mathrm B$: Boltzmann-Konstante). Der Abstand $E_2-E_1=10{,}2$ eV ist 395-mal größer, Wärme hebt das Elektron also nicht an. **Grenzfälle:** Für $n\to\infty$ geht $E_n\to0$, die Niveaus rücken zusammen und gehen in die freien Zustände über. Für $Z$ Protonen und ein Elektron ersetzt man $e^2$ durch $Ze^2$: Dann ist $E_n\propto Z^2$ und $r_1\propto1/Z$.

:::frage In der Box wächst die Energie mit $n^2$. Warum steht hier $1/n^2$, und warum rücken die Niveaus nach oben zusammen?
Die Box hat eine feste Breite, der Trichter wird nach oben breiter. Der Umkehrradius ist $r_\mathrm U=2n^2r_1$. Setzt man $L\propto n^2$ in die Box-Regel $E\propto n^2/L^2$ ein, entsteht $1/n^2$. Das ist nur eine Abschätzung, trifft aber das Gesetz.
:::

:::frage $|\psi_1|^2$ ist am Kern am größten. Warum ist dann $r_1$ der wahrscheinlichste Radius?
Beide Aussagen stimmen, sie antworten auf verschiedene Fragen. Die Dichte gilt für ein festes kleines Volumen. Der Radius zählt alle Punkte einer Kugelschale, und deren Volumen ist bei $r\to0$ winzig. Das Produkt aus fallender Dichte und wachsender Schale hat sein Maximum bei $r_1$.
:::

:::aufgabe Aufgabe 2 ★★ Warum das Elektron nicht in den Kern stürzt
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Berechne die beiden Terme von [(2.1)](#gl-2-1) und ihre Summe für $a=r_1$, $a=r_1/2$ und $a=2r_1$.

</li>

<li>

Zeige durch Ableiten, dass das Minimum genau bei $a=r_1$ liegt.

</li>

<li>

Grenzfälle: Was geschieht mit $E(a)$ für $a\to0$ und für $a\to\infty$?

</li>

<li>

Wiederhole die Rechnung für He$^+$ (Kernladung $2e$). Wie groß sind $a$ und $E$ im Minimum?

</li>

</ol>

:::loesung
(a) $a=r_1$: $13{,}61\,\mathrm{eV}-27{,}21\,\mathrm{eV}=-13{,}61$ eV. $a=r_1/2$: $54{,}4\,\mathrm{eV}-54{,}4\,\mathrm{eV}=0$. $a=2r_1$: $3{,}40\,\mathrm{eV}-13{,}61\,\mathrm{eV}=-10{,}20$ eV. (b) $\mathrm{d} E/\mathrm{d} a=-\hbar^2/(m_0a^3)+e^2/(4\pi\varepsilon_0a^2)=0$ ergibt $a=4\pi\varepsilon_0\hbar^2/(m_0e^2)=r_1$. (c) Für $a\to0$ wächst $E$ wie $+1/a^2$ ohne Grenze: Eine Welle, die auf den Kern zusammenschrumpft, kostet beliebig viel Energie. Für $a\to\infty$ geht $E\to0$ von unten, das ist das freie Elektron. (d) Mit $2e^2$ statt $e^2$ folgt $a=r_1/2=0{,}0265$ nm und $E=4E_1=-54{,}4$ eV.
:::
:::

:::aufgabe Aufgabe 3 ★★ Wo das Elektron sitzt
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Mit welcher Wahrscheinlichkeit liegt das Elektron im Grundzustand innerhalb von $r_1$? Tipp: $\int_0^q4w^2\mathrm{e}^{-2w}\,\mathrm{d} w=1-\mathrm{e}^{-2q}(1+2q+2q^2)$.

</li>

<li>

Das Proton hat den Radius 0,84 fm. Mit welcher Wahrscheinlichkeit liegt das Elektron im Proton? Warum darf $|\psi_1|^2$ dort als konstant gelten?

</li>

<li>

Welche Wellenlänge hat das Photon beim Übergang von $n=2$ nach $n=1$? Welche Wellenlänge ionisiert das Atom aus dem Grundzustand gerade noch?

</li>

</ol>

:::loesung
(a) Mit $w=r/r_1$ ist $\int_0^{r_1}P\,\mathrm{d} r=\int_0^14w^2\mathrm{e}^{-2w}\,\mathrm{d} w=1-5\mathrm{e}^{-2}=0{,}323$, also 32 %. (b) Der Kern ist $6\cdot10^4$-mal kleiner als $r_1$, dort ist $\mathrm{e}^{-2r/r_1}=1$. Mit dem Protonenradius $r_\mathrm p$ ist die Wahrscheinlichkeit $\frac43\pi r_\mathrm p^3\cdot1/(\pi r_1^3)=\frac43(r_\mathrm p/r_1)^3=5{,}3\cdot10^{-15}$. (c) $E_2-E_1=10{,}20$ eV gibt $\lambda=h\,c/\Delta E=121{,}5$ nm, die Ionisierung mit 13,61 eV gibt 91,1 nm. Beides liegt im Ultraviolett.
:::
:::
