---
title: Stufe 3: Das Maschenstromverfahren
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180500
summary: Die Knotenregel ist erledigt, m Maschenregeln mit m Unbekannten bleiben.
tags: Koppelwiderstand
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Knotenregel ist erledigt, $m$ Maschenregeln mit $m$ Unbekannten bleiben. Diese Stufe stellt sie auf und zeigt, warum man die Matrix ablesen kann.
:::

**Die Idee.** Man läuft eine Masche im Umlaufsinn ihres Stroms ab. An jedem Widerstand fällt $R$ mal Zweigstrom ab, und der Zweigstrom ist der eigene Maschenstrom plus oder minus der Nachbarn. Sortiert man nach Maschenströmen, steht vor dem eigenen Strom die Summe aller Widerstände der Masche. Vor einem fremden Strom steht nur, was beide Maschen gemeinsam durchlaufen. Mehr kann dort nicht stehen. Darum ist die Matrix eine Liste der Schaltung.

:::definition Definition 3.1 (Maschenstromverfahren)
<span class="anker" id="satz-3-1"></span>

Das Verfahren hat vier Schritte:

<ol>

<li>

Reale Stromquellen in reale Spannungsquellen umwandeln: $U_\mathrm q=I_\mathrm q\,R$, derselbe Widerstand in Reihe ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

$m$ unabhängige Maschen wählen, je einen Maschenstrom mit beliebiger Richtung eintragen. Der Umlaufsinn der Masche ist diese Richtung.

</li>

<li>

Für jede Masche die Maschenregel aufstellen oder die Matrix direkt ablesen.

</li>

<li>

Das System nach den Maschenströmen lösen, daraus Zweigströme und Zweigspannungen berechnen.

</li>

</ol>
:::

:::satz Satz 3.2 (Matrixform des Maschenstromverfahrens)
<span class="anker" id="satz-3-2"></span>

Die Maschenströme erfüllen $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$:

<span class="anker" id="gl-3-1"></span>
$$\begin{pmatrix}Z_{11}&Z_{12}&\dots&Z_{1m}\\mathbb{Z}_{21}&Z_{22}&\dots&Z_{2m}\\\vdots&\vdots&\ddots&\vdots\\mathbb{Z}_{m1}&Z_{m2}&\dots&Z_{mm}\end{pmatrix} \begin{pmatrix}I_1\\I_2\\\vdots\\I_m\end{pmatrix}= \begin{pmatrix}U_\mathrm{q1}\\U_\mathrm{q2}\\\vdots\\U_{\mathrm qm}\end{pmatrix}. \tag{3.1}$$

<ul>

<li>

$Z_{\mu\mu}$ ist die Summe aller Widerstände der Masche $\mu$.

</li>

<li>

$Z_{\mu\nu}$ ist der __Koppelwiderstand__, die Summe der Widerstände, die beide Maschen durchlaufen: positiv, wenn beide Ströme dort gleichsinnig fließen, negativ bei gegensinnigen Strömen, null ohne gemeinsamen Zweig. Es gilt $Z_{\mu\nu}=Z_{\nu\mu}$.

</li>

<li>

$U_{\mathrm q\mu}$ ist die Summe der Quellenspannungen in der Masche, positiv für jede Quelle, die den Maschenstrom antreibt. Bei Spannungspfeilen vom Plus- zum Minuspol (GZS, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) heißt das: Ein Pfeil gegen den Umlauf zählt positiv, ein Pfeil mit dem Umlauf negativ.

</li>

</ul>
:::

:::herleitung Von der Maschenregel zur Matrix
Für die Masche $\mu$ ist die Summe aller $R_a\,I_a$ gleich der treibenden Spannung $U_{\mathrm q\mu}$, weil die Quellen auf die rechte Seite wechseln. Dabei ist $I_a$ der Strom in $R_a$, gezählt im Umlaufsinn von $\mu$. Nach [(2.1)](maschenstrome-erfullen-die-knotenregel.html#gl-2-1) ist $I_a=I_\mu+\sum_{\nu\neq\mu}\sigma_{a\nu}\,I_\nu$. Umordnen ergibt vor $I_\mu$ die Summe aller $R_a$ und vor $I_\nu$ die Summe $\sum_a\sigma_{a\nu}R_a$ über die gemeinsamen Widerstände. Masche $\nu$ erhält denselben Widerstand mit demselben Vorzeichen, denn gleichsinnig ist eine Beziehung zwischen zwei Maschen. Deshalb ist $\mathbf Z$ symmetrisch.
:::

⁠**So liest man das:** Die Zeile $\mu$ ist die Maschenregel der Masche $\mu$. Die Spalte $\nu$ sagt, welche Spannung ein Ampere Maschenstrom $\nu$ in jeder Masche erzeugt. Daher die Einheit Ohm, typisch sind hier Kiloohm. Der Buchstabe $Z$ kommt von der Impedanz ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)), hier sind es reine Widerstände. **Gültigkeit:** Das Netz enthält lineare Widerstände und feste Spannungsquellen. Die Symmetrie ist zugleich eine Kontrolle: Ein Fehler beim Aufstellen zerstört sie meist.

