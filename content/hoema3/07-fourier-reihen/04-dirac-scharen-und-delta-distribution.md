---
title: Dirac-Scharen und die δ-Distribution
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070400
summary: Von Grund auf – eine Dirac-Schar $\varphi_\varepsilon(x)=\frac1\varepsilon\varphi(x/\varepsilon)$ ist eine Familie glatter Glättungskerne, die sich bei $0$ konzentrieren ($\int\varphi_\varepsilon=1$). Die Faltung $\varphi_\varepsilon*f$ glättet $f$ und konvergiert gegen $f$ – eine „Approximation der Eins". Im Grenzwert entsteht die Dirac'sche δ-Distribution, die stetige Funktionen auswertet, $\int f\,d\delta_x=f(x)$. Als Fourier-Reihe ist der „Dirac-Kamm" gerade $\frac1{2\pi}\sum_k e^{ikx}$ – die Brücke zum Dirichlet-Kern.
tags: Dirac-Schar, Glättungskern, Faltung, approximative Eins, Delta-Distribution, Siebeigenschaft, Dirac-Kamm, Distributionssinn
---

:::grafik
Einstiegs-Animation: Eine __Dirac-Schar__ $\varphi_\varepsilon$ — glatte, nichtnegative Buckel mit **konstanter Fläche
$1$**, die für $\varepsilon\downarrow0$ immer schmaler und höher werden und sich bei $x=0$ zusammenziehen. Links wird
eine Funktion $f$ mit $\varphi_\varepsilon$ **gefaltet**: $\varphi_\varepsilon*f$ ist eine verwischte, glatte Version
von $f$, die mit $\varepsilon\to0$ wieder scharf wird ($\to f$). Rechts der Grenzwert als __δ-Distribution__: ein
unendlich dünner „Spike" bei $0$, der aus einer Funktion nur den Wert $f(0)$ **heraussiebt**. Kernbotschaft: Eine
Dirac-Schar ist eine „Approximation der Eins"; ihr Grenzwert ist kein Funktionswert, sondern eine Auswertung.
:::

:::konzept
Die $L^2$-Konvergenz sagt nichts über **einzelne Punkte**. Für die punktweise Konvergenz von Fourier-Reihen brauchen
wir ein Werkzeug, das Funktionen an einem Punkt „ausliest". Dieser Exkurs baut es auf: Eine __Dirac-Schar__ ist eine
Familie von Glättungskernen, mit denen man eine Funktion **mittelt** (faltet) — das Ergebnis ist glatt und nähert die
Funktion beliebig gut an. Im Grenzwert wird aus der Schar die __Dirac'sche δ-Distribution__: kein gewöhnliches
Objekt mehr, sondern eine **Auswertung** $f\mapsto f(0)$. In der Physik und Signaltheorie ist das der „Impuls"; für
uns ist der entscheidende Punkt, dass das $N$-te Fourierpolynom genau eine solche Mittelung ist (mit dem
__Dirichlet-Kern__) — der Schlüssel zum nächsten Artikel.
:::

**Worum es geht:** Wir definieren __Glättungskern__ und __Dirac-Schar__, zeigen, dass die __Faltung__ $\varphi_
\varepsilon*f\to f$ (Satz 7.16), deuten die Schar als __Approximation der Eins__ und führen die __δ-Distribution__ ein.

## Glättungskern und Dirac-Schar

Man fixiert eine beliebig oft differenzierbare Funktion — einen __Glättungskern__ — mit

$$\varphi:\mathbb{R}\to[0,\infty), \qquad \varphi(x)=0\ \text{für } |x|\ge1, \qquad \int_{\mathbb{R}}\varphi(x)\,dx=1.$$

Ein klassisches Beispiel ist der **Buckel** $\varphi(x)=\frac1c\exp\!\big(\tfrac{1}{x^2-1}\big)$ für $|x|<1$ (und $0$
sonst), mit $c=\int_{-1}^1\exp(\tfrac1{y^2-1})\,dy$ zur Normierung. Durch Umskalieren entsteht die __Dirac-Schar__

$$\varphi_\varepsilon(x):=\frac{1}{\varepsilon}\,\varphi\!\Big(\frac{x}{\varepsilon}\Big), \qquad \varepsilon>0,$$

die ebenfalls glatt ist, $\varphi_\varepsilon(x)=0$ für $|x|\ge\varepsilon$ und $\int_{\mathbb{R}}\varphi_\varepsilon=1$
erfüllt. Für $\varepsilon\downarrow0$ **konzentriert sie sich bei $x=0$**, während das Integral stets $1$ bleibt — der
Buckel wird schmaler und höher, die Fläche bleibt erhalten.

## Glättung durch Faltung

