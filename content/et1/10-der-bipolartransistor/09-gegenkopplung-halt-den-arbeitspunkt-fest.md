---
title: Stufe 7: Gegenkopplung hält den Arbeitspunkt fest
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200900
summary: Der Arbeitspunkt aus Stufe 5 hängt an B und an U BE , und beide sind unzuverlässig.
tags: Stromgegenkopplung, Spannungsgegenkopplung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Der Arbeitspunkt aus Stufe [5](der-arbeitspunkt.html#stufe-5) hängt an $B$ und an $U_\mathrm{BE}$, und beide sind unzuverlässig. Diese Stufe zeigt, wie die Schaltung den Strom selbst festhält.
:::

**Die Idee.** Im Rechenmodell ist $I_\mathrm{C}=B\cdot10$ µ A. Ein Exemplar mit $B=100$ führt 1 mA ($U_\mathrm{CE}=9$ V), eines mit $B=400$ erreicht die Sättigung. Eine feste Spannung $U_\mathrm{BE}$ wäre schlimmer: Bei festem Strom sinkt $U_\mathrm{BE}$ um rund 2 mV je Kelvin, und 18 mV verdoppeln den Strom, also verdoppeln schon 9 K Erwärmung $I_\mathrm{C}$.

Die Abhilfe ist ein Widerstand im Emitter. Ein Teiler hält das Basispotenzial nahezu fest. Der Strom läuft nun in einer Schleife gegen sich selbst:

$I_\mathrm{C}$ steigt $\to$ Spannung an $R_\mathrm{E}$ steigt $\to$ $\varphi_\mathrm{E}$ steigt $\to$ $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$ sinkt $\to$ weniger Injektion $\to$ $I_\mathrm{C}$ sinkt.

Die Wirkung schwächt ihre Ursache: Das ist Gegenkopplung, hier __Stromgegenkopplung__, weil der Strom durch $R_\mathrm{E}$ die Gegenspannung erzeugt. Am Ende ändert sich $U_\mathrm{BE}$ nur um Millivolt, und der Strom folgt aus dem ohmschen Gesetz an $R_\mathrm{E}$ statt aus der e-Funktion. Die zweite Form verbindet $R_\mathrm{B}$ mit dem Kollektor (Abb. [8](#abb-8), Mitte). Steigt $I_\mathrm{C}$, sinkt $U_\mathrm{CE}$, und mit ihr sinkt $I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$. Das ist die __Spannungsgegenkopplung__.

:::abbildung et1/k10gegenkopplung 8
Links Stromgegenkopplung mit Basisteiler, in der Mitte Spannungsgegenkopplung. Rechts $I_\mathrm{C}$ über $B$ im Rechenmodell. Ohne Gegenkopplung wächst der Strom proportional zu $B$ bis zur Sättigung (grau). Die Stromgegenkopplung (blau) bleibt fast flach, die Spannungsgegenkopplung (orange) liegt dazwischen.
:::

:::satz Satz 7.1 (Arbeitspunkt mit Gegenkopplung)
<span class="anker" id="satz-7-1"></span>

Stromgegenkopplung mit dem Teiler $R_1$, $R_2$ und $R_\mathrm{i}=R_1\parallel R_2$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2},\quad I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}},\quad I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}. \tag{7.1}$$

Für $R_\mathrm{E}\gg R_\mathrm{i}/B$ und $B\gg1$ ist $I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$, für zusätzlich $U_\mathrm{q}\gg U_\mathrm{BE}$ ist $I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$.

Spannungsgegenkopplung mit $R_\mathrm{B}$ vom Kollektor zur Basis:

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}},\qquad\text{für } R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}:\ I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}. \tag{7.2}$$
:::

