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
