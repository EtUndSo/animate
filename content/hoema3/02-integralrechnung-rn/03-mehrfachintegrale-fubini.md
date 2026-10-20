---
title: Mehrfachintegrale und der Satz von Fubini
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020300
summary: Von Grund auf – wie man eine Funktion über einen Quader im $\mathbb{R}^n$ integriert, indem man nacheinander über jede Variable integriert (iteriertes Integral). Der Satz von Fubini sichert, dass die Reihenfolge egal ist – eine kluge Wahl vereinfacht die Rechnung stark. Mit Linearität, Monotonie, Standardabschätzung und dem Integral über $\mathbb{R}^n$ für Funktionen mit kompaktem Träger.
tags: Mehrfachintegral, iteriertes Integral, Satz von Fubini, Volumenintegral, Reihenfolge der Integration, kompakter Träger, Monotonie
---

## Anschaulich

Über einem Rechteck $[a,b]\times[c,d]$ wölbt sich eine Fläche $z=f(x,y)$. Gesucht ist das **Volumen** darunter.

Dafür gibt es zwei Wege. Man kann in $x$-Richtung dünne Scheiben schneiden, die Fläche jeder Scheibe als
$\int_a^b f(x,y)\,dx$ bestimmen und diese über $y$ aufstapeln. Oder man schneidet in $y$-Richtung und stapelt über
$x$.

Beide Stapel ergeben **dasselbe** Volumen — das ist der Kern des Satzes von Fubini. Ein Mehrfachintegral löst man
also als geschachtelte 1D-Integrale, und die **Reihenfolge** ist frei wählbar.

Das ist nicht nur beruhigend, sondern praktisch Gold wert: Oft ist die eine Reihenfolge mühsam, die andere
geschenkt.

:::grafik
Szene: hoema3/integralrechnung-rn/03-fubini-scheiben · Vorlage: volumen-scheiben-3d
Das Volumen unter $z=f(x,y)$ über $[a,b]\times[c,d]$, einmal aus $x$-Scheiben (Flächen $\int_a^b f\,dx$, über $y$
gestapelt), einmal aus $y$-Scheiben, mit großem Gleichheitszeichen dazwischen. Ein Umschalter „Reihenfolge
$dx\,dy\leftrightarrow dy\,dx$". (Rot = Fläche $f$, orange = eine Scheibe, grau = Grundrechteck.)
:::

## Das iterierte Integral über einen Quader

Sei $Q=[a_1,b_1]\times\cdots\times[a_n,b_n]$ ein $n$-dimensionaler Quader und $f:Q\to\mathbb{R}$ stetig. Die
naheliegende Vorschrift ist, **sukzessive** nach allen Variablen zu integrieren:

:::formel Definition
$$\int_{a_n}^{b_n}\!\!\left(\cdots\int_{a_2}^{b_2}\!\left(\int_{a_1}^{b_1} f(x_1,\ldots,x_n)\,dx_1\right)dx_2\cdots\right)dx_n.$$
:::

Man liest das von innen nach außen: Das innerste Integral behandelt alle Variablen außer $x_1$ als Konstanten und
liefert eine Funktion von $(x_2,\ldots,x_n)$; die nächste Integration verarbeitet diese, und so weiter.

Dass das wohldefiniert ist, folgt induktiv aus dem vorigen Artikel: Im 2D-Fall ist $F(y)=\int_a^b f(x,y)\,dx$ nach
dem Parameterintegral-Satz **stetig** in $y$, also existiert $\int_c^d F(y)\,dy$. Schritt für Schritt überträgt
sich das auf jede Dimension.

## Der Satz von Fubini

Jetzt die entscheidende Frage: Darf man die Reihenfolge der Integrationen vertauschen? Für stetige Funktionen
lautet die Antwort **ja**.

:::formel Satz
$$\int_c^d\!\left(\int_a^b f(x,y)\,dx\right)dy = \int_a^b\!\left(\int_c^d f(x,y)\,dy\right)dx \qquad (f\text{ stetig auf }[a,b]\times[c,d]).$$
:::

Entsprechendes gilt in beliebiger Dimension. Anschaulich ist das das **Cavalieri-Prinzip** fürs Rechnen: Das
Volumen unter $f$ ist dasselbe, egal ob man es aus $x$- oder aus $y$-Scheiben aufbaut.

:::herleitung
Man betrachtet die bis zu variablen Grenzen integrierte Differenz der beiden Reihenfolgen,

$$h(\xi,\eta) := \int_a^\xi\!\left(\int_c^\eta f(x,y)\,dy\right)dx - \int_c^\eta\!\left(\int_a^\xi f(x,y)\,dx\right)dy.$$

Mit dem Hauptsatz der Differential- und Integralrechnung und der Leibnizregel (voriger Artikel) rechnet man nach,
dass $\frac{\partial h}{\partial\xi}=\frac{\partial h}{\partial\eta}=0$. Also ist $h$ **konstant**. Wegen
$h(a,c)=0$ ist $h\equiv0$ — und für $\xi=b,\eta=d$ ist das genau die behauptete Gleichheit.
:::

