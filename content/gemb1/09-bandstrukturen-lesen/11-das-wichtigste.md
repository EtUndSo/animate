---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Bandstrukturen lesen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen
knoten: Kapitel 9: Bandstrukturen lesen
order: 4191100
summary: Was Graphen, Silizium und GaAs unterscheidet und was eine Kurve über Leitung, Licht und Masse verrät
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**2D:** $E=E_\mathrm s-2V_\mathrm{ss}\cos(k_xa)-2V_\mathrm{ss}\cos(k_ya)$, gezeichnet längs eines Wegs durch Hochsymmetriepunkte.

</li>

<li>

⁠**Graphen:** zwei Atome je Zelle, $E_\pm=E_\mathrm p\pm V_{\mathrm{pp}\pi}|1+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_1}+\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol a_2}|$. Lineare Berührung an den Dirac-Punkten, $E_\mathrm g=0$.

</li>

<li>

⁠**Silizium:** acht Elektronen je Zelle, vier volle Bänder. Valenzband bei $\Gamma$ 2-fach, Leitungsband nahe $X$ 6-fach entartet, $E_\mathrm g=1{,}12$ eV indirekt.

</li>

<li>

⁠**GaAs:** $E_\mathrm g=1{,}42$ eV direkt bei $\Gamma$. Direkt leuchtet gut, indirekt braucht ein Phonon.

</li>

<li>

⁠**Masse:** $F=\hbar\,\mathrm{d} k/\mathrm{d} t$ und $v=\hbar^{-1}\partial E/\partial k$ ergeben $m^*=(\hbar^{-2}\partial^2E/\partial k^2)^{-1}$. Oben im Band ist sie negativ. Silizium: $m_\mathrm h^*=0{,}92\,m_0$, $m_\mathrm l^*=0{,}19\,m_0$.

</li>

<li>

⁠**Loch:** leerer Zustand im vollen Band, Ladung $+e$, Masse $m_\mathrm V^*>0$, $k_\mathrm h=-k_\mathrm e$.

</li>

<li>

⁠**Ablesen:** Band schneidet $E_\mathrm F$: Metall. Lücke an $E_\mathrm F$: Halbleiter oder Isolator.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Das Rezept aus [Kapitel 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) ergibt auch für echte Kristalle Bänder, ihre Zahl folgt aus den Orbitalen der Zelle, ihre Füllung aus den Elektronen der Zelle.

</li>

<li>

Die Lage der Kanten sagt, ob ein Stoff leitet und ob er leuchtet: Eine Lücke an $E_\mathrm F$ trennt Halbleiter und Isolator vom Metall, Kanten über demselben $\boldsymbol k$ erlauben den Sprung mit Licht allein.

</li>

<li>

Die Krümmung an den Kanten sagt, wie Ladungsträger auf Kräfte antworten: Sie bestimmt die effektive Masse von Elektronen und Löchern.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Eine Bandstruktur ist $E(\boldsymbol k)$ plus Besetzung. Fast alles in diesem Kapitel folgt aus zwei Blicken darauf: wie die Kurve aussieht und bis wohin sie gefüllt ist.

| Ergebnis | Woher es kommt |
|---|---|
| Breite $8V_\mathrm{ss}$ im Quadratgitter | Vier Nachbarn, jede Richtung ein Kosinus (Stufe [1](das-band-in-der-ebene.html#stufe-1)) |
| Dirac-Punkte in Graphen | Drei Hüpfwege löschen sich aus (Stufe [2](graphen.html#stufe-2)) |
| Vier volle Bänder, sechs Täler | Acht Elektronen, sechs Richtungen des Würfels (Stufe [3](silizium.html#stufe-3)) |
| Direkt leuchtet, indirekt kaum | Das Photon liefert Energie, aber kein $k$ (Stufe [4](gaas-direkte-und-indirekte-lucke.html#stufe-4)) |
| $m^*$ aus der Krümmung | Äußere Kraft ändert $k$, Steigung ergibt $v$ (Stufe [5](die-effektive-masse-im-kristall.html#stufe-5)) |
| Zwei Massen in Silizium | Ein Tal ist längs flach, quer steil (Stufe [6](masse-und-richtung.html#stufe-6)) |
| Loch mit $+e$ und $m^*>0$ | Volles Band minus ein Elektron (Stufe [7](das-loch.html#stufe-7)) |
| Metall, Halbleiter, Isolator | Ein Feld braucht freie Zustände in Reichweite (Stufe [8](was-man-an-einer-bandstruktur-abliest.html#stufe-8)) |
