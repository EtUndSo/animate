---
title: Ideale und reale Quellen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70300
summary: Was eine ideale Spannungs- und Stromquelle ausmacht, warum echte Quellen unter Last einbrechen und wie man eine reale Spannungsquelle in eine gleichwertige Stromquelle umrechnet.
tags: Spannungsquelle, Stromquelle, Innenwiderstand, Leerlaufspannung, Kurzschlussstrom, Quellenumwandlung
---

:::konzept
Jede Schaltung braucht einen Antrieb — eine Quelle. Im Idealfall ist sie unerschütterlich: Eine ideale
**Spannungsquelle** hält ihre Spannung, egal wie viel Strom man zieht; eine ideale **Stromquelle** hält ihren
Strom, egal welche Spannung sich einstellt. Echte Quellen schaffen das nicht ganz — unter Last brechen sie ein,
weil in ihnen ein **Innenwiderstand** steckt. Und: Eine reale Spannungsquelle und eine reale Stromquelle können
sich nach außen völlig gleich verhalten; man kann sie ineinander umrechnen.
:::

**Worum es geht:** Bevor man Netzwerke mit Ersatzquellen und Superposition zerlegt, braucht man ein sauberes
Modell für Quellen. Wir bauen es in Stufen: erst die beiden Idealquellen, dann der __Innenwiderstand__ als
Realitätskorrektur, schließlich die __Quellenumwandlung__.

## Die ideale Spannungsquelle

Eine __ideale Spannungsquelle__ liefert eine feste __Quellenspannung__ $U_0$ — unabhängig davon, welcher Strom
fließt. Ihr __Innenwiderstand__ ist

$$R_i = 0.$$

In der __Kennlinie__ (Klemmenspannung über Strom) ist das eine **waagerechte** Linie: Egal wie groß der Strom
wird, die Spannung bleibt $U_0$. Das ist eine Idealisierung — eine echte Steckdose oder Batterie käme bei
unendlichem Strom an ihre Grenzen —, aber als Modell extrem nützlich.

## Die ideale Stromquelle

Spiegelbildlich dazu liefert eine __ideale Stromquelle__ einen festen __Quellenstrom__ $I_0$ — unabhängig von
der Spannung, die sich an ihr einstellt. Ihr Innenwiderstand ist

$$R_i \to \infty.$$

Ihre Kennlinie ist eine **senkrechte** Linie: Der Strom ist immer $I_0$, die Spannung richtet sich allein nach
dem angeschlossenen Verbraucher. Eine Stromquelle „presst" also einen festen Strom durch, koste es an Spannung,
was es wolle.

:::grafik
Ein Kennlinienfeld (Klemmenspannung $U$ über Strom $I$): eine waagerechte Linie auf Höhe $U_0$ (ideale
Spannungsquelle) und eine senkrechte Linie bei $I_0$ (ideale Stromquelle), jeweils beschriftet. Daneben die
Schaltsymbole beider Quellen.
:::

## Reale Quellen: der Innenwiderstand

Echte Quellen haben einen endlichen __Innenwiderstand__ $R_i$. Man modelliert die __reale Spannungsquelle__ als
ideale Quelle $U_0$ mit einem $R_i$ in **Reihe**. Fließt ein Strom $I$, fällt an $R_i$ die Spannung $R_i\,I$ ab,
und nach außen bleibt nur die __Klemmenspannung__

$$U = U_0 - R_i \cdot I.$$

