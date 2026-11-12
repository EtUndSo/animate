---
title: Stufe 1: Drei Schichten, zwei Spannungen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200300
summary: Eine Diode hat zwei Anschlüsse und eine Kennlinie.
tags: npn-Transistor, BE-Diode, CB-Diode, pnp-Transistor, Schaltzeichen, Kollektorstrom, Basisstrom, Emitterstrom
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Diode hat zwei Anschlüsse und eine Kennlinie. Der Transistor hat drei Anschlüsse. Diese Stufe klärt seinen Aufbau und zählt, wie viele Größen frei sind.
:::

**Die Idee.** Ein __npn-Transistor__ besteht aus drei Gebieten desselben Halbleiters: n-dotierter Emitter, p-dotierte Basis, n-dotierter Kollektor (Abb. [1](#abb-1)). Der Emitter ist am stärksten dotiert, damit er viele Elektronen abgeben kann. Der Kollektor ist am schwächsten dotiert, damit seine Raumladungszone breit wird und hohe Spannungen aushält. Die Basis liegt dazwischen und ist sehr schmal, rund 1 µ m. So entstehen zwei pn-Übergänge, die sich die Basis teilen: die __BE-Diode__ und die __CB-Diode__. Im Normalbetrieb leitet die BE-Diode, die CB-Diode sperrt. Vertauscht man n und p, entsteht der __pnp-Transistor__ (Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)). Im __Schaltzeichen__, dem Symbol im Schaltplan, ist der Emitter der Anschluss mit dem Pfeil. Er zeigt die Richtung des technischen Stroms.

:::abbildung et1/k10aufbau 1
Links: npn-Transistor als Schichtfolge und als Schaltzeichen mit allen Zählpfeilen. Rechts: pnp-Transistor mit umgekehrter Schichtfolge. Der Emitterpfeil zeigt dort in das Bauteil hinein, alle Ströme und Spannungen kehren sich um.
:::

:::definition Definition 1.1 (Ströme und Spannungen am npn-Transistor)
<span class="anker" id="satz-1-1"></span>

$I_\mathrm{B}$ und $I_\mathrm{C}$ zählen in das Bauteil hinein, $I_\mathrm{E}$ heraus. Spannungen sind Potenzialdifferenzen, der erste Index ist der Pluspol: $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$. Immer gilt

<span class="anker" id="gl-1-1"></span>
$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}. \tag{1.1}$$
:::

⁠**So liest man das:** $I_\mathrm{C}$ ist der __Kollektorstrom__, je nach Typ von Mikroampere bis Ampere. $I_\mathrm{B}$ ist der viel kleinere __Basisstrom__, $I_\mathrm{E}$ der __Emitterstrom__. $U_\mathrm{BE}$ liegt an der BE-Diode, um 0,6 V. $U_\mathrm{CE}$ reicht von rund 0,2 V bis zu einigen 10 V. $U_\mathrm{CB}$ ist die Sperrspannung der CB-Diode. **Gültigkeit:** Knoten- und Maschenregel gelten in jedem Betriebszustand.

:::herleitung Wie viele Größen frei sind
Ein Bauteil mit $n$ Anschlüssen hat $n$ Ströme. Es speichert keine Ladung, also nimmt die Knotenregel ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) einen Strom weg. Es hat $n$ Potenziale, aber nur Differenzen zählen, also bleiben $n-1$ Spannungen. Die Diode ($n=2$) hat eine Spannung, einen Strom und eine Kurve. Der Transistor ($n=3$) hat zwei Spannungen und zwei Ströme. Sein Inneres verknüpft sie durch zwei Gleichungen,

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE}).$$

Er ist also ein Zweitor ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)), dessen beide Tore sich den Emitter teilen.
:::

::::beispiel
Im Rechenmodell sind $\varphi_\mathrm{E}=0$, $\varphi_\mathrm{B}=0{,}6$ V, $\varphi_\mathrm{C}=6$ V. Damit ist $U_\mathrm{BE}=0{,}6$ V, $U_\mathrm{CE}=6$ V und $U_\mathrm{CB}=5{,}4$ V. Die BE-Diode leitet, denn ihre p-Seite liegt höher. Die CB-Diode sperrt, denn ihre n-Seite liegt 5,4 V höher. Aus $I_\mathrm{C}=2$ mA und $I_\mathrm{B}=10$ µ A folgt $I_\mathrm{E}=2{,}01$ mA.
::::