**Satz 7.16.** Sei $f:\mathbb{R}\to\mathbb{R}$ stetig und $f_\varepsilon(x):=\int_{\mathbb{R}}\varphi_\varepsilon(x-y)
f(y)\,dy$. Dann ist $f_\varepsilon$ für $\varepsilon>0$ **beliebig glatt**, und $f_\varepsilon(x)\to f(x)$ für
$\varepsilon\downarrow0$ (punktweise, auf endlichen Intervallen sogar gleichmäßig, Bemerkung 7.17).

*Beweis der Konvergenz.* Weil $\int\varphi_\varepsilon(x-y)\,dy=1$, ist $\int\varphi_\varepsilon(x-y)f(x)\,dy=f(x)$,
und mit der Standardabschätzung für Integrale

$$|f(x)-f_\varepsilon(x)|=\Big|\int_{\mathbb{R}}\varphi_\varepsilon(x-y)\big(f(x)-f(y)\big)\,dy\Big|\le\sup_{|x-y|<\varepsilon}|f(x)-f(y)|\xrightarrow{\varepsilon\downarrow0}0$$

(nur $|x-y|<\varepsilon$ trägt bei, da $\varphi_\varepsilon$ außerhalb verschwindet; dort ist $f$ wegen Stetigkeit fast
konstant). Die Glattheit von $f_\varepsilon$ folgt aus dem Satz über Parameterintegrale (Ableitung fällt auf das glatte
$\varphi_\varepsilon$). Daher der Name **Glättungskern**: $f_\varepsilon$ ist eine geglättete Version von $f$.

Die auftretende Operation ist die __Faltung__ $(f*g)(x):=\int_{\mathbb{R}}f(x-y)g(y)\,dy$; sie ist **kommutativ**
($f*g=g*f$, Verschiebung $y\mapsto x-y$) und erzeugt wieder eine stetige, integrierbare Funktion.

:::grafik
Links die Dirac-Schar $\varphi_\varepsilon$ für fallendes $\varepsilon$ (immer schmaler/höher, Fläche $1$). Mitte eine
raue Funktion $f$ und ihre Faltungen $\varphi_\varepsilon*f$ (glatt, für kleines $\varepsilon$ fast deckungsgleich mit
$f$). Rechts die Abschätzung $|f-f_\varepsilon|\le\sup_{|x-y|<\varepsilon}|f(x)-f(y)|$ als schrumpfendes Fehlerband.
:::

## Die Approximation der Eins und die δ-Distribution

Die Faltung ist eine Art **Multiplikation** von Funktionen — aber sie hat **kein Einselement**: Es gibt keine Funktion
$g$ mit $f*g=f$ für alle $f$. Die Dirac-Schar $\varphi_\varepsilon$ ist die beste Näherung daran, eine __Approximation
der Eins__. Insbesondere liefert dasselbe Argument

$$\int_{\mathbb{R}}f(y)\,\varphi_\varepsilon(y)\,dy\longrightarrow f(0)\qquad(\varepsilon\downarrow0).$$

Es gibt **keine Funktion** $\delta$ mit $\int f(y)\delta(y)\,dy=f(0)$ — das geht nur als **Limes** von Integralen, und
als Funktionenfolge konvergiert $\varphi_\varepsilon$ nicht. Man sagt: $\varphi_\varepsilon$ konvergiert gegen
$\delta_0$ **im Distributionssinn**, und meint

$$\lim_{\varepsilon\downarrow0}\int_{\mathbb{R}}f(y)\,\varphi_\varepsilon(y)\,dy=f(0)=:\int_{\mathbb{R}}f(x)\,\delta_0(dx).$$

Die __Dirac'sche δ-Distribution__ $\delta_0$ definiert also ein **neues Integral**, das eine stetige Funktion bei
$x=0$ **auswertet** (__Siebeigenschaft__). Allgemeiner für $x\in\mathbb{R}$ und $I\subset\mathbb{R}$ (Bemerkung 7.18):

$$\int_I f(y)\,\delta_x(dy)=\int_I f\,d\delta_x=\begin{cases}f(x), & x\in I,\\ 0, & x\notin I,\end{cases} \qquad \delta_x(I)=\begin{cases}1, & x\in I,\\ 0, & x\notin I.\end{cases}$$

Anders als das $R$-Integral „bemerkt" das δ-Integral, ob über ein offenes oder abgeschlossenes Intervall integriert
wird (ob der Punkt $x$ dazugehört).

