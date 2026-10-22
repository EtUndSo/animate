---
title: Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080200
summary: Von Grund auf – wie sich Information auf Wahrscheinlichkeiten auswirkt. Die bedingte Wahrscheinlichkeit $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ aktualisiert die Chance für $A$, wenn $B$ bekannt ist. Unabhängigkeit bedeutet, dass diese Information nichts ändert: $P(A\cap B)=P(A)P(B)$. Mit dem Gesetz der totalen Wahrscheinlichkeit und der Formel von Bayes rechnet man Ursachen aus Wirkungen zurück.
tags: bedingte Wahrscheinlichkeit, stochastische Unabhängigkeit, totale Wahrscheinlichkeit, Satz von Bayes, Zerlegung, disjunkte Ereignisse, Multiplikationsregel
---

:::grafik
Einstiegs-Animation: Der Stichprobenraum $\Omega$ als Fläche, darin zwei überlappende Ereignisse $A$ und $B$. Wird
$B$ **bekannt**, schrumpft die „Welt" auf $B$ zusammen — die neue Wahrscheinlichkeit von $A$ ist der Anteil von
$A\cap B$ **an $B$**, also $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$. Rechts zwei Szenen: Bei **Unabhängigkeit** ist der
Anteil von $A$ in $B$ genauso groß wie in ganz $\Omega$ — das Wissen um $B$ ändert nichts. Darunter das
__Gesetz der totalen Wahrscheinlichkeit__: $\Omega$ ist in disjunkte Stücke $A_i$ zerlegt, und $P(B)$ setzt sich aus
den Beiträgen $P(B\mid A_i)P(A_i)$ zusammen. Kernbotschaft: Bedingen heißt die Bezugswelt verkleinern;
Unabhängigkeit heißt, das ändert nichts.
:::

:::konzept
Die spannendste Frage der Wahrscheinlichkeit ist: Wie ändert __neue Information__ unsere Einschätzung? Die
__bedingte Wahrscheinlichkeit__ $P(A\mid B)$ beantwortet das — sie ist die Wahrscheinlichkeit von $A$, **nachdem**
man erfahren hat, dass $B$ eingetreten ist. Daraus wird der präzise Begriff der __stochastischen Unabhängigkeit__:
Zwei Ereignisse sind unabhängig, wenn das Wissen um das eine die Chance des anderen **nicht** verändert. Und aus
denselben Bausteinen entstehen die zwei großen Werkzeuge der angewandten Statistik: das __Gesetz der totalen
Wahrscheinlichkeit__ (Wirkung aus allen Ursachen zusammensetzen) und die __Formel von Bayes__ (von der Wirkung auf
die Ursache zurückschließen) — das Fundament von medizinischen Tests, Spamfiltern und maschinellem Lernen.
:::

**Worum es geht:** Wir definieren die __bedingte Wahrscheinlichkeit__, daraus die __stochastische Unabhängigkeit__
(auch für mehrere Ereignisse), und leiten das __Gesetz der totalen Wahrscheinlichkeit__ sowie die __Formel von
Bayes__ her.

## Bedingte Wahrscheinlichkeit

Erfährt man, dass $B$ eingetreten ist, so sind nur noch Ergebnisse in $B$ möglich — die „Welt" schrumpft auf $B$.
Die Wahrscheinlichkeit von $A$ unter dieser Bedingung ist der Anteil von $A\cap B$ an $B$:

__Definition.__ Für Ereignisse $A,B$ mit $P(B)\neq0$ heißt
$$P(A\mid B):=\frac{P(A\cap B)}{P(B)}$$
die __bedingte Wahrscheinlichkeit von $A$ gegeben $B$__.

Der Nenner $P(B)$ ist gerade die **Renormierung** auf die neue Bezugswelt: Setzt man $A=\Omega$, so wird
$P(\Omega\mid B)=\frac{P(B)}{P(B)}=1$ — die Bedingung $B$ ist jetzt sicher. Umgestellt ergibt sich die oft nützlichere
__Multiplikationsregel__ $P(A\cap B)=P(A\mid B)\,P(B)$.

## Stochastische Unabhängigkeit

Intuitiv heißt „$A$ unabhängig von $B$", dass das Wissen um $B$ die Chance für $A$ nicht ändert, also $P(A\mid
B)=P(A)$. Setzt man das in die Definition ein, wird daraus $\frac{P(A\cap B)}{P(B)}=P(A)$, d. h. $P(A\cap
B)=P(A)P(B)$ — eine **symmetrische** Bedingung, die ohne die Einschränkung $P(B)\neq0$ auskommt.

