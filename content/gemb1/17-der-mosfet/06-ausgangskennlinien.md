---
title: Stufe 4: Ausgangskennlinien
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270600
summary: Die Parabel (3.2) hat einen Scheitel und würde danach fallen.
tags: Abschnürung, Sättigung, Sättigungsspannung, Sättigungsstrom, Triodenbereich, ohmsche Bereich
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Parabel [(3.2)](gradual-channel-approximation.html#gl-3-2) hat einen Scheitel und würde danach fallen. Diese Stufe klärt, was dort im Kanal geschieht, und zeigt das ganze Kennlinienfeld.
:::

**Die Idee.** Mit wachsendem $V_\mathrm{DS}$ sinkt die Spannung zwischen Gate und Kanal am Drain-Ende. Erreicht sie $V_\mathrm{th}$, verschwindet dort die Inversionsschicht. Der Kanal ist abgeschnürt, das ist die __Abschnürung__ (englisch pinch-off). Noch größeres $V_\mathrm{DS}$ schiebt den Abschnürpunkt nur ein kurzes Stück zur Source. Die zusätzliche Spannung fällt auf der verarmten Strecke vor dem Drain ab. Der Kanal selbst sieht weiter dieselbe Spannung, also bleibt der Strom gleich. Das ist die __Sättigung__. Sie passt zu Stufe [2](die-barriere-im-kanal.html#stufe-2): Nur die Source liefert noch Elektronen, und wie viele, bestimmt das Gate.

:::analogie
Ein Fluss stürzt über eine Kante. Wie viel Wasser je Sekunde fällt, legt der Lauf oberhalb fest, nicht die Fallhöhe. Der Lauf ist der Kanal, die Kante der Abschnürpunkt, die Fallhöhe $V_\mathrm{DS}-V_\mathrm{DS,sat}$. Das Bild stimmt nicht mehr, sobald die Kante wandert: Der Abschnürpunkt rückt mit $V_\mathrm{DS}$ ein Stück zur Source.
:::

:::satz Satz 4.1 (Sättigung)
<span class="anker" id="satz-4-1"></span>

Die __Sättigungsspannung__ und der __Sättigungsstrom__ sind

<span class="anker" id="gl-4-1"></span>
$$V_\mathrm{DS,sat}=V_\mathrm{GS}-V_\mathrm{th},\qquad I_\mathrm{D,sat}=\frac K2\bigl(V_\mathrm{GS}-V_\mathrm{th}\bigr)^2. \tag{4.1}$$
:::

:::herleitung Scheitel der Parabel
Aus [(3.2)](gradual-channel-approximation.html#gl-3-2) folgt $\mathrm{d} I_\mathrm D/\mathrm{d} V_\mathrm{DS}=K(V_\mathrm{GS}-V_\mathrm{th}-V_\mathrm{DS})$. Weil $K\ne0$ ist, liegt der Scheitel bei $V_\mathrm{DS}=V_\mathrm{GS}-V_\mathrm{th}$. Dort ist nach [(3.1)](gradual-channel-approximation.html#gl-3-1) $Q'_\mathrm{inv}(L)=0$. Das ist die Abschnürung. Einsetzen in [(3.2)](gradual-channel-approximation.html#gl-3-2) gibt $I_\mathrm{D,sat}$. Der fallende Ast rechts davon existiert nicht, denn [(3.1)](gradual-channel-approximation.html#gl-3-1) würde dort am Drain positive bewegliche Ladung ergeben.
:::

| Bereich | Bedingung | Drainstrom |
|---|---|---|
| Aus-Zustand | $V_\mathrm{GS}<V_\mathrm{th}$ | $I_\mathrm D\approx0$ |
| ohmscher Bereich | $V_\mathrm{DS}\ll V_\mathrm{GS}-V_\mathrm{th}$ | $I_\mathrm D\approx K(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}$ |
| ungesättigter Bereich | $V_\mathrm{DS}\le V_\mathrm{GS}-V_\mathrm{th}$ | $I_\mathrm D=K\bigl[(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}-\frac12V_\mathrm{DS}^2\bigr]$ |
| Sättigungsbereich | $V_\mathrm{DS}>V_\mathrm{GS}-V_\mathrm{th}$ | $I_\mathrm D=\frac K2(V_\mathrm{GS}-V_\mathrm{th})^2$ |

⁠**So liest man das:** Die letzten drei Zeilen gelten für $V_\mathrm{GS}>V_\mathrm{th}$. Der ungesättigte Bereich heißt auch __Triodenbereich__, weil der Strom dort wie in einer Elektronenröhre von beiden Spannungen abhängt. Der __ohmsche Bereich__ ist sein Anfang. Dort ist der MOSFET ein Widerstand, den $V_\mathrm{GS}$ steuert:

<span class="anker" id="gl-4-2"></span>
$$R=\frac{V_\mathrm{DS}}{I_\mathrm D}=\frac1{K(V_\mathrm{GS}-V_\mathrm{th})}. \tag{4.2}$$

Sein Fehler ist $V_\mathrm{DS}/(2(V_\mathrm{GS}-V_\mathrm{th}))$. $I_\mathrm{D,sat}$ heißt auch $I_\mathrm{DSS}$. **Gültigkeit:** wie in Stufe [3](gradual-channel-approximation.html#stufe-3), zusätzlich muss die verarmte Strecke kurz gegen $L$ sein.

:::abbildung gemb1/k17ausgang 4
Links: Ausgangskennlinien des Rechenmodells. Rot gepunktet die Grenze $V_\mathrm{DS}=V_\mathrm{DS,sat}$, grau unterlegt der ungesättigte Bereich, rote Geraden die ohmsche Näherung, grau gestrichelt der fallende Ast der Parabel, den es nicht gibt. Rechts: Kanal (blau) bei $V_\mathrm{GS}=3$ V, Dicken schematisch. Er wird zum Drain dünner, ist bei $V_\mathrm{DS,sat}$ dort abgeschnürt und endet darüber kurz davor.
:::

::::beispiel
Das Rechenmodell ergibt:

| $V_\mathrm{GS}$ in V | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $V_\mathrm{DS,sat}$ in V | 0,677 | 1,677 | 2,677 | 3,677 |
| $I_\mathrm{D,sat}$ in mA | 0,198 | 1,21 | 3,09 | 5,84 |
| $R$ in $\Omega$ | 1712 | 691 | 433 | 315 |

Gleiche Schritte von $V_\mathrm{GS}$ geben wachsende Abstände der Kurven, denn der Strom ist quadratisch. Bei $V_\mathrm{GS}=3$ V und $V_\mathrm{DS}=5$ V liegen 2,32 V auf der verarmten Strecke. Nach der Kastenformel ist sie rund 320 nm lang, das sind 6 % von $L$.
::::

⁠**Grenzfall:** Bei $V_\mathrm{DS}=0{,}1$ V und $V_\mathrm{GS}=3$ V weicht die ohmsche Gerade nur um 1,9 % ab.

:::frage Wenn der Kanal abgeschnürt ist, warum fließt dann überhaupt noch Strom?
Abgeschnürt heißt nicht unterbrochen. An der Stelle hat nur die Inversionsschicht ihre gebundene Dichte verloren. Hinter ihr liegt eine verarmte Strecke mit starkem Feld zum Drain, rund 15 MV/m im Beispiel. Jedes ankommende Elektron wird mitgerissen, so wie die Zone eines gesperrten p-n-Übergangs Minoritätsträger abzieht ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)).
:::

:::zusatz Wie genau ist das quadratische Gesetz?
Bedingung (4) ist nur genähert. Zum Drain hin wächst die Verarmungszone, denn dort ist $\varphi_\mathrm s$ um $V(y)$ größer. Mit dieser Ladung sinkt $I_\mathrm{D,sat}$ im Rechenmodell bei $V_\mathrm{GS}=3$ V von 3,09 auf 2,48 mA. Außerdem steigt $\varphi_\mathrm s$ über $V_\mathrm{th}$ noch etwas weiter ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)). Eine numerische Rechnung mit beidem und mit Diffusion gibt 2,15 mA. Die Form der Kennlinien bleibt. In der Praxis passt man $K$ und $V_\mathrm{th}$ an Messungen an.
:::

