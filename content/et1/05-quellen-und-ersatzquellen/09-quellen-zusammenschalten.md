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
