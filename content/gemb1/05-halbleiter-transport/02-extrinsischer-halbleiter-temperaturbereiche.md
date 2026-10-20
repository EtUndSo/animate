---
title: Der extrinsische Halbleiter und die drei Temperaturbereiche
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Halbleiter und Ladungstransport
order: 4050200
summary: Wie sich die Ladungsträgerdichte eines dotierten Halbleiters mit der Temperatur verhält – und warum sie in einem weiten Bereich konstant bleibt. Die Elektroneutralität legt das Fermi-Niveau fest; im Arrhenius-Plot zeigen sich drei Bereiche: Freeze-out (tiefe T), Störstellenerschöpfung mit $n\approx N_d$ (der Arbeitsbereich der Bauelemente) und Eigenleitung (hohe T).
tags: extrinsischer Halbleiter, Elektroneutralität, ionisierte Störstellen, Freeze-out, Störstellenerschöpfung, Eigenleitung, Arrhenius-Plot, Fermi-Niveau
---

:::grafik
Einstiegs-Animation: Ein Arrhenius-Diagramm $\ln n$ über $1/T$ baut sich von rechts (tiefe Temperatur) nach links
(hohe Temperatur) auf. Drei Abschnitte leuchten nacheinander auf: rechts ein ansteigender Ast, der bei $1/T\to\infty$
gegen null geht (__Freeze-out__); in der Mitte ein **flaches Plateau** auf Höhe der Dotierung $N_d$
(__Störstellenerschöpfung__); links ein steiler Anstieg (__Eigenleitung__). Parallel wandert im Bänderschema das
Fermi-Niveau $E_f$: tief von nahe $E_L$ herunter bis zur Bandmitte. Kernbotschaft: Die Zahl der Ladungsträger
durchläuft drei Regime, und dazwischen liegt ein stabiles Plateau.
:::

:::konzept
Ein dotierter (__extrinsischer__) Halbleiter wird **genauso** berechnet wie ein reiner — über $n=\int D(E)f(E)\,dE$.
Neu ist nur, dass die Dotieratome **zusätzliche Zustände** in der Bandlücke beisteuern. Die eigentliche Frage ist:
Wo stellt sich das __Fermi-Niveau__ ein, und wie viele Ladungsträger gibt es bei welcher Temperatur? Die Antwort —
drei charakteristische Temperaturbereiche mit einem stabilen Plateau dazwischen — ist der Grund, warum man
Halbleiterbauelemente überhaupt zuverlässig betreiben kann: Im mittleren Bereich ist die Ladungsträgerdichte
schlicht **gleich der Dotierung** und praktisch temperaturunabhängig.
:::

**Worum es geht:** Wir beschreiben die Störstellen als zusätzliche Zustände, bestimmen über die
__Elektroneutralität__ das Fermi-Niveau und lesen daraus die drei Temperaturbereiche __Freeze-out__,
__Störstellenerschöpfung__ und __Eigenleitung__ ab.

## Störstellen als scharfe Zusatzzustände

Solange die Dotieratome weit genug auseinander sitzen (bis etwa $N_d \sim 10^{19}\,$cm⁻³), „sehen" sich ihre
Wellenfunktionen nicht. Jedes Atom liefert dann genau **einen** scharfen Zustand bei der Energie $E_d$ (Donator)
bzw. $E_a$ (Akzeptor). Die Zustandsdichte der Dotierung ist deshalb eine **Delta-Funktion** (ein unendlich
schmaler Peak mit Gesamtfläche $N_d$):

$$D_d(E) = N_d\,\delta(E - E_d), \qquad D_a(E) = N_a\,\delta(E - E_a).$$

:::grafik
Bänderschema mit der Wurzel-Zustandsdichte von Leitungs- und Valenzband; dazwischen in der Lücke ein scharfer
senkrechter Strich bei $E_d$ (Fläche $N_d$) als Delta-Peak der Donatoren. Beschriftung „ein scharfer Zustand pro
Dotieratom".
:::

## Wie viele Donatoren sind ionisiert?

