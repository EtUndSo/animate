---
title: Stufe 1: Das verzerrungsfreie System
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250200
summary: Was genau soll eine „gute“ Übertragung leisten?
tags: Phasenlaufzeit, Gruppenlaufzeit
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Was genau soll eine „gute“ Übertragung leisten? Und mit welchen Kenngrößen misst man, wie weit ein System davon abweicht?
:::

**Die Idee.** Ein Signal ist unverzerrt angekommen, wenn es nur lauter oder leiser und später ist, seine Form aber gleich:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

Im Spektrum heißt das: Jede Schwingung wird mit demselben Faktor $h_0$ multipliziert, und jede wird um dieselbe Zeit $t_0$ verschoben. Eine Zeitverschiebung $t_0$ ist bei der Frequenz $f$ der Winkel $2\pi ft_0$. Deshalb muss die Phase $\varphi(f)=-2\pi t_0f$ eine Gerade durch den Ursprung sein.

:::definition Definition 1.1 (Kenngrößen eines LTI-Systems)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Dämpfungsmaß:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{bzw.}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Dämpfungswinkel:} && b(f)=-\varphi(f),\\ &\text{Phasenlaufzeit:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Gruppenlaufzeit:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**So liest man das:** Die __Phasenlaufzeit__ ist die Verzögerung einer einzelnen Schwingung der Frequenz $f$. Die __Gruppenlaufzeit__ ist die Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve (Stufe [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)). Beim verzerrungsfreien System sind $a$, $t_\mathrm p$ und $t_\mathrm g$ konstant und $t_\mathrm p=t_\mathrm g=t_0$.

::::beispiel das RC-Glied
Mit $\varphi=-\arctan(2\pi f\,RC)$ und $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

Für $f\to0$ sind beide $RC=1$ s. Bei $f=0{,}159$ Hz ($2\pi fRC=1$) ist $t_\mathrm p=0{,}785$ s, $t_\mathrm g=0{,}5$ s und $a=3{,}0$ dB. Das RC-Glied ist also nicht verzerrungsfrei: Es dämpft frequenzabhängig, und verschiedene Frequenzen kommen verschieden spät an.
::::

:::ltspice Dämpfung und Laufzeiten des RC-Glieds ablesen
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`), Quellwert `AC 1`, Direktive `.ac dec 100 0.01 10`.

⁠**Ablesen:** Die linke Achse zeigt $20\lg|H|=-a$ in dB. Fahre mit der Maus auf die rechte Achse (Phase), bis der Zeiger zum Lineal wird, klicke und wähle „Group Delay“: Dann zeigt sie $t_\mathrm g(f)$ nach [(1.5)](#gl-1-5). Die Phasenlaufzeit rechnest du aus der Phase, $t_\mathrm p=-\varphi/(2\pi f)$ mit $\varphi$ im Bogenmaß.

⁠**Was du siehst:** Zu tiefen Frequenzen hin strebt $t_\mathrm g$ gegen 1 s. Bei 0,159 Hz liest du $a=3{,}0$ dB, $\varphi=-45^\circ$ und $t_\mathrm g=0{,}5$ s ab, daraus $t_\mathrm p=0{,}785$ s. Vergleiche die Werte bei $2\pi fRC=10$ mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(b).
:::

:::aufgabe Aufgabe 1 ★ Laufzeiten des RC-Glieds
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Leite $t_\mathrm g$ des RC-Glieds aus [(1.5)](#gl-1-5) her.

</li>

<li>

Berechne $t_\mathrm p$, $t_\mathrm g$ und $a$ bei $2\pi fRC=10$. In welchem Frequenzbereich ist das RC-Glied näherungsweise verzerrungsfrei?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$, also $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) Bei $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0{,}147$ s, $t_\mathrm g=\frac{RC}{101}=0{,}0099$ s, $a=20{,}0$ dB. Näherungsweise verzerrungsfrei ist das RC-Glied nur für $2\pi fRC\ll1$, also weit unter 0,16 Hz: Dort ist $|H|\approx1$ und $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::

::::formelsammlung
**Verzerrungsfreies System**

$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}$$

Das Signal wird nur mit dem Faktor $h_0$ verstärkt oder abgeschwächt und um $t_0$ verzögert, seine Form bleibt gleich. Im Spektrum: jede Schwingung mit demselben Faktor, jede um dieselbe Zeit verschoben.

**Phase des verzerrungsfreien Systems**

$$\varphi(f)=-2\pi t_0f$$

Eine Zeitverschiebung $t_0$ ist bei der Frequenz $f$ der Winkel $2\pi ft_0$. Die Phase ist deshalb eine Gerade durch den Ursprung.

**Dämpfungsmaß**

$$a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{bzw.}\quad a(f)=-\ln|H(f)|\ \text{Np}$$

Abschwächung des Betrags, logarithmisch in Dezibel oder Neper; positiv, wenn das System dämpft.

**Dämpfungswinkel**

$$b(f)=-\varphi(f)$$

Negative Phase des Frequenzgangs.

**Phasenlaufzeit**

$$t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f}$$

Verzögerung einer einzelnen Schwingung der Frequenz $f$; $\varphi$ im Bogenmaß.

**Gruppenlaufzeit**

$$t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}$$

Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve. Beim verzerrungsfreien System sind $a$, $t_\mathrm p$ und $t_\mathrm g$ konstant und $t_\mathrm p=t_\mathrm g=t_0$.

**Laufzeiten des RC-Glieds**

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}$$

Aus der Phase $\varphi=-\arctan(2\pi f\,RC)$. Für $f\to0$ sind beide $RC$; näherungsweise verzerrungsfrei ist das RC-Glied nur für $2\pi fRC\ll1$.
::::

::::lernkarten
:::karte formel Verzerrungsfreies System
Wie lauten Ausgangssignal, Impulsantwort und Frequenzgang eines Systems, das ein Signal verzerrungsfrei überträgt?
---
$g(t)=h_0\,s(t-t_0)$, $h(t)=h_0\,\delta(t-t_0)$ und $H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: Das Signal wird nur mit dem Faktor $h_0$ verstärkt oder abgeschwächt und um $t_0$ verzögert, seine Form bleibt gleich.
--- falsch
$g(t)=h_0\,s(t-t_0)$ mit $H(f)=h_0\,\mathrm{e}^{-\mathrm{j}\varphi_0}$: Alle Frequenzen werden um denselben festen Winkel $\varphi_0$ gedreht, unabhängig von $f$; das entspricht für jede Schwingung derselben Verzögerung $t_0$.
--- falsch
$g(t)=h_0\,s(t-t_0)$, wobei nur $|H(f)|=h_0$ gelten muss: Für die Form zählt allein der Betrag; die Phase darf beliebig von der Frequenz abhängen, weil sie nur den Zeitpunkt der Ankunft bestimmt.
--- falsch
$g(t)=h_0\,s(t)$ mit $h(t)=h_0\,\delta(t)$ und $H(f)=h_0$: Das System darf das Signal nur verstärken oder abschwächen; schon eine Verzögerung um $t_0$ würde die Form des Signals verändern.
:::
:::karte zusammenhang Lineare Phase
Warum muss die Phase eines verzerrungsfreien Systems eine Gerade durch den Ursprung sein?
---
Weil jede Schwingung um dieselbe Zeit $t_0$ verschoben werden soll und eine Zeitverschiebung $t_0$ bei der Frequenz $f$ den Winkel $2\pi ft_0$ bedeutet. Der Winkel wächst also proportional mit $f$: $\varphi(f)=-2\pi t_0f$.
--- falsch
Weil jede Schwingung um denselben Winkel gedreht werden soll; eine Gerade durch den Ursprung ist die einzige Phase, die für alle Frequenzen denselben Winkel liefert, und verschiebt deshalb alle Schwingungen gleich.
--- falsch
Weil die Phase bei $f=0$ verschwinden muss, damit der Gleichanteil erhalten bleibt; wie sie bei höheren Frequenzen verläuft, ist für die Form des Signals ohne Bedeutung.
--- falsch
Weil hohe Frequenzen im System stärker gedämpft werden; die mit $f$ fallende Phase gleicht diese Dämpfung genau aus, sodass am Ende alle Schwingungen gleich stark ankommen.
:::
:::karte formel Dämpfungsmaß und Dämpfungswinkel
Wie sind das Dämpfungsmaß und der Dämpfungswinkel eines LTI-Systems aus seinem Frequenzgang $H(f)$ definiert?
---
$a(f)=-20\lg|H(f)|$ dB bzw. $a(f)=-\ln|H(f)|$ Np und $b(f)=-\varphi(f)$. Das Dämpfungsmaß beschreibt die Abschwächung des Betrags, der Dämpfungswinkel ist die negative Phase.
--- falsch
$a(f)=20\lg|H(f)|$ dB und $b(f)=\varphi(f)$: Das Dämpfungsmaß ist positiv, wenn das System das Signal verstärkt, und der Dämpfungswinkel ist die Phase selbst.
--- falsch
$a(f)=-10\lg|H(f)|$ dB und $b(f)=-\varphi(f)$: Weil $|H|$ eine Leistungsgröße ist, nimmt man den zehnfachen Logarithmus; der Dämpfungswinkel ist die negative Phase.
--- falsch
$a(f)=-20\lg|H(f)|$ dB und $b(f)=-\frac{\mathrm{d}\varphi}{\mathrm{d} f}$: Das Dämpfungsmaß beschreibt die Abschwächung des Betrags, der Dämpfungswinkel die Steigung der Phase über der Frequenz.
:::
:::karte begriff Phasenlaufzeit
Was gibt die Phasenlaufzeit eines LTI-Systems bei der Frequenz $f$ an, und wie berechnet man sie aus der Phase?
---
Die Phasenlaufzeit ist die Verzögerung einer einzelnen Schwingung der Frequenz $f$: $t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f}$. Sie rechnet den Phasenwinkel bei dieser Frequenz in eine Zeit um.
--- falsch
Die Phasenlaufzeit ist die Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve: $t_\mathrm p(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}$. Sie ergibt sich aus der Steigung der Phase.
--- falsch
Die Phasenlaufzeit ist der Phasenwinkel selbst: $t_\mathrm p(f)=-\varphi(f)$. Sie gibt an, um wie viel Grad eine Schwingung der Frequenz $f$ beim Durchlaufen des Systems gedreht wird.
--- falsch
Die Phasenlaufzeit ist die Verzögerung einer Schwingung der Frequenz $f$: $t_\mathrm p(f)=-2\pi f\,\varphi(f)$. Sie wächst bei fester Phase mit der Frequenz, weil schnelle Schwingungen mehr Perioden durchlaufen.
:::
:::karte begriff Gruppenlaufzeit
Was beschreibt die Gruppenlaufzeit eines LTI-Systems, und wie hängt sie mit der Phase zusammen?
---
Die Gruppenlaufzeit ist die Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve: $t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}$. Sie ist durch die Steigung der Phase bestimmt.
--- falsch
Die Gruppenlaufzeit ist die Verzögerung einer einzelnen Schwingung der Frequenz $f$: $t_\mathrm g(f)=-\frac{\varphi(f)}{2\pi f}$. Sie ist durch den Wert der Phase bei dieser Frequenz bestimmt.
--- falsch
Die Gruppenlaufzeit ist die mittlere Verzögerung aller Frequenzen, die ein System durchlässt. Sie ist durch die Fläche unter der Phasenkurve bestimmt und hängt deshalb nicht von $f$ ab.
--- falsch
Die Gruppenlaufzeit beschreibt, wie stark eine Gruppe benachbarter Frequenzen gedämpft wird: $t_\mathrm g(f)=-\frac{\mathrm{d} a(f)}{\mathrm{d} f}$. Sie ist durch die Steigung des Dämpfungsmaßes bestimmt.
:::
:::karte zusammenhang Laufzeiten des verzerrungsfreien Systems
Was gilt für Dämpfungsmaß, Phasenlaufzeit und Gruppenlaufzeit eines verzerrungsfreien Systems?
---
Alle drei sind konstant, und es gilt $t_\mathrm p=t_\mathrm g=t_0$. Weil die Phase $\varphi(f)=-2\pi t_0f$ eine Gerade durch den Ursprung ist, liefern Quotient und Steigung denselben Wert.
--- falsch
Das Dämpfungsmaß ist konstant, die Laufzeiten wachsen mit der Frequenz: Weil die Phase $\varphi(f)=-2\pi t_0f$ mit $f$ immer weiter fällt, kommen hohe Frequenzen später an als tiefe.
--- falsch
Alle drei sind null: Ein verzerrungsfreies System darf das Signal weder abschwächen noch verzögern, denn jede Verzögerung verändert bereits die Lage und damit die Form.
--- falsch
Alle drei sind konstant, aber es gilt $t_\mathrm g=2t_\mathrm p$: Die Gruppenlaufzeit enthält die Ableitung der Phase und ist deshalb bei einer Geraden doppelt so groß wie die Phasenlaufzeit.
:::
:::karte formel Laufzeiten des RC-Glieds
Wie lauten Phasenlaufzeit und Gruppenlaufzeit des RC-Glieds mit der Phase $\varphi=-\arctan(2\pi f\,RC)$?
---
$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f}$ und $t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}$. Für $f\to0$ sind beide gleich $RC$; mit wachsender Frequenz werden beide kleiner und weichen voneinander ab.
--- falsch
$t_\mathrm p=t_\mathrm g=RC$ für alle Frequenzen: Das RC-Glied verzögert jede Schwingung um seine Zeitkonstante, weil seine Phase linear mit der Frequenz fällt.
--- falsch
$t_\mathrm p=\frac{RC}{1+(2\pi f\,RC)^2}$ und $t_\mathrm g=\frac{\arctan(2\pi f\,RC)}{2\pi f}$: Die Phasenlaufzeit enthält die Ableitung des Arcustangens, die Gruppenlaufzeit den Quotienten aus Phase und Kreisfrequenz.
--- falsch
$t_\mathrm p=\arctan(2\pi f\,RC)$ und $t_\mathrm g=2\pi f\,RC$: Beide wachsen mit der Frequenz, sodass hohe Frequenzen später ankommen als tiefe und sich die Kanten des Signals verschieben.
:::
:::karte zusammenhang RC-Glied nicht verzerrungsfrei
Warum ist das RC-Glied kein verzerrungsfreies System, und in welchem Frequenzbereich ist es näherungsweise verzerrungsfrei?
---
Es dämpft frequenzabhängig, und seine Laufzeiten hängen von der Frequenz ab: Verschiedene Frequenzen kommen verschieden spät an. Nur für $2\pi fRC\ll1$ ist $|H|\approx1$ und $t_\mathrm p\approx t_\mathrm g\approx RC$.
--- falsch
Es verzögert alle Frequenzen gleich, dämpft aber die hohen stärker. Näherungsweise verzerrungsfrei ist es für $2\pi fRC\gg1$, weil die Dämpfung dort gleichmäßig um 20 dB je Dekade wächst.
--- falsch
Es dämpft alle Frequenzen gleich, verzögert aber die tiefen stärker als die hohen. Näherungsweise verzerrungsfrei ist es nur genau bei $2\pi fRC=1$, weil dort Phasen- und Gruppenlaufzeit übereinstimmen.
--- falsch
Es ist nur wegen seiner Phase nicht verzerrungsfrei, sein Betrag ist konstant. Näherungsweise verzerrungsfrei ist es bei allen Frequenzen, bei denen die Phase betragsmäßig unter $45^\circ$ bleibt.
:::
:::karte herleitung Gruppenlaufzeit des RC-Glieds
Wie folgt aus $\varphi=-\arctan(2\pi fRC)$ und $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$ die Gruppenlaufzeit des RC-Glieds?
---
Man leitet die Phase nach $f$ ab und erhält $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$, weil die Ableitung von $\arctan x$ gleich $1/(1+x^2)$ ist und die innere Ableitung von $2\pi fRC$ den Faktor $2\pi RC$ liefert.
---
Man setzt diese Ableitung in $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$ ein, weil die Gruppenlaufzeit so definiert ist; die beiden Minuszeichen und die Faktoren $2\pi$ heben sich auf.
---
Es bleibt $t_\mathrm g=\frac{RC}{1+(2\pi fRC)^2}$, das für $f\to0$ gegen $RC$ geht, weil der Nenner dort gegen 1 strebt.
:::
::::
