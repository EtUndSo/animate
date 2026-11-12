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

::::formelsammlung
**Gleichung des RC-Kreises**

$$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C$$

Aus der Maschenregel $U_0=u_R+u_C$ mit $u_R=R\,i$ und $i=C\,\mathrm{d} u_C/\mathrm{d} t$. Eine Differenzialgleichung: Gesucht ist die Funktion $u_C(t)$.

**Steigung der Ladekurve**

$$\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}$$

Die Steigung ist der Abstand zum Endwert, geteilt durch $\tau$; zu jedem Startwert gehört genau eine Kurve.

**Aufladen**

$$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr),\qquad i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad\tau=R\,C$$

Für $u_C(0)=0$ und $t\ge0$; ideale Bauteile, konstante Quelle, $t=0$ ist der Moment des Schaltens. Leer wirkt der Kondensator im ersten Moment wie ein Kurzschluss, $i(0)=U_0/R$; voll wie eine Unterbrechung, $i=0$.

**Zeitkonstante aus dem Anfangsstrom**

$$C\,U_0/(U_0/R)=RC$$

$\tau$ ist die Endladung geteilt durch den Anfangsstrom: Die Tangente am Start erreicht den Endwert genau bei $t=\tau$.

**Zeit bis zu einem Ladestand**

$$t=\tau\ln2,\qquad t=\tau\ln100$$

Aus $\mathrm{e}^{-t/\tau}=\frac12$ bzw. $\mathrm{e}^{-t/\tau}=0{,}01$: Zeit bis zur halben Endspannung bzw. bis 99 % der Endspannung.

**Energiebilanz des Ladens**

$$W_\mathrm{B}=C\,U_0^2,\qquad W_R=\frac12CU_0^2$$

Ab $u_C=0$ gibt die Batterie $C\,U_0^2$ ab; je die Hälfte geht in den Kondensator und als Wärme in den Widerstand, unabhängig von $R$. Der Wirkungsgrad des Ladens aus einer festen Spannung ist 50 %.
::::

