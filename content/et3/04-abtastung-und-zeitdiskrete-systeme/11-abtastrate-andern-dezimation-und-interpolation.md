---
title: Stufe 10: Abtastrate ändern, Dezimation und Interpolation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3241100
summary: Eine Folge lässt sich nachträglich mit niedrigerer oder höherer Rate darstellen.
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Eine Folge lässt sich nachträglich mit niedrigerer oder höherer Rate darstellen. Für das Spektrum gelten dieselben Regeln wie beim ersten Abtasten.
:::

**Herabtasten um den Faktor $c$.** Man behält nur jeden $c$-ten Wert. Gedanklich erst mit einem Kamm aus Einheitsimpulsen multiplizieren, dann die Nullen weglassen:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

Die Multiplikation mit dem Kamm erzeugt $c$ Kopien des Spektrums im Abstand $1/c$, das Weglassen der Nullen dehnt die Frequenzachse um $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

Reicht das Spektrum bis $f_\mathrm g$ (bezogen auf die alte Rate), reicht es nach dem Herabtasten bis $cf_\mathrm g$. Kein Aliasing gibt es nur, wenn $cf_\mathrm g\le\frac12$. Sonst muss vorher ein digitaler Tiefpass das Band begrenzen.

**Hochtasten um den Faktor $c$.** Man fügt zwischen je zwei Werte $c-1$ Nullen ein, $s_\uparrow(n)=s(n/c)$ für durch $c$ teilbare $n$, sonst 0. Das Spektrum wird um $c$ gestaucht, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, und enthält jetzt $c-1$ Spiegelspektren in der Periode. Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $c$ entfernt sie. Dabei füllt er die Nullen mit interpolierten Werten (die si-Interpolation aus Stufe [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) in diskreter Form), die ursprünglichen Werte bleiben erhalten. Herab- und Hochtasten nacheinander ändern die Rate um einen rationalen Faktor $c_1/c_2$.

:::abbildung et3/k4rate 7
Spektren (Frequenz bezogen auf die jeweilige Rate) beim Ändern der Abtastrate. Herabtasten dehnt das Band, Hochtasten staucht es und erzeugt Spiegelspektren, die ein Interpolationsfilter entfernt.
:::

:::aufgabe Aufgabe 10 ★★ Herabtasten
<span class="anker" id="aufg-10"></span>

Eine Folge hat ein Spektrum bis $f_\mathrm g=0{,}2$.

<ol class="al">

<li>

Darf man sie ohne Vorfilter um $c=2$ herabtasten? Um $c=3$?

</li>

<li>

Was muss vor dem Herabtasten um $c=3$ geschehen, und was verliert man dabei?

</li>

</ol>

:::loesung
(a) $c=2$: Das Band reicht danach bis $0{,}4\le0{,}5$, kein Aliasing. $c=3$: bis $0{,}6>0{,}5$, Aliasing.

(b) Vorher mit einem digitalen Tiefpass auf $\frac{1}{2c}=\frac16\approx0{,}167$ begrenzen. Die Anteile zwischen 0,167 und 0,2 gehen dabei verloren. Das ist der Preis der niedrigeren Rate.
:::
:::

::::formelsammlung
**Herabtasten**

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc)$$

Jeden $c$-ten Wert behalten: gedanklich erst mit einem Kamm aus Einheitsimpulsen multiplizieren, dann die Nullen weglassen.

**Spektrum beim Herabtasten**

$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr)$$

$c$ Kopien im Abstand $1/c$; das Weglassen der Nullen dehnt die Frequenzachse um $c$. Ein Band bis $f_\mathrm g$ reicht danach bis $cf_\mathrm g$.

**Herabtasten ohne Aliasing**

$$cf_\mathrm g\le\frac12$$

$f_\mathrm g$ bezogen auf die alte Rate. Sonst muss vorher ein digitaler Tiefpass das Band begrenzen.

**Hochtasten**

$$S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$$

$c-1$ Nullen zwischen je zwei Werte: $s_\uparrow(n)=s(n/c)$ für durch $c$ teilbare $n$, sonst 0. Das Spektrum wird um $c$ gestaucht und enthält $c-1$ Spiegelspektren in der Periode. Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $c$ entfernt sie und füllt die Nullen mit interpolierten Werten.
::::

