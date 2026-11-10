---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1251100
summary: Was alles daraus folgt, dass kleine Änderungen am Eingang kleine Änderungen am Ausgang machen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

$\mathrm{e}^x:=\lim_{n\to\infty}(1+\frac xn)^n$ erfüllt $\mathrm{e}^{x+y}=\mathrm{e}^x\mathrm{e}^y$ und ist eine streng wachsende Bijektion von $\mathbb{R}$ auf $(0,\infty)$. Ihre Umkehrung ist $\log$, und $a^x:=\mathrm{e}^{x\log a}$ erklärt jede Potenz mit $a>0$.

</li>

<li>

$f$ ist in $x_0$ stetig, wenn zu jeder Ausgangstoleranz $\varepsilon>0$ eine Eingangstoleranz $\delta>0$ existiert mit $|f(x)-f(x_0)|<\varepsilon$ für alle $x$ mit $|x-x_0|<\delta$.

</li>

<li>

Stetige Funktionen auf einem abgeschlossenen, beschränkten Intervall sind beschränkt, nehmen Maximum und Minimum an, lassen keinen Zwischenwert aus und sind gleichmäßig stetig. Fehlt eine Voraussetzung, kann jede dieser Aussagen falsch werden.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

$\mathrm{e}^x=\lim(1+\frac xn)^n$; $\mathrm{e}^{x+y}=\mathrm{e}^x\mathrm{e}^y$, $\mathrm{e}^x\ge1+x$, $\mathrm{e}^x>x^n$ für $x>4n^2$. $\log$ ist die Umkehrung: $\log(xy)=\log x+\log y$, $\log t\le t-1$. $a^x=\mathrm{e}^{x\log a}$ für $a>0$.

</li>

<li>

$\lim_{x\to x_0}f(x)=y_0$: Für jede Folge $x_n\to x_0$, $x_n\ne x_0$ gilt $f(x_n)\to y_0$. Polynome: einsetzen, Lücken: kürzen, $\lim_{x\to0}\frac{\mathrm{e}^x-1}x=1$.

</li>

<li>

Stetig in $x_0$: $\lim_{x\to x_0}f(x)=f(x_0)$, gleichwertig $\varepsilon$-$\delta$, gleichwertig $\lim f(x_n)=f(\lim x_n)$. Summe, Produkt, Quotient und Verkettung bleiben stetig.

</li>

<li>

Bolzano-Weierstraß: Beschränkte Folgen haben eine konvergente Teilfolge. Daraus folgt für $f:[a,b]\to\mathbb{R}$ stetig: beschränkt, Maximum und Minimum werden angenommen, $\mathcal W(f)=[m,M]$, gleichmäßig stetig. Streng monoton: Die Umkehrfunktion ist stetig.

</li>

<li>

Nullstellen: Halbieren oder Sekante $\alpha=a-\frac{b-a}{f(b)-f(a)}f(a)$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Stetigkeit transportiert Grenzwerte: Läuft der Eingang gegen $x_0$, läuft der Ausgang gegen $f(x_0)$. Auf $[a,b]$ besitzt jede Folge eine Teilfolge, die gegen eine Stelle im Intervall läuft. Diese zwei Schritte tragen die Ergebnisse. Fehlt eine Voraussetzung, bricht einer von ihnen.

| Ergebnis | Woher es kommt |
|---|---|
| $\mathrm{e}^x$ ist überall stetig | Die Funktionalgleichung trägt die Stetigkeit von 0 zu jeder Stelle (Stufe [5](stetigkeit-vererben.html#stufe-5)) |
| Maximum und Minimum | Eine Teilfolge läuft gegen $x_1\in[a,b]$, ihre Bilder laufen gegen $f(x_1)$ (Stufe [7](maximum-minimum-gleichmaige-stetigkeit.html#stufe-7)) |
| Zwischenwerte | Halbieren liefert $x_0$ mit Werten beider Vorzeichen daneben, also $f(x_0)=0$ (Stufe [8](zwischenwerte-nullstellen-umkehrfunktion.html#stufe-8)) |
| Umkehrfunktion | Zwischenwerte ergeben die Surjektivität und die Stetigkeit der Umkehrung (Stufe [8](zwischenwerte-nullstellen-umkehrfunktion.html#stufe-8)) |
| Gleichmäßige Stetigkeit | Dieselben zwei Schritte, angewandt auf zwei Folgen zugleich (Stufe [7](maximum-minimum-gleichmaige-stetigkeit.html#stufe-7)) |
