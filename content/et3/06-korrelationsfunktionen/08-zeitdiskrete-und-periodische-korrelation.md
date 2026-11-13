---
title: Stufe 7: Zeitdiskrete und periodische Korrelation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260800
summary: Für Abtastwerte wird aus dem Integral eine Summe.
tags: schnelle Korrelation
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Für Abtastwerte wird aus dem Integral eine Summe. Mit der DFT rechnet man Korrelationen schnell.
:::

:::satz Satz 7.1 (Zeitdiskrete Korrelation)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{Periode }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

Für abgetastete Tiefpasssignale gilt $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ und $E_s=T\sum_n|s(nT)|^2$. Ein zeitdiskretes Energiesignal ist eine quadratisch summierbare Folge.

::::beispiel
$s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ für $m=-2,\dots,2$. Maximum $6=E_s$ bei $m=0$, gerade, fünf Werte statt drei. Probe mit Wiener-Khintchine bei $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.
::::

**Periodische Korrelation.** Wie bei der Faltung ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) gilt für Folgen der Periode $M$

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Mit der FFT berechnet heißt das __schnelle Korrelation__. Damit die periodische Korrelation die gewöhnliche wiedergibt, muss $M$ groß genug sein. Für $(1,2,1)$ ergibt $M=3$ die überlappte Folge $(6,5,5)$, $M=5$ dagegen $(6,4,1,1,4)$, die gewöhnliche AKF zyklisch angeordnet.

**Leistungssignale.** Für Signale unendlicher Energie mittelt man:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

Sind beide Signale mit derselben Periode periodisch, genügt eine Periode, und die Korrelationsfunktion ist ebenfalls periodisch. Beispiel: $A\cos(2\pi Ft+\varphi_0)$ hat die AKF $\frac{A^2}{2}\cos(2\pi F\tau)$. Die Phase $\varphi_0$ ist verschwunden, bei $\tau=0$ steht die Leistung $\frac{A^2}{2}$.

:::aufgabe Aufgabe 6 ★ Diskrete AKF
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Rechne die AKF von $(1,2,1)$ von Hand nach.

</li>

<li>

Bestimme die AKF von $(1,-1)$. Was sagt $\varphi(\pm1)<0$ über das Signal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. Ein negativer Wert bei der Verschiebung 1 heißt: Benachbarte Werte haben eher entgegengesetztes Vorzeichen, das Signal wechselt schnell. Passend dazu ist $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ bei $f=0$ null und bei $f=\frac12$ maximal: ein Hochpasssignal.
:::
:::

:::aufgabe Aufgabe 7 ★★ AKF eines Kosinus
<span class="anker" id="aufg-7"></span>

Leite die AKF von $A\cos(2\pi Ft+\varphi_0)$ mit [(7.4)](#gl-7-4) über eine Periode her. Warum fällt $\varphi_0$ heraus, und was bedeutet das für die Messung der Phase mit der AKF?

:::loesung
Mit $\omega=2\pi F$ und $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

Das zweite Integral läuft über zwei volle Perioden und ist null. $\varphi_0$ verschiebt nur den Zeitnullpunkt, und die Mittelung über alle Zeiten kennt keinen Nullpunkt. Mit der AKF eines einzelnen Signals kann man deshalb keine Phase messen. Die Phasendifferenz *zweier* Signale zeigt dagegen die Kreuzkorrelation.
:::
:::

::::formelsammlung
**Zeitdiskrete Korrelation**

$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m)$$

Summe statt Integral, ganzzahlige Verschiebung $m$. Ein zeitdiskretes Energiesignal ist eine quadratisch summierbare Folge.

**Energie einer Folge**

$$E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f$$

Parseval für Folgen: Integral über eine Periode des Spektrums.

**Wiener-Khintchine und Wiener-Lee für Folgen**

$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{Periode }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m)$$

Dieselben Sätze wie im Zeitkontinuierlichen, mit Faltungssummen.

**Abgetastete Tiefpasssignale**

$$\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T),\qquad E_s=T\sum_n|s(nT)|^2$$

Korrelation und Energie aus den Abtastwerten mit dem Abtastabstand $T$.

**Periodische Korrelation**

$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k)$$

Für Folgen der Periode $M$. Mit der FFT berechnet: schnelle Korrelation. Sie gibt die gewöhnliche Korrelation nur wieder, wenn $M$ groß genug ist; sonst überlappen sich die Werte.

**Korrelation von Leistungssignalen**

$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t$$

Für Signale unendlicher Energie. Sind beide Signale mit derselben Periode periodisch, genügt eine Periode, und die Korrelationsfunktion ist ebenfalls periodisch.

**AKF eines Kosinus**

