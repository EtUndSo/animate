---
title: Mehrfachintegrale und der Satz von Fubini
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020300
summary: Von Grund auf – wie man eine Funktion über einen Quader im $\mathbb{R}^n$ integriert, indem man nacheinander über jede Variable integriert (iteriertes Integral). Der Satz von Fubini sichert, dass die Reihenfolge der Integrationen egal ist – und eine kluge Wahl der Reihenfolge kann die Rechnung drastisch vereinfachen. Mit den Grundeigenschaften (Linearität, Monotonie, Abschätzung) und dem Integral über $\mathbb{R}^n$ für Funktionen mit kompaktem Träger.
tags: Mehrfachintegral, iteriertes Integral, Satz von Fubini, Volumenintegral, Reihenfolge der Integration, kompakter Träger, Monotonie
---

:::grafik
Einstiegs-Animation: Über einem Rechteck $[a,b]\times[c,d]$ wölbt sich eine Fläche $z=f(x,y)$; gesucht ist das
**Volumen** darunter. Zwei Wege werden gezeigt: (1) Man schneidet in $x$-Richtung dünne Scheiben, bestimmt die
Fläche jeder Scheibe $\int_a^b f(x,y)\,dx$ und stapelt sie über $y$. (2) Man schneidet in $y$-Richtung und stapelt
über $x$. Beide Stapel ergeben **dasselbe** Volumen — das ist der Satz von Fubini. Ein Umschalter „Reihenfolge
$dx\,dy \leftrightarrow dy\,dx$" zeigt, dass eine Richtung manchmal viel leichter zu rechnen ist. Kernbotschaft:
Mehrfachintegrale löst man als geschachtelte 1D-Integrale, und die Reihenfolge ist frei wählbar.
:::

