---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3211200
summary: Warum die Antwort auf einen einzigen Stoß das ganze System beschreibt
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Jedes Signal ist eine Überlagerung unendlich vieler kurzer Stöße: an jeder Stelle $\tau$ ein Stoß mit dem Gewicht $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

Ein LTI-System antwortet auf einen verschobenen Stoß mit der verschobenen Impulsantwort $h(t-\tau)$ (Zeitinvarianz) und auf eine Summe von Stößen mit der Summe der Antworten (Linearität).

</li>

<li>

Deshalb ist der Ausgang die Faltung $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, und $h(t)$ beschreibt das System vollständig.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Verschieben $t\to t-t_0$ verzögert, Dehnen $t\to t/T$ verbreitert; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: Mitte $t_0$, Dauer $|T|$, Höhe $a$.

</li>

<li>

RC-Tiefpass: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; Sprungantwort $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: Überlagerungssatz und $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ und $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Rechnen: spiegeln, schieben, multiplizieren, integrieren.

</li>

<li>

$s*\delta=s$; kommutativ, assoziativ (Kette: $h_1*h_2$), distributiv (parallel: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Sprungantwort $=\int h$, Impulsantwort $=\frac{\mathrm{d}}{\mathrm{d} t}$Sprungantwort.

</li>

<li>

Kausal: $h(t)=0$ für $t<0$. Stabil: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**Wie es weitergeht.** Die Faltung ist aufwendig: Für jeden Zeitpunkt $t$ steht dort ein eigenes Integral. Der nächste Teil zerlegt Signale so, dass aus dem Integral eine einfache Multiplikation wird.

**Ein Prinzip hinter allen Ergebnissen.** Die Tabelle ordnet die Ergebnisse dieses Kapitels dem Prinzip „zerlegen, Baustein durchschicken, zusammensetzen“ zu.

| Ergebnis | Woher es kommt |
|---|---|
| Faltungsintegral | Stöße überlagern, verschobene Impulsantworten überlagern (Stufe [4](das-faltungsintegral.html#stufe-4)) |
| Spiegeln beim Ausrechnen | $h(t-\tau)$ ist die Antwort auf einen Stoß, der vor $t-\tau$ Sekunden kam (Stufe [5](die-faltung-ausrechnen.html#stufe-5)) |
| $\delta$ ist das Einselement | ein Signal aus Stößen, durch ein System, das jeden Stoß unverändert lässt (Stufe [6](rechenregeln-der-faltung.html#stufe-6)) |
| Kommutativ-, Assoziativ-, Distributivgesetz | Rollen tauschen, Systeme in Kette, Systeme parallel (Stufe [6](rechenregeln-der-faltung.html#stufe-6)) |
| Siebeigenschaft, Dehnung des Dirac-Impulses | $\delta$ ist nur über seine Fläche definiert (Stufe [7](der-dirac-impuls.html#stufe-7)) |
| Sprungantwort = Integral der Impulsantwort | ein Sprung ist die Summe aller Stöße bis $t$ (Stufe [8](integrieren-und-differenzieren.html#stufe-8)) |
| Kausalität, Stabilität | Bedingungen an $h(t)$: null vor dem Stoß, endliche Fläche von $\vert h\vert $ (Stufe [9](kausal-und-stabil.html#stufe-9)) |
| Faltung ohne System | dieselbe Überlagerung, zum Beispiel bei der Augensumme zweier Würfel (Stufe [10](faltung-ganz-ohne-system.html#stufe-10)) |
