---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Strom im Halbleiter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter
knoten: Kapitel 12: Strom im Halbleiter
order: 4221100
summary: Wie aus einer verschobenen Besetzung ein Strom wird und was ihn bremst
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Strom:** $j=-\frac eL\sum_kv(k)f(k)$. Gleichgewicht und volle Bänder geben $j=0$. Eine Kraft verschiebt die Besetzung, $k(t)=k(0)+Ft/\hbar$.

</li>

<li>

⁠**Streuung:** an Phononen, Störstellen, Defekten, Elektronen. Raten addieren sich: $1/\tau_\text{scat}=\sum_i1/\tau_i$. Ohne Stöße: Bloch-Schwingung.

</li>

<li>

⁠**Transportgleichung:** $\partial_tf+v\,\partial_xf+(F/\hbar)\,\partial_kf=\partial_tf|_\text{coll.}\approx-(f-f^0)/\tau$. Gleichgewicht verlangt $\mathrm{d} E_\mathrm F/\mathrm{d} x=0$ und $\mathrm{d} T/\mathrm{d} x=0$.

</li>

<li>

⁠**Stationär, homogen:** $\delta k=-e\mathcal E\tau_\text{scat}/\hbar$, $\mu=e\tau_\text{scat}/m^*$, $j=e\,n\,\mu\,\mathcal E$.

</li>

<li>

⁠**Temperatur:** $\mu_\mathrm{ph}\propto T^{-3/2}$, $\mu_\mathrm{ion}\propto T^{+3/2}$, allgemein $\mu\propto T^{-\beta}$. Leitfähigkeit: $\sigma=e(n\mu_\mathrm n+p\mu_\mathrm p)$, $\rho=1/\sigma$.

</li>

<li>

⁠**Hall:** $U_\mathrm H=R_\mathrm HIB/d$, $R_\mathrm H=-1/(ne)$ oder $+1/(pe)$, $\tan\Theta_\mathrm H=-\mu_\mathrm nB$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Strom entsteht durch eine Schieflage der Besetzung im $k$-Raum, die eine Kraft aufbaut und Stöße abbauen.

</li>

<li>

Die Boltzmann-Transportgleichung beschreibt dieses Wechselspiel, und im stationären Fall ergibt sie die verschobene Verteilung mit $\mu=e\tau_\text{scat}/m^*$.

</li>

<li>

Temperatur und Dotierung wirken über Streuzeit und Dichte, die Leitfähigkeit ist $\sigma=e(n\mu_\mathrm n+p\mu_\mathrm p)$, und der Hall-Effekt trennt $n$ und $\mu$.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Eine Kraft baut eine Abweichung vom Gleichgewicht auf, Stöße bauen sie ab. Fast alles hier ist die Frage, wie groß die Abweichung ist, bei der sich beide die Waage halten.

| Ergebnis | Woher es kommt |
|---|---|
| Bloch-Schwingung, Matthiessen | Ohne Stöße läuft $k$ durch die Zone, Raten addieren sich (Stufe [2](ohne-stoe-kein-gleichstrom.html#stufe-2)) |
| Boltzmann-Gleichung | Besetzung bleibt auf der Bahn, Stöße versetzen sie (Stufe [3](vom-wellenpaket-zur-verteilungsfunktion.html#stufe-3) und [5](der-streuterm-und-die-relaxationszeit.html#stufe-5)) |
| $\mathrm{d} E_\mathrm F/\mathrm{d} x=0$ | Die Bandkante hebt sich gegen die Kraft weg (Stufe [4](was-das-gleichgewicht-verlangt.html#stufe-4)) |
| $\mu=e\tau_\text{scat}/m^*$ | Schub $F/\hbar$ gegen Abbau $1/\tau_\text{scat}$ (Stufe [6](der-stationare-strom.html#stufe-6)) |
| $\mu(T)$ mit Maximum | Zwei Streuraten mit entgegengesetztem Gang (Stufe [7](beweglichkeit-und-leitfahigkeit.html#stufe-7)) |
| Vorzeichen von $U_\mathrm H$ | Gleicher Rand, verschiedene Ladung (Stufe [8](erganzung-der-hall-effekt.html#stufe-8)) |
