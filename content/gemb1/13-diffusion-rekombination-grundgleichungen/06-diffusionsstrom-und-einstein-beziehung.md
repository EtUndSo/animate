---
title: Stufe 4: Diffusionsstrom und Einstein-Beziehung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230600
summary: Elektronen und Löcher sind geladen, ihre Diffusion ist also ein elektrischer Strom.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Elektronen und Löcher sind geladen, ihre Diffusion ist also ein elektrischer Strom. Diese Stufe leitet ihn aus den Stößen her und zeigt, warum Diffusion und Beweglichkeit nicht unabhängig sind.
:::

**Die Idee.** Im Feld gewinnt ein Träger bis zum nächsten Stoß eine kleine Zusatzgeschwindigkeit, die Beweglichkeit misst sie. In der Diffusion trägt ihn seine Wärmebewegung bis zum nächsten Stoß. In beiden Fällen begrenzt derselbe Stoß den Weg. Der Unterschied ist nur die Geschwindigkeit, und die legt die Wärmeenergie $k_\mathrm BT$ fest.

:::satz Satz 4.1 (Diffusionsstrom und Einstein-Beziehung)
<span class="anker" id="satz-4-1"></span>

Für Elektronen (Ladung $-e$) und Löcher (Ladung $+e$) gilt

<span class="anker" id="gl-4-1"></span>
$$j_{\mathrm n,\text{diff}}=+e\,D_\mathrm n\frac{\partial n}{\partial x},\quad j_{\mathrm p,\text{diff}}=-e\,D_\mathrm p\frac{\partial p}{\partial x},\qquad D_\mathrm n=\frac{k_\mathrm BT}e\,\mu_\mathrm n,\quad D_\mathrm p=\frac{k_\mathrm BT}e\,\mu_\mathrm p. \tag{4.1}$$
:::

