---
title: Stufe 8: Was man an einer Bandstruktur abliest
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4191000
summary: Alle Bausteine liegen vor.
tags: Fermi-Energie
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Alle Bausteine liegen vor. Diese Stufe ordnet sie zu einem Verfahren, mit dem man aus jeder Bandstruktur die Eigenschaften eines Stoffs abliest, und schärft das Bild von Metall, Halbleiter und Isolator aus [Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html).
:::

**Die Idee.** Ein Band besteht aus diskreten $\boldsymbol k$-Zuständen, die so dicht liegen, dass sie zusammenhängend erscheinen. Je Volumen fasst es $2n_\mathrm I$ Elektronen mit der Dichte $n_\mathrm I$ der Rumpfionen. Man füllt von unten, und wo die Elektronen enden, entscheidet sich alles. Leitung heißt: Ein Feld ändert $k$, also muss ein Elektron in einen benachbarten freien Zustand wechseln können.

:::definition Definition 8.1 (Fermi-Energie)
<span class="anker" id="satz-8-1"></span>

Die __Fermi-Energie__ $E_\mathrm F$ trennt bei $T=0$ die besetzten von den leeren Zuständen. Schneidet ein Band diese Energie, ist sie die höchste besetzte Energie. Sonst liegt $E_\mathrm F$ in der Lücke.
:::

:::merke Fünf Schritte zum Ablesen
<ol>

<li>

⁠**Zählen.** Außenelektronen je Zelle durch zwei ergibt die Zahl der vollen Bänder.

</li>

<li>

⁠**$E_\mathrm F$ suchen.** Schneidet ein Band $E_\mathrm F$, ist der Stoff ein Metall. Sonst liegen darunter Valenz-, darüber Leitungsbänder.

</li>

<li>

⁠**Lücke.** $E_\mathrm g=E_\mathrm C-E_\mathrm V$ an der Fermi-Energie. Lücken tiefer im Diagramm sind Lücken, aber nicht die Bandlücke.

</li>

<li>

⁠**Direkt oder indirekt.** Stehen beide Kanten über demselben $\boldsymbol k$?

</li>

<li>

⁠**Massen und Entartung.** Krümmung an den Kanten ergibt $m_\mathrm C^*$ und $m_\mathrm V^*$, Steigung $v$, gleichwertige Täler und Bänder den Entartungsgrad.

</li>

</ol>
:::

:::abbildung gemb1/k9lesen 8
Schemabilder, nicht maßstäblich, mit der Fermi-Energie (rot). Blau: bei $T=0$ besetzt, grau: leer. Metall: Das Band schneidet $E_\mathrm F$. Halbleiter und Isolator unterscheiden sich nur in der Größe der Lücke. Graphen: Die Bänder berühren sich am Dirac-Punkt.
:::

**Isolator und Halbleiter.** Beide haben volle Valenz- und leere Leitungsbänder, ein Feld findet keinen freien Zustand. Beim Isolator bleibt es dabei: Diamant hat $E_\mathrm g=5{,}46$ eV, 211-mal die Wärmeenergie $k_\mathrm BT=26$ meV. Beim Halbleiter ist die Lücke klein. Bei $T=0$ isoliert auch er, bei Raumtemperatur gelangen einige Elektronen ins Leitungsband. Dort finden sie freie Zustände, und im Valenzband bleiben Löcher zurück. Beide Sorten tragen Strom, ihre Zahl wächst mit der Temperatur.

**Metall.** Zwei Wege führen dorthin. Erstens kann das oberste Band nur teilweise gefüllt sein: Einwertige Metalle wie Natrium oder Kupfer haben $n_\mathrm I$ Elektronen auf $2n_\mathrm I$ Plätzen, das Band ist halb voll. Zweitens können sich in drei Dimensionen erlaubte Bänder überlappen. Zweiwertige Stoffe wie Magnesium müssten nach Schritt 1 ein Band genau füllen, doch das nächste beginnt tiefer, als das erste endet. Die Elektronen verteilen sich auf beide, und beide leiten, teils überwiegend durch Löcher. Schritt 1 gilt also nur ohne Überlapp.

Ob man wie in [Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) Atome annähert oder Elektronen in ein fertiges Gitter aus Rumpfionen füllt, beide Modelle ergeben dasselbe Bild.

**Bandlücken.** Werte bei Raumtemperatur, dazu $m^*/m_0$ im Leitungsband:

| $E_\mathrm g$ in eV; $m^*/m_0$ | Al | Ga | In | Gruppe IV | $E_\mathrm g$ in eV |
|---|---|---|---|---|---|
| N | 6,2 | 3,37 | 0,7 | C | 5,46 |
| P | 3,12; 0,83 | 2,26; 0,35 | 1,27; 0,077 | Si | 1,12 |
| As | 2,16; 0,15 | 1,42; 0,067 | 0,355; 0,023 | Ge | 0,67 |
| Sb | 1,58; 0,12 | 0,69; 0,041 | 0,17; 0,014 | Sn | 0 |

