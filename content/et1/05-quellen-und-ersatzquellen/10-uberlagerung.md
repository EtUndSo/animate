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

::::formelsammlung
**Superposition für eine Spannung**

$$U_\mathrm{AB}=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m}$$

Lineares Netz mit $n$ unabhängigen Spannungsquellen und $m$ unabhängigen Stromquellen; unabhängig heißt, ihr Wert hängt von keiner Größe im Netz ab. $a_k$ ist die Spannungsverstärkung (Empfindlichkeit) ohne Einheit, $Z_k$ der Übertragungswiderstand in $\Omega$. Die Koeffizienten hängen nur von den Widerständen ab. Gilt nur für lineare Netze und nur für Spannungen und Ströme.

**Superposition für einen Strom**

$$I_\mathrm{CD}=Y_1U_\mathrm{q1}+\dots+Y_nU_{\mathrm{q}n}+b_1I_\mathrm{q1}+\dots+b_mI_{\mathrm{q}m}$$

Strom zwischen zwei Knoten C und D; $Y_k$ in S, $b_k$ ist die Stromverstärkung. Beim Überlagern wird eine abgeschaltete Spannungsquelle zum Kurzschluss, eine abgeschaltete Stromquelle zu offenen Klemmen; Innenwiderstände bleiben im Netz.

**Leerlaufspannung von N**

$$U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}$$

Aus der Knotenregel an A bei offenen Klemmen, $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$. Jeder Summand gehört zu einer Quelle. Mit $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$, $I_\mathrm{q2}=1{,}5$ A: 6 V plus 3 V.

**Leistung überlagert sich nicht**

$$P=UI=U^2/R$$

Quadratisch in der Spannung: Beim Addieren der Teilleistungen fehlt das Mischglied $2U'U''/R_2$. Leistungen darf man nicht überlagern, Spannungen und Ströme schon.
::::

