---
title: Rechte bei Verzeichnissen
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120500
summary: Auch Verzeichnisse haben die neun Rechte, aber ein Verzeichnis ist keine gewöhnliche Datei: Es ist eine Tabelle von Namen.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Auch Verzeichnisse haben die neun Rechte, aber ein Verzeichnis ist keine gewöhnliche Datei: Es ist eine Tabelle von Namen. Dieser Abschnitt zeigt, was Lesen, Schreiben und Ausführen bei so einer Tabelle bedeuten, und löst die Überraschung vom Anfang des Kapitels auf.
:::

### Lesen: die Namen sehen

<span class="anker" id="stufe-4-1"></span>

Ein Verzeichnis ist nach [Kapitel 3, Abschnitt 8.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-2) eine Tabelle, die Namen auf Inode-Nummern abbildet. Mit so einer Tabelle kann man drei Dinge tun: die Namen darin lesen, einen Namen benutzen, um zu seiner Datei zu gelangen, und die Tabelle ändern. Für jedes davon gibt es ein Recht. Abbildung [11](#abb-11) zeigt alle drei auf einmal; die folgenden Unterabschnitte nehmen sie einzeln durch.

:::abbildung linux/k7verzrechte 11
Das Verzeichnis `fach` als Tabelle mit den Spalten Name und Inode und einer Zeile `brief.txt` mit ihrer Inode-Nummer, rechts daneben die Datei. Erster Schritt, Recht r: Ein Auge liest die Spalte Name; die Spalte Inode bleibt verdeckt. Zweiter Schritt, Recht x: Ein Pfeil geht vom Namen über die Inode-Nummer zur Datei. Dritter Schritt, Recht w zusammen mit x: Ein Stift fügt eine Zeile `neu.txt` hinzu; die Datei `brief.txt` wird dabei nicht berührt.
:::

:::definition Definition 4.1 (Leserecht eines Verzeichnisses)
<span class="anker" id="satz-4-1"></span>

Das Leserecht `r` an einem Verzeichnis erlaubt, die Namen seiner Einträge aufzulisten.
:::

Für die Versuche dieses Abschnitts legst du ein Verzeichnis `fach` mit einem Brief darin an, wie ein Postfach:

```console
$ mkdir fach
$ echo "Treffen am Freitag" > fach/brief.txt
$ ls -ld fach
drwxr-xr-x 2 student student 4096 Nov 10 12:32 fach
```

Neue Verzeichnisse bekommen auf dem Testsystem `rwxr-xr-x`. Jetzt nimmst du dir selbst das Ausführungsrecht und behältst nur Lesen und Schreiben:

```console
$ chmod 644 fach
$ ls -ld fach
drw-r--r-- 2 student student 4096 Nov 10 12:32 fach
$ ls fach
brief.txt
$ cat fach/brief.txt
cat: fach/brief.txt: Permission denied
$ cd fach
bash: cd: fach: Permission denied
```

Den Namen `brief.txt` kann `ls` lesen, denn das Leserecht ist da. Den Brief selbst aber kann `cat` nicht öffnen, obwohl die Datei `rw-r--r--` hat, und `cd` scheitert ebenfalls. Dafür fehlt etwas, das der nächste Unterabschnitt erklärt.

::::beispiel Namen ohne Angaben
`ls -l` will zu jedem Namen auch die Angaben aus der Inode zeigen. Die kann es ohne Ausführungsrecht nicht holen:

```console
$ ls -l fach
total 0
-????????? ? ? ? ?            ? brief.txt
```

Der Name ist da, alles andere sind Fragezeichen. Die GNU-Fassung von `ls` schreibt zusätzlich für jeden Eintrag „cannot access … Permission denied“; die uutils-Fassung in Ubuntu 26.04 zeigt nur die Fragezeichen.
::::

⁠**Kurz gesagt:** `r` an einem Verzeichnis erlaubt, die Namen zu lesen, und nicht mehr.

### Ausführen: hindurchgehen

<span class="anker" id="stufe-4-2"></span>

Ein Verzeichnis lässt sich nicht als Programm starten. Das dritte Recht hat bei Verzeichnissen deshalb eine eigene Bedeutung: Es entscheidet, ob man die Tabelle benutzen darf, um von einem Namen zur Datei zu kommen.

:::definition Definition 4.2 (Ausführungsrecht eines Verzeichnisses)
<span class="anker" id="satz-4-2"></span>

Das Ausführungsrecht `x` an einem Verzeichnis, auch Suchrecht genannt, erlaubt, über die Namen in diesem Verzeichnis auf die Einträge zuzugreifen: Dateien darin zu öffnen, ihre Angaben zu lesen und mit `cd` in das Verzeichnis zu wechseln. Den Namen muss man dafür schon kennen.
:::

Diesmal bekommt `fach` nur das Ausführungsrecht, für alle drei Klassen:

```console
$ chmod 111 fach
$ ls -ld fach
d--x--x--x 2 student student 4096 Nov 10 12:32 fach
$ ls fach
ls: cannot open directory 'fach': Permission denied
$ cat fach/brief.txt
Treffen am Freitag
$ cd fach
$ pwd
/home/student/linuxk7/fach
$ cd ..
```

Jetzt ist es genau umgekehrt: Auflisten geht nicht, aber wer den Namen `brief.txt` kennt, kann den Brief lesen, und `cd` klappt. Ein Verzeichnis mit `x` und ohne `r` ist wie ein Haus mit Briefkästen ohne Namensschilder: Wer den Namen kennt, kann einwerfen und abholen, wer ihn nicht kennt, erfährt ihn hier nicht.

⁠**Kurz gesagt:** `x` an einem Verzeichnis erlaubt, durch einen bekannten Namen zu einer Datei darin zu gelangen; `r` ohne `x` zeigt Namen, die man nicht benutzen kann.

### Schreiben: Einträge ändern

<span class="anker" id="stufe-4-3"></span>

Bleibt das Schreibrecht. Eine Tabelle zu ändern heißt, eine Zeile hinzuzufügen, eine zu streichen oder einen Namen zu ändern. Genau das geschieht, wenn man in einem Verzeichnis eine Datei anlegt, löscht oder umbenennt.

:::definition Definition 4.3 (Schreibrecht eines Verzeichnisses)
<span class="anker" id="satz-4-3"></span>

Das Schreibrecht `w` an einem Verzeichnis erlaubt, zusammen mit dem Ausführungsrecht `x`, Einträge anzulegen, zu löschen und umzubenennen. Ohne `x` nützt `w` nichts.
:::

Mit `r-x` für alle darf man in `fach` hineinschauen, aber nichts verändern:

```console
$ chmod 555 fach
$ touch fach/neu.txt
touch: cannot touch 'fach/neu.txt': Permission denied
$ rm fach/brief.txt
rm: cannot remove 'fach/brief.txt': Permission denied
$ chmod 755 fach
$ touch fach/neu.txt
$ ls fach
brief.txt  neu.txt
```

Ohne `w` scheitern Anlegen und Löschen, mit `rwx` für den Besitzer klappen sie wieder. Bemerkenswert ist das `rm`: Der Brief hat `rw-r--r--`, du darfst ihn also verändern. Löschen darfst du ihn trotzdem nicht, solange das Verzeichnis kein Schreibrecht hat.

⁠**Kurz gesagt:** `w` und `x` an einem Verzeichnis erlauben, darin Dateien anzulegen, zu löschen und umzubenennen.

### Löschen ändert das Verzeichnis

<span class="anker" id="stufe-4-4"></span>

Jetzt lässt sich die Überraschung vom Anfang auflösen. Ob du eine Datei löschen darfst, hängt nicht an ihren eigenen Rechten. Abbildung [12](#abb-12) zeigt, warum.

:::abbildung linux/k7loeschen 12
Links das Verzeichnis `fach` als Tabelle mit einem Schloss `w` an der Tabelle, rechts die Datei `brief.txt` mit einem Schloss an ihrem Inhalt (`r--r--r--`). `rm` streicht die Zeile `brief.txt` aus der Tabelle; dabei öffnet sich nur das Schloss der Tabelle. Das Schloss der Datei bleibt zu und wird nicht gebraucht. Weil kein anderer Name mehr auf die Inode zeigt, wird sie danach grau: freigegeben.
:::

:::satz Satz 4.4 (Löschen)
<span class="anker" id="satz-4-4"></span>

Eine Datei zu löschen heißt, ihren Namen aus einem Verzeichnis zu streichen. Bei einem gewöhnlichen Verzeichnis braucht man dafür das Schreib- und das Ausführungsrecht an diesem Verzeichnis. Die Rechte der Datei selbst spielen dabei keine Rolle.
:::

Das folgt direkt aus [Kapitel 3, Abschnitt 8.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-4): `rm` verändert nur die Tabelle des Verzeichnisses. Die Rechte einer Datei schützen ihren Inhalt, nicht ihren Namen.

::::beispiel Einen schreibgeschützten Brief löschen
Gib dem Brief nur noch Leserechte und versuche, etwas anzuhängen:

```console
$ chmod 444 fach/brief.txt
$ ls -l fach/brief.txt
-r--r--r-- 1 student student 19 Nov 10 12:32 fach/brief.txt
$ echo "Bitte Kuchen mitbringen" >> fach/brief.txt
bash: fach/brief.txt: Permission denied
$ rm fach/brief.txt
rm: remove write-protected regular file 'fach/brief.txt'? y
$ ls fach
neu.txt
```

Anhängen scheitert, denn dafür bräuchte die Datei das Schreibrecht. Löschen klappt, denn `fach` hat für dich `rwx`. `rm` fragt vorher nach, weil die Datei schreibgeschützt ist; du antwortest mit `y` (englisch „yes“). Diese Frage ist eine Höflichkeit von `rm`, kein Schutz: Mit `rm -f` fällt sie weg, und der Kernel hätte das Löschen ohnehin erlaubt.
::::

⁠**Kurz gesagt:** Löschen ändert das Verzeichnis, nicht die Datei; wer ein Verzeichnis schreiben darf, entscheidet über alle Namen darin.

:::hintergrund Und wie schützt man eine Datei vor dem Löschen?
Wer verhindern will, dass andere eine Datei löschen oder umbenennen, muss das Verzeichnis schützen, nicht die Datei: Andere dürfen dort kein Schreibrecht haben. Das ist bei Heimatverzeichnissen der Fall, deshalb kann dort nur der Besitzer Namen anlegen und streichen. Schwierig wird es bei Verzeichnissen, in die alle schreiben sollen; für sie gibt es ein eigenes, besonderes Recht. Umgekehrt gilt: Wer in einem fremden Verzeichnis Schreibrecht hat, kann dort jede Datei löschen und unter demselben Namen eine neue anlegen, auch wenn er die alte nicht lesen durfte.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-5"></span>

:::aufgabe Aufgabe 8 ★★ Ein Verzeichnis mit drei Rechten
<span class="anker" id="aufg-8"></span>

Lege ein Verzeichnis `test` mit einer Datei `test/a.txt` an. Gib dem Verzeichnis nacheinander die Rechte 644, 555 und 311, in dieser Reihenfolge. Sage jedes Mal vorher, ob `ls test`, `cat test/a.txt`, `cd test` (danach `cd ..`), `touch test/b.txt` und `rm test/a.txt` klappen, und prüfe dann. Gib dem Verzeichnis zum Schluss wieder 755.

:::loesung
Mit 644, also `rw-` für den Besitzer, aber ohne `x`:

```console
$ mkdir test
$ echo a > test/a.txt
$ chmod 644 test
$ ls test
a.txt
$ cat test/a.txt
cat: test/a.txt: Permission denied
$ cd test
bash: cd: test: Permission denied
$ touch test/b.txt
touch: setting times of 'test/b.txt': Permission denied
$ rm test/a.txt
rm: cannot remove 'test/a.txt': Permission denied
```

Nur `ls` klappt, denn dafür reicht `r`. Alles andere braucht `x`, auch Anlegen und Löschen, obwohl `w` da ist. Die Meldung von `touch` ist der Stand der uutils-Fassung in Ubuntu 26.04; die GNU-Fassung meldet „cannot touch 'test/b.txt': Permission denied“.

Mit 555, also `r-x` für alle:

```console
$ chmod 555 test
$ ls test
a.txt
$ cat test/a.txt
a
$ cd test
$ cd ..
$ touch test/b.txt
touch: cannot touch 'test/b.txt': Permission denied
$ rm test/a.txt
rm: cannot remove 'test/a.txt': Permission denied
```

Lesen, Hineinschauen und Wechseln klappen, Anlegen und Löschen nicht, denn `w` fehlt.

Mit 311, also `-wx` für den Besitzer:

```console
$ chmod 311 test
$ ls test
ls: cannot open directory 'test': Permission denied
$ cat test/a.txt
a
$ cd test
$ cd ..
$ touch test/b.txt
$ rm test/a.txt
$ chmod 755 test
$ ls test
b.txt
```

Auflisten scheitert, denn `r` fehlt. Alles, was einen bekannten Namen benutzt, klappt, und mit `w` und `x` auch Anlegen und Löschen. Deshalb kam 311 zuletzt: Danach ist `a.txt` gelöscht, und `b.txt` ist neu.
:::
:::

:::aufgabe Aufgabe 9 ★ Schutz vor dem Löschen
<span class="anker" id="aufg-9"></span>

(a) Warum konntest du `fach/brief.txt` löschen, obwohl die Datei `r--r--r--` hatte? (b) Welche Rechte müsste `fach` haben, damit niemand außer root Dateien darin löschen kann, du aber weiterhin alle Briefe lesen kannst? (c) Wozu fragt `rm` bei einer schreibgeschützten Datei überhaupt nach?

:::loesung
(a) Löschen streicht nur den Namen aus der Tabelle von `fach`, und für `fach` hatte `student` `rwx`. Die Rechte `r--r--r--` der Datei schützen nur ihren Inhalt. (b) `fach` braucht für alle Klassen `r-x`, also 555: Ohne `w` kann niemand außer root dort Namen anlegen oder streichen; mit `r` und `x` kannst du alle Briefe sehen und öffnen, sofern die Briefe selbst `r` für dich haben. Als Besitzer könntest du das Verzeichnis allerdings mit `chmod` jederzeit wieder freigeben. (c) `rm` fragt aus Rücksicht: Wer einer Datei das Schreibrecht genommen hat, wollte sie vermutlich schützen, also vergewissert sich `rm`. Der Kernel würde das Löschen ohne Frage erlauben; `rm -f` fragt nicht.
:::
:::
