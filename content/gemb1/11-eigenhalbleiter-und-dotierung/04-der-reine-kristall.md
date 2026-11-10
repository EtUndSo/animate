---
title: Stufe 2: Der reine Kristall
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210400
summary: Kapitel 10 liefert n und p für eine gegebene Fermi-Energie.
tags: Generation, Rekombination, Lebensdauer, intrinsische Ladungsträgerdichte, intrinsische Fermi-Energie, mittlere effektive Zustandsdichte, Arrhenius-Darstellung, entartet
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
[Kapitel 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) liefert $n$ und $p$ für eine gegebene Fermi-Energie. Im reinen Kristall ist sie nicht frei wählbar. Diese Stufe bestimmt sie und berechnet daraus die Dichte der Ladungsträger.
:::

**Die Idee.** Wärme hebt laufend Elektronen aus dem Valenz- ins Leitungsband, das heißt __Generation__. Jedes hinterlässt einen freien Platz. Ein Nachbarelektron rückt nach, dadurch wandert der Platz: Das Loch bewegt sich wie ein freies Teilchen mit der Ladung $+e$. Trifft ein Elektron ein Loch, fällt es zurück und gibt seine Energie an das Gitter ab, das heißt __Rekombination__. Die mittlere Zeit dazwischen ist die __Lebensdauer__ $\tau_\mathrm{rec}$. Im Gleichgewicht laufen beide Vorgänge gleich oft ab: Die Dichte ist konstant, das Gleichgewicht ist dynamisch. Weil Elektronen und Löcher nur paarweise entstehen, ist ihre Zahl gleich. Diese eine Bedingung legt $E_\mathrm F$ fest.

:::definition Definition 2.1 (Eigenleitungsdichte)
<span class="anker" id="satz-2-1"></span>

Im Eigenhalbleiter gilt $n=p=:n_\mathrm i$. $n_\mathrm i$ heißt __intrinsische Ladungsträgerdichte__ oder Eigenleitungsdichte, die Fermi-Energie heißt hier __intrinsische Fermi-Energie__ $E_\mathrm{Fi}$.
:::

:::satz Satz 2.2 (Lage der Fermi-Energie und Eigenleitungsdichte)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
<span class="anker" id="gl-2-2"></span>
$$\begin{aligned} E_\mathrm{Fi}(T)&=E_\mathrm V+\frac12E_\mathrm g+\frac34k_\mathrm BT\ln\frac{m_\mathrm V^*}{m_\mathrm C^*}, \\ n_\mathrm i&=\sqrt{n\cdot p}=\sqrt{N_\mathrm CN_\mathrm V}\,\exp\Bigl(-\frac12\frac{E_\mathrm g}{k_\mathrm BT}\Bigr)=A\,T^{3/2}\exp\Bigl(-\frac{E_\mathrm g}{2k_\mathrm BT}\Bigr). \end{aligned} \tag{2.1|2.2}$$
:::

:::herleitung Fermi-Energie und $n_\mathrm i$
⁠**Fermi-Energie.** $n=p$ ergibt mit [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1)

$$N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm{Fi}}{k_\mathrm BT}\Bigr)=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm{Fi}-E_\mathrm V}{k_\mathrm BT}\Bigr).$$

