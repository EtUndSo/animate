---
title: Stufe 1: Größen, Kraft und Arbeit
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110300
summary: Spannung wird sich als Arbeit je Ladung erweisen.
tags: qualitativ, quantitativ, ohmsche Gesetz, physikalische Größe, SI-Einheitensystem, Basisgrößen, Strom, SI-Vorsätze
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Spannung wird sich als Arbeit je Ladung erweisen. Dafür braucht man Größen mit Einheiten, die Kraft, die Arbeit und die Bewegungsenergie.
:::

**Die Idee.** Wer aus dem Schnee kommt, nennt einen Raum warm, wer aus der Sauna kommt, kühl. Solche Urteile sind __qualitativ__. Ein Thermometer zeigt beiden 21 °C, das ist __quantitativ__: eine Zahl mit Maßstab, unabhängig davon, wer misst. Mit solchen Größen formuliert die Physik ihre Gesetze, zum Beispiel das __ohmsche Gesetz__ $U=R\cdot I$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Die wichtigste mechanische Größe dieses Kapitels ist die Arbeit: Eine Kraft, die längs eines Wegs wirkt, überträgt Energie, und es zählt nur ihr Anteil in Wegrichtung. Wer einen Rucksack hebt, arbeitet gegen die Schwerkraft, wer ihn waagerecht trägt, nicht (Abb. [2](#abb-2)).

:::definition Definition 1.1 (Physikalische Größe)
<span class="anker" id="satz-1-1"></span>

Eine __physikalische Größe__ ist eine messbare Eigenschaft, das Produkt aus Zahlenwert und Einheit:

<span class="anker" id="gl-1-1"></span>
$$\text{Größe}=\text{Zahlenwert}\cdot\text{Einheit}. \tag{1.1}$$
:::

⁠**So liest man das:** In $U=9$ V ist $U$ das Formelzeichen (kursiv), 9 der Zahlenwert, V die Einheit (aufrecht). Eckige Klammern fragen nach der Einheit: $[U]=\mathrm V$. Der Zahlenwert hängt von der Einheit ab, die Größe nicht: 72 km/h und 20 m/s sind dieselbe Geschwindigkeit.

**Einheiten.** Das __SI-Einheitensystem__ kennt sieben __Basisgrößen__, die sich nicht durcheinander ausdrücken lassen: Länge (Meter, m), Masse (Kilogramm, kg), Zeit (Sekunde, s), Stromstärke (Ampere, A), absolute Temperatur (Kelvin, K), Lichtstärke (Candela, cd) und Stoffmenge (Mol, mol). Ihre Definitionen werden mit der Messtechnik weiterentwickelt. Die Einheiten aller anderen Größen sind Produkte von Potenzen der Basiseinheiten. Ein elektrischer __Strom__ ist bewegte Ladung, ein Ampere transportiert je Sekunde ein Coulomb. Die Leistung ist Energie je Zeit. Für dieses Kapitel genügen:

| Größe | Einheit | in Basiseinheiten | auch |
|---|---|---|---|
| Kraft $F$ | Newton, N | $\mathrm{kg\,m/s^2}$ | $\mathrm{J/m}$ |
| Energie, Arbeit $W$ | Joule, J | $\mathrm{kg\,m^2/s^2}$ | $\mathrm{N\,m}=\mathrm{W\,s}$ |
| Leistung $P$ | Watt, W | $\mathrm{kg\,m^2/s^3}$ | $\mathrm{V\,A}$ |
| Ladung $Q$ | Coulomb, C | $\mathrm{A\,s}$ |  |
| Spannung $U$ | Volt, V | $\mathrm{kg\,m^2/(s^3\,A)}$ | $\mathrm{J/C}$ |

__SI-Vorsätze__ skalieren einen Zahlenwert um Zehnerpotenzen. Vielfache schreibt man groß, Teile klein, nur Deka, Hekto und Kilo weichen aus historischen Gründen ab. Es steht immer nur ein Vorsatz vor einer Einheit, und er bildet mit ihr ein einziges Symbol.

| Vorsatz | Potenz | in Worten | Vorsatz | Potenz | in Worten |
|---|---|---|---|---|---|
| Atto, a | $10^{-18}$ | Trillionstel | Exa, E | $10^{18}$ | Trillion |
| Femto, f | $10^{-15}$ | Billiardstel | Peta, P | $10^{15}$ | Billiarde |
| Piko, p | $10^{-12}$ | Billionstel | Tera, T | $10^{12}$ | Billion |
| Nano, n | $10^{-9}$ | Milliardstel | Giga, G | $10^{9}$ | Milliarde |
| Mikro, µ | $10^{-6}$ | Millionstel | Mega, M | $10^{6}$ | Million |
| Milli, m | $10^{-3}$ | Tausendstel | Kilo, k | $10^{3}$ | Tausend |
| Zenti, c | $10^{-2}$ | Hundertstel | Hekto, h | $10^{2}$ | Hundert |
| Dezi, d | $10^{-1}$ | Zehntel | Deka, da | $10^{1}$ | Zehn |

**Rechnen mit Einheiten.**

<ol>

<li>

⁠**Addieren** darf man nur Größen derselben Einheit, Vorsätze gleicht man vorher an: $2\,\mathrm{kV}+40\,\mathrm{V}=2{,}04\,\mathrm{kV}$, nicht 42 kV. Verschiedene Einheiten in einer Summe verraten fast immer einen Rechenfehler.

</li>

<li>

⁠**Multiplizieren** darf man immer. Zahlenwerte, Einheiten und Vorsätze werden getrennt multipliziert, in Brüchen kürzen sich Einheiten wie Zahlen: $\frac{6\,\mathrm{N\,m}}{3\,\mathrm{m}}=2\,\mathrm{N}$, $0{,}5\,\mathrm{A}\cdot9\,\mathrm{V}=4{,}5\,\mathrm{W}$, $\mathrm{k\cdot M}=\mathrm G$, $\mu\text{}\cdot\mathrm M=1$. Im Rechenmodell ist $9\,\mathrm{V}/3\,\mathrm{mm}=3000\,\mathrm{V/m}=3\,\mathrm{kV/m}$.

</li>

<li>

⁠**Umrechnen** braucht manchmal einen Vorfaktor: $1\,\mathrm{Wh}=3600\,\mathrm{W\,s}$, $1\,\mathrm{km/h}=\frac{1}{3{,}6}\,\mathrm{m/s}$. Weil Vorsatz und Einheit ein Symbol sind, ist $1\,\mathrm{km^2}=(1000\,\mathrm{m})^2=10^6\,\mathrm{m^2}$, nicht 1000 m$^2$.

</li>

<li>

⁠**Die Größe entscheidet über die Einheit.** Energie schreibt man je nach Gebiet in W s, N m oder J. Gleiche Basiseinheiten beweisen aber keine gleiche Größe: Hertz (Schwingungen je Sekunde) und Becquerel (Zerfälle je Sekunde) sind beide $1/\mathrm s$, und N m ist auch das Drehmoment (Kraft mal Hebelarm).

</li>

</ol>

**Kraft und Arbeit.** Eine __Kraft__ verformt einen festgehaltenen Körper oder beschleunigt einen beweglichen. __Energie__ ist die Fähigkeit, Arbeit zu verrichten. Kraft und Weg sind __Vektoren__: Größen mit Betrag und Richtung, geschrieben mit Pfeil, $\vec F$. Die __Geschwindigkeit__ ist die Änderung des Wegs je Zeit, $v=\mathrm{d} s/\mathrm{d} t$, die __Beschleunigung__ die Änderung der Geschwindigkeit je Zeit, $a=\mathrm{d} v/\mathrm{d} t$.

:::definition Definition 1.2 (Kraft und Arbeit)
<span class="anker" id="satz-1-2"></span>

Die Kraft auf einen Körper mit Masse $m$ und Beschleunigung $a$ und die Kraft zwischen zwei Massen $m$, $M$ im Abstand $r$ sind

<span class="anker" id="gl-1-2"></span>
$$F=m\,a,\qquad F=\gamma\,\frac{m\,M}{r^2}. \tag{1.2}$$

Die __Arbeit__ einer Kraft längs eines Wegs ist

<span class="anker" id="gl-1-3"></span>
$$\Delta W=\vec F\cdot\Delta\vec s=F\,\Delta s\cos\alpha,\qquad W=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s. \tag{1.3}$$
:::

:::satz Satz 1.3 (Konstante Beschleunigung und Bewegungsenergie)
<span class="anker" id="satz-1-3"></span>

Mit den Startwerten $s_0$ und $v_0$ bei $t=0$ gilt für konstantes $a$

<span class="anker" id="gl-1-4"></span>
$$v(t)=v_0+a\,t,\qquad s(t)=s_0+v_0\,t+\tfrac12a\,t^2. \tag{1.4}$$

Ein Körper der Geschwindigkeit $v$ trägt die __Bewegungsenergie__ $W_\mathrm{kin}=\frac12m\,v^2$.
:::

⁠**So liest man das:** $[F]=\mathrm N$, auf 100 g wirkt an der Erdoberfläche rund 1 N. $\gamma=6{,}674\cdot10^{-11}\,\mathrm{N\,m^2/kg^2}$ ist die __Gravitationskonstante__. $\alpha$ ist der Winkel zwischen Kraft und Wegstück. Das Produkt $\vec F\cdot\Delta\vec s$ heißt __Skalarprodukt__, sein Ergebnis ist eine Zahl. Das Integral heißt __Linienintegral__: Man zerlegt den Weg in kurze gerade Stücke und summiert ihre Beiträge. $[W]=\mathrm J$, ein Joule hebt 102 g um einen Meter. Für $\alpha<90^\circ$ gibt die Kraft Energie an den Körper ab, für $\alpha>90^\circ$ entzieht sie ihm welche. **Gültigkeit:** [(1.4)](#gl-1-4) gilt nur für konstante Beschleunigung, Stufe [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9) braucht genau diesen Fall.

:::herleitung Bewegungsenergie
Aus [(1.4)](#gl-1-4) mit $v_0=0$ und $s_0=0$ folgt $t=v/a$ und $s=\frac12a\,t^2=v^2/(2a)$. Eine konstante Kraft $F=m\,a$ verrichtet auf diesem Weg die Arbeit $F\,s=m\,a\,v^2/(2a)=\frac12m\,v^2$.
:::

:::abbildung et1/k1wegarbeit 2
Ein Rucksack mit 2 kg wird von A nach B gebracht, 8 m zur Seite und 6 m hinauf. Auf der Treppe zählen nur die roten Stücke, zusammen 6 m. Auf der Rampe ist der Weg 10 m lang und $\cos\alpha=0{,}6$. Beide Wege ergeben 117,7 J.
:::

::::beispiel
Auf den Rucksack wirkt die __Gewichtskraft__ $F_\mathrm{G}=m\,g=19{,}62\,\mathrm{N}$. Um ihn gleichmäßig zu heben, bringt die Hand dieselbe Kraft nach oben auf. Über die Treppe ist $W=19{,}62\,\mathrm{N}\cdot6\,\mathrm{m}=117{,}7\,\mathrm{J}$, über die Rampe $W=19{,}62\,\mathrm{N}\cdot10\,\mathrm{m}\cdot0{,}6=117{,}7\,\mathrm{J}$. Die Hand verrichtet $+117{,}7$ J, die Gewichtskraft $-117{,}7$ J. Die Energie steckt danach in der Höhe, als __potenzielle Energie__: Fällt der Rucksack, wird sie zu Bewegungsenergie. Dieses Paar aus Arbeit der Feldkraft und Arbeit von außen kehrt in Stufe [6](arbeit-im-feld.html#stufe-6) wieder.
::::

⁠**Grenzfälle:** $\alpha=0$ ergibt $\Delta W=F\,\Delta s$, $\alpha=90^\circ$ ergibt $\Delta W=0$.

:::frage Beim waagerechten Tragen wird der Arm doch müde. Wird da keine Arbeit verrichtet?
Am Rucksack nicht: Er gewinnt weder Höhe noch Geschwindigkeit. Der Muskel verbraucht trotzdem Energie, weil seine Fasern sich laufend neu anspannen. Sie wird im Körper zu Wärme und erreicht den Rucksack nicht.
:::

:::aufgabe Aufgabe 1 ★ Einheiten und Vorsätze
<span class="anker" id="aufg-1"></span>

Berechne und gib das Ergebnis in einer passenden Einheit an: (a) $3\,\mathrm{kN}+450\,\mathrm{N}$, (b) $2\,\mathrm{mA}\cdot4\,\mathrm{ks}$, (c) $6\,\mu\text{C}/3\,\mathrm{ms}$, (d) 1 kWh in Joule, (e) 1,5 mm$^2$ in m$^2$, (f) die Einheit V/m in Basiseinheiten.

:::loesung
(a) $3000\,\mathrm{N}+450\,\mathrm{N}=3{,}45\,\mathrm{kN}$. (b) Milli und Kilo heben sich auf, $\mathrm{A\cdot s}=\mathrm C$: 8 C. (c) $\mu\text{}/\mathrm m=\mathrm m$ (Milli) und $\mathrm{C/s}=\mathrm A$: 2 mA. (d) $1000\,\mathrm{W}\cdot3600\,\mathrm{s}=3{,}6\,\mathrm{MJ}$. (e) $1\,\mathrm{mm^2}=(10^{-3}\,\mathrm{m})^2=10^{-6}\,\mathrm{m^2}$, also $1{,}5\cdot10^{-6}\,\mathrm{m^2}$. (f) $\frac{\mathrm V}{\mathrm m}=\frac{\mathrm{kg\,m^2}}{\mathrm{A\,s^3}\cdot\mathrm m}=\frac{\mathrm{kg\,m}}{\mathrm{A\,s^3}}$.
:::
:::

::::lernkarten
:::karte begriff physikalische Größe
Was ist eine physikalische Größe?
---
Eine messbare Eigenschaft, angegeben als Produkt aus Zahlenwert und Einheit: $\text{Größe}=\text{Zahlenwert}\cdot\text{Einheit}$. Der Zahlenwert hängt von der Einheit ab, die Größe nicht.
--- falsch
Eine messbare Eigenschaft, angegeben als Summe aus Zahlenwert und Einheit: $\text{Größe}=\text{Zahlenwert}+\text{Einheit}$. Zahlenwert und Einheit hängen nicht voneinander ab.
--- falsch
Eine messbare Eigenschaft, angegeben allein durch ihren Zahlenwert. Die Einheit wird nur zur Erläuterung dazugeschrieben und ändert am Zahlenwert nichts.
--- falsch
Eine Eigenschaft, die man mit Urteilen wie warm oder kühl beschreibt. Ihr Wert hängt davon ab, wer sie beurteilt und womit er sie vergleicht.
:::
:::karte begriff Basisgrößen
Was sind die Basisgrößen des SI-Einheitensystems?
---
Die sieben Größen, die sich nicht durcheinander ausdrücken lassen: Länge, Masse, Zeit, Stromstärke, absolute Temperatur, Lichtstärke und Stoffmenge. Die Einheiten aller anderen Größen sind Produkte von Potenzen ihrer Einheiten.
--- falsch
Die sieben Größen, die sich nicht durcheinander ausdrücken lassen: Länge, Masse, Zeit, Ladung, Spannung, absolute Temperatur und Stoffmenge. Die Einheiten aller anderen Größen sind Produkte von Potenzen ihrer Einheiten.
--- falsch
Die Größen mit eigenem Einheitennamen wie Newton, Joule, Volt und Watt. Die Einheiten aller übrigen Größen setzt man aus diesen und aus Meter und Sekunde zusammen.
--- falsch
Die sieben Größen, die man am häufigsten misst: Länge, Masse, Zeit, Kraft, Energie, Spannung und Leistung. Die übrigen Größen haben eigene Einheiten, die mit diesen nicht zusammenhängen.
:::
:::karte begriff SI-Vorsatz
Was ist ein SI-Vorsatz?
---
Ein Zeichen vor einer Einheit, das den Zahlenwert um eine Zehnerpotenz skaliert, etwa k für $10^{3}$. Vorsatz und Einheit bilden ein Symbol; vor einer Einheit steht immer nur ein Vorsatz.
--- falsch
Ein Zeichen vor einer Einheit, das den Zahlenwert um eine Zehnerpotenz skaliert, etwa k für $10^{3}$. Mehrere Vorsätze dürfen hintereinander stehen, etwa kk für $10^{6}$; ihre Faktoren multiplizieren sich.
--- falsch
Ein Zeichen vor einer Einheit, das den Zahlenwert skaliert. Großbuchstaben stehen für Teile, Kleinbuchstaben für Vielfache, etwa m für $10^{3}$ und M für $10^{-3}$.
--- falsch
Ein Faktor vor dem Zahlenwert, der mit der Einheit nichts zu tun hat. Potenzen wirken deshalb nur auf die Einheit, etwa $1\,\mathrm{km^2}=1000\,\mathrm{m^2}$.
:::
:::karte zusammenhang Addieren mit Einheiten
Warum ergibt $2\,\mathrm{kV}+40\,\mathrm{V}$ nicht $42\,\mathrm{kV}$?
---
Weil man nur Größen derselben Einheit addieren darf; die Vorsätze gleicht man vorher an: $2\,\mathrm{kV}+40\,\mathrm{V}=2{,}04\,\mathrm{kV}$.
--- falsch
Weil man Größen mit Einheiten gar nicht addieren darf, sondern nur multiplizieren. Erlaubt wäre hier allein das Produkt $2\,\mathrm{kV}\cdot40\,\mathrm{V}$.
--- falsch
Weil man die Vorsätze vorher angleichen muss, $40\,\mathrm{V}=0{,}4\,\mathrm{kV}$. Die richtige Summe ist also $2\,\mathrm{kV}+40\,\mathrm{V}=2{,}4\,\mathrm{kV}$.
--- falsch
Weil eine Summe immer die Einheit des kleineren Summanden bekommt. Die richtige Summe ist also $2\,\mathrm{kV}+40\,\mathrm{V}=42\,\mathrm{V}$.
:::
:::karte begriff Kraft
Was ist eine Kraft?
---
Eine vektorielle Größe, die einen festgehaltenen Körper verformt oder einen beweglichen beschleunigt: $F=m\,a$, Einheit Newton, $1\,\mathrm{N}=1\,\mathrm{kg\,m/s^2}$.
--- falsch
Eine skalare Größe, die angibt, wie viel Bewegung ein Körper enthält: $F=m\,v$, Einheit Newton, $1\,\mathrm{N}=1\,\mathrm{kg\,m/s}$.
--- falsch
Eine vektorielle Größe, die einen Körper mit konstanter Geschwindigkeit in Bewegung hält. Ohne Kraft kommt jeder bewegliche Körper sofort zur Ruhe.
--- falsch
Die Fähigkeit eines Körpers, Arbeit zu verrichten. Sie wird in Joule gemessen, $1\,\mathrm{J}=1\,\mathrm{N\,m}$, und hat keine Richtung.
:::
:::karte begriff Arbeit
Was ist die Arbeit einer Kraft längs eines Wegs?
---
Die Energie, die die Kraft dabei überträgt. Es zählt nur ihr Anteil in Wegrichtung: $\Delta W=\vec F\cdot\Delta\vec s=F\,\Delta s\cos\alpha$, Einheit Joule.
--- falsch
Die Energie, die die Kraft dabei überträgt. Es zählt nur ihr Anteil quer zum Weg: $\Delta W=F\,\Delta s\sin\alpha$, Einheit Joule.
--- falsch
Die Energie, die die Kraft dabei überträgt: Betrag der Kraft mal Weglänge, gleich in welche Richtung sie zeigt, $\Delta W=F\,\Delta s$, Einheit Joule.
--- falsch
Die Energie, die die Kraft je Sekunde überträgt: Kraft mal Geschwindigkeit in Wegrichtung, $\Delta W=F\,v\cos\alpha$, Einheit Watt.
:::
:::karte formel Arbeit längs eines Wegs
Wie berechnet man die Arbeit einer Kraft $\vec F$ längs eines gekrümmten Wegs von $P_1$ nach $P_2$?
---
Mit dem Linienintegral $W=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s$: Man zerlegt den Weg in kurze gerade Stücke und summiert ihre Beiträge. Für $\alpha>90^\circ$ entzieht die Kraft dem Körper Energie.
--- falsch
Mit $W=F\cdot s$, wobei $s$ die Länge des gekrümmten Wegs ist. Die Richtung der Kraft spielt keine Rolle, weil die Arbeit eine Zahl ist und kein Vektor, der eine Richtung hätte.
--- falsch
Mit dem Integral über die Beträge, $W=\int_{P_1}^{P_2}F\,\mathrm{d} s$. Der Winkel zwischen Kraft und Weg zählt nur bei geraden Wegen, auf gekrümmten mittelt er sich heraus.
--- falsch
Man multipliziert die Kraft am Startpunkt $P_1$ mit der Weglänge. Änderungen der Kraft längs des Wegs gleichen sich im Mittel aus und dürfen entfallen.
:::
:::karte formel Konstante Beschleunigung
Welche Geschwindigkeit und welchen Ort hat ein Körper mit konstanter Beschleunigung $a$ und den Startwerten $s_0$, $v_0$ bei $t=0$?
---
$v(t)=v_0+a\,t$ und $s(t)=s_0+v_0\,t+\tfrac12a\,t^2$. Die Gleichungen gelten nur für konstante Beschleunigung.
--- falsch
$v(t)=v_0+a\,t$ und $s(t)=s_0+v_0\,t+a\,t^2$. Die Gleichungen gelten nur für konstante Beschleunigung.
--- falsch
$v(t)=v_0+\tfrac12a\,t^2$ und $s(t)=s_0+v_0\,t+a\,t$. Die Gleichungen gelten nur für konstante Beschleunigung.
--- falsch
$v(t)=v_0+a\,t$ und $s(t)=s_0+v_0\,t+\tfrac12a\,t^2$. Die Gleichungen gelten für jede Beschleunigung, auch für eine veränderliche.
:::
:::karte formel Bewegungsenergie
Welche Bewegungsenergie trägt ein Körper der Masse $m$ mit der Geschwindigkeit $v$?
---
$W_\mathrm{kin}=\frac12m\,v^2$, in Joule. Sie wächst mit dem Quadrat der Geschwindigkeit: Doppelte Geschwindigkeit ergibt vierfache Energie.
--- falsch
$W_\mathrm{kin}=m\,v^2$, in Joule. Sie wächst mit dem Quadrat der Geschwindigkeit: Doppelte Geschwindigkeit ergibt vierfache Energie.
--- falsch
$W_\mathrm{kin}=\frac12m\,v$, in Joule. Sie wächst proportional zur Geschwindigkeit: Doppelte Geschwindigkeit ergibt doppelte Energie.
--- falsch
$W_\mathrm{kin}=\frac12m^2v^2$, in Joule. Sie wächst mit dem Quadrat der Masse: Doppelte Masse ergibt vierfache Energie.
:::
:::karte herleitung Bewegungsenergie
Leite aus den Gleichungen für konstante Beschleunigung her, dass eine konstante Kraft einen Körper aus der Ruhe auf die Bewegungsenergie $\frac12m\,v^2$ bringt.
---
Der Körper startet aus der Ruhe am Ursprung, $v_0=0$ und $s_0=0$. Aus $v(t)=v_0+a\,t$ folgt $t=v/a$, weil nur $a\,t$ übrig bleibt.
---
Eingesetzt in $s(t)=s_0+v_0\,t+\tfrac12a\,t^2$ ergibt sich $s=\frac12a\,t^2=v^2/(2a)$, weil so die Zeit durch die erreichte Geschwindigkeit ersetzt ist.
---
Die konstante Kraft $F=m\,a$ zeigt in Wegrichtung und verrichtet die Arbeit $F\,s$, weil $\alpha=0$ ist.
---
Einsetzen ergibt $F\,s=m\,a\,v^2/(2a)=\frac12m\,v^2$, weil sich $a$ herauskürzt. Diese Arbeit steckt danach als Bewegungsenergie im Körper.
:::
:::karte zusammenhang Treppe und Rampe
Warum kostet es gleich viel Arbeit, einen Rucksack über eine Treppe oder über eine Rampe auf dieselbe Höhe zu heben?
---
Weil nur der Kraftanteil in Wegrichtung zählt. Die Hand drückt senkrecht nach oben, also zählen nur die senkrechten Wegstücke; auf beiden Wegen ergeben sie den Höhenunterschied.
--- falsch
Weil die Rampe zwar länger ist, aber weniger Kraft braucht. Das gleicht sich bei dem gewählten Neigungswinkel zufällig genau aus; bei einer flacheren oder steileren Rampe wäre die Arbeit anders.
--- falsch
Weil die Arbeit nur vom Gewicht abhängt, nicht vom Weg. Auch waagerechtes Tragen über dieselbe Strecke kostet deshalb genau dieselbe Arbeit.
--- falsch
Weil auf beiden Wegen dieselbe Zeit vergeht. Arbeit ist Kraft mal Zeit, und die Kraft ist auf beiden Wegen gleich groß.
:::
:::karte zusammenhang Waagerechtes Tragen
Warum verrichtet man am Rucksack keine Arbeit, wenn man ihn waagerecht trägt, obwohl der Arm müde wird?
---
Weil die Haltekraft senkrecht nach oben zeigt, der Weg aber waagerecht verläuft: $\alpha=90^\circ$, also $\Delta W=0$. Der Muskel verbraucht Energie, die im Körper zu Wärme wird.
--- falsch
Weil der Rucksack beim Tragen nicht beschleunigt wird. Ohne Beschleunigung wirkt nach $F=m\,a$ überhaupt keine Kraft auf ihn, auch keine Gewichtskraft.
--- falsch
Weil sich die Arbeit der Hand und die der Gewichtskraft beim Tragen aufheben. Einzeln ist jede so groß wie beim Heben um dieselbe Strecke.
--- falsch
Weil der Muskel die Energie zunächst speichert. Er gibt sie erst beim Absetzen an den Rucksack ab; dann wird die Arbeit nachträglich am Rucksack verrichtet.
:::
::::