::::lernkarten
:::karte zusammenhang Warum sich Wirkungen addieren
Warum addieren sich in einem Netz aus festen Widerständen die Wirkungen mehrerer Quellen?
---
Knotenregel, Maschenregel und ohmsches Gesetz enthalten kein Produkt und kein Quadrat von Strömen und Spannungen, solange $R$ fest ist; die Gleichungen sind linear. Sind $x'$ und $x''$ Lösungen für je eine Quelle, ist $x'+x''$ die Lösung für beide.
--- falsch
Weil sich die Quellen gegenseitig nicht spüren, solange sie an verschiedenen Stellen im Netz sitzen. Liegen zwei Quellen im selben Zweig, addieren sich ihre Wirkungen dagegen nicht, und man muss beide zusammen wie eine einzige Quelle rechnen.
--- falsch
Weil sich in jedem Netz die Leistungen der Quellen addieren und Ströme und Spannungen aus den Leistungen folgen. Deshalb addiert man zuerst die Leistungen und rechnet daraus die Ströme in den Zweigen zurück, Zweig für Zweig.
--- falsch
Weil die Gleichungen des Netzes quadratisch in den Strömen sind und sich Quadrate addieren lassen. Das gilt deshalb auch, wenn eine Diode im Netz sitzt, denn auch ihre Kennlinie ist eine Parabel.
:::
:::karte begriff Superposition und Superpositionsverfahren
Was besagt die Superposition in einem linearen Netz, und wie nutzt das Superpositionsverfahren sie?
---
In einem linearen Netz addieren sich die Wirkungen der Quellen; jede treibt ihren Strom, als wäre die andere nicht da. Das Verfahren rechnet jede Quelle für sich und addiert die Teilwirkungen vorzeichenrichtig.
--- falsch
In einem linearen Netz wirkt nur die stärkste Quelle, die übrigen werden von ihr überlagert. Das Verfahren sucht diese Quelle, rechnet nur mit ihr und lässt die anderen weg.
--- falsch
In einem linearen Netz addieren sich die Leistungen der Quellen. Das Verfahren rechnet für jede Quelle die Leistung in jedem Widerstand und zählt diese Leistungen am Ende zusammen; die Ströme folgen daraus.
--- falsch
In einem linearen Netz multiplizieren sich die Wirkungen der Quellen. Das Verfahren rechnet jede Quelle für sich und multipliziert die Teilwirkungen am Ende vorzeichenrichtig miteinander.
:::
:::karte begriff unabhängig
Wann nennt man eine Quelle unabhängig, wie es der Satz über die Superposition voraussetzt?
---
Wenn ihr Wert von keiner Größe im Netz abhängt. Ihre Spannung oder ihr Strom ist fest vorgegeben, gleich was im übrigen Netz geschieht.
--- falsch
Wenn sie an kein anderes Bauteil angeschlossen ist und allein zwischen zwei Klemmen liegt, ohne Verbindung zum übrigen Netz.
--- falsch
Wenn sich ihr Wert nach der Spannung an der Last richtet, sodass sie unabhängig von Schwankungen der Last immer gleich viel Leistung liefert.
--- falsch
Wenn sie keinen Innenwiderstand hat, also ideal ist. Reale Quellen mit $R_\mathrm{q}>0$ gelten deshalb im Satz immer als abhängig.
:::
:::karte formel Satz über die Superposition
In welcher Form hängt eine Spannung $U_\mathrm{AB}$ in einem linearen Netz von den unabhängigen Quellen ab, und wovon hängen die Koeffizienten ab?
---
$U_\mathrm{AB}=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m}$. Die Koeffizienten $a_k$ ohne Einheit und $Z_k$ in $\Omega$ hängen nur von den Widerständen ab, nicht von den Quellen. Für Ströme gilt dasselbe mit $Y_k$ und $b_k$.
--- falsch
$U_\mathrm{AB}=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m}$. Die Koeffizienten hängen von den Quellen und der Last ab und müssen für jeden Wert einer Quelle neu bestimmt werden, weil sich mit ihr alle Ströme ändern.
--- falsch
$U_\mathrm{AB}=a_1U_\mathrm{q1}^2+\dots+a_nU_{\mathrm{q}n}^2+Z_1I_\mathrm{q1}^2+\dots+Z_mI_{\mathrm{q}m}^2$, weil die Leistung quadratisch ist. Die Koeffizienten hängen nur von den Widerständen ab.
--- falsch
$U_\mathrm{AB}=a_1U_\mathrm{q1}\cdot\ldots\cdot a_nU_{\mathrm{q}n}$, ein Produkt über alle Spannungsquellen; Stromquellen tragen zu Spannungen nichts bei. Die Koeffizienten hängen von den Quellen ab.
:::
:::karte begriff Empfindlichkeit
Was gibt die Empfindlichkeit $a_k$ einer Spannung $U_\mathrm{AB}$ auf eine Spannungsquelle $k$ an?
---
Die Spannungsverstärkung von Quelle $k$ zur Spannung $U_\mathrm{AB}$, ohne Einheit: Um so viel Volt ändert sich $U_\mathrm{AB}$ je Volt der Quelle. Sie hängt nur von den Widerständen ab.
--- falsch
Den kleinsten Wert der Quelle, auf den $U_\mathrm{AB}$ überhaupt reagiert, in Volt. Unterhalb dieses Werts ändert sich $U_\mathrm{AB}$ nicht, gleich wie die Quelle sich ändert.
--- falsch
Den Übertragungswiderstand von der Quelle $k$ zur Spannung $U_\mathrm{AB}$, in $\Omega$: Um so viel Volt ändert sich $U_\mathrm{AB}$ je Ampere der Quelle.
--- falsch
Um so viel Volt ändert sich $U_\mathrm{AB}$ je Volt der Quelle. Sie hängt aber vom Wert der Quelle selbst ab und muss für jede neue Quellenspannung neu gemessen oder berechnet werden.
:::
:::karte zusammenhang Quellen abschalten
Wodurch ersetzt man beim Überlagern eine abgeschaltete ideale Spannungsquelle und eine abgeschaltete ideale Stromquelle, und warum?
---
Die Spannungsquelle durch einen Kurzschluss: Mit dem Wert null erzwingt sie gleiche Potenziale, wie ein Draht. Die Stromquelle durch offene Klemmen: Mit dem Wert null erzwingt sie den Strom null, wie eine Lücke. Innenwiderstände bleiben.
--- falsch
Die Spannungsquelle durch offene Klemmen, weil null Volt keinen Strom mehr treibt. Die Stromquelle durch einen Draht, weil null Ampere keinen Widerstand braucht und den Strom ungehindert durchlassen soll. Innenwiderstände bleiben im Netz.
--- falsch
Beide durch einen Draht, weil eine abgeschaltete Quelle nichts mehr bewirkt und den Strom ungehindert durchlassen muss. Ihre Innenwiderstände nimmt man ebenfalls heraus, weil sie zur Quelle gehören.
--- falsch
Beide durch offene Klemmen, weil eine abgeschaltete Quelle aus dem Netz verschwindet und kein Strom mehr durch sie fließen darf. Die Innenwiderstände bleiben als einzelne Widerstände stehen.
:::
:::karte formel Teilbilder von N
Welche Teilbilder entstehen beim Überlagern im Netzwerk N mit $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$, $I_\mathrm{q2}=1{,}5$ A bei offenen Klemmen, und was liefern sie?
---
Mit offener Stromquelle bleibt ein Spannungsteiler, $U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}$, hier 6 V. Mit der Spannungsquelle als Draht speist die Stromquelle $R_1$ und $R_2$ parallel, $U''=(R_1\parallel R_2)\,I_\mathrm{q2}$, hier 3 V.
--- falsch
Mit offener Stromquelle bleibt $U'=\frac{R_1}{R_1+R_2}\,U_\mathrm{q1}$, hier 12 V. Mit der Spannungsquelle als Draht liegen $R_1$ und $R_2$ in Reihe, $U''=(R_1+R_2)\,I_\mathrm{q2}$, hier 13,5 V. Zusammen 25,5 V.
--- falsch
Mit der Stromquelle als Draht sind A und B verbunden, also $U'=0$. Mit offener Spannungsquelle speist die Stromquelle nur $R_2$, $U''=R_2I_\mathrm{q2}$, hier 4,5 V, und das ist zugleich die ganze Spannung.
--- falsch
Mit offener Stromquelle bleibt $U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}$, hier 6 V. Mit offener Spannungsquelle fließt der Quellenstrom nur durch $R_2$, $U''=R_2I_\mathrm{q2}$, hier 4,5 V. Zusammen 10,5 V.
:::
:::karte herleitung Koeffizienten von N
Leite für das Netzwerk N (Spannungsquelle $U_\mathrm{q1}$ über $R_1$ an A, Stromquelle $I_\mathrm{q2}$ nach A, $R_2$ zwischen A und B) die Leerlaufspannung aus der Knotenregel her und zeige, dass sie die Form der Superposition hat.
---
Bei offenen Klemmen lautet die Knotenregel an A $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$, weil durch $R_1$ und aus der Stromquelle Strom zufließt und nur durch $R_2$ Strom abfließt.
---
Nach der gesuchten Spannung umgestellt ergibt sich $U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}$, weil man mit $R_1R_2$ malnimmt und die Glieder mit $U_\mathrm{AB}$ auf einer Seite sammelt.
---
Das ist die Form der Superposition, weil jeder Summand zu genau einer Quelle gehört und die Koeffizienten nur Widerstände enthalten: $a=\frac13$ für $U_\mathrm{q1}$ und $Z=2\,\Omega$ für $I_\mathrm{q2}$.
---
Mit den Werten liefern die beiden Summanden 6 V und 3 V, zusammen $U_\mathrm{AB}=9$ V, weil sich die Teilwirkungen addieren.
:::
:::karte zusammenhang Keine Überlagerung von Leistungen
Warum darf man Leistungen nicht überlagern, Spannungen und Ströme aber schon?
---
Die Leistung ist quadratisch in der Spannung, $P=UI=U^2/R$. Beim Addieren der Teilleistungen fehlt das Mischglied $2U'U''/R_2$: In $R_2$ von N ergäben die Teilbilder 15 W, wahr sind 27 W.
--- falsch
Weil Leistungen keine Richtung haben und sich deshalb nicht vorzeichenrichtig addieren lassen. Rechnet man mit Beträgen, stimmt die Summe der Teilleistungen wieder.
--- falsch
Man darf es: In $R_2$ von N ergeben die Teilbilder 12 W und 3 W, zusammen 15 W, und genau das liefert auch die Rechnung mit beiden Quellen zugleich.
--- falsch
Weil Leistung nur in den Widerständen umgesetzt wird und Quellen keine Leistung haben. Beim Überlagern fehlen deshalb die Leistungen der abgeschalteten Quellen.
:::
:::karte zusammenhang Grenzen der Überlagerung
Wann gilt die Überlagerung nicht mehr, auch nicht für Spannungen und Ströme?
---
Sobald das Netz nicht linear ist, etwa wenn eine Diode darin sitzt oder ein Widerstand vom Strom abhängt. Dann sind die Gleichungen nicht mehr linear, und Lösungen lassen sich nicht addieren.
--- falsch
Sobald mehr als zwei Quellen im Netz sitzen. Dann beeinflussen sich die Quellen gegenseitig, und man muss alle zugleich rechnen, statt jede einzeln zu betrachten.
--- falsch
Sobald Strom- und Spannungsquellen gemischt vorkommen. Die Überlagerung gilt nur für Netze, in denen alle Quellen von derselben Art sind, weil man sonst Volt und Ampere addieren müsste.
--- falsch
Sobald die Quellen verschieden groß sind. Nur bei gleich großen Quellen hat jede Teilwirkung dasselbe Gewicht, und man darf die Teilwirkungen einfach addieren.
:::
:::karte zusammenhang Quellen verdoppeln
Was geschieht mit der Leerlaufspannung von N, wenn man beide Quellen verdoppelt, und warum?
---
Sie verdoppelt sich von 9 V auf 18 V, weil die Koeffizienten nur von den Widerständen abhängen und gleich bleiben.
--- falsch
Sie vervierfacht sich auf 36 V, weil zwei Quellen verdoppelt werden und sich die beiden Faktoren multiplizieren.
--- falsch
Sie bleibt 9 V, weil sich die stärkeren Quellen gegenseitig im Gleichgewicht halten und die Widerstände gleich bleiben.
--- falsch
Sie steigt nur auf 12 V, weil mit dem größeren Strom auch mehr Spannung an den Widerständen im Netz abfällt.
:::
::::
