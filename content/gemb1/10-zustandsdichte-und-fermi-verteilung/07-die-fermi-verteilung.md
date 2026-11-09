---
title: Stufe 5: Die Fermi-Verteilung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
order: 4200700
summary: Gesucht ist die Verteilung mit dem größten Gewicht bei gegebener Temperatur und Elektronenzahl.
tags: chemisches Potential
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Gesucht ist die Verteilung mit dem größten Gewicht bei gegebener Temperatur und Elektronenzahl. Diese Stufe rechnet sie aus und erhält die Besetzungswahrscheinlichkeit.
:::

**Die Idee.** Hebt man ein Elektron von einer Gruppe in eine höhere, ändert sich zweierlei. Die Elektronen gewinnen oder verlieren Anordnungen, je nachdem, wie voll beide Gruppen sind. Und das Gitter muss die Energie hergeben und verliert dadurch selbst Anordnungen. Im Gleichgewicht ist die Verschiebung kein Gewinn mehr: Beide Änderungen heben sich auf. Was das Gitter für eine Energie $\mathrm{d} E$ an Entropie verliert, bestimmt seine Temperatur.

**Die Bilanz.** Man nennt $E_\mathrm{ges}=\sum_iN_iE_i$ die Gesamtenergie und $N_\mathrm{ges}=\sum_iN_i$ die Zahl der Elektronen. Für jede kleine Änderung im Gleichgewicht gilt

<span class="anker" id="gl-5-1"></span>
$$\mathrm{d} E_\mathrm{ges}=E_\mathrm F\,\mathrm{d} N_\mathrm{ges}+T\,\mathrm{d} S. \tag{5.1}$$

⁠**So liest man das:** Der zweite Summand ist zugeführte Wärme. $T\,\mathrm{d} S$ ist zugleich die Definition der Temperatur: Sie sagt, wie viel Energie zu einem Zuwachs $\mathrm{d} S$ gehört. Der erste Summand ist die Energie, die ein zusätzliches Elektron dem System bringt, wenn $S$ fest bleibt. Diese Größe heißt __chemisches Potential__ der Elektronen. Sie ist für alle Gruppen gleich, denn sonst lohnte es sich, Elektronen zu verschieben. Bei $T=0$ ist sie die Grenze zwischen besetzt und leer, also die Fermi-Energie $E_\mathrm F$ aus [Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html), und dieser Name gilt nun für jede Temperatur.

:::satz Satz 5.1 (Fermi-Verteilung)
<span class="anker" id="satz-5-1"></span>

Im thermischen Gleichgewicht ist ein Platz der Energie $E$ mit der Wahrscheinlichkeit

<span class="anker" id="gl-5-2"></span>
$$f(E)=\frac1{1+\exp\Bigl(\dfrac{E-E_\mathrm F}{k_\mathrm BT}\Bigr)} \tag{5.2}$$

besetzt. Gleichwertig: Besetzt und leer stehen im Verhältnis $f/(1-f)=\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$.
:::

:::herleitung Von der Abzählung zur Besetzung
<ol>

<li>

Änderungen: $\mathrm{d} E_\mathrm{ges}=\sum_iE_i\,\mathrm{d} N_i$ und $\mathrm{d} N_\mathrm{ges}=\sum_i\mathrm{d} N_i$, denn die $E_i$ liegen fest.

</li>

<li>

