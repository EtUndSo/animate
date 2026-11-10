---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271400
summary: Mittelwerte, Verteilungen, Leistungsdichte, Rauschen in Systemen und der optimale Empfänger
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Zufallssignal beschreibt man durch Mittelwerte: Mittelwert, Leistung, Varianz, Autokorrelationsfunktion und Verteilungsdichte. Bei ergodischen Prozessen darf man sie aus einem einzigen, langen Signal bestimmen.

</li>

<li>

Die Fourier-Transformierte der Autokorrelationsfunktion ist das Leistungsdichtespektrum. Ein LTI-System multipliziert es mit $|H(f)|^2$, genau wie bei Energiesignalen ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Gegen weißes Rauschen ist das Korrelationsfilter $h(t)=s(T-t)$ optimal. Es erreicht das Signal-Rausch-Verhältnis $E_s/N_0$, unabhängig von der Signalform.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Scharmittel $\mathrm E\{\cdot\}$; stationär: verschiebungsunabhängig; ergodisch: Zeitmittel $=$ Scharmittel.

</li>

<li>

$m_s$ (Gleichanteil), $L_s=\mathrm E\{s^2\}$ (Leistung), $\sigma_s^2=L_s-m_s^2$ (Wechselleistung).

</li>

<li>

AKF: $\varphi_{ss}(0)=L_s$, gerade, Maximum bei 0; Kovarianz $\mu=\varphi-m^2$; Summe: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; Gleichverteilung $\sigma^2=a^2/12$.

</li>

<li>

Kennlinie: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; Quantisierungsfehler $\Delta^2/12$, 6 dB je Bit.

</li>

<li>

Unabhängig $\Rightarrow$ unkorreliert; Summe unabhängiger: $p_s=p_f*p_g$; Gauß: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

Weiß: $\Phi=N_0$, $\varphi=N_0\delta$; thermisch $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Matched Filter: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Man ersetzt das unbekannte Signal durch seine Mittelwerte, und für Mittelwerte gilt Linearität:

| Ergebnis | Woher es kommt |
|---|---|
| Mittelwert, Leistung, Varianz | Scharmittel und Zeitmittel (Stufen [1](der-zufallsprozess.html#stufe-1)–[3](mittelwert-leistung-varianz.html#stufe-3)) |
| AKF, Kovarianz, KKF | Mittel über Produkte zweier Zeitpunkte (Stufe [4](autokorrelation-kovarianz-und-kreuzkorrelation.html#stufe-4)) |
| Verteilungsdichte | Anteil der Zeit oder der Schar unter einer Schwelle (Stufe [5](verteilungsfunktion-und-verteilungsdichte.html#stufe-5)) |
| Summe unabhängiger Größen | Faltung der Dichten, daher Gauß (Stufen [6](verbundverteilung-unabhangigkeit-unkorreliertheit.html#stufe-6), [7](die-gau-verteilung.html#stufe-7)) |
| Leistungsdichte, Wiener-Lee | Linearität des Mittelwerts im Faltungsintegral (Stufe [8](zufallssignale-in-lti-systemen-leistungsdichte.html#stufe-8)) |
| weißes Rauschen | konstante Leistungsdichte, AKF $=N_0\delta$ (Stufe [9](weies-rauschen-und-thermisches-rauschen.html#stufe-9)) |
| Korrelationsfilter | Cauchy-Schwarz: Am größten ist die Korrelation mit sich selbst (Stufe [10](das-korrelationsfilter-matched-filter.html#stufe-10)) |
| Fehlerwahrscheinlichkeit | Fläche unter einer Gaußkurve jenseits der Schwelle (Stufe [11](fehlerwahrscheinlichkeit-beim-binarempfang.html#stufe-11)) |
