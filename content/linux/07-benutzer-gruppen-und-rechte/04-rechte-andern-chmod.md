---
title: Rechte ändern: chmod
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120400
summary: Rechte zu lesen genügt nicht; man will sie auch einstellen: eine Datei nur für sich behalten, ein Programm startbar machen, einer Gruppe das Ändern erlauben.
tags: Bit, symbolische Schreibweise, Oktalschreibweise
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Rechte zu lesen genügt nicht; man will sie auch einstellen: eine Datei nur für sich behalten, ein Programm startbar machen, einer Gruppe das Ändern erlauben. Dieser Abschnitt zeigt den Befehl dafür in seinen zwei Schreibweisen, mit Buchstaben und mit Zahlen, und erklärt, warum die Zahlen gerade so aussehen.
:::

:::::vorwissen Was du dafür brauchst: Bits und Binärzahlen

<span class="anker" id="stufe-3-1"></span>

Ein __Bit__ ist eine Stelle, die nur 0 oder 1 sein kann. Eine Binärzahl schreibt eine Zahl mit solchen Stellen; die Stelle ganz rechts zählt 1, die nächste 2, die nächste 4, jede doppelt so viel wie ihre rechte Nachbarin. So bedeutet `101` im Binärsystem $1\cdot 4 + 0\cdot 2 + 1\cdot 1 = 5$. Mit drei Bits lassen sich genau acht Muster schreiben, von `000` = 0 bis `111` = 7. Ausführlich erklärt das [Python, Kapitel 2, Abschnitt 3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3).

Ein Recht ist entweder da oder nicht, also genau ein Bit: 1 für erlaubt, 0 für verboten. Die drei Rechte einer Klasse bilden drei Bits nebeneinander, `rw-` zum Beispiel das Muster `110`.

⁠**Kurz gesagt:** Ein Bit ist 0 oder 1; drei Bits ergeben eine Zahl von 0 bis 7, und die drei Rechte einer Klasse sind genau drei Bits.

:::::

### chmod mit Buchstaben

<span class="anker" id="stufe-3-2"></span>

Meistens will man ein einzelnes Recht ändern und den Rest lassen, wie er ist: der Gruppe das Schreiben erlauben, allen anderen das Lesen nehmen. Dafür hat `chmod` eine Schreibweise, die sich fast wie ein Satz liest.

:::definition Definition 3.1 (chmod, symbolische Schreibweise)
<span class="anker" id="satz-3-1"></span>

`chmod angabe datei …` (englisch „change mode“, den Modus ändern) setzt die Rechte der genannten Dateien. Die __symbolische Schreibweise__ einer Angabe besteht aus drei Teilen ohne Leerzeichen:

<ol>

<li>

wer: `u`, `g`, `o` oder `a` (englisch „all“, alle drei), auch mehrere zusammen wie `go`;

</li>

<li>

was geschieht: `+` fügt Rechte hinzu, `-` nimmt sie weg, `=` setzt genau diese Rechte und nimmt die übrigen weg;

</li>

<li>

welche Rechte: `r`, `w`, `x` oder mehrere davon.

</li>

</ol>

Mehrere Angaben trennt ein Komma. Nur der Besitzer einer Datei und root dürfen ihre Rechte ändern.
:::

