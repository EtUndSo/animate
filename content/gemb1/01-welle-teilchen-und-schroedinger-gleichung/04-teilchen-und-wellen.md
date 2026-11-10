---
title: Stufe 2: Teilchen und Wellen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung
knoten: Kapitel 1: Welle, Teilchen und Schrödinger-Gleichung
order: 4110400
summary: Das Gasmodell behandelt Elektronen als Kugeln.
tags: Photonen, Welle-Teilchen-Dualismus, Materiewelle, Wellenvektor, plancksche Wirkungsquantum
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Das Gasmodell behandelt Elektronen als Kugeln. Diese Stufe widerlegt das mit einem Versuch und nennt die Regel, die Teilchen und Wellen verbindet.
:::

**Die Idee.** Vor einem Schirm steht eine Wand mit zwei engen Spalten (Abb. [2](#abb-2)). Kugeln fliegen durch den einen oder anderen Spalt und häufen sich an zwei Stellen. Eine Welle läuft durch beide zugleich. Dahinter überlagern sich zwei Kreiswellen: Berg auf Berg verstärkt, Berg auf Tal löscht aus, und auf dem Schirm entstehen viele Streifen. Elektronen zeigen beides. Jedes kommt als einzelner Punkt an wie ein Teilchen. Aus vielen Punkten wächst aber das Streifenmuster einer Welle, auch wenn immer nur ein Elektron unterwegs ist. Schließt man einen Spalt, verschwinden die Streifen. Auch Licht zeigt beides: Es interferiert als Welle und besteht zugleich aus abzählbaren Teilchen, den __Photonen__. Strahlung und Materie haben also zugleich Teilchen- und Welleneigenschaften (__Welle-Teilchen-Dualismus__). Eine Welle, die zu Materie gehört, heißt __Materiewelle__.

:::abbildung gemb1/k1doppelspalt 2
Links: Kugeln treffen an zwei Stellen auf. Rechts: Die Wellen aus beiden Spalten überlagern sich, die Dichte der Elektronen zeigt Streifen (rot, Einhüllende schematisch). Unten: Jedes Elektron erzeugt genau einen Punkt, das Muster entsteht erst aus vielen Punkten (zufällig gezogen aus der roten Verteilung).
:::

:::satz Satz 2.1 (de-Broglie-Beziehung)
<span class="anker" id="satz-2-1"></span>

Zu einem Teilchen mit der Energie $E$ und dem Impuls $p$ gehört eine Welle mit Frequenz $\nu$ und Wellenlänge $\lambda$:

<span class="anker" id="gl-2-1"></span>
$$E=h\,\nu=\hbar\,\omega,\qquad p=\frac h\lambda=\frac h{2\pi}\frac{2\pi}\lambda=\hbar\,k. \tag{2.1}$$

In drei Dimensionen sind Impuls und Wellenzahl Vektoren, $\boldsymbol p=\hbar\boldsymbol k$. Der __Wellenvektor__ $\boldsymbol k$ zeigt in Laufrichtung und hat den Betrag $2\pi/\lambda$.
:::

⁠**So liest man das:** Links stehen Teilcheneigenschaften, rechts Welleneigenschaften. $h$ ist das __plancksche Wirkungsquantum__, $\hbar=h/(2\pi)$ sagt man „h quer“. Einheiten: $[p]=\text{kg\,m/s}=\text{eV\,s/m}$, $[k]=1/\text{m}$. Für Teilchen weit unter Lichtgeschwindigkeit gilt $p=m\,v=\sqrt{2mE_\mathrm{kin}}$ und damit

<span class="anker" id="gl-2-2"></span>
$$\lambda=\frac h{\sqrt{2mE_\mathrm{kin}}}. \tag{2.2}$$

⁠**Gültigkeit:** [(2.1)](#gl-2-1) ist ein Befund aus dem Experiment und gilt für alle Teilchen. Die Welle fällt nur auf, wenn $\lambda$ nicht viel kleiner ist als die Strukturen, an denen sie gebeugt, also abgelenkt wird.

:::herleitung Wo die Streifen liegen
Die Spalte haben den Abstand $s$, der Schirm die Entfernung $D\gg s$. Zum Schirmpunkt $y$ unter dem kleinen Winkel $\theta$ ist der Weg von einem Spalt um $s\sin\theta\approx s\,y/D$ länger als vom anderen. Hell ist es, wenn dieser Unterschied ein ganzes Vielfaches von $\lambda$ beträgt. Benachbarte Streifen haben also den Abstand $y_\mathrm S=\lambda\,D/s$.
:::

::::beispiel
Die Elektronen aus Stufe [1](elektronen-als-gas.html#stufe-1) haben $E_\mathrm{kin}=\frac32k_\mathrm BT=38{,}8$ meV, also nach [(2.2)](#gl-2-2) $\lambda=6{,}2$ nm. Das ist das 24-fache des Atomabstands in Kupfer (0,26 nm) und das Sechsfache der angenommenen freien Weglänge. Eine Kugel, die von Atom zu Atom fliegt, ist also schon nach den eigenen Zahlen das falsche Bild. Das Probe-Elektron mit 1 eV hat $p=5{,}40\cdot10^{-25}$ kg m/s, $k=5{,}12\cdot10^{9}\,\mathrm{m^{-1}}$ und $\lambda=1{,}23$ nm.
::::

⁠**Grenzfall:** Ein Staubkorn von 1 µ g mit 1 mm/s hat $\lambda=6{,}6\cdot10^{-22}$ m. Für große Masse geht $\lambda\to0$, die Streifen rücken zusammen, bis nur die zwei Häufungen bleiben. Deshalb sieht man im Alltag keine Materiewellen.

:::frage Geht ein Elektron nun durch einen Spalt oder durch beide?
Ein Messgerät am Spalt findet immer ein ganzes Elektron, das stimmt. Aber diese Messung zerstört die Streifen. Ohne Messung beschreibt nur eine Welle durch beide Spalte das Ergebnis. „Durch welchen“ setzt eine Bahn voraus, und die gibt es hier nicht.
:::

:::aufgabe Aufgabe 2 ★★ Wellenlängen und Doppelspalt
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Berechne $\lambda$ für Elektronen mit 0,05 eV, 1 eV und 100 eV. Welche dieser Wellen taugt, um Atomabstände von 0,3 nm durch Beugung zu untersuchen?

</li>

<li>

Um welchen Faktor ist $\lambda$ für ein Proton ($m=1{,}673\cdot10^{-27}$ kg) mit 1 eV kürzer als für das Elektron?

</li>

<li>

Elektronen durchlaufen 1 kV und treffen auf einen Doppelspalt mit $s=0{,}5$ µ m, der Schirm steht bei $D=2$ m. Berechne $\lambda$ und $y_\mathrm S$.

</li>

<li>

Alle 1 ms startet ein Elektron. Wie lang ist die Flugzeit? Was folgt daraus für die Herkunft der Streifen?

</li>

<li>

Vorhersage: Eine Stelle war dunkel. Was geschieht dort, wenn du einen Spalt schließt?

</li>

</ol>

:::loesung
(a) Nach [(2.2)](#gl-2-2): 5,48 nm, 1,23 nm, 0,123 nm. Die Welle mit 100 eV taugt. Ihre Wellenlänge liegt in der Größenordnung des Atomabstands, daher entstehen gut messbare Beugungswinkel. Viel längere Wellen lösen den Abstand nicht auf. (b) $\lambda\propto1/\sqrt m$, der Faktor ist $\sqrt{m/m_0}=42{,}9$, also 28,6 pm. (c) 1 keV sind 0,2 % der Ruheenergie von 511 keV, die klassische Formel genügt: $\lambda=38{,}8$ pm, $v=1{,}9\cdot10^{7}$ m/s, $y_\mathrm S=\lambda\,D/s=155$ µ m. (d) Die Flugzeit ist $D/v=107$ ns, viel kürzer als 1 ms. Es ist also immer nur ein Elektron unterwegs. Die Streifen entstehen nicht durch Stöße zwischen Elektronen, jede Welle interferiert mit sich selbst. (e) Die Stelle wird hell. Vorher löschten sich beide Anteile aus, jetzt fehlt einer: Weniger Öffnung bringt dort mehr Treffer.
:::
:::
