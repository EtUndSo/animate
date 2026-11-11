---
title: Eigenfunktionen von LTI-Systemen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220200
summary: Ein LTI-System verändert die Form fast jedes Signals.
tags: Realteil, Imaginärteil, konjugiert komplexe, Eigenfunktion, Eigenwert, komplexe Frequenz, p-Ebene, Laplace-Übertragungsfunktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein LTI-System verändert die Form fast jedes Signals. Dieser Abschnitt sucht Signale, deren Form es *nicht* verändert, und bestimmt die Zahl, mit der das System sie multipliziert.
:::

:::::vorwissen Was du dafür brauchst: die komplexe Exponentialfunktion

<span class="anker" id="stufe-1-1"></span>

In diesem Kapitel rechnet man ständig mit Exponentialfunktionen, deren Exponent eine komplexe Zahl ist. Dieser Unterabschnitt stellt zusammen, was ein solcher Ausdruck bedeutet.

**Komplexe Zahlen.** Eine komplexe Zahl $z=x+\mathrm{j} y$ besteht aus dem __Realteil__ $x=\operatorname{Re} z$ und dem __Imaginärteil__ $y=\operatorname{Im} z$, beides reelle Zahlen. Für die imaginäre Einheit gilt $\mathrm{j}^2=-1$. In der Elektrotechnik schreibt man $\mathrm{j}$ statt $i$, weil $i$ für den Strom vergeben ist. Man stellt $z$ als Punkt in einer Ebene dar: $x$ nach rechts, $y$ nach oben. Die zu $z$ __konjugiert komplexe__ Zahl $z^*=x-\mathrm{j} y$ ist ihr Spiegelbild an der waagerechten Achse.

**Die Eulersche Formel.** Für jede reelle Zahl $\varphi$ gilt

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}\varphi}=\cos\varphi+\mathrm{j}\sin\varphi . \tag{1.1}$$

Anschaulich ist $\mathrm{e}^{\mathrm{j}\varphi}$ der Punkt auf dem Kreis mit Radius 1, der um den Winkel $\varphi$ gegen den Uhrzeigersinn gedreht ist. Deshalb ist $|\mathrm{e}^{\mathrm{j}\varphi}|=\sqrt{\cos^2\varphi+\sin^2\varphi}=1$. Löst man [(1.1)](#gl-1-1) und die Formel für $-\varphi$ nach Kosinus und Sinus auf, erhält man

<span class="anker" id="gl-1-2"></span>
$$\cos\varphi=\frac{\mathrm{e}^{\mathrm{j}\varphi}+\mathrm{e}^{-\mathrm{j}\varphi}}{2},\qquad \sin\varphi=\frac{\mathrm{e}^{\mathrm{j}\varphi}-\mathrm{e}^{-\mathrm{j}\varphi}}{2\mathrm{j}}. \tag{1.2}$$

**Exponent mit Real- und Imaginärteil.** Die Rechenregel $\mathrm{e}^{z_1+z_2}=\mathrm{e}^{z_1}\,\mathrm{e}^{z_2}$ gilt auch für komplexe Zahlen. Mit einer reellen Zahl $\sigma$, einer reellen Kreisfrequenz $\omega$ und der Zeit $t$ folgt

$$\mathrm{e}^{(\sigma+\mathrm{j}\omega)t}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}\omega t}=\mathrm{e}^{\sigma t}\bigl[\cos(\omega t)+\mathrm{j}\sin(\omega t)\bigr].$$

Der Realteil $\mathrm{e}^{\sigma t}\cos(\omega t)$ ist eine Schwingung mit der Kreisfrequenz $\omega$, deren Amplitude $\mathrm{e}^{\sigma t}$ für $\sigma<0$ abklingt und für $\sigma>0$ wächst. Für $\sigma=0$ ist die Amplitude konstant 1.

::::beispiel
Für $\sigma=-0{,}5/\mathrm s$, $\omega=\pi/\mathrm s$ und $t=1\,\mathrm{s}$ ist $\mathrm{e}^{(-0{,}5+\mathrm{j}\pi)\cdot1}=\mathrm{e}^{-0{,}5}\bigl[\cos\pi+\mathrm{j}\sin\pi\bigr]=0{,}607\cdot(-1+0)=-0{,}607$.
::::

⁠**Kurz gesagt:** $\mathrm{e}^{(\sigma+\mathrm{j}\omega)t}$ ist eine komplexe Schwingung mit der Kreisfrequenz $\omega$, deren Amplitude $\mathrm{e}^{\sigma t}$ abklingt oder wächst.

:::::

### Rückblick: die Antwort eines LTI-Systems

<span class="anker" id="stufe-1-2"></span>

Ein LTI-System ist durch seine Impulsantwort $h(t)$ vollständig beschrieben. Auf ein Eingangssignal $s(t)$ antwortet es mit der Faltung

