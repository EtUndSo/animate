---
title: Wahrscheinlichkeitsräume
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080100
summary: Von Grund auf – das mathematische Fundament des Zufalls. Ein Wahrscheinlichkeitsraum ist ein Tripel $(\Omega,\mathcal E,P)$ aus Stichprobenraum (alle Ergebnisse), Ereignisraum (eine $\sigma$-Algebra von Teilmengen) und Wahrscheinlichkeitsmaß ($\sigma$-additiv, $P(\Omega)=1$). Im diskreten Fall summiert man Einzelwahrscheinlichkeiten; der Laplace-Raum macht Wahrscheinlichkeit zum Abzählen (Urnenmodell). Im kontinuierlichen Fall integriert man eine Dichte $\rho$ – beide Welten vereint der Integralbegriff.
tags: Wahrscheinlichkeitsraum, Stichprobenraum, Ereignis, Sigma-Algebra, Wahrscheinlichkeitsmaß, Laplace-Raum, Urnenmodell, Wahrscheinlichkeitsdichte
---

:::grafik
Einstiegs-Animation: Drei ineinandergreifende Bausteine. Zuerst der __Stichprobenraum__ $\Omega$ als Menge von
Punkten (die Elementarereignisse, z. B. die 36 Würfelpaare). Dann ein __Ereignis__ $A\subset\Omega$ als umkreiste
Teilmenge („Antwort ja auf eine Frage"), sein Komplement $A^c$ als „nein". Schließlich das __Wahrscheinlichkeitsmaß__
$P$, das jeder solchen Teilmenge eine Zahl in $[0,1]$ zuordnet, mit $P(\Omega)=1$. Rechts die zwei Welten:
**diskret** (Punktmassen $p_i$, Wahrscheinlichkeit = Summe) und **kontinuierlich** (eine Dichtekurve $\rho$,
Wahrscheinlichkeit = Fläche unter $\rho$ über $A$). Kernbotschaft: Zufall wird zu Mengenlehre plus einem Maß.
:::

:::konzept
Die ganze Wahrscheinlichkeitsrechnung ruht auf einem einzigen Begriff, den Kolmogorow 1933 präzisierte: dem
__Wahrscheinlichkeitsraum__. Er fasst drei Dinge zusammen: __was passieren kann__ (der Stichprobenraum $\Omega$),
__welche Fragen man stellen darf__ (der Ereignisraum $\mathcal E$, eine $\sigma$-Algebra) und __wie wahrscheinlich
jede Antwort ist__ (das Maß $P$). Der Clou: Ereignisse sind Teilmengen, logische Verknüpfungen (und/oder/nicht)
werden zu Mengenoperationen (Schnitt/Vereinigung/Komplement), und Wahrscheinlichkeit wird zu einem Maß — genau die
Integrationstheorie aus der Analysis. Dadurch behandelt derselbe Rahmen den Würfel (diskret) und das Rauschen eines
Messsignals (kontinuierlich).
:::

**Worum es geht:** Wir definieren __Stichprobenraum__, __Ereignis__ und die __$\sigma$-Algebra__, führen das
__Wahrscheinlichkeitsmaß__ und den __Wahrscheinlichkeitsraum__ ein, und sehen die zwei Grundtypen: __diskrete__
Räume (Laplace, Urnenmodell, Bernoulli) und __kontinuierliche__ Räume (Dichten, Normalverteilung).

## Stichprobenraum und Ereignisse

Ausgangspunkt ist der __Stichprobenraum__ $\Omega$ — die Menge aller __Elementarereignisse__ $\omega$, also aller
möglichen Ausgänge eines Zufallsexperiments. Wirft man zwei Würfel, kann $\Omega$ aus den $36$ geordneten Paaren
$(i,j)$ mit $i,j\in\{1,\dots,6\}$ bestehen. Entscheidend: $\Omega$ ist __nicht eindeutig__, sondern
**problemabhängig** — interessiert nur die Augensumme $N\in\{2,\dots,12\}$, so genügt ein $\Omega$ aus $11$
Elementen.

Ein __Ereignis__ entspricht einer Frage, die mit **ja oder nein** beantwortbar ist. „Ist die maximale Augenzahl
$\le2$?" wird zur Teilmenge $A=\{(1,1),(1,2),(2,1),(2,2)\}\subset\Omega$ (Antwort „ja"); der Antwort „nein"
entspricht das __Komplement__ $A^c=\Omega\setminus A$. Deshalb modelliert man Ereignisse als **Teilmengen**
$A\subset\Omega$. Oft sind aber nicht alle Teilmengen sinnvolle Ereignisse: Beim Dartspiel zählt nicht die exakte
Position auf $\Omega\subset\mathbb R^2$, sondern nur das getroffene Segment $A_i$. Die Menge der erlaubten
Ereignisse heißt __Ereignisraum__ $\mathcal E$ — auch er ist problemabhängig.

