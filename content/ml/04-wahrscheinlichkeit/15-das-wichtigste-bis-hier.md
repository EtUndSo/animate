---
title: Das Wichtigste bis hier
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241500
summary: Unsicherheit rechnen: Ereignisse, Verteilungen, Kovarianz und die Normalverteilung
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ergebnisraum $\Omega$, Ereignisse als Teilmengen; Axiome: $P(A)\ge0$, $P(\Omega)=1$, Additivität für unvereinbare Ereignisse. Folgen: $P(A^{\mathrm c})=1-P(A)$, $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

</li>

<li>

Bedingt: $P(A\mid B)=P(A\cap B)/P(B)$; Produktregel $P(A\cap B)=P(A\mid B)P(B)$; totale Wahrscheinlichkeit $P(A)=\sum_iP(A\mid B_i)P(B_i)$.

</li>

<li>

Bayes: $P(B\mid A)=P(A\mid B)P(B)/P(A)$; bei kleiner Basisrate sind die meisten Alarme Fehlalarme; natürliche Häufigkeiten machen das sichtbar.

</li>

<li>

Unabhängig: $P(A\cap B)=P(A)P(B)$; unvereinbar ist nicht unabhängig; paarweise ist nicht gegenseitig; bedingt unabhängig ist nicht unabhängig.

</li>

<li>

Zufallsvariable = Funktion auf $\Omega$; diskret: $P(X=x)$, stetig: Dichte $p$ mit $P(a\le X\le b)=\int_a^bp$, Einheit eins durch die Einheit von $x$, Zahlenwert darf größer als $1$ sein; Verteilungsfunktion $F(x)=P(X\le x)$.

</li>

<li>

$\mathbb{E}[X]=\sum x\,P(X=x)=\mathbf{v}^{\top}\mathbf{p}$ bzw. $\int x\,p(x)\,\mathrm{d} x$, linear ohne Voraussetzung; $\operatorname{Var}(X)=\mathbb{E}[(X-\mu)^2]=\mathbb{E}[X^2]-\mu^2$, $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$. Mittelwert und $\operatorname{std}$ eines Datensatzes sind die der empirischen Verteilung.

</li>

<li>

$\mathrm{Ber}(\theta)$: $\theta$, $\theta(1-\theta)$; $\mathrm{Bin}(n,\theta)$: $n\theta$, $n\theta(1-\theta)$; $\mathcal U(a,b)$: $\tfrac{a+b}2$, $\tfrac{(b-a)^2}{12}$; $\mathcal N(\mu,\sigma^2)$: $68{,}3/95{,}4/99{,}7\,\%$ innerhalb $\pm1,2,3\,\sigma$; $Z=(X-\mu)/\sigma$, $\Phi$.

</li>

<li>

Gemeinsame, Rand- und bedingte Verteilung; unabhängig heißt Produkt der Randverteilungen; i.i.d. Stichprobe als Modell eines Datensatzes.

</li>

<li>

$\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E} X\,\mathbb{E} Y$, $\rho=\operatorname{Cov}/(\sigma_X\sigma_Y)\in[-1,1]$; $\operatorname{Var}(X+Y)=\operatorname{Var} X+\operatorname{Var} Y+2\operatorname{Cov}$; Kovarianz rechnet wie ein Skalarprodukt; unkorreliert ist nicht unabhängig.

</li>

<li>

$\boldsymbol{\Sigma}=\mathbb{E}[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}]$, Daten: $\mathbf{S}=\tfrac1N\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}$; $\operatorname{Cov}(\mathbf{A}\mathbf{x}+\mathbf{b})=\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$, $\operatorname{Var}(\mathbf{u}^{\top}\mathbf{x})=\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$; psd, Eigenvektoren = Richtungen extremer Streuung.

</li>

<li>

$\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$: Höhenlinien = Ellipsen konstanten Mahalanobis-Abstands, Halbachsen $\Delta\sqrt{\lambda_i}$; im Eigensystem unabhängige Komponenten; bleibt unter $\mathbf{A}\mathbf{x}+\mathbf{b}$ normal; bedingt: $\mu_1+\tfrac{\Sigma_{12}}{\Sigma_{22}}(x_2-\mu_2)$, $\Sigma_{11}(1-\rho^2)$; gemeinsam normal und unkorreliert heißt unabhängig.

</li>

<li>