$$\varphi^L_{ss}(\tau)=\frac{A^2}{2}\cos(2\pi F\tau)$$

Für $A\cos(2\pi Ft+\varphi_0)$. Die Phase $\varphi_0$ fällt heraus, bei $\tau=0$ steht die Leistung $\frac{A^2}{2}$. Die AKF eines einzelnen Signals misst keine Phase.
::::

::::lernkarten
:::karte formel Zeitdiskrete Korrelation
Wie lautet die Korrelationsfunktion zweier zeitdiskreter Energiesignale, und wie schreibt man sie als Faltung?
---
$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m)$: Aus dem Integral wird eine Summe über die Abtastwerte, und die Verschiebung $m$ ist ganzzahlig.
--- falsch
$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(m-n)=s^*(m)*g(m)$: Die zeitdiskrete Korrelation ist die gewöhnliche Faltungssumme der beiden Folgen ohne Spiegeln.
--- falsch
$\varphi^E_{sg}(m)=\int_{-\infty}^{\infty}s^*(t)\,g(t+mT)\,\mathrm{d} t$: Auch bei Folgen bleibt die Korrelation ein Integral, nur die Verschiebung wird auf Vielfache von $T$ beschränkt.
--- falsch
$\varphi^E_{sg}(m)=\sum_{n=0}^{M-1}s^*(n)\,g(n+m)$: Man summiert immer nur über die Länge $M$ der Folgen, weil zeitdiskrete Korrelationen grundsätzlich periodisch sind.
:::
:::karte formel Energie einer Folge
Wie berechnet man die Energie eines zeitdiskreten Signals im Zeit- und im Frequenzbereich?
---
$E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f$: als Summe der Betragsquadrate oder als Integral des Energiedichtespektrums über eine Periode.
--- falsch
$E_s=\sum_n|s(n)|^2=\int_{-\infty}^{\infty}|S_\mathrm a(f)|^2\,\mathrm{d} f$: Man integriert wie bei zeitkontinuierlichen Signalen über alle Frequenzen, sonst fehlt ein Teil der Energie.
--- falsch
$E_s=\sum_n s(n)=S_\mathrm a(0)$: Die Energie ist die Summe der Abtastwerte und damit der Wert des Spektrums bei $f=0$, an dem sich alle Werte addieren.
--- falsch
$E_s=\sum_n|s(n)|^2=|S_\mathrm a(0)|^2$: Die Energie ist das Energiedichtespektrum bei $f=0$, weil dort alle Abtastwerte gleichphasig addiert werden und keiner verloren geht.
:::
:::karte formel Wiener-Khintchine und Wiener-Lee für Folgen
Welches Spektrum gehört zur AKF einer Folge, und wie ändert ein zeitdiskretes LTI-System diese AKF?
---
$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2$ mit der Periode 1, und am Ausgang gilt $\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m)$: dieselben Sätze wie bei zeitkontinuierlichen Signalen, nur mit Summen.
--- falsch
$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2$ ohne Periode, und am Ausgang gilt $\varphi^E_{gg}(m)=\varphi^E_{ss}(m)\,\varphi^E_{hh}(m)$: Bei Folgen werden die AKFs multipliziert statt gefaltet.
--- falsch
$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)$ mit der Periode 1, und am Ausgang gilt $\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*h(m)$: Die AKF wird wie die Folge selbst gefiltert.
--- falsch
$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2$ mit der Periode 1; der Satz von Wiener-Lee gilt für Folgen aber nicht, weil die Faltungssumme kein Assoziativgesetz kennt und sich die Faktoren nicht umsortieren lassen.
:::
:::karte formel Abgetastete Tiefpasssignale
Wie erhält man Korrelationsfunktion und Energie eines abgetasteten Tiefpasssignals aus seinen Abtastwerten?
---
$\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ und $E_s=T\sum_n|s(nT)|^2$: Die Summen über die Abtastwerte werden mit dem Abtastabstand $T$ multipliziert.
--- falsch
$\varphi^E_{sg}(mT)=\sum_ns^*(nT)g((n+m)T)$ und $E_s=\sum_n|s(nT)|^2$: Der Abtastabstand fällt heraus, weil man nur Abtastwerte miteinander multipliziert.
--- falsch
$\varphi^E_{sg}(mT)=\frac1T\sum_ns^*(nT)g((n+m)T)$ und $E_s=\frac1T\sum_n|s(nT)|^2$: Man teilt durch $T$, weil die Abtastwerte mit der Rate $1/T$ eintreffen.
--- falsch
$\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ und $E_s=T^2\sum_n|s(nT)|^2$: Bei der Energie geht $T$ quadratisch ein, weil das Signal quadriert wird.
:::
:::karte zusammenhang AKF einer Folge
Woran erkennt man an der AKF der Folge $s=(1,2,1)$ die allgemeinen Eigenschaften einer AKF?
---
Die AKF ist $\varphi^E_{ss}=(1,4,6,4,1)$ für $m=-2,\dots,2$: Das Maximum $6=E_s$ liegt bei $m=0$, sie ist gerade, und sie hat fünf Werte statt drei, ist also fast doppelt so lang.
--- falsch
Die AKF ist $(1,4,6)$ für $m=0,1,2$: Eine Folge mit drei Werten hat eine AKF mit drei Werten, und das Maximum $6=E_s$ liegt am Ende bei $m=2$.
--- falsch
Die AKF ist $(1,4,6,4,1)$ für $m=-2,\dots,2$: Ihr Maximum 6 ist das Quadrat der Summe der Werte, $(1+2+1)^2$, und liegt bei $m=0$, weil die Folge dort ihren größten Wert hat.
--- falsch
Die AKF ist $(1,2,1)*(1,2,1)=(1,4,6,4,1)$: Jede AKF ist die Faltung der Folge mit sich selbst ohne Spiegeln, auch bei Folgen, die nicht symmetrisch sind.
:::
:::karte zusammenhang Probe mit Wiener-Khintchine
Warum ergibt die Summe aller Werte der AKF $(1,4,6,4,1)$ der Folge $(1,2,1)$ den Wert 16?
---
Nach Wiener-Khintchine gehört $\varphi^E_{ss}(m)$ zu $|S_\mathrm a(f)|^2$, und bei $f=0$ ist das Spektrum die Summe der Folge: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.
--- falsch
Weil jeder Wert der AKF ein Teil der Energie ist: Die Energie der Folge ist nach Parseval 16, und die Werte der AKF teilen diese Energie unter den Verschiebungen auf.
--- falsch
Weil die Summe der AKF zum Energiedichtespektrum bei $f=\frac12$ gehört: $|S_\mathrm a(\tfrac12)|^2=16$, denn bei der halben Abtastfrequenz addieren sich alle Werte gleichphasig.
--- falsch
Weil die AKF bei $m=0$ den Wert $|S_\mathrm a(0)|^2$ hat und die Summe aller ihrer Werte nach dem Flächensatz gleich diesem Wert bei $m=0$ ist.
:::
:::karte formel Periodische Korrelation
Wie lautet die periodische Korrelation zweier Folgen der Periode $M$, und welches DFT-Spektrum gehört zu ihr?
---
$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k)$: Man summiert über eine Periode, und im DFT-Bereich wird daraus das Produkt des konjugierten mit dem zweiten Spektrum.
--- falsch
$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d(k)\,G_d(k)$: Im DFT-Bereich ist die periodische Korrelation das Produkt der Spektren, wie die periodische Faltung.
--- falsch
$\varphi^E_{sgd}(m)=\sum_{n=-\infty}^{\infty}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k)$: Man summiert über alle $n$, damit keine Periode der Folgen fehlt und das Ergebnis der gewöhnlichen Korrelation gleicht.
--- falsch
$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;|S_d(k)|^2+|G_d(k)|^2$: Im DFT-Bereich addieren sich die Energiedichtespektren der beiden Folgen Wert für Wert.
:::
:::karte begriff schnelle Korrelation
Was versteht man unter schneller Korrelation, und worauf beruht sie?
---
Die Berechnung der periodischen Korrelation mit der FFT über das Produkt $S_d^*(k)\,G_d(k)$. Damit sie die gewöhnliche Korrelation liefert, muss die Periode $M$ groß genug sein.
--- falsch
Die Korrelation von Folgen, die schneller als mit der doppelten Grenzfrequenz abgetastet wurden: Man spart Rechenzeit, weil die AKF dann weniger Werte hat als die Folge selbst.
--- falsch
Die Korrelation bei nur einer einzigen Verschiebung $m=0$: Man berechnet statt der ganzen Funktion nur ihr Maximum, die Energie, und spart so alle übrigen Summen.
--- falsch
Die direkte Berechnung der Summe $\sum s^*(n)\,g(n+m)$ nur über die von null verschiedenen Werte; die FFT braucht man dafür nicht, weil die Summe ohnehin kurz ist.
:::
:::karte zusammenhang Periode groß genug
Was passiert, wenn man die AKF von $(1,2,1)$ periodisch mit der Periode $M=3$ statt mit $M=5$ berechnet?
---
Mit $M=3$ überlappen sich die fünf Werte der gewöhnlichen AKF, und man erhält $(6,5,5)$. Mit $M=5$ ist Platz für alle fünf Werte: $(6,4,1,1,4)$ ist die gewöhnliche AKF $(1,4,6,4,1)$, zyklisch angeordnet.
--- falsch
Mit $M=3$ erhält man $(6,4,1)$, die rechte Hälfte der AKF; mit $M=5$ erhält man dieselben Werte und zwei Nullen. Die Periode ändert die Werte nicht, nur ihre Zahl.
--- falsch
Mit $M=3$ erhält man die gewöhnliche AKF, weil die Folge drei Werte hat; mit $M=5$ kommen zwei Nullen hinzu, die die Werte zu $(6,5,5,0,0)$ verfälschen.
--- falsch
Beide Perioden liefern $(6,5,5)$, bei $M=5$ ergänzt um zwei Nullen: Bei der periodischen Korrelation überlappen sich die Randwerte immer, gleich wie groß man die Periode $M$ wählt.
:::
:::karte formel Korrelation von Leistungssignalen
Wie definiert man die Korrelationsfunktion für Leistungssignale, deren Energie unendlich ist?
---
Durch Mittelung: $\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t$. Sind beide Signale mit derselben Periode periodisch, genügt eine Periode, und die Korrelationsfunktion ist ebenfalls periodisch.
--- falsch
Wie bei Energiesignalen: $\varphi^L_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t$. Das Integral bleibt endlich, weil sich bei Dauersignalen positive und negative Anteile des Produkts über die Zeit gegenseitig aufheben.
--- falsch
Durch Mittelung: $\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t$. Auch bei periodischen Signalen muss man über alle Zeiten mitteln, und die Funktion ist dann nicht periodisch.
--- falsch
Durch Mittelung ohne Verschiebung: $\varphi^L_{sg}=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t)\,\mathrm{d} t$. Eine Verschiebung $\tau$ ist bei Leistungssignalen nicht nötig, weil sie unendlich lange andauern.
:::
:::karte zusammenhang AKF eines Kosinus
Warum hängt die AKF $\frac{A^2}{2}\cos(2\pi F\tau)$ des Kosinus $A\cos(2\pi Ft+\varphi_0)$ nicht von der Phase $\varphi_0$ ab, und was folgt daraus für Messungen?
---
$\varphi_0$ verschiebt nur den Zeitnullpunkt, und die Mittelung über alle Zeiten kennt keinen Nullpunkt. Mit der AKF eines einzelnen Signals misst man deshalb keine Phase; die Phasendifferenz zweier Signale zeigt die KKF.
--- falsch
Weil $\varphi_0$ nur bei $\tau=0$ herausfällt und man die AKF meist dort auswertet. Für $\tau\neq0$ enthält sie die Phase, und man kann sie an jeder anderen Verschiebung als Versatz des Kosinus ablesen.
--- falsch
Weil der Kosinus eine gerade Funktion ist und die Phase deshalb keine Wirkung auf die Mittelung hat. Bei einem Sinus mit der Phase $\varphi_0$ enthielte die AKF dagegen die Phase als Verschiebung.
--- falsch
Weil sich $\varphi_0$ und $-\varphi_0$ in der Rechnung gegenseitig aufheben. Auch die Kreuzkorrelation zweier Signale enthält deshalb keine Phasendifferenz; Phasen sind mit Korrelationen grundsätzlich nicht messbar.
:::
:::karte zusammenhang Negative Werte der AKF
Was sagt ein negativer Wert $\varphi(\pm1)<0$ der AKF einer Folge über das Signal aus, etwa bei der Folge $(1,-1)$?
---
Benachbarte Werte haben eher entgegengesetztes Vorzeichen, das Signal wechselt schnell. Für $(1,-1)$ ist $\varphi(\pm1)=-1$, und $|S_\mathrm a(f)|^2=2-2\cos(2\pi f)$ ist bei $f=0$ null und bei $f=\frac12$ maximal: ein Hochpasssignal.
--- falsch
Benachbarte Werte haben eher gleiches Vorzeichen, das Signal ändert sich langsam. Für $(1,-1)$ ist $|S_\mathrm a(f)|^2$ bei $f=0$ maximal und bei $f=\frac12$ null: ein Tiefpasssignal.
--- falsch
Das Signal hat bei der Verschiebung 1 eine negative Energie. Für $(1,-1)$ ist $\varphi(0)=0$, weil sich die beiden Werte aufheben, und das Signal trägt insgesamt keine Energie.
--- falsch
Ein negativer Wert zeigt, dass die Folge nicht reell ist: Bei reellen Folgen ist die AKF überall positiv, weil sie zum nie negativen Energiedichtespektrum gehört und dieses keine negativen Anteile liefern kann.
:::
::::
