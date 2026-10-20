---
title: Die Diode und ihre Kennlinie
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100300
summary: Wie aus dem pn-Übergang ein Ventil für den Strom wird, warum die Diode erst ab etwa 0,7 Volt leitet, was die Shockley-Gleichung über ihre Kennlinie sagt und welche Spezialdioden es gibt.
tags: Diode, pn-Übergang, Durchlassrichtung, Sperrrichtung, Schleusenspannung, Shockley-Gleichung, Z-Diode
---

:::konzept
Setzt man an den pn-Übergang eine Spannung, wird aus ihm ein **Ventil für den Strom**: In der einen Richtung
leitet die **Diode** (sobald man eine kleine Schwelle überschreitet), in der anderen sperrt sie fast
vollständig. Das ist das elektrische Gegenstück zum Rückschlagventil in einer Wasserleitung — Durchfluss nur in
eine Richtung. Diese Einseitigkeit ist die Grundlage von Gleichrichtern, Schutzschaltungen und vielem mehr.
:::

**Worum es geht:** Aus dem pn-Übergang des vorigen Abschnitts wird jetzt ein Bauelement. Wir sehen, was in
__Durchlass-__ und __Sperrrichtung__ passiert, fassen das Verhalten in der __Shockley-Gleichung__ zusammen und
lesen die __Kennlinie__ — inklusive der wichtigsten Spezialdioden.

## Durchlass- und Sperrrichtung

Eine __Diode__ hat zwei Anschlüsse: die __Anode__ (am p-Gebiet) und die __Kathode__ (am n-Gebiet). Entscheidend
ist die Polung der äußeren Spannung relativ zur __Raumladungszone__ (der ladungsträgerarmen Sperrschicht aus dem
vorigen Abschnitt).

In __Durchlassrichtung__ legt man den Pluspol an die Anode. Die äußere Spannung wirkt dem inneren Feld entgegen,
die Raumladungszone wird **schmaler**, und ab einer kleinen Schwelle können die Ladungsträger sie überwinden —
es fließt ein kräftiger Strom.

In __Sperrrichtung__ legt man den Pluspol an die Kathode. Jetzt verstärkt die äußere Spannung das innere Feld,
die Raumladungszone wird **breiter**, und frei bewegliche Träger werden von der Grenze weggezogen. Es fließt nur
ein winziger __Sperrstrom__ (bei Silizium im Nanoampere-Bereich), getragen von den wenigen Minoritätsträgern.

:::grafik
Zwei pn-Übergänge nebeneinander: links in Durchlassrichtung (äußere Quelle $+$ an p, schmale Raumladungszone,
großer Strompfeil), rechts in Sperrrichtung ($+$ an n, breite Raumladungszone, nur ein dünner Sperrstrom-Pfeil).
Darunter das Diodensymbol mit Anode/Kathode und Durchlassrichtung in Pfeilrichtung des Symbols.
:::

## Die Shockley-Gleichung

Den Zusammenhang zwischen Strom und Spannung einer idealen Diode beschreibt die __Shockley-Gleichung__:

$$I = I_\text{S}\left(e^{\,U/U_\text{T}} - 1\right).$$

Die Bestandteile:

- __$I$__: der __Diodenstrom__.
- __$U$__: die anliegende __Spannung__ (in Durchlassrichtung positiv gezählt).
- __$I_\text{S}$__: der __Sättigungssperrstrom__ — ein sehr kleiner Materialparameter, der den Sperrstrom
  bestimmt.
- __$U_\text{T}$__: die __Temperaturspannung__ $U_\text{T} = \dfrac{k\,T}{q}$, bei Raumtemperatur etwa
  $26\,\text{mV}$ ($k$ Boltzmann-Konstante, $T$ absolute Temperatur, $q$ Elementarladung).

