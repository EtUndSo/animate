---
title: Die Laplace-Transformation
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220100
summary: Jedes Signal als Überlagerung von $\ee^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: Wachstumsrate, Frequenz, absolut integrierbares, Dichte, Partialbruchzerlegung, Stabilität, Eigenbewegung
lang: de
---

## Worum es geht

:::frage Ich habe die Rechnung verstanden, wie man vom Faltungsintegral mit einer Eigenfunktion auf $H(p)$ kommt. Ich glaube aber, dass hinter der Laplace-Transformation viel mehr steckt als diese Rechenvorschrift: dass jede beliebige Funktion als Summe komplexer e-Funktionen dargestellt werden kann.
Die Vermutung trifft den Kern. Ohne sie wäre die Eigenfunktions-Rechnung nur eine Kuriosität, denn sie gilt zunächst nur für das eine Signal $\mathrm{e}^{pt}$. Erst weil sich (fast) jedes Signal aus solchen Bausteinen zusammensetzen lässt, folgt aus ihr eine Aussage über *jedes* Eingangssignal. Drei Präzisierungen machen die Vermutung exakt:

<ol>

<li>

Im Allgemeinen ist es keine Summe, sondern ein *Integral*: unendlich viele Bausteine $\mathrm{e}^{pt}$, jeder mit einem infinitesimalen Gewicht. Die Bausteine liegen auf einer senkrechten Linie $\operatorname{Re} p=\sigma$ der $p$-Ebene (Stufe [2](#stufe-2)).

</li>

<li>

Nicht jede Funktion, sondern jede, für die ein Konvergenzbereich existiert: Sie darf auf jeder Seite der Zeitachse höchstens exponentiell wachsen, und eine einzige Dämpfung muss beide Seiten zugleich bändigen (Abschnitt [2.3](#stufe-2-3)).

</li>

<li>

Ist $S(p)$ ein Bruch aus Polynomen, wird aus dem Integral tatsächlich eine *endliche Summe* $\sum_r A_r\,\mathrm{e}^{p_r t}$. Die Exponenten $p_r$ sind die Pole von $S(p)$ (Stufe [4](#stufe-4)).

</li>

</ol>
:::

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Ein LTI-System kann den Baustein $\mathrm{e}^{pt}$ nur mit einer Zahl $H(p)$ multiplizieren, weil bei $\mathrm{e}^{pt}$ Verschieben dasselbe ist wie Multiplizieren.

</li>

<li>

Jedes Signal mit Konvergenzbereich ist eine Überlagerung solcher Bausteine. $S(p)$ gibt an, mit welchem Gewicht der Baustein $\mathrm{e}^{pt}$ im Signal steckt.

</li>

<li>

Deshalb wird aus der Faltung eine Multiplikation, $G(p)=H(p)\,S(p)$. Bei rationalem $S(p)$ ist das Signal eine endliche Summe $\sum_r A_r\mathrm{e}^{p_r t}$ mit den Polen als Exponenten.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast jedes Ergebnis zur Laplace-Transformation ist eine Folge dieser drei Sätze. Die Tabelle ordnet zu, die Stufen erklären.

| Ergebnis | Woher es kommt |
|---|---|
| Eigenfunktion $\mathrm{e}^{pt}$, Übertragungsfunktion $H(p)$ | Verschieben von $\mathrm{e}^{pt}$ ist Multiplizieren mit $\mathrm{e}^{-p\tau}$ (Stufe [1](#stufe-1)) |
| Laplace-Transformierte $S(p)$ | Gewicht des Bausteins $\mathrm{e}^{pt}$ im Signal (Stufe [2](#stufe-2)) |
| Konvergenzbereich | die Dämpfungen $\sigma$, mit denen $s(t)\mathrm{e}^{-\sigma t}$ absolut integrierbar wird (Abschnitt [2.3](#stufe-2-3)) |
| Faltung $\to$ Produkt, Kettenschaltung | jeder Baustein wird mit $H(p)$ multipliziert (Stufe [3](#stufe-3)) |
| Ableitung $\to p$, Integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ und $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (Stufe [3](#stufe-3)) |
| Differentialgleichung $\to$ Polynombruch | jede Ableitung wird ein Faktor $p$ (Stufe [3](#stufe-3)) |
| Pole, Partialbrüche | die Exponenten und Gewichte der endlich vielen Bausteine (Stufe [4](#stufe-4)) |
| Stabilität | ein kausaler Baustein $\mathrm{e}^{p_r t}$ klingt nur ab, wenn $\operatorname{Re} p_r<0$ (Stufe [4](#stufe-4)) |
| Fourier-Transformation | dieselbe Überlagerung auf der Linie $\sigma=0$ (Stufe [2](#stufe-2)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
Alle Beispiele benutzen dieselben zwei Bausteine:

<ul>

<li>

einen **RC-Tiefpass** mit $RC=1$ s (zum Beispiel $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Seine Impulsantwort und seine Übertragungsfunktion sind

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

mit $t$ in s und $p$ in $1/\mathrm{s}$;

</li>

<li>

den **Einheitssprung** $s(t)=\varepsilon(t)$ mit $S(p)=1/p$ für $\operatorname{Re} p>0$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap2.py` nach.
:::

## Stufe 1: Warum gerade $\mathrm{e}^{pt}$

<span class="anker" id="stufe-1"></span>

:::zweck
Setzt man $\mathrm{e}^{pt}$ ins Faltungsintegral ein, kommt $H(p)\,\mathrm{e}^{pt}$ heraus: $\mathrm{e}^{pt}$ ist eine Eigenfunktion. Hier geht es darum, welche Eigenschaft von $\mathrm{e}^{pt}$ das erzwingt und warum die Bausteine komplex sein müssen.
:::

**Die Idee.** Das Faltungsintegral

$$g(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau$$

liest sich so: Der Ausgang ist eine Summe *verzögerter Kopien* des Eingangs. Die Kopie mit der Verzögerung $\tau$ geht mit dem Gewicht $h(\tau)\,\mathrm{d}\tau$ ein. Bei einer beliebigen Signalform sieht jede verzögerte Kopie anders aus als das Original, und die Summe hat eine neue Form. Bei $\mathrm{e}^{pt}$ nicht:

$$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt}.$$

Die Verzögerung um $\tau$ wirkt wie die Multiplikation mit der *konstanten Zahl* $\mathrm{e}^{-p\tau}$. Alle Kopien sind Vielfache derselben Funktion $\mathrm{e}^{pt}$, also auch ihre Summe:

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{pt}*h(t)=\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)}=H(p)\,\mathrm{e}^{pt}. \tag{1.1}$$

⁠**Kurz gesagt:** $\mathrm{e}^{pt}$ ist eine Eigenfunktion, weil für $\mathrm{e}^{pt}$ Verschieben dasselbe ist wie Multiplizieren.

**Was $p$ bedeutet.** Mit $p=\sigma+\mathrm{j}2\pi f$ zerfällt der Baustein in zwei Faktoren:

$$\mathrm{e}^{pt}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{e}^{\sigma t}\bigl[\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)\bigr].$$

Der Realteil $\sigma$ (in $1/\mathrm s$) ist die __Wachstumsrate__: Für $\sigma<0$ klingt der Baustein ab, für $\sigma=0$ schwingt er mit konstanter Amplitude, für $\sigma>0$ wächst er. Der Imaginärteil $2\pi f$ legt die __Frequenz__ der Schwingung fest. Jeder Punkt der $p$-Ebene ist also ein Baustein, und die Lage des Punkts sagt, wie er aussieht (Abb. [1](#abb-1)).

:::abbildung et3/k2bausteine
Die $p$-Ebene als Landkarte der Bausteine. Links vier Punkte $p$, rechts jeweils der Realteil $\operatorname{Re}\{\mathrm{e}^{pt}\}=\mathrm{e}^{\sigma t}\cos(2\pi ft)$ mit der Hüllkurve $\pm\mathrm{e}^{\sigma t}$ (gestrichelt). Die Punkte b, c, d haben $2\pi f=\pi/\mathrm s$, also $f=0{,}5$ Hz. Der Abstand von der imaginären Achse bestimmt Abklingen oder Wachsen, die Höhe die Frequenz.
:::

:::frage Warum komplex? Ein Sinus ist doch auch ein einfaches Signal.
Ein Sinus wird beim Verschieben nicht nur skaliert. Mit $\omega_0=2\pi f_0$ gilt

$$\sin\bigl(\omega_0(t-\tau)\bigr)=\cos(\omega_0\tau)\,\sin(\omega_0t)-\sin(\omega_0\tau)\,\cos(\omega_0t).$$

Es entsteht ein Kosinusanteil, die verzögerte Kopie hat eine andere Form. Deshalb antwortet ein System auf $\sin(\omega_0t)$ mit $|H|\sin(\omega_0t+\varphi)$: Amplitude *und Phase* ändern sich. Eine Phasenverschiebung lässt sich nicht als Multiplikation mit einer reellen Zahl schreiben, wohl aber als Multiplikation mit der komplexen Zahl $\mathrm{e}^{\mathrm{j}\varphi}$. Deshalb sind die Bausteine komplex: Die eine Zahl $H(p)$ trägt Betrag und Phase. Ein reeller Sinus besteht aus zwei Bausteinen, $\sin(\omega_0t)=\bigl(\mathrm{e}^{\mathrm{j}\omega_0t}-\mathrm{e}^{-\mathrm{j}\omega_0t}\bigr)/(2\mathrm{j})$, und jeder von ihnen wird mit seiner eigenen Zahl multipliziert (Aufgabe [1](#aufg-1)d).
:::

:::frage Warum ist $\mathrm{e}^{pt}$ für *jedes* LTI-System eine Eigenfunktion, obwohl die Systeme so verschieden sind?
Die Form der Eigenfunktion folgt nur aus der Zeitinvarianz (Verschieben = Multiplizieren), und die haben alle LTI-Systeme gemeinsam. Vom System hängt nur der Faktor $H(p)$ ab, denn in ihn gehen die Gewichte $h(\tau)$ ein. Deshalb dient *ein* Satz von Bausteinen allen LTI-Systemen zugleich. Das macht die Laplace-Transformation universell.
:::

:::zusatz Nur Exponentialfunktionen haben diese Eigenschaft
Gesucht ist eine differenzierbare Funktion $x(t)$ mit $x(0)=1$, deren verschobene Kopien Vielfache von ihr selbst sind: $x(t+u)=c(u)\,x(t)$ für alle $t,u$. Mit $t=0$ folgt $c(u)=x(u)$, also $x(t+u)=x(t)\,x(u)$. Ableiten nach $u$ an der Stelle $u=0$ ergibt $x'(t)=x'(0)\,x(t)$. Das ist die Differentialgleichung $x'=p\,x$ mit $p=x'(0)$, und ihre Lösung mit $x(0)=1$ ist $x(t)=\mathrm{e}^{pt}$. Es gibt also keine anderen Bausteine mit dieser Eigenschaft.
:::

:::frage Sind e-Funktionen die einzigen möglichen Eigenfunktionen von LTI-Systemen?
Man muss zwei Fragen trennen.

⁠**Eigenfunktion *aller* LTI-Systeme zugleich: ja, nur $c\,\mathrm{e}^{pt}$.** Das ideale Laufzeitglied $g(t)=s(t-u)$ ist selbst ein LTI-System, und zwar für jede Verzögerung $u$. Eine Funktion, die Eigenfunktion jedes LTI-Systems ist, muss also bei jeder Verschiebung in ein Vielfaches ihrer selbst übergehen. Das erfüllt nach dem Kasten oben nur $\mathrm{e}^{pt}$.

⁠**Eigenfunktion eines *bestimmten* Systems: nicht nur.** Das System multipliziert jeden Baustein $\mathrm{e}^{p_kt}$ mit seiner eigenen Zahl $H(p_k)$. Eine Summe $\sum_kc_k\mathrm{e}^{p_kt}$ bleibt genau dann ein Vielfaches ihrer selbst, wenn alle diese Faktoren gleich sind, $H(p_k)=\lambda$. Der gemeinsame Faktor $\lambda$ ist dann der Eigenwert. Zwei Beispiele:

<ul>

<li>

Ideales Laufzeitglied um $T$: $H(p)=\mathrm{e}^{-pT}$ hat an allen Stellen $p_k=\mathrm{j}2\pi k/T$ denselben Wert 1. Jedes Signal mit der Periode $T$ ist eine Eigenfunktion mit dem Eigenwert 1, denn $s(t-T)=s(t)$.

</li>

<li>

Idealer Tiefpass ohne Laufzeit, $H(f)=1$ im ganzen Durchlassbereich: Jedes Signal, dessen Spektrum ganz im Durchlassbereich liegt, kommt unverändert heraus und ist eine Eigenfunktion mit dem Eigenwert 1.

</li>

</ul>

Beim RC-Glied dagegen nimmt $H(p)=1/(1+pRC)$ jeden Wert nur einmal an. Dort sind die einzelnen $c\,\mathrm{e}^{pt}$ (mit $p$ im Konvergenzbereich) die einzigen Eigenfunktionen, die sich aus Bausteinen zusammensetzen lassen.

⁠**Kurz gesagt:** $\mathrm{e}^{pt}$ ist die einzige Eigenfunktion, die *jedes* LTI-System hat. Ein einzelnes System kann zusätzlich Mischungen von Bausteinen als Eigenfunktionen haben, wenn es alle diese Bausteine mit derselben Zahl multipliziert.
:::

:::ltspice Eine Eigenfunktion im Experiment
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg` von `in` nach `out`, `cap` mit `1u` nach Masse). Als Quelle eine Verhaltensquelle `bv` mit `V=exp(-time/2)`, der Baustein mit $p=-0{,}5/\mathrm s$.

⁠**Direktiven:** `.tran 0 10 0 1m` und `.ic V(out)=X` mit einer Zahl für $X$: Der Kondensator startet bei $X$ Volt. Lass dir mit „Add Traces“ den Ausdruck `V(out)/V(in)` zeichnen.

⁠**Was du siehst:** Setzt du für $X$ den Wert, den dein Ergebnis aus Aufgabe [1](#aufg-1)(b) bei $t=0$ hat, ist das Verhältnis von Anfang an konstant: Der Ausgang ist eine Zahl mal der Eingang. Mit $X=0$ nähert es sich derselben Zahl erst nach einigen Sekunden. Der Grund: Ein Eingang, der schon immer anlag, hätte den Kondensator bei $t=0$ genau auf diesen Wert geladen. Jede andere Anfangsspannung baut das RC-Glied mit $\mathrm{e}^{-t}$ ab, schneller als der Eingang mit $\mathrm{e}^{-t/2}$ abklingt.

⁠**Zu (d):** Quelle `voltage` mit `SINE(0 1 {1/(2*pi)} 0 0 90)`, das ist $\cos t$. Vergleiche Amplitude und Nacheilung von `V(out)` nach dem Einschwingen mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(d).
:::

:::aufgabe Aufgabe 1 ★ Eigenfunktion oder nicht?
<span class="anker" id="aufg-1"></span>

Benutze den RC-Tiefpass des Rechenmodells, $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Berechne $H(p)=\int h(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. Für welche $p$ konvergiert das Integral, und warum hängt das nur von $\operatorname{Re} p$ ab?

</li>

<li>

Eingang $s(t)=\mathrm{e}^{-t/2}$ für alle $t$. Berechne den Ausgang einmal direkt mit dem Faltungsintegral und einmal mit $H(p)$. Welches $p$ hat dieser Baustein?

</li>

<li>

Eingang $s(t)=t$ für alle $t$. Zeige mit dem Faltungsintegral, dass $g(t)=t-1$ herauskommt. Warum ist $t$ keine Eigenfunktion, obwohl der Ausgang ähnlich aussieht? Was bedeutet die $-1$ für den Kondensator?

</li>

<li>

Eingang $s(t)=\cos t$ (also $\omega_0=1/\mathrm s$). Zerlege den Kosinus in zwei Bausteine, multipliziere jeden mit seinem $H(p)$ und setze wieder zusammen. Zeige, dass $g(t)=A\cos(t+\varphi)$ ist, und bestimme $A$ und $\varphi$. Ist $\cos t$ eine Eigenfunktion?

</li>

</ol>

⁠*Tipp zu (c):* $\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau=1$ und $\int_0^\infty\tau\,\mathrm{e}^{-\tau}\mathrm{d}\tau=1$.

:::loesung
(a) $H(p)=\int_0^\infty\mathrm{e}^{-\tau}\mathrm{e}^{-p\tau}\mathrm{d}\tau=\int_0^\infty\mathrm{e}^{-(p+1)\tau}\mathrm{d}\tau=\dfrac{1}{p+1}$. Das Integral konvergiert genau dann, wenn $|\mathrm{e}^{-(p+1)\tau}|=\mathrm{e}^{-(\sigma+1)\tau}$ abklingt, also für $\operatorname{Re} p>-1$. Der Betrag hängt nur von $\sigma$ ab, weil $|\mathrm{e}^{-\mathrm{j}2\pi f\tau}|=1$ ist.

(b) Direkt:

$$g(t)=\int_0^\infty\mathrm{e}^{-\tau}\,\mathrm{e}^{-(t-\tau)/2}\mathrm{d}\tau=\mathrm{e}^{-t/2}\int_0^\infty\mathrm{e}^{-\tau/2}\mathrm{d}\tau=2\,\mathrm{e}^{-t/2}.$$

Mit $H(p)$: Der Baustein hat $p=-\tfrac12$ (reell, ohne Schwingung). Es liegt im Konvergenzbereich, $H(-\tfrac12)=1/(\tfrac12)=2$, also $g(t)=2\,\mathrm{e}^{-t/2}$. Beide Wege stimmen überein (numerisch: $g(1\,\mathrm{s})=1{,}2131$).

(c) $g(t)=\int_0^\infty\mathrm{e}^{-\tau}(t-\tau)\mathrm{d}\tau=t\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau-\int_0^\infty\tau\mathrm{e}^{-\tau}\mathrm{d}\tau=t-1$. Das ist kein Vielfaches von $t$: Die verzögerten Kopien $t-\tau$ sind keine Vielfachen von $t$ (der Faktor $1-\tau/t$ hängt von $t$ selbst ab). Der Ausgang ist die *verschobene* Rampe: Die Kondensatorspannung folgt der Eingangsrampe mit einer Verzögerung von $RC=1$ s. Gestalt gleich, aber verschoben statt skaliert, also keine Eigenfunktion.

(d) $\cos t=\tfrac12\mathrm{e}^{\mathrm{j} t}+\tfrac12\mathrm{e}^{-\mathrm{j} t}$, Bausteine bei $p=\pm\mathrm{j}$, beide im Konvergenzbereich ($\operatorname{Re} p=0>-1$).

$$H(\mathrm{j})=\frac{1}{1+\mathrm{j}}=\frac{1}{\sqrt2}\,\mathrm{e}^{-\mathrm{j}\pi/4},\qquad H(-\mathrm{j})=H(\mathrm{j})^*=\frac{1}{\sqrt2}\,\mathrm{e}^{+\mathrm{j}\pi/4}.$$

$$g(t)=\tfrac12H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}+\tfrac12H(-\mathrm{j})\mathrm{e}^{-\mathrm{j} t}=\operatorname{Re}\bigl\{H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}\bigr\}=\frac{1}{\sqrt2}\cos\Bigl(t-\frac\pi4\Bigr).$$

Also $A=1/\sqrt2\approx0{,}707$ und $\varphi=-45^\circ$ (numerisch: $g(1\,\mathrm{s})=0{,}6909$). Jeder der beiden komplexen Bausteine ist eine Eigenfunktion, ihre Summe $\cos t$ nicht: Die beiden Bausteine werden mit *verschiedenen* Zahlen multipliziert, $H(\mathrm{j})\neq H(-\mathrm{j})$. Dadurch verschiebt sich die Phase.
:::
:::

## Stufe 2: Ein Signal aus lauter Bausteinen

<span class="anker" id="stufe-2"></span>

:::zweck
Stufe [1](#stufe-1) gilt für einen einzelnen Baustein. Nützlich wird sie erst, wenn sich jedes Signal aus Bausteinen $\mathrm{e}^{pt}$ zusammensetzen lässt. Diese Stufe zeigt, dass das geht, wie die Gewichte heißen und wo die Grenzen liegen.
:::

### Ausgangspunkt $\sigma=0$: reine Schwingungen

<span class="anker" id="stufe-2-1"></span>

Auf der imaginären Achse ($\sigma=0$) sind die Bausteine reine Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$. Ein __absolut integrierbares__ Signal ($\int|s(t)|\,\mathrm{d} t<\infty$, es klingt also nach beiden Seiten schnell genug ab) lässt sich aus ihnen zusammensetzen. Das ist die Fourier-Darstellung, die im Teil zur Fourier-Transformation ausführlich folgt:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Für viele Signale der Systemtheorie reicht das nicht. Der Sprung $\varepsilon(t)$ klingt nicht ab, $\mathrm{e}^{2t}\varepsilon(t)$ (die Impulsantwort eines instabilen Systems) wächst sogar. Aus Schwingungen mit konstanter Amplitude lässt sich ein Signal, das über alle Grenzen wächst, nicht zusammensetzen.

### Der Trick: dämpfen, zerlegen, zurückmultiplizieren

<span class="anker" id="stufe-2-2"></span>

**Die Idee.** Man macht das Signal erst zerlegbar und nimmt die Änderung danach wieder zurück:

<ol>

<li>

⁠**Dämpfen.** Man multipliziert mit $\mathrm{e}^{-\sigma t}$. Wächst ein rechtsseitiges Signal höchstens wie $\mathrm{e}^{\alpha t}$, klingt $s(t)\,\mathrm{e}^{-\sigma t}$ für jedes $\sigma>\alpha$ ab und ist absolut integrierbar.

</li>

<li>

⁠**Zerlegen.** Das gedämpfte Signal ist eine Überlagerung reiner Schwingungen. Sein Fourier-Spektrum ist genau die Laplace-Transformierte $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ auf der Linie $\operatorname{Re} p=\sigma$ (Aufgabe [2](#aufg-2)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**Zurückmultiplizieren.** Man multipliziert die Zerlegung mit $\mathrm{e}^{\sigma t}$. Der Faktor hängt nicht von $f$ ab und darf ins Integral. Dort macht er aus jeder Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ den Baustein $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$.

</li>

</ol>

Das Ergebnis ist die vermutete Überlagerung.

:::satz Satz 2.1 (Umkehrformel der Laplace-Transformation)
<span class="anker" id="satz-2-1"></span>

Liegt $\sigma$ im Konvergenzbereich von $S(p)$, dann gilt

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**So liest man das:**

<ul>

<li>

Der Integrationsweg ist die senkrechte Linie $\operatorname{Re} p=\sigma$ in der $p$-Ebene, von unten nach oben durchlaufen ($f$ von $-\infty$ bis $+\infty$, Abb. [2](#abb-2)).

</li>

<li>

$\mathrm{e}^{pt}$ ist der Baustein, $S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$ sein komplexes Gewicht. $S(p)$ selbst ist eine __Dichte__: Gewicht pro Frequenzintervall. Ist $s$ eine Spannung in V, hat $S$ die Einheit V s.

</li>

<li>

Das Integral ist als Grenzwert $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$ gemeint. Es liefert $s(t)$ an jeder Stelle, an der $s$ stetig ist, und an einer Sprungstelle den Mittelwert aus links- und rechtsseitigem Grenzwert.

</li>

</ul>

⁠**Grenzfall $\sigma=0$:** Liegt die imaginäre Achse im Konvergenzbereich, darf man $\sigma=0$ wählen. Dann ist $p=\mathrm{j}2\pi f$, und [(2.1)](#gl-2-1) wird die Fourier-Umkehrformel. Die Laplace-Transformation enthält die Fourier-Transformation als Spezialfall.

:::herleitung Umkehrformel aus der Fourier-Umkehrformel
Nach Schritt 2 ist $S(\sigma+\mathrm{j}2\pi f)$ das Fourier-Spektrum von $s(t)\mathrm{e}^{-\sigma t}$. Die Fourier-Umkehrformel liefert

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Multiplikation mit $\mathrm{e}^{\sigma t}$, das nicht von $f$ abhängt:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

Substitution $p=\sigma+\mathrm{j}2\pi f$ bei festem $\sigma$: $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$, also $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$. Die Grenzen $f=\mp\infty$ werden zu $p=\sigma\mp\mathrm{j}\infty$:

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**Beispiel: der Sprung aus Bausteinen.** Für $\varepsilon(t)$ ist $S(p)=1/p$ mit $\operatorname{Re} p>0$. Gewählt wird $\sigma=0{,}5/\mathrm s$ (Abb. [2](#abb-2)). Abbildung [3](#abb-3) zeigt, was herauskommt, wenn man nur die Bausteine mit $|f|\le F$ überlagert. Schon bei $F=0{,}25$ Hz ist die Form des Sprungs erkennbar. Mit wachsendem $F$ wird die Kante steiler, bei $t=0$ strebt die Kurve gegen den Mittelwert $\tfrac12$ (0,40; 0,47; 0,49), bei $t=-1$ s gegen null (0,053; 0,029; 0,008).

:::abbildung et3/k2linie
$p$-Ebene für den Sprung $\varepsilon(t)$, $S(p)=1/p$. Der Konvergenzbereich (blau hinterlegt) liegt rechts vom Pol $p=0$. Jede senkrechte Linie darin taugt als Integrationsweg; hier $\sigma=0{,}5/\mathrm s$. Jeder Punkt der Linie ist ein Baustein $\mathrm{e}^{pt}$ mit dem Gewicht $S(p)$.
:::

:::abbildung et3/k2sprung
Der Sprung, überlagert aus den Bausteinen $\mathrm{e}^{pt}$ auf der Linie $\operatorname{Re} p=0{,}5/\mathrm s$, wobei nur die Bausteine mit $|f|\le F$ mitgenommen werden: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ mit $S(p)=1/p$. Je mehr Bausteine, desto genauer der Sprung; bei $t=0$ strebt die Kurve gegen $\tfrac12$.
:::

:::frage Alle Bausteine sind komplex. Warum kommt eine reelle Kurve heraus?
Die Bausteine treten paarweise auf: zu $f$ gehört $-f$, also zu $p$ der konjugierte Punkt $p^*$. Für ein reelles Signal ist das Gewicht dort konjugiert, $S(p^*)=S(p)^*$ (die Rechnung $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ mit reellem $s$ zeigt es). Jedes Paar ergibt $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, also eine reelle, gedämpfte oder wachsende Schwingung. Die Imaginärteile heben sich paarweise auf.
:::

:::frage Ist es nun eine Summe oder ein Integral?
Im Allgemeinen ein Integral: Auf der Linie liegen kontinuierlich viele Bausteine, jeder mit einem infinitesimalen Gewicht $S\,\mathrm{d} f$. Eine echte Summe mit endlich vielen Gliedern entsteht in einem wichtigen Fall: wenn $S(p)$ ein Polynombruch ist. Dann ist das Signal eine Summe von Bausteinen an den Polen (Stufe [4](#stufe-4)). Eine Summe mit unendlich vielen Gliedern ist die Fourier-Reihe eines periodischen Signals.
:::

### Konvergenzbereich: welche Dämpfungen funktionieren

<span class="anker" id="stufe-2-3"></span>

**Die Idee.** Der Faktor $\mathrm{e}^{-\sigma t}$ wirkt auf beiden Seiten der Zeitachse, aber gegensätzlich. Für $t\to+\infty$ dämpft er umso stärker, je größer $\sigma$ ist. Für $t\to-\infty$ ist $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, dort verstärkt ein großes $\sigma$. Daraus folgen die drei Formen des Konvergenzbereichs:

<ul>

<li>

⁠**rechtsseitiges Signal**, $s(t)=0$ für $t<0$, wachsend höchstens wie $\mathrm{e}^{\alpha t}$: Jedes $\sigma>\alpha$ funktioniert. Konvergenzbereich: die Halbebene *rechts* einer Grenze.

</li>

<li>

⁠**linksseitiges Signal**: Nur die Seite $t\to-\infty$ zählt, kleine $\sigma$ helfen. Konvergenzbereich: eine Halbebene *links* einer Grenze.

</li>

<li>

⁠**zweiseitiges Signal**: Beide Bedingungen müssen gleichzeitig gelten. Konvergenzbereich: ein *Streifen*, der auch leer sein kann.

</li>

</ul>

Warum immer senkrechte Grenzen? Es gilt $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Ob $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ endlich ist, hängt nur von $\sigma$ ab, nie von $f$.

⁠**Kurz gesagt:** Der Konvergenzbereich ist die Menge aller Dämpfungen $\sigma$, mit denen $s(t)\,\mathrm{e}^{-\sigma t}$ absolut integrierbar wird.

:::merke Die Grundpaare (werden im ganzen Artikel benutzt)
Für eine beliebige komplexe Zahl $p_0$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{alle }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

Mit $p_0=0$ folgt aus [(2.2)](#gl-2-2) der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$. Die ersten beiden Zeilen haben *denselben* Ausdruck und verschiedene Konvergenzbereiche: Erst beide zusammen legen das Signal fest.
:::

:::herleitung Grundpaare
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. Der Wert an der oberen Grenze verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. Der Wert bei $t\to-\infty$ verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): Siebeigenschaft, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): partielle Integration, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ für $\operatorname{Re} p>0$.
:::

:::frage Warum fallen beim Ausrechnen von $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$ die e-Terme weg, und warum kommt $\frac{1}{b+p}$ heraus und nicht $\frac{1}{-(b+p)}$?
Beides liegt am Einsetzen der Grenzen. Die Stammfunktion von $\mathrm{e}^{-(b+p)t}$ ist $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, mit Minus, weil Ableiten den Faktor $-(b+p)$ liefert. Dann rechnet man „obere Grenze minus untere Grenze“:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Obere Grenze:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ geht genau dann gegen null, wenn $\operatorname{Re} p>-\operatorname{Re} b$. Diese Bedingung *ist* der Konvergenzbereich. Außerhalb bliebe der e-Term stehen und wüchse über alle Grenzen.

</li>

<li>

⁠**Untere Grenze:** $\mathrm{e}^0=1$, dort bleibt kein e-Term übrig.

</li>

<li>

⁠**Vorzeichen:** Das Minus der Stammfunktion trifft auf das Minus, mit dem die untere Grenze abgezogen wird. Minus mal Minus ergibt Plus.

</li>

</ul>

Beim linksseitigen Impuls $\mathrm{e}^{-bt}\varepsilon(-t)$ ist es umgekehrt. Integriert wird von $-\infty$ bis $0$, jetzt ist $t=0$ die *obere* Grenze. Ihr Beitrag $-\frac{1}{b+p}$ wird nicht abgezogen, das Minus bleibt stehen. Die untere Grenze $t\to-\infty$ verschwindet nur für $\operatorname{Re}(b+p)<0$, deshalb liegt dieser Konvergenzbereich links. Mit $p_0=-b$ sind das die Grundpaare [(2.2)](#gl-2-2) und [(2.3)](#gl-2-3).
:::

:::frage Betrachtet man die Realteile von $b$ und $p$, weil das Abklingen des Integranden über die Integrierbarkeit entscheidet? Für manche $b$ klingt das Signal ab, für andere wächst es, sinkt nicht auf null, und das Integral konvergiert nicht, weil immer noch etwas dazukommt.
Ja, genau so. Der Betrag des Integranden ist

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

Der Imaginärteil lässt den Integranden nur in der komplexen Ebene kreisen, am Betrag ändert er nichts. Über Wachsen oder Abklingen entscheidet allein der Realteil. Drei Präzisierungen:

<ul>

<li>

Es zählt die *Summe* $\operatorname{Re} b+\sigma$. Das Signal darf selbst wachsen ($\operatorname{Re} b<0$), solange die Dämpfung $\sigma$ stärker ist. Das ist der Trick „dämpfen“ aus Abschnitt 2.2.

</li>

<li>

„Geht gegen null“ allein reicht nicht. Auch $1/t$ geht gegen null, aber $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, weil die Beiträge zu langsam kleiner werden. Exponentielles Abklingen ist schnell genug: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ ist endlich.

</li>

<li>

Auf der Grenze $\operatorname{Re}(b+p)=0$ hat der Integrand den konstanten Betrag 1 und kreist nur. Das Integral pendelt dann, statt sich einem Wert zu nähern, und genau im Pol wächst es sogar linear (Aufgabe [3a](#aufg-3a)). Deshalb gehört die Grenzlinie nicht zum Konvergenzbereich.

</li>

</ul>
:::

:::frage Gilt das also für jede beliebige Funktion?
Nein, nur für Funktionen mit nicht leerem Konvergenzbereich. Drei Gegenbeispiele:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ wächst schneller als jede Exponentialfunktion. $\mathrm{e}^{t^2-\sigma t}\to\infty$ für jedes $\sigma$, keine Dämpfung reicht.

</li>

<li>

$\mathrm{e}^{|t|}$: Die rechte Hälfte verlangt $\sigma>1$, die linke $\sigma<-1$. Beides zugleich geht nicht.

</li>

<li>

Selbst die Konstante $s(t)=1$ für alle $t$: rechts $\sigma>0$, links $\sigma<0$. Die Fourier-Transformation erfasst solche Signale trotzdem, mit einem Dirac-Impuls im Spektrum.

</li>

</ul>

Für rechtsseitige Signale mit höchstens exponentiellem Wachstum klappt es immer. Dazu gehört jedes Signal, das in einer Schaltung bei $t=0$ eingeschaltet wird.
:::

:::frage Warum reicht eine einzige Linie, wenn die $p$-Ebene zweidimensional ist?
Jede Linie im Konvergenzbereich liefert dasselbe $s(t)$: Bei größerem $\sigma$ dämpft man in Schritt 1 stärker und multipliziert in Schritt 3 stärker zurück, beides hebt sich auf. Numerisch bestätigt: Mit $\sigma=0{,}2$ und $\sigma=1/\mathrm s$ ergibt sich für den Sprung beide Male $s(1\,\mathrm{s})\approx1{,}00$ und $s(-1\,\mathrm{s})\approx0{,}00$. Die Ebene enthält also mehr, als man für die Überlagerung braucht. Ihr Nutzen liegt woanders: In der Ebene lässt sich $S(p)$ durch wenige Zahlen beschreiben, die Pole und Nullstellen. (Zusatz: $S(p)$ ist im Konvergenzbereich komplex differenzierbar, deshalb legen die Werte auf einer Linie die Funktion im ganzen Bereich fest.)
:::

:::aufgabe Aufgabe 2 ★ Laplace ist Fourier eines gedämpften Signals
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Zeige $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$, indem du $\mathrm{e}^{-pt}$ in zwei Faktoren zerlegst.

</li>

<li>

Prüfe es am Sprung: Berechne $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ für $\sigma>0$ direkt und vergleiche mit $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ für $\sigma>0$. Das ist $1/p$ an der Stelle $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Ein wachsendes Signal
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, zum Beispiel die Impulsantwort eines instabilen Systems ($t$ in s).

<ol class="al">

<li>

Warum gibt es keine Fourier-Transformierte im klassischen Sinn?

</li>

<li>

Für welche $\sigma$ ist $s(t)\,\mathrm{e}^{-\sigma t}$ absolut integrierbar?

</li>

<li>

Berechne $S(p)$ direkt aus dem Integral. Zeichne Pol und Konvergenzbereich in die $p$-Ebene.

</li>

<li>

Welche $\sigma$ darfst du in der Umkehrformel benutzen? Der Ausdruck $S(\mathrm{j}2\pi f)$ ist endlich. Warum darfst du trotzdem nicht $\sigma=0$ wählen, und welches Signal käme mit $\sigma=0$ heraus? (Tipp: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: Das Signal ist nicht absolut integrierbar. Anschaulich: Aus Schwingungen konstanter Amplitude lässt sich nichts Wachsendes zusammensetzen.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ für $t>0$, integrierbar genau für $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ für $\operatorname{Re} p>2$. Pol bei $p=2$, Konvergenzbereich rechts davon, wie bei jedem rechtsseitigen Signal. Numerische Kontrolle: $S(3)=1$, $S(2{,}5+\mathrm{j})=0{,}4-0{,}8\mathrm{j}$.

(d) Jedes $\sigma>2/\mathrm s$, zum Beispiel $\sigma=3/\mathrm s$. $\sigma=0$ liegt links vom Pol, also außerhalb des Konvergenzbereichs. Der Ausdruck $1/(\mathrm{j}2\pi f-2)$ ist zwar endlich, er gehört aber zu einem *anderen* Signal: Nach [(2.3)](#gl-2-3) hat auch $-\mathrm{e}^{2t}\varepsilon(-t)$ die Transformierte $1/(p-2)$, mit Konvergenzbereich $\operatorname{Re} p<2$. Mit $\sigma=0$ käme dieses linksseitige, abklingende Signal heraus. Das ist das Signal, dessen Fourier-Transformierte $1/(\mathrm{j}2\pi f-2)$ tatsächlich ist.
:::
:::

:::aufgabe Aufgabe 3a ★★ Was auf der Grenze passiert
<span class="anker" id="aufg-3a"></span>

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
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ mit $p=\sigma+\mathrm{j}\omega$. Der Betrag des Integranden ist $\mathrm{e}^{-(\sigma-1)t}$, das Integral konvergiert genau für $\sigma>1$. Die 3 (die Kreisfrequenz des Signals) taucht im Betrag nicht auf. Sie bestimmt nur, wo auf der Grenzlinie der Pol sitzt: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, Pol bei $p=1+3\mathrm{j}$.

(b) Mit $p=1+\mathrm{j}\omega$ ist $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. Der Zähler kreist für wachsendes $T$ auf einem Kreis um 1 und nähert sich keinem Wert. Das Integral bleibt beschränkt, hat aber keinen Grenzwert.

</li>

<li>

$\omega=3$, also genau im Pol $p=1+3\mathrm{j}$: Der Integrand ist konstant 1, das Integral ist $T$ und wächst über alle Grenzen.

</li>

</ul>

Auf der Grenzlinie konvergiert das Integral also nirgends. Der Konvergenzbereich ist die offene Halbebene $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Aufgabe 4 ★ Richtig oder falsch? Mit Begründung
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Jede Funktion hat eine Laplace-Transformierte.

</li>

<li>

Ob $p$ im Konvergenzbereich liegt, hängt nur von $\operatorname{Re} p$ ab.

</li>

<li>

Liegt die imaginäre Achse im Konvergenzbereich, ist $S(\mathrm{j}2\pi f)$ die Fourier-Transformierte von $s(t)$.

</li>

<li>

In der Umkehrformel liefert $\sigma=1/\mathrm s$ ein anderes Signal als $\sigma=2/\mathrm s$, wenn beide im Konvergenzbereich liegen.

</li>

<li>

$\cos(2\pi f_0t)$ ist eine Eigenfunktion jedes LTI-Systems.

</li>

</ol>

:::loesung
(a) Falsch. Gegenbeispiele: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, die zweiseitige Konstante.

(b) Richtig. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$, die Frequenz $f$ kommt im Betrag nicht vor. Deshalb besteht der Konvergenzbereich aus ganzen senkrechten Linien.

(c) Richtig. Mit $\sigma=0$ ist $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) Falsch. Jede Linie im Konvergenzbereich liefert dasselbe Signal, weil die Dämpfung $\mathrm{e}^{-\sigma t}$ und das Zurückmultiplizieren mit $\mathrm{e}^{\sigma t}$ sich aufheben.

(e) Falsch. Der Ausgang ist $|H|\cos(2\pi f_0t+\varphi)$ mit $H=H(\mathrm{j}2\pi f_0)$. Er ist nur dann ein Vielfaches von $\cos(2\pi f_0t)$, wenn $\varphi=0$ oder $\varphi=\pi$ ist, wenn also $H(\mathrm{j}2\pi f_0)$ reell ist. Für den RC-Tiefpass ist das bei keiner Frequenz $f_0>0$ der Fall.
:::
:::

## Stufe 3: Aus der Faltung wird eine Multiplikation

<span class="anker" id="stufe-3"></span>

:::zweck
Stufe [1](#stufe-1) sagt, was das System mit einem Baustein macht. Stufe [2](#stufe-2) sagt, dass jedes Signal aus Bausteinen besteht. Zusammen ergeben sie den wichtigsten Satz der Laplace-Transformation.
:::

**Die Idee.** Ein LTI-System ist linear: Es verarbeitet jeden Baustein des Eingangs für sich und addiert die Ergebnisse. Jeden Baustein $\mathrm{e}^{pt}$ multipliziert es mit $H(p)$. Der Ausgang besteht also aus *denselben* Bausteinen wie der Eingang, nur ist jedes Gewicht mit $H(p)$ multipliziert. Abbildung [4](#abb-4) zeigt die beiden Wege zum Ausgang.

:::abbildung et3/k2wege
Zwei Wege vom Eingang zum Ausgang. Oben direkt mit dem Faltungsintegral. Unten: Eingang in Bausteine zerlegen, jedes Gewicht mit $H(p)$ multiplizieren, wieder zusammensetzen. Der untere Weg funktioniert, weil jeder Baustein eine Eigenfunktion ist.
:::

:::satz Satz 3.1 (Faltungssatz)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

gültig für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.
:::

⁠**So liest man das:** $S(p)$ ist das Gewicht des Bausteins $\mathrm{e}^{pt}$ im Eingang, $H(p)$ der Faktor, mit dem das System diesen Baustein multipliziert, $G(p)$ das Gewicht im Ausgang. Die Bedingung an $p$ kommt daher, dass die Linie der Umkehrformel durch beide Konvergenzbereiche laufen muss: Der Eingang muss in Bausteine zerlegbar sein, und das System muss jeden davon verarbeiten können.

:::herleitung Faltungssatz aus Überlagerung und Eigenfunktion
Man setzt den Eingang als Überlagerung [(2.1)](#gl-2-1) in die Faltung ein, mit einer Linie $\operatorname{Re} p=\sigma$, die in beiden Konvergenzbereichen liegt:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linearität: Die Faltung darf ins Integral, sie wirkt auf jeden Baustein einzeln:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Eigenfunktion [(1.1)](#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

Das ist die Umkehrformel für $g$ mit dem Gewicht $S(p)H(p)$. Da die Gewichte eines Signals eindeutig sind, ist $G(p)=S(p)H(p)$.
:::

⁠**Kurz gesagt:** Die Faltung wird zur Multiplikation, weil das System jeden Baustein $\mathrm{e}^{pt}$ nur mit der Zahl $H(p)$ multipliziert.

:::analogie
Ein Equalizer zerlegt Musik in Frequenzbänder, multipliziert jedes Band mit der Stellung seines Reglers und setzt die Bänder wieder zusammen. Ein LTI-System macht dasselbe mit den Bausteinen $\mathrm{e}^{pt}$, und die Reglerstellung ist $H(p)$. Die Analogie hinkt an zwei Stellen: Ein Equalizer hat endlich viele Bänder mit reellen Reglern. Hier gibt es kontinuierlich viele Bausteine, die auch wachsen oder abklingen können, und jeder „Regler“ ist eine komplexe Zahl, die zusätzlich die Phase verschiebt.
:::

**Derselbe Mechanismus erklärt Ableitung, Integral und Differentialgleichungen.**

<ul>

<li>

⁠**Ableiten.** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. Der Differenzierer ist ein LTI-System, und jeder Baustein ist seine Eigenfunktion mit dem Eigenwert $p$. Also wird jedes Gewicht mit $p$ multipliziert: $\mathcal{L}\{\dot s\}=p\,S(p)$.

</li>

<li>

⁠**Integrieren.** $\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$, aber nur für $\operatorname{Re} p>0$, sonst divergiert das Integral bei $-\infty$. Daher $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$ mit der zusätzlichen Bedingung $\operatorname{Re} p>0$.

</li>

<li>

⁠**Kette.** Zwei Systeme hintereinander multiplizieren nacheinander mit $H_1(p)$ und $H_2(p)$, zusammen mit $H_1H_2$. Die Reihenfolge ist egal, weil Zahlen kommutieren.

</li>

<li>

⁠**Differentialgleichung.** Jede Ableitung wird zum Faktor $p$. Aus einer linearen Differentialgleichung mit konstanten Koeffizienten

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{wird}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

also eine algebraische Gleichung, und $H(p)=G/S$ ist ein Polynombruch.

</li>

</ul>

**Beispiel: die Sprungantwort des RC-Tiefpasses.** Eingang $\varepsilon(t)$ mit $S(p)=1/p$ ($\operatorname{Re} p>0$), System $H(p)=1/(p+1)$ ($\operatorname{Re} p>-1$). Der gemeinsame Bereich ist $\operatorname{Re} p>0$:

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

Die Rücktransformation der beiden Summanden folgt aus [(2.2)](#gl-2-2) mit $p_0=0$ und $p_0=-1$. Direkt nachgerechnet: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ für $t>0$. Auch die Umkehrformel [(2.1)](#gl-2-1), numerisch auf der Linie $\sigma=0{,}5/\mathrm s$ ausgewertet, ergibt $g(0{,}5\,\mathrm{s})=0{,}3935$, $g(1\,\mathrm{s})=0{,}6321$, $g(3\,\mathrm{s})=0{,}9502$ und $g(-1\,\mathrm{s})=0$, genau $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

:::ltspice Die Übertragungsfunktion direkt eingeben
⁠**Zeichnen:** das RC-Glied (`1Meg`, `1u`) von `in` nach `rc`. Daneben eine spannungsgesteuerte Spannungsquelle `e`: Steuereingang an `in` und Masse, Ausgang am Netz `lap`, Wert `Laplace=1/(1+s)`. Diese Quelle ist ein LTI-System, das nur durch $H$ gegeben ist: LTspice berechnet daraus selbst die Impulsantwort und faltet den Eingang mit ihr. LTspice schreibt $s$ statt $p$.

⁠**Quelle und Direktive:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**Was du siehst:** `V(rc)` und `V(lap)` liegen übereinander (Abstand unter 0,001), auf 0,3935 bei 0,5 s, 0,6321 bei 1 s und 0,9502 bei 3 s. Mit dem Quellwert `AC 1` und `.ac dec 100 0.01 100` zeigt LTspice $H(s)$ für $s=\mathrm{j}2\pi f$, also nur auf der imaginären Achse: $-3{,}0$ dB und $-45^\circ$ bei 0,159 Hz.

⁠**Zu Aufgabe [6](#aufg-6):** Quelle `PWL(0 0 10 10)`, die Rampe $t\,\varepsilon(t)$ bis 10 s, und `.tran 0 10 0 1m`. Vergleiche `V(rc)` mit deinem Ergebnis aus Aufgabe [6](#aufg-6)(b).
:::

:::aufgabe Aufgabe 5 ★★ Kette und Ableitung über die Bausteine
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Begründe mit dem Bausteinbild (ohne Faltungsintegral), warum zwei LTI-Systeme in Kette die Übertragungsfunktion $H_1(p)H_2(p)$ haben. Warum folgt daraus, dass die Faltung kommutativ ist?

</li>

<li>

Leite $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ aus der Umkehrformel her, indem du sie nach $t$ ableitest.

</li>

</ol>

:::loesung
(a) Der Eingang besteht aus Bausteinen $\mathrm{e}^{pt}$ mit Gewichten $S(p)$. Das erste System multipliziert jeden Baustein mit $H_1(p)$, die Gewichte sind danach $H_1S$. Das zweite multipliziert mit $H_2(p)$: $G=H_2H_1S$. Die Kette hat also $H=H_1H_2$. Weil $H_1H_2=H_2H_1$, ist das Ergebnis von der Reihenfolge unabhängig, und da $h_1*h_2$ die Impulsantwort der Kette ist, folgt $h_1*h_2=h_2*h_1$.

(b) Ableiten unter dem Integral wirkt nur auf $\mathrm{e}^{pt}$:

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

Das ist die Umkehrformel mit dem Gewicht $pS(p)$, also $\mathcal{L}\{\dot s\}=pS(p)$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Rampenantwort des RC-Tiefpasses
<span class="anker" id="aufg-6"></span>

Eingang $s(t)=t\,\varepsilon(t)$ mit $S(p)=1/p^2$ für $\operatorname{Re} p>0$, Grundpaar [(2.5)](#gl-2-5).

<ol class="al">

<li>

Bestimme $G(p)$ und seinen Konvergenzbereich.

</li>

<li>

Prüfe die Zerlegung $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ und bestimme $g(t)$.

</li>

<li>

Kontrolle: Was ist $g(0)$, und warum muss das so sein? Was ist $\dot g(t)$?

</li>

<li>

Wie verhält sich $g(t)$ für $t\gg1$ s? Vergleiche mit Aufgabe [1](#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ für $\operatorname{Re} p>0$ (Durchschnitt aus $\operatorname{Re} p>0$ und $\operatorname{Re} p>-1$).

(b) Auf den Hauptnenner: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Rücktransformation mit [(2.5)](#gl-2-5) und [(2.2)](#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: Die Kondensatorspannung kann nicht springen, und der Eingang startet bei null. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, genau die Sprungantwort. Das passt: Die Rampe ist das Integral des Sprungs, also ist die Rampenantwort das Integral der Sprungantwort.

(d) Für $t\gg1$ s ist $\mathrm{e}^{-t}\approx0$ und $g(t)\approx t-1$: Der Ausgang folgt der Rampe mit einer Verzögerung von $RC=1$ s, genau wie bei der zweiseitigen Rampe in Aufgabe [1](#aufg-1)c. Der Unterschied ist der Baustein $\mathrm{e}^{-t}$ (Pol $-1$ des Systems): der Einschwingvorgang, weil die Rampe hier erst bei $t=0$ beginnt.
:::
:::

## Stufe 4: Aus dem Integral wird eine Summe

<span class="anker" id="stufe-4"></span>

:::zweck
Die Vermutung wörtlich: Für die Signale, um die es in der Systemtheorie fast immer geht, ist das Signal eine *endliche Summe* komplexer e-Funktionen. Die Pole sind die Exponenten.
:::

**Die Idee.** Bei Netzwerken aus $R$, $L$, $C$ und bei allen Systemen mit einer Differentialgleichung ist $S(p)$ ein Bruch aus Polynomen. Die __Partialbruchzerlegung__ schreibt ihn bei einfachen Polen als

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Jeder Summand ist die Transformierte *eines einzigen Bausteins*: Nach [(2.2)](#gl-2-2) gehört $A_r/(p-p_r)$ zu $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$, wenn der Konvergenzbereich rechts des Pols liegt, und der konstante Summand $A_0$ gehört nach [(2.4)](#gl-2-4) zu $A_0\,\delta(t)$. Für ein rechtsseitiges Signal ist also

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**Kurz gesagt:** Ein rechtsseitiges Signal mit rationaler Laplace-Transformierten ist eine endliche Summe von Bausteinen $\mathrm{e}^{p_r t}$. Die Pole sind die Exponenten, die Partialbruchkoeffizienten die Gewichte.

Damit lässt sich jedes solche Signal an seinen Polen ablesen, mit der Landkarte aus Abb. [1](#abb-1): $\operatorname{Re} p_r$ sagt, ob der Baustein abklingt oder wächst, $\operatorname{Im} p_r$, wie schnell er schwingt. Ein konjugiertes Polpaar $p_r,p_r^*$ ergibt zusammen eine reelle gedämpfte Schwingung. Hier liegt auch der Kern der __Stabilität__: Ein kausaler Baustein $\mathrm{e}^{p_r t}\varepsilon(t)$ klingt genau dann ab, wenn $\operatorname{Re} p_r<0$. Ein kausales System ist deshalb stabil, wenn alle Pole von $H(p)$ in der linken Halbebene liegen.

**Beispiel.** Die Sprungantwort aus Stufe [3](#stufe-3) hat die Pole $0$ und $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{Pol }0\text{ (von }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{Pol }-1\text{ (von }H)}\qquad(t>0).$$

Der Pol des Eingangs liefert den Anteil, den der Eingang erzwingt (die Endspannung 1). Der Pol des Systems liefert die __Eigenbewegung__ des RC-Glieds, das Abklingen mit $RC=1$ s. Das gilt allgemein: Im Ausgang $G=SH$ stecken die Pole des Eingangs und die Pole des Systems.

:::zusatz Warum das Integral zur Summe zusammenfällt: der Residuensatz
Dieser Abschnitt braucht den Residuensatz der Funktionentheorie. Er erklärt, warum [(2.1)](#gl-2-1) und [(4.1)](#gl-4-1) dasselbe sind und warum der Konvergenzbereich über das Signal entscheidet.

Sei $S(p)$ ein Polynombruch mit kleinerem Zählergrad als Nennergrad und einfachen Polen.

<ul>

<li>

⁠**$t>0$:** Man schließt die Integrationslinie durch einen großen Halbkreis nach *links*. Dort geht $\operatorname{Re} p\to-\infty$, also $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, und $S(p)\to0$. Der Halbkreis trägt im Grenzfall nichts bei (Jordansches Lemma). Der geschlossene Weg läuft gegen den Uhrzeigersinn, und der Residuensatz gibt

$$s(t)=\sum_{\text{Pole links der Linie}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{links}}A_r\,\mathrm{e}^{p_r t}.$$

Das Residuum an einem einfachen Pol ist $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: genau der Partialbruchkoeffizient.

</li>

<li>

⁠**$t<0$:** Jetzt verschwindet $\mathrm{e}^{pt}$ für $\operatorname{Re} p\to+\infty$. Man schließt nach *rechts*, der Weg läuft im Uhrzeigersinn, das gibt ein Minuszeichen:

$$s(t)=-\sum_{\text{Pole rechts der Linie}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Folge:** Die Lage der Linie, also der Konvergenzbereich, entscheidet, welche Pole kausale Bausteine liefern (links der Linie) und welche antikausale (rechts der Linie). Beispiel: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (Abb. [5](#abb-5)). Liegt die Linie zwischen den Polen, $-2<\sigma<-1$, wirkt $-2$ für $t>0$ und $-1$ für $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Numerisch auf der Linie $\sigma=-1{,}5/\mathrm s$ ausgewertet: $s(1\,\mathrm{s})=-0{,}1353=-\mathrm{e}^{-2}$ und $s(-1\,\mathrm{s})=-2{,}7183=-\mathrm{e}^{1}$. Liegt die Linie rechts von beiden Polen, ergibt dieselbe Formel das kausale Signal $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$, liegt sie links von beiden, das antikausale $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$.

:::abbildung et3/k2residuen
Integrationslinie $\sigma=-1{,}5/\mathrm s$ im Streifen $-2<\operatorname{Re} p<-1$ (blau) und die Halbkreise, mit denen man sie schließt (rot).
:::
:::

:::aufgabe Aufgabe 7 ★★★ (Vertiefung) Dieselbe Formel, zwei Signale
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Konvergenzbereich $\operatorname{Re} p>-1$. Werte die Umkehrformel mit dem Residuensatz aus, getrennt für $t>0$ und $t<0$.

</li>

<li>

Dasselbe für den Konvergenzbereich $\operatorname{Re} p<-1$.

</li>

<li>

Vergleiche mit den Grundpaaren [(2.2)](#gl-2-2) und [(2.3)](#gl-2-3). Was lernst du daraus über die Angabe „$S(p)=1/(p+1)$“ ohne Konvergenzbereich?

</li>

</ol>

:::loesung
(a) Linie rechts vom Pol, zum Beispiel $\sigma=0$. Für $t>0$ nach links schließen: Der Pol $-1$ liegt innen, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, also $s(t)=\mathrm{e}^{-t}$. Für $t<0$ nach rechts schließen: Rechts der Linie liegt kein Pol, $s(t)=0$. Zusammen $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Linie links vom Pol, zum Beispiel $\sigma=-2$. Für $t>0$ nach links schließen: kein Pol, $s(t)=0$. Für $t<0$ nach rechts schließen: Pol innen, Umlauf im Uhrzeigersinn, $s(t)=-\mathrm{e}^{-t}$. Zusammen $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) Das sind genau die Grundpaare [(2.2)](#gl-2-2) und [(2.3)](#gl-2-3) mit $p_0=-1$. Die Angabe „$S(p)=1/(p+1)$“ allein legt das Signal nicht fest. Erst mit dem Konvergenzbereich ist klar, auf welcher Seite der Linie der Pol liegt und ob er einen kausalen oder einen antikausalen Baustein liefert.
:::
:::

## Stufe 5: Warum man auch den Eingang transformiert

<span class="anker" id="stufe-5"></span>

:::frage Es ergibt Sinn, $h(t)$ zu transformieren, damit man $H(p)$ mit Eigenfunktionen multiplizieren und den Ausgang bestimmen kann. Aber $s(t)$ zu transformieren, ergibt doch erst mal keinen Sinn, damit kann man systemtheoretisch nichts anfangen. Klar, $s*h=h*s$, aber $h(t)$ ist meistens keine Eigenfunktion, man kann also nicht $h(t)\cdot S(p)$ schreiben. Welche systembezogene Bedeutung hat es, ein beliebiges Signal zu transformieren?
⁠**Was an der Frage stimmt:** $H(p)$ sagt, was das System mit einem Baustein $\mathrm{e}^{pt}$ macht. Und $h(t)\cdot S(p)$ ergibt tatsächlich keinen Sinn.

⁠**Wo der Denkfehler liegt:** Auch der Eingang ist fast nie eine Eigenfunktion. Ein Sprung, ein Sprachsignal, ein Rechteckimpuls sind keine einzelnen Bausteine $\mathrm{e}^{pt}$. Deshalb ergibt $H(p)\cdot s(t)$ genauso wenig Sinn wie $h(t)\cdot S(p)$: $H(p)$ darf nur auf einen Baustein angewandt werden, und für ein beliebiges $s(t)$ ist gar nicht klar, welches $p$ gemeint sein soll. Bevor $H(p)$ irgendetwas tun kann, muss der Eingang in Bausteine zerlegt sein. Genau das leistet $S(p)$.

⁠**Die richtige Sicht:** Im Faltungssatz $G(p)=H(p)\,S(p)$ hat jeder Faktor eine eigene, systembezogene Bedeutung:

<ul>

<li>

$S(p)$ ist das *Rezept des Eingangs*: wie viel vom Baustein $\mathrm{e}^{pt}$ im Eingang steckt;

</li>

<li>

$H(p)$ ist die *Wirkung des Systems*: mit welcher Zahl es diesen Baustein multipliziert;

</li>

<li>

$G(p)$ ist das Rezept des Ausgangs.

</li>

</ul>

Ohne $S(p)$ kennt man nur die Wirkung auf einzelne Bausteine, aber nicht, welche Bausteine ankommen. $H(p)$ allein beantwortet die Frage „Was passiert mit dem Ausgang?“ nur für den einen Sonderfall, dass der Eingang selbst ein einzelner Baustein ist.

⁠**Am Beispiel Sprung und RC-Tiefpass.** Der Sprung hat das Rezept $S(p)=1/p$. Auf der Linie $\sigma=0{,}5/\mathrm s$ ist $|S|=2$ bei $f=0$, $0{,}16$ bei 1 Hz und $0{,}016$ bei 10 Hz. Die schnellen Bausteine sind schwach, aber vorhanden, und sie bilden die scharfe Kante (Abb. [3](#abb-3): Je mehr schnelle Bausteine, desto steiler die Kante). Der RC-Tiefpass multipliziert sie mit $|H|=0{,}67$, $0{,}15$ und $0{,}016$. Im Ausgang sind die schnellen Bausteine also noch einmal etwa um den Faktor $2\pi f\cdot RC$ schwächer (für $f\gg1/(2\pi RC)=0{,}16$ Hz), und die Kante ist weg: $g(t)=1-\mathrm{e}^{-t}$ steigt stetig an. Diese Erklärung braucht beide Transformierten. $H$ allein sagt nur „schnelle Bausteine werden geschwächt“, erst $S$ sagt, dass die Kante aus schnellen Bausteinen besteht.

⁠**Und die Symmetrie $s*h=h*s$?** Mathematisch sind beide Signale gleichberechtigt: Man kann auch $h$ als Eingang und $s$ als „System“ lesen, dann ist $H(p)$ das Rezept und $S(p)$ die Wirkung. Die Systemtheorie verteilt die Rollen nur nach der Physik: Das eine Signal kommt von außen, das andere beschreibt die Schaltung. Im Bildbereich werden dabei immer *beide* transformiert.
:::

**Weitere Gründe, ein Signal für sich zu transformieren.**

<ul>

<li>

⁠**Ein System ausmessen.** Misst man Eingang und Ausgang eines unbekannten Systems, liefert $H(p)=G(p)/S(p)$ das System. Dafür transformiert man zwei Signale, jedes für sich (Aufgabe [9](#aufg-9)).

</li>

<li>

⁠**Das Signal selbst verstehen.** Der Ton einer angeschlagenen Glocke ist eine Summe gedämpfter Schwingungen, jede ein konjugiertes Polpaar. $\operatorname{Im} p_r$ ist die Tonhöhe eines Teiltons, $-\operatorname{Re} p_r$ seine Abklingrate. Wenige Pole beschreiben den ganzen Klang. Ein Messgerät, das ein Spektrum anzeigt, tut dasselbe auf der Linie $\sigma=0$.

</li>

<li>

⁠**Faltung ohne System.** Die Faltung überlagert verschobene, gewichtete Kopien eines Signals. Das System ist eine Deutung dieser Operation, nicht die einzige. Ein Beispiel ganz ohne System ist die Augensumme zweier Würfel (Artikel zur Faltung).

</li>

</ul>

:::ltspice Ein Netzwerk zu zwei Messungen
⁠**Zeichnen:** das Netzwerk, das du in Aufgabe [9](#aufg-9)(c) gefunden hast, mit der Quelle `PULSE(0 1 0 1u 1u 100)` am Eingang und dem Ausgang am Netz `out`. Daneben, ohne Verbindung zur Schaltung, eine Verhaltensquelle `bv` am Netz `mess` mit `V=1-exp(-2*time)`. Sie spielt die gemessene Ausgangskurve.

⁠**Direktiven:** `.tran 0 3 0 1m`, `.meas tran abw MAX abs(V(out)-V(mess))`.

⁠**Was du siehst:** Stimmen Netzwerk und Bauteilwerte, liegen `V(out)` und `V(mess)` übereinander, und die größte Abweichung `abw` ist praktisch null (unter $10^{-5}$). Vergleiche so die Kurven mit deinem Ergebnis aus Aufgabe [9](#aufg-9)(c).
:::

:::aufgabe Aufgabe 8 ★★ Welche Bausteine bilden die Kante?
<span class="anker" id="aufg-8"></span>

Eingang $\varepsilon(t)$, System RC-Tiefpass mit $RC=1$ s. Betrachte die Bausteine auf der Linie $\sigma=0{,}5/\mathrm s$.

<ol class="al">

<li>

Berechne $|S(p)|$, $|H(p)|$ und $|G(p)|$ für $f=0$, $1$ Hz und $10$ Hz.

</li>

<li>

Um welchen Faktor schwächt das System die Bausteine bei 10 Hz stärker als die bei 1 Hz?

</li>

<li>

Erkläre mit (a) und Abb. [3](#abb-3), warum der Ausgang keine Kante hat. Warum reicht $H(p)$ allein für diese Erklärung nicht?

</li>

</ol>

:::loesung
(a) Mit $p=0{,}5+\mathrm{j}2\pi f$ (in $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0,667 | 1,33 |
| 1 Hz | 0,159 | 0,155 | 0,0246 |
| 10 Hz | 0,0159 | 0,0159 | 0,000253 |

(b) $0{,}155/0{,}0159\approx9{,}7$, also fast um den Faktor 10, so wie die Frequenz. Für große $|p|$ ist $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) Die Kante des Sprungs besteht aus den schnellen Bausteinen: In Abb. [3](#abb-3) wird sie steiler, je mehr davon mitgenommen werden. Im Eingang fallen ihre Gewichte wie $1/f$, im Ausgang wie $1/f^2$. Die schnellen Bausteine sind im Ausgang so schwach, dass keine Kante mehr entsteht, und $g(t)$ steigt stetig an. $H(p)$ allein sagt nur, dass schnelle Bausteine geschwächt werden. Dass die Kante aus genau diesen Bausteinen besteht, ist eine Aussage über den Eingang, und die steht in $S(p)$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Ein unbekanntes System aus zwei Messungen
<span class="anker" id="aufg-9"></span>

An ein unbekanntes kausales LTI-System wird zur Zeit $t=0$ eine Spannung von 1 V angelegt, $s(t)=\varepsilon(t)$ in V. Am Ausgang misst man $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ in V ($t$ in s).

<ol class="al">

<li>

Transformiere beide Signale, jedes für sich.

</li>

<li>

Bestimme $H(p)$ und daraus $h(t)$.

</li>

<li>

Um welches Netzwerk könnte es sich handeln? Welcher Wert ergibt sich?

</li>

<li>

Welcher Pol in $G(p)$ stammt vom Eingang, welcher vom System?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ für $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ für $\operatorname{Re} p>0$ (Grundpaar [(2.2)](#gl-2-2) mit $p_0=0$ und $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Da das System kausal ist, liegt der Konvergenzbereich rechts vom Pol: $\operatorname{Re} p>-2$. Mit [(2.2)](#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ in $1/\mathrm s$.

(c) Ein RC-Tiefpass hat $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. Der Vergleich mit $\dfrac{2}{p+2}$ ergibt $RC=0{,}5$ s, zum Beispiel $R=500\,\mathrm{k\Omega}$ und $C=1$ µ F. (Jedes andere Netzwerk mit derselben Übertragungsfunktion verhielte sich an den Klemmen genauso. Aus Messungen an Ein- und Ausgang kennt man nur $H$, nicht die Bauteile.)

(d) Der Pol $p=0$ stammt vom Eingang (Sprung), der Pol $p=-2$ vom System. Beim Teilen $G/S$ kürzt sich genau der Pol des Eingangs heraus.
:::
:::

:::merke Das Wichtigste bis hier
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, daher $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ mit $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ ist die Wachstumsrate, $f$ die Frequenz des Bausteins.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$, $\sigma$ im Konvergenzbereich; jede solche Linie liefert dasselbe $s(t)$.

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$; für $\sigma=0$ die Fourier-Transformation.

</li>

<li>

Konvergenzbereich: hängt nur von $\sigma$ ab; rechtsseitig eine rechte Halbebene, linksseitig eine linke, zweiseitig ein Streifen.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; Ableiten $\to p$, Integrieren $\to1/p$.

</li>

<li>

Rational und rechtsseitig: $s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$, Pole = Exponenten. Kausal und stabil: alle Pole links.

</li>

</ul>
:::
