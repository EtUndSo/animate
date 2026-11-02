---
title: Stufe 7: Die Zahl $\pi$ und die Wertetabelle
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270900
summary: In den Reihen kommt pi nicht vor.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
In den Reihen kommt $\pi$ nicht vor. Diese Stufe definiert $\pi$ aus der Cosinusreihe und zeigt, warum Sinus und Cosinus periodisch sind.
:::

**Die Idee.** $\mathrm{e}^{\mathrm{i}x}$ läuft mit wachsendem $x$ von 1 aus über den Einheitskreis. Der Cosinus ist bei $x=0$ noch 1, bei $x=2$ schon negativ. Dazwischen wird er null: Dort ist der Punkt bei $\mathrm{i}$ angekommen, nach einer Vierteldrehung. Dieses $x$ nennt man $\pi/2$. Der Rest folgt aus der Funktionalgleichung: Vier Vierteldrehungen führen zurück zur 1.

:::satz Satz 7.1 (Cosinus und Sinus auf dem Intervall von 0 bis 2)
<span class="anker" id="satz-7-1"></span>

<ol class="al">

<li>

Der Cosinus ist auf $[0,2]$ streng monoton fallend und hat dort genau eine Nullstelle $\chi\in(0,2)$.

</li>

<li>

Es gilt $\sin\varphi>0$ für alle $\varphi\in(0,2]$.

</li>

</ol>
:::

:::beweis Reihen abschätzen
(b): Man fasst je zwei Glieder der Sinusreihe zusammen: $\frac{\varphi^{4k+1}}{(4k+1)!}\bigl(1-\frac{\varphi^2}{(4k+2)(4k+3)}\bigr)$. Für $0<\varphi\le2$ ist die Klammer mindestens $1-\frac46>0$.

(a): Für $0\le x<y\le2$ sei $s:=\frac{x+y}2$ und $t:=\frac{y-x}2$. Die Additionstheoreme für $\cos(s-t)$ und $\cos(s+t)$ geben $\cos x-\cos y=2\sin s\sin t>0$ nach (b). Es ist $\cos0=1$, und bei $x=2$ fallen die Beträge der Glieder $1;\ 2;\ 0{,}667;\ 0{,}089;\dots$ ab dem zweiten, also ist $\cos2\le1-2+\frac23<0$. Der Zwischenwertsatz gibt eine Nullstelle, die Monotonie ihre Eindeutigkeit.
:::

:::definition Definition 7.2 (Kreiszahl)
<span class="anker" id="satz-7-2"></span>

$\pi:=2\chi$, wobei $\chi$ die Nullstelle aus dem Satz ist. Es ist $\pi=3{,}14159\dots$
:::

⁠**So liest man das:** Dass $\varphi$ die Bogenlänge auf dem Einheitskreis ist und $\pi$ der halbe Umfang, zeigt die Integralrechnung. **Zahlen:** Die Reihe gibt $\cos1{,}5=0{,}0707$ und $\cos1{,}6=-0{,}0292$, also liegt $\chi$ dazwischen. Vierzehnmal Intervallhalbieren gibt $2\chi\approx3{,}1416$.

:::satz Satz 7.3 (Wertetabelle und Periodizität)
<span class="anker" id="satz-7-3"></span>

Für alle $\varphi\in\mathbb{R}$ gilt $\mathrm{e}^{\mathrm{i}(\varphi+2\pi)}=\mathrm{e}^{\mathrm{i}\varphi}$, $\sin(\varphi+2\pi)=\sin\varphi$ und $\cos(\varphi+2\pi)=\cos\varphi$. Die Werte auf dem ersten Umlauf sind:

| $\varphi$ | $0$ | $\frac\pi4$ | $\frac\pi2$ | $\pi$ | $\frac32\pi$ | $2\pi$ |
|---|---|---|---|---|---|---|
| $\mathrm{e}^{\mathrm{i}\varphi}$ | $1$ | $\frac1{\sqrt2}(1+\mathrm{i})$ | $\mathrm{i}$ | $-1$ | $-\mathrm{i}$ | $1$ |
| $\sin\varphi$ | $0$ | $\frac1{\sqrt2}$ | $1$ | $0$ | $-1$ | $0$ |
| $\cos\varphi$ | $1$ | $\frac1{\sqrt2}$ | $0$ | $-1$ | $0$ | $1$ |
:::

