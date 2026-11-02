---
title: Stufe 10: Das Dirichlet-Problem
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3171100
summary: Auf dem Rand einer Kreisscheibe sind Temperatur oder Potential vorgegeben.
tags: Dirichlet-Problem, harmonisch, Poisson-Kern, Maximumprinzip
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Auf dem Rand einer Kreisscheibe sind Temperatur oder Potential vorgegeben. Diese Stufe bestimmt das Innere aus der Fourier-Reihe der Randwerte.
:::

**Die Idee.** Sei $\mathbb D=\{(x,y)\in\mathbb{R}^2:x^2+y^2<1\}$ die Einheitskreisscheibe, $\mathbb{R}^2$ mit $\mathbb{C}$ gleichgesetzt, und $g:\partial\mathbb D\to\mathbb{R}$ stetig. Das __Dirichlet-Problem__ lautet

<span class="anker" id="gl-10-1"></span>
$$\Delta u=0\quad\text{in }\mathbb D,\qquad u=g\quad\text{auf }\partial\mathbb D. \tag{10.1}$$

Eine Funktion mit $\Delta u=0$ heißt __harmonisch__. Der Rand ist ein Kreis, also ist $\varphi\mapsto g(\mathrm{e}^{\mathrm{i}\varphi})$ eine $2\pi$-periodische Funktion mit einer Fourier-Reihe $\sum_kc_k\mathrm{e}^{\mathrm{i}k\varphi}$. Die Laplace-Gleichung ist linear. Man setzt also jeden Baustein einzeln ins Innere fort und addiert.

**Die Bausteine im Inneren.** In Polarkoordinaten sei $u(r\mathrm{e}^{\mathrm{i}\varphi})=v(r,\varphi)$. Nach [Teil 4](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/koordinatentransformationen.html) lautet die Aufgabe

$$\frac{\partial^2v}{\partial r^2}+\frac1r\frac{\partial v}{\partial r}+\frac1{r^2}\frac{\partial^2v}{\partial\varphi^2}=0,\qquad v(1,\varphi)=g(\mathrm{e}^{\mathrm{i}\varphi}).$$

Mit dem Ansatz $v_k(r,\varphi)=A_k(r)\,\mathrm{e}^{\mathrm{i}k\varphi}$ entsteht die gewöhnliche Gleichung

<span class="anker" id="gl-10-2"></span>
$$r^2A_k''(r)+r\,A_k'(r)-k^2A_k(r)=0,\qquad A_k(1)=c_k. \tag{10.2}$$

Der Potenzansatz $A=r^\alpha$ gibt $\alpha^2=k^2$. Es gibt also die Lösungen $r^{|k|}$ und $r^{-|k|}$, für $k=0$ die Lösungen $1$ und $\ln r$. Die Lösungen $r^{-|k|}$ und $\ln r$ sind nahe $r=0$ unbeschränkt und scheiden aus. Es bleibt $A_k(r)=c_k\,r^{|k|}$, also $v_k(r,\varphi)=c_k\,r^{|k|}\mathrm{e}^{\mathrm{i}k\varphi}$. Hohe Frequenzen klingen zur Mitte hin am schnellsten ab.

**Der Poisson-Kern.** Summiert man alle $v_k$ und setzt $c_k=\frac1{2\pi}\int_0^{2\pi}g(\mathrm{e}^{\mathrm{i}t})\,\mathrm{e}^{-\mathrm{i}kt}\,\mathrm{d} t$ ein, darf man für $r<1$ Summe und Integral tauschen, denn die Reihe $\sum_kr^{|k|}\mathrm{e}^{\mathrm{i}k(\varphi-t)}g(\mathrm{e}^{\mathrm{i}t})$ konvergiert nach dem M-Test gleichmäßig in $t$. Das gibt

<span class="anker" id="gl-10-3"></span>
$$v(r,\varphi)=\sum_{k\in\mathbb{Z}}c_k\,r^{|k|}\mathrm{e}^{\mathrm{i}k\varphi}=\frac1{2\pi}\int_0^{2\pi}P_r(\varphi-t)\,g(\mathrm{e}^{\mathrm{i}t})\,\mathrm{d} t \tag{10.3}$$

mit dem __Poisson-Kern__ $P_r(\varphi):=\sum_{k\in\mathbb{Z}}r^{|k|}\mathrm{e}^{\mathrm{i}k\varphi}$. Die Formel ist also eine periodische Faltung. Mit $z=r\mathrm{e}^{\mathrm{i}\varphi}$ ergeben zwei geometrische Reihen für $r\in[0,1)$

