---
title: Stufe 1: Warum gerade $\mathrm{e}^{pt}$
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220200
summary: Setzt man e pt ins Faltungsintegral ein, kommt H(p)\,e pt heraus: e pt ist eine Eigenfunktion.
tags: Wachstumsrate, Frequenz
lang: de
---

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

:::abbildung et3/k2bausteine 1
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

Idealer Tiefpass ohne Laufzeit, $H(f)=1$ im ganzen Durchlassbereich: Jedes Signal, das nur aus Schwingungen mit Frequenzen im Durchlassbereich besteht, kommt unverändert heraus und ist eine Eigenfunktion mit dem Eigenwert 1.

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
