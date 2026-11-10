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
