---
title: Das Newtonpotential und die Poisson-Gleichung
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040300
summary: Von Grund auf – das Potential einer kontinuierlichen Ladungs- oder Massenverteilung als Überlagerung von Punktpotentialen, $u(x)=\frac{1}{4\pi}\int \frac{f(y)}{|x-y|}\,dy$. Dieses Newtonpotential ist dank des $r^2$-Volumenfaktors wohldefiniert und löst die Poisson-Gleichung $\Delta u=-f$. Als klassische Anwendung folgt das Newtonsche Schalentheorem: Von außen wirkt eine Kugel wie eine Punktladung, im Hohlraum ist das Feld null.
tags: Newtonpotential, Poisson-Gleichung, Potentialtheorie, Fundamentallösung, Superposition, Schalentheorem, Kugelschale, harmonische Funktion
---

:::grafik
Einstiegs-Animation: Eine ausgedehnte Ladungs-/Massenverteilung $f(y)$ (eingefärbte Dichte). Jedes kleine
Volumenstück $dy$ trägt ein __Punktpotential__ $\frac{1}{4\pi|x-y|}$ bei; alle addieren sich (Superposition) zum
Gesamtpotential $u(x)$. Rechts das __Schalentheorem__ als Animation: Von einem Punkt **außerhalb** einer
homogenen Kugel aus ist das Potential dasselbe, als säße die ganze Masse im **Zentrum** (Punktladung); **innerhalb**
eines hohlen Schalenbereichs ist das Potential **konstant** — kein Feld. Kernbotschaft: Das Newtonpotential
summiert Punktpotentiale und löst die Poisson-Gleichung.
:::

:::konzept
Die __Potentialtheorie__ beantwortet die Grundfrage der Elektrostatik und Gravitation: Welches Potential erzeugt
eine gegebene Ladungs- oder Massenverteilung? Die Idee ist **Superposition**: Jedes Volumenstück wirkt wie eine
winzige Punktladung mit Coulomb-Potential $\frac{1}{4\pi|x-y|}$, und man integriert über alle Beiträge. Das
Ergebnis, das __Newtonpotential__, ist trotz der Singularität bei $x=y$ wohldefiniert (dank des $r^2$-Faktors aus
dem vorigen Artikel) und löst die __Poisson-Gleichung__ $\Delta u=-f$ — die zentrale Feldgleichung. Daraus folgt
ganz nebenbei das berühmte Newtonsche __Schalentheorem__.
:::

**Worum es geht:** Wir definieren das __Newtonpotential__ als singuläres Parameterintegral, verbinden es über die
__Poisson-Gleichung__ mit der Quelldichte und leiten das __Schalentheorem__ für die homogene Kugel(schale) her.

## Das Newtonpotential

In der Potentialtheorie treten singuläre Parameterintegrale $u(x)=\int_{\mathbb{R}^n} G(x-y)\,f(y)\,dy$ auf, bei
denen der „Kern" $G$ bei $0$ eine Singularität hat. Man versteht sie als uneigentliche Integrale (Singularität
ausschneiden, Grenzübergang). Das wichtigste Beispiel im $\mathbb{R}^3$ ist das __Newtonpotential__ einer stetig
differenzierbaren Quelldichte $f$ mit kompaktem Träger (Satz 4.9):

$$u(x) = \frac{1}{4\pi}\int_{\mathbb{R}^3} \frac{f(y)}{|x-y|}\,dy.$$

Es ist für alle $x\in\mathbb{R}^3$ **wohldefiniert**: Der Integrand hat bei $y=x$ eine Singularität vom Typ
$1/|x-y|$, also Exponent $\alpha=1<3$ — und nach dem Ergebnis des vorigen Artikels ist eine solche Singularität im
Raum integrierbar (der $r^2$-Faktor des Volumenelements entschärft sie). Anschaulich ist $u(x)$ die **Überlagerung
der Punktpotentiale** $\frac{1}{4\pi|x-y|}$ aller Quellelemente $f(y)\,dy$.

## Die Poisson-Gleichung

Das Newtonpotential $u$ ist zweimal stetig differenzierbar und löst die __Poisson-Gleichung__

$$\Delta u = -f \quad\text{in } \mathbb{R}^3, \qquad u(x)\to 0 \ \text{für } |x|\to\infty.$$

Der Grund ist die **Fundamentallösung**: Das Punktpotential erfüllt $-\Delta\frac{1}{4\pi|x|}=\delta$ (die
Dirac-Distribution) — außerhalb des Ursprungs ist $\frac{1}{4\pi|x|}$ harmonisch (Kapitel 1, Coulomb-Potential),
und die gesamte „Krümmung" konzentriert sich im Ursprung. Wendet man $\Delta$ auf die Superposition an, greift es
also gerade die Quelldichte heraus: $\Delta u(x) = \int(-\delta(x-y))\,f(y)\,dy = -f(x)$.

In der **Physik** schreibt man dieselbe Gleichung mit Konstanten, etwa $\Delta\varphi = -\rho/\varepsilon_0$ für
das elektrostatische Potential einer Ladungsdichte $\rho$. **Wo keine Quellen sind** ($f=0$), ist $u$
**harmonisch** ($\Delta u=0$) — das verbindet die Potentialtheorie mit den harmonischen Funktionen.

