---
title: Zwei wichtige Beispiele zu Fuß
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070200
summary: Von Grund auf – zwei klassische Fourier-Reihen von Hand gerechnet. Der Sägezahn $\frac{\pi-x}{2}=\sum_{k\ge1}\frac{\sin kx}{k}$ ist eine reine Sinusreihe (ungerade), die am Sprung nur punktweise (nicht gleichmäßig) konvergiert. Sein Integral, die Parabel $\frac{(\pi-x)^2}{4}=\sum_{k\ge1}\frac{\cos kx}{k^2}+C$, ist eine Kosinusreihe, die dank $\sum 1/k^2<\infty$ sogar gleichmäßig (überall) konvergiert.
tags: Sägezahn, Fourier-Reihe, Sinusreihe, Kosinusreihe, Dirichlet-Kern, gliedweise Integration, gleichmäßige Konvergenz, Sprungstelle
---

:::grafik
Einstiegs-Animation: Zwei Funktionen und ihre Fourier-Reihen. Oben der __Sägezahn__ $f(x)=\frac{\pi-x}{2}$ (fallende
Geraden mit Sprung bei $0,2\pi,\dots$) und seine Partialsummen $\sum_{k=1}^N\frac{\sin kx}{k}$ — sie nähern sich der
Säge an, bleiben aber am Sprung „überschwingend" (Gibbs). Unten das Integral davon, die __Parabel__ $F(x)=\frac{(\pi-x)^2}{4}$
(glatt, ohne Sprung) mit $\sum_{k=1}^N\frac{\cos kx}{k^2}$ — die Partialsummen schmiegen sich **überall gleichmäßig** an.
Kernbotschaft: Der Sprung macht den Unterschied — die Säge konvergiert nur weg vom Sprung, ihr Integral überall.
:::

:::konzept
Theorie wird erst durch Rechnen greifbar. Dieser Artikel führt zwei __klassische Fourier-Reihen__ von Hand vor — den
Sägezahn und seine Stammfunktion (eine Parabel). An ihnen sieht man die ganze Mechanik: Wie die Koeffizienten
entstehen, warum eine **ungerade** Funktion eine reine **Sinusreihe** und eine **gerade** eine reine **Kosinusreihe**
liefert, und — am wichtigsten — wie die __Konvergenzgüte am Sprung__ kippt. Der glatte Fall (Parabel) konvergiert dank
der summierbaren Majorante $\sum 1/k^2$ gleichmäßig, der Sprungfall (Säge) nur weg vom Sprung. Beide Reihen tauchen als
Werkzeug immer wieder auf (und liefern nebenbei berühmte Zahlenreihen).
:::

**Worum es geht:** Wir berechnen die Fourier-Reihe des __Sägezahns__ (Sinusreihe, Konvergenz am Sprung) und durch
gliedweise Integration die der __Parabel__ (Kosinusreihe, gleichmäßig).

## Der Sägezahn

Betrachte die $2\pi$-periodische Fortsetzung von

$$f(x):=\begin{cases}0, & x=0,\\[1mm] \dfrac{\pi-x}{2}, & x\in(0,2\pi).\end{cases}$$

Diese Funktion ist (um den Mittelpunkt) **ungerade**, also eine reine Sinusreihe. Die Rechnung $b_k=\frac1\pi\int_0^{2\pi}
\frac{\pi-x}{2}\sin(kx)\,dx=\frac1k$ (partielle Integration) liefert $a_k=0$ und das Resultat

$$f(x)=\sum_{k=1}^\infty\frac{\sin(kx)}{k}\qquad\text{für alle } x\in\mathbb{R}.$$

**Konvergenzverhalten.** Die Reihe konvergiert für jedes $\delta>0$ **gleichmäßig** auf $[\delta,2\pi-\delta]$ — aber
**nicht** gleichmäßig über den Sprung bei $x=0$ hinweg. Das zeigt man über die Partialsummen: Mit $\sum_{k=1}^N\frac
{\sin(kx)}{k}=\int_\pi^x\sum_{k=1}^N\cos(ky)\,dy$ und dem __Dirichlet-Kern__ (Lemma 7.8)

$$\sum_{|k|\le N}e^{ikx}=\frac{\sin\!\big((N+\tfrac12)x\big)}{\sin\tfrac{x}{2}}$$

