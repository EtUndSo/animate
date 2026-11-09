---
title: Stufe 2: Zählen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3180300
summary: Sind die Ausgänge abzählbar, genügt ein Gewicht für jeden einzelnen.
tags: diskreter Wahrscheinlichkeitsraum, Laplacesche Wahrscheinlichkeitsraum, Laplace-Experiment, Permutationen, Binomialkoeffizient
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Sind die Ausgänge abzählbar, genügt ein Gewicht für jeden einzelnen. Sind alle gleich wahrscheinlich, wird aus Wahrscheinlichkeit reines Zählen. Diese Stufe zählt die vier Grundsituationen des Ziehens.
:::

**Die Idee.** Ist $\Omega=\{\omega_1,\omega_2,\dots\}$ endlich oder abzählbar, nimmt man $\mathcal E=\mathcal P(\Omega)$ und gibt jedem Ausgang ein Gewicht $p_i\ge0$ mit $\sum_ip_i=1$. Dann ist

<span class="anker" id="gl-2-1"></span>
$$\mathbb{P}(A)=\sum_{\omega_i\in A}p_i \tag{2.1}$$

ein Wahrscheinlichkeitsmaß mit $\mathbb{P}(\omega_i)=p_i$, wobei $\mathbb{P}(\omega_i)$ kurz für $\mathbb{P}(\{\omega_i\})$ steht. Die $\sigma$-Additivität gilt, weil man Reihen mit nichtnegativen Gliedern beliebig umordnen und gruppieren darf. Das ist ein __diskreter Wahrscheinlichkeitsraum__.

Im Spezialfall $\Omega=\{\omega_1,\dots,\omega_n\}$ mit $p_i=1/n$ sind alle Ausgänge gleich wahrscheinlich. Das ist der __Laplacesche Wahrscheinlichkeitsraum__, der Versuch heißt __Laplace-Experiment__, und es gilt

<span class="anker" id="gl-2-2"></span>
$$\mathbb{P}(A)=\frac{\text{Anzahl der Elemente von }A}{\text{Anzahl der Elemente von }\Omega}=\frac{|A|}{|\Omega|}. \tag{2.2}$$

**Das Urnenmodell.** Eine Urne enthält die Kugeln $U=\{1,\dots,n\}$, und man zieht $k$-mal. Je nachdem, ob die Reihenfolge zählt und ob zurückgelegt wird, entstehen vier Fälle. Die letzte Spalte zählt für $n=4$, $k=2$, das sind die Augenpaare der Vierer-Würfel.

|  | Reihenfolge | Zurücklegen | Elemente von $\Omega$ | $\vert \Omega\vert $ | $n=4$, $k=2$ |
|---|---|---|---|---|---|
| (i) | ja | ja | alle $\omega\in U^k$ | $n^k$ | 16 |
| (ii) | ja | nein | $\omega_i\neq\omega_j$ für $i\neq j$ | $(n)_k:=\dfrac{n!}{(n-k)!}$ | 12 |
| (iii) | nein | nein | $\omega_1<\dots<\omega_k$ | $\dbinom nk=\dfrac{n!}{k!\,(n-k)!}$ | 6 |
| (iv) | nein | ja | $\omega_1\le\dots\le\omega_k$ | $\dbinom{n+k-1}{k}$ | 10 |

:::herleitung Die vier Anzahlen
(i) Für jede der $k$ Stellen gibt es $n$ Möglichkeiten.

(ii) Für die erste Stelle gibt es $n$ Möglichkeiten, für die zweite $n-1$, und so weiter: $|\Omega|=n(n-1)\cdots(n-k+1)$. Für $k=n$ ist das $k!$, die Anzahl der __Permutationen__, also Anordnungen, von $k$ Dingen.

(iii) Sortiert man die Tupel aus (ii), fallen jeweils $k!$ zusammen, denn so viele Anordnungen hat eine Auswahl von $k$ Kugeln. Das Ergebnis heißt __Binomialkoeffizient__.

