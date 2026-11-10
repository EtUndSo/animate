---
title: Schneller arbeiten: Vervollständigung, Verlauf, Tastenkürzel
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070600
summary: Wer viel an der Kommandozeile arbeitet, tippt trotzdem wenig.
tags: Vervollständigung, Verlauf, Rückwärtssuche, Strg+C, Strg+D, Tastenkürzel
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Wer viel an der Kommandozeile arbeitet, tippt trotzdem wenig. Die Shell ergänzt angefangene Namen, merkt sich jede Zeile, findet alte Befehle wieder und kennt Tastenkürzel zum Abbrechen, Beenden und Bearbeiten. Dieser Abschnitt stellt diese Hilfen vor und erklärt, wer im Hintergrund die Tasten auswertet.
:::

### Die Vervollständigung

<span class="anker" id="stufe-5-1"></span>

Lange Befehls- und Dateinamen sind mühsam zu tippen, und jeder Tippfehler führt zu `command not found` oder `No such file`. Dabei kennt die Shell die Namen schon: Sie weiß, welche Befehle es gibt und welche Dateien in einem Ordner liegen.

:::abbildung linux/k2tab 19
Die Vervollständigung mit der Tabulatortaste. Ist der Anfang eindeutig, ergänzt die Shell den Namen sofort. Passen mehrere Namen, ergänzt sie den gemeinsamen Teil, und ein zweiter Druck auf die Taste zeigt alle Möglichkeiten.
:::

:::definition Definition 5.1 (Vervollständigung)
<span class="anker" id="satz-5-1"></span>

Die __Vervollständigung__ ergänzt ein angefangenes Wort, sobald man die Tabulatortaste drückt. Im ersten Wort einer Zeile ergänzt die Shell Befehlsnamen, in den übrigen Wörtern meist Dateinamen. Passt nur ein Name, schreibt sie ihn aus; passen mehrere, ergänzt sie nur den Teil, den alle gemeinsam haben, und ein zweiter Druck auf die Taste listet alle Möglichkeiten auf.
:::

::::beispiel Einmal eindeutig, einmal mehrdeutig
Tippe `unam` und drücke die Tabulatortaste. Es gibt nur einen Befehl, der so beginnt, und die Shell schreibt ihn mit einem Leerzeichen dahinter aus:

```text
student@labor:~$ uname
```

Du ergänzt `-r` und drückst die Eingabetaste. Danach tippst du `cat /etc/host` und zweimal die Tabulatortaste. Drei Dateien beginnen so, die Shell kann sich nicht entscheiden und zeigt alle drei; darunter steht deine angefangene Zeile unverändert:

```text
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
student@labor:~$ cat /etc/host
host.conf  hostname   hosts
student@labor:~$ cat /etc/host
```

Ein `n` macht den Anfang eindeutig. Noch einmal die Tabulatortaste, dann die Eingabetaste:

```text
student@labor:~$ cat /etc/hostname
labor
```

Den Rest des Dateinamens hat die Shell ergänzt, und ein Tippfehler darin war ausgeschlossen.
::::

⁠**Kurz gesagt:** Die Tabulatortaste ergänzt Befehls- und Dateinamen; zweimal gedrückt zeigt sie alle Möglichkeiten.

### Der Verlauf

<span class="anker" id="stufe-5-2"></span>

Viele Befehle tippt man mehrmals, oft mit kleinen Änderungen. Statt sie neu zu tippen, holt man sie zurück, denn die Shell hat jede Zeile aufgeschrieben.

:::abbildung linux/k2verlauf 20
Der Verlauf als nummerierte Liste im Speicher der Shell. Mit der Pfeiltaste nach oben wandert man rückwärts durch die Liste. Am Ende der Sitzung schreibt die Shell die Liste in die Datei `~/.bash_history`; eine Zeile, die mit einem Leerzeichen beginnt, nimmt Ubuntu gar nicht erst auf.
:::

:::definition Definition 5.2 (Verlauf)
<span class="anker" id="satz-5-2"></span>

Der __Verlauf__ ist die nummerierte Liste der zuletzt getippten Befehlszeilen, die die Shell in ihrem Speicher hält. Die Pfeiltaste nach oben holt die vorige Zeile zurück, jeder weitere Druck eine ältere; die Pfeiltaste nach unten geht wieder vorwärts. Der eingebaute Befehl `history` zeigt die Liste. Am Ende der Sitzung schreibt bash den Verlauf in die Datei `.bash_history` im persönlichen Ordner, und die nächste Sitzung liest ihn von dort wieder ein.
:::

