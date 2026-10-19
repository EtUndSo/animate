---
title: Effektive Masse und Löcher
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bandstruktur
order: 4030400
summary: Wie man ein Elektron im Kristall trotz des komplizierten Gitterpotentials wie ein freies Teilchen behandelt – mit einer effektiven Masse $m^\star$, die die ganze Wirkung des Gitters in sich aufnimmt. Sie steckt in der Krümmung des Bandes: $m^\star=(\tfrac1{\hbar^2}\partial^2E/\partial k^2)^{-1}$. Starke Krümmung heißt leicht und schnell, ein flaches Band heißt schwer. Am Valenzbandmaximum wird die Krümmung negativ – daraus entsteht das Loch.
tags: effektive Masse, Löcher, Bandkrümmung, Gruppengeschwindigkeit, Valenzband, Ellipsoide, GaAs, Silizium
---

:::grafik
Einstiegs-Animation: Ein $E(k)$-Band mit zwei Extrema. Ans Leitungsband-Minimum werden nacheinander zwei
Parabeln angeschmiegt — eine **stark gekrümmte** (schmal) mit Label „leicht, schnell" und eine **flache** mit
„schwer, langsam". Parallel reagiert eine kleine Kugel auf einen Kraftpfeil: bei starker Krümmung schnellt sie
los, bei flachem Band bewegt sie sich kaum. Am Valenzband-Maximum zeigt die Parabel **nach unten** (negative
Krümmung); dort blinkt ein leerer Platz auf, der sich wie ein **positives** Teilchen bewegt — das __Loch__.
Kernbotschaft: Die Krümmung des Bandes ist die Trägheit des Ladungsträgers.
:::

:::konzept
Ein Elektron im Kristall ist **kein** freies Teilchen — es bewegt sich im komplizierten periodischen Potential
der Atomrümpfe. Trotzdem möchte man es so **einfach** behandeln wie ein freies Teilchen, auf das man bloß
$F = ma$ anwendet. Der geniale Trick: Man steckt die **gesamte** Wirkung des Gitters in eine einzige geänderte
Zahl — die __effektive Masse__ $m^\star$. Dann rechnet man wieder wie mit einem freien Teilchen, nur mit $m^\star$
statt der echten Elektronenmasse. Und diese effektive Masse kann man direkt aus der **Form** der Bandstruktur
ablesen: aus ihrer Krümmung. Als Nebenprodukt fällt dabei das __Loch__ heraus — der positive Ladungsträger, ohne
den kein Transistor funktioniert.
:::

**Worum es geht:** Wir nähern ein Band nahe seinem Extremum durch eine Parabel, leiten daraus über $F=ma$ die
__effektive Masse__ her, deuten sie als Trägheit (Krümmung), und sehen, wie am Valenzbandmaximum aus der negativen
Krümmung das __Loch__ entsteht.

## Nahe am Extremum sieht jedes Band wie ein freies Teilchen aus

Ein wirklich freies Elektron hat die Energie $E = \hbar^2 k^2/(2m)$ — eine **Parabel** über $k$. Ein Kristallband
ist komplizierter (ein Kosinus, siehe Tight-Binding), aber in der **Nähe** eines Extremums (Bandminimum oder
-maximum) lässt sich jede glatte Kurve durch eine Parabel annähern. Genau dort halten sich die relevanten
Ladungsträger auf (die Elektronen sammeln sich am Leitungsband-**Minimum**, die Löcher am
Valenzband-**Maximum**). Wir schreiben also:

$$E(k) \approx E_0 \pm \frac{\hbar^2 k^2}{2m^\star}.$$

- __$E_0$__: die Energie am Bandextremum.
- __$m^\star$__: die __effektive Masse__ — der einzige Parameter, der die Parabel (und damit das lokale
  Transportverhalten) festlegt.
- __$\pm$__: Pluszeichen am Leitungsband-Minimum (nach oben offene Parabel), Minuszeichen am
  Valenzband-Maximum (nach unten offen).

:::grafik
Ein Kosinus-Band; an sein Minimum ist eine nach oben offene Parabel angeschmiegt (Leitungsband), an sein Maximum
eine nach unten offene (Valenzband). Beschriftung „lokal $\approx$ freies Teilchen mit Masse $m^\star$".
:::

