---
title: Stufe 9: Aufladen über einen Widerstand
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1131000
summary: An einer Spannungsquelle hängt der Ladestrom von der Kondensatorspannung ab, und die hängt vom Ladestrom ab.
tags: Kurzschluss, Unterbrechung, Differenzialgleichung
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
An einer Spannungsquelle hängt der Ladestrom von der Kondensatorspannung ab, und die hängt vom Ladestrom ab. Diese Stufe stellt die Gleichung für diese Rückkopplung auf und löst sie von Grund auf.
:::

**Die Idee.** Im RC-Kreis (Abb. [9](#abb-9)) legt der Schalter S bei $t=0$ von Stellung 2 auf 1 um, der Kondensator ist leer. Die Spannung kann nicht springen (Stufe [3](strom-und-spannung-am-kondensator.html#stufe-3)), also ist $u_C(0)=0$. Die ganze Batteriespannung liegt an $R$, und es fließt $i(0)=U_0/R=0{,}9$ mA. Für diesen Moment verhält sich der Kondensator wie ein Draht, daher das Wort __Kurzschluss__: Strom fließt, die Spannung ist null. Der Grund: Noch ist keine Ladung getrennt, also gibt es kein Feld, das dem Strom entgegenwirkt.

Der Strom bringt Ladung, $u_C$ steigt. Nach der Maschenregel bleibt für $R$ weniger, der Strom sinkt, und $u_C$ steigt langsamer. Diese Rückkopplung formt die ganze Kurve. Am Ende ist $u_C=U_0$. An $R$ liegt nichts mehr, $i=0$: Der Kondensator verhält sich wie eine __Unterbrechung__, die Anschlüsse wirken offen. Der Grund: Das Feld der getrennten Ladung hebt die Platte auf das Potenzial des Pols, längs $R$ bleibt kein Gefälle.

:::abbildung et1/k3rckreis 9
Links der RC-Kreis mit Zählpfeilen, Maschenregel $U_0=u_R+u_C$. Stellung 1 lädt, Stellung 2 entlädt. Rechts die beiden Ersatzbilder: Bei $t=0$ wirkt der leere Kondensator wie ein Draht, nach langer Zeit der volle wie offene Klemmen.
:::

**Die Gleichung.** Die Maschenregel ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) lautet $U_0=u_R+u_C$. Mit dem ohmschen Gesetz $u_R=R\,i$ und mit $i=C\,\mathrm{d} u_C/\mathrm{d} t$ aus [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) folgt

<span class="anker" id="gl-9-1"></span>
$$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C. \tag{9.1}$$

Das ist eine __Differenzialgleichung__: eine Gleichung, in der die gesuchte Größe zusammen mit ihrer Ableitung steht. Gesucht ist keine Zahl, sondern eine ganze Funktion $u_C(t)$. Umgestellt mit $\tau=RC$ lautet sie

<span class="anker" id="gl-9-2"></span>
$$\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}. \tag{9.2}$$

