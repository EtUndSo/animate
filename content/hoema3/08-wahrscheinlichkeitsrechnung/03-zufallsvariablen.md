---
title: Zufallsvariablen und Verteilungen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080300
summary: Von Grund auf – eine Zufallsvariable $X:\Omega\to\mathbb R$ ordnet jedem Ausgang eine Zahl zu und macht Zufall messbar. Ihre Verteilungsfunktion $F_X(x)=P(X\le x)$ ist monoton, rechtsstetig und läuft von 0 nach 1. Diskrete Variablen beschreibt die Wahrscheinlichkeitsfunktion (Binomial, Poisson, hypergeometrisch), absolut-stetige eine Dichte $f_X$ mit $F_X=\int_{-\infty}^x f_X$ (Gleich-, Normalverteilung). Die Verteilung $P_X$ löst $X$ ganz vom Grundraum.
tags: Zufallsvariable, Verteilungsfunktion, Wahrscheinlichkeitsfunktion, Dichte, Binomialverteilung, Poisson-Verteilung, Normalverteilung, absolut-stetig
---

:::grafik
Einstiegs-Animation: Eine __Zufallsvariable__ $X$ als Pfeil, der jeden Ausgang $\omega\in\Omega$ auf eine reelle Zahl
abbildet (z. B. Tippergebnis → Gewinnsumme). Darunter die __Verteilungsfunktion__ $F_X(x)=P(X\le x)$: eine von $0$
nach $1$ steigende Kurve — bei diskreten $X$ eine **rechtsstetige Treppe** mit Sprüngen an den möglichen Werten, bei
absolut-stetigen $X$ eine glatte Kurve, deren Steigung die __Dichte__ $f_X$ ist. Rechts zwei Beschreibungsweisen:
diskret die Stäbe der __Wahrscheinlichkeitsfunktion__ $p_X(x_k)=P(X=x_k)$, stetig die Fläche unter $f_X$. Kernbotschaft:
Eine Zufallsvariable übersetzt Zufall in Zahlen, und ihre Verteilung beschreibt sie vollständig — losgelöst vom
Grundraum.
:::

:::konzept
Bisher war Zufall qualitativ: Ereignisse traten ein oder nicht. Eine __Zufallsvariable__ macht ihn **quantitativ** —
sie misst eine Zahl am Ausgang eines Experiments (Augensumme, Messrauschen, Gewinn). Technisch ist das eine Funktion
$X:\Omega\to\mathbb R$, die eine __Messbarkeitsbedingung__ erfüllen muss, damit „$X\le x$" überhaupt ein Ereignis ist.
Die ganze Information über $X$ steckt dann in ihrer __Verteilung__ — gegeben durch die Verteilungsfunktion $F_X$, im
diskreten Fall die Wahrscheinlichkeitsfunktion, im stetigen Fall die Dichte. Der entscheidende Perspektivwechsel: Man
vergisst den Grundraum $(\Omega,\mathcal E,P)$ und arbeitet nur noch mit der Verteilung auf $\mathbb R$ — so werden
Binomial-, Poisson- und Normalverteilung zu universellen Bausteinen.
:::

**Worum es geht:** Wir definieren die __Zufallsvariable__ und ihre __Verteilungsfunktion__ $F_X$ (Lemma 8.19),
unterscheiden __diskrete__ (Binomial, Poisson, hypergeometrisch) und __absolut-stetige__ Variablen (Dichte, Gleich-,
Normalverteilung) und führen die __Verteilung__ $P_X$ ein.

## Zufallsvariable und Verteilungsfunktion

Eine __reelle Zufallsvariable__ ist eine Zahl, die am Ausgang eines Experiments abgelesen wird — also eine Funktion
auf $\Omega$. Damit „$X$ ist höchstens $x$" ein zulässiges Ereignis ist, braucht man eine Strukturbedingung:

