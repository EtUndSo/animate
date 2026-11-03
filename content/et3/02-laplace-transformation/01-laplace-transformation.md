---
title: Überblick: Die Laplace-Transformation
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220100
summary: Jedes Signal als Überlagerung von $\mathrm{e}^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: 
lang: de
---

## Worum es geht



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
Alle Beispiele benutzen dieselben zwei Bausteine:

<ul>

<li>

einen **RC-Tiefpass** mit $RC=1$ s (zum Beispiel $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Seine Impulsantwort und seine Übertragungsfunktion sind

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

mit $t$ in s und $p$ in $1/\mathrm{s}$;

</li>

<li>

den **Einheitssprung** $s(t)=\varepsilon(t)$ mit $S(p)=1/p$ für $\operatorname{Re} p>0$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap2.py` nach.
:::
