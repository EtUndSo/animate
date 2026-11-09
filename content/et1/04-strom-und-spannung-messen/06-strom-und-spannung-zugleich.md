---
title: Stufe 5: Strom und Spannung zugleich
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom und Spannung messen
order: 1140600
summary: Wer einen Widerstand aus R=U/I bestimmt, braucht beide Instrumente.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Wer einen Widerstand aus $R=U/I$ bestimmt, braucht beide Instrumente. Eines liegt dann im Messkreis des anderen. Diese Stufe vergleicht die zwei möglichen Schaltungen.
:::

**Die Idee.** Das Voltmeter lässt sich vor oder hinter dem Amperemeter anklemmen (Abb. [6](#abb-6)). Liegt es vor dem Amperemeter, zählt das Amperemeter genau den Strom durch $R$, doch das Voltmeter misst die Spannung an $R$ und am Amperemeter zusammen. Liegt es direkt an $R$, stimmt die Spannung, doch das Amperemeter zählt den Strom des Voltmeters mit.

:::abbildung et1/k4richtig 6
Die zwei Messschaltungen. Grün die richtige Anzeige, rot die Anzeige mit dem Beitrag des anderen Instruments.
:::

:::definition Definition 5.1 (Stromrichtige und spannungsrichtige Messung)
<span class="anker" id="satz-5-1"></span>

$U$ und $I$ sind die Anzeigen, $U_R$ und $I_R$ die Werte am Widerstand.

Stromrichtig: $I=I_R$, aber $U=U_R+U_\mathrm{iA}\neq U_R$. Daraus folgt

<span class="anker" id="gl-5-1"></span>
$$\frac UI=R+R_\mathrm{iA},\qquad f=+\frac{R_\mathrm{iA}}{R}. \tag{5.1}$$

Spannungsrichtig: $U=U_R$, aber $I=I_R+I_\mathrm{iV}\neq I_R$. Daraus folgt

<span class="anker" id="gl-5-2"></span>
$$\frac UI=R\parallel R_\mathrm{iV},\qquad f=-\frac{R}{R+R_\mathrm{iV}}. \tag{5.2}$$
:::

⁠**So liest man das:** $U_\mathrm{iA}$ ist der Spannungsabfall am Amperemeter, $I_\mathrm{iV}$ der Strom durch das Voltmeter. $f$ ist der Fehler von $U/I$ gegenüber $R$. Es ist nicht möglich, Strom und Spannung an einem Widerstand zugleich richtig abzulesen. Kennt man die Innenwiderstände, lässt sich das Ergebnis aber korrigieren: $R=U/I-R_\mathrm{iA}$ beziehungsweise $1/R=I/U-1/R_\mathrm{iV}$.

:::herleitung Quotient der Anzeigen
Stromrichtig: $U/I=(I_RR+I_RR_\mathrm{iA})/I_R=R+R_\mathrm{iA}$. Spannungsrichtig: $I/U=(I_R+I_\mathrm{iV})/U_R=1/R+1/R_\mathrm{iV}$, also $U/I=R\parallel R_\mathrm{iV}$ und $f=(R\parallel R_\mathrm{iV})/R-1=-R/(R+R_\mathrm{iV})$.
:::

::::beispiel
Das Rechenmodell in beiden Schaltungen:

|  | Anzeige $U$ | Anzeige $I$ | $U/I$ und Fehler |
|---|---|---|---|
| stromrichtig | 9,000 V (an $R$: 8,950 V) | 4,972 mA | 1810 $\Omega$, $+0{,}56\,\%$ |
| spannungsrichtig | 8,950 V | 5,017 mA (durch $R$: 4,972 mA) | 1783,9 $\Omega$, $-0{,}89\,\%$ |

Die rechnerische Korrektur führt in beiden Fällen auf 1800 $\Omega$ zurück.
::::

**Welche Schaltung?** Abb. [7](#abb-7) zeigt beide Fehler über $R$. Kleine Widerstände misst man spannungsrichtig, weil ihr Strom den des Voltmeters weit übertrifft. Große misst man stromrichtig, weil ihre Spannung den Abfall am Amperemeter weit übertrifft. Die Kurven kreuzen sich nahe 1,4 k$\Omega$ (Aufgabe [6](#aufg-6)). Bei 1,8 k$\Omega$ ist stromrichtig etwas besser.

:::abbildung et1/k4fehler 7
Betrag des relativen Fehlers von $U/I$ für $R_\mathrm{iA}=10\,\Omega$ und $R_\mathrm{iV}=200$ k$\Omega$, beide Achsen logarithmisch. Die Punkte gehören zum Rechenmodell.
:::

:::ltspice Beide Messschaltungen
⁠**Zeichnen:** Quelle `voltage` mit 9 V am Netz `q`. Das Amperemeter ist ein `res` mit 10, das Voltmeter ein `res` mit 200k. Stromrichtig: `RA1` von `q` nach `a`, `RX1` = 1.8k von `a` nach Masse, `RV1` von `q` nach Masse. Spannungsrichtig: `RA2` von `q` nach `b`, `RX2` = 1.8k und `RV2` von `b` nach Masse.

⁠**Direktiven:** `.op`

⁠**Was du siehst:** `I(RA1)` = 4,972 mA bei `V(q)` = 9 V, also 1810 $\Omega$. `I(RA2)` = 5,017 mA bei `V(b)` = 8,950 V, also 1783,9 $\Omega$. Setze dann die Werte aus Aufgabe [5](#aufg-5) ein und vergleiche.
:::

:::frage Warum misst man nicht nacheinander, erst Strom, dann Spannung?
Das hilft hier nicht. Allein im Kreis zeigt das Amperemeter wieder 4,972 mA, allein an $R$ zeigt das Voltmeter 9,000 V. Das Ergebnis ist 1810 $\Omega$ wie in der stromrichtigen Schaltung: Der eigene Fehler jedes Instruments bleibt.
:::

**Widerstand messen ohne Strommesser.** Ein Digitalmultimeter misst Widerstände deshalb anders. Eine genaue Konstantstromquelle (Stromquelle mit bekanntem, festem Strom) treibt den Strom $I_\mathrm q$ durch $R$, gemessen wird nur noch die Spannung: $R=U/I_\mathrm q\propto U$. Der Strom ist eine glatte Zehnerpotenz, sodass die Anzeige nur Komma und Vorsatz (Milli, Kilo, Mega) setzen muss: 1 mA an 1,8 k$\Omega$ ergibt 1,800 V, angezeigt als 1,800 k$\Omega$. Übrig bleibt der Fehler $R/(R+R_\mathrm{iV})$, bei 10 M$\Omega$ also 0,018 %. Bei kleinen Widerständen stören die Anschlussleitungen: 0,1 $\Omega$ Leitung an 0,5 $\Omega$ sind 20 %. Die Kelvin-Messung trennt deshalb die Wege: Zwei Leitungen führen den Strom, zwei weitere greifen die Spannung direkt am Bauteil ab. Durch diese fließt fast kein Strom, ihr Widerstand wirkt also nicht.

:::aufgabe Aufgabe 5 ★★ Welche Schaltung?
<span class="anker" id="aufg-5"></span>

Instrumente wie im Rechenmodell, Bereiche passend gewählt, Innenwiderstände unverändert. Berechne $U/I$ und $f$ in beiden Schaltungen für (a) $R=100\,\Omega$ an 0,9 V und (b) $R=180$ k$\Omega$ an 9 V. (c) Zeige, dass beide Korrekturformeln aus dem Rechenmodell 1800 $\Omega$ zurückgeben.

:::loesung
(a) Stromrichtig: $U/I=110\,\Omega$, $f=+10\,\%$. Spannungsrichtig: $U/I=100\,\Omega\parallel200\,\mathrm{k\Omega}=99{,}95\,\Omega$, $f=-0{,}05\,\%$.

(b) Stromrichtig: $U/I=180{,}01$ k$\Omega$, $f=+0{,}0056\,\%$. Spannungsrichtig: $U/I=180\,\mathrm{k\Omega}\parallel200\,\mathrm{k\Omega}=94{,}74$ k$\Omega$, $f=-47{,}4\,\%$: Durch das Voltmeter fließt fast so viel Strom wie durch $R$ (45 µ A gegen 50 µ A). Klein also spannungsrichtig, groß stromrichtig.

(c) $1810\,\Omega-10\,\Omega=1800\,\Omega$ und $1/(1/1783{,}94\,\Omega-1/200\,\mathrm{k\Omega})=1800\,\Omega$.
:::
:::

:::aufgabe Aufgabe 6 ★★★ Gleicher Fehler
<span class="anker" id="aufg-6"></span>

Für welches $R$ sind beide Fehler gleich groß? Berechne den exakten Wert und zeige, dass für $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$ näherungsweise $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$ gilt.

:::loesung
$R_\mathrm{iA}/R=R/(R+R_\mathrm{iV})$ führt auf $R^2-R_\mathrm{iA}R-R_\mathrm{iA}R_\mathrm{iV}=0$ mit der positiven Lösung

$$R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}}=1419\,\Omega.$$

Für $R\ll R_\mathrm{iV}$ wird aus der rechten Seite $R/R_\mathrm{iV}$, also $R^2\approx R_\mathrm{iA}R_\mathrm{iV}$ und $R\approx1414\,\Omega$. Beide Fehler betragen dort rund 0,7 %.
:::
:::
