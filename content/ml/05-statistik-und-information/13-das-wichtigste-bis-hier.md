---
title: Das Wichtigste bis hier
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15251300
summary: Aus Daten schätzen und Überraschung messen
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Statistik schließt von Daten auf die Verteilung, die sie erzeugt hat; ein Modell ist eine Familie $P(X=x\mid\theta)$, ein Datensatz eine i.i.d. Stichprobe mit $P(\mathcal D\mid\theta)=\prod_iP(X=x_i\mid\theta)$.

</li>

<li>

Ein Schätzer $\hat\theta=g(X_1,\dots,X_N)$ ist eine Zufallsvariable mit einer Stichprobenverteilung; Verzerrung $\mathbb{E}[\hat\theta]-\theta$, Standardfehler $\sqrt{\operatorname{Var}(\hat\theta)}$, $\operatorname{MSE}=\operatorname{Bias}^2+\operatorname{Var}$; konsistent heißt $P(|\hat\theta_N-\theta|\ge\varepsilon)\to0$, und $\operatorname{MSE}\to0$ genügt.

</li>

<li>

$\hat\sigma^2_N=\frac1N\sum(X_i-\bar X)^2$ hat $\mathbb{E}=\frac{N-1}N\sigma^2$, weil $\bar x$ näher an den eigenen Daten liegt als $\mu$; $\hat\sigma^2_{N-1}$ ist erwartungstreu, aber nicht genauer, und $\hat\sigma_{N-1}$ unterschätzt $\sigma$.

</li>

<li>

Die Likelihood $\mathcal L(\theta)=P(\mathcal D\mid\theta)$ ist eine Funktion des Parameters, keine Verteilung über ihn; $\ell=\ln\mathcal L=\sum_i\ln P(X=x_i\mid\theta)$ hat das Maximum an derselben Stelle.

</li>

<li>

Maximum Likelihood: $\hat\theta_{\mathrm{ML}}=\operatorname*{arg\,max}\ell$; Bernoulli $N_1/N$; Normalverteilung $\hat\mu=\bar x$, $\hat\sigma^2=\hat\sigma^2_N$ (verzerrt); umkehrbare Umrechnungen rechnet man einfach mit.

</li>

<li>

Bayes für Parameter: $p(\theta\mid\mathcal D)\propto\mathcal L(\theta)\,p(\theta)$; Beta-Prior $\mathrm{Beta}(\alpha_1,\alpha_0)$ mit Bernoulli-Daten gibt $\mathrm{Beta}(\alpha_1+N_1,\alpha_0+N_0)$; Vorhersage $=\mathbb{E}[\theta\mid\mathcal D]=\frac{\alpha_1+N_1}{\alpha_1+\alpha_0+N}$, mit $\mathrm{Beta}(1,1)$ die Laplace-Regel $\frac{N_1+1}{N+2}$.

</li>

<li>

MAP: $\operatorname*{arg\,max}[\ell(\theta)+\ln p(\theta)]$; der Prior wirkt als Strafterm, der mit wachsendem $N$ an Gewicht verliert; mit Gauß-Prior das nach Kehrwerten der Varianzen gewichtete Mittel von $\bar x$ und $\mu_0$; MAP hängt von der Beschreibung des Parameters ab.

</li>

<li>

Informationsgehalt $I(A)=\log_2\frac1{P(A)}$ bit; Entropie $H(\mathbf{p})=\sum_kp_k\log_2\frac1{p_k}$, die kleinste mittlere Länge eines Präfixcodes; binäre Entropie höchstens $1$ bit, bei $\theta=\frac12$.

</li>

<li>

Kreuzentropie $H(\mathbf{p},\mathbf{q})=\sum p_k\log_2\frac1{q_k}$, KL-Divergenz $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=H(\mathbf{p},\mathbf{q})-H(\mathbf{p})\ge0$ (Gibbs, aus $\ln x\le x-1$), null nur bei $\mathbf{p}=\mathbf{q}$; nicht symmetrisch, keine Dreiecksungleichung.

</li>

<li>

Größte Entropie: $\log_2K$ bei der Gleichverteilung; bei fester Varianz $\frac12\ln(2\pi\mathrm{e}\sigma^2)$ bei der Normalverteilung; differentielle Entropie kann negativ sein und hängt von der Einheit ab, die KL-Divergenz nicht.

</li>

<li>

