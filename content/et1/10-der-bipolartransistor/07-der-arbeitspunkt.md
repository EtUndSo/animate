---
title: Stufe 5: Der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1200700
summary: Welcher Bereich gilt, weiß man vorher nicht.
tags: Arbeitsgerade, Versorgungsspannung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Welcher Bereich gilt, weiß man vorher nicht. Diese Stufe bestimmt den Arbeitspunkt durch Annehmen und Prüfen und zeichnet ihn als Schnittpunkt.
:::

**Die Idee.** Der Transistor liefert seine Kennlinien, der Stromkreis Maschengleichungen. Beide müssen zugleich gelten. Das Ergebnis ist der Arbeitspunkt (AP), wie in [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) der Schnitt einer Kennlinie mit einer Geraden. Weil jeder Bereich ein anderes Ersatzschaltbild hat, nimmt man einen Bereich an, rechnet linear und prüft. Ein Widerspruch zu den Bedingungen [(4.1)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-1) bis [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) verrät die falsche Annahme.

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

**Beispiel.** Rechenmodell: $I_\mathrm{B}=(5\,\mathrm{V}-0{,}6\,\mathrm{V})/440\,\text{k}\Omega=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-6\,\mathrm{V}=6$ V. Das ist mehr als 0,2 V, also aktiv (Punkt A). Eine falsche erste Annahme schadet nicht: Sättigung ergäbe $I_\mathrm{C}=3{,}93$ mA, aber $B\,I_\mathrm{B}=2$ mA ist kleiner, im Widerspruch zu [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3). Für $U_\mathrm{ein}=12$ V ist $I_\mathrm{B}=25{,}9$ µ A. Aktiv angenommen käme $U_\mathrm{CE}=-3{,}5$ V heraus, also Widerspruch. In der Sättigung sind $I_\mathrm{C}=3{,}93$ mA und $B\,I_\mathrm{B}=5{,}18$ mA (Punkt S). **Grenzfälle:** $R_\mathrm{C}=0$ ergibt $U_\mathrm{CE}=U_\mathrm{CC}$, der Ausgang ist starr. $U_\mathrm{ein}<0{,}6$ V ergibt $I_\mathrm{C}=0$ und $U_\mathrm{CE}=12$ V (Punkt Z).

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
