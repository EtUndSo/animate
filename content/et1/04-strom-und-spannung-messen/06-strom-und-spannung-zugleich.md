---
title: Stufe 5: Strom und Spannung zugleich
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
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

::::formelsammlung
**Stromrichtige Messung**

$$I=I_R,\qquad U=U_R+U_\mathrm{iA},\qquad \frac UI=R+R_\mathrm{iA},\qquad f=+\frac{R_\mathrm{iA}}{R}$$

$U$ und $I$ sind die Anzeigen, $U_R$ und $I_R$ die Werte am Widerstand, $U_\mathrm{iA}$ der Spannungsabfall am Amperemeter; $f$ ist der Fehler von $U/I$ gegenüber $R$. Für große Widerstände.

**Spannungsrichtige Messung**

$$U=U_R,\qquad I=I_R+I_\mathrm{iV},\qquad \frac UI=R\parallel R_\mathrm{iV},\qquad f=-\frac{R}{R+R_\mathrm{iV}}$$

$I_\mathrm{iV}$ ist der Strom durch das Voltmeter. Für kleine Widerstände.

**Korrektur mit bekannten Innenwiderständen**

$$R=U/I-R_\mathrm{iA},\qquad 1/R=I/U-1/R_\mathrm{iV}$$

Links für die stromrichtige, rechts für die spannungsrichtige Schaltung.

**Gleicher Fehler beider Schaltungen**

$$R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}},\qquad R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$$

Aus $R_\mathrm{iA}/R=R/(R+R_\mathrm{iV})$; die Näherung gilt für $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$. Kleinere Widerstände misst man spannungsrichtig, größere stromrichtig.

**Widerstandsmessung mit Konstantstrom**

$$R=U/I_\mathrm q\propto U$$

Eine genaue Konstantstromquelle treibt den Strom $I_\mathrm q$ durch $R$, gemessen wird nur die Spannung; übrig bleibt der Fehler $R/(R+R_\mathrm{iV})$. Bei kleinen Widerständen trennt die Kelvin-Messung die Wege: zwei Leitungen für den Strom, zwei für die Spannung direkt am Bauteil.
::::

