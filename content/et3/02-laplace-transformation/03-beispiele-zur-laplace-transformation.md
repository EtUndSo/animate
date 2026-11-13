---
title: Beispiele zur Laplace-Transformation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220300
summary: Vier Signale werden transformiert.
tags: rechtsseitig, Konvergenzbereich, linksseitig, Linearität, Superposition, Streifen, Polstelle
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Vier Signale werden transformiert. Dabei zeigt sich: Das Integral existiert nur für bestimmte $p$, und erst der Ausdruck $S(p)$ zusammen mit diesen $p$ legt das Signal fest.
:::

### Der rechtsseitige Exponentialimpuls

<span class="anker" id="stufe-2-1"></span>

Ein Signal heißt __rechtsseitig__ oder kausal, wenn es für $t<0$ null ist. Das einfachste Beispiel ist der rechtsseitige Exponentialimpuls

$$s_1(t)=\mathrm{e}^{-bt}\cdot\varepsilon(t)$$

mit einer Konstanten $b$, die auch komplex sein darf. Die Impulsantwort des RC-Tiefpasses hat diese Form, mit $b=1/RC$ und dem Vorfaktor $1/RC$. Die Transformierte ist

<span class="anker" id="gl-2-1"></span>
$$S_1(p)=\int_0^{\infty}\mathrm{e}^{-bt}\,\mathrm{e}^{-pt}\,\mathrm{d} t=\Bigl[-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr]_0^\infty=\frac{1}{b+p}\qquad\text{für }\sigma=\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}. \tag{2.1}$$

Die Bedingung kommt von der oberen Grenze. Der Betrag des Integranden ist

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t},$$

denn der zweite Faktor hat nach der Eulerschen Formel den Betrag 1. Er geht für $t\to\infty$ genau dann gegen null, wenn $\operatorname{Re}(b+p)>0$ ist, also $\operatorname{Re} p>-\operatorname{Re} b$. Nur dann verschwindet der Wert an der oberen Grenze, und es bleibt $0-\bigl(-\frac{1}{b+p}\bigr)=\frac{1}{b+p}$.

⁠**Kurz gesagt:** $\mathrm{e}^{-bt}\varepsilon(t)\longleftrightarrow\frac{1}{b+p}$, aber nur für $\operatorname{Re} p>-\operatorname{Re} b$.

:::hintergrund Warum beim Einsetzen der Grenzen ein Plus herauskommt
Die Stammfunktion von $\mathrm{e}^{-(b+p)t}$ ist $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, mit Minus, weil Ableiten den Faktor $-(b+p)$ liefert. Dann rechnet man „obere Grenze minus untere Grenze“:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

An der unteren Grenze ist $\mathrm{e}^0=1$, dort bleibt kein e-Term übrig. Das Minus der Stammfunktion trifft auf das Minus, mit dem die untere Grenze abgezogen wird. Minus mal Minus ergibt Plus.
:::

:::hintergrund Warum allein der Realteil über die Konvergenz entscheidet
Der Imaginärteil von $b+p$ lässt den Integranden nur in der komplexen Ebene kreisen, am Betrag ändert er nichts. Über Wachsen oder Abklingen entscheidet allein der Realteil. Drei Präzisierungen:

<ul>

<li>

Es zählt die *Summe* $\operatorname{Re} b+\sigma$. Das Signal darf selbst wachsen ($\operatorname{Re} b<0$), solange $\sigma$ groß genug ist. Der Faktor $\mathrm{e}^{-\sigma t}$ dämpft dann das Wachstum.

</li>

<li>

„Geht gegen null“ allein reicht nicht. Auch $1/t$ geht gegen null, aber $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, weil die Beiträge zu langsam kleiner werden. Exponentielles Abklingen ist schnell genug: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ ist endlich.

</li>

<li>