:::konzept
Bisher hatten wir ein Integral mit einem Parameter. Jetzt integrieren wir **über mehrere Variablen** — über einen
Quader im $\mathbb{R}^n$. Die naheliegende Idee: nacheinander nach jeder Variablen integrieren, also ein
geschachteltes („iteriertes") Integral bilden. Zwei Fragen sind sofort zu klären: Ist das wohldefiniert, und
hängt das Ergebnis von der **Reihenfolge** der Integrationen ab? Die Antwort gibt der __Satz von Fubini__: Für
stetige Funktionen darf man die Reihenfolge beliebig vertauschen. Das ist nicht nur theoretisch beruhigend,
sondern praktisch Gold wert — oft ist die eine Reihenfolge mühsam, die andere geschenkt.
:::

**Worum es geht:** Wir definieren das __Mehrfachintegral__ über einen Quader als iteriertes Integral, beweisen den
__Satz von Fubini__ (Vertauschbarkeit der Reihenfolge), nutzen ihn zum Rechnen, sammeln die Grundeigenschaften und
erweitern das Integral auf $\mathbb{R}^n$ (kompakter Träger).

## Das iterierte Integral über einen Quader

Sei $Q = [a_1,b_1]\times\cdots\times[a_n,b_n]$ ein $n$-dimensionaler Quader und $f:Q\to\mathbb{R}$ stetig. Die
naheliegende Integrationsvorschrift ist, **sukzessive** nach allen Variablen zu integrieren:

$$\int_{a_n}^{b_n}\!\!\left(\cdots\int_{a_2}^{b_2}\!\left(\int_{a_1}^{b_1} f(x_1,\ldots,x_n)\,dx_1\right)dx_2\cdots\right)dx_n.$$

Dass das wohldefiniert ist, folgt induktiv aus dem vorigen Artikel: Im 2D-Fall $f:[a,b]\times[c,d]\to\mathbb{R}$ ist
$F(y)=\int_a^b f(x,y)\,dx$ nach dem Parameterintegral-Satz **stetig** in $y$, also existiert $\int_c^d F(y)\,dy$.
Schritt für Schritt überträgt sich das auf beliebige Dimension.

## Der Satz von Fubini

Jetzt die entscheidende Frage: Darf man die Reihenfolge der Integrationen vertauschen? Für stetige Funktionen
lautet die Antwort **ja** — das ist der __Satz von Fubini__ (elementare Version). Für stetiges
$f:[a,b]\times[c,d]\to\mathbb{R}$ gilt

$$\int_c^d\!\left(\int_a^b f(x,y)\,dx\right)dy = \int_a^b\!\left(\int_c^d f(x,y)\,dy\right)dx,$$

und Entsprechendes in beliebigen Dimensionen.

**Beweisidee.** Man betrachtet die „bis zu variablen Grenzen" aufintegrierte Differenz der beiden Reihenfolgen,

$$h(\xi,\eta) := \int_a^\xi\!\left(\int_c^\eta f(x,y)\,dy\right)dx - \int_c^\eta\!\left(\int_a^\xi f(x,y)\,dx\right)dy.$$

Mit dem Hauptsatz der Differential- und Integralrechnung und der Leibnizregel (voriger Artikel) rechnet man nach,
dass $\frac{\partial h}{\partial\xi}=\frac{\partial h}{\partial\eta}=0$ — also ist $h$ **konstant**. Da
$h(a,c)=0$, ist $h\equiv 0$, und das ist genau die behauptete Gleichheit (für $\xi=b,\eta=d$). $\square$

Anschaulich ist Fubini das **Cavalieri-Prinzip** fürs Rechnen: Das Volumen unter $f$ ist dasselbe, egal ob man es
aus Scheiben in $x$- oder in $y$-Richtung aufbaut.

:::grafik
Das Volumen unter $z=f(x,y)$ über $[a,b]\times[c,d]$, einmal aus $x$-Scheiben (Flächen $\int_a^b f\,dx$, über $y$
gestapelt), einmal aus $y$-Scheiben, mit großem Gleichheitszeichen dazwischen. Darunter die Hilfsfunktion-Idee:
$\partial_\xi h=\partial_\eta h=0\Rightarrow h\equiv0$.
:::

**Stolperstein:** Für **stetige** Funktionen auf einem **endlichen** Quader ist die Vertauschung immer erlaubt.
Bei uneigentlichen Mehrfachintegralen (unendliches Gebiet oder Singularität) gilt Fubini nur unter zusätzlicher
**absoluter** Integrierbarkeit — sonst können die beiden Reihenfolgen verschiedene Werte liefern.

## Die Reihenfolge klug wählen

Weil die Reihenfolge frei ist, wählt man die **leichtere**. Betrachte

$$\iint_{[0,1]^2} y\,e^{xy}\,dx\,dy.$$

Integriert man **zuerst nach $x$** (mit $y$ als Konstante), ist $\int_0^1 y\,e^{xy}\,dx = \big[e^{xy}\big]_{x=0}^{1}
= e^{y}-1$, und dann

$$\int_0^1 \big(e^{y}-1\big)\,dy = (e-1) - 1 = e-2.$$

Die andere Reihenfolge (zuerst nach $y$) führt dagegen auf $\int_0^1 y\,e^{xy}\,dy$, das partielle Integration
erfordert — viel umständlicher für dasselbe Ergebnis. **Merke:** Erst die Variable integrieren, bei der der
Integrand am einfachsten eine Stammfunktion hat.

## Eigenschaften und das Volumenintegral

Das Mehrfachintegral über $Q$ schreibt man kurz $\int_Q f(x)\,dx$ (auch $\int_Q f\,d^n x$ oder, im 3D-Fall der
Physik, als __Volumenintegral__ $\iiint_Q f\,dV$). Es ist **linear** und **monoton**: Für stetige $f,g$ und
$\lambda,\mu\in\mathbb{R}$ gilt

$$\int_Q (\lambda f + \mu g)\,dx = \lambda\!\int_Q f\,dx + \mu\!\int_Q g\,dx, \qquad f\le g \ \Rightarrow\ \int_Q f\,dx \le \int_Q g\,dx.$$

Daraus folgt die wichtige **Standardabschätzung** (Betrag des Integrals ≤ Volumen mal Maximum):

$$\left|\int_Q f(x)\,dx\right| \le |Q|\cdot\sup_{x\in Q}|f(x)|, \qquad |Q| = (b_1-a_1)\cdots(b_n-a_n).$$

Dabei ist $|Q|$ das **Volumen** des Quaders. Diese Abschätzung ist das mehrdimensionale Gegenstück zur bekannten
1D-Regel „Integral ≤ Intervalllänge × Maximum" und taucht in Beweisen ständig auf.

## Integration über den ganzen $\mathbb{R}^n$: kompakter Träger

Um über unbeschränkte Gebiete zu integrieren, beginnt man mit einem einfachen, sauberen Fall. Eine stetige
Funktion $f:\mathbb{R}^n\to\mathbb{R}$ hat __kompakten Träger__, wenn sie außerhalb einer Kugel verschwindet: Es
gibt ein $R>0$ mit $f(x)=0$ für alle $|x|>R$. Dann setzt man

$$\int_{\mathbb{R}^n} f(x)\,dx := \int_Q f(x)\,dx$$

für einen beliebigen Quader $Q$, außerhalb dessen $f=0$ ist — der Wert hängt nicht von der Wahl von $Q$ ab, da
dort ohnehin nichts beiträgt. Für allgemeinere Funktionen (ohne kompakten Träger) erweitert man diesen Begriff als
Grenzwert; der angemessene Rahmen dafür ist das **Lebesgue-Integral**, das über diesen Kurs hinausgeht.

:::grafik
Eine „Buckel"-Funktion mit kompaktem Träger (außerhalb eines Radius $R$ überall null), eingebettet in einen Quader
$Q$; Beschriftung „$\int_{\mathbb{R}^n}f=\int_Q f$, $Q$ beliebig solange $f=0$ außerhalb". Daneben die
Standardabschätzung $|\int_Q f|\le|Q|\sup|f|$ als schraffierter Quader der Höhe $\sup|f|$.
:::

:::kern
Das __Mehrfachintegral__ über einen Quader $Q=[a_1,b_1]\times\cdots\times[a_n,b_n]$ ist das **iterierte** Integral
(nacheinander nach jeder Variablen); es ist wohldefiniert, weil jedes innere Integral eine stetige Funktion der
übrigen Variablen liefert. Der __Satz von Fubini__ sichert für stetige $f$ die **Vertauschbarkeit der
Reihenfolge**: $\int_c^d\!\int_a^b f\,dx\,dy=\int_a^b\!\int_c^d f\,dy\,dx$ (Beweis: Hilfsfunktion $h$ mit
$\partial_\xi h=\partial_\eta h=0$). Eine kluge Reihenfolge vereinfacht die Rechnung oft stark (Beispiel
$\iint_{[0,1]^2} y e^{xy}=e-2$, zuerst nach $x$). Das Integral ist **linear** und **monoton** mit der
__Standardabschätzung__ $|\int_Q f|\le|Q|\sup_Q|f|$ ($|Q|$=Quadervolumen). Für $f$ mit __kompaktem Träger__ ist
$\int_{\mathbb{R}^n}f:=\int_Q f$ ($Q$ groß genug); allgemeiner → Lebesgue-Integral. **Vorsicht:** Fubini braucht
im uneigentlichen Fall absolute Integrierbarkeit.
:::

Bisher integrierten wir über **Quader**. Reale Gebiete sind aber selten rechteckig — Kreise, Kugeln, Dreiecke. Wie
man über solche **allgemeinen Mengen** integriert und daraus **Volumina** berechnet (Cavalieri-Prinzip), ist das
Thema des nächsten Artikels.