Mit $N_\mathrm V/N_\mathrm C=(m_\mathrm V^*/m_\mathrm C^*)^{3/2}$ folgt nach dem Logarithmieren $\frac32k_\mathrm BT\ln(m_\mathrm V^*/m_\mathrm C^*)=-(E_\mathrm V+E_\mathrm C-2E_\mathrm{Fi})$. Einsetzen von $E_\mathrm C=E_\mathrm V+E_\mathrm g$ ergibt [(2.1)](#gl-2-1).

⁠**Dichte.** Aus $n=p=n_\mathrm i$ folgt $n_\mathrm i=\sqrt{n\,p}$, und in [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2) steht $n\,p$. Die Exponenten addieren sich zu $\frac12(-E_\mathrm C+E_\mathrm F-E_\mathrm F+E_\mathrm V)/(k_\mathrm BT)=-E_\mathrm g/(2k_\mathrm BT)$.

⁠**Als Reaktion.** Die Paarbildung lautet $\varnothing\rightleftharpoons\mathrm e^-+\mathrm h^+$, nach rechts Generation, nach links Rekombination. Das Massenwirkungsgesetz der Chemie sagt $n\,p=[\varnothing]\,K'(T)$. $[\varnothing]$ ist die Konzentration der Valenzelektronen. Sie ist praktisch konstant, denn von $2\cdot10^{23}$ Valenzelektronen je cm$^3$ fehlen nur rund $10^{10}$. $K'(T)$ ist die Massenwirkungskonstante.
:::

⁠**So liest man das:** $E_\mathrm{Fi}$ liegt nahe der Bandmitte. Der kleine Zusatz schiebt es zum Band mit der kleineren Masse: Dort gibt es weniger Plätze, also muss $E_\mathrm F$ näher heran, damit gleich viele besetzt sind. $A$ ist eine Materialkonstante, die die effektiven Massen enthält. Oft nennt man stattdessen die __mittlere effektive Zustandsdichte__ $N_\mathrm{eff}=\sqrt{N_\mathrm CN_\mathrm V}=A\,T^{3/2}$, für Si bei 300 K $2{,}27\cdot10^{19}\,\mathrm{cm^{-3}}$ mit $A=4{,}37\cdot10^{15}\,\mathrm{cm^{-3}\,K^{-3/2}}$. Logarithmieren ergibt eine Geradengleichung, die __Arrhenius-Darstellung__:

<span class="anker" id="gl-2-3"></span>
$$\ln\frac{n_\mathrm i}{A\,T^{3/2}}=-\frac{E_\mathrm g}{2k_\mathrm B}\cdot\frac1T. \tag{2.3}$$

Über $1/T$ aufgetragen ist die Steigung $-E_\mathrm g/(2k_\mathrm B)$. So misst man $E_\mathrm g$. **Gültigkeit:** [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1), also $E_\mathrm{Fi}$ mindestens $3k_\mathrm BT$ von beiden Rändern entfernt, und thermisches Gleichgewicht.

:::abbildung gemb1/k11ni 2
Links: Eigenleitungsdichte von Ge, Si und GaAs über $1000/T$, gerechnet mit $E_\mathrm g(T)$ nach [(1.1)](welche-stoffe-halbleiter-sind.html#gl-1-1). Die Kurven sind steiler, je größer die Lücke ist. Rechts: $E_\mathrm g(T)$ derselben Stoffe.
:::

| Stoff | $E_\mathrm g$ in eV | $\varepsilon_\mathrm r$ | $N_\mathrm C$ in cm$^{-3}$ | $N_\mathrm V$ in cm$^{-3}$ | $n_\mathrm i$ in cm$^{-3}$ | $m_\mathrm h^*$; $m_\mathrm l^*$ | $m_\mathrm{hh}^*$; $m_\mathrm{lh}^*$ |
|---|---|---|---|---|---|---|---|
| Ge | 0,67 | 16,0 | $1{,}04\cdot10^{19}$ | $6{,}0\cdot10^{18}$ | $1{,}9\cdot10^{13}$ | 1,64; 0,082 | 0,28; 0,044 |
| Si | 1,12 | 11,7 | $2{,}82\cdot10^{19}$ | $1{,}83\cdot10^{19}$ | $8{,}9\cdot10^{9}$ | 0,92; 0,19 | 0,49; 0,16 |
| GaAs | 1,42 | 13,1 | $4{,}7\cdot10^{17}$ | $7{,}0\cdot10^{18}$ | $2{,}1\cdot10^{6}$ | 0,067 | 0,45; 0,082 |
| InSb | 0,18 | 17,7 | $4{,}3\cdot10^{16}$ | $6{,}3\cdot10^{18}$ | $1{,}6\cdot10^{16}$ | 0,0145 | 0,49 |

Die Werte gelten für 300 K, $n_\mathrm i$ ist mit [(2.2)](#gl-2-2) gerechnet, Massen in Einheiten von $m_0$. In GaAs und InSb ist das Tal kugelförmig, dort steht eine einzige Elektronenmasse.

::::beispiel
Silizium hat bei 300 K $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$, ein Paar auf $5{,}6\cdot10^{12}$ Atome. $E_\mathrm{Fi}$ liegt 5,6 meV unter der Bandmitte, das sind 0,5 % von $E_\mathrm g$. Von 300 K auf 310 K wächst $n_\mathrm i$ um den Faktor 2,11, davon stammen nur 1,05 aus $T^{3/2}$ und 2,01 aus dem Exponenten.
::::

⁠**Grenzfälle:** Für $T\to0$ geht $n_\mathrm i$ gegen null. Bei $m_\mathrm C^*=m_\mathrm V^*$ liegt $E_\mathrm{Fi}$ genau in der Mitte. In InSb ist die Lücke klein und das Massenverhältnis groß, $E_\mathrm{Fi}$ rückt bis auf rund $1\,k_\mathrm BT$ an $E_\mathrm C$ heran. Dann gilt $E-E_\mathrm F>3k_\mathrm BT$ nicht mehr, solche Halbleiter heißen __entartet__. In Ge, Si und GaAs geschieht das erst weit oberhalb der Zimmertemperatur oder durch sehr hohe Dotierung.

:::frage Ein Paar kostet die ganze Lücke $E_\mathrm g$. Warum steht im Exponenten nur die Hälfte?
Für das Paar stimmt das: Das Produkt $n\,p$ folgt $\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}$. Aber $n$ allein ist die Wurzel daraus, denn es entstehen zwei Teilchen. Jedes zahlt die Hälfte: Von $E_\mathrm F$ bis zu jedem Bandrand sind es rund $E_\mathrm g/2$.
:::

:::aufgabe Aufgabe 2 ★★ Germanium
<span class="anker" id="aufg-2"></span>

Benutze die Tabelle. Ge hat $4{,}4\cdot10^{22}$ Atome je cm$^3$.

<ol class="al">

<li>

Berechne $n_\mathrm i$ bei 300 K und den Anteil der Atome, der ein Paar gebildet hat.

</li>

<li>

Wo liegt $E_\mathrm{Fi}$ relativ zur Bandmitte? Rechne über $N_\mathrm V/N_\mathrm C$. Darf man hier die Boltzmann-Näherung benutzen?

</li>

<li>

Um welchen Faktor wächst $n_\mathrm i$ von 300 K auf 360 K bei festem $E_\mathrm g$?

</li>

<li>

Wiederhole (b) für GaAs und InSb. In welchem Stoff versagt die Näherung?

</li>

</ol>

:::loesung
(a) $n_\mathrm i=\sqrt{1{,}04\cdot10^{19}\cdot6{,}0\cdot10^{18}}\,\,\mathrm{cm^{-3}}\cdot\mathrm{e}^{-12{,}96}=1{,}9\cdot10^{13}\,\mathrm{cm^{-3}}$, Anteil $4{,}2\cdot10^{-10}$. (b) $E_\mathrm{Fi}-\frac12(E_\mathrm C+E_\mathrm V)=\frac12k_\mathrm BT\ln(N_\mathrm V/N_\mathrm C)=-7{,}1$ meV. $E_\mathrm C-E_\mathrm{Fi}=342$ meV $=13{,}2\,k_\mathrm BT$, die Näherung gilt. (c) $n_\mathrm i(360\,\mathrm{K})=2{,}1\cdot10^{14}\,\mathrm{cm^{-3}}$, Faktor 11,4. (d) GaAs: $+35$ meV, das sind 2,5 % von $E_\mathrm g$, $E_\mathrm C-E_\mathrm{Fi}=26\,k_\mathrm BT$. InSb: $+65$ meV, $E_\mathrm C-E_\mathrm{Fi}=26$ meV $\approx1\,k_\mathrm BT$. Dort versagt sie.
:::
:::

:::aufgabe Aufgabe 3 ★★ Bandlücke aus zwei Messungen
<span class="anker" id="aufg-3"></span>

Ein unbekannter Eigenhalbleiter zeigt $n_\mathrm i(320\,\mathrm{K})=5{,}67\cdot10^{11}\,\mathrm{cm^{-3}}$ und $n_\mathrm i(450\,\mathrm{K})=1{,}37\cdot10^{14}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Bestimme $E_\mathrm g$ ohne den Faktor $T^{3/2}$.

</li>

<li>

Bestimme $E_\mathrm g$ mit diesem Faktor. Wie groß ist der Fehler aus (a)?

</li>

</ol>

:::loesung
Es ist $\ln(n_2/n_1)=5{,}487$ und $1/T_1-1/T_2=9{,}03\cdot10^{-4}\,\mathrm{K^{-1}}$. (a) $E_\mathrm g=2k_\mathrm B\cdot5{,}487/(9{,}03\cdot10^{-4}\,\mathrm{K^{-1}})=1{,}05$ eV. (b) Vom Logarithmus geht $\frac32\ln(T_2/T_1)=0{,}511$ ab, also $E_\mathrm g=0{,}95$ eV. Der Fehler aus (a) beträgt 10 %.
:::
:::
