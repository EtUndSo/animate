---
title: Stufe 7: Monotone Folgen und die Vollständigkeit
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240900
summary: Bisher stand der Grenzwert fest, bevor der Nachweis begann.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher stand der Grenzwert fest, bevor der Nachweis begann. Die Wurzelfolge besteht aus Brüchen und strebt zu einem Wert, der kein Bruch ist. Diese Stufe zeigt Konvergenz, ohne das Ziel zu kennen, und macht sichtbar, wo die Vollständigkeit aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) wirkt.
:::

**Die Idee.** Eine monoton wachsende Folge kann nicht zurück, und eine obere Schranke ist für sie eine Decke. Die tiefste Decke ist das Supremum der Wertemenge. An diese Decke muss die Folge heran: Bliebe sie dauerhaft um $\varepsilon$ darunter, wäre „Supremum minus $\varepsilon$“ eine noch tiefere Decke. Der Beweis steht und fällt damit, dass es die tiefste Decke im Zahlbereich gibt. Das sagt das Vollständigkeitsaxiom.

:::satz Satz 7.1 (Monotonie-Lemma)
<span class="anker" id="satz-7-1"></span>

<ol>

<li>

Eine monoton wachsende Folge $\{a_n\}$, die nach oben beschränkt ist, ist konvergent, und es gilt $\lim_{n\to\infty}a_n=\sup\mathcal W(a_n)\in\mathbb{R}$.

</li>

<li>

Eine monoton fallende Folge $\{b_n\}$, die nach unten beschränkt ist, ist konvergent, und es gilt $\lim_{n\to\infty}b_n=\inf\mathcal W(b_n)\in\mathbb{R}$.

</li>

</ol>
:::

