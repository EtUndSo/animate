---
title: Der interaktive Modus
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020500
summary: Python lässt sich wie ein Taschenrechner benutzen: Man tippt eine Zeile ein und sieht sofort das Ergebnis.
tags: interaktiven Modus, Wert, Ausdruck, Auswerten, Zeichenkette, Funktion, Funktionsaufruf
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Python lässt sich wie ein Taschenrechner benutzen: Man tippt eine Zeile ein und sieht sofort das Ergebnis. Dieser Abschnitt zeigt diese Arbeitsweise und die ersten Bausteine von Python: Werte, Ausdrücke, Zeichenketten und den Aufruf einer Funktion.
:::

### Der interaktive Modus

<span class="anker" id="stufe-4-1"></span>

Um eine einzelne Zeile auszuprobieren, will man keine Datei anlegen. Python bietet dafür eine eigene Arbeitsweise.

**Ein Taschenrechner.** Am Taschenrechner tippt man eine Rechnung, drückt „=“ und liest das Ergebnis ab. Dann tippt man die nächste Rechnung. Genau so arbeitet Python, wenn man es ohne Dateinamen startet.

:::definition Definition 4.1 (Interaktiver Modus)
<span class="anker" id="satz-4-1"></span>

Im __interaktiven Modus__ liest Python eine Eingabe, führt sie aus, zeigt das Ergebnis an und wartet dann auf die nächste Eingabe.
:::

Die Eingabeaufforderung des interaktiven Modus ist `>>>`. Auf Englisch heißt dieser Kreislauf aus Lesen, Ausführen und Anzeigen *read–eval–print loop*, abgekürzt REPL.

**Beispiel.** Starte im Terminal `py` (Windows) oder `python3` (Linux), ohne etwas dahinter. Python meldet sich mit seiner Version und wartet auf eine Eingabe:

```console Windows (PowerShell)
PS> py
Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 7 * 6
42
>>> exit
```

```console Linux
$ python3
Python 3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 7 * 6
42
>>> exit
```

Hinter jedes `>>>` tippst du eine Zeile und drückst Enter. Python antwortet in der nächsten Zeile und zeigt wieder `>>>`. Ein paar Handgriffe dazu:

<ul>

<li>

⁠**Beenden:** `exit` eintippen (ab Python 3.13; in jeder Version geht `exit()` mit Klammern), oder Strg+D unter Linux, Strg+Z und dann Enter unter Windows. Danach steht wieder die Eingabeaufforderung des Terminals da.

</li>

<li>

⁠**Frühere Eingaben:** Die Pfeiltaste nach oben holt die letzte Eingabe zurück; man kann sie ändern und erneut mit Enter abschicken.

</li>

<li>

⁠**Unvollständige Eingabe:** Fehlt noch etwas, etwa eine schließende Klammer, zeigt Python `...` statt `>>>` und wartet auf den Rest der Eingabe.

</li>

</ul>

Ab Python 3.13 ist der interaktive Modus farbig; in diesem Kapitel sind die Sitzungen ohne Farben abgedruckt.

⁠**Kurz gesagt:** Im interaktiven Modus tippt man hinter `>>>` eine Zeile, und Python antwortet sofort.

:::hintergrund Woher der interaktive Modus kommt
Der Name *read–eval–print loop* stammt aus der Programmiersprache Lisp. In den 1960er-Jahren hatten Lisp-Systeme bereits genau diesen Kreislauf: eine Eingabe lesen (*read*), sie ausrechnen (*evaluate*), das Ergebnis ausgeben (*print*), von vorn beginnen (*loop*). Viele Sprachen haben ihn übernommen, weil man so eine Sprache ausprobieren kann, ohne ein ganzes Programm zu schreiben.

Seit Python 3.13 bringt CPython einen überarbeiteten interaktiven Modus mit: Eingabeaufforderung und Fehlermeldungen sind farbig, man kann mehrzeilige Eingaben als Ganzes bearbeiten, `exit` und `help` funktionieren ohne Klammern, und die Tasten F1, F2 und F3 öffnen Hilfe, Verlauf und einen Modus zum Einfügen längerer Texte. Ab Python 3.14 färbt er zusätzlich die eingetippten Zeilen nach ihrer Syntax ein. In älteren Versionen und in manchen Umgebungen erscheint die einfachere frühere Fassung; was sie ausrechnet, ist dasselbe.
:::

