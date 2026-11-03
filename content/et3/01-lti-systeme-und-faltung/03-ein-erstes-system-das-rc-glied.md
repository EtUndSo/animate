---
title: Stufe 2: Ein erstes System, das RC-Glied
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
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

⁠**So liest man das:** $|H|$ sagt, um welchen Faktor die Amplitude schrumpft, $\varphi$, um welchen Winkel die Schwingung nacheilt. Bei $x=1$, also $F=1/(2\pi RC)=0{,}16$ Hz im Rechenmodell, ist $|H|=0{,}707$ und $\varphi=-45^\circ$. Bei $x=10$ ist $|H|=0{,}0995$ und $\varphi=-84{,}3^\circ$ (Abb. [3](#abb-3)). **Grenzfälle:** $F\to0$ ergibt $H\to1$ (der Kondensator hat Zeit, sich voll aufzuladen), $F\to\infty$ ergibt $H\to0$ mit $\varphi\to-90^\circ$ (der Kondensator wirkt wie ein Kurzschluss).

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
