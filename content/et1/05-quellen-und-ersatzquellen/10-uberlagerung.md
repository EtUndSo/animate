---
title: Stufe 8: Überlagerung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1151000
summary: Stehen mehrere Quellen an verschiedenen Stellen im Netz, helfen Gruppen allein nicht.
tags: Superpositionsverfahren, unabhängig, Empfindlichkeit
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Stehen mehrere Quellen an verschiedenen Stellen im Netz, helfen Gruppen allein nicht. Das __Superpositionsverfahren__ zerlegt das Problem in eine Rechnung je Quelle.
:::

**Die Idee.** Ein Netz wird durch drei Sorten von Gleichungen festgelegt: Knotenregel, Maschenregel, ohmsches Gesetz. In keiner davon steht ein Produkt oder ein Quadrat von Strömen und Spannungen, solange $R$ fest ist. Solche Gleichungen sind linear. Hat ein solches System für eine Quelle die Lösung $x'$ und für eine andere die Lösung $x''$, dann ist $x'+x''$ die Lösung, wenn beide Quellen zugleich wirken. Einsetzen zeigt das: Jede Gleichung addiert sich Glied für Glied. Jede Quelle treibt also ihren eigenen Strom durchs Netz, als wäre die andere nicht da, und die Ströme addieren sich in jedem Zweig.

:::satz Satz 8.1 (Superposition)
<span class="anker" id="satz-8-1"></span>

In einem linearen Netz mit $n$ unabhängigen Spannungsquellen und $m$ unabhängigen Stromquellen gilt für jede Zweigspannung und jeden Zweigstrom

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
$$\begin{aligned} U_\mathrm{AB}&=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m},\\ I_\mathrm{CD}&=Y_1U_\mathrm{q1}+\dots+Y_nU_{\mathrm{q}n}+b_1I_\mathrm{q1}+\dots+b_mI_{\mathrm{q}m}. \end{aligned} \tag{8.1|8.2}$$

Die Koeffizienten hängen nur von den Widerständen ab, nicht von den Quellen.
:::

⁠**So liest man das:** Eine Quelle ist __unabhängig__, wenn ihr Wert von keiner Größe im Netz abhängt. $a_k$ ist die Spannungsverstärkung von Quelle $k$ zur Spannung $U_\mathrm{AB}$ ohne Einheit: Um so viel Volt ändert sich $U_\mathrm{AB}$ je Volt der Quelle. Man nennt das auch die __Empfindlichkeit__. $Z_k$ in $\Omega$ ist der Übertragungswiderstand (die Transimpedanz) von einer Stromquelle zu dieser Spannung. Entsprechend beschreiben $Y_k$ in S und die Stromverstärkung $b_k$ den Strom zwischen zwei Knoten C und D. $U_\mathrm{AB}$ und $I_\mathrm{CD}$ stehen stellvertretend für jede Spannung und jeden Strom des Netzes. **Gültigkeit:** nur für lineare Netze und nur für Spannungen und Ströme.

**Das Vorgehen.**

<ol>

<li>

Alle Quellen bis auf eine abschalten. Eine ideale Spannungsquelle mit dem Wert null erzwingt gleiche Potenziale an ihren Klemmen, das tut ein Draht: Sie wird zum **Kurzschluss**. Eine ideale Stromquelle mit dem Wert null erzwingt den Strom null, das tut eine Lücke: Sie wird zu **offenen Klemmen**. Innenwiderstände realer Quellen bleiben im Netz.

</li>

<li>

Die Teilwirkung dieser einen Quelle ausrechnen. Meist bleibt nur ein Spannungs- oder Stromteiler.

</li>

<li>

Für jede Quelle wiederholen und alle Teilwirkungen vorzeichenrichtig addieren.

</li>

</ol>

:::abbildung et1/k5ueberlagerung 9
Das Netzwerk N und seine beiden Teilbilder. Mitte: Die Stromquelle ist offen, es bleibt ein Spannungsteiler. Rechts: Die Spannungsquelle ist ein Draht, die Stromquelle speist $R_1$ und $R_2$ parallel. Die Klemmen A und B sind offen.
:::

