---
title: Stufe 1: Drei Stoffe auf einer Energieskala
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4250300
summary: Metall, Isolator und Halbleiter haben verschiedene Bänder.
tags: Substrat, MOS-Kondensator, Feldeffekt, Vakuumniveau, Austrittsarbeit, Elektronenaffinität, Flachbandspannung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Metall, Isolator und Halbleiter haben verschiedene Bänder. Diese Stufe legt sie auf eine gemeinsame Skala und klärt, wann die Struktur ohne Spannung im Ruhezustand ist.
:::

**Die Idee.** Der MIS-Kondensator (engl. metal-insulator-semiconductor) trägt auf dem Halbleiter einen Isolator und darauf das Gate. Die Halbleiterscheibe heißt __Substrat__ und ist auf der Rückseite leitend kontaktiert. Der wichtigste Typ ist der __MOS-Kondensator__ (metal-oxide-semiconductor) mit $\mathrm{SiO_2}$ auf Silizium. Dicke Isolatorschichten von 100 bis 1000 nm schützen Halbleiteroberflächen vor Feuchtigkeit und trennen Leiterbahnen vom Halbleiter. Dünne Schichten erlauben es, die Oberflächenleitfähigkeit durch ein Feld zu steuern, das ist der __Feldeffekt__. Um die Stoffe zu vergleichen, braucht man einen gemeinsamen Nullpunkt der Energie: das __Vakuumniveau__ $E_\mathrm{vac}$, die Energie eines ruhenden Elektrons knapp außerhalb des Stoffs.

:::definition Definition 1.1 (Austrittsarbeit und Elektronenaffinität)
<span class="anker" id="satz-1-1"></span>

Die __Austrittsarbeit__ $\Phi=E_\mathrm{vac}-E_\mathrm F$ ist die Energie, die ein Elektron vom Fermi-Niveau ins Vakuum hebt. Die __Elektronenaffinität__ $\chi=E_\mathrm{vac}-E_\mathrm C$ ist der Abstand zwischen Vakuumniveau und Leitungsbandkante.
:::

⁠**So liest man das:** $\Phi$ und $\chi$ sind Energien in eV. Die Definition von $\Phi$ gilt für Metalle, Halbleiter und Isolatoren. Index M steht für Metall, SC für den Halbleiter, IS für den Isolator. Silizium hat $\chi_\mathrm{SC}=4{,}05$ eV, $\mathrm{SiO_2}$ hat $\chi_\mathrm{IS}=0{,}9$ eV. Die Barriere zwischen Metall und Isolator ist $\Phi_\mathrm B=\Phi_\mathrm M-\chi_\mathrm{IS}$, gemessen von $E_\mathrm F$ bis zur Leitungsbandkante $E_\mathrm{C,IS}$ des Isolators. Dotierung verschiebt nur $E_\mathrm F$. Deshalb hängt $\Phi_\mathrm{SC}$ von ihr ab, $\chi_\mathrm{SC}$ nicht.

:::abbildung gemb1/k15aufbau 1
Idealer MIS-Kondensator des Rechenmodells ohne Spannung, Energien maßstäblich. Der Isolator reicht nach unten über den Bildrand hinaus. Alle Bänder verlaufen waagerecht, weil $\Phi_\mathrm M=\Phi_\mathrm{SC}$ ist: der Flachbandfall.
:::

:::satz Satz 1.2 (Austrittsarbeit eines Halbleiters)
<span class="anker" id="satz-1-2"></span>

Mit dem Eigenniveau $E_\mathrm{Fi,\infty}$ tief im Halbleiter gilt für n- und p-Dotierung

<span class="anker" id="gl-1-1"></span>
$$\Phi_\mathrm{SC}=\chi_\mathrm{SC}+\frac{E_\mathrm g}{2}+\bigl(E_\mathrm{Fi,\infty}-E_\mathrm F\bigr). \tag{1.1}$$
:::

