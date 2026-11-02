---
title: Stufe 7: Die verstimmte Brücke
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom und Spannung messen
order: 1140800
summary: Ändert sich ein Widerstand nur wenig oder laufend, stellt man nicht nach.
tags: Dehnungsmessstreifen
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ändert sich ein Widerstand nur wenig oder laufend, stellt man nicht nach. Die Abweichung von null ist dann das Messsignal. Diese Stufe zeigt, warum so kleinste Änderungen sichtbar werden.
:::

**Die Idee.** Ein Instrument allein muss die ganze Spannung anzeigen, die Änderung ist davon ein winziger Teil. Die Brücke zieht die große gemeinsame Spannung ab. Übrig bleibt nur die Änderung, und die passt in einen kleinen Messbereich. Weil der Anzeigefehler am Bereichsendwert hängt, sinkt er mit dem Bereich.

:::satz Satz 7.1 (Brückenspannung)
<span class="anker" id="satz-7-1"></span>

Zwischen den Mittelpunkten liegt $U_\mathrm d=U_4-U_2$ mit den Spannungen $U_2$ an $R_2$ und $U_4$ an $R_4$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}. \tag{7.1}$$

Für $R_1=R_2=R_3=R$ und $R_4=R+\Delta R$ gilt

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}\qquad\text{für }\Delta R\ll R. \tag{7.2}$$
:::

⁠**So liest man das:** Der Zähler in [(7.1)](#gl-7-1) wird im Abgleich null. $\Delta R/R$ ist die relative Änderung, ohne Einheit. **Gültigkeit:** Das Voltmeter entnimmt keinen merklichen Strom. **Grenzfälle:** $\Delta R=0$ ergibt $U_\mathrm d=0$. $\Delta R\to\infty$ ergibt $U_\mathrm d\to U_\mathrm q/2$: Der rechte Mittelpunkt liegt dann am Pluspol.

:::herleitung Kleine Änderung
Mit $U_2=U_\mathrm q/2$ und $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$ ist

$$U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}.$$
:::

:::abbildung et1/k4dms 9
Links die Brücke mit dem veränderlichen $R_4$. Rechts dieselbe Änderung auf zwei Skalen: rote Linie die Anzeige, helles Band der Anzeigefehler. Auf der 10-V-Skala geht eine Änderung um 9 mV im Fehler unter. Auf der 100-mV-Skala ist die Abweichung selbst das Signal.
:::

**Beispiel: Dehnungsmessstreifen.** Ein __Dehnungsmessstreifen__ ist eine dünne Metallbahn, die auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, wird die Bahn länger und dünner, und ihr Widerstand $R=\rho\,l/A$ steigt. Die relative Widerstandsänderung beträgt etwa das Doppelte der Dehnung. Bei 2 ‰ Dehnung wächst $R_4$ um 0,4 % von 350 $\Omega$ auf 351,4 $\Omega$. Dann ist $U_2=4{,}500$ V und $U_4=9\,\mathrm{V}\cdot351{,}4/701{,}4=4{,}509$ V, also $U_\mathrm d=8{,}98$ mV. Die Näherung gibt 9,00 mV, sie weicht um 0,2 % ab. Am 10-M$\Omega$-Voltmeter fließen 0,9 nA, gegen 12,9 mA in den Zweigen ein Anteil von $7\cdot10^{-8}$: vernachlässigbar.

**Warum das genauer ist.** Direkt gemessen müsste das Instrument 4,509 V von 4,500 V unterscheiden, also im 10-V-Bereich drei Stellen hinter dem Komma sicher anzeigen. Sein Anzeigefehler von $\pm100$ mV ist aber das Elffache der gesuchten Änderung. An der Brücke reicht der 100-mV-Bereich mit $\pm1$ mV, ein Hundertstel davon (Abb. [9](#abb-9)). Dazu kommen zwei Vorteile. Schwankt die Quelle um 1 %, ändert sich $U_4$ um 45 mV, das Fünffache des Signals, $U_\mathrm d$ dagegen nur um 0,09 mV. Und ändern sich alle vier Widerstände um denselben Faktor, etwa durch Wärme, bleibt $U_\mathrm d$ gleich.

:::frage Könnte man nicht $U_4$ messen und im Kopf 4,5 V abziehen?
Rechnen lässt sich das, aber die $\pm100$ mV Anzeigefehler bleiben im Ergebnis. Die Brücke zieht ab, bevor das Instrument misst. Deshalb darf es einen kleinen Bereich haben.
:::

⁠**Von hier an:** Wenn nichts anderes dasteht, gelten Messgeräte in allen folgenden Teilen als ideal: Amperemeter mit $R_\mathrm i\to0$, Voltmeter mit $R_\mathrm i\to\infty$.

:::aufgabe Aufgabe 8 ★★★ Zwei Messstreifen
<span class="anker" id="aufg-8"></span>

Im rechten Zweig sitzen nun zwei Messstreifen: $R_3=R-\Delta R$ wird gestaucht, $R_4=R+\Delta R$ gedehnt, $R_1=R_2=R$. (a) Berechne $U_\mathrm d$ allgemein und für das Beispiel. (b) Warum ist das Ergebnis exakt linear in $\Delta R$? (c) Was ändert sich, wenn sich alle vier Widerstände durch Wärme um 1 % ändern?

:::loesung
(a) $R_3+R_4=2R$, also $U_4=U_\mathrm q(R+\Delta R)/(2R)$. Mit $U_2=U_\mathrm q/2$ folgt $U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R=4{,}5\,\mathrm{V}\cdot0{,}004=18{,}0$ mV, doppelt so viel wie mit einem Streifen.

(b) Die Summe $R_3+R_4$ bleibt $2R$. Der Strom im rechten Zweig bleibt deshalb 12,9 mA, und $U_4$ wächst genau mit $R_4$. Bei einem Streifen wächst die Summe mit, das ergibt den Nenner in [(7.2)](#gl-7-2).

(c) Nichts: In [(7.1)](#gl-7-1) kürzt sich ein gemeinsamer Faktor aller Widerstände heraus.
:::
:::
