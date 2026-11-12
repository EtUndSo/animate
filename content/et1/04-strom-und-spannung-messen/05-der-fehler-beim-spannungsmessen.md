---
title: Stufe 4: Der Fehler beim Spannungsmessen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140500
summary: Das Voltmeter liegt außerhalb des Stromkreises, und trotzdem fließt Strom durch es.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Das Voltmeter liegt außerhalb des Stromkreises, und trotzdem fließt Strom durch es. Diese Stufe zeigt, wann das die Spannung senkt, die es messen soll.
:::

**Die Idee.** Das Voltmeter öffnet zwischen zwei Knoten einen zweiten Strompfad. Sein Strom muss irgendwoher kommen. Treibt eine Stromquelle (sie hält ihren Strom fest, [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) den Lastwiderstand $R_L$, teilt sich der feste Strom auf: Was durch das Voltmeter fließt, fehlt in $R_L$, und die Spannung sinkt (Abb. [5](#abb-5)). Hängt $R_L$ dagegen direkt an einer idealen Spannungsquelle, liefert sie den Zusatzstrom, und nichts ändert sich. Fehler entstehen also nur dort, wo der Strom nicht frei nachfließen kann. Beim Spannungsteiler bremst $R_1$ den Nachschub: Der Gesamtstrom steigt, an $R_1$ fällt mehr ab, die Mitte sinkt.

:::abbildung et1/k4spannung 5
Das Voltmeter (Bereich 10 V, gestrichelt: Innenwiderstand und ideales Gerät) an zwei gleichwertigen Schaltungen. In beiden zweigt es 13,6 µ A ab, und die Anzeige fällt von 3 V auf 2,727 V.
:::

:::satz Satz 4.1 (Fehler des Voltmeters)
<span class="anker" id="satz-4-1"></span>

An einer Stromquelle $I_\mathrm q$ mit Last $R_L$ gilt ohne Gerät $U_L=I_\mathrm qR_L$ und mit Gerät

<span class="anker" id="gl-4-1"></span>
$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}. \tag{4.1}$$

Der relative Fehler ist $f=-R_L/(R_L+R_\mathrm i)$, für $R_L\ll R_\mathrm i$ also $f\approx-R_L/R_\mathrm i$. Am Spannungsteiler gilt dasselbe mit $R_L=R_1\parallel R_2$.
:::

⁠**So liest man das:** Der Bruch ist der Fehlerfaktor. $R_L$ ist der Widerstand, den das Gerät zwischen seinen Anschlüssen vorfindet. Für einen kleinen Fehler braucht es $R_\mathrm i\gg R_L$, ideal $R_\mathrm i\to\infty$. **Gültigkeit:** ideale Quellen, Widerstände unabhängig von der Spannung.

:::herleitung Fehlerfaktor
Mit der Knotenregel $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$ teilt sich der Strom auf zwei parallele Widerstände auf, an beiden liegt $U_L'$. Also ist $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$, und Kürzen mit $R_\mathrm i$ ergibt [(4.1)](#gl-4-1). Am Teiler gilt ohne Gerät $U_2=U\,R_2/(R_1+R_2)$. Mit Gerät ist $R_2$ durch $R_2\parallel R_\mathrm i$ zu ersetzen (belasteter Spannungsteiler, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)):

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)} \quad\Rightarrow\quad \frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}.$$
:::

::::beispiel
Am Teiler ist $R_1\parallel R_2=20$ k$\Omega$ und $R_L/R_\mathrm i=0{,}1$. Die Anzeige beträgt $3\,\mathrm{V}/1{,}1=2{,}727$ V, also $f=-9{,}1\,\%$. Der Mechanismus in Zahlen: Der Strom durch $R_1$ steigt von 100 µ A auf 104,5 µ A, davon fließen 90,9 µ A durch $R_2$ und 13,6 µ A durch das Voltmeter. Dieselben Werte ergibt $I_\mathrm q=150$ µ A an $R_L=20$ k$\Omega$. Ein Digitalmultimeter mit 10 M$\Omega$ zeigt 2,994 V, also $f=-0{,}2\,\%$.
::::

⁠**Grenzfälle:** $R_\mathrm i\to\infty$ ergibt $f\to0$. $R_L\to0$ (Quelle direkt am Gerät) ergibt ebenfalls $f\to0$. Bei $R_\mathrm i=R_L$ halbiert sich die Spannung.