## Herleitung: die effektive Masse aus F = ma

Wir verlangen, dass das Kristallelektron dem newtonschen Gesetz $F = m^\star a$ gehorcht, und nutzen zwei
quantenmechanische Bausteine aus den vorigen Artikeln: den **Kristallimpuls** $p = \hbar k$ und die
**Gruppengeschwindigkeit** $v = \tfrac1\hbar\,\partial E/\partial k$.

__Schritt 1__ — Die Kraft ändert den Kristallimpuls:

$$F = \frac{dp}{dt} = \hbar\,\frac{dk}{dt}.$$

__Schritt 2__ — Die Beschleunigung ist die Zeitableitung der Gruppengeschwindigkeit; mit Kettenregel über $k$:

$$a = \frac{dv}{dt} = \frac{1}{\hbar}\frac{\partial^2 E}{\partial k^2}\,\frac{dk}{dt}.$$

__Schritt 3__ — Wir setzen $\tfrac{dk}{dt} = F/\hbar$ (aus Schritt 1) ein:

$$a = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k^2}\,F.$$

Vergleich mit $a = F/m^\star$ liefert die **zentrale Formel**:

$$m^\star = \left(\frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k^2}\right)^{-1}.$$

Die effektive Masse ist also der **Kehrwert der Bandkrümmung** (zweite Ableitung von $E(k)$), mal $\hbar^2$.

:::grafik
Drei-Schritt-Kette als Flussdiagramm: $F=\hbar\,\dot k$ → $a=\tfrac1\hbar E''\dot k$ → $a=\tfrac1{\hbar^2}E''F$,
darunter der Vergleich mit $a=F/m^\star$ und das eingerahmte Ergebnis $m^\star=(\tfrac1{\hbar^2}E'')^{-1}$.
:::

## Krümmung = Trägheit

Die Formel bedeutet anschaulich: Die **Krümmung** des Bandes *ist* die Trägheit des Ladungsträgers.

- **Stark gekrümmtes (schmales, steiles) Band** → große zweite Ableitung → **kleine** effektive Masse. Das
  Elektron reagiert schnell auf Kräfte, ist „leicht" und schnell.
- **Flaches Band** → kleine Krümmung → **große** effektive Masse. Das Elektron ist träge und langsam.

Das ist der direkte Draht von der Bandform zum Bauelement: Steile Bänder bedeuten schnelle Ladungsträger, also
schnelle Transistoren. Und da steile Bänder mit **starker Kopplung** und damit **kleiner Bandlücke** einhergehen
(vorige Artikel), gilt die Faustregel: **kleinere Bandlücke ↔ kleinere effektive Masse**.

