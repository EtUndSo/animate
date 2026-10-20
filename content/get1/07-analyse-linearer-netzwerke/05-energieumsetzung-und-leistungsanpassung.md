---
title: Energieumsetzung und Leistungsanpassung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70800
summary: Wie ein Widerstand elektrische Energie in Wärme umsetzt, bei welchem Lastwiderstand eine Quelle die größte Leistung abgibt und warum maximale Leistung ausgerechnet mit nur 50 % Wirkungsgrad erkauft wird.
tags: Leistung, Joulesche Wärme, Leistungsanpassung, maximale Leistung, Wirkungsgrad
---

:::konzept
Ein Widerstand verwandelt elektrische Energie in Wärme — das ist mal erwünscht (Heizung, Kochplatte) und mal
lästig (Verluste in Leitungen). Wie viel Leistung eine Quelle an einen Verbraucher abgibt, hängt vom
Lastwiderstand ab, und es gibt einen **optimalen Wert**: Die größte Leistung kommt beim Verbraucher an, wenn
sein Widerstand genau zum Innenwiderstand der Quelle passt. Der Haken dabei: In diesem Punkt geht die Hälfte der
Leistung in der Quelle selbst verloren.
:::

**Worum es geht:** Nachdem wir Netze analysieren können, kommt die energetische Frage. Wir klären, wie der
Widerstand __Energie umsetzt__, leiten die __Leistungsanpassung__ für maximale Leistung her und stellen ihr den
__Wirkungsgrad__ gegenüber — zwei Ziele, die sich widersprechen.

## Energieumsetzung im Widerstand

Fließt durch einen Widerstand ein Strom, stoßen die driftenden Elektronen ständig mit dem Gitter zusammen und
geben Energie ab — der Widerstand erwärmt sich. Die umgesetzte __Leistung__ ist

$$P = U \cdot I = I^2 \cdot R = \frac{U^2}{R}.$$

- __$P$__: die __Leistung__ (umgesetzte Energie pro Zeit), in Watt.
- __$U$__: die __Spannung__ am Widerstand.
- __$I$__: der __Strom__ durch den Widerstand.
- __$R$__: der __Widerstand__.

Die drei Formen sind über das Ohmsche Gesetz dieselbe Aussage, nur nach den jeweils bekannten Größen aufgelöst.
Diese in Wärme umgesetzte Leistung heißt __Joulesche Wärme__. Über eine Zeit $t$ ergibt sich die Energie
$W = P\cdot t$. Wichtig ist die **quadratische** Abhängigkeit: Doppelter Strom bedeutet vierfache Verlustleistung
— der Grund, warum man in der Energieübertragung den Strom klein (und die Spannung hoch) hält.

:::grafik
Ein Widerstand, durch den Strom $I$ fließt, mit Wärmewellen nach außen. Beschriftung $P = I^2 R$ und der Hinweis
„doppelter Strom → vierfache Wärme" zur quadratischen Abhängigkeit.
:::

## Leistungsanpassung: maximale Leistung an den Verbraucher

Eine reale Quelle (Leerlaufspannung $U_0$, Innenwiderstand $R_i$) speist einen Lastwiderstand $R_\text{L}$.
Welcher Lastwert holt die **größte** Leistung heraus?

**Schritt 1** — der Strom im Kreis folgt aus der Reihenschaltung: $I = \dfrac{U_0}{R_i + R_\text{L}}$.

**Schritt 2** — die am Verbraucher umgesetzte Leistung ist $P_\text{L} = I^2 R_\text{L}$, also

$$P_\text{L} = \frac{U_0^2 \cdot R_\text{L}}{(R_i + R_\text{L})^2}.$$

**Schritt 3** — diesen Ausdruck nach $R_\text{L}$ maximieren (Ableitung null setzen). Das Ergebnis ist die
__Anpassungsbedingung__:

$$R_\text{L} = R_i.$$

Der Verbraucher bekommt also die meiste Leistung, wenn sein Widerstand **gleich dem Innenwiderstand** der Quelle
ist. Setzt man das ein, ergibt sich die maximal übertragbare Leistung

$$P_\text{max} = \frac{U_0^2}{4\,R_i}.$$

- __$R_\text{L}$__: der __Lastwiderstand__ (der Verbraucher).
- __$R_i$__: der __Innenwiderstand__ der Quelle.
- __$P_\text{max}$__: die größtmögliche __Verbraucherleistung__.

Anschaulich ist das ein Kompromiss: Bei sehr kleinem $R_\text{L}$ fließt zwar viel Strom, aber es liegt kaum
Spannung an ihm an; bei sehr großem $R_\text{L}$ liegt viel Spannung an, aber es fließt kaum Strom. Dazwischen,
genau bei $R_\text{L} = R_i$, ist das Produkt $P = U\cdot I$ am größten.

:::grafik
Die Kurve $P_\text{L}$ über $R_\text{L}$: steigt von null an, erreicht ein deutliches Maximum bei
$R_\text{L} = R_i$ (dort $P_\text{max} = U_0^2/4R_i$ markiert) und fällt für große $R_\text{L}$ wieder langsam
ab.
:::

## Wirkungsgrad: warum maximale Leistung nicht maximale Effizienz ist

Die größte Leistung ist nicht dasselbe wie die sparsamste Übertragung. Der __Wirkungsgrad__ ist der Anteil der
Nutzleistung an der gesamten von der Quelle aufgebrachten Leistung:

$$\eta = \frac{P_\text{L}}{P_\text{ges}} = \frac{R_\text{L}}{R_i + R_\text{L}}.$$

Setzt man die Anpassungsbedingung $R_\text{L} = R_i$ ein, ergibt sich