(iv) Die Vorschrift $\tilde\omega_i:=\omega_i+(i-1)$ macht aus $\omega_1\le\dots\le\omega_k$ eine streng steigende Folge in $\{1,\dots,n+k-1\}$ und lässt sich umkehren. Das ist Fall (iii) mit $n+k-1$ Kugeln.
:::

⁠**Vorsicht:** Fall (iv) zählt nur, beim echten Ziehen ist er kein Laplace-Experiment: Bei den Vierer-Würfeln hat das ungeordnete Paar $\{1,1\}$ die Wahrscheinlichkeit $\frac1{16}$, das Paar $\{1,2\}$ aber $\frac2{16}$.

::::beispiel Adressen
$k$ Geräte wählen jedes für sich zufällig eine von 256 Adressen. Das ist Fall (i), also $|\Omega|=256^k$. Das Ereignis $A$ „alle Adressen sind verschieden“ ist Fall (ii):

<span class="anker" id="gl-2-3"></span>
$$\mathbb{P}(A)=\frac{(256)_k}{256^k}. \tag{2.3}$$

Für $k=19$ ist das nur noch $0{,}504$ (Abb. [2](#abb-2)). Es zählen nicht die Geräte, sondern die Paare, und das sind schon 171. Für 365 statt 256 heißt das Geburtstagsproblem.
::::

⁠**Grenzfall:** Für $k=1$ gibt [(2.3)](#gl-2-3) den Wert 1, für $k>256$ den Wert 0.

:::abbildung hm3/k8kollision 2
Wahrscheinlichkeit, dass unter $k$ Geräten mit je einer zufälligen von 256 Adressen zwei dieselbe wählen, also $1-(256)_k/256^k$. Ab $k=20$ ist das wahrscheinlicher als das Gegenteil.
:::

::::beispiel Kiste
Man greift 5 Widerstände heraus, das ist Fall (iii) mit $|\Omega|=\binom{20}5=15504$. Mit $A_i$ für „genau $i$ defekt“ ist $|A_i|=\binom4i\binom{16}{5-i}$: $i$ defekte aus den 4 defekten, die übrigen aus den 16 guten. Damit gilt

$$\mathbb{P}(\text{mindestens 2 defekt})=\frac{\binom42\binom{16}3+\binom43\binom{16}2+\binom44\binom{16}1}{\binom{20}5}=\frac{3856}{15504}\approx0{,}249.$$
::::

::::beispiel Ableitungen
Eine $k$-mal stetig differenzierbare Funktion von $n$ Variablen hat $\binom{n+k-1}k$ verschiedene partielle Ableitungen der Ordnung $k$. Nach dem Lemma von Schwarz ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)) zählt nur, wie oft nach jeder Variablen abgeleitet wird, das ist Fall (iv). Für $f(x,y)$ und $k=3$ sind das 4: $f_{xxx},f_{xxy},f_{xyy},f_{yyy}$.
::::

:::aufgabe Aufgabe 3 ★★ Fehler auf Platinen
<span class="anker" id="aufg-3"></span>

Vier Lötfehler verteilen sich auf drei Platinen.

<ol class="al">

<li>

Wie viele Belegungen gibt es, wenn die Fehler nicht unterscheidbar sind und nur zählt, wie viele auf jeder Platine liegen? Wie wahrscheinlich ist Platine 1 fehlerfrei, wenn alle Belegungen gleich wahrscheinlich wären?

</li>

<li>

Trifft in Wirklichkeit jeder Fehler für sich jede Platine mit $\frac13$, wie groß ist die Wahrscheinlichkeit dann? Woher kommt der Unterschied?

</li>

</ol>

:::loesung
(a) Fall (iv) mit $n=3$, $k=4$ gibt $\binom64=15$ Belegungen. Ist Platine 1 frei, bleiben $n=2$, also $\binom54=5$. Das wären $\frac13$. (b) $(\frac23)^4=\frac{16}{81}\approx0{,}198$. Die Belegungen sind nicht gleich wahrscheinlich: $(4,0,0)$ entsteht auf eine Art, $(2,1,1)$ auf 12 Arten. Für echte, unabhängige Fehler ist (b) richtig.
:::
:::