__Definition 8.16.__ Eine Funktion $X:\Omega\to\mathbb R$ heißt __Zufallsvariable__, wenn
$$\{\omega\in\Omega:X(\omega)\le x\}\in\mathcal E\qquad\text{für alle }x\in\mathbb R$$
(__Messbarkeit__ bezüglich $\mathcal E$). Genau dann ist die __Verteilungsfunktion__
$$F_X(x):=P(X\le x)=P(\{\omega:X(\omega)\le x\})$$
wohldefiniert. Die Messbarkeit ist also keine Schikane, sondern genau das, was gebraucht wird, damit $F_X$ Sinn
ergibt — jede interessierende Wahrscheinlichkeit „$X$ in einem Bereich" muss ein Ereignis sein.

__Bemerkung 8.17.__ Verkettet man $X$ mit einer stetigen Funktion $g:\mathbb R\to\mathbb R$, so ist $Y=g(X)$ wieder
eine Zufallsvariable — man darf also rechnen (quadrieren, skalieren, …) und bleibt im Rahmen.

__Lemma 8.19 (Eigenschaften von $F_X$).__ Jede Verteilungsfunktion ist
$$\text{monoton steigend},\quad\text{rechtsseitig stetig},\qquad \lim_{x\to-\infty}F_X(x)=0,\quad\lim_{x\to+\infty}F_X(x)=1.$$
Monotonie folgt aus der Monotonie von $P$ (größeres $x$ ⇒ größeres Ereignis $\{X\le x\}$); die Grenzwerte und die
Rechtsstetigkeit sind gerade die Stetigkeit des Maßes (Satz 8.4), angewandt auf auf- bzw. absteigende
Ereignisfolgen $\{X\le x_n\}$ mit $x_n\to\pm\infty$ bzw. $x_n\downarrow x$. Anschaulich: $F_X$ sammelt
Wahrscheinlichkeit „von links nach rechts" bis auf $1$ auf.

## Diskrete Zufallsvariablen

__Definition 8.20.__ Hat $X$ einen endlichen oder abzählbaren Wertebereich $\{x_0,x_1,\dots\}$, heißt $X$
__diskret__. Dann beschreibt man sie durch die __Wahrscheinlichkeitsfunktion__
$$p_X(x)=\begin{cases}P(X=x_k) & x=x_k,\\ 0 & \text{sonst,}\end{cases}\qquad F_X(x)=\sum_{x_k\le x}p_X(x_k).$$
Die Verteilungsfunktion entsteht also durch **Aufsummieren** der Stäbe bis zur Stelle $x$ — eine rechtsstetige Treppe
mit Sprunghöhe $p_X(x_k)$ an jedem möglichen Wert.

__Beispiel 8.21 (Binomialverteilung).__ $X$ zählt die Treffer bei $n$ unabhängigen Bernoulli-Versuchen mit
Trefferwahrscheinlichkeit $p$:
$$P(X=k)=\binom nk p^k(1-p)^{n-k}=:b_{n,p}(k),\qquad k=0,\dots,n.$$

__Beispiel 8.22 (Poisson-Verteilung).__ $X$ ist __Poisson-verteilt__ mit Parameter $\lambda>0$, wenn
$$P(X=k)=\frac{\lambda^k}{k!}\,e^{-\lambda},\qquad k\in\mathbb N_0.$$
Sie ist der __Grenzfall der Binomialverteilung__ für $n\to\infty$, $p\to0$ bei festem $np=\lambda$ („Verteilung der
seltenen Ereignisse"). Der Grenzübergang zeigt, wie sie entsteht:
$$\binom nk\Big(\frac\lambda n\Big)^k\Big(1-\frac\lambda n\Big)^{n-k}=\frac{\lambda^k}{k!}\underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\to1}\underbrace{\Big(1-\frac\lambda n\Big)^n}_{\to e^{-\lambda}}\underbrace{\Big(1-\frac\lambda n\Big)^{-k}}_{\to1}\ \xrightarrow{n\to\infty}\ \frac{\lambda^k}{k!}e^{-\lambda}.$$
Die drei markierten Faktoren streben gegen $1$, $e^{-\lambda}$ und $1$ — übrig bleibt genau die Poisson-Formel.