:::abbildung et1/k8maschen 3
Das Rechenmodell für das Maschenstromverfahren. Rechts ist die Stromquelle in eine Spannungsquelle umgewandelt. Rot sind die gemeinsamen Widerstände $R_2$ und $R_4$: Sie stehen außerhalb der Diagonale von $\mathbf Z$. I und III haben keinen gemeinsamen Zweig, deshalb ist $Z_{13}=0$.
:::

::::beispiel
Rechts wird $U_\mathrm{q5}=I_\mathrm q\,R_5=20$ V mit $R_5$ in Reihe (Abb. [3](#abb-3)). Die drei Umläufe im Uhrzeigersinn lauten

$$\begin{aligned} \text{I:}\quad&R_1I_\mathrm I+R_2(I_\mathrm I-I_\mathrm{II})-U_\mathrm q=0,\\ \text{II:}\quad&R_2(I_\mathrm{II}-I_\mathrm I)+R_3I_\mathrm{II}+R_4(I_\mathrm{II}-I_\mathrm{III})=0,\\ \text{III:}\quad&R_4(I_\mathrm{III}-I_\mathrm{II})+R_5I_\mathrm{III}+U_\mathrm{q5}=0. \end{aligned}$$

Geordnet, in k$\Omega$, mA und V, ist das genau, was man auch abliest:

$$\begin{pmatrix}R_1+R_2&-R_2&0\\-R_2&R_2+R_3+R_4&-R_4\\0&-R_4&R_4+R_5\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}5&-4&0\\-4&16&-10\\0&-10&15\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}9\\0\\-20\end{pmatrix}.$$

Alle Nebendiagonalen sind negativ, weil benachbarte Kreise gleicher Drehrichtung im gemeinsamen Zweig gegeneinander laufen. $U_\mathrm q$ treibt Masche I an, $U_\mathrm{q5}$ wirkt gegen Masche III. Mit [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) und [(0.2)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-2) ist

$$D=5\cdot140+4\cdot(-60)=460,\qquad D_1=9\cdot140+4\cdot(-200)=460,$$

$$D_2=5\cdot(-200)-9\cdot(-60)=-460,\qquad D_3=-1600+320+360=-920.$$

Also sind $I_\mathrm I=1$ mA, $I_\mathrm{II}=-1$ mA und $I_\mathrm{III}=-2$ mA. Das Minus sagt: Masche II und III laufen in Wirklichkeit gegen den Uhrzeigersinn. Die Zweigströme aus Stufe [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2) sind 1 mA in $R_1$, 2 mA in $R_2$ nach unten, 1 mA in $R_3$ von Knoten 2 nach Knoten 1 und 1 mA in $R_4$ nach unten. **Kontrolle:** $U_1=R_2\cdot2\,\mathrm{mA}=8$ V und $U_2=R_4\cdot1\,\mathrm{mA}=10$ V. Masche I: $1+8-9=0$.
::::

⁠**Grenzfall:** Für $R_2\to0$ wird $Z_{12}=0$, die Masche I ist entkoppelt: Ein Draht in der Mitte trennt beide Seiten, denn seine Spannung ist null, was immer durch ihn fließt.

:::frage Müssen alle Maschenströme gleich herum laufen?
Nein. Gleiche Drehrichtung ist nur bequem, weil dann alle Nebendiagonalen negativ sind. Dreht man einen Maschenstrom um, wechseln seine Zeile und seine Spalte das Vorzeichen, die Diagonale bleibt, und der Wert des Stroms wechselt ebenfalls das Vorzeichen. Der Zweigstrom ändert sich nicht.
:::