**Stolperstein:** Für **stetige** Funktionen auf einem **endlichen** Quader ist die Vertauschung immer erlaubt.
Bei uneigentlichen Mehrfachintegralen (unendliches Gebiet oder Singularität) gilt Fubini nur unter zusätzlicher
**absoluter** Integrierbarkeit — sonst können die beiden Reihenfolgen verschiedene Werte liefern.

## Die Reihenfolge klug wählen

Weil die Reihenfolge frei ist, wählt man die **leichtere**. Betrachte

$$\iint_{[0,1]^2} y\,e^{xy}\,dx\,dy.$$

Integriert man **zuerst nach $x$** (mit $y$ als Konstante), ist die Stammfunktion sofort da:

$$\int_0^1 y\,e^{xy}\,dx = \big[e^{xy}\big]_{x=0}^{1} = e^{y}-1,$$

und dann

$$\int_0^1 \big(e^{y}-1\big)\,dy = (e-1)-1 = e-2.$$

Die andere Reihenfolge (zuerst nach $y$) führt auf $\int_0^1 y\,e^{xy}\,dy$, das partielle Integration erfordert —
viel umständlicher für dasselbe Ergebnis. **Merke:** Erst die Variable integrieren, bei der der Integrand am
einfachsten eine Stammfunktion hat.

## Eigenschaften und das Volumenintegral

Das Mehrfachintegral über $Q$ schreibt man kurz $\int_Q f(x)\,dx$ (auch $\int_Q f\,d^n x$ oder, im 3D-Fall der
Physik, als __Volumenintegral__ $\iiint_Q f\,dV$). Es ist **linear** und **monoton**:

$$\int_Q(\lambda f+\mu g)\,dx = \lambda\!\int_Q f\,dx+\mu\!\int_Q g\,dx, \qquad f\le g \ \Rightarrow\ \int_Q f\,dx\le\int_Q g\,dx.$$

Daraus folgt die wichtige __Standardabschätzung__ — Betrag des Integrals $\le$ Volumen mal Maximum:

$$\left|\int_Q f(x)\,dx\right| \le |Q|\cdot\sup_{x\in Q}|f(x)|, \qquad |Q|=(b_1-a_1)\cdots(b_n-a_n).$$

Dabei ist $|Q|$ das **Volumen** des Quaders. Das ist das mehrdimensionale Gegenstück zur 1D-Regel „Integral $\le$
Intervalllänge × Maximum" und taucht in Beweisen ständig auf.

## Integration über den ganzen $\mathbb{R}^n$: kompakter Träger

Um über ein unbeschränktes Gebiet zu integrieren, beginnt man mit einem sauberen Spezialfall. Eine stetige
Funktion $f:\mathbb{R}^n\to\mathbb{R}$ hat __kompakten Träger__, wenn sie außerhalb einer Kugel verschwindet: Es
gibt ein $R>0$ mit $f(x)=0$ für alle $|x|>R$. Dann setzt man

$$\int_{\mathbb{R}^n} f(x)\,dx := \int_Q f(x)\,dx$$

für einen beliebigen Quader $Q$, außerhalb dessen $f=0$ ist. Der Wert hängt nicht von der Wahl von $Q$ ab, weil
dort ohnehin nichts beiträgt.

Für Funktionen ohne kompakten Träger erweitert man diesen Begriff als Grenzwert; der angemessene Rahmen dafür ist
das **Lebesgue-Integral**, das über diesen Kurs hinausgeht.

:::grafik
Szene: hoema3/integralrechnung-rn/03-kompakter-traeger · Vorlage: buckel-im-quader-2d
Eine „Buckel"-Funktion mit kompaktem Träger (außerhalb eines Radius $R$ überall null), eingebettet in einen
Quader $Q$; Beschriftung „$\int_{\mathbb{R}^n}f=\int_Q f$, $Q$ beliebig solange $f=0$ außerhalb". Daneben die
Standardabschätzung als schraffierter Quader der Höhe $\sup|f|$. (Rot = $f$, grau = Quader/Schranke.)
:::

## Bedeutung und Ausblick

Mit dem iterierten Integral und Fubini kann man jedes Integral über einen Quader auf gewöhnliche 1D-Integrationen
zurückführen — und sich die bequemste Reihenfolge aussuchen. Das ist die Rechengrundlage für alle folgenden
Volumen- und Feldintegrale.

Bisher integrierten wir über **Quader**. Reale Gebiete sind aber selten rechteckig — Kreise, Kugeln, Dreiecke. Wie
man über solche **allgemeinen Mengen** integriert und daraus **Volumina** berechnet, ist das Thema des nächsten
Artikels.

