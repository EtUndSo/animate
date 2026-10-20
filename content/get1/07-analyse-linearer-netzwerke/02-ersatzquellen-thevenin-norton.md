---
title: Ersatzquellen – Thévenin und Norton
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70500
summary: Warum sich jedes lineare Netzwerk von zwei Klemmen aus durch eine einzige Ersatzquelle beschreiben lässt, wie man Leerlaufspannung, Kurzschlussstrom und Innenwiderstand bestimmt und wie Thévenin und Norton zusammenhängen.
tags: Ersatzspannungsquelle, Ersatzstromquelle, Thévenin, Norton, Leerlaufspannung, Kurzschlussstrom, Innenwiderstand
---

:::konzept
Egal wie viele Quellen und Widerstände in einer Schaltung stecken — betrachtet man sie nur von zwei
Anschlussklemmen aus, verhält sie sich wie eine **einzige reale Quelle**: eine ideale Quelle plus ein
Widerstand. Man darf die ganze komplizierte Box also durch dieses schlichte Ersatzbild ersetzen, ohne dass ein
angeschlossener Verbraucher den Unterschied merkt. In der Spannungsform heißt das **Thévenin**, in der Stromform
**Norton** — und beide beschreiben dasselbe.
:::

**Worum es geht:** Mit der Quellenumwandlung aus dem vorigen Abschnitt im Rücken verallgemeinern wir sie: Nicht
nur eine reale Quelle, sondern ein **ganzes lineares Netzwerk** lässt sich auf eine Ersatzquelle reduzieren. Das
spart enorm Rechenarbeit, sobald man wissen will, wie sich die Schaltung gegenüber verschiedenen Verbrauchern
verhält.

## Die Grundidee: das Netzwerk als Zweipol

Trennt man aus einer Schaltung zwei Klemmen heraus, an die später ein Verbraucher kommt, bildet der Rest einen
__aktiven Zweipol__ — ein Netzwerk mit zwei Anschlüssen, in dem Quellen stecken. Weil alle Bauteile linear sind,
ist der Zusammenhang zwischen Klemmenspannung und Klemmenstrom eine **Gerade** — genau wie bei einer realen
Quelle. Und zwei Zweipole mit derselben Kennlinie sind von außen ununterscheidbar.

Daraus folgt der __Zweipolsatz__: Jeder lineare aktive Zweipol lässt sich durch eine reale Quelle ersetzen. Man
braucht dafür nur drei Größen — zwei davon sind die bekannten Grenzfälle, die dritte folgt aus ihnen.

:::grafik
Links eine „Black Box" mit vielen Quellen und Widerständen und zwei herausgeführten Klemmen. Ein Pfeil zeigt auf
das Ersatzbild rechts: eine ideale Quelle in Reihe mit einem Widerstand $R_i$. Darüber „von den Klemmen aus
gleich".
:::

## Die drei Größen bestimmen

Um die Ersatzquelle festzulegen, braucht man:

- __$U_\text{L}$__: die __Leerlaufspannung__ — die Spannung zwischen den **offenen** Klemmen (kein Verbraucher,
  Strom null).
- __$I_\text{K}$__: den __Kurzschlussstrom__ — den Strom, der fließt, wenn man die Klemmen **direkt verbindet**
  (Spannung null).
- __$R_i$__: den __Innenwiderstand__ des Zweipols, der beide verknüpft:

$$R_i = \frac{U_\text{L}}{I_\text{K}}.$$

Für $R_i$ gibt es einen zweiten, oft bequemeren Weg: Man **deaktiviert alle Quellen** und misst den Widerstand
zwischen den Klemmen. „Deaktivieren" heißt dabei präzise — jede ideale __Spannungsquelle__ wird durch einen
**Kurzschluss** (Draht) ersetzt, jede ideale __Stromquelle__ durch eine **Unterbrechung** (offene Stelle). Übrig
bleibt ein reines Widerstandsnetz, das man mit Reihen- und Parallelregeln zusammenfasst.

**Warum gerade so deaktivieren?** Eine ideale Spannungsquelle mit $R_i = 0$ „ist" im passiven Netz ein Draht; eine
ideale Stromquelle mit $R_i \to \infty$ „ist" eine Unterbrechung. Man ersetzt jede Quelle also durch ihren
eigenen Innenwiderstand — das ist der Zustand, in dem nur noch die Widerstände das Klemmenverhalten bestimmen.

:::grafik
Dasselbe Netzwerk zweimal: links mit aktiven Quellen (zur Bestimmung von $U_\text{L}$ im Leerlauf und
$I_\text{K}$ im Kurzschluss), rechts mit deaktivierten Quellen — Spannungsquelle als Draht, Stromquelle als
Lücke — zur Bestimmung von $R_i$ aus dem reinen Widerstandsnetz.
:::

## Ersatzspannungsquelle (Thévenin)

Die __Ersatzspannungsquelle__ beschreibt den Zweipol als ideale Spannungsquelle mit der __Leerlaufspannung__
$U_\text{L}$ in **Reihe** mit dem Innenwiderstand $R_i$. An einem Lastwiderstand $R_\text{L}$ liefert sie dann
nach der Spannungsteiler- bzw. Reihenschaltungsregel den Strom

$$I = \frac{U_\text{L}}{R_i + R_\text{L}}.$$

Das ist die ganze Stärke des Verfahrens: Ändert man nur den Verbraucher $R_\text{L}$, muss man **nicht** das
ganze Netzwerk neu durchrechnen — $U_\text{L}$ und $R_i$ bleiben gleich, man setzt einfach das neue $R_\text{L}$
ein.

## Ersatzstromquelle (Norton)