:::aufgabe Aufgabe 4 ★ Bereiche bestimmen
<span class="anker" id="aufg-4"></span>

Ein MOSFET hat $K=2$ mA/V$^2$ und $V_\mathrm{th}=0{,}8$ V, es ist $V_\mathrm{GS}=2$ V.

<ol class="al">

<li>

Für welche $V_\mathrm{DS}$ liegt er im ungesättigten Bereich, für welche in Sättigung?

</li>

<li>

Berechne $I_\mathrm D$ für $V_\mathrm{DS}=0{,}05$, 0,8, 1,2 und 3 V und nenne jeweils den Bereich.

</li>

<li>

Wie groß ist $R$ im ohmschen Bereich? Was gilt bei $V_\mathrm{GS}=0{,}6$ V?

</li>

</ol>

:::loesung
(a) $V_\mathrm{DS,sat}=1{,}2$ V. Ungesättigt für $V_\mathrm{DS}\le1{,}2$ V, darüber Sättigung. (b) 0,05 V: 0,1175 mA, ohmsch (Näherung 0,120 mA). 0,8 V: 1,28 mA, ungesättigt. 1,2 V: 1,44 mA, am Übergang. 3 V: 1,44 mA, Sättigung. (c) $R=1/(2\,\mathrm{mA/V^2}\cdot1{,}2\,\mathrm{V})=417\,\Omega$. Bei $V_\mathrm{GS}=0{,}6$ V liegt er unter der Schwelle: Aus-Zustand, nach dem Modell $I_\mathrm D\approx0$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Einen Transistor auslegen
<span class="anker" id="aufg-5"></span>

Eine Fertigung bietet 12 nm $\mathrm{SiO_2}$, $L=2{,}5$ µ m, $\mu_\mathrm n=420\,\mathrm{cm^2/(V\,s)}$ und $V_\mathrm{th}=0{,}5$ V.

<ol class="al">

<li>

Bei $V_\mathrm{GS}=1{,}2$ V soll der Sättigungsstrom 50 µ A sein. Berechne $W$ und $K$.

</li>

<li>

Berechne $V_\mathrm{DS,sat}$ und $I_\mathrm{D,sat}$ für $V_\mathrm{GS}=0{,}7$, 0,8, 0,9, 1,0 und 1,2 V und skizziere das Kennlinienfeld.

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=287{,}8\,\mathrm{nF/cm^2}$, $\mu_\mathrm nC'_\mathrm{IS}=120{,}9$ µ A/V$^2$. Aus $I_\mathrm{D,sat}=\frac K2\cdot(0{,}7\,\mathrm{V})^2$ folgt $K=204$ µ A/V$^2$, also $W/L=1{,}69$ und $W=4{,}22$ µ m. (b) $V_\mathrm{DS,sat}=0{,}2$, 0,3, 0,4, 0,5, 0,7 V und $I_\mathrm{D,sat}=4{,}1$, 9,2, 16,3, 25,5, 50,0 µ A. Das Feld sieht aus wie Abb. [4](#abb-4), die Scheitel liegen auf der Parabel $I=\frac K2V_\mathrm{DS}^2$.
:::
:::