__Beispiel 8.23 (Hypergeometrische Verteilung).__ Eine Urne enthält $N$ Elemente, davon $M$ mit einer bestimmten
Eigenschaft; man zieht $n$ **ohne Zurücklegen**. Die Zahl $X$ der gezogenen „Eigenschafts-Elemente" ist
$$P(X=k)=\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn},\qquad k=0,\dots,n.$$
Das ist Urnenmodell (iii): abzählen, wie viele Auswahlen genau $k$ markierte enthalten. (Beim Lotto „6 aus 49" ist
$N=49$, $M=6$.)

:::grafik
Links drei diskrete Verteilungen als Stabdiagramme $P(X=k)$: Binomial $b_{n,p}$ (symmetrisch um $np$), Poisson
(rechtsschief, Grenzfall seltener Ereignisse), hypergeometrisch (Ziehen ohne Zurücklegen). Rechts die zugehörige
Treppen-Verteilungsfunktion $F_X$, die die Stäbe aufsummiert — rechtsstetig, Sprünge an den $x_k$.
:::

## Absolut-stetige Zufallsvariablen

Bei kontinuierlichem Wertebereich ist $P(X=x)$ meist $0$ und damit nutzlos — die sinnvolle Frage ist: „Mit welcher
Wahrscheinlichkeit liegt $X$ in $(a,b]$?". Die Antwort liefert $F_X$: Aus $A=\{X\le a\}\subset B=\{X\le b\}$ und
$P(B\setminus A)=P(B)-P(A)$ folgt
$$P(a<X\le b)=F_X(b)-F_X(a).$$
Das erinnert an den 2. Hauptsatz $\int_a^b f=F(b)-F(a)$ — und motiviert die Dichte.

__Definition 8.24.__ $X$ heißt __absolut-stetig__, wenn eine nichtnegative integrierbare __Dichte__ $f_X:\mathbb
R\to[0,\infty)$ existiert mit
$$F_X(x)=\int_{-\infty}^x f_X(y)\,dy\qquad\text{für alle }x.$$

__Bemerkung 8.25.__ „Absolut-stetig" bezieht sich auf $F_X$, nicht auf $X$. Für absolut-stetige $X$ ist notwendig
$P(X=x)=0$ für **jeden** Punkt (ein einzelner Wert hat keine Fläche), und an Stetigkeitsstellen von $f_X$ ist $F_X$
differenzierbar mit $F_X'(x)=f_X(x)$ — die Dichte ist also die **Ableitung** der Verteilungsfunktion. Eine konstante
Variable $X\equiv c$ ist **nicht** absolut-stetig (ihre „Dichte" wäre eine singuläre Dirac-Masse bei $c$).

__Beispiel 8.26 (Gleichverteilung).__ $X$ ist über $[a,b]$ gleichverteilt mit Dichte $f_X(x)=\frac{1}{b-a}$ für
$x\in[a,b]$, sonst $0$ — jeder Teilbereich gleicher Länge ist gleich wahrscheinlich.

__Beispiel 8.27 (Normalverteilung).__ $X\sim\mathcal N(\mu,\sigma^2)$ hat die Dichte
$$f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac12\big(\frac{x-\mu}{\sigma}\big)^2};$$
$\mu=0,\sigma=1$ ist die __Standard-Normalverteilung__. Sie ist die wichtigste stetige Verteilung überhaupt — warum,
zeigt der zentrale Grenzwertsatz.

## Der Begriff der Verteilung

Die Charakterisierung von $X$ ist oft __völlig losgelöst__ vom Grundraum $(\Omega,\mathcal E,P)$ — man gibt nur noch
$F_X$ (bzw. $f_X$ oder $p_X$) an. Formal ist die __Verteilung__ von $X$ das Wahrscheinlichkeitsmaß $P_X$ auf
$\mathbb R$:
$$P_X(A)=P(X\in A)=P(\{\omega:X(\omega)\in A\})\qquad\text{für Borelmengen }A\subset\mathbb R.$$
Für halboffene Intervalle ist $P_X((a,b])=F_X(b)-F_X(a)$; bei absolut-stetigem $X$ speziell
$P_X((a,b])=\int_a^b f_X(x)\,dx$ (dann spielt offen/abgeschlossen keine Rolle, da Punkte Wahrscheinlichkeit $0$
haben), im diskreten Fall $P_X(A)=\sum_{x_k\in A}p_X(x_k)$. $P_X$ „überträgt" also das Maß von $\Omega$ nach
$\mathbb R$ — und nur dieses übertragene Maß braucht man für alle weiteren Rechnungen.

