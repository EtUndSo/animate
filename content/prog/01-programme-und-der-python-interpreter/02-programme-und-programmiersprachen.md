---
title: Programme und Programmiersprachen
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020200
summary: Ein Rechner tut nur, was man ihm Schritt für Schritt vorgibt.
tags: Programm, Anweisung, Prozessor, Maschinenbefehl, Maschinencode, Programmiersprache, Syntax, Semantik
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Rechner tut nur, was man ihm Schritt für Schritt vorgibt. Dieser Abschnitt klärt, was ein Programm ist, welche Befehle der Prozessor eines Rechners versteht und warum man Programme in einer eigenen Sprache aufschreibt.
:::

### Das Programm

<span class="anker" id="stufe-1-1"></span>

Ein Rechner kann sehr schnell rechnen, aber er entscheidet nichts von sich aus. Bevor er etwas Nützliches tut, muss ihm jemand genau sagen, welche Schritte er in welcher Reihenfolge ausführen soll.

**Ein Rezept.** Ein Kochrezept ist eine solche Schrittfolge: „Wasser zum Kochen bringen. Nudeln hineingeben. Neun Minuten warten. Abgießen.“ Wer es befolgt, muss nicht wissen, warum Nudeln neun Minuten brauchen. Er muss nur jeden Schritt eindeutig verstehen und die Reihenfolge einhalten.

**Wissen, was etwas ist, und wissen, wie man es findet.** Der Satz „Die Wurzel aus 2 ist die positive Zahl, die mit sich selbst multipliziert 2 ergibt“ beschreibt $\sqrt2$ vollständig. Er sagt aber nicht, wie man diese Zahl findet. Ein Rezept, das die Zahl Schritt für Schritt liefert, ist Wissen einer anderen Art: Es beschreibt ein Verfahren. Ein Rechner kann nur mit Wissen dieser zweiten Art etwas anfangen.

:::definition Definition 1.1 (Programm)
<span class="anker" id="satz-1-1"></span>

Ein __Programm__ ist eine Folge von eindeutig beschriebenen Arbeitsschritten, die ein Rechner der Reihe nach ausführt, ohne nachzufragen.
:::

Einen einzelnen Arbeitsschritt eines Programms nennt man __Anweisung__.

::::beispiel ein Rezept für die Wurzel aus 2
Das folgende Rezept heißt Heron-Verfahren, nach Heron von Alexandria, der es im ersten Jahrhundert beschrieben hat. Es braucht nur die Grundrechenarten:

<ol>

<li>

Wähle eine erste Schätzung $g$, zum Beispiel $g=1$.

</li>

<li>

Berechne $2/g$ und bilde den Mittelwert $\frac12\bigl(g+2/g\bigr)$. Dieser Mittelwert ist die neue Schätzung $g$.

</li>

<li>

Wiederhole Schritt 2, bis sich $g$ in den Stellen, die dich interessieren, nicht mehr ändert.

</li>

</ol>

Von Hand mit einem Taschenrechner ergibt sich:

| Durchgang | $g$ | $2/g$ | neue Schätzung $\frac12\bigl(g+2/g\bigr)$ |
|---|---|---|---|
| 1 | $1$ | $2$ | $1{,}5$ |
| 2 | $1{,}5$ | $1{,}333\,333$ | $1{,}416\,667$ |
| 3 | $1{,}416\,667$ | $1{,}411\,765$ | $1{,}414\,216$ |
| 4 | $1{,}414\,216$ | $1{,}414\,211$ | $1{,}414\,214$ |

