---
title: Das Wichtigste bis hier
pfad: Informatik / Machine Learning / Ableitung, Gradient und Kettenregel
order: 6231300
summary: Wie eine Zahl auf ihre Eingänge reagiert: von der Tangente bis zum Rückwärtsmodus
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ableitung: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$; nahe bei $x$ ist $f(x+h)\approx f(x)+f'(x)h$, mit einem Fehler, der schneller als $h$ verschwindet. Mit der zweiten Ableitung: $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$.

</li>

<li>

Kettenregel: $(f\circ g)'(x)=f'(g(x))\,g'(x)$; bei langen Ketten das Produkt aller Faktoren. Logistische Funktion: $\sigma'=\sigma(1-\sigma)\le\tfrac14$.

</li>

<li>

Gradient $\nabla f\in\mathbb{R}^d$ als Spalte; $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$, wenn $f$ differenzierbar ist; partielle Ableitungen allein genügen nicht.

</li>

<li>

Richtungsableitung $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$; steilster Anstieg in Richtung $\nabla f$ mit Steigung $\lVert\nabla f\rVert$ (Cauchy-Schwarz); $\nabla f$ steht senkrecht auf den Höhenlinien; $-\nabla f$ zeigt nur bei runden Höhenlinien zum tiefsten Punkt.

</li>

<li>

Jacobi-Matrix $\mathbf J_{\mathbf g}\in\mathbb{R}^{m\times n}$, Zeile je Ausgang: $\mathbf g(\mathbf{x}+\mathbf{h})\approx\mathbf g(\mathbf{x})+\mathbf J_{\mathbf g}\mathbf{h}$; für $\mathbf{A}\mathbf{x}+\mathbf{b}$ ist sie $\mathbf{A}$, für elementweise Funktionen diagonal.

</li>

<li>

Kettenregel: $\mathbf J_{\mathbf f\circ\mathbf g}=\mathbf J_{\mathbf f}\mathbf J_{\mathbf g}$, komponentenweise Summe über alle Wege; $\nabla(f\circ\mathbf g)=\mathbf J_{\mathbf g}^{\top}\nabla f$.

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$, $\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, $\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$, $\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$; rückwärts durch $\mathbf{y}=\mathbf{A}\mathbf{x}$: $\nabla_{\mathbf{A}}=\nabla_{\mathbf{y}}f\,\mathbf{x}^{\top}$, $\nabla_{\mathbf{x}}=\mathbf{A}^{\top}\nabla_{\mathbf{y}}f$.

</li>

<li>

Hesse-Matrix $\mathbf{H}_f$, symmetrisch nach Schwarz; $f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$; Krümmung in Richtung $\mathbf{u}$ ist $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$, zwischen kleinstem und größtem Eigenwert.

</li>

<li>

Rechengraph: Grundoperationen, Vorwärtsrechnung mit gespeicherten Werten, lokale Ableitungen an den Kanten.

</li>

<li>

Vorwärtsmodus: Tangentenwerte, ein Durchlauf je Richtung ($\mathbf J\dot{\mathbf{x}}$). Rückwärtsmodus: Adjungierte $\bar a=\sum\bar b\,\partial b/\partial a$ ab $\bar f=1$, ein Durchlauf für den ganzen Gradienten, Aufwand ein kleines Vielfaches einer Auswertung, Preis: Speicher.

</li>

<li>

Numerisch: Vorwärtsdifferenz Fehler $\approx\tfrac12f''h$, zentrale Differenz $\approx\tfrac16f'''h^2$; Rundung wächst wie $\varepsilon_{\mathrm M}/h$, daher die V-Kurve; Gradientenprüfung mit relativem Fehler, über $10^{-2}$ falsch, unter $10^{-7}$ gut.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Wie eine Zahl auf kleine Änderungen ihrer Eingänge reagiert, sagt ihre lineare Näherung: Jeder Eingang trägt seine partielle Ableitung mal seiner Änderung bei, und die Beiträge addieren sich zum Skalarprodukt mit dem Gradienten.

</li>

<li>

Nach der Cauchy-Schwarz-Ungleichung ist dieses Skalarprodukt bei Schritten fester Länge am größten in Richtung des Gradienten, der deshalb am steilsten bergauf zeigt und senkrecht auf den Höhenlinien steht.

</li>

<li>

Entsteht die Zahl durch eine lange Kette von Rechenschritten, so ist ihre Ableitung ein Produkt von Jacobi-Matrizen, also eine Summe über alle Wege, und der Rückwärtsmodus berechnet dieses Produkt von der Zahl aus mit Zeilenvektoren, sodass er alle Ableitungen auf einmal für ein kleines Vielfaches des Aufwands einer einzigen Auswertung liefert.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Prinzip: Nahe genug an einer Stelle ist jede differenzierbare Funktion linear. Ableitung, Gradient und Jacobi-Matrix sind diese lineare Näherung, die Kettenregel schaltet lineare Näherungen hintereinander und multipliziert dabei ihre Matrizen, und Vorwärts- und Rückwärtsmodus sind zwei Arten, dieses Produkt zu klammern.

| Ergebnis | Woher es kommt |
|---|---|
| Ableitung und Tangente | die einzige Gerade, deren Fehler schneller als $h$ verschwindet (Abschnitt [1](die-ableitung.html#stufe-1)) |
| Produktregel | das Eckstück $\Delta u\,\Delta v$ ist klein von zweiter Ordnung (Abschnitt [1.4](die-ableitung.html#stufe-1-4)) |
| Kettenregel einer Variablen | jede Stufe gibt kleine Änderungen mit ihrem Faktor weiter (Abschnitt [2](die-kettenregel.html#stufe-2)) |
| Gradient und Tangentialebene | die Wirkungen kleiner Änderungen addieren sich (Abschnitt [3](partielle-ableitungen-und-der-gradient.html#stufe-3)) |
| Steilster Anstieg | Cauchy-Schwarz für $\nabla f^{\top}\mathbf{u}$ (Abschnitt [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)) |
| Gradient senkrecht zur Höhenlinie | entlang der Höhenlinie ist die Steigung null (Abschnitte [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) und [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Jacobi-Matrix | die Matrix der linearen Näherung einer vektorwertigen Funktion (Abschnitt [5](die-jacobi-matrix.html#stufe-5)) |
| Kettenregel als Matrixprodukt, Summe über Wege | hintereinandergeschaltete lineare Näherungen (Abschnitt [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Matrixidentitäten, Rückwärtsregel | Kettenregel komponentenweise, in fester Layout-Konvention (Abschnitt [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)) |
| Hesse-Matrix und Krümmung | zweite Ableitung entlang einer Geraden, Eigenwerte einer quadratischen Form (Abschnitt [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8)) |
| Rückwärtsmodus | Wege nach ihrer ersten Kante gruppieren, Zwischensummen wiederverwenden; Klammerung von links (Abschnitte [9](rechengraphen.html#stufe-9) und [10](automatische-differentiation.html#stufe-10)) |
| Zentrale Differenz, V-Kurve | gerade Taylorglieder heben sich auf; Rundungsfehler wachsen wie $1/h$ (Abschnitt [11](numerische-ableitung-und-gradientenprufung.html#stufe-11)) |