$$\eta = \frac{R_i}{R_i + R_i} = \frac{1}{2} = 50\,\%.$$

Im Punkt maximaler Leistung geht also die **Hälfte** der Energie als Joulesche Wärme im Innenwiderstand der
Quelle verloren — genauso viel, wie beim Verbraucher ankommt. Das ist der entscheidende Gegensatz: Für die
Energieübertragung (Kraftwerk, Netzteil) will man einen hohen Wirkungsgrad und wählt $R_\text{L} \gg R_i$; dann
sinkt zwar die absolute Leistung, aber fast alles kommt beim Verbraucher an. Die __Leistungsanpassung__
($R_\text{L} = R_i$) nutzt man dagegen dort, wo es auf die **maximale** Leistung ankommt und die Verluste eine
Nebenrolle spielen — etwa bei schwachen Signalen in der Nachrichten- und Messtechnik.

:::grafik
Zwei Kurven über $R_\text{L}/R_i$ in einem Diagramm: die Verbraucherleistung $P_\text{L}$ (Maximum bei
$R_\text{L}/R_i = 1$) und der Wirkungsgrad $\eta$ (steigt monoton gegen 100 %). Am Schnittpunkt-Bereich
hervorgehoben: bei der Anpassung ist $\eta$ erst 50 %.
:::

:::kern
Ein Widerstand setzt die __Leistung__ $P = UI = I^2R = U^2/R$ in __Joulesche Wärme__ um (quadratisch im Strom!).
Eine Quelle gibt die **größte** Leistung ab, wenn der Lastwiderstand ihrem Innenwiderstand gleicht
(__Leistungsanpassung__ $R_\text{L} = R_i$, $P_\text{max} = U_0^2/4R_i$). Dabei ist der __Wirkungsgrad__ aber nur
$\eta = R_\text{L}/(R_i+R_\text{L}) = 50\,\%$. Für hohe Effizienz wählt man dagegen $R_\text{L} \gg R_i$ —
maximale Leistung und maximaler Wirkungsgrad schließen sich aus.
:::

Bleibt ein letzter, allgemeinerer Baustein: Bauteile mit **vier** Anschlüssen, die ein Eingangs- mit einem
Ausgangstor verknüpfen — die __Zweitore__.

:::quiz
F: Warum erwärmt sich ein stromdurchflossener Widerstand?
A: Die driftenden Elektronen stoßen ständig mit den Gitterbausteinen zusammen und geben dabei Bewegungsenergie ab. Diese Energie erscheint als Wärme — die Joulesche Wärme.
F: Warum sind $P=UI$, $P=I^2R$ und $P=U^2/R$ dieselbe Aussage?
A: Sie entstehen auseinander durch Einsetzen des Ohmschen Gesetzes $U=RI$. Man wählt die Form, in der die gerade bekannten Größen stehen.
F: Warum hält man in der Energieübertragung den Strom klein und die Spannung hoch?
A: Die Verlustleistung in den Leitungen ist $I^2R$, also quadratisch im Strom — halber Strom bedeutet nur ein Viertel Verlust. Dieselbe Leistung $P=UI$ überträgt man daher lieber mit hoher Spannung und kleinem Strom.
F: Warum gibt es überhaupt einen optimalen Lastwiderstand für maximale Leistung?
A: Bei kleinem $R_L$ fließt viel Strom, aber es liegt kaum Spannung an; bei großem $R_L$ ist es umgekehrt. Das Produkt $P=UI$ ist dazwischen maximal — bei $R_L=R_i$.
F: Wie leitet man die Anpassungsbedingung $R_L=R_i$ her?
A: Man schreibt $P_L=U_0^2 R_L/(R_i+R_L)^2$ und maximiert nach $R_L$, indem man die Ableitung null setzt. Das liefert als Optimum $R_L=R_i$.
F: Wie groß ist die maximal übertragbare Leistung?
A: Setzt man $R_L=R_i$ ein, ergibt sich $P_\text{max}=U_0^2/(4R_i)$. Mehr als dieses Viertel von $U_0^2/R_i$ kann die Quelle an keinen Verbraucher abgeben.
F: Warum ist der Wirkungsgrad bei Leistungsanpassung nur 50 %?
A: Bei $R_L=R_i$ sind Last- und Innenwiderstand gleich, sodass in beiden gleich viel Leistung umgesetzt wird. Die Hälfte geht als Wärme im Innenwiderstand der Quelle verloren, $\eta=R_L/(R_i+R_L)=1/2$.
F: Warum schließen sich maximale Leistung und maximaler Wirkungsgrad aus?
A: Maximale Leistung verlangt $R_L=R_i$ (η = 50 %), hoher Wirkungsgrad dagegen $R_L\gg R_i$. Je effizienter man überträgt, desto kleiner wird die absolute Leistung — beide Ziele liegen auf entgegengesetzten Seiten des Optimums.
F: Wann wählt man Leistungsanpassung, wann hohen Wirkungsgrad?
A: Anpassung ($R_L=R_i$) nutzt man, wo es auf die maximale Leistung ankommt und Verluste zweitrangig sind — etwa bei schwachen Signalen in der Nachrichten- und Messtechnik. Hoher Wirkungsgrad ($R_L\gg R_i$) gilt der Energieübertragung in Kraftwerk und Netzteil.
F: Was bedeutet die quadratische Stromabhängigkeit der Leistung für einen verdoppelten Strom?
A: Bei doppeltem Strom vervierfacht sich die umgesetzte Leistung ($P\propto I^2$). Deshalb steigen Verluste und Erwärmung überproportional, wenn der Strom wächst.
:::
