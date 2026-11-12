---
title: Von Grund auf: Drei Gleichungen, drei Unbekannte
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180200
summary: Warum ein Netz mit wenigen Unbekannten auskommt
tags: symmetrisch, Leitwert
lang: de
---

Beide Verfahren enden bei einem linearen Gleichungssystem $\mathbf M\,\mathbf x=\mathbf b$, also einer Matrix mal einem Spaltenvektor ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). $\mathbf x$ enthält die Unbekannten, $\mathbf b$ die bekannte rechte Seite. Jede Zeile der Matrix ist eine Gleichung, jede Spalte gehört zu einer Unbekannten. Für zwei Unbekannte ist die Determinante $\det\mathbf M=a\,d-b\,c$ bekannt. Für drei Unbekannte geht man die erste Zeile durch. Jede Zahl wird mit der Determinante multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleibt, und die Vorzeichen wechseln ($+,-,+$):

<span class="anker" id="gl-0-1"></span>
$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p). \tag{0.1}$$

:::satz Satz 0.1 (Cramersche Regel)
<span class="anker" id="satz-0-1"></span>

Ist $D=\det\mathbf M\neq0$, hat $\mathbf M\,\mathbf x=\mathbf b$ genau eine Lösung. Ihre $i$-te Komponente ist

<span class="anker" id="gl-0-2"></span>
$$x_i=\frac{D_i}{D}. \tag{0.2}$$

$D_i$ ist die Determinante der Matrix, in der die Spalte $i$ durch $\mathbf b$ ersetzt wurde.
:::

:::herleitung Cramer bei zwei Unbekannten
Aus $a\,x+b\,y=e$ und $c\,x+d\,y=f$ entsteht $y$-frei: $d$ mal die erste minus $b$ mal die zweite Gleichung ergibt $(a\,d-b\,c)\,x=e\,d-b\,f$. Links steht $D\,x$, rechts die Determinante mit $(e,f)$ in Spalte 1. Bei mehr Unbekannten läuft es gleich.
:::

Beispiel: $2x+y=5$ und $x+3y=5$ haben $D=5$, $D_1=10$, $D_2=5$, also $x=2$, $y=1$. Die Regel eignet sich für die Handrechnung bis etwa vier Unbekannte, besonders wenn die Matrix viele Nullen enthält. Eine Matrix heißt __symmetrisch__, wenn sie sich beim Spiegeln an der Hauptdiagonale (von links oben nach rechts unten) nicht ändert. Der __Leitwert__ $G=1/R$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) hat die Einheit Siemens: $1\,\mathrm{mS}=1/\mathrm{k\Omega}$.

::::formelsammlung
**Lineares Gleichungssystem**

$$\mathbf M\,\mathbf x=\mathbf b$$

Matrix mal Spaltenvektor. $\mathbf x$ enthält die Unbekannten, $\mathbf b$ die bekannte rechte Seite. Jede Zeile der Matrix ist eine Gleichung, jede Spalte gehört zu einer Unbekannten.

**Determinante bei zwei Unbekannten**

$$\det\mathbf M=a\,d-b\,c$$

Für das System $a\,x+b\,y=e$ und $c\,x+d\,y=f$, also mit $a$, $b$ in der ersten und $c$, $d$ in der zweiten Zeile der Matrix.

**Determinante bei drei Unbekannten**

$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p)$$

Entwicklung nach der ersten Zeile: Jede Zahl wird mit der Determinante multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleibt; die Vorzeichen wechseln ($+,-,+$).

**Cramersche Regel**

$$x_i=\frac{D_i}{D}$$

$D=\det\mathbf M$; $D_i$ ist die Determinante der Matrix, in der die Spalte $i$ durch $\mathbf b$ ersetzt wurde. Gilt für $D\neq0$, dann hat $\mathbf M\,\mathbf x=\mathbf b$ genau eine Lösung. Geeignet für die Handrechnung bis etwa vier Unbekannte, besonders bei vielen Nullen in der Matrix.

**Leitwert**

$$G=1/R,\qquad 1\,\mathrm{mS}=1/\mathrm{k\Omega}$$

Einheit Siemens. Wegen $\mathrm{k\Omega\cdot mA}=\mathrm V$ und $\mathrm{mS\cdot V}=\mathrm{mA}$ rechnet man in V, mA, k$\Omega$ und mS ohne Zehnerpotenzen.
::::

