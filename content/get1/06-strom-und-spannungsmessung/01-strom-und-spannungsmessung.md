---
title: Strom- und Spannungsmessung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Strom- und Spannungsmessung
order: 60100
summary: Warum ein Amperemeter in Reihe und ein Voltmeter parallel geschaltet wird, wieso das eine möglichst keinen und das andere möglichst unendlichen Innenwiderstand braucht und wie man mit Shunt und Vorwiderstand den Messbereich erweitert.
tags: Messung, Amperemeter, Voltmeter, Innenwiderstand, Shunt, Vorwiderstand, Messbereichserweiterung
---

:::konzept
Ein gutes Messgerät hat eine unbequeme Aufgabe: Es soll eine Größe bestimmen, ohne sie dabei zu verändern. Ein
**Amperemeter** muss sich in den Strompfad einklinken, darf ihn aber nicht bremsen — also möglichst **keinen**
Widerstand haben. Ein **Voltmeter** zapft eine Spannung ab, darf dem Kreis aber keinen Strom stehlen — also
möglichst **unendlichen** Widerstand haben. Aus diesen zwei Idealen folgt alles Weitere: wie man misst und wie
man den Messbereich erweitert.
:::

**Worum es geht:** Nachdem wir Ströme und Spannungen berechnen können, geht es ums Messen. Entscheidend ist der
__Innenwiderstand__ des Messgeräts — er bestimmt, ob die Messung die Schaltung stört. Wir klären die richtige
Schaltung für Strom und Spannung und wie man mit Zusatzwiderständen größere Werte misst.

## Strommessung: das Amperemeter in Reihe

Ein __Amperemeter__ misst den Strom, der durch es hindurchfließt. Also muss es **in Reihe** in den Zweig
geschaltet werden, dessen Strom man wissen will — nur so fließt genau dieser Strom hindurch.

Dabei liegt das Gerät mit seinem __Innenwiderstand__ $R_i$ im Strompfad. Nach der Reihenschaltung addiert sich
$R_i$ zum vorhandenen Widerstand und verkleinert den Strom — genau das, was man eigentlich messen wollte. Damit
dieser Fehler klein bleibt, muss das Amperemeter einen **möglichst kleinen** Innenwiderstand haben. Das __ideale
Amperemeter__ hat

$$R_i = 0,$$

verhält sich also wie ein widerstandsloses Stück Draht und verändert den Strom überhaupt nicht.

:::grafik
Ein Stromkreis mit Quelle und Widerstand, dazwischen ein Amperemeter (Kreis mit „A") in Reihe im Leiter.
Hinweis: „idealerweise $R_i = 0$ — stört den Strom nicht". Als Warnung ein zweites Bild: Amperemeter
fälschlich parallel, mit rotem Kreuz.
:::

## Spannungsmessung: das Voltmeter parallel

Ein __Voltmeter__ misst die Spannung zwischen zwei Punkten. Spannung ist eine Differenz zwischen zwei Orten,
also legt man das Gerät **parallel** zum Bauteil, über dem man die Spannung abgreifen will.

Jetzt ist die Gefahr umgekehrt: Über seinen Innenwiderstand $R_i$ zieht das parallel liegende Voltmeter einen
kleinen Strom, der sonst woanders geflossen wäre — die Messung verfälscht die Stromverteilung. Damit dieser
Nebenstrom verschwindet, muss das Voltmeter einen **möglichst großen** Innenwiderstand haben. Das __ideale
Voltmeter__ hat

$$R_i \to \infty,$$

nimmt also keinen Strom auf und belastet die Schaltung nicht.

**Anders betrachtet.** Die beiden Ideale sind spiegelbildlich und folgen beide aus demselben Grundsatz „nicht
stören": In Reihe stört ein Widerstand (Amperemeter → $R_i$ klein), parallel stört ein Strompfad (Voltmeter →
$R_i$ groß). Merkt man sich das eine, folgt das andere.

:::grafik
Derselbe Stromkreis, nun mit einem Voltmeter (Kreis mit „V") parallel über dem Widerstand. Hinweis:
„idealerweise $R_i \to \infty$ — zieht keinen Strom". Daneben als Warnung ein Voltmeter fälschlich in Reihe, mit
rotem Kreuz.
:::

## Messbereichserweiterung

Ein Messwerk schlägt nur bis zu einem bestimmten Strom bzw. einer bestimmten Spannung voll aus. Mit einem
Zusatzwiderstand lässt sich der Messbereich um einen Faktor $n$ vergrößern — für Strom und Spannung auf genau
gegensätzliche Weise.

Für das __Amperemeter__ legt man einen __Nebenwiderstand__ (englisch __Shunt__) **parallel** zum Messwerk. Er
übernimmt den Großteil des Stroms, sodass durch das Messwerk nur noch ein bekannter Bruchteil fließt. Für die
$n$-fache Reichweite gilt

$$R_\text{p} = \frac{R_i}{n - 1}.$$

Für das __Voltmeter__ schaltet man einen __Vorwiderstand__ **in Reihe**. Er nimmt den überschüssigen Teil der
Spannung auf, sodass am Messwerk nur ein bekannter Bruchteil anliegt. Für die $n$-fache Reichweite gilt

$$R_\text{v} = R_i\,(n - 1).$$

- __$n$__: der __Erweiterungsfaktor__ (Verhältnis von neuem zu altem Messbereich).
- __$R_i$__: der __Innenwiderstand__ des Messwerks.
- __$R_\text{p}, R_\text{v}$__: __Nebenwiderstand__ (parallel) bzw. __Vorwiderstand__ (in Reihe).

Die Logik ist wieder das Teilerprinzip: Der Shunt bildet mit dem Messwerk einen __Stromteiler__ (ein fester
Anteil fließt durchs Messwerk), der Vorwiderstand einen __Spannungsteiler__ (ein fester Anteil fällt am Messwerk
ab). Mess­bereichs­erweiterung ist also nichts Neues, nur eine Anwendung der Teilerregeln.

:::grafik
Zwei kleine Schaltbilder: links das Messwerk mit parallelem Shunt $R_\text{p}$ (Strom teilt sich auf), rechts
das Messwerk mit Vorwiderstand $R_\text{v}$ in Reihe (Spannung teilt sich auf). Jeweils die Formel darunter.
:::

:::kern
Ein __Amperemeter__ liegt __in Reihe__ und braucht einen __kleinen__ Innenwiderstand (ideal $R_i = 0$), ein
__Voltmeter__ liegt __parallel__ und braucht einen __großen__ Innenwiderstand (ideal $R_i \to \infty$) — beide,
um die Messung nicht zu stören. Den Messbereich erweitert man um den Faktor $n$ mit einem __Shunt__ parallel zum
Amperemeter ($R_\text{p} = R_i/(n-1)$, ein Stromteiler) bzw. einem __Vorwiderstand__ in Reihe zum Voltmeter
($R_\text{v} = R_i(n-1)$, ein Spannungsteiler).
:::

Besonders genau wird eine Messung, wenn man gar nicht auf einen Zeigerausschlag angewiesen ist, sondern nur auf
„Strom null" abgleicht. Dieses Prinzip steckt in der __Wheatstoneschen Messbrücke__ — dem Thema des nächsten
Abschnitts.
