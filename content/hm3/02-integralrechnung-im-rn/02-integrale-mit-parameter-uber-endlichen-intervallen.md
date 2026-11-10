---
title: Integrale mit Parameter über endlichen Intervallen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralrechnung im Rⁿ
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn
knoten: Kapitel 2: Integralrechnung im Rⁿ
order: 3120200
summary: Hängt der Integrand außer von der Integrationsvariablen noch von einer weiteren Größe ab, dann hängt auch der Wert des Integrals von ihr ab.
tags: Riemann-Summe, bestimmte Integral, Integrand, Integrationsvariable, Zwischenstelle, Randpunkt, Rand, abgeschlossen
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Hängt der Integrand außer von der Integrationsvariablen noch von einer weiteren Größe ab, dann hängt auch der Wert des Integrals von ihr ab. Dieser Abschnitt klärt, wann diese neue Funktion stetig ist, wann man sie ableiten darf, indem man unter dem Integralzeichen ableitet, und was beim Ableiten hinzukommt, wenn auch die Grenzen des Integrals von der Größe abhängen.
:::

### Was du dafür brauchst: das bestimmte Integral

<span class="anker" id="stufe-1-1"></span>

Alles in diesem Kapitel baut auf dem Integral einer Funktion einer Variablen auf. Wichtig ist hier vor allem, *wie* es entsteht: als Grenzwert von Summen.

**Riemann-Summen.** Sei $u\colon[a,b]\to\mathbb{R}$ eine stetige Funktion. Man teilt das Intervall $[a,b]$ in $N$ gleich lange Stücke der Länge $\Delta t=(b-a)/N$. Im $k$-ten Stück wählt man eine Stelle $t_k$ und bildet das Rechteck mit der Breite $\Delta t$ und der Höhe $u(t_k)$. Die Summe der Rechteckflächen,

$$\sum_{k=1}^{N}u(t_k)\,\Delta t ,$$

heißt eine __Riemann-Summe__ von $u$. Rechtecke unter der $t$-Achse zählen dabei negativ.

**Das Integral.** Für stetiges $u$ streben die Riemann-Summen für $N\to\infty$ gegen eine Zahl, und zwar gleichgültig, wie man die Stellen $t_k$ in den Stücken wählt. Diese Zahl heißt das __bestimmte Integral__ von $u$ über $[a,b]$:

$$\int_a^b u(t)\,\mathrm{d} t=\lim_{N\to\infty}\sum_{k=1}^{N}u(t_k)\,\Delta t .$$

Die Funktion $u$ unter dem Integralzeichen heißt der __Integrand__. Die Variable $t$, über die integriert wird, heißt die __Integrationsvariable__. Sie kommt im Ergebnis nicht mehr vor, man darf sie deshalb beliebig umbenennen: $\int_a^bu(t)\,\mathrm{d} t=\int_a^bu(s)\,\mathrm{d} s$. Man vereinbart $\int_b^au(t)\,\mathrm{d} t=-\int_a^bu(t)\,\mathrm{d} t$ und $\int_a^au(t)\,\mathrm{d} t=0$.

**Rechenregeln.** Aus der Summe übertragen sich drei Regeln. Das Integral ist *linear*: $\int_a^b(\lambda_1u+\lambda_2v)\,\mathrm{d} t=\lambda_1\int_a^bu\,\mathrm{d} t+\lambda_2\int_a^bv\,\mathrm{d} t$ für Zahlen $\lambda_1,\lambda_2$. Es ist *monoton*: Aus $u\le v$ auf $[a,b]$ folgt $\int_a^bu\,\mathrm{d} t\le\int_a^bv\,\mathrm{d} t$. Es ist *additiv* bezüglich der Grenzen: $\int_a^cu\,\mathrm{d} t=\int_a^bu\,\mathrm{d} t+\int_b^cu\,\mathrm{d} t$. Aus der Monotonie folgt mit $-|u|\le u\le|u|$ die Abschätzung $\bigl|\int_a^bu\,\mathrm{d} t\bigr|\le\int_a^b|u|\,\mathrm{d} t$.

::::beispiel
$u(t)=t^2$ auf $[0,1]$ mit $N=4$ Stücken der Länge $\Delta t=\frac14$. Mit den rechten Enden $t_k=\frac k4$ ist die Riemann-Summe $\frac14\bigl(\frac1{16}+\frac4{16}+\frac9{16}+\frac{16}{16}\bigr)=\frac{15}{32}\approx0{,}469$, mit den linken Enden $\frac14\bigl(0+\frac1{16}+\frac4{16}+\frac9{16}\bigr)=\frac7{32}\approx0{,}219$. Mit $N=100$ und rechten Enden ergibt sich $0{,}33835$. Der Grenzwert ist $\int_0^1t^2\,\mathrm{d} t=\frac13$.
::::

⁠**Kurz gesagt:** Das Integral ist der Grenzwert der Rechtecksummen $\sum u(t_k)\,\Delta t$. Es ist linear, monoton und additiv in den Grenzen.

### Was du dafür brauchst: der Hauptsatz

<span class="anker" id="stufe-1-2"></span>

Ableiten und Integrieren heben sich gegenseitig auf. Das sagt der Hauptsatz der Differential- und Integralrechnung, der schon in [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) kurz vorkam. In diesem Kapitel wird er in beiden Richtungen gebraucht.

:::satz Satz 1.1 (Hauptsatz der Differential- und Integralrechnung)
<span class="anker" id="satz-1-1"></span>

<ol class="rm">

<li>

Ist $u$ stetig auf einem Intervall und $a$ ein Punkt darin, dann ist $s\mapsto\int_a^su(t)\,\mathrm{d} t$ differenzierbar mit

$$\frac{\mathrm{d}}{\mathrm{d} s}\int_a^su(t)\,\mathrm{d} t=u(s).$$

</li>

<li>

Ist $u$ stetig differenzierbar auf $[a,b]$, dann gilt $\int_a^bu'(t)\,\mathrm{d} t=u(b)-u(a)$.

</li>

</ol>
:::

⁠**So liest man das:** (i) Schiebt man die obere Grenze um ein kleines $h$ weiter, kommt ein Streifen der Breite $h$ und der Höhe ungefähr $u(s)$ hinzu. Die Fläche wächst also mit der Rate $u(s)$. Steht die Variable in der *unteren* Grenze, dreht sich das Vorzeichen um: $\frac{\mathrm{d}}{\mathrm{d} s}\int_s^bu(t)\,\mathrm{d} t=-u(s)$, denn $\int_s^b=-\int_b^s$. (ii) Eine Funktion mit der Ableitung $u$ heißt Stammfunktion von $u$ ([Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)). Man integriert also, indem man eine Stammfunktion an den Grenzen auswertet.

::::beispiel
$\int_0^st^2\,\mathrm{d} t=\frac{s^3}3$, und die Ableitung nach $s$ ist $s^2$, der Integrand an der oberen Grenze. Mit (ii): $\int_1^2 2t\,\mathrm{d} t=2^2-1^2=3$.
::::

⁠**Kurz gesagt:** Ein Integral nach seiner oberen Grenze abzuleiten ergibt den Integranden an dieser Grenze. Integrieren heißt, eine Stammfunktion an den Grenzen auszuwerten.

### Was du dafür brauchst: der Mittelwertsatz

<span class="anker" id="stufe-1-3"></span>

Mehrere Beweise in diesem Kapitel ersetzen einen Differenzenquotienten durch eine Ableitung. Das erlaubt der Mittelwertsatz der Differentialrechnung.

Man zeichnet den Graphen einer differenzierbaren Funktion zwischen zwei Stellen und verbindet die beiden Endpunkte durch eine Gerade, die Sekante. Irgendwo dazwischen hat der Graph eine Tangente, die zur Sekante parallel ist.

:::satz Satz 1.2 (Mittelwertsatz)
<span class="anker" id="satz-1-2"></span>