:::grafik
Links die Superposition: Quelldichte $f(y)$, jedes Element trägt $\frac{1}{4\pi|x-y|}$ bei, Summe $u(x)$. Rechts
die Fundamentallösung: $\frac{1}{4\pi|x|}$ harmonisch außerhalb $0$, mit einer $\delta$-Spitze im Ursprung
($-\Delta\frac{1}{4\pi|x|}=\delta$) → $\Delta u=-f$.
:::

## Das Schalentheorem (homogene Kugelschale)

Eine klassische Anwendung. Betrachte eine homogen geladene __Kugelschale__ $S=\{R_1\le|y|\le R_2\}$ mit Dichte
$\rho$ und ihr Newtonpotential $u(x)=\frac{\rho}{4\pi}\int_S\frac{d^3y}{|x-y|}$. Aus Symmetriegründen genügt ein
Aufpunkt auf der Achse, $x=(0,0,a)$; in Kugelkoordinaten ist $|x-y|=\sqrt{r^2-2ra\cos\vartheta+a^2}$. Das
Winkelintegral über $\vartheta$ liefert (per Substitution) $\tfrac{2}{a}$ für $a\ge r$ und $\tfrac{2}{r}$ für
$a\le r$, und nach dem Radialintegral bleibt

$$u(x) = \rho\cdot\begin{cases} \dfrac{R_2^3 - R_1^3}{3a}, & a\ge R_2 \quad(\text{außerhalb}),\\[2mm] \dfrac{R_2^2 - R_1^2}{2}, & a\le R_1 \quad(\text{im Hohlraum}).\end{cases}$$

Zwei bemerkenswerte Folgerungen — das __Schalentheorem__:

- **Außen** ($a\ge R_2$): Mit der Gesamtladung $Q=\rho\cdot\mathrm{vol}(S)$ ist (für die Vollkugel $R_1=0,R_2=R$)
  $u=\dfrac{Q}{4\pi a}$ — **exakt das Punktpotential**, als säße die ganze Ladung im Zentrum. Von außen kann man
  nicht unterscheiden, ob die Masse/Ladung homogen verteilt oder im Punkt konzentriert ist.
- **Im Hohlraum** ($a\le R_1$): $u$ ist **konstant** (unabhängig von $a$), also ist das Feld $-\nabla u=0$ —
  **im Inneren einer hohlen Schale herrscht kein Feld**.

Das ist (für Gravitation wie Elektrostatik) Newtons berühmtes Resultat — hier als reine Konsequenz des
Transformationssatzes in Kugelkoordinaten.

:::grafik
Eine Kugelschale $R_1\le|y|\le R_2$ mit Dichte $\rho$; ein Aufpunkt auf der $z$-Achse bei Höhe $a$. Drei Zonen:
außen ($a\ge R_2$) mit $u=\tfrac{Q}{4\pi a}$ (wie Punktladung), in der Schale selbst, und im Hohlraum ($a\le R_1$)
mit konstantem $u$ (Feld null). Daneben das Achsenintegral $|x-y|=\sqrt{r^2-2ra\cos\vartheta+a^2}$.
:::

**Stolperstein:** (1) Das Vorzeichen in $\Delta u=-f$ gehört zur Fundamentallösung $-\Delta\frac{1}{4\pi|x|}=\delta$
— je nach Lehrbuch/Konvention (und je nach Vorzeichen in der Potentialdefinition) kann es anders notiert sein.
(2) Der Integrand ist **singulär**; Wohldefiniertheit und das Ableiten unter dem Integral stützen sich auf das
Majorantenargument für radiale Singularitäten aus dem vorigen Artikel.

:::kern
Das __Newtonpotential__ einer Quelldichte $f$ (kompakter Träger) ist $u(x)=\frac{1}{4\pi}\int_{\mathbb{R}^3}
\frac{f(y)}{|x-y|}\,dy$ — die __Superposition__ der Punktpotentiale $\frac{1}{4\pi|x-y|}$, wohldefiniert, weil die
$1/|x-y|$-Singularität ($\alpha=1<3$) im Raum integrierbar ist. Es ist $C^2$ und löst die __Poisson-Gleichung__
$\Delta u=-f$ ($u\to0$ im Unendlichen), denn $-\Delta\frac{1}{4\pi|x|}=\delta$ (__Fundamentallösung__); physikalisch
$\Delta\varphi=-\rho/\varepsilon_0$. Wo $f=0$, ist $u$ __harmonisch__. __Schalentheorem__ (homogene Kugelschale):
außen $u=\frac{Q}{4\pi a}$ wie eine **Punktladung** im Zentrum, im **Hohlraum** $u=$ const, also **feldfrei** —
Newtons Resultat als Folge des Transformationssatzes in Kugelkoordinaten.
:::

