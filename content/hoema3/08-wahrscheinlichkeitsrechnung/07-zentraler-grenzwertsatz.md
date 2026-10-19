---
title: Der zentrale Grenzwertsatz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080700
summary: Von Grund auf – warum die Glockenkurve überall auftaucht. Standardisiert man die Summe $S_n=\sum X_i$ unabhängiger, identisch verteilter Variablen zu $S_n^*=\frac{S_n-n\mu}{\sigma\sqrt n}$, so konvergiert ihre Verteilung – unabhängig von der Ausgangsverteilung – gegen die Standard-Normalverteilung. Die Fluktuationen des Mittels sind von der Ordnung $\sigma/\sqrt n$ und normalförmig. Der Beweis läuft über die charakteristische Funktion, eine Fourier-Transformierte.
tags: zentraler Grenzwertsatz, Standardisierung, Normalverteilung, charakteristische Funktion, Fourier-Transformation, i.i.d., Fluktuationen, Wahlprognose
---

:::grafik
Einstiegs-Animation: Links eine beliebige, krumme Ausgangsverteilung (schief, mehrgipflig — egal). Man zieht $n$
unabhängige Stichproben, summiert sie und __standardisiert__. Mit wachsendem $n$ formt sich das Histogramm der
standardisierten Summe $S_n^*$ immer glatter zur **Glockenkurve** $\Phi$ — ganz gleich, wie die Ausgangsverteilung
aussah. Rechts die zwei Botschaften: Die typische Fluktuation des Mittels $\overline X_n$ um $\mu$ ist von der
**Größe** $\sigma/\sqrt n$ (sie schrumpft), und ihre **Gestalt** ist universell normalverteilt. Kernbotschaft: Summen
vieler kleiner unabhängiger Zufälle sind immer normalverteilt — deshalb ist die Gaußkurve überall.
:::

:::konzept
Das Gesetz der großen Zahlen sagt, **dass** das Mittel $\overline X_n$ gegen $\mu$ strebt. Der __zentrale
Grenzwertsatz__ (ZGS) sagt, **wie** es das tut: Skaliert man die Abweichung $\overline X_n-\mu$ richtig (mit
$\sqrt n$), so ist ihre Verteilung — __unabhängig von der Ausgangsverteilung__ — die Standard-Normalverteilung. Das
erklärt die alles überragende Rolle der Glockenkurve in Natur und Technik: Überall, wo sich viele kleine, unabhängige
Einflüsse **addieren** (Messrauschen, Teilchenbewegung, Stimmenauszählung), entsteht eine Normalverteilung. Der ZGS
ist zugleich ein schönes Beispiel für die Einheit der Mathematik: Sein Beweis läuft über die __charakteristische
Funktion__ — nichts anderes als eine Fourier-Transformierte der Dichte.
:::

**Worum es geht:** Wir __standardisieren__ Zufallsvariablen und Summen, formulieren den __zentralen Grenzwertsatz__
(Satz 8.61), skizzieren den Beweis über die __charakteristische Funktion__ (Satz/Def. 8.62) und wenden ihn auf eine
__Wahlprognose__ an.

## Standardisierung

Hat $X$ den Erwartungswert $\mu$ und die Varianz $\sigma^2$, so ist die __standardisierte Zufallsvariable__
$$X^*=\frac{X-\mu}{\sigma},\qquad E(X^*)=0,\ \ \mathrm{Var}(X^*)=1.$$
Man verschiebt auf Mittel $0$ und skaliert auf Streuung $1$ — die „Einheitsform" jeder Verteilung. Für die
__Partialsumme__ $S_n=X_1+\dots+X_n$ unabhängiger $X_i$ (gleiches $\mu,\sigma^2$) ist nach Satz 8.53 $E(S_n)=n\mu$
und $\mathrm{Var}(S_n)=n\sigma^2$, also
$$S_n^*=\frac{S_n-n\mu}{\sigma\sqrt n},\qquad S_n^*=\frac{\sqrt n}{\sigma}\,(\overline X_n-\mu).$$
Der Zusammenhang mit dem Mittel zeigt direkt: Die typischen __Fluktuationen__ von $\overline X_n$ um $\mu$ sind von
der Ordnung $\sigma/\sqrt n$. Der entscheidende Skalierungsfaktor ist $\sqrt n$ (nicht $n$): Teilt man nur durch $n$
(Gesetz der großen Zahlen), verschwindet die Abweichung; multipliziert man die Abweichung mit $\sqrt n$, wird sie
gerade sichtbar — als normalverteilte Schwankung.

