---
title: Stufe 5: Der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200700
summary: Welcher Bereich gilt, weiß man vorher nicht.
tags: Arbeitsgerade, Versorgungsspannung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Welcher Bereich gilt, weiß man vorher nicht. Diese Stufe bestimmt den Arbeitspunkt durch Annehmen und Prüfen und zeichnet ihn als Schnittpunkt.
:::

**Die Idee.** Der Transistor liefert seine Kennlinien, der Stromkreis Maschengleichungen. Beide müssen zugleich gelten. Das Ergebnis ist der Arbeitspunkt (AP), wie in [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) der Schnitt einer Kennlinie mit einer Geraden. Weil jeder Bereich ein anderes Ersatzschaltbild hat, nimmt man einen Bereich an, rechnet linear und prüft. Ein Widerspruch zu den Bedingungen [(4.1)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-1) bis [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) verrät die falsche Annahme.

:::abbildung et1/k10arbeit 6
Links die Schaltung des Rechenmodells. Rechts die linearisierten Ausgangskennlinien mit der Arbeitsgeraden von $(0;\,4\,\mathrm{mA})$ nach $(12\,\mathrm{V};\,0)$. Sie trifft die Linie $I_\mathrm{B}=10$ µ A im Arbeitspunkt A. S ist der Punkt in der Sättigung, Z der Punkt im Sperrbereich.
:::

:::satz Satz 5.1 (Arbeitspunkt der Schaltung mit Basis- und Kollektorwiderstand)
<span class="anker" id="satz-5-1"></span>

Die Eingangsmasche ist $U_\mathrm{ein}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$, die Ausgangsmasche die __Arbeitsgerade__ $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$. Für $U_\mathrm{ein}\le U_\mathrm{BE,ein}$ sperrt der Transistor, und es gilt $U_\mathrm{BE}=U_\mathrm{ein}$. Für $U_\mathrm{ein}>U_\mathrm{BE,ein}$ ist in beiden leitenden Bereichen

<span class="anker" id="gl-5-1"></span>
$$I_\mathrm{B}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{B}}. \tag{5.1}$$

Aktiv angenommen folgt

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{C}=B\,I_\mathrm{B},\qquad U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}. \tag{5.2}$$

Ist das Ergebnis $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$, stimmt die Annahme. Sonst liegt Sättigung vor mit

<span class="anker" id="gl-5-3"></span>
$$U_\mathrm{CE}=U_\mathrm{CE,sat},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}. \tag{5.3}$$
:::

⁠**So liest man das:** $U_\mathrm{CC}$ ist die __Versorgungsspannung__, $U_\mathrm{ein}$ die Eingangsspannung gegen Masse. $R_\mathrm{B}$ setzt den Basisstrom, $R_\mathrm{C}$ wandelt den Kollektorstrom in eine Spannung. **Gültigkeit:** Emitter an Masse, das lineare Modell aus Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4). Gleichung [(5.1)](#gl-5-1) gilt in beiden leitenden Bereichen, weil dort dieselbe 0,6-V-Quelle zwischen B und E liegt.

::::beispiel
Rechenmodell: $I_\mathrm{B}=(5\,\mathrm{V}-0{,}6\,\mathrm{V})/440\,\text{k}\Omega=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-6\,\mathrm{V}=6$ V. Das ist mehr als 0,2 V, also aktiv (Punkt A). Eine falsche erste Annahme schadet nicht: Sättigung ergäbe $I_\mathrm{C}=3{,}93$ mA, aber $B\,I_\mathrm{B}=2$ mA ist kleiner, im Widerspruch zu [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3). Für $U_\mathrm{ein}=12$ V ist $I_\mathrm{B}=25{,}9$ µ A. Aktiv angenommen käme $U_\mathrm{CE}=-3{,}5$ V heraus, also Widerspruch. In der Sättigung sind $I_\mathrm{C}=3{,}93$ mA und $B\,I_\mathrm{B}=5{,}18$ mA (Punkt S).
::::

⁠**Grenzfälle:** $R_\mathrm{C}=0$ ergibt $U_\mathrm{CE}=U_\mathrm{CC}$, der Ausgang ist starr. $U_\mathrm{ein}<0{,}6$ V ergibt $I_\mathrm{C}=0$ und $U_\mathrm{CE}=12$ V (Punkt Z).

**Die Mitte des aktiven Bereichs.** Im aktiven Bereich liegt $U_\mathrm{CE}$ zwischen 0,2 V und $U_\mathrm{CC}$. Damit ein Signal nach beiden Seiten gleich viel Platz hat, legt man den Punkt in die Mitte. Mit $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}=11{,}8$ V ist