::::beispiel
Gesucht ist $U_\mathrm{AB}$ in N bei offenen Klemmen (Abb. [9](#abb-9)). Teilbild 1: Spannungsteiler, $U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}=\frac13\cdot18\,\mathrm{V}=6$ V. Teilbild 2: $U''=(R_1\parallel R_2)\,I_\mathrm{q2}=2\,\Omega\cdot1{,}5\,\mathrm{A}=3$ V. Summe: $U_\mathrm{AB}=9$ V. Die Koeffizienten sind also $a=\frac13$ für $U_\mathrm{q1}$ und $Z=2\,\Omega$ für $I_\mathrm{q2}$. **Kontrolle** mit der Knotenregel an A: Durch $R_1$ kommen $(18-9)\,\mathrm{V}/6\,\Omega=1{,}5$ A, dazu 1,5 A aus der Stromquelle, und durch $R_2$ gehen $9\,\mathrm{V}/3\,\Omega=3$ A ab. Auch die Zweigströme überlagern sich: In $R_1$ fließen $2$ A aus Teilbild 1 und $-0{,}5$ A aus Teilbild 2.
::::

⁠**Grenzfall:** Verdoppelt man beide Quellen, verdoppelt sich $U_\mathrm{AB}$ auf 18 V, denn die Koeffizienten bleiben.

:::herleitung Die Koeffizienten von N
Die Knotenregel an A lautet bei offenen Klemmen $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$. Nach der gesuchten Spannung umgestellt:

$$U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}.$$

Das ist die Form [(8.1)](#gl-8-1): Jeder Summand gehört zu einer Quelle, die Koeffizienten enthalten nur Widerstände.
:::

**Die Grenze: Leistung.** Die Leistung in einem Widerstand ist quadratisch in der Spannung, $P=UI=U^2/R$ ([Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). In $R_2$ ergäbe Addieren $(6\,\mathrm{V})^2/3\,\Omega+(3\,\mathrm{V})^2/3\,\Omega=15$ W. Wahr sind $(9\,\mathrm{V})^2/3\,\Omega=27$ W. Es fehlt das Mischglied $2U'U''/R_2=12$ W. Leistungen darf man nicht überlagern, Spannungen und Ströme schon. Eine Ausnahme kommt später: Bei Wechselgrößen verschiedener Frequenz verschwindet das Mischglied im zeitlichen Mittel. Ebenso wenig gilt die Überlagerung, sobald eine Diode im Netz sitzt ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::frage Warum darf ich eine abgeschaltete Spannungsquelle nicht aus dem Netz herausnehmen?
Weil aus null Volt nicht „nichts“ wird. Die Quelle bleibt ein Teil der Leitung, sie hält nur keine Spannung mehr. Nimmt man sie heraus, unterbricht man den Strompfad durch sie. Das wäre der Fall der Stromquelle, nicht der Spannungsquelle.
:::

:::aufgabe Aufgabe 9 ★★ Zwei Quellen, ein Verbraucher
<span class="anker" id="aufg-9"></span>

Von Knoten C führen drei Zweige zur gemeinsamen Masse: $R_3=4\,\Omega$ direkt, $R_\mathrm{s}=2\,\Omega$ in Reihe mit $U_\mathrm{s}=12$ V und $R_\mathrm{t}=4\,\Omega$ in Reihe mit $U_\mathrm{t}=6$ V (beide Pluspole zeigen zu C). (a) Berechne die Spannung $U_3$ über $R_3$ durch Überlagerung und allgemein als Formel. Prüfe mit der Knotenregel. (b) Vergleiche die wahre Leistung in $R_3$ mit der Summe der Teilleistungen. (c) Wie groß ist die Empfindlichkeit von $U_3$ auf $U_\mathrm{t}$? Was ergibt sich damit für $U_\mathrm{t}=8$ V, ohne alles neu zu rechnen?

:::loesung
(a) $U_\mathrm{t}$ abgeschaltet: $R_\mathrm{t}\parallel R_3=2\,\Omega$, Teiler $U_3'=\frac{2}{2+2}\cdot12\,\mathrm{V}=6$ V. $U_\mathrm{s}$ abgeschaltet: $R_\mathrm{s}\parallel R_3=\frac43\,\Omega$, Teiler $U_3''=\frac{4/3}{4+4/3}\cdot6\,\mathrm{V}=1{,}5$ V. Also $U_3=7{,}5$ V. Allgemein:

$$U_3=\frac{R_\mathrm{t}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{s}+\frac{R_\mathrm{s}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{t}.$$

Knotenregel: $\frac{12-7{,}5}{2}\,\mathrm{A}+\frac{6-7{,}5}{4}\,\mathrm{A}=2{,}25\,\mathrm{A}-0{,}375\,\mathrm{A}=1{,}875$ A, und $7{,}5\,\mathrm{V}/4\,\Omega=1{,}875$ A. Die 6-V-Quelle nimmt Strom auf.

(b) Teilleistungen: 9 W und 0,5625 W, Summe 9,56 W. Wahr: $(7{,}5\,\mathrm{V})^2/4\,\Omega=14{,}06$ W.

(c) $a_\mathrm{t}=\frac{1{,}5\,\mathrm{V}}{6\,\mathrm{V}}=\frac14$. Für 8 V: $U_3=6\,\mathrm{V}+\frac14\cdot8\,\mathrm{V}=8$ V.
:::
:::
