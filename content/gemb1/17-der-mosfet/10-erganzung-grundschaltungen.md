---
title: Stufe 8: Ergänzung: Grundschaltungen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4271000
summary: Ein Transistor arbeitet in einer Schaltung.
tags: Vierpol, Source-Schaltung, Drain-Schaltung, Gate-Schaltung, Inverter
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein Transistor arbeitet in einer Schaltung. Diese Ergänzung zeigt die drei Grundschaltungen und daran den einfachsten digitalen Baustein.
:::

**Die Idee.** Eine Schaltung mit Eingang und Ausgang ist ein __Vierpol__ mit je zwei Klemmen. Der MOSFET hat, mit dem Substrat an der Source, nur drei Anschlüsse. Einer muss also zu Eingang und Ausgang gehören. Er ist der gemeinsame Bezugspunkt und gibt der Schaltung den Namen. In der Source-Schaltung setzt man einen Widerstand zwischen Versorgung und Drain. Sperrt der Transistor, zieht der Widerstand den Ausgang hoch. Leitet er, zieht der Transistor ihn herunter.

:::definition Definition 8.1 (Grundschaltungen)
<span class="anker" id="satz-8-1"></span>

| gemeinsamer Anschluss | Eingang | Ausgang |
|---|---|---|
| __Source-Schaltung__: Source | Gate | Drain |
| __Drain-Schaltung__: Drain | Gate | Source |
| __Gate-Schaltung__: Gate | Source | Drain |
:::

:::satz Satz 8.2 (Inverter in Source-Schaltung)
<span class="anker" id="satz-8-2"></span>

Mit $R_\mathrm D$ zwischen $V_\mathrm{DD}$ und Drain, $V_\mathrm{GS}=V_\mathrm{in}$, $V_\mathrm{DS}=V_\mathrm{out}$ und unbelastetem Ausgang gilt

<span class="anker" id="gl-8-1"></span>
$$V_\mathrm{out}=V_\mathrm{DD}-R_\mathrm DI_\mathrm D(V_\mathrm{in},V_\mathrm{out}). \tag{8.1}$$
:::