### Der Wert

<span class="anker" id="stufe-4-2"></span>

Ein Taschenrechner arbeitet mit Zahlen. Auch Python braucht einen Namen für die Daten, mit denen es arbeitet.

:::definition Definition 4.2 (Wert)
<span class="anker" id="satz-4-2"></span>

Ein __Wert__ ist ein einzelnes Datum, mit dem Python arbeitet, zum Beispiel die Zahl 42 oder die Zahl 0,5.
:::

Zahlen mit Nachkommastellen schreibt man in Python mit einem Punkt, nicht mit einem Komma: `0.5` statt 0,5. Im Fließtext dieses Kapitels stehen Zahlen weiter mit Komma; in Python-Zeilen und in den Antworten von Python stehen sie mit Punkt.

**Beispiel.** Tippt man eine Zahl ein, zeigt der interaktive Modus ihren Wert. Er schreibt ihn so, wie Python ihn selbst schreiben würde, und lässt zum Beispiel eine überflüssige Null am Ende weg:

```console
>>> 42
42
>>> 0.5
0.5
>>> 2.50
2.5
```

⁠**Kurz gesagt:** Ein Wert ist ein Datum wie die Zahl 42; Nachkommastellen stehen in Python hinter einem Punkt.

### Der Ausdruck

<span class="anker" id="stufe-4-3"></span>

Meist tippt man nicht einen fertigen Wert ein, sondern eine Rechnung, deren Wert Python erst bestimmen soll.

:::definition Definition 4.3 (Ausdruck)
<span class="anker" id="satz-4-3"></span>

Ein __Ausdruck__ ist ein Stück Quelltext, das Python zu einem Wert ausrechnen kann.
:::

Das Ausrechnen eines Ausdrucks heißt __Auswerten__.

**Beispiel.** `2 + 3` ist ein Ausdruck mit dem Wert 5. Auch eine einzelne Zahl wie `42` ist ein Ausdruck, der einfachste überhaupt: Ihr Wert ist die Zahl selbst. Der interaktive Modus wertet jeden eingetippten Ausdruck aus und zeigt den Wert in der nächsten Zeile an. Die Sitzungen oben sind also lauter Paare aus Ausdruck und Wert.

⁠**Kurz gesagt:** Ein Ausdruck ist Quelltext, der einen Wert ergibt; der interaktive Modus zeigt diesen Wert sofort an.

### Rechnen wie mit dem Taschenrechner

<span class="anker" id="stufe-4-4"></span>

Für die Grundrechenarten und Potenzen hat Python eigene Zeichen.

| Zeichen | Bedeutung | Beispiel | Wert |
|---|---|---|---|
| `+` | plus | `7 + 2` | `9` |
| `-` | minus | `7 - 2` | `5` |
| `*` | mal | `7 * 2` | `14` |
| `/` | geteilt durch | `7 / 2` | `3.5` |
| `**` | hoch | `2 ** 10` | `1024` |

**Regeln.**

<ul>

<li>

Python rechnet wie in der Mathematik: Potenzen vor Punktrechnung, Punktrechnung vor Strichrechnung. `100 + 220 * 2` ergibt 540; wer zuerst addieren will, setzt Klammern: `(100 + 220) * 2` ergibt 640.

</li>

<li>

Klammern sind nur die runden. Eckige und geschweifte Klammern haben in Python andere Bedeutungen.

</li>

<li>

Leerzeichen um die Rechenzeichen sind erlaubt, aber nicht nötig; sie machen eine Zeile lesbarer.

</li>

<li>

Das Ergebnis von `/` schreibt Python immer mit Punkt, auch wenn die Division aufgeht: `12 / 4` ergibt `3.0`.

</li>

<li>

