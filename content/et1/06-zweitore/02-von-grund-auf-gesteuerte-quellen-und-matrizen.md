---
title: Von Grund auf: Gesteuerte Quellen und Matrizen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160200
summary: Warum vier Zahlen ein ganzes Netzwerk ersetzen und jede Parameterform nur eine andere Wahl ist
tags: gesteuerte Quelle, Matrix, Determinante, inverse Matrix, Einheitsmatrix
lang: de
---

Eine ideale Quelle aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) liefert einen festen Wert. Eine __gesteuerte Quelle__ liefert einen Wert, der einer anderen Spannung oder einem anderen Strom an anderer Stelle der Schaltung proportional ist. Ihr Schaltzeichen ist eine Raute. Die Abkürzungen kommen aus dem Englischen (voltage bzw. current controlled voltage bzw. current source).

| Name | Kürzel | Gesetz | Faktor |
|---|---|---|---|
| spannungsgesteuerte Spannungsquelle | VCVS | $U=\mu\,U_\mathrm{s}$ | ohne Einheit |
| stromgesteuerte Spannungsquelle | CCVS | $U=r\,I_\mathrm{s}$ | in $\Omega$ |
| spannungsgesteuerte Stromquelle | VCCS | $I=g\,U_\mathrm{s}$ | in S |
| stromgesteuerte Stromquelle | CCCS | $I=\beta\,I_\mathrm{s}$ | ohne Einheit |

Der Index s steht für die steuernde Größe. Das bekannteste Beispiel ist der Bipolartransistor ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)): Ein kleiner Basisstrom steuert einen großen Kollektorstrom. Die Energie dafür kommt aus der Versorgungsspannung, das Steuersignal liefert nur die Information. Steuergröße und Quelle sitzen an verschiedenen Stellen, deshalb ist jede gesteuerte Quelle von Natur aus ein Zweitor.

Eine __Matrix__ ist ein rechteckiges Zahlenschema, hier fast immer mit zwei Zeilen und zwei Spalten. Fett gedruckte Buchstaben stehen für Matrizen und für Spalten aus zwei Größen. Beim Multiplizieren wird jede Zeile der linken Matrix mit jeder Spalte der rechten verrechnet, Element mal Element, dann addiert:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix},\qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}.$$

Bei zwei Matrizen kommt es auf die Reihenfolge an. Addiert werden Matrizen Element für Element. Die Zahl $\det\mathbf M=a\,d-b\,c$ heißt __Determinante__. Ist sie nicht null, gibt es die __inverse Matrix__, die $\mathbf y=\mathbf M\,\mathbf x$ nach $\mathbf x$ auflöst:

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

Das Produkt $\mathbf M\,\mathbf M^{-1}$ ist die __Einheitsmatrix__ $\mathbf 1$ mit Einsen auf der Diagonale und Nullen sonst. Sie ändert nichts, womit man sie multipliziert.

::::formelsammlung
**Gesteuerte Quellen**

$$U=\mu\,U_\mathrm{s},\qquad U=r\,I_\mathrm{s},\qquad I=g\,U_\mathrm{s},\qquad I=\beta\,I_\mathrm{s}$$

Der Wert der Quelle ist einer Spannung oder einem Strom an anderer Stelle der Schaltung proportional; der Index s steht für die steuernde Größe. Der Reihe nach: spannungsgesteuerte Spannungsquelle (VCVS, $\mu$ ohne Einheit), stromgesteuerte Spannungsquelle (CCVS, $r$ in $\Omega$), spannungsgesteuerte Stromquelle (VCCS, $g$ in S), stromgesteuerte Stromquelle (CCCS, $\beta$ ohne Einheit). Schaltzeichen: Raute. Steuergröße und Quelle sitzen an verschiedenen Stellen, deshalb ist jede gesteuerte Quelle ein Zweitor.

**Matrix mal Spalte**

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix}$$

Jede Zeile der Matrix wird mit der Spalte verrechnet, Element mal Element, dann addiert. Fett gedruckte Buchstaben stehen für Matrizen und für Spalten aus zwei Größen.

**Matrix mal Matrix**

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}$$

Jede Zeile der linken Matrix wird mit jeder Spalte der rechten verrechnet. Die Reihenfolge zählt. Addiert werden Matrizen Element für Element.

**Determinante**

$$\det\mathbf M=a\,d-b\,c$$

Für die Matrix mit $a$, $b$ in der ersten und $c$, $d$ in der zweiten Zeile. Ist sie nicht null, gibt es die inverse Matrix.

**Inverse Matrix**

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

Löst $\mathbf y=\mathbf M\,\mathbf x$ nach $\mathbf x$ auf. Nur wenn die Determinante nicht null ist.

**Einheitsmatrix**

$$\mathbf M\,\mathbf M^{-1}=\mathbf 1$$

$\mathbf 1$ hat Einsen auf der Diagonale und Nullen sonst. Sie ändert nichts, womit man sie multipliziert.
::::