<span class="anker" id="gl-5-4"></span>
$$U_\mathrm{CE,AP}=U_\mathrm{CE,sat}+\frac{\Delta U}{2}=6{,}1\,\mathrm{V},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,AP}}{R_\mathrm{C}}=1{,}97\,\mathrm{mA}. \tag{5.4}$$

Daraus folgt $R_\mathrm{B}=(U_\mathrm{ein}-U_\mathrm{BE})\,B/I_\mathrm{C}=447$ k$\Omega$. Die 440 k$\Omega$ des Rechenmodells liegen fast dort.

**Mit Emitterwiderstand.** Liegt die Basis direkt an $U_\mathrm{ein}$ und der Emitter über $R_\mathrm{E}$ an Masse, lautet die Eingangsmasche $U_\mathrm{ein}=U_\mathrm{BE,ein}+R_\mathrm{E}I_\mathrm{E}$. Für $U_\mathrm{ein}>0{,}6$ V sperrt der Transistor nicht, und

<span class="anker" id="gl-5-5"></span>
$$I_\mathrm{E}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{E}},\quad I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B},\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}. \tag{5.5}$$

Mit $U_\mathrm{ein}=2{,}6$ V und $R_\mathrm{E}=1$ k$\Omega$ sind $I_\mathrm{E}=2$ mA, $I_\mathrm{C}=1{,}99$ mA und $U_\mathrm{CE}=4{,}03$ V. Hier kam $B$ erst im letzten Schritt ins Spiel und ändert fast nichts. Das nutzt Stufe [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7).

:::aufgabe Aufgabe 5 ★★ Arbeitspunkt rechnen
<span class="anker" id="aufg-5"></span>

Gegeben sind T, $U_\mathrm{CC}=10$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{B}=220$ k$\Omega$. (a) Bestimme den Arbeitspunkt für $U_\mathrm{ein}=3$ V. (b) Bestimme ihn für $U_\mathrm{ein}=8$ V. (c) Welches $R_\mathrm{B}$ legt den Punkt bei $U_\mathrm{ein}=3$ V in die Mitte des aktiven Bereichs?

:::loesung
(a) $I_\mathrm{B}=2{,}4\,\mathrm{V}/220\,\text{k}\Omega=10{,}9$ µ A, $I_\mathrm{C}=2{,}18$ mA, $U_\mathrm{CE}=10\,\mathrm{V}-4{,}36\,\mathrm{V}=5{,}64$ V: aktiv.

(b) $I_\mathrm{B}=33{,}6$ µ A, $B\,I_\mathrm{B}=6{,}73$ mA. Aktiv angenommen wäre $U_\mathrm{CE}=-3{,}45$ V, ein Widerspruch. Also Sättigung: $U_\mathrm{CE}=0{,}2$ V, $I_\mathrm{C}=9{,}8\,\mathrm{V}/2\,\text{k}\Omega=4{,}9$ mA $<6{,}73$ mA.

(c) $U_\mathrm{CE,AP}=0{,}2\,\mathrm{V}+4{,}9\,\mathrm{V}=5{,}1$ V, $I_\mathrm{C}=4{,}9\,\mathrm{V}/2\,\text{k}\Omega=2{,}45$ mA, $I_\mathrm{B}=12{,}25$ µ A, $R_\mathrm{B}=2{,}4\,\mathrm{V}/12{,}25\,\mu\text{A}=196$ k$\Omega$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Emitterwiderstand
<span class="anker" id="aufg-6"></span>

Die Basis von T liegt direkt an $U_\mathrm{ein}=1{,}6$ V, dazu $U_\mathrm{CC}=12$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{E}=500\,\Omega$. (a) Bestimme $I_\mathrm{E}$, $I_\mathrm{B}$, $I_\mathrm{C}$ und $U_\mathrm{CE}$. (b) Was ändert sich, wenn $B$ auf 100 sinkt?