Die __Ersatzstromquelle__ beschreibt denselben Zweipol als ideale Stromquelle mit dem __Kurzschlussstrom__
$I_\text{K}$ **parallel** zum Innenwiderstand $R_i$. Sie ist nichts anderes als die per Quellenumwandlung
überführte Thévenin-Quelle — mit genau den Beziehungen aus dem vorigen Abschnitt:

$$I_\text{K} = \frac{U_\text{L}}{R_i}, \qquad U_\text{L} = R_i \cdot I_\text{K}.$$

Welche Form man wählt, ist Rechenbequemlichkeit: Die Spannungsform ist handlich, wenn der Verbraucher
hochohmig ist (viel größer als $R_i$), die Stromform, wenn er niederohmig ist. Beide beschreiben denselben
Zweipol und liefern dasselbe Ergebnis.

:::grafik
Thévenin und Norton nebeneinander mit Doppelpfeil: links $U_\text{L}$ in Reihe mit $R_i$, rechts $I_\text{K}$
parallel zu $R_i$. Am Pfeil $I_\text{K} = U_\text{L}/R_i$, darunter „gleicher $R_i$, gleiches Klemmenverhalten".
:::

:::kern
Jeder lineare aktive __Zweipol__ ist von zwei Klemmen aus eine reale Quelle (__Zweipolsatz__). Man bestimmt die
__Leerlaufspannung__ $U_\text{L}$ (offene Klemmen), den __Kurzschlussstrom__ $I_\text{K}$ (verbundene Klemmen)
und den __Innenwiderstand__ $R_i = U_\text{L}/I_\text{K}$ — alternativ durch Deaktivieren der Quellen
(Spannungsquelle → Kurzschluss, Stromquelle → offen). __Thévenin__: $U_\text{L}$ in Reihe mit $R_i$ (Laststrom
$I = U_\text{L}/(R_i + R_\text{L})$). __Norton__: $I_\text{K}$ parallel $R_i$, mit $I_\text{K} = U_\text{L}/R_i$.
Beide sind gleichwertig.
:::

Die Ersatzquelle nutzt die Linearität, um ein Netz zu *ersetzen*. Dieselbe Linearität erlaubt noch einen zweiten
Trick — mehrere Quellen getrennt zu behandeln und ihre Wirkungen zu addieren: das __Superpositionsverfahren__.

:::quiz
F: Warum lässt sich jedes lineare Netzwerk von zwei Klemmen aus als reale Quelle beschreiben?
A: Weil bei linearen Bauteilen der Zusammenhang zwischen Klemmenspannung und -strom eine Gerade ist — genau wie bei einer realen Quelle. Zwei Zweipole mit derselben Kennlinie sind von außen ununterscheidbar.
F: Was ist ein aktiver Zweipol?
A: Ein aus der Schaltung herausgetrenntes Netzwerk mit zwei Anschlussklemmen, in dem Quellen stecken. Der Rest der Welt „sieht" von ihm nur die Klemmengrößen Spannung und Strom.
F: Welche drei Größen legen die Ersatzquelle fest, und wie hängen sie zusammen?
A: Leerlaufspannung $U_L$, Kurzschlussstrom $I_K$ und Innenwiderstand $R_i=U_L/I_K$. Zwei davon sind die bekannten Grenzfälle, die dritte folgt aus ihnen.
F: Wie misst man $U_L$ und $I_K$ konkret?
A: $U_L$ ist die Spannung zwischen den offenen Klemmen (kein Verbraucher, Strom null), $I_K$ der Strom bei direkt verbundenen Klemmen (Spannung null). Es sind die beiden Extremfälle der Belastung.
F: Wie bestimmt man $R_i$ über das Deaktivieren der Quellen?
A: Man ersetzt jede ideale Spannungsquelle durch einen Kurzschluss und jede ideale Stromquelle durch eine Unterbrechung und fasst das verbleibende Widerstandsnetz zwischen den Klemmen zusammen. Das ergibt denselben $R_i$ wie $U_L/I_K$.
F: Warum ersetzt man Spannungsquellen durch Draht und Stromquellen durch eine Lücke?
A: Man ersetzt jede Quelle durch ihren eigenen Innenwiderstand: eine ideale Spannungsquelle hat $R_i=0$ (Draht), eine ideale Stromquelle $R_i\to\infty$ (offene Stelle). Übrig bleibt nur noch das Widerstandsnetz, das das Klemmenverhalten bestimmt.
F: Was ist der große praktische Vorteil der Ersatzquelle bei wechselnder Last?
A: $U_L$ und $R_i$ hängen nur vom Netzwerk ab, nicht vom Verbraucher. Ändert man $R_L$, setzt man es einfach in $I=U_L/(R_i+R_L)$ ein, ohne das ganze Netz neu zu berechnen.
F: Wie hängen Thévenin- und Norton-Form zusammen?
A: Sie sind per Quellenumwandlung dasselbe: $I_K=U_L/R_i$ und derselbe $R_i$, einmal in Reihe (Thévenin), einmal parallel (Norton). Beide beschreiben denselben Zweipol mit identischem Klemmenverhalten.
F: Wann ist die Spannungs-, wann die Stromform bequemer?
A: Die Thévenin-Form ist handlich bei hochohmiger Last (viel größer als $R_i$), die Norton-Form bei niederohmiger. Das Ergebnis ist in beiden Fällen gleich — es ist reine Rechenbequemlichkeit.
F: Worauf beruht der ganze Zweipolsatz letztlich?
A: Auf der Linearität aller Bauteile, die eine geradlinige Klemmen-Kennlinie garantiert. Ohne Linearität (z. B. mit einer Diode im Netz) wäre die Kennlinie gekrümmt und nicht durch eine einzige reale Quelle darstellbar.
:::
