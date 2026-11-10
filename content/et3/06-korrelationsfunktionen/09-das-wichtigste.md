---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260900
summary: Wie ähnlich sind zwei Signale, und wie verteilt sich die Energie über die Frequenz?
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Ähnlichkeit zweier Signale misst man am Integral ihres Produkts. Die Korrelationsfunktion tut das für jede Verschiebung $\tau$, sie ist eine Faltung mit dem gespiegelten Signal.

</li>

<li>

Die Fourier-Transformierte der Autokorrelationsfunktion ist das Energiedichtespektrum $|S(f)|^2$. Bei $\tau=0$ steht die Energie (Parseval).

</li>

<li>

Durch ein LTI-System werden Energiedichtespektren mit $|H(f)|^2$ multipliziert und Autokorrelationsfunktionen mit der Autokorrelationsfunktion von $h$ gefaltet.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: orthogonal.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

AKF: gerade (reell), Maximum $\varphi^E_{ss}(0)=E_s$, doppelte Dauer.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener-Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Bandpass: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Diskret: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periodisch: $S_d^*G_d$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Korrelation ist Faltung mit einem gespiegelten Signal. Deshalb gelten alle Werkzeuge der Faltung:

| Ergebnis | Woher es kommt |
|---|---|
| Korrelationskoeffizient | Energie der Differenz zweier normierter Signale (Stufe [2](ahnlichkeit-messen-der-korrelationskoeffizient.html#stufe-2)) |
| Korrelationsprodukt | Faltung mit dem gespiegelten, konjugierten Signal (Stufe [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| AKF gerade, Maximum bei 0 | Spiegeln, und am ähnlichsten ist ein Signal sich selbst (Stufe [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| Energiedichtespektrum, Parseval | Spiegeln und Konjugieren wird $S^*$, Faltung wird Produkt (Stufe [4](energiedichtespektrum.html#stufe-4)) |
| Wiener-Lee | Assoziativgesetz der Faltung (Stufe [5](korrelation-und-lti-systeme.html#stufe-5)) |
| zeitdiskret, periodisch, DFT | dieselbe Rechnung mit Summen (Stufe [7](zeitdiskrete-und-periodische-korrelation.html#stufe-7)) |