:::loesung
(a) $I_\mathrm{E}=1\,\mathrm{V}/500\,\Omega=2$ mA, $I_\mathrm{B}=2\,\mathrm{mA}/201=9{,}95$ µ A, $I_\mathrm{C}=1{,}99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3{,}98\,\mathrm{V}-1\,\mathrm{V}=7{,}02$ V.

(b) $I_\mathrm{E}$ bleibt 2 mA, denn es hängt nur an $U_\mathrm{ein}$ und $R_\mathrm{E}$. $I_\mathrm{B}$ wird 19,8 µ A, $I_\mathrm{C}$ wird 1,98 mA, $U_\mathrm{CE}$ wird 7,04 V. Halbes $B$, aber nur 0,5 % weniger Kollektorstrom.
:::
:::

::::formelsammlung
**Eingangsmasche**

$$U_\mathrm{ein}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$$

Schaltung mit Basiswiderstand $R_\mathrm{B}$ und Kollektorwiderstand $R_\mathrm{C}$, Emitter an Masse, Eingangsspannung $U_\mathrm{ein}$ gegen Masse. Für $U_\mathrm{ein}\le U_\mathrm{BE,ein}$ sperrt der Transistor, und $U_\mathrm{BE}=U_\mathrm{ein}$.

**Arbeitsgerade**

$$U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$$

Ausgangsmasche mit der Versorgungsspannung $U_\mathrm{CC}$; im Rechenmodell von $(0;\,4\,\mathrm{mA})$ nach $(12\,\mathrm{V};\,0)$. Der Arbeitspunkt ist ihr Schnitt mit der Kennlinie.

**Basisstrom im leitenden Betrieb**

$$I_\mathrm{B}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{B}}$$

Für $U_\mathrm{ein}>U_\mathrm{BE,ein}$, in beiden leitenden Bereichen, weil dort dieselbe 0,6-V-Quelle zwischen B und E liegt.

**Arbeitspunkt, aktiv angenommen**

$$I_\mathrm{C}=B\,I_\mathrm{B},\qquad U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$$

Die Annahme stimmt, wenn $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$ herauskommt.

**Arbeitspunkt in der Sättigung**

$$U_\mathrm{CE}=U_\mathrm{CE,sat},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}$$

Gilt, wenn die aktive Annahme $U_\mathrm{CE}<U_\mathrm{CE,sat}$ ergibt.

**Mitte des aktiven Bereichs**

$$U_\mathrm{CE,AP}=U_\mathrm{CE,sat}+\frac{\Delta U}{2},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,AP}}{R_\mathrm{C}}$$

Mit $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}$; ein Signal hat dann nach beiden Seiten gleich viel Platz. Der passende Basiswiderstand ist $R_\mathrm{B}=(U_\mathrm{ein}-U_\mathrm{BE})\,B/I_\mathrm{C}$.

**Arbeitspunkt mit Emitterwiderstand**

$$I_\mathrm{E}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{E}},\quad I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B},\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}$$

Basis direkt an $U_\mathrm{ein}$, Emitter über $R_\mathrm{E}$ an Masse, $U_\mathrm{ein}>0{,}6$ V; aus der Masche $U_\mathrm{ein}=U_\mathrm{BE,ein}+R_\mathrm{E}I_\mathrm{E}$. $B$ geht erst im letzten Schritt ein und ändert fast nichts.
::::

