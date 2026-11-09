---
title: Integration längs regulärer Kurven
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130200
summary: Ein Teilchen läuft auf einem Weg durch ein Vektorfeld.
tags: rechtsseitige Ableitung, linksseitige Ableitung, streng monoton wachsend, streng monoton fallend, Umkehrfunktion, Cauchy-Schwarz-Ungleichung, stückweise stetig differenzierbar, Knickstelle
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Teilchen läuft auf einem Weg durch ein Vektorfeld. Dieser Abschnitt legt fest, welche Wege zugelassen sind, und summiert das Feld längs eines Wegs zu einer Zahl auf. Er klärt, was diese Zahl von der Beschreibung des Wegs übernimmt und was nicht, wie man die Länge eines Wegs berechnet und wie man die Zahl abschätzt, ohne sie auszurechnen.
:::

### Was du dafür brauchst: Kurven und einseitige Ableitungen

<span class="anker" id="stufe-1-1"></span>

Ein Weg durch den Raum wird in diesem Kapitel als Kurve beschrieben. [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat Kurven eingeführt, [Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html) die einseitigen Ableitungen; beides wird hier zusammengeführt.

**Kurven.** Eine *Kurve* ist eine Abbildung $\gamma\colon I\to\mathbb{R}^n$, $t\mapsto\gamma(t)=\bigl(\gamma_1(t),\dots,\gamma_n(t)\bigr)$, von einem Intervall $I$ in den $\mathbb{R}^n$ ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)). Man liest $t$ als Zeit und $\gamma(t)$ als den Ort eines Punkts zur Zeit $t$. In diesem Kapitel ist $I$ fast immer ein abgeschlossenes Intervall $[a,b]$ mit $a<b$. Die Kurve heißt differenzierbar, wenn jede Komponente $\gamma_j$ differenzierbar ist. Dann ist $\dot\gamma(t)=\bigl(\dot\gamma_1(t),\dots,\dot\gamma_n(t)\bigr)$ der Tangentenvektor. Er zeigt in Laufrichtung, und seine Länge $|\dot\gamma(t)|$ ist das Tempo. Für kleine Zahlen $\tau'$ gilt $\gamma(t+\tau')\approx\gamma(t)+\tau'\,\dot\gamma(t)$; der Punkt rückt also um ungefähr „Tangentenvektor mal Zeitschritt“ vor.

**Einseitige Ableitungen.** Am linken Ende $a$ eines Intervalls kann man sich nur von rechts nähern. Der Grenzwert

$$\lim_{h\searrow0}\frac{\gamma(t+h)-\gamma(t)}{h},$$

bei dem $h$ nur positive Werte annimmt, heißt die __rechtsseitige Ableitung__ von $\gamma$ an der Stelle $t$. Entsprechend heißt der Grenzwert mit negativen $h$, also $h\nearrow0$, die __linksseitige Ableitung__. Beide werden Komponente für Komponente gebildet, wie in [Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html). Ist $\gamma$ an einer inneren Stelle differenzierbar, stimmen beide mit $\dot\gamma(t)$ überein.

::::beispiel
Der Kreis $\gamma(t)=(\cos t,\sin t)$, $t\in[0,2\pi]$, hat den Tangentenvektor $\dot\gamma(t)=(-\sin t,\cos t)$ mit dem Tempo $1$. Die Kurve $\gamma(t)=(t,|t|)$ auf $[-1,1]$ ist bei $t=0$ nicht differenzierbar. Für $h>0$ ist $\frac{\gamma(h)-\gamma(0)}h=(1,1)$, für $h<0$ ist es $(1,-1)$. Die rechtsseitige Ableitung bei $0$ ist also $(1,1)$, die linksseitige $(1,-1)$.
::::

⁠**Kurz gesagt:** Eine Kurve ist eine Abbildung von einem Intervall in den $\mathbb{R}^n$. Wo sie nicht differenzierbar ist, kann es trotzdem eine Ableitung von links und eine von rechts geben.

### Was du dafür brauchst: streng monotone Funktionen und Umkehrfunktionen

<span class="anker" id="stufe-1-2"></span>

Dieselbe Kurve lässt sich mit einer anderen Uhr ablesen. Dafür braucht man Funktionen, die die Zeitachse umnummerieren, ohne die Reihenfolge durcheinanderzubringen.

**Streng monoton.** Eine Funktion $\tau\colon[c,d]\to\mathbb{R}$ heißt __streng monoton wachsend__, wenn aus $u_1<u_2$ stets $\tau(u_1)<\tau(u_2)$ folgt. Sie heißt __streng monoton fallend__, wenn aus $u_1<u_2$ stets $\tau(u_1)>\tau(u_2)$ folgt. Ist $\tau$ differenzierbar und $\tau'(u)>0$ für alle $u$, dann ist $\tau$ streng monoton wachsend. Das folgt aus dem Mittelwertsatz ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)): $\tau(u_2)-\tau(u_1)=\tau'(\vartheta)\,(u_2-u_1)>0$ mit einer Zwischenstelle $\vartheta$.

**Umkehrfunktion.** Eine streng monotone stetige Funktion $\tau\colon[c,d]\to\mathbb{R}$ nimmt jeden Wert zwischen $\tau(c)$ und $\tau(d)$ genau einmal an. Ordnet man jedem solchen Wert $t$ die Stelle $u$ mit $\tau(u)=t$ zu, entsteht die __Umkehrfunktion__ $\tau^{-1}$. Ist $\tau$ stetig differenzierbar mit $\tau'(u)\neq0$ für alle $u$, dann ist auch $\tau^{-1}$ stetig differenzierbar, und Ableiten von $\tau\bigl(\tau^{-1}(t)\bigr)=t$ mit der Kettenregel ergibt

$$\bigl(\tau^{-1}\bigr)'(t)=\frac{1}{\tau'\bigl(\tau^{-1}(t)\bigr)} .$$

::::beispiel
$\tau(u)=2u+1$ auf $[0,1]$ ist streng monoton wachsend mit $\tau'=2$. Die Umkehrfunktion ist $\tau^{-1}(t)=\frac{t-1}2$ auf $[1,3]$ mit der Ableitung $\frac12=\frac1{\tau'}$. Die Funktion $\tau(u)=u^3$ auf $[-1,1]$ ist ebenfalls streng monoton wachsend, aber $\tau'(0)=0$. Ihre Umkehrfunktion $t\mapsto\sqrt[3]{t}$ (für negative $t$ als $-\sqrt[3]{|t|}$) ist bei $t=0$ nicht differenzierbar: Dort ist ihre Steigung unendlich groß.
::::

⁠**Kurz gesagt:** Eine streng monotone Funktion bringt keine Reihenfolge durcheinander und hat eine Umkehrfunktion. Ist ihre Ableitung nirgends null, ist auch die Umkehrfunktion differenzierbar.

### Was du dafür brauchst: die Cauchy-Schwarz-Ungleichung

<span class="anker" id="stufe-1-3"></span>

Das Skalarprodukt zweier Vektoren kann nicht größer werden als das Produkt ihrer Längen. Diese Abschätzung wird am Ende des Abschnitts gebraucht.

Nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist $\boldsymbol a\cdot\boldsymbol b=|\boldsymbol a|\,|\boldsymbol b|\cos\alpha$ mit dem Winkel $\alpha$ zwischen den beiden Vektoren. Wegen $|\cos\alpha|\le1$ folgt die __Cauchy-Schwarz-Ungleichung__

<span class="anker" id="gl-1-1"></span>
$$|\boldsymbol a\cdot\boldsymbol b|\le|\boldsymbol a|\,|\boldsymbol b| . \tag{1.1}$$

Gleichheit gilt genau dann, wenn die beiden Vektoren parallel oder antiparallel sind oder einer von ihnen null ist.

::::beispiel
$(1,2)\cdot(3,4)=11$ und $|(1,2)|\,|(3,4)|=\sqrt5\cdot5\approx11{,}18$. Für die parallelen Vektoren $(1,2)$ und $(2,4)$ ist $(1,2)\cdot(2,4)=10=\sqrt5\cdot\sqrt{20}$.
::::

⁠**Kurz gesagt:** Der Betrag eines Skalarprodukts ist höchstens das Produkt der Längen.

### Stückweise stetig differenzierbare Kurven

<span class="anker" id="stufe-1-4"></span>

Der Rand eines Quadrats ist ein geschlossener Weg mit vier Ecken. In den Ecken springt die Laufrichtung, die Kurve ist dort nicht differenzierbar. Solche Wege will man trotzdem zulassen, solange es nur endlich viele Ecken sind.