Die Gleichung erklärt beide Richtungen auf einen Schlag. In **Sperrrichtung** ($U$ stark negativ) geht
$e^{U/U_\text{T}}$ gegen null, und es bleibt $I \approx -I_\text{S}$ — der winzige, nahezu konstante Sperrstrom.
In **Durchlassrichtung** ($U$ positiv, einige Zehntel Volt) wächst der Exponentialterm extrem schnell, die $-1$
wird bedeutungslos, und der Strom steigt __exponentiell__ mit der Spannung. (Bei realen Dioden ergänzt man im
Exponenten einen __Idealitätsfaktor__ $n$ zu $e^{U/(n\,U_\text{T})}$, der Werte zwischen 1 und 2 annimmt.)

## Die Kennlinie und die Schleusenspannung

Trägt man den Strom über der Spannung auf, ergibt sich das typische „Knie". Wegen des exponentiellen Anstiegs
bleibt der Strom bis zu einer bestimmten Spannung praktisch null und schießt dann steil hoch. Diese praktische
Einsatzschwelle heißt __Schleusenspannung__ $U_\text{S}$:

| Material | Schleusenspannung $U_\text{S}$ |
|---|---|
| Silizium (Si) | $\approx 0{,}7\,\text{V}$ |
| Germanium (Ge) | $\approx 0{,}3\ldots0{,}5\,\text{V}$ |
| Schottky | $\approx 0{,}2\ldots0{,}4\,\text{V}$ |

Oberhalb der Schleusenspannung fällt über der leitenden Diode nur noch wenig mehr Spannung ab — für viele
Rechnungen nähert man sie deshalb als „leitet ab $0{,}7\,\text{V}$, sonst sperrt sie". In Sperrrichtung bleibt
der Strom bis zur __Durchbruchspannung__ winzig; überschreitet die Sperrspannung diesen Wert, bricht der Strom
schlagartig durch (bei normalen Dioden zerstörerisch, bei Z-Dioden gewollt — siehe unten).

:::grafik
Die $I$-$U$-Kennlinie der Diode: in Durchlassrichtung ein flacher Beginn und ab der Schleusenspannung
($\approx 0{,}7\,\text{V}$ bei Si) ein steiler exponentieller Anstieg; in Sperrrichtung nahezu null, bis bei der
Durchbruchspannung der Strom nach unten einbricht. Achsen und die drei Bereiche beschriftet.
:::

## Spezialdioden

Durch gezielte Bauform entstehen Dioden mit besonderen Eigenschaften:

- __Z-Diode__ (Zener-Diode): für den **Betrieb in Sperrrichtung** ausgelegt. Ihre Durchbruchspannung ist genau
  festgelegt; oberhalb davon hält sie die Spannung nahezu konstant — ideal als **Spannungsreferenz** oder zur
  Spannungsstabilisierung.
- __Leuchtdiode__ (LED): In Durchlassrichtung geben rekombinierende Elektron-Loch-Paare ihre Energie als
  **Licht** ab. Die Farbe hängt von der Bandlücke des Halbleiters ab.
- __Schottky-Diode__: ein Metall-Halbleiter-Übergang mit sehr kleiner Schleusenspannung und hoher
  Schaltgeschwindigkeit — für schnelle Schaltungen und geringe Verluste.
- __Photodiode__: nutzt den umgekehrten Effekt zur LED — einfallendes Licht erzeugt in Sperrrichtung einen
  messbaren Strom (Grundlage von Sensoren und Solarzellen).

:::grafik
Vier kleine Symbole mit Kurzbeschriftung: Z-Diode (Betrieb in Sperrrichtung, konstante Spannung), LED (Pfeile
nach außen = Licht), Schottky-Diode (kleines Knie), Photodiode (Pfeile nach innen = Licht). Darunter jeweils das
Stichwort zur Anwendung.
:::

:::kern
Die __Diode__ ist ein pn-Übergang als Ventil: In __Durchlassrichtung__ (Plus an der Anode) wird die
Raumladungszone schmal und der Strom fließt, in __Sperrrichtung__ wird sie breit und es bleibt nur ein winziger
__Sperrstrom__. Die __Shockley-Gleichung__ $I = I_\text{S}(e^{U/U_\text{T}} - 1)$ (mit $U_\text{T} \approx
26\,\text{mV}$) beschreibt beides; in Durchlass steigt der Strom __exponentiell__ ab der __Schleusenspannung__
(Si $\approx 0{,}7\,\text{V}$). Spezialdioden: __Z-Diode__ (Spannungsreferenz im Durchbruch), __LED__ (Licht),
__Schottky__ (schnell, kleine Schwelle), __Photodiode__ (Lichtsensor).
:::

