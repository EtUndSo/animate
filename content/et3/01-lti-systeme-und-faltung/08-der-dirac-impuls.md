---
title: Stufe 7: Der Dirac-Impuls
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210800
summary: Der Dirac-Impuls ist das Grenzobjekt aus Stufe 4.
tags: Distribution, ideales Laufzeitglied, verallgemeinerte Differentiation
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Der Dirac-Impuls ist das Grenzobjekt aus Stufe [4](das-faltungsintegral.html#stufe-4). Er ist keine gewöhnliche Funktion. Alle seine Eigenschaften folgen daraus, dass er nur über seine Fläche wirkt.
:::

**Was $\delta$ ist und was nicht.** Die Rechtecke $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ werden für $T_0\to0$ immer schmaler und höher, ihre Fläche bleibt 1 (Abb. [8](#abb-8)). Einen Grenzwert im Sinne gewöhnlicher Funktionen gibt es nicht: Eine Funktion, die überall außer in einem Punkt null ist, hat die Fläche null, egal welchen Wert sie in diesem Punkt hat. $\delta(t)$ ist deshalb eine __Distribution__: ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist, nämlich durch [(4.1)](das-faltungsintegral.html#gl-4-1). Gezeichnet wird es als Pfeil, dessen Höhe das Gewicht (die Fläche) angibt.

:::abbildung et3/k1dirac 8
Links: Rechtecke der Fläche 1, immer schmaler und höher. Rechts: das Symbol des Grenzobjekts. Die Pfeilhöhe ist das Gewicht, nicht der Funktionswert.
:::

:::satz Satz 7.1 (Eigenschaften des Dirac-Impulses)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Gewicht:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Sieb:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Fläche:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Dehnung:} && \delta(bt)=\frac{1}{|b|}\,\delta(t)\quad(b\neq0),\qquad \delta(-t)=\delta(t),\\ &\text{Verschiebung:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**So liest man das:** Das Produkt $s(t)\,\delta(t-T)$ kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$. Ein gestauchter Impuls $\delta(bt)$ ist zwar genauso „unendlich hoch“, hat aber nur noch die Fläche $1/|b|$. Ein System mit $h(t)=\delta(t-t_0)$ verzögert jedes Signal um $t_0$, es heißt __ideales Laufzeitglied__. Und weil der Sprung das laufende Integral des Stoßes ist, darf man Funktionen mit Sprungstellen ableiten: Ein Sprung der Höhe $A$ wird zu $A\,\delta$. Das heißt __verallgemeinerte Differentiation__. Vorsicht: Viele Operationen, etwa das Quadrieren $\delta^2$, sind für Dirac-Impulse nicht definiert.

:::herleitung Dehnung und Sieb-Produkt
⁠**Dehnung.** Für $b>0$ mit $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

Für $b<0$ kehrt die Substitution die Integrationsrichtung um, es kommt $-\frac1b=\frac{1}{|b|}$ heraus. Also wirkt $\delta(bt)$ wie $\frac1{|b|}\delta(t)$. Mit $b=-1$ folgt die Symmetrie $\delta(-t)=\delta(t)$.

⁠**Sieb-Produkt.** Faltet man $s(t)\delta(t)$ mit einem beliebigen $g(t)$, ergibt die Siebeigenschaft

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Beide wirken auf jedes $g$ gleich, also $s(t)\delta(t)=s(0)\delta(t)$. Mit Verschiebung folgt $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, und $\varepsilon(t-\tau)=1$ genau für $\tau\le t$.
:::

:::frage $\delta(0)$ ist doch unendlich. Dann ist $\delta(2t)$ dasselbe wie $\delta(t)$, oder?
Nein. „Unendlich hoch“ beschreibt $\delta$ nicht, denn alle Funktionswerte außer bei $0$ sind gleich, und der Wert bei $0$ ist keine Zahl. Was $\delta$ ausmacht, ist seine Fläche. Staucht man das Rechteck der Fläche 1 auf die halbe Breite und lässt die Höhe gleich, halbiert sich die Fläche. Deshalb ist $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Aufgabe 8 ★ Rechnen mit $\delta$
<span class="anker" id="aufg-8"></span>

Berechne: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0{,}135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::

::::kurzfassung
Der Dirac-Impuls ist keine gewöhnliche Funktion. Alle seine Eigenschaften folgen daraus, dass er nur über seine Fläche wirkt.

Die Rechtecke $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ werden für $T_0\to0$ immer schmaler und höher, ihre Fläche bleibt 1. Einen Grenzwert im Sinne gewöhnlicher Funktionen gibt es nicht, denn eine Funktion, die überall außer in einem Punkt null ist, hat die Fläche null. $\delta(t)$ ist deshalb eine __Distribution__: ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist. Man zeichnet es als Pfeil, dessen Höhe das Gewicht angibt, also die Fläche. Die wichtigsten Regeln sind das Sieb-Produkt und die Dehnung:

$$s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\qquad \delta(bt)=\frac{1}{|b|}\,\delta(t).$$

Dazu kommen $\delta(-t)=\delta(t)$ und $\delta(t-t_0)*s(t)=s(t-t_0)$. Ein System mit $h(t)=\delta(t-t_0)$ verzögert also jedes Signal um $t_0$; es heißt __ideales Laufzeitglied__. Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$ folgt: Ein Sprung der Höhe $A$ wird beim Ableiten zu $A\,\delta$. Dieses Ableiten über Sprungstellen hinweg heißt __verallgemeinerte Differentiation__.

Der Grund für die Dehnung: Staucht man das Rechteck der Fläche 1 auf die halbe Breite und lässt die Höhe gleich, halbiert sich die Fläche. Das Produkt $s(t)\,\delta(t-T)$ kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$.

Falle: „Unendlich hoch“ beschreibt $\delta$ nicht. Deshalb ist $\delta(2t)$ nicht dasselbe wie $\delta(t)$, sondern $\frac12\delta(t)$. Manche Operationen, etwa das Quadrieren $\delta^2$, sind gar nicht definiert.
::::

::::formelsammlung
**Rechtecke der Fläche 1**

$$\frac{1}{T_0}\operatorname{rect}(t/T_0)$$

Für $T_0\to0$ immer schmaler und höher, Fläche stets 1. Einen gewöhnlichen Grenzwert gibt es nicht; $\delta(t)$ ist eine Distribution, festgelegt durch $s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$.

**Gewicht**

$$[a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t)$$

$a$, $a_1$, $a_2$ Konstanten. Gezeichnet als Pfeil, dessen Höhe das Gewicht (die Fläche) angibt.

**Siebeigenschaft**

$$\int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T)$$

Das Produkt mit $\delta(t-T)$ wirkt nur an der Stelle $T$; es zählt nur $s(T)$.

**Fläche**

$$\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a$$

$a$ konstant.

**Dehnung**

$$\delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t)$$

$b$ reell, $b\ne0$. Der gestauchte Impuls hat nur noch die Fläche $1/|b|$.

**Verschiebung**

$$\delta(t-t_0)*s(t)=s(t-t_0)$$

Ein System mit $h(t)=\delta(t-t_0)$ verzögert jedes Signal um $t_0$: ideales Laufzeitglied.

**Sprung als Integral des Dirac-Impulses**

$$\varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$$

Verallgemeinerte Differentiation: Ein Sprung der Höhe $A$ wird beim Ableiten zu $A\,\delta$. Nicht definiert sind viele Operationen, etwa $\delta^2$.
::::

::::lernkarten
:::karte begriff Distribution
Was ist eine Distribution, und warum ist der Dirac-Impuls eine Distribution und keine gewöhnliche Funktion?
---
Ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist, beim Dirac-Impuls durch $s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$. Eine Funktion, die überall außer in einem Punkt null ist, hätte die Fläche null.
--- falsch
Eine Funktion, die nur an einzelnen Punkten von null verschieden ist. Der Dirac-Impuls ist eine solche Funktion: Er hat bei $t=0$ den Wert unendlich, überall sonst den Wert null, und deshalb genau die Fläche 1.
--- falsch
Eine Verteilung von Wahrscheinlichkeiten über die Zeit. Der Dirac-Impuls ist eine Distribution, weil er angibt, dass ein Stoß mit Sicherheit genau zur Zeit $t=0$ eintrifft.
--- falsch
Eine Funktion, die sich nur näherungsweise angeben lässt, etwa durch ein schmales Rechteck. Der Dirac-Impuls ist das Rechteck mit $T_0=1$ ms, denn kürzere Rechtecke misst man nicht.
:::
:::karte zusammenhang Pfeilhöhe
Was gibt die Höhe des Pfeils an, mit dem man einen Dirac-Impuls wie $2\delta(t-1{,}5)$ zeichnet?
---
Das Gewicht, also die Fläche des Impulses, hier 2, und nicht einen Funktionswert. Der Pfeil steht dort, wo das Argument $t-1{,}5$ null wird.
--- falsch
Den Funktionswert an der Stelle, an der der Pfeil steht, hier 2; die Fläche des Impulses ist null, weil er keine Breite hat.
--- falsch
Die Dauer des Impulses, hier 2 Zeiteinheiten; seine Fläche ist immer 1, deshalb muss man sie nicht eigens zeichnen.
--- falsch
Die Höhe des schmalen Rechtecks, aus dem der Impuls entsteht, hier 2; die Fläche hängt zusätzlich von der Breite ab.
:::
:::karte formel Gewicht
Was bewirkt ein Faktor $a$ vor dem Dirac-Impuls in einer Faltung und unter einem Integral?
---
$[a\,\delta(t)]*s(t)=a\,s(t)$ und $\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a$: Der Faktor ist das Gewicht, also die Fläche des Impulses. Gewichte an derselben Stelle addieren sich, $a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t)$.
--- falsch
$[a\,\delta(t)]*s(t)=s(at)$: Der Faktor staucht das Signal, weil er die Breite des Impulses ändert. Unter dem Integral ist $\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=1$, denn die Fläche eines Dirac-Impulses bleibt immer 1.
--- falsch
$\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=1$ für jedes $a$, weil ein Dirac-Impuls immer die Fläche 1 hat. Der Faktor $a$ gibt nur an, wie hoch man den Pfeil zeichnet, und ändert in einer Faltung nichts am Ergebnis.
--- falsch
$[a\,\delta(t)]*s(t)=a\,s(t)$ und $\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a$. Zwei Impulse an derselben Stelle ergeben aber $a_1a_2\,\delta(t)$, weil sich Gewichte an derselben Stelle multiplizieren.
:::
:::karte formel Siebeigenschaft
Was ergibt das Produkt $s(t)\,\delta(t-T)$ eines Signals mit einem verschobenen Dirac-Impuls?
---
$s(t)\,\delta(t-T)=s(T)\,\delta(t-T)$: Das Produkt kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$. Unter dem Integral siebt der Impuls den Wert heraus, $\int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0)$.
--- falsch
$s(t)\,\delta(t-T)=s(t-T)$: Der Impuls verschiebt das Signal um $T$, genau wie bei der Faltung mit $\delta(t-T)$, weil Produkt und Faltung mit einem Dirac-Impuls stets dasselbe bewirken; der Wert $s(T)$ spielt keine Rolle.
--- falsch
$s(t)\,\delta(t-T)=s(T)$, eine Zahl: Der Impuls siebt den Wert an der Stelle $T$ heraus, und übrig bleibt kein Impuls mehr, weil seine Fläche dabei schon verbraucht ist.
--- falsch
$s(t)\,\delta(t-T)=s(0)\,\delta(t-T)$: Es zählt der Wert des Signals im Ursprung, weil der Dirac-Impuls nur über seine Fläche bei $t=0$ festgelegt ist, auch wenn er verschoben wird.
:::
:::karte formel Dehnung
Was ergibt die Dehnung $\delta(bt)$ des Dirac-Impulses für $b\neq0$?
---
$\delta(bt)=\frac{1}{|b|}\,\delta(t)$, mit $b=-1$ also $\delta(-t)=\delta(t)$. Ein gestauchter Impuls ist zwar genauso „unendlich hoch“, hat aber nur noch die Fläche $1/|b|$, und auf die Fläche kommt es an.
--- falsch
$\delta(bt)=b\,\delta(t)$: Staucht man die Zeit um den Faktor $b$, wird der Impuls $b$-mal so stark, weil er in kürzerer Zeit wirkt und so mehr Fläche auf kleinem Raum sammelt.
--- falsch
$\delta(bt)=\frac{1}{b}\,\delta(t)$ für jedes $b\neq0$; für $b<0$ wird der Impuls deshalb negativ, er zeigt nach unten, und es gilt $\delta(-t)=-\delta(t)$.
--- falsch
$\delta(bt)=\delta(t)$: Der Impuls ist bei $t=0$ unendlich hoch und sonst null, und daran ändert eine Stauchung der Zeitachse nichts, weil null und unendlich dabei bleiben.
:::
:::karte herleitung Dehnung aus der Faltung
Wie folgt $\delta(bt)=\frac{1}{|b|}\,\delta(t)$ aus der Wirkung von $\delta(bt)$ in einer Faltung?
---
Man faltet $\delta(bt)$ mit einem beliebigen $s(t)$, weil der Dirac-Impuls nur durch seine Wirkung unter einem Integral festgelegt ist: $\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau$.
---
Für $b>0$ substituiert man $\vartheta=b\tau$, weil dann wieder $\delta(\vartheta)$ im Integral steht; dabei entsteht der Vorfaktor $\frac1b$.
---
Die Siebeigenschaft gibt $\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t)$, weil $\delta(\vartheta)$ nur an der Stelle null wirkt.
---
Für $b<0$ kommt $-\frac1b=\frac{1}{|b|}$ heraus, weil die Substitution dann die Integrationsrichtung umkehrt. Da $\delta(bt)$ auf jedes $s$ wie $\frac1{|b|}\delta(t)$ wirkt, sind beide gleich.
---
Mit $b=-1$ folgt die Symmetrie $\delta(-t)=\delta(t)$, weil der Betrag von $-1$ eins ist.
:::
:::karte herleitung Sieb-Produkt
Wie zeigt man $s(t)\,\delta(t)=s(0)\,\delta(t)$, obwohl man mit $\delta$ nicht wie mit einer gewöhnlichen Funktion rechnen kann?
---
Man faltet $s(t)\delta(t)$ mit einem beliebigen $g(t)$, weil der Dirac-Impuls nur durch seine Wirkung unter einem Integral festgelegt ist.
---
Die Siebeigenschaft gibt $[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)$, weil $\delta(\tau)$ nur an der Stelle null wirkt.
---
Dasselbe Ergebnis $s(0)\,g(t)$ liefert $[s(0)\delta(t)]*g(t)$, weil $s(0)$ eine Konstante ist und $\delta$ das Einselement der Faltung.
---
Beide wirken auf jedes $g$ gleich, also ist $s(t)\delta(t)=s(0)\delta(t)$. Mit Verschiebung folgt $s(t)\delta(t-T)=s(T)\delta(t-T)$, weil man den Impuls an jede Stelle $T$ legen kann.
:::
:::karte begriff ideales Laufzeitglied
Was ist ein ideales Laufzeitglied, und welche Impulsantwort hat es?
---
Ein System, das jedes Signal nur um eine feste Zeit $t_0$ verzögert. Seine Impulsantwort ist $h(t)=\delta(t-t_0)$, denn $\delta(t-t_0)*s(t)=s(t-t_0)$.
--- falsch
Ein System, das jedes Signal um $t_0$ verzögert und dabei glättet. Seine Impulsantwort ist ein Rechteck der Dauer $t_0$, weil es das Signal so lange festhält.
--- falsch
Ein System, das jedes Signal um $t_0$ verzögert. Seine Impulsantwort ist $h(t)=\delta(t+t_0)$, weil die Antwort $t_0$ später kommt und das Argument dafür wachsen muss.
--- falsch
Ein System, das ein Signal ohne jede Laufzeit weitergibt. Seine Impulsantwort ist $h(t)=\delta(t)$, denn $\delta(t)*s(t)=s(t)$; ideal heißt hier: Verzögerung null.
:::
:::karte begriff verallgemeinerte Differentiation
Was versteht man unter verallgemeinerter Differentiation, und worauf beruht sie?
---
Das Ableiten von Funktionen mit Sprungstellen: Ein Sprung der Höhe $A$ wird dabei zu $A\,\delta$. Es beruht darauf, dass der Sprung das laufende Integral des Stoßes ist, $\varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau$, also $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$.
--- falsch
Das Ableiten von Funktionen mit Sprungstellen, bei dem man die Sprünge weglässt: An der Sprungstelle setzt man die Ableitung null, weil die Funktion dort weder steigt noch fällt und $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=0$ ist.
--- falsch
Das Ableiten von Funktionen mit Sprungstellen: Ein Sprung der Höhe $A$ wird dabei zu $\delta$, unabhängig von $A$, weil der Dirac-Impuls immer die Fläche 1 hat und der Sprung nur seine Lage festlegt.
--- falsch
Das Ableiten von Produkten aus Dirac-Impulsen, etwa $\delta^2$, mit der Produktregel wie bei gewöhnlichen Funktionen. Es beruht darauf, dass sich $\delta$ als Grenzwert schmaler Rechtecke wie eine Funktion verhält.
:::
:::karte zusammenhang Nicht definierte Operationen
Darf man mit Dirac-Impulsen jede Rechenoperation ausführen, die für gewöhnliche Funktionen erlaubt ist?
---
Nein. Viele Operationen sind für Dirac-Impulse nicht definiert, etwa das Quadrieren $\delta^2$, weil $\delta$ nur durch seine Wirkung unter einem Integral festgelegt ist und der Wert bei 0 keine Zahl ist.
--- falsch
Ja. Sobald man $\delta$ als Grenzwert schmaler Rechtecke auffasst, gelten alle Rechenregeln für Funktionen, auch für Produkte; zum Beispiel ist $\delta^2=\delta$, weil das Rechteck die Höhe 1 hat.
--- falsch
Ja, mit einer Ausnahme: Man darf $\delta$ nicht verschieben, weil der Impuls fest an die Stelle $t=0$ gebunden ist; ein Stoß an einer anderen Stelle braucht ein eigenes Symbol.
--- falsch
Nein, aber nur das Integrieren ist verboten: Die Fläche unter $\delta$ lässt sich nicht bestimmen, weil der Impuls unendlich hoch ist und unendlich mal null keine Zahl ergibt.
:::
::::