__Definition.__ Zwei Ereignisse $A,B$ heißen __unabhängig__ genau dann, wenn
$$P(A\cap B)=P(A)\,P(B).$$

__Bemerkung.__ Sind $A,B$ unabhängig, so auch $A$ und $B^c$: Aus $P(A)=P(A\cap B)+P(A\cap B^c)$ folgt $P(A\cap
B^c)=P(A)-P(A)P(B)=P(A)(1-P(B))=P(A)P(B^c)$. Unabhängigkeit überträgt sich also auf die Gegenereignisse — wer von
$B$ unabhängig ist, ist es auch von „nicht $B$".

__Beispiel.__ Sei $\Omega=[0,1]^2$ und $P(M)$ der Flächeninhalt der (Borel-)Menge $M$. Dann sind $A=\{(x,y):
x\le\tfrac12\}$ (linke Hälfte) und $B=\{(x,y):\tfrac14\le x\le\tfrac34,\ \tfrac14\le y\le\tfrac34\}$ (zentrales
Quadrat) unabhängig — man rechnet $P(A)=\tfrac12$, $P(B)=\tfrac14$, $P(A\cap B)=\tfrac18=P(A)P(B)$ nach. Verschiebt
man $B$ **vertikal**, bleibt die Unabhängigkeit erhalten (die $x$-Bilanz ändert sich nicht), bei **horizontaler**
Verschiebung geht sie verloren — ein Hinweis, dass Unabhängigkeit eine feine, geometrieabhängige Eigenschaft ist, keine
bloße „Überlappungsfreiheit".

__Mehrere Ereignisse.__ __Definition:__ Ereignisse $\{A_i:i\in I\}$ heißen __unabhängig__, wenn für **jede**
endliche Auswahl $i_1,\dots,i_n$
$$P(A_{i_1}\cap\dots\cap A_{i_n})=P(A_{i_1})\cdots P(A_{i_n})$$
gilt. Wichtig: Es genügt **nicht**, dass die Ereignisse nur paarweise unabhängig sind — die Produktformel muss für
**alle** Teilmengen zugleich gelten.

:::grafik
Links die bedingte Wahrscheinlichkeit: $\Omega$ schrumpft auf $B$, $P(A\mid B)$ ist der Anteil des schraffierten
$A\cap B$ an $B$. Mitte Unabhängigkeit im Einheitsquadrat: $A$ linke Hälfte, $B$ zentrales Quadrat,
$P(A\cap B)=\tfrac18=\tfrac12\cdot\tfrac14$; vertikale Verschiebung von $B$ erlaubt, horizontale zerstört es. Rechts
der Unterschied „paarweise" vs. „gemeinsam" unabhängig.
:::

## Das Gesetz der totalen Wahrscheinlichkeit

Oft kennt man $P(B)$ nicht direkt, wohl aber $P(B\mid A_i)$ für verschiedene „Fälle" $A_i$. Zerlegt man $\Omega$ in
disjunkte Fälle, lässt sich $P(B)$ zusammensetzen.

__Satz.__ Sei $A_1,A_2,\dots$ eine (endliche oder abzählbare) Familie **paarweise disjunkter** Ereignisse mit
$\bigcup_i A_i=\Omega$ (eine __Zerlegung__). Dann gilt für jedes Ereignis $B$
$$\text{(i)}\quad P(B)=\sum_i P(B\cap A_i), \qquad\text{(ii)}\quad P(B)=\sum_i P(B\mid A_i)\,P(A_i),$$
summiert über alle $A_i$ mit $P(A_i)>0$.

Teil (i) ist die $\sigma$-Additivität, angewandt auf die disjunkte Zerlegung $B=\bigcup_i(B\cap A_i)$; Teil (ii)
setzt die Multiplikationsregel $P(B\cap A_i)=P(B\mid A_i)P(A_i)$ ein. Die Deutung: Die Gesamtwahrscheinlichkeit von
$B$ ist der **gewichtete Durchschnitt** der bedingten Wahrscheinlichkeiten über alle Fälle, mit den Fallgewichten
$P(A_i)$.

__Beispiel (zweistufiges Experiment).__ Eine Zahl $Z\in\mathbb N$ wird mit $P(Z=n)=1/2^n$ gezogen. Fällt
$Z=n$, so wirft man eine gezinkte Münze, die mit Wahrscheinlichkeit $e^{-n}$ Kopf zeigt. Wie wahrscheinlich ist
insgesamt Kopf? Mit $A_n=\{Z=n\}$ ($P(A_n)=1/2^n$) und $B=\{\text{Kopf}\}$ ($P(B\mid A_n)=e^{-n}$) gibt Teil (ii) des Satzes
$$P(B)=\sum_{n=1}^\infty\Big(\tfrac12\Big)^n e^{-n}=\sum_{n=1}^\infty\Big(\tfrac{1}{2e}\Big)^n=\frac{1/(2e)}{1-1/(2e)}=\frac{1}{2e-1}.$$
Die geometrische Reihe erledigt die Summe; die beiden Zufallsstufen (welche Zahl, dann welche Münze) werden sauber
über die Fallzerlegung verrechnet.

