---
title: Stufe 7: Rechnen mit Kondensator und Diode
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210900
summary: Bisher machte ein Widerstand aus Spannung Strom und ein zweiter aus Strom Spannung.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher machte ein Widerstand aus Spannung Strom und ein zweiter aus Strom Spannung. Diese Stufe setzt andere Bauteile ein, ohne die Regel zu ändern. Daher hat der OPV seinen Namen: Er führt Rechenoperationen aus.
:::

**Die Idee.** Liegt der Plus-Eingang an Masse, sagt die Knotenregel am Minus-Eingang: Der Strom des Eingangsbauteils fließt vollständig durch das Rückführbauteil, $I_\mathrm{ein}=-I_\mathrm{rück}$. Das Eingangsbauteil sieht $U_\mathrm{E}$ und liefert einen Strom. Das Rückführbauteil sieht $U_\mathrm{A}$ und muss denselben Strom führen. Welche Funktion entsteht, legt allein deren Strom-Spannungs-Gesetz fest (Abb. [9](#abb-9)).

:::satz Satz 7.1 (Operationen)
<span class="anker" id="satz-7-1"></span>

Mit Plus-Eingang an Masse und idealem OPV gilt

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \text{Integrierer: }&u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t', \\ \text{Differenzierer: }&u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}, \\ \text{Logarithmierer: }&U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}, \\ \text{Exponentialschaltung: }&U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}. \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**So liest man das:** $R\,C$ ist eine Zeitkonstante in s, $I_\mathrm{S}$ der Sättigungssperrstrom der Diode, $U_T=26$ mV. **Gültigkeit:** [(7.3)](#gl-7-3) verlangt $U_\mathrm{E}>0$ und $U_\mathrm{E}/R\gg I_\mathrm{S}$, [(7.4)](#gl-7-4) verlangt $U_\mathrm{E}\gg U_T$, und alle verlangen einen Ausgang innerhalb seiner Grenzen.

:::herleitung Vier Knotenregeln
Integrierer: Durch $R$ fließt $i=u_\mathrm{E}/R$. Er lädt den Kondensator, $C\,\mathrm{d} u_C/\mathrm{d} t=i$. Die linke Platte liegt fest auf 0, also ist $u_\mathrm{A}=-u_C$. Differenzierer: $i=C\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$ durch den Kondensator am Eingang, $u_\mathrm{A}=-R\,i$. Logarithmierer: $I=U_\mathrm{E}/R$ fließt durch die Diode, also $I=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{F}/U_T}$ mit der Diodenspannung $U_\mathrm{F}=-U_\mathrm{A}$. Auflösen ergibt [(7.3)](#gl-7-3). Exponentialschaltung: $U_\mathrm{E}$ liegt an der Diode, ihr Strom $I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ fließt durch $R$.
:::

:::abbildung et1/k11bauteile 9
Vier Schaltungen, eine Regel: Das linke Bauteil macht aus der Eingangsspannung einen Strom, das obere verlangt dafür eine Ausgangsspannung. Die Knoten liegen auf virtueller Masse.
:::

::::beispiel [Beispiele]
⁠*Integrierer* mit $R=10$ k$\Omega$, $C=10$ nF, also $R\,C=100$ µ s. Bei $U_\mathrm{E}=1$ V fließt ein fester Strom von 100 µ A. Anders als beim RC-Glied aus [Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) sinkt er nicht beim Laden, denn die Spannung an $R$ bleibt 1 V. $u_\mathrm{A}$ fällt gleichmäßig um 10 V/ms und erreicht $-11$ V nach 1,1 ms. Ein Rechteck $\pm1$ V mit 1 kHz wird zum Dreieck mit $\pm2{,}5$ V. *Differenzierer* mit demselben $R\,C$: Ein Dreieck $\pm1$ V mit 1 kHz steigt um 4 V/ms, $u_\mathrm{A}$ wird zum Rechteck mit $\pm0{,}4$ V. Für einen Sinus wächst sein Betrag mit der Frequenz, $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$: 0,63 bei 1 kHz, 62,8 bei 100 kHz. Deshalb verstärkt er hochfrequentes Rauschen (Stufe [1](rauschen.html#stufe-1)) besonders stark. *Logarithmierer* mit $R=10$ k$\Omega$ und $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A: 0,1 V, 1 V, 10 V ergeben $-0{,}462$ V, $-0{,}522$ V, $-0{,}582$ V. Jede Dekade (Faktor 10) bringt $U_T\ln10=59{,}9$ mV. *Exponentialschaltung* mit denselben Werten: 0,5 V ergeben $-0{,}427$ V, je 18 mV mehr verdoppeln den Betrag.
::::

⁠**Grenzfälle:** $u_\mathrm{E}=0$ lässt den Integrierer stehen, er hält $u_\mathrm{A}(0)$. Bei $U_\mathrm{E}<0$ sperrt die Diode des Logarithmierers, die Rückführung ist unterbrochen, und der Ausgang läuft zum Anschlag: Die Regel gilt nur, solange der Rückweg leitet.

**Multiplizieren.** Wegen $\ln x+\ln y=\ln(x\,y)$ multipliziert eine Kette analog: zwei Logarithmierer, ein Addierer, eine Exponentialschaltung. Am Ausgang steht bis auf einen festen Faktor das Produkt $U_x\,U_y$. Weil $U_T$ und $I_\mathrm{S}$ von der Temperatur abhängen, ersetzt man die Dioden in der Praxis durch Transistoren mit zusätzlicher Temperaturkompensation. Vor den Digitalrechnern bauten solche Schaltungen Rechenmaschinen, daher der Name Operationsverstärker.

:::aufgabe Aufgabe 7 ★★ Integrierer
<span class="anker" id="aufg-7"></span>

$R=100$ k$\Omega$, $C=10$ nF, $u_\mathrm{A}(0)=0$. (a) Wie groß ist $R\,C$? Wo steht $u_\mathrm{A}$ nach 10 ms bei $U_\mathrm{E}=-0{,}2$ V? (b) Wann schlägt der Ausgang an? (c) Ein Rechteck $\pm0{,}5$ V mit 100 Hz liegt an. Welche Amplitude hat das Dreieck? Was geschieht bei 20 Hz?

:::loesung
(a) $R\,C=1$ ms. $u_\mathrm{A}$ steigt mit 200 V/s, nach 10 ms auf $+2$ V. (b) Nach $11\,\mathrm{V}/(200\,\mathrm{V/s})=55$ ms. (c) Eine Halbperiode von 5 ms ändert $u_\mathrm{A}$ um 2,5 V, die Amplitude ist 1,25 V. Bei 20 Hz ist der Hub 12,5 V. Bei $u_\mathrm{A}(0)=0$ und positivem Start erreicht das Dreieck $-11$ V und schlägt an.
:::
:::

:::aufgabe Aufgabe 8 ★★ Logarithmierer
<span class="anker" id="aufg-8"></span>

$R=1$ k$\Omega$, $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A. (a) Berechne $U_\mathrm{A}$ für 1 V und 2 V. Sage die Differenz vorher, ohne $I_\mathrm{S}$ zu benutzen. (b) Wie weit überstreicht $U_\mathrm{A}$, wenn $U_\mathrm{E}$ von 10 mV bis 10 V läuft? (c) Bei 330 K statt 300 K ist $U_T=28{,}6$ mV. Um wie viel verschiebt allein das $U_\mathrm{A}$ bei 100 µ A Strom?

:::loesung
(a) 1 mA ergibt $-0{,}582$ V, 2 mA ergeben $-0{,}600$ V. Die Differenz ist $U_T\ln2=18$ mV, ohne $I_\mathrm{S}$. (b) Drei Dekaden: $3\cdot59{,}9\,\mathrm{mV}=180$ mV. (c) $U_\mathrm{F}$ wächst von 0,522 V auf 0,574 V, also um 52 mV. In Wirklichkeit steigt auch $I_\mathrm{S}$ stark, deshalb braucht man die Temperaturkompensation.
:::
:::

::::formelsammlung
**Eingangsbauteil und Rückführbauteil**

$$I_\mathrm{ein}=-I_\mathrm{rück}$$

Knotenregel am Minus-Eingang bei Plus-Eingang an Masse; das Strom-Spannungs-Gesetz der beiden Bauteile legt die Operation fest.

**Integrierer**

$$u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t'$$

$R$ am Eingang, $C$ in der Rückführung; $R\,C$ ist eine Zeitkonstante in s. Idealer OPV, Ausgang innerhalb seiner Grenzen.

**Differenzierer**

$$u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}$$

$C$ am Eingang, $R$ in der Rückführung. Für einen Sinus ist $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$; hochfrequentes Rauschen wird besonders stark verstärkt.

**Logarithmierer**

$$U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$$

$R$ am Eingang, Diode in der Rückführung; $I_\mathrm{S}$ ist der Sättigungssperrstrom. Verlangt $U_\mathrm{E}>0$ und $U_\mathrm{E}/R\gg I_\mathrm{S}$. Jede Dekade am Eingang bringt $U_T\ln10$.

**Exponentialschaltung**

$$U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$$

Diode am Eingang, $R$ in der Rückführung. Verlangt $U_\mathrm{E}\gg U_T$.
::::

::::lernkarten
:::karte zusammenhang Eingangsbauteil und Rückführbauteil
Warum legen bei einem OPV mit Plus-Eingang an Masse allein die Strom-Spannungs-Gesetze von Eingangs- und Rückführbauteil fest, welche Rechenoperation entsteht?
---
Die Knotenregel verlangt $I_\mathrm{ein}=-I_\mathrm{rück}$. Das Eingangsbauteil macht aus $U_\mathrm{E}$ einen Strom, das Rückführbauteil verlangt für denselben Strom eine Ausgangsspannung.
--- falsch
Der OPV erkennt das Bauteil in der Rückführung und schaltet intern auf die passende Rechenart um; die Bauteile bestimmen nur den Maßstab des Ergebnisses, also seine Größe.
--- falsch
Die Knotenregel verlangt $I_\mathrm{ein}=I_\mathrm{rück}$ mit gleichem Vorzeichen; beide Bauteile führen ihren Strom gemeinsam zur virtuellen Masse ab.
--- falsch
Allein das Eingangsbauteil legt die Operation fest; das Rückführbauteil begrenzt nur den Strom und könnte ebenso gut ein beliebiger Widerstand mit passendem Wert sein.
:::
:::karte formel Integrierer
Wie hängt die Ausgangsspannung eines Integrierers mit $R$ am Eingang und $C$ in der Rückführung von der Eingangsspannung ab?
---
$u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t'$: das negative, durch $R\,C$ geteilte Integral der Eingangsspannung. Gilt, solange der Ausgang in seinen Grenzen bleibt.
--- falsch
$u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}$: die negative, mit $R\,C$ multiplizierte Ableitung der Eingangsspannung. Gilt, solange der Ausgang in seinen Grenzen bleibt und der OPV ideal ist.
--- falsch
$u_\mathrm{A}(t)=u_\mathrm{A}(0)+R\,C\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t'$: das positive, mit $R\,C$ multiplizierte Integral. Der Ausgang wächst dabei ohne jede Grenze.
--- falsch
$u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t'$, aber nur bis $t=R\,C$; danach ist der Kondensator voll, und $u_\mathrm{A}$ bleibt stehen.
:::
:::karte herleitung Integrierer aus der Knotenregel
Wie folgt aus der Knotenregel am Minus-Eingang, dass der Integrierer das Integral der Eingangsspannung bildet?
---
Durch $R$ fließt $i=u_\mathrm{E}/R$, weil sein rechtes Ende auf virtueller Masse liegt.
---
Dieser Strom lädt den Kondensator, $C\,\mathrm{d} u_C/\mathrm{d} t=i$, weil kein Strom in den Minus-Eingang fließen kann.
---
Die linke Platte liegt fest auf 0, also ist $u_\mathrm{A}=-u_C$, weil die Kondensatorspannung zwischen Knoten und Ausgang liegt.
---
Integriert man über die Zeit, folgt $u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t'$, weil die Änderungsgeschwindigkeit von $u_C$ proportional zu $u_\mathrm{E}$ ist.
:::
:::karte zusammenhang Konstanter Ladestrom
Warum steigt die Ausgangsspannung eines Integrierers bei konstanter Eingangsspannung gleichmäßig, während ein RC-Glied immer langsamer lädt?
---
Das rechte Ende von $R$ liegt auf virtueller Masse, deshalb bleibt der Ladestrom $U_\mathrm{E}/R$ fest. Beim RC-Glied sinkt er, weil die Kondensatorspannung der Quelle entgegensteht.
--- falsch
Der OPV verstärkt den Ladestrom mit $A$; dadurch ist der Kondensator schon nach einem Bruchteil von $R\,C$ voll, und der Anstieg wirkt nur gleichmäßig, weil er so kurz ist.
--- falsch
Beim Integrierer ist der Kondensator so groß, dass seine Spannung kaum steigt; mit kleinerem $C$ würde der Strom auch hier beim Laden sinken wie beim RC-Glied aus Widerstand und Kondensator.
--- falsch
Die Spannung an $R$ bleibt fest, weil der Ausgang am Anschlag steht; der Strom ist deshalb konstant, bis der Ausgang den Anschlag wieder verlässt.
:::
:::karte zusammenhang Rechteck wird Dreieck
Warum macht ein Integrierer aus einer Rechteckspannung eine Dreieckspannung?
---
In jeder Halbperiode ist $u_\mathrm{E}$ konstant, also läuft $u_\mathrm{A}$ gleichmäßig in eine Richtung und in der nächsten mit gleicher Steigung zurück. So entstehen gerade Flanken.
--- falsch
Der Kondensator lädt in jeder Halbperiode exponentiell auf und ab; die abgerundeten Flanken sehen bei hoher Frequenz nur wie ein Dreieck aus.
--- falsch
Der Integrierer bildet die Ableitung des Rechtecks; die Sprünge ergeben kurze Spitzen, die der OPV wegen seiner Trägheit zu einem Dreieck glättet.
--- falsch
In jeder Halbperiode ist $u_\mathrm{E}$ konstant, also bleibt $u_\mathrm{A}$ stehen; nur an den Sprüngen ändert er sich, und die Stufen verbinden sich zum Dreieck.
:::
:::karte formel Differenzierer
Wie hängt die Ausgangsspannung eines Differenzierers mit $C$ am Eingang und $R$ in der Rückführung von der Eingangsspannung ab?
---
$u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}$, weil durch den Kondensator $i=C\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$ fließt. Für einen Sinus wächst der Betrag mit der Frequenz, $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$.
--- falsch
$u_\mathrm{A}(t)=-\frac{1}{R\,C}\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}$; für einen Sinus sinkt der Betrag mit der Frequenz, $\hat u_\mathrm{A}/\hat u_\mathrm{E}=1/(2\pi f\,R\,C)$.
--- falsch
$u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}$; für einen Sinus hängt der Betrag nicht von der Frequenz ab, nur die Phase verschiebt sich um ein Viertel der Periode.
--- falsch
$u_\mathrm{A}(t)=-R\,C\,u_\mathrm{E}(t)$: Der Kondensator wirkt am Eingang wie ein Widerstand, und der Ausgang ist die verstärkte Eingangsspannung mit umgekehrtem Vorzeichen.
:::
:::karte zusammenhang Differenzierer und Rauschen
Warum verstärkt ein Differenzierer hochfrequentes Rauschen besonders stark?
---
Für einen Sinus ist $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$, der Betrag wächst also mit der Frequenz. Rauschen enthält viele hohe Frequenzen, die so am stärksten gehoben werden.
--- falsch
Der Kondensator am Eingang rauscht selbst, und zwar umso stärker, je höher die Frequenz ist; mit einem Widerstand am Eingang entfiele dieses Rauschen.
--- falsch
Der Differenzierer arbeitet ohne Gegenkopplung, deshalb verstärkt er jedes Signal mit der vollen Leerlaufverstärkung $A$, das Rauschen eingeschlossen.
--- falsch
Für einen Sinus ist $\hat u_\mathrm{A}/\hat u_\mathrm{E}=1/(2\pi f\,R\,C)$; tiefe Frequenzen werden also gehoben, und dort liegt das meiste Rauschen.
:::
:::karte formel Logarithmierer
Welche Ausgangsspannung liefert ein Logarithmierer mit $R$ am Eingang und einer Diode in der Rückführung, und wann gilt sie?
---
$U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$ mit dem Sättigungssperrstrom $I_\mathrm{S}$, gültig für $U_\mathrm{E}>0$ und $U_\mathrm{E}/R\gg I_\mathrm{S}$. Jede Dekade am Eingang bringt $U_T\ln10=59{,}9$ mV.
--- falsch
$U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$ für beide Vorzeichen von $U_\mathrm{E}$; bei negativem Eingang wird der Ausgang einfach positiv und folgt dem Betrag.
--- falsch
$U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$, gültig für $U_\mathrm{E}\gg U_T$; jede Verdoppelung der Eingangsspannung verdoppelt auch die Ausgangsspannung.
--- falsch
$U_\mathrm{A}=-U_T\,\lg\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$ mit dem Zehnerlogarithmus, gültig für $U_\mathrm{E}>0$; jede Dekade am Eingang bringt genau $U_T=26$ mV.
:::
:::karte herleitung Logarithmierer aus der Knotenregel
Wie folgt aus der Knotenregel und der Diodenkennlinie die Ausgangsspannung des Logarithmierers?
---
Durch $R$ fließt $I=U_\mathrm{E}/R$, weil sein rechtes Ende auf virtueller Masse liegt.
---
Derselbe Strom fließt durch die Diode, $I=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{F}/U_T}$, weil kein Strom in den Minus-Eingang fließt.
---
Die Diodenspannung ist $U_\mathrm{F}=-U_\mathrm{A}$, weil die Diode zwischen dem Knoten auf 0 V und dem Ausgang liegt.
---
Auflösen nach $U_\mathrm{A}$ ergibt $U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$, weil der Logarithmus die e-Funktion umkehrt.
:::
:::karte formel Exponentialschaltung
Welche Ausgangsspannung liefert die Exponentialschaltung mit einer Diode am Eingang und $R$ in der Rückführung?
---
$U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ für $U_\mathrm{E}\gg U_T$: $U_\mathrm{E}$ liegt an der Diode, und ihr Strom fließt durch $R$. Je 18 mV mehr am Eingang verdoppeln den Betrag.
--- falsch
$U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}$: $U_\mathrm{E}$ liegt an der Diode, und ihr Strom fließt durch $R$. Je 60 mV mehr am Eingang verdoppeln den Betrag.
--- falsch
$U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ für $U_\mathrm{E}\ll U_T$; für größere Eingangsspannungen bleibt der Ausgang konstant bei $-R\,I_\mathrm{S}$.
--- falsch
$U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_T/U_\mathrm{E}}$ für $U_\mathrm{E}\gg U_T$: Der Betrag sinkt, wenn die Eingangsspannung wächst, und nähert sich $R\,I_\mathrm{S}$.
:::
:::karte zusammenhang Gesperrte Diode im Logarithmierer
Was passiert mit einem Logarithmierer, wenn die Eingangsspannung negativ wird?
---
Die Diode sperrt, die Rückführung ist unterbrochen: Der Ausgang läuft zum Anschlag. Die Regel gilt nur, solange der Rückweg leitet.
--- falsch
Der Ausgang wird positiv und zeigt den Logarithmus des Betrags; der Logarithmierer arbeitet für beide Vorzeichen gleich gut.
--- falsch
Die Diode lässt in Sperrrichtung den Strom $I_\mathrm{S}$ durch; der Ausgang bleibt auf 0 V stehen, bis $U_\mathrm{E}$ wieder positiv ist.
--- falsch
Die Diode bricht durch und wirkt wie eine Spannungsquelle; der Ausgang hält dann die Durchbruchspannung, und die Regel gilt weiter wie zuvor.
:::
:::karte zusammenhang Multiplizieren
Warum kann eine Kette aus zwei Logarithmierern, einem Addierer und einer Exponentialschaltung zwei Spannungen multiplizieren?
---
Wegen $\ln x+\ln y=\ln(x\,y)$: Der Addierer summiert die Logarithmen, und die Exponentialschaltung macht daraus bis auf einen festen Faktor das Produkt $U_x\,U_y$. Daher stammt der Name Operationsverstärker.
--- falsch
Der Addierer multipliziert die Spannungen direkt, wenn alle Widerstände gleich sind; die Logarithmierer schützen ihn nur vor zu großen Eingangsspannungen und begrenzen sie.
--- falsch
Wegen $\ln x\cdot\ln y=\ln(x+y)$: Die Exponentialschaltung multipliziert die Logarithmen, und der Addierer bildet daraus die Summe $U_x+U_y$.
--- falsch
Wegen $\ln x+\ln y=\ln(x\,y)$; temperaturunabhängig ist das Produkt aber nur mit Dioden, Transistoren an ihrer Stelle würden es verfälschen und den Faktor verschieben.
:::
::::
