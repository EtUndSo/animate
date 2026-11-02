---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3161100
summary: Wann man mit dem Grenzwert rechnen darf wie mit den Näherungen
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Punktweise: $\lim_nf_n(x)=f(x)$ für jedes $x$. Gleichmäßig, also stärker: $\lim_n\sup_x|f_n(x)-f(x)|=0$. Dagegen spricht schon eine Stelle $x_n$ mit $|f_n(x_n)-f(x_n)|\ge c>0$.

</li>

<li>

Cauchy-Kriterium: Gleichmäßig konvergent heißt $\sup_x|f_m-f_n|\to0$ für $m,n\to\infty$.

</li>

<li>

Gleichmäßige Grenzwerte stetiger Funktionen sind stetig, und $\lim_n\int_a^bf_n\,\mathrm{d} x=\int_a^bf\,\mathrm{d} x$. Springt der Grenzwert, war die Konvergenz nicht gleichmäßig.

</li>

<li>

Ableitung: Konvergiert $f_n$ punktweise und $f_n'$ gleichmäßig, ist $f'=\lim_nf_n'$.

</li>

<li>

M-Test: Aus $|g_k(x)|\le M_k$ und $\sum_kM_k<\infty$ folgt, dass $\sum_kg_k$ gleichmäßig konvergiert.

</li>

<li>

Potenzreihen: $R=1/\limsup_k\sqrt[k]{|c_k|}$. Gleichmäßig auf $|x-x_0|\le r<R$, stetig und beliebig oft gliedweise differenzierbar in $|x-x_0|<R$, Rand gesondert prüfen.

</li>

<li>

$C^0([a,b];\mathbb{C})$ ist mit $\|f\|_{\sup}=\sup_x|f(x)|$ vollständig, $C^k$ mit $\|f\|_{C^k}=\sup_x\sum_{i=0}^k|f^{(i)}(x)|$.

</li>

<li>

Quadratisches Mittel: $\int_a^b|f_n-f|^2\,\mathrm{d} x\to0$, gleichbedeutend $\|f_n-f\|_2\to0$ mit $\langle f,g\rangle=\frac1{b-a}\int_a^bf\,\overline g\,\mathrm{d} x$. Es folgt aus gleichmäßiger Konvergenz, nicht umgekehrt. Integrale tauschen auf endlichen Intervallen wegen $|\langle f,g\rangle|\le\|f\|_2\|g\|_2$. Die Vervollständigung ist der Hilbertraum $L^2((a,b);\mathbb{C})$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Punktweise Konvergenz prüft jede Stelle einzeln und erhält weder Stetigkeit noch Integral. Gleichmäßige Konvergenz verlangt, dass der größte Abstand gegen null geht.

</li>

<li>

Dann bleiben Stetigkeit und Integral erhalten, für die Ableitung müssen die Ableitungen gleichmäßig konvergieren. Der M-Test liefert das für Reihen, Potenzreihen erfüllen es innerhalb des Konvergenzradius.

</li>

<li>

Der größte Abstand ist eine Norm, in der die stetigen Funktionen einen vollständigen Raum bilden. Das quadratische Mittel ist ein schwächeres Maß aus einem Skalarprodukt, das auch Funktionen mit Sprüngen erreicht.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles hier folgt daraus, dass eine einzige Zahl alle Stellen zugleich kontrolliert: Derselbe Index passt überall.

| Ergebnis | Woher es kommt |
|---|---|
| Cauchy-Kriterium | Vollständigkeit der Zahlen an jeder Stelle (Stufe [2](gleichmaige-konvergenz.html#stufe-2)) |
| Grenzwert bleibt stetig | dasselbe $n_0$ gilt an $x$ und $y$, drei Drittel (Stufe [3](stetigkeit-und-integral-bleiben-erhalten.html#stufe-3)) |
| Integral und Grenzwert | Fläche ist höchstens Breite mal größter Abstand (Stufe [3](stetigkeit-und-integral-bleiben-erhalten.html#stufe-3)) |
| Ableitung und Grenzwert | Hauptsatz macht aus der Ableitung ein Integral (Stufe [4](die-ableitung-braucht-mehr.html#stufe-4)) |
| M-Test | der Rest der Zahlenreihe hängt nicht von $x$ ab (Stufe [5](funktionenreihen-und-der-m-test.html#stufe-5)) |
| Potenzreihen | geometrischer Vergleich für $r<R$ (Stufe [6](potenzreihen.html#stufe-6)) |
| $C^0$ ist vollständig | Cauchy-Kriterium und Stetigkeitssatz (Stufe [7](funktionen-als-punkte-eines-raums.html#stufe-7)) |
| Integral im Mittel | Cauchy-Schwarz mit der Funktion 1 (Stufe [8](konvergenz-im-quadratischen-mittel.html#stufe-8)) |