Nach drei Durchgängen ist $g=1{,}414\,216$ und $g^2=2{,}000\,006$, nach vier Durchgängen stimmen die ersten sechs Nachkommastellen mit $\sqrt2=1{,}414\,213\,56\ldots$ überein. Abbildung [1](#abb-1) zeigt, was dabei geschieht: $g$ und $2/g$ liegen immer auf verschiedenen Seiten von $\sqrt2$, und ihr Mittelwert rückt jedes Mal näher heran.

:::abbildung prog/k1heron 1
Das Heron-Verfahren für $\sqrt2$ auf dem Zahlenstrahl. In jedem Durchgang liegen die Schätzung $g$ (blau) und $2/g$ (orange) auf verschiedenen Seiten von $\sqrt2$, weil ihr Produkt 2 ist. Ihr Mittelwert (Strich) wird die neue Schätzung. Der Abstand der beiden Punkte schrumpft von $1$ über $0{,}17$ auf $0{,}005$; im dritten Durchgang liegen sie in dieser Darstellung fast aufeinander.
:::
::::

Wer das Rezept befolgt, muss nicht wissen, warum es funktioniert. Jeder Schritt ist so eindeutig, dass auch eine Maschine ihn ausführen kann. Genau das macht aus einem Rezept ein Programm.

⁠**Kurz gesagt:** Ein Programm ist ein Rezept aus eindeutigen Schritten, das ein Rechner ohne Rückfrage ausführen kann.

:::hintergrund Warum das Rezept zum Ziel führt
Ist eine Schätzung zu groß, $g>\sqrt2$, dann ist $2/g$ zu klein, denn das Produkt $g\cdot(2/g)$ ist immer 2. Die Wurzel liegt also zwischen $2/g$ und $g$, und der Mittelwert der beiden ist ein vernünftiger nächster Versuch.

Wie schnell das geht, zeigt eine kleine Rechnung. Für die neue Schätzung $g'=\frac12(g+2/g)$ gilt

$$g'^2-2=\frac{g^2+4+4/g^2}{4}-2=\frac{g^2-4+4/g^2}{4}=\frac{(g-2/g)^2}{4}=\frac{(g^2-2)^2}{4g^2}.$$

Daraus folgen zwei Dinge:

<ul>

<li>

Die rechte Seite ist nie negativ. Ab dem ersten Durchgang ist jede Schätzung also mindestens so groß wie $\sqrt2$, und $2/g$ liegt darunter.

</li>

<li>

Der Fehler $g^2-2$ wird in jedem Durchgang quadriert und zusätzlich durch $4g^2$ geteilt, ab dem zweiten Durchgang also durch mindestens 8. Mit $g=1$ beginnend ist $g^2-2$ nacheinander $0{,}25$, dann $0{,}0069$, dann $0{,}000\,006$, dann $4{,}5\cdot10^{-12}$. Die Zahl der richtigen Stellen verdoppelt sich ungefähr in jedem Durchgang.

</li>

</ul>

Wer das Newton-Verfahren aus der Mathematik kennt: Das Heron-Verfahren ist das Newton-Verfahren für die Nullstelle von $f(x)=x^2-2$. Dessen Schritt $x-f(x)/f'(x)=x-\frac{x^2-2}{2x}$ ist genau $\frac12(x+2/x)$.
:::

### Was der Prozessor versteht: Maschinenbefehle

<span class="anker" id="stufe-1-2"></span>

Die Schritte eines Programms führt im Rechner der __Prozessor__ aus, ein Chip, der rechnet und den Ablauf steuert. Seine Befehle sind viel einfacher als „bilde den Mittelwert von $g$ und $2/g$“.

**Ein sehr wörtlicher Arbeiter.** Man kann sich den Prozessor als einen äußerst schnellen Arbeiter mit winzigem Wortschatz vorstellen. Er versteht Befehle wie „hole die Zahl aus Speicherplatz 12“, „addiere zwei Zahlen“, „teile zwei Zahlen“ oder „mach bei Befehl 3 weiter“. Mehr kann er nicht, aber davon schafft er Milliarden in jeder Sekunde. (Das Bild ist eine Vorstellungshilfe; der Prozessor versteht nichts im menschlichen Sinn, sondern schaltet.)

:::definition Definition 1.2 (Maschinenbefehl)
<span class="anker" id="satz-1-2"></span>

Ein __Maschinenbefehl__ ist ein Befehl, den der Prozessor unmittelbar ausführen kann. Er steht im Speicher als Zahl; an dieser Zahl erkennt die Schaltung des Prozessors, was zu tun ist.
:::

Ein Programm, das nur aus Maschinenbefehlen besteht, heißt __Maschinencode__.

::::beispiel
Schritt 2 des Heron-Rezepts zerfällt in Maschinenbefehle etwa so:

<ol>

<li>

Hole die Zahl $g$ aus dem Speicher.

</li>

<li>

[Teile 2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html) durch diese Zahl.

</li>

<li>

Addiere $g$ zum Ergebnis.

</li>

<li>

Teile das Ergebnis durch 2.

</li>

<li>

Lege das Ergebnis als neues $g$ im Speicher ab.

</li>

</ol>

Jeder dieser Befehle ist im Speicher eine Zahl. Welche Zahl welchen Befehl bedeutet, ist für jede Familie von Prozessoren anders festgelegt. Die Prozessoren der meisten PCs verstehen andere Zahlen als die eines Smartphones oder eines Raspberry Pi. Maschinencode für den einen läuft auf dem anderen deshalb nicht.
::::

⁠**Kurz gesagt:** Der Prozessor versteht nur sehr einfache Maschinenbefehle, die als Zahlen im Speicher stehen, und jede Prozessorfamilie hat ihre eigenen.

:::hintergrund Warum der Prozessor nur so einfache Befehle kennt
Jeder Maschinenbefehl muss als Schaltung gebaut sein. Ein Rechenwerk aus Logikgattern addiert zwei Binärzahlen; ein Steuerwerk liest die Zahl des nächsten Befehls und schaltet die passenden Teile zusammen, etwa „Speicherplatz 12 an den Eingang des Rechenwerks, Ausgang zurück in den Speicher“. Je weniger und je einfachere Befehle es gibt, desto kleiner, schneller und sparsamer lässt sich diese Schaltung bauen. Alles Komplizierte entsteht durch Hintereinanderschalten vieler einfacher Befehle, so wie eine komplizierte Schaltung aus wenigen Arten von Bauelementen besteht.

Der Prozessor arbeitet dabei immer denselben Kreislauf ab: Befehl holen, Befehl entschlüsseln, Befehl ausführen, zum nächsten Befehl gehen.
:::

### Die Programmiersprache

<span class="anker" id="stufe-1-3"></span>

Maschinencode ist eine lange Folge von Zahlen. Menschen können ihn kaum lesen, und er gilt nur für eine Prozessorfamilie. Ein Rezept in Alltagssprache wäre bequemer, aber Alltagssprache ist mehrdeutig.

**Mehrdeutigkeit.** „Ich sah den Mann mit dem Fernglas.“ Hatte ich das Fernglas oder der Mann? Ein Mensch errät die gemeinte Bedeutung aus dem Zusammenhang. Ein Rechner kann das nicht; er braucht für jeden Satz genau eine Bedeutung.

:::definition Definition 1.3 (Programmiersprache)
<span class="anker" id="satz-1-3"></span>

Eine __Programmiersprache__ ist eine künstliche Sprache, in der genau festgelegt ist, welche Texte erlaubt sind und was jeder erlaubte Text bewirkt.
:::

::::beispiel
Python, C und C++ sind Programmiersprachen. Den ersten Durchgang des Heron-Rezepts mit $g=1$ schreibt man in Python so:

```python
(1 + 2 / 1) / 2
```

Das Zeichen `/` bedeutet „geteilt durch“, `+` bedeutet „plus“, und die Klammern wirken wie in der Mathematik. Diese Zeile hat in Python genau eine Bedeutung: [Teile 2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html) durch 1, addiere 1, teile das Ergebnis durch 2.
::::

⁠**Kurz gesagt:** Eine Programmiersprache ist eine künstliche Sprache ohne Mehrdeutigkeit, in der man Programme aufschreibt.

### Die Syntax

<span class="anker" id="stufe-1-4"></span>

Bei einer Programmiersprache muss man zwei Fragen trennen: Ist ein Text überhaupt erlaubt? Und was bewirkt er? Die erste Frage betrifft nur die Form.

**Form ohne Bedeutung.** Der Satz „Der Wulp blinzt das Graffel.“ ist grammatisch richtig gebaut: Subjekt, Verb, Objekt. Er bedeutet nur nichts. „Graffel das blinzt Wulp der.“ ist dagegen schon in der Form falsch. Ob ein Satz richtig gebaut ist, kann man prüfen, ohne seine Bedeutung zu kennen.

:::definition Definition 1.4 (Syntax)
<span class="anker" id="satz-1-4"></span>

Die __Syntax__ einer Programmiersprache ist die Gesamtheit der Regeln, die festlegen, welche Texte in ihr erlaubt sind.
:::

::::beispiel
In Python ist `(1 + 2 / 1) / 2` erlaubt. Die folgenden Zeilen verletzen die Syntax:

<ul>

<li>

`(1 + 2 / 1 / 2`: Eine Klammer wird geöffnet und nie geschlossen.

</li>

<li>

`1 + / 2`: Zwischen `+` und `/` fehlt eine Zahl.

</li>

</ul>
::::

⁠**Kurz gesagt:** Die Syntax legt die erlaubte Form fest, unabhängig davon, was ein Text bedeutet.

### Die Semantik

<span class="anker" id="stufe-1-5"></span>

Ein Text in erlaubter Form muss außerdem eine festgelegte Wirkung haben.

:::definition Definition 1.5 (Semantik)
<span class="anker" id="satz-1-5"></span>

Die __Semantik__ einer Programmiersprache legt fest, was ein erlaubter Text bedeutet, also was geschieht, wenn er ausgeführt wird.
:::

::::beispiel
Die Zeile `7 / 2` ist in Python und in C erlaubt, hat also in beiden Sprachen die richtige Form. In Python bedeutet sie „teile 7 durch 2“, das Ergebnis ist 3,5. In C bedeutet derselbe Text bei ganzen Zahlen „teile und lass den Rest weg“, das Ergebnis ist 3. Gleiche Form, verschiedene Bedeutung.

Ein zweites Beispiel: Wer den Mittelwert von 3 und 4 berechnen will und `3 + 4 / 2` schreibt, hat einen erlaubten Text geschrieben. Seine festgelegte Bedeutung ist aber $3+\frac42=5$, nicht der gemeinte Mittelwert $3{,}5$. Die Semantik richtet sich nach dem Text, nicht nach der Absicht.
::::

⁠**Kurz gesagt:** Die Semantik legt fest, was ein erlaubter Text bewirkt.

:::hintergrund Woher Python weiß, welche Texte erlaubt sind
Die Syntax von Python ist als formale Grammatik aufgeschrieben: eine Liste von Regeln der Art „ein Ausdruck in Klammern ist eine öffnende Klammer, dann ein Ausdruck, dann eine schließende Klammer“. Sie steht vollständig in der Sprachreferenz von Python. Das Programm, das Python-Texte ausführt, enthält einen Teil, der aus genau dieser Grammatik erzeugt ist und jeden Text gegen ihre Regeln prüft. Die Semantik ist dagegen in Worten beschrieben: Für jede erlaubte Form sagt die Sprachreferenz, was sie bewirkt.
:::

### Der Quelltext

<span class="anker" id="stufe-1-6"></span>

Was ein Mensch in einer Programmiersprache aufschreibt, braucht einen Namen, um es vom Maschinencode zu unterscheiden.

:::definition Definition 1.6 (Quelltext)
<span class="anker" id="satz-1-6"></span>

Der __Quelltext__ eines Programms ist sein Text in einer Programmiersprache, so wie Menschen ihn schreiben und lesen.
:::

::::beispiel
Die Zeile `(1 + 2 / 1) / 2` ist ein sehr kurzer Python-Quelltext. Ein Prozessor kann ihn nicht ausführen, denn er versteht nur Maschinenbefehle. Zwischen dem Quelltext und dem Prozessor muss also übersetzt werden.
::::

⁠**Kurz gesagt:** Der Quelltext ist das Programm in der Form, in der Menschen es schreiben; der Prozessor kann ihn nicht unmittelbar ausführen.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-7"></span>

:::aufgabe Aufgabe 1 ★ Das Rezept von Hand
<span class="anker" id="aufg-1"></span>

Berechne mit dem Heron-Rezept und einem Taschenrechner die Wurzel aus 10. Ersetze dazu im Rezept die Zahl 2 durch 10, also $g'=\frac12(g+10/g)$.

<ol class="al">

<li>

Beginne mit $g=3$ und führe drei Durchgänge aus. Notiere $g$ jeweils mit sechs Nachkommastellen.

</li>

<li>

Berechne nach jedem Durchgang $g^2$. Wie nahe liegt es an 10?

</li>

<li>

Vergleiche in jedem Durchgang $g$ und $10/g$. Welche der beiden Zahlen ist größer?

</li>

</ol>

:::loesung
Das Rezept lautet hier $g'=\frac12(g+10/g)$; der wahre Wert ist $\sqrt{10}=3{,}162\,277\,66\ldots$

| Durchgang | $g$ vorher | $10/g$ | $g$ nachher | $g^2$ nachher |
|---|---|---|---|---|
| 1 | $3$ | $3{,}333\,333$ | $3{,}166\,667$ | $10{,}027\,778$ |
| 2 | $3{,}166\,667$ | $3{,}157\,895$ | $3{,}162\,281$ | $10{,}000\,019$ |
| 3 | $3{,}162\,281$ | $3{,}162\,275$ | $3{,}162\,278$ | $10{,}000\,000$ |

(a) Nach drei Durchgängen ist $g=3{,}162\,278$; alle sechs Nachkommastellen stimmen mit $\sqrt{10}$ überein.

(b) $g^2$ liegt nach dem ersten Durchgang um $0{,}028$ über 10, nach dem zweiten um $0{,}000\,019$, nach dem dritten um weniger als $10^{-11}$. Der Abstand schrumpft jedes Mal drastisch, weil er nach dem Hintergrund-Kasten in Unterabschnitt [1.1](#stufe-1-1) quadriert und geteilt wird: $0{,}028^2/(4\cdot10{,}03)\approx0{,}000\,019$.

(c) Vor dem ersten Durchgang ist $g=3$ kleiner als $10/g=3{,}333$: Die Startschätzung ist zu klein. Ab dann ist immer $g$ die größere Zahl ($3{,}166\,667>3{,}157\,895$ und $3{,}162\,281>3{,}162\,275$). Der Grund: Das Produkt $g\cdot(10/g)$ ist immer 10, also liegt $\sqrt{10}$ stets zwischen den beiden Zahlen; und nach einem Durchgang ist $g$ nie mehr zu klein, wie der Hintergrund-Kasten in Unterabschnitt [1.1](#stufe-1-1) zeigt.
:::
:::

:::aufgabe Aufgabe 2 ★ Form oder Bedeutung?
<span class="anker" id="aufg-2"></span>

Entscheide für jeden Fall, ob die Syntax verletzt ist, ob ein erlaubter Text etwas anderes bedeutet als gemeint oder ob der Text mehrdeutig ist.

<ol class="al">

<li>

In Python: `(3 + 4 / 2`.

</li>

<li>

In Python soll der Mittelwert von 3 und 4 berechnet werden: `3 + 4 / 2`.

</li>

<li>

In Python: `3 + * 4`.

</li>

<li>

Eine Anleitung: „Schließe den Widerstand an die Leitung mit der Lötöse an.“

</li>

<li>

Ein Programm in C enthält `7 / 2` und soll 3,5 ergeben.

</li>

</ol>

:::loesung
(a) Syntax verletzt: Die geöffnete Klammer wird nie geschlossen.

(b) Erlaubter Text mit anderer Bedeutung als gemeint. Python rechnet Punkt vor Strich, also $3+4/2=3+2=5$. Gemeint war `(3 + 4) / 2` mit dem Wert 3,5.

(c) Syntax verletzt: Hinter `+` fehlt eine Zahl, bevor `*` folgt.

(d) Mehrdeutig: Hat der Widerstand die Lötöse oder die Leitung? Ein Mensch fragt nach oder entscheidet nach dem Zusammenhang; in einer Programmiersprache darf es eine solche Stelle nicht geben.

(e) Erlaubter Text mit anderer Bedeutung als gemeint. Nach der Semantik von C ergibt `7 / 2` mit ganzen Zahlen 3, nicht 3,5. Wer in C 3,5 will, muss mindestens eine der Zahlen mit Nachkommastelle schreiben, etwa `7.0 / 2`.
:::
:::

:::aufgabe Aufgabe 3 ★★ Ein Rezept in Maschinenbefehlen
<span class="anker" id="aufg-3"></span>

Der Mittelwert von drei Zahlen $a$, $b$ und $c$, die im Speicher stehen, soll berechnet und im Speicher abgelegt werden. Zerlege die Rechnung in Befehle der Art „hole eine Zahl aus dem Speicher“, „addiere“, „teile durch eine Zahl“ und „lege im Speicher ab“, wie im Beispiel von Unterabschnitt [1.2](#stufe-1-2). Wie viele Befehle brauchst du? Hole jede Zahl dabei nur einmal.

:::loesung
Eine mögliche Folge:

<ol>

<li>

Hole $a$ aus dem Speicher.

</li>

<li>

Hole $b$ aus dem Speicher.

</li>

<li>

Addiere die beiden Zahlen; Ergebnis $a+b$.

</li>

<li>

Hole $c$ aus dem Speicher.

</li>

<li>

Addiere $c$; Ergebnis $a+b+c$.

</li>

<li>

Teile das Ergebnis durch 3.

</li>

<li>

Lege das Ergebnis im Speicher ab.

</li>

</ol>

Das sind sieben Befehle: drei zum Holen, zwei Additionen, eine Division, einmal Ablegen. Eine Zeile Quelltext wie `(a + b + c) / 3` wird also zu mehreren Maschinenbefehlen. Wie viele genau, hängt von der Prozessorfamilie ab; manche Prozessoren können zum Beispiel eine Zahl aus dem Speicher holen und im selben Befehl addieren.
:::
:::