::::lernkarten
:::karte begriff stromrichtige Messung
Was kennzeichnet die stromrichtige Messung, wenn man einen Widerstand mit Amperemeter und Voltmeter zugleich misst?
---
Eine Messschaltung, in der das Voltmeter vor dem Amperemeter liegt: Das Amperemeter zählt genau den Strom durch $R$, $I=I_R$, aber das Voltmeter misst die Spannung an $R$ und am Amperemeter zusammen, $U=U_R+U_\mathrm{iA}$.
--- falsch
Eine Messschaltung, in der das Voltmeter direkt an $R$ liegt: Das Amperemeter zählt genau den Strom durch $R$, weil das Voltmeter keinen Strom aufnimmt, und auch die Spannung an $R$ stimmt dann genau.
--- falsch
Eine Messschaltung, in der das Amperemeter den Strom beider Zweige misst, $I=I_R+I_\mathrm{iV}$; dafür misst das Voltmeter genau die Spannung an $R$, also gilt $U=U_R$.
--- falsch
Eine Messschaltung, in der das Voltmeter vor dem Amperemeter liegt: Der Strom stimmt, $I=I_R$, und weil das Amperemeter ideal ist, stimmt auch die Spannung; $U/I$ ist exakt $R$.
:::
:::karte begriff spannungsrichtige Messung
Was kennzeichnet die spannungsrichtige Messung, wenn man einen Widerstand mit Amperemeter und Voltmeter zugleich misst?
---
Eine Messschaltung, in der das Voltmeter direkt an $R$ liegt: Die Spannung stimmt, $U=U_R$, aber das Amperemeter zählt den Strom des Voltmeters mit, $I=I_R+I_\mathrm{iV}$.
--- falsch
Eine Messschaltung, in der das Voltmeter vor dem Amperemeter liegt: Die Spannung stimmt, $U=U_R$, aber das Amperemeter zählt den Strom des Voltmeters nicht mit.
--- falsch
Eine Messschaltung, in der das Voltmeter direkt an $R$ liegt: Die Spannung stimmt, und weil durch das Voltmeter kein Strom fließt, stimmt auch der Strom; $U/I$ ist exakt $R$.
--- falsch
Eine Messschaltung, in der das Voltmeter direkt an der Quelle liegt: Es misst die Quellspannung, die sich nicht ändert, und das Amperemeter misst den Strom durch $R$ allein.
:::
:::karte formel Quotient bei stromrichtiger Messung
Welchen Wert liefert der Quotient $U/I$ der Anzeigen bei der stromrichtigen Messung, und wie groß ist sein relativer Fehler gegenüber $R$?
---
$\frac UI=R+R_\mathrm{iA}$ und $f=+\frac{R_\mathrm{iA}}{R}$: Der Quotient ist um den Innenwiderstand des Amperemeters zu groß, weil das Voltmeter dessen Spannungsabfall mitmisst.
--- falsch
$\frac UI=R-R_\mathrm{iA}$ und $f=-\frac{R_\mathrm{iA}}{R}$: Der Quotient ist um den Innenwiderstand des Amperemeters zu klein, weil an diesem Spannung verloren geht, die dem Voltmeter fehlt.
--- falsch
$\frac UI=R\parallel R_\mathrm{iA}$ und $f=-\frac{R_\mathrm{iA}}{R+R_\mathrm{iA}}$: Der Quotient ist zu klein, weil das Amperemeter neben dem Widerstand einen Nebenweg bildet.
--- falsch
$\frac UI=R+R_\mathrm{iA}$ und $f=+\frac{R}{R_\mathrm{iA}}$: Der Fehler ist umso kleiner, je kleiner $R$ gegenüber dem Innenwiderstand des Amperemeters ist.
:::
:::karte formel Quotient bei spannungsrichtiger Messung
Welchen Wert liefert der Quotient $U/I$ der Anzeigen bei der spannungsrichtigen Messung, und wie groß ist sein relativer Fehler gegenüber $R$?
---
$\frac UI=R\parallel R_\mathrm{iV}$ und $f=-\frac{R}{R+R_\mathrm{iV}}$: Der Quotient ist zu klein, weil das Amperemeter den Strom des Voltmeters mitzählt.
--- falsch
$\frac UI=R+R_\mathrm{iV}$ und $f=+\frac{R_\mathrm{iV}}{R}$: Der Quotient ist zu groß, weil der Innenwiderstand des Voltmeters zum Widerstand hinzukommt.
--- falsch
$\frac UI=R\parallel R_\mathrm{iV}$ und $f=-\frac{R_\mathrm{iV}}{R+R_\mathrm{iV}}$: Der Quotient ist zu klein, und zwar umso mehr, je größer der Innenwiderstand des Voltmeters ist.
--- falsch
$\frac UI=R$ und $f=0$: Weil die Spannung stimmt und ein Voltmeter keinen Strom aufnimmt, ist die spannungsrichtige Messung fehlerfrei.
:::
:::karte herleitung Quotient der Anzeigen
Leite ausgehend von den Anzeigen $U$ und $I$ für beide Messschaltungen den Quotienten $U/I$ und den Fehler der spannungsrichtigen Messung her.
---
Stromrichtig gilt $U/I=(I_RR+I_RR_\mathrm{iA})/I_R=R+R_\mathrm{iA}$, weil das Amperemeter genau $I_R$ zählt und das Voltmeter die Spannungen an $R$ und am Amperemeter zusammen misst.
---
Spannungsrichtig gilt $I/U=(I_R+I_\mathrm{iV})/U_R=1/R+1/R_\mathrm{iV}$, weil das Voltmeter genau $U_R$ misst und das Amperemeter den Strom durch beide Zweige zählt.
---
Also ist $U/I=R\parallel R_\mathrm{iV}$, weil sich die Leitwerte paralleler Zweige addieren.
---
Der Fehler ist $f=(R\parallel R_\mathrm{iV})/R-1=-R/(R+R_\mathrm{iV})$, weil $f$ die Abweichung von $U/I$ bezogen auf $R$ ist.
:::
:::karte formel Korrektur mit bekannten Innenwiderständen
Wie korrigiert man das Ergebnis $U/I$ der beiden Messschaltungen, wenn man die Innenwiderstände der Instrumente kennt?
---
Stromrichtig gilt $R=U/I-R_\mathrm{iA}$, spannungsrichtig $1/R=I/U-1/R_\mathrm{iV}$. Strom und Spannung lassen sich nicht zugleich richtig ablesen, das Ergebnis lässt sich aber berichtigen.
--- falsch
Stromrichtig gilt $R=U/I+R_\mathrm{iA}$, spannungsrichtig $1/R=I/U+1/R_\mathrm{iV}$. Man addiert jeweils den Beitrag des anderen Instruments, den die Anzeige verschluckt hat.
--- falsch
Stromrichtig gilt $R=U/I-R_\mathrm{iV}$, spannungsrichtig $R=U/I-R_\mathrm{iA}$. Man zieht jeweils den Innenwiderstand des Instruments ab, das falsch anzeigt.
--- falsch
Gar nicht: Weil immer eine der beiden Anzeigen falsch ist, lässt sich das Ergebnis auch mit bekannten Innenwiderständen nicht berichtigen, nur über die Wahl der Schaltung verbessern.
:::
:::karte zusammenhang Welche Schaltung
Warum misst man kleine Widerstände spannungsrichtig und große Widerstände stromrichtig?
---
Ein kleiner Widerstand führt einen Strom, der den des Voltmeters weit übertrifft; ein großer trägt eine Spannung, die den Abfall am Amperemeter weit übertrifft. So bleibt jeweils der Beitrag des anderen Instruments klein.
--- falsch
Ein kleiner Widerstand trägt eine Spannung, die den Abfall am Amperemeter weit übertrifft; ein großer führt einen Strom, der den des Voltmeters weit übertrifft. So bleibt jeweils der Beitrag des anderen Instruments klein.
--- falsch
Kleine Widerstände vertragen den Strom des Voltmeters nicht und müssen davor geschützt werden; große Widerstände würden dagegen das Amperemeter überlasten, wenn es nicht direkt vor ihnen läge.
--- falsch
Weil das Voltmeter an kleinen und das Amperemeter an großen Widerständen genauer abliest; der Fehler durch die Innenwiderstände ist dagegen in beiden Schaltungen gleich groß.
:::
:::karte formel Gleicher Fehler beider Schaltungen
Bei welchem Widerstand $R$ sind die Fehler der stromrichtigen und der spannungsrichtigen Messung gleich groß?
---
Exakt bei $R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}}$, für $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$ näherungsweise bei $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$. Mit 10 $\Omega$ und 200 k$\Omega$ liegt die Grenze nahe 1,4 k$\Omega$.
--- falsch
Beim Mittelwert der beiden Innenwiderstände, $R=(R_\mathrm{iA}+R_\mathrm{iV})/2$; mit 10 $\Omega$ und 200 k$\Omega$ liegt die Grenze nahe 100 k$\Omega$. Darunter misst man stromrichtig, darüber spannungsrichtig.
--- falsch
Näherungsweise bei $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$, mit 10 $\Omega$ und 200 k$\Omega$ nahe 1,4 k$\Omega$. Unterhalb davon ist die stromrichtige, oberhalb die spannungsrichtige Messung die bessere.
--- falsch
Bei keinem: Die stromrichtige Messung ist bei jedem Widerstand genauer, weil ihr Fehler $R_\mathrm{iA}/R$ wegen des kleinen Innenwiderstands des Amperemeters immer kleiner ist als der andere.
:::
:::karte zusammenhang Nacheinander messen
Warum hilft es nicht, Strom und Spannung an einem Widerstand nacheinander statt gleichzeitig zu messen?
---
Der eigene Fehler jedes Instruments bleibt: Allein im Kreis zeigt das Amperemeter wieder den gesenkten Strom, allein an $R$ zeigt das Voltmeter die volle Quellspannung. Das Ergebnis ist dasselbe wie bei der stromrichtigen Messung.
--- falsch
Es hilft: Nacheinander stört kein Instrument das andere, deshalb sind beide Anzeigen richtig, und $U/I$ ergibt genau $R$; die Messung dauert nur etwas länger als mit beiden Geräten zugleich, weil man zweimal umklemmen muss.
--- falsch
Weil sich die Quelle zwischen den beiden Messungen erholt und eine andere Spannung liefert; gleichzeitig gemessen liegt dagegen an beiden Instrumenten dieselbe Quellspannung an, und die Werte passen zusammen.
--- falsch
Weil das Amperemeter allein im Kreis den Strom erhöht und das Voltmeter allein die Spannung senkt; das Ergebnis ist dadurch schlechter als in jeder der beiden gemeinsamen Schaltungen, in denen sich die Fehler teilweise ausgleichen.
:::
:::karte zusammenhang Widerstandsmessung mit Konstantstrom
Wie misst ein Digitalmultimeter einen Widerstand, ohne dafür einen Strommesser zu brauchen?
---
Eine genaue Konstantstromquelle (Stromquelle mit bekanntem, festem Strom) treibt $I_\mathrm q$ durch $R$, gemessen wird nur die Spannung: $R=U/I_\mathrm q\propto U$. Weil der Strom eine glatte Zehnerpotenz ist, setzt die Anzeige nur Komma und Vorsatz.
--- falsch
Es legt seine Batteriespannung an $R$ und misst, wie schnell sie sinkt. Ein großer Widerstand entlädt die Batterie langsam, ein kleiner schnell; aus der Zeit, die das dauert, rechnet das Gerät den Widerstand mit einer eingebauten Tabelle aus.
--- falsch
Es legt eine feste Spannung an $R$ und misst nur den Strom: Bei festem $U$ ist die Anzeige dem Strom proportional, deshalb braucht es keinen Spannungsmesser, und der Fehler des Voltmeters entfällt.
--- falsch
Es vergleicht $R$ mit einem eingebauten Referenzwiderstand, indem es beide abwechselnd an die Anzeige legt und den Unterschied der Helligkeit misst; Strom und Spannung spielen dabei keine Rolle.
:::
:::karte begriff Kelvin-Messung
Was ist die Kelvin-Messung, und warum braucht man sie bei kleinen Widerständen?
---
Eine Widerstandsmessung mit getrennten Wegen: Zwei Leitungen führen den Strom, zwei weitere greifen die Spannung direkt am Bauteil ab. Durch diese fließt fast kein Strom, ihr Widerstand wirkt nicht; sonst wären 0,1 $\Omega$ Leitung an 0,5 $\Omega$ schon 20 %.
--- falsch
Eine Widerstandsmessung bei sehr tiefer Temperatur, bei der die Leitungen keinen Widerstand mehr haben; so stören die 0,1 $\Omega$ der Anschlussleitungen auch an einem Bauteil von 0,5 $\Omega$ nicht mehr. Daher hat sie den Namen der Temperatureinheit.
--- falsch
Eine Widerstandsmessung mit zwei Leitungen, die man nacheinander vertauscht; aus beiden Anzeigen bildet man den Mittelwert, und der Widerstand der Leitungen hebt sich dabei heraus, gleich wie klein das Bauteil ist.
--- falsch
Eine Widerstandsmessung mit vier Leitungen, die alle den Strom führen; weil sich der Strom auf vier Wege verteilt, sinkt der Einfluss der Leitungen auf ein Viertel des Werts mit zwei Leitungen, was auch bei 0,5 $\Omega$ genügt.
:::
::::