**Stolperstein:** (1) Die __Messbarkeit__ (Def. 8.16) ist Voraussetzung, nicht Beiwerk: Ohne sie ist „$X\le x$" kein
Ereignis und $F_X$ nicht definiert. (2) $F_X$ ist __rechtsseitig__ stetig (wegen „$\le x$"); an einem Sprung gehört
der Wert zur **oberen** Stufe. (3) Eine __Dichte ist keine Wahrscheinlichkeit__ — $f_X(x)$ darf $>1$ sein; nur
$\int_a^b f_X\in[0,1]$. (4) Absolut-stetig heißt $P(X=x)=0$ überall; „Wahrscheinlichkeit $0$" ist nicht „unmöglich".
(5) Poisson ist der Grenzfall der Binomialverteilung bei $np=\lambda=\text{const}$ — nicht bei festem $p$.

:::kern
__Zufallsvariable__ (Def. 8.16): messbare $X:\Omega\to\mathbb R$, $\{X\le x\}\in\mathcal E$ ⟹
__Verteilungsfunktion__ $F_X(x)=P(X\le x)$. __Lemma 8.19__: $F_X$ monoton steigend, rechtsstetig,
$F_X(-\infty)=0$, $F_X(+\infty)=1$ (aus Satz 8.4); $g$ stetig ⟹ $g(X)$ Zufallsvariable (Bem. 8.17). __Diskret__
(Def. 8.20): $p_X(x_k)=P(X=x_k)$, $F_X(x)=\sum_{x_k\le x}p_X(x_k)$ (Treppe). Beispiele: __Binomial__ $\binom nk
p^k(1-p)^{n-k}$; __Poisson__ $\frac{\lambda^k}{k!}e^{-\lambda}$ (Grenzfall Binomial, $n\to\infty,p\to0,np=\lambda$);
__hypergeometrisch__ $\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn}$ (Ziehen ohne Zurücklegen). __Absolut-stetig__
(Def. 8.24): Dichte $f_X\ge0$ mit $F_X(x)=\int_{-\infty}^x f_X$; dann $P(X=x)=0$, $F_X'=f_X$ (Bem. 8.25);
$P(a<X\le b)=F_X(b)-F_X(a)=\int_a^b f_X$. Beispiele: __Gleichverteilung__ $\frac1{b-a}$ auf $[a,b]$,
__Normalverteilung__ $\mathcal N(\mu,\sigma^2)$ $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$. __Verteilung__
$P_X(A)=P(X\in A)$ auf $\mathbb R$ (Borel) — löst $X$ vom Grundraum.
:::

