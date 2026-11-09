---
title: Stufe 1: Zwei Kontakte am MOS-Kondensator
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270300
summary: Durch einen MOS-Kondensator fließt kein Gleichstrom.
tags: Polysilizium, Feldeffekt-Transistor, Drainstrom, Kanallänge, Kanalweite
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Durch einen MOS-Kondensator fließt kein Gleichstrom. Diese Stufe ergänzt zwei Kontakte und klärt, warum das Gate den Strom zwischen ihnen schaltet.
:::

**Die Idee.** Ein niedrig dotiertes p-Substrat dient als mechanischer Träger. Seine Oberfläche ist mit einem dünnen Isolator überzogen, meist $\mathrm{SiO_2}$. Durch Öffnungen im Isolator werden zwei stark n-dotierte Gebiete (n$^+$) diffundiert oder implantiert, aufgedampfte und einlegierte Metallkontakte führen sie nach außen. Auf dem Isolator dazwischen liegt das Gate aus Metall oder __Polysilizium__ (polykristallinem, stark dotiertem Silizium).

Von Source nach Drain folgt also n, p, n: zwei p-n-Übergänge gegeneinander. Bei positiver Spannung am Drain sperrt der Übergang am Drain, und es fließt fast kein Strom. Wird die Gatespannung größer als $V_\mathrm{th}$, entsteht an der Oberfläche eine Inversionsschicht. Sie ist n-leitend und verbindet beide n$^+$-Gebiete. Ihre Elektronen liefert die Source ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)). Mehr Gatespannung bedeutet mehr Ladung im Kanal und damit mehr Strom. Das Gate wirkt nur über sein Feld, daher der Name __Feldeffekt-Transistor__ (FET). Transistor steht für transfer resistor, Übertragungswiderstand. Bei beliebigem Isolator sagt man MISFET oder IGFET (insulated gate FET).

:::abbildung gemb1/k17aufbau 1
Links: Querschnitt eines n-Kanal-MOSFET, der Kanal (blau) ist viel zu dick gezeichnet. $z$ zeigt aus der Zeichenebene heraus, in dieser Richtung liegt die Weite $W$. Rechts: Schaltzeichen mit Zählpfeilen, Source und Substrat sind verbunden.
:::

:::definition Definition 1.1 (Anschlüsse, Spannungen, Richtungen)
<span class="anker" id="satz-1-1"></span>

Die Anschlüsse heißen Source S (Quelle), Drain D (Senke), Gate G (Tor) und Substrat B (englisch bulk). $V_\mathrm{GS}$ ist die Spannung von Gate zu Source, $V_\mathrm{DS}$ die von Drain zu Source, $V_\mathrm{SB}$ die von Source zu Substrat. Der __Drainstrom__ $I_\mathrm D$ zählt in den Drain hinein. Die Richtungen sind: $x$ Tiefe ins Substrat, $y$ Transport von $y=0$ an der Source bis $y=L$ am Drain, $z$ quer zum Strom.
:::

⁠**So liest man das:** In [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) ist $x$ die Tiefe, deshalb läuft der Strom hier in $y$-Richtung. Mit $V_\mathrm{SB}=0$ ist $V_\mathrm{GS}$ die Spannung $V_\mathrm G$ aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html). Die __Kanallänge__ $L$ ist der Abstand von Source und Drain, sie reicht von Nanometern bis zu Mikrometern. Die __Kanalweite__ $W$ liegt zwischen unter 1 µ m in Digitalschaltungen und mehreren Millimetern in Leistungstransistoren. Der Isolator ist typisch 10 nm dick, der Kanal nur wenige Nanometer tief. **Gültigkeit:** Bis auf Weiteres ist ein n-Kanal-MOSFET mit $V_\mathrm{th}>0$ gemeint, Source und Substrat sind verbunden, und durch den Isolator fließt kein Strom.