## Die Formel von Bayes

Das Gesetz der totalen Wahrscheinlichkeit geht „vorwärts" (Ursache $A_i$ → Wirkung $B$). Die __Formel von Bayes__
dreht die Richtung um — von der beobachteten Wirkung zurück auf die Ursache. Für $P(A),P(B)>0$:
$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}.$$

Sie folgt in einer Zeile aus der Symmetrie der Multiplikationsregel: $P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A)$,
Auflösen nach $P(A\mid B)$. Setzt man für $P(B)$ das Gesetz der totalen Wahrscheinlichkeit ein (mit einer Zerlegung
$A_1,A_2,\dots$), erhält man die anwendungsreife Form
$$P(A_k\mid B)=\frac{P(B\mid A_k)\,P(A_k)}{\sum_i P(B\mid A_i)\,P(A_i)}.$$

In Worten: Aus den __A-priori__-Wahrscheinlichkeiten $P(A_k)$ (Vorwissen über die Ursachen) und der Likelihood
$P(B\mid A_k)$ (wie gut jede Ursache die Beobachtung erklärt) wird die __A-posteriori__-Wahrscheinlichkeit
$P(A_k\mid B)$ (aktualisiertes Wissen nach der Beobachtung). Das ist der mathematische Kern des Lernens aus Daten —
und der Grund, warum ein hochtreffsicherer Test bei einer seltenen Krankheit trotzdem viele Fehlalarme liefern kann:
Das kleine $P(A_k)$ im Zähler dämpft die große Likelihood.

**Stolperstein:** (1) $P(A\mid B)\neq P(B\mid A)$ im Allgemeinen — die beiden unterscheiden sich gerade um den
Bayes-Faktor $P(A)/P(B)$; sie zu verwechseln ist der „Prosecutor's Fallacy". (2) __Unabhängig ist nicht disjunkt__:
Disjunkte Ereignisse mit $P>0$ sind gerade **abhängig** (tritt eines ein, ist das andere ausgeschlossen, $P(A\cap
B)=0\neq P(A)P(B)$). (3) __Paarweise__ Unabhängigkeit $\neq$ __gemeinsame__ Unabhängigkeit — für letztere muss die
Produktformel für **jede** Teilfamilie gelten. (4) Die $A_i$ im Gesetz der totalen Wahrscheinlichkeit müssen eine echte
Zerlegung sein (disjunkt **und** ausschöpfend), sonst zählt man doppelt oder lässt Fälle aus.

:::kern
__Bedingte Wahrscheinlichkeit__: $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ ($P(B)\neq0$) — Renormierung auf die
neue Bezugswelt $B$; __Multiplikationsregel__ $P(A\cap B)=P(A\mid B)P(B)$. __Unabhängigkeit__: $P(A\cap
B)=P(A)P(B)$ ⟺ $P(A\mid B)=P(A)$ (Wissen um $B$ ändert nichts); dann auch $A,B^c$ unabhängig. Mehrere
Ereignisse: Produktformel für **jede** endliche Auswahl (paarweise $\neq$ gemeinsam). __Gesetz der
totalen Wahrscheinlichkeit__ (Zerlegung $A_i$ disjunkt, $\bigcup A_i=\Omega$): $P(B)=\sum_i P(B\cap
A_i)=\sum_i P(B\mid A_i)P(A_i)$. __Formel von Bayes__: $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$, mit Zerlegung
$P(A_k\mid B)=\frac{P(B\mid A_k)P(A_k)}{\sum_i P(B\mid A_i)P(A_i)}$ (A-priori × Likelihood → A-posteriori). Unabhängig
$\neq$ disjunkt.
:::

Bisher waren Ereignisse Teilmengen, Zufall rein qualitativ. Als Nächstes machen wir den Zufall **quantitativ**: Eine
__Zufallsvariable__ ordnet jedem Ausgang eine Zahl zu und bringt Verteilungsfunktion und Dichte ins Spiel — das Thema
des nächsten Artikels.