**Eigene Beispiele (andere Dirac-Scharen).** Der Glättungskern muss nicht kompakten Träger haben; es genügen
Nichtnegativität, Integral $1$ und Konzentration bei $0$. Klassiker: der __Gauß-Kern__ $\varphi_\varepsilon(x)=
\frac{1}{\sqrt{2\pi\varepsilon}}\,e^{-x^2/(2\varepsilon)}$ (die Wärmeleitungslösung — glatt, überall positiv) und das
einfachste __Rechteck__ $\varphi_\varepsilon(x)=\frac{1}{2\varepsilon}\mathbf{1}_{[-\varepsilon,\varepsilon]}(x)$ (der
gleitende Mittelwert). Beide erfüllen $\varphi_\varepsilon*f\to f$.

## Der Dirac-Kamm und die Brücke zu Fourier

„Formal" besitzt die $2\pi$-periodische Fortsetzung von $\delta_0$ (der __Dirac-Kamm__) die Fourier-Koeffizienten

$$c_k=\frac{1}{2\pi}\int_0^{2\pi}e^{-ikx}\,\delta_0(dx)=\frac{1}{2\pi}\qquad\text{für alle } k\in\mathbb{Z}$$

(die Siebeigenschaft wertet $e^{-ik\cdot0}=1$ aus). Damit liegt die Vermutung nahe

$$\delta_0=\frac{1}{2\pi}\sum_{k\in\mathbb{Z}}e^{ikx}, \qquad\text{bzw.}\qquad \frac{1}{2\pi}\sum_{|k|\le N}e^{ikx}\xrightarrow{N\to\infty}\delta_0\ \text{im Distributionssinn}.$$

Die endliche Summe $\frac{1}{2\pi}\sum_{|k|\le N}e^{ikx}$ ist (bis auf Normierung) genau der **Dirichlet-Kern** aus dem
Sägezahn-Beispiel — eine Dirac-artige Schar in $N$. Das Fourierpolynom $T_Nf$ ist also eine **Faltung von $f$ mit dem
Dirichlet-Kern**, und punktweise Konvergenz heißt: Konvergiert dieser Kern gegen $\delta$? Das klärt der nächste
Artikel.