:::zusatz Ideale Stromquelle
Für $R_5\to\infty$ wächst $U_\mathrm{q5}$ ohne Grenze, das Umwandeln versagt ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Man legt die Maschen dann so, dass nur eine durch die Stromquelle läuft. Ihr Maschenstrom ist bekannt. Die Maschengleichung dieser Masche lässt man weg, denn sie enthält die unbekannte Spannung der Quelle. Eine Unbekannte weniger, eine Gleichung weniger.
:::

:::aufgabe Aufgabe 3 ★★ Das Netz aus Kapitel 2
<span class="anker" id="aufg-3"></span>

Das Netz aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) hat eine ideale Quelle mit 9 V zwischen $K_1$ und $K_4$ und $R_\mathrm a=2\,\mathrm{k\Omega}$ ($K_1K_2$), $R_\mathrm b=5\,\mathrm{k\Omega}$ ($K_2K_4$), $R_\mathrm c=3\,\mathrm{k\Omega}$ ($K_1K_3$), $R_\mathrm d=1\,\mathrm{k\Omega}$ ($K_3K_4$), $R_\mathrm e=2\,\mathrm{k\Omega}$ ($K_2K_3$). Die Maschen laufen so: $I_\mathrm A$ durch die Quelle von $K_4$ nach $K_1$, dann $K_2$, zurück nach $K_4$. $I_\mathrm B$ von $K_1$ nach $K_3$, $K_2$, zurück nach $K_1$. $I_\mathrm C$ von $K_2$ nach $K_3$, $K_4$, zurück nach $K_2$.

<ol class="al">

<li>

Lies $\mathbf Z$ und die rechte Seite ab. Prüfe die Symmetrie.

</li>

<li>

Berechne die Maschenströme mit der cramerschen Regel.

</li>

<li>

Bestimme die fünf Widerstandsströme und vergleiche mit [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).

</li>

</ol>

:::loesung
(a) Masche A enthält $R_\mathrm a$, $R_\mathrm b$, Masche B $R_\mathrm a$, $R_\mathrm c$, $R_\mathrm e$, Masche C $R_\mathrm b$, $R_\mathrm d$, $R_\mathrm e$. Alle laufen in den gemeinsamen Zweigen gegensinnig:

$$\mathbf Z=\begin{pmatrix}7&-2&-5\\-2&7&-2\\-5&-2&8\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\0\end{pmatrix}\mathrm V.$$

Die Matrix ist symmetrisch.

(b) $D=7(56-4)+2(-16-10)-5(4+35)=364-52-195=117$. $D_1=9\cdot52=468$, $D_2=234$, $D_3=351$. Also $I_\mathrm A=4$ mA, $I_\mathrm B=2$ mA, $I_\mathrm C=3$ mA.

(c) $I_\mathrm a=I_\mathrm A-I_\mathrm B=2$ mA, $I_\mathrm b=I_\mathrm A-I_\mathrm C=1$ mA, $I_\mathrm c=I_\mathrm B=2$ mA, $I_\mathrm d=I_\mathrm C=3$ mA, $I_\mathrm e=I_\mathrm C-I_\mathrm B=1$ mA von $K_2$ nach $K_3$. Das ist die Tabelle aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), mit drei Gleichungen statt zwölf.
:::
:::

:::aufgabe Aufgabe 4 ★★ Umdrehen und kurzschließen
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Drehe im Rechenmodell nur Maschenstrom II um. Wie lauten $\mathbf Z$, die rechte Seite und $I_\mathrm{II}$?

</li>

<li>

Vorhersage: $R_4$ wird durch einen Draht ersetzt. Welche Einträge von $\mathbf Z$ werden null? Bestimme $I_\mathrm{III}$ ohne Gleichungssystem.

</li>

</ol>

:::loesung
(a) Zeile und Spalte II wechseln das Vorzeichen, die Diagonale bleibt:

$$\mathbf Z=\begin{pmatrix}5&4&0\\4&16&10\\0&10&15\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\-20\end{pmatrix}\mathrm V,\qquad I_\mathrm{II}=+1\,\mathrm{mA}.$$

In beiden gemeinsamen Zweigen laufen die Kreise nun gleichsinnig. Die rechte Seite bleibt, weil in Masche II keine Quelle sitzt.

