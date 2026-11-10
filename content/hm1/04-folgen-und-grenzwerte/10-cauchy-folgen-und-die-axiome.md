---
title: Stufe 8: Cauchy-Folgen und die Axiome
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1241000
summary: Die Pendelfolge ist nicht monoton, das Monotonie-Lemma greift nicht.
tags: Cauchy-Folge, Intervallschachtelung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die Pendelfolge ist nicht monoton, das Monotonie-Lemma greift nicht. Diese Stufe gibt einen Test für beliebige Folgen, der ohne den Grenzwert auskommt, und fasst zusammen, was die Axiome von $\mathbb{R}$ für Folgen leisten.
:::

**Die Idee.** Der Abstand zum Ziel lässt sich nicht messen, wenn das Ziel unbekannt ist. Messen lässt sich der Abstand der Glieder untereinander. Rücken die Glieder ab einem Index alle eng zusammen, sollte dort ein Ziel sein. Um das zu zeigen, faltet man eine beliebige Folge in zwei monotone: ihre obere und ihre untere Hülle (Abb. [9](#abb-9)).

:::satz Satz 8.1 (Abgeleitete Sup- und Inf-Folgen)
<span class="anker" id="satz-8-1"></span>

Sei $\{a_n\}$ eine beschränkte Folge. Setze

<span class="anker" id="gl-8-1"></span>
$$b_n:=\sup\{a_m:\ m\ge n\},\qquad c_n:=\inf\{a_m:\ m\ge n\}. \tag{8.1}$$

Dann gilt: (i) $c_n\le a_n\le b_n$, (ii) $b_n\ge b_{n+1}$, (iii) $c_n\le c_{n+1}$, (iv) $\lim a_n=a\iff\lim b_n=\lim c_n=a$.
:::

⁠**So liest man das:** $b_n$ ist die tiefste Decke über allen Gliedern ab Platz $n$, $c_n$ der höchste Boden darunter. Rückt $n$ weiter, fallen Glieder weg, die Decke kann nur sinken und der Boden nur steigen. Nach dem Monotonie-Lemma konvergieren beide Folgen immer, jede mit Grenzwert in $\mathbb{R}$. Haben sie denselben Grenzwert, ist das nach (iv) der Grenzwert von $a_n$, und die Bedingung $a\in\mathbb{R}$ ist von selbst erfüllt. Für unbeschränkte Folgen setzt man $\sup M:=+\infty$ beziehungsweise $\inf M:=-\infty$. Für $a_n=n$ ist dann $b_n=+\infty$, $c_n=n$, und (iv) hilft nicht. **Grenzfall:** Für eine konstante Folge ist $b_n=c_n$.

:::beweis Hüllen
Mit $M_n:=\{a_m:m\ge n\}$ ist $b_n=\sup M_n$, $c_n=\inf M_n$.

(i) $a_n\in M_n$. (ii), (iii) $M_{n+1}\subset M_n$: Jede obere Schranke von $M_n$ ist auch eine von $M_{n+1}$, also $\sup M_{n+1}\le\sup M_n$. Für das Infimum geht es entsprechend.

(iv) „$\Leftarrow$“ ist das Sandwich-Lemma mit (i). „$\Rightarrow$“: Liegen alle $a_m$ mit $m>N_0$ im Schlauch um $a$, gilt für $n>N_0$ auch $a-\varepsilon\le c_n\le b_n\le a+\varepsilon$.
:::

::::beispiel
Für die Pendelfolge sind die Hüllen $b_n=2+3/m$ mit der kleinsten geraden Zahl $m\ge n$ und $c_n=2-3/m$ mit der kleinsten ungeraden Zahl $m\ge n$. Das ergibt $b_1,\dots,b_6=3{,}5;\ 3{,}5;\ 2{,}75;\ 2{,}75;\ 2{,}5;\ 2{,}5$ und $c_1,\dots,c_6=-1;\ 1;\ 1;\ 1{,}4;\ 1{,}4;\ 1{,}571$. Beide streben gegen 2.
::::

:::abbildung hm1/k4trichter 9
Die Pendelfolge mit ihren Hüllen: Die obere Hülle $b_n$ fällt, die untere Hülle $c_n$ steigt. Die Glieder wechseln zwischen beiden. Der Abstand $b_n-c_n$ schließt sich wie ein Trichter um den Wert 2.
:::

:::definition Definition 8.2 (Cauchy-Folge)
<span class="anker" id="satz-8-2"></span>

Eine Folge $\{a_n\}$ heißt __Cauchy-Folge__, wenn gilt:

<span class="anker" id="gl-8-2"></span>
$$\forall\,\varepsilon>0\quad\exists\,N_0\in\mathbb{N},\quad\text{so dass}\quad|a_n-a_m|<\varepsilon\quad\forall\,n>N_0,\ \forall\,m>N_0. \tag{8.2}$$
:::

⁠**So liest man das:** Es ist das Spiel aus Stufe [2](das-epsilon-spiel.html#stufe-2), aber kein Grenzwert kommt vor. Hinter $N_0$ liegen je *zwei* beliebige Glieder näher als $\varepsilon$ beieinander, nicht nur Nachbarn. Beispiel: Für $a_n=3/n$ und $m\ge n$ ist $|a_n-a_m|=3\,\frac{m-n}{nm}\le\frac3n$, also gewinnt $N_0=\lfloor3/\varepsilon\rfloor+1$.

:::satz Satz 8.3 (Konvergent und Cauchy)
<span class="anker" id="satz-8-3"></span>

<ol class="rm">

<li>

Jede konvergente reelle Folge ist eine Cauchy-Folge.

</li>

<li>

Jede Cauchy-Folge $\{a_n\}\subset\mathbb{R}$ ist konvergent, mit Grenzwert in $\mathbb{R}$.

</li>

</ol>
:::

⁠**So liest man das:** (i) gilt in jedem Zahlbereich, (ii) braucht die Vollständigkeit. In $\mathbb{R}$ sind „Cauchy-Folge“ und „konvergent“ dasselbe. **Voraussetzung nötig:** In $\mathbb{Q}$ ist die Wurzelfolge eine Cauchy-Folge, denn sie konvergiert in $\mathbb{R}$ und alle Glieder sind Brüche, aber sie hat dort keinen Grenzwert.

:::beweis (i) vollständig, (ii) Idee
(i) Sei $\varepsilon>0$ und $a_n\to a$. Zu $\varepsilon/2$ gibt es $N_0$ mit $|a_n-a|<\varepsilon/2$ für $n>N_0$. Der Umweg über $a$ gibt für $n,m>N_0$

$$|a_n-a_m|\le|a_n-a|+|a-a_m|<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.$$

(ii) Eine Cauchy-Folge ist beschränkt: Zu $\varepsilon=1$ liegen alle Glieder hinter $N_0$ näher als 1 bei $a_{N_0+1}$, davor stehen endlich viele. Also existieren $b_n$ und $c_n$ aus [(8.1)](#gl-8-1). Sei $\varepsilon>0$ und $N_0$ wie in [(8.2)](#gl-8-2). Für $k,\ell>N_0$ ist $a_k<a_\ell+\varepsilon$. Für festes $\ell$ ist $a_\ell+\varepsilon$ also eine obere Schranke der $a_k$, somit $b_n\le a_\ell+\varepsilon$ für $n>N_0$. Damit ist $b_n-\varepsilon$ eine untere Schranke der $a_\ell$, also $b_n-\varepsilon\le c_n$. Es folgt

$$0\le b_n-c_n\le\varepsilon\qquad\forall\,n>N_0.$$

Die Intervalle $[c_n,b_n]$ sind ineinander geschachtelt und werden beliebig kurz. Das ist eine __Intervallschachtelung__, nach [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) enthalten sie genau eine Zahl $x\in\mathbb{R}$. An dieser Stelle wirkt die Vollständigkeit. Dann ist $\lim c_n=x=\lim b_n$, und Satz [8.1](#satz-8-1) (iv) gibt $a_n\to x$.
:::

**Was die Axiome für Folgen leisten.** Das Vollständigkeitsaxiom (V) aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) lässt sich durch eine Forderung über Folgen ersetzen:

| Axiome | Inhalt | Wirkung auf Folgen |
|---|---|---|
| Körperaxiome | Addition und Multiplikation mit Assoziativ-, Kommutativ- und Distributivgesetz, Null, Eins, Negatives, Inverses (zu Elementen $\ne0$), $0\ne1$ | Mit Gliedern rechnen, Rechenregeln (Stufe [5](rechenregeln.html#stufe-5)) |
| Anordnungsaxiome | Genau eines von $x>0$, $x=0$, $-x>0$; Summe und Produkt positiver Zahlen sind positiv | Betrag, Schlauch, Monotonie, Einklemmen (Stufe [2](das-epsilon-spiel.html#stufe-2) bis [6](einklemmen-und-divergenz.html#stufe-6)) |
| Vollständigkeit, Infimumsversion (V) | Jede nach unten beschränkte, nicht leere Menge besitzt ein Infimum aus dem Körper | Existenz des Grenzwerts monotoner beschränkter Folgen (Stufe [7](monotone-folgen-und-die-vollstandigkeit.html#stufe-7)) |
| Vollständigkeit, Cauchy-Version ($\widetilde{\mathrm V}$) | Jede Cauchy-Folge konvergiert mit Grenzwert im Körper | Existenz des Grenzwerts ohne Monotonie (diese Stufe) |

$\mathbb{Q}$ erfüllt die ersten beiden Zeilen, $\mathbb{R}$ alle. Körperaxiome, Anordnung und (V) beschreiben $\mathbb{R}$ eindeutig ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Dasselbe leistet ($\widetilde{\mathrm V}$) anstelle von (V), wenn zusätzlich der Satz von Archimedes gilt (zu jeder Zahl gibt es eine größere natürliche Zahl). Aus (V) folgt er von selbst, neben ($\widetilde{\mathrm V}$) muss man ihn fordern. Die Cauchy-Version braucht nur einen Abstand, keine Ordnung. Deshalb überträgt sie sich auf $\mathbb{C}$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)), wo es keine Anordnung gibt.

:::frage Wenn benachbarte Glieder sich immer näher kommen, ist die Folge dann Cauchy?
Nein. Für $\sqrt n$ geht der Nachbarabstand $\sqrt{n+1}-\sqrt n$ gegen 0 (Stufe [3](nullfolgen-vergleichen.html#stufe-3)), und doch wächst die Folge ohne Grenze. In [(8.2)](#gl-8-2) müssen alle Paare hinter $N_0$ nah sein, auch weit entfernte. Viele kleine Schritte können zusammen beliebig weit führen.
:::

:::aufgabe Aufgabe 11 ★★ Hüllen ausrechnen
<span class="anker" id="aufg-11"></span>

Für $u_n=1+(-1)^n\,\frac2n$: Bestimme $b_1,\dots,b_4$ und $c_1,\dots,c_4$ aus [(8.1)](#gl-8-1). Gib allgemeine Formeln an und lies daraus den Grenzwert ab. Zeige $0\le b_n-c_n\le\frac4n$.

:::loesung
Die Glieder sind $u_1,\dots,u_6=-1;\ 2;\ \frac13;\ \frac32;\ \frac35;\ \frac43$. Also $b_1,\dots,b_4=2;\ 2;\ \frac32;\ \frac32$ und $c_1,\dots,c_4=-1;\ \frac13;\ \frac13;\ \frac35$. Die geraden Glieder fallen auf 1 zu, die ungeraden steigen. Allgemein ist $b_n=1+2/m$ mit der kleinsten geraden Zahl $m\ge n$ und $c_n=1-2/m'$ mit der kleinsten ungeraden Zahl $m'\ge n$. Beide streben gegen 1, also ist $\lim u_n=1$. Wegen $m,m'\ge n$ ist $0\le b_n-c_n=2/m+2/m'\le4/n$.
:::
:::

:::aufgabe Aufgabe 12 ★★★ Kein Cauchy
<span class="anker" id="aufg-12"></span>

Zeige, dass $\sqrt n$ keine Cauchy-Folge ist. Verneine dazu [(8.2)](#gl-8-2) und wähle $\varepsilon_0=1$ und $m=4n$. Wie groß ist der Nachbarabstand bei $n=100$? Warum widerspricht das nicht Satz [8.3](#satz-8-3)?

:::loesung
Keine Cauchy-Folge heißt: $\exists\,\varepsilon_0>0\ \forall\,N\in\mathbb{N}\ \exists\,n,m>N:\ |a_n-a_m|\ge\varepsilon_0$. Zu $\varepsilon_0=1$ und beliebigem $N$ wähle $n=N+1$ und $m=4n$. Dann ist $|\sqrt{4n}-\sqrt n|=\sqrt n\ge1$. Der Nachbarabstand bei $n=100$ ist $\sqrt{101}-10=0{,}0499$. Kein Widerspruch: Satz [8.3](#satz-8-3) sagt, dass eine konvergente Folge Cauchy ist. Die Folge $\sqrt n$ konvergiert nicht und ist auch nicht Cauchy, kleine Nachbarabstände allein reichen nicht.
:::
:::