wird $\sum_{k=1}^N\frac{\sin(kx)}{k}=\int_\pi^x\frac{\sin((N+\frac12)y)}{2\sin\frac{y}{2}}\,dy+\frac{\pi-x}{2}$. Mit
$\varphi(y)=1/\sin\frac{y}{2}$ und **partieller Integration** strebt das Restintegral für $x\in[\delta,2\pi-\delta]$
gleichmäßig gegen null (weil $\varphi$ und $\varphi'$ dort beschränkt sind) — der oszillierende Faktor $\cos((N+\frac12)
y)$ mittelt sich weg. Am Sprung selbst ($x=0$) ist $\sum\frac{\sin(k\cdot0)}{k}=0$, also gerade der **Mittelwert**
$\frac12(f(0^+)+f(2\pi^-))=\frac12(\frac\pi2+(-\frac\pi2))=0$ der beiden Sprungseiten.

:::grafik
Der Sägezahn $\frac{\pi-x}{2}$ mit Sprung bei $x=0$ (von $+\frac\pi2$ auf $-\frac\pi2$); Partialsummen $N=3,10,30$
überschwingen nahe dem Sprung (Gibbs-Überschwinger ~9 %), während sie im Inneren $[\delta,2\pi-\delta]$ gleichmäßig
anliegen; am Sprung treffen sie den Mittelwert $0$.
:::

## Das Integral: die Parabel

Jetzt integrieren wir den Sägezahn. Sei $F$ die $2\pi$-periodische Funktion mit $F(x):=\frac{(\pi-x)^2}{4}$ für
$x\in[0,2\pi]$. Wegen $\frac{d}{dy}\frac{(\pi-y)^2}{4}=-\frac{\pi-y}{2}$ ist

$$\frac{(\pi-x)^2}{4}=\int_\pi^x\frac{d}{dy}\frac{(\pi-y)^2}{4}\,dy=-\int_\pi^x\frac{\pi-y}{2}\,dy=-\int_\pi^x\sum_{k=1}^\infty\frac{\sin(ky)}{k}\,dy.$$

Da die Sägezahn-Reihe auf kompakten Teilintervallen **gleichmäßig** konvergiert, dürfen wir für $x\in(0,2\pi)$
**Summation und Integration vertauschen** (Satz 6.6):

$$\frac{(\pi-x)^2}{4}=-\sum_{k=1}^\infty\int_\pi^x\frac{\sin(ky)}{k}\,dy=\sum_{k=1}^\infty\frac{\cos kx}{k^2}-\sum_{k=1}^\infty\frac{(-1)^k}{k^2}.$$

Das ist eine reine **Kosinusreihe** (denn $F$ ist gerade) mit $a_k=\frac{1}{k^2}$. Weil $\sum\frac{\cos kx}{k^2}$ nach
dem **Weierstraßschen M-Test** ($M_k=\frac1{k^2}$, $\sum\frac1{k^2}<\infty$) **gleichmäßig auf ganz $\mathbb{R}$**
konvergiert, ist die rechte Seite stetig und stimmt auf $[0,2\pi]$ mit der stetigen Parabel überein:

**Lemma 7.9.** $\displaystyle\frac{(\pi-x)^2}{4}=\sum_{k=1}^\infty\frac{\cos kx}{k^2}+C$ für alle $x\in[0,2\pi]$, mit
$C=\sum_{k=1}^\infty\frac{(-1)^{k+1}}{k^2}$; die Reihe konvergiert **gleichmäßig**.

Der Kontrast ist lehrreich: Die **glatte** Parabel (ihre Reihe fällt mit $1/k^2$ ab) konvergiert überall gleichmäßig;
der **sprunghafte** Sägezahn (Reihe fällt nur mit $1/k$) konvergiert nur weg vom Sprung. **Je glatter die Funktion,
desto schneller fallen die Koeffizienten** und desto besser die Konvergenz — ein zentrales Prinzip der Fourier-Theorie.