<span class="anker" id="gl-1-3"></span>
$$g(t)=s(t)*h(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau . \tag{1.3}$$

Man kann das Integral so lesen: Der Ausgang ist eine Summe *verzögerter Kopien* des Eingangs. Die Kopie, die um $\tau$ verzögert ist, geht mit dem Gewicht $h(\tau)\,\mathrm{d}\tau$ ein. Meist hat diese Summe eine andere Form als der Eingang. Ein Beispiel aus dem Kapitel zur Faltung: Ein Rechteckimpuls am Eingang eines RC-Glieds wird zu einem Signal, das ansteigt und wieder abklingt.

### Eigenfunktion und Eigenwert

<span class="anker" id="stufe-1-3"></span>

Gibt es Signale, die beim Durchgang durch ein LTI-System ihre Form behalten, die also höchstens mit einer Zahl multipliziert werden?

:::definition Definition 1.1 (Eigenfunktion und Eigenwert)
<span class="anker" id="satz-1-1"></span>

Ein Signal $s_\mathrm{E}(t)$ heißt __Eigenfunktion__ eines LTI-Systems mit der Impulsantwort $h(t)$, wenn es eine Konstante $H$ gibt, sodass

<span class="anker" id="gl-1-4"></span>
$$s_\mathrm{E}(t)*h(t)=H\cdot s_\mathrm{E}(t)\qquad\text{für alle }t . \tag{1.4}$$

Die Konstante $H$ heißt der zugehörige __Eigenwert__. Sie darf komplex sein, aber nicht von $t$ abhängen.
:::

Anschaulich: Der Ausgang ist der Eingang, nur mit einer Zahl multipliziert. Die Form bleibt erhalten.

::::beispiel das ideale Laufzeitglied
Es verzögert jedes Signal um die feste Zeit $T$: Seine Impulsantwort ist $h(t)=\delta(t-T)$, sein Ausgang $g(t)=s(t-T)$.

<ul>

<li>

Eingang $s(t)=\mathrm{e}^{at}$ mit einer reellen Zahl $a$: Der Ausgang ist $\mathrm{e}^{a(t-T)}=\mathrm{e}^{-aT}\cdot\mathrm{e}^{at}$, also eine Zahl mal der Eingang. $\mathrm{e}^{at}$ ist eine Eigenfunktion mit dem Eigenwert $\mathrm{e}^{-aT}$.

</li>

<li>

Eingang $s(t)=t$: Der Ausgang $t-T$ ist kein festes Vielfaches von $t$, denn der Quotient $(t-T)/t$ hängt von $t$ ab. $t$ ist keine Eigenfunktion.

</li>

</ul>
::::

⁠**Kurz gesagt:** Eine Eigenfunktion kommt aus dem System in derselben Form heraus, nur mit dem Eigenwert multipliziert.

### Die Exponentialfunktion $\mathrm{e}^{pt}$ als Eigenfunktion

<span class="anker" id="stufe-1-4"></span>

Das Beispiel legt nahe, Exponentialfunktionen zu untersuchen, und zwar gleich mit komplexem Exponenten:

<span class="anker" id="gl-1-5"></span>
$$s_\mathrm{E}(t)=\mathrm{e}^{pt}\quad\text{mit}\quad p=\sigma+\mathrm{j}2\pi f \quad\Longrightarrow\quad s_\mathrm{E}(t)=\mathrm{e}^{\sigma t}\bigl[\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)\bigr]. \tag{1.5}$$

Dabei sind $\sigma$ und $f$ reelle Zahlen, die Kreisfrequenz aus Abschnitt [1.1](#stufe-1-1) ist $\omega=2\pi f$. Setzt man $\mathrm{e}^{pt}$ in das Faltungsintegral [(1.3)](#gl-1-3) ein, so gilt für jedes komplexe $p$, für das das Integral existiert:

<span class="anker" id="gl-1-6"></span>
$$h(t)*\mathrm{e}^{pt}=\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{p(t-\tau)}\,\mathrm{d}\tau =\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)} . \tag{1.6}$$