:::grafik
Zwei Parabeln übereinander: eine schmale (stark gekrümmt, „klein $m^\star$, schnell") und eine breite (flach,
„groß $m^\star$, langsam"). Darunter jeweils eine Kugel am selben Kraftpfeil — die leichte schnellt weit, die
schwere kaum.
:::

**Warum nicht einfach die echte Elektronenmasse $m_0$ nehmen?** Weil das Elektron im Gitter auf eine Kraft völlig
anders reagiert als im Vakuum — mal leichter, mal schwerer, am Bandrand sogar mit *negativer* Trägheit (siehe
unten). Die effektive Masse fasst genau diese Gitterwirkung in einer Zahl zusammen; die freie Masse $m_0$ würde
das Transportverhalten grob falsch vorhersagen.

## Das Loch: wenn die Krümmung negativ wird

Am **Valenzbandmaximum** ist die Parabel nach unten offen — die Krümmung ist **negativ**, also wäre $m^\star < 0$.
Eine negative Masse ist unanschaulich. Der Ausweg ist ein Buchhaltungstrick von großer Tragweite: Statt das
**fast volle** Valenzband mit seinen Milliarden Elektronen zu verfolgen, beschreibt man die **wenigen fehlenden**
Elektronen. Ein solcher fehlender Platz heißt __Loch__ und verhält sich wie ein echtes Teilchen mit

- **positiver** effektiver Masse und
- **positiver** Ladung $+e$.

**Warum das erlaubt ist:** Ein volles Band trägt keinen Strom (voriger Artikel). Nimmt man ein Elektron heraus,
ist der verbleibende Strom gerade *minus* der Beitrag dieses einen fehlenden Elektrons — und das rechnet sich
exakt so, als bewege sich ein einzelnes **positiv** geladenes Teilchen. Das Loch ist also kein „echtes" Teilchen,
aber eine vollkommen korrekte und viel einfachere Beschreibung. In Halbleitern sind Löcher die zweite Sorte
Ladungsträger neben den Elektronen.

:::grafik
Ein nach unten offenes Valenzband-Maximum; ein einzelner leerer Zustand (Loch) ist markiert. Nebeneinander zwei
Sichtweisen: links „$\sim 10^{23}$ Elektronen minus eines", rechts „ein Loch: $+e$, $m^\star>0$", verbunden durch
ein Gleichheitszeichen.
:::

## Isotrop oder anisotrop: eine Zahl oder mehrere

Ob eine **einzige** effektive Masse genügt, hängt von der Form der Flächen konstanter Energie im $k$-Raum ab:

- **Isotrop:** Sind diese Flächen **Kugeln** (z. B. das Leitungsband-Minimum von GaAs bei $\Gamma$), ist die
  Krümmung in alle Richtungen gleich → **eine** effektive Masse genügt.
- **Anisotrop (Silizium):** Das Silizium-Leitungsband hat sein Minimum **nicht** im Zentrum, sondern in **sechs**
  gleichwertigen Tälern entlang der $\langle 100\rangle$-Richtungen. Jede Fläche konstanter Energie ist ein
  **Ellipsoid** — in der Längsrichtung anders gekrümmt als quer. Daher braucht Silizium **zwei** effektive
  Massen: eine longitudinale $m_l^\star \approx 0{,}92\,m_0$ (entlang der Ellipsoid-Längsachse) und eine
  transversale $m_t^\star \approx 0{,}19\,m_0$ (quer dazu) ([IUE TU Wien](https://www.iue.tuwien.ac.at/phd/smirnov/node45.html),
  [QuantumATK](https://docs.quantumatk.com/tutorials/effective_mass/effective_mass.html)).

:::grafik
Links GaAs: eine kugelförmige Fläche konstanter Energie um $\Gamma$ → eine einzige Masse. Rechts Silizium: sechs
ellipsoide „Zigarren" entlang der Würfelachsen $\langle100\rangle$, mit eingezeichneter Längskrümmung
($m_l^\star=0{,}92\,m_0$) und Querkrümmung ($m_t^\star=0{,}19\,m_0$).
:::

:::kern
Nahe einem Bandextremum ist $E(k)\approx E_0\pm\hbar^2k^2/2m^\star$ (Parabel wie beim freien Teilchen). Aus
$F=m^\star a$ mit $p=\hbar k$ und $v=\tfrac1\hbar\partial E/\partial k$ folgt die __effektive Masse__
$m^\star=(\tfrac1{\hbar^2}\,\partial^2E/\partial k^2)^{-1}$ — der Kehrwert der **Bandkrümmung**. Starke Krümmung →
**kleine** $m^\star$ (leicht/schnell), flaches Band → **große** $m^\star$; kleinere Lücke ↔ kleinere $m^\star$. Am
__Valenzbandmaximum__ ist die Krümmung negativ → man beschreibt die fehlenden Elektronen als __Löcher__ mit
**positiver** Masse und **positiver** Ladung $+e$. **Isotrop** (GaAs-$\Gamma$, Kugeln → eine Masse) vs.
**anisotrop** (Si: 6 Ellipsoid-Täler entlang $\langle100\rangle$, $m_l^\star\approx0{,}92\,m_0$,
$m_t^\star\approx0{,}19\,m_0$).
:::

Wir können jetzt aus einer Bandstruktur die **Geschwindigkeit** und **Trägheit** der Ladungsträger ablesen. Im
letzten Bandstruktur-Artikel schauen wir **reale** Materialien an — Silizium, Galliumarsenid, Graphen — und den
für die Optoelektronik entscheidenden Unterschied zwischen einer __direkten__ und einer __indirekten__ Bandlücke.