## Der zentrale Grenzwertsatz

__Satz 8.61 (ZGS).__ Sei $(X_i)$ eine Folge __i.i.d.__ Zufallsvariablen mit endlichem $\mu$ und $\sigma^2$. Dann ist
die standardisierte Summe $S_n^*$ für große $n$ __asymptotisch standard-normalverteilt__: für alle $x\in\mathbb R$
$$P(S_n^*\le x)\ \xrightarrow{n\to\infty}\ \Phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-y^2/2}\,dy.$$
Das Bemerkenswerte: Der Grenzwert $\Phi$ hängt **nicht** von der Verteilung der $X_i$ ab — nur $\mu$ und $\sigma^2$
gehen (über die Standardisierung) ein. Der ZGS macht also nicht nur eine Aussage über die **Größe** der Fluktuationen
(das tat schon die Varianz-Rechnung), sondern über ihre **Gestalt** — und die ist universell die Glocke.

:::grafik
Links der Standardisierungs-Mechanismus: Ausgangsverteilung → Summe (breiter, Varianz $n\sigma^2$) → standardisiert
(Varianz $1$). Rechts das Herzstück: Histogramme von $S_n^*$ für $n=1,2,5,30$, die sich — egal bei welcher
Ausgangsverteilung — an dieselbe Glockenkurve $\Phi$ anschmiegen. Beschriftung „Form universell, nur $\mu,\sigma$
zählen".
:::

## Beweisidee: die charakteristische Funktion

__Definition 8.62.__ Die __charakteristische Funktion__ einer Zufallsvariablen $X$ ist
$$\varphi_X(t)=E(e^{itX}).$$
Für absolut-stetiges $X$ mit Dichte $f_X$ ist $\varphi_X(t)=\int_{\mathbb R}f_X(x)e^{itx}\,dx$ (Satz 8.31) — bis auf
den Faktor $1/\sqrt{2\pi}$ die __Fourier-Transformierte__ der Dichte. Hier schließt sich der Kreis zur
Fourier-Analysis: Die Gaußfunktion ist ihr **eigener** Fixpunkt unter der Fourier-Transformation,
$$f_X(x)=\tfrac{1}{\sqrt{2\pi}}e^{-x^2/2}\ \Longleftrightarrow\ \varphi_X(t)=e^{-t^2/2},$$
also ist $X\sim\mathcal N(0,1)$ gleichbedeutend mit $\varphi_X(t)=e^{-t^2/2}$.

__Warum $\varphi_{S_n^*}(t)\to e^{-t^2/2}$?__ Setzt man $Y_j=\frac{X_j-\mu}{\sigma\sqrt n}$ (i.i.d., $E(Y_j)=0$,
$E(Y_j^2)=\frac{1}{n}$), so ist $S_n^*=Y_1+\dots+Y_n$. Weil die $e^{itY_j}$ unabhängig und identisch verteilt sind,
faktorisiert der Erwartungswert (Produkteigenschaft):
$$\varphi_{S_n^*}(t)=E\big(e^{itS_n^*}\big)=\prod_{j=1}^n E\big(e^{itY_j}\big)=\big[E(e^{itY_1})\big]^n.$$
Die Taylor-Entwicklung der Exponentialfunktion und die Linearität des Erwartungswerts geben
$$E(e^{itY_1})=1+itE(Y_1)-\tfrac{t^2}{2}E(Y_1^2)+\dots=1-\frac{t^2}{2n}+\dots,$$
und mit der Grenzwertformel $\big(1-\frac{t^2}{2n}\big)^n\to e^{-t^2/2}$ folgt $\varphi_{S_n^*}(t)\to e^{-t^2/2}$ —
die charakteristische Funktion der Standard-Normalverteilung. Da $\varphi$ die Verteilung eindeutig festlegt, ist
$S_n^*$ asymptotisch normal. (Der vollständige Beweis ist technisch aufwendig; dies ist die tragende Heuristik.)

## Anwendung: Wahlprognose