::::lernkarten
:::karte formel Gleichungssystem in Matrixform
Wie schreibt man das lineare Gleichungssystem, bei dem beide Verfahren enden, in Matrixform, und wofür stehen Zeilen und Spalten der Matrix?
---
$\mathbf M\,\mathbf x=\mathbf b$, eine Matrix mal einem Spaltenvektor. $\mathbf x$ enthält die Unbekannten, $\mathbf b$ die bekannte rechte Seite. Jede Zeile der Matrix ist eine Gleichung, jede Spalte gehört zu einer Unbekannten.
--- falsch
$\mathbf M\,\mathbf x=\mathbf b$, eine Matrix mal einem Spaltenvektor. $\mathbf x$ enthält die bekannte rechte Seite, $\mathbf b$ die Unbekannten. Jede Zeile der Matrix gehört zu einer Unbekannten, jede Spalte ist eine Gleichung.
--- falsch
$\mathbf M\,\mathbf x=\mathbf b$, eine Matrix mal einem Spaltenvektor. $\mathbf x$ enthält die Unbekannten, $\mathbf b$ die rechte Seite. Jede Spalte der Matrix ist eine Gleichung, jede Zeile gehört zu einer Unbekannten.
--- falsch
$\mathbf x=\mathbf M\,\mathbf b$, die Unbekannten stehen direkt als Matrix mal rechter Seite da. Jede Zeile der Matrix ist eine Gleichung, jede Spalte gehört zu einer bekannten Größe der rechten Seite.
:::
:::karte formel Determinante bei zwei Unbekannten
Wie berechnet man die Determinante eines Gleichungssystems mit zwei Unbekannten, wenn in der ersten Zeile der Matrix $a$, $b$ und in der zweiten $c$, $d$ stehen?
---
$\det\mathbf M=a\,d-b\,c$: das Produkt der Hauptdiagonale minus das Produkt der anderen Diagonale. Ist das Ergebnis nicht null, hat das System genau eine Lösung.
--- falsch
$\det\mathbf M=a\,b-c\,d$: das Produkt der ersten Zeile minus das Produkt der zweiten Zeile. Ist das Ergebnis nicht null, hat das System genau eine Lösung.
--- falsch
$\det\mathbf M=a\,d+b\,c$: die Summe der Produkte beider Diagonalen. Ist das Ergebnis nicht null, hat das System genau eine Lösung, sonst unendlich viele.
--- falsch
$\det\mathbf M=a\,d-b\,c$: das Produkt der Hauptdiagonale minus das Produkt der anderen Diagonale. Ist das Ergebnis null, hat das System genau eine Lösung.
:::
:::karte formel Determinante bei drei Unbekannten
Wie berechnet man die Determinante einer $3\times3$-Matrix, wenn man sie nach der ersten Zeile entwickelt?
---
Jede Zahl der ersten Zeile wird mit der Determinante multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleibt, und die Vorzeichen wechseln ($+,-,+$): $\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p)$.
--- falsch
Jede Zahl der ersten Zeile wird mit der Determinante multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleibt, alle mit Pluszeichen: $a\,(e\,r-f\,q)+b\,(d\,r-f\,p)+c\,(d\,q-e\,p)$.
--- falsch
Man multipliziert die drei Zahlen der Hauptdiagonale und zieht das Produkt der drei Zahlen auf der anderen Diagonale ab, wie bei zwei Unbekannten: $a\,e\,r-c\,e\,p$. Die übrigen Zahlen tragen nichts bei.
--- falsch
Jede Zahl der ersten Zeile wird mit der Summe der Zahlen multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleiben, mit wechselnden Vorzeichen: $a\,(e+f+q+r)-b\,(d+f+p+r)+c\,(d+e+p+q)$.
:::
:::karte formel Cramersche Regel
Wie berechnet man mit der cramerschen Regel die $i$-te Unbekannte eines Gleichungssystems $\mathbf M\,\mathbf x=\mathbf b$, und wann ist sie anwendbar?
---
$x_i=\frac{D_i}{D}$ mit $D=\det\mathbf M$. $D_i$ ist die Determinante der Matrix, in der die Spalte $i$ durch $\mathbf b$ ersetzt wurde. Die Regel gilt für $D\neq0$, dann hat das System genau eine Lösung.
--- falsch
$x_i=\frac{D}{D_i}$ mit $D=\det\mathbf M$. $D_i$ ist die Determinante der Matrix, in der die Spalte $i$ durch $\mathbf b$ ersetzt wurde. Die Regel gilt für $D_i\neq0$, dann hat das System genau eine Lösung.
--- falsch
$x_i=\frac{D_i}{D}$ mit $D=\det\mathbf M$. $D_i$ ist die Determinante der Matrix, in der die Zeile $i$ durch $\mathbf b$ ersetzt wurde. Die Regel gilt für $D\neq0$, dann hat das System genau eine Lösung.
--- falsch
$x_i=\frac{D_i}{D}$ mit $D=\det\mathbf M$. $D_i$ ist die Determinante der Matrix, die nach Streichen von Zeile und Spalte $i$ übrig bleibt. Die Regel gilt für jedes $D$, auch für $D=0$.
:::
:::karte zusammenhang Cramersche Regel von Hand
Für welche Gleichungssysteme eignet sich die cramersche Regel bei der Handrechnung besonders gut?
---
Für Systeme bis etwa vier Unbekannte, besonders wenn die Matrix viele Nullen enthält. Bei der Entwicklung fällt jedes Glied weg, dessen Zahl aus der ersten Zeile null ist, und damit eine ganze Unterdeterminante.
--- falsch
Für Systeme mit beliebig vielen Unbekannten, weil der Aufwand nur so schnell wächst wie die Zahl der Zeilen. Nullen in der Matrix spielen dabei keine Rolle, denn jede Determinante kostet gleich viel Rechenarbeit.
--- falsch
Nur für Systeme mit zwei Unbekannten, weil die Determinante nur für $2\times2$-Matrizen erklärt ist. Bei drei Unbekannten setzt man deshalb nacheinander ein, bis zwei Gleichungen übrig bleiben.
--- falsch
Für Systeme bis etwa vier Unbekannte, aber nur, wenn die Matrix keine Nullen enthält. Eine Null in der ersten Zeile macht die Determinante null, und dann versagt die Regel.
:::
:::karte herleitung Cramersche Regel bei zwei Unbekannten
Leite aus den Gleichungen $a\,x+b\,y=e$ und $c\,x+d\,y=f$ die cramersche Regel für $x$ her.
---
Man multipliziert die erste Gleichung mit $d$ und die zweite mit $b$, weil $y$ dann in beiden Gleichungen denselben Vorfaktor hat.
---
Man zieht die zweite Gleichung von der ersten ab, weil sich dabei die Glieder mit $y$ aufheben: $(a\,d-b\,c)\,x=e\,d-b\,f$.
---
Links steht $D\,x$, weil $a\,d-b\,c$ die Determinante der Matrix ist.
---
Rechts steht $D_1$, weil $e\,d-b\,f$ die Determinante der Matrix ist, in der $(e,f)$ die Spalte 1 ersetzt. Für $D\neq0$ folgt $x=\frac{D_1}{D}$; bei mehr Unbekannten läuft es gleich.
:::
:::karte begriff symmetrisch
Wann nennt man die Matrix eines Gleichungssystems symmetrisch?
---
Wenn sie sich beim Spiegeln an der Hauptdiagonale, die von links oben nach rechts unten läuft, nicht ändert. Jeder Eintrag oberhalb der Diagonale ist dann gleich seinem Spiegelbild unterhalb.
--- falsch
Wenn sie sich beim Spiegeln an der Nebendiagonale, die von rechts oben nach links unten läuft, nicht ändert. Die Einträge auf der Hauptdiagonale müssen dann zusätzlich alle denselben Wert haben.
--- falsch
Wenn alle Einträge auf der Hauptdiagonale gleich sind und alle übrigen null. Jede Gleichung enthält dann nur eine Unbekannte, und das System löst sich Zeile für Zeile.
--- falsch
Wenn ihre erste Zeile gleich ihrer letzten und ihre erste Spalte gleich ihrer letzten ist. Die Matrix sieht dann von oben und von unten gelesen gleich aus.
:::
:::karte begriff Leitwert
Was gibt der Leitwert eines Widerstands an, und welche Einheit gehört zu ihm, wenn man Widerstände in Kiloohm angibt?
---
Den Kehrwert des Widerstands, $G=1/R$, in der Einheit Siemens. Zu Kiloohm gehört Millisiemens: $1\,\mathrm{mS}=1/\mathrm{k\Omega}$.
--- falsch
Den Kehrwert des Widerstands, $G=1/R$, in der Einheit Siemens. Zu Kiloohm gehört Kilosiemens: $1\,\mathrm{kS}=1/\mathrm{k\Omega}$.
--- falsch
Den Widerstand, bezogen auf einen Strom von einem Ampere, $G=U/I$, in der Einheit Siemens. Zu Kiloohm gehört Millisiemens.
--- falsch
Den Widerstand je Länge des Leiters, $G=R/l$, in der Einheit Siemens je Meter. Zu Kiloohm gehört Millisiemens: $1\,\mathrm{mS}=1\,\mathrm{k\Omega}$.
:::
::::