$-\frac1N\ell(\boldsymbol{\theta})=H(\hat{\mathbf{p}},\mathbf{q}(\boldsymbol{\theta}))=H(\hat{\mathbf{p}})+D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{q}(\boldsymbol{\theta}))$: Maximum Likelihood minimiert die KL-Divergenz von der empirischen Verteilung; kategorisch daher $N_k/N$; bei normalverteilten Daten mit fester Varianz ist es die kleinste mittlere quadratische Abweichung.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Schätzer ist eine Zufallsvariable, weil er von zufälligen Daten abhängt; sein mittlerer quadratischer Fehler zerfällt in quadrierte Verzerrung und Varianz, und weil der eigene Mittelwert näher an den Daten liegt als der wahre, unterschätzt die Varianz mit dem Nenner $N$ die wahre im Mittel um den Faktor $(N-1)/N$.

</li>

<li>

Die Likelihood bewertet Parameterwerte danach, wie wahrscheinlich sie die beobachteten Daten machen; ihr Maximum ist der Maximum-Likelihood-Schätzer, und mit einem Prior liefert der Satz von Bayes den Posterior, dessen Gipfel der MAP-Schätzer ist, das Maximum von Log-Likelihood plus Strafterm des Priors.

</li>

<li>

Der Informationsgehalt $\log_2(1/p)$ misst Überraschung, die Entropie ihren Mittelwert und zugleich die kürzeste mittlere Codelänge, die KL-Divergenz den nie negativen Mehraufwand durch eine falsche Verteilung, und Maximum Likelihood heißt genau, die Modellverteilung mit der kleinsten KL-Divergenz von der empirischen Verteilung der Daten zu wählen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Werkzeugen: dem Erwartungswert über gedachte Wiederholungen der Daten und dem Logarithmus einer Wahrscheinlichkeit. Der erste bewertet Schätzer, der zweite macht aus multiplizierten Wahrscheinlichkeiten addierbare Überraschungen.

| Ergebnis | Woher es kommt |
|---|---|
| Schätzer sind zufällig | sie hängen von zufälligen Daten ab; ihre Güte ist ein Erwartungswert über gedachte Datensätze (Abschnitt [1](schatzen-aus-einer-stichprobe.html#stufe-1)) |
| $\operatorname{MSE}=\operatorname{Bias}^2+\operatorname{Var}$ | Verschiebungsformel; die Schwankung um den eigenen Erwartungswert mittelt sich weg (Abschnitt [2](wie-gut-ist-ein-schatzer.html#stufe-2)) |
| Nenner $N-1$ | $\bar x$ ist an die eigenen Daten angepasst; der Fehlbetrag $N(\bar x-\mu)^2$ hat den Erwartungswert $\sigma^2$ (Abschnitt [3](die-varianz-schatzen.html#stufe-3)) |
| Log-Likelihood | der Logarithmus macht das Produkt unabhängiger Wahrscheinlichkeiten zur Summe und wächst streng monoton (Abschnitt [4](die-likelihood.html#stufe-4)) |
| $N_1/N$, $\bar x$, $\hat\sigma^2_N$ | Ableitung der Log-Likelihood null und Vorzeichenwechsel; bei der Normalverteilung die Quadratsumme im Exponenten (Abschnitt [5](die-maximum-likelihood-schatzung.html#stufe-5)) |
| Posterior, Beta-Bernoulli | Satz von Bayes mit Integral; beim Multiplizieren addieren sich die Hochzahlen (Abschnitt [6](prior-und-posterior.html#stufe-6)) |
| MAP $=$ Log-Likelihood $+$ Strafterm | Logarithmus von Likelihood mal Prior; der Prior wächst nicht mit $N$ (Abschnitt [7](die-maximum-a-posteriori-schatzung.html#stufe-7)) |
| Informationsgehalt $\log_2(1/p)$ | unabhängige Überraschungen addieren sich, Wahrscheinlichkeiten multiplizieren sich (Abschnitt [8](informationsgehalt-und-entropie.html#stufe-8)) |
| $D_{\mathrm{KL}}\ge0$, Codelänge $\ge H$ | $\ln x\le x-1$, mit den Wahrscheinlichkeiten gemittelt (Abschnitt [9](kreuzentropie-und-kl-divergenz.html#stufe-9)) |
| Gleichverteilung und Normalverteilung maximal | Gibbs-Ungleichung zur Gleichverteilung beziehungsweise zur Normalverteilung, deren Logarithmus quadratisch ist (Abschnitt [10](die-grote-entropie.html#stufe-10)) |
| Maximum Likelihood $=$ kleinste KL-Divergenz | $-\ell/N$ ist die Kreuzentropie zur empirischen Verteilung, deren Entropie nicht vom Parameter abhängt (Abschnitt [11](maximum-likelihood-und-kl-divergenz.html#stufe-11)) |
