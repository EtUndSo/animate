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