⁠**Grenzfall:** Für $U_\mathrm{CB}=0$ ist $U_\mathrm{CE}=U_\mathrm{BE}$. Dort endet der Normalbetrieb.

:::frage Kann ich einen Transistor aus zwei Dioden zusammenlöten?
Nein. Das Ersatzbild aus zwei Dioden zeigt nur die Polung der Grenzen. In zwei getrennten Dioden rekombiniert jedes Elektron, lange bevor es die zweite Sperrschicht erreicht, und die gesperrte Diode bleibt gesperrt. Der Transistoreffekt entsteht erst dadurch, dass beide Grenzen enger beieinanderliegen, als ein Elektron im p-Gebiet überlebt.
:::

:::aufgabe Aufgabe 1 ★ Vom Potenzial zur Spannung
<span class="anker" id="aufg-1"></span>

Gegen Masse werden $\varphi_\mathrm{E}=1{,}2$ V, $\varphi_\mathrm{B}=1{,}85$ V und $\varphi_\mathrm{C}=7$ V gemessen, dazu $I_\mathrm{B}=15$ µ A und $I_\mathrm{C}=3$ mA. (a) Bestimme $U_\mathrm{BE}$, $U_\mathrm{CE}$, $U_\mathrm{CB}$ und prüfe [(1.1)](#gl-1-1). (b) Wie groß ist $I_\mathrm{E}$? (c) Auf welchen Wert muss $\varphi_\mathrm{C}$ fallen, damit $U_\mathrm{CB}=0$ wird?

:::loesung
(a) $U_\mathrm{BE}=0{,}65$ V, $U_\mathrm{CE}=5{,}8$ V, $U_\mathrm{CB}=5{,}15$ V. Probe: $5{,}15\,\mathrm{V}+0{,}65\,\mathrm{V}=5{,}8$ V. (b) $I_\mathrm{E}=3{,}015$ mA. (c) $U_\mathrm{CB}=0$ heißt $\varphi_\mathrm{C}=\varphi_\mathrm{B}=1{,}85$ V.
:::
:::

::::formelsammlung
**Knoten- und Maschenregel am Transistor**

$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$$

$I_\mathrm{B}$ und $I_\mathrm{C}$ zählen in das Bauteil hinein, $I_\mathrm{E}$ heraus. Gilt in jedem Betriebszustand.

**Spannungen als Potenzialdifferenzen**

$$U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E},\qquad U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E},\qquad U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$$

Der erste Index ist der Pluspol. $U_\mathrm{BE}$ liegt an der BE-Diode, um 0,6 V; $U_\mathrm{CB}$ ist die Sperrspannung der CB-Diode. Für $U_\mathrm{CB}=0$ ist $U_\mathrm{CE}=U_\mathrm{BE}$, dort endet der Normalbetrieb.

**Zwei Gleichungen des Transistors**

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE})$$

Ein Bauteil mit $n$ Anschlüssen hat $n-1$ freie Ströme und $n-1$ Spannungen. Der Transistor ($n=3$) ist ein Zweitor, dessen beide Tore sich den Emitter teilen.
::::