::::lernkarten
:::karte begriff gesteuerte Quelle
Wodurch unterscheidet sich eine gesteuerte Quelle von einer idealen Quelle mit festem Wert?
---
Sie liefert einen Wert, der einer anderen Spannung oder einem anderen Strom an anderer Stelle der Schaltung proportional ist. Ihr Schaltzeichen ist eine Raute.
--- falsch
Sie liefert einen festen Wert, den man aber von außen mit einem Regler verstellen kann. Ihr Schaltzeichen ist ein Kreis mit einem Pfeil durch die Mitte.
--- falsch
Sie liefert einen Wert, der ihrem eigenen Strom proportional ist. Deshalb verhält sie sich an ihren Anschlüssen wie ein Widerstand und hat auch dessen Schaltzeichen.
--- falsch
Sie liefert einen Wert, der sich nach einem festen Zeitplan ändert, unabhängig von der übrigen Schaltung. Ihr Schaltzeichen ist eine Raute.
:::
:::karte formel Vier Arten gesteuerter Quellen
Welche Gesetze gelten für die vier Arten gesteuerter Quellen, und welche Einheit hat jeweils ihr Faktor?
---
VCVS $U=\mu\,U_\mathrm{s}$ und CCCS $I=\beta\,I_\mathrm{s}$ mit Faktoren ohne Einheit, CCVS $U=r\,I_\mathrm{s}$ mit $r$ in $\Omega$, VCCS $I=g\,U_\mathrm{s}$ mit $g$ in S. Der Index s steht für die steuernde Größe.
--- falsch
VCVS $U=\mu\,U_\mathrm{s}$ und CCCS $I=\beta\,I_\mathrm{s}$ mit Faktoren ohne Einheit, CCVS $U=r\,I_\mathrm{s}$ mit $r$ in S, VCCS $I=g\,U_\mathrm{s}$ mit $g$ in $\Omega$. Der Index s steht für die steuernde Größe.
--- falsch
Alle vier Faktoren sind ohne Einheit, weil sie nur Verhältnisse angeben: $U=\mu\,U_\mathrm{s}$, $U=r\,I_\mathrm{s}$, $I=g\,U_\mathrm{s}$, $I=\beta\,I_\mathrm{s}$. Der Index s steht für die Speisung der Quelle.
--- falsch
VCCS $U=r\,I_\mathrm{s}$ mit $r$ in $\Omega$, CCVS $I=g\,U_\mathrm{s}$ mit $g$ in S, VCVS und CCCS ohne Einheit. Der erste Buchstabe des Kürzels nennt die gelieferte Größe, der zweite die steuernde.
:::
:::karte zusammenhang Gesteuerte Quelle als Zweitor
Warum ist jede gesteuerte Quelle von Natur aus ein Zweitor?
---
Steuergröße und Quelle sitzen an verschiedenen Stellen der Schaltung. Die steuernde Spannung oder der steuernde Strom gehört zu einem Anschlusspaar, die gelieferte Größe zu einem anderen.
--- falsch
Weil sie wie jede Quelle zwei Anschlüsse hat, an denen der Strom hinein- und wieder herausfließt. Ein einzelnes solches Anschlusspaar heißt bereits Zweitor, weil es zwei Klemmen hat.
--- falsch
Weil sie ihre Energie aus dem Steuersignal bezieht. Dieses Signal muss über ein zweites Anschlusspaar zugeführt werden, das zusammen mit dem ersten das Zweitor bildet.
--- falsch
Weil sie immer aus zwei Bauteilen besteht, einer idealen Quelle und einem Widerstand in Reihe. Jedes der beiden Bauteile bildet dabei ein eigenes Tor.
:::
:::karte zusammenhang Energie der gesteuerten Quelle
Woher kommt beim Bipolartransistor, der als gesteuerte Quelle wirkt, die Energie für den großen Kollektorstrom?
---
Aus der Versorgungsspannung. Der kleine Basisstrom liefert nur die Information, wie groß der Kollektorstrom sein soll.
--- falsch
Aus dem Basisstrom selbst: Er wird im Transistor vervielfacht, und die zusätzliche Energie entsteht beim Vervielfachen der Ladung.
--- falsch
Aus dem Steuersignal: Der kleine Basisstrom trägt bei hoher Spannung genug Leistung, um den großen Kollektorstrom zu treiben.
--- falsch
Aus der Last: Sie gibt beim Stromfluss Energie an den Transistor zurück, die er als Kollektorstrom weiterleitet.
:::
:::karte begriff Matrix
Was ist eine Matrix, wie sie zur Beschreibung von Zweitoren gebraucht wird, und wofür stehen fett gedruckte Buchstaben?
---
Ein rechteckiges Zahlenschema, hier fast immer mit zwei Zeilen und zwei Spalten. Fett gedruckte Buchstaben stehen für Matrizen und für Spalten aus zwei Größen.
--- falsch
Eine einzelne Zahl, die man aus vier Messwerten mittelt. Fett gedruckte Buchstaben kennzeichnen gemessene Größen im Unterschied zu berechneten.
--- falsch
Ein Gleichungssystem aus zwei Gleichungen mit vier Unbekannten. Fett gedruckte Buchstaben stehen für die Unbekannten, normal gedruckte für bekannte Werte.
--- falsch
Ein Zahlenschema, das stets genau zwei Zeilen und zwei Spalten hat. Fett gedruckte Buchstaben stehen nur für Ströme und Spannungen, nie für Matrizen.
:::
:::karte formel Matrix mal Spalte
Wie multipliziert man eine Matrix mit zwei Zeilen und zwei Spalten mit einer Spalte aus zwei Größen?
---
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix}$. Jede Zeile der Matrix wird mit der Spalte verrechnet, Element mal Element, dann addiert.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+c\,y\\b\,x+d\,y\end{pmatrix}$. Jede Spalte der Matrix wird mit der Spalte verrechnet, Element mal Element, dann addiert.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,x\\c\,y+d\,y\end{pmatrix}$. Jede Zeile der Matrix wird mit einer der beiden Größen multipliziert, dann wird addiert.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x&b\,y\\c\,x&d\,y\end{pmatrix}$. Jedes Element wird mit der Größe seiner Spalte multipliziert, addiert wird dabei nicht.
:::
:::karte formel Produkt zweier Matrizen
Wie multipliziert man zwei Matrizen mit je zwei Zeilen und zwei Spalten, und spielt die Reihenfolge eine Rolle?
---
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}$. Jede Zeile der linken wird mit jeder Spalte der rechten verrechnet. Die Reihenfolge zählt.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e&b\,f\\c\,g&d\,h\end{pmatrix}$. Man multipliziert Element für Element wie beim Addieren, deshalb ist die Reihenfolge gleichgültig.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}$. Die Reihenfolge ist gleichgültig, wie beim Multiplizieren gewöhnlicher Zahlen.
--- falsch
$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}$. Die Reihenfolge zählt, und auch beim Addieren verrechnet man Zeilen mit Spalten.
:::
:::karte begriff Determinante
Was ist die Determinante einer Matrix mit zwei Zeilen und zwei Spalten, und was folgt aus ihrem Wert?
---
Die Zahl $\det\mathbf M=a\,d-b\,c$, gebildet aus $a$, $b$ in der ersten und $c$, $d$ in der zweiten Zeile. Ist sie nicht null, gibt es die inverse Matrix.
--- falsch
Die Zahl $\det\mathbf M=a\,d+b\,c$, gebildet aus den vier Elementen. Ist sie nicht null, gibt es die inverse Matrix; ist sie null, ist die Matrix die Einheitsmatrix.
--- falsch
Die Zahl $\det\mathbf M=a\,d-b\,c$, gebildet aus den vier Elementen. Ist sie null, gibt es die inverse Matrix, weil sich die beiden Gleichungen dann nicht widersprechen.
--- falsch
Die Zahl $\det\mathbf M=a\,b-c\,d$, das Produkt der ersten Zeile minus das der zweiten. Ist sie nicht null, sind die beiden Zeilen gleich.
:::
:::karte begriff inverse Matrix
Was leistet die inverse Matrix bei einer Gleichung $\mathbf y=\mathbf M\,\mathbf x$, und wie lautet sie für zwei Zeilen und zwei Spalten?
---
Sie löst die Gleichung nach $\mathbf x$ auf: $\mathbf x=\mathbf M^{-1}\mathbf y$ mit $\mathbf M^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$. Es gibt sie nur, wenn die Determinante nicht null ist.
--- falsch
Sie kehrt jedes Element einzeln um: $\mathbf M^{-1}=\begin{pmatrix}1/a&1/b\\1/c&1/d\end{pmatrix}$. Es gibt sie, solange kein einziges Element der Matrix null ist.
--- falsch
Sie löst die Gleichung nach $\mathbf x$ auf: $\mathbf x=\mathbf M^{-1}\mathbf y$ mit $\mathbf M^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}a&-b\\-c&d\end{pmatrix}$. Es gibt sie nur, wenn die Determinante nicht null ist.
--- falsch
Sie löst die Gleichung nach $\mathbf x$ auf, mit $\mathbf M^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$. Es gibt sie immer; ist die Determinante null, wird der Bruch nur sehr groß.
:::
:::karte begriff Einheitsmatrix
Was ist die Einheitsmatrix $\mathbf 1$, und bei welchem Produkt tritt sie auf?
---
Die Matrix mit Einsen auf der Diagonale und Nullen sonst. Sie ist das Produkt $\mathbf M\,\mathbf M^{-1}$ und ändert nichts, womit man sie multipliziert.
--- falsch
Die Matrix, in der jedes Element eins ist. Sie ist das Produkt $\mathbf M\,\mathbf M^{-1}$ und ändert nichts, womit man sie multipliziert.
--- falsch
Die Matrix mit Nullen auf der Diagonale und Einsen sonst. Sie ist das Produkt $\mathbf M\,\mathbf M^{-1}$ und vertauscht die beiden Größen jeder Spalte.
--- falsch
Die Matrix mit Einsen auf der Diagonale und Nullen sonst. Sie ist die Summe aus $\mathbf M$ und $\mathbf M^{-1}$ und macht jede Spalte zu null.
:::
::::
