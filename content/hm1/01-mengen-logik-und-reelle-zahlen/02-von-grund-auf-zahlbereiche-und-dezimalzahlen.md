---
title: Von Grund auf: Zahlbereiche und Dezimalzahlen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210200
summary: Was man über die Zahlen voraussetzen muss und warum die Wurzel aus 2 kein Bruch ist
tags: natürlichen Zahlen, ganzen Zahlen, rationalen Zahlen, reelle Zahl, irrational
lang: de
---

Das Zeichen $:=$ heißt „wird definiert als“. Die __natürlichen Zahlen__ sind $\mathbb{N}:=\{1,2,3,\dots\}$, die __ganzen Zahlen__ $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$, die __rationalen Zahlen__ (Brüche) $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$. Der Doppelpunkt heißt „für die gilt“.

:::definition Definition 0.1 (Reelle Zahl, vorläufig)
<span class="anker" id="satz-0-1"></span>

Eine __reelle Zahl__ ist eine Zahl mit Dezimaldarstellung, das heißt mit einem Vorzeichen, einem $m\in\mathbb{N}\cup\{0\}$ und Ziffern $a_1,a_2,\ldots\in\{0,1,\dots,9\}$, endlich oder unendlich vielen:

<span class="anker" id="gl-0-1"></span>
$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr). \tag{0.1}$$

$\mathbb{R}$ ist die Menge der reellen Zahlen. Die Zahlen aus $\mathbb{R}$, die kein Bruch sind, heißen __irrational__.
:::

⁠**So liest man das:** $3/8=0{,}375$ endet, $5/11=0{,}4545\ldots$ ist periodisch, und jeder Bruch hat eine dieser beiden Formen. $\sqrt2=1{,}41421356\ldots$ wird nie periodisch. Es gilt $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. Diese Definition ist eine Übergangslösung: Sie erklärt nicht, was eine unendliche Summe ist ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)), und sie ist nicht eindeutig, $1{,}000\ldots$ und $0{,}999\ldots$ sind dieselbe Zahl. Stufe [6](das-vollstandigkeitsaxiom.html#stufe-6) ersetzt sie durch Axiome.
