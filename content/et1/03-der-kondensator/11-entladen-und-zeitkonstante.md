---
title: Stufe 10: Entladen und Zeitkonstante
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Kondensator
order: 1131100
summary: Der geladene Kondensator gibt seine Ladung über einen Widerstand zurück.
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Der geladene Kondensator gibt seine Ladung über einen Widerstand zurück. Es ist dieselbe Gleichung mit anderem Startwert. Daraus folgt eine Regel für jeden Schaltvorgang im RC-Kreis.
:::

**Die Idee.** Der Schalter geht von Stellung 1 auf 2, die Batterie ist abgetrennt. Der Kondensator hält seine 9 V, denn sie können nicht springen. Diese Spannung liegt nun über $R$. Die Elektronen der negativen Platte laufen über $R$ zur positiven zurück. Der Strom läuft also entgegen dem Zählpfeil von Abb. [9](aufladen-uber-einen-widerstand.html#abb-9), und er springt: Eben war er null, nun beträgt er $-0{,}9$ mA. Mit jeder abfließenden Ladung sinkt die Spannung und damit der Strom. Der Kondensator wirkt anfangs wie eine Quelle, die immer schwächer wird.

:::satz Satz 10.1 (Entladen)
<span class="anker" id="satz-10-1"></span>

Ohne Batterie lautet die Maschenregel $u_R+u_C=0$, also $RC\,\mathrm{d} u_C/\mathrm{d} t+u_C=0$. Mit $u_C(0)=U_0$ und $t\ge0$ gilt

<span class="anker" id="gl-10-1"></span>
$$u_C(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad i(t)=-\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=-U_0\,\mathrm{e}^{-t/\tau}. \tag{10.1}$$
:::

Allgemein gilt für jeden Schaltvorgang im RC-Kreis mit konstanter Quelle: Die Spannung läuft vom Startwert $u_C(0)$ zum Endwert $u_\infty$ auf

<span class="anker" id="gl-10-2"></span>
$$u_C(t)=u_\infty+\bigl(u_C(0)-u_\infty\bigr)\,\mathrm{e}^{-t/\tau}. \tag{10.2}$$

⁠**So liest man das:** Das Minuszeichen bei $i$ sagt: Der Strom läuft gegen den Zählpfeil. $u_\infty$ ist die Spannung, die der Kondensator nach langer Zeit erreicht, beim Laden $U_0$, beim Entladen 0. Die Differenz zum Endwert schrumpft in jeder Zeit $\tau$ auf 36,8 %. **Gültigkeit:** $\tau$ wird mit dem Widerstand des jeweiligen Stromwegs gebildet. Beide Stellungen haben hier dasselbe $R$.

:::herleitung Allgemeine Regel
Für den Abstand $x=u_\infty-u_C$ gilt wie in Stufe [9](aufladen-uber-einen-widerstand.html#stufe-9) $\mathrm{d} x/\mathrm{d} t=-x/\tau$. Die Schritte 2 bis 4 gelten für jedes Vorzeichen von $x$, wenn man $\ln|x|$ schreibt, und ergeben $x(t)=x(0)\,\mathrm{e}^{-t/\tau}$. Einsetzen von $x(0)=u_\infty-u_C(0)$ liefert [(10.2)](#gl-10-2). Für $u_\infty=0$ entsteht [(10.1)](#gl-10-1), für $u_\infty=U_0$ und $u_C(0)=0$ entsteht [(9.3)](aufladen-uber-einen-widerstand.html#gl-9-3).
:::

**Die Zeitkonstante.** $\tau=RC$ ist die Zeit, nach der Strom und Restspannung auf $1/\mathrm{e}$ gefallen sind. Beim Laden sind dann 63,2 % erreicht. Laden und Entladen werden schneller mit kleinerem $C$, weil weniger Ladung zu bewegen ist, und mit kleinerem $R$, weil mehr Strom fließt. $U_0$ kommt in $\tau$ nicht vor: Doppelte Spannung ergibt doppelten Strom, aber auch doppelte Ladung. Die Tabelle gilt für jeden RC-Kreis, die letzte Zeile für das Rechenmodell.

| Zeit | $1\tau$ | $2\tau$ | $3\tau$ | $4\tau$ | $5\tau$ |
|---|---|---|---|---|---|
| Laden: $1-\mathrm{e}^{-t/\tau}$ in % | 63,2 | 86,5 | 95,0 | 98,2 | 99,3 |
| Entladen: $\mathrm{e}^{-t/\tau}$ in % | 36,8 | 13,5 | 5,0 | 1,8 | 0,7 |
| Laden: $u_C$ in V | 5,69 | 7,78 | 8,55 | 8,84 | 8,94 |

:::abbildung et1/k3entladen 12
Fünf Sekunden Laden, fünf Sekunden Entladen. Die Spannung verläuft stetig, die Prozentzahlen beziehen sich auf den Endwert beim Laden und auf den Startwert beim Entladen. Der Strom springt beim Umschalten und wechselt beim Entladen das Vorzeichen, gestrichelt die Sprünge.
:::

::::beispiel
Im Rechenmodell startet das Entladen bei 9 V. Im ersten Moment ist $u_R=-9$ V und $i=-0{,}9$ mA. Nach 1 s sind es $u_C=3{,}31$ V und $i=-0{,}331$ mA, nach 3 s noch 0,448 V. Lädt man nur 5 s lang wie in Abb. [12](#abb-12), startet das Entladen bei 8,94 V.
::::

⁠**Kontrolle:** Die Ladung, die beim Entladen durch $R$ fließt, ist $\int_0^\infty|i|\,\mathrm{d} t=\frac{U_0}{R}\,\tau=C\,U_0$, genau die gespeicherte Ladung. **Grenzfall:** Für $u_C(0)=u_\infty$ ist die Klammer in [(10.2)](#gl-10-2) null: Es passiert nichts, der Kondensator ist schon im Endzustand.

:::frage Warum darf der Strom beim Umschalten springen, die Spannung aber nicht?
Die Spannung ist an die gespeicherte Ladung gebunden, und die kann sich nur mit endlichem Strom in endlicher Zeit ändern. Der Strom hat keinen solchen Speicher. Er folgt in jedem Moment aus der Spannung an $R$, und die ändert sich mit dem Umlegen des Schalters.
:::

:::ltspice Laden und Entladen im RC-Kreis
⁠**Zeichnen:** `voltage` von `in` nach Masse mit `PULSE(0 9 0 1u 1u 5 10)`, `res` mit `10k` von `in` nach `out`, `cap` mit `100u` von `out` nach Masse. Die Quelle ersetzt den Schalter: 5 s lang 9 V, dann 0 V, also ein Weg über $R$ zurück.

⁠**Direktiven:** `.tran 0 10 0 1m`, dazu Messungen wie `.meas tran u1 FIND V(out) AT=1` für $t=1$, 2, 3, 5 und 6 s sowie `.meas tran i0 FIND I(R1) AT=10u`.

⁠**Was du siehst:** 5,69 V; 7,78 V; 8,55 V; 8,94 V beim Laden, wie in der Tabelle, bei 6 s dann 3,29 V, also 36,8 % von 8,94 V. Am Start ist `i0` $=0{,}90$ mA. Stelle danach 12 V, `4.7k` und `220u` ein und prüfe deine Ergebnisse aus Aufgabe [10](aufladen-uber-einen-widerstand.html#aufg-10).
:::

:::aufgabe Aufgabe 12 ★★ Startwerte und Selbstentladung
<span class="anker" id="aufg-12"></span>

Es gelten $R=10\,\mathrm{k\Omega}$, $C=100\,\mu\text{F}$ und $\tau=1$ s.

<ol class="al">

<li>

Der Kondensator trägt schon 3 V, wenn $U_0=9$ V zugeschaltet wird. Gib $u_C(t)$ an und berechne $u_C(1\,\mathrm{s})$.

</li>

<li>

Wie lange dauert es dabei, bis $u_C$ von 3 V auf 6 V gestiegen ist?

</li>

<li>

Entladen von 9 V aus: Wann fällt $u_C$ unter 1 V?

</li>

<li>

Der geladene Kondensator (9 V) ist abgetrennt, nur $R_\mathrm{I}=1\,\mathrm{M\Omega}$ entlädt ihn. Wie groß ist $u_C$ nach einer Minute?

</li>

</ol>

:::loesung
(a) Mit [(10.2)](#gl-10-2), $u_\infty=9$ V und $u_C(0)=3$ V: $u_C(t)=9\,\mathrm{V}-6\,\mathrm{V}\cdot\mathrm{e}^{-t/\tau}$. Für $t=1$ s: 6,79 V.

(b) $6=9-6\,\mathrm{e}^{-t/\tau}$ ergibt $\mathrm{e}^{-t/\tau}=\frac12$, also $t=\tau\ln2=0{,}693$ s.

(c) $9\,\mathrm{e}^{-t/\tau}=1$ ergibt $t=\tau\ln9=2{,}20$ s.

(d) Die Zeitkonstante ist $R_\mathrm{I}\,C=100$ s, also $u_C(60\,\mathrm{s})=9\,\mathrm{V}\cdot\mathrm{e}^{-0{,}6}=4{,}94$ V.
:::
:::