Auf der Grenze $\operatorname{Re}(b+p)=0$ hat der Integrand den konstanten Betrag 1 und kreist nur. Das Integral pendelt dann, statt sich einem Wert zu nähern (Aufgabe [2a](#aufg-2a)).

</li>

</ul>
:::

### Der Konvergenzbereich

<span class="anker" id="stufe-2-2"></span>

Beim rechtsseitigen Exponentialimpuls existiert die Transformierte nur für einen Teil der $p$-Ebene. Das ist der Normalfall.

:::definition Definition 2.1 (Konvergenzbereich)
<span class="anker" id="satz-2-1"></span>

Der __Konvergenzbereich__ einer Laplace-Transformierten $S(p)$ ist die Menge aller $p$, für die das Integral [(1.9)](eigenfunktionen-von-lti-systemen.html#gl-1-9) absolut konvergiert, für die also $\int_{-\infty}^{\infty}\bigl|s(t)\,\mathrm{e}^{-pt}\bigr|\,\mathrm{d} t<\infty$ ist.
:::

Wegen $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$ hängt diese Bedingung nur von $\sigma=\operatorname{Re} p$ ab, nie vom Imaginärteil. Gehört ein Punkt $p$ zum Konvergenzbereich, dann auch jeder andere Punkt mit demselben Realteil. Der Konvergenzbereich besteht deshalb aus ganzen senkrechten Linien, und seine Grenzen sind senkrechte Geraden.

Beim rechtsseitigen Exponentialimpuls ist er die Halbebene rechts der Geraden $\operatorname{Re} p=-\operatorname{Re} b$ (Abb. [2](#abb-2), links). Die Grenzgerade selbst gehört nicht dazu.

⁠**Kurz gesagt:** Der Konvergenzbereich ist der Teil der $p$-Ebene, in dem die Transformierte existiert. Er hängt nur von $\operatorname{Re} p$ ab und wird von senkrechten Geraden begrenzt.

### Der linksseitige Exponentialimpuls

<span class="anker" id="stufe-2-3"></span>

Ein Signal heißt __linksseitig__ oder antikausal, wenn es für $t>0$ null ist. Der linksseitige Exponentialimpuls ist

$$s_2(t)=\mathrm{e}^{-bt}\cdot\varepsilon(-t).$$

Jetzt läuft das Integral von $-\infty$ bis $0$:

<span class="anker" id="gl-2-2"></span>
$$S_2(p)=\int_{-\infty}^{0}\mathrm{e}^{-bt}\,\mathrm{e}^{-pt}\,\mathrm{d} t=\Bigl[-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr]_{-\infty}^0=-\frac{1}{b+p}\qquad\text{für }\sigma=\operatorname{Re}\{p\}<-\operatorname{Re}\{b\}. \tag{2.2}$$

Die Grenze $t=0$ ist jetzt die *obere*, ihr Beitrag $-\frac{1}{b+p}$ bleibt mit seinem Minus stehen. An der unteren Grenze $t\to-\infty$ muss $\mathrm{e}^{-(b+p)t}$ verschwinden. Für negative $t$ ist $-\operatorname{Re}(b+p)\,t$ genau dann sehr negativ, wenn $\operatorname{Re}(b+p)<0$ ist. Deshalb liegt dieser Konvergenzbereich *links* der Geraden $\operatorname{Re} p=-\operatorname{Re} b$ (Abb. [2](#abb-2), rechts).

:::abbildung et3/k2kbhalb 2
Konvergenzbereiche (blau) in der $p$-Ebene für den rechtsseitigen (links) und den linksseitigen Exponentialimpuls (rechts), hier für ein $b$ mit $\operatorname{Re} b=1/\mathrm s$. Die gestrichelte Grenzgerade $\operatorname{Re} p=-\operatorname{Re} b$ gehört nicht dazu.
:::

Vergleicht man mit dem rechtsseitigen Impuls, fällt auf: Das Signal $-s_2(t)=-\mathrm{e}^{-bt}\varepsilon(-t)$ hat dieselbe Transformierte $\frac{1}{b+p}$ wie $s_1(t)$, nur mit einem anderen Konvergenzbereich. Der Ausdruck allein unterscheidet die beiden Signale nicht.

⁠**Kurz gesagt:** Ein rechtsseitiges und ein linksseitiges Signal können denselben Ausdruck $S(p)$ haben. Erst der Konvergenzbereich legt fest, welches Signal gemeint ist.

:::hintergrund Wie ein Ausdruck zu zwei Signalen gehören kann
Der Ausdruck $\frac{1}{b+p}$ ist eine Formel, die für jedes $p\ne-b$ einen Wert hat. Das Integral liefert ihn aber nur in einem Teil der Ebene. Rechts der Geraden $\operatorname{Re} p=-\operatorname{Re} b$ ist er das Integral über den rechtsseitigen Impuls $\mathrm{e}^{-bt}\varepsilon(t)$. Links davon divergiert dieses Integral; die Formel hat dort zwar weiter Werte, aber sie sind kein Integral über $\mathrm{e}^{-bt}\varepsilon(t)$ mehr. Dort sind sie das Integral über den linksseitigen Impuls $-\mathrm{e}^{-bt}\varepsilon(-t)$. Die Grenzgerade durch den Pol teilt die Ebene in zwei Hälften, und jede Hälfte gehört zu einem anderen Signal. Deshalb ist eine Laplace-Transformierte erst mit ihrem Konvergenzbereich vollständig angegeben.
:::

### Summen von Signalen

<span class="anker" id="stufe-2-4"></span>

Das Integral [(1.9)](eigenfunktionen-von-lti-systemen.html#gl-1-9) ist linear: Für Konstanten $a_1,a_2$ gilt

$$\mathcal{L}\{a_1s_1(t)+a_2s_2(t)\}=a_1S_1(p)+a_2S_2(p).$$

Das gilt für alle $p$, für die *beide* Integrale konvergieren. Der Konvergenzbereich der Summe enthält also den Durchschnitt der beiden Konvergenzbereiche. Die Eigenschaft heißt __Linearität__ oder __Superposition__.

⁠**Kurz gesagt:** Die Transformierte einer Summe ist die Summe der Transformierten, dort, wo beide existieren.

### Der zweiseitige Exponentialimpuls

<span class="anker" id="stufe-2-5"></span>

Der zweiseitige Exponentialimpuls ist

<span class="anker" id="gl-2-3"></span>
$$s_3(t)=\mathrm{e}^{-b|t|}. \tag{2.3}$$

Für $t>0$ ist er $\mathrm{e}^{-bt}$, für $t<0$ ist er $\mathrm{e}^{+bt}$. Den rechten Teil kennt man aus [(2.1)](#gl-2-1). Für den linken Teil setzt man in [(2.2)](#gl-2-2) $-b$ statt $b$ ein:

<span class="anker" id="gl-2-4"></span>
$$s_2'(t)=\mathrm{e}^{bt}\cdot\varepsilon(-t)\quad\Longrightarrow\quad S_2'(p)=\frac{-1}{-b+p}\qquad\text{für }\sigma=\operatorname{Re}\{p\}<\operatorname{Re}\{b\}. \tag{2.4}$$

Mit der Linearität folgt

<span class="anker" id="gl-2-5"></span>
$$S_3(p)=S_1(p)+S_2'(p)=\frac{1}{b+p}-\frac{1}{p-b}=\frac{2b}{b^2-p^2}\qquad\text{für }-\operatorname{Re}\{b\}<\operatorname{Re}\{p\}<\operatorname{Re}\{b\}. \tag{2.5}$$

Zur Kontrolle auf den Hauptnenner: $\frac{(p-b)-(b+p)}{(b+p)(p-b)}=\frac{-2b}{p^2-b^2}=\frac{2b}{b^2-p^2}$.

Der Konvergenzbereich ist ein senkrechter __Streifen__: Der rechte Teil verlangt $\operatorname{Re} p>-\operatorname{Re} b$, der linke $\operatorname{Re} p<\operatorname{Re} b$. Beides zugleich geht nur, wenn $-\operatorname{Re} b<\operatorname{Re} b$ ist, also $\operatorname{Re} b>0$. Für $\operatorname{Re} b>0$ klingt das Signal nach beiden Seiten ab (Abb. [3](#abb-3), oben). Für $\operatorname{Re} b\le0$ wächst es nach mindestens einer Seite, der Streifen ist leer, und das Signal hat keine Laplace-Transformierte (Abb. [3](#abb-3), unten).

:::abbildung et3/k2zweiseitig 3
Links: der zweiseitige Exponentialimpuls $\mathrm{e}^{-b|t|}$ für reelles $b>0$ (oben, klingt nach beiden Seiten ab) und $b<0$ (unten, wächst nach beiden Seiten). Rechts: Konvergenzbereich für reelles $b>0$, der Streifen $-b<\operatorname{Re} p<b$ zwischen den Polstellen $\pm b$ (Kreuze).
:::

⁠**Kurz gesagt:** Ein zweiseitiges Signal hat als Konvergenzbereich einen Streifen, und der kann leer sein.

### Polstellen

<span class="anker" id="stufe-2-6"></span>

In [(2.5)](#gl-2-5) wird der Nenner $b^2-p^2$ für $p=\pm b$ null. Dort wächst $S_3(p)$ über alle Grenzen.

:::definition Definition 2.2 (Polstelle)
<span class="anker" id="satz-2-2"></span>

Eine Stelle $p$, an der $S(p)$ über alle Grenzen wächst, heißt __Polstelle__ oder kurz Pol von $S(p)$. Ist $S(p)$ ein Bruch aus zwei Polynomen in $p$, so sind die Pole die Nullstellen des Nennerpolynoms (sofern sie sich nicht gegen Nullstellen des Zählers kürzen).
:::

Beim zweiseitigen Exponentialimpuls liegen die Pole bei $p=\pm b$. Die Grenzen des Konvergenzbereichs gehen genau durch sie hindurch (Abb. [3](#abb-3)): Der Konvergenzbereich reicht bis an die Pole heran, enthält aber keinen. Dasselbe gilt für die beiden einseitigen Impulse: Ihr Pol liegt bei $p=-b$, also auf ihrer Grenzgeraden $\operatorname{Re} p=-\operatorname{Re} b$.

⁠**Kurz gesagt:** Pole sind die Stellen, an denen $S(p)$ unendlich wird. Sie liegen auf den Grenzen des Konvergenzbereichs, nie in ihm.

:::hintergrund Warum die Pole genau bei den Exponenten des Signals liegen
Der Kasten „Suchfilter“ im ersten Abschnitt hat es vorweggenommen: Multipliziert man einen Anteil $\mathrm{e}^{p_0t}$ mit der Probe $\mathrm{e}^{-pt}$, so bleibt für $p=p_0$ eine Konstante übrig, und das Integral wird unendlich. In den Beispielen:

<ul>

<li>

$\mathrm{e}^{-bt}\varepsilon(t)$ hat den Exponenten $-b$, und der Pol liegt bei $p=-b$.

</li>

<li>

$\mathrm{e}^{-b|t|}$ besteht rechts aus $\mathrm{e}^{-bt}$ und links aus $\mathrm{e}^{+bt}$, also aus den Exponenten $-b$ und $+b$. Genau dort liegen die Pole.

</li>

</ul>

Auch die Grenze des Konvergenzbereichs erklärt sich so. Auf der Geraden $\operatorname{Re} p=\operatorname{Re} p_0$ hat der Integrand $\mathrm{e}^{(p_0-p)t}$ den konstanten Betrag 1: Die Probe gleicht das Wachsen oder Abklingen des Anteils genau aus, und das Integral kann nicht konvergieren. Rechts davon dämpft die Probe stärker, als der Anteil wächst, links davon schwächer. Deshalb endet der Konvergenzbereich eines rechtsseitigen Anteils genau an der Senkrechten durch seinen Pol.

Kurz: Die Pole einer Laplace-Transformierten zeigen, aus welchen Exponentialfunktionen das Signal besteht. Sie zeigen nicht, *wann* das Signal stattfindet; dafür braucht man zusätzlich den Konvergenzbereich, der die Seite festlegt.
:::

### Eine Summe aus drei Exponentialimpulsen

<span class="anker" id="stufe-2-7"></span>

Das Signal

<span class="anker" id="gl-2-6"></span>
$$s(t)=\mathrm{e}^{-2t}\cdot\varepsilon(t)+\mathrm{e}^{-t}\cdot\cos(3t)\cdot\varepsilon(t)\qquad(t\text{ in s}) \tag{2.6}$$

ist eine abklingende Exponentialfunktion plus eine abklingende Schwingung, beide rechtsseitig. Mit [(1.2)](eigenfunktionen-von-lti-systemen.html#gl-1-2) wird der Kosinus zu zwei Exponentialfunktionen:

$$s(t)=\mathrm{e}^{-2t}\,\varepsilon(t)+\tfrac12\,\mathrm{e}^{-(1-3\mathrm{j})t}\,\varepsilon(t)+\tfrac12\,\mathrm{e}^{-(1+3\mathrm{j})t}\,\varepsilon(t).$$

Das sind drei rechtsseitige Exponentialimpulse mit $b=2$, $b=1-3\mathrm{j}$ und $b=1+3\mathrm{j}$. Nach [(2.1)](#gl-2-1) und der Linearität ist

<span class="anker" id="gl-2-7"></span>
$$S(p)=\underbrace{\frac{1}{p+2}}_{\operatorname{Re} p>-2}+\underbrace{\frac{1/2}{p+(1-3\mathrm{j})}}_{\operatorname{Re} p>-1}+\underbrace{\frac{1/2}{p+(1+3\mathrm{j})}}_{\operatorname{Re} p>-1}. \tag{2.7}$$

Alle drei Bedingungen gelten zugleich für $\operatorname{Re} p>-1$. Die beiden letzten Brüche fasst man über den Hauptnenner $(p+1-3\mathrm{j})(p+1+3\mathrm{j})=(p+1)^2+9=p^2+2p+10$ zusammen:

$$\frac{1/2}{p+1-3\mathrm{j}}+\frac{1/2}{p+1+3\mathrm{j}}=\frac{\tfrac12\bigl[(p+1+3\mathrm{j})+(p+1-3\mathrm{j})\bigr]}{p^2+2p+10}=\frac{p+1}{p^2+2p+10}.$$

Dazu kommt $\frac{1}{p+2}$:

<span class="anker" id="gl-2-8"></span>
$$S(p)=\frac{(p^2+2p+10)+(p+1)(p+2)}{(p^2+2p+10)(p+2)}=\frac{2p^2+5p+12}{(p^2+2p+10)(p+2)}\qquad\text{für }\operatorname{Re} p>-1. \tag{2.8}$$

Die Pole sind die Nullstellen des Nenners: $p_{\mathrm P1}=-2$ und $p_{\mathrm P2,3}=-1\pm3\mathrm{j}$. Der Konvergenzbereich liegt rechts der Geraden $\operatorname{Re} p=-1$, auf der das Polpaar $-1\pm3\mathrm{j}$ sitzt.

⁠**Kurz gesagt:** Eine abklingende Schwingung liefert ein Paar konjugiert komplexer Pole. Der Realteil der Pole ist die Abklingrate, der Imaginärteil die Kreisfrequenz.

### Die Grundpaare

<span class="anker" id="stufe-2-8"></span>

Die Beispiele liefern eine Handvoll Paare, die im ganzen Kapitel gebraucht werden. Dazu kommen der Dirac-Impuls und die Rampe.

:::merke Die Grundpaare
Für eine beliebige komplexe Zahl $p_0$:

<span class="anker" id="gl-2-9"></span>
<span class="anker" id="gl-2-10"></span>
<span class="anker" id="gl-2-11"></span>
<span class="anker" id="gl-2-12"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{alle }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.9|2.10|2.11|2.12}$$

[(2.9)](#gl-2-9) ist der rechtsseitige Impuls [(2.1)](#gl-2-1) mit $p_0=-b$, [(2.10)](#gl-2-10) der linksseitige [(2.2)](#gl-2-2) mit umgekehrtem Vorzeichen. Mit $p_0=0$ folgt aus [(2.9)](#gl-2-9) der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$.
:::

:::herleitung Grundpaare
[(2.9)](#gl-2-9): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. Der Wert an der oberen Grenze verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)>0$.

[(2.10)](#gl-2-10): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. Der Wert bei $t\to-\infty$ verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)<0$.

[(2.11)](#gl-2-11): Siebeigenschaft des Dirac-Impulses, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.12)](#gl-2-12): partielle Integration, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ für $\operatorname{Re} p>0$.
:::

:::hintergrund Hat jede Funktion eine Laplace-Transformierte?
Nein, nur Funktionen mit nicht leerem Konvergenzbereich. Drei Gegenbeispiele:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ wächst schneller als jede Exponentialfunktion. $\mathrm{e}^{t^2-\sigma t}\to\infty$ für jedes $\sigma$.

</li>

<li>

$\mathrm{e}^{|t|}$, also der zweiseitige Impuls mit $b=-1$: Die rechte Hälfte verlangt $\sigma>1$, die linke $\sigma<-1$. Beides zugleich geht nicht.

</li>

<li>

Selbst die Konstante $s(t)=1$ für alle $t$: rechts $\sigma>0$, links $\sigma<0$.

</li>

</ul>

Für rechtsseitige Signale, die höchstens exponentiell wachsen, gibt es dagegen immer einen Konvergenzbereich. Dazu gehört jedes Signal, das in einer Schaltung bei $t=0$ eingeschaltet wird.
:::

:::aufgabe Aufgabe 2 ★★ Ein wachsendes Signal
<span class="anker" id="aufg-2"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, zum Beispiel die Impulsantwort eines Systems, das sich aufschaukelt ($t$ in s).

<ol class="al">

<li>

Für welche $\sigma$ ist $s(t)\,\mathrm{e}^{-\sigma t}$ absolut integrierbar?

</li>

<li>

Berechne $S(p)$ direkt aus dem Integral. Zeichne Pol und Konvergenzbereich in die $p$-Ebene.

</li>

<li>

Berechne die Transformierte des linksseitigen Signals $-\mathrm{e}^{2t}\varepsilon(-t)$ samt Konvergenzbereich. Was lernst du aus dem Vergleich mit (b)? Welches der beiden Signale klingt ab?

</li>

</ol>

:::loesung
(a) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ für $t>0$ und null für $t<0$. Das ist genau dann integrierbar, wenn der Exponent negativ ist, also für $\sigma>2/\mathrm s$.

(b) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ für $\operatorname{Re} p>2$. Pol bei $p=2$, Konvergenzbereich rechts davon, wie bei jedem rechtsseitigen Signal. Numerische Kontrolle: $S(3)=1$, $S(2{,}5+\mathrm{j})=\frac{1}{0{,}5+\mathrm{j}}=0{,}4-0{,}8\mathrm{j}$.

(c) $-\int_{-\infty}^0\mathrm{e}^{2t}\,\mathrm{e}^{-pt}\mathrm{d} t=-\Bigl[-\frac{\mathrm{e}^{-(p-2)t}}{p-2}\Bigr]_{-\infty}^0=\dfrac{1}{p-2}$. Der Wert bei $t\to-\infty$ verschwindet nur für $\operatorname{Re}(p-2)<0$, also ist der Konvergenzbereich $\operatorname{Re} p<2$. Das ist das Grundpaar [(2.10)](#gl-2-10) mit $p_0=2$. Der Ausdruck ist derselbe wie in (b), nur der Konvergenzbereich liegt auf der anderen Seite des Pols. Der Ausdruck $\frac{1}{p-2}$ allein legt das Signal also nicht fest. Das linksseitige Signal $-\mathrm{e}^{2t}\varepsilon(-t)$ klingt für $t\to-\infty$ ab; sein Konvergenzbereich enthält $\sigma=0$, es ist also absolut integrierbar. Das rechtsseitige wächst über alle Grenzen.
:::
:::

:::aufgabe Aufgabe 2a ★★ Was auf der Grenze passiert
<span class="anker" id="aufg-2a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, also $b=-1-3\mathrm{j}$ ($t$ in s).

<ol class="al">

<li>

Für welche $\sigma$ konvergiert $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$? Welche Rolle spielt die 3?

</li>

<li>

Setze $p=1+\mathrm{j}\omega$, also genau auf die Grenze, und berechne $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. Was passiert für $T\to\infty$? Unterscheide $\omega\neq3$ und $\omega=3$. Wo liegt der Pol?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ mit $p=\sigma+\mathrm{j}\omega$. Der Betrag des Integranden ist $\mathrm{e}^{-(\sigma-1)t}$, das Integral konvergiert genau für $\sigma>1$. Die 3 (die Kreisfrequenz des Signals) taucht im Betrag nicht auf. Sie bestimmt nur, wo auf der Grenzgeraden der Pol sitzt: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, Pol bei $p=1+3\mathrm{j}$.

(b) Mit $p=1+\mathrm{j}\omega$ ist $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. Der Zähler kreist für wachsendes $T$ auf einem Kreis um 1 und nähert sich keinem Wert. Das Integral bleibt beschränkt, hat aber keinen Grenzwert.

</li>

<li>

$\omega=3$, also genau im Pol $p=1+3\mathrm{j}$: Der Integrand ist konstant 1, das Integral ist $T$ und wächst über alle Grenzen.

</li>

</ul>

Auf der Grenzgeraden konvergiert das Integral also nirgends. Der Konvergenzbereich ist die offene Halbebene $\operatorname{Re} p>1$.
:::
:::

::::kurzfassung
Das Laplace-Integral existiert nur in einem Teil der $p$-Ebene. Erst der Ausdruck $S(p)$ zusammen mit diesem Teil legt das Signal fest.

Ein Signal heißt __rechtsseitig__ oder kausal, wenn es für $t<0$ null ist, und __linksseitig__ oder antikausal, wenn es für $t>0$ null ist. Der __Konvergenzbereich__ ist die Menge aller $p$, für die $\int_{-\infty}^{\infty}\bigl|s(t)\,\mathrm{e}^{-pt}\bigr|\,\mathrm{d} t<\infty$ ist. Wegen $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$ hängt er nur von $\operatorname{Re} p$ ab; seine Grenzen sind senkrechte Geraden. Eine __Polstelle__ oder kurz ein Pol ist eine Stelle, an der $S(p)$ über alle Grenzen wächst; bei einem Bruch aus zwei Polynomen sind das die Nullstellen des Nenners, sofern sie sich nicht kürzen. Pole liegen auf den Grenzen des Konvergenzbereichs, nie in ihm. Die __Linearität__, auch __Superposition__ genannt, erlaubt, Summen gliedweise zu transformieren, dort, wo alle Teile konvergieren. Aus den Beispielen folgen die Grundpaare für eine komplexe Zahl $p_0$:

$$\mathrm{e}^{p_0t}\,\varepsilon(t)\longleftrightarrow\frac{1}{p-p_0},\ \operatorname{Re} p>\operatorname{Re} p_0;\qquad -\mathrm{e}^{p_0t}\,\varepsilon(-t)\longleftrightarrow\frac{1}{p-p_0},\ \operatorname{Re} p<\operatorname{Re} p_0 .$$

Dazu kommen $\delta(t)\longleftrightarrow1$ für alle $p$ und $t\,\varepsilon(t)\longleftrightarrow\frac{1}{p^2}$ für $\operatorname{Re} p>0$.

Der Mechanismus: Das Integral prüft das Signal mit der Probe $\mathrm{e}^{-pt}$. Trifft $p$ den Exponenten $p_0$ eines Anteils $\mathrm{e}^{p_0t}$, bleibt ein konstanter Integrand, und das Integral wird unendlich; dort sitzt ein Pol. Die Pole zeigen also, aus welchen Exponentialfunktionen das Signal besteht. Eine abklingende Schwingung liefert so ein konjugiert komplexes Polpaar.

Falle: Der rechtsseitige und der linksseitige Impuls haben denselben Ausdruck $\frac{1}{p-p_0}$; erst der Konvergenzbereich unterscheidet sie. Ein zweiseitiges Signal hat einen __Streifen__ als Konvergenzbereich, und ist er leer, gibt es keine Laplace-Transformierte.
::::

::::formelsammlung
**Rechtsseitiger Exponentialimpuls**

$$s_1(t)=\mathrm{e}^{-bt}\cdot\varepsilon(t)\qquad\longleftrightarrow\qquad S_1(p)=\frac{1}{b+p}$$

$b$ konstant, auch komplex; Konvergenzbereich $\sigma=\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}$. Rechtsseitig (kausal): null für $t<0$.

**Konvergenzbereich (Definition)**

$$\int_{-\infty}^{\infty}\bigl|s(t)\,\mathrm{e}^{-pt}\bigr|\,\mathrm{d} t<\infty$$

Menge aller $p$, für die das Laplace-Integral absolut konvergiert. Hängt wegen $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$ nur von $\operatorname{Re} p$ ab; die Grenzen sind senkrechte Geraden.

**Linksseitiger Exponentialimpuls**

$$s_2(t)=\mathrm{e}^{-bt}\cdot\varepsilon(-t)\qquad\longleftrightarrow\qquad S_2(p)=-\frac{1}{b+p}$$

Konvergenzbereich $\sigma=\operatorname{Re}\{p\}<-\operatorname{Re}\{b\}$. Linksseitig (antikausal): null für $t>0$.

**Linearität (Superposition)**

$$\mathcal{L}\{a_1s_1(t)+a_2s_2(t)\}=a_1S_1(p)+a_2S_2(p)$$

$a_1,a_2$ Konstanten; gilt für alle $p$, für die beide Integrale konvergieren. Der Konvergenzbereich der Summe enthält den Durchschnitt beider Bereiche.

**Zweiseitiger Exponentialimpuls**

$$s_3(t)=\mathrm{e}^{-b|t|}\qquad\longleftrightarrow\qquad S_3(p)=\frac{2b}{b^2-p^2}$$

Konvergenzbereich ist der Streifen $-\operatorname{Re}\{b\}<\operatorname{Re}\{p\}<\operatorname{Re}\{b\}$; nicht leer nur für $\operatorname{Re} b>0$. Pole bei $p=\pm b$.

**Grundpaar: rechtsseitig**

$$\mathrm{e}^{p_0t}\,\varepsilon(t)\longleftrightarrow\frac{1}{p-p_0}$$

$p_0$ beliebig komplex; $\operatorname{Re} p>\operatorname{Re} p_0$. Mit $p_0=0$: Sprung $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$.

**Grundpaar: linksseitig**

$$-\mathrm{e}^{p_0t}\,\varepsilon(-t)\longleftrightarrow\frac{1}{p-p_0}$$

$\operatorname{Re} p<\operatorname{Re} p_0$. Derselbe Ausdruck wie rechtsseitig; nur der Konvergenzbereich unterscheidet die Signale.

**Grundpaar: Dirac-Impuls**

$$\delta(t)\longleftrightarrow1$$

Für alle $p$ (Siebeigenschaft).

**Grundpaar: Rampe**

$$t\,\varepsilon(t)\longleftrightarrow\frac{1}{p^2}$$

$\operatorname{Re} p>0$.
::::

::::lernkarten
:::karte begriff rechtsseitig
Wann heißt ein Signal bei der Laplace-Transformation rechtsseitig, und welches ist das einfachste Beispiel dafür?
---
Wenn es für $t<0$ null ist; man nennt es auch kausal. Das einfachste Beispiel ist der rechtsseitige Exponentialimpuls $s_1(t)=\mathrm{e}^{-bt}\cdot\varepsilon(t)$ mit einer Konstanten $b$, die auch komplex sein darf.
--- falsch
Wenn es für $t>0$ null ist und nur vor dem Einschalten Werte hat; man nennt es auch antikausal. Das einfachste Beispiel ist der Impuls $\mathrm{e}^{-bt}\cdot\varepsilon(-t)$ mit einer Konstanten $b$, die auch komplex sein darf.
--- falsch
Wenn es nur positive Werte annimmt, sein Graph also ganz oberhalb der Zeitachse liegt. Das einfachste Beispiel ist der Sprung $\varepsilon(t)$, weil er nie negativ wird und für große $t$ konstant bleibt.
--- falsch
Wenn es für $t\to\infty$ abklingt, also rechts auf der Zeitachse verschwindet. Das einfachste Beispiel ist der Exponentialimpuls $\mathrm{e}^{-bt}$ für alle Zeiten $t$, mit einer reellen Konstanten $b>0$.
:::
:::karte formel Rechtsseitiger Exponentialimpuls
Welche Laplace-Transformierte hat der rechtsseitige Exponentialimpuls $\mathrm{e}^{-bt}\cdot\varepsilon(t)$, und für welche $p$ gilt sie?
---
$S_1(p)=\frac{1}{b+p}$ für $\sigma=\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}$. Nur dann geht $\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}$ für $t\to\infty$ gegen null, und der Wert der Stammfunktion an der oberen Grenze verschwindet.
--- falsch
$S_1(p)=-\frac{1}{b+p}$ für $\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}$. Das Minus stammt aus der Stammfunktion $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$ und bleibt beim Einsetzen der Grenzen stehen, weil an der unteren Grenze $\mathrm{e}^0=1$ ist.
--- falsch
$S_1(p)=\frac{1}{b+p}$ für $\operatorname{Re}\{p\}>\operatorname{Re}\{b\}$. Nur dann ist der Exponent des Integranden negativ, weil $p$ größer als $b$ sein muss, damit $\mathrm{e}^{-(b+p)t}$ für $t\to\infty$ verschwindet.
--- falsch
$S_1(p)=\frac{1}{b+p}$ für alle $p$ mit $|p|>|b|$, also außerhalb eines Kreises um den Ursprung. Dort ist der Betrag des Integranden kleiner als 1, und das Integral über $\mathrm{e}^{-(b+p)t}$ konvergiert.
:::
:::karte herleitung Transformierte des rechtsseitigen Exponentialimpulses
Wie berechnet man aus dem Laplace-Integral die Transformierte $\frac{1}{b+p}$ des rechtsseitigen Exponentialimpulses $\mathrm{e}^{-bt}\cdot\varepsilon(t)$?
---
Das Integral beginnt bei null, weil $\varepsilon(t)=0$ für $t<0$ ist, und die beiden Exponentialfunktionen werden zusammengefasst: $\int_0^{\infty}\mathrm{e}^{-bt}\,\mathrm{e}^{-pt}\,\mathrm{d} t=\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t$.
---
Die Stammfunktion ist $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, mit Minus, weil Ableiten den Faktor $-(b+p)$ liefert.
---
Der Wert an der oberen Grenze verschwindet, weil $\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}$ für $\operatorname{Re}(b+p)>0$, also für $\operatorname{Re} p>-\operatorname{Re} b$, gegen null geht.
---
An der unteren Grenze steht $-\frac{1}{b+p}$, weil $\mathrm{e}^0=1$ ist. Sie wird abgezogen: $0-\bigl(-\frac{1}{b+p}\bigr)=\frac{1}{b+p}$, mit Plus, weil Minus mal Minus Plus ergibt.
:::
:::karte begriff Konvergenzbereich
Was ist der Konvergenzbereich einer Laplace-Transformierten $S(p)$, und warum wird er von senkrechten Geraden begrenzt?
---
Die Menge aller $p$, für die das Integral absolut konvergiert, für die also $\int_{-\infty}^{\infty}\bigl|s(t)\,\mathrm{e}^{-pt}\bigr|\,\mathrm{d} t<\infty$ ist. Wegen $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$ hängt das nur von $\sigma=\operatorname{Re} p$ ab, nie vom Imaginärteil; deshalb besteht er aus ganzen senkrechten Linien.
--- falsch
Die Menge aller $p$, für die $S(p)$ einen endlichen Wert hat, also alle Punkte außer den Polen. Er wird von senkrechten Geraden begrenzt, weil die Pole bei reellen Signalen stets auf der reellen Achse liegen und man ihre Umgebung als Streifen ausspart.
--- falsch
Die Menge aller $p$, für die das Signal $s(t)$ selbst absolut integrierbar ist. Weil das Signal nicht von $p$ abhängt, ist er entweder die ganze $p$-Ebene oder leer; senkrechte Grenzen entstehen erst durch die Pole des Systems, durch das das Signal läuft.
--- falsch
Die Menge aller $p$, für die das Integral absolut konvergiert. Weil $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\operatorname{Im} p\cdot t}$ nur vom Imaginärteil abhängt, besteht er aus ganzen waagerechten Linien; senkrechte Grenzen hat er nur bei Signalen, die reell sind.
:::
:::karte begriff linksseitig
Wann heißt ein Signal linksseitig, und wo liegt der Konvergenzbereich des linksseitigen Exponentialimpulses $\mathrm{e}^{-bt}\cdot\varepsilon(-t)$?
---
Wenn es für $t>0$ null ist; man nennt es auch antikausal. Der linksseitige Exponentialimpuls hat die Transformierte $-\frac{1}{b+p}$ für $\operatorname{Re}\{p\}<-\operatorname{Re}\{b\}$, also links der Geraden $\operatorname{Re} p=-\operatorname{Re} b$, weil nur dort $\mathrm{e}^{-(b+p)t}$ für $t\to-\infty$ verschwindet.
--- falsch
Wenn es für $t<0$ null ist; man nennt es auch antikausal. Der linksseitige Exponentialimpuls hat die Transformierte $\frac{1}{b+p}$ für $\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}$, also rechts der Geraden $\operatorname{Re} p=-\operatorname{Re} b$, wie jeder Exponentialimpuls, der für große $t$ abklingt.
--- falsch
Wenn es für $t>0$ null ist; man nennt es auch antikausal. Sein Konvergenzbereich ist dieselbe Halbebene $\operatorname{Re} p>-\operatorname{Re} b$ wie beim rechtsseitigen Impuls, weil der Betrag $|\mathrm{e}^{-pt}|$ nicht davon abhängt, auf welcher Seite der Zeitachse das Signal liegt.
--- falsch
Wenn es für $t>0$ null ist; man nennt es auch antikausal. Es hat keine Laplace-Transformierte, weil das Integral über $\mathrm{e}^{-bt}$ für $t\to-\infty$ für jedes $p$ über alle Grenzen wächst; man muss es vorher an der senkrechten Achse spiegeln.
:::
:::karte zusammenhang Ein Ausdruck, zwei Signale
Warum legt der Ausdruck $\frac{1}{b+p}$ allein noch nicht fest, welches Signal gemeint ist?
---
Rechts der Geraden $\operatorname{Re} p=-\operatorname{Re} b$ ist er das Integral über den rechtsseitigen Impuls $\mathrm{e}^{-bt}\varepsilon(t)$, links davon das Integral über den linksseitigen Impuls $-\mathrm{e}^{-bt}\varepsilon(-t)$. Die Grenzgerade durch den Pol teilt die Ebene in zwei Hälften, die zu verschiedenen Signalen gehören; erst der Konvergenzbereich entscheidet.
--- falsch
Weil man aus $\frac{1}{b+p}$ nur den Betrag des Signals ablesen kann, nicht sein Vorzeichen. Ob $\mathrm{e}^{-bt}\varepsilon(t)$ oder $-\mathrm{e}^{-bt}\varepsilon(t)$ gemeint ist, muss man deshalb zusätzlich angeben; der Konvergenzbereich ist für beide Signale derselbe Bereich rechts des Pols und hilft bei dieser Entscheidung nicht.
--- falsch
Weil $b$ komplex sein darf und $\frac{1}{b+p}$ dann zu einem reellen und einem komplexen Signal gehört. Welches gemeint ist, entscheidet der Imaginärteil von $b$: Ist er null, ist das Signal reell und rechtsseitig, sonst komplex und linksseitig, und zwar für alle $p$.
--- falsch
Weil der Ausdruck bei $p=-b$ nicht definiert ist und das Signal genau an dieser Stelle offenbleibt. Man ergänzt deshalb den Wert des Signals bei $t=0$; danach ist es eindeutig festgelegt, gleichgültig, auf welcher Seite der Grenzgeraden der Konvergenzbereich liegt.
:::
:::karte zusammenhang Linearität und Superposition
Warum enthält der Konvergenzbereich einer Summe $a_1s_1(t)+a_2s_2(t)$ den Durchschnitt der beiden einzelnen Konvergenzbereiche?
---
Das Laplace-Integral ist linear: $\mathcal{L}\{a_1s_1(t)+a_2s_2(t)\}=a_1S_1(p)+a_2S_2(p)$. Diese Gleichung gilt überall dort, wo beide Integrale konvergieren, also mindestens im Durchschnitt der beiden Bereiche.
--- falsch
Weil sich die Konvergenzbereiche bei einer Summe ebenfalls addieren: Der Bereich der Summe ist die Vereinigung beider Bereiche, und die enthält den Durchschnitt mit. Wo eines der beiden Integrale konvergiert, konvergiert auch die Summe.
--- falsch
Weil die Laplace-Transformierte einer Summe das Produkt der Transformierten ist, $S_1(p)\,S_2(p)$. Ein Produkt existiert nur dort, wo beide Faktoren existieren, also genau im Durchschnitt der beiden Bereiche.
--- falsch
Das Laplace-Integral ist linear, $\mathcal{L}\{a_1s_1+a_2s_2\}=a_1S_1+a_2S_2$, aber nur für positive Konstanten $a_1,a_2$. Für negative Konstanten kehrt sich der Konvergenzbereich um, und der Durchschnitt wird zur Vereinigung.
:::
:::karte formel Zweiseitiger Exponentialimpuls
Welche Laplace-Transformierte hat der zweiseitige Exponentialimpuls $\mathrm{e}^{-b|t|}$, und in welchem Bereich gilt sie?
---
$S_3(p)=\frac{1}{b+p}-\frac{1}{p-b}=\frac{2b}{b^2-p^2}$ für $-\operatorname{Re}\{b\}<\operatorname{Re}\{p\}<\operatorname{Re}\{b\}$: die Summe aus dem rechten Teil $\mathrm{e}^{-bt}\varepsilon(t)$ und dem linken Teil $\mathrm{e}^{bt}\cdot\varepsilon(-t)$, die beide zugleich nur in diesem Streifen konvergieren.
--- falsch
$S_3(p)=\frac{1}{b+p}+\frac{1}{p-b}=\frac{2p}{p^2-b^2}$ für $\operatorname{Re}\{p\}>|\operatorname{Re}\{b\}|$: die Summe aus dem rechten und dem linken Teil, die beide rechts beider Pole konvergieren, weil das Signal nach beiden Seiten abklingt.
--- falsch
$S_3(p)=\frac{2b}{b^2-p^2}$ für alle $p$ außer $\pm b$: Weil das Signal nach beiden Seiten abklingt, konvergiert das Integral überall in der $p$-Ebene, und nur die beiden Pole selbst sind ausgenommen.
--- falsch
$S_3(p)=\frac{2}{b+p}$ für $\operatorname{Re}\{p\}>-\operatorname{Re}\{b\}$: Wegen $|t|$ ist das Signal symmetrisch, die linke Hälfte trägt dasselbe bei wie die rechte, und man verdoppelt einfach die Transformierte des rechtsseitigen Impulses.
:::
:::karte begriff Streifen
Wann ist der Konvergenzbereich ein Streifen, und wann ist dieser Streifen beim zweiseitigen Exponentialimpuls $\mathrm{e}^{-b|t|}$ leer?
---
Bei einem zweiseitigen Signal: Der rechte Teil verlangt $\operatorname{Re} p>-\operatorname{Re} b$, der linke $\operatorname{Re} p<\operatorname{Re} b$, dazwischen liegt ein senkrechter Streifen. Er ist nur für $\operatorname{Re} b>0$ nicht leer. Für $\operatorname{Re} b\le0$ wächst das Signal nach mindestens einer Seite und hat keine Laplace-Transformierte.
--- falsch
Bei einem rechtsseitigen Signal, dessen Pole konjugiert komplex sind: Der Streifen liegt zwischen den beiden Polen. Beim zweiseitigen Exponentialimpuls ist er leer, wenn $b$ reell ist, weil dann beide Pole auf derselben senkrechten Geraden liegen.
--- falsch
Bei einem zweiseitigen Signal: Der rechte Teil verlangt $\operatorname{Re} p>-\operatorname{Re} b$, der linke $\operatorname{Re} p<\operatorname{Re} b$. Der Streifen ist nur für $\operatorname{Re} b<0$ nicht leer, weil das Signal dann nach beiden Seiten wächst und erst die Dämpfung $\mathrm{e}^{-\sigma t}$ es integrierbar macht.
--- falsch
Bei einem zweiseitigen Signal ist der Konvergenzbereich ein waagerechter Streifen um die reelle Achse, weil die beiden Hälften verschiedene Frequenzen haben. Er ist leer, wenn $b$ rein imaginär ist, weil das Signal dann auf keiner Seite abklingt.
:::
:::karte begriff Polstelle
Was ist eine Polstelle einer Laplace-Transformierten $S(p)$, und wo liegt sie, wenn $S(p)$ ein Bruch aus zwei Polynomen ist?
---
Eine Stelle $p$, an der $S(p)$ über alle Grenzen wächst, kurz Pol. Ist $S(p)$ ein Bruch aus zwei Polynomen in $p$, so sind die Pole die Nullstellen des Nennerpolynoms, sofern sie sich nicht gegen Nullstellen des Zählers kürzen.
--- falsch
Eine Stelle $p$, an der $S(p)$ null wird, kurz Pol. Ist $S(p)$ ein Bruch aus zwei Polynomen in $p$, so sind die Pole die Nullstellen des Zählerpolynoms, sofern sie sich nicht gegen Nullstellen des Nenners kürzen.
--- falsch
Ein Zeitpunkt $t$, an dem das Signal $s(t)$ springt oder unendlich wird, kurz Pol. Ist $S(p)$ ein Bruch aus zwei Polynomen, so liest man diese Zeitpunkte an den Nullstellen des Nennerpolynoms ab, gemessen in Sekunden.
--- falsch
Eine Stelle $p$, an der das Laplace-Integral gerade noch konvergiert, kurz Pol. Pole bilden deshalb ganze senkrechte Linien, nämlich die Grenzen des Konvergenzbereichs, und gehören selbst noch zum Konvergenzbereich dazu.
:::
:::karte zusammenhang Pole auf der Grenze des Konvergenzbereichs
Warum liegen die Pole einer Laplace-Transformierten auf den Grenzen ihres Konvergenzbereichs, aber nie in ihm?
---
Ein Pol liegt beim Exponenten $p_0$ eines Anteils $\mathrm{e}^{p_0t}$. Auf der Geraden $\operatorname{Re} p=\operatorname{Re} p_0$ hat der Integrand $\mathrm{e}^{(p_0-p)t}$ den konstanten Betrag 1: Die Probe gleicht Wachsen oder Abklingen genau aus, und das Integral konvergiert nicht. Deshalb endet der Konvergenzbereich genau an der Senkrechten durch den Pol.
--- falsch
Weil der Konvergenzbereich so definiert ist, dass man um jeden Pol einen kleinen Kreis ausspart. Die Grenzen des Bereichs sind die Ränder dieser Kreise, und weil die Kreise sehr klein sind, sehen sie in der Zeichnung wie senkrechte Geraden aus, die durch die Pole gehen.
--- falsch
Weil an einem Pol der Integrand selbst unendlich wird: Das Signal hat an dieser Stelle einen Dirac-Impuls. Das Integral über einen Dirac-Impuls konvergiert nur von einer Seite aus, deshalb bildet der Pol den Rand des Konvergenzbereichs und liegt nie in seinem Inneren.
--- falsch
Weil der Pol beim Kehrwert $1/p_0$ des Exponenten liegt. Auf der Geraden durch $1/p_0$ wechselt der Integrand sein Vorzeichen, und das Integral konvergiert nur auf einer Seite davon; die Grenze des Konvergenzbereichs verläuft deshalb genau durch den Pol.
:::
:::karte zusammenhang Abklingende Schwingung
Was liefert eine abklingende Schwingung wie $\mathrm{e}^{-t}\cdot\cos(3t)\cdot\varepsilon(t)$ in der Laplace-Transformierten, und woran sieht man Abklingen und Frequenz?
---
Ein Paar konjugiert komplexer Pole, hier $-1\pm3\mathrm{j}$, weil der Kosinus nach der Eulerschen Formel aus zwei Exponentialfunktionen besteht. Der Realteil $-1$ der Pole gehört zum Abklingen mit $\mathrm{e}^{-t}$, der Imaginärteil $\pm3$ zur Kreisfrequenz.
--- falsch
Einen einzelnen reellen Pol bei $-1$, weil der Kosinus reell ist, beschränkt bleibt und deshalb keine eigenen Pole hat. Das Abklingen liest man an diesem Pol ab, die Kreisfrequenz 3 dagegen an den beiden Nullstellen des Zählers.
--- falsch
Ein Paar konjugiert komplexer Pole bei $-3\pm\mathrm{j}$: Der Realteil gibt die Kreisfrequenz an, der Imaginärteil das Abklingen mit $\mathrm{e}^{-t}$, weil der Faktor $\mathrm{j}$ im Exponenten die Abklingrate kennzeichnet.
--- falsch
Zwei reelle Pole bei $-1$ und $-3$, je einen für jeden Faktor des Signals. Der Pol bei $-1$ gehört zum Abklingen, der Pol bei $-3$ zur Schwingung, deren Kreisfrequenz der Betrag dieses Pols ist.
:::
:::karte formel Grundpaare der Exponentialimpulse
Welche Transformierten haben die Exponentialimpulse $\mathrm{e}^{p_0t}\,\varepsilon(t)$ und $-\mathrm{e}^{p_0t}\,\varepsilon(-t)$ mit einer komplexen Zahl $p_0$, und wie folgt daraus der Sprung?
---
Beide haben den Ausdruck $\frac{1}{p-p_0}$: $\mathrm{e}^{p_0t}\,\varepsilon(t)$ für $\operatorname{Re} p>\operatorname{Re} p_0$, $-\mathrm{e}^{p_0t}\,\varepsilon(-t)$ für $\operatorname{Re} p<\operatorname{Re} p_0$. Mit $p_0=0$ folgt aus dem ersten der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$.
--- falsch
Beide haben den Ausdruck $\frac{1}{p-p_0}$, und beide gelten für $\operatorname{Re} p>\operatorname{Re} p_0$; das Minuszeichen beim linksseitigen Signal gleicht die Spiegelung der Zeitachse aus. Mit $p_0=0$ folgt der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für alle $p$.
--- falsch
$\mathrm{e}^{p_0t}\,\varepsilon(t)$ hat $\frac{1}{p-p_0}$ für $\operatorname{Re} p>\operatorname{Re} p_0$, $-\mathrm{e}^{p_0t}\,\varepsilon(-t)$ hat $\frac{1}{p+p_0}$ für $\operatorname{Re} p<-\operatorname{Re} p_0$, gespiegelt an der imaginären Achse. Mit $p_0=0$ folgt der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$.
--- falsch
Beide haben den Ausdruck $\frac{1}{p_0-p}$: $\mathrm{e}^{p_0t}\,\varepsilon(t)$ für $\operatorname{Re} p<\operatorname{Re} p_0$, $-\mathrm{e}^{p_0t}\,\varepsilon(-t)$ für $\operatorname{Re} p>\operatorname{Re} p_0$. Mit $p_0=0$ folgt aus dem ersten der Sprung: $\varepsilon(t)\leftrightarrow-1/p$ für $\operatorname{Re} p<0$.
:::
:::karte formel Dirac-Impuls und Rampe
Welche Laplace-Transformierten haben der Dirac-Impuls $\delta(t)$ und die Rampe $t\,\varepsilon(t)$, und wie erhält man sie?
---
$\delta(t)\longleftrightarrow1$ für alle $p$, wegen der Siebeigenschaft $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$: Der Impuls sitzt bei $t=0$, wo die Probe den Wert 1 hat. Dazu $t\,\varepsilon(t)\longleftrightarrow\frac{1}{p^2}$ für $\operatorname{Re} p>0$, durch partielle Integration.
--- falsch
$\delta(t)\longleftrightarrow0$ für alle $p$, weil der Dirac-Impuls außerhalb von $t=0$ überall null ist und das Integral verschwindet. Dazu $t\,\varepsilon(t)\longleftrightarrow\frac{1}{p}$ für $\operatorname{Re} p>0$, weil die Rampe das Integral des Sprungs ist.
--- falsch
$\delta(t)\longleftrightarrow1$ nur für $\operatorname{Re} p>0$, weil der Impuls bei $t=0$ sitzt und wie ein rechtsseitiges Signal behandelt wird. Dazu $t\,\varepsilon(t)\longleftrightarrow\frac{1}{p^2}$ für alle $p$, weil die Rampe keinen Pol hat.
--- falsch
$\delta(t)\longleftrightarrow\infty$ für alle $p$, weil der Dirac-Impuls bei $t=0$ unendlich hoch ist und das Integral diesen Wert übernimmt. Dazu $t\,\varepsilon(t)\longleftrightarrow\frac{1}{p^2}$ für $\operatorname{Re} p>0$, durch partielle Integration.
:::
:::karte zusammenhang Signal ohne Laplace-Transformierte
Warum hat die Konstante $s(t)=1$ für alle $t$ keine Laplace-Transformierte?
---
Die rechte Hälfte konvergiert nur für $\sigma>0$, die linke nur für $\sigma<0$. Beides zugleich geht nicht, der Konvergenzbereich ist leer. Eine Laplace-Transformierte haben aber nur Funktionen mit nicht leerem Konvergenzbereich.
--- falsch
Weil eine Konstante keine Exponentialfunktion ist und die Transformation nur Signale erfasst, die aus Exponentialfunktionen bestehen. Schreibt man die Konstante als $\mathrm{e}^{0\cdot t}$, hat sie dagegen die Transformierte $1/p$.
--- falsch
Weil eine Konstante unendlich viel Energie enthält und deshalb schon das Signal selbst nicht integrierbar ist. Jedes Signal, das nicht absolut integrierbar ist, hat keine Laplace-Transformierte, auch nicht der Sprung.
--- falsch
Die rechte Hälfte konvergiert nur für $\sigma<0$, die linke nur für $\sigma>0$, und beide Bereiche treffen sich nur auf der imaginären Achse. Dort ist der Integrand eine reine Schwingung, deren Integral nicht konvergiert.
:::
::::