**Stolperstein:** (1) $\delta_0$ ist **keine Funktion** (kein punktweiser Wert „$\delta(0)=\infty$" ist gemeint),
sondern ein **Funktional** / Maß — definiert nur über das Integral/den Limes. (2) Die Konvergenz $\varphi_\varepsilon
\to\delta_0$ ist im **Distributionssinn** (getestet gegen stetige $f$), nicht punktweise und nicht in einer Norm. (3)
Der Dirichlet-Kern ist zwar Dirac-artig, aber **nicht nichtnegativ** — deshalb ist die punktweise Konvergenz von
Fourier-Reihen subtiler als die glatte Glättung hier (der nichtnegative __Fejér-Kern__ der Cesàro-Mittel verhält sich
besser).

:::kern
__Glättungskern__ $\varphi\ge0$ glatt, $\varphi=0$ für $|x|\ge1$, $\int\varphi=1$ (z. B. Buckel $\frac1c e^{1/(x^2-1)}$);
__Dirac-Schar__ $\varphi_\varepsilon(x)=\frac1\varepsilon\varphi(x/\varepsilon)$, $\int\varphi_\varepsilon=1$,
konzentriert bei $0$ für $\varepsilon\downarrow0$. __Satz 7.16__: $f_\varepsilon=\varphi_\varepsilon*f$ ist glatt und
$f_\varepsilon\to f$ (Beweis: $|f-f_\varepsilon|\le\sup_{|x-y|<\varepsilon}|f(x)-f(y)|\to0$). __Faltung__ $(f*g)(x)=
\int f(x-y)g(y)\,dy$ (kommutativ, kein Einselement) ⇒ Dirac-Schar = __Approximation der Eins__. __δ-Distribution__:
$\int f\,d\delta_x=f(x)$ (__Siebeigenschaft__), $\delta_x(I)=1$ falls $x\in I$ sonst $0$; **keine Funktion**, nur als
Limes im __Distributionssinn__ $\lim_{\varepsilon}\int f\varphi_\varepsilon=f(0)$. __Dirac-Kamm__ hat $c_k=\frac1{2\pi}$
∀$k$ ⇒ $\frac1{2\pi}\sum_{|k|\le N}e^{ikx}\to\delta_0$ = __Dirichlet-Kern__; $T_Nf=f*$Dirichlet-Kern (Brücke zur
punktweisen Konvergenz).
:::

Mit der Dirac-Schar im Gepäck untersuchen wir jetzt, wann $T_Nf(x)\to f(x)$ **punktweise** gilt. Das Werkzeug ist der
__Dirichlet-Kern__, und das Ergebnis betrifft insbesondere Sprungstellen (Mittelwert) — das Thema des nächsten Artikels.

:::quiz
F: Was macht eine Dirac-Schar $\varphi_\varepsilon$ aus, und was bleibt beim Umskalieren erhalten?
A: Es ist eine Familie glatter, nichtnegativer Buckel, die sich für $\varepsilon\downarrow0$ immer schmaler und höher bei $x=0$ zusammenziehen. Die Umskalierung $\varphi_\varepsilon(x)=\frac1\varepsilon\varphi(x/\varepsilon)$ ist gerade so gebaut, dass das Integral stets $1$ bleibt — die Fläche bleibt erhalten.
F: Warum macht gerade der Faktor $\frac1\varepsilon$ das Integral unabhängig von $\varepsilon$?
A: Beim Stauchen des Arguments um den Faktor $\varepsilon$ schrumpft die Fläche um $\varepsilon$; der Vorfaktor $\frac1\varepsilon$ gleicht das genau aus. Per Substitution $u=x/\varepsilon$ wird $\int\frac1\varepsilon\varphi(x/\varepsilon)dx=\int\varphi(u)\,du=1$.
F: Was bedeutet die Faltung $\varphi_\varepsilon*f$ anschaulich?
A: Sie bildet an jeder Stelle einen gewichteten Mittelwert von $f$ über eine kleine Umgebung, wobei $\varphi_\varepsilon$ die Gewichte liefert. Das Ergebnis ist eine geglättete, „verwischte" Version von $f$ — daher der Name Glättungskern.
F: Warum konvergiert $\varphi_\varepsilon*f$ gegen $f$?
A: Weil $\int\varphi_\varepsilon=1$ ist, gilt $f(x)-f_\varepsilon(x)=\int\varphi_\varepsilon(x-y)(f(x)-f(y))\,dy$. Nur $|x-y|<\varepsilon$ trägt bei, und dort ist $f$ wegen Stetigkeit fast konstant, also geht der Fehler $\le\sup_{|x-y|<\varepsilon}|f(x)-f(y)|\to0$.
F: Warum ist $\varphi_\varepsilon*f$ glatt, obwohl $f$ selbst rau sein kann?
A: Nach dem Satz über Parameterintegrale fällt beim Ableiten die Ableitung komplett auf den glatten Faktor $\varphi_\varepsilon$, nicht auf $f$. Da $\varphi_\varepsilon$ beliebig oft differenzierbar ist, ist es auch die Faltung — die Rauheit von $f$ wird „weggemittelt".
F: Was heißt „Approximation der Eins", und warum braucht man sie?
A: Die Faltung hat kein neutrales Element — keine Funktion $g$ mit $f*g=f$ für alle $f$. Die Dirac-Scharen $\varphi_\varepsilon$ kommen dem beliebig nahe ($\varphi_\varepsilon*f\to f$), sind also eine „approximative Eins" der Faltung.
F: Warum ist die δ-Distribution keine gewöhnliche Funktion?
A: Es gibt keine Funktion $\delta$ mit $\int f(y)\delta(y)\,dy=f(0)$; die Scharen $\varphi_\varepsilon$ konvergieren als Funktionenfolge gar nicht. $\delta_0$ existiert nur als Grenzwert der Integrale, also als Funktional/Maß, das eine Funktion auswertet — „im Distributionssinn".
F: Was besagt die Siebeigenschaft der δ-Distribution?
A: $\int f\,d\delta_x=f(x)$ — das δ-„Integral" greift aus einer stetigen Funktion genau ihren Wert an der Stelle $x$ heraus. Anders als das Riemann-Integral merkt es sogar, ob der Punkt $x$ zum Integrationsbereich gehört.
F: Wieso hat der Dirac-Kamm die Fourier-Koeffizienten $c_k=\frac{1}{2\pi}$ für alle $k$?
A: Nach der Siebeigenschaft ist $c_k=\frac{1}{2\pi}\int_0^{2\pi}e^{-ikx}\,\delta_0(dx)=\frac{1}{2\pi}e^{-ik\cdot0}=\frac{1}{2\pi}$. Alle Frequenzen sind also gleich stark vertreten — ein „weißes" Spektrum.
F: Wieso ist der Dirichlet-Kern zwar Dirac-artig, aber problematischer als die glatten Glättungskerne hier?
A: Das Fourierpolynom $T_Nf$ ist die Faltung von $f$ mit dem Dirichlet-Kern $\frac{1}{2\pi}\sum_{|k|\le N}e^{ikx}$, der für $N\to\infty$ gegen $\delta_0$ strebt. Er ist aber nicht nichtnegativ, sondern oszilliert — deshalb ist die punktweise Konvergenz subtiler (und der nichtnegative Fejér-Kern verhält sich gutmütiger).
:::