⁠**So liest man das:** $U_\mathrm{q}$ und $R_\mathrm{i}$ beschreiben den Teiler als Ersatzspannungsquelle ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)): $U_\mathrm{q}$ ist seine Leerlaufspannung, $R_\mathrm{i}$ sein Innenwiderstand. $R_\mathrm{E}$ wirkt im Nenner fast voll, $R_\mathrm{i}$ nur durch $B$ geteilt. **Gültigkeit:** aktiver Bereich. Das ist am Ende zu prüfen. $U_\mathrm{BE}$ ist hier ein fester Wert, die letzte Näherung in [(7.1)](#gl-7-1) braucht große $U_\mathrm{q}$.

:::herleitung Die Formeln aus den Maschen
Der Teiler wird zur Quelle $U_\mathrm{q}$ mit $R_\mathrm{i}$ in Reihe. Die Masche über Basis und Emitter lautet mit $I_\mathrm{E}=(1+B)I_\mathrm{B}$

$$U_\mathrm{q}=I_\mathrm{B}R_\mathrm{i}+U_\mathrm{BE}+I_\mathrm{B}(1+B)R_\mathrm{E}.$$

Auflösen nach $I_\mathrm{B}$ und Multiplizieren mit $B$ ergibt [(7.1)](#gl-7-1). Bei der Spannungsgegenkopplung fließt durch $R_\mathrm{C}$ der Strom $I_\mathrm{C}+I_\mathrm{B}$, durch $R_\mathrm{B}$ nur $I_\mathrm{B}$. Mit $I_\mathrm{B}=I_\mathrm{C}/B$ lautet die Masche

$$U_\mathrm{CC}-U_\mathrm{BE}=\Bigl(\frac{I_\mathrm{C}}{B}+I_\mathrm{C}\Bigr)R_\mathrm{C}+\frac{I_\mathrm{C}}{B}R_\mathrm{B}.$$

Auflösen nach $I_\mathrm{C}$ ergibt [(7.2)](#gl-7-2).
:::

::::beispiel
Rechenmodell: $U_\mathrm{q}=2{,}7$ V, $R_\mathrm{i}=6{,}98$ k$\Omega$, $R_\mathrm{i}/B=35\,\Omega\ll1$ k$\Omega$. Damit ist $I_\mathrm{C}=2{,}1\,\mathrm{V}/1040\,\Omega=2{,}02$ mA und $U_\mathrm{CE}=12\,\mathrm{V}-6{,}06\,\mathrm{V}-2{,}03\,\mathrm{V}=3{,}91$ V, also aktiv. Das Basispotenzial liegt bei 2,63 V, der Teiler führt 300 µ A, das 30-Fache von $I_\mathrm{B}$.

| $I_\mathrm{C}$ bei | $B=100$ | $B=200$ | $B=400$ |
|---|---|---|---|
| ohne Gegenkopplung ($I_\mathrm{B}=10$ µ A) | 1 mA | 2 mA | 3,93 mA (Sättigung) |
| Spannungsgegenkopplung ($R_\mathrm{B}=540$ k$\Omega$) | 1,35 mA | 1,99 mA | 2,62 mA |
| Stromgegenkopplung | 1,94 mA | 2,02 mA | 2,06 mA |

Auch die Temperatur wirkt kaum noch: 50 K Erwärmung senken $U_\mathrm{BE}$ um 0,1 V, $I_\mathrm{C}$ steigt mit [(7.1)](#gl-7-1) nur um 4,8 %. Bei fester Spannung $U_\mathrm{BE}$ wäre es das 47-Fache. Die Spannungsgegenkopplung erreicht weniger, denn hier ist $R_\mathrm{B}/B=2{,}7$ k$\Omega$ nicht klein gegen 3 k$\Omega$. Mit $R_\mathrm{B}=100$ k$\Omega$ schwankt $I_\mathrm{C}$ nur noch zwischen 2,83 mA und 3,50 mA, doch dann bleiben nur $U_\mathrm{CE}=2{,}2$ V.
::::

⁠**Grenzfälle:** $R_\mathrm{E}\to0$ ergibt $I_\mathrm{C}=B(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$, die Formel mit Basiswiderstand aus Stufe [5](der-arbeitspunkt.html#stufe-5). $B\to\infty$ ergibt $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$.

:::frage Was kostet der Emitterwiderstand?
Zweierlei. Die Spannung an $R_\mathrm{E}$, hier 2 V, fehlt dem Kollektor für die Aussteuerung. Und die Gegenkopplung wirkt auch auf das Signal: Die Spannungsverstärkung sinkt stark (Stufe [10](drei-grundschaltungen.html#stufe-10)). Ein Kondensator parallel zu $R_\mathrm{E}$ wirkt für Wechselsignale wie ein Draht und nimmt den zweiten Nachteil weg.
:::

:::ltspice $I_\mathrm{C}$ ist fast unabhängig von $B$
⁠**Zeichnen:** `voltage` `VCC` mit 12 am Netz `cc`. Teiler `res` 31k von `cc` nach `b`, 9k von `b` nach Masse. `npn` mit Modell `T`, `res` 3k von `cc` zum Kollektor, `res` 1k vom Emitter nach Masse.

⁠**Direktiven:** `.model T NPN(IS=1.55e-13 BF={BF} VAF=74)`, `.param BF=186`, `.step param BF list 93 186 372`, `.dc VCC 0 12 0.1`, `.meas dc ic FIND Ic(Q1) AT=12`. Die drei Werte entsprechen $B=100$, 200, 400 bei 6 V.

⁠**Was du siehst:** Drei fast deckungsgleiche Kurven. Bei 12 V liefert LTspice 1,94 mA; 2,02 mA; 2,06 mA, genau wie die Rechnung. Trage die Werte aus Aufgabe [8](#aufg-8) ein und prüfe deine Streuung.
:::

:::aufgabe Aufgabe 8 ★★★ Arbeitspunkt entwerfen
<span class="anker" id="aufg-8"></span>

Entwirf mit T eine Stromgegenkopplung für $U_\mathrm{CC}=15$ V, $I_\mathrm{C}=1$ mA, 2 V an $R_\mathrm{E}$ und $U_\mathrm{CE}=6$ V. (a) Bestimme $R_\mathrm{E}$ und $R_\mathrm{C}$ auf runde Werte. (b) Durch $R_2$ sollen $10\,I_\mathrm{B}$ fließen. Bestimme $R_2$ und $R_1$ (runde auf 52 k$\Omega$ und 225 k$\Omega$). (c) Berechne $I_\mathrm{C}$ für $B=100$, 200, 400 und vergleiche mit der Schaltung aus der Tabelle. Warum ist die Streuung größer? Sage das Ergebnis vorher, bevor du rechnest.

:::loesung
(a) $R_\mathrm{E}=2\,\mathrm{V}/1\,\mathrm{mA}=2$ k$\Omega$, $R_\mathrm{C}=(15-6-2)\,\mathrm{V}/1\,\mathrm{mA}=7$ k$\Omega$.

(b) $I_\mathrm{B}=5$ µ A, Basispotenzial 2,6 V. $R_2=2{,}6\,\mathrm{V}/50\,\mu\text{A}=52$ k$\Omega$. Durch $R_1$ fließen 55 µ A: $R_1=12{,}4\,\mathrm{V}/55\,\mu\text{A}=225$ k$\Omega$.

(c) $U_\mathrm{q}=2{,}82$ V, $R_\mathrm{i}=42{,}2$ k$\Omega$. Mit [(7.1)](#gl-7-1) sind $I_\mathrm{C}=0{,}91$ mA; 1,00 mA; 1,05 mA. Vorhersage: Die Streuung ist größer, weil $R_\mathrm{i}/B=211\,\Omega$ nicht mehr klein gegen $R_\mathrm{E}$ ist. Der Teiler führt hier nur das Zehnfache von $I_\mathrm{B}$ statt das Dreißigfache. LTspice: 0,92 mA; 1,01 mA; 1,06 mA.
:::
:::

:::aufgabe Aufgabe 9 ★★ Spannungsgegenkopplung
<span class="anker" id="aufg-9"></span>

Nimm die Spannungsgegenkopplung aus dem Beispiel. (a) Prüfe $I_\mathrm{C}$ und $U_\mathrm{CE}$ für $B=200$. (b) Grenzfall $R_\mathrm{B}\to0$: Welche Werte haben $U_\mathrm{CE}$ und $I_\mathrm{C}$? Ist der Transistor dann aktiv? Antworte mit [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) und der Bedeutung von $U_\mathrm{CB}$.

:::loesung
(a) $I_\mathrm{C}=11{,}4\,\mathrm{V}/(3015\,\Omega+2700\,\Omega)=1{,}99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3\,\text{k}\Omega\cdot2{,}005\,\mathrm{mA}=5{,}99$ V.

(b) Basis und Kollektor sind verbunden: $U_\mathrm{CE}=U_\mathrm{BE}=0{,}6$ V und $I_\mathrm{C}=11{,}4\,\mathrm{V}/3015\,\Omega=3{,}78$ mA. Wegen $U_\mathrm{CE}>0{,}2$ V ist der Transistor aktiv, genau auf der Linie $U_\mathrm{CB}=0$. Das ist T1 im Stromspiegel.
:::
:::

::::formelsammlung
**Basisteiler als Ersatzspannungsquelle**

$$U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2},\qquad R_\mathrm{i}=R_1\parallel R_2$$

Leerlaufspannung $U_\mathrm{q}$ und Innenwiderstand $R_\mathrm{i}$ des Teilers $R_1$, $R_2$ an der Basis.

**Stromgegenkopplung**

$$I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}},\qquad I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}$$

Aktiver Bereich (am Ende prüfen), $U_\mathrm{BE}$ als fester Wert. $R_\mathrm{E}$ wirkt im Nenner fast voll, $R_\mathrm{i}$ nur durch $B$ geteilt. Grenzfälle: $R_\mathrm{E}\to0$ ergibt $I_\mathrm{C}=B(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$, $B\to\infty$ ergibt $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$.

**Näherungen der Stromgegenkopplung**

$$I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E},\qquad I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$$

Die erste gilt für $R_\mathrm{E}\gg R_\mathrm{i}/B$ und $B\gg1$, die zweite zusätzlich für $U_\mathrm{q}\gg U_\mathrm{BE}$.

**Spannungsgegenkopplung**

$$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}}$$

$R_\mathrm{B}$ vom Kollektor zur Basis, aktiver Bereich; der Basisstrom ist $I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$. Für $R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}$ gilt $I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}$.
::::

::::lernkarten
:::karte zusammenhang Unzuverlässiger Arbeitspunkt
Warum ist ein Arbeitspunkt mit festem Basisstrom oder mit fester Spannung $U_\mathrm{BE}$ unzuverlässig?
---
Bei festem $I_\mathrm{B}$ ist $I_\mathrm{C}=B\,I_\mathrm{B}$, und $B$ streut: $B=100$ gibt 1 mA, $B=400$ Sättigung. Bei fester $U_\mathrm{BE}$ wirkt die Temperatur: $U_\mathrm{BE}$ sinkt bei festem Strom um rund 2 mV je Kelvin, und schon 9 K verdoppeln $I_\mathrm{C}$.
--- falsch
Bei festem $I_\mathrm{B}$ altert der Basiswiderstand und ändert den Strom um den Faktor 2. Bei fester $U_\mathrm{BE}$ ist der Strom dagegen völlig stabil, weil die e-Funktion überhaupt nicht von der Temperatur abhängt.
--- falsch
Bei festem $I_\mathrm{B}$ hängt $I_\mathrm{C}$ stark von $U_\mathrm{CE}$ ab, rund 50 % je Volt. Bei fester $U_\mathrm{BE}$ steigt $U_\mathrm{BE}$ mit der Temperatur um 2 mV je Kelvin, und $I_\mathrm{C}$ fällt.
--- falsch
Beide sind zuverlässig, solange der Transistor gesperrt bleibt. Erst im aktiven Bereich streut $B$, und $I_\mathrm{C}$ springt dann zwischen 1 mA und 4 mA hin und her.
:::
:::karte zusammenhang Gegenkopplung
Wie hält ein Emitterwiderstand den Kollektorstrom durch Gegenkopplung fest, wenn $I_\mathrm{C}$ zu steigen beginnt?
---
Steigt $I_\mathrm{C}$, steigt die Spannung an $R_\mathrm{E}$ und mit ihr $\varphi_\mathrm{E}$. Bei festem Basispotenzial sinkt $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, die Injektion nimmt ab, und $I_\mathrm{C}$ sinkt wieder: Die Wirkung schwächt ihre Ursache.
--- falsch
Steigt $I_\mathrm{C}$, sinkt die Spannung an $R_\mathrm{E}$ und mit ihr $\varphi_\mathrm{E}$. Dadurch wächst $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, die Injektion nimmt zu, und der Strom pendelt sich auf einem höheren Wert ein.
--- falsch
Steigt $I_\mathrm{C}$, erwärmt sich $R_\mathrm{E}$ und vergrößert dadurch seinen Widerstand. Der größere Widerstand begrenzt den Strom wie eine Sicherung, ohne dass sich $U_\mathrm{BE}$ oder das Emitterpotenzial dabei ändern.
--- falsch
Steigt $I_\mathrm{C}$, hebt die Spannung an $R_\mathrm{E}$ das Basispotenzial $\varphi_\mathrm{B}$ mit an. $U_\mathrm{BE}$ bleibt deshalb gleich, und $R_\mathrm{E}$ begrenzt den Strom nur über das ohmsche Gesetz.
:::
:::karte begriff Stromgegenkopplung
Was versteht man unter Stromgegenkopplung in einer Transistorschaltung?
---
Gegenkopplung durch einen Widerstand $R_\mathrm{E}$ im Emitter: Der Strom durch $R_\mathrm{E}$ erzeugt die Gegenspannung, die $U_\mathrm{BE}$ zurücknimmt. Ein Teiler hält dabei das Basispotenzial nahezu fest.
--- falsch
Gegenkopplung durch einen Widerstand vom Kollektor zur Basis: Der Kollektorstrom fließt zurück in die Basis und verkleinert dort den Basisstrom. Ein Teiler ist dafür nicht nötig.
--- falsch
Gegenkopplung durch eine Stromquelle im Emitter, die den Emitterstrom auf einen festen Wert zwingt. Der Transistor arbeitet dann unabhängig von $U_\mathrm{BE}$ und vom Basispotenzial.
--- falsch
Gegenkopplung durch einen Widerstand $R_\mathrm{E}$ im Emitter, der den Basisstrom auf einen festen Wert begrenzt. Das Basispotenzial folgt dabei dem Emitter, damit $U_\mathrm{BE}$ konstant bleibt.
:::
:::karte begriff Spannungsgegenkopplung
Wie wirkt die Spannungsgegenkopplung mit $R_\mathrm{B}$ vom Kollektor zur Basis?
---
Gegenkopplung, bei der $R_\mathrm{B}$ den Basisstrom aus der Kollektorspannung bezieht: Steigt $I_\mathrm{C}$, sinkt $U_\mathrm{CE}$, und mit ihr sinkt $I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$.
--- falsch
Gegenkopplung, bei der $R_\mathrm{B}$ die Versorgung mit der Basis verbindet: Steigt $I_\mathrm{C}$, steigt $U_\mathrm{CE}$, und mit ihr wächst der Basisstrom, der den Arbeitspunkt nachführt.
--- falsch
Gegenkopplung, bei der ein Emitterwiderstand eine Spannung erzeugt: Steigt $I_\mathrm{C}$, steigt die Spannung am Emitter, und $U_\mathrm{BE}$ sinkt, bei festem Basispotenzial.
--- falsch
Gegenkopplung, bei der $R_\mathrm{B}$ den Basisstrom aus der Eingangsspannung bezieht: Er hängt nur von $U_\mathrm{ein}$ ab, und $U_\mathrm{CE}$ wirkt auf ihn nicht zurück.
:::
:::karte formel Kollektorstrom mit Stromgegenkopplung
Wie groß ist $I_\mathrm{C}$ bei Stromgegenkopplung mit dem Teiler $R_1$, $R_2$ und dem Emitterwiderstand $R_\mathrm{E}$?
---
$I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}$ mit $U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2}$ und $R_\mathrm{i}=R_1\parallel R_2$. Gültig im aktiven Bereich, mit festem $U_\mathrm{BE}$.
--- falsch
$I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{i}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{E}}{B}}$ mit $U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2}$ und $R_\mathrm{i}=R_1\parallel R_2$. Gültig im aktiven Bereich, mit festem $U_\mathrm{BE}$.
--- falsch
$I_\mathrm{C}=B\,\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{i}}$ mit $U_\mathrm{q}=U_\mathrm{CC}\frac{R_1}{R_1+R_2}$ und $R_\mathrm{i}=R_1+R_2$. Gültig im aktiven Bereich; $R_\mathrm{E}$ spielt für den Gleichstrom keine Rolle.
--- falsch
$I_\mathrm{C}=\frac{U_\mathrm{q}+U_\mathrm{BE}}{R_\mathrm{E}(1+B)+R_\mathrm{i}\,B}$ mit $U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2}$ und $R_\mathrm{i}=R_1\parallel R_2$. Gültig in jedem Bereich, auch in der Sättigung.
:::
:::karte formel Näherungen bei Stromgegenkopplung
Welche Näherungen gelten für $I_\mathrm{C}$ bei Stromgegenkopplung, wenn $R_\mathrm{E}\gg R_\mathrm{i}/B$ und $B\gg1$ sind?
---
$I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$; ist zusätzlich $U_\mathrm{q}\gg U_\mathrm{BE}$, gilt $I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$. Der Strom folgt dann aus dem ohmschen Gesetz an $R_\mathrm{E}$.
--- falsch
$I_\mathrm{C}\approx B\,(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$; ist zusätzlich $U_\mathrm{q}\gg U_\mathrm{BE}$, gilt $I_\mathrm{C}\approx B\,U_\mathrm{q}/R_\mathrm{i}$. Der Strom folgt dann aus dem Basisstrom durch den Teiler.
--- falsch
$I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$; ist zusätzlich $U_\mathrm{q}\gg U_\mathrm{BE}$, gilt $I_\mathrm{C}\approx U_\mathrm{CC}/R_\mathrm{E}$. Der Teiler spielt dann keine Rolle mehr, nur die Versorgung.
--- falsch
$I_\mathrm{C}\approx U_\mathrm{CC}/(R_\mathrm{C}+R_\mathrm{E})$; der Strom hängt dann nur von der Versorgung und den beiden Widerständen im Ausgangskreis ab, nicht vom Teiler an der Basis.
:::
:::karte formel Kollektorstrom mit Spannungsgegenkopplung
Wie groß ist $I_\mathrm{C}$ bei Spannungsgegenkopplung mit $R_\mathrm{B}$ vom Kollektor zur Basis?
---
$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}}$; für $R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}$ ist $I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}$. Gültig im aktiven Bereich.
--- falsch
$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{B}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{C}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{B}}$; für $R_\mathrm{B}\gg R_\mathrm{C}$ hängt $I_\mathrm{C}$ nur vom Basiswiderstand ab. Gültig im aktiven Bereich.
--- falsch
$I_\mathrm{C}=B\,\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{B}}$, wie ohne Gegenkopplung, weil $R_\mathrm{B}$ den Basisstrom aus der Versorgung bezieht; der Kollektorwiderstand geht nicht ein. Gültig im aktiven Bereich.
--- falsch
$I_\mathrm{C}=\frac{U_\mathrm{CC}+U_\mathrm{BE}}{R_\mathrm{C}+B\,R_\mathrm{B}}$; für großes $B$ wird $I_\mathrm{C}$ deshalb sehr klein, und die Schaltung sperrt. Gültig in jedem Bereich, auch in der Sättigung.
:::
:::karte herleitung Stromgegenkopplung aus der Masche
Wie folgt aus der Masche über Basis und Emitter die Formel für $I_\mathrm{C}$ bei Stromgegenkopplung?
---
Man ersetzt den Teiler durch die Quelle $U_\mathrm{q}$ mit $R_\mathrm{i}$ in Reihe, weil er sich nach außen wie eine Ersatzspannungsquelle mit Leerlaufspannung $U_\mathrm{q}$ und Innenwiderstand $R_\mathrm{i}$ verhält.
---
Durch $R_\mathrm{E}$ fließt $I_\mathrm{E}=(1+B)I_\mathrm{B}$, weil sich Basis- und Kollektorstrom im Emitter vereinigen.
---
Die Masche lautet $U_\mathrm{q}=I_\mathrm{B}R_\mathrm{i}+U_\mathrm{BE}+I_\mathrm{B}(1+B)R_\mathrm{E}$, weil die Spannungen an $R_\mathrm{i}$, an der BE-Strecke und an $R_\mathrm{E}$ zusammen $U_\mathrm{q}$ ergeben.
---
Auflösen ergibt $I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}}$, weil $I_\mathrm{B}$ in beiden Widerstandsgliedern als Faktor steht.
---
Multiplizieren mit $B$ ergibt $I_\mathrm{C}$, weil im aktiven Bereich $I_\mathrm{C}=B\,I_\mathrm{B}$ gilt.
:::
:::karte herleitung Spannungsgegenkopplung aus der Masche
Wie folgt aus der Masche über $R_\mathrm{C}$, $R_\mathrm{B}$ und die BE-Strecke die Formel für $I_\mathrm{C}$ bei Spannungsgegenkopplung?
---
Durch $R_\mathrm{C}$ fließt $I_\mathrm{C}+I_\mathrm{B}$, durch $R_\mathrm{B}$ nur $I_\mathrm{B}$, weil sich der Strom durch $R_\mathrm{C}$ am Kollektor in Kollektor- und Basisstrom teilt.
---
Mit $I_\mathrm{B}=I_\mathrm{C}/B$ lautet die Masche $U_\mathrm{CC}-U_\mathrm{BE}=\Bigl(\frac{I_\mathrm{C}}{B}+I_\mathrm{C}\Bigr)R_\mathrm{C}+\frac{I_\mathrm{C}}{B}R_\mathrm{B}$, weil der Weg von $U_\mathrm{CC}$ über $R_\mathrm{C}$, $R_\mathrm{B}$ und die BE-Strecke zur Masse führt.
---
Auflösen nach $I_\mathrm{C}$ ergibt $I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}$, weil $I_\mathrm{C}$ auf der rechten Seite in jedem Glied als Faktor steht.
:::
:::karte zusammenhang Teiler und Emitterwiderstand im Nenner
Warum bleibt $I_\mathrm{C}$ bei Stromgegenkopplung fast unabhängig von $B$?
---
Im Nenner wirkt $R_\mathrm{E}$ fast voll, $R_\mathrm{i}$ nur durch $B$ geteilt. Ist $R_\mathrm{i}/B$ klein gegen $R_\mathrm{E}$, hängt $I_\mathrm{C}$ kaum noch von $B$ ab: Im Rechenmodell 1,94 mA bis 2,06 mA für $B=100$ bis 400.
--- falsch
Im Nenner wirkt $R_\mathrm{i}$ fast voll, $R_\mathrm{E}$ nur durch $B$ geteilt. Ist $R_\mathrm{i}$ groß, hängt $I_\mathrm{C}$ kaum noch von $B$ ab: Im Rechenmodell 1 mA bis 3,93 mA für $B=100$ bis 400.
--- falsch
$B$ kommt in der Formel gar nicht vor, weil der Teiler den Basisstrom fest vorgibt und $R_\mathrm{E}$ ihn nicht beeinflusst. Der Strom ist deshalb im Rechenmodell für jedes $B$ genau 2,02 mA.
--- falsch
Der Emitterwiderstand misst $B$ und stellt den Teiler passend nach. Im Rechenmodell bleibt $I_\mathrm{C}$ deshalb exakt 2 mA, solange $B$ zwischen 100 und 400 liegt.
:::
:::karte zusammenhang Schwächere Spannungsgegenkopplung
Warum stabilisiert die Spannungsgegenkopplung im Rechenmodell den Strom schlechter als die Stromgegenkopplung?
---
Hier ist $R_\mathrm{B}/B=2{,}7$ k$\Omega$ nicht klein gegen $R_\mathrm{C}=3$ k$\Omega$, also bestimmt $B$ den Nenner mit. Ein kleineres $R_\mathrm{B}$ hilft, lässt aber nur noch wenig $U_\mathrm{CE}$ übrig.
--- falsch
Hier fließt der Basisstrom über $R_\mathrm{C}$ und erwärmt den Kollektorwiderstand, der dadurch seinen Wert ändert. Ein größeres $R_\mathrm{B}$ würde das beheben, ohne $U_\mathrm{CE}$ zu ändern.
--- falsch
Hier ist $R_\mathrm{B}/B=2{,}7$ k$\Omega$ viel größer als $R_\mathrm{C}=3$ k$\Omega$, also hängt $I_\mathrm{C}$ nur von $R_\mathrm{B}$ ab. Ein größeres $R_\mathrm{B}$ macht den Strom deshalb stabiler.
--- falsch
Hier wirkt die Gegenkopplung nur auf die Temperatur, nicht auf $B$. Gegen Streuung von $B$ hilft nur ein Emitterwiderstand, ein anderer Wert von $R_\mathrm{B}$ ändert daran nichts.
:::
:::karte zusammenhang Erwärmung bei Stromgegenkopplung
Was passiert mit $I_\mathrm{C}$ im Rechenmodell mit Stromgegenkopplung, wenn sich der Transistor um 50 K erwärmt?
---
$U_\mathrm{BE}$ sinkt um 0,1 V, doch $I_\mathrm{C}$ steigt nur um 4,8 %, weil sich in der Formel nur der Zähler $U_\mathrm{q}-U_\mathrm{BE}$ wenig ändert. Bei fester Spannung $U_\mathrm{BE}$ stiege $I_\mathrm{C}$ auf das 47-Fache.
--- falsch
$U_\mathrm{BE}$ steigt um 0,1 V, deshalb sinkt $I_\mathrm{C}$ um rund 5 %. Ohne Emitterwiderstand wäre es ebenso, denn $U_\mathrm{BE}$ wirkt in beiden Schaltungen auf genau dieselbe Weise auf den Strom.
--- falsch
$U_\mathrm{BE}$ sinkt um 0,1 V, und $I_\mathrm{C}$ steigt auf das 47-Fache, weil die e-Funktion auch mit Emitterwiderstand voll wirkt. Erst ein zweiter Teiler könnte das abfangen.
--- falsch
$U_\mathrm{BE}$ bleibt gleich, weil die Gegenkopplung jede Änderung sofort ausgleicht. $I_\mathrm{C}$ ändert sich deshalb überhaupt nicht, auch nicht um Bruchteile eines Prozents.
:::
:::karte zusammenhang Preis des Emitterwiderstands
Was kostet der Emitterwiderstand in einer Schaltung mit Stromgegenkopplung, und wie nimmt man einen der Nachteile wieder weg?
---
Die Spannung an $R_\mathrm{E}$ fehlt dem Kollektor für die Aussteuerung, und die Spannungsverstärkung sinkt stark. Ein Kondensator parallel zu $R_\mathrm{E}$ wirkt für Wechselsignale wie ein Draht und nimmt den zweiten Nachteil weg.
--- falsch
Er verdoppelt den Basisstrom, und der Teiler muss entsprechend mehr liefern. Ein Kondensator in Reihe mit $R_\mathrm{E}$ sperrt den Gleichstrom und nimmt diesen Nachteil weg.
--- falsch
Er verbraucht die halbe Versorgungsleistung, und der Transistor wird dadurch heißer. Ein zweiter Widerstand parallel zu $R_\mathrm{E}$ halbiert diesen Verlust, ohne die Gegenkopplung für den Arbeitspunkt zu schwächen.
--- falsch
Er macht den Arbeitspunkt wieder von $B$ abhängig, weil $R_\mathrm{E}$ im Nenner durch $B$ geteilt wird. Ein Kondensator parallel zum Teiler gleicht diesen Nachteil wieder aus.
:::
::::