In Worten: Die Steigung der Kurve ist der Abstand zum Endwert, geteilt durch $\tau$. Zu jedem Punkt $(t,u_C)$ liegt also eine Steigung fest (Abb. [10](#abb-10)). Wer beim Startwert beginnt und überall dieser Steigung folgt, zeichnet die Lösung. Darum gehört zu jedem Startwert genau eine Kurve.

:::abbildung et1/k3richtung 10
Gleichung [(9.2)](#gl-9-2) im Bild: Jeder graue Strich zeigt die Steigung an dieser Stelle, für $U_0=9$ V und $\tau=1$ s. Weit unter 9 V ist sie groß, bei 9 V null, darüber negativ. Die Kurven folgen den Strichen von den Startwerten 0 V, 3 V und 12 V aus und nähern sich alle demselben Endwert.
:::

:::satz Satz 9.1 (Aufladen)
<span class="anker" id="satz-9-1"></span>

Für $u_C(0)=0$ und $t\ge0$ gilt

<span class="anker" id="gl-9-3"></span>
$$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr),\qquad i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad\tau=R\,C. \tag{9.3}$$
:::

⁠**So liest man das:** $\mathrm{e}=2{,}718$ ist die Eulersche Zahl. $\tau$ ist die Zeitkonstante in s: $\mathrm{\Omega\cdot F}=\frac{\mathrm V}{\mathrm A}\cdot\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm s$. Der Faktor $\mathrm{e}^{-t/\tau}$ beginnt bei 1 und fällt in jeder Zeit $\tau$ auf das $1/\mathrm{e}$-Fache, also auf 36,8 %. **Gültigkeit:** ideale Bauteile, konstante Quelle, $t=0$ ist der Moment des Schaltens.

:::herleitung Die Gleichung von Grund auf lösen
⁠**Schritt 1: Nur der Abstand zum Ende zählt.** Setze $x(t)=U_0-u_C(t)$. Weil $U_0$ konstant ist, gilt $\mathrm{d} x/\mathrm{d} t=-\mathrm{d} u_C/\mathrm{d} t$, und aus [(9.2)](#gl-9-2) wird

$$\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac{x}{\tau},\qquad x(0)=U_0.$$

Die Änderung von $x$ ist proportional zu $x$ selbst: Je größer der Rest, desto schneller schrumpft er.

⁠**Schritt 2: Durch $x$ teilen.** Für $x>0$ ist $\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac1\tau$. Die linke Seite ist nach der Kettenregel die Ableitung von $\ln x(t)$, denn $\frac{\mathrm{d}}{\mathrm{d} t}\ln x(t)=\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}$.

⁠**Schritt 3: Integrieren.** $\ln x(t)$ hat also die konstante Steigung $-1/\tau$ und ist eine Gerade: $\ln x(t)=-t/\tau+K$ mit einer Konstanten $K$.

⁠**Schritt 4: Logarithmus auflösen.** Die e-Funktion auf beide Seiten angewandt ergibt $x(t)=\mathrm{e}^{K}\,\mathrm{e}^{-t/\tau}$. Für $t=0$ steht dort $x(0)=\mathrm{e}^{K}$, also ist $\mathrm{e}^{K}=U_0$. Damit ist $x(t)=U_0\,\mathrm{e}^{-t/\tau}$.

⁠**Schritt 5: Zurückrechnen.** $u_C=U_0-x=U_0(1-\mathrm{e}^{-t/\tau})$. Ableiten: $i=C\,\mathrm{d} u_C/\mathrm{d} t=\frac{C\,U_0}{\tau}\mathrm{e}^{-t/\tau}=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$, und $u_R=R\,i$.

⁠**Probe:** Einsetzen in [(9.1)](#gl-9-1) ergibt $R\,C\cdot\frac{U_0}{\tau}\mathrm{e}^{-t/\tau}+U_0-U_0\mathrm{e}^{-t/\tau}=U_0$. Stimmt.

⁠**Derselbe Weg über den Strom:** Aus $U_0=R\,i+\frac1C\int_0^ti\,\mathrm{d} t'$ folgt durch Ableiten $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$. Kurz geschrieben ist das $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, und Schritt 2 bis 4 liefern $\ln i=-\frac{t}{RC}+\ln\frac{U_0}{R}$, also wieder $i=\frac{U_0}{R}\mathrm{e}^{-t/RC}$.
:::

::::beispiel
Im Rechenmodell ist nach $t=1$ s $u_C=9\,\mathrm{V}\cdot(1-\mathrm{e}^{-1})=5{,}69$ V, $u_R=3{,}31$ V und $i=0{,}331$ mA (Abb. [11](#abb-11)). Beide Spannungen ergeben zu jeder Zeit 9 V. Die Tangente am Start steigt mit $U_0/\tau=9$ V/s und erreicht 9 V genau bei $t=\tau$: Bliebe der Anfangsstrom konstant wie in Stufe [3](strom-und-spannung-am-kondensator.html#stufe-3), wäre der Kondensator nach $\tau$ voll.
::::

⁠**Kurz gesagt:** $\tau$ ist die Endladung geteilt durch den Anfangsstrom, $C\,U_0/(U_0/R)=RC$.

:::abbildung et1/k3laden 11
Aufladen mit $U_0=9$ V, $R=10\,\mathrm{k\Omega}$ und $C=100\,\mu\text{F}$. Links die Spannungen, rechts der Strom. Der Strom springt bei $t=0$ von null auf 0,9 mA und klingt ab. Die Tangenten am Start treffen bei $t=\tau=1$ s den Endwert. Die Punkte gehören zu $t=\tau$.
:::

⁠**Grenzfälle:** Für $t\to0$ wird $\mathrm{e}^{-t/\tau}\to1$: $u_C=0$, $i=U_0/R$, das ist der Kurzschluss. Für $t\to\infty$ wird $\mathrm{e}^{-t/\tau}\to0$: $u_C=U_0$, $i=0$, das ist die Unterbrechung. Für $R\to0$ geht $\tau\to0$ und $i(0)\to\infty$. Bei realen 0,1 $\Omega$ Leitungswiderstand wären es 90 A für 10 µs.

:::frage Wird der Kondensator jemals ganz voll?
Rechnerisch nie, denn $\mathrm{e}^{-t/\tau}$ erreicht null nicht. Praktisch nach wenigen $\tau$: Nach $5\tau$ fehlen 0,7 %, im Rechenmodell 61 mV. Der Ladestrom beträgt dann noch 6 µA und liegt in der Größenordnung des Leckstroms aus Stufe [5](bauformen-und-selbstentladung.html#stufe-5).
:::

:::aufgabe Aufgabe 10 ★★ Ein anderer RC-Kreis
<span class="anker" id="aufg-10"></span>

Eine Quelle mit 12 V lädt über 4,7 k$\Omega$ einen leeren Kondensator mit 220 µF.

<ol class="al">

<li>

Berechne $\tau$ und $i(0)$.

</li>

<li>

Wie groß ist $u_C$ nach 1 s?

</li>

<li>

Wann erreicht $u_C$ die Hälfte von 12 V, wann 99 %?

</li>

<li>

Sage vorher: Was ändert sich an $\tau$ und an $i(0)$, wenn $R$ verdoppelt wird, was an der Endspannung?

</li>

</ol>

:::loesung
(a) $\tau=4{,}7\,\mathrm{k\Omega}\cdot220\,\mu\text{F}=1{,}034$ s, $i(0)=12\,\mathrm{V}/4{,}7\,\mathrm{k\Omega}=2{,}55$ mA.

(b) $u_C=12\,\mathrm{V}\cdot(1-\mathrm{e}^{-1/1{,}034})=7{,}44$ V.

(c) $\mathrm{e}^{-t/\tau}=\frac12$ ergibt $t=\tau\ln2=0{,}717$ s. Für 99 % ist $\mathrm{e}^{-t/\tau}=0{,}01$, also $t=\tau\ln100=4{,}76$ s.

(d) $\tau$ verdoppelt sich, $i(0)$ halbiert sich, die Endspannung bleibt 12 V, denn am Ende fließt kein Strom mehr durch $R$.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Die Energiebilanz des Ladens
<span class="anker" id="aufg-11"></span>

Der Kondensator im RC-Kreis wird von 0 auf $U_0$ geladen.

<ol class="al">

<li>

Zeige mit $W_\mathrm{B}=\int_0^\infty U_0\,i\,\mathrm{d} t$, dass die Batterie $C\,U_0^2$ abgibt.

</li>

<li>

Zeige mit $W_R=\int_0^\infty R\,i^2\,\mathrm{d} t$, dass im Widerstand $\frac12CU_0^2$ zu Wärme wird. Gib die Zahlen im Rechenmodell an.

</li>

<li>

Warum kommt $R$ im Ergebnis nicht vor, obwohl der ganze Verlust in $R$ entsteht?

</li>

</ol>

:::loesung
(a) $W_\mathrm{B}=U_0\int_0^\infty i\,\mathrm{d} t=U_0\,Q=C\,U_0^2$, denn das Integral des Stroms ist die Ladung. Rechenweg: $\int_0^\infty\frac{U_0}{R}\mathrm{e}^{-t/\tau}\mathrm{d} t=\frac{U_0}{R}\tau=C\,U_0$.

(b) $W_R=\int_0^\infty R\,\frac{U_0^2}{R^2}\mathrm{e}^{-2t/\tau}\mathrm{d} t=\frac{U_0^2}{R}\cdot\frac\tau2=\frac12CU_0^2$. Rechenmodell: Die Batterie liefert 8,10 mJ, je 4,05 mJ gehen in den Kondensator und in den Widerstand.

(c) Kleineres $R$ erhöht den Strom, verkürzt aber die Zeit. In $W_R=\frac{U_0^2}{R}\cdot\frac{\tau}{2}=\frac{U_0^2}{R}\cdot\frac{RC}{2}$ kürzt sich $R$ deshalb genau heraus. Der Wirkungsgrad des Ladens aus einer festen Spannung ist immer 50 %, solange der Kondensator von null startet. Dieselbe Rechnung steckt im Verlust [(8.3)](ladungserhaltung-beim-umschalten.html#gl-8-3).
:::
:::
