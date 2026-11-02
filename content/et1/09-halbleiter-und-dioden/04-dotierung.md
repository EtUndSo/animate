---
title: Stufe 2: Dotierung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190400
summary: Reines Silizium hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab.
tags: Valenzelektronen, kovalente Bindung, Donator, Akzeptor, n-Gebiet, p-Gebiet, Mehrheitsträger, Minderheitsträger
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Reines Silizium hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab. Diese Stufe legt Art und Zahl der Träger mit Fremdatomen fest.
:::

**Die Idee.** Silizium hat vier __Valenzelektronen__ (Elektronen der äußersten Schale). Jedes Atom teilt mit jedem seiner vier Nachbarn ein Elektronenpaar, das ist die __kovalente Bindung__. Ersetzt man ein Atom durch Phosphor mit fünf Valenzelektronen, binden vier, das fünfte bleibt übrig (Abb. [3](#abb-3)). Es hängt nur mit 45 meV am Phosphorrumpf, das ist das 1,7-fache von $k_\mathrm BT$. Wärme löst es fast immer ab, es wird ein freies Elektron im LB, und ein ortsfestes $\mathrm P^+$-Ion bleibt zurück. Bor hat nur drei Valenzelektronen. Eine Bindung bleibt offen, und ein Nachbarelektron springt mit ebenfalls 45 meV hinein. Das ortsfeste $\mathrm B^-$-Ion bleibt, das Loch wandert davon.

:::abbildung et1/k9dotierung 3
Links: Kristall in der Ebene, jede Doppellinie ist eine Bindung. Rechts: Bänder bei 300 K, nicht maßstäblich. Das Niveau $W_\mathrm D$ des Phosphors liegt 45 meV unter dem LB, das Niveau $W_\mathrm A$ des Bors 45 meV über dem VB. Pfeile: Wärme gibt die Elektronen ins LB ab (oben) und holt sie aus dem VB (unten). Die Fermi-Energie rückt zum Band der Mehrheit.
:::

:::definition Definition 2.1 (n- und p-Dotierung)
<span class="anker" id="satz-2-1"></span>

Ein __Donator__ (Phosphor) gibt ein Elektron ab, ein __Akzeptor__ (Bor) nimmt eines auf. Mit $N_\mathrm D$ Donatoren je cm$^3$ entsteht ein __n-Gebiet__, mit $N_\mathrm A$ Akzeptoren je cm$^3$ ein __p-Gebiet__:

<span class="anker" id="gl-2-1"></span>
$$\text{n-Gebiet: }n\approx N_\mathrm D,\qquad\text{p-Gebiet: }p\approx N_\mathrm A,\qquad\text{überall: }n\,p=n_\mathrm i^2. \tag{2.1}$$
:::

⁠**So liest man das:** $n$ und $p$ sind die Dichten der Elektronen und Löcher in 1/cm$^3$. Die häufigere Sorte heißt __Mehrheitsträger__, die seltenere __Minderheitsträger__. Üblich sind $N=10^{15}$ bis $10^{19}\,\mathrm{cm^{-3}}$. Dotierung lädt den Kristall nicht auf: Zu jedem freien Elektron gehört ein ortsfestes $\mathrm P^+$. Die Fermi-Energie steigt im n-Gebiet um $k_\mathrm BT\ln(n/n_\mathrm i)$ über die Bandmitte. **Gültigkeit:** Raumtemperatur (alle Fremdatome ionisiert) und $N\gg n_\mathrm i$.

:::herleitung Warum das Produkt konstant ist
Die Wärme erzeugt Paare aus Elektron und Loch mit einer Rate, die nur von $T$ und dem Stoff abhängt. Rekombination braucht ein Treffen beider, ihre Rate ist $c\,n\,p$. Im Gleichgewicht sind beide Raten gleich, also ist $n\,p$ konstant. In reinem Silizium ist $n=p=n_\mathrm i$, also $n\,p=n_\mathrm i^2$. Mehr Elektronen bedeuten mehr Rekombination und weniger Löcher.
:::

**Beispiel.** Mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ kommt ein Fremdatom auf $5\cdot10^{6}$ Siliziumatome, und doch steigt $n$ auf das Millionenfache von $n_\mathrm i$. Die Löcher sinken auf $p=10^{20}/10^{16}=10^{4}\,\mathrm{cm^{-3}}$. Mehrheit und Minderheit trennt der Faktor $10^{12}$. $W_\mathrm F$ steigt um $25{,}85\,\mathrm{meV}\cdot\ln10^{6}=0{,}36$ eV. **Grenzfall:** Für $N_\mathrm D\to0$ ergibt [(2.1)](#gl-2-1) wieder $n=p=n_\mathrm i$.

:::frage Ist n-Silizium negativ und p-Silizium positiv geladen?
Nein, beide sind neutral. „n“ und „p“ nennen das Vorzeichen der beweglichen Ladungen, nicht das des Stücks. Im n-Gebiet steht jedem freien Elektron ein ortsfestes positives Ion gegenüber. Erst am pn-Übergang trennen sich beide (Stufe [3](die-raumladungszone.html#stufe-3)).
:::

:::aufgabe Aufgabe 2 ★★ Träger zählen
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Silizium erhält $N_\mathrm D=5\cdot10^{15}\,\mathrm{cm^{-3}}$. Wie viele Siliziumatome kommen auf ein Fremdatom? Wie groß sind $n$ und $p$?

</li>

<li>

Wie groß sind $n$ und $p$ bei $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$?

</li>

<li>

Vorhersage: Ein Stück erhält gleich viele Donatoren und Akzeptoren. Was passiert mit den Ladungsträgern?

</li>

</ol>

:::loesung
(a) $5\cdot10^{22}/5\cdot10^{15}=10^{7}$ Atome je Fremdatom, $n=5\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=10^{20}/5\cdot10^{15}=2\cdot10^{4}\,\mathrm{cm^{-3}}$. (b) $p=2\cdot10^{17}\,\mathrm{cm^{-3}}$, $n=500\,\mathrm{cm^{-3}}$. (c) Jedes Donatorelektron fällt auf einen Akzeptor. Es entstehen keine zusätzlichen Träger, $n=p=n_\mathrm i$. Der Kristall verhält sich wie reines Silizium, obwohl er voller Ionen steckt. Das heißt __Kompensation__.
:::
:::