(b) $Z_{23}=Z_{32}=0$, denn $R_4$ war der einzige gemeinsame Widerstand. Masche III enthält nur noch $R_5$ und $U_\mathrm{q5}$: $I_\mathrm{III}=-20\,\mathrm{V}/5\,\mathrm{k\Omega}=-4$ mA. Das ist die umgewandelte Stromquelle im Kurzschluss, der Kurzschlussstrom von 4 mA. Die Maschen I und II bleiben gekoppelt.
:::
:::

::::formelsammlung
**Umwandeln einer realen Stromquelle**

$$U_\mathrm q=I_\mathrm q\,R$$

Derselbe Widerstand $R$ liegt danach in Reihe. Erster Schritt des Maschenstromverfahrens.

**Matrixform des Maschenstromverfahrens**

$$\begin{pmatrix}Z_{11}&Z_{12}&\dots&Z_{1m}\\mathbb{Z}_{21}&Z_{22}&\dots&Z_{2m}\\\vdots&\vdots&\ddots&\vdots\\mathbb{Z}_{m1}&Z_{m2}&\dots&Z_{mm}\end{pmatrix} \begin{pmatrix}I_1\\I_2\\\vdots\\I_m\end{pmatrix}= \begin{pmatrix}U_\mathrm{q1}\\U_\mathrm{q2}\\\vdots\\U_{\mathrm qm}\end{pmatrix}$$

Kurz $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$. $Z_{\mu\mu}$ ist die Summe aller Widerstände der Masche $\mu$. $U_{\mathrm q\mu}$ ist die Summe der Quellenspannungen der Masche, positiv für jede Quelle, die den Maschenstrom antreibt; bei Spannungspfeilen vom Plus- zum Minuspol zählt ein Pfeil gegen den Umlauf positiv. Zeile $\mu$ ist die Maschenregel der Masche $\mu$, Einheit Ohm. Gilt für lineare Widerstände und feste Spannungsquellen.

**Koppelwiderstand**

$$Z_{\mu\nu}=Z_{\nu\mu}$$

Summe der Widerstände, die beide Maschen durchlaufen: positiv, wenn beide Ströme dort gleichsinnig fließen, negativ bei gegensinnigen Strömen, null ohne gemeinsamen Zweig. Die Symmetrie dient als Kontrolle beim Aufstellen.
::::

