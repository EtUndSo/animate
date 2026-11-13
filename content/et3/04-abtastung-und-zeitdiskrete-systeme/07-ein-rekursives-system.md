---
title: Stufe 6: Ein rekursives System
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240700
summary: Am einfachsten IIR-System sieht man, wie Rückkopplung eine unendlich lange Impulsantwort erzeugt und wann das System stabil ist.
tags: kausal, stabil
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Am einfachsten IIR-System sieht man, wie Rückkopplung eine unendlich lange Impulsantwort erzeugt und wann das System stabil ist.
:::

Das System $g(n)=s(n)+b\,g(n-1)$ addiert zum Eingang den mit $b$ gewichteten letzten Ausgang. Für $s=\delta$ und Ruhe vor $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

Der Stoß läuft in der Rückkopplung immer wieder herum und wird jedes Mal mit $b$ multipliziert. Das System ist __kausal__ ($h(n)=0$ für $n<0$). Es ist __stabil__, wenn $\sum_n|h(n)|<\infty$ (das diskrete Gegenstück zu [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), hier also genau für $|b|<1$, mit $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Antwort auf eine Rechteckfolge.** Eingang $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ Einsen). Mit der Faltungssumme und der geometrischen Summenformel $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

Im Rechenmodell ($b=0{,}6$, $M=4$): $g=1;\ 1{,}6;\ 1{,}96;\ 2{,}176$, danach $1{,}306;\ 0{,}783;\ 0{,}470;\dots$, jeder Wert das 0,6-Fache des vorigen (Abb. [5](#abb-5)). Das ist das diskrete Gegenstück zur Rechteckantwort des RC-Glieds in [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek 5
Das rekursive System mit $b=0{,}6$. Links die Impulsantwort. Rechts die Antwort auf vier Einsen: Sie steigt bis 2,176 an und klingt danach mit dem Faktor 0,6 je Takt ab.
:::

:::aufgabe Aufgabe 5 ★★ Das rekursive System untersuchen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Bestätige die ersten fünf Werte von $g(n)$ im Rechenmodell direkt mit der Rekursion.

</li>

<li>

Gegen welchen Wert strebt der Ausgang bei einer unendlich langen Folge von Einsen ($M\to\infty$)? Vergleiche mit $\sum_nh(n)$.

</li>

<li>

Wie sieht $h(n)$ für $b=-0{,}6$ und für $b=1{,}1$ aus? Welches System ist stabil?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0{,}6=1{,}6$, $g(2)=1+0{,}96=1{,}96$, $g(3)=1+1{,}176=2{,}176$, $g(4)=0+0{,}6\cdot2{,}176=1{,}306$.

(b) $\frac{1}{1-b}=2{,}5$. Das ist $\sum_nh(n)=\sum0{,}6^n=2{,}5$: Bei konstantem Eingang 1 summiert die Faltung alle Werte der Impulsantwort. Es ist auch $H_\mathrm a(0)=2{,}5$.

(c) $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, wechselndes Vorzeichen, abklingend, stabil. $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, wachsend, instabil.
:::
:::

:::aufgabe Aufgabe 6 ★★ System erster Ordnung
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0{,}5\,s(n-1)+0{,}6\,g(n-1)$ (Abb. [4](zeitdiskrete-signale-und-die-diskrete-faltung.html#abb-4) mit $a_0=1$, $a_1=0{,}5$, $b_1=0{,}6$).

<ol class="al">

<li>

Berechne $h(0)$ bis $h(3)$ mit der Rekursion.

</li>

<li>

Zeige, dass $h(n)=\frac{11}{6}\,0{,}6^n\varepsilon(n)-\frac56\delta(n)$ ist.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0{,}5+0{,}6\cdot1=1{,}1$, $h(2)=0{,}6\cdot1{,}1=0{,}66$, $h(3)=0{,}396$.

(b) Die Formel gibt $h(0)=\frac{11}{6}-\frac56=1$ und $h(1)=\frac{11}{6}\cdot0{,}6=1{,}1$. Ab $n=2$ ist der Eingang null, die Rekursion lautet $h(n)=0{,}6\,h(n-1)$, und die Formel erfüllt sie, weil $\frac{11}{6}0{,}6^n=0{,}6\cdot\frac{11}{6}0{,}6^{n-1}$. (Mit der z-Transformation folgt die Formel aus der Zerlegung $H(z)=-\frac56+\frac{11/6}{1-0{,}6z^{-1}}$.)
:::
:::

::::formelsammlung
**Impulsantwort des rekursiven Systems**

$$h(n)=\varepsilon(n)\,b^n$$

System $g(n)=s(n)+b\,g(n-1)$ in Ruhe vor $n=0$; aus der Rekursion $h(n)=\delta(n)+b\,h(n-1)$. Kausal, weil $h(n)=0$ für $n<0$.

**Stabilität**

$$\sum_n|h(n)|<\infty$$

Diskretes Gegenstück zum Stabilitätskriterium kontinuierlicher Systeme. Für das rekursive System genau bei $|b|<1$, mit $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Geometrische Summenformel**

$$\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$$

Für $q\neq1$.

**Antwort auf eine Rechteckfolge**

$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases}$$

Eingang $s(n)=\varepsilon(n)-\varepsilon(n-M)$ aus $M$ Einsen. Nach dem Rechteck klingt der Ausgang mit dem Faktor $b$ je Takt ab.
::::

::::lernkarten
:::karte formel Impulsantwort des rekursiven Systems
Welche Impulsantwort hat das rekursive System $g(n)=s(n)+b\,g(n-1)$, wenn es vor $n=0$ in Ruhe ist?
---
$h(n)=\varepsilon(n)\,b^n$, also $h(0)=1$, $h(1)=b$, $h(2)=b^2$ und so weiter. Der Stoß läuft in der Rückkopplung immer wieder herum und wird jedes Mal mit $b$ multipliziert.
--- falsch
$h(n)=\varepsilon(n)\,b\,n$, also $h(0)=0$, $h(1)=b$, $h(2)=2b$ und so weiter. Bei jedem Umlauf in der Rückkopplung wird der Faktor $b$ einmal mehr zum Ausgang addiert.
--- falsch
$h(n)=\delta(n)+b\,\delta(n-1)$, also nur $h(0)=1$ und $h(1)=b$. Der Stoß läuft genau einmal durch die Rückkopplung und ist danach vollständig verbraucht.
--- falsch
$h(n)=\varepsilon(n)\,b^{-n}$, also $h(0)=1$, $h(1)=1/b$, $h(2)=1/b^2$ und so weiter. Bei jedem Umlauf wird der Stoß durch $b$ geteilt, weil der Ausgang zurückgeführt wird.
:::
:::karte herleitung Impulsantwort durch Rekursion
Wie gewinnt man aus $g(n)=s(n)+b\,g(n-1)$ die Impulsantwort $h(n)=\varepsilon(n)\,b^n$?
---
Man setzt $s=\delta$ ein und erhält $h(n)=\delta(n)+b\,h(n-1)$, weil die Impulsantwort die Antwort auf den Einheitsimpuls ist.
---
Für $n<0$ ist $h(n)=0$, weil das System vor $n=0$ in Ruhe ist und noch kein Impuls angekommen ist.
---
Bei $n=0$ ist $h(0)=1$, weil dort der Einheitsimpuls den Wert 1 hat und der vorige Ausgang noch null ist.
---
Für $n\ge1$ ist der Eingang null, und jeder Wert ist das $b$-Fache des vorigen, weil nur noch die Rückkopplung wirkt. So folgt $h(1)=b$, $h(2)=b^2$ und allgemein $h(n)=\varepsilon(n)\,b^n$.
:::
:::karte zusammenhang kausal
Woran erkennt man, dass das rekursive System $g(n)=s(n)+b\,g(n-1)$ kausal ist?
---
Seine Impulsantwort $h(n)=\varepsilon(n)\,b^n$ ist null für $n<0$: Der Ausgang beginnt nicht vor dem Impuls. Das System verwendet nur den aktuellen Eingang und vergangene Ausgänge, keine künftigen Werte.
--- falsch
Daran, dass seine Impulsantwort für $|b|<1$ abklingt. Ein System, dessen Antwort mit der Zeit verschwindet, reagiert nur auf die Ursache und nicht auf spätere Ereignisse und ist deshalb kausal.
--- falsch
Daran, dass es eine Rückkopplung hat. Erst die Rückkopplung verknüpft den Ausgang mit einer Ursache; Systeme ohne Rückkopplung sind deshalb nie kausal.
--- falsch
Daran, dass seine Impulsantwort für alle $n$ von null verschieden ist. Ein kausales System reagiert zu jeder Zeit auf den Impuls, auch schon vor seinem Eintreffen.
:::
:::karte zusammenhang stabil
Für welche Werte von $b$ ist das rekursive System $g(n)=s(n)+b\,g(n-1)$ stabil, und warum?
---
Genau für $|b|<1$. Stabil heißt $\sum_n|h(n)|<\infty$, und mit $h(n)=\varepsilon(n)\,b^n$ ist das die geometrische Reihe $\sum_n|b|^n$, die nur für $|b|<1$ endlich ist, nämlich $\frac{1}{1-|b|}$.
--- falsch
Für jedes $b$, weil die Rückkopplung den Ausgang immer nur um den vorigen Wert erhöht. Ein System, das nur einen Takt zurückblickt, kann nicht über alle Grenzen wachsen.
--- falsch
Genau für $b<1$, auch für negative Werte wie $b=-2$. Stabil heißt, dass die Impulsantwort nicht über alle Grenzen wächst, und bei negativem $b$ wird sie in jedem Takt kleiner.
--- falsch
Genau für $|b|\le1$. Stabil heißt $\sum_n|h(n)|<\infty$, und die geometrische Reihe $\sum_n|b|^n$ ist auch für $|b|=1$ endlich, weil dann jeder Summand gleich 1 ist.
:::
:::karte formel Antwort auf eine Rechteckfolge
Welche Antwort liefert das rekursive System $g(n)=s(n)+b\,g(n-1)$ auf die Rechteckfolge $s(n)=\varepsilon(n)-\varepsilon(n-M)$ aus $M$ Einsen?
---
Für $0\le n<M$ ist $g(n)=\frac{1-b^{n+1}}{1-b}$, die Antwort steigt an; für $n\ge M$ ist $g(n)=\frac{b^{n-M+1}-b^{n+1}}{1-b}$, sie klingt mit dem Faktor $b$ je Takt ab. Vor $n=0$ ist $g(n)=0$.
--- falsch
Für $0\le n<M$ ist $g(n)=n+1$, die Antwort steigt linear an; für $n\ge M$ ist $g(n)=0$, sie bricht sofort ab, weil kein Eingang mehr kommt. Vor $n=0$ ist $g(n)=0$.
--- falsch
Für $0\le n<M$ ist $g(n)=b^n$, die Antwort klingt schon während des Rechtecks ab; für $n\ge M$ ist $g(n)=0$, weil die Rückkopplung ohne Eingang nichts mehr liefert. Vor $n=0$ ist $g(n)=0$.
--- falsch
Für $0\le n<M$ ist $g(n)=\frac{1-b^{n+1}}{1-b}$, die Antwort steigt an; für $n\ge M$ bleibt sie beim Endwert $\frac{1-b^{M}}{1-b}$ stehen, weil die Rückkopplung den letzten Wert festhält. Vor $n=0$ ist $g(n)=0$.
:::
:::karte zusammenhang Abklingen nach dem Rechteck
Warum klingt die Antwort des Systems $g(n)=s(n)+0{,}6\,g(n-1)$ nach dem Ende einer Rechteckfolge mit dem Faktor 0,6 je Takt ab, etwa von 2,176 auf 1,306?
---
Nach dem Rechteck ist der Eingang null, und es wirkt nur noch die Rückkopplung: Jeder Wert ist das 0,6-Fache des vorigen, so wie die Impulsantwort von Takt zu Takt mit $b$ multipliziert wird.
--- falsch
Weil der Ausgang in jedem Takt um 0,6 kleiner wird: Die Rekursion zieht nach dem Rechteck den Wert $b$ ab, bis der Ausgang null erreicht und dort stehen bleibt.
--- falsch
Weil das System nach dem Rechteck auf seine Impulsantwort umschaltet: Der letzte Eingangswert 1 wirkt wie ein neuer Impuls, und die Folge $0{,}6^n$ beginnt danach wieder bei 1.
--- falsch
Weil sich die Werte des Rechtecks nachträglich gegenseitig aufheben. Jeder Eingangswert zieht nach $M$ Takten seinen eigenen Beitrag wieder ab, bis vom Ausgang nur noch ein Rest übrig ist.
:::
:::karte zusammenhang Endwert bei Dauereingang
Gegen welchen Wert strebt der Ausgang des Systems $g(n)=s(n)+0{,}6\,g(n-1)$ bei einer unendlich langen Folge von Einsen, und warum?
---
Gegen $\frac{1}{1-b}=2{,}5$. Bei konstantem Eingang 1 summiert die Faltung alle Werte der Impulsantwort, und $\sum_nh(n)=\sum0{,}6^n=2{,}5$. Der Ausgang nähert sich diesem Wert von unten, Takt für Takt.
--- falsch
Gegen unendlich, weil in jedem Takt eine weitere Eins hinzukommt und die Rückkopplung den bisherigen Ausgang vollständig behält; der Ausgang wächst deshalb ohne Grenze.
--- falsch
Gegen 1, weil die Rückkopplung mit der Zeit abklingt und am Ende nur noch der aktuelle Eingangswert zum Ausgang beiträgt, unabhängig vom Wert von $b$.
--- falsch
Gegen $\frac{1}{b}\approx1{,}67$, weil im eingeschwungenen Zustand der Ausgang gleich $b$ mal dem Ausgang sein muss. Der Eingang spielt dann keine Rolle mehr, nur der Rückkopplungsfaktor.
:::
:::karte zusammenhang Vorzeichen und Betrag von b
Wie sieht die Impulsantwort des rekursiven Systems für $b=-0{,}6$ und für $b=1{,}1$ aus, und welches der beiden Systeme ist stabil?
---
Bei $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, das Vorzeichen wechselt, die Werte klingen ab, das System ist stabil. Bei $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, die Werte wachsen, das System ist instabil.
--- falsch
Bei $b=-0{,}6$ wachsen die Werte mit wechselndem Vorzeichen, weil ein negativer Faktor die Rückkopplung umkehrt; instabil. Bei $b=1{,}1$ klingen sie langsam ab, weil $b$ nahe bei 1 liegt; stabil.
--- falsch
Bei $b=-0{,}6$ sind alle Werte negativ und klingen ab; stabil. Bei $b=1{,}1$ wachsen die Werte zwar, das System ist aber trotzdem stabil, solange der Eingang beschränkt bleibt.
--- falsch
Bei $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\dots$, das System ist instabil, weil eine Folge mit wechselndem Vorzeichen nicht absolut summierbar ist. Bei $b=1{,}1$ wachsen die Werte, ebenfalls instabil.
:::
::::