__Beispiel 8.63.__ Ein Kandidat hat den unbekannten Stimmenanteil $p$. Man wertet $n$ zufällige Stimmzettel
$X_j\in\{0,1\}$ aus (Bernoulli, $E(X_j)=p$, $\mathrm{Var}(X_j)=p(1-p)$). Wie groß muss $n$ sein, damit die Prognose
$\overline X_n$ mit höchstens $5\%$ Wahrscheinlichkeit um mehr als $1\%$ danebenliegt, also $P(|\overline
X_n-p|<0.01)\ge0.95$? Mit $S_n^*=\frac{\sqrt n}{\sigma}(\overline X_n-p)$ und dem ZGS:
$$P(|\overline X_n-p|<0.01)=P\Big(|S_n^*|<0.01\sqrt{\tfrac{n}{p(1-p)}}\Big)\approx 2\Phi\Big(0.01\sqrt{\tfrac{n}{p(1-p)}}\Big)-1.$$
Mit der **worst-case**-Abschätzung $p(1-p)\le\tfrac14$ (Maximum bei $p=\tfrac12$) ist das $\ge
2\Phi(0.02\sqrt n)-1$. Die Forderung $\ge0.95$ führt auf $\Phi(0.02\sqrt n)\approx0.975$; mit dem Tabellenwert
$\Phi(1.96)=0.975$ also $0.02\sqrt n\approx1.96$, d. h.
$$n\approx\Big(\frac{1.96}{0.02}\Big)^2=(50\cdot1.96)^2\approx 9600.$$
Rund $9600$ Stimmzettel genügen — bemerkenswert wenige, und die Zahl hängt **nicht** von der (riesigen)
Gesamtwählerzahl ab. Das ist die praktische Kraft des ZGS: aus der universellen Glockenform konkrete Stichprobengrößen.

**Stolperstein:** (1) Der Skalierungsfaktor ist $\sqrt n$, nicht $n$: Durch $n$ geteilt verschwindet die Abweichung
(Gesetz der großen Zahlen), mit $\sqrt n$ skaliert bleibt die normalverteilte Fluktuation sichtbar. (2) Der ZGS
braucht __endliche Varianz__ — bei Verteilungen mit $\sigma^2=\infty$ (z. B. Cauchy) gilt er nicht. (3) Universell
ist nur die __standardisierte__ Summe; die Verteilung von $S_n$ selbst wird immer breiter ($\mathrm{Var}=n\sigma^2$).
(4) „$\approx$ normal" ist asymptotisch — für kleine $n$ oder stark schiefe Ausgangsverteilungen kann die Näherung
schlecht sein. (5) Die charakteristische Funktion ist eine Fourier-Transformierte — die Normalverteilung taucht auf,
weil die Gaußfunktion deren Fixpunkt ist.

:::kern
__Standardisierung__ $X^*=\frac{X-\mu}{\sigma}$ ($E=0$, $\mathrm{Var}=1$); Summe $S_n=\sum X_i$:
$S_n^*=\frac{S_n-n\mu}{\sigma\sqrt n}=\frac{\sqrt n}{\sigma}(\overline X_n-\mu)$. Fluktuationen von $\overline X_n$
der Ordnung $\sigma/\sqrt n$. __ZGS__ (Satz 8.61): für i.i.d. $(X_i)$ mit endlichem $\mu,\sigma^2$ gilt
$P(S_n^*\le x)\to\Phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-y^2/2}dy$ — **unabhängig** von der
Ausgangsverteilung (nur $\mu,\sigma^2$ zählen; Form universell normal). __Beweisidee__ via __charakteristische
Funktion__ $\varphi_X(t)=E(e^{itX})$ (= Fourier-Transformierte der Dichte, Def. 8.62): $\varphi_{S_n^*}=[\varphi_{Y_1}]^n$
mit $\varphi_{Y_1}(t)\approx1-\frac{t^2}{2n}$, also $\to e^{-t^2/2}=\varphi_{\mathcal N(0,1)}$ (Gauß = Fixpunkt der
Fourier-Transformation). __Anwendung__ Wahlprognose: $P(|\overline X_n-p|<0.01)\ge0.95$, $p(1-p)\le\tfrac14$,
$\Phi(1.96)=0.975$ ⇒ $n\approx9600$ (unabhängig von der Wählerzahl).
:::

Damit schließt die Wahrscheinlichkeitsrechnung — und mit ihr die gesamte Höhere Mathematik III: von der
Vektoranalysis über die Integralsätze, Funktionenfolgen und Fourier-Reihen bis zur Stochastik. Der zentrale
Grenzwertsatz verbindet dabei alle Fäden: Die Normalverteilung des Zufalls ist dieselbe Gaußfunktion, die als Fixpunkt
der Fourier-Transformation schon die Analysis durchzog — ein letzter Beleg für die tiefe Einheit der Mathematik.