:::frage 200 k$\Omega$ klingt nach viel. Warum stört das Gerät den Teiler trotzdem?
Groß oder klein gibt es nur im Vergleich mit $R_L$. Der Teiler führt nur 100 µ A. Daneben sind 13,6 µ A kein kleiner Anteil.
:::

:::aufgabe Aufgabe 4 ★★ Hochohmiger Teiler
<span class="anker" id="aufg-4"></span>

$R_1=6$ M$\Omega$ und $R_2=3$ M$\Omega$ liegen an 9 V. (a) Was zeigen das Voltmeter mit 200 k$\Omega$ und das Digitalmultimeter mit 10 M$\Omega$ an $R_2$? (b) Wie gewinnst du aus der Anzeige 2,5 V den wahren Wert zurück? (c) Welches $R_\mathrm i$ bräuchte man für 1 % Fehler?

:::loesung
(a) $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$, wahr sind 3 V. Mit 200 k$\Omega$: $3\,\mathrm{V}/(1+10)=0{,}273$ V, $f=-91\,\%$. Mit 10 M$\Omega$: $3\,\mathrm{V}/(1+0{,}2)=2{,}5$ V, $f=-16{,}7\,\%$.

(b) Umstellen von [(4.1)](#gl-4-1): $U=U'(1+R_L/R_\mathrm i)=2{,}5\,\mathrm{V}\cdot1{,}2=3$ V. (c) $R_L/(R_L+R_\mathrm i)\le0{,}01$ ergibt $R_\mathrm i\ge99\,R_L=198$ M$\Omega$.
:::
:::

::::formelsammlung
**Spannung mit Voltmeter**

$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}$$

Stromquelle $I_\mathrm q$ mit Last $R_L$, ohne Gerät $U_L=I_\mathrm qR_L$. Der Bruch ist der Fehlerfaktor. $R_L$ ist der Widerstand, den das Gerät zwischen seinen Anschlüssen vorfindet. Gilt für ideale Quellen und Widerstände, die nicht von der Spannung abhängen.

**Fehler des Voltmeters**

$$f=-R_L/(R_L+R_\mathrm i),\qquad f\approx-R_L/R_\mathrm i$$

Näherung für $R_L\ll R_\mathrm i$; für einen kleinen Fehler braucht es $R_\mathrm i\gg R_L$, ideal $R_\mathrm i\to\infty$. Für $R_L\to0$ (Quelle direkt am Gerät) geht $f\to0$, bei $R_\mathrm i=R_L$ halbiert sich die Spannung.