Die Verteilung beschreibt $X$ vollständig, ist aber oft zu viel Information. Als Nächstes verdichten wir sie zu zwei
Kennzahlen: dem __Erwartungswert__ (dem „Schwerpunkt") und der __Varianz__ (dem Maß für die Streuung) — das Thema des
nächsten Artikels.

:::quiz
F: Warum muss eine Zufallsvariable die Messbarkeitsbedingung $\{X\le x\}\in\mathcal E$ erfüllen?
A: Nur dann ist „$X$ ist höchstens $x$" ein zulässiges Ereignis, dem das Maß $P$ eine Wahrscheinlichkeit zuordnen kann. Ohne diese Bedingung wäre die Verteilungsfunktion $F_X(x)=P(X\le x)$ gar nicht definiert — die Messbarkeit ist genau das, was $F_X$ Sinn gibt.
F: Was beschreibt die Verteilungsfunktion $F_X$ anschaulich, und warum läuft sie von 0 nach 1?
A: $F_X(x)=P(X\le x)$ sammelt die Wahrscheinlichkeit „von links nach rechts" auf: links von allem ist noch nichts dabei ($\to0$), rechts von allem ist alles erfasst ($\to1$). Dazwischen wächst sie monoton, weil ein größeres $x$ ein größeres Ereignis einschließt.
F: Woher kommen Monotonie und Rechtsstetigkeit von $F_X$?
A: Die Monotonie folgt aus der Monotonie von $P$ ($x_1\le x_2\Rightarrow\{X\le x_1\}\subset\{X\le x_2\}$). Rechtsstetigkeit und die Grenzwerte $0$/$1$ sind die Stetigkeit des Maßes (Satz 8.4), angewandt auf absteigende bzw. auf-/absteigende Ereignisfolgen $\{X\le x_n\}$.
F: Warum ist bei diskreten Variablen $F_X$ eine rechtsstetige Treppe?
A: $F_X(x)=\sum_{x_k\le x}p_X(x_k)$ springt an jedem möglichen Wert $x_k$ um dessen Wahrscheinlichkeit $p_X(x_k)$ und bleibt dazwischen konstant. Weil die Bedingung „$\le x$" den Wert $x_k$ einschließt, gehört der Sprung zur oberen Stufe — also rechtsstetig.
F: Wie entsteht die Poisson-Verteilung als Grenzfall der Binomialverteilung?
A: Man lässt $n\to\infty$ und $p\to0$ bei festem Produkt $np=\lambda$. Im Ausdruck $\binom nk(\lambda/n)^k(1-\lambda/n)^{n-k}$ streben die kombinatorischen Faktoren gegen $1$ und $(1-\lambda/n)^n\to e^{-\lambda}$, sodass $\frac{\lambda^k}{k!}e^{-\lambda}$ übrig bleibt — die Verteilung der seltenen Ereignisse.
F: Warum ist für kontinuierliche Variablen $P(X=x)=0$ und $P(a<X\le b)=F_X(b)-F_X(a)$ die sinnvolle Größe?
A: Ein einzelner Punkt hat keine Fläche unter der Dichte, also $P(X=x)=0$ — die Frage nach einem exakten Wert ist leer. Sinnvoll ist die Wahrscheinlichkeit für ein Intervall, und die ist gerade die Differenz der Verteilungsfunktion an den Rändern (wie beim 2. Hauptsatz).
F: Was besagt die Dichte $f_X$, und in welchem Sinne ist sie die Ableitung von $F_X$?
A: $F_X(x)=\int_{-\infty}^x f_X$, also ist $f_X$ nach dem Hauptsatz an Stetigkeitsstellen die Ableitung $F_X'=f_X$. Die Dichte gibt die lokale „Wahrscheinlichkeitsrate" an: viel Dichte bedeutet steiles Ansteigen von $F_X$, also hohe Wahrscheinlichkeit in der Nähe.
F: Warum ist eine Dichte keine Wahrscheinlichkeit, und warum darf $f_X(x)>1$ sein?
A: Wahrscheinlichkeit entsteht erst durch Integration über ein Intervall ($\int_a^b f_X$). Die Dichte selbst ist eine Rate pro Längeneinheit; auf einem sehr schmalen Träger (z. B. Gleichverteilung auf $[0,\tfrac12]$ mit $f_X=2$) kann sie $>1$ sein, solange das Gesamtintegral $1$ bleibt.
F: Warum ist eine konstante Zufallsvariable $X\equiv c$ nicht absolut-stetig?
A: Ihre ganze Wahrscheinlichkeitsmasse sitzt im Punkt $c$ ($P(X=c)=1$), aber absolut-stetige Variablen haben $P(X=x)=0$ überall. Es gäbe höchstens eine singuläre Dirac-„Dichte" bei $c$, keine gewöhnliche integrierbare Funktion $f_X$.
F: Was bedeutet die Verteilung $P_X$, und warum ist sie vom Grundraum losgelöst?
A: $P_X(A)=P(X\in A)$ ist das von $X$ nach $\mathbb R$ „übertragene" Maß — es sagt, mit welcher Wahrscheinlichkeit $X$ in einem Bereich $A$ landet. Für alle weiteren Rechnungen genügt $P_X$ (bzw. $F_X$, $f_X$, $p_X$); welcher konkrete $\Omega$ dahintersteht, spielt keine Rolle mehr.
:::
