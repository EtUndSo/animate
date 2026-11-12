---
title: Stufe 2: Ein erstes System, das RC-Glied
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210300
summary: Am RC-Tiefpass (Abb.
tags: Frequenzgang
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Am RC-Tiefpass (Abb. [2](#abb-2)) lässt sich ausrechnen, wie ein System auf zwei typische Eingänge antwortet: auf eine komplexe Exponentialfunktion und auf einen Sprung.
:::

**Die Differentialgleichung.** Der Strom durch $R$ ist $(u_1-u_2)/R$. Er fließt vollständig in den Kondensator und lädt ihn, $C\,\dot u_2=(u_1-u_2)/R$. Umgestellt:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung 2
RC-Tiefpass: Eingang $u_1$, Ausgang $u_2$ am Kondensator. Im Rechenmodell ist $RC=1$ s.
:::

**Eingang $\mathrm{e}^{\mathrm{j}2\pi Ft}$: der Ausgang ist eine Zahl mal der Eingang.** Legt man $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ an, hat der Ausgang im eingeschwungenen Zustand dieselbe Form, nur mit anderer Amplitude und Phase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Die Zahl $H(F)$ hängt von der Frequenz ab und heißt deshalb __Frequenzgang__. Der Grund ist, dass Ableiten die Form nicht ändert, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Eingesetzt in [(2.1)](#gl-2-1):

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

Dasselbe liefert die Wechselstromrechnung mit Zeigern: Der Kondensator hat die Impedanz $1/(\mathrm{j}2\pi FC)$, und die Schaltung ist ein Spannungsteiler,

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

Die reelle Spannung zu einem Zeiger ist $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$ (Effektivwertzeiger).

:::satz Satz 2.1 (Übertragungsfunktion des RC-Tiefpasses)
<span class="anker" id="satz-2-1"></span>

Mit $x=2\pi FRC$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**So liest man das:** $|H|$ sagt, um welchen Faktor die Amplitude schrumpft. $\varphi$ ist negativ: Die Schwingung eilt um den Winkel $-\varphi=\arctan x$ nach. Bei $x=1$, also $F=1/(2\pi RC)=0{,}16$ Hz im Rechenmodell, ist $|H|=0{,}707$ und $\varphi=-45^\circ$. Bei $x=10$ ist $|H|=0{,}0995$ und $\varphi=-84{,}3^\circ$ (Abb. [3](#abb-3)). **Grenzfälle:** $F\to0$ ergibt $H\to1$ (der Kondensator hat Zeit, sich voll aufzuladen), $F\to\infty$ ergibt $H\to0$ mit $\varphi\to-90^\circ$ (der Kondensator wirkt wie ein Kurzschluss).

:::abbildung et3/k1bode 3
Betrag und Phase der Übertragungsfunktion des RC-Tiefpasses über $x=2\pi FRC$ (logarithmisch). Langsame Schwingungen kommen fast unverändert durch, schnelle werden geschwächt und eilen bis zu $90^\circ$ nach.
:::

**Die Phase allgemein.** Für eine beliebige komplexe Zahl $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$ gilt

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{ganzzahlig}, \tag{2.4}$$

wobei $\arctan$ den Hauptwert in $[-\pi/2,\pi/2]$ liefert.

:::frage Warum braucht die Phasenformel den Zusatz $\lambda\pi$?
$\arctan$ sieht nur das Verhältnis $\operatorname{Im}/\operatorname{Re}$. Die Zahlen $1+\mathrm{j}$ und $-1-\mathrm{j}$ haben dasselbe Verhältnis 1, liegen aber in entgegengesetzten Quadranten. $\arctan1=45^\circ$ stimmt für $1+\mathrm{j}$. Für $-1-\mathrm{j}$ ist der wahre Winkel $45^\circ+180^\circ=225^\circ$, gleichwertig $-135^\circ$ (mit $l=-1$). Immer wenn der Realteil negativ ist, muss man $\pi$ addieren.
:::

**Eingang Sprung: die Exponentialkurve.** Bei $t=0$ wird $u_1=1$ V angelegt, der Kondensator ist leer. Für $t\ge0$ liefert die Maschenregel mit dem Strom $i$

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

Ableiten gibt $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, also $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, und Integrieren

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

denn im ersten Moment liegt die ganze Spannung an $R$. Mit der Maschenregel $u_2=1-R\,i$ folgt

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

Der Mechanismus: Je voller der Kondensator, desto weniger Spannung bleibt für $R$, desto kleiner der Ladestrom, desto langsamer füllt er sich weiter. Diese Rückwirkung macht die Kurve exponentiell.

:::ltspice RC-Tiefpass: Sprungantwort und Frequenzgang
⁠**Zeichnen:** Quelle `voltage` am Netz `in`, `res` mit `1Meg` von `in` nach `out`, `cap` mit `1u` von `out` nach Masse, also $RC=1$ s. Vorsicht: SPICE liest `1M` als 1 Milli, Mega heißt `Meg`.

⁠**Sprung:** Quelle `PULSE(0 1 0 1u 1u 100)`, Direktive `.tran 5`. Genaue Werte liefert eine Messung wie `.meas tran g1 FIND V(out) AT=1`, das Ergebnis steht im SPICE Error Log (View, SPICE Error Log). Erwartet: 0,393 bei 0,5 s, 0,632 bei 1 s und 0,950 bei 3 s, also $1-\mathrm{e}^{-t}$ wie in [(2.5)](#gl-2-5).

⁠**Frequenzgang:** Quellwert `AC 1`, statt `.tran` die Direktive `.ac dec 100 0.01 100`. LTspice zeichnet den Betrag in dB (durchgezogen) und die Phase (gestrichelt). Bei 0,159 Hz ($x=1$) stehen dort $-3{,}0$ dB, also $|H|=0{,}707$, und $-45^\circ$. Vergleiche die Werte bei $x=10$ mit deinem Ergebnis aus Aufgabe [2](#aufg-2)(a).
:::

:::aufgabe Aufgabe 2 ★★ Frequenzgang und Phase
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Berechne $|H|$ und $\varphi$ des RC-Tiefpasses für $x=0$, $1$ und $10$. Bei welcher Frequenz in Hz liegt $x=10$ im Rechenmodell?

</li>

<li>

Ein Signal $u_1(t)=\cos(2\pi Ft)$ mit $x=1$ liegt an. Schreibe $u_2(t)$ hin. Um wie viel Sekunden eilt $u_2$ nach, wenn $RC=1$ s?

</li>

<li>

Bestimme mit [(2.4)](#gl-2-4) die Phasen von $-1-\mathrm{j}$, $-\mathrm{j}$ und $-2$.

</li>

</ol>

:::loesung
(a) $x=0$: $|H|=1$, $\varphi=0$. $x=1$: $|H|=0{,}707$, $\varphi=-45^\circ$. $x=10$: $|H|=0{,}0995$, $\varphi=-84{,}3^\circ$. $x=10$ bedeutet $F=10/(2\pi RC)=1{,}59$ Hz.

(b) $u_2(t)=0{,}707\cos(2\pi Ft-45^\circ)$ mit $2\pi F=1/\mathrm s$, also $F=0{,}159$ Hz. Nacheilen um $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0{,}785$ s.

(c) $-1-\mathrm{j}$: $\arctan1=45^\circ$, Realteil negativ, also $+180^\circ$: $225^\circ$, gleichwertig $-135^\circ$. $-\mathrm{j}$: Realteil null, Imaginärteil negativ; $\arctan(\operatorname{Im}/\operatorname{Re})$ strebt gegen $-90^\circ$, die Phase ist $-90^\circ$. $-2$: $\arctan0=0$, Realteil negativ, also $180^\circ$.
:::
:::

::::kurzfassung
Der RC-Tiefpass antwortet auf eine komplexe Exponentialfunktion mit derselben Funktion, multipliziert mit einer Zahl. Auf einen Sprung antwortet er mit einer Exponentialkurve.

Der Strom $(u_1-u_2)/R$ durch $R$ lädt den Kondensator. Daraus folgt die Differentialgleichung $RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1$ mit dem Eingang $u_1$ und dem Ausgang $u_2$ am Kondensator. Liegt $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ an, ist der Ausgang im eingeschwungenen Zustand $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Die Zahl $H(F)$ hängt von der Frequenz ab und heißt __Frequenzgang__:

$$H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

Mit $x=2\pi FRC$ ist der Betrag $|H(F)|=\frac{1}{\sqrt{1+x^2}}$ der Faktor, um den die Amplitude schrumpft. Die Phase $\varphi(F)=-\arctan x$ ist negativ: Der Ausgang eilt dem Eingang um den Winkel $\arctan x$ nach. Für $F\to0$ geht $H\to1$, für $F\to\infty$ geht $H\to0$ mit $\varphi\to-90^\circ$. Wird bei leerem Kondensator ein Sprung auf 1 V angelegt, antwortet das Glied mit $u_2(t)=1-\mathrm{e}^{-t/RC}$ für $t\ge0$; das ist seine __Sprungantwort__.

Der Grund: Ableiten ändert die Form von $\mathrm{e}^{\mathrm{j}2\pi Ft}$ nicht, es multipliziert nur mit $\mathrm{j}2\pi F$. Aus der Differentialgleichung wird so eine Gleichung für die Zahl $H(F)$. Beim Sprung wirkt eine Rückwirkung: Je voller der Kondensator, desto kleiner der Ladestrom, desto langsamer füllt er sich weiter.

Falle: $\arctan$ sieht nur das Verhältnis von Imaginär- zu Realteil. Ist der Realteil negativ, muss man zur Phase $\pi$ addieren.
::::

::::formelsammlung
**Differentialgleichung des RC-Tiefpasses**

$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1$$

$u_1$ Eingang, $u_2$ Ausgang am Kondensator. Der Strom $(u_1-u_2)/R$ durch $R$ fließt vollständig in den Kondensator, $C\,\dot u_2=(u_1-u_2)/R$.

**Ableitung der komplexen Exponentialfunktion**

$$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$$

Ableiten ändert die Form nicht; deshalb antwortet der RC-Tiefpass auf $\mathrm{e}^{\mathrm{j}2\pi Ft}$ im eingeschwungenen Zustand mit $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$.

**Frequenzgang des RC-Tiefpasses**

$$H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}$$

Komplexe Zahl, mit der der Tiefpass $\mathrm{e}^{\mathrm{j}2\pi Ft}$ im eingeschwungenen Zustand multipliziert; hängt von der Frequenz $F$ ab.

**Spannungsteiler mit Zeigern**

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1$$

Impedanz des Kondensators $1/(\mathrm{j}2\pi FC)$; $\underline U_1$, $\underline U_2$ Zeiger von Ein- und Ausgangsspannung.

**Reelle Spannung zum Effektivwertzeiger**

$$u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$$

Effektivwertzeiger: $|\underline U|$ Effektivwert, $\varphi$ Winkel des Zeigers.

**Real- und Imaginärteil**

$$\operatorname{Re}\{H\}=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2}$$

RC-Tiefpass, $x=2\pi FRC$.

**Betrag und Phase**

$$|H(F)|=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x$$

RC-Tiefpass, $x=2\pi FRC$. $|H|$: Faktor, um den die Amplitude schrumpft; $\varphi$: Der Ausgang eilt um den Winkel $\arctan x$ nach. Bei $x=1$, also $F=1/(2\pi RC)$: $|H|=0{,}707$, $\varphi=-45^\circ$. $F\to0$: $H\to1$; $F\to\infty$: $H\to0$, $\varphi\to-90^\circ$.

**Phase einer komplexen Zahl**

$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases}$$

Für jede komplexe Zahl $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$; $l$ ganzzahlig; $\arctan$ liefert den Hauptwert in $[-\pi/2,\pi/2]$ und sieht nur das Verhältnis, daher der Zusatz $\lambda\pi$ bei negativem Realteil.

**Ladestrom nach dem Sprung**

$$i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R$$

Sprung auf $u_1=1$ V bei $t=0$, Kondensator anfangs leer; im ersten Moment liegt die ganze Spannung an $R$.

**Sprungantwort des RC-Tiefpasses**

$$u_2(t)=1-\mathrm{e}^{-t/RC}$$

Für $t\ge0$; Sprung auf $u_1=1$ V bei $t=0$, Kondensator anfangs leer. Aus der Maschenregel $u_2=1-R\,i$.
::::

::::lernkarten
:::karte formel Differentialgleichung des RC-Tiefpasses
Welche Differentialgleichung verknüpft Eingang $u_1$ und Ausgang $u_2$ des RC-Tiefpasses, und woher kommt sie?
---
$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1$. Der Strom $(u_1-u_2)/R$ durch $R$ fließt vollständig in den Kondensator und lädt ihn, $C\,\dot u_2=(u_1-u_2)/R$.
--- falsch
$RC\,\frac{\mathrm{d} u_1}{\mathrm{d} t}+u_1=u_2$. Der Strom $u_2/R$ durch $R$ lädt den Kondensator, und die Eingangsspannung folgt der Ladung mit einer Verzögerung.
--- falsch
$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}=u_1$. Der Strom $u_1/R$ fließt vollständig in den Kondensator, weil die Spannung am Kondensator den Strom durch $R$ nicht beeinflusst.
--- falsch
$\frac{1}{RC}\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1$. Der Strom durch $R$ ist $(u_1-u_2)\,R$; er fließt vollständig in den Kondensator und lädt ihn auf.
:::
:::karte begriff Frequenzgang
Was gibt der Frequenzgang $H(F)$ eines Systems wie des RC-Tiefpasses an?
---
Die komplexe Zahl, mit der das System die Eingangsschwingung $\mathrm{e}^{\mathrm{j}2\pi Ft}$ im eingeschwungenen Zustand multipliziert, $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Sie hängt von der Frequenz ab und legt Amplitude und Phase des Ausgangs fest.
--- falsch
Den zeitlichen Verlauf der Ausgangsspannung, nachdem am Eingang eine Schwingung der Frequenz $F$ eingeschaltet wurde, einschließlich des Einschwingens bis zum eingeschwungenen Zustand. Er hängt von der Frequenz ab, daher der Name.
--- falsch
Die reelle Zahl, um die das System die Frequenz einer Eingangsschwingung ändert: Aus $\mathrm{e}^{\mathrm{j}2\pi Ft}$ wird $\mathrm{e}^{\mathrm{j}2\pi H(F)t}$, Amplitude und Phase bleiben dabei gleich.
--- falsch
Die komplexe Zahl, die das System im eingeschwungenen Zustand zur Eingangsschwingung addiert, $u_2=\mathrm{e}^{\mathrm{j}2\pi Ft}+H(F)$. Sie hängt von der Frequenz ab und verschiebt den Ausgang nach oben.
:::
:::karte zusammenhang Ableiten ändert die Form nicht
Warum antwortet der RC-Tiefpass auf den Eingang $\mathrm{e}^{\mathrm{j}2\pi Ft}$ im eingeschwungenen Zustand wieder mit einer Funktion derselben Form?
---
Weil Ableiten die Form nicht ändert, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Mit $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$ wird jedes Glied der Differentialgleichung ein Vielfaches von $\mathrm{e}^{\mathrm{j}2\pi Ft}$, und es bleibt eine Gleichung für die Zahl $H(F)$.
--- falsch
Weil $\mathrm{e}^{\mathrm{j}2\pi Ft}$ den Betrag 1 hat. Signale mit dem Betrag 1 kommen durch jedes System unverändert hindurch, sie werden höchstens verzögert, und die Form bleibt deshalb erhalten; bei einem Sinus wäre das anders.
--- falsch
Weil Ableiten aus $\mathrm{e}^{\mathrm{j}2\pi Ft}$ einen reellen Kosinus macht. Der Ausgang ist deshalb im eingeschwungenen Zustand immer ein reeller Kosinus derselben Frequenz, nur kleiner.
--- falsch
Weil der RC-Tiefpass bei jeder Frequenz $H=1$ hat. Im eingeschwungenen Zustand ist der Kondensator voll geladen, und der Ausgang ist deshalb gleich dem Eingang.
:::
:::karte herleitung Frequenzgang des RC-Tiefpasses
Wie folgt aus der Differentialgleichung $RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1$ mit dem Eingang $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ der Frequenzgang des RC-Tiefpasses?
---
Man setzt $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$ an, weil der Ausgang im eingeschwungenen Zustand dieselbe Form wie der Eingang hat, nur mit anderer Amplitude und Phase.
---
Die Ableitung ist $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$, weil Ableiten die Form nicht ändert. Eingesetzt entsteht $H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}$.
---
Man teilt durch $\mathrm{e}^{\mathrm{j}2\pi Ft}$, weil dieser Faktor auf beiden Seiten steht und nie null wird, und erhält $H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}$.
---
Der Spannungsteiler mit Zeigern liefert dasselbe, weil der Kondensator die Impedanz $1/(\mathrm{j}2\pi FC)$ hat: $\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1$.
:::
:::karte formel Betrag und Phase
Wie groß sind Betrag und Phase des Frequenzgangs des RC-Tiefpasses, ausgedrückt mit $x=2\pi FRC$, und was bedeuten sie?
---
$|H(F)|=\frac{1}{\sqrt{1+x^2}}$ ist der Faktor, um den die Amplitude schrumpft. $\varphi(F)=-\arctan x$ ist negativ: Der Ausgang eilt um den Winkel $\arctan x$ nach. Bei $x=1$ ist $|H|=0{,}707$ und $\varphi=-45^\circ$.
--- falsch
$|H(F)|=\frac{1}{1+x^2}$ ist der Faktor, um den die Amplitude schrumpft; er ist gleich dem Realteil von $H$, weil der Imaginärteil nur die Phase trägt. $\varphi(F)=-\arctan x$, bei $x=1$ also $-45^\circ$ und $|H|=0{,}5$.
--- falsch
$|H(F)|=\frac{1}{\sqrt{1+x^2}}$ ist der Faktor, um den die Amplitude schrumpft. $\varphi(F)=+\arctan x$ ist positiv: Der Ausgang eilt voraus, weil der Kondensator die Spannung vorwegnimmt. Bei $x=1$ ist $\varphi=+45^\circ$.
--- falsch
$|H(F)|=\sqrt{1+x^2}$ ist der Faktor, um den die Amplitude wächst, weil der Kondensator bei höherer Frequenz schneller umgeladen wird. $\varphi(F)=-\arctan x$, bei $x=1$ also $-45^\circ$ und $|H|=1{,}41$.
:::
:::karte formel Real- und Imaginärteil
Wie lauten Real- und Imaginärteil des Frequenzgangs des RC-Tiefpasses, und wie folgt daraus der Betrag?
---
Mit $x=2\pi FRC$ ist $\operatorname{Re}\{H\}=\frac{1}{1+x^2}$ und $\operatorname{Im}\{H\}=\frac{-x}{1+x^2}$. Der Betrag ist $|H(F)|=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}}$.
--- falsch
Mit $x=2\pi FRC$ ist $\operatorname{Re}\{H\}=1$ und $\operatorname{Im}\{H\}=-x$, denn das sind die beiden Summanden im Nenner. Der Betrag ist deshalb $|H(F)|=\operatorname{Re}\{H\}+\operatorname{Im}\{H\}=1-x$.
--- falsch
Mit $x=2\pi FRC$ ist $\operatorname{Re}\{H\}=\frac{1}{1+x^2}$ und $\operatorname{Im}\{H\}=\frac{x}{1+x^2}$. Der Betrag ist $|H(F)|=\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2=\frac{1}{1+x^2}$, ganz ohne Wurzel.
--- falsch
Mit $x=2\pi FRC$ ist $\operatorname{Re}\{H\}=\frac{1}{1+x}$ und $\operatorname{Im}\{H\}=\frac{-x}{1+x}$. Der Betrag ist $|H(F)|=\sqrt{H\,H^*}=1$, weil sich die beiden Teile gegenseitig ausgleichen.
:::
:::karte zusammenhang Grenzfälle
Was passiert mit dem Frequenzgang des RC-Tiefpasses bei sehr kleinen und bei sehr großen Frequenzen, und warum?
---
Für $F\to0$ geht $H\to1$, weil der Kondensator Zeit hat, sich voll aufzuladen. Für $F\to\infty$ geht $H\to0$ mit $\varphi\to-90^\circ$, weil der Kondensator wie ein Kurzschluss wirkt.
--- falsch
Für $F\to0$ geht $H\to0$, weil der Kondensator Gleichspannung sperrt. Für $F\to\infty$ geht $H\to1$, weil der Kondensator dann wie ein Kurzschluss wirkt und alles durchlässt.
--- falsch
Für $F\to0$ geht $H\to1$. Für $F\to\infty$ geht $H\to0$ mit $\varphi\to-180^\circ$, weil sich die Phase mit wachsender Frequenz ohne Grenze immer weiter dreht.
--- falsch
In beiden Grenzfällen geht $H\to1$, weil der Kondensator weder bei Gleichspannung noch bei sehr schnellen Schwingungen nennenswert Ladung aufnimmt und so nichts abzweigt.
:::
:::karte zusammenhang Zusatz in der Phasenformel
Warum braucht die allgemeine Phasenformel $\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi$ den Zusatz $\lambda\pi$?
---
$\arctan$ sieht nur das Verhältnis $\operatorname{Im}/\operatorname{Re}$ und liefert den Hauptwert in $[-\pi/2,\pi/2]$. $1+\mathrm{j}$ und $-1-\mathrm{j}$ haben dasselbe Verhältnis, liegen aber in entgegengesetzten Quadranten. Bei negativem Realteil muss man deshalb $\pi$ addieren.
--- falsch
$\arctan$ liefert nur Winkel bis $\pi/4$. Für größere Winkel addiert man $\pi$, und zwar immer dann, wenn der Imaginärteil negativ ist, weil die Zahl dann unterhalb der reellen Achse liegt.
--- falsch
Die Phase eines Systems muss negativ sein, damit der Ausgang dem Eingang nacheilt. $\lambda\pi$ zieht bei positivem Realteil eine halbe Umdrehung ab und sorgt so dafür, dass der Winkel stets negativ wird, wie beim RC-Tiefpass.
--- falsch
$\arctan$ rechnet im Bogenmaß, die Phase gibt man aber in Grad an. $\lambda\pi$ rechnet das Ergebnis um, sobald der Realteil negativ ist; bei positivem Realteil stimmen beide Maße ohnehin überein.
:::
:::karte formel Effektivwertzeiger
Wie gewinnt man aus dem Effektivwertzeiger $\underline U$ einer Spannung die reelle Spannung $u(t)$?
---
$u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$. Der Betrag des Zeigers ist der Effektivwert, die Amplitude ist $\sqrt2$-mal so groß.
--- falsch
$u(t)=\operatorname{Re}\{|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=|\underline U|\cos(2\pi Ft+\varphi)$. Der Betrag des Zeigers ist die Amplitude; einen Faktor braucht man nicht, weil der Realteil schon reell ist.
--- falsch
$u(t)=\operatorname{Im}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\sin(2\pi Ft+\varphi)$. Der Betrag des Zeigers ist der Effektivwert, die reelle Spannung ist stets ein Sinus.
--- falsch
$u(t)=\operatorname{Re}\{|\underline U|/\sqrt2\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=|\underline U|\cos(2\pi Ft+\varphi)/\sqrt2$. Der Betrag des Zeigers ist die Amplitude, der Effektivwert ist $\sqrt2$-mal kleiner.
:::
:::karte begriff Sprungantwort
Was ist die Sprungantwort eines Systems, und wie verläuft sie beim RC-Tiefpass?
---
Die Antwort des Systems auf einen Sprung am Eingang. Beim RC-Tiefpass mit anfangs leerem Kondensator und einem Sprung auf $u_1=1$ V bei $t=0$ ist sie $u_2(t)=1-\mathrm{e}^{-t/RC}$ für $t\ge0$, eine Exponentialkurve von 0 gegen 1.
--- falsch
Die Antwort des Systems auf einen Sprung am Eingang. Beim RC-Tiefpass springt der Ausgang sofort mit auf 1 V, weil am Ausgang keine Last hängt und der Kondensator deshalb keinen Strom braucht.
--- falsch
Die Antwort des Systems auf einen Sprung am Eingang. Beim RC-Tiefpass ist sie eine Gerade mit der Steigung $1/RC$, die bei $t=RC$ den Endwert 1 erreicht und dort stehen bleibt, weil der Ladestrom konstant ist.
--- falsch
Der Sprung, den der Ausgang eines Systems macht, wenn man es einschaltet. Beim RC-Tiefpass ist das der Strom $i(t)=1-\mathrm{e}^{-t/RC}$, der von 0 gegen 1 steigt, bis der Kondensator voll ist.
:::
:::karte zusammenhang Rückwirkung beim Laden
Woran liegt es, dass die Sprungantwort des RC-Tiefpasses exponentiell verläuft und nicht geradlinig?
---
An einer Rückwirkung: Je voller der Kondensator, desto weniger Spannung bleibt für $R$, desto kleiner der Ladestrom, desto langsamer füllt er sich weiter.
--- falsch
Daran, dass der Widerstand mit wachsender Spannung zunimmt und den Ladestrom immer stärker bremst; mit konstantem $R$ verliefe die Ladung geradlinig.
--- falsch
Daran, dass die Quelle ihre Spannung selbst nur exponentiell erhöht; ein idealer Sprung würde den Kondensator geradlinig bis zum Endwert laden.
--- falsch
Daran, dass der Kondensator Ladung nur in festen Portionen aufnimmt; jede Portion halbiert den freien Platz für die nächste, bis er voll ist.
:::
:::karte herleitung Sprungantwort aus der Maschenregel
Wie folgt aus der Maschenregel $1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau$ für den anfangs leeren Kondensator die Sprungantwort $u_2(t)=1-\mathrm{e}^{-t/RC}$?
---
Ableiten gibt $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, weil die angelegte Spannung von 1 V für $t\ge0$ konstant ist.
---
Umgestellt ist $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, und Integrieren gibt $\ln|i|=-\frac{t}{RC}+K$, weil links nur noch $i$ und rechts nur noch $t$ steht.
---
Also ist $i(t)=A\,\mathrm{e}^{-t/RC}$ mit $A=i(0)=\frac1R$, weil im ersten Moment die ganze Spannung an $R$ liegt.
---
Mit der Maschenregel $u_2=1-R\,i$ folgt $u_2(t)=1-\mathrm{e}^{-t/RC}$, weil am Kondensator der Rest der angelegten Spannung liegt.
:::
::::