Ubuntu stellt den Verlauf so ein, dass sich die Shell die letzten 1 000 Zeilen merkt und die Datei höchstens 2 000 Zeilen behält. Zwei weitere Voreinstellungen: Eine Zeile, die genau der vorigen gleicht, wird nicht noch einmal aufgenommen, und eine Zeile, die mit einem Leerzeichen beginnt, gar nicht.

::::beispiel Drei Befehle, einer davon unsichtbar
Diese Sitzung beginnt mit einem leeren Verlauf. Die dritte Zeile beginnt mit einem Leerzeichen:

```text
student@labor:~$ whoami
student
student@labor:~$ uname -m
x86_64
student@labor:~$  echo geheim
geheim
student@labor:~$ history
    1  whoami
    2  uname -m
    3  history
```

`echo geheim` fehlt in der Liste; auch `history` selbst ist ein Eintrag. Zweimal die Pfeiltaste nach oben holt den zweiten Eintrag zurück, fertig zum Bearbeiten oder Ausführen:

```text
student@labor:~$ uname -m
```

In deinem eigenen Terminal sind die Nummern höher, denn dort stehen auch die Zeilen früherer Sitzungen im Verlauf.
::::

**Zeilen wiederholen mit Ausrufezeichen.** Die Shell kennt außerdem Kürzel, die auf den Verlauf verweisen: `!!` steht für die vorige Zeile, `!`*n* für den Eintrag mit der Nummer *n*. Sie schreibt die eingesetzte Zeile hin, bevor sie sie ausführt, damit man sieht, was geschieht:

```text
student@labor:~$ !!
history
    1  whoami
    2  uname -m
    3  history
```

⁠**Kurz gesagt:** Die Shell merkt sich jede Zeile im Verlauf; die Pfeiltaste nach oben und `history` holen sie zurück.

:::warnung Keine Geheimnisse in die Befehlszeile
Alles, was du in die Befehlszeile tippst, landet im Verlauf und am Ende der Sitzung als gewöhnlicher Text in `~/.bash_history`. Tippe deshalb nie ein Passwort oder einen Zugangsschlüssel als Argument. Programme, die ein Passwort brauchen, fragen selbst danach und zeigen die Eingabe dabei nicht an; diese Eingabe gelangt nicht in den Verlauf. Das Leerzeichen am Zeilenanfang ist kein verlässlicher Schutz: Es wirkt nur, weil Ubuntu es so voreinstellt, und auf anderen Systemen oft nicht.
:::

### Die Rückwärtssuche

<span class="anker" id="stufe-5-3"></span>

Liegt der gesuchte Befehl hundert Zeilen zurück, ist die Pfeiltaste zu langsam. Meist erinnert man sich aber an ein Stück des Befehls, etwa an seinen Namen.

:::abbildung linux/k2rsuche 21
Die Rückwärtssuche mit Strg+R. Jedes getippte Zeichen grenzt die Suche ein, und die Shell zeigt die jüngste Zeile des Verlaufs, die das Getippte enthält. Ein weiteres Strg+R springt zum nächstälteren Treffer.
:::

:::definition Definition 5.3 (Rückwärtssuche)
<span class="anker" id="satz-5-3"></span>

Die __Rückwärtssuche__ durchsucht den Verlauf von der jüngsten Zeile zur ältesten nach dem Text, den man tippt; man startet sie mit Strg+R. Jedes weitere Zeichen grenzt die Suche ein, jedes weitere Strg+R springt zum nächstälteren Treffer. Die Eingabetaste führt den gefundenen Befehl aus, eine Pfeiltaste übernimmt ihn zum Bearbeiten, und Strg+G bricht die Suche ab.
:::

::::beispiel Zweimal suchen, einmal ausführen
Im Verlauf stehen `uname -r`, `whoami`, `uname -m` und `head -n 1 /etc/os-release`. Nach Strg+R und den Buchstaben `un` zeigt die Shell die jüngste passende Zeile:

```text
(reverse-i-search)`un': uname -m
```

Ein zweites Strg+R springt zur älteren Zeile, die `un` enthält:

```text
(reverse-i-search)`un': uname -r
```

Die Eingabetaste führt sie aus, als hättest du sie neu getippt:

```text
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
```

Gibt es keinen älteren Treffer mehr, schreibt die Shell `failed` vor die Suche und bleibt beim letzten.
::::