::::lernkarten
:::karte zusammenhang Arbeitspunkt
Wie legt die äußere Schaltung den Arbeitspunkt eines Transistors fest?
---
Der Transistor liefert Kennlinien, der Stromkreis Maschengleichungen, und beide müssen zugleich gelten. Der Arbeitspunkt ist der Gleichstromzustand, der beides erfüllt: der Schnitt der Arbeitsgeraden mit einer Kennlinie.
--- falsch
Der Transistor wählt seinen Arbeitspunkt selbst, und zwar immer im Knick der Eingangskennlinie bei 0,6 V. Die äußere Schaltung bestimmt nur, wie viel Strom dort fließt, nicht, in welchem Bereich er liegt.
--- falsch
Die Versorgungsspannung allein legt ihn fest: Der Arbeitspunkt liegt immer bei $U_\mathrm{CE}=U_\mathrm{CC}/2$, gleich welche Widerstände angeschlossen sind und welches $B$ der Transistor hat, weil sich die Spannung symmetrisch aufteilt.
--- falsch
Der Arbeitspunkt ist der Punkt, an dem die Kennlinien zweier Transistoren sich schneiden. Die äußere Schaltung legt fest, welche zwei Kennlinien man dafür verwendet.
:::
:::karte begriff Versorgungsspannung
Welche Aufgabe hat die Versorgungsspannung $U_\mathrm{CC}$ in der Schaltung mit Basis- und Kollektorwiderstand?
---
Die Gleichspannung, die den Ausgangskreis aus Kollektorwiderstand und Transistor speist. Aus ihr kommt die Energie am Ausgang, das Eingangssignal stellt nur ein.
--- falsch
Die Eingangsspannung gegen Masse, die über $R_\mathrm{B}$ den Basisstrom einstellt. Aus ihr kommt das Signal, das der Transistor am Ausgang verstärkt wiedergibt.
--- falsch
Die Spannung zwischen Basis und Emitter, die den Transistor leitend macht. Sie beträgt im leitenden Betrieb immer rund 0,6 V.
--- falsch
Die Spannung, die am Kollektorwiderstand abfällt. Aus ihr folgt mit dem ohmschen Gesetz direkt der Basisstrom, der den Transistor steuert.
:::
:::karte zusammenhang Arbeitsgerade
Warum ist die Ausgangsmasche $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$ eine Gerade im Ausgangskennlinienfeld, und wo verläuft sie im Rechenmodell?
---
Sie hängt linear von $I_\mathrm{C}$ ab, weil nur der Widerstand $R_\mathrm{C}$ und die Quelle $U_\mathrm{CC}$ den Kreis bilden. Im Rechenmodell verbindet sie $(0;\,4\,\mathrm{mA})$ und $(12\,\mathrm{V};\,0)$.
--- falsch
Sie ist eine Gerade, weil der Transistor im aktiven Bereich wie ein Widerstand wirkt. Im Rechenmodell verbindet sie $(0;\,2\,\mathrm{mA})$ und $(6\,\mathrm{V};\,0)$, den Arbeitspunkt.
--- falsch
Sie ist eine Gerade, weil $I_\mathrm{C}=B\,I_\mathrm{B}$ linear ist. Im Rechenmodell läuft sie waagerecht bei 2 mA, weil der Basisstrom fest ist.
--- falsch
Sie hängt linear von $I_\mathrm{C}$ ab, weil $R_\mathrm{C}$ fest ist. Im Rechenmodell verläuft sie senkrecht bei 12 V, weil die Versorgung die Spannung festhält.
:::
:::karte formel Basisstrom in den leitenden Bereichen
Wie groß ist $I_\mathrm{B}$ in der Schaltung mit Basis- und Kollektorwiderstand, wenn der Transistor leitet, und warum gilt die Formel in beiden leitenden Bereichen?
---
$I_\mathrm{B}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{B}}$ für $U_\mathrm{ein}>U_\mathrm{BE,ein}$, aus der Eingangsmasche $U_\mathrm{ein}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$. In beiden Bereichen liegt dieselbe 0,6-V-Quelle zwischen B und E.
--- falsch
$I_\mathrm{B}=\frac{U_\mathrm{ein}}{R_\mathrm{B}}$ für jedes $U_\mathrm{ein}$, aus dem ohmschen Gesetz am Basiswiderstand. Die Basis liegt in beiden Bereichen an Masse, deshalb fällt dort keine Spannung ab.
--- falsch
$I_\mathrm{B}=\frac{U_\mathrm{CC}-U_\mathrm{BE,ein}}{R_\mathrm{B}}$ für $U_\mathrm{CC}>U_\mathrm{BE,ein}$, aus der Ausgangsmasche. In beiden Bereichen fließt der Basisstrom aus der Versorgung über $R_\mathrm{C}$.
--- falsch
$I_\mathrm{B}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{B}}$, aber nur im aktiven Bereich. In der Sättigung sinkt $U_\mathrm{BE}$ auf $U_\mathrm{CE,sat}$, und der Basisstrom wird entsprechend größer.
:::
:::karte formel Arbeitspunkt aktiv oder gesättigt
Welche Werte haben $I_\mathrm{C}$ und $U_\mathrm{CE}$ in der Schaltung mit Basis- und Kollektorwiderstand, wenn der Transistor aktiv ist, und welche in der Sättigung?
---
Aktiv: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$, gültig, wenn $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$ herauskommt. Sonst Sättigung: $U_\mathrm{CE}=U_\mathrm{CE,sat}$, $I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}$.
--- falsch
Aktiv: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}+B\,I_\mathrm{B}R_\mathrm{C}$, gültig, wenn $U_\mathrm{CE}\le U_\mathrm{CC}$ herauskommt. Sonst Sättigung: $U_\mathrm{CE}=U_\mathrm{CC}$, $I_\mathrm{C}=0$.
--- falsch
Aktiv: $I_\mathrm{C}=\frac{U_\mathrm{CC}}{R_\mathrm{C}}$, $U_\mathrm{CE}=U_\mathrm{CE,sat}$, gültig für jedes $I_\mathrm{B}>0$. Sättigung: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$, wenn das Ergebnis für $U_\mathrm{CE}$ negativ wird.
--- falsch
Aktiv: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$, gültig für jedes Ergebnis. Sättigung tritt nur auf, wenn $I_\mathrm{B}$ größer als $I_\mathrm{C}$ wird, unabhängig von $R_\mathrm{C}$.
:::
:::karte herleitung Annehmen und Prüfen
Wie bestimmt man den Arbeitspunkt der Schaltung mit $R_\mathrm{B}$ und $R_\mathrm{C}$, wenn man den Bereich vorher nicht kennt?
---
Man vergleicht $U_\mathrm{ein}$ mit $U_\mathrm{BE,ein}$, weil der Transistor für $U_\mathrm{ein}\le U_\mathrm{BE,ein}$ sperrt und dann $I_\mathrm{C}=0$ gilt.
---
Sonst berechnet man $I_\mathrm{B}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{B}}$, weil in beiden leitenden Bereichen dieselbe 0,6-V-Quelle zwischen B und E liegt.
---
Man nimmt den aktiven Bereich an und rechnet $U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$, weil dort $I_\mathrm{C}=B\,I_\mathrm{B}$ gilt und die Arbeitsgerade den Rest liefert.
---
Ist $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$, stimmt die Annahme, sonst liegt Sättigung vor, weil ein Widerspruch zu den Bedingungen des Bereichs die falsche Annahme verrät.
---
In der Sättigung gilt $U_\mathrm{CE}=U_\mathrm{CE,sat}$ und $I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}$, weil dann zwischen C und E die 0,2-V-Quelle liegt.
:::
:::karte zusammenhang Falsche erste Annahme
Was passiert, wenn man für den Arbeitspunkt des Rechenmodells zuerst den falschen Bereich annimmt?
---
Nichts Schlimmes: Das Ergebnis widerspricht dann den Bedingungen des angenommenen Bereichs. Sättigung ergäbe $I_\mathrm{C}=3{,}93$ mA, aber $B\,I_\mathrm{B}=2$ mA ist kleiner, also ist der Transistor aktiv.
--- falsch
Man erhält einen zweiten, ebenso gültigen Arbeitspunkt. Der Transistor kann dann zwischen beiden springen, je nachdem, welcher Bereich beim Einschalten zuerst erreicht wird.
--- falsch
Die Rechnung liefert dann ein Ergebnis, das ohne Widerspruch aussieht. Den Fehler erkennt man erst mit einer Messung, weil die Bedingungen der Bereiche dafür nicht ausreichen.
--- falsch
Das Ergebnis ist trotzdem richtig, weil beide Ersatzschaltbilder dieselben Werte liefern. Im Rechenmodell ergeben aktiver Bereich und Sättigung beide $I_\mathrm{C}=2$ mA.
:::
:::karte formel Mitte des aktiven Bereichs
Wo legt man den Arbeitspunkt auf die Arbeitsgerade, damit ein Signal nach beiden Seiten gleich viel Platz hat, und welche Formel ergibt sich?
---
In die Mitte des aktiven Bereichs: $U_\mathrm{CE,AP}=U_\mathrm{CE,sat}+\frac{\Delta U}{2}$ mit $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}$, dazu $I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,AP}}{R_\mathrm{C}}$. Im Rechenmodell sind das 6,1 V und 1,97 mA.
--- falsch
In die Mitte der Versorgung: $U_\mathrm{CE,AP}=\frac{U_\mathrm{CC}}{2}$, dazu $I_\mathrm{C}=\frac{U_\mathrm{CC}}{R_\mathrm{C}}$. Im Rechenmodell sind das 6 V und 4 mA, der volle Strom der Arbeitsgeraden.
--- falsch
Möglichst nahe an die Sättigung: $U_\mathrm{CE,AP}=U_\mathrm{CE,sat}$, dazu $I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}$. Dort ist der Strom am größten und das Signal deshalb am stärksten und saubersten.
--- falsch
In die Mitte des aktiven Bereichs: $U_\mathrm{CE,AP}=U_\mathrm{CE,sat}+\Delta U$ mit $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}$, dazu $I_\mathrm{C}=B\,I_\mathrm{B}$. Im Rechenmodell sind das 12 V und 2 mA.
:::
:::karte formel Arbeitspunkt mit Emitterwiderstand
Wie berechnet man den Arbeitspunkt, wenn die Basis direkt an $U_\mathrm{ein}$ liegt und der Emitter über $R_\mathrm{E}$ an Masse?
---
Aus der Masche $U_\mathrm{ein}=U_\mathrm{BE,ein}+R_\mathrm{E}I_\mathrm{E}$: $I_\mathrm{E}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{E}}$, $I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B}$, $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}$; für $U_\mathrm{ein}>0{,}6$ V.
--- falsch
Aus der Masche $U_\mathrm{ein}=R_\mathrm{E}I_\mathrm{B}$: $I_\mathrm{B}=\frac{U_\mathrm{ein}}{R_\mathrm{E}}$, $I_\mathrm{C}=B\,I_\mathrm{B}$, $I_\mathrm{E}=(1+B)\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$; der Emitterwiderstand spielt für $U_\mathrm{CE}$ keine Rolle.
--- falsch
Aus der Masche $U_\mathrm{ein}=U_\mathrm{BE,ein}+R_\mathrm{E}I_\mathrm{E}$: $I_\mathrm{E}=\frac{U_\mathrm{ein}-U_\mathrm{BE,ein}}{R_\mathrm{E}}$, $I_\mathrm{C}=(1+B)\,I_\mathrm{E}$, $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}+R_\mathrm{E}I_\mathrm{E}$; für jedes $U_\mathrm{ein}$.
--- falsch
Aus der Masche $U_\mathrm{CC}=U_\mathrm{BE,ein}+R_\mathrm{E}I_\mathrm{E}$: $I_\mathrm{E}=\frac{U_\mathrm{CC}-U_\mathrm{BE,ein}}{R_\mathrm{E}}$, $I_\mathrm{B}=\frac{I_\mathrm{E}}{B}$, $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{E}I_\mathrm{E}$; $U_\mathrm{ein}$ legt nur fest, ob der Transistor leitet.
:::
:::karte zusammenhang Emitterwiderstand macht B fast unwichtig
Warum ändert ein kleineres $B$ den Kollektorstrom kaum, wenn die Basis direkt an $U_\mathrm{ein}$ liegt und der Emitter über $R_\mathrm{E}$ an Masse?
---
$I_\mathrm{E}$ folgt nur aus $U_\mathrm{ein}$, $U_\mathrm{BE,ein}$ und $R_\mathrm{E}$. $B$ kommt erst beim Aufteilen von $I_\mathrm{E}$ in Basis- und Kollektorstrom ins Spiel: Halbes $B$ senkt $I_\mathrm{C}$ nur um rund 0,5 %.
--- falsch
Weil $R_\mathrm{E}$ den Basisstrom auf einen festen Wert begrenzt. $I_\mathrm{C}=B\,I_\mathrm{B}$ ändert sich deshalb zwar proportional zu $B$, aber der Emitterwiderstand gleicht das über $U_\mathrm{CE}$ aus.
--- falsch
Weil der Transistor mit Emitterwiderstand immer gesättigt ist. In der Sättigung legen nur $U_\mathrm{CC}$ und die Widerstände den Strom fest, $B$ spielt dort keine Rolle mehr.
--- falsch
Weil $R_\mathrm{E}$ den Transistor so stark erwärmt, dass $B$ immer auf denselben Wert steigt. Exemplare mit kleinem $B$ gleichen sich dadurch den anderen an.
:::
::::