⁠**So liest man das:** $k_\mathrm BT/e$ ist eine Spannung, 25,85 mV bei 300 K. Damit hat $D_\mathrm n$ die Einheit $\mathrm V\cdot\mathrm{cm^2/(V\,s)}=\mathrm{cm^2/s}$. Für Teilchen der Ladung $z_ie$ lautet die Beziehung $D_i=k_\mathrm BT\,\mu_i/(|z_i|\,e)$. Abb. [4](#abb-4) zeigt die Vorzeichen. **Gültigkeit:** konstante Temperatur, Boltzmann-Näherung der Besetzung ([Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html)), also kein entartetes Band.

:::abbildung gemb1/k13vorzeichen 4
Teilchenstrom und elektrischer Strom in den vier Fällen. Drift: Das Feld treibt beide Sorten in entgegengesetzte Richtungen, die Ströme addieren sich. Diffusion: Beide Sorten laufen in dieselbe Richtung, ihre Ströme sind entgegengesetzt.
:::

:::herleitung Aus den Stößen: das erste Moment ohne Feld
Stationär und ohne Feld bleibt von [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) nur $v\,\partial f/\partial x=-(f-f^0)/\tau_\text{scat}$. Multipliziere mit $v$ und summiere über alle Zustände je Länge (erstes Moment wie in [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html), wegen $k=m^*v/\hbar$ gleichwertig zum Faktor $k$):

$$\tau_\text{scat}\,\frac{\partial}{\partial x}\,\frac1L\sum_kv^2f=-\frac1L\sum_kv\,f+\frac1L\sum_kv\,f^0.$$

Die letzte Summe ist null, weil $f^0$ in $k$ symmetrisch ist. Links steht $\tau_\text{scat}\,\partial(n\langle v^2\rangle)/\partial x$, rechts bleibt $-\mathcal J_\mathrm n$. Je Richtung gehört zur Wärmebewegung die Energie $\frac12m^*\langle v^2\rangle=\frac12k_\mathrm BT$. Also

$$\mathcal J_\mathrm n=-\tau_\text{scat}\,\frac{k_\mathrm BT}{m^*}\,\frac{\partial n}{\partial x}=-D_\mathrm n\frac{\partial n}{\partial x},\qquad D_\mathrm n=\frac{e\tau_\text{scat}}{m^*}\,\frac{k_\mathrm BT}e=\mu_\mathrm n\frac{k_\mathrm BT}e.$$

Das ist $D=v^2\tau_\text{scat}$ aus Stufe [1](warum-teilchen-ohne-kraft-stromen.html#stufe-1) mit $v^2=k_\mathrm BT/m^*$. Die elektrische Stromdichte ist $j_\mathrm n=-e\mathcal J_\mathrm n$.
:::

:::herleitung Aus dem Gleichgewicht
Der Gesamtstrom $j_\mathrm n=e\,n\,\mu_\mathrm n\mathcal E+e\,D_\mathrm n\,\mathrm{d} n/\mathrm{d} x$ muss im Gleichgewicht null sein, und dort ist $e\mathcal E=-(k_\mathrm BT/n)\,\mathrm{d} n/\mathrm{d} x$. Einsetzen ergibt $-\mu_\mathrm nk_\mathrm BT\,\mathrm{d} n/\mathrm{d} x+e\,D_\mathrm n\,\mathrm{d} n/\mathrm{d} x=0$, also $D_\mathrm n=\mu_\mathrm nk_\mathrm BT/e$. Bei jedem anderen Verhältnis flösse im Gleichgewicht Strom.
:::

**Beispiel.** In der Probe ist $D_\mathrm n=31\,\mathrm{cm^2/s}$ und $D_\mathrm p=10{,}8\,\mathrm{cm^2/s}$. Fällt $n=10^{16}\,\mathrm{cm^{-3}}$ auf 10 µ m um den Faktor $\mathrm{e}$, ist $|j_{\mathrm n,\text{diff}}|=50\,\mathrm{A/cm^2}$. Denselben Strom treiben 25,85 mV über 10 µ m. **Kurz gesagt:** Ein Dichtegefälle, das $n$ auf einer Strecke um den Faktor $\mathrm{e}$ ändert, wirkt wie die Spannung $k_\mathrm BT/e$ über dieser Strecke. **Grenzfälle:** Für $T\to0$ ist $D_\mathrm n\to0$, die Wärmebewegung fehlt. Für $\tau_\text{scat}\to0$ verschwinden $\mu_\mathrm n$ und $D_\mathrm n$ gemeinsam.

:::frage Beim Elektronenstrom steht ein Plus. Läuft Diffusion nicht immer zur kleineren Dichte?
Doch, die Teilchen tun das: $\mathcal J_\mathrm n=-D_\mathrm n\,\partial n/\partial x$. Das Plus gehört zum elektrischen Strom. Elektronen tragen die Ladung $-e$, die Stromrichtung ist also der Laufrichtung entgegengesetzt.
:::

:::aufgabe Aufgabe 5 ★★ Einstein anwenden
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Wie groß ist $D_\mathrm n$ für $\mu_\mathrm n=6000\,\mathrm{cm^2/(V\,s)}$ bei 300 K?

</li>

<li>

Für $\mu_\mathrm n\propto T^{-3/2}$: Um welchen Faktor ändern sich $\mu_\mathrm n$ und $D_\mathrm n$ von 300 K nach 400 K? Warum sinkt $D_\mathrm n$ schwächer?

</li>

<li>

In einer Probe fällt $N_\mathrm D(x)=N_1\mathrm{e}^{-x/b}$ mit $b=2$ µ m, es fließt kein Strom, $n\approx N_\mathrm D$. Bestimme $\mathcal E$ nach Betrag und Richtung und die Spannung zwischen zwei Punkten im Abstand 10 µ m. Wie groß ist dort das Dichteverhältnis?

</li>

</ol>

:::loesung
(a) $D_\mathrm n=25{,}85\,\mathrm{mV}\cdot\mu_\mathrm n=155\,\mathrm{cm^2/s}$. (b) $\mu_\mathrm n$ sinkt auf das 0,65-fache, $D_\mathrm n\propto T\,T^{-3/2}=T^{-1/2}$ nur auf das 0,87-fache: Mehr Wärme macht die Träger schneller. (c) $j_\mathrm n=0$ mit $\mathrm{d} n/\mathrm{d} x=-n/b$ gibt $\mathcal E=(k_\mathrm BT/e)/b=12{,}9$ kV/m in $+x$-Richtung: Die Elektronen diffundieren nach rechts, die Kraft $-e\mathcal E$ schiebt sie zurück. Über 10 µ m sind das 129 mV, Dichteverhältnis $\mathrm{e}^5=148$.
:::
:::