:::quiz
F: Warum steht in der bedingten Wahrscheinlichkeit der Nenner $P(B)$?
A: Weil mit dem Eintreten von $B$ nur noch Ergebnisse in $B$ möglich sind — die Bezugswelt schrumpft auf $B$. Teilt man $P(A\cap B)$ durch $P(B)$, renormiert man auf diese neue Welt, sodass $P(B\mid B)=1$ wird.
F: Wie hängen die beiden Charakterisierungen $P(A\mid B)=P(A)$ und $P(A\cap B)=P(A)P(B)$ der Unabhängigkeit zusammen?
A: Setzt man $P(A\mid B)=\frac{P(A\cap B)}{P(B)}=P(A)$ um, erhält man direkt $P(A\cap B)=P(A)P(B)$. Die zweite Form ist aber symmetrisch in $A,B$ und braucht $P(B)\neq0$ nicht — deshalb nimmt man sie als Definition.
F: Warum sind unabhängige Ereignisse etwas ganz anderes als disjunkte?
A: Disjunkt heißt $P(A\cap B)=0$: tritt eines ein, ist das andere ausgeschlossen — das ist maximale Abhängigkeit. Unabhängig heißt $P(A\cap B)=P(A)P(B)$: das Wissen um das eine ändert die Chance des anderen nicht. Zwei disjunkte Ereignisse mit positiver Wahrscheinlichkeit sind sogar immer abhängig.
F: Warum folgt aus der Unabhängigkeit von $A$ und $B$ auch die von $A$ und $B^c$?
A: Man zerlegt $A=(A\cap B)\cup(A\cap B^c)$ disjunkt, also $P(A\cap B^c)=P(A)-P(A\cap B)=P(A)-P(A)P(B)=P(A)(1-P(B))=P(A)P(B^c)$. Unabhängigkeit vom Eintreten von $B$ bedeutet also automatisch auch Unabhängigkeit vom Nicht-Eintreten.
F: Warum genügt paarweise Unabhängigkeit nicht, um gemeinsame Unabhängigkeit zu garantieren?
A: Paarweise Unabhängigkeit prüft nur die Produktformel für Paare; die gemeinsame verlangt sie für jede endliche Auswahl. Es gibt Beispiele, in denen je zwei Ereignisse unabhängig sind, das Wissen um zwei davon aber das dritte determiniert — die Dreierformel also verletzt ist.
F: Was besagt das Gesetz der totalen Wahrscheinlichkeit anschaulich?
A: Zerlegt man alle möglichen Fälle $A_i$ disjunkt und ausschöpfend, so ist $P(B)$ der mit den Fallgewichten $P(A_i)$ gewichtete Durchschnitt der bedingten Wahrscheinlichkeiten $P(B\mid A_i)$. Man setzt die Gesamtwahrscheinlichkeit aus den Beiträgen aller Ursachen zusammen.
F: Wieso müssen die $A_i$ im Gesetz der totalen Wahrscheinlichkeit paarweise disjunkt sein und $\Omega$ ausschöpfen?
A: Ausschöpfend, damit jeder mögliche Ausgang von $B$ von genau einem Fall erfasst wird (sonst fehlen Beiträge); disjunkt, damit kein Ausgang doppelt gezählt wird. Nur dann ist $B=\bigcup_i(B\cap A_i)$ eine disjunkte Zerlegung, auf die die $\sigma$-Additivität passt.
F: Wie leitet sich die Formel von Bayes aus der Multiplikationsregel ab?
A: $P(A\cap B)$ lässt sich auf zwei Weisen schreiben: $P(A\mid B)P(B)=P(B\mid A)P(A)$. Löst man nach $P(A\mid B)$ auf, erhält man $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$ — Bayes ist also nur die Symmetrie des gemeinsamen Ereignisses, nach der anderen Bedingung aufgelöst.
F: Was bedeuten A-priori, Likelihood und A-posteriori in der Bayes-Formel?
A: $P(A_k)$ ist das Vorwissen über die Ursache (a priori), $P(B\mid A_k)$ wie gut diese Ursache die Beobachtung erklärt (Likelihood), und $P(A_k\mid B)$ das aktualisierte Wissen nach der Beobachtung (a posteriori). Bayes beschreibt genau, wie eine Beobachtung das Vorwissen zu neuem Wissen umformt.
F: Warum kann ein sehr treffsicherer Test für eine seltene Krankheit trotzdem viele Fehlalarme produzieren?
A: In Bayes steht die kleine A-priori-Wahrscheinlichkeit $P(\text{krank})$ als Faktor im Zähler und dämpft die hohe Likelihood. Ist die Krankheit selten, überwiegen in absoluten Zahlen die (wenigen Prozent) falsch-positiven unter den vielen Gesunden die echten Positiven — $P(\text{krank}\mid\text{positiv})$ bleibt klein.
:::
