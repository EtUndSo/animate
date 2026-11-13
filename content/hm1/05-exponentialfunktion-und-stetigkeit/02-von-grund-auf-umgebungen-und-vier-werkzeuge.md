---
title: Von Grund auf: Umgebungen und vier Werkzeuge
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250200
summary: Was alles daraus folgt, dass kleine Änderungen am Eingang kleine Änderungen am Ausgang machen
tags: Umgebung, punktierte Umgebung
lang: de
---

⁠**Umgebung.** Für $\eta>0$ (griechisch eta) heißt $U_\eta(x_0):=(x_0-\eta,x_0+\eta)$ __Umgebung__ von $x_0$ und $\dot U_\eta(x_0):=U_\eta(x_0)\setminus\{x_0\}$ __punktierte Umgebung__: Sie lässt die Stelle selbst aus. $x\in U_\eta(x_0)$ bedeutet $|x-x_0|<\eta$.

⁠**Werkzeuge.** *Monotonie-Lemma* ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)): Monotone beschränkte Folgen konvergieren. *Sandwich-Lemma* ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)): Aus $c_n\le a_n\le b_n$ und $\lim c_n=\lim b_n=a$ folgt $\lim a_n=a$. *Bernoulli* ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): $(1+h)^m>1+mh$ für $h>-1$, $h\ne0$, $m\ge2$. *Intervallschachtelung* ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): Geschachtelte Intervalle $[a_n,b_n]$ mit $b_n-a_n\to0$ enthalten genau eine gemeinsame Zahl.

Aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) stammen $\mathcal W(f)$ (Wertebereich) und die Aussage: Streng monotone $f$ sind auf $\mathcal W(f)$ bijektiv, $f^{-1}$ ist monoton in dieselbe Richtung. Außerdem ist $\mathbb{R}^+:=(0,\infty)$.

::::formelsammlung
**Umgebung**

$$U_\eta(x_0):=(x_0-\eta,x_0+\eta)$$

Für $\eta>0$; $x\in U_\eta(x_0)$ bedeutet $|x-x_0|<\eta$.

**Punktierte Umgebung**

$$\dot U_\eta(x_0):=U_\eta(x_0)\setminus\{x_0\}$$

Die Umgebung ohne die Stelle $x_0$ selbst.

**Sandwich-Lemma**

$$c_n\le a_n\le b_n,\quad\lim c_n=\lim b_n=a\quad\Longrightarrow\quad\lim a_n=a$$

Dazu das Monotonie-Lemma: Monotone beschränkte Folgen konvergieren.

**Bernoulli-Ungleichung**

$$(1+h)^m>1+mh$$

Für $h>-1$, $h\ne0$, $m\ge2$.

**Intervallschachtelung**

$$[a_n,b_n]\ \text{geschachtelt},\qquad b_n-a_n\to0$$

Dann enthalten die Intervalle genau eine gemeinsame Zahl.

**Positive reelle Zahlen**

$$\mathbb{R}^+:=(0,\infty)$$

$\mathcal W(f)$ ist der Wertebereich. Streng monotone $f$ sind auf $\mathcal W(f)$ bijektiv, $f^{-1}$ ist monoton in dieselbe Richtung.
::::