::::lernkarten
:::karte begriff Maschenstromverfahren
Was ist das Maschenstromverfahren, und in welchen Schritten berechnet man damit ein Netz?
---
Ein Verfahren mit $m$ Maschenströmen als Unbekannten, bei dem nur Maschenregeln aufzustellen sind. Schritte: reale Stromquellen in Spannungsquellen umwandeln, Maschenströme wählen, Matrix ablesen, lösen.
--- falsch
Ein Verfahren mit den $m$ Maschenströmen als Unbekannten, sodass nur Knotenregeln aufzustellen sind. Schritte: reale Spannungsquellen in Stromquellen umwandeln, Maschen wählen, Knotenregeln aufstellen, lösen.
--- falsch
Ein Verfahren mit allen $z$ Zweigströmen als Unbekannten, das für jede Masche eine Gleichung aufstellt. Schritte: Zweigströme eintragen, alle Maschenregeln aufschreiben, nacheinander einsetzen, lösen.
--- falsch
Ein Verfahren mit den $m$ Maschenströmen als Unbekannten, das Knoten- und Maschenregeln gemeinsam aufstellt. Schritte: alle Quellen entfernen, Maschen wählen, für jeden Knoten und jede Masche eine Gleichung, lösen.
:::
:::karte formel Matrixform des Maschenstromverfahrens
Welche Matrixgleichung erfüllen die Maschenströme eines Netzes, und was steht auf der Diagonale, daneben und rechts?
---
$\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$. $Z_{\mu\mu}$ ist die Summe aller Widerstände der Masche $\mu$, $Z_{\mu\nu}$ der Koppelwiderstand zu Masche $\nu$, $U_{\mathrm q\mu}$ die Summe der Quellenspannungen der Masche. Das gilt für lineare Widerstände und feste Spannungsquellen.
--- falsch
$\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$. $Z_{\mu\mu}$ ist der größte Widerstand der Masche $\mu$, $Z_{\mu\nu}$ die Summe ihrer übrigen Widerstände, $U_{\mathrm q\mu}$ die Summe der Quellenspannungen. Das gilt auch für Stromquellen, die man dafür nicht erst umwandeln muss.
--- falsch
$\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$. $Z_{\mu\mu}$ ist die Summe aller Widerstände der Masche $\mu$, $Z_{\mu\nu}$ die Summe aller Widerstände der Masche $\nu$, $U_{\mathrm q\mu}$ die Summe der Quellenströme der Masche $\mu$.
--- falsch
$\mathbf Z\,\mathbf U_\mathrm q=\mathbf I$. $Z_{\mu\mu}$ ist die Summe aller Widerstände der Masche $\mu$, $Z_{\mu\nu}$ der Koppelwiderstand, rechts stehen die gesuchten Maschenströme. Das gilt für lineare Widerstände und feste Quellen.
:::
:::karte begriff Widerstandsmatrix
Was beschreiben die Zeilen und die Spalten der Widerstandsmatrix $\mathbf Z$ im Maschenstromverfahren, und welche Einheit hat sie?
---
Zeile $\mu$ ist die Maschenregel der Masche $\mu$, mit der Summe ihrer Widerstände auf der Diagonale und gemeinsamen Widerständen daneben. Spalte $\nu$ gibt die Spannung an, die ein Ampere Maschenstrom $\nu$ in jeder Masche erzeugt, daher Ohm.
--- falsch
Zeile $\mu$ ist die Knotenregel des Knotens $\mu$: Auf der Diagonale steht die Summe der Widerstände am Knoten, daneben stehen die Widerstände zwischen zwei Knoten. Die Einheit ist Ohm, weil man Widerstände einträgt.
--- falsch
Zeile $\mu$ ist die Maschenregel der Masche $\mu$: Auf der Diagonale steht die Summe der Widerstände der Masche, daneben stehen ihre Kehrwerte, die Leitwerte. Spalte $\nu$ gibt an, welchen Strom ein Volt in Masche $\nu$ treibt, daher die Einheit Siemens.
--- falsch
Zeile $\mu$ ist die Maschenregel der Masche $\mu$: Auf der Diagonale stehen nur die Widerstände, die keine andere Masche durchläuft, daneben die gemeinsamen. Die Einheit ist Volt, weil jede Zeile eine Spannungsbilanz ist.
:::
:::karte begriff Koppelwiderstand
Was gibt der Koppelwiderstand $Z_{\mu\nu}$ zweier Maschen an, und welches Vorzeichen hat er?
---
Die Summe der Widerstände, die beide Maschen durchlaufen: positiv, wenn beide Maschenströme dort gleichsinnig fließen, negativ bei gegensinnigen Strömen, null ohne gemeinsamen Zweig. Es gilt $Z_{\mu\nu}=Z_{\nu\mu}$.
--- falsch
Die Summe der Widerstände, die beide Maschen durchlaufen. Er ist immer negativ, weil benachbarte Maschenströme im gemeinsamen Zweig stets gegeneinander laufen, und es gilt $Z_{\mu\nu}=-Z_{\nu\mu}$.
--- falsch
Die Summe aller Widerstände beider Maschen zusammen, auch der nicht gemeinsamen: positiv bei gleichsinnigen, negativ bei gegensinnigen Strömen im gemeinsamen Zweig, null ohne gemeinsamen Zweig. Es gilt $Z_{\mu\nu}=Z_{\nu\mu}$.
--- falsch
Die Summe der Widerstände, die beide Maschen durchlaufen: positiv bei gegensinnigen Strömen, negativ bei gleichsinnigen Strömen, null ohne gemeinsamen Zweig. Es gilt $Z_{\mu\nu}=Z_{\nu\mu}$.
:::
:::karte formel Umwandeln einer realen Stromquelle
Wie bringt man eine reale Stromquelle mit dem Quellenstrom $I_\mathrm q$ und dem Parallelwiderstand $R$ in eine Form, die das Maschenstromverfahren verarbeiten kann?
---
Man wandelt sie in eine reale Spannungsquelle um: $U_\mathrm q=I_\mathrm q\,R$, derselbe Widerstand liegt danach in Reihe. Im Rechenmodell wird so $U_\mathrm{q5}=I_\mathrm q\,R_5=20$ V.
--- falsch
Man wandelt sie in eine reale Spannungsquelle um: $U_\mathrm q=I_\mathrm q/R$, derselbe Widerstand liegt danach in Reihe. Im Rechenmodell wird so aus 4 mA und 5 k$\Omega$ eine Quelle mit 0,8 V.
--- falsch
Man wandelt sie in eine reale Spannungsquelle um: $U_\mathrm q=I_\mathrm q\,R$, derselbe Widerstand bleibt parallel zur neuen Quelle, weil er auch vorher parallel lag.
--- falsch
Man lässt den Parallelwiderstand weg und setzt eine ideale Spannungsquelle mit $U_\mathrm q=I_\mathrm q\,R$ ein, weil der Widerstand in der Quellenspannung schon enthalten ist.
:::
:::karte formel Quellenspannungen auf der rechten Seite
Mit welchem Vorzeichen geht eine Quellenspannung in die rechte Seite $U_{\mathrm q\mu}$ einer Maschengleichung ein?
---
Positiv für jede Quelle, die den Maschenstrom antreibt. Bei Spannungspfeilen vom Plus- zum Minuspol zählt deshalb ein Pfeil gegen den Umlauf positiv, ein Pfeil mit dem Umlauf negativ.
--- falsch
Positiv für jede Quelle, die den Maschenstrom antreibt. Bei Spannungspfeilen vom Plus- zum Minuspol zählt deshalb ein Pfeil mit dem Umlauf positiv, ein Pfeil gegen den Umlauf negativ.
--- falsch
Immer positiv, weil jede Quelle Energie in die Masche liefert. Das Vorzeichen des Spannungspfeils spielt erst bei der Berechnung der Zweigströme eine Rolle.
--- falsch
Negativ für jede Quelle, die den Maschenstrom antreibt, weil sie beim Wechsel auf die rechte Seite das Vorzeichen tauscht. Quellen, die gegen den Umlauf wirken, zählen positiv.
:::
:::karte herleitung Von der Maschenregel zur Matrix
Leite aus der Maschenregel der Masche $\mu$ die Einträge der Widerstandsmatrix her und zeige, dass $\mathbf Z$ symmetrisch ist.
---
Für die Masche $\mu$ ist die Summe aller $R_a\,I_a$ gleich der treibenden Spannung $U_{\mathrm q\mu}$, weil die Quellen auf die rechte Seite wechseln. Dabei ist $I_a$ der Strom in $R_a$, gezählt im Umlaufsinn von $\mu$.
---
Jeder dieser Ströme ist $I_a=I_\mu+\sum_{\nu\neq\mu}\sigma_{a\nu}\,I_\nu$, weil sich ein Zweigstrom aus dem eigenen Maschenstrom und den Maschenströmen der Nachbarn zusammensetzt.
---
Ordnet man nach Maschenströmen, steht vor $I_\mu$ die Summe aller $R_a$ der Masche, weil der eigene Strom durch alle ihre Widerstände läuft.
---
Vor $I_\nu$ steht $\sum_a\sigma_{a\nu}R_a$, nur über die gemeinsamen Widerstände, weil der fremde Maschenstrom nur dort fließt.
---
Masche $\nu$ erhält denselben Widerstand mit demselben Vorzeichen, weil gleichsinnig eine Beziehung zwischen zwei Maschen ist. Deshalb ist $\mathbf Z$ symmetrisch.
:::
:::karte zusammenhang Symmetrie als Kontrolle
Warum ist die Widerstandsmatrix symmetrisch, und wozu nutzt man das beim Aufstellen?
---
Ein gemeinsamer Widerstand steht in beiden Maschengleichungen mit demselben Vorzeichen, denn gleichsinnig ist eine Beziehung zwischen zwei Maschen. Ein Fehler beim Aufstellen zerstört die Symmetrie meist, sie dient also als Kontrolle.
--- falsch
Weil jede Masche gleich viele Widerstände enthält, sodass alle Zeilen dieselbe Summe haben. Ein Fehler beim Aufstellen ändert eine Zeilensumme, deshalb vergleicht man die Summen der Zeilen zur Kontrolle.
--- falsch
Weil man alle Maschenströme im Uhrzeigersinn wählt. Mit anderen Richtungen ist $\mathbf Z$ nicht mehr symmetrisch, denn dann wechseln einzelne Einträge ihr Vorzeichen; die Symmetrie taugt also nur bei gleicher Drehrichtung als Kontrolle.
--- falsch
Weil die Quellenspannungen auf beide Maschen gleich verteilt werden. Die Symmetrie hängt deshalb von den Quellen ab und taugt nicht als Kontrolle für die Widerstände.
:::
:::karte zusammenhang Negative Nebendiagonale
Warum sind alle Einträge neben der Diagonale von $\mathbf Z$ negativ, wenn alle Maschenströme im Uhrzeigersinn laufen?
---
Benachbarte Kreise gleicher Drehrichtung laufen im gemeinsamen Zweig gegeneinander. Der fremde Maschenstrom zählt dort gegen den eigenen Umlauf, also steht der gemeinsame Widerstand mit Minus da.
--- falsch
Weil im Uhrzeigersinn alle Spannungspfeile gegen den Umlauf zeigen. Die Widerstände außerhalb der Diagonale wechseln dadurch das Vorzeichen, die auf der Diagonale nicht.
--- falsch
Benachbarte Kreise gleicher Drehrichtung laufen im gemeinsamen Zweig in dieselbe Richtung. Der fremde Strom verstärkt dort den eigenen, und das Minus gleicht diese Verdopplung im gemeinsamen Widerstand aus.
--- falsch
Weil Koppelwiderstände immer negativ sind, gleich welche Richtung man wählt. Das Minus kennzeichnet Widerstände, die zu zwei Maschen gehören, nicht eine Stromrichtung.
:::
:::karte zusammenhang Maschenstrom umdrehen
Was ändert sich am Gleichungssystem und an den Ergebnissen, wenn man die Richtung eines einzelnen Maschenstroms umdreht?
---
Seine Zeile und seine Spalte wechseln das Vorzeichen, die Diagonale bleibt, und der Wert des Stroms wechselt ebenfalls das Vorzeichen. Die Zweigströme ändern sich nicht.
--- falsch
Nur seine Spalte wechselt das Vorzeichen, weil sie zu dieser Unbekannten gehört, die Zeile bleibt. Der Wert des Stroms wechselt das Vorzeichen, und die Zweigströme ändern sich mit.
--- falsch
Seine Zeile und seine Spalte wechseln das Vorzeichen, auch der Eintrag auf der Diagonale. Der Wert des Stroms bleibt gleich, weil nur die Bezeichnung der Richtung geändert wurde.
--- falsch
Die Matrix bleibt gleich, nur die rechte Seite wechselt das Vorzeichen. Der Strom wechselt sein Vorzeichen, und in allen Zweigen seiner Masche dreht sich der Zweigstrom um.
:::
:::karte zusammenhang Ideale Stromquelle
Wie behandelt man im Maschenstromverfahren eine ideale Stromquelle, die sich nicht in eine Spannungsquelle umwandeln lässt?
---
Man legt die Maschen so, dass nur eine durch die Stromquelle läuft. Ihr Maschenstrom ist dann bekannt, und ihre Maschengleichung lässt man weg, weil sie die unbekannte Spannung der Quelle enthält: eine Unbekannte und eine Gleichung weniger.
--- falsch
Man setzt für die Stromquelle eine Spannungsquelle mit $U_\mathrm q=0$ ein, weil eine ideale Stromquelle keinen Innenwiderstand hat. Der Maschenstrom durch sie bleibt dann eine gewöhnliche Unbekannte, und alle Gleichungen bleiben stehen.
--- falsch
Man legt die Maschen so, dass möglichst viele durch die Stromquelle laufen. Ihr Strom verteilt sich dann auf diese Maschen, und für jede Masche stellt man die Maschenregel wie üblich auf, die Quelle steht rechts.
--- falsch
Man nimmt einen sehr großen Parallelwiderstand an und wandelt um. $U_\mathrm q=I_\mathrm q\,R$ wird dabei zwar groß, das Ergebnis ist aber genau, solange man bei der Rechnung genug Stellen mitnimmt.
:::
:::karte zusammenhang Draht als gemeinsamer Zweig
Was passiert mit der Kopplung zweier Maschen, wenn man ihren einzigen gemeinsamen Widerstand durch einen Draht ersetzt?
---
Der Koppelwiderstand wird null, die Maschen sind entkoppelt. Ein Draht trennt beide Seiten, denn seine Spannung ist null, was immer durch ihn fließt.
--- falsch
Die Kopplung wird unendlich stark, weil der Draht beide Maschen kurzschließt. Beide Maschenströme werden gleich, und eine Unbekannte fällt weg.
--- falsch
Der Koppelwiderstand wird null, aber die Maschen bleiben gekoppelt, weil der Draht den Strom beider Maschen führt und die Ströme so aneinander bindet.
--- falsch
Der Koppelwiderstand wird null, und beide Maschenströme werden null, weil der Draht den ganzen Strom an den übrigen Widerständen vorbeileitet.
:::
::::