## Die σ-Algebra: welche Fragen erlaubt sind

Damit die Mengenoperationen (und damit die logischen Verknüpfungen von Fragen) nie aus $\mathcal E$ herausführen,
muss der Ereignisraum eine __$\sigma$-Algebra__ sein.

__Definition 8.1.__ Ein System $\mathcal E$ von Teilmengen von $\Omega$ heißt __$\sigma$-Algebra über $\Omega$__,
wenn
$$\text{(i)}\ \ \Omega\in\mathcal E, \qquad \text{(ii)}\ \ A,B\in\mathcal E\Rightarrow A\cap B\in\mathcal E, \qquad \text{(iii)}\ \ A_i\in\mathcal E\ (i\in\mathbb N)\Rightarrow \bigcup_{i\in\mathbb N}A_i\in\mathcal E.$$

Hinweis zur Notation: In manchen Darstellungen fordert (ii) die Abgeschlossenheit unter **Komplement** statt unter
Schnitt; zusammen mit (i) und (iii) sind beide Varianten äquivalent. Aus diesen Axiomen folgt sofort viel mehr: Aus
(i) und der Komplementbildung ist die __leere Menge__ $\emptyset\in\mathcal E$, aus (ii) folgt die
__Mengendifferenz__ $A\setminus B\in\mathcal E$, und mit den de-Morgan-Regeln liefert (iii) auch die Abgeschlossenheit
unter **abzählbaren Schnitten**:
$$A_i\in\mathcal E\ (i\in\mathbb N)\quad\Longrightarrow\quad \bigcap_{i\in\mathbb N}A_i\in\mathcal E.$$

Das „$\sigma$" steht gerade für die **abzählbare** (nicht nur endliche) Version von (iii) — sie ist nötig, damit man
Grenzwerte von Ereignisfolgen bilden darf. __Beispiel 8.2:__ Die __Potenzmenge__ $\mathcal P(\Omega)$ (alle
Teilmengen) ist die größtmögliche $\sigma$-Algebra über $\Omega$.

## Das Wahrscheinlichkeitsmaß

Jetzt ordnet man jedem Ereignis eine Wahrscheinlichkeit zu. Die Leitidee: $P(A)$ soll der __relativen Häufigkeit__
von $A$ in sehr vielen unabhängigen Wiederholungen entsprechen. Relative Häufigkeiten sind nichtnegativ, addieren
sich bei disjunkten Ereignissen und ergeben in der Summe über alle Ausgänge $1$ — daraus wird die Definition.

__Definition 8.3.__ Sei $\mathcal E$ eine $\sigma$-Algebra über $\Omega$. Eine __$\sigma$-additive__ Mengenfunktion
$P:\mathcal E\to[0,1]$, d. h. für **paarweise disjunkte** $A_i\in\mathcal E$ gilt
$$P\!\Big(\bigcup_{i\in\mathbb N}A_i\Big)=\sum_{i\in\mathbb N}P(A_i),$$
mit $P(\Omega)=1$, heißt __Wahrscheinlichkeitsmaß__ auf $\Omega$. Aus den Axiomen folgen unmittelbar:
$$P(A^c)=1-P(A)\quad(\text{Gegenwahrscheinlichkeit}),\qquad P(A)\le P(B)\ \text{falls}\ A\subset B\quad(\text{Monotonie}).$$