Abbildung [9](#abb-9) führt drei Änderungen an der Einkaufsliste vor, die du gleich selbst ausführst.

:::abbildung linux/k7symbolisch 9
Ein Raster mit drei Zeilen u, g, o und drei Spalten r, w, x; besetzte Felder sind gefüllt, leere hohl. Ausgangszustand `rw-r--r--`. Erster Schritt `g+w`: das Feld g/w füllt sich. Zweiter Schritt `o-r`: das Feld o/r leert sich. Dritter Schritt `u=rw,go=r`: die Zeile u wird auf r und w gesetzt, die Zeilen g und o auf nur r; dabei leert sich g/w wieder und o/r füllt sich. Unter dem Raster steht jeweils die Buchstabenfolge, wie `ls -l` sie zeigt.
:::

```console
$ chmod g+w einkauf.txt
$ ls -l einkauf.txt
-rw-rw-r-- 1 student student 25 Nov 10 12:32 einkauf.txt
$ chmod o-r einkauf.txt
$ ls -l einkauf.txt
-rw-rw---- 1 student student 25 Nov 10 12:32 einkauf.txt
$ chmod u=rw,go=r einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 25 Nov 10 12:32 einkauf.txt
```

`g+w` hat der Gruppe das Schreiben erlaubt, `o-r` allen anderen das Lesen genommen. `u=rw,go=r` setzt den Zustand vom Anfang wieder her, ganz gleich, wie die Rechte vorher aussahen.

Eine Datei, die dir nicht gehört, kannst du so nicht ändern:

```console
$ chmod o+w /etc/passwd
chmod: Operation not permitted (os error 1)
```

Der Kernel lehnt ab, weil `student` nicht der Besitzer ist. Die Meldung ist der Stand der uutils-Fassung in Ubuntu 26.04; die GNU-Fassung nennt zusätzlich die Datei: `chmod: changing permissions of '/etc/passwd': Operation not permitted`.

⁠**Kurz gesagt:** `chmod` ändert Rechte; die symbolische Angabe nennt wer (`ugoa`), was (`+ - =`) und welche Rechte (`rwx`), und nur der Besitzer und root dürfen das.

### Die Oktalschreibweise

<span class="anker" id="stufe-3-3"></span>

Will man alle neun Rechte auf einmal festlegen, wird die symbolische Schreibweise lang. Weil jede Klasse genau drei Bits hat und drei Bits eine Zahl von 0 bis 7 ergeben, passt jede Klasse in eine einzige Ziffer. Drei Ziffern beschreiben dann alle neun Rechte.

:::definition Definition 3.2 (Oktalschreibweise)
<span class="anker" id="satz-3-2"></span>

In der __Oktalschreibweise__ steht für jede Klasse eine Ziffer von 0 bis 7. Sie entsteht, indem man die Werte der vorhandenen Rechte addiert: `r` zählt 4, `w` zählt 2, `x` zählt 1. Die drei Ziffern stehen in der Reihenfolge Besitzer, Gruppe, andere.
:::

Der Name kommt von „oktal“, achtwertig: Jede Ziffer hat acht mögliche Werte. Die Werte 4, 2 und 1 sind genau die Stellenwerte der drei Bits aus Unterabschnitt [3.1](#stufe-3-1): `r` sitzt auf der Stelle, die 4 zählt, `w` auf der Stelle, die 2 zählt, `x` auf der Stelle, die 1 zählt.

::::beispiel Von den Buchstaben zur Zahl
Der Besitzer hat `rwx`, also $4 + 2 + 1 = 7$. Die Gruppe hat `r-x`, also $4 + 0 + 1 = 5$. Die anderen haben `---`, also $0 + 0 + 0 = 0$. Zusammen ergibt das 750. Abbildung [10](#abb-10) rechnet es Schritt für Schritt.

:::abbildung linux/k7oktal 10
Rechenbild: oben `rwx r-x ---` in drei Gruppen. Darunter für jede Gruppe die Bits `111`, `101`, `000`, darunter die Stellenwerte 4, 2, 1. Zeile für Zeile erscheinen die Summen $4+2+1 = 7$, $4+0+1 = 5$, $0+0+0 = 0$ und zum Schluss die Zahl 750.
:::

Umgekehrt zerlegt man jede Ziffer in 4, 2 und 1: Die 6 ist $4 + 2$, also `rw-`; die 4 ist nur `r--`. 644 heißt deshalb `rw-r--r--`.
::::

⁠**Kurz gesagt:** In der Oktalschreibweise ist jede Klasse eine Ziffer aus den Werten $r = 4$, $w = 2$, $x = 1$; drei Ziffern für Besitzer, Gruppe und andere.

:::hintergrund Warum gerade Oktal und warum die Summe gefahrlos ist
Rechner speichern Bits, Menschen lesen lieber kurze Zahlen. Eine Ziffer im Oktalsystem steht für genau drei Bits, und genau drei Bits hat jede Klasse. So entspricht jede Ziffer einer Klasse, ohne dass eine Klasse über zwei Ziffern verteilt wäre. Das verbreitetere Hexadezimalsystem fasst vier Bits zu einer Ziffer zusammen und würde die Klassen zerschneiden. Die Addition der Werte 4, 2 und 1 kann nie einen Übertrag erzeugen, weil jeder Wert höchstens einmal vorkommt und jeder ein eigenes Bit belegt. Sie ist deshalb dasselbe wie das Zusammensetzen der Bits mit „oder“: Bit für Bit ist das Ergebnis 1, wenn eines der Rechte dort 1 ist.
:::

### chmod mit Zahlen

<span class="anker" id="stufe-3-4"></span>

`chmod` versteht die Oktalschreibweise direkt. Statt zu sagen, was sich ändern soll, legst du fest, wie das Ergebnis aussieht.

:::definition Definition 3.3 (chmod mit Oktalzahl)
<span class="anker" id="satz-3-3"></span>

`chmod ziffern datei …` setzt die neun Rechte genau auf den Wert der drei Oktalziffern. Alle Rechte, die die Zahl nicht enthält, sind danach weg.
:::

`stat -c` mit `%a` zeigt die Rechte als Oktalzahl:

```console
$ chmod 640 einkauf.txt
$ stat -c '%a %A %n' einkauf.txt
640 -rw-r----- einkauf.txt
$ chmod 644 einkauf.txt
$ stat -c '%a %A %n' einkauf.txt
644 -rw-r--r-- einkauf.txt
```

Mit 640 durfte nur noch die Gruppe mitlesen, mit 644 wieder alle. Tabelle [1](#tab-1) sammelt die Zahlen, die man im Alltag fast immer braucht.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Häufige Rechte in beiden Schreibweisen

| Zahl | Buchstaben | typisch für |
|---|---|---|
| 644 | `rw-r--r--` | gewöhnliche Dateien, die alle lesen dürfen |
| 600 | `rw-------` | private Dateien |
| 640 | `rw-r-----` | Dateien, die eine Gruppe mitlesen darf |
| 755 | `rwxr-xr-x` | Programme und Verzeichnisse für alle |
| 750 | `rwxr-x---` | Programme und Verzeichnisse für eine Gruppe |
| 700 | `rwx------` | private Programme und Verzeichnisse |

::::beispiel Ein Tagebuch nur für dich
Eine Datei, die außer dir niemand lesen soll, bekommt 600. Mit Buchstaben ginge dasselbe als `chmod u=rw,go= tagebuch.txt`: Hinter dem Gleichheitszeichen steht nichts, also bekommen Gruppe und andere gar keine Rechte. Die Zahl ist kürzer und legt alles auf einmal fest; die Buchstaben sind sicherer, wenn man nur eine einzelne Klasse ändern will.
::::

⁠**Kurz gesagt:** `chmod 640 datei` setzt alle neun Rechte auf einmal; `stat -c '%a'` zeigt sie als Zahl.

:::warnung chmod 777 ist keine Lösung
Meldet ein Befehl „Permission denied“, liegt es nahe, einer Datei mit `chmod 777` alle Rechte für alle zu geben. Damit darf jeder Benutzer und jedes Programm auf dem Rechner sie ändern, auch ein fehlerhaftes oder bösartiges. Finde stattdessen heraus, welcher Klasse welches Recht fehlt, und gib genau dieses eine. Oft ist die Meldung auch richtig, und der Zugriff soll nicht klappen.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-5"></span>

:::aufgabe Aufgabe 6 ★★ Zwischen den Schreibweisen umrechnen
<span class="anker" id="aufg-6"></span>

(a) Schreibe als Oktalzahl: `rwxr-xr-x`, `rw-r-----`, `r--------`, `rwx--x--x`. (b) Schreibe mit Buchstaben: 600, 711, 604, 775. (c) Warum gibt es keine Rechte-Ziffer 8?

:::loesung
(a) `rwx r-x r-x` ergibt $7, 5, 5$, also 755; `rw- r-- ---` ergibt 640; `r-- --- ---` ergibt 400; `rwx --x --x` ergibt 711. (b) 600 ist `rw-------`, 711 ist `rwx--x--x`, 604 ist `rw----r--`, 775 ist `rwxrwxr-x`. Jede Ziffer zerlegt man in 4, 2 und 1: $7 = 4 + 2 + 1$, $6 = 4 + 2$, $5 = 4 + 1$, $1 = 1$. (c) Drei Bits ergeben höchstens $4 + 2 + 1 = 7$. Für eine 8 bräuchte eine Klasse ein viertes Recht, das es nicht gibt.
:::
:::

:::aufgabe Aufgabe 7 ★★ Eine Folge von chmod vorhersagen
<span class="anker" id="aufg-7"></span>

Lege eine Datei `probe.txt` an und gib ihr mit `chmod 640` die Rechte `rw-r-----`. Sage für jeden der folgenden Befehle voraus, welche Oktalzahl danach gilt, und prüfe mit `stat -c '%a %A %n'`: (a) `chmod u+x,g-r probe.txt`, (b) `chmod a=r probe.txt`, (c) `chmod go+w probe.txt`, (d) `chmod 644 probe.txt`.

:::loesung
```console
$ touch probe.txt
$ chmod 640 probe.txt
$ chmod u+x,g-r probe.txt
$ stat -c '%a %A %n' probe.txt
700 -rwx------ probe.txt
$ chmod a=r probe.txt
$ stat -c '%a %A %n' probe.txt
444 -r--r--r-- probe.txt
$ chmod go+w probe.txt
$ stat -c '%a %A %n' probe.txt
466 -r--rw-rw- probe.txt
$ chmod 644 probe.txt
$ stat -c '%a %A %n' probe.txt
644 -rw-r--r-- probe.txt
```

(a) `u+x` macht aus `rw-` beim Besitzer `rwx`, `g-r` nimmt der Gruppe ihr einziges Recht: 700. (b) `a=r` setzt bei allen drei Klassen genau `r` und nimmt alles andere weg, auch das x des Besitzers: 444. (c) `go+w` fügt Gruppe und anderen `w` hinzu, der Besitzer behält nur `r`: 466. Das ist ein seltsamer Zustand, in dem andere mehr dürfen als der Besitzer. (d) 644 setzt alle neun Bits neu, ganz gleich, was vorher war.
:::
:::