Man kann sich einen Wanderweg vorstellen, der aus mehreren glatten Stücken besteht. An jeder Ecke kommt man mit einer Richtung an und geht mit einer anderen weiter (Abb. [1](#abb-1)). Die Ankunftsrichtung ist die linksseitige Ableitung, die Abgangsrichtung die rechtsseitige.

:::abbildung hm3/k3knick 1
Eine Kurve aus zwei glatten Stücken mit einem Knick bei $t=a_1$. Rot die linksseitige Ableitung im Knick: die Richtung, mit der der Punkt ankommt. Grün die rechtsseitige Ableitung: die Richtung, mit der er weiterläuft. Beide existieren, sie sind nur verschieden.
:::

:::definition Definition 1.1 (Stückweise stetig differenzierbar)
<span class="anker" id="satz-1-1"></span>

Eine Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ heißt __stückweise stetig differenzierbar__, wenn sie stetig ist und es endlich viele Stellen $a=a_0<a_1<\dots<a_N=b$ gibt, so dass $\gamma$ auf jedem Teilintervall $[a_{k-1},a_k]$ stetig differenzierbar ist. An den Enden der Teilintervalle sind dabei die einseitigen Ableitungen gemeint.
:::

⁠**So liest man das:** Innerhalb jedes Stücks ist die Kurve glatt, und ihr Tangentenvektor ändert sich stetig. An einer Stelle $a_k$ zwischen zwei Stücken existieren die linksseitige Ableitung des linken Stücks und die rechtsseitige des rechten. Stimmen sie nicht überein, heißt $a_k$ eine __Knickstelle__. Die Bedingung, dass $\gamma$ stetig ist, verbietet Sprünge: Am Ende jedes Stücks beginnt das nächste.

::::beispiel [Beispiel 1]
$\gamma(t)=(t,|t|)$ auf $[-1,1]$ mit den Stücken $[-1,0]$ und $[0,1]$. Auf dem ersten ist $\gamma(t)=(t,-t)$ mit $\dot\gamma=(1,-1)$, auf dem zweiten $\gamma(t)=(t,t)$ mit $\dot\gamma=(1,1)$. Die Stelle $t=0$ ist eine Knickstelle.
::::

::::beispiel [Beispiel 2]
Der Rand des Einheitsquadrats, gegen den Uhrzeigersinn durchlaufen, mit der Parametrisierung $\gamma(t)=(t,0)$ für $t\in[0,1]$, $(1,t-1)$ für $t\in[1,2]$, $(3-t,1)$ für $t\in[2,3]$ und $(0,4-t)$ für $t\in[3,4]$. Die Knickstellen sind $t=1,2,3$.
::::

::::beispiel [Gegenbeispiel]
$\gamma(t)=\bigl(t,\sqrt{|t|}\bigr)$ auf $[-1,1]$. Für $h>0$ ist $\frac{\gamma(h)-\gamma(0)}h=\bigl(1,\,1/\sqrt h\bigr)$, und die zweite Komponente wächst über alle Grenzen. Bei $t=0$ gibt es also keine einseitige Ableitung, die Kurve ist dort nicht stückweise stetig differenzierbar.
::::

⁠**Kurz gesagt:** Eine stückweise stetig differenzierbare Kurve besteht aus endlich vielen glatten Stücken, die ohne Lücke aneinanderhängen.

### Reguläre Parametrisierung

<span class="anker" id="stufe-1-5"></span>

Längs eines Wegs soll es an jeder Stelle eine Laufrichtung geben. Das geht schief, wenn der Punkt stehen bleibt, denn dann ist der Tangentenvektor null und zeigt nirgendwohin.

Abb. [2](#abb-2) zeigt die Kurve $\gamma(t)=(t^2,t^3)$ für $t\in[-1,1]$. Die Punkte gehören zu gleich großen Zeitschritten. Sie rücken zum Nullpunkt hin immer enger zusammen: Der Punkt wird langsamer, steht bei $t=0$ still und läuft dann in die Richtung zurück, aus der er gekommen ist. Dabei entsteht eine Spitze, obwohl die Formel keinen Knick enthält.

:::abbildung hm3/k3spitze 2
Die Kurve $\gamma(t)=(t^2,t^3)$ für $t\in[-1,1]$. Die Punkte gehören zu den Zeiten $t=-1,-\frac34,\dots,1$. Unten läuft der Punkt auf den Nullpunkt zu und wird dabei langsamer, oben läuft er wieder weg (rote Pfeile: Laufrichtung). Bei $t=0$ ist $\dot\gamma=(0,0)$, und die Spur hat eine Spitze.
:::

:::definition Definition 1.2 (Regulär parametrisierte Kurve)
<span class="anker" id="satz-1-2"></span>

Eine stückweise stetig differenzierbare Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ heißt __regulär parametrisiert__, wenn

$$\dot\gamma(t)\neq0$$

für alle $t\in[a,b]$ gilt, an denen $\gamma$ differenzierbar ist. An Knickstellen und an den Endpunkten $a$ und $b$ gilt diese Bedingung für die einseitigen Ableitungen.
:::

⁠**So liest man das:** Regulär heißt: Der Punkt bleibt nie stehen. Dann hat die Kurve überall eine Laufrichtung, im Knick sogar zwei, eine ankommende und eine abgehende. Die Abbildung $\gamma$ nennt man auch die __Parametrisierung__ der Kurve, und $t$ den __Parameter__.

::::beispiel
Der Kreis $(\cos t,\sin t)$ ist regulär parametrisiert, denn $|\dot\gamma(t)|=1$. Die Kurve $(t,|t|)$ ist es ebenfalls: Ihre Ableitungen $(1,\pm1)$ sind nie null, auch die beiden einseitigen im Knick nicht. Die Kurve $\gamma(t)=(t^2,t^3)$ hat $\dot\gamma(t)=(2t,3t^2)$ und $\dot\gamma(0)=(0,0)$; sie ist nicht regulär parametrisiert.
::::

:::hintergrund Warum man Stillstand verbietet
Die Laufrichtung an der Stelle $t$ ist der Pfeil $\dot\gamma(t)/|\dot\gamma(t)|$. Bei $\dot\gamma(t)=0$ ist dieser Bruch nicht erklärt. Das ist mehr als ein Formfehler. Bei der Kurve $(t^2,t^3)$ kommt der Punkt aus der Richtung $(1,-1)$, bleibt stehen und kehrt um (Abb. [2](#abb-2)). Löst man $x=t^2$ und $y=t^3$ nach $t$ auf, besteht die Spur aus den beiden Ästen $y=\pm x^{3/2}$, $x\ge0$. Sie berühren sich im Nullpunkt und bilden dort eine Spitze, keinen glatten Bogen.

Regularität ist eine Eigenschaft der Parametrisierung, nicht der Punktmenge. Die Kurve $(t^3,t^3)$ auf $[-1,1]$ läuft auf derselben Strecke wie $(t,t)$, aber ihr Tangentenvektor $(3t^2,3t^2)$ ist bei $t=0$ null: Der Punkt hält mitten auf der Strecke kurz an. Die erste Parametrisierung ist nicht regulär, die zweite schon. Man kann also manchmal eine reguläre Parametrisierung finden, wo die gegebene es nicht ist; bei der Spitze von $(t^2,t^3)$ geht das nicht, weil der Punkt dort wirklich umkehrt.
:::

⁠**Kurz gesagt:** Eine Kurve ist regulär parametrisiert, wenn der Punkt nie stehen bleibt: Ihr Tangentenvektor ist überall ungleich null, in Knicken von beiden Seiten.

### Geschlossene Kurven

<span class="anker" id="stufe-1-6"></span>

Manche Wege führen zum Ausgangspunkt zurück, etwa ein Rundweg oder der Rand einer Fläche.

:::definition Definition 1.3 (Geschlossene Kurve)
<span class="anker" id="satz-1-3"></span>

Eine Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ heißt __geschlossen__, wenn $\gamma(a)=\gamma(b)$ gilt.
:::

::::beispiel
Der Kreis $(\cos t,\sin t)$ auf $[0,2\pi]$ ist geschlossen, denn $\gamma(0)=\gamma(2\pi)=(1,0)$. Der Rand des Einheitsquadrats aus Unterabschnitt [1.4](#stufe-1-4) ist geschlossen. Der Viertelkreis $\kappa(t)=(\cos t,\sin t)$, $t\in[0,\pi/2]$, ist es nicht: Er beginnt in $(1,0)$ und endet in $(0,1)$.
::::

⁠**Kurz gesagt:** Eine geschlossene Kurve endet dort, wo sie beginnt.

### Einfache Kurven

<span class="anker" id="stufe-1-7"></span>

Eine Kurve kann sich selbst kreuzen oder dieselbe Strecke mehrfach durchlaufen. Oft braucht man Kurven, die das nicht tun, etwa um von „der Fläche innerhalb der Kurve“ sprechen zu können.

Abb. [3](#abb-3) zeigt vier Kurven. Der Kreis ist nur am Anfang und am Ende am selben Ort. Der zweimal durchlaufene Kreis und die Acht sind auch zwischendurch zu zwei verschiedenen Zeiten am selben Ort.

:::abbildung hm3/k3kurven 3
Vier Kurven. Der Kreis ist nur am Anfang und am Ende am selben Ort. Der zweimal durchlaufene Kreis und die Acht sind auch zwischendurch zu zwei verschiedenen Zeiten am selben Ort (rot). In der Spitze steht der Punkt einen Augenblick still, obwohl die Formel glatt ist.
:::

:::definition Definition 1.4 (Einfache Kurve)
<span class="anker" id="satz-1-4"></span>

Eine Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ heißt __einfach__ oder __doppelpunktfrei__, wenn aus

$$\gamma(t_1)=\gamma(t_2)\qquad\text{mit}\qquad t_1<t_2$$

stets $t_1=a$ und $t_2=b$ folgt.
:::

⁠**So liest man das:** $t_1$ und $t_2$ sind zwei Zeitpunkte derselben Kurve. Ist der Punkt zu diesen beiden Zeiten am selben Ort, dann muss es sich um Anfang und Ende handeln. Ein Punkt der Spur, der zu zwei verschiedenen Zeiten erreicht wird und nicht Anfangs- und Endpunkt zugleich ist, heißt ein __Doppelpunkt__. Eine Kurve, die geschlossen und einfach ist, heißt __einfach geschlossen__.

::::beispiel
Der Kreis $(\cos t,\sin t)$ auf $[0,2\pi]$ ist einfach geschlossen. Auf $[0,4\pi]$ ist er nicht einfach, denn $\gamma(0)=\gamma(2\pi)$, und $2\pi$ ist nicht das Ende des Intervalls. Die Acht $(\sin t,\sin2t)$ auf $[0,2\pi]$ ist im Nullpunkt bei $t=0$, $t=\pi$ und $t=2\pi$; das Paar $t_1=0$, $t_2=\pi$ zeigt, dass sie nicht einfach ist. Tabelle [1](#tab-1) fasst die Eigenschaften der vier Kurven zusammen.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Die Kurven aus Abb. [3](#abb-3) und der Viertelkreis $\kappa$.

| Kurve | regulär | geschlossen | einfach |
|---|---|---|---|
| Kreis $(\cos t,\sin t)$ auf $[0,2\pi]$ | ja | ja | ja |
| Kreis $(\cos t,\sin t)$ auf $[0,4\pi]$ | ja | ja | nein |
| Acht $(\sin t,\sin2t)$ auf $[0,2\pi]$ | ja | ja | nein |
| Spitze $(t^2,t^3)$ auf $[-1,1]$ | nein | nein | ja |
| Viertelkreis $\kappa(t)=(\cos t,\sin t)$ auf $[0,\pi/2]$ | ja | nein | ja |
::::

:::hintergrund Was bedeuten die beiden Parameterwerte in der Definition einer einfachen Kurve?
Die Definition vergleicht die Kurve mit sich selbst. $t_1$ und $t_2$ sind keine Parameter zweier verschiedener Kurven, sondern zwei Zeitpunkte auf derselben Uhr. Man fragt: Gibt es zwei verschiedene Zeitpunkte, zu denen der Punkt am selben Ort ist? Die Bedingung $t_1<t_2$ legt nur fest, welcher der beiden der frühere ist, damit man nicht jedes Paar doppelt zählt.

So prüft man es: Man setzt $\gamma(t_1)=\gamma(t_2)$ an, Komponente für Komponente, und sucht alle Lösungen mit $t_1<t_2$. Gibt es keine, ist die Kurve einfach und nicht geschlossen. Ist die einzige Lösung $t_1=a$, $t_2=b$, ist sie einfach geschlossen. Jede andere Lösung ist ein Doppelpunkt. Beim Kreis auf $[0,4\pi]$ führt die erste Komponente auf $\cos t_1=\cos t_2$, die zweite auf $\sin t_1=\sin t_2$; zusammen heißt das $t_2=t_1+2\pi k$ mit einer ganzen Zahl $k$. Mit $t_1=1$, $t_2=1+2\pi$ erhält man einen Doppelpunkt mitten in der Kurve.

Warum man einfache geschlossene Kurven hervorhebt: Eine einfach geschlossene Kurve in der Ebene teilt die Ebene in genau zwei Teile, ein beschränktes Inneres und ein unbeschränktes Äußeres. Das ist der Jordansche Kurvensatz, ein anschaulich klarer, aber schwer zu beweisender Satz. Deshalb kann eine solche Kurve den Rand einer Fläche bilden. Die Acht dagegen umschließt zwei Flächen, die sie in entgegengesetzter Richtung umläuft.
:::

⁠**Kurz gesagt:** Eine einfache Kurve ist zu verschiedenen Zeiten an verschiedenen Orten, höchstens Anfang und Ende dürfen zusammenfallen.

### Das Kurvenintegral

<span class="anker" id="stufe-1-8"></span>

Ein Feld schiebt ein Teilchen, das einen Weg entlangläuft, an jeder Stelle mehr oder weniger stark in Laufrichtung. Man möchte diese Wirkung über den ganzen Weg zu einer Zahl aufsummieren.

Man zerlegt den Weg in kleine Stücke mit den Wegvektoren $\Delta\boldsymbol{x}_k$ (Abb. [4](#abb-4)). Auf jedem Stück zählt nur der Anteil des Felds in Wegrichtung, und das misst das Skalarprodukt

$$\boldsymbol{F}\cdot\Delta\boldsymbol{x}_k=|\boldsymbol{F}|\,|\Delta\boldsymbol{x}_k|\cos\vartheta_k ,$$

wobei $\vartheta_k$ der Winkel zwischen $\boldsymbol{F}$ und $\Delta\boldsymbol{x}_k$ ist. Zeigt das Feld in Wegrichtung, zählt es voll; steht es quer dazu, zählt es nicht; zeigt es gegen den Weg, zählt es negativ. Teilt man das Zeitintervall in gleich lange Schritte $\Delta t$ und setzt $\boldsymbol{x}_k=\gamma(t_k)$, dann ist nach Unterabschnitt [1.1](#stufe-1-1) $\Delta\boldsymbol{x}_k=\gamma(t_k)-\gamma(t_{k-1})\approx\dot\gamma(t_{k-1})\,\Delta t$. Die Summe wird damit zu

$$\sum_k\boldsymbol{F}\bigl(\gamma(t_{k-1})\bigr)\cdot\Delta\boldsymbol{x}_k\approx\sum_k\boldsymbol{F}\bigl(\gamma(t_{k-1})\bigr)\cdot\dot\gamma(t_{k-1})\,\Delta t ,$$

und rechts steht eine Riemann-Summe ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). Für $\Delta t\to0$ wird sie zu einem Integral über $t$.

:::abbildung hm3/k3integral 4
Vier Stellen einer Kurve mit dem Wegstück $\Delta\boldsymbol{x}$ (grün) und dem Feld $\boldsymbol{F}$ (blau). Es zählt nur der Anteil von $\boldsymbol{F}$ in Wegrichtung (rot an der schrägen Stelle). Parallel zum Weg zählt das Feld voll, quer gar nicht, entgegen negativ.
:::

:::definition Definition 1.5 (Kurvenintegral)
<span class="anker" id="satz-1-5"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $\gamma\colon[a,b]\to\mathcal U$ eine regulär parametrisierte Kurve und $\boldsymbol{F}$ ein stetiges Vektorfeld auf $\mathcal U$. Das __Kurvenintegral__ von $\boldsymbol{F}$ längs $\gamma$ ist

<span class="anker" id="gl-1-2"></span>
$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}:=\int_a^b\boldsymbol{F}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)\,\mathrm{d} t . \tag{1.2}$$

Genauer ist bei einer Kurve mit den Stücken $[a_{k-1},a_k]$ wie in Unterabschnitt [1.4](#stufe-1-4)

$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}:=\sum_{k=1}^N\int_{a_{k-1}}^{a_k}\boldsymbol{F}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)\,\mathrm{d} t .$$

Die Definition gilt ebenso für Felder, die nur längs der Kurve erklärt sind, sofern $t\mapsto\boldsymbol{F}(\gamma(t))$ stetig ist. Formal schreibt man $\mathrm{d}\boldsymbol{x}=\dot\gamma(t)\,\mathrm{d} t$.
:::

⁠**So liest man das:** $\mathrm{d}\boldsymbol{x}$ ist ein kurzes Wegstück, also ein Vektor. Unter dem Integral steht ein Skalarprodukt, das Ergebnis ist deshalb eine reelle Zahl. Auf jedem Stück ist der Integrand $\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)$ stetig, an den Knickstellen darf er springen. Die Kurve muss in der Menge verlaufen, auf der das Feld erklärt ist; sonst fehlt an manchen Stellen der Pfeil.

::::beispiel
In der Ebene seien das *Drehfeld* $\boldsymbol V(x,y)=(-y,\,x)$ aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) und das *Strahlfeld* $\boldsymbol S(x,y)=(x,\,y)$ gegeben, dazu der Viertelkreis $\kappa(t)=(\cos t,\sin t)$, $t\in[0,\pi/2]$, und die Strecke $\sigma(t)=(1-t,\,t)$, $t\in[0,1]$. Beide Wege führen von $(1,0)$ nach $(0,1)$.

<ul>

<li>

Längs $\kappa$ ist $\boldsymbol V(\kappa(t))=(-\sin t,\cos t)=\dot\kappa(t)$, also $\boldsymbol V\cdot\dot\kappa=\sin^2t+\cos^2t=1$ und $\int_\kappa\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=\int_0^{\pi/2}1\,\mathrm{d} t=\frac\pi2$.

</li>

<li>

Längs $\sigma$ ist $\boldsymbol V(\sigma(t))=(-t,\,1-t)$ und $\dot\sigma=(-1,1)$, also $\boldsymbol V\cdot\dot\sigma=t+1-t=1$ und $\int_\sigma\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=\int_0^11\,\mathrm{d} t=1$.

</li>

<li>

Längs $\kappa$ ist $\boldsymbol S(\kappa(t))=(\cos t,\sin t)$, also $\boldsymbol S\cdot\dot\kappa=-\cos t\sin t+\sin t\cos t=0$ und $\int_\kappa\boldsymbol S\cdot\mathrm{d}\boldsymbol{x}=0$. Das Strahlfeld steht überall quer zum Kreis.

</li>

</ul>
::::

:::hintergrund Was das Kurvenintegral physikalisch bedeutet: Arbeit
Schiebt eine konstante Kraft $\boldsymbol{F}$ einen Körper geradlinig um die Strecke $\Delta\boldsymbol{x}$, verrichtet sie die Arbeit $W=\boldsymbol{F}\cdot\Delta\boldsymbol{x}=|\boldsymbol{F}|\,|\Delta\boldsymbol{x}|\cos\vartheta$, gemessen in $\mathrm N\cdot\mathrm m=\mathrm J$. Nur der Anteil der Kraft in Bewegungsrichtung leistet Arbeit. Ist die Kraft ein Kraftfeld und der Weg krumm, zerlegt man den Weg in kurze, fast gerade Stücke, auf denen die Kraft fast konstant ist. Die Summe der Teilarbeiten ist die Riemann-Summe von oben, und ihr Grenzwert ist das Kurvenintegral. Das Kurvenintegral eines Kraftfelds ist also die Arbeit, die das Feld an einem Teilchen längs $\gamma$ von $\gamma(a)$ nach $\gamma(b)$ verrichtet.

Ein Beispiel für eine Kraft, die nie Arbeit leistet: Auf eine Ladung $q$, die sich mit der Geschwindigkeit $\boldsymbol v$ durch ein Magnetfeld $\boldsymbol B$ bewegt, wirkt die Lorentzkraft $q\,\boldsymbol v\times\boldsymbol B$. Sie steht senkrecht auf $\boldsymbol v$, also auf der Bahn, und ihr Integrand $\boldsymbol{F}\cdot\dot\gamma$ ist überall null. Sie lenkt die Ladung ab, macht sie aber weder schneller noch langsamer.

Das Kurvenintegral beantwortet nur die Frage nach der Arbeit des Felds. Ob ein freies Teilchen den Weg $\gamma$ überhaupt von selbst nehmen würde, ist eine andere Frage. Läuft es einen vorgegebenen Weg, muss etwas anderes es führen, etwa eine Schiene, und deren Kräfte stehen nicht im Integral. Beim elektrischen Feld $\boldsymbol{E}$ ist $\int_\gamma\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}$ noch keine Arbeit, sondern eine Größe in $\frac{\mathrm V}{\mathrm m}\cdot\mathrm m=\mathrm V$; die Arbeit an einer Ladung $q$ ist $q\int_\gamma\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}$.
:::

⁠**Kurz gesagt:** Das Kurvenintegral summiert längs des Wegs das Skalarprodukt aus Feld und Tangentenvektor, also den Anteil des Felds in Laufrichtung.

### Linearität

<span class="anker" id="stufe-1-9"></span>

Setzt sich ein Feld aus zwei Feldern zusammen, möchte man die beiden Kurvenintegrale getrennt ausrechnen und addieren.

Für zwei stetige Vektorfelder $\boldsymbol{F}$ und $\boldsymbol G$ längs einer regulär parametrisierten Kurve $\gamma$ und Zahlen $\lambda,\mu\in\mathbb{R}$ gilt

<span class="anker" id="gl-1-3"></span>
$$\int_\gamma(\lambda\boldsymbol{F}+\mu\boldsymbol G)\cdot\mathrm{d}\boldsymbol{x}=\lambda\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}+\mu\int_\gamma\boldsymbol G\cdot\mathrm{d}\boldsymbol{x} . \tag{1.3}$$

Der Grund: Der Integrand $(\lambda\boldsymbol{F}+\mu\boldsymbol G)\cdot\dot\gamma=\lambda\,\boldsymbol{F}\cdot\dot\gamma+\mu\,\boldsymbol G\cdot\dot\gamma$ zerfällt nach den Regeln des Skalarprodukts, und das Integral über $t$ ist linear ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)).