⁠**Kurz gesagt:** Strg+R sucht rückwärts im Verlauf nach dem, was du tippst; die Eingabetaste führt den Treffer aus.

### Der Abbruch mit Strg+C

<span class="anker" id="stufe-5-4"></span>

Manchmal läuft ein Befehl länger als gedacht, wartet auf etwas, das nie kommt, oder man merkt mitten in der Zeile, dass man etwas anderes wollte. Dann braucht man einen Notausgang, der fast immer funktioniert.

:::abbildung linux/k2strgcd 22
Zwei Tastenkombinationen, die nicht als gewöhnliche Zeichen ankommen. Strg+C wird zur Aufforderung an das laufende Programm, sofort aufzuhören. Strg+D meldet dem lesenden Programm, dass keine Eingabe mehr kommt.
:::

:::definition Definition 5.4 (Abbruch mit Strg+C)
<span class="anker" id="satz-5-4"></span>

Die Tastenkombination __Strg+C__ fordert das Programm, das gerade im Terminal läuft, auf, sofort aufzuhören; fast alle Programme brechen daraufhin ab, und die Shell zeigt wieder die Eingabeaufforderung. Läuft kein Programm, verwirft Strg+C die angefangene Zeile. Im Fenster erscheint dabei `^C`.
:::

::::beispiel Ein wartendes Programm und eine halbe Zeile
Der Befehl `sleep 30` tut 30 Sekunden lang nichts und endet dann; er ist ideal zum Ausprobieren. Hier wurde er nach einer Sekunde mit Strg+C abgebrochen. Danach wurde `uname -r` getippt und, statt die Eingabetaste zu drücken, mit Strg+C verworfen:

```text
student@labor:~$ sleep 30
^C
student@labor:~$ uname -r^C
student@labor:~$
```

Die verworfene Zeile wurde nicht ausgeführt.
::::

⁠**Kurz gesagt:** Strg+C bricht das laufende Programm ab oder verwirft die angefangene Zeile.

:::warnung Strg+C kopiert im Terminal nicht
In fast allen Programmen kopiert Strg+C den markierten Text; im Terminal bricht es ab. Kopieren und Einfügen geht dort mit **Strg+Umschalt+C** und **Strg+Umschalt+V**, im Terminal von Ubuntu wie im Windows-Terminal. Das Windows-Terminal kopiert zusätzlich mit Strg+C, aber nur, solange Text markiert ist; ohne Markierung schickt es Strg+C an das laufende Programm. Wer sich die Variante mit Umschalt angewöhnt, bricht nie versehentlich etwas ab.
:::

