---
title: Stufe 3: Der Fehler beim Strommessen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140400
summary: Das Amperemeter muss in den Stromkreis.
tags: relative Fehler
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das Amperemeter muss in den Stromkreis. Diese Stufe berechnet, wie stark sein Innenwiderstand genau den Strom senkt, den es messen soll.
:::

**Die Idee.** Zum Messen trennt man den Kreis auf und setzt das Instrument ein (Abb. [4](#abb-4)). Die Masche enthält nun $R$ und $R_\mathrm i$. Die Quelle hält $U$ fest und treibt durch den größeren Gesamtwiderstand weniger Strom. Die Anzeige stimmt: Sie zeigt den Strom, der jetzt fließt. Falsch ist nur der Schluss, derselbe Strom fließe auch ohne Gerät.

:::abbildung et1/k4strom 4
Das Rechenmodell ohne und mit Amperemeter. Am Innenwiderstand fallen 49,7 mV ab, die dem Widerstand fehlen. Der Strom sinkt um 0,55 %.
:::

:::satz Satz 3.1 (Fehler des Amperemeters)
<span class="anker" id="satz-3-1"></span>

Ohne Gerät fließt $I_R$, mit Gerät $I_R'$:

<span class="anker" id="gl-3-1"></span>
$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R,\qquad \frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}. \tag{3.1}$$

Der __relative Fehler__ ist $f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i)$. Für $R_\mathrm i\ll R$ gilt $f\approx-R_\mathrm i/R$.
:::

⁠**So liest man das:** $U$ ist die Quellspannung in V, $R$ der Widerstand der Schaltung, $R_\mathrm i$ der des Geräts. Der gestrichene Strom ist der Strom mit Gerät. Allgemein gilt $f=(\text{Anzeige}-\text{wahrer Wert})/\text{wahrer Wert}$, ein negatives $f$ heißt: Die Anzeige ist zu klein. **Gültigkeit:** Die Schaltung ist eine ideale Quelle mit einem Widerstand. Für einen kleinen Fehler braucht es $R_\mathrm i\ll R$, ideal $R_\mathrm i=0$.

:::herleitung Fehler des Amperemeters
Die Maschenregel lautet $U=I_R'R+I_R'R_\mathrm i$, also $I_R'=U/(R+R_\mathrm i)$. Damit ist $f=I_R'/I_R-1=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$.
:::

::::beispiel
$I_R=5$ mA, $I_R'=9\,\mathrm{V}/1810\,\Omega=4{,}972$ mA, also $f=-0{,}55\,\%$. Mit 1 $\Omega$ wie beim Digitalmultimeter wären es 4,997 mA und $f=-0{,}056\,\%$: Fehler vernachlässigbar. An einem kleinen Widerstand sieht es anders aus: 0,9 V an 90 $\Omega$ ergeben 10 mA, mit dem Instrument nur 9 mA, also $f=-10\,\%$. Nicht das Gerät allein entscheidet, sondern das Verhältnis $R_\mathrm i/R$.
::::

⁠**Grenzfälle:** $R_\mathrm i\to0$ ergibt $f\to0$. $R\to0$ ergibt $I_R'\to U/R_\mathrm i$ und $f\to-100\,\%$: Nur noch das Instrument begrenzt den Strom. Das ist Aufgabe [1](das-messgerat-ist-ein-bauteil.html#aufg-1)(a).

:::frage Ist der Strom hinter dem Amperemeter kleiner als davor?
Nein. Im Instrument geht keine Ladung verloren, nur Energie. Der Strom ist im ganzen Kreis gleich und sinkt überall zugleich, weil der Gesamtwiderstand gestiegen ist.
:::

:::aufgabe Aufgabe 3 ★★ Welcher Bereich?
<span class="anker" id="aufg-3"></span>

(a) Ab welchem $R$ bleibt der Fehler des 10-$\Omega$-Amperemeters unter 1 %? (b) An 9 V liegen 90 k$\Omega$. Vergleiche den 10-mA-Bereich mit dem 250-µ A-Bereich: den Fehler durch $R_\mathrm i$ und den Anzeigefehler (1 % des Bereichsendwerts). Welcher Bereich misst besser?

:::loesung
(a) $R_\mathrm i/(R+R_\mathrm i)\le0{,}01$ ergibt $R\ge99\,R_\mathrm i=990\,\Omega$.