Ein Donator kann **ein** Elektron tragen (mit Spin auf *oder* ab — zwei Möglichkeiten), aber wegen der
Coulomb-Abstoßung niemals **zwei**. Dieser __Spin-Entartungsfaktor__ verändert die Besetzungsstatistik gegenüber
der einfachen Fermi-Funktion. Die Dichte der **ionisierten** (positiv geladenen, also Elektron-abgebenden)
Donatoren ist

$$N_d^+ = \frac{N_d}{1 + 2\exp\!\left(\dfrac{E_f - E_d}{k_B T}\right)}.$$

- Liegt $E_f$ **unter** $E_d$ (hohe Temperatur / wenig besetzt): Der Exponent ist negativ, der Nenner $\approx 1$,
  also $N_d^+ \approx N_d$ — **alle** Donatoren ionisiert.
- Liegt $E_f$ **über** $E_d$ (tiefe Temperatur): Der Nenner wird groß, $N_d^+ \to 0$ — die Elektronen bleiben am
  Donator „eingefroren".

:::grafik
Die Kurve $N_d^+/N_d$ als Funktion von $E_f$ (bzw. Temperatur): nahe 1, wenn $E_f$ deutlich unter $E_d$ liegt,
nahe 0, wenn $E_f$ darüber liegt, mit dem Übergang am Donatorniveau. Daneben zwei Gitterbilder: Donator mit
gebundenem vs. abgegebenem Elektron.
:::

## Das Fermi-Niveau aus der Elektroneutralität

Der Kristall ist als Ganzes **elektrisch neutral**: Die positiven Ladungen (Löcher $p$ und ionisierte Donatoren
$N_d^+$) müssen die negativen (Elektronen $n$ und ionisierte Akzeptoren $N_a^-$) genau ausgleichen:

$$p + N_d^+ - n - N_a^- \overset{!}{=} 0.$$

Weil **alle** vier Größen über die bisherigen Formeln von $E_f$ abhängen, ist das die Bestimmungsgleichung für das
Fermi-Niveau (im Allgemeinen nur numerisch lösbar). Für einen rein n-dotierten Halbleiter ($p, N_a^-$
vernachlässigbar) vereinfacht sie sich zu $N_d^+ = n$ — und das lässt sich in drei Temperaturbereichen auswerten.

:::grafik
Eine Waage: linke Schale „positiv: $p + N_d^+$", rechte Schale „negativ: $n + N_a^-$", im Gleichgewicht
ausbalanciert. Darunter der vereinfachte n-Fall $N_d^+ = n$.
:::

## Die drei Temperaturbereiche

Trägt man $\ln n$ über $1/T$ auf, zeigen sich drei Bereiche (von tiefer zu hoher Temperatur):

**Bereich III — Freeze-out (tiefe $T$).** Es fehlt thermische Energie, um alle Donatoren zu ionisieren; ein Teil
der Elektronen bleibt „eingefroren". Mit $N_d^+ = n$ ergibt sich

$$n = \sqrt{\tfrac{N_d}{2}\,N_L}\;\exp\!\left(-\frac{E_L - E_d}{2k_B T}\right).$$

Für $T\to 0$ geht $n\to 0$ — der Halbleiter „friert aus" und wird zum Isolator. Die Steigung im Arrhenius-Plot ist
$\sim (E_L - E_d)/2k_B$ (die **halbe** Donator-Ionisierungsenergie).

**Bereich II — Störstellenerschöpfung / Sättigung (mittlere $T$, inkl. Raumtemperatur).** Jetzt sind **alle**
Donatoren ionisiert, aber die intrinsische Paarerzeugung ist noch vernachlässigbar. Also

$$n \approx N_d = \text{const.}$$

Die Elektronendichte ist **temperaturunabhängig** und gleich der Dotierkonzentration. Das ist der
**Arbeitsbereich** aller Bauelemente — genau deshalb funktionieren sie über einen weiten Temperaturbereich stabil.
Das Fermi-Niveau liegt bei $E_f = E_L - k_B T\ln(N_L/N_d)$.

**Bereich I — Eigenleitung (hohe $T$).** Bei hohen Temperaturen wird $n_i$ so groß, dass es die feste Dotierung
$N_d$ **übersteigt**; der Halbleiter verhält sich wieder intrinsisch:

$$n \approx n_i \propto T^{3/2}\exp\!\left(-\frac{E_g}{2k_B T}\right).$$

Die Steigung $\sim E_g/2k_B$ ist deutlich **steiler** als in Bereich III (weil $E_g \gg E_L - E_d$), und das
Fermi-Niveau kehrt zur Bandmitte zurück.

:::grafik
Der vollständige Arrhenius-Plot $\ln n$ über $1/T$ mit allen drei Bereichen beschriftet: rechts Freeze-out
(Steigung $(E_L-E_d)/2k_B$, fällt gegen 0), Mitte Plateau $n\approx N_d$ („Arbeitsbereich"), links Eigenleitung
(steile Steigung $E_g/2k_B$). Die beiden Steigungsdreiecke sind eingezeichnet.
:::

**Die Wanderung des Fermi-Niveaus** fasst alles zusammen: Bei tiefer Temperatur liegt $E_f$ hoch (zwischen $E_L$
und $E_d$), sinkt im Sättigungsbereich allmählich ab und landet bei hoher Temperatur in der Bandmitte — zurück
beim intrinsischen Wert.

:::grafik
Bänderschema mit der Temperaturachse von links (tief) nach rechts (hoch); eine Kurve für $E_f(T)$ startet nahe
$E_L$/$E_d$, fällt durch den Sättigungsbereich und endet in Bandmitte. Die drei Bereiche sind farblich unterlegt.
:::

## Sehr hohe Dotierung: das Störstellenband

Treibt man die Dotierung über $\sim 10^{19}\,$cm⁻³, rücken die Dotieratome so eng zusammen, dass ihre
Wellenfunktionen **überlappen** — genau wie beim periodischen Gitter (Bandstruktur-Oberthema) entsteht aus den
diskreten $E_d$-Niveaus ein **Störstellenband**. Es verbreitert sich, verschmilzt mit dem Leitungsband und
verkleinert die effektive Bandlücke (__Bandgap-Narrowing__). Das Fermi-Niveau rückt dann **in** das Band hinein —
der Halbleiter wird __entartet__ und verhält sich metallisch (leitet auch bei $T=0$).

:::grafik
Drei Stufen zunehmender Dotierung: (1) einzelner scharfer Donatorpeak, (2) verbreitertes Störstellenband unter
$E_L$, (3) mit dem Leitungsband verschmolzen, $E_f$ im Band — „entartet / metallisch". Pfeil „$N_d$ steigt".
:::

:::kern
Ein __extrinsischer__ Halbleiter rechnet sich wie ein reiner, plus Dotier-Zustände $D_d=N_d\,\delta(E-E_d)$.
Ionisierte Donatoren: $N_d^+=N_d/(1+2e^{(E_f-E_d)/k_BT})$ (Faktor 2 = Spin-Entartung). Die __Elektroneutralität__
$p+N_d^+-n-N_a^-=0$ legt $E_f$ fest. Im Arrhenius-Plot $\ln n$ vs. $1/T$ drei Bereiche: **III Freeze-out** (tiefe
$T$, $n\sim e^{-(E_L-E_d)/2k_BT}$, $T\to0\Rightarrow n\to0$), **II Störstellenerschöpfung** (mittlere $T$,
$n\approx N_d=$ const — der **Arbeitsbereich**), **I Eigenleitung** (hohe $T$, $n\approx n_i\sim e^{-E_g/2k_BT}$,
steilere Steigung). $E_f$ wandert von nahe $E_L$ zur Bandmitte. Sehr hohe Dotierung ($\gtrsim10^{19}\,$cm⁻³) →
__Störstellenband__ → Bandgap-Narrowing → __entarteter__ (metallischer) Halbleiter.
:::

Wir wissen jetzt, **wie viele** bewegliche Ladungsträger vorhanden sind. Im nächsten Artikel beginnt der zweite
Teil des Oberthemas: **wie** diese Ladungsträger unter einem elektrischen Feld einen __Strom__ erzeugen — und
warum dafür ausgerechnet Streuung nötig ist.

:::quiz
F: Was legt im dotierten Halbleiter die Lage des Fermi-Niveaus fest?
A: Die Elektroneutralität des Kristalls: Die positiven Ladungen (Löcher + ionisierte Donatoren) müssen die negativen (Elektronen + ionisierte Akzeptoren) genau ausgleichen. Da alle vier Dichten von $E_f$ abhängen, ist diese Bilanz die Bestimmungsgleichung für $E_f$.
F: Warum beschreibt man die Dotieratome über eine Delta-Funktion in der Zustandsdichte?
A: Solange die Atome weit genug auseinandersitzen, überlappen ihre Wellenfunktionen nicht und jedes liefert genau einen scharfen Zustand bei $E_d$. Viele identische, unendlich schmale Zustände mit Gesamtfläche $N_d$ ergeben zusammen einen Delta-Peak.
F: Warum steht im Nenner von $N_d^+$ der Faktor 2 (Spin-Entartung)?
A: Ein Donator kann sein Elektron mit Spin auf *oder* Spin ab binden, also auf zwei Weisen besetzt sein, aber wegen der Coulomb-Abstoßung niemals mit zwei Elektronen. Diese Asymmetrie zwischen „zwei Besetzungsmöglichkeiten, aber nur ein Elektron" liefert den Faktor 2.
F: Warum friert ein Halbleiter bei tiefer Temperatur zum Isolator aus (Freeze-out)?
A: Es fehlt die thermische Energie, um die Elektronen von den Donatoren ins Leitungsband zu heben. Für $T\to0$ bleiben alle Elektronen an ihren Donatoren gebunden, $n\to0$, und ohne bewegliche Ladung leitet der Kristall nicht.
F: Warum ist die Ladungsträgerdichte im Sättigungsbereich temperaturunabhängig?
A: Dort sind bereits alle Donatoren ionisiert (mehr geht nicht), während die intrinsische Paarbildung noch vernachlässigbar ist. Damit ist $n\approx N_d$ fest durch die Dotierung vorgegeben und ändert sich über einen weiten Temperaturbereich kaum.
F: Warum ist gerade der Sättigungsbereich der Arbeitsbereich der Bauelemente?
A: Weil dort die Ladungsträgerdichte gleich der eingestellten Dotierung und praktisch temperaturstabil ist. Nur so haben Dioden und Transistoren über den Betriebstemperaturbereich vorhersagbare, konstante Eigenschaften.
F: Warum übernimmt bei hoher Temperatur die Eigenleitung?
A: Die intrinsische Dichte $n_i$ wächst exponentiell mit $T$ und übersteigt irgendwann die feste Dotierung $N_d$. Dann dominieren die thermisch über die Bandlücke erzeugten Paare, und der Halbleiter verhält sich wieder intrinsisch.
F: Warum ist die Arrhenius-Steigung bei Eigenleitung steiler als beim Freeze-out?
A: Die Freeze-out-Steigung ist $(E_L-E_d)/2k_B$, die Eigenleitungs-Steigung $E_g/2k_B$. Da die Bandlücke $E_g$ viel größer ist als der kleine Donatorabstand $E_L-E_d$, fällt der Eigenleitungsast deutlich steiler aus.
F: Wie wandert das Fermi-Niveau beim Durchlaufen der drei Bereiche?
A: Bei tiefer Temperatur liegt $E_f$ hoch, zwischen $E_L$ und $E_d$. Mit steigender Temperatur sinkt es durch den Sättigungsbereich ab und landet bei Eigenleitung wieder in der Bandmitte — dem intrinsischen Wert.
F: Was passiert bei sehr hoher Dotierung ($\gtrsim10^{19}\,$cm⁻³)?
A: Die Dotieratome rücken so eng zusammen, dass ihre Wellenfunktionen überlappen und aus den diskreten Niveaus ein Störstellenband entsteht. Es verschmilzt mit dem Leitungsband (Bandgap-Narrowing), $E_f$ rückt ins Band, und der Halbleiter wird entartet und leitet metallisch sogar bei $T=0$.
:::