::::beispiel
Bei $V_\mathrm{GS}=3$ V und kleinem $V_\mathrm{DS}$ ist $Q'_\mathrm{inv}=-172{,}7\,\mathrm{nF/cm^2}\cdot2{,}677\,\mathrm{V}=-462\,\mathrm{nC/cm^2}$. Das sind $2{,}9\cdot10^{12}$ Elektronen je cm$^2$, im Kanal von 250 µ m$^2$ also $7{,}2\cdot10^{6}$ Elektronen. Eine Schicht mit dem Flächenleitwert $|Q'_\mathrm{inv}|\,\mu_\mathrm n=0{,}231$ mS und dem Verhältnis $L/W=0{,}1$ hat den Widerstand $433\,\Omega$.
::::

⁠**Grenzfall:** Für $V_\mathrm{GS}\to V_\mathrm{th}$ geht $Q'_\mathrm{inv}\to0$ und der Widerstand gegen unendlich: Der Schalter öffnet.

:::frage Source und Drain sehen gleich aus. Woran erkennt man, welcher Anschluss welcher ist?
Der Aufbau ist symmetrisch, und das stimmt auch elektrisch. Die Rollen legt die Spannung fest: Beim n-Kanal-MOSFET ist die Source der n$^+$-Anschluss mit dem tieferen Potential, denn dort starten die Elektronen. Dreht man $V_\mathrm{DS}$ um, tauschen beide Anschlüsse die Namen.
:::

:::zusatz Geschichte und andere Feldeffekttransistoren
J. E. Lilienfeld ließ die Stromsteuerung über eine Elektrode 1925 patentieren. Das Wort Transistor entstand 1948 für das erste Halbleiter-Verstärkerelement von J. Bardeen und W. H. Brattain. Silizium-MOSFETs folgten ab 1960 (D. Kahng, M. Atalla; 1963 S. R. Hofstein, F. P. Heiman). P. K. Weimer stellte 1962 den Dünnfilmtransistor (TFT) aus polykristallinem CdS auf Glas vor, TFTs steuern heute Flachbildschirme. Sperrschicht-FETs nutzen als Gate einen p-n-Übergang (JFET, W. Shockley 1952, G. C. Dacey und I. M. Ross 1953) oder einen Metall-Halbleiter-Kontakt (MESFET, C. A. Mead 1966, auf GaAs). Die Spannung ändert dort die Ausdehnung der Raumladungszone und damit den leitenden Querschnitt. GaAs-MESFETs erreichen hohe Frequenzen, Silizium-MOSFETs lassen sich einfacher und billiger fertigen und tragen heute integrierte Schaltungen mit über 100 Millionen Transistoren auf wenigen Quadratmillimetern.
:::

:::aufgabe Aufgabe 1 ★ Ein Kanal in Zahlen
<span class="anker" id="aufg-1"></span>

Ein MOSFET hat 15 nm $\mathrm{SiO_2}$, $W=30$ µ m, $L=3$ µ m und $\mu_\mathrm n=450\,\mathrm{cm^2/(V\,s)}$. Es ist $V_\mathrm{GS}-V_\mathrm{th}=1{,}5$ V, $V_\mathrm{DS}$ ist klein.

<ol class="al">

<li>

Berechne $Q'_\mathrm{inv}$, die Elektronen je cm$^2$ und die Elektronen im Kanal.

</li>

<li>

Wie groß ist der Widerstand zwischen Source und Drain?

</li>

<li>

Vorhersage: Wie ändert er sich, wenn $W$ doppelt so groß wird? Und wenn $V_\mathrm{GS}-V_\mathrm{th}$ halb so groß wird?

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=230{,}2\,\mathrm{nF/cm^2}$, also $Q'_\mathrm{inv}=-345\,\mathrm{nC/cm^2}$, das sind $2{,}15\cdot10^{12}$ Elektronen je cm$^2$. Auf 90 µ m$^2$ sitzen $1{,}9\cdot10^{6}$ Elektronen. (b) Der Flächenleitwert ist $345\,\mathrm{nC/cm^2}\cdot450\,\mathrm{cm^2/(V\,s)}=0{,}155$ mS, also $R=(L/W)/0{,}155\,\mathrm{mS}=644\,\Omega$. (c) Doppelte Weite heißt parallele Schichten: 322 $\Omega$. Halbe Spannung heißt halbe Ladung: 1287 $\Omega$.
:::
:::