(b) Der wahre Strom ist $9\,\mathrm{V}/90\,\mathrm{k\Omega}=100$ µ A. Im 10-mA-Bereich ist $R_\mathrm i=10\,\Omega$, $f=-0{,}011\,\%$, aber der Anzeigefehler beträgt $\pm100$ µ A, so viel wie der Strom selbst. Im 250-µ A-Bereich ist $R_\mathrm i=100\,\mathrm{mV}/250\,\mu\text{A}=400\,\Omega$, $f=-0{,}44\,\%$, der Anzeigefehler beträgt $\pm2{,}5$ µ A, also 2,5 %. Der kleine Bereich greift stärker ein, misst aber viel besser. Die $-0{,}44\,\%$ lassen sich zudem herausrechnen.
:::
:::

::::formelsammlung
**Strom ohne und mit Amperemeter**

$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R$$

Ideale Spannungsquelle $U$ mit einem Widerstand $R$, Amperemeter mit $R_\mathrm i$; der gestrichene Strom fließt mit Gerät. Die Masche enthält nun $R$ und $R_\mathrm i$, die Quelle treibt durch den größeren Gesamtwiderstand weniger Strom. Die Anzeige stimmt für die veränderte Schaltung.

**Verhältnis der Ströme**

$$\frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}$$

Der Strom ist im ganzen Kreis gleich und sinkt überall zugleich.

**Relativer Fehler**

$$f=(\text{Anzeige}-\text{wahrer Wert})/\text{wahrer Wert}$$

Ohne Einheit; ein negatives $f$ heißt: Die Anzeige ist zu klein.

**Fehler des Amperemeters**

$$f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i),\qquad f\approx-R_\mathrm i/R$$

Näherung für $R_\mathrm i\ll R$; ideal ist $R_\mathrm i=0$. Es entscheidet das Verhältnis $R_\mathrm i/R$, nicht das Gerät allein. Für $R\to0$ geht $f\to-100\,\%$: Nur noch das Instrument begrenzt den Strom.
::::

