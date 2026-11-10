---
title: Stufe 3: Fremdatome im Gitter
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210500
summary: Der reine Kristall hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab.
tags: Störstelle, Aktivierungsenergie, n-Typ, p-Typ, Majoritätsträger, Minoritätsträger, flachen Störstelle, Tiefe Störstellen
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Der reine Kristall hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab. Diese Stufe legt Art und Zahl der Träger mit Fremdatomen fest.
:::

**Die Idee.** Bisher war der Kristall fehlerfrei. Reale Kristalle enthalten Störungen, die fast alle Eigenschaften beeinflussen. Hier baut man sie gezielt ein: Eine __Störstelle__ ist ein Fremdatom, das ein Gitteratom ersetzt, ein Punktdefekt. Ersetzt Phosphor mit fünf Valenzelektronen ein Si-Atom, gehen vier in die Bindungen. Das fünfte findet dort keinen Platz. Der Rumpf $\mathrm P^{5+}$ hat gegenüber $\mathrm{Si}^{4+}$ eine positive Elementarladung zu viel und hält es nur schwach fest. Wenig Wärme löst es ab. Dann bewegt es sich frei im Gitter, energetisch im Leitungsband, und eine ortsfeste positive Ladung bleibt zurück. Bor hat nur drei Valenzelektronen, eine Bindung bleibt unvollständig. Mit wenig Energie springt ein Elektron aus einer Nachbarbindung hinein, also aus dem Valenzband. Das Bor trägt dann eine ortsfeste negative Ladung, und der freie Platz wandert als Loch davon.

:::abbildung gemb1/k11dotierung 3
Links oben: Phosphor gibt sein fünftes Elektron ab und bleibt als ortsfeste positive Ladung zurück. Links unten: Bor nimmt ein Elektron aus einer Nachbarbindung auf und lässt ein Loch zurück. Rechts: Niveaus von Fremdatomen in Silizium, Abstand zur nächsten Bandkante in meV, maßstäblich. Oben Donatoren, unten Akzeptoren.
:::

:::definition Definition 3.1 (Donatoren, Akzeptoren, Dotierungstyp)
<span class="anker" id="satz-3-1"></span>

Donatoren sind fünfwertig (P, As, Sb). Ihr gebundenes Elektron hat die Energie $E_\mathrm D$ knapp unter $E_\mathrm C$. Die __Aktivierungsenergie__ ist $\Delta E_\mathrm D=E_\mathrm C-E_\mathrm D$. Akzeptoren sind dreiwertig (B, Al, Ga, In). Ihr aufnahmebereiter Zustand liegt bei $E_\mathrm A$ knapp über $E_\mathrm V$, mit $\Delta E_\mathrm A=E_\mathrm A-E_\mathrm V$. Ihre Dichten heißen $N_\mathrm D$ und $N_\mathrm A$. Ein Halbleiter mit Donatoren heißt n-dotiert oder __n-Typ__, einer mit Akzeptoren p-dotiert oder __p-Typ__. Die häufigere Trägersorte heißt __Majoritätsträger__, die seltenere __Minoritätsträger__.
:::

⁠**So liest man das:** In Silizium ist $\Delta E_\mathrm D=45$ meV für P, 39 meV für Sb, 54 meV für As, und $\Delta E_\mathrm A=45$ meV für B, 67 meV für Al, 72 meV für Ga, 160 meV für In. Bei einer __flachen Störstelle__ liegt die Energie in der Größenordnung von $k_\mathrm BT$. __Tiefe Störstellen__ wie Au, Cr und Fe liegen nahe der Bandmitte. Sie werden kaum ionisiert, liefern kaum Träger und erleichtern die Rekombination. Nach oben begrenzt die temperaturabhängige __Löslichkeit__ die Dotierung, die größte Dichte, die der Kristall aufnimmt: Sie liegt in Si für P und As um $10^{21}\,\mathrm{cm^{-3}}$, für B um $10^{20}\,\mathrm{cm^{-3}}$.

**Kompensation.** Sind beide Sorten vorhanden, fällt das Elektron des Donators auf den tieferen Akzeptor. Beide sind dann ionisiert, ohne einen freien Träger zu liefern, das ist ein __kompensierter Halbleiter__. Es zählt nur die Differenz, die effektive Dichte $N_\mathrm D^*=N_\mathrm D-N_\mathrm A$ beziehungsweise $N_\mathrm A^*=N_\mathrm A-N_\mathrm D$.

::::beispiel
Bei $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ kommt ein P-Atom auf $5\cdot10^{6}$ Si-Atome. Nimm an, alle haben ihr Elektron abgegeben. Dann ist $n=10^{16}\,\mathrm{cm^{-3}}=1{,}1\cdot10^{6}\,n_\mathrm i$, und [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2) erzwingt $p=n_\mathrm i^2/n=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$: Je mehr Elektronen, desto mehr Rekombination, desto weniger Löcher. Für $10^{15}\,\mathrm{cm^{-3}}$ müssen unkontrollierte Fremdatome bei $10^{13}$ bis $10^{14}\,\mathrm{cm^{-3}}$ bleiben, eines auf $5\cdot10^{8}$ bis $5\cdot10^{9}$ Si-Atome. Das reinste Silizium hat noch rund $10^{12}\,\mathrm{cm^{-3}}$.
::::

⁠**Grenzfälle:** Für $N_\mathrm D\to0$ folgt wieder $n=p=n_\mathrm i$. Bei $N_\mathrm D=N_\mathrm A$ ebenso, obwohl der Kristall voller Ionen steckt.

:::frage Ist n-Silizium negativ geladen und p-Silizium positiv?
Nein, beide sind neutral. „n“ und „p“ nennen das Vorzeichen der beweglichen Ladung, nicht das des Stücks. Zu jedem freien Elektron gehört ein ortsfester positiver Rumpf.
:::

:::aufgabe Aufgabe 4 ★ Dotieren und Kompensieren
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Si erhält $N_\mathrm D=2\cdot10^{15}\,\mathrm{cm^{-3}}$. Wie viele Si-Atome kommen auf ein P-Atom? Wie groß sind $n$ und $p$ bei 300 K?

</li>

<li>

Dazu kommen $N_\mathrm A=5\cdot10^{14}\,\mathrm{cm^{-3}}$ Bor. Wie groß sind $n$ und $p$ jetzt?

</li>

<li>

Vorhersage: Wie viel Bor kompensiert die Probe vollständig? Wo liegt dann $E_\mathrm F$?

</li>

</ol>

:::loesung
(a) $2{,}5\cdot10^{7}$ Si-Atome. $n=2\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=3{,}9\cdot10^{4}\,\mathrm{cm^{-3}}$. (b) $n=N_\mathrm D-N_\mathrm A=1{,}5\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=5{,}3\cdot10^{4}\,\mathrm{cm^{-3}}$. (c) $N_\mathrm A=N_\mathrm D=2\cdot10^{15}\,\mathrm{cm^{-3}}$. Dann ist $n=p=n_\mathrm i$ und $E_\mathrm F=E_\mathrm{Fi}$, obwohl alle Fremdatome ionisiert sind.
:::
:::