Die Gegenwahrscheinlichkeit folgt aus $\Omega=A\cup A^c$ (disjunkt) und $P(\Omega)=1$; die Monotonie aus
$B=A\cup(B\setminus A)$ (disjunkt), sodass $P(B)=P(A)+P(B\setminus A)\ge P(A)$.

Das Tripel $(\Omega,\mathcal E,P)$ heißt __Wahrscheinlichkeitsraum__.

__Satz 8.4 (Stetigkeit von $P$).__ Ist $(A_n)$ eine **aufsteigende** Ereignisfolge ($A_n\subset A_{n+1}$), so gilt
$$\lim_{n\to\infty}P(A_n)=P\!\Big(\bigcup_{k\in\mathbb N}A_k\Big);$$
für eine **absteigende** Folge entsprechend $\lim_{n\to\infty}P(A_n)=P\big(\bigcap_{k}A_k\big)$. Das ist die
„Stetigkeit des Maßes" gegenüber monotoner Konvergenz von Mengen — genau hier wird die $\sigma$-Additivität (nicht
nur endliche) gebraucht.

:::grafik
Links die $\sigma$-Algebra-Axiome als Mengenbild: $\Omega$ und $\emptyset$ enthalten, mit $A$ auch $A^c$, mit
$A_1,A_2,\dots$ auch Vereinigung und Schnitt. Rechts die $\sigma$-Additivität: disjunkte Stücke $A_1,A_2,\dots$
füllen eine Menge, ihre Wahrscheinlichkeiten addieren sich; daneben $P(A^c)=1-P(A)$ als „Rest auf $1$".
:::

## Diskrete Wahrscheinlichkeitsräume

Im einfachsten Fall ist $\Omega=\{\omega_1,\omega_2,\dots\}$ endlich oder abzählbar. Man wählt $\mathcal
E=\mathcal P(\Omega)$ und nichtnegative __Gewichte__ $p_1,p_2,\dots$ mit $\sum_i p_i=1$. Dann ist
$$P(A)=\sum_{\omega_i\in A}p_i,\qquad P(\{\omega_i\})=p_i$$
ein Wahrscheinlichkeitsmaß — die Wahrscheinlichkeit eines Ereignisses ist einfach die Summe der Gewichte seiner
Elemente.

__Der Laplace-Raum.__ Sind alle $n$ Elementarereignisse **gleich wahrscheinlich**, $p_i=1/n$, so ist
$$P(A)=\frac{|A|}{|\Omega|}=\frac{\text{Anzahl günstiger Fälle}}{\text{Anzahl möglicher Fälle}}.$$
Wahrscheinlichkeit wird dann zu reiner __Kombinatorik__ — man muss nur abzählen.

## Das Urnenmodell und die Abzählregeln

Aus einer Urne mit $n$ unterscheidbaren Kugeln wird $k$-mal gezogen. Je nachdem, ob die __Reihenfolge__ zählt und ob
__zurückgelegt__ wird, ergeben sich vier Standardfälle mit ihrer Mächtigkeit $|\Omega|$:

- __(i) mit Reihenfolge, mit Zurücklegen:__ $\Omega=U^k$, also $|\Omega|=n^k$.
- __(ii) mit Reihenfolge, ohne Zurücklegen:__ $|\Omega|=n(n-1)\cdots(n-k+1)=\dfrac{n!}{(n-k)!}=:(n)_k$. Für $k=n$ sind das die $k!$ __Permutationen__.
- __(iii) ohne Reihenfolge, ohne Zurücklegen:__ Fall (ii) geteilt durch die $k!$ Umordnungen, also $|\Omega|=\dfrac{n!}{k!\,(n-k)!}=\dbinom{n}{k}$ (__Binomialkoeffizient__).
- __(iv) ohne Reihenfolge, mit Zurücklegen:__ Durch die Umkehr-eindeutige Umbenennung $\tilde\omega_i:=\omega_i+(i-1)$ auf Fall (iii) mit $n+k-1$ zurückgeführt: $|\Omega|=\dbinom{n+k-1}{k}$.