::::lernkarten
:::karte begriff Bipolartransistor
Was ist ein Bipolartransistor, und welche Rolle spielt er zwischen einem kleinen Signal und einer großen Last?
---
Ein Halbleiterbauelement aus drei Schichten mit drei Anschlüssen, das mit einem kleinen Signal einen großen Strom steuert. Die Energie kommt aus der Versorgungsspannung, das Signal stellt nur ein.
--- falsch
Ein Halbleiterbauelement aus drei Schichten mit drei Anschlüssen, das die Energie des kleinen Signals selbst vervielfacht. Eine Versorgungsspannung braucht es deshalb nicht, nur das Signal am Eingang.
--- falsch
Ein Halbleiterbauelement aus zwei Schichten mit zwei Anschlüssen, das Strom nur in einer Richtung durchlässt. Die Last wird so vor einer falsch gepolten Versorgungsspannung geschützt.
--- falsch
Ein Bauelement aus drei Schichten mit drei Anschlüssen, das die Spannung des Signals wie ein Transformator hochsetzt. Der Strom am Ausgang ist dabei kleiner als am Eingang.
:::
:::karte begriff npn-Transistor
Wie ist ein npn-Transistor aus Gebieten desselben Halbleiters aufgebaut?
---
Aus drei Gebieten: n-dotierter Emitter, p-dotierte Basis, n-dotierter Kollektor. Die Basis liegt in der Mitte und ist sehr schmal, rund 1 µ m.
--- falsch
Aus drei Gebieten: p-dotierter Emitter, n-dotierte Basis, p-dotierter Kollektor. Die Basis liegt in der Mitte und ist sehr schmal, rund 1 µ m.
--- falsch
Aus drei Gebieten: n-dotierte Basis außen, p-dotierter Emitter in der Mitte, n-dotierter Kollektor. Der Emitter ist sehr schmal, rund 1 µ m.
--- falsch
Aus zwei gleich breiten n-Gebieten, Emitter und Kollektor, die direkt aneinandergrenzen. Die Basis ist ein Metallkontakt an ihrer Grenze.
:::
:::karte begriff Emitter
Welche Aufgabe hat der Emitter im npn-Transistor, und warum ist er am stärksten dotiert?
---
Das n-dotierte Gebiet des npn-Transistors, das Elektronen abgibt. Es ist am stärksten dotiert, damit es viele Elektronen abgeben kann.
--- falsch
Das p-dotierte Gebiet des npn-Transistors, das Löcher einsammelt. Es ist am stärksten dotiert, damit seine Raumladungszone hohe Spannungen aushält.
--- falsch
Das n-dotierte Gebiet des npn-Transistors, das die Elektronen am Ende einsammelt. Es ist am stärksten dotiert, damit es wenig Widerstand hat.
--- falsch
Das schmale Gebiet in der Mitte des npn-Transistors, das den Strom steuert. Es ist am stärksten dotiert, damit schon eine kleine Spannung genügt.
:::
:::karte begriff Basis
Was ist die Basis eines npn-Transistors, und wie schmal ist sie?
---
Das p-dotierte Gebiet zwischen Emitter und Kollektor. Es ist sehr schmal, rund 1 µ m, und lässt die Elektronen aus dem Emitter durch.
--- falsch
Das n-dotierte Gebiet zwischen Emitter und Kollektor. Es ist rund 1 mm breit, damit es die Elektronen aus dem Emitter sicher zurückhält.
--- falsch
Das äußere p-dotierte Gebiet neben dem Emitter. Es ist sehr schmal, rund 1 µ m, und liefert die Elektronen, die der Emitter weitergibt.
--- falsch
Das p-dotierte Gebiet zwischen Emitter und Kollektor. Es ist am stärksten dotiert und breit, damit die Elektronen darin rekombinieren.
:::
:::karte begriff Kollektor
Was ist der Kollektor eines npn-Transistors, und warum ist er am schwächsten dotiert?
---
Das n-dotierte Gebiet, das die Elektronen einsammelt. Es ist am schwächsten dotiert, damit seine Raumladungszone breit wird und hohe Spannungen aushält.
--- falsch
Das n-dotierte Gebiet, das die Elektronen abgibt. Es ist am schwächsten dotiert, damit der Kollektorstrom klein bleibt und das Bauteil nicht überhitzt.
--- falsch
Das p-dotierte Gebiet, das die Löcher einsammelt. Es ist am schwächsten dotiert, damit seine Raumladungszone schmal bleibt und schnell schaltet.
--- falsch
Das n-dotierte Gebiet, das die Elektronen einsammelt. Es ist am schwächsten dotiert, weil dort die meisten Elektronen rekombinieren sollen.
:::
:::karte begriff BE-Diode und CB-Diode
Welche zwei pn-Übergänge enthält ein npn-Transistor, und wie sind sie im Normalbetrieb gepolt?
---
Die BE-Diode zwischen Basis und Emitter und die CB-Diode zwischen Kollektor und Basis; beide teilen sich die Basis. Im Normalbetrieb leitet die BE-Diode, die CB-Diode sperrt.
--- falsch
Die BE-Diode zwischen Basis und Emitter und die CB-Diode zwischen Kollektor und Basis. Im Normalbetrieb sperrt die BE-Diode, und die CB-Diode leitet den Kollektorstrom.
--- falsch
Die BE-Diode zwischen Basis und Emitter und die CB-Diode zwischen Kollektor und Basis. Im Normalbetrieb leiten beide, sonst könnte kein Strom vom Kollektor zum Emitter fließen.
--- falsch
Die CE-Diode zwischen Kollektor und Emitter und die BE-Diode zwischen Basis und Emitter; beide teilen sich den Emitter. Im Normalbetrieb leitet die CE-Diode, die BE-Diode sperrt.
:::
:::karte begriff pnp-Transistor
Wie unterscheidet sich ein pnp-Transistor im Aufbau und im Schaltzeichen vom npn-Transistor?
---
Ein Transistor mit vertauschtem n und p: p-dotierter Emitter, n-dotierte Basis, p-dotierter Kollektor. Der Emitterpfeil zeigt in das Bauteil hinein, alle Ströme und Spannungen kehren sich um.
--- falsch
Emitter und Kollektor sind vertauscht, die Schichtfolge bleibt n, p, n. Der Pfeil sitzt deshalb am Kollektor, die Ströme behalten ihre Richtung.
--- falsch
Ein Transistor mit vertauschtem n und p: p-dotierter Emitter, n-dotierte Basis, p-dotierter Kollektor. Das Schaltzeichen bleibt gleich, nur die Basis liegt jetzt am Pluspol der Versorgung.
--- falsch
Er hat eine zusätzliche p-Schicht vor dem Emitter. Der Emitterpfeil zeigt wie beim npn-Transistor hinaus, nur die Basisspannung wird größer.
:::
:::karte begriff Schaltzeichen
Was ist das Schaltzeichen eines Transistors, und woran erkennt man darin den Emitter?
---
Das Symbol des Transistors im Schaltplan. Der Emitter ist der Anschluss mit dem Pfeil, der die Richtung des technischen Stroms zeigt.
--- falsch
Die Typenbezeichnung auf dem Gehäuse. Der Emitter ist der Anschluss, der in der Bezeichnung als erster genannt wird.
--- falsch
Das Symbol des Transistors im Schaltplan. Der Emitter ist der Anschluss ohne Pfeil; der Pfeil zeigt die Bewegung der Elektronen.
--- falsch
Das Symbol des Transistors im Schaltplan. Der Emitter ist der mittlere Anschluss, weil er zwischen Basis und Kollektor liegt.
:::
:::karte begriff Kollektorstrom, Basisstrom und Emitterstrom
Welche drei Ströme fließen an den Anschlüssen eines npn-Transistors, und wie sind sie gezählt?
---
Der Kollektorstrom $I_\mathrm{C}$ und der viel kleinere Basisstrom $I_\mathrm{B}$ zählen in das Bauteil hinein, der Emitterstrom $I_\mathrm{E}$ heraus. Es gilt immer $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$.
--- falsch
Kollektor- und Emitterstrom zählen hinein, der Basisstrom heraus. Der Basisstrom ist der größte der drei, weil die Basis in der Mitte liegt und beide anderen Ströme aufnimmt.
--- falsch
Alle drei zählen in das Bauteil hinein, weil jeder Anschluss mit der Versorgung verbunden ist. Ihre Summe ist der Strom, den die Versorgung liefert.
--- falsch
Basis- und Emitterstrom zählen hinein, der Kollektorstrom heraus. Er ist genau so groß wie der Emitterstrom, der Basisstrom fließt getrennt über die Basis ab.
:::
:::karte formel Knoten- und Maschenregel am Transistor
Welche zwei Gleichungen gelten am npn-Transistor immer, und woraus folgen sie?
---
$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$ aus der Knotenregel und $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$ aus der Maschenregel. Sie gelten in jedem Betriebszustand.
--- falsch
$I_\mathrm{C}=I_\mathrm{B}+I_\mathrm{E}$ aus der Knotenregel und $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$ aus der Maschenregel. Sie gelten nur, solange der Transistor leitet.
--- falsch
$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$ aus der Knotenregel und $U_\mathrm{CE}=U_\mathrm{CB}-U_\mathrm{BE}$ aus der Maschenregel. Sie gelten in jedem Betriebszustand.
--- falsch
$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$ und $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$, beide aus den Eigenschaften des Halbleiters. Sie gelten nur im Normalbetrieb, solange die CB-Diode sperrt.
:::
:::karte formel Spannungen als Potenzialdifferenzen
Wie sind $U_\mathrm{BE}$, $U_\mathrm{CE}$ und $U_\mathrm{CB}$ am npn-Transistor über die Potenziale der Anschlüsse festgelegt?
---
Als Potenzialdifferenzen, der erste Index ist der Pluspol: $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$.
--- falsch
Als Potenzialdifferenzen, der zweite Index ist der Pluspol: $U_\mathrm{BE}=\varphi_\mathrm{E}-\varphi_\mathrm{B}$, $U_\mathrm{CE}=\varphi_\mathrm{E}-\varphi_\mathrm{C}$, $U_\mathrm{CB}=\varphi_\mathrm{B}-\varphi_\mathrm{C}$.
--- falsch
Als Potenzial des ersten Anschlusses gegen Masse, weil der Emitter immer an Masse liegt: $U_\mathrm{BE}=\varphi_\mathrm{B}$, $U_\mathrm{CE}=\varphi_\mathrm{C}$, $U_\mathrm{CB}=\varphi_\mathrm{C}$.
--- falsch
Als Summen der Potenziale, weil beide Anschlüsse beitragen: $U_\mathrm{BE}=\varphi_\mathrm{B}+\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}+\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}+\varphi_\mathrm{B}$.
:::
:::karte herleitung Wie viele Größen frei sind
Wie folgt aus der Zahl der Anschlüsse, dass der Transistor zwei freie Spannungen hat und durch zwei Gleichungen beschrieben wird?
---
Ein Bauteil mit $n$ Anschlüssen hat $n$ Ströme, von denen nur $n-1$ frei sind, weil es keine Ladung speichert und die Knotenregel einen Strom festlegt.
---
Von den $n$ Potenzialen bleiben $n-1$ Spannungen, weil nur Differenzen zählen.
---
Die Diode ($n=2$) hat deshalb eine Spannung und einen Strom, verknüpft durch eine Kurve, weil ihr Inneres den einen Strom aus der einen Spannung bestimmt.
---
Der Transistor ($n=3$) hat zwei Spannungen und zwei Ströme, verknüpft durch $I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE})$ und $I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE})$, weil jeder freie Strom von beiden Spannungen abhängen kann.
---
Er ist also ein Zweitor, dessen beide Tore sich den Emitter teilen, weil beide Spannungen gegen den Emitter gezählt werden.
:::
:::karte zusammenhang Normalbetrieb an den Potenzialen erkennen
Woran erkennt man bei $\varphi_\mathrm{E}=0$, $\varphi_\mathrm{B}=0{,}6$ V und $\varphi_\mathrm{C}=6$ V, dass die BE-Diode leitet und die CB-Diode sperrt?
---
Die p-Seite der BE-Diode, die Basis, liegt 0,6 V über ihrer n-Seite, dem Emitter: Durchlass. Die n-Seite der CB-Diode, der Kollektor, liegt 5,4 V über der Basis: Sperrrichtung.
--- falsch
Die Basis liegt 0,6 V über dem Emitter, das ist für eine Diode zu wenig, sie sperrt also. Der Kollektor liegt 6 V über dem Emitter, die CB-Diode leitet deshalb.
--- falsch
Die n-Seite der BE-Diode, die Basis, liegt 0,6 V höher: Durchlass. Die p-Seite der CB-Diode, der Kollektor, liegt 5,4 V höher als die Basis, also leiten beide Dioden in Durchlassrichtung.
--- falsch
Beide Dioden haben ihr höheres Potenzial auf der Seite des Kollektors. Leiten kann aber nur die Diode, an der die kleinere Spannung liegt, hier also die BE-Diode.
:::
:::karte zusammenhang Zwei Dioden sind kein Transistor
Warum entsteht kein Transistor, wenn man zwei einzelne Dioden zusammenlötet?
---
In getrennten Dioden rekombiniert jedes Elektron lange vor der zweiten Sperrschicht, und die gesperrte Diode bleibt gesperrt. Der Effekt braucht zwei Grenzen, die enger liegen, als ein Elektron im p-Gebiet überlebt.
--- falsch
Zwei Dioden haben zusammen vier Anschlüsse statt drei. Die Knotenregel liefert dann eine Gleichung zu viel, und die Schaltung hat keinen eindeutigen Arbeitspunkt mehr, an dem sie verstärken könnte.
--- falsch
Die Lötstelle bildet einen Widerstand, der die Stromverstärkung stark verkleinert. Mit sehr kurzen, dicken Drähten entsteht aber ein Transistor, der nur etwas schlechter verstärkt als ein echter aus einem Stück.
--- falsch
Einzelne Dioden sind immer gleich stark dotiert, ein Transistor braucht aber einen stark dotierten Emitter. Mit zwei passend dotierten Einzeldioden würde der Transistoreffekt auftreten.
:::
::::
