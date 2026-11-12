---
title: Stufe 7: Quellen zusammenschalten
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150900
summary: Oft reicht eine Quelle nicht.
tags: Ausgleichsstrom
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Oft reicht eine Quelle nicht. Reihenschaltung erhöht die Spannung, Parallelschaltung den Strom. Diese Stufe rechnet beides aus und nennt die Gefahr.
:::

**Die Idee.** In Reihe fließt durch beide Quellen derselbe Strom, ihre Klemmenspannungen addieren sich bei jedem Strom. Parallel liegt an beiden dieselbe Spannung, ihre Ströme addieren sich bei jeder Spannung. Für die Reihe rechnet man deshalb in der Spannungsquellenform, für die Parallelschaltung in der Stromquellenform. Aus zwei Geraden wird dabei wieder eine Gerade, also wieder eine reale Quelle.

:::satz Satz 7.1 (Zusammenschalten realer Quellen)
<span class="anker" id="satz-7-1"></span>

Zwei Quellen in Reihe beziehungsweise parallel wirken wie eine:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2},\quad R_\mathrm{ers}=R_\mathrm{q1}+R_\mathrm{q2} \qquad\text{bzw.}\qquad I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2},\quad G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}. \tag{7.1}$$

Für die Parallelschaltung heißt das in Spannungsquellenform

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{ers}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}},\qquad R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}. \tag{7.2}$$
:::

⁠**So liest man das:** Die Spannung in [(7.2)](#gl-7-2) ist ein gewichteter Mittelwert, die niederohmigere Quelle zählt stärker. Zwei gleiche Quellen ergeben parallel $U_\mathrm{q}$ und $R_\mathrm{q}/2$, in Reihe $2U_\mathrm{q}$ und $2R_\mathrm{q}$. **Gültigkeit:** Reihenschaltungen von Spannungsquellen und Parallelschaltungen von Stromquellen sind technisch unkritisch. Parallele Spannungsquellen brauchen gleiche Spannungen oder genügend Innenwiderstand: Bei $U_\mathrm{q1}\neq U_\mathrm{q2}$ kreist schon ohne Last ein __Ausgleichsstrom__

<span class="anker" id="gl-7-3"></span>
$$I_\mathrm{ausgl}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}. \tag{7.3}$$

Er läuft aus der stärkeren Quelle in die schwächere hinein. Zwei ideale Spannungsquellen mit verschiedenen Spannungen darf man nicht parallel schalten, zwei ideale Stromquellen mit verschiedenen Strömen nicht in Reihe: Das Modell hat dann keine Lösung.