Der entscheidende Schritt ist $\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{pt}\cdot\mathrm{e}^{-p\tau}$. Der Faktor $\mathrm{e}^{pt}$ hängt nicht von der Integrationsvariablen $\tau$ ab und darf deshalb vor das Integral. Was übrig bleibt, hängt nicht mehr von $t$ ab: Es ist eine Zahl, die nur von $p$ und vom System abhängt. Damit erfüllt $\mathrm{e}^{pt}$ die Definition [(1.4)](#gl-1-4), und zwar für *jedes* LTI-System.

⁠**Kurz gesagt:** $\mathrm{e}^{pt}$ ist eine Eigenfunktion jedes LTI-Systems, weil eine Verschiebung von $\mathrm{e}^{pt}$ dasselbe ist wie eine Multiplikation mit einer Zahl.

:::hintergrund Warum es genügt, dass Verschieben dasselbe ist wie Multiplizieren
Nach [(1.3)](#gl-1-3) ist der Ausgang eine Summe verzögerter Kopien des Eingangs. Bei einem beliebigen Signal sieht jede verzögerte Kopie anders aus als das Original, und ihre Summe hat eine neue Form. Bei $\mathrm{e}^{pt}$ ist die um $\tau$ verzögerte Kopie

$$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt},$$

also das Original, multipliziert mit der *konstanten Zahl* $\mathrm{e}^{-p\tau}$. Alle Kopien sind Vielfache derselben Funktion $\mathrm{e}^{pt}$. Dann ist auch ihre gewichtete Summe ein Vielfaches von $\mathrm{e}^{pt}$. Das System bestimmt nur, *welches* Vielfache: Die Gewichte $h(\tau)$ gehen in die Zahl $H(p)$ ein, die Form $\mathrm{e}^{pt}$ bleibt.
:::

:::hintergrund Warum der Exponent komplex sein muss
Ein Sinus wird beim Verschieben nicht nur skaliert. Mit $\omega_0=2\pi f_0$ gilt

$$\sin\bigl(\omega_0(t-\tau)\bigr)=\cos(\omega_0\tau)\,\sin(\omega_0t)-\sin(\omega_0\tau)\,\cos(\omega_0t).$$

Es entsteht ein Kosinusanteil, die verzögerte Kopie hat eine andere Form. Deshalb antwortet ein System auf $\sin(\omega_0t)$ im Allgemeinen mit einer Schwingung, deren Amplitude *und* Phase verändert sind. Eine Phasenverschiebung lässt sich nicht als Multiplikation mit einer reellen Zahl schreiben, wohl aber als Multiplikation mit der komplexen Zahl $\mathrm{e}^{\mathrm{j}\varphi}$. Die komplexe Exponentialfunktion verbindet beides: Ihre verschobene Kopie ist ein komplexes Vielfaches von ihr selbst. Ein reeller Sinus besteht nach [(1.2)](#gl-1-2) aus zwei solchen Funktionen, $\mathrm{e}^{\mathrm{j}\omega_0t}$ und $\mathrm{e}^{-\mathrm{j}\omega_0t}$, und jede wird mit ihrem eigenen Eigenwert multipliziert (Aufgabe [1](#aufg-1)c).
:::

### Die komplexe Frequenz und die $p$-Ebene

<span class="anker" id="stufe-1-5"></span>

Die Zahl $p=\sigma+\mathrm{j}2\pi f$ in [(1.5)](#gl-1-5) heißt __komplexe Frequenz__. Ihre beiden Teile legen fest, wie $\mathrm{e}^{pt}$ aussieht:

<ul>

<li>

Der Realteil $\sigma=\operatorname{Re} p$, gemessen in $1/\mathrm s$, ist die Wachstumsrate. Für $\sigma<0$ klingt $\mathrm{e}^{pt}$ ab, für $\sigma=0$ schwingt es mit konstanter Amplitude, für $\sigma>0$ wächst es.

</li>

<li>

Der Imaginärteil $\operatorname{Im} p=2\pi f$ legt die Frequenz $f$ der Schwingung fest, gemessen in Hz.

</li>

</ul>

Trägt man $\operatorname{Re} p$ nach rechts und $\operatorname{Im} p$ nach oben auf, so entsteht die __$p$-Ebene__. Jeder Punkt dieser Ebene steht für eine Funktion $\mathrm{e}^{pt}$. Seine Lage zeigt, wie sie aussieht (Abb. [1](#abb-1)): Der Abstand von der senkrechten Achse bestimmt das Abklingen oder Wachsen, die Höhe die Frequenz.

:::abbildung et3/k2bausteine 1
Die $p$-Ebene als Landkarte der Funktionen $\mathrm{e}^{pt}$. Links vier Punkte $p$ (in $1/\mathrm s$), rechts jeweils der Realteil $\operatorname{Re}\{\mathrm{e}^{pt}\}=\mathrm{e}^{\sigma t}\cos(2\pi ft)$ mit der Hüllkurve $\pm\mathrm{e}^{\sigma t}$ (gestrichelt). Die Punkte b, c, d haben $2\pi f=\pi/\mathrm s$, also $f=0{,}5$ Hz.
:::

⁠**Kurz gesagt:** Jeder Punkt $p$ der $p$-Ebene ist eine Funktion $\mathrm{e}^{pt}$. Links von der senkrechten Achse klingt sie ab, rechts wächst sie, und je höher der Punkt liegt, desto schneller schwingt sie.

### Die Laplace-Übertragungsfunktion

<span class="anker" id="stufe-1-6"></span>

Die Zahl, mit der das System $\mathrm{e}^{pt}$ multipliziert, steht in [(1.6)](#gl-1-6) unter der Klammer. Sie hängt vom System und von $p$ ab.

:::definition Definition 1.2 (Laplace-Übertragungsfunktion)
<span class="anker" id="satz-1-2"></span>

Für ein LTI-System mit der Impulsantwort $h(t)$ heißt

<span class="anker" id="gl-1-7"></span>
$$H(p)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t \tag{1.7}$$

die __Laplace-Übertragungsfunktion__. Sie ist für alle $p$ erklärt, für die das Integral existiert. $H(p)$ ist der Eigenwert, mit dem das System die Eigenfunktion $\mathrm{e}^{pt}$ multipliziert.
:::

Die Integrationsvariable heißt hier $t$ statt $\tau$, der Wert ist derselbe. Hat $h$ die Einheit $1/\mathrm s$, so ist $H(p)$ eine reine Zahl. Für welche $p$ das Integral existiert, hängt von $h$ ab.

::::beispiel der RC-Tiefpass
Seine Impulsantwort ist $h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)$. Wegen $\varepsilon(t)=0$ für $t<0$ beginnt das Integral bei null:

$$H(p)=\frac{1}{RC}\int_0^\infty\mathrm{e}^{-(p+1/RC)t}\,\mathrm{d} t=\frac{1}{RC}\cdot\frac{1}{p+1/RC}=\frac{1}{1+pRC}.$$

Das Integral existiert, wenn $\bigl|\mathrm{e}^{-(p+1/RC)t}\bigr|=\mathrm{e}^{-(\sigma+1/RC)t}$ für $t\to\infty$ abklingt, also für $\operatorname{Re} p>-1/RC$. Mit $RC=1\,\mathrm{s}$ ist $H(p)=1/(p+1)$, und zum Beispiel $H(-0{,}5/\mathrm s)=2$: Auf den Eingang $\mathrm{e}^{-t/2}$ antwortet das RC-Glied mit $2\,\mathrm{e}^{-t/2}$.
::::

⁠**Kurz gesagt:** $H(p)$ ist die Zahl, mit der ein LTI-System die Eigenfunktion $\mathrm{e}^{pt}$ multipliziert.

:::hintergrund Warum alle LTI-Systeme dieselben Eigenfunktionen haben
Die Form der Eigenfunktion folgt allein aus der Zeitinvarianz (Verschieben ist für $\mathrm{e}^{pt}$ dasselbe wie Multiplizieren), und die haben alle LTI-Systeme gemeinsam. Vom System hängt nur der Eigenwert $H(p)$ ab, denn in ihn gehen die Gewichte $h(\tau)$ ein. Deshalb dient *eine* Familie von Funktionen $\mathrm{e}^{pt}$ allen LTI-Systemen zugleich. Das macht die Laplace-Transformation universell.
:::

:::hintergrund Sind Exponentialfunktionen die einzigen Eigenfunktionen?
Man muss zwei Fragen trennen.

⁠**Eigenfunktion *aller* LTI-Systeme zugleich: ja, nur $c\,\mathrm{e}^{pt}$.** Das ideale Laufzeitglied $g(t)=s(t-u)$ ist für jede Verzögerung $u$ ein LTI-System. Eine Funktion $x(t)$, die Eigenfunktion jedes LTI-Systems ist, muss also bei jeder Verschiebung in ein Vielfaches ihrer selbst übergehen: $x(t+u)=c(u)\,x(t)$ für alle $t,u$. Ist $x$ differenzierbar und $x(0)=1$, folgt mit $t=0$ zunächst $c(u)=x(u)$, also $x(t+u)=x(t)\,x(u)$. Ableiten nach $u$ an der Stelle $u=0$ ergibt $x'(t)=x'(0)\,x(t)$. Das ist die Differentialgleichung $x'=p\,x$ mit $p=x'(0)$, und ihre Lösung mit $x(0)=1$ ist $x(t)=\mathrm{e}^{pt}$.

⁠**Eigenfunktion eines *bestimmten* Systems: nicht nur.** Das System multipliziert jedes $\mathrm{e}^{p_kt}$ mit seinem eigenen Eigenwert $H(p_k)$. Eine Summe $\sum_kc_k\mathrm{e}^{p_kt}$ bleibt genau dann ein Vielfaches ihrer selbst, wenn alle diese Eigenwerte gleich sind. Beispiel: Das Laufzeitglied um $T$ hat $H(p)=\int\delta(t-T)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{-pT}$. An allen Stellen $p_k=\mathrm{j}2\pi k/T$ mit ganzzahligem $k$ ist dieser Wert 1. Deshalb ist jedes Signal mit der Periode $T$ eine Eigenfunktion des Laufzeitglieds mit dem Eigenwert 1: $s(t-T)=s(t)$. Beim RC-Tiefpass dagegen nimmt $H(p)=1/(1+pRC)$ jeden Wert nur einmal an. Dort sind die einzelnen $c\,\mathrm{e}^{pt}$ die einzigen Eigenfunktionen, die sich aus Exponentialfunktionen zusammensetzen lassen.
:::

### Zwei Systeme in Kette

<span class="anker" id="stufe-1-7"></span>

Zwei LTI-Systeme mit den Impulsantworten $h_1(t)$ und $h_2(t)$ sind __in Kette__ geschaltet, wenn der Ausgang des ersten der Eingang des zweiten ist. Die Kette heißt __rückwirkungsfrei__, wenn das zweite System den Ausgang des ersten nicht verändert, zum Beispiel weil ein Trennverstärker dazwischen sitzt, der das erste System nicht belastet. Dann gilt für eine Eigenfunktion $s_\mathrm{E}(t)=\mathrm{e}^{pt}$:

<span class="anker" id="gl-1-8"></span>
$$\bigl[s_\mathrm{E}(t)*h_1(t)\bigr]*h_2(t)=\bigl[H_1(p)\,s_\mathrm{E}(t)\bigr]*h_2(t)=H_1(p)\,H_2(p)\,s_\mathrm{E}(t). \tag{1.8}$$

Das erste System multipliziert mit $H_1(p)$. Das Ergebnis ist immer noch ein Vielfaches von $\mathrm{e}^{pt}$, also eine Eigenfunktion des zweiten Systems, und dieses multipliziert mit $H_2(p)$.

::::beispiel
Zwei RC-Tiefpässe mit $RC=1\,\mathrm{s}$, entkoppelt durch einen Trennverstärker, multiplizieren $\mathrm{e}^{pt}$ mit $H_1(p)H_2(p)=1/(p+1)^2$.
::::

⁠**Kurz gesagt:** In einer rückwirkungsfreien Kette multiplizieren sich die Übertragungsfunktionen.

### Die Laplace-Transformation eines Signals

<span class="anker" id="stufe-1-8"></span>

Die Rechenvorschrift [(1.7)](#gl-1-7) lässt sich auf jedes Signal anwenden, nicht nur auf eine Impulsantwort.

:::definition Definition 1.3 (Zweiseitige Laplace-Transformation)
<span class="anker" id="satz-1-3"></span>

Für ein Signal $s(t)$ heißt

<span class="anker" id="gl-1-9"></span>
$$S(p)=\mathcal{L}_2\{s(t)\}=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t \tag{1.9}$$

die __Laplace-Transformierte__ von $s(t)$. Sie ist für alle $p$ erklärt, für die das Integral konvergiert.
:::

Das Signal $s(t)$ lebt im __Zeitbereich__, seine Transformierte $S(p)$ im __Bildbereich__. Man schreibt Zeitsignale mit kleinen und ihre Transformierten mit großen Buchstaben. Gehören $s(t)$ und $S(p)$ zusammen, schreibt man $s(t)\longleftrightarrow S(p)$. Die Übertragungsfunktion ist in dieser Sprache die Laplace-Transformierte der Impulsantwort, $H(p)=\mathcal{L}_2\{h(t)\}$.

::::beispiel der Einheitssprung
Für $s(t)=\varepsilon(t)$ ist

$$S(p)=\int_0^\infty\mathrm{e}^{-pt}\,\mathrm{d} t=\Bigl[-\frac{\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty=\frac1p,$$

sofern $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$ für $t\to\infty$ abklingt, also für $\operatorname{Re} p>0$.
::::

⁠**Kurz gesagt:** Die Laplace-Transformation ordnet einem Signal $s(t)$ die Funktion $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ der komplexen Frequenz zu.

:::hintergrund Warum man überhaupt transformiert: die Eigenfunktionen als Koordinatensystem
Das Vorbild stammt aus der linearen Algebra. Eine Matrix $\mathbf A$ hat Eigenvektoren $\mathbf v_k$ mit $\mathbf A\mathbf v_k=\lambda_k\mathbf v_k$. Schreibt man einen Vektor als Kombination dieser Eigenvektoren, $\mathbf x=\sum_kc_k\mathbf v_k$, so wirkt $\mathbf A$ besonders einfach:

$$\mathbf A\mathbf x=\sum_k\lambda_k\,c_k\,\mathbf v_k .$$

Jede Koordinate $c_k$ wird nur mit ihrem Eigenwert $\lambda_k$ multipliziert. In der Basis ihrer Eigenvektoren ist die Matrix diagonal, alle Kopplungen zwischen den Koordinaten sind verschwunden.

Ein LTI-System ist ebenfalls eine lineare Abbildung, nur von Signalen auf Signale. Seine Eigenfunktionen sind die Funktionen $\mathrm{e}^{pt}$, seine Eigenwerte die Zahlen $H(p)$. Im Zeitbereich beschreibt man ein Signal durch seine Werte zu allen Zeitpunkten $t$, und die Faltung koppelt sie: Jeder Ausgangswert hängt von allen Eingangswerten ab. Beschreibt man das Signal stattdessen dadurch, wie viel von jeder Funktion $\mathrm{e}^{pt}$ in ihm steckt, dann wirkt das System nur noch durch Multiplikation „Koordinate mal Eigenwert“. Diesen Wechsel der Beschreibung leistet die Laplace-Transformation. Darin liegt ihr ganzer Nutzen.

Der Vergleich ist ein Bild und hinkt an einer Stelle: Ein Vektor hat endlich viele Koordinaten, ein Signal dagegen kontinuierlich viele, eine für jedes $p$. Statt einer Summe braucht man deshalb ein Integral.
:::

:::hintergrund Was das Integral eigentlich tut: ein Suchfilter für Exponentialfunktionen
Das Integral $S(p)=\int s(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t$ multipliziert das Signal mit einer Probefunktion $\mathrm{e}^{-pt}$ und summiert das Produkt über alle Zeiten. Was dabei herauskommt, zeigt ein Signal, das aus einem einzigen Anteil $A\,\mathrm{e}^{p_0t}$ besteht: $s(t)=A\,\mathrm{e}^{p_0t}\,\varepsilon(t)$ mit einer komplexen Zahl $p_0$. Nach der Multiplikation steht im Integral

$$A\,\mathrm{e}^{p_0t}\cdot\mathrm{e}^{-pt}=A\,\mathrm{e}^{(p_0-p)t}.$$

<ul>

<li>

⁠**Die Probe trifft genau, $p=p_0$:** Der Integrand ist die Konstante $A$. Er schwingt nicht und klingt nicht ab, und das Integral $\int_0^\infty A\,\mathrm{d} t$ wächst über alle Grenzen.

</li>

<li>

⁠**Die Probe trifft nicht genau, $p\ne p_0$ mit $\operatorname{Re} p>\operatorname{Re} p_0$:** Der Integrand kreist wegen des Imaginärteils von $p_0-p$ und klingt wegen des Realteils ab. Das Integral bleibt endlich: $\int_0^\infty A\,\mathrm{e}^{-(p-p_0)t}\,\mathrm{d} t=\frac{A}{p-p_0}$.

</li>

</ul>

$|S(p)|$ ist also umso größer, je näher $p$ an $p_0$ liegt, und bei $p=p_0$ wird $S(p)$ unendlich. Im Zähler steht die Stärke $A$ des Anteils. Enthält das Signal mehrere Anteile, etwa $s(t)=\bigl(A_1\mathrm{e}^{p_1t}+A_2\mathrm{e}^{p_2t}\bigr)\varepsilon(t)$, so ist wegen der Linearität des Integrals

$$S(p)=\frac{A_1}{p-p_1}+\frac{A_2}{p-p_2}.$$

Über der $p$-Ebene aufgetragen, hat $|S(p)|$ an den Stellen $p_1$ und $p_2$ je eine Spitze, die ins Unendliche reicht. Die Transformation sucht das Signal also nach Exponentialfunktionen ab: Wo $S(p)$ unendlich wird, sitzt der Exponent eines Anteils, und der Zähler verrät seine Stärke. Gedämpfte Schwingungen bestehen nach der Eulerschen Formel aus genau solchen Anteilen; ein Kosinus zum Beispiel aus zwei.

⁠**Ein Bild dazu:** Nach demselben Prinzip arbeitet ein Lock-in-Verstärker. Er multipliziert ein verrauschtes Messsignal mit einer Referenzschwingung der gesuchten Frequenz und mittelt das Produkt. Nur der Anteil mit derselben Frequenz wird dabei zu einer Konstanten und übersteht das Mitteln; alle anderen schwingen weiter und mitteln sich heraus. Auch Funkempfänger mischen das Antennensignal mit einer Schwingung, um einen Sender herauszuholen. Die Laplace-Transformation macht das für alle $p$ zugleich, und weil $p$ komplex ist, sucht sie nicht nur nach Frequenzen, sondern auch nach Abklingraten. Das Bild hinkt an einer Stelle: Ein Messgerät mittelt über eine endliche Zeit und liefert einen endlichen Wert. Das Integral läuft über alle Zeiten, deshalb wird ein genau getroffener Anteil unendlich groß.
:::

### Die einseitige Laplace-Transformation

<span class="anker" id="stufe-1-9"></span>

Viele Signale beginnen erst bei $t=0$, zum Beispiel weil eine Spannung eingeschaltet wird. Für sie genügt die __einseitige Laplace-Transformation__

<span class="anker" id="gl-1-10"></span>
$$S(p)=\mathcal{L}_1\{s(t)\}=\int_{0}^{\infty}s(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t . \tag{1.10}$$

Ist $s(t)=0$ für $t<0$, liefern [(1.9)](#gl-1-9) und [(1.10)](#gl-1-10) denselben Wert. Damit ein Dirac-Impuls genau bei $t=0$ mitgezählt wird, lässt man das Integral knapp links von null beginnen. In diesem Kapitel ist mit $\mathcal{L}$ ohne Index die zweiseitige Transformation gemeint.

⁠**Kurz gesagt:** Für Signale, die erst bei $t=0$ beginnen, sind einseitige und zweiseitige Transformation gleich.

:::ltspice Eine Eigenfunktion im Experiment
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg` von `in` nach `out`, `cap` mit `1u` nach Masse), also $RC=1\,\mathrm{s}$. Als Quelle eine Verhaltensquelle `bv` mit `V=exp(-time/2)`, das ist $\mathrm{e}^{pt}$ mit $p=-0{,}5/\mathrm s$.

⁠**Direktiven:** `.tran 0 10 0 1m` und `.ic V(out)=X` mit einer Zahl für $X$: Der Kondensator startet bei $X$ Volt. Lass dir mit „Add Traces“ den Ausdruck `V(out)/V(in)` zeichnen.

⁠**Was du siehst:** Setzt du für $X$ den Wert, den dein Ergebnis aus Aufgabe [1](#aufg-1)(a) bei $t=0$ hat, ist das Verhältnis von Anfang an konstant: Der Ausgang ist eine Zahl mal der Eingang. Mit $X=0$ nähert es sich derselben Zahl erst nach einigen Sekunden. Der Grund: Ein Eingang, der schon immer anlag, hätte den Kondensator bei $t=0$ genau auf diesen Wert geladen. Jede andere Anfangsspannung baut das RC-Glied mit $\mathrm{e}^{-t}$ ab, schneller als der Eingang mit $\mathrm{e}^{-t/2}$ abklingt.

⁠**Zu (c):** Quelle `voltage` mit `SINE(0 1 {1/(2*pi)} 0 0 90)`, das ist $\cos t$. Vergleiche Amplitude und Nacheilung von `V(out)` nach dem Einschwingen mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(c).
:::

:::aufgabe Aufgabe 1 ★ Eigenfunktion oder nicht?
<span class="anker" id="aufg-1"></span>

Benutze den RC-Tiefpass mit $RC=1\,\mathrm{s}$, also $h(t)=\mathrm{e}^{-t}\varepsilon(t)$ und $H(p)=1/(p+1)$ für $\operatorname{Re} p>-1$.

<ol class="al">

<li>

Eingang $s(t)=\mathrm{e}^{-t/2}$ für alle $t$. Berechne den Ausgang einmal direkt mit dem Faltungsintegral und einmal mit $H(p)$. Welches $p$ hat dieses Signal?

</li>

<li>

Eingang $s(t)=t$ für alle $t$. Zeige mit dem Faltungsintegral, dass $g(t)=t-1$ herauskommt. Warum ist $t$ keine Eigenfunktion, obwohl der Ausgang ähnlich aussieht? Was bedeutet die $-1$ für den Kondensator?

</li>

<li>

Eingang $s(t)=\cos t$ (also $\omega_0=1/\mathrm s$). Zerlege den Kosinus mit [(1.2)](#gl-1-2) in zwei Exponentialfunktionen, multipliziere jede mit ihrem $H(p)$ und setze wieder zusammen. Zeige, dass $g(t)=A\cos(t+\varphi)$ ist, und bestimme $A$ und $\varphi$. Ist $\cos t$ eine Eigenfunktion?

</li>

</ol>

⁠*Tipp zu (b):* $\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau=1$ und $\int_0^\infty\tau\,\mathrm{e}^{-\tau}\mathrm{d}\tau=1$.

:::loesung
(a) Direkt:

$$g(t)=\int_0^\infty\mathrm{e}^{-\tau}\,\mathrm{e}^{-(t-\tau)/2}\mathrm{d}\tau=\mathrm{e}^{-t/2}\int_0^\infty\mathrm{e}^{-\tau/2}\mathrm{d}\tau=2\,\mathrm{e}^{-t/2}.$$

Mit $H(p)$: Das Signal ist $\mathrm{e}^{pt}$ mit $p=-\tfrac12/\mathrm s$ (reell, ohne Schwingung). Es liegt im Bereich $\operatorname{Re} p>-1$, in dem $H(p)$ existiert, und $H(-\tfrac12)=1/(\tfrac12)=2$, also $g(t)=2\,\mathrm{e}^{-t/2}$. Beide Wege stimmen überein (numerisch: $g(1\,\mathrm{s})=1{,}2131$).

(b) $g(t)=\int_0^\infty\mathrm{e}^{-\tau}(t-\tau)\mathrm{d}\tau=t\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau-\int_0^\infty\tau\mathrm{e}^{-\tau}\mathrm{d}\tau=t-1$. Das ist kein Vielfaches von $t$: Die verzögerten Kopien $t-\tau$ sind keine Vielfachen von $t$ (der Faktor $1-\tau/t$ hängt von $t$ selbst ab). Der Ausgang ist die *verschobene* Rampe: Die Kondensatorspannung folgt der Eingangsrampe mit einer Verzögerung von $RC=1$ s. Gestalt gleich, aber verschoben statt skaliert, also keine Eigenfunktion.

(c) Nach [(1.2)](#gl-1-2) ist $\cos t=\tfrac12\mathrm{e}^{\mathrm{j} t}+\tfrac12\mathrm{e}^{-\mathrm{j} t}$, also zwei Exponentialfunktionen mit $p=\pm\mathrm{j}$. Beide liegen im Bereich $\operatorname{Re} p=0>-1$.

$$H(\mathrm{j})=\frac{1}{1+\mathrm{j}}=\frac{1}{\sqrt2}\,\mathrm{e}^{-\mathrm{j}\pi/4},\qquad H(-\mathrm{j})=H(\mathrm{j})^*=\frac{1}{\sqrt2}\,\mathrm{e}^{+\mathrm{j}\pi/4}.$$

$$g(t)=\tfrac12H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}+\tfrac12H(-\mathrm{j})\mathrm{e}^{-\mathrm{j} t}=\operatorname{Re}\bigl\{H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}\bigr\}=\frac{1}{\sqrt2}\cos\Bigl(t-\frac\pi4\Bigr).$$

Also $A=1/\sqrt2\approx0{,}707$ und $\varphi=-45^\circ$ (numerisch: $g(1\,\mathrm{s})=0{,}6909$). Jede der beiden komplexen Exponentialfunktionen ist eine Eigenfunktion, ihre Summe $\cos t$ nicht: Die beiden werden mit *verschiedenen* Zahlen multipliziert, $H(\mathrm{j})\neq H(-\mathrm{j})$. Dadurch verschiebt sich die Phase.
:::
:::

::::kurzfassung
Ein LTI-System verändert die Form fast jedes Signals. Die komplexe Exponentialfunktion $\mathrm{e}^{pt}$ ist die Ausnahme: Jedes LTI-System multipliziert sie nur mit einer Zahl.

Ein Signal $s_\mathrm{E}(t)$ heißt __Eigenfunktion__ eines LTI-Systems mit der Impulsantwort $h(t)$, wenn $s_\mathrm{E}(t)*h(t)=H\cdot s_\mathrm{E}(t)$ für alle $t$ gilt. Die Konstante $H$ heißt __Eigenwert__; sie darf komplex sein, aber nicht von $t$ abhängen. Der Exponent $p=\sigma+\mathrm{j}2\pi f$ heißt __komplexe Frequenz__: $\sigma=\operatorname{Re} p$ ist die Wachstumsrate, $f$ die Frequenz der Schwingung. In der __$p$-Ebene__ steht jeder Punkt für eine Funktion $\mathrm{e}^{pt}$; links der senkrechten Achse klingt sie ab, rechts wächst sie. Der Eigenwert zu $\mathrm{e}^{pt}$ ist die __Laplace-Übertragungsfunktion__

$$H(p)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t ,$$

erklärt für alle $p$, für die das Integral existiert.

Der Grund ist $\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt}$: Jede verzögerte Kopie von $\mathrm{e}^{pt}$ ist ein Vielfaches von $\mathrm{e}^{pt}$, also auch die gewichtete Summe solcher Kopien, die das Faltungsintegral bildet. Das folgt allein aus der Zeitinvarianz; vom System hängt nur der Eigenwert ab.

Zwei Systeme sind __in Kette__ geschaltet, wenn der Ausgang des ersten der Eingang des zweiten ist. Ist die Kette __rückwirkungsfrei__, multiplizieren sich die Übertragungsfunktionen zu $H_1(p)\,H_2(p)$. Dieselbe Rechenvorschrift, auf ein beliebiges Signal angewandt, ergibt seine __Laplace-Transformierte__ $S(p)=\mathcal{L}_2\{s(t)\}$. Das Signal $s(t)$ liegt im __Zeitbereich__, $S(p)$ im __Bildbereich__. Für Signale, die erst bei $t=0$ beginnen, liefert die __einseitige Laplace-Transformation__ $\mathcal{L}_1$ mit dem Integral ab $0$ denselben Wert.

Falle: Ein reeller Kosinus ist im Allgemeinen keine Eigenfunktion. Er besteht aus $\mathrm{e}^{\mathrm{j}\omega_0t}$ und $\mathrm{e}^{-\mathrm{j}\omega_0t}$, und jede der beiden bekommt ihren eigenen Eigenwert.
::::

::::formelsammlung
**Eulersche Formel**

$$\mathrm{e}^{\mathrm{j}\varphi}=\cos\varphi+\mathrm{j}\sin\varphi$$

$\varphi$ reell; $\mathrm{e}^{\mathrm{j}\varphi}$ liegt auf dem Kreis mit Radius 1, $|\mathrm{e}^{\mathrm{j}\varphi}|=1$.

**Kosinus und Sinus durch Exponentialfunktionen**

$$\cos\varphi=\frac{\mathrm{e}^{\mathrm{j}\varphi}+\mathrm{e}^{-\mathrm{j}\varphi}}{2},\qquad \sin\varphi=\frac{\mathrm{e}^{\mathrm{j}\varphi}-\mathrm{e}^{-\mathrm{j}\varphi}}{2\mathrm{j}}$$

Aufgelöst aus der Eulerschen Formel für $\varphi$ und $-\varphi$.

**Exponent mit Real- und Imaginärteil**

$$\mathrm{e}^{(\sigma+\mathrm{j}\omega)t}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}\omega t}=\mathrm{e}^{\sigma t}\bigl[\cos(\omega t)+\mathrm{j}\sin(\omega t)\bigr]$$

$\sigma$ reell, $\omega$ reelle Kreisfrequenz, $t$ Zeit. Die Amplitude $\mathrm{e}^{\sigma t}$ klingt für $\sigma<0$ ab, wächst für $\sigma>0$ und ist für $\sigma=0$ konstant 1.

**Antwort eines LTI-Systems (Faltung)**

$$g(t)=s(t)*h(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau$$

$s(t)$ Eingang, $h(t)$ Impulsantwort, $g(t)$ Ausgang; die um $\tau$ verzögerte Kopie des Eingangs geht mit dem Gewicht $h(\tau)\,\mathrm{d}\tau$ ein.

**Eigenfunktion und Eigenwert (Definition)**

$$s_\mathrm{E}(t)*h(t)=H\cdot s_\mathrm{E}(t)$$

Für alle $t$. $s_\mathrm{E}(t)$ Eigenfunktion des LTI-Systems mit der Impulsantwort $h(t)$; $H$ Eigenwert, darf komplex sein, hängt nicht von $t$ ab.

**Komplexe Frequenz**

$$p=\sigma+\mathrm{j}2\pi f$$

$\sigma=\operatorname{Re} p$ Wachstumsrate in $1/\mathrm s$ ($\sigma<0$ abklingend, $\sigma=0$ konstante Amplitude, $\sigma>0$ wachsend); $\operatorname{Im} p=2\pi f$ mit der Frequenz $f$ in Hz, $\omega=2\pi f$. Jeder Punkt der $p$-Ebene steht für eine Funktion $\mathrm{e}^{pt}$.

**$\mathrm{e}^{pt}$ als Eigenfunktion jedes LTI-Systems**

$$h(t)*\mathrm{e}^{pt}=\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{p(t-\tau)}\,\mathrm{d}\tau=\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)}$$

Für jedes komplexe $p$, für das das Integral existiert. Schlüssel: $\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{pt}\cdot\mathrm{e}^{-p\tau}$.

**Laplace-Übertragungsfunktion (Definition)**

$$H(p)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t$$

Eigenwert, mit dem das System $\mathrm{e}^{pt}$ multipliziert; erklärt für alle $p$, für die das Integral existiert. Hat $h$ die Einheit $1/\mathrm s$, ist $H(p)$ eine reine Zahl.

**RC-Tiefpass**

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}$$

Das Integral existiert für $\operatorname{Re} p>-1/RC$.

**Rückwirkungsfreie Kette**

$$\bigl[s_\mathrm{E}(t)*h_1(t)\bigr]*h_2(t)=\bigl[H_1(p)\,s_\mathrm{E}(t)\bigr]*h_2(t)=H_1(p)\,H_2(p)\,s_\mathrm{E}(t)$$

$s_\mathrm{E}(t)=\mathrm{e}^{pt}$; Ausgang des ersten Systems ist Eingang des zweiten, das zweite verändert den Ausgang des ersten nicht.

**Zweiseitige Laplace-Transformation (Definition)**

$$S(p)=\mathcal{L}_2\{s(t)\}=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t$$

Für alle $p$, für die das Integral konvergiert. $s(t)$ im Zeitbereich, $S(p)$ im Bildbereich; Schreibweise $s(t)\longleftrightarrow S(p)$. Es gilt $H(p)=\mathcal{L}_2\{h(t)\}$.

**Einseitige Laplace-Transformation**

$$S(p)=\mathcal{L}_1\{s(t)\}=\int_{0}^{\infty}s(t)\,\mathrm{e}^{-pt}\,\mathrm{d} t$$

Untere Grenze knapp links von null, damit ein Dirac-Impuls bei $t=0$ mitzählt. Gleich der zweiseitigen, wenn $s(t)=0$ für $t<0$. $\mathcal{L}$ ohne Index bedeutet die zweiseitige Transformation.
::::