Mittelwert von $n$ i.i.d.: Standardfehler $\sigma/\sqrt n$; Tschebyschow $P(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$; Gesetz der großen Zahlen; zentraler Grenzwertsatz: standardisierte Mittelwerte werden normalverteilt.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Mit Unsicherheit rechnet man, indem man jedem Ereignis eine Wahrscheinlichkeit gibt, die sich wie ein Anteil an einer Gesamtmenge vom Inhalt $1$ verhält; eine neue Information schränkt die Gesamtmenge auf die passenden Fälle ein, und der Satz von Bayes gewichtet dabei jede mögliche Ursache mit ihrer Basisrate, weshalb bei seltenen Ursachen auch ein guter Befund oft ein Fehlalarm ist.

</li>

<li>

Den typischen Wert einer schwankenden Größe gibt ihr Erwartungswert an, ihre Streuung die Varianz, und das gemeinsame Schwanken mehrerer Größen die Kovarianzmatrix, die wie ein Skalarprodukt rechnet: Sie liefert die Varianz jeder Linearkombination als quadratische Form, ist deshalb positiv semidefinit und zeigt mit ihren Eigenvektoren die Richtungen extremer Streuung.

</li>

<li>

Weil sich die Varianzen unabhängiger Größen addieren, wird ein Mittelwert aus $n$ Messungen mit $\sigma/\sqrt n$ genauer und nähert sich dem Erwartungswert, und weil Summen vieler unabhängiger Beiträge nach dem zentralen Grenzwertsatz normalverteilt sind, ist die Normalverteilung, deren Höhenlinien im Eigensystem der Kovarianzmatrix Ellipsen sind, die natürliche Beschreibung von Rauschen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Prinzip: Wahrscheinlichkeit verhält sich wie eine Masse vom Gesamtgewicht $1$, die über die möglichen Ausgänge verteilt ist. Ereignisse sind Teile dieser Masse, Bedingen schneidet einen Teil heraus und wiegt ihn neu auf $1$, Unabhängigkeit heißt, dass sich die Masse als Produkt verteilt, der Erwartungswert ist ihr Schwerpunkt und die Varianz ihr Trägheitsmoment um den Schwerpunkt. Mit der Kovarianz wird das Wiegen von Abweichungen zu einem Skalarprodukt, und die Geometrie aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) und [Grundlagen 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) gilt für Zufallsgrößen.

| Ergebnis | Woher es kommt |
|---|---|
| Gegenereignis, Additionssatz | Masse ist additiv und hat das Gesamtgewicht $1$ (Abschnitt [2](wahrscheinlichkeit-2.html#stufe-2)) |
| Bedingte Wahrscheinlichkeit | Masse auf $B$ beschränken und neu auf $1$ wiegen (Abschnitt [3](bedingte-wahrscheinlichkeit.html#stufe-3)) |
| Produktregel, totale Wahrscheinlichkeit | bedingte Wahrscheinlichkeit nach dem Zähler aufgelöst; Masse nach Fällen zerlegt (Abschnitt [3](bedingte-wahrscheinlichkeit.html#stufe-3)) |
| Satz von Bayes, Basisratenfehler | Produktregel in zwei Richtungen; die Basisrate wiegt jeden Fall (Abschnitt [4](der-satz-von-bayes.html#stufe-4)) |
| Unabhängigkeit | die Masse verteilt sich als Produkt (Abschnitte [5](unabhangigkeit.html#stufe-5) und [9](mehrere-zufallsvariablen.html#stufe-9)) |
| Dichte mit Einheit | Masse pro Längeneinheit (Abschnitt [6](zufallsvariablen-und-verteilungen.html#stufe-6)) |
| Erwartungswert, Linearität | Schwerpunkt; gewichtete Summe mit festen Gewichten (Abschnitt [7](erwartungswert-und-varianz.html#stufe-7)) |
| Verschiebungsformel | Trägheitsmoment um den Nullpunkt minus Anteil des Schwerpunkts (Abschnitt [7](erwartungswert-und-varianz.html#stufe-7)) |
| Varianz einer Summe, $\vert \rho\vert \le1$ | Kovarianz als Skalarprodukt: Pythagoras und Cauchy-Schwarz (Abschnitt [10](kovarianz-und-korrelation.html#stufe-10)) |
| Kovarianzmatrix psd, Hauptachsen | jede Projektion hat eine Varianz $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}\ge0$ (Abschnitt [11](zufallsvektoren-und-die-kovarianzmatrix.html#stufe-11)) |
| Ellipsen der Normalverteilung | quadratische Form im Eigensystem, Drehung mit Flächenfaktor $1$ (Abschnitt [12](die-mehrdimensionale-normalverteilung.html#stufe-12)) |
| Standardfehler, Gesetz der großen Zahlen | Varianzen unabhängiger Summanden addieren sich, Mitteln teilt durch $n^2$ (Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13)) |
| Zentraler Grenzwertsatz | wiederholte Faltung, bei der nur Erwartungswert und Varianz übrig bleiben (Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13)) |