:::herleitung Parallel in der Stromquellenform
Beide Quellen haben die Spannung $U_\mathrm{AB}$, die Knotenregel addiert ihre Ströme: $I_\mathrm{A}=(I_\mathrm{q1}-G_\mathrm{q1}U_\mathrm{AB})+(I_\mathrm{q2}-G_\mathrm{q2}U_\mathrm{AB})=(I_\mathrm{q1}+I_\mathrm{q2})-(G_\mathrm{q1}+G_\mathrm{q2})U_\mathrm{AB}$. Das ist wieder die Form aus [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1). Mit [(6.1)](spannungsquelle-oder-stromquelle.html#gl-6-1) folgt daraus [(7.2)](#gl-7-2). In der Reihe addiert die Maschenregel entsprechend die Spannungen. Der Ausgleichsstrom ist die Umlaufspannung $U_\mathrm{q1}-U_\mathrm{q2}$ durch den Widerstand des Umlaufs.
:::

:::abbildung et1/k5zusammen 8
Links zwei gleiche Batterien parallel. Rechts die Kennlinien: Parallel bleibt die Leerlaufspannung, der Kurzschlussstrom verdoppelt sich. In Reihe verdoppelt sich die Leerlaufspannung, der Kurzschlussstrom bleibt. Die Punkte zeigen die Arbeitspunkte an 16 $\Omega$.
:::

::::beispiel
Zwei Batterien aus dem Rechenmodell. Parallel: 9 V, 1 $\Omega$, $I_\mathrm{KS}=9$ A. Stromform zur Kontrolle: $4{,}5+4{,}5=9$ A und $0{,}5+0{,}5=1$ S. In Reihe: 18 V, 4 $\Omega$, $I_\mathrm{KS}=4{,}5$ A. An 16 $\Omega$ liefert die Parallelschaltung 8,47 V und 0,529 A, die Reihenschaltung 14,4 V und 0,9 A (Abb. [8](#abb-8)). Die Parallelschaltung bringt hier wenig, weil 2 $\Omega$ klein gegen 16 $\Omega$ sind.

Ist eine der Batterien auf 8 V entladen, kreisen nach [(7.3)](#gl-7-3) im Leerlauf $1\,\mathrm{V}/4\,\Omega=0{,}25$ A. Beide Klemmen stehen auf 8,5 V, auch nach [(7.2)](#gl-7-2).
::::

⁠**Grenzfall:** Mit nur je 10 m$\Omega$ Innenwiderstand wären es 50 A. Darum schaltet man große Akkuzellen nur mit gleicher Spannung parallel. Für $U_\mathrm{q1}=U_\mathrm{q2}$ verschwindet der Ausgleichsstrom.

:::frage Bringen zwei parallele Batterien mehr Spannung?
Im Leerlauf nein, beide liefern 9 V. Unter Last ein wenig, denn der Strom teilt sich auf zwei Innenwiderstände auf und innen fällt nur die Hälfte ab. Der eigentliche Gewinn ist ein doppelt so großer Kurzschlussstrom und die doppelte Ladungsmenge.
:::

:::aufgabe Aufgabe 8 ★★ Alter und neuer Akku
<span class="anker" id="aufg-8"></span>

Ein neuer Akku (12,6 V, 0,1 $\Omega$) wird zu einem alten (11,8 V, 0,3 $\Omega$) parallel geschaltet. (a) Wie groß ist der Ausgleichsstrom? Welche Ersatzquelle ergibt sich? (b) Eine Last zieht 10 A. Welche Spannung stellt sich ein, und was liefert jeder Akku? (c) Ab welchem Laststrom liefert der alte Akku überhaupt Strom? Was passiert darunter?

:::loesung
(a) $I_\mathrm{ausgl}=\frac{0{,}8\,\mathrm{V}}{0{,}4\,\Omega}=2$ A. $U_\mathrm{ers}=\frac{10\,\mathrm{S}\cdot12{,}6\,\mathrm{V}+3{,}33\,\mathrm{S}\cdot11{,}8\,\mathrm{V}}{13{,}33\,\mathrm{S}}=12{,}4$ V, $R_\mathrm{ers}=0{,}1\,\Omega\parallel0{,}3\,\Omega=75$ m$\Omega$. Probe: $12{,}6\,\mathrm{V}-0{,}1\,\Omega\cdot2\,\mathrm{A}=12{,}4$ V.

(b) $U=12{,}4\,\mathrm{V}-75\,\mathrm{m\Omega}\cdot10\,\mathrm{A}=11{,}65$ V. Neu: $\frac{12{,}6-11{,}65}{0{,}1}\,\mathrm{A}=9{,}5$ A. Alt: $\frac{11{,}8-11{,}65}{0{,}3}\,\mathrm{A}=0{,}5$ A. Summe 10 A.

(c) Der alte Akku liefert erst, wenn $U<11{,}8$ V ist, also für $I_\mathrm{L}>\frac{12{,}4-11{,}8}{0{,}075}\,\mathrm{A}=8$ A. Darunter fließt Strom in ihn hinein, und der neue Akku lädt ihn.
:::
:::

::::formelsammlung
**Quellen in Reihe**

$$U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2},\quad R_\mathrm{ers}=R_\mathrm{q1}+R_\mathrm{q2}$$

Derselbe Strom durch beide, die Klemmenspannungen addieren sich (Spannungsquellenform). Zwei gleiche Quellen ergeben $2U_\mathrm{q}$ und $2R_\mathrm{q}$. Zwei ideale Stromquellen mit verschiedenen Strömen darf man nicht in Reihe schalten.

**Quellen parallel, Stromquellenform**

$$I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2},\quad G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$$

Dieselbe Spannung an beiden, die Ströme addieren sich (Knotenregel).

**Quellen parallel, Spannungsquellenform**

$$U_\mathrm{ers}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}},\qquad R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$$