- __$U$__: die __Klemmenspannung__ (was außen tatsächlich ankommt).
- __$U_0$__: die __Quellenspannung__ (die innere, „ideale" Spannung).
- __$R_i$__: der __Innenwiderstand__ der Quelle.
- __$I$__: der entnommene __Strom__.

Zwei Grenzfälle lesen sich direkt ab. Ohne Last ($I = 0$) fällt an $R_i$ nichts ab, und die Klemmenspannung ist
gleich der __Leerlaufspannung__ $U = U_0$. Bei Kurzschluss ($U = 0$) fließt der maximale __Kurzschlussstrom__

$$I_\text{K} = \frac{U_0}{R_i}.$$

Die Kennlinie ist also keine Waagerechte mehr, sondern eine **fallende Gerade**: Je mehr Strom man zieht, desto
stärker bricht die Klemmenspannung ein. Genau das merkt man, wenn die Autobatterie beim Anlassen „in die Knie
geht". Je kleiner $R_i$, desto flacher die Gerade, desto „idealer" die Quelle.

:::grafik
Links das Ersatzschaltbild der realen Spannungsquelle: ideale Quelle $U_0$ in Reihe mit $R_i$, dahinter die
Klemmen. Rechts die fallende Kennlinie $U = U_0 - R_i I$ mit markierter Leerlaufspannung $U_0$ (bei $I=0$) und
Kurzschlussstrom $I_\text{K} = U_0/R_i$ (bei $U=0$).
:::

## Quellenumwandlung: Spannungsquelle ↔ Stromquelle

Jetzt der elegante Teil. Eine reale Spannungsquelle ($U_0$ in Reihe mit $R_i$) und eine reale Stromquelle
($I_0$ **parallel** zu $R_i$) können an ihren Klemmen **exakt dieselbe** Kennlinie haben — von außen sind sie
dann nicht unterscheidbar. Die Umrechnung folgt direkt aus den beiden Grenzfällen:

$$I_0 = \frac{U_0}{R_i}, \qquad U_0 = R_i \cdot I_0.$$

- __$I_0$__: der __Quellenstrom__ der Stromquelle (gleich dem Kurzschlussstrom der Spannungsquelle).
- __$U_0$__: die __Quellenspannung__ (gleich der Leerlaufspannung).
- __$R_i$__: der __Innenwiderstand__ — in beiden Darstellungen **derselbe**, nur einmal in Reihe und einmal parallel.

Das Rezept: Der __Kurzschlussstrom__ der Spannungsquelle wird zum Quellenstrom der Stromquelle, die
__Leerlaufspannung__ bleibt erhalten, und der Innenwiderstand wandert von der Reihe in die Parallelschaltung
(oder umgekehrt). Diese Umwandlung ist das zentrale Werkzeug, um gemischte Netzwerke zu vereinfachen — man wählt
jeweils die Darstellung, die sich gerade leichter zusammenfassen lässt.

:::grafik
Zwei nebeneinanderstehende Ersatzschaltbilder mit einem Doppelpfeil dazwischen: links $U_0$ in Reihe mit $R_i$,
rechts $I_0$ parallel zu $R_i$. Am Pfeil die Umrechnung $I_0 = U_0/R_i$ und $U_0 = R_i I_0$, dazu „gleicher
$R_i$, gleiche Klemmen-Kennlinie".
:::

:::kern
Die __ideale Spannungsquelle__ hält $U_0$ ($R_i = 0$, waagerechte Kennlinie), die __ideale Stromquelle__ hält
$I_0$ ($R_i \to \infty$, senkrechte Kennlinie). Reale Quellen haben einen endlichen __Innenwiderstand__: Die
reale Spannungsquelle liefert $U = U_0 - R_i I$ (Leerlauf $U_0$, Kurzschluss $I_\text{K} = U_0/R_i$, fallende
Gerade). Eine reale Spannungsquelle und eine reale Stromquelle sind ineinander umwandelbar: $I_0 = U_0/R_i$,
gleicher $R_i$ (einmal in Reihe, einmal parallel) — nach außen gleichwertig.
:::

Diese Gleichwertigkeit ist der Schlüssel zu einem mächtigen Werkzeug: Man kann ein ganzes Netzwerk, so
kompliziert es auch ist, von zwei Klemmen aus durch **eine einzige** Ersatzquelle beschreiben — die
__Ersatzspannungsquelle__ und __Ersatzstromquelle__ (Thévenin und Norton).

:::quiz
F: Was bedeutet $R_i=0$ für eine ideale Spannungsquelle anschaulich?
A: Es fällt intern keine Spannung ab, egal wie viel Strom fließt, also bleibt die Klemmenspannung immer $U_0$. Die Kennlinie ist eine Waagerechte — die Quelle ist unerschütterlich.
F: Warum hat eine ideale Stromquelle einen unendlichen Innenwiderstand?
A: Nur bei $R_i\to\infty$ bleibt der eingeprägte Strom unabhängig von der anliegenden Spannung konstant. Die Quelle „presst" einen festen Strom durch, und die Spannung stellt sich allein nach dem Verbraucher ein.
F: Warum bricht eine reale Spannungsquelle unter Last ein?
A: Der entnommene Strom fällt am Innenwiderstand als $R_i I$ ab, sodass außen nur $U=U_0-R_i I$ ankommt. Je mehr Strom, desto größer dieser interne Abfall und desto kleiner die Klemmenspannung.
F: Was ist die Leerlaufspannung und warum ist sie gleich $U_0$?
A: Im Leerlauf fließt kein Strom ($I=0$), also fällt an $R_i$ nichts ab. Damit erscheint an den Klemmen die volle innere Spannung $U_0$.
F: Wie entsteht der Kurzschlussstrom $I_K=U_0/R_i$?
A: Bei Kurzschluss ist die Klemmenspannung null, sodass die gesamte Quellenspannung über $R_i$ abfällt. Nach dem Ohmschen Gesetz ergibt das den maximalen Strom $U_0/R_i$.
F: Woran erkennt man an der Kennlinie eine „gute" (nahezu ideale) Spannungsquelle?
A: An einer möglichst flachen, nur schwach fallenden Geraden — kleines $R_i$ bedeutet geringen Einbruch unter Last. Je flacher, desto näher an der idealen Waagerechten.
F: Warum können eine reale Spannungs- und eine reale Stromquelle von außen ununterscheidbar sein?
A: Beide erzeugen dieselbe fallende Klemmen-Kennlinie, wenn $I_0=U_0/R_i$ und derselbe $R_i$ verwendet wird. Da ein Verbraucher nur die Klemmengrößen „sieht", kann er die beiden Modelle nicht unterscheiden.
F: Wie lautet das Rezept der Quellenumwandlung?
A: Die Leerlaufspannung bleibt $U_0$, der Kurzschlussstrom $I_0=U_0/R_i$ wird zum Quellenstrom, und derselbe $R_i$ wandert von der Reihe in die Parallelschaltung (oder umgekehrt). Damit sind beide Darstellungen äquivalent.
F: Warum liegt $R_i$ bei der Spannungsquelle in Reihe, bei der Stromquelle aber parallel?
A: In Reihe zieht $R_i$ mit steigendem Strom Spannung ab (Einbruch), parallel leitet er mit steigender Spannung Strom ab. Beide Anordnungen erzeugen genau dieselbe fallende Klemmen-Kennlinie.
F: Wozu ist die Quellenumwandlung in der Netzwerkanalyse nützlich?
A: Man wählt jeweils die Darstellung, die sich gerade leichter zusammenfassen lässt — Reihen-Spannungsquellen oder parallele Stromquellen. So lassen sich gemischte Netze schrittweise vereinfachen.
:::