**Berühmte Zahlenreihen (Ausblick).** Wertet man Lemma 7.9 an einem Punkt aus, fallen klassische Summen heraus. Die
Konstante $C$ bestimmen wir im nächsten Artikel mit der Parseval-Gleichung zu $C=\frac{\pi^2}{12}$; einsetzen von $x=0$
($\cos0=1$) gibt dann $\frac{\pi^2}{4}=\sum\frac1{k^2}+\frac{\pi^2}{12}$, also die berühmte __Basel-Summe__ $\sum_{k=1}
^\infty\frac1{k^2}=\frac{\pi^2}{6}$.

:::grafik
Links die Säge (Koeffizienten $1/k$, langsamer Abfall → nur punktweise am Sprung); rechts die Parabel (Koeffizienten
$1/k^2$, schneller Abfall → gleichmäßig überall). Ein Balkendiagramm $|c_k|$ vs. $k$ verdeutlicht $1/k$ gegen $1/k^2$;
Pfeil „glatter ⇒ schnellerer Koeffizientenabfall ⇒ bessere Konvergenz".
:::

**Stolperstein:** (1) An einer **Sprungstelle** konvergiert die Fourier-Reihe gegen den **Mittelwert** der beiden
einseitigen Grenzwerte, nicht gegen einen der Werte — und die Konvergenz dort ist nicht gleichmäßig (Gibbs-Phänomen,
ein fester ~9 %-Überschwinger). (2) **Gliedweise Integration** war erlaubt, weil die Sägezahn-Reihe gleichmäßig
konvergiert; sie **glättet** und verbessert die Konvergenz (aus $1/k$ wird $1/k^2$). Gliedweise **Differentiation**
täte das Gegenteil und ist hier nicht ohne Weiteres erlaubt. (3) $C$ ist eine echte, von $x$ unabhängige Konstante —
sie entsteht, weil die Stammfunktion nur bis auf eine Konstante bestimmt ist (bzw. aus dem Mittelwert $a_0/2$).

:::kern
__Sägezahn__: $f(x)=\frac{\pi-x}{2}$ auf $(0,2\pi)$ (ungerade) hat $a_k=0$, $b_k=\frac1k$, also $f(x)=\sum_{k=1}^\infty
\frac{\sin kx}{k}$. Konvergenz **gleichmäßig auf $[\delta,2\pi-\delta]$**, nicht über den Sprung; am Sprung $x=0$ →
Mittelwert $0$. Werkzeug: __Dirichlet-Kern__ (Lemma 7.8) $\sum_{|k|\le N}e^{ikx}=\frac{\sin((N+\frac12)x)}{\sin(x/2)}$ +
partielle Integration. __Parabel__ (Integral der Säge): $F(x)=\frac{(\pi-x)^2}{4}$ (gerade) → gliedweise Integration
(erlaubt wegen glm. Konvergenz) gibt $\frac{(\pi-x)^2}{4}=\sum_{k=1}^\infty\frac{\cos kx}{k^2}+C$ (Lemma 7.9), $C=\sum
\frac{(-1)^{k+1}}{k^2}$; **gleichmäßig auf ganz $\mathbb{R}$** (M-Test, $M_k=1/k^2$). Prinzip: glatter ⇒ Koeffizienten
fallen schneller ($1/k\to1/k^2$) ⇒ bessere Konvergenz. Ausblick: $C=\frac{\pi^2}{12}$, $x=0$ ⇒ $\sum\frac1{k^2}=
\frac{\pi^2}{6}$ (Basel).
:::

Diese Beispiele zeigen Konvergenz „zu Fuß". Der nächste Artikel liefert den **abstrakten** Zugang: Fourierpolynome als
__Projektion__ auf endlichdimensionale Unterräume, die __Besselsche Ungleichung__ und die __Parseval-Gleichung__ — und
damit die $L^2$-Konvergenz jeder Fourier-Reihe.