⁠**So liest man das:** $\mathcal W(a_n)=\{a_n:n\in\mathbb{N}\}$ ist die Wertemenge aus Stufe [1](folgen-und-ihr-verlauf.html#stufe-1). Der Satz gibt Konvergenz, ohne dass der Grenzwert vorher in einer Formel bekannt sein muss. **Voraussetzungen nötig:** Ohne Schranke wächst $n^2$ ohne Grenze, ohne Monotonie pendelt $(-1)^n$. **Grenzfall:** Die konstante Folge $c$ ist monoton in beide Richtungen, ihr Supremum und Infimum sind $c$.

:::beweis Monotonie-Lemma
(I) Die Wertemenge $M:=\mathcal W(a_n)\subset\mathbb{R}$ ist nicht leer und nach oben beschränkt. Nach dem Vollständigkeitsaxiom existiert $a:=\sup M\in\mathbb{R}$. Sei $\varepsilon>0$. Dann ist $a-\varepsilon$ keine obere Schranke von $M$, denn $a$ ist die kleinste. Also gibt es ein $N_0$ mit $a-\varepsilon<a_{N_0}\le a$. Wegen der Monotonie gilt für alle $n>N_0$

$$a-\varepsilon<a_{N_0}\le a_n\le a,\quad\text{also}\quad|a_n-a|<\varepsilon.$$

(II) Die Folge $a_n:=-b_n$ ist monoton wachsend und nach oben beschränkt, mit $\sup\mathcal W(a_n)=-\inf\mathcal W(b_n)$. Nach (I) konvergiert sie, die Rechenregeln übertragen das auf $b_n$.
:::

:::abbildung hm1/k4monoton 8
Links die Summenfolge unter der Decke $\sup\mathcal W(s_n)=2$. Der rote Streifen hat die Breite $\varepsilon=0{,}1$. Ab $N_0=3$ bleiben alle Glieder darin. Rechts die Wurzelfolge: Sie fällt, ist nach unten beschränkt und strebt gegen $\sqrt2$. Innerhalb der rationalen Zahlen gibt es dort kein Ziel.
:::

::::beispiel die Wurzelfolge
Alle Glieder $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$ sind positiv und rational, denn Brüche bleiben bei den Grundrechenarten Brüche. Ausmultiplizieren zeigt zwei Dinge:

$$x_{n+1}^2-2=\tfrac14\Bigl(x_n-\frac2{x_n}\Bigr)^2\ge0,\qquad x_n-x_{n+1}=\frac{x_n^2-2}{2x_n}\ge0.$$

Die erste Gleichung sagt mit $x_1^2=4$, dass $x_n^2\ge2$ für alle $n$ gilt, die zweite sagt damit: Die Folge fällt monoton. Nach unten ist sie durch 1 beschränkt, denn $x_n^2\ge2$ erzwingt $x_n\ge1$. Das Monotonie-Lemma liefert in $\mathbb{R}$ einen Grenzwert $x\ge1$. Ihn berechnet man, indem man in der Vorschrift auf beiden Seiten zum Grenzwert übergeht (Rechenregeln, $\{x_{n+1}\}$ hat denselben Grenzwert wie $\{x_n\}$):

$$x=\tfrac12\Bigl(x+\frac2x\Bigr)\quad\Longrightarrow\quad x^2=2\quad\Longrightarrow\quad x=\sqrt2.$$

Zahlen: $x_3=1{,}4167$, $x_4=1{,}414216$, $x_5=1{,}4142135624$. Der Fehler von $x_5$ liegt unter $2\cdot10^{-12}$. Das Heron-Verfahren ist ein gängiger Weg, Wurzeln in digitalen Rechenwerken zu bestimmen.
::::

**Warum das in $\mathbb{Q}$ scheitert.** Alle Voraussetzungen des Monotonie-Lemmas prüft man innerhalb von $\mathbb{Q}$: Die $x_n$ sind Brüche, sie fallen, und die Schranke 1 ist ein Bruch. Trotzdem gibt es in $\mathbb{Q}$ keinen Grenzwert: Jeder Grenzwert müsste die Gleichung $x^2=2$ erfüllen, und kein Bruch tut das ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Der Beweis des Lemmas bricht genau an einer Stelle: Die Menge $\{x_n\}$ hat in $\mathbb{Q}$ kein Infimum. Zu jeder rationalen unteren Schranke gibt es eine größere. Die Folge läuft auf eine Lücke zu. Deshalb steht in der Definition der Konvergenz $a\in\mathbb{R}$ und deshalb ist die Vollständigkeit keine Formalie: *In $\mathbb{R}$ hat jede monotone beschränkte Folge ein Ziel, in $\mathbb{Q}$ nicht.*

:::frage Ein Rechner kennt nur Brüche. Wozu braucht man die Lücken in $\mathbb{Q}$ geschlossen?
Für einen Zahlenwert genügt ein Bruch: $x_5$ trifft $\sqrt2$ auf 11 Nachkommastellen. Aussagen wie „diese Folge hat einen Grenzwert“ brauchen dagegen $\mathbb{R}$. Stetigkeit ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)) und Reihen ([Kapitel 6](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen/unendliche-reihen.html)) beruhen darauf, dass der Grenzwert existiert, auch wenn ihn niemand als Bruch hinschreiben kann.
:::

:::aufgabe Aufgabe 9 ★★ Wurzelkette
<span class="anker" id="aufg-9"></span>

Gegeben ist $y_1=1$, $y_{n+1}=\sqrt{2y_n+3}$. (a) Berechne $y_2,y_3,y_4$. (b) Zeige durch Induktion $0<y_n<3$ und $y_n<y_{n+1}$. (c) Warum konvergiert die Folge? (d) Berechne den Grenzwert. Warum scheidet $-1$ aus?

:::loesung
(a) $y_2=\sqrt5=2{,}2361$, $y_3=2{,}7335$, $y_4=2{,}9098$. (b) $y_1=1$ liegt in $(0,3)$. Aus $0<y_n<3$ folgt $3<2y_n+3<9$, also $0<y_{n+1}<3$. Weiter ist $y_{n+1}^2-y_n^2=2y_n+3-y_n^2=(3-y_n)(1+y_n)>0$, und weil beide positiv sind, ist $y_{n+1}>y_n$. (c) Die Folge ist monoton wachsend und beschränkt, das Monotonie-Lemma greift. (d) Grenzübergang in $y_{n+1}^2=2y_n+3$ gibt $y^2=2y+3$, also $(y-3)(y+1)=0$. Wegen $y_n\ge1$ ist $y\ge1$, also $y=3$.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Heron für 3
<span class="anker" id="aufg-10"></span>