Kubisches BN hat 6,4 eV. **So liest man das:** Weiter unten im Periodensystem sind mehr Orbitale der Atome besetzt, die Abstände werden länger, Lücke und effektive Masse schrumpfen. **Mechanismus:** Größerer Abstand schwächt die Bindung ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)), bindende und antibindende Zustände rücken zusammen. Valenz- und Leitungsband stoßen sich ab wie die Bänder mit s-p-Kopplung in [Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html). Je näher sie sich kommen, desto stärker krümmen sie sich an der Kante, und desto kleiner ist $m^*$.

::::beispiel GaAs lesen
Acht Elektronen, vier volle Bänder (Schritt 1). Kein Band schneidet $E_\mathrm F$ (2). $E_\mathrm g=1{,}42$ eV (3). Eine zweite Lücke rund 7 bis 10 eV unter $E_\mathrm V$ öffnet sich, weil Ga und As verschieden sind, wie in Aufgabe [2](graphen.html#aufg-2), und spielt für die Leitung keine Rolle. Die Lücke ist direkt (4). Das stark gekrümmte Leitungsband ergibt $m_\mathrm C^*=0{,}067\,m_0$ mit Entartung 1 im $\Gamma$-Tal, oben im Valenzband liegen schwere und leichte Löcher (5). Wie viele Elektronen bei gegebener Temperatur tatsächlich ins Leitungsband gelangen, bleibt die offene Frage.
::::

:::aufgabe Aufgabe 9 ★★ Eine Kette lesen
<span class="anker" id="aufg-9"></span>

Eine Kette mit $a=0{,}3$ nm hat die Bänder $E_1(k)=-1\,\mathrm{eV}+1\,\mathrm{eV}\cdot\cos(ka)$ und $E_2(k)=2\,\mathrm{eV}+0{,}8\,\mathrm{eV}\cdot\cos(ka)$.

<ol class="al">

<li>

Wo liegen Valenzbandmaximum und Leitungsbandminimum? Wie groß ist $E_\mathrm g$? Ist die Lücke direkt?

</li>

<li>

Bestimme $m_\mathrm V^*$, $m_\mathrm C^*$ und $v_\text{max}$ in beiden Bändern.

</li>

<li>

Wie viele Elektronen je Atom ergeben einen Halbleiter, wie viele ein Metall?

</li>

<li>

Was ändert sich mit $E_2(k)=2\,\mathrm{eV}-0{,}8\,\mathrm{eV}\cdot\cos(ka)$?

</li>

</ol>

:::loesung
(a) $E_1$ reicht von $-2$ bis 0 eV, Maximum bei $k=0$. $E_2$ reicht von 1,2 bis 2,8 eV, Minimum bei $k=\pi/a=10{,}47\,\mathrm{nm^{-1}}$. $E_\mathrm g=1{,}2$ eV, indirekt. Senkrecht sind es 2,8 eV bei $k=0$ und 3,2 eV bei $\pi/a$. (b) $E_1\approx-\frac12a^2k^2\cdot1$ eV ergibt $m_\mathrm V^*=\hbar^2/(1\,\mathrm{eV}\cdot a^2)=0{,}85\,m_0$, ebenso $m_\mathrm C^*=\hbar^2/(0{,}8\,\mathrm{eV}\cdot a^2)=1{,}06\,m_0$. Die Steigung ergibt $v_\text{max}=4{,}6\cdot10^5$ m/s und $3{,}6\cdot10^5$ m/s. (c) Ein Atom je Zelle, zwei Plätze je Band. Zwei Elektronen füllen $E_1$: Halbleiter. Ein oder drei Elektronen füllen ein Band halb: Metall. (d) Das Minimum von $E_2$ wandert nach $k=0$, $E_\mathrm g=1{,}2$ eV bleibt, die Lücke wird direkt.
:::
:::

:::aufgabe Aufgabe 10 ★★ Stoffe zuordnen
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Zwei Bandstrukturen gehören zu zwei Formen von Kohlenstoff. In der ersten liegt zwischen vollen und leeren Bändern eine Lücke von 5,5 eV, in der zweiten berühren sich zwei Bänder an den Ecken der Zone. Ordne Graphen und Diamant zu. Welche Form leitet?

</li>

<li>

Bilde $m^*/E_\mathrm g$ für GaAs, InP, InAs, InSb und GaSb. Wie gut gilt $m^*\propto E_\mathrm g$? Warum fallen die indirekten Stoffe AlP und GaP aus der Reihe?

</li>

</ol>

:::loesung
(a) Die erste gehört zu Diamant, die zweite zu Graphen mit seinen Dirac-Punkten. Graphen leitet, Diamant isoliert. (b) In $m_0$/eV: GaAs 0,047, InP 0,061, InAs 0,065, InSb 0,082, GaSb 0,059. Die Regel stimmt in der Größenordnung. AlP (0,27) und GaP (0,16) passen nicht: Ihr Leitungsbandminimum liegt nicht über dem Valenzbandmaximum, die Abstoßung der beiden Kanten wirkt dort also nicht.
:::
:::