__Standardbeispiele.__ Das __Geburtstagsproblem__ für $k$ Personen bei $n=365$ Tagen: alle an verschiedenen Tagen
entspricht Modell (ii) in (i), also $P=\frac{(365)_k}{365^k}$. Das __Zahlenlotto „6 aus 49"__ ist Modell (iii) mit
$n=49$, $k=6$, also $|\Omega|=\binom{49}{6}$ und $P(\text{6 Richtige})=1/\binom{49}{6}$; „genau $i$ Richtige" hat
$\binom{6}{i}\binom{43}{6-i}$ günstige Fälle. Und die Zahl der verschiedenen partiellen Ableitungen der Ordnung $k$
einer Funktion in $n$ Variablen ist $\binom{n+k-1}{k}$ — genau Modell (iv).

## Bernoulli-Experimente

Ein __Bernoulli-Experiment__ hat genau zwei Ausgänge, $\omega\in\{0,1\}$, mit $P(1)=p$ und $P(0)=1-p$ für ein
$p\in(0,1)$ (für $p=\tfrac12$ wieder ein Laplace-Fall). Wiederholt man es $n$-mal unabhängig, so ist
$\Omega=\{0,1\}^n$ mit $P_n(\omega)=P(\omega_1)\cdots P(\omega_n)$. Die Wahrscheinlichkeit, dass **genau $k$-mal**
der Ausgang $1$ auftritt, ist die __Binomialverteilung__
$$P_n(A_k)=\binom{n}{k}\,p^k(1-p)^{n-k}.$$
Der Faktor $\binom nk$ zählt dabei, auf wie viele Weisen sich die $k$ Einsen auf die $n$ Plätze verteilen können.

## Kontinuierliche Wahrscheinlichkeitsräume

Nimmt der Zufall ein **Kontinuum** von Werten an (z. B. $\Omega=\mathbb R$), ist Abzählen sinnlos — man braucht eine
__Wahrscheinlichkeitsdichte__: eine stetige, nichtnegative, (uneigentlich) integrierbare Funktion $\rho:\mathbb
R\to\mathbb R$ mit $\int_{-\infty}^{\infty}\rho(x)\,dx=1$. Für ein Intervall (oder eine endliche Vereinigung von
Intervallen) $A$ setzt man
$$P(A)=\int_A\rho(x)\,dx.$$
Wahrscheinlichkeit ist nun **Fläche unter der Dichte**, nicht Summe von Punktmassen — ein einzelner Punkt hat
Wahrscheinlichkeit $0$.