:::quiz
F: Warum ist der Sägezahn eine reine Sinusreihe?
A: Die $2\pi$-periodische Fortsetzung ist um den Mittelpunkt ungerade ($f(-x)=-f(x)$). Nach der Symmetrieregel verschwinden dann alle Kosinus-Koeffizienten ($a_k=0$), und es bleibt eine reine Sinusreihe $\sum\frac{\sin kx}{k}$.
F: Gegen welchen Wert konvergiert die Sägezahn-Reihe an der Sprungstelle $x=0$, und warum?
A: Gegen den Mittelwert $\tfrac12(f(0^+)+f(2\pi^-))=\tfrac12(\tfrac\pi2-\tfrac\pi2)=0$ der beiden einseitigen Grenzwerte. Jeder Summand $\sin(k\cdot0)=0$, also ist die Summe dort exakt null — und das ist gerade der Mittelwert, nie einer der beiden Sprungwerte.
F: Warum konvergiert die Sägezahn-Reihe weg vom Sprung gleichmäßig, aber nicht über den Sprung hinweg?
A: Auf $[\delta,2\pi-\delta]$ sind im Dirichlet-Kern-Argument $1/\sin(y/2)$ und seine Ableitung beschränkt, sodass der oszillierende Faktor sich per partieller Integration „wegmittelt". Nahe dem Sprung wächst $1/\sin(y/2)$ unbeschränkt, die Abschätzung bricht zusammen — dort überschwingt die Reihe (Gibbs).
F: Was ist das Gibbs-Phänomen?
A: An einer Sprungstelle überschwingen die Partialsummen die Funktion um einen festen Betrag (~9 % der Sprunghöhe), der auch für $N\to\infty$ nicht verschwindet, sondern nur schmaler zum Sprung wandert. Es ist die konkrete Erscheinungsform der fehlenden gleichmäßigen Konvergenz am Sprung.
F: Wozu dient der Dirichlet-Kern $\sum_{|k|\le N}e^{ikx}=\frac{\sin((N+\frac12)x)}{\sin(x/2)}$ im Beweis?
A: Er bringt die Partialsumme aus einer offenen Summe in eine geschlossene Form, die man integrieren und abschätzen kann. Der Nenner $\sin(x/2)$ zeigt direkt, wo das Problem sitzt (bei $x=0$), und steuert so das Konvergenzargument.
F: Warum darf man die Sägezahn-Reihe gliedweise integrieren, um die Parabel zu bekommen?
A: Weil die Sägezahn-Reihe auf kompakten Teilintervallen gleichmäßig konvergiert, und gleichmäßige Konvergenz erlaubt das Vertauschen von Summe und Integral (Satz 6.6). Man integriert also einfach jeden $\frac{\sin ky}{k}$-Term einzeln.
F: Warum konvergiert die Parabel-Reihe $\sum\frac{\cos kx}{k^2}$ gleichmäßig auf ganz $\mathbb{R}$, der Sägezahn aber nicht?
A: Die Parabel-Koeffizienten fallen wie $1/k^2$, und $\sum 1/k^2<\infty$ liefert über den Weierstraß-M-Test eine summierbare Majorante — also gleichmäßige Konvergenz überall. Die Sägezahn-Koeffizienten fallen nur wie $1/k$, und $\sum 1/k$ divergiert, sodass der M-Test nicht greift.
F: Welches allgemeine Prinzip über Glattheit und Koeffizientenabfall illustrieren die beiden Beispiele?
A: Je glatter eine Funktion ist, desto schneller fallen ihre Fourier-Koeffizienten und desto besser konvergiert die Reihe. Der Sprung des Sägezahns erzwingt langsamen $1/k$-Abfall, die glatte Parabel erlaubt $1/k^2$ — das Integrieren hat die Funktion geglättet und die Koeffizienten beschleunigt.
F: Warum verbessert gliedweises Integrieren die Konvergenz, während Differenzieren sie verschlechtern würde?
A: Integrieren teilt die Koeffizienten effektiv durch $k$ (aus $1/k$ wird $1/k^2$), macht die Funktion also glatter. Differenzieren multipliziert mit $ik$, verstärkt hohe Frequenzen und kann die Konvergenz zerstören — deshalb ist es nicht ohne Weiteres erlaubt.
F: Woher stammt die Integrationskonstante $C$ in der Parabel-Darstellung?
A: Beim gliedweisen Integrieren ist die Stammfunktion nur bis auf eine additive Konstante bestimmt; $C$ ist gerade dieser $x$-unabhängige Gleichanteil (der Mittelwert $a_0/2$). Ihr Wert $\pi^2/12$ liefert, bei $x=0$ eingesetzt, die Basel-Summe $\sum 1/k^2=\pi^2/6$.
:::