::::beispiel
Längs des Viertelkreises $\kappa$ ist $\int_\kappa(\boldsymbol V+3\boldsymbol S)\cdot\mathrm{d}\boldsymbol{x}=\frac\pi2+3\cdot0=\frac\pi2$.
::::

⁠**Kurz gesagt:** Das Kurvenintegral ist linear im Feld.

### Umparametrisierung und Parameterinvarianz

<span class="anker" id="stufe-1-10"></span>

Denselben Weg kann man schnell oder langsam durchlaufen, gleichmäßig oder mit wechselndem Tempo. Das Kurvenintegral soll eine Eigenschaft des Wegs sein und nicht der Uhr, mit der man ihn abläuft.

Abb. [5](#abb-5) zeigt denselben Viertelkreis zweimal. Die Punkte gehören zu gleich großen Schritten im Parameter. Links liegen sie gleichmäßig, rechts am Anfang dicht und am Ende weit auseinander. Der zweite Läufer ist anfangs langsam und am Ende schnell, aber er besucht dieselben Punkte in derselben Reihenfolge.

:::abbildung hm3/k3invarianz 5
Derselbe Viertelkreis zweimal. Die Punkte gehören zu gleich großen Schritten im Parameter. Links gleichmäßig mit $\kappa(t)$, rechts mit $\kappa(\tau(u))$ für $\tau(u)=\frac\pi4(u^2+u)$: erst langsam, dann schnell. Weg und Kurvenintegral bleiben dieselben.
:::

Eine stetig differenzierbare Funktion $\tau\colon[u_0,u_1]\to[a,b]$ mit $\tau(u_0)=a$, $\tau(u_1)=b$ und $\tau'(u)>0$ für alle $u$ ist streng monoton wachsend (Unterabschnitt [1.2](#stufe-1-2)). Die Kurve $\gamma\circ\tau$, also $u\mapsto\gamma(\tau(u))$, durchläuft dann dieselben Punkte wie $\gamma$, in derselben Reihenfolge und mit einer anderen Uhr. Sie heißt eine __Umparametrisierung__ von $\gamma$. Nach der Kettenregel ist ihr Tangentenvektor $\frac{\mathrm{d}}{\mathrm{d} u}\gamma(\tau(u))=\dot\gamma(\tau(u))\,\tau'(u)$, und der ist nie null: Die Umparametrisierung ist wieder regulär parametrisiert.

:::satz Satz 1.6 (Invarianz unter Umparametrisierung)
<span class="anker" id="satz-1-6"></span>

Sei $\boldsymbol{F}$ ein stetiges Vektorfeld auf der offenen Menge $\mathcal U\subset\mathbb{R}^n$, $\gamma\colon[a,b]\to\mathcal U$ regulär parametrisiert und $\tau\colon[u_0,u_1]\to[a,b]$ stetig differenzierbar und streng monoton wachsend mit $\tau(u_0)=a$ und $\tau(u_1)=b$. Dann gilt

<span class="anker" id="gl-1-4"></span>
$$\int_{u_0}^{u_1}\boldsymbol{F}\bigl(\gamma(\tau(u))\bigr)\cdot\frac{\mathrm{d}}{\mathrm{d} u}\bigl(\gamma(\tau(u))\bigr)\,\mathrm{d} u=\int_a^b\boldsymbol{F}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)\,\mathrm{d} t, \qquad\text{also}\qquad \int_{\gamma\circ\tau}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x} . \tag{1.4}$$
:::

