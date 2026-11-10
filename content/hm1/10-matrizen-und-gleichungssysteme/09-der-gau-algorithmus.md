---
title: Stufe 7: Der Gauß-Algorithmus
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1300900
summary: Stufe 6 beschreibt die Lösungsmenge, sagt aber nicht, wie man sie findet.
tags: Gauß-Tableau, Vorwärtselimination, Pivot, Zeilenstufenform, Rückwärtseinsetzen, freie Variablen
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Stufe [6](gleichungssysteme-fragen-ruckwarts.html#stufe-6) beschreibt die Lösungsmenge, sagt aber nicht, wie man sie findet. Diese Stufe gibt ein Verfahren für jedes System und zeigt, warum es die Lösungsmenge nicht verändert.
:::

**Die Idee.** Man eliminiert die Unbekannten der Reihe nach: Geeignete Vielfache der oberen Gleichungen werden von den unteren abgezogen, bis unten nur noch eine Unbekannte steht. Geometrisch wird jede Gerade um den Lösungspunkt gedreht, der Punkt selbst bleibt (Abb. [8](#abb-8)). Der Grund: Eine Summe wahrer Gleichungen ist wahr, und weil die benutzte Gleichung stehen bleibt, lässt sich der Schritt rückgängig machen.

:::abbildung hm1/k10gauss 8
Das System $Z_1$: $x_1+x_2=3$ (blau), $Z_2$: $2x_1-x_2=3$ (rot). Nach $Z_2-2Z_1$ ist $Z_2$ die Gleichung $-3x_2=-3$, nach $Z_1+\frac13Z_2$ wird $Z_1$ zu $x_1=2$. Die Geraden drehen sich, der Punkt $(2,1)$ bleibt, und zuletzt lässt sich die Lösung ablesen.
:::

:::satz Satz 7.1 (Zeilenumformungen ändern die Lösungsmenge nicht)
<span class="anker" id="satz-7-1"></span>

Die Lösungsmenge von $Ax=b$ bleibt gleich bei (G1) Vertauschen zweier Gleichungen, (G2) Multiplikation einer Gleichung mit $c\ne0$, (G3) Addition des $c$-fachen einer *anderen* Gleichung.
:::

:::beweis Zeilenumformungen
(G1) Die Reihenfolge von Bedingungen ändert nichts. Bei (G2) und (G3) gibt es zwei Richtungen.

Vorwärts: Löst $x$ das alte System, so sind alle alten Gleichungen wahr. Die neue Gleichung ist ein Vielfaches oder eine Summe davon, also auch wahr.

Rückwärts: Jede Umformung hat eine Gegenumformung, die das alte System zurückholt. Zu (G2) gehört das $\frac1c$-fache, zu (G3) das Addieren des $(-c)$-fachen. Dabei steht die benutzte Gleichung noch unverändert da. Also löst jede Lösung des neuen Systems auch das alte.
:::

⁠**So liest man das:** Es geht keine Information verloren, weil jeder Schritt umkehrbar ist. **Warum die Voraussetzungen nötig sind:** Für $c=0$ würde (G2) eine Gleichung löschen. Ersetzt man im System aus Abb. [8](#abb-8) beide Zeilen gleichzeitig durch $Z_1-Z_2$ und $Z_2-Z_1$, entsteht zweimal dieselbe Geradengleichung $x_1=2x_2$, und ein Punkt wie $(4,2)$ löst das neue, aber nicht das alte System. Deshalb muss die benutzte Zeile stehen bleiben.

**Das Verfahren.** Weil $+$, $x_j$ und $=$ nur Schreibarbeit sind, notiert man die erweiterte Matrix $(A\,|\,b)$, das __Gauß-Tableau__.

<ol class="rm">

<li>

__Vorwärtselimination__. Suche die erste Spalte, die nicht nur Nullen enthält, und bringe durch (G1) einen Eintrag $\ne0$ nach oben. Dieser Eintrag heißt __Pivot__. Ziehe von jeder Zeile darunter das Vielfache der Pivotzeile ab, das unter dem Pivot eine Null erzeugt. Wiederhole das mit den Zeilen darunter.

</li>

<li>

Das Ergebnis ist die __Zeilenstufenform__ $(\tilde A\,|\,\tilde b)$: In jeder Zeile stehen links vom Pivot nur Nullen, das Pivot rückt pro Zeile mindestens eine Stelle nach rechts, und unten stehen $m-r$ Nullzeilen. Die Zahl $r$ der Pivots ist die Zahl der Stufen (Abb. [9](rang-und-inverse.html#abb-9) in Stufe [8](rang-und-inverse.html#stufe-8)).

</li>

<li>

__Rückwärtseinsetzen__. Lautet eine Nullzeile $0=\tilde b_i$ mit $\tilde b_i\ne0$, gibt es keine Lösung. Sonst heißen die Unbekannten in Spalten ohne Pivot __freie Variablen__, sie dürfen jeden Wert annehmen. Die übrigen berechnet man von unten nach oben.

</li>

</ol>

::::beispiel genau eine Lösung
Für $Hx=(3,7,4)$ rechnet man $Z_2-2Z_1$, $Z_3-Z_1$ und dann $Z_3-2Z_2$:

$$\left(\begin{array}{ccc|c}2&1&1&3\\4&3&3&7\\2&3&4&4\end{array}\right)\iff\left(\begin{array}{ccc|c}2&1&1&3\\0&1&1&1\\0&2&3&1\end{array}\right)\iff\left(\begin{array}{ccc|c}2&1&1&3\\0&1&1&1\\0&0&1&-1\end{array}\right).$$

Von unten: $x_3=-1$, dann $x_2=1-x_3=2$, dann $2x_1=3-x_2-x_3=2$, also $x_1=1$. Probe: $H(1,2,-1)=(3,7,4)$.
::::

::::beispiel unendlich viele oder keine
Für $Q$ mit $b=(3,7,10)$ rechnet man $Z_2-2Z_1$, $Z_3-3Z_1$, $Z_3-Z_2$:

$$\left(\begin{array}{ccc|c}1&2&1&3\\2&4&3&7\\3&6&4&10\end{array}\right)\iff\left(\begin{array}{ccc|c}1&2&1&3\\0&0&1&1\\0&0&1&1\end{array}\right)\iff\left(\begin{array}{ccc|c}1&2&1&3\\0&0&1&1\\0&0&0&0\end{array}\right).$$

Die Pivots stehen in den Spalten 1 und 3, also ist $x_2=t$ frei. Von unten: $x_3=1$, $x_1=3-2t-1=2-2t$. Das ist die Lösungsmenge aus Stufe [6](gleichungssysteme-fragen-ruckwarts.html#stufe-6). Mit $b=(3,7,11)$ wäre die letzte Zeile $0=1$: keine Lösung.
::::

⁠**Grenzfall:** Für $m=n=1$ lautet das System $ax=b$. Mit $a\ne0$ ist $a$ das Pivot und $x=b/a$. Für $a=0$ steht dort $0=b$: Bei $b\ne0$ gibt es keine Lösung, bei $b=0$ löst jedes $x$. Alle drei Fälle stecken schon hier. Über $\mathbb{C}$ läuft alles gleich, nur die Vielfachen sind komplex.

:::frage Darf ich auch Spalten umformen?
Nicht ohne weiteres. Zeilen sind Gleichungen, und mit Gleichungen darf man rechnen. Spalten gehören zu Unbekannten: Vertauscht man zwei Spalten, vertauschen sich die Namen der Unbekannten. Das muss man sich merken. Addiert man Spalten, ändert sich die Bedeutung der Unbekannten.
:::

:::aufgabe Aufgabe 10 ★★ Gauß rechnen
<span class="anker" id="aufg-10"></span>

Löse mit dem Gauß-Tableau:

<ol class="al">

<li>

$x_1+2x_2-x_3=-1$, $2x_1+5x_2+x_3=3$, $-x_1+x_2+7x_3=10$;

</li>

<li>

über $\mathbb{C}$: $x_1+\mathrm{i}x_2=1+3\mathrm{i}$, $\mathrm{i}x_1+2x_2=3+\mathrm{i}$;

</li>

<li>

$x_1-x_2+2x_3+x_4=3$, $2x_1-2x_2+5x_3+4x_4=8$. Gib die Lösungsmenge in der Form [(6.2)](gleichungssysteme-fragen-ruckwarts.html#gl-6-2) an.

</li>

</ol>

:::loesung
(a) $Z_2-2Z_1$, $Z_3+Z_1$, dann $Z_3-3Z_2$ ergibt die Zeilen $(1,2,-1\,|\,{-1})$, $(0,1,3\,|\,5)$, $(0,0,-3\,|\,{-6})$. Von unten: $x_3=2$, $x_2=5-6=-1$, $x_1=-1+2+2=3$. (b) $Z_2-\mathrm{i}Z_1$ gibt $(2-\mathrm{i}^2)x_2=3+\mathrm{i}-\mathrm{i}(1+3\mathrm{i})$, also $3x_2=6$ und $x_2=2$. Dann ist $x_1=1+3\mathrm{i}-2\mathrm{i}=1+\mathrm{i}$. (c) $Z_2-2Z_1$ gibt $x_3+2x_4=2$. Pivots in Spalten 1 und 3, frei sind $x_2=s$, $x_4=t$. Von unten: $x_3=2-2t$, $x_1=3+s-2(2-2t)-t=-1+s+3t$. Also $\mathbb L=\{(-1,0,2,0)+s(1,1,0,0)+t(3,0,-2,1):s,t\in\mathbb{R}\}$.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Parameter
<span class="anker" id="aufg-11"></span>

Für welche $c,d\in\mathbb{R}$ hat das System $x_1+x_2+x_3=1$, $x_1+2x_2+3x_3=2$, $2x_1+3x_2+cx_3=d$ keine, genau eine, unendlich viele Lösungen? Gib für $c=4$, $d=3$ die Lösungsmenge an.

:::loesung
$Z_2-Z_1$ und $Z_3-2Z_1$, dann $Z_3-Z_2$ ergibt die Zeilen $(1,1,1\,|\,1)$, $(0,1,2\,|\,1)$, $(0,0,c-4\,|\,d-3)$. Für $c\ne4$ hat jede Spalte ein Pivot: genau eine Lösung, für jedes $d$. Für $c=4$, $d\ne3$ steht dort $0=d-3\ne0$: keine Lösung. Für $c=4$, $d=3$ ist $x_3=t$ frei: $x_2=1-2t$, $x_1=1-x_2-x_3=t$. Also $\mathbb L=\{(0,1,0)+t(1,-2,1):t\in\mathbb{R}\}$.
:::
:::
