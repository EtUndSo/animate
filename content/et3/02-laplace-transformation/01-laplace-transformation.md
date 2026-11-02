---
title: Überblick: Die Laplace-Transformation
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220100
summary: Jedes Signal als Überlagerung von $\ee^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: 
lang: de
---

## Worum es geht

:::frage Ich habe die Rechnung verstanden, wie man vom Faltungsintegral mit einer Eigenfunktion auf $H(p)$ kommt. Ich glaube aber, dass hinter der Laplace-Transformation viel mehr steckt als diese Rechenvorschrift: dass jede beliebige Funktion als Summe komplexer e-Funktionen dargestellt werden kann.
Die Vermutung trifft den Kern. Ohne sie wäre die Eigenfunktions-Rechnung nur eine Kuriosität, denn sie gilt zunächst nur für das eine Signal $\mathrm{e}^{pt}$. Erst weil sich (fast) jedes Signal aus solchen Bausteinen zusammensetzen lässt, folgt aus ihr eine Aussage über *jedes* Eingangssignal. Drei Präzisierungen machen die Vermutung exakt:

<ol>

<li>

Im Allgemeinen ist es keine Summe, sondern ein *Integral*: unendlich viele Bausteine $\mathrm{e}^{pt}$, jeder mit einem infinitesimalen Gewicht. Die Bausteine liegen auf einer senkrechten Linie $\operatorname{Re} p=\sigma$ der $p$-Ebene (Stufe [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)).

</li>

<li>

Nicht jede Funktion, sondern jede, für die ein Konvergenzbereich existiert: Sie darf auf jeder Seite der Zeitachse höchstens exponentiell wachsen, und eine einzige Dämpfung muss beide Seiten zugleich bändigen (Abschnitt [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)).

</li>

<li>

Ist $S(p)$ ein Bruch aus Polynomen, wird aus dem Integral tatsächlich eine *endliche Summe* $\sum_r A_r\,\mathrm{e}^{p_r t}$. Die Exponenten $p_r$ sind die Pole von $S(p)$ (Stufe [4](aus-dem-integral-wird-eine-summe.html#stufe-4)).

</li>

</ol>
:::



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