Gegeben ist $w_1=2$, $w_{n+1}=\frac12(w_n+3/w_n)$. (a) Berechne $w_2,w_3$ als Brüche. (b) Zeige wie im Beispiel: $w_n^2\ge3$, und die Folge fällt monoton. (c) Bestimme ihren Grenzwert in $\mathbb{R}$. (d) Eine Bekannte behauptet: „Die Folge fällt und ist beschränkt, also konvergiert sie auch in $\mathbb{Q}$.“ Was ist falsch, wenn du weißt, dass $\sqrt3$ irrational ist?

:::loesung
(a) $w_2=\frac12(2+\frac32)=\frac74$, $w_3=\frac12(\frac74+\frac{12}7)=\frac{97}{56}=1{,}7321$. (b) $w_{n+1}^2-3=\frac14(w_n-3/w_n)^2\ge0$ und $w_1^2=4\ge3$, also $w_n^2\ge3$. Damit ist $w_n-w_{n+1}=\frac{w_n^2-3}{2w_n}\ge0$. (c) Die Folge ist durch 1 nach unten beschränkt, also konvergiert sie in $\mathbb{R}$ gegen ein $w\ge1$. Der Grenzübergang gibt $w=\frac12(w+3/w)$, also $w^2=3$ und $w=\sqrt3$. (d) Das Monotonie-Lemma braucht ein Infimum im Zahlbereich, und das fehlt in $\mathbb{Q}$. Ein rationaler Grenzwert müsste $w^2=3$ erfüllen. Das schließt die Irrationalität von $\sqrt3$ aus.
:::
:::

::::formelsammlung
**Monotonie-Lemma**

$$\lim_{n\to\infty}a_n=\sup\mathcal W(a_n)\in\mathbb{R},\qquad\lim_{n\to\infty}b_n=\inf\mathcal W(b_n)\in\mathbb{R}$$

Für monoton wachsende, nach oben beschränkte $\{a_n\}$ und monoton fallende, nach unten beschränkte $\{b_n\}$. Die Existenz liefert das Vollständigkeitsaxiom; in $\mathbb{Q}$ kann der Grenzwert fehlen.

**Heron-Verfahren (Wurzelfolge)**

$$x_1=2,\qquad x_{n+1}=\frac12(x_n+2/x_n)$$

Lauter Brüche, monoton fallend, nach unten durch 1 beschränkt; Grenzwert $\sqrt2$ in $\mathbb{R}$, keiner in $\mathbb{Q}$.

**Monotonie und Schranke der Wurzelfolge**

$$x_{n+1}^2-2=\tfrac14\Bigl(x_n-\frac2{x_n}\Bigr)^2\ge0,\qquad x_n-x_{n+1}=\frac{x_n^2-2}{2x_n}\ge0$$

Mit $x_1^2=4$ folgt $x_n^2\ge2$, damit fällt die Folge.

**Grenzübergang in der Vorschrift**

$$x=\tfrac12\Bigl(x+\frac2x\Bigr)\quad\Longrightarrow\quad x^2=2\quad\Longrightarrow\quad x=\sqrt2$$

Erst nach dem Nachweis der Existenz; $\{x_{n+1}\}$ hat denselben Grenzwert wie $\{x_n\}$.
::::

