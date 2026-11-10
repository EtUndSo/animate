---
title: Stufe 7: Der Erwartungswert
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180800
summary: Eine Verteilung enthält alles, ist aber unhandlich.
tags: Erwartungswert, Maßintegral
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Eine Verteilung enthält alles, ist aber unhandlich. Diese Stufe fasst sie in einer Zahl zusammen: dem Wert, den $X$ im Mittel annimmt.
:::

**Die Idee.** Beobachtet man $X$ sehr oft, tritt der Wert $x_k$ mit dem Anteil $\mathbb{P}(X=x_k)$ auf. Der Mittelwert der Beobachtungen ist dann $\sum_kx_k\,\mathbb{P}(X=x_k)$. Das ist der Schwerpunkt: Legt man die Massen $\mathbb{P}(X=x_k)$ auf die Zahlengerade, balanciert sie genau dort (Abb. [7](#abb-7)).

:::definition Definition 7.1 (Erwartungswert)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Für diskretes $X$ ist $\mathbb{E}(X)=\sum_kx_k\,\mathbb{P}(X=x_k)$, falls die Summe absolut konvergiert.

</li>

<li>

Für absolut stetiges $X$ ist $\mathbb{E}(X)=\int_\mathbb{R} x\,f_X(x)\,\mathrm{d} x$, falls das Integral absolut konvergiert.

</li>

</ol>

$\mathbb{E}(X)$ heißt __Erwartungswert__ von $X$ und wird oft mit $\mu_X$ bezeichnet.
:::

⁠**So liest man das:** Beide Fälle mitteln $x$ über die Verteilung. Allgemein schreibt man das als __Maßintegral__ $\mathbb{E}(X)=\int_\mathbb{R} x\,\mathbb{P}_X(\mathrm{d} x)$, wobei formal $\mathbb{P}_X(\mathrm{d} x)=\sum_kp_X(x_k)\,\delta_{x_k}(\mathrm{d} x)$ bzw. $\mathbb{P}_X(\mathrm{d} x)=f_X(x)\,\mathrm{d} x$ gilt. Dieses Integral braucht einen erweiterten Integralbegriff, deshalb bleibt es hier bei den beiden Fällen. Die absolute Konvergenz macht den Wert unabhängig von der Reihenfolge.

::::beispiel [Beispiele]
$\mathbb{E}(W_1)=\frac{1+2+3+4}4=\frac52$, $\mathbb{E}(S)=5$. Für die LED gibt partielle Integration

$$\mathbb{E}(X)=\int_0^\infty x\,\tfrac12\mathrm{e}^{-x/2}\,\mathrm{d} x=\Bigl[-x\,\mathrm{e}^{-x/2}\Bigr]_0^\infty+\int_0^\infty\mathrm{e}^{-x/2}\,\mathrm{d} x=2.$$

Die Gleichverteilung auf $[a,b]$ hat $\mathbb{E}(X)=\frac{a+b}2$, die Mitte.
::::

⁠**Grenzfall:** $\mathbb{E}(c)=c$ für eine Konstante.

:::abbildung hm3/k8schwerpunkt 7
Der Erwartungswert als Schwerpunkt. Bei der LED ist die Dichte bei 0 am größten, der Schwerpunkt liegt trotzdem bei 2, weil der lange Ausläufer mit großem Hebel zieht.
:::

:::herleitung Poisson und Normalverteilung
Poisson: Der Summand $k=0$ fällt weg, und $\frac{k}{k!}=\frac1{(k-1)!}$:

$$\mathbb{E}(X)=\sum_{k=0}^\infty k\,\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda}=\lambda\,\mathrm{e}^{-\lambda}\sum_{k=1}^\infty\frac{\lambda^{k-1}}{(k-1)!}=\lambda.$$

Normal: Zerlege $x=(x-\mu)+\mu$. Die Dichte ist auf 1 normiert, und $(x-\mu)\,f_X(x)$ ist punktsymmetrisch um $\mu$, das Integral darüber verschwindet. Also ist $\mathbb{E}(X)=\mu$.
:::

:::satz Satz 7.2 (Linearität und Monotonie)
<span class="anker" id="satz-7-2"></span>

Für Zufallsvariablen $X,Y$ auf demselben Wahrscheinlichkeitsraum und $c\in\mathbb{R}$ gilt, sofern die Erwartungswerte existieren,

<span class="anker" id="gl-7-1"></span>
$$\mathbb{E}(X+cY)=\mathbb{E}(X)+c\,\mathbb{E}(Y), \tag{7.1}$$

und aus $X\le Y$ folgt $\mathbb{E}(X)\le\mathbb{E}(Y)$.
:::

:::beweis Für einen diskreten Raum
Sei $\Omega=\{\omega_1,\omega_2,\dots\}$, $\mathcal E=\mathcal P(\Omega)$. Fasst man in $\sum_iX(\omega_i)\,\mathbb{P}(\omega_i)$ alle $\omega_i$ mit demselben Wert $x_k$ zusammen, entsteht $\sum_kx_k\,\mathbb{P}(X=x_k)$. Also ist

<span class="anker" id="gl-7-2"></span>
$$\mathbb{E}(X)=\sum_iX(\omega_i)\,\mathbb{P}(\omega_i), \tag{7.2}$$

und beide Aussagen lassen sich an den Summanden ablesen. Allgemein ist $\mathbb{E}$ ein Integral von $X$ über $\Omega$ bezüglich $\mathbb{P}$, und Integrale haben diese Eigenschaften.
:::

⁠**So liest man das:** [(7.1)](#gl-7-1) verlangt keine Unabhängigkeit. Für binomialverteiltes $X$ ist $X=\sum_{i=1}^nX_i$ mit $X_i(\omega)=\omega_i$ und $\mathbb{E}(X_i)=p$, also $\mathbb{E}(X)=np$. Ohne Zurücklegen ist jeder Zug für sich mit $M/N$ ein Treffer: Die Stichprobe aus der Kiste enthält im Mittel $5\cdot\frac4{20}=1$ defektes Teil.

**Funktionen von $X$.** Aus [(7.2)](#gl-7-2) folgt $\mathbb{E}(g(X))=\sum_ig(X(\omega_i))\,\mathbb{P}(\omega_i)$ für jede reelle Funktion $g$. Im absolut stetigen Fall gilt das Entsprechende.

:::satz Satz 7.3 (Erwartungswert einer Funktion)
<span class="anker" id="satz-7-3"></span>

Sei $X$ absolut stetig mit Dichte $f_X$ und $g:\mathbb{R}\to\mathbb{R}$ stetig. Dann gilt, falls das Integral absolut konvergiert,

<span class="anker" id="gl-7-3"></span>
$$\mathbb{E}(g(X))=\int_\mathbb{R} g(x)\,f_X(x)\,\mathrm{d} x. \tag{7.3}$$
:::

Der Satz wird hier ohne Beweis benutzt.

::::beispiel
Für die LED gibt zweimalige partielle Integration $\mathbb{E}(X^2)=8$. Das ist nicht $\mathbb{E}(X)^2=4$: Im Allgemeinen ist $\mathbb{E}(g(X))\neq g(\mathbb{E}(X))$.
::::

:::frage Ist der Erwartungswert der wahrscheinlichste Wert?
Nein. Bei der LED ist $\mathbb{P}(X<2)=1-\mathrm{e}^{-1}\approx0{,}63$, die meisten halten kürzer als der Mittelwert. Bei $W_1$ kommt $\frac52$ gar nicht vor.
:::

:::aufgabe Aufgabe 11 ★★ Wenn der Mittelwert nicht existiert
<span class="anker" id="aufg-11"></span>

Eine faire Münze wird geworfen, bis zum ersten Mal Kopf fällt. Geschieht das beim $n$-ten Wurf, zahlt ein Spiel $X$ aus.

<ol class="al">

<li>

Berechne $\mathbb{E}(X)$ für die Auszahlung $(5/4)^n$.

</li>

<li>

Zeige, dass bei der Auszahlung $2^n$ kein Erwartungswert existiert. Was bedeutet das für einen fairen Einsatz?

</li>

</ol>

:::loesung
Kopf fällt beim $n$-ten Wurf mit $2^{-n}$. (a) $\mathbb{E}(X)=\sum_{n\ge1}(\frac54)^n2^{-n}=\sum_{n\ge1}(\frac58)^n=\frac53$. (b) $\sum_{n\ge1}2^n2^{-n}=\sum_{n\ge1}1$ divergiert. Kein endlicher Einsatz ist fair, obwohl $\mathbb{P}(X\le8)=\frac78$ gilt.
:::
:::

Dass $X$ den Mittelwert $\mu$ hat, sagt noch nicht, dass $X$ nahe bei $\mu$ liegt.