⁠**So liest man das:** $V_\mathrm{DD}$ ist die Versorgungsspannung. [(8.1)](#gl-8-1) ist eine Gerade im Ausgangskennlinienfeld, ihr Schnitt mit der Kennlinie zu $V_\mathrm{in}$ ist der Arbeitspunkt. Für $V_\mathrm{in}<V_\mathrm{th}$ ist $V_\mathrm{out}\approx V_\mathrm{DD}$. In Sättigung ist $V_\mathrm{out}=V_\mathrm{DD}-R_\mathrm DK(V_\mathrm{in}-V_\mathrm{th})^2/2$. Bei großem $V_\mathrm{in}$ wirkt der Transistor als $R$ aus [(4.2)](ausgangskennlinien.html#gl-4-2), und es entsteht der Teiler $V_\mathrm{out}\approx V_\mathrm{DD}R/(R+R_\mathrm D)$. **Gültigkeit:** statischer Betrieb. Durch das Gate fließt dann kein Strom, $I_\mathrm G=0$.

:::abbildung gemb1/k17inverter 8
Links: n-Kanal-MOSFET in Source-Schaltung. Rechts: $V_\mathrm{out}(V_\mathrm{in})$ des Rechenmodells mit $V_\mathrm{DD}=5$ V und $R_\mathrm D=5\,\mathrm{k\Omega}$. Am roten Punkt wechselt der Transistor von der Sättigung in den ungesättigten Bereich.
:::

::::beispiel
Mit dem Rechenmodell, $V_\mathrm{DD}=5$ V und $R_\mathrm D=5\,\mathrm{k\Omega}$ ergeben $V_\mathrm{in}=0$, 1, 2 und 5 V die Ausgangsspannungen 5,00, 4,01, 0,76 und 0,24 V. Die Bereichsgrenze liegt bei $V_\mathrm{in}=1{,}63$ V und $V_\mathrm{out}=1{,}31$ V. Eine hohe Eingangsspannung gibt eine niedrige Ausgangsspannung, das ist ein __Inverter__. Im Zustand $V_\mathrm{in}=5$ V fließen 0,95 mA, die Schaltung nimmt 4,5 mW auf. Bei $V_\mathrm{in}=0$ sind es nur 0,11 nW aus dem Unterschwellstrom.
::::

⁠**Grenzfall:** Für $R_\mathrm D\to0$ bleibt $V_\mathrm{out}=V_\mathrm{DD}$, der Transistor kann den Ausgang nicht mehr herunterziehen.

:::ltspice Kennlinienfeld und Inverter des Rechenmodells
⁠**Zeichnen:** `nmos4` namens `M1`, Wert `NM`, Zusatzzeile `L=5u W=50u`. Source und Substrat an Masse, Drain über `R1` ($5\,\mathrm{k\Omega}$) an `V2` (5 V), Gate an `V1`, Ausgang `out` am Drain.

⁠**Direktiven:** `.model NM NMOS(LEVEL=1 VTO=0.3233 KP=86.33u GAMMA=0.578 PHI=0.7773)` und `.dc V1 0 5 10m`. KP ist $\mu_\mathrm nC'_\mathrm{IS}$.

⁠**Was du siehst:** `V(out)` ergibt bei 1, 1,5, 2, 3 und 5 V die Werte 4,012, 2,012, 0,757, 0,430 und 0,242 V wie in Aufgabe [12](#aufg-12) mit anderen Zahlen. Unter $V_\mathrm{th}$ bleibt `V(out)` bei genau 5 V, denn LEVEL 1 kennt keinen Unterschwellstrom. Ohne `R1`, mit `.step param VG list 1 2 3 4` und `.dc V2 0 5 10m` sowie `V1` auf `{VG}`, erscheint das Kennlinienfeld: Bei 5 V liest du 0,198, 1,21, 3,09 und 5,84 mA.
:::

:::frage Bei hohem Eingang fließt ständig Strom. Lässt sich das vermeiden?
Der Strom fließt, weil der Widerstand immer an $V_\mathrm{DD}$ hängt. Ersetzt man ihn durch einen p-Kanal-Anreicherungstyp mit demselben Eingang, sperrt dieser, sobald der n-Kanal-Transistor leitet, und umgekehrt. Im Ruhezustand bleibt dann nur der Unterschwellstrom.
:::

:::aufgabe Aufgabe 12 ★★ Einen Inverter auslegen
<span class="anker" id="aufg-12"></span>

Ein n-Kanal-MOSFET mit $K=2$ mA/V$^2$ und $V_\mathrm{th}=0{,}6$ V liegt wie in Abb. [8](#abb-8) an $V_\mathrm{DD}=3{,}3$ V, der Ausgang ist unbelastet.

<ol class="al">

<li>

Welche Grundschaltung ist das? Wie groß ist $I_\mathrm G$ im statischen Betrieb?

</li>

<li>

Wähle $R_\mathrm D$ so, dass $V_\mathrm{in}=1{,}6$ V die Spannung $V_\mathrm{out}=1{,}3$ V ergibt. In welchem Bereich arbeitet der Transistor?

</li>

<li>

Wähle $R_\mathrm D$ so, dass $V_\mathrm{in}=1{,}6$ V die Spannung $V_\mathrm{out}=0{,}3$ V ergibt.

</li>

<li>

Bestimme für $R_\mathrm D=2{,}2\,\mathrm{k\Omega}$ die Spannung $V_\mathrm{out}$ bei $V_\mathrm{in}=0$, 1, 1,5, 2 und 3,3 V. Welches logische Gatter ist das?

</li>

</ol>

:::loesung
(a) Source-Schaltung, $I_\mathrm G=0$. (b) $V_\mathrm{in}-V_\mathrm{th}=1$ V, $V_\mathrm{out}=1{,}3$ V ist größer, also Sättigung: $I_\mathrm D=1$ mA und $R_\mathrm D=(3{,}3-1{,}3)\,\mathrm{V}/1\,\mathrm{mA}=2{,}0\,\mathrm{k\Omega}$. (c) $0{,}3$ V ist kleiner als 1 V, also ungesättigt: $I_\mathrm D=2\,\mathrm{mA/V^2}\cdot(0{,}3-0{,}045)\,\mathrm{V^2}=0{,}51$ mA und $R_\mathrm D=3\,\mathrm{V}/0{,}51\,\mathrm{mA}=5{,}9\,\mathrm{k\Omega}$. (d) $V_\mathrm{in}=0$: 3,30 V, Aus. 1 V: 2,95 V, Sättigung. 1,5 V: 1,52 V, Sättigung. 2 V: 0,56 V, ungesättigt. 3,3 V: 0,27 V, ungesättigt. Das ist ein NICHT-Gatter (Inverter).
:::
:::
