---
title: Stufe 9: Zusammenschaltung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1161100
summary: Stufe 8 hat gezeigt, dass die Kette zur A-Form passt.
tags: 
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Stufe [8](kettenform.html#stufe-8) hat gezeigt, dass die Kette zur A-Form passt. Diese Stufe beantwortet die Frage allgemein: Welche Form passt zu welcher Zusammenschaltung?
:::

**Die Idee.** Verbindet man zwei Zweitore, teilen sie an jedem Tor entweder den Strom (Reihe) oder die Spannung (parallel). Die geteilte Größe ist für beide Teile gleich, die andere summiert sich. Das sagt, welche Form passt: Die gemeinsamen Größen gehören zu den Ursachen, die summierten zu den Wirkungen. Dann steht auf der rechten Seite für beide Teile dasselbe, und die Parameter addieren sich.

:::satz Satz 9.1 (Zusammenschaltung zweier Zweitore)
<span class="anker" id="satz-9-1"></span>

Bleibt in beiden Teilen die Torbedingung erhalten, gilt:

| Schaltung (Tor 1, Tor 2) | gleich für beide | summiert sich | Regel |
|---|---|---|---|
| Reihe, Reihe | $I_1$, $I_2$ | $U_1$, $U_2$ | $\mathbf Z=\mathbf Z'+\mathbf Z''$ |
| parallel, parallel | $U_1$, $U_2$ | $I_1$, $I_2$ | $\mathbf Y=\mathbf Y'+\mathbf Y''$ |
| Reihe, parallel | $I_1$, $U_2$ | $U_1$, $I_2$ | $\mathbf H=\mathbf H'+\mathbf H''$ |
| Kette | $U_2'=U_1''$, $-I_2'=I_1''$ | nichts | $\mathbf A=\mathbf A'\mathbf A''$ |
:::

⁠**So liest man das:** Das Schaltbild sagt, welche Größen gleich sind, die Tabelle sagt, welche Form sich addiert (Abb. [11](#abb-11)). Daher hat die H-Matrix ihren zweiten Namen Reihenparallelmatrix. Die Schaltung „parallel, Reihe“ ist der fehlende Fall. Zu ihr gehört die umgekehrte Hybridform mit $U_1$ und $I_2$ als Ursachen, die man mit der Inversen von $\mathbf H$ erhält.

:::herleitung Warum sich die Parameter addieren
In Reihe, Reihe führen beide Teile dieselben Ströme: $\mathbf I'=\mathbf I''=\mathbf I$. Also ist $\mathbf U=\mathbf U'+\mathbf U''=\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$. Parallel gilt dasselbe mit vertauschten Rollen. Bei Reihe, parallel ist die Ursachenspalte $(I_1,\,U_2)$ für beide gleich, die Wirkungsspalte $(U_1,\,I_2)$ ist die Summe beider Wirkungsspalten.
:::

:::abbildung et1/k6zusammen 11
Drei Zusammenschaltungen. Links Reihe, Reihe: gleiche Ströme, Z addiert sich. Mitte parallel, parallel: gleiche Spannungen, Y addiert sich. Rechts Reihe, parallel: gleiches $I_1$ und $U_2$, H addiert sich.
:::

::::beispiel
⁠**Reihe:** Das T-Zweitor selbst ist eine Reihenschaltung aus zwei getrennten Längswiderständen und einem Querwiderstand:

$$\mathbf Z=\begin{pmatrix}15&0\\0&20\end{pmatrix}\Omega+\begin{pmatrix}20&20\\20&20\end{pmatrix}\Omega=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**Parallel:** Legt man einen Widerstand von 100 $\Omega$ von Klemme 1 nach Klemme 2 über das T-Zweitor, kommt zu $\mathbf Y$ der Längsleitwert hinzu:

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}+\begin{pmatrix}10&-10\\-10&10\end{pmatrix}\mathrm{mS}=\begin{pmatrix}50&-30\\-30&45\end{pmatrix}\mathrm{mS}.$$

Kontrolle: Mit kurzgeschlossenem Tor 2 ist $1/Y_{11}=20\,\Omega$, und direkt ist das $25\,\Omega\parallel100\,\Omega=20\,\Omega$.

**Wann die Regel versagt.** Die Regeln setzen voraus, dass jedes Teil für sich die Torbedingung behält. Bei der Kette ist sie sicher, denn das hintere Teil samt Last ist für das vordere ein Zweipol. Zwei Dreipole mit gemeinsamer Masseleitung darf man ebenfalls parallel schalten: Bei ihnen fallen 1$'$ und 2$'$ in einem Punkt zusammen, es zählt nur die Summe der Rückströme. Bei der Reihe ist Vorsicht nötig. Setzt man zwei T-Zweitore mit ihren Masseleitungen übereinander, schließt die Masseleitung des oberen die beiden oberen Klemmen des unteren kurz. Ein Teil des Stroms von Tor 1 läuft dann im unteren T durch $R_\mathrm{c}$, die Torbedingung bricht. Statt $Z_{11}=70\,\Omega$ misst man $35\,\Omega+15\,\Omega\parallel20\,\Omega+20\,\Omega=63{,}6\,\Omega$. Abhilfe: Man spiegelt das untere T, sodass nur die beiden Masseleitungen verbunden sind. Dann bleiben beide Dreipole, und die Regel gibt die richtigen 70 $\Omega$.

⁠**Grenzfall:** Zwei gleiche Zweitore parallel haben die halbe Matrix $\mathbf Z$, gleiche Widerstände parallel ergeben den halben Widerstand. In Reihe verdoppelt sich $\mathbf Z$.

:::frage Warum addiert sich bei der Reihe nicht auch die Kettenmatrix?
Weil bei der Reihe $I_1$ für beide gleich ist, $U_1$ aber nicht. In der Kettenform steht $U_1$ zusammen mit $I_1$ auf der linken Seite, und rechts stünden die Ausgangsgrößen. Für beide Teile wäre die rechte Spalte verschieden, und nichts ließe sich zusammenfassen.
:::

:::aufgabe Aufgabe 9 ★★ Welche Form passt?
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Zwei gleiche T-Zweitore werden parallel, parallel verbunden. Wie groß ist $\mathbf Z$ der Schaltung? Warum ist die Rechnung hier zulässig?

</li>

<li>

Zwei gleiche T-Zweitore, das untere gespiegelt, liegen in Reihe, Reihe. Wie groß ist $\mathbf Z$?

</li>

<li>

Die Hybridmatrix des T-Zweitors ist bekannt. Wie groß ist $\mathbf H$ für zwei gleiche Zweitore in Reihe, parallel (Torbedingung vorausgesetzt)?

</li>

<li>

Zum T-Zweitor kommt ein Querwiderstand von 10 $\Omega$ in Reihe, Reihe. Welches $\mathbf Z$ ergibt sich, und welche T-Schaltung gehört dazu?

</li>

</ol>

:::loesung
(a) $\mathbf Y$ verdoppelt sich, also halbiert sich $\mathbf Z$: $Z_{11}=17{,}5\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=20\,\Omega$. Beide sind Dreipole mit gemeinsamer Masseleitung, die Tore bleiben Tore. (b) $\mathbf Z$ verdoppelt sich: 70, 40, 40, 80 $\Omega$. (c) $\mathbf H$ verdoppelt sich: $H_{11}=50\,\Omega$, $H_{12}=1$, $H_{21}=-1$, $H_{22}=50$ mS. (d) $Z_{11}=45\,\Omega$, $Z_{12}=Z_{21}=30\,\Omega$, $Z_{22}=50\,\Omega$. Das ist ein T mit $R_\mathrm{a}=15\,\Omega$, $R_\mathrm{b}=30\,\Omega$, $R_\mathrm{c}=20\,\Omega$: Der Querwiderstand liegt in Reihe zu $R_\mathrm{b}$, weil er denselben Summenstrom führt.
:::
:::

::::formelsammlung
**Reihe, Reihe**

$$\mathbf Z=\mathbf Z'+\mathbf Z''$$

Gleich für beide Teile sind $I_1$, $I_2$; es summieren sich $U_1$, $U_2$.

**Parallel, parallel**

$$\mathbf Y=\mathbf Y'+\mathbf Y''$$

Gleich für beide Teile sind $U_1$, $U_2$; es summieren sich $I_1$, $I_2$.

**Reihe, parallel**

$$\mathbf H=\mathbf H'+\mathbf H''$$

Gleich für beide Teile sind $I_1$, $U_2$; es summieren sich $U_1$, $I_2$. Daher heißt die H-Matrix auch Reihenparallelmatrix. Zu parallel, Reihe gehört die umgekehrte Hybridform, die man mit der Inversen von $\mathbf H$ erhält.

**Kette**

$$\mathbf A=\mathbf A'\mathbf A''$$

Gleich sind $U_2'=U_1''$ und $-I_2'=I_1''$, nichts summiert sich. Alle Regeln setzen voraus, dass jedes Teil für sich die Torbedingung behält. Sicher ist das bei der Kette und bei Dreipolen mit gemeinsamer Masseleitung in parallel, parallel.
::::

::::lernkarten
:::karte formel Reihe, Reihe
Welche Matrix addiert sich, wenn zwei Zweitore an beiden Toren in Reihe geschaltet sind, und warum gerade diese?
---
$\mathbf Z=\mathbf Z'+\mathbf Z''$. In Reihe führen beide Teile dieselben Ströme $I_1$, $I_2$, und die Spannungen summieren sich. Die Ströme sind die Ursachen der Z-Form.
--- falsch
$\mathbf Y=\mathbf Y'+\mathbf Y''$. In Reihe liegen an beiden Teilen dieselben Spannungen, und die Ströme summieren sich; die Spannungen sind die Ursachen der Y-Form.
--- falsch
$\mathbf A=\mathbf A'\mathbf A''$. In Reihe fließt der Strom erst durch das eine, dann durch das andere Zweitor, wie bei jeder Hintereinanderschaltung von Zweitoren.
--- falsch
$\mathbf Z=\mathbf Z'+\mathbf Z''$. In Reihe liegen an beiden Teilen dieselben Spannungen, und Widerstände in Reihe addieren sich immer, gleich in welcher Form.
:::
:::karte formel Parallel, parallel
Welche Matrix addiert sich, wenn zwei Zweitore an beiden Toren parallel geschaltet sind, und warum gerade diese?
---
$\mathbf Y=\mathbf Y'+\mathbf Y''$. Parallel liegen an beiden Teilen dieselben Spannungen $U_1$, $U_2$, und die Ströme summieren sich. Die Spannungen sind die Ursachen der Y-Form.
--- falsch
$\mathbf Z=\mathbf Z'+\mathbf Z''$. Parallel führen beide Teile dieselben Ströme, und die Spannungen summieren sich; die Ströme sind die Ursachen der Z-Form.
--- falsch
$\mathbf Y=\mathbf Y'\mathbf Y''$. Parallel geschaltete Leitwerte multiplizieren sich, deshalb ergibt sich die Y-Matrix der Schaltung als Produkt der beiden Matrizen.
--- falsch
$\mathbf H=\mathbf H'+\mathbf H''$. Parallel ist an einem Tor der Strom gleich und am anderen die Spannung, genau wie bei den Ursachen der H-Form.
:::
:::karte formel Reihe, parallel
Welche Matrix addiert sich bei der Schaltung Reihe am Eingang, parallel am Ausgang, und welchen zweiten Namen hat sie deshalb?
---
$\mathbf H=\mathbf H'+\mathbf H''$. Gleich für beide Teile sind $I_1$ und $U_2$, die Ursachen der H-Form; $U_1$ und $I_2$ summieren sich. Daher heißt die H-Matrix auch Reihenparallelmatrix.
--- falsch
$\mathbf A=\mathbf A'\mathbf A''$. Gleich für beide Teile sind $U_2$ und $-I_2$, die Ursachen der Kettenform, und nichts summiert sich. Daher heißt die Kettenmatrix auch Reihenparallelmatrix.
--- falsch
$\mathbf H=\mathbf H'+\mathbf H''$. Gleich für beide Teile sind $U_1$ und $I_2$, die sich bei dieser Schaltung nicht ändern. Daher heißt die H-Matrix auch Reihenparallelmatrix.
--- falsch
Keine Matrix addiert sich, denn das Reihentor verlangt die Z-Form und das Paralleltor die Y-Form. Deshalb heißt die gemischte Rechnung Reihenparallelverfahren.
:::
:::karte zusammenhang Welche Form sich addiert
Nach welcher Regel erkennt man, welche Parameterform sich bei einer Zusammenschaltung zweier Zweitore addiert?
---
An jedem Tor teilen die Teile entweder den Strom (Reihe) oder die Spannung (parallel). Die geteilten Größen sind die Ursachen, die summierten die Wirkungen; dann steht rechts für beide Teile dasselbe.
--- falsch
Die summierten Größen gehören zu den Ursachen, die gemeinsamen zu den Wirkungen. Dann addieren sich die Parameter, weil sich auf der rechten Seite die Ursachen beider Teile addieren und die Wirkungen gleich bleiben.
--- falsch
Es addiert sich immer die Z-Form, weil Widerstände bei jeder Zusammenschaltung zusammengezählt werden. Die anderen Formen rechnet man danach aus der Summe um.
--- falsch
Es addiert sich die Form, deren Parameter die kleinsten Werte haben, weil kleine Parameter beim Zusammenschalten die geringsten Rechenfehler erzeugen.
:::
:::karte zusammenhang Kettenmatrix bei der Reihe
Warum addiert sich bei der Schaltung Reihe, Reihe nicht die Kettenmatrix?
---
Bei der Reihe ist $I_1$ für beide Teile gleich, $U_1$ aber nicht. In der Kettenform stehen $U_1$ und $I_1$ zusammen links; die rechten Spalten beider Teile wären verschieden.
--- falsch
Sie addiert sich doch. Die Kettenmatrix addiert sich bei jeder Zusammenschaltung zweier Zweitore, nur bei der Kette selbst multipliziert sie sich stattdessen.
--- falsch
Weil die Kettenmatrix Parameter ohne Einheit enthält. Matrizen lassen sich nur addieren, wenn alle ihre Elemente dieselbe Einheit haben, wie bei Z oder Y.
--- falsch
Weil bei der Reihe die Ausgangsgrößen beider Teile gleich sind, die Eingangsgrößen aber nicht. Die Kettenform bräuchte gleiche Eingangsgrößen auf der rechten Seite.
:::
:::karte zusammenhang Voraussetzung der Additionsregeln
Unter welcher Voraussetzung gelten die Regeln für zusammengeschaltete Zweitore, und wann ist sie sicher erfüllt?
---
Jedes Teil muss für sich die Torbedingung behalten. Sicher ist das bei der Kette, weil das hintere Teil samt Last für das vordere ein Zweipol ist, und bei Dreipolen mit gemeinsamer Masseleitung parallel.
--- falsch
Beide Teile müssen gleich sein. Bei verschiedenen Zweitoren gelten die Regeln nur näherungsweise, bei gleichen dagegen immer, gleich wie man sie miteinander verbindet.
--- falsch
Beide Teile müssen erdsymmetrisch sein. Zweitore mit Masseleitung darf man weder in Reihe noch parallel zusammenschalten, sondern nur in Kette, weil sonst Ströme über die gemeinsame Masse an den Toren vorbei abfließen.
--- falsch
Jedes Teil muss für sich die Torbedingung behalten. Sicher ist das bei Reihe, Reihe, weil dort derselbe Strom nacheinander durch beide Teile fließt und nirgends abzweigen kann.
:::
:::karte zusammenhang Zwei T-Zweitore in Reihe
Was geht schief, wenn man zwei T-Zweitore mit ihren Masseleitungen übereinander in Reihe, Reihe schaltet, und wie hilft man ab?
---
Die Masseleitung des oberen schließt die oberen Klemmen des unteren kurz, ein Teil des Stroms läuft durch dessen $R_\mathrm{c}$. Die Torbedingung bricht: $63{,}6\,\Omega$ statt $70\,\Omega$. Abhilfe: das untere T spiegeln.
--- falsch
Nichts, denn die Regel $\mathbf Z=\mathbf Z'+\mathbf Z''$ gilt bei Reihe, Reihe immer, weil beide Teile denselben Strom führen. Man misst wie berechnet $Z_{11}=70\,\Omega$, eine Abhilfe ist nicht nötig.
--- falsch
Die Masseleitungen der beiden T liegen dann parallel und halbieren so den wirksamen Querwiderstand. Abhilfe: einen der beiden Querwiderstände doppelt so groß wählen.
--- falsch
Die Ströme in den beiden Masseleitungen heben sich gegenseitig auf, und $Z_{11}$ wird null. Abhilfe: zwischen die beiden T-Zweitore einen zusätzlichen Längswiderstand setzen, der die Masseleitungen trennt.
:::
:::karte zusammenhang Gleiche Zweitore zusammengeschaltet
Was geschieht mit der Z-Matrix, wenn man zwei gleiche Zweitore parallel, parallel oder in Reihe, Reihe schaltet und die Torbedingung erhalten bleibt?
---
Parallel verdoppelt sich $\mathbf Y$, also halbiert sich $\mathbf Z$, so wie gleiche Widerstände parallel den halben Widerstand ergeben. In Reihe verdoppelt sich $\mathbf Z$.
--- falsch
Parallel verdoppelt sich $\mathbf Z$, in Reihe halbiert es sich, weil in der Parallelschaltung doppelt so viel Strom fließt wie in einem einzelnen Zweitor allein.
--- falsch
Parallel halbieren sich nur $Z_{11}$ und $Z_{22}$, die Transfergrößen bleiben gleich, weil sich die Kopplung der Tore durch das Verbinden nicht ändert.
--- falsch
In beiden Fällen bleibt $\mathbf Z$ gleich, weil zwei gleiche Zweitore an ihren Toren dasselbe Verhalten zeigen wie ein einzelnes Zweitor dieser Art.
:::
:::karte zusammenhang Parallel, Reihe
Welche Form gehört zur Schaltung parallel am Eingang, Reihe am Ausgang?
---
Die umgekehrte Hybridform mit $U_1$ und $I_2$ als Ursachen, weil diese beiden Größen dann für beide Teile gleich sind. Man erhält sie mit der Inversen von $\mathbf H$.
--- falsch
Die Hybridform $\mathbf H$ selbst, weil auch hier ein Tor in Reihe und eines parallel liegt. Auf die Reihenfolge der beiden Tore kommt es dabei nicht an.
--- falsch
Keine: Für parallel, Reihe gibt es keine passende Form, man muss die beiden Teile einzeln rechnen und die Ergebnisse von Hand verbinden.
--- falsch
Die Kettenform, weil der Ausgang des einen Teils in Reihe am Eingang des anderen liegt und die Kettenmatrix dann ein Produkt ist.
:::
:::karte herleitung Warum sich die Parameter addieren
Leite her, warum sich bei der Schaltung Reihe, Reihe die Z-Matrizen der beiden Teile addieren, und übertrage das Ergebnis auf die anderen Schaltungen.
---
In Reihe, Reihe führen beide Teile dieselben Ströme, $\mathbf I'=\mathbf I''=\mathbf I$, weil an jedem Tor derselbe Strom nacheinander durch beide Teile fließt.
---
Die Torspannungen addieren sich, $\mathbf U=\mathbf U'+\mathbf U''$, weil die Teile an jedem Tor in Reihe liegen.
---
Mit der Z-Form beider Teile folgt $\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$, weil man die gemeinsame Ursachenspalte $\mathbf I$ ausklammern kann.
---
Parallel gilt dasselbe mit vertauschten Rollen, also $\mathbf Y=\mathbf Y'+\mathbf Y''$, weil dort die Spannungen gemeinsam sind und sich die Ströme addieren.
---
Bei Reihe, parallel ist die Ursachenspalte $(I_1,\,U_2)$ für beide gleich und die Wirkungsspalte $(U_1,\,I_2)$ die Summe beider Wirkungsspalten, also $\mathbf H=\mathbf H'+\mathbf H''$, weil $I_1$ am Reihentor und $U_2$ am Paralleltor geteilt werden.
:::
::::