Zehnerpotenzen schreibt man mit `e`: `2.5e-3` bedeutet $2{,}5\cdot10^{-3}$, also 2,5 mA, wenn die Zahl ein Strom in Ampere ist. Ebenso ist `4.7e3` die Zahl 4700.

</li>

<li>

Ergebnisse mit Nachkommastellen zeigt Python mit bis zu 17 gültigen Stellen. Wie viele davon sinnvoll sind, entscheidest du beim Ablesen.

</li>

<li>

Python kennt keine Einheiten. Welche Einheit eine Zahl hat, musst du selbst im Kopf behalten.

</li>

</ul>

**Beispiel: das ohmsche Gesetz.** An einem Widerstand von $470\,\Omega$ liegen $5\,\mathrm V$. Der Strom ist $I=U/R$, die Leistung $P=U^2/R$. Und an einem Widerstand von $2{,}2\,\mathrm{k\Omega}$, durch den $2{,}5\,\mathrm{mA}$ fließen, liegt $U=R\cdot I$:

```console
>>> 5 / 470
0.010638297872340425
>>> 5 ** 2 / 470
0.05319148936170213
>>> 2200 * 2.5e-3
5.5
```

Abgelesen: $I\approx0{,}0106\,\mathrm A=10{,}6\,\mathrm{mA}$, $P\approx0{,}053\,\mathrm W=53\,\mathrm{mW}$ und $U=5{,}5\,\mathrm V$.

**Das letzte Ergebnis.** Der interaktive Modus merkt sich den zuletzt angezeigten Wert unter dem Zeichen `_` (Unterstrich), so wie die Taste ANS eines Taschenrechners. Nach der Sitzung oben ergibt `_ * 1000` also 5500.0. Das funktioniert nur im interaktiven Modus.

**Vorsicht, Komma.** Wer aus Gewohnheit `2,5 * 2` statt `2.5 * 2` tippt, bekommt keine Fehlermeldung, sondern ein falsches Ergebnis:

```console
>>> 2,5 * 2
(2, 10)
```

Python liest das Komma als Trennzeichen zwischen zwei Werten: `2` und `5 * 2`. Es zeigt beide in Klammern an, statt 5,0 zu rechnen.

⁠**Kurz gesagt:** Python rechnet mit `+ - * / **` und runden Klammern nach den Regeln der Mathematik, Nachkommastellen stehen hinter einem Punkt, Einheiten kennt es nicht.

:::hintergrund Warum die Potenz `**` heißt und nicht `^`
Für „hoch“ hat sich in Programmiersprachen kein einheitliches Zeichen durchgesetzt. Python folgt der Schreibweise `**`, die schon die Sprache Fortran in den 1950er-Jahren benutzte. Das Zeichen `^` hat Python dagegen aus der Sprache C übernommen, wo es eine Verknüpfung einzelner Binärstellen bedeutet, die mit Potenzen nichts zu tun hat. Deshalb ergibt `2 ^ 3` in Python 1 und nicht 8, und zwar ohne Fehlermeldung. Wer aus Tabellenkalkulation oder Taschenrechner das Zeichen `^` gewohnt ist, sollte darauf achten.
:::

### Das Rezept im interaktiven Modus: erst von Hand, dann fertig

<span class="anker" id="stufe-4-5"></span>