**Am Spannungsteiler**

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)},\qquad \frac{U_2'}{U_2}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}$$

Ohne Gerät $U_2=U\,R_2/(R_1+R_2)$; mit Gerät ist $R_2$ durch $R_2\parallel R_\mathrm i$ zu ersetzen. Es gilt also derselbe Fehlerfaktor mit $R_L=R_1\parallel R_2$.

**Wahren Wert zurückgewinnen**

$$U=U'(1+R_L/R_\mathrm i)$$

Umgestellter Fehlerfaktor: $U'$ ist die Anzeige, $U$ der Wert ohne Gerät; $R_L$ und $R_\mathrm i$ müssen bekannt sein.
::::

::::lernkarten
:::karte zusammenhang Strom durch das Voltmeter
Warum fließt Strom durch ein Voltmeter, obwohl es außerhalb des Stromkreises liegt, und woher muss dieser Strom kommen?
---
Es öffnet zwischen zwei Knoten einen zweiten Strompfad durch seinen Innenwiderstand. Sein Strom muss nachfließen: Kann die Quelle ihn liefern, ändert sich nichts; sonst fehlt er in den anderen Zweigen.
--- falsch
Weil es eine eigene Batterie enthält, die Strom in die Schaltung schickt. Dieser Strom kommt also aus dem Gerät selbst und fließt zusätzlich durch die Bauteile der Schaltung, bevor er zum Gerät zurückkehrt.
--- falsch
Es fließt gar kein Strom: Ein Voltmeter liegt außerhalb des Kreises und vergleicht nur die Potenziale an zwei Punkten, ohne dabei Ladung zu bewegen; deshalb heißt es Spannungsmesser.
--- falsch
Weil sich das Gerät beim Anschließen auflädt wie ein Kondensator; danach fließt kein Strom mehr, und die Spannung der Schaltung bleibt nach diesem kurzen Ladestrom unverändert.
:::
:::karte zusammenhang Stromquelle und Spannungsquelle
Warum senkt ein Voltmeter die Spannung an einer Last, die eine Stromquelle speist, nicht aber an einem Widerstand direkt an einer idealen Spannungsquelle?
---
Die Stromquelle hält ihren Strom fest: Was durch das Voltmeter fließt, fehlt in $R_L$, und die Spannung sinkt. Die ideale Spannungsquelle liefert den Zusatzstrom, und nichts ändert sich. Fehler entstehen nur, wo der Strom nicht frei nachfließen kann.
--- falsch
Die Stromquelle liefert mehr Strom, sobald das Voltmeter angeschlossen ist, und senkt dabei ihre Spannung, um ihre Leistung zu halten; die Spannungsquelle liefert gleich viel Strom wie vorher, deshalb ändert sich an ihrem Widerstand nichts.
--- falsch
An der Spannungsquelle sinkt die Spannung ebenso stark, man sieht es nur nicht: Das Voltmeter misst dort die Quellspannung selbst und nicht die Spannung am Widerstand, der an ihr hängt; in Wahrheit sind beide Fehler gleich groß.
--- falsch
Weil die Last an der Stromquelle der größere Widerstand ist: Ein Voltmeter senkt die Spannung an jedem großen Widerstand, gleich welche Quelle ihn speist, und an keinem kleinen.
:::
:::karte zusammenhang Spannungsteiler unter Last
Warum sinkt die Spannung in der Mitte eines Spannungsteilers, sobald man dort ein Voltmeter anschließt?
---
$R_1$ bremst den Nachschub: Durch den zusätzlichen Pfad steigt der Gesamtstrom, an $R_1$ fällt mehr Spannung ab, und die Mitte sinkt. Im Beispiel steigt der Strom durch $R_1$ von 100 µ A auf 104,5 µ A.
--- falsch
Das Voltmeter nimmt Ladung aus der Mitte auf und speichert sie. Dadurch sinkt das Potenzial dort, bis das Gerät voll ist; danach steigt es wieder auf den alten Wert, und die Anzeige stimmt.
--- falsch
Der Gesamtstrom sinkt, weil mit dem Voltmeter ein weiterer Widerstand hinzukommt. An $R_2$ fällt deshalb weniger Spannung ab und an $R_1$ ebenfalls, sodass auch die Spannung in der Mitte sinkt.
--- falsch
An $R_2$ fällt weniger ab, weil das Voltmeter in Reihe mit ihm liegt und einen Teil seiner Spannung übernimmt. Der Gesamtstrom des Teilers bleibt dabei unverändert.
:::
:::karte formel Spannung mit Voltmeter
Welche Spannung zeigt ein Voltmeter mit dem Innenwiderstand $R_\mathrm i$ an einer Last $R_L$, die von einer Stromquelle $I_\mathrm q$ gespeist wird?
---
$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}$ mit $U_L=I_\mathrm qR_L$ ohne Gerät. Der Bruch ist der Fehlerfaktor; vorausgesetzt sind ideale Quellen und Widerstände, die nicht von der Spannung abhängen.
--- falsch
$U_L'=I_\mathrm q\,(R_L+R_\mathrm i)=U_L\cdot(1+R_\mathrm i/R_L)$: Das Voltmeter kommt zur Last hinzu, deshalb zeigt es mehr an, als ohne Gerät an der Last anliegt. Das gilt für jede Quelle.
--- falsch
$U_L'=I_\mathrm qR_L=U_L$: Die Stromquelle hält ihren Strom fest, also bleibt die Spannung an der Last gleich, und das Voltmeter zeigt sie ohne Fehler an, gleich wie groß sein Innenwiderstand ist.
--- falsch
$U_L'=U_L\cdot\frac{1}{1+R_\mathrm i/R_L}$ mit $U_L=I_\mathrm qR_L$ ohne Gerät: Der Fehlerfaktor wird umso besser, je kleiner der Innenwiderstand gegenüber der Last ist.
:::
:::karte formel Fehler des Voltmeters
Wie groß ist der relative Fehler eines Voltmeters mit dem Innenwiderstand $R_\mathrm i$, und welcher Widerstand $R_L$ geht dabei ein?
---
$f=-R_L/(R_L+R_\mathrm i)$, für $R_L\ll R_\mathrm i$ also $f\approx-R_L/R_\mathrm i$. $R_L$ ist der Widerstand, den das Gerät zwischen seinen Anschlüssen vorfindet, am Spannungsteiler $R_L=R_1\parallel R_2$.
--- falsch
$f=-R_L/(R_L+R_\mathrm i)$ mit $R_L$ gleich dem Bauteil, an dem gemessen wird. Am Spannungsteiler ist das $R_2$ allein; $R_1$ spielt für den Fehler des Voltmeters keine Rolle.
--- falsch
$f=-R_\mathrm i/(R_L+R_\mathrm i)$, für $R_\mathrm i\ll R_L$ also $f\approx-R_\mathrm i/R_L$. $R_L$ ist am Spannungsteiler die Summe $R_1+R_2$ der beiden Widerstände.
--- falsch
$f=+R_L/R_\mathrm i$: Die Anzeige ist zu groß, weil der Strom des Geräts zusätzlich durch die Last fließt. $R_L$ ist am Spannungsteiler $R_1\parallel R_2$.
:::
:::karte herleitung Fehlerfaktor an der Stromquelle
Leite ausgehend von der Knotenregel her, welche Spannung $U_L'$ ein Voltmeter mit dem Innenwiderstand $R_\mathrm i$ an einer Last $R_L$ an der Stromquelle $I_\mathrm q$ anzeigt.
---
Die Knotenregel gibt $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$, weil sich der feste Quellstrom auf Last und Voltmeter aufteilt.
---
An beiden liegt dieselbe Spannung $U_L'$, weil sie parallel zwischen denselben Knoten liegen; also ist $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$.
---
Kürzen mit $R_\mathrm i$ ergibt $U_L'=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}$, weil ohne Gerät $U_L=I_\mathrm qR_L$ gilt.
---
Der relative Fehler ist $f=-R_L/(R_L+R_\mathrm i)$, weil man vom Fehlerfaktor 1 abzieht und auf den gemeinsamen Nenner $R_L+R_\mathrm i$ bringt.
:::
:::karte herleitung Voltmeter am Spannungsteiler
Leite her, dass am Spannungsteiler aus $R_1$ und $R_2$ der Widerstand $R_L=R_1\parallel R_2$ in den Fehlerfaktor des Voltmeters eingeht.
---
Ohne Gerät gilt $U_2=U\,R_2/(R_1+R_2)$, weil der Teiler die Spannung im Verhältnis der Widerstände aufteilt.
---
Mit Gerät ist $R_2$ durch $R_2\parallel R_\mathrm i$ zu ersetzen, weil das Voltmeter parallel zu $R_2$ liegt (belasteter Spannungsteiler).
---
Einsetzen ergibt $U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)}$, weil man den Doppelbruch mit $R_2+R_\mathrm i$ erweitert.
---
Der Quotient ist $\frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}$, weil sich $R_2$ kürzt und $R_1+R_2$ in den Zähler wandert.
---
Teilen durch $R_\mathrm i(R_1+R_2)$ ergibt $\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}$, weil $R_1R_2/(R_1+R_2)$ nach der Schreibweise für parallele Widerstände gerade $R_1\parallel R_2$ ist.
:::
:::karte zusammenhang Groß nur im Vergleich
Warum stört ein Voltmeter mit 200 k$\Omega$ Innenwiderstand einen Spannungsteiler aus 60 k$\Omega$ und 30 k$\Omega$ merklich, obwohl 200 k$\Omega$ nach viel klingt?
---
Groß oder klein gibt es nur im Vergleich mit $R_L=R_1\parallel R_2=20$ k$\Omega$: Mit $R_L/R_\mathrm i=0{,}1$ zeigt es 2,727 V statt 3 V, also $f=-9{,}1\,\%$. Der Teiler führt nur 100 µ A, daneben sind 13,6 µ A kein kleiner Anteil.
--- falsch
Weil 200 k$\Omega$ für ein Voltmeter wenig ist: Erst ab 1 M$\Omega$ stört ein Gerät keinen Spannungsteiler mehr, gleich wie groß dessen Widerstände sind. Darunter beträgt der Fehler immer rund 10 %.
--- falsch
Weil das Voltmeter in Reihe mit $R_2$ liegt und den Teiler so auf 290 k$\Omega$ vergrößert: Der Strom sinkt dadurch auf ein Drittel, und die Spannung in der Mitte sinkt entsprechend mit.
--- falsch
Es stört ihn nicht merklich: Mit einem Innenwiderstand, der gut dreimal so groß ist wie $R_1$, bleibt der Fehler unter 1 %; die Anzeige von 2,73 V liegt an der Toleranz der Widerstände.
:::
:::karte zusammenhang Grenzfälle beim Spannungsmessen
Was ergibt der Fehler eines Voltmeters für $R_\mathrm i\to\infty$, für $R_L\to0$ und für $R_\mathrm i=R_L$?
---
Für $R_\mathrm i\to\infty$ geht $f\to0$, ebenso für $R_L\to0$, wenn die Quelle direkt am Gerät liegt. Bei $R_\mathrm i=R_L$ halbiert sich die Spannung.
--- falsch
Für $R_\mathrm i\to\infty$ geht $f\to0$, für $R_L\to0$ dagegen $f\to-100\,\%$, weil das Gerät dann allein den Strom führt. Bei $R_\mathrm i=R_L$ ist der Fehler null.
--- falsch
Für $R_\mathrm i\to\infty$ geht $f\to-100\,\%$, weil durch das Gerät kein Strom mehr fließt; für $R_L\to0$ geht $f\to0$. Bei $R_\mathrm i=R_L$ verdoppelt sich die Spannung.
--- falsch
In allen drei Fällen bleibt $f$ gleich, weil der Fehler eines Voltmeters nur von seinem Bereichsendwert abhängt, nicht vom Verhältnis zwischen $R_\mathrm i$ und $R_L$.
:::
:::karte formel Wahren Wert zurückgewinnen
Wie gewinnt man aus der Anzeige $U'$ eines Voltmeters den Wert $U$ ohne Gerät zurück, wenn $R_L$ und $R_\mathrm i$ bekannt sind?
---
Durch Umstellen des Fehlerfaktors: $U=U'(1+R_L/R_\mathrm i)$. Zeigt ein Gerät mit 10 M$\Omega$ an einem Teiler mit 2 M$\Omega$ Ersatzwiderstand 2,5 V, waren es ohne Gerät 3 V.
--- falsch
Durch Abziehen des Fehlers: $U=U'(1-R_L/R_\mathrm i)$. Zeigt ein Gerät mit 10 M$\Omega$ an einem Teiler mit 2 M$\Omega$ Ersatzwiderstand 2,5 V, waren es ohne Gerät 2 V.
--- falsch
Durch Teilen durch den Faktor: $U=U'/(1+R_L/R_\mathrm i)$. Zeigt ein Gerät mit 10 M$\Omega$ an einem Teiler mit 2 M$\Omega$ Ersatzwiderstand 2,5 V, waren es rund 2,08 V.
--- falsch
Gar nicht: Der Wert ohne Gerät ist durch das Messen verloren; man kann nur ein Gerät mit größerem Innenwiderstand nehmen und hoffen, dass der Fehler dann klein genug ist.
:::
:::karte zusammenhang Hochohmiger Teiler
Warum zeigt selbst ein Digitalmultimeter mit 10 M$\Omega$ an einem Spannungsteiler aus 6 M$\Omega$ und 3 M$\Omega$ an 9 V deutlich zu wenig an?
---
Das Gerät sieht $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$, nicht mehr klein gegen 10 M$\Omega$: Es zeigt $3\,\mathrm{V}/(1+0{,}2)=2{,}5$ V statt 3 V, also $f=-16{,}7\,\%$. Für 1 % Fehler bräuchte man $R_\mathrm i\ge99\,R_L=198$ M$\Omega$.
--- falsch
Weil Digitalmultimeter erst in der Nähe ihres Bereichsendwerts genau messen; weit darunter weicht ihre Anzeige stets um einige Prozent nach unten ab, gleich an welcher Schaltung man misst.
--- falsch
Weil das Gerät nur mit $R_2=3$ M$\Omega$ verglichen werden muss: Mit einem Innenwiderstand von gut dem Dreifachen ergibt sich ein Fehler von 25 %, die Anzeige liegt bei 2,25 V.
--- falsch
Weil die Quelle bei so großen Widerständen kaum Strom liefern kann und ihre Spannung deshalb auf 7,5 V sinkt; das Gerät zeigt davon richtig ein Drittel an.
:::
::::