:::kern
- Das __Mehrfachintegral__ über einen Quader $Q$ ist das **iterierte** Integral (nacheinander nach jeder Variablen); wohldefiniert, weil jedes innere Integral eine stetige Funktion der übrigen Variablen liefert.
- Der __Satz von Fubini__ sichert für stetige $f$ die **Vertauschbarkeit der Reihenfolge**: $\int_c^d\!\int_a^b f\,dx\,dy=\int_a^b\!\int_c^d f\,dy\,dx$ (Beweis: Hilfsfunktion $h$ mit $\partial_\xi h=\partial_\eta h=0$).
- Eine kluge Reihenfolge vereinfacht oft stark (Beispiel $\iint_{[0,1]^2} y e^{xy}=e-2$, zuerst nach $x$).
- Das Integral ist **linear** und **monoton**, mit der __Standardabschätzung__ $|\int_Q f|\le|Q|\sup_Q|f|$ ($|Q|$ = Quadervolumen).
- Für $f$ mit __kompaktem Träger__ ist $\int_{\mathbb{R}^n}f:=\int_Q f$ ($Q$ groß genug); allgemeiner → Lebesgue-Integral.
- **Vorsicht:** Fubini braucht im uneigentlichen Fall absolute Integrierbarkeit.
:::

:::quiz
F: Was ist ein iteriertes Integral, und warum ist es wohldefiniert?
A: Man integriert nacheinander nach je einer Variablen und behandelt die übrigen als Parameter. Wohldefiniert ist das, weil jedes innere Integral nach dem Parameterintegral-Satz eine **stetige** Funktion der restlichen Variablen liefert — über die man dann weiter integrieren kann (induktiv in jeder Dimension).
F: Was besagt der Satz von Fubini, und unter welcher Voraussetzung?
A: Für eine **stetige** Funktion auf einem **endlichen** Quader darf man die Reihenfolge der Integrationen beliebig vertauschen: $\int_c^d\int_a^b f\,dx\,dy=\int_a^b\int_c^d f\,dy\,dx$. Das Ergebnis hängt nicht von der Reihenfolge ab.
F: Warum ist Fubini anschaulich nichts anderes als das Cavalieri-Prinzip?
A: Das Integral ist das Volumen unter der Fläche $z=f(x,y)$. Ob man dieses Volumen aus Scheiben in $x$-Richtung oder in $y$-Richtung aufbaut, ändert nichts am Gesamtvolumen — genau das ist Cavalieri.
F: Wie zeigt der Beweis, dass beide Reihenfolgen gleich sind (Rolle der Hilfsfunktion $h$)?
A: Man bildet die Differenz $h(\xi,\eta)$ der beiden bis zu variablen Grenzen integrierten Reihenfolgen. Mit Hauptsatz und Leibnizregel folgt $\partial_\xi h=\partial_\eta h=0$, also ist $h$ konstant; wegen $h(a,c)=0$ ist $h\equiv0$ — und das ist die behauptete Gleichheit.
F: Warum lohnt es sich, die Integrationsreihenfolge klug zu wählen, und nach welchem Kriterium?
A: Weil beide Reihenfolgen dasselbe Ergebnis geben, aber unterschiedlich aufwändig sind — eine kann elementar sein, die andere partielle Integration erfordern. Faustregel: zuerst die Variable integrieren, bei der der Integrand am einfachsten eine Stammfunktion hat.
F: Warum gilt Fubini bei uneigentlichen Mehrfachintegralen nur unter absoluter Integrierbarkeit?
A: Ohne absolute Konvergenz hängt der Wert von der Summationsreihenfolge ab — die beiden Integrationsreihenfolgen können dann **verschiedene** Ergebnisse liefern. Absolute Integrierbarkeit garantiert, dass die Vertauschung erlaubt bleibt.
F: Was besagt die Standardabschätzung $|\int_Q f|\le|Q|\sup_Q|f|$, und woher kommt sie?
A: Der Betrag des Integrals ist höchstens das Quadervolumen mal den größten Funktionsbetrag. Sie folgt aus Monotonie und Linearität ($|f|\le\sup|f|$ integrieren) und ist das mehrdimensionale Gegenstück zur 1D-Regel „Integral $\le$ Intervalllänge × Maximum".
F: Wozu sind Linearität und Monotonie des Integrals praktisch nützlich?
A: Linearität erlaubt, Integrale zu zerlegen und Konstanten herauszuziehen; Monotonie erlaubt Abschätzungen nach oben/unten. Zusammen sind sie das Rückgrat fast aller Integral-Beweise (u. a. der Standardabschätzung).
F: Was heißt „kompakter Träger", und warum ist $\int_{\mathbb{R}^n}f:=\int_Q f$ unabhängig vom gewählten Quader $Q$?
A: $f$ hat kompakten Träger, wenn $f(x)=0$ für $|x|>R$. Außerhalb dieses Radius trägt nichts zum Integral bei, also liefert **jeder** Quader $Q$, der den Träger umschließt, denselben Wert — die Wahl von $Q$ ist beliebig.
F: Warum braucht man für Funktionen ohne kompakten Träger einen Grenzwert bzw. das Lebesgue-Integral?
A: Der einfache Quader-Zugang funktioniert nur, solange das Gebiet beschränkt ist bzw. $f$ außerhalb verschwindet. Für unbeschränkte Gebiete oder langsam abfallende Funktionen muss man das Integral als Grenzwert auffassen; der saubere Rahmen dafür ist das Lebesgue-Integral.
:::