⁠**So liest man das:** Ein Umlauf ist $2\pi$, danach wiederholt sich alles (Abb. [7](#abb-7)). $\mathrm{e}^{\mathrm{i}\pi}=-1$ heißt: Eine halbe Drehung ist die Multiplikation mit $-1$.

:::abbildung hm1/k7pi 7
Cosinus und Sinus mit den Punkten der Wertetabelle. Im Bereich $[0,2]$ fällt der Cosinus und der Sinus ist positiv. Die Nullstelle $\chi$ des Cosinus definiert $\pi$.
:::

:::beweis Vierteldrehungen zusammensetzen
Spalte 0: Stufe [3](sinus-und-cosinus-als-reihen.html#stufe-3). Spalte $\pi/2$: Es ist $\cos\frac\pi2=0$, also $\sin^2\frac\pi2=1$ nach [(6.2)](die-eulersche-formel.html#gl-6-2). Wegen $\sin\frac\pi2>0$ ist $\sin\frac\pi2=1$ und $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$. Spalten $\pi$, $\frac32\pi$, $2\pi$: Die Funktionalgleichung gibt $\mathrm{e}^{\mathrm{i}\pi}=\mathrm{i}^2=-1$, $\mathrm{e}^{3\mathrm{i}\pi/2}=\mathrm{i}^3=-\mathrm{i}$ und $\mathrm{e}^{2\pi\mathrm{i}}=\mathrm{i}^4=1$. Sinus und Cosinus liest man mit [(6.1)](die-eulersche-formel.html#gl-6-1) ab.

Spalte $\pi/4$: $w:=\mathrm{e}^{\mathrm{i}\pi/4}$ erfüllt $w^2=\mathrm{i}$. Nach [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) hat $w^2=\mathrm{i}$ genau die Lösungen $\pm\frac1{\sqrt2}(1+\mathrm{i})$. Wegen $\sin\frac\pi4>0$ gilt das Pluszeichen.

Periodizität: $\mathrm{e}^{\mathrm{i}(\varphi+2\pi)}=\mathrm{e}^{\mathrm{i}\varphi}\mathrm{e}^{2\pi\mathrm{i}}=\mathrm{e}^{\mathrm{i}\varphi}$. Real- und Imaginärteil ergeben die beiden anderen Formeln.
:::

:::frage Warum definiert man $\pi$ nicht als Umfang durch Durchmesser?
Dazu müsste die Länge einer krummen Linie erklärt sein, und das braucht Integrale. Die Nullstelle des Cosinus kommt ohne sie aus und ergibt dieselbe Zahl.
:::

:::aufgabe Aufgabe 7 ★★ Tabelle und Drehung
<span class="anker" id="aufg-7"></span>

(a) Bestimme $\mathrm{e}^{3\mathrm{i}\pi/4}$, $\mathrm{e}^{7\mathrm{i}\pi/4}$ und $\cos\frac{11\pi}4$ aus der Tabelle. (b) Zeige mit $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$: $\cos(\varphi+\frac\pi2)=-\sin\varphi$ und $\sin(\varphi+\frac\pi2)=\cos\varphi$. Was bedeutet das in der Ebene? (c) Berechne $\cos1{,}57$ und $\cos1{,}58$ aus den Gliedern bis $x^8$. Welche Schranken für $\pi$ folgen?

:::loesung
(a) $\mathrm{e}^{3\mathrm{i}\pi/4}=\mathrm{e}^{\mathrm{i}\pi/2}\mathrm{e}^{\mathrm{i}\pi/4}=\frac{\mathrm{i}(1+\mathrm{i})}{\sqrt2}=\frac{-1+\mathrm{i}}{\sqrt2}$. $\mathrm{e}^{7\mathrm{i}\pi/4}=\mathrm{e}^{2\pi\mathrm{i}}\mathrm{e}^{-\mathrm{i}\pi/4}=\overline{\mathrm{e}^{\mathrm{i}\pi/4}}=\frac{1-\mathrm{i}}{\sqrt2}$. $\cos\frac{11\pi}4=\cos\frac{3\pi}4=-\frac1{\sqrt2}$ nach der Periodizität. (b) $\cos(\varphi+\frac\pi2)+\mathrm{i}\sin(\varphi+\frac\pi2)=\mathrm{i}\,\mathrm{e}^{\mathrm{i}\varphi}=-\sin\varphi+\mathrm{i}\cos\varphi$. Real- und Imaginärteil vergleichen. In der Ebene: Aus $(x,y)$ wird $(-y,x)$, die Vierteldrehung aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). (c) Bis $x^8$ ist $\cos1{,}57\approx0{,}00082$ und $\cos1{,}58\approx-0{,}00918$, der Fehler ist höchstens rund $3\cdot10^{-5}$. Also ist $1{,}57<\chi<1{,}58$ und $3{,}14<\pi<3{,}16$.
:::
:::