::::lernkarten
:::karte begriff Umgebung
Was ist die Umgebung $U_\eta(x_0)$ einer Stelle $x_0$, und was bedeutet $x\in U_\eta(x_0)$ als Ungleichung?
---
Für $\eta>0$ das offene Intervall $U_\eta(x_0):=(x_0-\eta,x_0+\eta)$ um $x_0$. $x\in U_\eta(x_0)$ bedeutet $|x-x_0|<\eta$: $x$ liegt näher als $\eta$ an $x_0$.
--- falsch
Für $\eta>0$ das abgeschlossene Intervall $[x_0-\eta,x_0+\eta]$ um $x_0$. $x\in U_\eta(x_0)$ bedeutet $|x-x_0|\le\eta$: $x$ liegt höchstens $\eta$ von $x_0$ entfernt.
--- falsch
Für $\eta>0$ das Intervall $(x_0,x_0+\eta)$ rechts von $x_0$. $x\in U_\eta(x_0)$ bedeutet $0<x-x_0<\eta$: $x$ liegt etwas rechts von $x_0$, aber nie auf $x_0$.
--- falsch
Für $\eta\ge0$ das offene Intervall $(x_0-\eta,x_0+\eta)$ um $x_0$. $x\in U_\eta(x_0)$ bedeutet $|x-x_0|<\eta$; für $\eta=0$ besteht die Umgebung nur aus $x_0$ selbst.
:::
:::karte begriff punktierte Umgebung
Was ist die punktierte Umgebung $\dot U_\eta(x_0)$, und worin unterscheidet sie sich von der Umgebung $U_\eta(x_0)$?
---
Die Umgebung ohne die Stelle selbst: $\dot U_\eta(x_0):=U_\eta(x_0)\setminus\{x_0\}$. Sie enthält alle $x$ mit $|x-x_0|<\eta$ außer $x_0$.
--- falsch
Die Umgebung ohne ihre beiden Randpunkte: $\dot U_\eta(x_0):=U_\eta(x_0)\setminus\{x_0-\eta,x_0+\eta\}$. Sie enthält alle $x$ mit $|x-x_0|<\eta$.
--- falsch
Die Umgebung samt Randpunkten: $\dot U_\eta(x_0):=[x_0-\eta,x_0+\eta]$. Sie enthält alle $x$ mit $|x-x_0|\le\eta$, auch $x_0$ selbst.
--- falsch
Nur die Stelle selbst: $\dot U_\eta(x_0):=\{x_0\}$, ein einzelner Punkt. Der Index $\eta$ gibt dabei an, wie fein man die Stelle markiert.
:::
:::karte formel Monotonie-Lemma
Was sagt das Monotonie-Lemma über eine Folge, und welche beiden Eigenschaften muss sie dafür haben?
---
Monotone beschränkte Folgen konvergieren: Ist eine Folge monoton und zugleich beschränkt, so besitzt sie einen Grenzwert.
--- falsch
Monotone Folgen konvergieren immer: Ist eine Folge monoton wachsend oder fallend, so besitzt sie einen Grenzwert; eine Schranke ist dafür nicht nötig.
--- falsch
Beschränkte Folgen konvergieren: Liegt eine Folge in einem festen Streifen, so besitzt sie einen Grenzwert, ob sie monoton ist oder nicht.
--- falsch
Konvergente Folgen sind monoton: Besitzt eine Folge einen Grenzwert, so ist sie ab einem Index monoton wachsend oder monoton fallend.
:::
:::karte formel Sandwich-Lemma
Was folgt nach dem Sandwich-Lemma aus $c_n\le a_n\le b_n$, und welche Bedingung brauchen die beiden äußeren Folgen?
---
Gilt $\lim c_n=\lim b_n=a$, dann folgt $\lim a_n=a$: Die eingeklemmte Folge übernimmt den gemeinsamen Grenzwert der beiden äußeren.
--- falsch
Konvergieren $c_n$ und $b_n$ überhaupt, dann konvergiert auch $a_n$, und zwar gegen den Mittelwert $\frac12(\lim c_n+\lim b_n)$ der beiden Grenzwerte.
--- falsch
Gilt $\lim c_n=\lim b_n=a$, dann ist $a_n$ beschränkt, muss aber nicht konvergieren, weil sie zwischen den Schranken weiter pendeln darf.
--- falsch
Gilt $\lim c_n=a$, dann folgt schon $\lim a_n=a$, denn die untere Folge zieht $a_n$ mit; auf die obere Folge $b_n$ kommt es nicht an.
:::
:::karte formel Bernoulli-Ungleichung
In welcher Form wird die Bernoulli-Ungleichung als Werkzeug gebraucht, und unter welchen Voraussetzungen gilt sie dann?
---
$(1+h)^m>1+mh$ für $h>-1$, $h\ne0$ und $m\ge2$. Das echte Größerzeichen verlangt diese Ausschlüsse, denn für $h=0$ oder $m=1$ gilt Gleichheit.
--- falsch
$(1+h)^m>1+mh$ für alle $h\in\mathbb{R}$ und $m\ge2$. Auch Werte $h<-1$ sind erlaubt, weil die Potenz die Klammer stets positiv macht.
--- falsch
$(1+h)^m<1+mh$ für $h>-1$, $h\ne0$ und $m\ge2$. Die Potenz bleibt unter der Geraden, weil kleine Zuwächse sich beim Potenzieren nicht aufschaukeln.
--- falsch
$(1+h)^m>1+h^m$ für $h>-1$, $h\ne0$ und $m\ge2$. Ausmultiplizieren liefert die Summanden 1 und $h^m$ und dazu nur positive gemischte Glieder.
:::
:::karte formel Intervallschachtelung
Was liefert eine Intervallschachtelung, und welche Bedingung an die Intervalllängen braucht man dafür?
---
Geschachtelte Intervalle $[a_n,b_n]$, jedes im vorigen enthalten, mit $b_n-a_n\to0$ enthalten genau eine gemeinsame Zahl.
--- falsch
Geschachtelte Intervalle $[a_n,b_n]$ mit $b_n-a_n\to0$ enthalten keine gemeinsame Zahl, denn ihre Längen schrumpfen auf null.
--- falsch
Geschachtelte Intervalle $[a_n,b_n]$, jedes im vorigen enthalten, enthalten genau eine gemeinsame Zahl, auch ohne Längenbedingung.
--- falsch
Geschachtelte Intervalle $[a_n,b_n]$ mit $b_n-a_n\to0$ enthalten genau eine gemeinsame Zahl, aber nur bei rationalen Rändern.
:::
:::karte zusammenhang Wertebereich
Was gilt nach [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) für eine streng monotone Funktion $f$ als Abbildung auf ihren Wertebereich $\mathcal W(f)$, und wie verhält sich ihre Umkehrung?
---
Sie ist auf $\mathcal W(f)$ bijektiv, weil verschiedene Stellen verschiedene Werte haben und jeder Wert in $\mathcal W(f)$ getroffen wird. Die Umkehrfunktion $f^{-1}$ ist monoton in dieselbe Richtung.
--- falsch
Sie ist auf $\mathcal W(f)$ nur injektiv; die Surjektivität muss man zusätzlich fordern, weil nicht jeder Wert in $\mathcal W(f)$ getroffen werden muss. $f^{-1}$ ist monoton in dieselbe Richtung.
--- falsch
Sie ist auf $\mathcal W(f)$ bijektiv, weil verschiedene Stellen verschiedene Werte haben. Die Umkehrfunktion $f^{-1}$ ist aber monoton in die Gegenrichtung, weil sie den Graphen spiegelt.
--- falsch
Sie ist auf ganz $\mathbb{R}$ bijektiv, weil eine streng monotone Funktion jeden reellen Wert genau einmal annimmt. Die Umkehrfunktion $f^{-1}$ ist monoton in dieselbe Richtung.
:::
::::