::::lernkarten
:::karte begriff relativer Fehler
Wie ist der relative Fehler $f$ einer Messung festgelegt, und was bedeutet ein negatives Vorzeichen?
---
Die Abweichung der Anzeige, bezogen auf den wahren Wert: $f=(\text{Anzeige}-\text{wahrer Wert})/\text{wahrer Wert}$, ohne Einheit. Ein negatives $f$ heißt: Die Anzeige ist zu klein.
--- falsch
Die Abweichung der Anzeige, bezogen auf die Anzeige selbst: $f=(\text{Anzeige}-\text{wahrer Wert})/\text{Anzeige}$, ohne Einheit. Ein negatives $f$ heißt: Die Anzeige ist zu groß.
--- falsch
Die Abweichung der Anzeige in der Einheit der Messgröße: $f=\text{Anzeige}-\text{wahrer Wert}$, etwa in Ampere. Ein negatives $f$ heißt: Das Gerät ist falsch herum angeschlossen.
--- falsch
Die Abweichung, bezogen auf den wahren Wert: $f=(\text{wahrer Wert}-\text{Anzeige})/\text{wahrer Wert}$, ohne Einheit. Ein negatives $f$ heißt: Die Anzeige ist zu klein.
:::
:::karte formel Strom mit Amperemeter
Welcher Strom fließt durch einen Widerstand $R$ an einer idealen Spannungsquelle $U$, nachdem man ein Amperemeter mit dem Innenwiderstand $R_\mathrm i$ eingesetzt hat?
---
$I_R'=\frac{U}{R+R_\mathrm i}$, kleiner als $I_R=\frac UR$ ohne Gerät, denn die Masche enthält nun $R$ und $R_\mathrm i$. Das Verhältnis ist $I_R/I_R'=1+R_\mathrm i/R$.
--- falsch
$I_R'=\frac UR-\frac{U}{R_\mathrm i}$: Das Gerät zweigt einen eigenen Strom ab, der dem Widerstand fehlt. Das Verhältnis der Ströme ist deshalb $I_R/I_R'=1-R/R_\mathrm i$.
--- falsch
$I_R'=\frac{U}{R\parallel R_\mathrm i}$, größer als ohne Gerät: Das Amperemeter öffnet neben $R$ einen zweiten Strompfad, und die Quelle liefert entsprechend mehr Strom.
--- falsch
$I_R'=\frac UR$, also genau der Strom ohne Gerät: Die ideale Quelle hält ihre Spannung fest und gleicht den Innenwiderstand des Amperemeters dadurch vollständig aus.
:::
:::karte formel Fehler des Amperemeters
Wie groß ist der relative Fehler eines Amperemeters mit dem Innenwiderstand $R_\mathrm i$ in einem Kreis mit dem Widerstand $R$, und wann ist er klein?
---
$f=-R_\mathrm i/(R+R_\mathrm i)$, für $R_\mathrm i\ll R$ also $f\approx-R_\mathrm i/R$: Die Anzeige ist zu klein. Klein ist der Fehler für $R_\mathrm i\ll R$; ideal ist $R_\mathrm i=0$.
--- falsch
$f=-R/(R+R_\mathrm i)$, für $R\ll R_\mathrm i$ also $f\approx-R/R_\mathrm i$: Die Anzeige ist zu klein. Klein ist der Fehler für $R\ll R_\mathrm i$; ideal ist ein unendlich großes $R_\mathrm i$.
--- falsch
$f=+R_\mathrm i/R$: Die Anzeige ist zu groß, weil zum Widerstand des Kreises noch der des Geräts hinzukommt. Klein ist der Fehler für $R_\mathrm i\ll R$; ideal ist $R_\mathrm i=0$.
--- falsch
$f=-R_\mathrm i/(R+R_\mathrm i)$, aber unabhängig vom Kreis betrachtet: Ein Gerät mit kleinem $R_\mathrm i$ misst an jedem Widerstand gleich gut, auch an sehr kleinen Widerständen.
:::
:::karte herleitung Fehler des Amperemeters
Leite ausgehend von der Maschenregel den relativen Fehler eines Amperemeters mit dem Innenwiderstand $R_\mathrm i$ in einem Kreis mit $U$ und $R$ her.
---
Die Maschenregel lautet $U=I_R'R+I_R'R_\mathrm i$, weil derselbe Strom durch $R$ und $R_\mathrm i$ fließt und beide Spannungen zusammen die Quellspannung ergeben.
---
Also ist $I_R'=U/(R+R_\mathrm i)$, weil man $I_R'$ ausklammert und durch $R+R_\mathrm i$ teilt.
---
Der relative Fehler ist $f=I_R'/I_R-1$, weil $f=(I_R'-I_R)/I_R$ die Abweichung bezogen auf den Strom ohne Gerät ist.
---
Mit $I_R=\frac UR$ folgt $f=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$, weil sich $U$ herauskürzt.
---
Für $R_\mathrm i\ll R$ ist $f\approx-R_\mathrm i/R$, weil der Nenner $R+R_\mathrm i$ dann praktisch $R$ ist.
:::
:::karte zusammenhang Warum der Strom sinkt
Warum sinkt der Strom, sobald man ein Amperemeter in den Kreis einsetzt, und zeigt das Gerät dann trotzdem richtig an?
---
Die Quelle hält $U$ fest und treibt durch den größeren Gesamtwiderstand $R+R_\mathrm i$ weniger Strom. Die Anzeige stimmt, sie zeigt den Strom, der jetzt fließt; falsch ist nur der Schluss, derselbe Strom fließe auch ohne Gerät.
--- falsch
Das Amperemeter verbraucht einen Teil der Ladung, die durch es hindurchläuft. Seine Anzeige ist deshalb zu klein, und hinter dem Gerät fließt weniger Strom als davor, bis zur Quelle zurück, der die verbrauchte Ladung fehlt.
--- falsch
Der Strom sinkt gar nicht, nur die Anzeige: Das Gerät zeigt wegen seines Innenwiderstands weniger an, als tatsächlich durch den Kreis fließt, und zwar genau um den Abfall an $R_\mathrm i$.
--- falsch
Das Amperemeter erzeugt eine Gegenspannung, die den Strom bremst. Angezeigt wird aber der Strom ohne Gerät, weil das Gerät diese Gegenspannung intern wieder herausrechnet.
:::
:::karte zusammenhang Strom vor und hinter dem Gerät
Ist der Strom in einem einfachen Stromkreis hinter dem Amperemeter kleiner als davor?
---
Nein: Im Instrument geht keine Ladung verloren, nur Energie. Der Strom ist im ganzen Kreis gleich und sinkt überall zugleich, weil der Gesamtwiderstand gestiegen ist.
--- falsch
Ja: Ein Teil der Ladung bleibt im Innenwiderstand stecken; hinter dem Gerät fließt deshalb genau um den angezeigten Fehler weniger Strom als davor.
--- falsch
Nein, er ist größer: Das Amperemeter beschleunigt die Elektronen, deshalb fließt hinter ihm mehr Strom, während der Strom vor dem Gerät so bleibt wie ohne Gerät.
--- falsch
Nein, er ist gleich und bleibt auch so groß wie ohne Gerät: Ladung geht nicht verloren, deshalb kann der Strom im Kreis auch insgesamt nicht sinken.
:::
:::karte zusammenhang Das Verhältnis entscheidet
Warum misst dasselbe Amperemeter mit 10 $\Omega$ Innenwiderstand an 1,8 k$\Omega$ fast fehlerfrei, an 90 $\Omega$ aber deutlich zu wenig?
---
Nicht das Gerät allein entscheidet, sondern das Verhältnis $R_\mathrm i/R$: An 1,8 k$\Omega$ ist $f=-0{,}55\,\%$, an 90 $\Omega$ sinkt der Strom von 10 mA auf 9 mA, also $f=-10\,\%$.
--- falsch
Weil an 90 $\Omega$ ein größerer Strom fließt, der den Innenwiderstand des Geräts erwärmt und ihn dadurch vergrößert; an 1,8 k$\Omega$ bleibt das Gerät kalt und misst richtig.
--- falsch
Weil das Gerät an 90 $\Omega$ außerhalb seines Messbereichs arbeitet; innerhalb des Bereichs ist der Fehler eines Amperemeters immer gleich groß, gleich an welchem Widerstand es misst.
--- falsch
Weil an 90 $\Omega$ nur 0,9 V anliegen statt 9 V: Der Fehler eines Amperemeters hängt allein von der Quellspannung ab und ist bei kleiner Spannung entsprechend größer.
:::
:::karte zusammenhang Grenzfall ohne Widerstand
Was geschieht mit Strom und Fehler eines Amperemeters, wenn der Widerstand $R$ des Kreises gegen null geht?
---
Es gilt $I_R'\to U/R_\mathrm i$ und $f\to-100\,\%$: Nur noch das Instrument begrenzt den Strom, während der Strom ohne Gerät unbegrenzt wüchse.
--- falsch
Der Fehler geht gegen null, weil dann allein der kleine Innenwiderstand im Kreis liegt; das Gerät zeigt genau den Strom, der auch ohne Gerät flösse.
--- falsch
Der Strom geht gegen null, weil ohne Widerstand im Kreis keine Spannung mehr abfällt; das Gerät zeigt deshalb null an, der Fehler ist $-100\,\%$.
--- falsch
Strom und Fehler bleiben so wie vorher, weil das Gerät seinen Innenwiderstand an den Kreis anpasst und so im gewählten Messbereich bleibt.
:::
:::karte zusammenhang Den passenden Bereich wählen
Warum misst man einen Strom von 100 µ A besser im 250-µ A-Bereich als im 10-mA-Bereich, obwohl der kleine Bereich den größeren Innenwiderstand hat?
---
Der Fehler durch $R_\mathrm i$ bleibt mit $f=-0{,}44\,\%$ klein und lässt sich herausrechnen. Der Anzeigefehler beträgt aber 1 % des Bereichsendwerts: im 10-mA-Bereich $\pm100$ µ A, so viel wie der Strom selbst, im kleinen Bereich nur $\pm2{,}5$ µ A.
--- falsch
Weil der größere Innenwiderstand den Strom genauer einstellt: Er begrenzt den Kreis auf den Messbereich, und das verbessert die Anzeige um denselben Faktor, um den der Innenwiderstand wächst, hier also um das Vierzigfache.
--- falsch
Weil der Anzeigefehler immer 1 % des angezeigten Werts beträgt; im kleinen Bereich steht der Zeiger aber weiter rechts, und dort lässt sich die Skala viel genauer ablesen als am Anfang, wo die Striche eng liegen.
--- falsch
Man misst ihn dort nicht besser: Der 10-mA-Bereich greift mit $f=-0{,}011\,\%$ viel weniger ein und ist deshalb immer vorzuziehen, solange der Strom unter dem Bereichsendwert bleibt.
:::
:::karte formel Grenze für 1 Prozent Fehler
Ab welchem Widerstand $R$ bleibt der Fehler eines Amperemeters mit dem Innenwiderstand $R_\mathrm i$ unter 1 %?
---
Aus $R_\mathrm i/(R+R_\mathrm i)\le0{,}01$ folgt $R\ge99\,R_\mathrm i$; beim Amperemeter mit 10 $\Omega$ also ab 990 $\Omega$.
--- falsch
Aus $R/(R+R_\mathrm i)\le0{,}01$ folgt $R\le R_\mathrm i/99$; beim Amperemeter mit 10 $\Omega$ also nur bis höchstens 0,1 $\Omega$.
--- falsch
Aus $R_\mathrm i/(R+R_\mathrm i)\le0{,}01$ folgt $R\ge0{,}99\,R_\mathrm i$; beim Amperemeter mit 10 $\Omega$ also schon ab 9,9 $\Omega$.
--- falsch
Bei jedem $R$: Der Fehler eines Amperemeters liegt stets unter 1 %, weil sein Innenwiderstand höchstens 1 % des Messbereichs ausmacht.
:::
::::