::::lernkarten
:::karte begriff RC-Kreis
Was ist ein RC-Kreis, und wie lädt und entlädt man darin den Kondensator?
---
Die Reihenschaltung aus Widerstand und Kondensator an einer Quelle. Ein Schalter legt in einer Stellung die Quelle an (Laden) und schließt in der anderen den Kreis ohne Quelle über $R$ (Entladen).
--- falsch
Die Parallelschaltung aus Widerstand und Kondensator an einer Quelle. Der Widerstand entlädt den Kondensator laufend, während die Quelle ihn im selben Moment wieder auflädt; seine Spannung bleibt so konstant.
--- falsch
Die Reihenschaltung aus Widerstand und Kondensator ganz ohne Quelle. Der Kondensator gibt seine Ladung im Kreis an den Widerstand ab und bekommt sie von dort wieder zurück.
--- falsch
Ein Kreis, in dem ein Widerstand vor dem Kondensator dessen Kapazität erhöht, damit dieser bei gleicher Spannung mehr Ladung aufnimmt, als er ohne Widerstand könnte.
:::
:::karte begriff Kurzschluss und Unterbrechung
Wie verhält sich ein Kondensator im RC-Kreis im ersten Moment des Ladens und nach langer Zeit?
---
Leer wirkt er im ersten Moment wie ein Kurzschluss, ein Draht: Strom fließt, seine Spannung ist null. Voll wirkt er wie eine Unterbrechung, offene Klemmen: Spannung liegt an, aber kein Strom fließt.
--- falsch
Leer wirkt er wie eine Unterbrechung, weil er noch keine Ladung trägt, die den Strom weiterleiten könnte. Voll wirkt er wie ein Kurzschluss, weil seine getrennte Ladung dann den Strom zwischen den Platten leitet.
--- falsch
Leer und voll wirkt er gleich, nämlich wie ein Kurzschluss: Ein Kondensator lässt den Ladestrom immer ungehindert durch, nur seine Spannung wächst dabei langsam an.
--- falsch
Leer wirkt er wie ein Widerstand mit dem Wert $R$, voll wie einer mit dem doppelten Wert; der Strom halbiert sich deshalb beim Laden genau einmal und bleibt dann konstant.
:::
:::karte zusammenhang Warum der leere Kondensator kurzschließt
Warum verhält sich der leere Kondensator im ersten Moment nach dem Einschalten wie ein Kurzschluss?
---
Weil seine Spannung nicht springen kann, $u_C(0)=0$: Noch ist keine Ladung getrennt, kein Feld wirkt dem Strom entgegen. Die ganze Batteriespannung liegt an $R$, es fließt $i(0)=U_0/R$.
--- falsch
Weil das Dielektrikum im ungeladenen Zustand leitet; erst die getrennte Ladung macht es zum Isolator, und dann sinkt der Strom langsam auf null.
--- falsch
Weil die Batterie beim Einschalten kurz eine höhere Spannung abgibt, die den Kondensator überbrückt, bis sie sich nach einer Weile wieder auf ihren Nennwert beruhigt.
--- falsch
Weil seine Spannung im ersten Moment auf $U_0$ springt und dadurch den Widerstand überbrückt; deshalb fließt kurz ein sehr großer Strom an $R$ vorbei.
:::
:::karte formel Gleichung des RC-Kreises
Welche Gleichung gilt für die Kondensatorspannung $u_C$ beim Laden im RC-Kreis, und woraus folgt sie?
---
$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C$, aus der Maschenregel $U_0=u_R+u_C$ mit $u_R=R\,i$ und $i=C\,\mathrm{d} u_C/\mathrm{d} t$.
--- falsch
$U_0=R\,C\,u_C+\frac{\mathrm{d} u_C}{\mathrm{d} t}$, aus der Maschenregel $U_0=u_R+u_C$ mit $u_R=R\,i$ und $i=C\,u_C$.
--- falsch
$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}-u_C$, aus der Maschenregel $U_0=u_R-u_C$, weil die Kondensatorspannung der Quelle entgegenwirkt.
--- falsch
$U_0=\frac{1}{RC}\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C$, aus der Maschenregel $U_0=u_R+u_C$ mit $u_R=i/R$ und $i=C\,\mathrm{d} u_C/\mathrm{d} t$.
:::
:::karte begriff Differenzialgleichung
Was ist eine Differenzialgleichung, wie sie beim Laden im RC-Kreis entsteht, und was sucht man darin?
---
Eine Gleichung, in der die gesuchte Größe zusammen mit ihrer Ableitung steht. Gesucht ist keine Zahl, sondern eine ganze Funktion, hier $u_C(t)$.
--- falsch
Eine Gleichung zwischen den Differenzen zweier Spannungen. Gesucht ist eine einzelne Zahl, hier der Endwert der Spannung am Kondensator.
--- falsch
Eine Gleichung, in der nur Ableitungen stehen, nicht die gesuchte Größe selbst. Gesucht ist die Steigung der Kurve zu einem Zeitpunkt.
--- falsch
Eine Gleichung, die man durch Ableiten einer bekannten Funktion erhält. Gesucht ist deren Ableitung, hier der Strom $i(t)$ im Kreis.
:::
:::karte formel Steigung der Ladekurve
Was sagt die Gleichung $\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}$ über die Steigung der Ladekurve?
---
Die Steigung ist der Abstand zum Endwert, geteilt durch $\tau$: weit unter $U_0$ groß, bei $U_0$ null, darüber negativ. Deshalb gehört zu jedem Startwert genau eine Kurve.
--- falsch
Die Steigung ist überall gleich, nämlich $U_0/\tau$; die Spannung steigt deshalb gerade bis $U_0$ an und bleibt dort stehen. Jeder Startwert ergibt dieselbe Gerade.
--- falsch
Die Steigung wächst mit der Spannung: Je voller der Kondensator, desto schneller steigt $u_C$, bis er bei $U_0$ voll ist; über $U_0$ steigt sie weiter.
--- falsch
Die Steigung ist der Abstand zum Endwert mal $\tau$; ein größeres $\tau$ lässt die Spannung deshalb schneller steigen, und der Endwert ist früher erreicht.
:::
:::karte formel Aufladen
Wie verlaufen Kondensatorspannung, Strom und Widerstandsspannung, wenn ein leerer Kondensator über $R$ an $U_0$ geladen wird?
---
$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$, $i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau}$ und $u_R(t)=U_0\,\mathrm{e}^{-t/\tau}$ mit $\tau=R\,C$, für $u_C(0)=0$ und $t\ge0$.
--- falsch
$u_C(t)=U_0\,\mathrm{e}^{-t/\tau}$, $i(t)=\frac{U_0}{R}\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$ und $u_R(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$ mit $\tau=R\,C$: Der Strom beginnt bei null.
--- falsch
$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$, $i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau}$ und $u_R(t)=U_0\,\mathrm{e}^{-t/\tau}$ mit $\tau=R/C$, für $u_C(0)=0$ und $t\ge0$.
--- falsch
$u_C(t)=\frac{U_0}{\tau}\,t$, $i(t)=\frac{U_0}{R}$ und $u_R(t)=U_0$ mit $\tau=R\,C$: Der Strom bleibt konstant, und die Spannung steigt gerade an, bis sie $U_0$ erreicht.
:::
:::karte herleitung Die Ladegleichung lösen
Löse die Gleichung $\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}$ mit $u_C(0)=0$ und leite $u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$ her.
---
Setze $x(t)=U_0-u_C(t)$. Dann gilt $\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac{x}{\tau}$ mit $x(0)=U_0$, weil $U_0$ konstant ist und deshalb $\mathrm{d} x/\mathrm{d} t=-\mathrm{d} u_C/\mathrm{d} t$.
---
Für $x>0$ ist $\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac1\tau$, und die linke Seite ist die Ableitung von $\ln x(t)$, weil nach der Kettenregel $\frac{\mathrm{d}}{\mathrm{d} t}\ln x(t)=\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}$ gilt.
---
Also ist $\ln x(t)=-t/\tau+K$ mit einer Konstanten $K$, weil eine Funktion mit der konstanten Steigung $-1/\tau$ eine Gerade ist.
---
Die e-Funktion auf beide Seiten ergibt $x(t)=\mathrm{e}^{K}\,\mathrm{e}^{-t/\tau}$, und es ist $\mathrm{e}^{K}=U_0$, weil bei $t=0$ dort $x(0)=\mathrm{e}^{K}$ steht.
---
Zurückgerechnet ist $u_C=U_0-x=U_0(1-\mathrm{e}^{-t/\tau})$, weil $x$ der Abstand zum Endwert war; Ableiten liefert $i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$.
:::
:::karte zusammenhang Rückkopplung beim Laden
Warum steigt die Kondensatorspannung beim Laden über einen Widerstand immer langsamer?
---
Der Strom bringt Ladung, $u_C$ steigt. Nach der Maschenregel bleibt für $R$ weniger Spannung, der Strom sinkt, und $u_C$ steigt langsamer. Diese Rückkopplung formt die ganze Kurve.
--- falsch
Weil sich die Batterie beim Laden erschöpft und ihre Spannung dabei sinkt; mit einer idealen Quelle stiege $u_C$ gleichmäßig bis $U_0$ an und bliebe dann stehen.
--- falsch
Weil sich der Widerstand durch den Strom erwärmt und dabei immer größer wird; dadurch sinkt der Ladestrom, und die Spannung am Kondensator steigt deshalb immer langsamer an.
--- falsch
Weil die Platten mit jeder Ladung voller werden und neuen Elektronen weniger Platz bieten; der Strom bleibt dabei gleich, nur kommt weniger Ladung an.
:::
:::karte zusammenhang Tangente am Start
Was bedeutet es, dass die Tangente an die Ladekurve im Startpunkt den Endwert genau bei $t=\tau$ erreicht?
---
Bliebe der Anfangsstrom $U_0/R$ konstant, wäre der Kondensator nach $\tau$ voll: $\tau$ ist die Endladung geteilt durch den Anfangsstrom, $C\,U_0/(U_0/R)=RC$.
--- falsch
Dass der Kondensator nach $t=\tau$ tatsächlich voll ist; danach fließt kein Strom mehr, die Kurve endet dort und bleibt danach beim Endwert stehen.
--- falsch
Dass die Spannung bei $t=\tau$ genau ihren halben Endwert erreicht; die Tangente zeigt also den Mittelwert der ganzen Ladekurve an.
--- falsch
Dass der Strom bei $t=\tau$ sein Vorzeichen wechselt; ab diesem Moment entlädt sich der Kondensator über $R$ wieder in die Quelle.
:::
:::karte zusammenhang Wann der Kondensator voll ist
Wird der Kondensator beim Laden über einen Widerstand jemals ganz voll?
---
Rechnerisch nie, denn $\mathrm{e}^{-t/\tau}$ erreicht null nicht. Praktisch nach wenigen $\tau$: Nach $5\tau$ fehlen nur noch 0,7 % der Endspannung.
--- falsch
Ja, genau nach $t=\tau$: Dann hat $u_C$ den Wert $U_0$ erreicht, und der Strom endet in diesem Moment ganz.
--- falsch
Ja, sobald der Strom auf die Hälfte seines Anfangswerts gefallen ist; danach fließt keine Ladung mehr nach, und die Spannung steht.
--- falsch
Praktisch nie: Selbst nach $100\tau$ fehlt noch rund ein Drittel der Endspannung, weil die Kurve so flach wird.
:::
:::karte zusammenhang Kleiner Widerstand beim Laden
Was geschieht beim Laden, wenn der Widerstand im Ladekreis gegen null geht?
---
Für $R\to0$ geht $\tau\to0$ und $i(0)\to\infty$: Der Kondensator lädt fast sofort, aber mit einem sehr großen Anfangsstrom, den nur der Leitungswiderstand begrenzt.
--- falsch
Der Kondensator lädt gar nicht mehr, weil ohne Widerstand kein Spannungsabfall entsteht, der den Strom treiben könnte; die Spannung am Kondensator bleibt null.
--- falsch
$\tau$ wird unendlich groß, weil ohne Widerstand nichts den Strom in den Kondensator lenkt; das Laden dauert dann beliebig lange, der Strom bleibt winzig.
--- falsch
Nichts ändert sich: $\tau$ hängt nur von $C$ ab, und der Widerstand begrenzt lediglich die Endspannung, die der Kondensator am Ende des Ladens erreicht.
:::
:::karte zusammenhang Energiebilanz des Ladens
Wie teilt sich die Energie der Batterie auf, wenn ein leerer Kondensator über einen Widerstand auf $U_0$ geladen wird?
---
Die Batterie gibt $C\,U_0^2$ ab, je die Hälfte, $\frac12CU_0^2$, geht in den Kondensator und als Wärme in den Widerstand. Das gilt für jedes $R$: Kleineres $R$ erhöht den Strom, verkürzt aber die Zeit.
--- falsch
Die Batterie gibt nur $\frac12CU_0^2$ ab, und alles davon geht in den Kondensator; in einem idealen Widerstand entsteht beim Laden überhaupt keine Wärme, weil der Strom am Ende ganz auf null zurückgeht.
--- falsch
Die Batterie gibt $C\,U_0^2$ ab; je kleiner $R$ ist, desto mehr davon landet im Kondensator, und mit $R\to0$ geht fast die ganze Energie in sein Feld, ohne Verlust.
--- falsch
Die Batterie gibt $C\,U_0^2$ ab; drei Viertel davon gehen in den Kondensator, ein Viertel wird im Widerstand zu Wärme, gleich wie groß der Widerstand ist.
:::
::::