Damit ist der Transformationssatz auf Volumen und Potentiale angewandt. Zum Abschluss des Kapitels betrachten wir,
wie sich die Differentialoperatoren $\nabla$, $\operatorname{div}$ und $\Delta$ in **krummlinigen**
Koordinatensystemen (Polar, Zylinder, Kugel) ausdrücken — mit den __Maßfaktoren__, die dabei auftreten. Das ist
das Thema des nächsten Artikels.

:::quiz
F: Was ist die Grundidee hinter dem Newtonpotential, bevor man überhaupt rechnet?
A: Superposition: Man zerlegt die kontinuierliche Quelldichte $f(y)$ in lauter winzige Punktladungen $f(y)\,dy$, von denen jede ihr Coulomb-Punktpotential $\frac{1}{4\pi|x-y|}$ beiträgt, und summiert (integriert) alle Beiträge. Das Gesamtpotential ist also ein Integral über Punktpotentiale.
F: Warum ist das Integral $u(x)=\frac{1}{4\pi}\int\frac{f(y)}{|x-y|}\,dy$ trotz der Singularität bei $y=x$ wohldefiniert?
A: Der Kern hat bei $y=x$ eine Singularität vom Typ $1/|x-y|$, also Exponent $\alpha=1<3$. Nach dem Ergebnis des vorigen Artikels sind radiale Singularitäten mit $\alpha<3$ im Raum integrierbar — der $r^2$-Faktor des Volumenelements entschärft sie, also existiert das Integral.
F: Was besagt die Poisson-Gleichung $\Delta u=-f$ inhaltlich?
A: Sie verknüpft das Potential mit seiner Quelle: Die „Krümmung" (der Laplace-Operator) des Potentials an einer Stelle ist genau die dort vorhandene negative Quelldichte. Das Potential ist nicht beliebig, sondern von der Ladungs-/Massenverteilung erzwungen.
F: Welche Rolle spielt die Fundamentallösung $-\Delta\frac{1}{4\pi|x|}=\delta$ beim Beweis von $\Delta u=-f$?
A: Das Punktpotential ist außerhalb des Ursprungs harmonisch, und seine gesamte „Quelle" steckt als Dirac-Spitze im Ursprung. Wendet man $\Delta$ auf die Superposition an, greift der Operator über die $\delta$-Distribution genau den Wert $f(x)$ heraus: $\Delta u(x)=\int(-\delta(x-y))f(y)\,dy=-f(x)$.
F: Warum ist das Potential dort, wo keine Quellen sitzen ($f=0$), harmonisch?
A: Setzt man $f=0$ in $\Delta u=-f$, bleibt $\Delta u=0$ — genau die Definition einer harmonischen Funktion. In quellfreien Gebieten verhält sich das Potential also wie die harmonischen Funktionen aus Kapitel 1 (Mittelwerteigenschaft, kein inneres Extremum).
F: Warum darf man beim Schalentheorem den Aufpunkt ohne Einschränkung auf die $z$-Achse legen?
A: Die homogene Kugelschale ist rotationssymmetrisch; das Potential hängt daher nur vom Abstand $a=|x|$ zum Zentrum ab, nicht von der Richtung. Man darf den Aufpunkt deshalb bequem auf die Achse $x=(0,0,a)$ legen, ohne Allgemeinheit zu verlieren.
F: Warum liefert das Winkelintegral zwei verschiedene Werte ($\tfrac2a$ bzw. $\tfrac2r$), je nachdem ob der Aufpunkt außen oder innen liegt?
A: Nach der Substitution im Integral $\int\frac{\sin\vartheta\,d\vartheta}{\sqrt{r^2-2ra\cos\vartheta+a^2}}$ entsteht ein Betrag $|a-r|$, der je nach Vorzeichen von $a-r$ unterschiedlich auflöst. Für $a\ge r$ dominiert $a$, für $a\le r$ dominiert $r$ — daher die Fallunterscheidung.
F: Was besagt das Schalentheorem für einen Beobachter außerhalb der Kugel, und warum ist das bemerkenswert?
A: Von außen ($a\ge R_2$) ist das Potential $u=\frac{Q}{4\pi a}$ — exakt das einer im Zentrum konzentrierten Punktladung $Q$. Man kann von außen also gar nicht unterscheiden, ob die Masse/Ladung homogen über die Kugel verteilt oder in einem Punkt gebündelt ist.
F: Warum herrscht im Hohlraum einer homogenen Kugelschale kein Feld?
A: Dort ($a\le R_1$) ist das Potential konstant, hängt also nicht von $a$ ab. Das Feld ist der (negative) Gradient $-\nabla u$; der Gradient einer Konstanten ist null. Die Beiträge aller Schalenteile heben sich im Inneren exakt auf.
F: Woran erkennt man, dass das Vorzeichen in $\Delta u=-f$ eine Konventionssache ist?
A: Es hängt direkt an der Vorzeichenwahl der Fundamentallösung $-\Delta\frac{1}{4\pi|x|}=\delta$ und an der Definition des Potentials. Je nach Lehrbuch (und physikalischer Konstante wie $\varepsilon_0$) kann dieselbe Physik mit umgekehrtem Vorzeichen notiert sein; wichtig ist die konsistente Kopplung Potential ↔ Quelle.
:::
