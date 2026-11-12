---
title: Die Rechte einer Datei
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120300
summary: Jetzt, da klar ist, wer auf dem Rechner etwas tun kann, geht es um die Dateien.
tags: Besitzer, Gruppe, Klassen, Leserecht, Schreibrecht, Ausführungsrecht
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Jetzt, da klar ist, wer auf dem Rechner etwas tun kann, geht es um die Dateien. Dieser Abschnitt zeigt, was jede Datei über sich selbst speichert: wem sie gehört, zu welcher Gruppe sie gehört und was Besitzer, Gruppe und alle übrigen mit ihr tun dürfen. Danach kannst du die zehn Zeichen am Anfang einer Zeile von `ls -l` vollständig lesen.
:::

### Besitzer und Gruppe einer Datei

<span class="anker" id="stufe-2-1"></span>

Damit Linux bei einer Datei entscheiden kann, wer sie benutzen darf, muss die Datei selbst etwas über ihre Zugehörigkeit wissen. Diese Angaben stehen in ihrer Inode, gleich neben der Größe und den Zeitstempeln.

:::definition Definition 2.1 (Besitzer, Gruppe einer Datei)
<span class="anker" id="satz-2-1"></span>

Jede Datei hat einen __Besitzer__, einen Benutzer, und eine __Gruppe__. In ihrer Inode stehen beide als Nummern. Eine neue Datei gehört dem Benutzer des Prozesses, der sie anlegt, und der Hauptgruppe dieses Prozesses.
:::

Lege im Übungsverzeichnis eine Einkaufsliste an; sie begleitet dich durch das ganze Kapitel. `printf` mit der Vorlage `'%s\n'` schreibt jedes Argument in eine eigene Zeile ([Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)):

```console
$ printf '%s\n' Milch Brot Äpfel Kaffee > einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 25 Nov 10 12:32 einkauf.txt
$ ls -n einkauf.txt
-rw-r--r-- 1 1000 1000 25 Nov 10 12:32 einkauf.txt
```