:::beweis Kettenregel und Substitution
Sei zunächst $\gamma$ stetig differenzierbar. Die Kettenregel gibt $\frac{\mathrm{d}}{\mathrm{d} u}\gamma(\tau(u))=\dot\gamma(\tau(u))\,\tau'(u)$. Damit wird die linke Seite zu

$$\int_{u_0}^{u_1}\boldsymbol{F}\bigl(\gamma(\tau(u))\bigr)\cdot\dot\gamma\bigl(\tau(u)\bigr)\,\tau'(u)\,\mathrm{d} u .$$

Das ist ein Integral der Form $\int_{u_0}^{u_1}g(\tau(u))\,\tau'(u)\,\mathrm{d} u$ mit der stetigen Funktion $g(t)=\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)$. Die Substitutionsregel aus [Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html) mit $t=\tau(u)$ und $\mathrm{d} t=\tau'(u)\,\mathrm{d} u$ macht daraus $\int_{\tau(u_0)}^{\tau(u_1)}g(t)\,\mathrm{d} t=\int_a^bg(t)\,\mathrm{d} t$, die rechte Seite. Hat $\gamma$ Knickstellen $a_k$, rechnet man auf jedem Stück $[\tau^{-1}(a_{k-1}),\tau^{-1}(a_k)]$ einzeln und addiert.
:::

Dass das Kurvenintegral bei einer Umparametrisierung gleich bleibt, heißt __Parameterinvarianz__.

::::beispiel
Der Viertelkreis $\kappa$ und das Drehfeld $\boldsymbol V$ ergaben $\frac\pi2$. Mit $\tau(u)=\frac\pi4(u^2+u)$ auf $[0,1]$ ist $\tau(0)=0$, $\tau(1)=\frac\pi2$ und $\tau'(u)=\frac\pi4(2u+1)>0$. Der Integrand wird $\boldsymbol V(\kappa(\tau))\cdot\dot\kappa(\tau)\,\tau'(u)=1\cdot\tau'(u)$, also

$$\int_{\kappa\circ\tau}\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=\int_0^1\tfrac\pi4(2u+1)\,\mathrm{d} u=\tfrac\pi4\,(1+1)=\tfrac\pi2 .$$
::::

:::hintergrund Was Parameterinvarianz bedeutet und warum das Tempo nicht zählt
Läuft man denselben Weg doppelt so schnell, ist der Tangentenvektor doppelt so lang und der Integrand $\boldsymbol{F}\cdot\dot\gamma$ doppelt so groß. Dafür dauert jedes Wegstück nur halb so lange. Im Produkt „Integrand mal Zeitschritt“ heben sich beide Faktoren auf. Das gilt auf jedem kurzen Stück einzeln, auch wenn das Tempo unterwegs schwankt: Der Beweis zeigt es mit dem Faktor $\tau'(u)$, den die Kettenregel in den Integranden bringt und den die Substitution $\mathrm{d} t=\tau'(u)\,\mathrm{d} u$ wieder verbraucht.

Noch klarer wird es an der Summe vom Anfang dieses Abschnitts. Die Summe $\sum_k\boldsymbol{F}(\boldsymbol{x}_{k-1})\cdot(\boldsymbol{x}_k-\boldsymbol{x}_{k-1})$ enthält nur Punkte des Wegs und ihre Reihenfolge. Wann der Läufer sie erreicht, kommt darin nicht vor. Physikalisch: Die Arbeit einer Kraft hängt vom zurückgelegten Weg ab, nicht davon, wie schnell man ihn zurücklegt.

