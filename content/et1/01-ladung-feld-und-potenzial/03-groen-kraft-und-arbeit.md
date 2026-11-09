---
title: Stufe 1: Größen, Kraft und Arbeit
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Ladung, Feld und Potenzial
order: 1110300
summary: Spannung wird sich als Arbeit je Ladung erweisen.
tags: qualitativ, quantitativ, ohmsche Gesetz, physikalische Größe, SI-Einheitensystem, Basisgrößen, Strom, SI-Vorsätze
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Spannung wird sich als Arbeit je Ladung erweisen. Dafür braucht man Größen mit Einheiten, die Kraft, die Arbeit und die Bewegungsenergie.
:::

**Die Idee.** Wer aus dem Schnee kommt, nennt einen Raum warm, wer aus der Sauna kommt, kühl. Solche Urteile sind __qualitativ__. Ein Thermometer zeigt beiden 21 °C, das ist __quantitativ__: eine Zahl mit Maßstab, unabhängig davon, wer misst. Mit solchen Größen formuliert die Physik ihre Gesetze, zum Beispiel das __ohmsche Gesetz__ $U=R\cdot I$ ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Die wichtigste mechanische Größe dieses Kapitels ist die Arbeit: Eine Kraft, die längs eines Wegs wirkt, überträgt Energie, und es zählt nur ihr Anteil in Wegrichtung. Wer einen Rucksack hebt, arbeitet gegen die Schwerkraft, wer ihn waagerecht trägt, nicht (Abb. [2](#abb-2)).

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