:::hintergrund Warum Strg+C nicht bei der Shell ankommt
Jede Strg-Kombination mit einem Buchstaben erzeugt ein Steuerzeichen aus der Zeichentabelle ASCII, die aus der Zeit der Fernschreiber stammt. Strg+C ergibt das Zeichen mit der Nummer 3, das dort „Ende des Textes“ heißt; der Großbuchstabe C hat die Nummer 67, und Strg zieht 64 ab. Dieses Zeichen geht vom Terminalemulator in das Pseudoterminal aus Unterabschnitt [1.2](terminal-und-shell.html#stufe-1-2). Dort wertet der Kernel es aus, bevor es irgendein Programm liest: Er verwandelt es in eine Unterbrechungsnachricht an das Programm, das gerade im Vordergrund des Terminals läuft. Die meisten Programme beenden sich daraufhin sofort. Weil der Kernel das erledigt, funktioniert Strg+C auch bei einem Programm, das gar nicht mehr auf Tasten achtet. Die Zuordnung zeigt der Befehl `stty -a` in der Zeile `intr = ^C`; „intr“ steht für interrupt, Unterbrechung. Diese Bedeutung im Terminal ist älter als die grafischen Oberflächen, in denen Strg+C später zum Kopieren wurde.
:::

### Das Ende der Eingabe mit Strg+D

<span class="anker" id="stufe-5-5"></span>

Manche Programme lesen, was du tippst, Zeile für Zeile, bis du ihnen sagst, dass nichts mehr kommt. Das geht nicht mit einem Wort, denn jedes Wort könnte ja Teil der Eingabe sein. Es braucht eine eigene Taste für „Ende“.

:::definition Definition 5.5 (Ende der Eingabe mit Strg+D)
<span class="anker" id="satz-5-5"></span>

Die Tastenkombination __Strg+D__ am Anfang einer Zeile meldet dem Programm, das gerade liest, dass keine Eingabe mehr folgt. Ein Programm, das bis zum Ende der Eingabe liest, ist dann fertig. Die Shell selbst liest ebenfalls Eingaben; Strg+D in einer leeren Befehlszeile beendet deshalb die Sitzung wie `exit`.
:::

::::beispiel Erst für cat, dann für die Shell
`cat` ohne Dateinamen liest, was du tippst, und gibt jede Zeile sofort wieder aus. Hier wurden `Hallo` und `Welt` getippt, jeweils mit der Eingabetaste, und danach Strg+D:

```text
student@labor:~$ cat
Hallo
Hallo
Welt
Welt
student@labor:~$
```

Jede Zeile steht zweimal da: einmal, wie du sie getippt hast, einmal, wie `cat` sie ausgegeben hat. Nach Strg+D war `cat` fertig, und die Shell zeigte wieder die Eingabeaufforderung. Ein zweites Strg+D in dieser leeren Zeile beendet die Shell; sie schreibt zum Abschied `exit` hin:

```text
student@labor:~$
exit
```
::::

⁠**Kurz gesagt:** Strg+D sagt dem lesenden Programm „keine Eingabe mehr“; in der leeren Befehlszeile beendet es die Shell.

:::hintergrund Strg+D ist kein Abbruch, sondern ein leeres Lesen
Ein Programm liest Eingaben, indem es den Kernel mit einem Systemaufruf um die nächsten Zeichen bittet. Der Kernel antwortet mit den Zeichen und ihrer Anzahl. Eine Antwort mit null Zeichen bedeutet nach fester Vereinbarung: Die Eingabe ist zu Ende, so wie am Ende einer Datei. Strg+D erzeugt das Steuerzeichen Nummer 4, „Ende der Übertragung“, und der Terminaltreiber im Kernel macht daraus genau diese Antwort mit null Zeichen, sofern die Zeile noch leer ist; `stty -a` zeigt es als `eof = ^D`, „end of file“. Das Programm wird also nicht unterbrochen wie bei Strg+C. Es liest ein Ende und hört aus eigenem Entschluss auf, nachdem es fertig gearbeitet hat. bash wertet die Taste etwas anders aus, weil sie die Zeile selbst bearbeitet, kommt aber zum selben Ergebnis: In einer leeren Zeile gilt Strg+D als Ende, in einer Zeile mit Text löscht es das Zeichen unter dem Cursor.
:::

### Tastenkürzel für die Befehlszeile

<span class="anker" id="stufe-5-6"></span>

Eine lange Befehlszeile mit einem Tippfehler am Anfang: Mit den Pfeiltasten Zeichen für Zeichen zurückzugehen dauert. Die Shell kennt Tastenkürzel, die den Cursor springen lassen und ganze Stücke der Zeile löschen.

:::abbildung linux/k2tasten 23
Eine Befehlszeile mit dem Cursor in der Mitte. Strg+A und Strg+E springen an den Anfang und an das Ende, Strg+U löscht alles links vom Cursor, Strg+K alles rechts davon, Strg+W das Wort davor.
:::

:::definition Definition 5.6 (Tastenkürzel der Befehlszeile)
<span class="anker" id="satz-5-6"></span>

Ein __Tastenkürzel__ der Befehlszeile ist eine Tastenkombination, die die Shell nicht als Zeichen in die Zeile schreibt, sondern als Anweisung zum Bearbeiten der Zeile oder des Fensters ausführt. Tabelle [4](#tab-4) nennt die wichtigsten.
:::

<span class="anker" id="tab-4"></span>

**Tabelle 4:** Die wichtigsten Tastenkürzel an der Kommandozeile von bash. Die letzte Zeile wertet nicht die Shell aus, sondern der Terminalemulator.

| Tasten | Wirkung |
|---|---|
| Tabulatortaste | Namen vervollständigen (Unterabschnitt [5.1](#stufe-5-1)) |
| Pfeil nach oben bzw. unten | ältere bzw. neuere Zeile aus dem Verlauf (Unterabschnitt [5.2](#stufe-5-2)) |
| Strg+R | rückwärts im Verlauf suchen (Unterabschnitt [5.3](#stufe-5-3)) |
| Strg+C | laufendes Programm abbrechen, Zeile verwerfen (Unterabschnitt [5.4](#stufe-5-4)) |
| Strg+D | Ende der Eingabe; in leerer Zeile Shell beenden (Unterabschnitt [5.5](#stufe-5-5)) |
| Strg+L | Fenster leeren; die aktuelle Zeile bleibt oben stehen |
| Strg+A bzw. Strg+E | an den Anfang bzw. an das Ende der Zeile |
| Strg+U | alles links vom Cursor löschen |
| Strg+K | alles rechts vom Cursor löschen |
| Strg+W | das Wort links vom Cursor löschen |
| Strg+Umschalt+C bzw. V | im Terminal kopieren bzw. einfügen |

::::beispiel Einen Tippfehler am Zeilenanfang beheben
Du hast `unme -n 2 /etc/os-release` getippt und merkst vor der Eingabetaste, dass der Befehl `head` heißen sollte. Strg+A springt an den Anfang, viermal Entf löscht `unme`, du tippst `head`, und die Eingabetaste führt die Zeile aus; wo der Cursor dabei steht, spielt keine Rolle. Willst du stattdessen von vorn beginnen, verwirft Strg+U alles links vom Cursor, nach Strg+E also die ganze Zeile. Strg+L leert danach ein volles Fenster, ohne die Zeile anzurühren.
::::

⁠**Kurz gesagt:** Strg+A und Strg+E springen an Anfang und Ende, Strg+U, Strg+K und Strg+W löschen Teile der Zeile, Strg+L leert das Fenster.

:::hintergrund Wer die Tasten auswertet: die Bibliothek Readline
Vervollständigung, Verlauf, Rückwärtssuche und die Tastenkürzel zum Bearbeiten der Zeile programmiert bash nicht selbst, sondern übernimmt sie aus der Programmbibliothek GNU Readline, einer Sammlung fertiger Programmteile zum Bearbeiten einer Eingabezeile. Readline schaltet die zeilenweise Verarbeitung des Terminaltreibers ab, bekommt jeden Tastendruck einzeln und baut die Zeile selbst zusammen; erst mit der Eingabetaste reicht es sie an bash weiter. Die Tastenbelegung folgt standardmäßig dem Texteditor Emacs, daher die etwas willkürlich wirkenden Buchstaben; als Merkhilfe taugen A wie der Anfang des Alphabets, E wie englisch end und K wie kill, wegschneiden. Wer den Editor vi bevorzugt, schaltet mit `set -o vi` auf dessen Tasten um. Weil auch andere Programme mit einer Eingabezeile Readline benutzen, funktionieren dieselben Kürzel dort ebenfalls.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-7"></span>

:::aufgabe Aufgabe 17 ★ Vervollständigen statt tippen
<span class="anker" id="aufg-17"></span>

Wie viele Tasten brauchst du mindestens, um mit der Tabulatortaste `cat /etc/os-release` zu tippen? Probiere `cat /etc/os`, einmal mit einfachem und einmal mit doppeltem Druck auf die Tabulatortaste. Was zeigt die Shell nach `who` und zweimal Tab, und warum ergänzt sie nicht sofort?

:::loesung
`/etc/os` ist eindeutig, denn nur die Datei `os-release` beginnt so. Ein Druck auf die Tabulatortaste ergänzt sofort:

```text
student@labor:~$ cat /etc/os-release
```

Ein zweiter Druck ist dann nicht mehr nötig. Mit `cat /etc/os`, einmal Tab und der Eingabetaste sind es 13 Tasten statt 20. Es geht noch kürzer, weil im obersten Ordner nur `etc` mit `e` beginnt: `cat /e`, Tab (ergibt `cat /etc/`), `os`, Tab, Eingabetaste sind 11 Tasten. Nur `o` statt `os` genügt nicht, denn in `/etc` gibt es auch den Ordner `opt`. Bei `who` kann die Shell nicht ergänzen, denn mehrere Befehle beginnen so, und `who` ist selbst schon einer davon. Der zweite Druck listet sie:

```text
student@labor:~$ who
who     whoami  whois
student@labor:~$ who
```

Unter WSL 2 erscheint zusätzlich `whoami.exe`, ein Programm von Windows, weil WSL die Ordner der Windows-Programme an den Suchpfad hängt (Unterabschnitt [3.2](arten-von-befehlen.html#stufe-3-2)).
:::
:::

:::aufgabe Aufgabe 18 ★★ Der eigene Verlauf
<span class="anker" id="aufg-18"></span>

Tippe in einer neuen Sitzung nacheinander `whoami`, noch einmal `whoami`, `uname -r` und ` echo test` (mit einem Leerzeichen vorn), dann `history`. Welche Einträge erscheinen am Ende der Liste, und warum fehlen zwei Zeilen? Was steht nach `exit` und einer neuen Sitzung am Ende der Ausgabe von `history`?

:::loesung
In einer neuen Sitzung stehen am Ende der Liste:

```text
student@labor:~$ whoami
student
student@labor:~$ whoami
student
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
student@labor:~$  echo test
test
student@labor:~$ history
    1  cat
    2  whoami
    3  uname -r
    4  history
```

In dieser Sitzung stand vorher noch `cat` im Verlauf; bei dir stehen dort die Zeilen deiner früheren Sitzungen, mit höheren Nummern. Das zweite `whoami` fehlt, weil Ubuntu eine Zeile, die der vorigen gleicht, nicht noch einmal aufnimmt; `echo test` fehlt wegen des Leerzeichens am Anfang. Nach `exit` schreibt bash den Verlauf in `~/.bash_history`, einschließlich der Zeile `exit`. Eine neue Sitzung liest die Datei ein, und `history` zeigt am Ende `whoami`, `uname -r`, `history`, `exit` und als jüngsten Eintrag das neue `history`.
:::
:::

:::aufgabe Aufgabe 19 ★★ Abbrechen oder beenden?
<span class="anker" id="aufg-19"></span>

Starte `cat` ohne Argument, tippe eine Zeile und drücke die Eingabetaste. Beende `cat` einmal mit Strg+C und einmal mit Strg+D. Was ist für dich im Fenster gleich? Erkläre mit den Hintergrund-Kästen, was in beiden Fällen für `cat` verschieden ist. Was geschieht, wenn du Strg+D drückst, während eine Zeile mit Text dasteht?

:::loesung
Im Fenster ist beides gleich: `cat` endet, und die Eingabeaufforderung erscheint wieder; bei Strg+C steht zusätzlich `^C` da.

```text
student@labor:~$ cat
Hallo
Hallo
^C
student@labor:~$
```

Für `cat` ist es verschieden. Bei Strg+C schickt der Kernel eine Unterbrechungsnachricht, und `cat` wird mitten in seiner Arbeit beendet, ohne selbst zu entscheiden. Bei Strg+D bekommt `cat` auf seine Leseanfrage die Antwort „null Zeichen“, erkennt daran das Ende der Eingabe und beendet sich selbst, nachdem es alles Gelesene ausgegeben hat. Für `cat` macht das keinen sichtbaren Unterschied, für ein Programm, das am Ende noch etwas speichern muss, schon.

Steht beim Strg+D schon Text in der Zeile, gibt der Kernel diesen Text ohne Zeilenende an `cat` weiter, und `cat` gibt ihn sofort aus; im Fenster steht er dann zweimal hintereinander. Erst ein zweites Strg+D trifft auf eine leere Eingabe und beendet `cat`. Weil die Ausgabe kein Zeilenende hatte, steht die Eingabeaufforderung direkt dahinter. Getippt wurde `abc`, dann zweimal Strg+D:

```text
student@labor:~$ cat
abcabcstudent@labor:~$
```
:::
:::

:::aufgabe Aufgabe 20 ★★★ Tastenrechnung
<span class="anker" id="aufg-20"></span>

In der Zeichentabelle ASCII hat der Großbuchstabe A die Nummer 65. Welche Nummern erzeugen Strg+A, Strg+D, Strg+L und Strg+R, wenn Strg die Nummer um 64 verringert? `stty -a` meldet unter anderem `susp = ^Z` und `kill = ^U`. Welche Nummern sind das? Prüfe deine Antwort für Strg+U mit Tabelle [4](#tab-4): Wer löscht die Zeile, wenn bash läuft?

:::loesung
Strg+A ergibt $65-64=1$, Strg+D $68-64=4$, Strg+L $76-64=12$, Strg+R $82-64=18$. Z hat die Nummer 90, Strg+Z also $26$; U hat 85, Strg+U also $21$. Laut `stty -a` wertet der Kernel Strg+U im Pseudoterminal als „kill“ aus: Er löscht die angefangene Zeile, solange er die Zeile selbst verwaltet, etwa während `cat` liest. Läuft dagegen bash an der Eingabeaufforderung, hat Readline die zeilenweise Verarbeitung des Kernels abgeschaltet und bekommt die Taste selbst; nach Tabelle [4](#tab-4) löscht es alles links vom Cursor. Steht der Cursor am Zeilenende, sieht beides gleich aus.
:::
:::