:::herleitung Aus den Abständen im Bänderdiagramm
Für n-Dotierung liest man $\Phi_\mathrm{SC}=\chi_\mathrm{SC}+(E_\mathrm C-E_\mathrm F)$ ab, mit $E_\mathrm C=E_\mathrm{Fi,\infty}+E_\mathrm g/2$. Für p-Dotierung ist $\Phi_\mathrm{SC}=\chi_\mathrm{SC}+E_\mathrm g-(E_\mathrm F-E_\mathrm V)$, mit $E_\mathrm V=E_\mathrm{Fi,\infty}-E_\mathrm g/2$. Beides ergibt [(1.1)](#gl-1-1). Die Klammer ist nach [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2) im p-Gebiet positiv und im n-Gebiet negativ.
:::

:::definition Definition 1.3 (Idealer MIS-Kondensator)
<span class="anker" id="satz-1-3"></span>

Ein MIS-Kondensator heißt ideal, wenn drei Bedingungen gelten:

<ol>

<li>

Die Austrittsarbeiten sind gleich: $\Phi_\mathrm M=\Phi_\mathrm{SC}$.

</li>

<li>

Im Isolator und an der Grenzfläche sitzen keine Ladungen und keine zusätzlichen Zustände.

</li>

<li>

Der Isolator ist ideal: Es fließt kein Strom durch ihn.

</li>

</ol>
:::

Verbindet man Metall und Halbleiter außen mit einem Draht, gleichen sich ihre Fermi-Niveaus an. Wegen $\Phi_\mathrm M=\Phi_\mathrm{SC}$ stimmen sie schon überein, also fließt keine Ladung. Ohne Ladung gibt es kein Feld, und die Bänder bleiben bis zur Grenzfläche waagerecht (Abb. [1](#abb-1)). Das ist der Flachbandfall. Die Spannung, die die Bänder flach macht, heißt __Flachbandspannung__ $V_\mathrm{FB}$. Für den idealen Kondensator ist $V_\mathrm{FB}=0$. Weil $\chi_\mathrm{SC}$ für n- und p-Silizium gleich ist, $\Phi_\mathrm{SC}$ aber nicht, braucht jedes Substrat sein eigenes Metall.

**Beispiel.** Im Rechenmodell ist $E_\mathrm{Fi,\infty}-E_\mathrm F=25{,}85\,\mathrm{meV}\cdot\ln(3\cdot10^{16}/8{,}9\cdot10^{9})=0{,}389$ eV, also $\Phi_\mathrm{SC}=4{,}05+0{,}56+0{,}389=5{,}00$ eV. Das Metall braucht denselben Wert. Dann ist $\Phi_\mathrm B=4{,}10$ eV, das sind $159\,k_\mathrm BT$. Der Boltzmann-Faktor $10^{-69}$ zeigt, warum thermisch kein Elektron den Isolator überwindet. n-Silizium mit $N_\mathrm D=3\cdot10^{16}\,\mathrm{cm^{-3}}$ hat 4,22 eV. **Grenzfall:** Für $N\to n_\mathrm i$ verschwindet die Klammer, beide Sorten haben $\chi_\mathrm{SC}+E_\mathrm g/2=4{,}61$ eV.

:::frage Warum ist die Elektronenaffinität für n- und p-Silizium gleich, die Austrittsarbeit aber nicht?
Wenige Fremdatome ändern den Kristall und seine Oberfläche kaum, also bleibt der Abstand von $E_\mathrm C$ zum Vakuum gleich. Sie legen aber fest, wie weit die Zustände besetzt sind, und damit $E_\mathrm F$. Die Austrittsarbeit zählt ab $E_\mathrm F$.
:::

:::aufgabe Aufgabe 1 ★ Das passende Metall
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $\Phi_\mathrm{SC}$ für Silizium mit $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$ und mit $N_\mathrm D=2\cdot10^{17}\,\mathrm{cm^{-3}}$.

</li>

<li>

In einem Bänderdiagramm liegt $E_\mathrm C$ im Flachbandfall 0,30 eV über $E_\mathrm F$. Ist der Halbleiter n- oder p-dotiert? Wie groß sind $\Phi_\mathrm{SC}$ und $n$?

</li>

<li>

Vorhersage: Welches Vorzeichen hat $\Phi_\mathrm{SC}-(\chi_\mathrm{SC}+E_\mathrm g/2)$ bei p-Dotierung, und warum?

</li>

</ol>

:::loesung
(a) Der Abstand ist $25{,}85\,\mathrm{meV}\cdot\ln(2\cdot10^{17}/8{,}9\cdot10^{9})=0{,}438$ eV. p-Silizium: $\Phi_\mathrm{SC}=4{,}05+0{,}56+0{,}438=5{,}05$ eV. n-Silizium: $4{,}05+0{,}56-0{,}438=4{,}17$ eV. (b) 0,30 eV ist kleiner als $E_\mathrm g/2=0{,}56$ eV, also liegt $E_\mathrm F$ über der Bandmitte: n-dotiert. $\Phi_\mathrm{SC}=\chi_\mathrm{SC}+0{,}30\,\mathrm{eV}=4{,}35$ eV, $n=N_\mathrm C\mathrm{e}^{-0{,}30/0{,}02585}=2{,}6\cdot10^{14}\,\mathrm{cm^{-3}}$. (c) Positiv: Bei p-Dotierung liegt $E_\mathrm F$ unter $E_\mathrm{Fi}$, das Elektron startet tiefer und braucht mehr Energie bis zum Vakuum.
:::
:::