:::quiz
F: Was fügt der zentrale Grenzwertsatz dem Gesetz der großen Zahlen hinzu?
A: Das Gesetz der großen Zahlen sagt nur, dass das Mittel gegen $\mu$ strebt. Der ZGS beschreibt zusätzlich die **Gestalt** der Abweichung: Richtig skaliert ist sie normalverteilt — er quantifiziert also, wie das Mittel um $\mu$ schwankt, nicht nur dass es konvergiert.
F: Warum standardisiert man zu $S_n^*=\frac{S_n-n\mu}{\sigma\sqrt n}$?
A: $S_n$ hat Erwartungswert $n\mu$ und Varianz $n\sigma^2$; Abziehen von $n\mu$ zentriert auf $0$, Teilen durch $\sigma\sqrt n$ normiert die Streuung auf $1$. Erst in dieser „Einheitsform" ($E=0$, $\mathrm{Var}=1$) kann ein universeller Grenzwert existieren.
F: Warum ist der Skalierungsfaktor $\sqrt n$ und nicht $n$?
A: Teilt man die Summe durch $n$, erhält man das Mittel, dessen Abweichung gegen $0$ geht (Gesetz der großen Zahlen) — zu stark skaliert, man sieht nichts. Mit $\sqrt n$ multipliziert bleibt die Fluktuation von konstanter Größenordnung sichtbar, gerade als normalverteilte Schwankung der Ordnung $\sigma/\sqrt n$.
F: Was ist die überraschendste Aussage des ZGS?
A: Dass der Grenzwert $\Phi$ völlig **unabhängig** von der Ausgangsverteilung ist — ob die $X_i$ Münzwürfe, Würfel oder schiefe Verteilungen sind, spielt keine Rolle. Nur Erwartungswert und Varianz gehen ein; die Form ist immer die Glocke.
F: Warum taucht die Normalverteilung so universell in Natur und Technik auf?
A: Überall dort, wo sich viele kleine, unabhängige Zufallseinflüsse **addieren** (Messrauschen, Diffusion, Summen von Fehlern), greift der ZGS. Die Summe ist dann näherungsweise normalverteilt — die Glockenkurve ist die „Attraktorform" von Summen unabhängiger Beiträge.
F: Was ist die charakteristische Funktion, und wie hängt sie mit Fourier zusammen?
A: $\varphi_X(t)=E(e^{itX})$; für eine Dichte ist das $\int f_X(x)e^{itx}dx$, also bis auf $1/\sqrt{2\pi}$ die Fourier-Transformierte von $f_X$. Sie legt die Verteilung eindeutig fest und verwandelt die Faltung von Summen in ein Produkt — ideal für Summen unabhängiger Variablen.
F: Warum faktorisiert $\varphi_{S_n^*}(t)$ in ein Produkt, und wie wird daraus eine $n$-te Potenz?
A: Mit $S_n^*=\sum Y_j$ ist $e^{itS_n^*}=\prod e^{itY_j}$; da die $Y_j$ unabhängig sind, sind es auch die $e^{itY_j}$, und der Erwartungswert des Produkts ist das Produkt der Erwartungswerte. Weil die $Y_j$ zudem identisch verteilt sind, sind alle Faktoren gleich — es entsteht $[\varphi_{Y_1}(t)]^n$.
F: Wie liefert die Taylor-Entwicklung den Grenzwert $e^{-t^2/2}$?
A: Mit $E(Y_1)=0$ und $E(Y_1^2)=\frac1n$ ist $\varphi_{Y_1}(t)=1-\frac{t^2}{2n}+\dots$. Potenziert man das $n$-fach, ergibt $\big(1-\frac{t^2}{2n}\big)^n\to e^{-t^2/2}$ — genau die charakteristische Funktion der Standard-Normalverteilung, deren Fixpunkt-Eigenschaft unter Fourier den Kreis schließt.
F: Warum braucht der ZGS eine endliche Varianz?
A: Die Standardisierung durch $\sigma$ und die Taylor-Entwicklung bis zum $E(Y^2)$-Term setzen $\sigma^2<\infty$ voraus. Verteilungen mit unendlicher Varianz (z. B. Cauchy) haben keinen solchen Grenzwert — dort mitteln sich die Ausreißer nicht zur Glocke, und der Satz gilt nicht.
F: Warum hängt die nötige Stichprobengröße in der Wahlprognose ($n\approx9600$) nicht von der Wählerzahl ab?
A: Der ZGS skaliert mit $\sqrt n$ der Stichprobe, nicht mit der Grundgesamtheit; die Genauigkeit $\sigma/\sqrt n$ hängt nur von der Stichprobengröße und $p(1-p)\le\tfrac14$ ab. Deshalb genügen für eine feste Fehlertoleranz immer dieselben ~9600 Zettel, egal ob 100000 oder 50 Millionen Wähler.
:::