__Beispiel 8.8 (Normalverteilungen).__ Für $\mu\in\mathbb R$ und $\sigma>0$ ist
$$\rho(x)=\frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\Big(-\tfrac12\big(\tfrac{x-\mu}{\sigma}\big)^2\Big)$$
eine Familie von Dichten — Verschiebungen (um $\mu$) und Skalierungen (mit $\sigma$) der Gaußfunktion
$f(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$, für die wir $\int_{\mathbb R}f=1$ früher über den Polarkoordinaten-Trick
bewiesen haben.

__Die Borel-Algebra.__ Endliche Vereinigungen offener Intervalle bilden **keine** $\sigma$-Algebra. Die kleinste
$\sigma$-Algebra, die alle offenen Intervalle enthält, heißt __Borel-Algebra__ $\mathcal B$; die Lebesgue-Theorie
erlaubt die Integration über Mengen in $\mathcal B$. So entsteht der Wahrscheinlichkeitsraum $(\mathbb R,\mathcal
B,P)$. (In der Physik: die Aufenthaltswahrscheinlichkeit eines Quantenteilchens ist $P(A)=\int_A|\psi(x)|^2\,dx$ mit
$\int_{\mathbb R^3}|\psi|^2=1$.)

## Die vereinigende Idee

Diskret und kontinuierlich sind zwei Seiten **einer** Medaille — des verallgemeinerten Integralbegriffs. Ersetzt man
die kontinuierliche Dichte durch eine Summe von __Dirac-Massen__ $\delta_{\omega_i}$ mit Gewichten $p_i\ge0$,
$\sum_i p_i=1$, also $\rho\,dx\rightsquigarrow\sum_i p_i\,\delta_{\omega_i}$, so wird
$$P(A)=\int_A\rho(x)\,dx\ \rightsquigarrow\ \sum_i p_i\int_A\delta_{\omega_i}(dx)=\sum_{\omega_i\in A}p_i$$
— genau der diskrete Fall. Das ist die eigentliche Stärke der maßtheoretischen Wahrscheinlichkeitsrechnung: Ein
einziger Rahmen, ein einziges Integral.

**Stolperstein:** (1) $\Omega$ und $\mathcal E$ sind __problemabhängig__ — es gibt nicht „den" richtigen
Stichprobenraum, nur einen zur Fragestellung passenden. (2) Das „$\sigma$" (abzählbare Additivität/Vereinigung) ist
**kein Luxus**: Nur damit gilt die Stetigkeit (Satz 8.4) und darf man Grenzwerte von Ereignissen bilden. (3) Im
kontinuierlichen Fall ist $P(\{x\})=0$ für jeden Einzelpunkt — Wahrscheinlichkeit $0$ heißt **nicht** „unmöglich".
(4) Eine Dichte ist **kein** Wahrscheinlichkeitswert: $\rho(x)$ darf $>1$ sein; erst das Integral über ein Intervall
liegt in $[0,1]$.

:::kern
Ein __Wahrscheinlichkeitsraum__ ist ein Tripel $(\Omega,\mathcal E,P)$: __Stichprobenraum__ $\Omega$ (alle
Ergebnisse, problemabhängig), __Ereignisraum__ $\mathcal E$ = __$\sigma$-Algebra__ (Def. 8.1: enthält $\Omega$,
abgeschlossen unter Komplement/Schnitt und **abzählbarer** Vereinigung ⇒ auch $\emptyset$, Differenz, abzählbarer
Schnitt), __Wahrscheinlichkeitsmaß__ $P:\mathcal E\to[0,1]$ (Def. 8.3: $\sigma$-additiv auf disjunkten Mengen,
$P(\Omega)=1$) ⇒ $P(A^c)=1-P(A)$, Monotonie, Stetigkeit (Satz 8.4). __Diskret__: $\Omega$ abzählbar, $P(A)=\sum_{\omega_i\in
A}p_i$; __Laplace__: $p_i=1/n$, $P(A)=|A|/|\Omega|$ (Kombinatorik). __Urnenmodell__ ($n$, $k$ Züge): (i) $n^k$,
(ii) $(n)_k=n!/(n-k)!$, (iii) $\binom nk$, (iv) $\binom{n+k-1}{k}$. __Bernoulli__/Binomial: $P_n(A_k)=\binom
nk p^k(1-p)^{n-k}$. __Kontinuierlich__: Dichte $\rho\ge0$, $\int\rho=1$, $P(A)=\int_A\rho$ (z. B. Normalverteilung
$\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$), $\sigma$-Algebra = __Borel-Algebra__ $\mathcal B$. Diskret und
kontinuierlich vereint der Integralbegriff (Dichte ↔ Summe von Dirac-Massen).
:::

Mit dem Rahmen steht die Bühne. Als Nächstes präzisieren wir, wann zwei Ereignisse einander **nicht beeinflussen** —
die __stochastische Unabhängigkeit__ — und die eng verwandte __bedingte Wahrscheinlichkeit__ mit der Formel von
Bayes. Das ist das Thema des nächsten Artikels.

:::quiz
F: Warum ist der Stichprobenraum $\Omega$ nicht eindeutig durch das Zufallsexperiment festgelegt?
A: Weil er davon abhängt, welche Frage man beantworten will. Wirft man zwei Würfel und interessiert sich für jedes Paar, hat $\Omega$ 36 Elemente; interessiert nur die Augensumme, genügen 11. Man wählt $\Omega$ so grob oder fein, wie die Fragestellung es verlangt.
F: Warum modelliert man Ereignisse als Teilmengen von $\Omega$?
A: Ein Ereignis ist eine mit ja/nein beantwortbare Frage, und die Menge aller Ergebnisse mit Antwort „ja" ist gerade eine Teilmenge $A\subset\Omega$. Logische Verknüpfungen von Fragen (und/oder/nicht) werden so zu Mengenoperationen (Schnitt/Vereinigung/Komplement).
F: Wofür steht das „$\sigma$" in $\sigma$-Algebra, und warum reicht endliche Abgeschlossenheit nicht?
A: Es steht für die Abgeschlossenheit unter **abzählbar** unendlichen Vereinigungen, nicht nur endlichen. Nur so darf man Grenzwerte von Ereignisfolgen bilden — etwa „irgendwann tritt $A$ ein" als $\bigcup_n A_n$ — und es gilt die Stetigkeit des Maßes (Satz 8.4).
F: Warum enthält jede $\sigma$-Algebra automatisch die leere Menge und ist unter abzählbarem Schnitt abgeschlossen?
A: Aus $\Omega\in\mathcal E$ und Abgeschlossenheit unter Komplement folgt $\emptyset=\Omega^c\in\mathcal E$. Mit den de-Morgan-Regeln ist ein abzählbarer Schnitt das Komplement einer abzählbaren Vereinigung von Komplementen — also wieder in $\mathcal E$.
F: Woraus leitet sich die Forderung ab, dass $P$ $\sigma$-additiv ist und $P(\Omega)=1$ gilt?
A: $P(A)$ soll die relative Häufigkeit von $A$ in sehr vielen Wiederholungen nachbilden. Relative Häufigkeiten sind nichtnegativ, addieren sich bei disjunkten Ereignissen und ergeben über alle Ausgänge zusammen $1$ — das führt direkt auf Additivität (verschärft zu $\sigma$-Additivität) und die Normierung $P(\Omega)=1$.
F: Wie folgt die Gegenwahrscheinlichkeit $P(A^c)=1-P(A)$ aus den Axiomen?
A: $\Omega$ zerfällt disjunkt in $A$ und $A^c$, also $P(A)+P(A^c)=P(\Omega)=1$ nach Additivität und Normierung. Umgestellt ergibt sich $P(A^c)=1-P(A)$ — oft rechnet man das Gegenereignis, weil es einfacher ist.
F: Was bedeutet die Stetigkeit des Wahrscheinlichkeitsmaßes (Satz 8.4) anschaulich?
A: Wächst eine Ereignisfolge monoton ($A_n\subset A_{n+1}$) gegen ihre Vereinigung, so konvergieren die Wahrscheinlichkeiten $P(A_n)$ gegen $P$ der Vereinigung. Grenzwertbildung bei Mengen und beim Maß sind also vertauschbar — genau dafür braucht man die abzählbare Additivität.
F: Warum reduziert sich im Laplace-Raum die Wahrscheinlichkeit auf das Abzählen von Elementen?
A: Sind alle $n$ Elementarereignisse gleich wahrscheinlich ($p_i=1/n$), so ist $P(A)=\sum_{\omega_i\in A}\frac1n=\frac{|A|}{n}$. Die Wahrscheinlichkeit ist dann nur noch das Verhältnis günstiger zu möglichen Fällen — ein rein kombinatorisches Zählproblem.
F: Warum tritt in der Binomialverteilung der Faktor $\binom nk$ auf?
A: $p^k(1-p)^{n-k}$ ist die Wahrscheinlichkeit **einer** bestimmten Abfolge mit $k$ Einsen und $n-k$ Nullen. Da die $k$ Einsen auf $\binom nk$ verschiedene Weisen auf die $n$ Plätze verteilt sein können und alle diese disjunkten Abfolgen gleich wahrscheinlich sind, summiert man sie mit dem Faktor $\binom nk$ auf.
F: Warum hat im kontinuierlichen Fall ein einzelner Punkt Wahrscheinlichkeit $0$, und was ist der Unterschied zwischen Dichte und Wahrscheinlichkeit?
A: $P(\{x\})=\int_{\{x\}}\rho=0$, weil das Integral über einen einzelnen Punkt (eine Nullmenge) verschwindet — Wahrscheinlichkeit entsteht erst über ein Intervall als Fläche. Die Dichte $\rho(x)$ selbst ist kein Wahrscheinlichkeitswert und darf $>1$ sein; erst $\int_A\rho$ liegt in $[0,1]$.
:::