::::lernkarten
:::karte formel Monotonie-Lemma
Was besagt das Monotonie-Lemma für monoton wachsende und für monoton fallende Folgen, und welchen Grenzwert liefert es?
---
Eine monoton wachsende, nach oben beschränkte Folge konvergiert mit $\lim_{n\to\infty}a_n=\sup\mathcal W(a_n)\in\mathbb{R}$; eine monoton fallende, nach unten beschränkte Folge konvergiert mit $\lim_{n\to\infty}b_n=\inf\mathcal W(b_n)\in\mathbb{R}$.
--- falsch
Eine monoton wachsende, nach unten beschränkte Folge konvergiert mit $\lim_{n\to\infty}a_n=\inf\mathcal W(a_n)$; eine monoton fallende, nach oben beschränkte Folge konvergiert mit $\lim_{n\to\infty}b_n=\sup\mathcal W(b_n)$.
--- falsch
Eine monoton wachsende, nach oben beschränkte Folge konvergiert gegen ihr größtes Glied, $\lim_{n\to\infty}a_n=\max\mathcal W(a_n)$; eine monoton fallende, nach unten beschränkte entsprechend gegen $\min\mathcal W(b_n)$.
--- falsch
Eine monoton wachsende Folge konvergiert immer, notfalls gegen $\sup\mathcal W(a_n)=+\infty$; eine monoton fallende konvergiert gegen $\inf\mathcal W(b_n)$, auch wenn sie nach unten keine Schranke hat.
:::
:::karte herleitung Monotonie-Lemma
Wie beweist man, dass eine monoton wachsende, nach oben beschränkte Folge gegen das Supremum ihrer Wertemenge konvergiert?
---
Die Wertemenge $M:=\mathcal W(a_n)$ ist nicht leer und nach oben beschränkt; deshalb existiert $a:=\sup M\in\mathbb{R}$, weil das Vollständigkeitsaxiom es garantiert.
---
Sei $\varepsilon>0$. Dann ist $a-\varepsilon$ keine obere Schranke von $M$, weil $a$ die kleinste ist; also gibt es ein $N_0$ mit $a-\varepsilon<a_{N_0}\le a$.
---
Für alle $n>N_0$ gilt $a-\varepsilon<a_{N_0}\le a_n\le a$, weil die Folge monoton wächst und $a$ eine obere Schranke ist.
---
Also ist $|a_n-a|<\varepsilon$ für alle $n>N_0$, weil $a_n$ zwischen $a-\varepsilon$ und $a$ liegt.
---
Die fallende Version folgt mit $a_n:=-b_n$, weil diese Folge monoton wächst, nach oben beschränkt ist und $\sup\mathcal W(a_n)=-\inf\mathcal W(b_n)$ hat; die Rechenregeln übertragen die Konvergenz auf $b_n$.
:::
:::karte zusammenhang tiefste Decke
Warum muss eine monoton wachsende, nach oben beschränkte Folge an das Supremum ihrer Wertemenge heranrücken?
---
Das Supremum ist die tiefste Decke über allen Gliedern. Bliebe die Folge dauerhaft um $\varepsilon$ darunter, wäre „Supremum minus $\varepsilon$“ eine noch tiefere Decke. Da die Folge nicht zurück kann, bleibt sie danach über dieser Marke.
--- falsch
Weil das Supremum immer ein Glied der Folge ist: Eine wachsende Folge erreicht ihre Decke nach endlich vielen Schritten und bleibt dann dort stehen. Das Heranrücken ist also in Wahrheit ein Ankommen nach endlich vielen Gliedern.
--- falsch
Weil jede beschränkte Folge an ihre Schranken heranrückt, ob monoton oder nicht; die Monotonie sorgt nur dafür, dass sie das von unten tut und nicht abwechselnd von oben und unten, wie es die Pendelfolge macht.
--- falsch
Weil die Abstände benachbarter Glieder gegen 0 gehen, sobald die Folge beschränkt ist; dann kommen die Glieder jeder Zahl oberhalb beliebig nahe, auch dem Supremum, und bleiben schließlich in seiner Nähe.
:::
:::karte zusammenhang Vollständigkeit
Warum hat in $\mathbb{R}$ jede monotone beschränkte Folge ein Ziel, in $\mathbb{Q}$ aber nicht, und was zeigt die Wurzelfolge dazu?
---
Das Monotonie-Lemma braucht das Supremum bzw. Infimum der Wertemenge im Zahlbereich; in $\mathbb{R}$ sichert das die Vollständigkeit. Die Wurzelfolge erfüllt in $\mathbb{Q}$ alle Voraussetzungen, doch $\{x_n\}$ hat dort kein Infimum: Ihr Grenzwert müsste $x^2=2$ erfüllen.
--- falsch
Weil in $\mathbb{Q}$ die Rechenregeln nicht gelten: Der Grenzübergang in $x_{n+1}=\frac12(x_n+2/x_n)$ ist in $\mathbb{Q}$ nicht erlaubt, deshalb findet man dort keinen Grenzwert, obwohl es einen gibt. In $\mathbb{R}$ gelten die Rechenregeln dagegen uneingeschränkt.
--- falsch
Weil die Wurzelfolge in $\mathbb{Q}$ nicht monoton ist: Erst in $\mathbb{R}$ fällt sie monoton, denn die Ungleichung $x_n^2\ge2$ lässt sich nur mit reellen Zahlen beweisen. Das Monotonie-Lemma ist deshalb in $\mathbb{Q}$ gar nicht anwendbar.
--- falsch
Weil in $\mathbb{Q}$ beschränkte Mengen keine Schranken haben: Die Wurzelfolge hat in $\mathbb{Q}$ keine untere Schranke, erst $\mathbb{R}$ liefert die Schranke 1 und damit das Ziel. Mit der Schranke gilt das Monotonie-Lemma dann in jedem Zahlbereich.
:::
:::karte begriff Heron-Verfahren
Was ist das Heron-Verfahren zur Bestimmung von $\sqrt2$, und welche Eigenschaften haben seine Glieder?
---
Die Wurzelfolge $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$: lauter positive Brüche, die monoton fallen, nach unten durch 1 beschränkt sind und sich $\sqrt2$ nähern; ein gängiger Weg, Wurzeln in Rechenwerken zu bestimmen.
--- falsch
Das Halbierungsverfahren: Man halbiert ein Intervall um $\sqrt2$ immer wieder und nimmt die Intervallmitten als Glieder; sie sind Brüche, liegen abwechselnd über und unter $\sqrt2$ und wachsen dabei monoton.
--- falsch
Die Wurzelfolge $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$: lauter irrationale Zahlen, die monoton wachsen, nach oben durch 2 beschränkt sind und $\sqrt2$ nach endlich vielen Schritten exakt erreichen.
--- falsch
Die Folge $x_1=2$, $x_{n+1}=x_n-\frac12$: lauter Brüche, die in gleichen Schritten fallen, bis sie $\sqrt2$ unterschreiten; das letzte Glied oberhalb von $\sqrt2$ ist die gesuchte Näherung.
:::
:::karte zusammenhang Wurzelfolge fällt
Warum ist die Wurzelfolge $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$ monoton fallend und nach unten beschränkt?
---
Ausmultiplizieren gibt $x_{n+1}^2-2=\frac14\bigl(x_n-\frac2{x_n}\bigr)^2\ge0$, mit $x_1^2=4$ also $x_n^2\ge2$ für alle $n$. Damit ist $x_n-x_{n+1}=\frac{x_n^2-2}{2x_n}\ge0$: Die Folge fällt. Aus $x_n^2\ge2$ folgt $x_n\ge1$.
--- falsch
Weil jeder Schritt den Mittelwert aus $x_n$ und $2/x_n$ bildet und ein Mittelwert immer kleiner als beide Zahlen ist; nach unten ist sie durch 0 beschränkt, weil alle Glieder positiv sind und es bleiben.
--- falsch
Ausmultiplizieren gibt $x_{n+1}^2-2=\frac14\bigl(x_n+\frac2{x_n}\bigr)^2\ge0$, also $x_n^2\ge2$; daraus folgt $x_{n+1}\ge x_n$. Die Folge wächst also und ist nach oben durch 2 beschränkt, ihr Startwert.
--- falsch
Weil $x_{n+1}=x_n-\frac1{x_n}$ ist: Es wird in jedem Schritt eine positive Zahl abgezogen. Nach unten beschränkt ist sie durch $\sqrt2$, weil sie diesen Wert nach endlich vielen Schritten erreicht und dann stehen bleibt.
:::
:::karte zusammenhang Grenzübergang in der Vorschrift
Wie berechnet man den Grenzwert der Wurzelfolge, und warum muss vorher feststehen, dass er existiert?
---
Man geht in der Vorschrift beidseitig zum Grenzwert über, da $\{x_{n+1}\}$ denselben Grenzwert hat wie $\{x_n\}$: $x=\frac12(x+\frac2x)$, also $x^2=2$ und wegen $x\ge1$ $x=\sqrt2$. Die Rechenregeln gelten nur für konvergente Folgen.
--- falsch
Man setzt $x_n=x_{n+1}$ für ein festes $n$ und löst nach $x_n$ auf; dieses eine Glied ist dann der Grenzwert der Folge. Ob er existiert, muss man nicht eigens prüfen, denn die Gleichung zeigt es von selbst, sobald sie eine Lösung hat.
--- falsch
Man geht in der Vorschrift zum Grenzwert über und erhält $x=\frac12(x+\frac2x)$, also $x^2=2$ und damit $x=-\sqrt2$ oder $x=\sqrt2$. Beide Lösungen sind Grenzwerte der Folge, weil eine Folge mehrere Grenzwerte haben darf.
--- falsch
Man rechnet so lange Glieder aus, bis sich die angezeigten Nachkommastellen nicht mehr ändern; bei $x_5$ ist das erreicht, und $x_5$ ist dann der Grenzwert. Die Existenz zeigt die Rechnung selbst, ein Satz ist dafür nicht nötig.
:::
:::karte zusammenhang Konvergenz ohne bekanntes Ziel
Was leistet das Monotonie-Lemma, was Epsilontik und Rechenregeln nicht leisten?
---
Es zeigt Konvergenz, ohne dass der Grenzwert vorher in einer Formel bekannt sein muss. Epsilontik braucht den Grenzwert $a$ im Abstand $|a_n-a|$, und die Rechenregeln führen ihn nur auf bekannte Grenzwerte zurück.
--- falsch
Es berechnet den Grenzwert als Formel, etwa $\sqrt2$; Epsilontik und Rechenregeln zeigen dagegen nur, dass ein Grenzwert existiert, ohne ihn anzugeben, und brauchen deshalb das Monotonie-Lemma als Ergänzung.
--- falsch
Es zeigt Konvergenz auch für Folgen, die nicht beschränkt sind; Epsilontik und Rechenregeln brauchen dagegen immer eine Schranke, weil sie nur für konvergente und damit beschränkte Folgen gelten.
--- falsch
Es gilt auch in $\mathbb{Q}$, während Epsilontik und Rechenregeln die Vollständigkeit von $\mathbb{R}$ brauchen; deshalb liefert es als einziges Werkzeug Grenzwerte, die keine Brüche sein müssen.
:::
:::karte zusammenhang Voraussetzungen des Monotonie-Lemmas
Warum kann man im Monotonie-Lemma weder auf die Schranke noch auf die Monotonie verzichten?
---
Ohne Schranke wächst $n^2$ ohne Grenze, obwohl die Folge monoton ist; ohne Monotonie pendelt $(-1)^n$, obwohl sie beschränkt ist. Beide Folgen divergieren.
--- falsch
Auf die Monotonie kann man verzichten: Jede beschränkte Folge konvergiert gegen das Supremum ihrer Wertemenge. Nur ohne Schranke scheitert es, wie bei $n^2$.
--- falsch
Auf die Schranke kann man verzichten: Jede monotone Folge konvergiert, $n^2$ etwa gegen $\sup\mathcal W(n^2)$. Nur ohne Monotonie scheitert es, wie bei $(-1)^n$.
--- falsch
Man kann auf beides verzichten, solange die Glieder Brüche sind; die Voraussetzungen braucht man nur in $\mathbb{R}$, weil dort die Vollständigkeit wirkt.
:::
:::karte zusammenhang Brüche und reelle Zahlen
Ein Rechner kennt nur Brüche; wozu braucht man dann die Lücken in $\mathbb{Q}$ geschlossen?
---
Für einen Zahlenwert genügt ein Bruch: $x_5$ trifft $\sqrt2$ auf 11 Nachkommastellen. Aussagen wie „diese Folge hat einen Grenzwert“ brauchen dagegen $\mathbb{R}$, denn der Grenzwert ist oft kein Bruch.
--- falsch
Weil ein Rechner mit Brüchen $\sqrt2$ nie genauer als auf zwei Nachkommastellen bestimmen kann; erst mit reellen Zahlen werden die Werte des Heron-Verfahrens genau, und deshalb muss jeder Rechner intern mit $\mathbb{R}$ arbeiten.
--- falsch
Man braucht sie nicht: Weil jeder Rechner mit Brüchen auskommt, ist $\mathbb{R}$ nur eine bequeme Schreibweise, und jede Folge aus Brüchen hat auch einen Grenzwert in $\mathbb{Q}$, wenn man nur genügend Stellen mitnimmt.
--- falsch
Weil Brüche beim Rechnen Rundungsfehler erzeugen, reelle Zahlen dagegen nicht; deshalb rechnen digitale Rechenwerke intern mit reellen Zahlen, auch beim Heron-Verfahren, und geben am Ende nur gerundete Brüche aus.
:::
::::
