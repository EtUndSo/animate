---
title: Stufe 1: Warum Silizium kaum leitet
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190300
summary: Metall leitet, Glas nicht, reines Silizium kaum.
tags: Energieniveaus, Band, verbotene Zone, Valenzband, Leitungsband, Bandabstand, Fermi-Energie, Metall
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Metall leitet, Glas nicht, reines Silizium kaum. Der Unterschied liegt in der Zahl der beweglichen Elektronen. Diese Stufe erklärt sie aus den erlaubten Energien im Kristall.
:::

**Die Idee.** Im einzelnen Atom haben Elektronen nur bestimmte Energien, die __Energieniveaus__. Im Kristall (regelmäßiges Gitter von Atomen) überlappen sich die Hüllen, die Elektronen gehören dem ganzen Kristall. Keine zwei Elektronen dürfen denselben Zustand besetzen. Deshalb spaltet jedes Niveau in so viele dicht liegende Niveaus auf, wie der Kristall Atome hat. So entsteht ein __Band__ erlaubter Energien. Zwischen den Bändern liegt die __verbotene Zone__: Dort gibt es keine Zustände. Ein Feld kann ein Elektron nur beschleunigen, wenn knapp über ihm ein freier Zustand liegt. Ein volles Band leitet also nicht, gleich wie viele Elektronen es enthält.

:::abbildung et1/k9baender 2
Bändermodell, nicht maßstäblich; $W$ ist die Energie eines Elektrons. Im Metall ist das oberste Band nur teilweise gefüllt. Im Halbleiter hebt Wärme wenige Elektronen über die kleine Lücke, zurück bleiben Löcher. Im Isolator ist die Lücke zu groß.
:::

:::definition Definition 1.1 (Bänder)
<span class="anker" id="satz-1-1"></span>

Das __Valenzband__ (VB) ist das oberste Band, das bei $T=0$ voll besetzt ist. Das __Leitungsband__ (LB) liegt darüber und ist bei $T=0$ leer. Der __Bandabstand__ $W_\mathrm g$ ist die kleinste Energie, die ein Elektron vom VB ins LB hebt. Die __Fermi-Energie__ $W_\mathrm F$ trennt bei $T=0$ besetzte von leeren Zuständen. Bei $T>0$ ist sie die Energie, bei der ein Zustand zur Hälfte der Zeit besetzt wäre; sie darf in der Lücke liegen, obwohl es dort keinen Zustand gibt.
:::

⁠**So liest man das:** Silizium hat $W_\mathrm g=1{,}12$ eV, Germanium 0,67 eV, Diamant 5,5 eV. **Drei Fälle:** Im __Metall__ ist das oberste besetzte Band nur teilweise gefüllt, freie Zustände liegen direkt über den Elektronen, und es leitet bei jeder Temperatur. Im __Isolator__ ist $W_\mathrm g$ so groß, dass kein Elektron hinübergelangt. Ein Halbleiter ist ein Isolator mit kleiner Lücke: Bei $T=0$ isoliert er, bei Anregung durch Wärme, Licht oder starke Felder gelangen Elektronen ins LB.

Ein Elektron, das ins LB wechselt, hinterlässt im VB einen freien Platz. Ein Nachbarelektron rückt nach, und der Platz wandert. Das __Loch__ (Defektelektron) verhält sich wie ein bewegliches Teilchen mit der Ladung $+e$. Beide zählen als Ladungsträger: Elektronen im LB und Löcher im VB. Fällt ein Elektron in ein Loch zurück, verschwinden beide, das heißt __Rekombination__.

:::satz Satz 1.2 (Anteil der Elektronen im Leitungsband)
<span class="anker" id="satz-1-2"></span>

In reinem Halbleiter liegt $W_\mathrm F$ in der Mitte der Lücke. Für die Zustände am Rand des LB ist deshalb

<span class="anker" id="gl-1-1"></span>
$$\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}. \tag{1.1}$$
:::

:::herleitung Warum die halbe Lücke zählt
Jedes Elektron im LB lässt ein Loch im VB zurück, also ist die Zahl beider gleich. Das geht bei ähnlich vielen Zuständen in beiden Bändern nur, wenn $W_\mathrm F$ von beiden Bandrändern denselben Abstand $W_\mathrm g/2$ hat. In [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1) zählt die Energie über $W_\mathrm F$, also $W=W_\mathrm g/2$.
:::

::::beispiel
Bei 300 K ist $W_\mathrm g/(k_\mathrm BT)=43{,}3$ und $\mathrm{e}^{-21{,}7}=3{,}9\cdot10^{-10}$. Die gemessene Dichte der freien Elektronen beträgt $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$. Das ist eines je $5\cdot10^{12}$ Atome, denn Silizium hat $5\cdot10^{22}$ Atome je cm$^3$. Kupfer hat $8{,}5\cdot10^{12}$-mal mehr freie Elektronen ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).
::::

⁠**Grenzfälle:** Für $T\to0$ geht [(1.1)](#gl-1-1) gegen null: Silizium isoliert. Je 10 K Erwärmung verdoppelt sich der Anteil. Deshalb sinkt der Widerstand eines Halbleiters mit der Temperatur ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::frage Warum leitet ein volles Band nicht, obwohl es voller Elektronen steckt?
Weil Strom eine Bewegung in Vorzugsrichtung braucht. Dafür müsste ein Elektron in einen Zustand mit etwas mehr Energie wechseln. Im vollen Band ist jeder solche Zustand besetzt. Zwei Elektronen könnten nur tauschen, und das ändert nichts. Das erste Loch macht das Band leitfähig.
:::

:::aufgabe Aufgabe 1 ★ Drei Stoffe vergleichen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Gib $W_\mathrm g=1{,}12$ eV in Joule an. Das Wievielfache von $k_\mathrm BT$ ist das bei 300 K?

</li>

<li>

Berechne [(1.1)](#gl-1-1) für Silizium, Germanium und Diamant. Welcher reine Stoff leitet am besten?

</li>

<li>

Silizium erwärmt sich von 300 K auf 330 K. Um welchen Faktor wächst der Anteil?

</li>

</ol>

:::loesung
(a) $1{,}12\cdot1{,}602\cdot10^{-19}\,\mathrm{J}=1{,}79\cdot10^{-19}$ J, das sind $1{,}12\,\mathrm{eV}/25{,}85\,\mathrm{meV}=43{,}3$-mal $k_\mathrm BT$. (b) Silizium $3{,}9\cdot10^{-10}$, Germanium $2{,}4\cdot10^{-6}$, Diamant $6{,}3\cdot10^{-47}$. Germanium leitet am besten, rund 6000-mal mehr Besetzung als Silizium, Diamant hat praktisch keine freien Elektronen. (c) Mit $U_T=28{,}44$ mV bei 330 K ist der Anteil $2{,}8\cdot10^{-9}$, das 7,2-fache.
:::
:::