Ist $u$ auf einem Intervall differenzierbar und liegen $s$ und $s+h$ mit $h\neq0$ darin, dann gibt es eine Stelle $\tau$ zwischen $s$ und $s+h$ mit

$$\frac{u(s+h)-u(s)}{h}=u'(\tau).$$
:::

⁠**So liest man das:** Links steht die mittlere Steigung zwischen $s$ und $s+h$, die Steigung der Sekante. Rechts steht die Steigung an einer Stelle $\tau$ dazwischen. Der Satz sagt nur, dass es diese Stelle gibt, nicht, wo sie liegt. Sie heißt hier die __Zwischenstelle__.

::::beispiel
$u(t)=t^2$, $s=0$, $h=1$. Die mittlere Steigung ist $(1-0)/1=1$. Wegen $u'(\tau)=2\tau$ liegt die Zwischenstelle bei $\tau=\frac12$.
::::

⁠**Kurz gesagt:** Die mittlere Steigung zwischen zwei Stellen wird an einer Zwischenstelle als echte Steigung angenommen.

### Was du dafür brauchst: abgeschlossene, beschränkte und kompakte Mengen

<span class="anker" id="stufe-1-4"></span>

[Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat offene Mengen eingeführt: Um jeden ihrer Punkte passt eine kleine Kugel, die ganz in der Menge liegt. Für Integrale braucht man das Gegenstück, Mengen, die ihren Rand enthalten und nicht ins Unendliche reichen.

**Rand.** Sei $M\subset\mathbb{R}^n$ eine Menge. Ein Punkt $\boldsymbol{x}_0\in\mathbb{R}^n$ heißt __Randpunkt__ von $M$, wenn jede Kugel um $\boldsymbol{x}_0$, wie klein sie auch ist, sowohl Punkte von $M$ als auch Punkte außerhalb von $M$ enthält. Ein Randpunkt muss nicht selbst zu $M$ gehören. Die Menge aller Randpunkte heißt der __Rand__ von $M$.

**Abgeschlossen.** Die Menge $M$ heißt __abgeschlossen__, wenn sie alle ihre Randpunkte enthält.

**Beschränkt.** Die Menge $M$ heißt __beschränkt__, wenn sie in einer Kugel mit endlichem Radius liegt.

**Kompakt.** Eine Menge, die abgeschlossen und beschränkt ist, heißt __kompakt__.

::::beispiel
Das Intervall $[a,b]$ ist kompakt: Sein Rand besteht aus den Punkten $a$ und $b$, und beide gehören dazu. Das Intervall $(0,1]$ ist nicht abgeschlossen, denn sein Randpunkt $0$ fehlt. Das Intervall $[0,\infty)$ ist abgeschlossen, aber nicht beschränkt. Ein Rechteck $[a,b]\times[c,d]$ mit seinen Kanten und die Kreisscheibe $\{|\boldsymbol{x}|\le1\}$ mit ihrem Randkreis sind kompakt. Die Kreisscheibe $\{|\boldsymbol{x}|<1\}$ ohne Randkreis ist offen und deshalb nicht abgeschlossen.
::::

⁠**Kurz gesagt:** Kompakt heißt: Die Menge enthält ihren Rand und reicht nicht ins Unendliche.

### Was du dafür brauchst: Stetigkeit mit $\varepsilon$ und $\delta$

<span class="anker" id="stufe-1-5"></span>

[Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat Stetigkeit mit Folgen beschrieben: $f$ ist stetig in $\boldsymbol{x}_0$, wenn $f(\boldsymbol{x}_\nu)\to f(\boldsymbol{x}_0)$ für jede Folge $\boldsymbol{x}_\nu\to\boldsymbol{x}_0$ gilt. Für die Beweise dieses Kapitels ist eine gleichwertige Form bequemer, die mit Abständen arbeitet.

Man stellt sich ein Fenster um den Punkt $\boldsymbol{x}_0$ vor. Wer verlangt, dass sich der Funktionswert um weniger als einen vorgegebenen kleinen Betrag $\varepsilon$ ändert, dem kann man ein Fenster der Breite $\delta$ nennen, in dem das gilt.

:::satz Satz 1.3 (Stetigkeit mit $\varepsilon$ und $\delta$)
<span class="anker" id="satz-1-3"></span>

Eine Funktion $f$ auf einer Menge $M\subset\mathbb{R}^n$ ist genau dann stetig im Punkt $\boldsymbol{x}_0\in M$, wenn es zu jedem $\varepsilon>0$ ein $\delta>0$ gibt mit

$$|f(\boldsymbol{x})-f(\boldsymbol{x}_0)|<\varepsilon\quad\text{für alle }\boldsymbol{x}\in M\text{ mit }|\boldsymbol{x}-\boldsymbol{x}_0|<\delta .$$
:::

⁠**So liest man das:** $\varepsilon$ ist die erlaubte Abweichung des Funktionswerts, $\delta$ der erlaubte Abstand vom Punkt. Je kleiner $\varepsilon$, desto kleiner muss man in der Regel $\delta$ wählen. Das $\delta$ darf außer von $\varepsilon$ auch vom Punkt $\boldsymbol{x}_0$ abhängen.

::::beispiel
$f(x)=x^2$ im Punkt $x_0=1$. Für $|x-1|<1$ ist $|x+1|<3$, also $|x^2-1|=|x-1|\,|x+1|<3\,|x-1|$. Zu $\varepsilon>0$ passt deshalb $\delta=\min(1,\varepsilon/3)$. Zu $\varepsilon=0{,}3$ gehört $\delta=0{,}1$. Zur Kontrolle: $1{,}1^2-1=0{,}21$ und $1-0{,}9^2=0{,}19$, beide kleiner als $0{,}3$.
::::

:::hintergrund Warum die beiden Beschreibungen der Stetigkeit dasselbe sagen
Gilt die Bedingung mit $\varepsilon$ und $\delta$, und geht eine Folge $\boldsymbol{x}_\nu$ gegen $\boldsymbol{x}_0$, dann ist von einem Index an $|\boldsymbol{x}_\nu-\boldsymbol{x}_0|<\delta$ und damit $|f(\boldsymbol{x}_\nu)-f(\boldsymbol{x}_0)|<\varepsilon$. Weil $\varepsilon$ beliebig war, folgt $f(\boldsymbol{x}_\nu)\to f(\boldsymbol{x}_0)$. Umgekehrt: Gäbe es ein $\varepsilon>0$, zu dem kein $\delta$ passt, dann fände man zu jedem $\delta=1/\nu$ einen Punkt $\boldsymbol{x}_\nu$ mit $|\boldsymbol{x}_\nu-\boldsymbol{x}_0|<1/\nu$, aber $|f(\boldsymbol{x}_\nu)-f(\boldsymbol{x}_0)|\ge\varepsilon$. Diese Folge geht gegen $\boldsymbol{x}_0$, ihre Funktionswerte aber nicht gegen $f(\boldsymbol{x}_0)$. Das widerspricht der Stetigkeit im Sinn von [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html).
:::

⁠**Kurz gesagt:** Stetig heißt: Zu jeder erlaubten Abweichung $\varepsilon$ des Werts gibt es einen erlaubten Abstand $\delta$ vom Punkt.

### Was du dafür brauchst: gleichmäßige Stetigkeit

<span class="anker" id="stufe-1-6"></span>

In der Definition der Stetigkeit darf $\delta$ vom Punkt abhängen. Mehrere Beweise in diesem Kapitel brauchen aber ein $\delta$, das für alle Punkte zugleich passt.

Abb. [1](#abb-1) zeigt, warum das nicht selbstverständlich ist. Die Funktion $1/t$ ist auf $(0,1]$ stetig. Zwei Fenster gleicher Breite $\delta=0{,}1$ liefern aber sehr verschiedene Änderungen: Nahe $t=1$ ändert sich der Wert kaum, nahe $t=0$ sehr stark.

:::abbildung hm3/k2gleich 1
Die Funktion $1/t$ auf $(0,1]$. Beide getönten Fenster sind $\delta=0{,}1$ breit. Im rechten ändert sich der Wert um $0{,}11$, im linken um $2{,}67$. Je näher das Fenster am Nullpunkt liegt, desto schmaler muss es sein, damit sich der Wert um weniger als ein vorgegebenes $\varepsilon$ ändert.
:::

:::definition Definition 1.4 (Gleichmäßige Stetigkeit)
<span class="anker" id="satz-1-4"></span>

Eine Funktion $f$ auf einer Menge $M\subset\mathbb{R}^n$ heißt __gleichmäßig stetig__, wenn es zu jedem $\varepsilon>0$ ein $\delta>0$ gibt mit

$$|f(\boldsymbol{x})-f(\boldsymbol{y})|<\varepsilon\quad\text{für alle }\boldsymbol{x},\boldsymbol{y}\in M\text{ mit }|\boldsymbol{x}-\boldsymbol{y}|<\delta .$$
:::

⁠**So liest man das:** Der Unterschied zur Stetigkeit steckt in der Reihenfolge. Bei der Stetigkeit wählt man zuerst den Punkt und dann $\delta$. Hier wählt man $\delta$ zuerst, und es muss für alle Punkte zugleich passen.

::::beispiel
Auf $[0{,}1;\,1]$ ist $1/t$ gleichmäßig stetig, denn $\bigl|\frac1s-\frac1t\bigr|=\frac{|t-s|}{st}\le100\,|t-s|$. Das $\delta=\varepsilon/100$ passt überall. Auf $(0,1]$ dagegen nicht: Zu $\varepsilon=1$ und jedem $\delta<1$ liegen die Punkte $\delta/2$ und $\delta$ weniger als $\delta$ auseinander, ihre Werte unterscheiden sich aber um $\frac2\delta-\frac1\delta=\frac1\delta>1$.
::::

Auf kompakten Mengen kann das nicht passieren:

:::satz Satz 1.5 (Gleichmäßige Stetigkeit auf kompakten Mengen)
<span class="anker" id="satz-1-5"></span>

Jede stetige Funktion auf einer kompakten Menge ist gleichmäßig stetig.
:::

:::hintergrund Warum Kompaktheit genügt
Angenommen, $f$ ist auf der kompakten Menge $M$ stetig, aber nicht gleichmäßig stetig. Dann gibt es ein $\varepsilon>0$, zu dem kein $\delta$ passt. Zu jedem $\delta=1/\nu$ findet man also zwei Punkte $\boldsymbol{x}_\nu,\boldsymbol{y}_\nu\in M$ mit $|\boldsymbol{x}_\nu-\boldsymbol{y}_\nu|<1/\nu$, aber $|f(\boldsymbol{x}_\nu)-f(\boldsymbol{y}_\nu)|\ge\varepsilon$. Weil $M$ beschränkt ist, hat die Folge $\boldsymbol{x}_\nu$ eine Teilfolge, also eine Auswahl unendlich vieler ihrer Glieder in der ursprünglichen Reihenfolge, die gegen einen Punkt $\boldsymbol{x}^*$ konvergiert; das ist der Satz von Bolzano-Weierstraß. Weil $M$ abgeschlossen ist, gehört $\boldsymbol{x}^*$ zu $M$. Längs dieser Teilfolge gehen auch die $\boldsymbol{y}_\nu$ gegen $\boldsymbol{x}^*$. Wegen der Stetigkeit in $\boldsymbol{x}^*$ streben dann $f(\boldsymbol{x}_\nu)$ und $f(\boldsymbol{y}_\nu)$ beide gegen $f(\boldsymbol{x}^*)$, und ihr Abstand kann nicht immer mindestens $\varepsilon$ sein. Widerspruch.

Der Beweis zeigt den Mechanismus. Ein immer kleineres $\delta$ braucht man nur dort, wohin die schlechten Punktpaare laufen. Das kann ein Punkt sein, der der Menge fehlt, wie $0$ bei $1/t$ auf $(0,1]$; das verbietet die Abgeschlossenheit. Es kann das Unendliche sein, wie bei $x^2$ auf $\mathbb{R}$, wo $\delta$ für große $x$ immer kleiner werden muss; das verbietet die Beschränktheit. Bleibt nur ein Punkt der Menge selbst, und dort ist $f$ stetig.
:::

:::hintergrund Warum Riemann-Summen konvergieren
Mit der gleichmäßigen Stetigkeit erklärt sich, warum es im Unterabschnitt [1.1](#stufe-1-1) nicht darauf ankommt, wo in den Stücken man die Stellen $t_k$ wählt. Sei $u$ stetig auf $[a,b]$, also nach Satz [1.5](#satz-1-5) gleichmäßig stetig. Zu $\varepsilon>0$ gibt es ein $\delta$ wie in der Definition. Sind die Stücke kürzer als $\delta$, dann unterscheiden sich zwei Werte von $u$ im selben Stück um weniger als $\varepsilon$. Zwei Riemann-Summen zur selben Einteilung unterscheiden sich deshalb um weniger als $N\cdot\varepsilon\,\Delta t=\varepsilon\,(b-a)$. Mit derselben Abschätzung vergleicht man eine grobe Einteilung mit einer feineren und erhält, dass die Summen für $N\to\infty$ einen Grenzwert haben.
:::

⁠**Kurz gesagt:** Gleichmäßig stetig heißt: Ein $\delta$ passt für alle Punkte zugleich. Stetige Funktionen auf kompakten Mengen sind gleichmäßig stetig.

### Das Parameterintegral

<span class="anker" id="stufe-1-7"></span>

Oft hängt eine Kurve von einer Stellgröße ab. Für jeden festen Wert der Stellgröße hat die Kurve eine Fläche, und jeder Wert liefert eine andere Fläche. So entsteht eine Funktion der Stellgröße.

Abb. [2](#abb-2) zeigt das an den Kurven $t\mapsto\mathrm{e}^{-xt}$ auf $[0,1]$. Die Zahl $x$ ist die Dämpfung: Je größer sie ist, desto schneller fällt die Kurve, und desto kleiner ist die Fläche darunter. Jede Fläche wird rechts zu einem Punkt einer neuen Kurve.

:::abbildung hm3/k2schar 2
Links die Kurven $\mathrm{e}^{-xt}$ für $x=0$, $x=1$ und $x=3$. Rechts wird jede dieser Flächen zu einem Punkt auf der Kurve $F(x)$. Bei $x=1$ ist die Steigung von $F$ gleich $2/\mathrm{e}-1\approx-0{,}264$ (gestrichelt die Tangente).
:::

Für eine Menge $\mathcal U\subset\mathbb{R}^n$ und ein Intervall $[a,b]$ schreibt man $\mathcal U\times[a,b]$ für die Menge aller Paare $(\boldsymbol{x},t)$ mit $\boldsymbol{x}\in\mathcal U$ und $t\in[a,b]$. Eine Funktion $f\colon\mathcal U\times[a,b]\to\mathbb{R}$ hat also $n+1$ Argumente, $x_1$ bis $x_n$ und $t$.

:::definition Definition 1.6 (Parameterintegral)
<span class="anker" id="satz-1-6"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\times[a,b]\to\mathbb{R}$ stetig. Die Funktion

<span class="anker" id="gl-1-1"></span>
$$F(\boldsymbol{x})=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t,\qquad\boldsymbol{x}\in\mathcal U, \tag{1.1}$$

heißt __Parameterintegral__. Die Größe $\boldsymbol{x}$ heißt __Parameter__.
:::

⁠**So liest man das:** Für jeden festen Parameter $\boldsymbol{x}$ ist $t\mapsto f(\boldsymbol{x},t)$ eine stetige Funktion einer Variablen, und $F(\boldsymbol{x})$ ist ihr Integral. Über $t$ wird integriert, $t$ verschwindet dabei. Übrig bleibt eine Funktion des Parameters.

::::beispiel Abklingkurven
Für $f(x,t)=\mathrm{e}^{-xt}$ auf $\mathbb{R}\times[0,1]$ ist für $x\neq0$

<span class="anker" id="gl-1-2"></span>
$$F(x)=\int_0^1\mathrm{e}^{-xt}\,\mathrm{d} t=\Bigl[-\frac{\mathrm{e}^{-xt}}x\Bigr]_{t=0}^{1}=\frac{1-\mathrm{e}^{-x}}x,\qquad\text{und}\quad F(0)=\int_0^11\,\mathrm{d} t=1 . \tag{1.2}$$

Zum Beispiel ist $F(1)=1-\mathrm{e}^{-1}\approx0{,}632$ und $F(3)=(1-\mathrm{e}^{-3})/3\approx0{,}317$. In diesem Kapitel heißt dieses Beispiel das Beispiel der *Abklingkurven*.
::::

⁠**Kurz gesagt:** Ein Parameterintegral ist eine Funktion des Parameters, deren Wert die Fläche unter der Kurve zu diesem Parameter ist.

### Die Stetigkeit des Parameterintegrals

<span class="anker" id="stufe-1-8"></span>

Ändert man den Parameter ein wenig, ändert sich die Kurve ein wenig. Ändert sich dann auch die Fläche nur ein wenig?

Ändern sich alle Werte $f(\boldsymbol{x},t)$ zugleich, für alle $t$, um weniger als $\varepsilon$, dann ändert sich die Fläche um höchstens $\varepsilon\,(b-a)$. Das Wort „zugleich“ ist dabei entscheidend, und es kommt aus der gleichmäßigen Stetigkeit.

:::satz Satz 1.7 (Stetigkeit von Parameterintegralen)
<span class="anker" id="satz-1-7"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\times[a,b]\to\mathbb{R}$ stetig. Dann ist das Parameterintegral $F(\boldsymbol{x})=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t$ stetig in $\mathcal U$.
:::

:::beweis Gleichmäßige Stetigkeit auf einem kompakten Stück
Sei $\boldsymbol{x}\in\mathcal U$. Weil $\mathcal U$ offen ist, liegt eine Kugel um $\boldsymbol{x}$ mit einem Radius $\rho>0$ ganz in $\mathcal U$. Die kleinere Kugel mit Rand, $B=\{\boldsymbol{y}:|\boldsymbol{y}-\boldsymbol{x}|\le\rho/2\}$, liegt dann ebenfalls in $\mathcal U$. Die Menge $B\times[a,b]$ ist abgeschlossen und beschränkt, also kompakt. Nach Satz [1.5](#satz-1-5) ist $f$ dort gleichmäßig stetig. Zu $\varepsilon>0$ gibt es also ein $\delta>0$ mit $\delta\le\rho/2$, sodass

$$|f(\boldsymbol{y},t)-f(\boldsymbol{x},t)|<\varepsilon\quad\text{für alle }t\in[a,b],\quad\text{falls }|\boldsymbol{y}-\boldsymbol{x}|<\delta .$$

Denn die Punkte $(\boldsymbol{y},t)$ und $(\boldsymbol{x},t)$ haben den Abstand $|\boldsymbol{y}-\boldsymbol{x}|$. Mit der Abschätzung aus Unterabschnitt [1.1](#stufe-1-1) folgt für diese $\boldsymbol{y}$

$$|F(\boldsymbol{y})-F(\boldsymbol{x})|=\Bigl|\int_a^b\bigl(f(\boldsymbol{y},t)-f(\boldsymbol{x},t)\bigr)\mathrm{d} t\Bigr|\le\int_a^b|f(\boldsymbol{y},t)-f(\boldsymbol{x},t)|\,\mathrm{d} t\le\varepsilon\,(b-a).$$

Weil $\varepsilon$ beliebig war, ist $F$ in $\boldsymbol{x}$ stetig.
:::

::::beispiel
Die Abklingkurven [(1.2)](#gl-1-2): $\mathrm{e}^{-xt}$ ist auf $\mathbb{R}\times[0,1]$ stetig, also ist $F$ auf ganz $\mathbb{R}$ stetig, auch im Punkt $x=0$, an dem die Formel $(1-\mathrm{e}^{-x})/x$ nicht erklärt ist. Zur Kontrolle: Wegen $\mathrm{e}^{-x}=1-x+\frac{x^2}2-\dots$ ist $(1-\mathrm{e}^{-x})/x=1-\frac x2+\dots$, und das geht für $x\to0$ gegen $1=F(0)$.
::::

::::beispiel [Gegenbeispiel]
Ohne die Stetigkeit von $f$ kann die Fläche springen. Sei

$$f(x,t)=\frac1{|x|}\,\mathrm{e}^{-t/|x|}\quad\text{für }x\neq0,\qquad f(0,t)=0,\qquad t\in[0,1].$$

Für $x\neq0$ ist $F(x)=\bigl[-\mathrm{e}^{-t/|x|}\bigr]_{t=0}^{1}=1-\mathrm{e}^{-1/|x|}$. Für $x\to0$ geht das gegen $1$, aber $F(0)=0$. Also ist $F$ im Nullpunkt nicht stetig. Die Kurven werden für $x\to0$ zu einer immer schmaleren und höheren Spitze bei $t=0$, deren Fläche gegen $1$ geht (Abb. [3](#abb-3)). Die Funktion $f$ ist im Punkt $(0,0)$ nicht stetig, denn $f(x,0)=1/|x|$ wächst über alle Grenzen.

:::abbildung hm3/k2spitze 3
Die Kurven $f(x,t)=\frac1x\,\mathrm{e}^{-t/x}$ für $x=1$, $x=\frac12$ und $x=\frac15$. Für $x\to0$ wird die Kurve zu einer Spitze bei $t=0$, die immer höher und schmaler wird. An jeder Stelle $t>0$ geht der Wert gegen null, die Fläche aber gegen $1$.
:::
::::

:::hintergrund Wohin die Fläche im Gegenbeispiel verschwindet
An jeder festen Stelle $t>0$ geht $f(x,t)=\frac1{|x|}\mathrm{e}^{-t/|x|}$ für $x\to0$ gegen null, denn die $\mathrm{e}$-Funktion fällt schneller, als $1/|x|$ wächst. Die Kurve geht also an jeder Stelle gegen die Nullfunktion, deren Fläche $0$ ist. Trotzdem bleibt die Fläche nahe $1$: Sie sammelt sich in einem immer schmaleren Streifen bei $t=0$ und entkommt dort nach oben. Genau das verhindert die Stetigkeit von $f$ auf der kompakten Menge $B\times[a,b]$ im Beweis: Eine gleichmäßig stetige Funktion kann keine Spitze bilden, die bei kleinen Änderungen des Parameters beliebig hoch wird. Die Fläche ändert sich dann höchstens um $\varepsilon\,(b-a)$, egal wo die Änderung sitzt.
:::

⁠**Kurz gesagt:** Ist der Integrand stetig in Parameter und Integrationsvariable zusammen, dann ist das Parameterintegral stetig.

### Ableiten unter dem Integralzeichen

<span class="anker" id="stufe-1-9"></span>

Wie schnell ändert sich die Fläche, wenn man den Parameter verstellt? Oft lässt sich das Integral nicht geschlossen ausrechnen, und man möchte die Ableitung trotzdem kennen.

Dreht man den Parameter $x$ in Abb. [2](#abb-2) um ein kleines $\Delta x$ weiter, dann ändert sich die Kurve an jeder Stelle $t$ um ungefähr $\frac{\partial f}{\partial x}(x,t)\,\Delta x$. Die Fläche ändert sich um die Summe all dieser kleinen Änderungen. Teilt man durch $\Delta x$, erwartet man: Die Ableitung der Fläche ist das Integral der partiellen Ableitung des Integranden.

:::satz Satz 1.8 (Ableiten unter dem Integralzeichen)
<span class="anker" id="satz-1-8"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\times[a,b]\to\mathbb{R}$ stetig. Sind für alle $k=1,\dots,n$ die partiellen Ableitungen

$$\frac{\partial f}{\partial x_k}\colon\mathcal U\times[a,b]\to\mathbb{R}$$

stetig, dann ist $F(\boldsymbol{x})=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t$ stetig differenzierbar in $\mathcal U$, und für alle $\boldsymbol{x}\in\mathcal U$ und $k=1,\dots,n$ gilt

<span class="anker" id="gl-1-3"></span>
$$\frac{\partial F}{\partial x_k}(\boldsymbol{x})=\int_a^b\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\,\mathrm{d} t . \tag{1.3}$$
:::

⁠**So liest man das:** Links wird zuerst integriert und dann nach $x_k$ abgeleitet, rechts zuerst abgeleitet und dann integriert. Die partielle Ableitung $\partial f/\partial x_k$ ist die aus [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html): Alle anderen Variablen, auch $t$, werden festgehalten. Beide Operationen sind Grenzwerte, die Formel vertauscht also zwei Grenzwerte. Voraussetzung ist, dass $f$ und alle $\partial f/\partial x_k$ als Funktionen von $(\boldsymbol{x},t)$ *zusammen* stetig sind.

:::beweis Ableitung und Integral vertauschen
Die Stetigkeit von $F$ ist Satz [1.7](#satz-1-7). Es bleibt die Ableitung.

⁠**Schritt 1: Differenzenquotient.** Fixiere $\boldsymbol{x}\in\mathcal U$ und $k$. Weil $\mathcal U$ offen ist, gibt es ein $h_0>0$ mit $\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k\in\mathcal U$ für alle $|h|\le h_0$. Das Integral ist linear, also ist für $0<|h|\le h_0$

$$\frac{F(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})}h=\int_a^b\frac{f(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k,t)-f(\boldsymbol{x},t)}h\,\mathrm{d} t .$$

⁠**Schritt 2: Mittelwertsatz.** Für festes $t$ ist $s\mapsto f(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k,t)$ eine differenzierbare Funktion einer Variablen mit der Ableitung $\frac{\partial f}{\partial x_k}(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k,t)$. Nach Satz [1.2](#satz-1-2) gibt es eine Zwischenstelle $\tau_h(t)$ zwischen $0$ und $h$ mit

$$\frac{f(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k,t)-f(\boldsymbol{x},t)}h=\frac{\partial f}{\partial x_k}\bigl(\boldsymbol{x}+\tau_h(t)\,\hat{\boldsymbol{e}}_k,t\bigr).$$

Die Zwischenstelle hängt von $t$ ab; man kennt sie nicht, man weiß nur $|\tau_h(t)|\le|h|$.

⁠**Schritt 3: gleichmäßige Stetigkeit.** Die Funktion $(s,t)\mapsto\frac{\partial f}{\partial x_k}(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k,t)$ ist stetig auf der kompakten Menge $[-h_0,h_0]\times[a,b]$, also nach Satz [1.5](#satz-1-5) gleichmäßig stetig. Zu jedem $\varepsilon>0$ gibt es daher ein $\delta>0$, das *nicht von $t$ abhängt*, mit

$$\Bigl|\frac{\partial f}{\partial x_k}(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k,t)-\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\Bigr|<\varepsilon\quad\text{für alle }t\in[a,b],\quad\text{falls }|s|<\delta .$$

⁠**Schritt 4: Grenzübergang.** Für $0<|h|<\delta$ ist $|\tau_h(t)|<\delta$ für jedes $t$. Mit den Schritten 1 und 2 folgt

$$\Bigl|\frac{F(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})}h-\int_a^b\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\,\mathrm{d} t\Bigr|\le\int_a^b\varepsilon\,\mathrm{d} t=\varepsilon\,(b-a).$$

Weil $\varepsilon$ beliebig war, geht der Differenzenquotient für $h\to0$ gegen das Integral in [(1.3)](#gl-1-3). Also existiert $\partial F/\partial x_k$. Nach Satz [1.7](#satz-1-7), angewendet auf die stetige Funktion $\partial f/\partial x_k$, ist diese partielle Ableitung stetig. Stetige partielle Ableitungen machen $F$ nach [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) stetig differenzierbar.
:::

::::beispiel
Für die Abklingkurven [(1.2)](#gl-1-2) ist $\partial_x\mathrm{e}^{-xt}=-t\,\mathrm{e}^{-xt}$, stetig auf $\mathbb{R}\times[0,1]$. Also ist

$$F'(x)=-\int_0^1t\,\mathrm{e}^{-xt}\,\mathrm{d} t .$$

Im Punkt $x=0$ ergibt das $F'(0)=-\int_0^1t\,\mathrm{d} t=-\frac12$; aus der Formel $(1-\mathrm{e}^{-x})/x$ bekäme man diesen Wert nur über einen Grenzwert. Im Punkt $x=1$ liefert partielle Integration $\int_0^1t\,\mathrm{e}^{-t}\,\mathrm{d} t=1-\frac2{\mathrm{e}}$, also $F'(1)=\frac2{\mathrm{e}}-1\approx-0{,}264$. Ableiten von $(1-\mathrm{e}^{-x})/x$ ergibt denselben Wert. Das ist die Steigung der Tangente in Abb. [2](#abb-2).
::::

⁠**Grenzfall:** Hängt $f$ nicht von $\boldsymbol{x}$ ab, ist $F$ konstant, und beide Seiten von [(1.3)](#gl-1-3) sind null.

:::hintergrund Warum man Ableitung und Integral vertauschen darf
Für eine endliche Summe ist die Vertauschung nur die Summenregel: Die Ableitung von $\sum_kf(\boldsymbol{x},t_k)\,\Delta t$ ist $\sum_k\partial_{x_k}f(\boldsymbol{x},t_k)\,\Delta t$. Das Integral ist aber der Grenzwert solcher Summen, und die Ableitung ist ebenfalls ein Grenzwert. Zwei Grenzwerte darf man im Allgemeinen nicht vertauschen. Der Beweis zeigt, was es hier erlaubt: In Schritt 3 hängt $\delta$ nicht von $t$ ab. Die Differenzenquotienten nähern sich also an *allen* Stellen $t$ zugleich der Ableitung. Dann ist auch der Fehler im Integral klein, höchstens $\varepsilon\,(b-a)$. Diese Gleichzeitigkeit liefert die gleichmäßige Stetigkeit auf der kompakten Menge $[-h_0,h_0]\times[a,b]$.

Was ohne sie geschieht, zeigt die Funktion $f(x,t)=\frac x{|x|}\,t\,\mathrm{e}^{-t/\sqrt{|x|}}$ für $x\neq0$, $f(0,t)=0$, auf $t\in[0,1]$. Sie ist stetig, und ihre partielle Ableitung nach $x$ existiert überall. Im Nullpunkt ist der Differenzenquotient $f(h,t)/h=\frac t{|h|}\mathrm{e}^{-t/\sqrt{|h|}}$. Für jedes feste $t$ geht er gegen null, also ist $\frac{\partial f}{\partial x}(0,t)=0$ und $\int_0^1\frac{\partial f}{\partial x}(0,t)\,\mathrm{d} t=0$. Als Funktion von $t$ ist dieser Differenzenquotient aber eine Spitze bei $t=\sqrt{|h|}$ mit der Höhe $1/(\mathrm{e}\sqrt{|h|})$, und ihre Fläche geht für $h\to0$ gegen $1$. Tatsächlich ist $F(x)=x\bigl(1-(1+1/\sqrt{|x|})\,\mathrm{e}^{-1/\sqrt{|x|}}\bigr)$ und $F'(0)=1$. Die Ableitung $\partial f/\partial x$ ist im Nullpunkt nicht stetig, und die Differenzenquotienten entkommen wie die Spitze in Abb. [3](#abb-3).
:::

⁠**Kurz gesagt:** Sind Integrand und seine partiellen Ableitungen nach dem Parameter stetig, dann darf man unter dem Integralzeichen ableiten.

### Parameter aus einem abgeschlossenen Intervall

<span class="anker" id="stufe-1-10"></span>

Oft ist der Parameter eine Zahl aus einem abgeschlossenen Intervall $[c,d]$, etwa weil der Integrand außerhalb gar nicht erklärt ist. An den Enden des Intervalls kann man nur von einer Seite herankommen.

Eine Funktion $F$ auf $[c,d]$ heißt im Punkt $c$ __rechtsseitig differenzierbar__, wenn der Grenzwert $\lim_{h\searrow0}\frac{F(c+h)-F(c)}h$ existiert. Dabei bedeutet $h\searrow0$, dass $h$ nur positive Werte annimmt. Entsprechend heißt $F$ in $d$ linksseitig differenzierbar, wenn $\lim_{h\nearrow0}\frac{F(d+h)-F(d)}h$ mit negativen $h$ existiert. Die Funktion heißt stetig differenzierbar auf $[c,d]$, wenn sie im Inneren differenzierbar ist, an den Enden einseitig, und wenn die Ableitung auf ganz $[c,d]$ stetig ist.

:::satz Satz 1.9 (Parameterintegrale mit abgeschlossenem Parameterintervall)
<span class="anker" id="satz-1-9"></span>

Ist $f\colon[a,b]\times[c,d]\to\mathbb{R}$ stetig, dann ist $F(y)=\int_a^bf(x,y)\,\mathrm{d} x$ stetig auf $[c,d]$. Existiert ferner $\partial f/\partial y$ auf $[a,b]\times[c,d]$, an den Rändern $y=c$ und $y=d$ als rechts- beziehungsweise linksseitige Ableitung, und ist dort stetig, dann ist $F$ stetig differenzierbar auf $[c,d]$ mit $F'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,\mathrm{d} x$.
:::

⁠**So liest man das:** Das ist Satz [1.8](#satz-1-8) für einen Parameter $y$, mit zwei Unterschieden: Die Integrationsvariable heißt jetzt $x$, und der Parameterbereich ist abgeschlossen statt offen. Der Beweis bleibt derselbe; an den Enden nimmt man im Differenzenquotienten nur $h$ einer Sorte. Die kompakte Menge im Beweis ist jetzt das ganze Rechteck $[a,b]\times[c,d]$.

::::beispiel
$F(y)=\int_0^1\ln(x+y)\,\mathrm{d} x$ für $y\in[1,2]$. Der Integrand und $\partial_y\ln(x+y)=\frac1{x+y}$ sind auf $[0,1]\times[1,2]$ stetig. Am linken Ende ist also die rechtsseitige Ableitung

$$F'(1)=\int_0^1\frac{\mathrm{d} x}{x+1}=\ln2\approx0{,}693 .$$

Zur Kontrolle: Es ist $F(y)=(1+y)\ln(1+y)-y\ln y-1$ und $F'(y)=\ln\frac{1+y}y$, bei $y=1$ also $\ln2$.
::::

⁠**Kurz gesagt:** Auch mit einem abgeschlossenen Parameterintervall darf man unter dem Integral ableiten; an den Enden sind einseitige Ableitungen gemeint.

### Grenzen, die vom Parameter abhängen: die Leibnizregel

<span class="anker" id="stufe-1-11"></span>

Oft hängen auch die Integrationsgrenzen vom Parameter ab. Dann ändert sich beim Verstellen des Parameters nicht nur die Kurve, sondern auch das Stück, über das man integriert.

Das Integral $F(y)=\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$ ist eine Fläche mit beweglichen Rändern. Ändert sich $y$ um ein kleines $\Delta y$, geschehen drei Dinge (Abb. [4](#abb-4)). Die Kurve hebt oder senkt sich; das ändert die Fläche um ungefähr $\Delta y\int_\alpha^\beta\frac{\partial f}{\partial y}\,\mathrm{d} x$. Die rechte Grenze rückt um ungefähr $\beta'(y)\,\Delta y$ vor; dort kommt ein Streifen der Höhe $f(\beta(y),y)$ hinzu. Die linke Grenze rückt um ungefähr $\alpha'(y)\,\Delta y$ vor; dort fällt ein Streifen der Höhe $f(\alpha(y),y)$ weg.

:::abbildung hm3/k2leibniz 4
Die drei Beiträge zur Änderung der Fläche. Das Band zwischen den beiden Kurven gehört zum Integral über $\partial f/\partial y$. Der rechte Streifen ist der positive Randterm, der linke der negative. Alle drei sind für kleine $\Delta y$ ungefähr proportional zu $\Delta y$.
:::

Für die Voraussetzungen braucht man ein Wort: Eine offene Menge, die eine Menge $D$ enthält, heißt eine __Umgebung__ von $D$.

:::satz Satz 1.10 (Leibnizregel)
<span class="anker" id="satz-1-10"></span>

Seien $\alpha,\beta\colon[c,d]\to\mathbb{R}$ stetig differenzierbar und $f$ stetig differenzierbar in einer Umgebung von

$$D=\{(x,y)\in\mathbb{R}^2:\ \alpha(y)\le x\le\beta(y),\ c\le y\le d\}.$$

Dann ist $F(y):=\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$ stetig differenzierbar auf $[c,d]$, und es gilt

<span class="anker" id="gl-1-4"></span>
$$F'(y)=\int_{\alpha(y)}^{\beta(y)}\frac{\partial f}{\partial y}(x,y)\,\mathrm{d} x+f\bigl(\beta(y),y\bigr)\,\beta'(y)-f\bigl(\alpha(y),y\bigr)\,\alpha'(y). \tag{1.4}$$

Sind nur $f$, $\alpha$ und $\beta$ stetig, dann ist $F$ immerhin stetig. Für die stetige Differenzierbarkeit von $F$ genügt es, zusätzlich die Existenz und Stetigkeit von $\partial f/\partial y$, $\alpha'$ und $\beta'$ vorauszusetzen.
:::

⁠**So liest man das:** Der erste Term ist die Änderung der Kurve bei festen Grenzen, also Satz [1.9](#satz-1-9). Der zweite ist die Höhe am rechten Rand mal die Geschwindigkeit, mit der dieser Rand wandert. Der dritte ist dasselbe am linken Rand, mit Minus, weil ein nach rechts wandernder linker Rand Fläche abschneidet.

:::herleitung Kettenregel und Hauptsatz
Setze $J(p,q,y):=\int_p^qf(x,y)\,\mathrm{d} x$ für $p,q$ nahe bei $\alpha(y)$ und $\beta(y)$. Dann ist $F(y)=J\bigl(\alpha(y),\beta(y),y\bigr)$, eine Verkettung im Sinn von [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html). Die partiellen Ableitungen von $J$ sind:

<ul>

<li>

$\partial J/\partial q=f(q,y)$ nach dem Hauptsatz, Satz [1.1](#satz-1-1) (i);

</li>

<li>

$\partial J/\partial p=-f(p,y)$ ebenfalls nach dem Hauptsatz, denn $\int_p^q=-\int_q^p$;

</li>

<li>

$\partial J/\partial y=\int_p^q\frac{\partial f}{\partial y}(x,y)\,\mathrm{d} x$ nach Satz [1.9](#satz-1-9).

</li>

</ul>

Alle drei sind stetige Funktionen von $(p,q,y)$. Nach [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist $J$ dann differenzierbar, und die Kettenregel aus [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) gibt

$$F'(y)=\frac{\partial J}{\partial p}\,\alpha'(y)+\frac{\partial J}{\partial q}\,\beta'(y)+\frac{\partial J}{\partial y}.$$

Einsetzen ergibt [(1.4)](#gl-1-4). Alle drei Terme sind stetig in $y$, also ist $F'$ stetig. Sind nur $f$, $\alpha$, $\beta$ stetig, dann ist $J$ stetig in $(p,q,y)$, und als Verkettung stetiger Funktionen ist $F$ stetig.
:::

::::beispiel
Bei $F(y)=\int_0^y\mathrm{e}^{-xy}\,\mathrm{d} x$ für $y>0$ steckt $y$ im Integranden und in der oberen Grenze. Mit $\alpha(y)=0$ und $\beta(y)=y$ ergibt [(1.4)](#gl-1-4)

$$F'(y)=-\int_0^yx\,\mathrm{e}^{-xy}\,\mathrm{d} x+\mathrm{e}^{-y^2}.$$

Bei $y=1$ ist $\int_0^1x\,\mathrm{e}^{-x}\,\mathrm{d} x=1-\frac2{\mathrm{e}}$, also $F'(1)=-\bigl(1-\frac2{\mathrm{e}}\bigr)+\frac1{\mathrm{e}}=\frac3{\mathrm{e}}-1\approx0{,}104$. Zur Kontrolle: Es ist $F(y)=(1-\mathrm{e}^{-y^2})/y$, und Ableiten ergibt bei $y=1$ denselben Wert.
::::

⁠**Grenzfälle:** Bei festen Grenzen ist $\alpha'=\beta'=0$, und es bleibt Satz [1.9](#satz-1-9). Hängt $f$ nicht von $y$ ab, bleibt $F'=f(\beta)\,\beta'-f(\alpha)\,\alpha'$, der Hauptsatz mit der Kettenregel. Bei $\alpha=\beta$ ist $F=0$, und die beiden Randterme heben sich auf.

⁠**Warum differenzierbare Grenzen?** Das Integral $F(y)=\int_0^{|y|}1\,\mathrm{d} x=|y|$ ist stetig, aber bei $y=0$ nicht differenzierbar. Der Knick steckt in der Grenze $\beta(y)=|y|$.

:::hintergrund Warum nicht erst integrieren und dann ableiten?
Wenn der Integrand eine Stammfunktion in geschlossener Form hat, geht das und liefert dasselbe. Die Leibnizregel hilft im anderen Fall: Sie gibt die Ableitung von $F$ an, auch wenn sich $F$ selbst nicht geschlossen hinschreiben lässt. In Aufgabe [3](#aufg-3) hat der Integrand keine elementare Stammfunktion, die Ableitung ist trotzdem ein geschlossener Ausdruck. In der Elektrotechnik hat die Antwort eines Systems, das zur Zeit null eingeschaltet wird, oft genau diese Bauart: Die Zeit steckt im Integranden und in der oberen Grenze. Aufgabe [4](#aufg-4) zeigt, wie die Leibnizregel daraus eine Differentialgleichung macht.
:::

⁠**Kurz gesagt:** Wandern die Grenzen mit, kommt zur Ableitung unter dem Integral an jedem Rand ein Term „Höhe mal Geschwindigkeit des Rands“ hinzu, am linken Rand mit Minus.

### Aufgaben

<span class="anker" id="stufe-1-12"></span>

:::aufgabe Aufgabe 1 ★ Ein Integral durch Ableiten
<span class="anker" id="aufg-1"></span>

Zeige mit [(1.3)](#gl-1-3), dass für die Abklingkurven [(1.2)](#gl-1-2) $\int_0^1t^2\,\mathrm{e}^{-xt}\,\mathrm{d} t=F''(x)$ gilt. Berechne damit $\int_0^1t^2\,\mathrm{e}^{-t}\,\mathrm{d} t$ ohne partielle Integration.

:::loesung
Der Integrand $f(x,t)=\mathrm{e}^{-xt}$ und seine Ableitungen $\partial_xf=-t\,\mathrm{e}^{-xt}$ und $\partial_x^2f=t^2\,\mathrm{e}^{-xt}$ sind auf $\mathbb{R}\times[0,1]$ stetig. Nach [(1.3)](#gl-1-3) ist $F'(x)=-\int_0^1t\,\mathrm{e}^{-xt}\,\mathrm{d} t$. Das ist wieder ein Parameterintegral mit stetigem Integranden und stetiger Ableitung nach $x$, also darf man noch einmal unter dem Integral ableiten:

$$F''(x)=\int_0^1\partial_x\bigl(-t\,\mathrm{e}^{-xt}\bigr)\mathrm{d} t=\int_0^1t^2\,\mathrm{e}^{-xt}\,\mathrm{d} t .$$

Aus $F(x)=(1-\mathrm{e}^{-x})/x$ folgt für $x\neq0$

$$F'(x)=\frac{(x+1)\mathrm{e}^{-x}-1}{x^2},\qquad F''(x)=\frac{2-(x^2+2x+2)\mathrm{e}^{-x}}{x^3}.$$

Bei $x=1$ ist also $\int_0^1t^2\,\mathrm{e}^{-t}\,\mathrm{d} t=F''(1)=2-\frac5{\mathrm{e}}\approx0{,}161$. Zweimal partiell integrieren ergibt denselben Wert.
:::
:::

:::aufgabe Aufgabe 2 ★★ Die wandernde Spitze
<span class="anker" id="aufg-2"></span>

Auf $[0,1]\times[0,1]$ sei $f(x,t)=x/(x^2+t^2)$ für $(x,t)\neq(0,0)$ und $f(0,0)=0$.

<ol class="al">

<li>

Berechne $F(x)=\int_0^1f(x,t)\,\mathrm{d} t$ für $x>0$ und für $x=0$.

</li>

<li>

Ist $F$ bei $x=0$ stetig? Welche Voraussetzung von Satz [1.9](#satz-1-9) fehlt, und an wie vielen Punkten?

</li>

<li>

Was macht die Kurve $t\mapsto f(x,t)$ für $x\searrow0$ bei $t=0$? Warum geht dabei keine Fläche verloren, solange $x>0$ ist?

</li>

</ol>

:::loesung
(a) Für $x>0$ ist $\frac{x}{x^2+t^2}$ die Ableitung von $\arctan(t/x)$ nach $t$, also $F(x)=\bigl[\arctan(t/x)\bigr]_{t=0}^{1}=\arctan(1/x)$. Für $x=0$ ist $f(0,t)=0$ für alle $t$, also $F(0)=0$.

(b) $\lim_{x\searrow0}F(x)=\lim_{x\searrow0}\arctan(1/x)=\frac\pi2\neq0=F(0)$. Also ist $F$ bei $x=0$ nicht stetig. Es fehlt die Stetigkeit von $f$ auf dem kompakten Rechteck $[0,1]\times[0,1]$, und zwar in dem einen Punkt $(0,0)$: Dort hat $f$ keinen Grenzwert, denn $f(x,0)=1/x$ wächst über alle Grenzen, während $f(0,t)=0$ ist. An allen anderen Punkten ist $f$ stetig.

(c) Bei $t=0$ hat die Kurve die Höhe $1/x$, und bei $t=x$ ist sie schon auf die Hälfte gefallen, $f(x,x)=\frac1{2x}$. Für $x\searrow0$ entsteht also eine immer höhere und schmalere Spitze bei $t=0$. Ihre Fläche $\arctan(1/x)$ geht dabei gegen $\frac\pi2$: Die Fläche sammelt sich in der Spitze, sie verschwindet nicht, solange $x>0$ ist. Erst bei $x=0$ ist die Spitze weg, und die Fläche springt auf null. Das ist der Fluchtweg „nach oben“ aus Abb. [7](uneigentliche-parameterintegrale.html#abb-7).
:::
:::

:::aufgabe Aufgabe 3 ★ Ableiten ohne Stammfunktion
<span class="anker" id="aufg-3"></span>

Sei $F(y)=\int_y^{y^2}\frac{\mathrm{e}^{xy}}x\,\mathrm{d} x$ für $y\ge1$. Berechne $F'(y)$ als geschlossenen Ausdruck. Welchen Wert hat $F'(1)$?

:::loesung
Hier ist $\alpha(y)=y$, $\beta(y)=y^2$ und $f(x,y)=\mathrm{e}^{xy}/x$ mit $\partial_yf=\mathrm{e}^{xy}$. Auf $D$ ist $x\ge y\ge1$, und in der Umgebung $x>\frac12$ von $D$ ist $f$ stetig differenzierbar. Aus [(1.4)](#gl-1-4):

$$F'(y)=\int_y^{y^2}\mathrm{e}^{xy}\,\mathrm{d} x+\frac{\mathrm{e}^{y^3}}{y^2}\cdot2y-\frac{\mathrm{e}^{y^2}}y\cdot1=\frac{\mathrm{e}^{y^3}-\mathrm{e}^{y^2}}y+\frac{2\mathrm{e}^{y^3}}y-\frac{\mathrm{e}^{y^2}}y=\frac{3\mathrm{e}^{y^3}-2\mathrm{e}^{y^2}}y .$$

Bei $y=1$ ist $F'(1)=3\mathrm{e}-2\mathrm{e}=\mathrm{e}$. Eine Stammfunktion von $\mathrm{e}^{xy}/x$ nach $x$ gibt es nicht in elementarer Form, $F$ selbst lässt sich also nicht geschlossen angeben, wohl aber $F'$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Ein eingeschaltetes System
<span class="anker" id="aufg-4"></span>

Sei $u\colon[0,\infty)\to\mathbb{R}$ stetig und

$$v(t)=\int_0^t\mathrm{e}^{-(t-s)}\,u(s)\,\mathrm{d} s,\qquad t\ge0 .$$

<ol class="al">

<li>

Zeige mit der Leibnizregel, dass $v'(t)+v(t)=u(t)$ und $v(0)=0$ gilt. Prüfe dazu, welche Voraussetzungen des Satzes erfüllt sein müssen.

</li>

<li>

Berechne $v$ für $u(s)=1$ und für $u(s)=s$ direkt und prüfe die Gleichung aus (a).

</li>

</ol>

:::loesung
(a) Integrationsvariable ist $s$, Parameter ist $t$. Der Integrand $f(s,t)=\mathrm{e}^{-(t-s)}u(s)$ ist stetig, und seine partielle Ableitung $\partial_tf(s,t)=-\mathrm{e}^{-(t-s)}u(s)$ ist ebenfalls stetig. Die Grenzen $\alpha(t)=0$ und $\beta(t)=t$ sind stetig differenzierbar mit $\alpha'=0$, $\beta'=1$. Damit $f$ in einer Umgebung des Bereichs $\{0\le s\le t\le d\}$ erklärt ist, setzt man $u$ durch $u(s)=u(0)$ für $s<0$ stetig fort; am Ergebnis ändert das nichts, weil die untere Grenze fest bei $0$ liegt. Nach dem letzten Satz der Leibnizregel genügen diese Voraussetzungen, und [(1.4)](#gl-1-4) ergibt

$$v'(t)=\int_0^t\bigl(-\mathrm{e}^{-(t-s)}u(s)\bigr)\mathrm{d} s+f(t,t)\cdot1-f(0,t)\cdot0=-v(t)+u(t).$$

Also ist $v'+v=u$. Außerdem ist $v(0)=\int_0^0\dots\,\mathrm{d} s=0$. So wird aus dem Integral eine Differentialgleichung erster Ordnung mit dem Anfangswert null.

(b) Für $u=1$: $v(t)=\mathrm{e}^{-t}\int_0^t\mathrm{e}^s\,\mathrm{d} s=\mathrm{e}^{-t}(\mathrm{e}^t-1)=1-\mathrm{e}^{-t}$. Dann ist $v'+v=\mathrm{e}^{-t}+1-\mathrm{e}^{-t}=1=u$ und $v(0)=0$. Für $u(s)=s$: Mit $\int s\,\mathrm{e}^s\,\mathrm{d} s=(s-1)\mathrm{e}^s$ ist

$$v(t)=\mathrm{e}^{-t}\Bigl[(s-1)\mathrm{e}^s\Bigr]_0^t=\mathrm{e}^{-t}\bigl((t-1)\mathrm{e}^t+1\bigr)=t-1+\mathrm{e}^{-t}.$$

Dann ist $v'(t)=1-\mathrm{e}^{-t}$ und $v'+v=t=u(t)$, und $v(0)=0$.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Ein Skalarpotential durch Integrieren
<span class="anker" id="aufg-5"></span>

Sei $\boldsymbol{F}=(F_1,F_2)$ ein stetig differenzierbares Vektorfeld auf $\mathbb{R}^2$ mit $\frac{\partial F_1}{\partial y}=\frac{\partial F_2}{\partial x}$, also $\operatorname{rot}\boldsymbol{F}=0$ im Sinn von [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html). Setze

$$\varphi(x,y)=\int_0^xF_1(s,0)\,\mathrm{d} s+\int_0^yF_2(x,s)\,\mathrm{d} s .$$

<ol class="al">

<li>

Zeige $\partial\varphi/\partial y=F_2$ mit dem Hauptsatz.

</li>

<li>

Zeige $\partial\varphi/\partial x=F_1$. Leite dazu das zweite Integral mit Satz [1.8](#satz-1-8) nach $x$ ab und benutze die Voraussetzung.

</li>

<li>

Berechne $\varphi$ für $\boldsymbol{F}=(2xy+1,\;x^2+3y^2)$ und prüfe $\nabla\varphi=\boldsymbol{F}$.

</li>

</ol>

:::loesung
(a) Der erste Summand hängt nicht von $y$ ab. Im zweiten steht $y$ als obere Grenze, und $s\mapsto F_2(x,s)$ ist stetig. Nach dem Hauptsatz, Satz [1.1](#satz-1-1) (i), ist $\frac{\partial\varphi}{\partial y}(x,y)=F_2(x,y)$.

(b) Den ersten Summanden leitet man nach dem Hauptsatz nach seiner oberen Grenze $x$ ab und erhält $F_1(x,0)$. Im zweiten ist $x$ ein Parameter aus der offenen Menge $\mathbb{R}$, und integriert wird über das feste Intervall zwischen $0$ und $y$. Der Integrand $F_2(x,s)$ und seine partielle Ableitung $\partial F_2/\partial x$ sind stetig, also gilt nach Satz [1.8](#satz-1-8) mit der Voraussetzung und Teil (ii) des Hauptsatzes

$$\frac\partial{\partial x}\int_0^yF_2(x,s)\,\mathrm{d} s=\int_0^y\frac{\partial F_2}{\partial x}(x,s)\,\mathrm{d} s=\int_0^y\frac{\partial F_1}{\partial s}(x,s)\,\mathrm{d} s=F_1(x,y)-F_1(x,0).$$

Für $y<0$ gilt dasselbe, denn $\int_0^y=-\int_y^0$. Zusammen ist $\frac{\partial\varphi}{\partial x}=F_1(x,0)+F_1(x,y)-F_1(x,0)=F_1(x,y)$. Damit ist $\nabla\varphi=\boldsymbol{F}$: Auf der ganzen Ebene genügt $\operatorname{rot}\boldsymbol{F}=0$ für ein Skalarpotential. Die Formel integriert erst längs der $x$-Achse und dann senkrecht nach oben; dazu muss dieser Weg ganz im Gebiet liegen. Beim Feld aus [Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) auf $\mathbb{R}^2\setminus\{0\}$ ist das nicht für alle Punkte der Fall.

(c) Die Voraussetzung gilt: $\partial F_1/\partial y=2x=\partial F_2/\partial x$. Es ist $F_1(s,0)=1$ und $F_2(x,s)=x^2+3s^2$, also

$$\varphi(x,y)=\int_0^x1\,\mathrm{d} s+\int_0^y(x^2+3s^2)\,\mathrm{d} s=x+x^2y+y^3 .$$

Kontrolle: $\nabla\varphi=(1+2xy,\;x^2+3y^2)=\boldsymbol{F}$.
:::
:::