Parameterinvarianz heißt deshalb nicht, dass jede Formel für dieselbe Punktmenge denselben Wert liefert. Es muss sich um eine Umparametrisierung handeln: dieselben Punkte, in derselben Reihenfolge, jeder Abschnitt gleich oft. Unterabschnitt [1.12](#stufe-1-12) zeigt, was sonst passiert.
:::

⁠**Kurz gesagt:** Das Kurvenintegral hängt nicht davon ab, mit welchem Tempo man den Weg durchläuft.

### Entgegengesetzt durchlaufene Kurven

<span class="anker" id="stufe-1-11"></span>

Was geschieht, wenn man denselben Weg rückwärts geht, also vom Ziel zum Start?

Beim Rückwärtslaufen besucht man dieselben Punkte in umgekehrter Reihenfolge. In der Summe vom Anfang des Unterabschnitts [1.8](#stufe-1-8) wird jedes Wegstück $\Delta\boldsymbol{x}_k$ zu $-\Delta\boldsymbol{x}_k$, während das Feld an jeder Stelle dasselbe bleibt (Abb. [4](#abb-4)). Jeder Summand wechselt also sein Vorzeichen.

:::definition Definition 1.7 (Entgegengesetzt durchlaufene Kurve)
<span class="anker" id="satz-1-7"></span>

Zu einer Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ heißt

$$\gamma^-(t):=\gamma(a+b-t),\qquad t\in[a,b],$$

die __entgegengesetzt durchlaufene Kurve__.
:::

Es ist $\gamma^-(a)=\gamma(b)$ und $\gamma^-(b)=\gamma(a)$. Man erhält $\gamma^-$ als $\gamma\circ\tau$ mit der streng monoton fallenden Funktion $\tau(t)=a+b-t$.

:::satz Satz 1.8 (Umkehr des Durchlaufsinns)
<span class="anker" id="satz-1-8"></span>

Für ein stetiges Vektorfeld $\boldsymbol{F}$ längs einer regulär parametrisierten Kurve $\gamma$ gilt

<span class="anker" id="gl-1-5"></span>
$$\int_{\gamma^-}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=-\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x} . \tag{1.5}$$
:::

:::beweis Substitution mit fallender Funktion
Es ist $\dot{\gamma^-}(t)=-\dot\gamma(a+b-t)$. Mit der Substitution $u=a+b-t$, $\mathrm{d} u=-\mathrm{d} t$, wandert die Grenze $t=a$ nach $u=b$ und $t=b$ nach $u=a$:

$$\int_a^b\boldsymbol{F}\bigl(\gamma(a+b-t)\bigr)\cdot\bigl(-\dot\gamma(a+b-t)\bigr)\,\mathrm{d} t=\int_b^a\boldsymbol{F}\bigl(\gamma(u)\bigr)\cdot\dot\gamma(u)\,\mathrm{d} u=-\int_a^b\boldsymbol{F}\bigl(\gamma(u)\bigr)\cdot\dot\gamma(u)\,\mathrm{d} u .$$

Bei Knickstellen rechnet man auf jedem Stück einzeln.
:::

::::beispiel
Der rückwärts durchlaufene Viertelkreis ist $\kappa^-(t)=\kappa(\frac\pi2-t)=(\sin t,\cos t)$ auf $[0,\frac\pi2]$. Es ist $\boldsymbol V(\kappa^-(t))=(-\cos t,\sin t)$ und $\dot{\kappa^-}(t)=(\cos t,-\sin t)$, also $\boldsymbol V\cdot\dot{\kappa^-}=-1$ und $\int_{\kappa^-}\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=-\frac\pi2$.
::::

:::hintergrund Warum die Richtung zählt, das Tempo aber nicht
Eine Umparametrisierung mit $\tau'>0$ dehnt oder staucht die Zeitachse; der Faktor $\tau'$ im Integranden und der Faktor $\mathrm{d} t=\tau'\,\mathrm{d} u$ heben sich auf. Bei einer fallenden Funktion ist $\tau'<0$. Der Faktor im Integranden behält sein Vorzeichen, aber die Grenzen des Integrals werden vertauscht, und $\int_b^a=-\int_a^b$ liefert das Minus. In der Summe vom Anfang ist es noch einfacher: Jedes Wegstück zeigt nach der Umkehr in die Gegenrichtung, und das Feld an derselben Stelle ist dasselbe. Physikalisch: Was ein Feld an Arbeit leistet, wenn man einen Körper bergab trägt, kostet es auf demselben Weg bergauf.
:::

⁠**Kurz gesagt:** Läuft man den Weg rückwärts, wechselt das Kurvenintegral sein Vorzeichen.

### Spur, reguläre Kurve und Orientierung

<span class="anker" id="stufe-1-12"></span>

Oft ist ein Weg nur als Punktmenge gegeben, etwa „der Kreis mit Radius $2$ um den Nullpunkt“ oder „die Strecke von $A$ nach $B$“. Man möchte über ihn integrieren, ohne eine bestimmte Formel auszeichnen zu müssen.

Die Punktmenge, die eine Kurve $\gamma\colon[a,b]\to\mathbb{R}^n$ durchläuft, also $\Gamma=\gamma([a,b])$, heißt die __Spur__ der Kurve. Eine Menge $\Gamma\subset\mathbb{R}^n$ heißt eine __reguläre Kurve__, wenn sie die Spur einer regulär parametrisierten und einfachen Kurve $\gamma$ ist. Für eine solche Parametrisierung schreibt man oft $\boldsymbol{x}=\boldsymbol{x}(t)$ statt $\gamma(t)$ und für ein Feld $\boldsymbol{F}$, das in einer Umgebung von $\Gamma$ stetig ist,

<span class="anker" id="gl-1-6"></span>
$$\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_a^b\boldsymbol{F}\bigl(\boldsymbol{x}(t)\bigr)\cdot\dot{\boldsymbol{x}}(t)\,\mathrm{d} t . \tag{1.6}$$

Zwei einfache reguläre Parametrisierungen derselben Spur gehen durch eine Umparametrisierung auseinander hervor, entweder mit einer wachsenden oder mit einer fallenden Funktion $\tau$. Nach den Sätzen [1.6](#satz-1-6) und [1.8](#satz-1-8) hängt der Wert von [(1.6)](#gl-1-6) deshalb nur noch davon ab, in welcher Richtung $\Gamma$ durchlaufen wird. Man ordnet einer regulären Kurve daher stets einen Durchlaufsinn zu, ihre __Orientierung__. Dieselbe Punktmenge mit dem entgegengesetzten Durchlaufsinn heißt $-\Gamma$.

::::beispiel
Sei $\Gamma$ der Halbkreis $\{(x,y):x^2+y^2=4,\ y\ge0\}$, orientiert von $(2,0)$ nach $(-2,0)$. Zwei Parametrisierungen sind $\boldsymbol{x}(t)=2(\cos t,\sin t)$ für $t\in[0,\pi]$ und $\boldsymbol{x}(u)=\bigl(-u,\sqrt{4-u^2}\bigr)$ für $u\in[-2,2]$. Die erste ist regulär. Die zweite beschreibt dieselbe Spur mit demselben Durchlaufsinn, ist an den Enden $u=\pm2$ aber nicht differenzierbar, denn dort wird die Steigung von $\sqrt{4-u^2}$ unendlich. Man nimmt also die erste. Für das Drehfeld ist $\boldsymbol V(\boldsymbol{x}(t))\cdot\dot{\boldsymbol{x}}(t)=2(-\sin t,\cos t)\cdot2(-\sin t,\cos t)=4$, also $\int_\Gamma\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=4\pi$ und $\int_{-\Gamma}\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=-4\pi$.
::::

:::hintergrund Liefert jede Parametrisierung derselben Spur denselben Wert?
Nein, nur eine, die jeden Punkt gleich oft und in derselben Richtung durchläuft. Der Kreis $(\cos t,\sin t)$ auf $[0,4\pi]$ hat dieselbe Spur wie auf $[0,2\pi]$, aber jeder Punkt wird zweimal erreicht. Für das Drehfeld ergibt er $\int_0^{4\pi}1\,\mathrm{d} t=4\pi$ statt $2\pi$. Das ist keine Umparametrisierung des einfachen Kreises: Eine streng monotone Funktion $\tau$ kann aus einem Umlauf nicht zwei machen. Deshalb verlangt die Definition der regulären Kurve eine *einfache* Parametrisierung; erst dann ist der Wert durch die Spur und die Orientierung festgelegt.

Warum gehen zwei einfache reguläre Parametrisierungen $\boldsymbol{x}$ und $\tilde{\boldsymbol{x}}$ derselben Spur durch eine Umparametrisierung auseinander hervor? Weil $\boldsymbol{x}$ einfach ist, gehört zu jedem Punkt der Spur genau ein Parameterwert, bei einer geschlossenen Kurve abgesehen vom Anfangs- und Endpunkt. Man setzt $\tau(u):=$ der Parameterwert $t$ mit $\boldsymbol{x}(t)=\tilde{\boldsymbol{x}}(u)$. Dass $\tau$ stetig differenzierbar ist und $\tau'\neq0$ gilt, folgt aus der Regularität beider Parametrisierungen; der genaue Beweis benutzt den Satz über die Umkehrfunktion und wird hier nicht ausgeführt.
:::

⁠**Kurz gesagt:** Eine reguläre Kurve ist eine Punktmenge mit einer einfachen regulären Parametrisierung. Ihr Kurvenintegral hängt nur von der Punktmenge und von der Orientierung ab.

### Der Anfangspunkt einer geschlossenen Kurve

<span class="anker" id="stufe-1-13"></span>

Bei einem Rundweg ist kein Punkt als Start ausgezeichnet. Ein Kreis lässt sich in $(1,0)$ beginnen oder in $(0,1)$.

:::satz Satz 1.9 (Beliebiger Anfangspunkt)
<span class="anker" id="satz-1-9"></span>

Ist $\Gamma$ eine geschlossene reguläre Kurve, dann hängt $\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ nicht davon ab, welcher Punkt von $\Gamma$ als Anfangs- und Endpunkt gewählt wird, solange die Orientierung erhalten bleibt.
:::

:::beweis Zwei Stücke, andere Reihenfolge
Sei $\boldsymbol{x}\colon[a,b]\to\mathbb{R}^n$ eine Parametrisierung mit $\boldsymbol{x}(a)=\boldsymbol{x}(b)$, und sei $\boldsymbol{x}(c)$ mit $a<c<b$ der neue Startpunkt. Die neue Parametrisierung durchläuft zuerst das Stück von $\boldsymbol{x}(c)$ bis $\boldsymbol{x}(b)$ und danach das Stück von $\boldsymbol{x}(a)=\boldsymbol{x}(b)$ bis $\boldsymbol{x}(c)$, etwa $\tilde{\boldsymbol{x}}(t)=\boldsymbol{x}(t)$ für $t\in[c,b]$ und $\tilde{\boldsymbol{x}}(t)=\boldsymbol{x}(t-b+a)$ für $t\in[b,b+c-a]$. Das zweite Stück ist eine Verschiebung der Zeitachse, also eine Umparametrisierung von $\boldsymbol{x}$ auf $[a,c]$. Beide Integrale bestehen damit aus denselben zwei Summanden $\int_a^c$ und $\int_c^b$, nur in anderer Reihenfolge.
:::

::::beispiel
Der Einheitskreis, in $(0,1)$ begonnen, ist $\tilde{\boldsymbol{x}}(t)=(\cos t,\sin t)$ für $t\in[\frac\pi2,\frac{5\pi}2]$. Für das Drehfeld ergibt er $\int_{\pi/2}^{5\pi/2}1\,\mathrm{d} t=2\pi$, wie mit dem Start in $(1,0)$.
::::

⁠**Kurz gesagt:** Bei einer geschlossenen Kurve ist es gleichgültig, wo man den Umlauf beginnt.

### Zusammengesetzte Kurven

<span class="anker" id="stufe-1-14"></span>

Viele Wege setzen sich aus Stücken zusammen: ein Streckenzug aus Strecken, der Rand eines Dreiecks aus drei Seiten. Man möchte über jedes Stück einzeln integrieren und addieren.

:::definition Definition 1.10 (Komposition)
<span class="anker" id="satz-1-10"></span>

Seien $\gamma_1\colon[a,b]\to\mathbb{R}^n$ und $\gamma_2\colon[c,d]\to\mathbb{R}^n$ regulär parametrisiert mit $\gamma_1(b)=\gamma_2(c)$. Die __Komposition__ $\gamma_1\oplus\gamma_2\colon[a,\,b+d-c]\to\mathbb{R}^n$ ist

<span class="anker" id="gl-1-7"></span>
$$(\gamma_1\oplus\gamma_2)(t):=\begin{cases}\gamma_1(t), & t\in[a,b],\\ \gamma_2(c-b+t), & t\in(b,\,b+d-c].\end{cases} \tag{1.7}$$
:::

⁠**So liest man das:** Zuerst läuft $\gamma_1$, danach $\gamma_2$, dessen Uhr so verschoben wird, dass es zur Zeit $b$ beginnt. Weil $\gamma_1$ dort endet, wo $\gamma_2$ beginnt, ist die Komposition stetig; die Stelle $t=b$ ist höchstens eine Knickstelle. Die Komposition ist also wieder regulär parametrisiert. Gehören zu $\gamma_1$ und $\gamma_2$ die regulären Kurven $\Gamma_1$ und $\Gamma_2$, schreibt man für die Kurve zu $\gamma_1\oplus\gamma_2$ kurz $\Gamma_1+\Gamma_2$ und für $\Gamma_1+(-\Gamma_2)$ kurz $\Gamma_1-\Gamma_2$. Die Kurvenintegrale sind additiv:

<span class="anker" id="gl-1-8"></span>
$$\int_{\Gamma_1\pm\Gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\Gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\pm\int_{\Gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x} . \tag{1.8}$$

Das folgt aus der stückweisen Definition [(1.2)](#gl-1-2) und für das Minuszeichen aus [(1.5)](#gl-1-5).

::::beispiel [Beispiel 1]
Der Streckenzug von $(1,0)$ über $(0,0)$ nach $(0,1)$ besteht aus $\Gamma_1$: $(1-t,0)$ und $\Gamma_2$: $(0,t)$, beide für $t\in[0,1]$. Für das Drehfeld ist auf $\Gamma_1$ der Integrand $(0,1-t)\cdot(-1,0)=0$, auf $\Gamma_2$ ist er $(-t,0)\cdot(0,1)=0$. Also ist $\int_{\Gamma_1+\Gamma_2}\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=0$: ein dritter Wert neben $\frac\pi2$ und $1$ für denselben Start und dasselbe Ziel.
::::

::::beispiel [Beispiel 2] Doppelpunkte zerlegen
Die Acht $\gamma(t)=(\sin t,\sin2t)$ auf $[0,2\pi]$ ist nicht einfach. Zerlegt man sie am Doppelpunkt, also bei $t=\pi$, entstehen die beiden Schleifen $\gamma$ auf $[0,\pi]$ und auf $[\pi,2\pi]$. Jede ist einfach geschlossen, und das Integral über die Acht ist die Summe der beiden Schleifenintegrale. Auf diese Weise zerlegt man die Kurven, mit denen man rechnet, an ihren Doppelpunkten in einfache Stücke. Doppelpunkte sind für das Integrieren deshalb keine wesentliche Einschränkung.
::::

⁠**Kurz gesagt:** Hängt man Kurven aneinander, addieren sich ihre Kurvenintegrale; ein rückwärts angehängtes Stück zählt negativ.

### Linienelement und Einheitstangentenvektor

<span class="anker" id="stufe-1-15"></span>

Im Kurvenintegral stecken zwei Dinge zugleich: wie lang ein Wegstück ist und in welche Richtung es zeigt. Man möchte beides trennen, um auch skalare Größen längs eines Wegs aufsummieren zu können, etwa die Masse eines gebogenen Drahts.

Ein kurzes Wegstück $\mathrm{d}\boldsymbol{x}=\dot{\boldsymbol{x}}(t)\,\mathrm{d} t$ hat die Länge $|\dot{\boldsymbol{x}}(t)|\,\mathrm{d} t$ und die Richtung $\dot{\boldsymbol{x}}(t)/|\dot{\boldsymbol{x}}(t)|$.

:::definition Definition 1.11 (Linienelement und Einheitstangentenvektor)
<span class="anker" id="satz-1-11"></span>

Sei $\boldsymbol{x}\colon[a,b]\to\mathbb{R}^n$ die Parametrisierung einer regulären Kurve $\Gamma$. Dann heißt

$$\mathrm{d} s=|\dot{\boldsymbol{x}}(t)|\,\mathrm{d} t$$

das __Linienelement__ von $\Gamma$. Der Vektor

$$\boldsymbol{t}\bigl(\boldsymbol{x}(t)\bigr)=\frac{\dot{\boldsymbol{x}}(t)}{|\dot{\boldsymbol{x}}(t)|}$$

heißt der __orientierte Einheitstangentenvektor__. An Knickstellen setzt man darin die rechtsseitige Ableitung ein.
:::

⁠**So liest man das:** $\mathrm{d} s$ ist die Länge eines kurzen Wegstücks, eine Zahl ohne Richtung. $\boldsymbol{t}$ hat die Länge $1$ und zeigt in Laufrichtung; er ist nur dank der Regularität erklärt. Längs $\Gamma$ ist $\boldsymbol{t}$ ein stückweise stetiges Vektorfeld, an Knickstellen springt es. Mit beiden zusammen ist $\mathrm{d}\boldsymbol{x}=\dot{\boldsymbol{x}}\,\mathrm{d} t=\boldsymbol{t}\,\mathrm{d} s$. Deshalb heißt $\mathrm{d}\boldsymbol{x}$ auch das __orientierte Linienelement__.

Für eine stetige skalare Funktion $f$ längs $\Gamma$ heißt

<span class="anker" id="gl-1-9"></span>
$$\int_\Gamma f\,\mathrm{d} s:=\int_a^bf\bigl(\boldsymbol{x}(t)\bigr)\,|\dot{\boldsymbol{x}}(t)|\,\mathrm{d} t \tag{1.9}$$

das __Integral über die Bogenlänge__. Weil $\boldsymbol{F}\cdot\dot{\boldsymbol{x}}=(\boldsymbol{F}\cdot\boldsymbol{t})\,|\dot{\boldsymbol{x}}|$ ist, schreibt sich das Kurvenintegral damit als

<span class="anker" id="gl-1-10"></span>
$$\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_\Gamma\boldsymbol{F}\cdot\boldsymbol{t}\;\mathrm{d} s . \tag{1.10}$$

Rechts wird der Tangentialanteil $\boldsymbol{F}\cdot\boldsymbol{t}$ des Felds mit der Weglänge gewichtet. Das Integral über die Bogenlänge hängt nicht von der Orientierung ab: Bei einer fallenden Umparametrisierung wird $|\frac{\mathrm{d}}{\mathrm{d} u}\boldsymbol{x}(\tau(u))|=|\dot{\boldsymbol{x}}(\tau(u))|\,|\tau'(u)|$ mit $|\tau'|=-\tau'$, und dieses zusätzliche Minus hebt das Minus aus den vertauschten Grenzen auf.

::::beispiel
Für den Viertelkreis $\kappa$ ist $|\dot\kappa|=1$, also $\mathrm{d} s=\mathrm{d} t$ und $\boldsymbol{t}=(-\sin t,\cos t)$. Das Drehfeld hat dort den Tangentialanteil $\boldsymbol V\cdot\boldsymbol{t}=1$, und [(1.10)](#gl-1-10) gibt $\int_\kappa1\,\mathrm{d} s=\frac\pi2$. Für $f(x,y)=x$ ist $\int_\kappa x\,\mathrm{d} s=\int_0^{\pi/2}\cos t\,\mathrm{d} t=1$. Ein Draht in Form dieses Viertelkreises mit der Massenbelegung $x$ Kilogramm pro Meter hätte also die Masse $1\,\mathrm{kg}$, wenn die Längen in Metern gemessen werden.
::::

⁠**Kurz gesagt:** $\mathrm{d} s=|\dot{\boldsymbol{x}}|\,\mathrm{d} t$ ist die Länge eines Wegstücks, $\boldsymbol{t}$ seine Richtung. Das Kurvenintegral ist der Tangentialanteil des Felds, über die Bogenlänge integriert.

### Die Kurvenlänge

<span class="anker" id="stufe-1-16"></span>

Wie lang ist ein krummer Weg? Mit einem Lineal misst man nur gerade Stücke.

Man setzt Punkte auf die Kurve und verbindet sie geradlinig. So entsteht ein Streckenzug, den man mit dem Lineal messen kann (Abb. [6](#abb-6)). Seine Strecken heißen __Sehnen__. Je dichter die Punkte liegen, desto besser schmiegt sich der Streckenzug an die Kurve. Für einen kleinen Zeitschritt $\Delta t$ ist eine Sehne fast „Tempo mal Zeit“: $|\boldsymbol{x}(t+\Delta t)-\boldsymbol{x}(t)|\approx|\dot{\boldsymbol{x}}(t)|\,\Delta t$. Die Summe aller Sehnen ist also fast eine Riemann-Summe von $|\dot{\boldsymbol{x}}|$.

:::abbildung hm3/k3sehnen 6
Der Viertelkreis mit dem Radius $2$ hat die Länge $\pi\approx3{,}142$. Der rote Streckenzug aus zwei Sehnen hat die Länge $8\sin\frac\pi8\approx3{,}061$, der grüne gestrichelte aus vier Sehnen $16\sin\frac\pi{16}\approx3{,}121$. Mit jeder Verfeinerung kommt der Streckenzug der Kurvenlänge näher.
:::

:::definition Definition 1.12 (Kurvenlänge)
<span class="anker" id="satz-1-12"></span>

Sei $\boldsymbol{x}\colon[a,b]\to\mathbb{R}^n$ die Parametrisierung einer regulären Kurve $\Gamma$. Die __Kurvenlänge__ von $\Gamma$ ist

<span class="anker" id="gl-1-11"></span>
$$\mathcal L(\Gamma)=\int_a^b|\dot{\boldsymbol{x}}(t)|\,\mathrm{d} t=\int_\Gamma\mathrm{d} s . \tag{1.11}$$
:::

⁠**So liest man das:** Tempo mal Zeit, summiert. Ausgeschrieben ist $|\dot{\boldsymbol{x}}(t)|=\sqrt{\dot x_1(t)^2+\dots+\dot x_n(t)^2}$. Die Länge ist das Integral über die Bogenlänge der Funktion $f=1$. Nach Unterabschnitt [1.15](#stufe-1-15) hängt sie weder von der gewählten Parametrisierung noch von der Orientierung ab. Für eine regulär parametrisierte Kurve $\gamma$, die nicht einfach sein muss, schreibt man ebenso $\mathcal L(\gamma)=\int_a^b|\dot\gamma(t)|\,\mathrm{d} t$; dann zählt jeder mehrfach durchlaufene Abschnitt mehrfach.

::::beispiel [Beispiel 1]
Der Kreis $\boldsymbol{x}(t)=R(\cos t,\sin t)$, $t\in[0,2\pi]$, hat das Tempo $|\dot{\boldsymbol{x}}|=R$, also $\mathcal L=\int_0^{2\pi}R\,\mathrm{d} t=2\pi R$.
::::

::::beispiel [Beispiel 2]
Die Schraubenlinie $\boldsymbol{x}(t)=(\cos t,\sin t,t)$, $t\in[0,2\pi]$, hat $|\dot{\boldsymbol{x}}|=\sqrt{\sin^2t+\cos^2t+1}=\sqrt2$, also $\mathcal L=2\sqrt2\,\pi\approx8{,}886$. Eine Windung der Schraube ist um den Faktor $\sqrt2$ länger als der Kreis, auf den sie von oben projiziert wird.
::::

::::beispiel [Beispiel 3] Graphen
Der Graph einer stetig differenzierbaren Funktion $y=f(x)$, $x\in[a,b]$, ist die Kurve $\boldsymbol{x}(x)=(x,f(x))$ mit $\dot{\boldsymbol{x}}=(1,f'(x))$. Sie ist regulär, und [(1.11)](#gl-1-11) wird

<span class="anker" id="gl-1-12"></span>
$$\mathcal L=\int_a^b\sqrt{1+f'(x)^2}\,\mathrm{d} x . \tag{1.12}$$

Für die Gerade $f(x)=mx$ ergibt das $(b-a)\sqrt{1+m^2}$, den Satz des Pythagoras.
::::

:::hintergrund Warum die Länge das Integral von $|\dot{\boldsymbol{x}}|$ ist
Die Länge eines krummen Wegs erklärt man ursprünglich über Streckenzüge. Zu einer Zerlegung $a=t_0<t_1<\dots<t_N=b$ gehört der Streckenzug durch die Punkte $\boldsymbol{x}(t_0),\dots,\boldsymbol{x}(t_N)$ mit der Länge $\sum_k|\boldsymbol{x}(t_k)-\boldsymbol{x}(t_{k-1})|$. Die Länge der Kurve ist die kleinste Zahl, die von keinem solchen Streckenzug übertroffen wird. Dass diese Zahl für eine stückweise stetig differenzierbare Kurve gleich $\int_a^b|\dot{\boldsymbol{x}}|\,\mathrm{d} t$ ist, folgt aus zwei Abschätzungen.

⁠*Keine Sehne ist länger als ihr Bogen.* Nach dem Hauptsatz, Komponente für Komponente angewendet, ist $\boldsymbol{x}(t_k)-\boldsymbol{x}(t_{k-1})=\int_{t_{k-1}}^{t_k}\dot{\boldsymbol{x}}(t)\,\mathrm{d} t$. Der Betrag eines Integrals von Vektoren ist höchstens das Integral der Beträge. Dazu setzt man $\boldsymbol w=\int\dot{\boldsymbol{x}}\,\mathrm{d} t$; dann ist $|\boldsymbol w|^2=\int\boldsymbol w\cdot\dot{\boldsymbol{x}}\,\mathrm{d} t\le|\boldsymbol w|\int|\dot{\boldsymbol{x}}|\,\mathrm{d} t$ nach [(1.1)](#gl-1-1). Also ist jede Sehne höchstens $\int_{t_{k-1}}^{t_k}|\dot{\boldsymbol{x}}|\,\mathrm{d} t$ lang, und jeder Streckenzug ist höchstens $\int_a^b|\dot{\boldsymbol{x}}|\,\mathrm{d} t$ lang.

⁠*Auf kurzen Stücken ist die Sehne fast so lang wie der Bogen.* Auf jedem glatten Stück ist $\dot{\boldsymbol{x}}$ stetig auf einem abgeschlossenen Intervall, also gleichmäßig stetig ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). Zu $\varepsilon>0$ gibt es daher eine Schrittweite, ab der sich $\dot{\boldsymbol{x}}$ innerhalb jedes Teilintervalls um weniger als $\varepsilon$ ändert. Dann ist der Bogen über $[t_{k-1},t_k]$ höchstens $(|\dot{\boldsymbol{x}}(t_{k-1})|+\varepsilon)\,\Delta t_k$ lang, und die Sehne ist mindestens $|\dot{\boldsymbol{x}}(t_{k-1})|\,\Delta t_k-\varepsilon\,\Delta t_k$ lang, weil $\boldsymbol{x}(t_k)-\boldsymbol{x}(t_{k-1})$ von $\dot{\boldsymbol{x}}(t_{k-1})\,\Delta t_k$ um höchstens $\varepsilon\,\Delta t_k$ abweicht. Summiert: Der Streckenzug ist um höchstens $2\varepsilon\,(b-a)$ kürzer als das Integral.

Beides zusammen: Feine Streckenzüge kommen dem Integral beliebig nahe, und keiner übertrifft es. Der Mechanismus ist anschaulich: Eine Gerade ist die kürzeste Verbindung, deshalb unterschätzt jede Sehne; und auf kurzen Stücken dreht der Tangentenvektor kaum, deshalb ist der Fehler klein. Ohne Ableitung kann das scheitern: Der Graph von $x\sin\frac1x$ auf $(0,1]$ ist stetig, aber jeder Streckenzug lässt sich durch weitere Punkte nahe bei $0$ beliebig verlängern, die Länge ist unendlich.
:::

:::hintergrund Wie berechnet man die Länge einer Kurve, die nicht als Parametrisierung gegeben ist?
Man sucht zuerst eine reguläre Parametrisierung, denn die Formel [(1.11)](#gl-1-11) braucht eine. Danach sind es drei Schritte: ableiten, den Betrag des Tangentenvektors bilden und integrieren.

<ul>

<li>

⁠*Als Graph* $y=f(x)$: Man nimmt $x$ als Parameter und erhält [(1.12)](#gl-1-12).

</li>

<li>

⁠*In Polarform* $r=g(\varphi)$, also mit dem Abstand $r$ vom Nullpunkt als Funktion des Winkels $\varphi$: Man nimmt $\boldsymbol{x}(\varphi)=g(\varphi)(\cos\varphi,\sin\varphi)$. Es ist $\dot{\boldsymbol{x}}=g'(\cos\varphi,\sin\varphi)+g(-\sin\varphi,\cos\varphi)$, und weil die beiden Klammern senkrecht aufeinander stehen und die Länge $1$ haben, folgt $|\dot{\boldsymbol{x}}|=\sqrt{g(\varphi)^2+g'(\varphi)^2}$.

</li>

<li>

⁠*Als Schnitt zweier Flächen*, etwa eines Zylinders $x^2+y^2=1$ mit einer Ebene $z=y$: Man parametrisiert eine Gleichung und setzt in die andere ein, hier $\boldsymbol{x}(t)=(\cos t,\sin t,\sin t)$.

</li>

</ul>

Bleibt eine Wurzel stehen, die sich nicht vereinfacht, hat der Integrand oft keine Stammfunktion in geschlossener Form. Dann rechnet man numerisch.
:::

⁠**Kurz gesagt:** Die Länge einer Kurve ist das Integral ihres Tempos, $\mathcal L=\int_a^b|\dot{\boldsymbol{x}}|\,\mathrm{d} t$. Sie ist der Grenzwert der Längen immer feinerer Streckenzüge.

### Parametrisierung nach der Bogenlänge

<span class="anker" id="stufe-1-17"></span>

Unter allen Uhren, mit denen man eine Kurve ablesen kann, ist eine besonders natürlich: die, die den zurückgelegten Weg anzeigt. Mit ihr läuft der Punkt immer mit dem Tempo $1$.

Sei $\gamma\colon[a,b]\to\mathbb{R}^n$ regulär parametrisiert. Die Funktion

<span class="anker" id="gl-1-13"></span>
$$s(t):=\int_a^t|\dot\gamma(w)|\,\mathrm{d} w,\qquad t\in[a,b], \tag{1.13}$$

gibt an, welchen Weg der Punkt bis zur Zeit $t$ zurückgelegt hat. Sie heißt die __Bogenlängenfunktion__ von $\gamma$. Nach dem Hauptsatz ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) ist sie auf jedem glatten Stück stetig differenzierbar mit

$$\frac{\mathrm{d} s}{\mathrm{d} t}=|\dot\gamma(t)|>0 .$$

Also ist $s$ streng monoton wachsend und bildet $[a,b]$ auf $[0,\mathcal L]$ ab, mit der Länge $\mathcal L=s(b)$. Nach Unterabschnitt [1.2](#stufe-1-2) hat $s$ eine Umkehrfunktion $t(s)$ mit der Ableitung $\frac{\mathrm{d} t}{\mathrm{d} s}=1/|\dot\gamma(t)|$.

:::definition Definition 1.13 (Parametrisierung nach der Bogenlänge)
<span class="anker" id="satz-1-13"></span>

Die Kurve $\tilde\gamma\colon[0,\mathcal L]\to\mathbb{R}^n$, $\tilde\gamma(s):=\gamma\bigl(t(s)\bigr)$, heißt die __Parametrisierung nach der Bogenlänge__.
:::

Nach der Kettenregel ist

$$\Bigl|\frac{\mathrm{d}\tilde\gamma}{\mathrm{d} s}\Bigr|=\Bigl|\dot\gamma\bigl(t(s)\bigr)\Bigr|\cdot\Bigl|\frac{\mathrm{d} t}{\mathrm{d} s}\Bigr|=\frac{|\dot\gamma(t)|}{|\dot\gamma(t)|}=1 .$$

Der Tangentenvektor von $\tilde\gamma$ ist also der Einheitstangentenvektor $\boldsymbol{t}$, und das Linienelement ist wörtlich $\mathrm{d} s$. Das erklärt die Schreibweise $\int_\Gamma f\,\mathrm{d} s$: Mit dieser Parametrisierung ist es das gewöhnliche Integral $\int_0^{\mathcal L}f(\tilde\gamma(s))\,\mathrm{d} s$.

::::beispiel
Der Kreis $\gamma(t)=R(\cos t,\sin t)$ hat $|\dot\gamma|=R$, also $s(t)=Rt$ und $t(s)=s/R$. Die Parametrisierung nach der Bogenlänge ist

$$\tilde\gamma(s)=R\Bigl(\cos\frac sR,\ \sin\frac sR\Bigr),\qquad s\in[0,2\pi R],$$

mit $\frac{\mathrm{d}\tilde\gamma}{\mathrm{d} s}=\bigl(-\sin\frac sR,\cos\frac sR\bigr)$ der Länge $1$. Für die Schraubenlinie aus Unterabschnitt [1.16](#stufe-1-16) ist $s(t)=\sqrt2\,t$ und $\tilde\gamma(s)=\bigl(\cos\frac s{\sqrt2},\sin\frac s{\sqrt2},\frac s{\sqrt2}\bigr)$.
::::

⁠**Kurz gesagt:** Nach der Bogenlänge parametrisiert, läuft jede reguläre Kurve mit dem Tempo $1$, und der Parameter ist der zurückgelegte Weg.

### Die Standardabschätzung

<span class="anker" id="stufe-1-18"></span>

Oft genügt es zu wissen, dass ein Kurvenintegral klein ist, ohne es auszurechnen. Eine einfache Schranke liefern die Länge des Wegs und die größte Länge des Felds auf ihm.

:::satz Satz 1.14 (Standardabschätzung)
<span class="anker" id="satz-1-14"></span>

Für ein stetiges Vektorfeld $\boldsymbol{F}$ längs einer regulären Kurve $\Gamma$ gilt

<span class="anker" id="gl-1-14"></span>
$$\Bigl|\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\Bigr|\le\sup_{\boldsymbol{x}\in\Gamma}|\boldsymbol{F}(\boldsymbol{x})|\;\mathcal L(\Gamma). \tag{1.14}$$
:::

:::beweis Dreiecksungleichung und Cauchy-Schwarz
Nach [(1.10)](#gl-1-10) und mit $|\int g\,\mathrm{d} t|\le\int|g|\,\mathrm{d} t$ ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) ist

$$\Bigl|\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\Bigr|=\Bigl|\int_\Gamma\boldsymbol{F}\cdot\boldsymbol{t}\,\mathrm{d} s\Bigr|\le\int_\Gamma|\boldsymbol{F}\cdot\boldsymbol{t}|\,\mathrm{d} s\le\int_\Gamma|\boldsymbol{F}|\,|\boldsymbol{t}|\,\mathrm{d} s=\int_\Gamma|\boldsymbol{F}|\,\mathrm{d} s\le\sup_\Gamma|\boldsymbol{F}|\int_\Gamma\mathrm{d} s .$$

Im zweiten Schritt steht die Cauchy-Schwarz-Ungleichung [(1.1)](#gl-1-1), im dritten $|\boldsymbol{t}|=1$, im letzten die Monotonie des Integrals. Das letzte Integral ist $\mathcal L(\Gamma)$.
:::

⁠**So liest man das:** Der Betrag des Kurvenintegrals ist höchstens „größte Feldstärke mal Weglänge“. Gleichheit gilt, wenn das Feld überall in Laufrichtung zeigt und überall gleich lang ist, denn dann sind alle drei Ungleichungen Gleichungen.

::::beispiel
Für das Drehfeld auf dem Viertelkreis ist $|\boldsymbol V|=1$ und $\mathcal L=\frac\pi2$; die Schranke $\frac\pi2$ wird erreicht, weil $\boldsymbol V$ dort parallel zum Weg läuft. Auf der Strecke $\sigma$ ist $|\boldsymbol V(\sigma(t))|^2=t^2+(1-t)^2\le1$ und $\mathcal L(\sigma)=\sqrt2$. Die Schranke $\sqrt2\approx1{,}41$ liegt über dem wahren Wert $1$, denn auf der Strecke steht das Feld schräg zum Weg und ist in der Mitte kürzer.
::::

:::hintergrund Wozu eine Abschätzung, wenn man das Integral ausrechnen kann?
Oft kann man es nicht: Der Integrand hat keine geschlossene Stammfunktion, oder das Feld ist nur ungefähr bekannt, etwa aus einer Messung mit einer Fehlerschranke. Die Abschätzung braucht nur zwei Zahlen. Sie ist außerdem das Werkzeug, um zu zeigen, dass ein Integral gegen null geht. Schrumpft der Weg, etwa ein Kreis mit dem Radius $R\to0$ um einen Punkt, an dem das Feld beschränkt bleibt, dann geht $\mathcal L=2\pi R$ gegen null und mit ihm das Integral. Der Mechanismus ist derselbe wie bei $|\int_a^bg\,\mathrm{d} t|\le(b-a)\max|g|$: Eine Summe ist höchstens so groß wie die Zahl ihrer Teile mal ihr größter Summand.
:::

⁠**Kurz gesagt:** Ein Kurvenintegral ist betragsmäßig höchstens die größte Feldlänge auf dem Weg mal die Weglänge.

### Aufgaben

<span class="anker" id="stufe-1-19"></span>

:::aufgabe Aufgabe 1 ★ Kurven einordnen
<span class="anker" id="aufg-1"></span>

Sind die folgenden Kurven regulär parametrisiert, geschlossen, einfach?

<ol class="al">

<li>

$(2\cos t,\,\sin t)$ auf $[0,2\pi]$

</li>

<li>

$(t^2-4,\,t^3-4t)$ auf $[-3,3]$

</li>

<li>

$(\cos t,\,\sin t,\,t)$ auf $[0,4\pi]$

</li>

<li>

$(\cos^3t,\,\sin^3t)$ auf $[0,2\pi]$

</li>

<li>

$(t,\,|t|)$ auf $[-1,1]$

</li>

<li>

$(t^3,\,t^3)$ auf $[-1,1]$. Gibt es eine reguläre Parametrisierung derselben Spur?

</li>

</ol>

Berechne außerdem die Längen der Kurven aus (c) und (d).

:::loesung
(a) $\dot\gamma=(-2\sin t,\cos t)\neq0$: regulär, geschlossen, einfach (eine Ellipse). (b) $\dot\gamma=(2t,3t^2-4)$: Die erste Komponente ist nur bei $t=0$ null, dort ist die zweite $-4$. Also regulär. $\gamma(-3)=(5,-15)\neq\gamma(3)=(5,15)$: nicht geschlossen. $\gamma(-2)=\gamma(2)=(0,0)$: nicht einfach. (c) $|\dot\gamma|=\sqrt2$: regulär, nicht geschlossen, einfach, weil die dritte Komponente wächst. Länge $4\pi\sqrt2$. (d) $\dot\gamma=3\sin t\cos t\,(-\cos t,\sin t)$ ist bei $t=k\pi/2$ null: nicht regulär, dort sitzen vier Spitzen. Geschlossen und einfach. Länge: $|\dot\gamma|=3|\sin t\cos t|$, also $4\int_0^{\pi/2}3\sin t\cos t\,\mathrm{d} t=6$. (e) Knick bei $t=0$ mit den einseitigen Ableitungen $(1,-1)$ und $(1,1)$: regulär, nicht geschlossen, einfach.
:::
:::

:::aufgabe Aufgabe 2 ★ Zwei Wege, zwei Werte
<span class="anker" id="aufg-2"></span>

Sei $\boldsymbol{F}(x,y)=(y,\,x^2)$.

<ol class="al">

<li>

Berechne das Kurvenintegral längs der Strecke von $(0,0)$ nach $(3,4)$.

</li>

<li>

Berechne es längs des Streckenzugs $(0,0)\to(3,0)\to(3,4)$, als Komposition zweier Strecken.

</li>

<li>

Prüfe (a) mit der Standardabschätzung.

</li>

</ol>

:::loesung
(a) $\gamma(t)=(3t,4t)$, $0\le t\le1$: $\boldsymbol{F}\cdot\dot\gamma=(4t,9t^2)\cdot(3,4)=12t+36t^2$, das Integral ist $6+12=18$. (b) Auf dem ersten Stück ist $y=0$ und $\mathrm{d} y=0$, also null. Auf dem zweiten ist $x=3$, $\mathrm{d} x=0$: $\int_0^49\,\mathrm{d} y=36$. Die Komposition ergibt $36$, also einen anderen Wert als in (a). (c) Auf der Strecke ist $|\boldsymbol{F}|^2=16t^2+81t^4\le97$ und $\mathcal L=5$, also $18\le5\sqrt{97}\approx49{,}2$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Dasselbe Integral, verschiedene Beschreibungen
<span class="anker" id="aufg-3"></span>

Sei $\boldsymbol{F}(x,y)=(y,\,2x)$ und $\gamma(t)=(t,t^2)$, $t\in[0,1]$.

<ol class="al">

<li>

Berechne $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ direkt und mit der Umparametrisierung $\tau(u)=\frac{u^2+u}2$, $u\in[0,1]$.

</li>

<li>

Was ergibt sich für $\gamma_1(t)=(1-t,(1-t)^2)$, $t\in[0,1]$? Welches $\tau$ gehört dazu?

</li>

<li>

Berechne $\int_\gamma x\,\mathrm{d} s$ und $\int_{\gamma_1}x\,\mathrm{d} s$. Warum kippt hier kein Vorzeichen?

</li>

<li>

Sei $\tau(u)=\sin^2u$ auf $[0,\pi]$. Die Kurve $\gamma\circ\tau$ läuft von $(0,0)$ nach $(1,1)$ und wieder zurück. Berechne $\int_0^\pi\boldsymbol{F}(\gamma(\tau(u)))\cdot\frac{\mathrm{d}}{\mathrm{d} u}\gamma(\tau(u))\,\mathrm{d} u$ und $\int_0^\pi|\frac{\mathrm{d}}{\mathrm{d} u}\gamma(\tau(u))|\,\mathrm{d} u$ und erkläre die beiden Ergebnisse.

</li>

</ol>

:::loesung
(a) $\boldsymbol{F}\cdot\dot\gamma=(t^2,2t)\cdot(1,2t)=5t^2$, das Integral ist $\frac53$. Mit $\tilde\gamma(u)=(u^3,u^6)$ ist $(u^6,2u^3)\cdot(3u^2,6u^5)=15u^8$, das Integral ist wieder $\frac53$. (b) $\gamma_1=\gamma\circ\tau$ mit $\tau(t)=1-t$, fallend. Also $-\frac53$. (c) $\int_\gamma x\,\mathrm{d} s=\int_0^1t\sqrt{1+4t^2}\,\mathrm{d} t=\bigl[\frac1{12}(1+4t^2)^{3/2}\bigr]_0^1=\frac{5\sqrt5-1}{12}\approx0{,}848$. Für $\gamma_1$ kommt mit $w=1-t$ dasselbe heraus. In $|\dot\gamma|$ geht die Richtung nicht ein.
:::
:::

:::aufgabe Aufgabe 4 ★★ Längen und Bogenlänge
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Berechne die Länge des Graphen von $f(x)=\frac23x^{3/2}$ für $x\in[0,3]$.

</li>

<li>

Parametrisiere die Schraubenlinie $\gamma(t)=(3\cos t,\,3\sin t,\,4t)$, $t\in[0,2\pi]$, nach der Bogenlänge und prüfe, dass der neue Tangentenvektor die Länge $1$ hat.

</li>

<li>

Berechne die Länge der Kurve in Polarform $r=\mathrm{e}^{\varphi}$ für $\varphi\in[0,2\pi]$.

</li>

</ol>

:::
