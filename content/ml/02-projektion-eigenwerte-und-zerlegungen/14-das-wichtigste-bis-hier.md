---
title: Das Wichtigste bis hier
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6221400
summary: Nächste Punkte, natürliche Richtungen und die Bausteine einer Matrix
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Orthonormale Vektoren: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$; Koordinaten sind Skalarprodukte $c_i=\mathbf{q}_i^{\top}\mathbf{x}$; orthogonale Matrizen erhalten Längen und Winkel. Bei nicht quadratischem $\mathbf{Q}$ ist $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.

</li>

<li>

Projektion auf eine Gerade: $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$; der Rest steht senkrecht auf $\mathbf{a}$, und $\hat{\mathbf{y}}$ ist der nächste Punkt. Projektionsmatrizen erfüllen $\mathbf{P}^2=\mathbf{P}$, orthogonale zusätzlich $\mathbf{P}^{\top}=\mathbf{P}$.

</li>

<li>

Beste Näherungslösung: Das Residuum $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ steht senkrecht auf dem Spaltenraum, also $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$; eindeutig genau bei unabhängigen Spalten.

</li>

<li>

Projektion auf einen Unterraum: $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$; Gram-Schmidt liefert $\mathbf{A}=\mathbf{Q}\mathbf{R}$, und $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$.

</li>

<li>

Quadratische Formen $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ hängen nur vom symmetrischen Anteil ab; Schüssel, Rinne, Sattel erkennt man durch quadratisches Ergänzen.

</li>

<li>

Eigenwerte: $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, $\det(\mathbf{A}-\lambda\mathbf{I})=0$; Spur $=\sum\lambda_i$, $\det=\prod\lambda_i$; Drehungen haben komplexe Eigenwerte.

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ entkoppelt, $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$. Symmetrisch: $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ mit reellen $\lambda_i$ und senkrechten Hauptachsen, Halbachsen $1/\sqrt{\lambda_i}$.

</li>

<li>

Positiv definit $\Leftrightarrow$ alle Eigenwerte $>0$ $\Leftrightarrow$ alle Pivots $>0$ $\Leftrightarrow$ alle führenden Hauptminoren $>0$; $\mathbf{A}^{\top}\mathbf{A}$ ist positiv semidefinit; Cholesky $\mathbf{A}=\mathbf L\mathbf L^{\top}$.

</li>

<li>

Singulärwertzerlegung $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$ für jede Matrix: drehen, strecken, drehen; $d_j^2$ sind die Eigenwerte von $\mathbf{A}^{\top}\mathbf{A}$, $\lVert\mathbf{A}\rVert_2=d_1$.

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$; $\mathbf{A}_k$ ist die beste Näherung vom Rang $k$, mit dem Fehler $d_{k+1}$ in der Spektralnorm.

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ liefert die kürzeste beste Näherungslösung; Spezialfälle $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ und $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$.

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ begrenzt die Verstärkung relativer Fehler; $1/\kappa$ ist der relative Abstand zur Singularität; $\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Gleichungssystem ohne Lösung löst man am besten, indem man die rechte Seite senkrecht auf den Spaltenraum projiziert: Das Residuum steht dann senkrecht auf allen Spalten, daraus folgen die Normalgleichungen, und nach Pythagoras liegt kein anderer Punkt näher.

</li>

<li>

Eigenvektoren sind die Richtungen, die eine Matrix nur streckt; in ihrer Basis wird die Matrix diagonal, und bei symmetrischen Matrizen bilden sie ein rechtwinkliges Achsenkreuz, an dem man die Form jeder quadratischen Form abliest.

</li>

<li>

Jede Matrix ist eine nach Größe geordnete Summe von Bausteinen $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ vom Rang $1$: Die ersten $k$ ergeben die beste Näherung vom Rang $k$, und das Verhältnis $d_1/d_n$ sagt, wie stark Fehler in den Daten die Lösung verfälschen können.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Prinzip: In einem rechtwinkligen Achsenkreuz zerfällt ein Längenquadrat nach Pythagoras in unabhängige Anteile, und der kürzeste Weg zu einer Geraden, Ebene oder einem Unterraum ist der senkrechte.

| Ergebnis | Woher es kommt |
|---|---|
| Koordinaten als Skalarprodukte, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | senkrechte Achsen der Länge $1$: gemischte Glieder fallen weg (Abschnitt [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)) |
| Nächster Punkt auf Gerade und Unterraum | Pythagoras: senkrechter Rest plus Verschiebung im Unterraum (Abschnitte [2](projektion-auf-eine-gerade.html#stufe-2) und [3](die-beste-naherungslosung.html#stufe-3)) |
| Normalgleichungen | Residuum senkrecht auf jeder Spalte: $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ (Abschnitt [3](die-beste-naherungslosung.html#stufe-3)) |
| Gram-Schmidt und QR | Schatten abziehen, den senkrechten Rest normieren (Abschnitt [4](projektion-auf-einen-unterraum.html#stufe-4)) |
| Schüssel, Rinne, Sattel | Vorzeichen der Faktoren einer Summe von Quadraten (Abschnitte [5](quadratische-formen.html#stufe-5) und [8](positiv-definite-matrizen.html#stufe-8)) |
| Entkoppeln durch Diagonalisieren | in der Eigenbasis wirkt jede Koordinate für sich (Abschnitt [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Spektralsatz | Symmetrie: $\mathbf{A}$ darf im Skalarprodukt die Seite wechseln, das Komplement eines Eigenvektors bleibt erhalten (Abschnitt [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Singulärwertzerlegung jeder Matrix | Spektralsatz für die symmetrische Matrix $\mathbf{A}^{\top}\mathbf{A}$ (Abschnitt [9](die-singularwertzerlegung.html#stufe-9)) |
| Beste Näherung vom Rang $k$ | der Kern einer Matrix vom Rang $k$ trifft die $k+1$ am stärksten gestreckten Richtungen (Abschnitt [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10)) |
| Kürzeste beste Näherungslösung | Pythagoras in den Koordinaten der Singulärvektoren: Anteile im Kern verlängern nur (Abschnitt [11](die-pseudoinverse.html#stufe-11)) |
| Konditionszahl | größte und kleinste Streckung $d_1$ und $d_n$ (Abschnitt [12](die-konditionszahl.html#stufe-12)) |