Weil die Diodenkennlinie gekrümmt (nichtlinear) ist, kann man nicht einfach mit einem festen Widerstand rechnen.
Wie man trotzdem den Betriebspunkt einer Diode in einer Schaltung bestimmt, zeigt der nächste Abschnitt über den
__Arbeitspunkt__.

:::quiz
F: Warum leitet die Diode nur in eine Richtung?
A: Die äußere Spannung wirkt je nach Polung dem inneren Feld der Raumladungszone entgegen oder verstärkt es. In Durchlassrichtung schrumpft die Sperrschicht und Strom fließt, in Sperrrichtung wächst sie und blockiert — ein Ventil.
F: Was passiert mit der Raumladungszone in Durchlass- und in Sperrrichtung?
A: In Durchlassrichtung (Plus an der Anode) wird sie schmaler, bis die Träger sie überwinden; in Sperrrichtung (Plus an der Kathode) wird sie breiter und zieht freie Träger von der Grenze weg. Breite der Zone und Leitfähigkeit hängen also direkt zusammen.
F: Woher kommt der winzige Sperrstrom, obwohl die Diode „sperrt"?
A: Er wird von den wenigen Minoritätsträgern getragen, die thermisch ständig erzeugt werden. Das innere Feld saugt sie ab, sodass ein kleiner, nahezu konstanter Strom ($\approx I_S$) fließt.
F: Wie erklärt die Shockley-Gleichung beide Betriebsrichtungen zugleich?
A: Bei stark negativem $U$ geht $e^{U/U_T}$ gegen null und übrig bleibt $I\approx-I_S$ (Sperrstrom); bei positivem $U$ wächst der Exponentialterm extrem und der Strom steigt exponentiell. Ein einziger Ausdruck deckt Sperren und Leiten ab.
F: Warum ist die $-1$ in der Shockley-Gleichung in Durchlassrichtung bedeutungslos?
A: Schon bei einigen Zehntel Volt ist $e^{U/U_T}$ riesig gegenüber 1. Die $-1$ sorgt nur dafür, dass bei $U=0$ der Strom exakt null ist, spielt im Durchlass aber keine Rolle mehr.
F: Warum steigt der Durchlassstrom so steil an („Knie")?
A: Wegen der exponentiellen Abhängigkeit von der Spannung ändert sich der Strom über viele Größenordnungen in einem engen Spannungsbereich. Unterhalb der Schleusenspannung ist er praktisch null, darüber schießt er hoch.
F: Was ist die Schleusenspannung, und ist sie eine scharfe Grenze?
A: Sie ist die praktische Einsatzschwelle, ab der merklich Strom fließt (Si ≈ 0,7 V). Sie ist keine exakte physikalische Grenze, sondern eine Näherung des exponentiellen Knies für die Schaltungsrechnung.
F: Warum nähert man eine Si-Diode oft als „leitet ab 0,7 V, sonst sperrt"?
A: Oberhalb der Schleusenspannung ändert sich die Diodenspannung kaum noch, obwohl der Strom stark steigt. Diese fast konstante Durchlassspannung erlaubt die einfache Näherung einer idealen Schwelle.
F: Wie nutzt die Z-Diode den Durchbruch gezielt?
A: Sie wird bewusst in Sperrrichtung betrieben; oberhalb ihrer festgelegten Durchbruchspannung hält sie die Spannung nahezu konstant. Das macht sie zur Spannungsreferenz bzw. zur Stabilisierung — ein bei normalen Dioden zerstörerischer Effekt wird hier genutzt.
F: Warum sind LED und Photodiode gegensätzliche Nutzungen desselben pn-Übergangs?
A: In der LED geben rekombinierende Elektron-Loch-Paare in Durchlassrichtung Energie als Licht ab; in der Photodiode erzeugt einfallendes Licht in Sperrrichtung Ladungsträger und damit einen messbaren Strom. Einmal Strom → Licht, einmal Licht → Strom.
:::