Mit dem, was bis hierher erklärt ist, lässt sich das Heron-Rezept aus Unterabschnitt [1.1](programme-und-programmiersprachen.html#stufe-1-1) im interaktiven Modus ausführen: zuerst von Hand, Durchgang für Durchgang, danach mit dem fertigen Weg, den Python mitbringt.

**Von Hand.** Der erste Durchgang mit $g=1$ ist `(1 + 2/1) / 2`. Für jeden weiteren Durchgang braucht man das letzte Ergebnis als neues $g$; dafür steht `_`. Mit der Pfeiltaste nach oben holt man die Zeile `(_ + 2/_) / 2` zurück und schickt sie erneut ab:

```console
>>> (1 + 2/1) / 2
1.5
>>> (_ + 2/_) / 2
1.4166666666666665
>>> (_ + 2/_) / 2
1.4142156862745097
>>> (_ + 2/_) / 2
1.4142135623746899
>>> (_ + 2/_) / 2
1.414213562373095
>>> (_ + 2/_) / 2
1.414213562373095
```

Nach dem fünften Durchgang ändert sich nichts mehr: Das Rezept ist am Ziel.

**Fertig.** Die Quadratwurzel ist die Potenz mit dem Exponenten $\frac12$. Python kann sie deshalb ohne Rezept berechnen:

```console
>>> 2 ** 0.5
1.4142135623730951
```

**Vergleich.** Beide Wege stimmen in den ersten 15 Nachkommastellen überein:

| Weg | Ergebnis |
|---|---|
| Heron von Hand, ab dem 5. Durchgang | `1.414213562373095` |
| fertig mit `2 ** 0.5` | `1.4142135623730951` |
| wahrer Wert $\sqrt2$ | $1{,}414\,213\,562\,373\,095\,048\,8\ldots$ |

Der Unterschied in der 16. Nachkommastelle hat eine einfache Ursache: Python rechnet nicht mit unendlich vielen Stellen, sondern rundet jedes Zwischenergebnis auf eine feste Zahl von Stellen. Zwischen zwei benachbarten gerundeten Zahlen liegt deshalb eine kleinste Stufe. Das Rezept rundet in jedem Durchgang mehrmals und bleibt am Ende eine solche Stufe neben dem eingebauten Ergebnis stehen. Der fertige Weg liegt hier näher am wahren Wert, braucht keine Durchgänge und keine Startschätzung; deshalb benutzt man ihn, sobald es ihn gibt.

Von Hand musste jeder Durchgang einzeln abgeschickt werden. Genau solche Wiederholungen soll ein Programm einem abnehmen.

⁠**Kurz gesagt:** Das Heron-Rezept läuft im interaktiven Modus Durchgang für Durchgang und landet nach fünf Durchgängen bis auf die letzte Stelle beim eingebauten Ergebnis von `2 ** 0.5`.

### Text als Wert: die Zeichenkette

<span class="anker" id="stufe-4-6"></span>

Programme geben nicht nur Zahlen aus, sondern auch Text, etwa „Strom in A:“ vor einem Ergebnis. Text muss deshalb ebenfalls ein Wert sein können.

:::definition Definition 4.4 (Zeichenkette)
<span class="anker" id="satz-4-4"></span>

Eine __Zeichenkette__ ist ein Wert, der aus Text besteht. Im Quelltext steht sie zwischen zwei geraden Anführungszeichen, `"Hallo"`, oder zwischen zwei Apostrophen, `'Hallo'`.
:::

**Beispiel.** Drei Eingaben im interaktiven Modus:

```console
>>> "Hallo"
'Hallo'
>>> "7 * 6"
'7 * 6'
>>> 7 * 6
42
```

Der interaktive Modus zeigt eine Zeichenkette mit Apostrophen an, auch wenn man sie mit Anführungszeichen eingetippt hat; beides bedeutet dasselbe. Wichtiger ist die zweite Zeile: `"7 * 6"` wird nicht ausgerechnet. Zwischen Anführungszeichen ist `7 * 6` nur eine Folge von fünf Zeichen.

Die Anführungszeichen müssen die geraden von der Tastatur sein. Die typografischen Zeichen „ und “ aus der Textverarbeitung sind für Python andere Zeichen.

⁠**Kurz gesagt:** Text in geraden Anführungszeichen ist eine Zeichenkette, also ein Wert, mit dem Python nicht rechnet.

:::hintergrund Warum der interaktive Modus die Anführungszeichen mitschreibt
Der interaktive Modus zeigt jeden Wert so, wie man ihn im Quelltext schreiben würde. Deshalb steht dort `'7 * 6'` mit Apostrophen und `42` ohne: Man sieht sofort, ob das Ergebnis eine Zahl oder ein Text ist. Ohne diese Kennzeichnung wären die Zahl 42 und der Text aus den Zeichen „4“ und „2“ auf dem Bildschirm nicht zu unterscheiden.
:::

### Die Funktion

<span class="anker" id="stufe-4-7"></span>

Viele Aufgaben kommen in fast jedem Programm vor, zum Beispiel etwas auf den Bildschirm zu schreiben. Dafür bringt Python fertige Teilprogramme mit.

**Eine Taste am Taschenrechner.** Die Taste $\sqrt{\ }$ eines Taschenrechners löst ein kleines eingebautes Programm aus. Man muss nicht wissen, wie es rechnet; man gibt eine Zahl hinein und bekommt die Wurzel heraus.

:::definition Definition 4.5 (Funktion)
<span class="anker" id="satz-4-5"></span>

Eine __Funktion__ ist ein fertiges Teilprogramm mit einem Namen, das man bei Bedarf ausführen lassen kann.
:::

**Beispiel.** Python bringt die Funktion mit dem Namen `print` mit. Sie schreibt Werte als Text in das Terminal.

⁠**Kurz gesagt:** Eine Funktion ist ein fertiges Teilprogramm mit Namen.

### Der Funktionsaufruf: `print`

<span class="anker" id="stufe-4-8"></span>

Eine Funktion tut erst etwas, wenn man sie ausführen lässt. Dazu gibt es eine feste Schreibweise.

:::definition Definition 4.6 (Funktionsaufruf)
<span class="anker" id="satz-4-6"></span>

Ein __Funktionsaufruf__ lässt eine Funktion ausführen. Man schreibt ihren Namen, dahinter runde Klammern und in die Klammern die Werte, mit denen die Funktion arbeiten soll, durch Kommas getrennt.
:::

**Beispiel.** Die Funktion `print` schreibt die Werte in ihren Klammern in eine Zeile, getrennt durch je ein Leerzeichen. Zeichenketten erscheinen dabei ohne Anführungszeichen. Steht in den Klammern ein Ausdruck, wertet Python ihn zuerst aus und gibt dann seinen Wert aus.

```console
>>> print("Hallo")
Hallo
>>> print(7 * 6)
42
>>> print("7 * 6")
7 * 6
>>> print("Strom in A:", 5 / 470)
Strom in A: 0.010638297872340425
```

Ein Aufruf ohne Werte, `print()`, schreibt eine leere Zeile.

Im interaktiven Modus sehen `"Hallo"` und `print("Hallo")` ähnlich aus, sind aber verschieden. Im ersten Fall zeigt der interaktive Modus den Wert eines Ausdrucks, mit Apostrophen. Im zweiten Fall schreibt die Funktion `print` den Text selbst ins Terminal, ohne Apostrophe. Der Aufruf von `print` hat danach keinen Wert, den der interaktive Modus noch anzeigen würde.

⁠**Kurz gesagt:** Man ruft eine Funktion mit ihrem Namen und runden Klammern auf; `print` schreibt die Werte in den Klammern ins Terminal.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-9"></span>

:::aufgabe Aufgabe 10 ★ Python als Taschenrechner
<span class="anker" id="aufg-10"></span>

Rechne im interaktiven Modus und gib die Ergebnisse mit sinnvoll vielen Stellen und mit Einheit an.

<ol class="al">

<li>

Ein Widerstand von $1{,}5\,\mathrm{k\Omega}$ hängt an einer $9$-V-Batterie. Welcher Strom fließt?

</li>

<li>

Welche Leistung setzt der Widerstand aus (a) in Wärme um?

</li>

<li>

Durch einen Widerstand von $3{,}3\,\mathrm{k\Omega}$ fließen $2{,}5\,\mathrm{mA}$. Welche Spannung liegt an ihm? Schreibe den Strom mit `e`.

</li>

<li>

Rechne direkt nach (a) mit `_` weiter und gib den Strom in Milliampere an.

</li>

</ol>

:::loesung
```console
>>> 9 / 1500
0.006
>>> _ * 1000
6.0
>>> 9 ** 2 / 1500
0.054
>>> 3300 * 2.5e-3
8.25
```

(a) $I=U/R=9\,\mathrm V/1500\,\Omega=0{,}006\,\mathrm A$. Den Widerstand gibt man in Ohm ein, $1{,}5\,\mathrm{k\Omega}=1500\,\Omega$.

(b) $P=U^2/R=0{,}054\,\mathrm W=54\,\mathrm{mW}$.

(c) $U=R\cdot I=3300\,\Omega\cdot2{,}5\cdot10^{-3}\,\mathrm A=8{,}25\,\mathrm V$.

(d) Direkt nach (a) steht in `_` der Wert `0.006`; `_ * 1000` ergibt `6.0`, also 6 mA. Rechnet man vorher (b) oder (c), steht in `_` deren Ergebnis, denn `_` hält immer nur den zuletzt angezeigten Wert.
:::
:::

:::aufgabe Aufgabe 11 ★★ Die Wurzel aus 3 von Hand und fertig
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Führe das Heron-Rezept für $\sqrt3$ im interaktiven Modus aus: Beginne mit `(1 + 3/1) / 2` und wiederhole `(_ + 3/_) / 2`, bis sich das Ergebnis nicht mehr ändert. Wie viele Durchgänge brauchst du?

</li>

<li>

Berechne $\sqrt3$ auf dem fertigen Weg und vergleiche.

</li>

<li>

Bei $\sqrt2$ unterschieden sich die beiden Wege in der letzten Stelle. Wie ist es hier?

</li>

</ol>

:::loesung
```console
>>> (1 + 3/1) / 2
2.0
>>> (_ + 3/_) / 2
1.75
>>> (_ + 3/_) / 2
1.7321428571428572
>>> (_ + 3/_) / 2
1.7320508100147274
>>> (_ + 3/_) / 2
1.7320508075688772
>>> (_ + 3/_) / 2
1.7320508075688772
>>> 3 ** 0.5
1.7320508075688772
```

(a) Nach fünf Durchgängen ändert sich das Ergebnis nicht mehr; der sechste bestätigt das nur.

(b) `3 ** 0.5` ergibt `1.7320508075688772`.

(c) Diesmal stimmen beide Wege bis in die letzte Stelle überein. Ob das Rezept genau auf dem eingebauten Ergebnis landet oder eine kleinste Stufe daneben, hängt davon ab, wie die einzelnen Rundungen ausfallen; bei $\sqrt2$ blieb es knapp daneben, bei $\sqrt3$ trifft es. Der fertige Weg ist in beiden Fällen der verlässlichere.
:::
:::

:::aufgabe Aufgabe 12 ★★ Was zeigt der interaktive Modus?
<span class="anker" id="aufg-12"></span>

Schreibe für jede Eingabe auf, was der interaktive Modus anzeigt. Prüfe danach am Rechner.

<ol class="al">

<li>

`12 / 3`

</li>

<li>

`"12 / 3"`

</li>

<li>

`print(12 / 3)`

</li>

<li>

`print("12 / 3 =", 12 / 3)`

</li>

<li>

`2,5 + 1`

</li>

<li>

`2 ** 3 * 2`

</li>

</ol>

:::loesung
```console
>>> 12 / 3
4.0
>>> "12 / 3"
'12 / 3'
>>> print(12 / 3)
4.0
>>> print("12 / 3 =", 12 / 3)
12 / 3 = 4.0
>>> 2,5 + 1
(2, 6)
>>> 2 ** 3 * 2
16
```

(a) Das Ergebnis von `/` steht immer mit Punkt, auch wenn die Division aufgeht.

(b) Zwischen Anführungszeichen wird nichts gerechnet; der interaktive Modus zeigt die Zeichenkette mit Apostrophen.

(c) `print` wertet erst den Ausdruck aus und schreibt dann den Wert.

(d) `print` schreibt die Zeichenkette ohne Anführungszeichen, ein Leerzeichen und dann den Wert.

(e) Das Komma trennt zwei Werte, `2` und `5 + 1`. Python zeigt beide in Klammern, ohne Fehlermeldung.

(f) Die Potenz kommt vor der Punktrechnung: $2^3=8$, dann $8\cdot2=16$.
:::
:::