<span class="anker" id="gl-10-4"></span>
$$P_r(\varphi)=\sum_{k=0}^\infty z^k+\sum_{k=1}^\infty\overline z^{\,k}=\frac1{1-z}+\frac{\overline z}{1-\overline z}=\frac{1-|z|^2}{|1-z|^2}=\frac{1-r^2}{1-2r\cos\varphi+r^2}. \tag{10.4}$$

:::satz Satz 10.1 (Randwerte)
<span class="anker" id="satz-10-1"></span>

Ist $f:\mathbb{R}\to\mathbb{C}$ stetig und $2\pi$-periodisch, gilt für $r\nearrow1$ gleichmäßig in $\varphi$

<span class="anker" id="gl-10-5"></span>
$$\frac1{2\pi}\int_0^{2\pi}P_r(\varphi-t)\,f(t)\,\mathrm{d} t\to f(\varphi). \tag{10.5}$$
:::

:::beweis Der Poisson-Kern mittelt wie eine Dirac-Schar
Aus [(10.4)](#gl-10-4) folgt $P_r\ge0$, und in der Reihe überlebt beim Integrieren nur $k=0$, also ist $\frac1{2\pi}\int_0^{2\pi}P_r\,\mathrm{d}\varphi=1$. Für $\alpha\le|\varphi|\le\pi$ ist $P_r(\varphi)\le\frac{1-r^2}{1-2r\cos\alpha+r^2}$, und das geht für $r\nearrow1$ gegen null. Wie in [(7.1)](mitteln-mit-dirac-scharen.html#gl-7-1) ist daher, über $(-\pi,\pi)$ integriert,

$$\Bigl|\frac1{2\pi}\int_{-\pi}^\pi P_r(t)\,f(\varphi-t)\,\mathrm{d} t-f(\varphi)\Bigr|\le\sup_{|t|\le\alpha}|f(\varphi-t)-f(\varphi)|+2\sup_\mathbb{R}|f|\cdot\sup_{\alpha\le|t|\le\pi}P_r(t).$$

Der erste Term ist wegen der gleichmäßigen Stetigkeit klein für kleines $\alpha$, unabhängig von $\varphi$. Bei festem $\alpha$ geht der zweite für $r\nearrow1$ gegen null.
:::

:::satz Satz 10.2 (Lösung des Dirichlet-Problems)
<span class="anker" id="satz-10-2"></span>

Zu stetigem $g:\partial\mathbb D\to\mathbb{R}$ gibt es genau eine glatte Lösung $u:\mathbb D\to\mathbb{R}$ von $\Delta u=0$ in $\mathbb D$ mit $\lim_{\boldsymbol y\to\boldsymbol{x}}u(\boldsymbol y)=g(\boldsymbol{x})$ für alle $\boldsymbol{x}\in\partial\mathbb D$. Sie ist durch [(10.3)](#gl-10-3) gegeben, also durch

<span class="anker" id="gl-10-6"></span>
$$u(r\mathrm{e}^{\mathrm{i}\varphi})=\frac1{2\pi}\int_0^{2\pi}\frac{1-r^2}{1-2r\cos(\varphi-t)+r^2}\,g(\mathrm{e}^{\mathrm{i}t})\,\mathrm{d} t. \tag{10.6}$$
:::

⁠**So liest man das:** Der Wert an der Stelle $r\mathrm{e}^{\mathrm{i}\varphi}$ ist ein gewichteter Mittelwert der Randwerte. Randpunkte nahe dieser Stelle zählen stark, ferne schwach.

:::beweis Existenz
Weil $v$ aus einer unendlichen Summe stammt, muss man die Lösungseigenschaft nachprüfen. Jeder Summand von $P_r$ ist harmonisch, die Reihe darf für $r<1$ gliedweise abgeleitet werden, also ist $P_r(\varphi-t)$ harmonisch in $(r,\varphi)$. Für jedes $\alpha>0$ sind $P_r$ und seine Ableitungen auf $[0,1-\alpha]\times[0,2\pi]$ gleichmäßig beschränkt. Nach dem Satz über Parameterintegrale ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) darf man in [(10.6)](#gl-10-6) unter dem Integral ableiten, also ist $u$ glatt und harmonisch. Die Randwerte nimmt $u$ nach Satz [10.1](#satz-10-1) an, denn $g$ ist stetig.
:::

**Eindeutigkeit: das Maximumprinzip.** Eine harmonische Funktion, die stetig bis zum Rand ist, nimmt Maximum und Minimum auf dem Rand an (__Maximumprinzip__).

:::beweis Maximumprinzip
Angenommen, $\max_{\partial\mathbb D}u<\max_{\overline{\mathbb D}}u$ mit Differenz $\mu>0$. Für $\tilde u(\boldsymbol{x})=u(\boldsymbol{x})+\frac\mu2|\boldsymbol{x}|^2$ ist auf dem Rand $\tilde u\le\max_{\partial\mathbb D}u+\frac\mu2<\max_{\overline{\mathbb D}}u$, also liegt das Maximum von $\tilde u$ bei einem $\boldsymbol{x}_0\in\mathbb D$ im Inneren. Dort sind $\partial_x^2\tilde u\le0$ und $\partial_y^2\tilde u\le0$, die Spur der Hesse-Matrix $D^2\tilde u$ (der Matrix der zweiten Ableitungen) ist also $\le0$. Andererseits ist $\operatorname{spur}D^2\tilde u(\boldsymbol{x}_0)=\Delta u+\frac\mu2\cdot4=2\mu>0$, ein Widerspruch. Für das Minimum wendet man das auf $-u$ an.
:::

Zwei Lösungen haben als Differenz eine harmonische Funktion mit Randwerten null. Ihr Maximum und Minimum sind also null, die Lösungen stimmen überein. **Wozu die ganze Scheibe?** Auf der gelochten Scheibe $\mathbb D\setminus\{0\}$ ist $\ln r$ harmonisch mit Randwert 0 auf $r=1$, ohne null zu sein: Das Maximumprinzip braucht auch den inneren Rand.

**Beispiel.** Sei $g(x,y)=x^2$, also $g(\mathrm{e}^{\mathrm{i}\varphi})=\cos^2\varphi=\frac12+\frac12\cos2\varphi$. Der Faktor $r^{|k|}$ gibt $u=\frac12+\frac12r^2\cos2\varphi=\frac12+\frac12(x^2-y^2)$. Es ist $\Delta u=1-1=0$, und auf dem Rand gilt $\frac12(x^2+y^2)+\frac12(x^2-y^2)=x^2$. **Grenzfall:** $P_0=1$, also ist $u(0,0)=\frac1{2\pi}\int_0^{2\pi}g(\mathrm{e}^{\mathrm{i}t})\,\mathrm{d} t$: Der Wert in der Mitte ist der Mittelwert der Randwerte, hier $\frac12$ (Abb. [10](#abb-10)).

:::abbildung hm3/k7poisson 10
Links: Der Poisson-Kern ist positiv, hat den Mittelwert 1 und konzentriert sich für $r\nearrow1$ bei $\varphi=0$. Rechts: Höhenlinien der Lösung $u=\frac12+\frac12(x^2-y^2)$ zu den Randwerten $g=x^2$. In der Mitte steht der Mittelwert der Randwerte.
:::

**Zwei Kerne im Vergleich.** Beide Kerne wirken als Faktoren auf die Fourier-Koeffizienten.

| Kern | Faktor vor $c_k$ | Folge |
|---|---|---|
| $D_N$ | $1$ für $\vert k\vert \le N$, sonst $0$ | hartes Abschneiden, $\int\vert D_N\vert \to\infty$, stetiges $f$ reicht nicht |
| $P_r$ | $r^{\vert k\vert }$, exponentiell klein | sanftes Dämpfen, $P_r\ge0$, Approximation der Eins für jedes stetige $f$ |

:::frage Warum kann eine hohe Frequenz am Rand im Inneren fast verschwinden?
Weil $r^{|k|}$ für große $|k|$ sehr klein ist: Bei $r=\frac12$ und $k=10$ bleibt ein Tausendstel. Deshalb ist die Lösung innen glatt, auch bei nur stetigem Rand.
:::

:::aufgabe Aufgabe 12 ★★ Scheibe mit Randwerten
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Löse das Dirichlet-Problem für $g(\mathrm{e}^{\mathrm{i}\varphi})=1+3\cos\varphi-\sin2\varphi$ und schreibe $u$ in $x$ und $y$. Prüfe $\Delta u=0$.

</li>

<li>

Berechne $P_{1/2}(0)$ und $P_{1/2}(\pi)$. Was bedeutet das Verhältnis für den Punkt $r=\frac12$, $\varphi=0$?

</li>

<li>

Sei $g(\mathrm{e}^{\mathrm{i}\varphi})=w(\varphi)$. Gib $u(0,0)$ und Schranken für $u$ in $\mathbb D$ an, ohne ein Integral zu lösen.

</li>

</ol>

:::loesung
(a) Die Faktoren $r^{|k|}$ geben $u=1+3r\cos\varphi-r^2\sin2\varphi=1+3x-2xy$, denn $r^2\sin2\varphi=2xy$. Beide Terme haben $\Delta=0$. (b) $P_{1/2}(0)=\frac{3/4}{1/4}=3$ und $P_{1/2}(\pi)=\frac{3/4}{9/4}=\frac13$. Der nächste Randpunkt zählt 9-mal so stark wie der entfernteste. (c) $u(0,0)=c_0=\frac\pi2$ ist der Mittelwert von $w$. Das Maximumprinzip gibt $0\le u\le\pi$.
:::
:::