Gewichteter Mittelwert, die niederohmigere Quelle zählt stärker. Zwei gleiche Quellen ergeben $U_\mathrm{q}$ und $R_\mathrm{q}/2$. Zwei ideale Spannungsquellen mit verschiedenen Spannungen darf man nicht parallel schalten.

**Ausgleichsstrom**

$$I_\mathrm{ausgl}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}$$

Kreist bei parallelen Spannungsquellen mit $U_\mathrm{q1}\neq U_\mathrm{q2}$ schon ohne Last, aus der stärkeren in die schwächere Quelle: Umlaufspannung durch den Widerstand des Umlaufs. Mit je 10 m$\Omega$ Innenwiderstand ergibt 1 V Differenz 50 A.
::::

::::lernkarten
:::karte zusammenhang Quellen in Reihe und parallel
Warum rechnet man Quellen in Reihe in der Spannungsquellenform und parallele Quellen in der Stromquellenform?
---
In Reihe fließt durch beide derselbe Strom, die Klemmenspannungen addieren sich bei jedem Strom. Parallel liegt an beiden dieselbe Spannung, die Ströme addieren sich bei jeder Spannung. Aus zwei Geraden wird wieder eine Gerade.
--- falsch
Weil nur Spannungsquellen in Reihe und nur Stromquellen parallel geschaltet werden dürfen. Die jeweils andere Form ergäbe keine reale Quelle mehr, sondern eine gekrümmte Kennlinie, die man nicht mit zwei Zahlen beschreiben kann.
--- falsch
In Reihe liegt an beiden dieselbe Spannung, und ihre Ströme addieren sich. Parallel fließt durch beide derselbe Strom, und ihre Spannungen addieren sich. Das Ergebnis ist deshalb keine Gerade mehr, sondern eine Kurve.
--- falsch
Weil die Rechnung in der anderen Form ein anderes Ergebnis lieferte. Die Wahl der Form legt fest, welche Quelle entsteht, und muss deshalb zur Bauart der Quellen passen.
:::
:::karte formel Quellen in Reihe
Welche Ersatzquelle bilden zwei reale Spannungsquellen, die in Reihe geschaltet sind?
---
$U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2}$ und $R_\mathrm{ers}=R_\mathrm{q1}+R_\mathrm{q2}$. Zwei gleiche Quellen ergeben in Reihe $2U_\mathrm{q}$ und $2R_\mathrm{q}$.
--- falsch
$U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2}$ und $R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$. Zwei gleiche Quellen ergeben in Reihe $2U_\mathrm{q}$ und $R_\mathrm{q}/2$.
--- falsch
$U_\mathrm{ers}=\frac12(U_\mathrm{q1}+U_\mathrm{q2})$ und $R_\mathrm{ers}=R_\mathrm{q1}+R_\mathrm{q2}$. Zwei gleiche Quellen ergeben in Reihe $U_\mathrm{q}$ und $2R_\mathrm{q}$.
--- falsch
$U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2}$ und $R_\mathrm{ers}=R_\mathrm{q1}$, weil der Strom nur einen Innenwiderstand durchläuft. Zwei gleiche Quellen ergeben $2U_\mathrm{q}$ und $R_\mathrm{q}$.
:::
:::karte formel Quellen parallel
Welche Ersatzquelle bilden zwei reale Quellen parallel, in der Stromquellenform und in der Spannungsquellenform geschrieben?
---
$I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2}$ und $G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$, also $U_\mathrm{ers}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}}$ und $R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$: ein gewichteter Mittelwert, die niederohmigere Quelle zählt stärker.
--- falsch
$I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2}$ und $G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$, also $U_\mathrm{ers}=U_\mathrm{q1}+U_\mathrm{q2}$ und $R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$. Parallel addieren sich Ströme und Spannungen zugleich, wie bei Batterien in Reihe.
--- falsch
$I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2}$ und $G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$, also $U_\mathrm{ers}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}}$ und $R_\mathrm{ers}=R_\mathrm{q1}+R_\mathrm{q2}$. Die hochohmigere Quelle zählt dabei stärker, weil an ihr mehr Spannung abfällt.
--- falsch
$I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2}$ und $G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$, also $U_\mathrm{ers}=\frac12(U_\mathrm{q1}+U_\mathrm{q2})$ und $R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$. Die Spannung ist stets der einfache Mittelwert.
:::
:::karte herleitung Parallel in der Stromquellenform
Leite aus der Knotenregel her, welche Ersatzquelle zwei parallel geschaltete reale Quellen bilden.
---
Beide Quellen haben dieselbe Spannung $U_\mathrm{AB}$, weil sie an denselben zwei Klemmen hängen.
---
Die Knotenregel addiert ihre Ströme: $I_\mathrm{A}=(I_\mathrm{q1}-G_\mathrm{q1}U_\mathrm{AB})+(I_\mathrm{q2}-G_\mathrm{q2}U_\mathrm{AB})$, weil jede Quelle in der Stromquellenform $I_\mathrm{q}-G_\mathrm{q}U_\mathrm{AB}$ nach außen liefert.
---
Zusammengefasst ist $I_\mathrm{A}=(I_\mathrm{q1}+I_\mathrm{q2})-(G_\mathrm{q1}+G_\mathrm{q2})U_\mathrm{AB}$, weil man die Glieder ohne und mit $U_\mathrm{AB}$ sammelt; das ist wieder eine reale Stromquelle mit $I_\mathrm{ers}=I_\mathrm{q1}+I_\mathrm{q2}$ und $G_\mathrm{ers}=G_\mathrm{q1}+G_\mathrm{q2}$.
---
Mit den Bedingungen der Äquivalenz folgen $U_\mathrm{ers}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}}$ und $R_\mathrm{ers}=R_\mathrm{q1}\parallel R_\mathrm{q2}$, weil die Ersatzspannung der Gesamtstrom durch den Gesamtleitwert ist und jeder Quellenstrom das Produkt aus Leitwert und Quellenspannung.
:::
:::karte begriff Ausgleichsstrom
Was ist der Ausgleichsstrom zweier parallel geschalteter realer Spannungsquellen, und wie groß ist er?
---
Der Strom, der bei $U_\mathrm{q1}\neq U_\mathrm{q2}$ schon ohne Last durch beide Quellen kreist: $I_\mathrm{ausgl}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}$. Er läuft aus der stärkeren Quelle in die schwächere hinein.
--- falsch
Der Strom, der erst unter Last fließt und die Last gleichmäßig auf beide Quellen verteilt: $I_\mathrm{ausgl}=\frac{U_\mathrm{q1}+U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}$. Ohne Last ist er null, gleich welche Spannungen die Quellen haben.
--- falsch
Der Strom, der bei ungleichen Spannungen ohne Last kreist: $I_\mathrm{ausgl}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}\parallel R_\mathrm{q2}}$, weil die Innenwiderstände parallel liegen. Er läuft aus der schwächeren Quelle in die stärkere.
--- falsch
Der Strom, der bei ungleichen Spannungen ohne Last kreist: $I_\mathrm{ausgl}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}$. Er ist harmlos, weil er die Klemmenspannung nicht verändert und keine Energie umsetzt.
:::
:::karte zusammenhang Große Akkuzellen parallel
Warum schaltet man große Akkuzellen nur mit gleicher Spannung parallel?
---
Ihr Innenwiderstand ist sehr klein, deshalb wird der Ausgleichsstrom schon bei kleiner Spannungsdifferenz groß: 1 V Differenz bei je 10 m$\Omega$ ergibt 50 A. Für $U_\mathrm{q1}=U_\mathrm{q2}$ verschwindet der Ausgleichsstrom.
--- falsch
Weil sich sonst ihre Spannungen addieren und die Last eine zu hohe Spannung erhält. Bei gleichen Spannungen bleibt die Klemmenspannung beim Wert einer einzelnen Zelle, wie die Last es erwartet, und nur so passen die Zellen zusammen.
--- falsch
Weil ihr Innenwiderstand groß ist und der Ausgleichsstrom deshalb lange kreist: Bei 1 V Differenz fließen über Stunden einige Milliampere, die beide Zellen nach und nach entladen, ohne Gefahr.
--- falsch
Weil die Zelle mit der kleineren Spannung sonst keinen Strom an die Last abgeben kann und ungenutzt bleibt. Gefährlich ist eine solche Schaltung dagegen nicht.
:::
:::karte zusammenhang Unmögliche Zusammenschaltungen
Für welche Zusammenschaltungen idealer Quellen hat das Modell keine Lösung, und warum?
---
Zwei ideale Spannungsquellen mit verschiedenen Spannungen parallel: Beide wollen die Spannung zwischen denselben Knoten festlegen. Zwei ideale Stromquellen mit verschiedenen Strömen in Reihe: Beide wollen den Strom desselben Zweigs festlegen.
--- falsch
Zwei ideale Spannungsquellen in Reihe und zwei ideale Stromquellen parallel: Dort addieren sich die festgehaltenen Größen ohne Grenze, und das Modell liefert unendliche Spannungen und Ströme, die kein Netz aufnehmen kann.
--- falsch
Jede Parallelschaltung von Quellen, auch mit gleichen Werten: Parallel geschaltete Quellen widersprechen sich immer, weil an denselben Knoten zwei Größen festgelegt werden.
--- falsch
Zwei ideale Spannungsquellen mit verschiedenen Spannungen in Reihe: Beide wollen den Strom im gemeinsamen Zweig festlegen, und die beiden Ströme passen nicht zusammen. Parallel geschaltet wären sie dagegen unproblematisch, weil sich ihre Ströme dann einfach teilen.
:::
:::karte zusammenhang Zwei Batterien parallel
Bringen zwei gleiche parallel geschaltete Batterien mehr Spannung als eine einzelne?
---
Im Leerlauf nein, beide liefern 9 V. Unter Last ein wenig, weil sich der Strom auf zwei Innenwiderstände aufteilt und innen nur die Hälfte abfällt. Der Gewinn ist vor allem der doppelte Kurzschlussstrom und die doppelte Ladungsmenge.
--- falsch
Ja, parallel addieren sich die Spannungen wie in Reihe: Zwei 9-V-Batterien liefern 18 V, aber nur den halben Strom einer einzelnen, weil sich der Strom auf beide aufteilt. Die Ladungsmenge bleibt dieselbe wie bei einer Batterie.
--- falsch
Nein, unter Last sogar weniger, weil die beiden Innenwiderstände sich addieren und der innere Abfall deshalb doppelt so groß wird wie bei einer einzelnen Batterie.
--- falsch
Im Leerlauf nein, unter Last auch nicht: Die Klemmenspannung ist bei jeder Last dieselbe wie bei einer einzelnen Batterie, weil jeder Innenwiderstand den vollen Strom führt. Gewonnen wird allein die doppelte Ladungsmenge.
:::
:::karte zusammenhang Alter und neuer Akku
Was geschieht, wenn ein alter Akku (11,8 V, 0,3 $\Omega$) parallel zu einem neuen (12,6 V, 0,1 $\Omega$) liegt und die Last nur wenig Strom zieht?
---
Der alte Akku liefert erst, wenn die Klemmenspannung unter 11,8 V fällt, hier ab 8 A Laststrom. Darunter fließt Strom in ihn hinein, und der neue Akku lädt ihn.
--- falsch
Beide liefern je die Hälfte des Laststroms, weil parallele Quellen den Strom immer gleichmäßig aufteilen, gleich wie alt sie sind.
--- falsch
Der alte Akku liefert den größeren Teil, weil sein Innenwiderstand größer ist und er deshalb mehr Spannung an den Klemmen bereitstellt als der neue.
--- falsch
Der alte Akku ist vom Kreis getrennt, solange die Last wenig zieht. Strom fließt durch ihn erst, wenn der neue Akku ganz leer ist und seine Spannung verloren hat.
:::
::::
