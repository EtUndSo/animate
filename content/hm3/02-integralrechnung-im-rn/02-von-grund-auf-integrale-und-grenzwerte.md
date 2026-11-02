---
title: Von Grund auf: Integrale und Grenzwerte
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120200
summary: Alle Beweise dieses Kapitels stützen sich auf wenige Tatsachen über Funktionen einer Variablen und über Mengen.
tags: Riemann-Summe, Integrand, Hauptsatz der Differential- und Integralrechnung, Mittelwertsatz, offen, abgeschlossen, beschränkt, kompakt
lang: de
---

:::zweck
Alle Beweise dieses Kapitels stützen sich auf wenige Tatsachen über Funktionen einer Variablen und über Mengen. Hier stehen sie gesammelt.
:::

**Das Integral als Grenzwert.** Für stetiges $u:[a,b]\to\mathbb{R}$ teilt man $[a,b]$ in $N$ gleiche Stücke der Breite $h=(b-a)/N$ und wählt in jedem Stück eine Stelle $t_k$. Die __Riemann-Summe__ $h\sum_{k=1}^Nu(t_k)$ zählt Rechtecke. Für $N\to\infty$ strebt sie gegen denselben Wert, wie auch immer man die $t_k$ wählt. Dieser Wert ist $\int_a^bu(t)\,\mathrm{d} t$. Die Funktion $u$ unter dem Integralzeichen heißt __Integrand__.

**Hauptsatz und Mittelwertsatz.** Der __Hauptsatz der Differential- und Integralrechnung__ sagt: $\frac{\mathrm{d}}{\mathrm{d} s}\int_a^su(t)\,\mathrm{d} t=u(s)$ und $\int_a^bu'(t)\,\mathrm{d} t=u(b)-u(a)$. Der __Mittelwertsatz__ sagt: Ist $u$ auf $[0,h]$ differenzierbar, gibt es ein $\tau\in[0,h]$ mit $\frac{u(h)-u(0)}{h}=u'(\tau)$. Die mittlere Steigung wird also irgendwo als echte Steigung angenommen.

**Mengen.** Eine Menge $\mathcal U\subset\mathbb{R}^n$ heißt __offen__, wenn um jeden ihrer Punkte eine kleine Kugel in $\mathcal U$ liegt. Sie heißt __abgeschlossen__, wenn sie ihren Rand enthält, und __beschränkt__, wenn sie in eine Kugel mit endlichem Radius passt. Abgeschlossen und beschränkt zusammen heißt __kompakt__. $[a,b]$ ist kompakt, $(a,b)$ und $[a,\infty)$ sind es nicht. Eine __Umgebung__ einer Menge ist eine offene Menge, die sie enthält.

**Gleichmäßige Stetigkeit.** Stetig heißt: Zu jedem $\varepsilon>0$ und jedem Punkt gibt es ein $\delta>0$, so dass sich der Funktionswert um weniger als $\varepsilon$ ändert, wenn man weniger als $\delta$ vom Punkt abrückt. Das $\delta$ darf vom Punkt abhängen. Gibt es ein $\delta$, das für alle Punkte zugleich passt, heißt die Funktion __gleichmäßig stetig__. $u(t)=1/t$ ist auf $(0,1]$ stetig, aber nicht gleichmäßig stetig: Je näher man an 0 kommt, desto kleiner muss $\delta$ sein. Auf kompakten Mengen gibt es dieses Problem nicht: **Jede stetige Funktion auf einer kompakten Menge ist gleichmäßig stetig.**

**Uneigentliche Integrale.** Ein __uneigentliches Integral__ ist als Grenzwert definiert, etwa $\int_a^\infty u(t)\,\mathrm{d} t:=\lim_{T\to\infty}\int_a^Tu(t)\,\mathrm{d} t$, entsprechend bei einer Polstelle am Rand, wo der Integrand unbeschränkt wird. Es heißt __absolut konvergent__, wenn auch $\int|u|\,\mathrm{d} t$ endlich ist. Dazu genügt der Vergleich: Ist $|u|\le v$ und $\int v\,\mathrm{d} t<\infty$, dann konvergiert $\int u\,\mathrm{d} t$ absolut. Für Vergleiche nützlich sind: $\int_1^\infty t^{-p}\,\mathrm{d} t<\infty$ genau für $p>1$, $\int_0^1t^{-p}\,\mathrm{d} t<\infty$ genau für $p<1$, und $\int_0^\infty\mathrm{e}^{-\lambda t}\,\mathrm{d} t=1/\lambda$ für $\lambda>0$. Die Exponentialfunktion gewinnt gegen jede Potenz: $t\mapsto t^k\mathrm{e}^{-\lambda t}$ ist auf $[0,\infty)$ für alle $k\ge0$, $\lambda>0$ beschränkt.