Entropie: Ableiten von [(4.4)](anordnungen-zahlen.html#gl-4-4) nach $N_i$ ergibt $-\ln N_i-1+1+\ln(g_i-N_i)+1-1$, also

$$\mathrm{d} S=k_\mathrm B\sum_i\bigl[\ln(g_i-N_i)-\ln N_i\bigr]\mathrm{d} N_i.$$

</li>

<li>

Einsetzen in [(5.1)](#gl-5-1):

$$\sum_i\bigl[E_i-E_\mathrm F+k_\mathrm BT\bigl(\ln N_i-\ln(g_i-N_i)\bigr)\bigr]\mathrm{d} N_i=0.$$

</li>

<li>

Die Bilanz gilt für jede kleine Verschiebung, auch wenn nur ein $\mathrm{d} N_i$ von null verschieden ist. Also verschwindet jede Klammer einzeln:

$$E_i-E_\mathrm F=k_\mathrm BT\ln\frac{g_i-N_i}{N_i}\quad\Longrightarrow\quad\mathrm{e}^{(E_i-E_\mathrm F)/(k_\mathrm BT)}=\frac{g_i}{N_i}-1.$$

</li>

<li>

Umstellen ergibt $N_i/g_i=1/\bigl(1+\mathrm{e}^{(E_i-E_\mathrm F)/(k_\mathrm BT)}\bigr)$. Der Anteil $N_i/g_i$ der besetzten Plätze ist die gesuchte Wahrscheinlichkeit.

</li>

</ol>
:::

⁠**So liest man das:** $f$ liegt zwischen 0 und 1, und bei $E_\mathrm F$ ist $f=\frac12$. $f$ gilt für jeden Platz einzeln: Plätze gleicher Energie haben dieselbe Besetzung. $E_\mathrm F$ ist keine Materialkonstante, die man vorgibt: Sie stellt sich so ein, dass $\int\mathrm{d} E\,D(E)\,f(E)$ die vorhandene Elektronenzahl ergibt. **Gültigkeit:** thermisches Gleichgewicht, große $N_i$ und $g_i-N_i$, keine Wechselwirkung der Elektronen untereinander.

:::abbildung gemb1/k10abzaehlen 5
Punkte: exakt ausgezählte Besetzung, 40 Niveaus im Abstand $\Delta E$ mit je einem Platz, 20 Elektronen. Blau: Fermi-Verteilung mit $E_\mathrm F=19{,}5\,\Delta E$ und $k_\mathrm BT=4{,}43\,\Delta E$.
:::

::::beispiel
Die Formel lässt sich ohne Näherung prüfen. In Abb. [5](#abb-5) liegt die Energie der Elektronen $30\,\Delta E$ über dem tiefsten Wert. Alle 5410 erlaubten Mikrozustände sind aufgezählt, und für jedes Niveau ist gezählt, wie oft es besetzt ist. Stirling kommt nicht vor. Die Punkte folgen [(5.2)](#gl-5-2) bis auf höchstens 0,014. $E_\mathrm F$ und $T$ sind dabei aus der Elektronenzahl und der Energie bestimmt.
::::

⁠**Grenzfall:** Die Niveaus liegen symmetrisch um die Mitte, und $E_\mathrm F$ liegt genau dort.

:::frage Eine Summe kann null sein, weil sich Summanden aufheben. Warum muss jede Klammer einzeln verschwinden?
Weil die Bilanz für jede kleine Änderung gilt, auch für eine, die nur ein einziges $N_i$ ändert. Dann steht in der Summe nur ein Summand, und er muss allein null sein. Eine solche Änderung ist erlaubt, denn [(5.1)](#gl-5-1) enthält $\mathrm{d} E_\mathrm{ges}$ und $\mathrm{d} N_\mathrm{ges}$ ausdrücklich: Weder Energie noch Elektronenzahl müssen dabei festgehalten werden.
:::

:::aufgabe Aufgabe 7 ★★ Die Bilanz nachrechnen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Leite den Ausdruck für $\mathrm{d} S$ aus Schritt 2 selbst her.

</li>

<li>

Eine Gruppe mit $g_i=10^6$ Plätzen liegt bei 300 K um 50 meV über $E_\mathrm F$. Wie viele Elektronen enthält sie? Wie groß ist das Verhältnis von besetzt zu leer?

</li>

<li>

Eine zweite Gruppe liegt 50 meV unter $E_\mathrm F$. Zeige, dass Plätze dieser Gruppe so oft leer sind wie die der ersten besetzt.

</li>

</ol>

:::loesung
(a) $\partial(N\ln N-N)/\partial N=\ln N$ und $\partial\bigl((g-N)\ln(g-N)-(g-N)\bigr)/\partial N=-\ln(g-N)$. Mit den Vorzeichen aus [(4.4)](anordnungen-zahlen.html#gl-4-4) bleibt $\ln(g_i-N_i)-\ln N_i$. (b) $u=1{,}934$, $f=0{,}126$, also $N_i=1{,}26\cdot10^5$. Besetzt zu leer: $\mathrm{e}^{-u}=0{,}145$. (c) $f(E_\mathrm F-50\,\mathrm{meV})=0{,}874$, leer also $0{,}126$, derselbe Wert. Allgemein: $1-1/(1+\mathrm{e}^{-u})=1/(1+\mathrm{e}^{u})$.
:::
:::