::::lernkarten
:::karte formel Herabtasten
Wie beschreibt man das Herabtasten einer Folge um den Faktor $c$, bei dem man nur jeden $c$-ten Wert behält?
---
Gedanklich in zwei Schritten: erst mit einem Kamm aus Einheitsimpulsen multiplizieren, $s_c(n)=s(n)\sum_m\delta(n-mc)$, dann die Nullen weglassen, $s_u(n)=s(nc)$.
--- falsch
Gedanklich in zwei Schritten: erst mit einem Kamm aus Einheitsimpulsen falten, $s_c(n)=s(n)*\sum_m\delta(n-mc)$, dann jeden $c$-ten Wert behalten, $s_u(n)=s(n/c)$.
--- falsch
In einem einzigen Schritt: Man teilt jeden Wert durch $c$, $s_u(n)=s(n)/c$. Die Zahl der Werte bleibt gleich, nur ihr Abstand wird gedanklich um den Faktor $c$ größer.
--- falsch
Gedanklich in zwei Schritten: erst zwischen je zwei Werte $c-1$ Nullen einfügen, dann mit einem Tiefpass glätten, sodass am Ende $s_u(n)=s(nc)$ entsteht.
:::
:::karte formel Spektrum beim Herabtasten
Wie sieht das Spektrum einer Folge aus, die man um den Faktor $c$ herabgetastet hat?
---
$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr)$ und $S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr)$: Der Kamm erzeugt $c$ Kopien im Abstand $1/c$, das Weglassen der Nullen dehnt die Frequenzachse um $c$.
--- falsch
$S_{u,\mathrm a}(f)=S_\mathrm a(cf)$: Das Spektrum wird um den Faktor $c$ gestaucht, weil die Folge kürzer wird. Kopien entstehen dabei keine, denn es werden ja nur Werte weggelassen und keine hinzugefügt.
--- falsch
$S_{c,\mathrm a}(f)=c\sum_{k=0}^{c-1}S_\mathrm a(f-kc)$ und $S_{u,\mathrm a}(f)=S_{c,\mathrm a}(f)$: Der Kamm erzeugt $c$ Kopien im Abstand $c$, das Weglassen der Nullen ändert das Spektrum dagegen nicht.
--- falsch
$S_{u,\mathrm a}(f)=\frac1cS_\mathrm a(f)$: Das Spektrum behält seine Form und Breite und wird nur um den Faktor $1/c$ kleiner, weil von je $c$ Werten nur einer übrig bleibt.
:::
:::karte zusammenhang Herabtasten dehnt das Band
Unter welcher Bedingung entsteht beim Herabtasten um den Faktor $c$ kein Aliasing, und was muss sonst vorher geschehen?
---
Ein Spektrum bis $f_\mathrm g$, bezogen auf die alte Rate, reicht danach bis $cf_\mathrm g$. Kein Aliasing gibt es nur, wenn $cf_\mathrm g\le\frac12$ ist. Sonst muss vorher ein digitaler Tiefpass das Band begrenzen.
--- falsch
Ein Spektrum bis $f_\mathrm g$ reicht danach nur noch bis $f_\mathrm g/c$. Aliasing entsteht deshalb nie; das Band wird sogar schmaler, und ein Tiefpass ist erst nach dem Herabtasten nötig, um Reste zu glätten.
--- falsch
Ein Spektrum bis $f_\mathrm g$ reicht danach bis $cf_\mathrm g$. Kein Aliasing gibt es, wenn $cf_\mathrm g\le1$ ist, denn die Periode des Spektrums ist 1. Sonst muss nachher ein Tiefpass die Kopien entfernen.
--- falsch
Ein Spektrum bis $f_\mathrm g$ reicht danach bis $cf_\mathrm g$. Kein Aliasing gibt es nur, wenn $cf_\mathrm g\le\frac12$ ist. Sonst interpoliert man die weggelassenen Werte nachträglich, dann verschwindet der Alias.
:::
:::karte zusammenhang Herabtasten um 2 oder um 3
Darf man eine Folge mit einem Spektrum bis $f_\mathrm g=0{,}2$ ohne Vorfilter um $c=2$ oder um $c=3$ herabtasten?
---
Um $c=2$ ja: Das Band reicht danach bis $0{,}4\le0{,}5$. Um $c=3$ nicht: Es reicht bis $0{,}6>0{,}5$, es entsteht Aliasing. Dann müsste vorher ein Tiefpass auf $\frac16\approx0{,}167$ begrenzen.
--- falsch
Um beide Faktoren ja: Das Band reicht danach nur bis $0{,}1$ bzw. $0{,}067$, weil Herabtasten das Spektrum staucht. Aliasing droht erst, wenn $f_\mathrm g$ über $0{,}5$ liegt.
--- falsch
Um keinen der beiden: Schon bei $c=2$ reicht das Band bis $0{,}4$, und das liegt über der halben neuen Rate $0{,}25$. Ohne Vorfilter entsteht in beiden Fällen Aliasing, bei $c=3$ nur noch stärker.
--- falsch
Um $c=3$ ja, um $c=2$ nicht: Ungerade Faktoren erzeugen keine Kopie bei $\frac12$, deshalb fällt bei $c=3$ keine Kopie auf das Band, während bei $c=2$ eine Kopie genau dort liegt.
:::
:::karte formel Hochtasten
Was geschieht beim Hochtasten einer Folge um den Faktor $c$ mit der Folge und mit ihrem Spektrum?
---
Man fügt zwischen je zwei Werte $c-1$ Nullen ein: $s_\uparrow(n)=s(n/c)$ für durch $c$ teilbare $n$, sonst 0. Das Spektrum wird um $c$ gestaucht, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, und enthält $c-1$ Spiegelspektren in der Periode.
--- falsch
Man wiederholt jeden Wert $c$-mal hintereinander. Das Spektrum wird um $c$ gedehnt, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(f/c)$, und bleibt frei von Kopien, weil keine neuen Werte hinzukommen.
--- falsch
Man fügt zwischen je zwei Werte $c-1$ Nullen ein. Das Spektrum bleibt dabei unverändert, weil Nullen nichts zum Spektrum beitragen; erst ein nachfolgender Tiefpass erzeugt die neuen Frequenzen.
--- falsch
Man fügt zwischen je zwei Werte $c-1$ Nullen ein: $s_\uparrow(n)=s(nc)$. Das Spektrum wird um $c$ gedehnt, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(f/c)$, und reicht danach bis $cf_\mathrm g$, ohne Kopien.
:::
:::karte begriff Interpolationsfilter
Was ist das Interpolationsfilter beim Hochtasten um den Faktor $c$, und was bewirkt es?
---
Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $c$. Er entfernt die $c-1$ Spiegelspektren und füllt dabei die eingefügten Nullen mit interpolierten Werten; die ursprünglichen Werte bleiben erhalten.
--- falsch
Ein Hochpass mit der Grenzfrequenz $\frac{1}{2c}$, der die tiefen Frequenzen der eingefügten Nullen entfernt. Die ursprünglichen Werte werden dabei leicht verändert, damit der Übergang zu den neuen Werten glatt wird.
--- falsch
Ein Tiefpass mit der Grenzfrequenz $\frac12$ und der Verstärkung 1. Er lässt das ganze Band durch und ersetzt nur die eingefügten Nullen durch den jeweils vorigen Wert der Folge.
--- falsch
Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $\frac1c$. Er entfernt die Spiegelspektren und verteilt dabei jeden ursprünglichen Wert gleichmäßig auf $c$ neue Werte.
:::
:::karte zusammenhang Rationaler Faktor
Wie ändert man die Abtastrate einer Folge um einen rationalen Faktor $c_1/c_2$?
---
Man tastet nacheinander um einen ganzzahligen Faktor hoch und um einen anderen herab. Jeder Schritt folgt den Regeln für das Spektrum: Interpolationsfilter beim Hochtasten, wenn nötig ein Vorfilter beim Herabtasten.
--- falsch
Man gewinnt aus der Folge mit der si-Interpolation die kontinuierliche Funktion zurück und tastet sie neu ab. Ein anderer Weg existiert nicht, weil Herab- und Hochtasten jeweils nur ganzzahlige Faktoren erlauben und sich nicht kombinieren lassen.
--- falsch
Man tastet um den Faktor $c_1\cdot c_2$ herab. Das Produkt zweier ganzer Zahlen deckt jeden rationalen Faktor ab, weil sich jeder Bruch durch Kürzen in diese Form bringen lässt.
--- falsch
Gar nicht: Eine Folge lässt sich nur um ganzzahlige Faktoren umrechnen. Für rationale Faktoren muss man das ursprüngliche analoge Signal mit der neuen Rate noch einmal abtasten.
:::
::::
