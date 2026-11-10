---
title: Stufe 12: Der zentrale Grenzwertsatz
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3181300
summary: Das Gesetz der großen Zahlen sagt, dass der Mittelwert gegen mu läuft.
tags: standardisierte Zufallsvariable, charakteristische Funktion
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Das Gesetz der großen Zahlen sagt, dass der Mittelwert gegen $\mu$ läuft. Diese Stufe sagt, wie groß die verbleibende Abweichung ist und welche Form sie hat.
:::

**Die Idee.** Addiert man viele kleine unabhängige Beiträge, geht jede Einzelheit ihrer Verteilung verloren. Übrig bleiben nur Mittelwert und Varianz. Die Form der Summe ist immer dieselbe Glocke (Abb. [12](#abb-12)).

**Standardisieren.** Für eine Zufallsvariable $X$ mit $\mathbb{E}(X)=\mu$, $\operatorname{Var}(X)=\sigma^2$ heißt $X^*=(X-\mu)/\sigma$ die __standardisierte Zufallsvariable__ zu $X$. Aus [(7.1)](der-erwartungswert.html#gl-7-1) und [(8.2)](varianz-kovarianz-und-tschebyschew.html#gl-8-2) folgt $\mathbb{E}(X^*)=0$ und $\operatorname{Var}(X^*)=1$.

Für $S_n=X_1+\dots+X_n$ mit unabhängigen $X_j$, $\mathbb{E}(X_j)=\mu$, $\operatorname{Var}(X_j)=\sigma^2$ gilt nach [(11.3)](das-gesetz-der-groen-zahlen.html#gl-11-3) $\mathbb{E}(S_n)=n\mu$ und $\operatorname{Var}(S_n)=n\sigma^2$. Also ist

<span class="anker" id="gl-12-1"></span>
$$S_n^*=\frac{S_n-n\mu}{\sqrt n\,\sigma}=\frac{\sqrt n}\sigma\bigl(\overline X_n-\mu\bigr). \tag{12.1}$$

Für $n=1$ ist das $X_1^*$. Aus $\mathbb{E}(S_n^*)=0$ und $\operatorname{Var}(S_n^*)=1$ liest man ab: Die typische Schwankung von $\overline X_n$ um $\mu$ hat die Größe $\sigma/\sqrt n$. Wer zehnmal genauer sein will, muss hundertmal mehr messen.

:::satz Satz 12.1 (Zentraler Grenzwertsatz)
<span class="anker" id="satz-12-1"></span>

Sei $(X_i)_{i\in\mathbb{N}}$ eine i.i.d.-Folge auf $(\Omega,\mathcal E,\mathbb{P})$ mit endlichem Erwartungswert und endlicher Varianz $\sigma^2>0$. Dann ist $S_n^*$ für große $n$ asymptotisch standard-normalverteilt, das heißt, für alle $x\in\mathbb{R}$ gilt

<span class="anker" id="gl-12-2"></span>
$$\mathbb{P}(S_n^*\le x)\to\Phi(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^x\mathrm{e}^{-y^2/2}\,\mathrm{d} y\quad\text{für }n\to\infty. \tag{12.2}$$
:::

⁠**So liest man das:** Die Gestalt der Schwankungen hängt von der Verteilung der $X_i$ gar nicht ab. Das erklärt, warum Messfehler aus vielen kleinen Ursachen normalverteilt sind. Praktisch rechnet man für großes $n$ mit $\mathbb{P}(a<S_n^*\le b)\approx\Phi(b)-\Phi(a)$.

:::abbildung hm3/k8zgs 12
Standardisierte Summe von $n$ Vierer-Würfeln, exakt berechnet und als Dichte aufgetragen, darüber die Glocke. Schon bei $n=16$ ist kaum ein Unterschied zu sehen.
:::

::::beispiel
80 Vierer-Würfel haben $\mathbb{E}(S_{80})=200$ und $\operatorname{Var}(S_{80})=100$. Damit ist (exakt wäre es $0{,}768$)

$$\mathbb{P}(190<S_{80}\le215)=\mathbb{P}(-1<S_{80}^*\le1{,}5)\approx\Phi(1{,}5)-\Phi(-1)=0{,}9332-0{,}1587=0{,}7745.$$
::::

**Wie groß muss eine Stichprobe sein?** Eine Serie hat den unbekannten Ausschussanteil $p\in(0,1)$. Wie viele Teile muss man prüfen, damit der gemessene Anteil mit mindestens 90 % um weniger als 3 Prozentpunkte von $p$ abweicht? Jedes Teil ist ein Bernoulli-Experiment mit $\mu=p$, $\sigma^2=p(1-p)$, gesucht ist $\mathbb{P}(A_n)\ge0{,}9$ für $A_n=\{|\overline X_n-p|<0{,}03\}$. Mit [(12.1)](#gl-12-1) ist $A_n=\bigl\{|S_n^*|<0{,}03\sqrt{n/(p(1-p))}\bigr\}$, und wegen $\Phi(-x)=1-\Phi(x)$ folgt

$$\mathbb{P}(A_n)\approx2\,\Phi\Bigl(0{,}03\sqrt{\frac n{p(1-p)}}\Bigr)-1\ge2\,\Phi\bigl(0{,}06\sqrt n\bigr)-1.$$

Im letzten Schritt steckt $p(1-p)\le\frac14$, der Scheitel der Parabel, so fällt das unbekannte $p$ heraus. Aus $\Phi(0{,}06\sqrt n)=0{,}95$ gibt die Tabelle $0{,}06\sqrt n=1{,}645$, also $n\approx752$.

**Die Brücke zur Fourier-Analyse.** Ein vollständiger Beweis von Satz [12.1](#satz-12-1) ist aufwendig. Die Idee benutzt die __charakteristische Funktion__

<span class="anker" id="gl-12-3"></span>
$$\varphi_X(t):=\mathbb{E}(\mathrm{e}^{\mathrm itX}). \tag{12.3}$$

Für absolut stetiges $X$ ist nach [(7.3)](der-erwartungswert.html#gl-7-3) $\varphi_X(t)=\int_\mathbb{R} f_X(x)\,\mathrm{e}^{\mathrm itx}\,\mathrm{d} x$. Das ist bis auf den Faktor $1/\sqrt{2\pi}$ die inverse Fourier-Transformierte von $f_X$ ([Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). Die Gaußfunktion $\frac1{\sqrt{2\pi}}\mathrm{e}^{-x^2/2}$ bleibt unter dieser Transformation unverändert. Daher gilt

<span class="anker" id="gl-12-4"></span>
$$X\sim\mathcal N(0,1)\iff\varphi_X(t)=\mathrm{e}^{-t^2/2}. \tag{12.4}$$

:::herleitung Warum die Glocke entsteht (Heuristik, kein Beweis)
Setze $Y_j=(X_j-\mu)/(\sigma\sqrt n)$. Die $Y_j$ sind i.i.d., $\mathbb{E}(Y_j)=0$, und $S_n^*=Y_1+\dots+Y_n$.

⁠**Schritt 1.** Die Exponentialfunktion macht aus der Summe ein Produkt, und die Faktoren $\exp(\mathrm itY_j)$ sind unabhängig. Nach [(11.3)](das-gesetz-der-groen-zahlen.html#gl-11-3), angewandt auf komplexe Zufallsvariablen, und wegen der identischen Verteilung ist

$$\mathbb{E}(\exp(\mathrm itS_n^*))=\mathbb{E}[\exp(\mathrm itY_1)]\cdots\mathbb{E}[\exp(\mathrm itY_n)]=\mathbb{E}[\exp(\mathrm itY_1)]^n.$$

⁠**Schritt 2.** Für eine Zufallsvariable $X$ gibt die Taylorreihe mit der Linearität

$$\mathbb{E}[\exp(\mathrm itX)]=\mathbb{E}\Bigl(1+\mathrm itX-\frac{t^2}2X^2+\dots\Bigr)=1+\mathrm it\,\mathbb{E}(X)-\frac{t^2}2\mathbb{E}(X^2)+\dots$$

⁠**Schritt 3.** Für $Y_1$ ist $\mathbb{E}(Y_1)=0$ und $\mathbb{E}(Y_1^2)=\mathbb{E}[(X_1-\mu)^2]/(\sigma^2n)=1/n$. Damit

$$\varphi_{S_n^*}(t)\approx\Bigl(1-\frac{t^2}{2n}\Bigr)^n\approx\mathrm{e}^{-t^2/2}.$$

Der Term erster Ordnung fällt weg, vom zweiten bleibt nur die Varianz, alle höheren verschwinden für großes $n$.
:::

:::frage Warum steht $\sqrt n$ im Nenner und nicht $n$?
Mit $n$ schrumpft die Verteilung auf einen Punkt, ohne Nenner wird sie immer breiter. Nur $\sqrt n$ hält die Varianz bei 1.
:::

:::aufgabe Aufgabe 19 ★★ Ersatzteile
<span class="anker" id="aufg-19"></span>

Eine Anlage braucht Licht. Fällt eine LED aus, wird sofort die nächste eingesetzt, die Lebensdauern sind unabhängig wie im Rechenmodell.

<ol class="al">

<li>

Wie groß ist näherungsweise die Wahrscheinlichkeit, dass 16 LEDs länger als 40 Jahre reichen?

</li>

<li>

Wie viele LEDs braucht man, damit 40 Jahre mit einer Wahrscheinlichkeit von etwa 95 % erreicht werden?

</li>

</ol>

:::loesung
(a) $\mathbb{E}(S_{16})=32$, $\operatorname{Var}(S_{16})=64$, also $\mathbb{P}(S_{16}>40)=1-\mathbb{P}(S_{16}^*\le1)\approx0{,}159$, exakt $0{,}157$. (b) Aus $(40-2n)/(2\sqrt n)=-1{,}645$ folgt mit $w=\sqrt n$: $w^2-1{,}645\,w-20=0$, also $w\approx5{,}37$, $n\approx29$.
:::
:::