Die Datei gehört dem Benutzer `student` und der Gruppe `student`. Steht bei dir am Anfang `-rw-rw-r--`, ist das eine andere Voreinstellung deines Systems; für die Versuche macht es keinen Unterschied. Die Option `-n` (englisch „numeric“) lässt `ls` die Übersetzung weg und zeigt, was wirklich in der Inode steht: zweimal die Zahl 1000. Abbildung [5](#abb-5) zeigt, woher die Namen kommen.

:::abbildung linux/k7besitz 5
Links die Inode von `einkauf.txt` mit den Feldern Besitzer `1000` und Gruppe `1000` (übrige Felder grau). Rechts `/etc/passwd` und `/etc/group`. `ls -l` schlägt die erste 1000 in `/etc/passwd` nach und schreibt `student`, dann die zweite in `/etc/group` und schreibt wieder `student`. Darunter die Zeile von `ls -n`, in der die Zahlen unverändert stehen.
:::

⁠**Kurz gesagt:** Jede Datei hat einen Besitzer und eine Gruppe, als Nummern in ihrer Inode; `ls -l` zeigt die Namen, `ls -n` die Nummern.

### Drei Klassen: Besitzer, Gruppe, alle anderen

<span class="anker" id="stufe-2-2"></span>

Für eine Datei gibt es unzählige mögliche Benutzer. Für jeden einzeln festzulegen, was er darf, wäre aufwendig. Unix teilt deshalb alle, die auf eine Datei zugreifen, in drei Klassen ein, wie ein Haus, das einen Schlüssel für den Eigentümer, einen für die Familie und eine Klingel für alle anderen hat.

:::definition Definition 2.2 (Klasse)
<span class="anker" id="satz-2-2"></span>

Für eine Datei fällt jeder Prozess in genau eine von drei __Klassen__:

<ul>

<li>

in die Klasse **Besitzer**, kurz `u` (englisch „user“), wenn seine Benutzernummer die des Besitzers ist;

</li>

<li>

sonst in die Klasse **Gruppe**, kurz `g`, wenn die Gruppe der Datei seine Hauptgruppe oder eine seiner Zusatzgruppen ist;

</li>

<li>

sonst in die Klasse **andere**, kurz `o` (englisch „others“).

</li>

</ul>
:::

Die Reihenfolge der Aufzählung ist wichtig: Wer Besitzer ist, gehört zur ersten Klasse, auch wenn er zusätzlich Mitglied der Gruppe ist. Abbildung [6](#abb-6) ordnet drei Benutzer einer Datei zu.

:::abbildung linux/k7klassen 6
In der Mitte die Datei `einkauf.txt` mit Besitzer `student` und Gruppe `student`. Drei Benutzer kommen von links: `student` landet im Feld u. Ein Benutzer, der Mitglied der Gruppe `student` ist, landet im Feld g. Ein dritter Benutzer, der weder Besitzer noch Mitglied ist, landet im Feld o. Jeder steht in genau einem Feld.
:::

⁠**Kurz gesagt:** Für jede Datei gehört jeder Prozess zu genau einer Klasse: Besitzer (u), Gruppe (g) oder andere (o).

:::hintergrund Warum es genau drei Klassen gibt
Die allgemeinste Lösung wäre eine Liste an jeder Datei, die für beliebig viele Benutzer festhält, was sie dürfen. Als Unix entstand, war Speicher teuer, und eine solche Liste hätte jede Datei aufgebläht und jeden Zugriff verlangsamt, weil die Liste durchsucht werden muss. Die Entwickler rechneten aus, dass sie sich etwa neun Bits je Datei leisten konnten. Sie stellten fest, dass drei Arten von Zugriff genügen und dass sich die meisten Wünsche mit drei Einträgen ausdrücken lassen. Die Namen der Einträge brauchten keinen Platz: Besitzer und Gruppe stehen ohnehin in der Inode, und „alle anderen“ ist einfach der Rest. Dazu genügt bei jedem Zugriff ein Blick in die Inode, die der Kernel sowieso liest, und ein paar einfache Vergleiche. Was sich so nicht ausdrücken lässt, etwa „Anna und Ben ja, alle anderen nein“, ohne eine eigene Gruppe anzulegen, braucht eine Erweiterung mit längeren Listen.
:::

### Lesen, Schreiben, Ausführen

<span class="anker" id="stufe-2-3"></span>

Für jede Klasse legt die Datei fest, was erlaubt ist. Drei Arten von Zugriff genügen für fast alles, was man mit einer Datei tun kann: hineinschauen, verändern und als Programm starten.

:::definition Definition 2.3 (Lese-, Schreib- und Ausführungsrecht)
<span class="anker" id="satz-2-3"></span>

Für eine gewöhnliche Datei bedeutet

<ul>

<li>

das __Leserecht__ `r` (englisch „read“): Der Inhalt darf gelesen werden;

</li>

<li>

das __Schreibrecht__ `w` (englisch „write“): Der Inhalt darf verändert werden, also überschrieben, angehängt oder geleert;

</li>

<li>

das __Ausführungsrecht__ `x` (englisch „execute“): Die Datei darf als Programm gestartet werden.

</li>

</ul>

Jede der drei Klassen hat jedes der drei Rechte oder hat es nicht. Das ergibt neun Rechte je Datei.
:::

Bemerkenswert ist, was in der Liste fehlt: Das Schreibrecht erlaubt nicht, die Datei umzubenennen oder zu löschen. Darüber entscheiden nicht die Rechte der Datei. Abbildung [7](#abb-7) zeigt, worauf die drei Rechte wirken und worauf nicht.

:::abbildung linux/k7rwx 7
Rechts die Datei `einkauf.txt` als Kasten mit ihrem Inhalt, links die Zeile mit ihrem Namen in der Tabelle des Verzeichnisses (grau). Nacheinander erscheinen an der Datei drei Symbole: ein Auge über dem Inhalt (r, lesen), ein Stift im Inhalt (w, verändern), ein Startknopf (x, als Programm starten). Zum Schluss leuchtet die Zeile mit dem Namen auf; ein Pfeil von w dorthin wird durchgestrichen: Umbenennen und Löschen betreffen die Tabelle, nicht die Datei.
:::

⁠**Kurz gesagt:** `r` erlaubt Lesen, `w` Verändern des Inhalts, `x` Starten als Programm; jede der drei Klassen hat jedes Recht oder nicht.

:::hintergrund Warum jeder Benutzer eine eigene Gruppe bekommt
Viele ältere Unix-Systeme steckten alle Menschen in eine gemeinsame Hauptgruppe, etwa `users`. Eine neue Datei gehörte dann dieser Gruppe, und wer ihr Rechte für die Gruppe gab, gab sie allen Menschen auf dem Rechner. Debian, Ubuntu und die meisten heutigen Distributionen gehen einen anderen Weg: Jeder Benutzer bekommt eine eigene Gruppe mit nur einem Mitglied, nämlich ihm selbst, und sie wird seine Hauptgruppe. Rechte für die Gruppe einer neuen Datei betreffen dann zunächst niemanden außer dem Besitzer. Wer eine Datei teilen will, gibt sie bewusst einer gemeinsamen Gruppe. So kann man neuen Dateien von vornherein Rechte für die Gruppe geben, ohne dass Fremde davon profitieren.
:::

### Die Rechte-Spalte lesen: ls -l und stat

<span class="anker" id="stufe-2-4"></span>

Die neun Rechte stehen in der Inode als neun einzelne Bits. `ls -l` zeigt sie als Buchstaben, und jetzt kannst du die zehn Zeichen am Zeilenanfang vollständig lesen. Abbildung [8](#abb-8) zerlegt sie.

:::abbildung linux/k7spalte 8
Die Zeile `-rw-r--r-- 1 student student 25 … einkauf.txt`. Die Spalten nach den Rechten bleiben grau, bis auf Besitzer und Gruppe; auch das erste Zeichen, die schon bekannte Art der Datei, bleibt grau. Dann erscheinen drei Klammern über je drei Zeichen mit den Beschriftungen u, g und o. In jeder Gruppe stehen die Stellen für r, w und x untereinander beschriftet; ein Strich heißt „Recht fehlt“. Zum Schluss verbinden Linien u mit `student` (Besitzer) und g mit `student` (Gruppe).
:::

:::definition Definition 2.4 (Rechte-Spalte)
<span class="anker" id="satz-2-4"></span>

Die ersten zehn Zeichen einer Zeile von `ls -l` bestehen aus der Art der Datei (`-` für eine gewöhnliche Datei, `d` für ein Verzeichnis) und drei Gruppen zu je drei Zeichen für die Klassen Besitzer, Gruppe und andere, in dieser Reihenfolge. In jeder Gruppe steht an erster Stelle `r` oder `-`, an zweiter `w` oder `-`, an dritter `x` oder `-`. Ein Strich bedeutet: Dieses Recht fehlt.
:::

Drei Dateien nebeneinander:

```console
$ ls -l /etc/shadow /usr/bin/bash einkauf.txt
-rw-r----- 1 root    shadow      731 Nov 10 12:21 /etc/shadow
-rwxr-xr-x 1 root    root    1540520 Feb 13  2026 /usr/bin/bash
-rw-r--r-- 1 student student      25 Nov 10 12:32 einkauf.txt
```

::::beispiel Drei Zeilen gelesen
`/etc/shadow` hat `rw-r-----`: Der Besitzer root darf lesen und schreiben, die Gruppe `shadow` nur lesen, alle anderen nichts. Deshalb bekam `student` in Unterabschnitt [1.8](benutzer-und-gruppen.html#stufe-1-8) die Meldung „Permission denied“. `/usr/bin/bash` hat `rwxr-xr-x`: root darf alles, Gruppe und andere dürfen lesen und das Programm starten, aber nicht verändern. So kann jeder die Shell benutzen, aber niemand außer root sie ersetzen. `einkauf.txt` hat `rw-r--r--`: `student` darf lesen und schreiben, alle anderen nur lesen; starten darf sie keiner, sie ist ja auch kein Programm.
::::

Der Befehl `stat` aus [Kapitel 3, Abschnitt 8.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-1) zeigt dieselben Angaben. Mit der Option `-c` und einer Vorlage schreibt er nur, was man verlangt: `%A` steht für die Rechte in Buchstaben, `%U` für den Besitzer, `%G` für die Gruppe und `%n` für den Namen:

```console
$ stat -c '%A %U %G %n' einkauf.txt /etc/shadow /usr/bin/bash
-rw-r--r-- student student einkauf.txt
-rw-r----- root shadow /etc/shadow
-rwxr-xr-x root root /usr/bin/bash
```

Die Vorlage steht in einfachen Anführungszeichen, damit sie trotz ihrer Leerzeichen ein einziges Argument bleibt ([Kapitel 5, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)).

⁠**Kurz gesagt:** Nach dem Zeichen für die Art folgen in `ls -l` drei Gruppen `rwx` für Besitzer, Gruppe und andere; ein Strich heißt „nicht erlaubt“. `stat -c` zeigt dasselbe nach eigener Vorlage.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Aufgabe 4 ★ Zeilen von ls -l deuten
<span class="anker" id="aufg-4"></span>

Was dürfen Besitzer, Gruppe und alle anderen bei diesen Dateien? `-rw-r--r-- 1 root root 1439 … /etc/passwd` `-rw-r----- 1 root shadow 731 … /etc/shadow` `-rwxr-x--- 1 anna kochclub 120 … rechne.sh` `-rw-rw-r-- 1 ben ben 300 … notizen.txt` Darf `ben` die Datei `rechne.sh` starten, wenn er nicht zur Gruppe `kochclub` gehört? Und wenn er dazugehört?

:::loesung
`/etc/passwd` (`rw-r--r--`): root darf lesen und schreiben, die Gruppe `root` und alle anderen dürfen lesen. `/etc/shadow` (`rw-r-----`): root liest und schreibt, die Gruppe `shadow` liest, alle anderen dürfen nichts. `rechne.sh` (`rwxr-x---`): `anna` darf alles, die Gruppe `kochclub` darf lesen und starten, alle anderen nichts. `notizen.txt` (`rw-rw-r--`): `ben` und seine Gruppe `ben` lesen und schreiben, alle anderen lesen. Gehört `ben` nicht zu `kochclub`, fällt er für `rechne.sh` in die Klasse andere mit `---` und darf die Datei weder lesen noch starten. Gehört er dazu, gilt für ihn die Klasse Gruppe mit `r-x`, und er darf sie starten.
:::
:::

:::aufgabe Aufgabe 5 ★ Rechte mit stat ansehen
<span class="anker" id="aufg-5"></span>

Lass dir mit einem einzigen Aufruf von `stat -c` Rechte, Besitzer, Gruppe und Namen von `/etc/hostname`, `/etc/gshadow` und `/usr/bin/grep` anzeigen. Welche der drei Dateien darfst du lesen, welche verändern, welche starten?

:::loesung
```console
$ stat -c '%A %U %G %n' /etc/hostname /etc/gshadow /usr/bin/grep
-rw-r--r-- root root /etc/hostname
-rw-r----- root shadow /etc/gshadow
-rwxr-xr-x root root /usr/bin/grep
```

Alle drei gehören root, `student` fällt also jeweils in die Klasse Gruppe oder andere; zu den Gruppen `root` und `shadow` gehört er nicht, also gelten die letzten drei Zeichen. `/etc/hostname` darf er lesen. `/etc/gshadow`, die Schattendatei zu `/etc/group`, darf er nicht einmal lesen. `/usr/bin/grep` darf er lesen und starten. Verändern darf er keine der drei.
:::
:::
