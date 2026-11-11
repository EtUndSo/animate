---
title: Den Inhalt eines Verzeichnisses anzeigen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080400
summary: ls ist der Befehl, den man an der Kommandozeile am häufigsten tippt: Er zeigt, was in einem Verzeichnis liegt.
tags: ls, versteckte Datei, -F, -l, gewöhnliche Datei, -h
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
`ls` ist der Befehl, den man an der Kommandozeile am häufigsten tippt: Er zeigt, was in einem Verzeichnis liegt. Mit wenigen Optionen verrät er auch versteckte Einträge, die Art jedes Eintrags, Größe und Alter. Dazu gehören die Regeln, welche Namen eine Datei überhaupt haben darf.
:::

### Der Befehl ls

<span class="anker" id="stufe-3-1"></span>

Abschnitt [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) hat `ls` schon benutzt, um die Namen in `/usr` und `/` zu zeigen. Hier geht es genauer darum, was er mit seinen Argumenten macht.

:::definition Definition 3.1 (ls)
<span class="anker" id="satz-3-1"></span>

Der Befehl __ls__ gibt für jedes Verzeichnis, das als Argument genannt ist, die Namen seiner Einträge aus, nach Namen sortiert, und für jede andere Datei ihren Namen. Ohne Argument zeigt er das Arbeitsverzeichnis.
:::

Nennt man mehrere Verzeichnisse, setzt `ls` vor jede Liste den Namen des Verzeichnisses und einen Doppelpunkt. Gibt es ein Argument nicht, meldet `ls` das und macht mit den übrigen weiter. In einem Terminal ordnet `ls` die Namen platzsparend in Spalten an.

::::beispiel Mehrere Argumente
```console
$ ls /usr /home
/home:
student

/usr:
bin  games  include  lib  lib64  libexec  local  sbin  share  src
$ ls /usr/bin/bash
/usr/bin/bash
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
```

Die Verzeichnisse erscheinen alphabetisch, nicht in der getippten Reihenfolge. Für die Datei `/usr/bin/bash` wiederholt `ls` nur ihren Namen: Das ist die Bestätigung, dass es sie gibt.
::::

⁠**Kurz gesagt:** `ls` listet die Einträge von Verzeichnissen auf; für eine gewöhnliche Datei nennt es ihren Namen.

### Die versteckte Datei

<span class="anker" id="stufe-3-2"></span>

Viele Programme legen Einstellungen im Heimatverzeichnis ab. Würden diese Dateien bei jedem `ls` erscheinen, gingen die eigenen Dateien darin unter. Deshalb gibt es eine Abmachung, solche Dateien aus der normalen Anzeige herauszuhalten. Abbildung [9](#abb-9) zeigt ein Verzeichnis, das ohne Option leer scheint.

:::abbildung linux/k3versteckt 9
Dasselbe Verzeichnis `/etc/skel` zweimal angezeigt. Ohne Option bleibt die Liste leer; mit `-a` erscheinen `.`, `..` und drei Dateien, deren Namen mit einem Punkt beginnen. Die Dateien waren die ganze Zeit da.
:::

:::definition Definition 3.2 (versteckte Datei)
<span class="anker" id="satz-3-2"></span>

Eine __versteckte Datei__ ist eine Datei oder ein Verzeichnis, dessen Name mit einem Punkt beginnt. `ls` zeigt solche Einträge nur mit der Option `-a` (kurz für „all“) an; `-A` zeigt sie ebenfalls, lässt aber `.` und `..` weg.
:::

„Versteckt“ heißt nur: nicht in der gewöhnlichen Liste. Jeder, der die Datei sonst lesen darf, kann sie auch lesen; geheim ist daran nichts.

::::beispiel Die Vorlage für neue Benutzer
Das Verzeichnis `/etc/skel` enthält die Dateien, die Linux beim Anlegen eines Benutzers in dessen neues Heimatverzeichnis kopiert:

```console
$ ls /etc/skel
$ ls -a /etc/skel
.  ..  .bash_logout  .bashrc  .profile
$ ls -A /etc/skel
.bash_logout  .bashrc  .profile
```

Ohne Option scheint das Verzeichnis leer. Mit `-a` erscheinen drei Einstellungsdateien der Shell und die beiden Sondereinträge aus Unterabschnitt [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5); sie sind also echte Einträge jedes Verzeichnisses. Kopien dieser drei Dateien liegen auch in deinem Heimatverzeichnis; `ls -a ~` zeigt sie neben weiteren versteckten Dateien.
::::

⁠**Kurz gesagt:** Ein Name mit Punkt am Anfang macht eine Datei unsichtbar für das gewöhnliche `ls`; `ls -a` zeigt alles.

:::hintergrund Versteckt ist nur eine Abmachung
Eine versteckte Datei hat kein besonderes Merkmal, das im System gespeichert wäre. Es gibt nur die Regel, dass `ls` und viele andere Programme Namen überspringen, die mit einem Punkt beginnen. Dateimanager mit grafischer Oberfläche halten sich ebenfalls daran und haben einen Schalter wie „Verborgene Dateien anzeigen“. Unter Windows ist das anders: Dort ist „versteckt“ ein Merkmal, das man jeder Datei einzeln geben oder nehmen kann, unabhängig vom Namen. Unter Linux macht man eine Datei sichtbar, indem man sie umbenennt.
:::

### Die Art eines Eintrags: ls -F

<span class="anker" id="stufe-3-3"></span>

In der gewöhnlichen Liste sehen ein Verzeichnis und eine Datei gleich aus. Wer sich durch den Baum bewegen will, muss sie aber unterscheiden können.

:::definition Definition 3.3 (ls -F)
<span class="anker" id="satz-3-3"></span>

Mit der Option __-F__ (lang `--classify`) hängt `ls` an jeden Namen ein Zeichen, das die Art des Eintrags verrät: `/` für ein Verzeichnis, `*` für eine ausführbare Datei, also ein Programm, und einige weitere Zeichen für seltenere Arten. Gewöhnliche Dateien bekommen kein Zeichen.
:::

Das Zeichen gehört nicht zum Namen; `ls` fügt es nur bei der Anzeige hinzu. Ubuntu färbt die Namen im Terminal zusätzlich, Verzeichnisse etwa blau und Programme grün; die Zeichen von `-F` funktionieren aber auch ohne Farben, etwa in einer Mitschrift oder in diesem Kapitel.

::::beispiel Verzeichnisse und ein Programm
```console
$ ls -F /usr
bin/    include/  lib64/    local/  share/
games/  lib/      libexec/  sbin/   src/
$ ls -F /usr/bin/bash
/usr/bin/bash*
```

Alle Einträge von `/usr` sind Verzeichnisse. `/usr/bin/bash` ist ein Programm, die Shell selbst.
::::

⁠**Kurz gesagt:** `ls -F` markiert Verzeichnisse mit `/` und Programme mit `*`.

### Die lange Form: ls -l

<span class="anker" id="stufe-3-4"></span>

Oft will man mehr wissen als den Namen: Wie groß ist eine Datei, wann wurde sie zuletzt geändert, ist sie ein Verzeichnis? Die lange Form gibt dafür jedem Eintrag eine eigene Zeile.

:::abbildung linux/k3lsl 10
Eine Zeile von `ls -l`, Spalte für Spalte zerlegt: Art des Eintrags, Zugriffsrechte, eine Zahl, Besitzer, Gruppe, Größe in Bytes, Zeitpunkt der letzten Änderung des Inhalts und Name. Erklärt werden in diesem Abschnitt die Art, Besitzer und Gruppe, die Größe, die Zeit und der Name.
:::

:::definition Definition 3.4 (ls -l)
<span class="anker" id="satz-3-4"></span>

Mit der Option __-l__ (kurz für „long“) gibt `ls` jeden Eintrag in einer eigenen Zeile mit sieben Angaben aus: Art und Zugriffsrechte, eine Zahl, Besitzer, Gruppe, Größe in Bytes, Zeitpunkt der letzten Änderung des Inhalts und Name.
:::

Abbildung [10](#abb-10) zerlegt eine solche Zeile. Die Angaben im Einzelnen:

<ul>

<li>

Das erste Zeichen nennt die Art. Ein `-` steht für eine __gewöhnliche Datei__, also eine Datei mit Inhalt wie ein Text oder ein Programm; ein `d` steht für ein Verzeichnis. Für seltenere Arten gibt es weitere Buchstaben.

</li>

<li>

Die nächsten neun Zeichen sind die Zugriffsrechte: Sie legen fest, wer die Datei lesen, ändern oder ausführen darf. Wie man sie liest, ist ein eigenes Thema; für dieses Kapitel genügt, dass sie da stehen.

</li>

<li>

Die Zahl danach ist bei gewöhnlichen Dateien meist 1, bei Verzeichnissen größer. Um sie geht es in diesem Abschnitt nicht.

</li>

<li>

Besitzer und Gruppe nennen den Benutzer, dem die Datei gehört, und eine Gruppe von Benutzern, der sie zugeordnet ist (Benutzer und Gruppen: [Kapitel 2, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2)).

</li>

<li>

Die Größe zählt die Bytes des Inhalts.

</li>

<li>

Der Zeitpunkt ist die letzte Änderung des Inhalts; liegt er mehr als ein halbes Jahr zurück, zeigt `ls` statt der Uhrzeit das Jahr.

</li>

</ul>

Vor der Liste steht eine Zeile `total`: Sie nennt, wie viel Platz die gezeigten Einträge zusammen auf dem Datenträger belegen, in Einheiten von 1024 Byte.

::::beispiel Die Vorlage in langer Form
```console
$ ls -la /etc/skel
total 20
drwxr-xr-x  2 root root 4096 Aug 27 16:10 .
drwxr-xr-x 93 root root 4096 Nov 10 02:36 ..
-rw-r--r--  1 root root  220 Feb 13  2026 .bash_logout
-rw-r--r--  1 root root 3771 Feb 13  2026 .bashrc
-rw-r--r--  1 root root  807 Feb 13  2026 .profile
```

Die Optionen `-l` und `-a` sind gebündelt ([Kapitel 2, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-4)). Die ersten beiden Zeilen sind Verzeichnisse (`d`): `.` ist `/etc/skel` selbst, `..` ist `/etc`. Die drei übrigen sind gewöhnliche Dateien (`-`) des Benutzers `root`; `.bashrc` ist mit 3771 Bytes die größte. Ihr Inhalt wurde im Februar 2026 zuletzt geändert, als Ubuntu diese Vorlage gebaut hat.
::::

**Ein Verzeichnis selbst ansehen.** Nennt man `ls -l` ein Verzeichnis, zeigt es dessen Inhalt. Will man die Angaben über das Verzeichnis selbst, kommt die Option `-d` (kurz für „directory“) dazu:

```console
$ ls -l /usr/bin/bash
-rwxr-xr-x 1 root root 1540520 Feb 13  2026 /usr/bin/bash
$ ls -ld /etc
drwxr-xr-x 93 root root 4096 Nov 10 02:36 /etc
```

Die Shell `bash` ist eine gewöhnliche Datei mit gut anderthalb Millionen Bytes; `/etc` ist ein Verzeichnis. Dass es genau 4096 Bytes groß ist, liegt an der Art, wie ein Dateisystem Platz zuteilt: in festen Stücken dieser Größe. Erst ein Verzeichnis mit sehr vielen Einträgen braucht mehrere davon; `/usr/bin` mit über tausend Einträgen ist auf dem Testrechner 36 864 Bytes groß.

⁠**Kurz gesagt:** `ls -l` zeigt je Eintrag Art, Rechte, Besitzer, Gruppe, Größe, Änderungszeit und Namen; `-d` zeigt das Verzeichnis selbst statt seines Inhalts.

### Lesbare Größen: ls -h

<span class="anker" id="stufe-3-5"></span>

Eine Zahl wie 1540520 muss man erst in Gedanken in Dreiergruppen teilen, bevor man sie einschätzen kann. Für das schnelle Hinsehen gibt es eine kürzere Schreibweise.

:::definition Definition 3.5 (ls -h)
<span class="anker" id="satz-3-5"></span>

Zusammen mit `-l` gibt `ls` mit der Option __-h__ (kurz für „human-readable“, für Menschen lesbar) jede Größe in der größten passenden Einheit aus: `K` für 1024 Byte, `M` für $1024^2$ Byte, `G` für $1024^3$ Byte. Unter 10 steht eine Nachkommastelle, und gerundet wird immer nach oben.
:::

Die Buchstaben meinen also Zweierpotenzen, genau wie KiB, MiB und GiB aus [Kapitel 1, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1); nur schreibt `ls` das `i` nicht dazu. Weil nach oben gerundet wird, sieht man nie eine Größe, die kleiner ist als die echte.

::::beispiel Die Größe der Shell
```console
$ ls -lh /usr/bin/bash
-rwxr-xr-x 1 root root 1.5M Feb 13  2026 /usr/bin/bash
```

Aus 1 540 520 Byte wird $1\,540\,520 / 1024 \approx 1504{,}4$ KiB und daraus $1504{,}4 / 1024 \approx 1{,}469$ MiB. Weil der Wert unter 10 liegt, bekommt er eine Nachkommastelle, aufgerundet: `1.5M`. `ls` schreibt wie fast alle Werkzeuge einen Dezimalpunkt statt eines Kommas.
::::

⁠**Kurz gesagt:** `ls -lh` schreibt Größen mit `K`, `M`, `G` zu je 1024 und rundet nach oben.

### Sortieren und weitere Optionen

<span class="anker" id="stufe-3-6"></span>

`ls` sortiert sonst nach Namen. Oft ist eine andere Reihenfolge nützlicher: die größten Dateien zuerst, wenn der Platz knapp wird, oder die neuesten, wenn man die Datei von eben sucht. Tabelle [1](#tab-1) sammelt die Optionen, die man am häufigsten braucht; alle lassen sich bündeln.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Häufige Optionen von `ls`.

| Option | lang | Wirkung |
|---|---|---|
| `-a` | `--all` | auch versteckte Einträge, dazu `.` und `..` |
| `-A` | `--almost-all` | auch versteckte Einträge, ohne `.` und `..` |
| `-F` | `--classify` | Zeichen für die Art anhängen (`/` Verzeichnis, `*` Programm) |
| `-l` |  | lange Form, eine Zeile je Eintrag |
| `-h` | `--human-readable` | Größen mit `K`, `M`, `G` (zu 1024), aufgerundet |
| `-d` | `--directory` | das Verzeichnis selbst statt seines Inhalts |
| `-S` |  | nach Größe sortieren, größte zuerst |
| `-t` |  | nach Änderungszeit sortieren, neueste zuerst |
| `-r` | `--reverse` | Reihenfolge umkehren |
| `-R` | `--recursive` | auch alle Unterverzeichnisse auflisten, Ebene für Ebene |

Abbildung [11](#abb-11) zeigt, wie dieselben Einträge mit `-S`, `-t` und `-r` ihre Plätze tauschen.

:::abbildung linux/k3sortieren 11
Vier Dateien als Karten mit Name, Größe und Uhrzeit. Ohne Option liegen sie nach Namen geordnet; mit `-S` wandern die größten nach oben, mit `-t` die zuletzt geänderten, und `-r` dreht die jeweilige Reihenfolge um.
:::

::::beispiel Die größten Lizenztexte
`/usr/share/common-licenses` enthält die Texte verbreiteter Lizenzen für freie Software. `-lhS` zeigt sie nach Größe, mit lesbaren Zahlen:

```console
$ ls -lhS /usr/share/common-licenses
total 260K
-rw-r--r-- 1 root root  35K Sep 30  2017 GPL-3
-rw-r--r-- 1 root root  26K Sep 18  2024 LGPL-2.1
-rw-r--r-- 1 root root  26K Apr  3  2017 MPL-1.1
...
-rw-r--r-- 1 root root 6.0K Dec 16  1996 Artistic
-rw-r--r-- 1 root root 1.5K Aug 26  1999 BSD
...
```

Die GNU General Public License in Fassung 3 ist mit 35 KiB die größte, die BSD-Lizenz mit 1,5 KiB die kleinste der gezeigten.
::::

⁠**Kurz gesagt:** `-S` sortiert nach Größe, `-t` nach Zeit, `-r` kehrt um, `-R` steigt in alle Unterverzeichnisse.

### Dateinamen

<span class="anker" id="stufe-3-7"></span>

Unter Windows lernt man irgendwann, welche Zeichen in einem Dateinamen verboten sind. Linux ist großzügiger, und gerade das birgt Fallen, sobald man Namen in eine Befehlszeile tippt. Abbildung [12](#abb-12) zeigt die häufigste, das Leerzeichen.

:::abbildung linux/k3namen 12
Wie die Shell eine Zeile mit dem Namen `Program Files` zerlegt. Ohne Anführungszeichen entstehen zwei Wörter und damit zwei Argumente; mit Anführungszeichen bleibt der Name ein einziges Wort.
:::

:::satz Satz 3.6 (Regeln für Dateinamen)
<span class="anker" id="satz-3-6"></span>

Ein Dateiname unter Linux darf jedes Zeichen enthalten außer dem Schrägstrich `/` und dem Nullbyte, dem Byte mit dem Wert 0; bei den üblichen Dateisystemen wie ext4 ist er höchstens 255 Byte lang. Groß- und Kleinbuchstaben sind verschieden: `Brief.txt` und `brief.txt` sind zwei Dateien. Eine Endung wie `.txt` oder `.jpg` ist nur ein Teil des Namens; das System deutet sie nicht.
:::

Erlaubt ist also auch das Leerzeichen. Doch die Shell zerlegt jede Zeile an Leerzeichen in Wörter ([Kapitel 2, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-1)), und ein Name mit Leerzeichen würde zu zwei Argumenten. Damit er ein einziges Wort bleibt, schließt man ihn in Anführungszeichen ein: `"mein urlaub.txt"`. Die Shell entfernt die Anführungszeichen, bevor sie den Befehl startet; das Programm bekommt den Namen ohne sie. Die Tabulatortaste erledigt das von selbst, sie setzt einen umgekehrten Schrägstrich vor das Leerzeichen: `mein\ urlaub.txt` bedeutet dasselbe.

Ähnlich lästig ist ein Strich am Anfang eines Namens: `-liste.txt` hält jedes Programm für eine Option. Abhilfe schafft das Ende der Optionen `--` aus [Kapitel 2, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-7), oder ein Pfad, der nicht mit dem Strich beginnt, etwa `./-liste.txt`.

**Gute Namen.** Die einfachste Regel ist, solche Fälle gar nicht erst entstehen zu lassen. Wer eigene Dateien benennt, nimmt Kleinbuchstaben, Ziffern, Punkt, Bindestrich und Unterstrich: `urlaub_2026.txt` statt `Urlaub 2026.txt`. Solche Namen tippt man ohne Anführungszeichen, und sie funktionieren auf jedem System.

::::beispiel Ein Windows-Verzeichnis mit Leerzeichen
Unter WSL 2 kannst du das mit dem Windows-Verzeichnis `Program Files` ausprobieren, ohne etwas zu verändern. Die Option `-d` zeigt das Verzeichnis selbst:

```console
$ ls -d /mnt/c/Program Files
ls: cannot access '/mnt/c/Program': No such file or directory
ls: cannot access 'Files': No such file or directory
$ ls -d "/mnt/c/Program Files"
 '/mnt/c/Program Files'
$ ls /ETC
ls: cannot access '/ETC': No such file or directory
```

Ohne Anführungszeichen bekommt `ls` zwei Argumente und findet beide nicht. Mit Anführungszeichen ist es ein einziges Argument. `ls` setzt den Namen in seiner Ausgabe selbst in einfache Anführungszeichen, damit man das Leerzeichen erkennt und den Namen so wieder in eine Befehlszeile kopieren kann; das Leerzeichen vor dem Namen gehört nur zur Ausrichtung der Spalten. `/ETC` gibt es nicht, denn das Verzeichnis heißt `/etc`. In einer virtuellen Maschine oder im Live-System gibt es `/mnt/c` nicht; dort lässt sich der erste Teil des Beispiels nur nachlesen.
::::

⁠**Kurz gesagt:** Dateinamen dürfen alles außer `/` enthalten und unterscheiden Groß und Klein; Leerzeichen und ein Strich am Anfang machen Ärger, also vermeidet man sie.

:::hintergrund Warum gerade der Schrägstrich verboten ist
Der Schrägstrich trennt in einem Pfad die Namen voneinander. Dürfte ein Name selbst einen enthalten, wüsste der Kernel nicht mehr, ob `a/b` „die Datei `b` im Verzeichnis `a`“ heißt oder „die Datei mit dem Namen `a/b`“. Das Nullbyte ist verboten, weil der Kernel und die meisten Programme damit intern das Ende eines Namens markieren. Windows verbietet mehr Zeichen, nämlich `\ : * ? " < > |`, dazu Namen wie `CON` oder `NUL`, und unterscheidet Groß und Klein nicht. Das zählt, sobald Dateien zwischen beiden Welten wandern: Unter `/mnt/c` gelten die Regeln von Windows ([Kapitel 1, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)), und zwei Linux-Dateien `Brief.txt` und `brief.txt` lassen sich dort nicht nebeneinander ablegen.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-8"></span>

:::aufgabe Aufgabe 7 ★ Eine Zeile von ls -l lesen
<span class="anker" id="aufg-7"></span>

Lies die Zeile `-rw-r--r-- 1 root root 3771 Feb 13 2026 .bashrc` aus dem Beispiel in Unterabschnitt [3.4](#stufe-3-4): Welche Art von Eintrag ist es, wem gehört er, wie groß ist er, wann wurde sein Inhalt zuletzt geändert, und warum erscheint er bei `ls /etc/skel` nicht?

:::loesung
Das erste Zeichen `-` kennzeichnet eine gewöhnliche Datei. Sie gehört dem Benutzer `root` und der Gruppe `root`. Sie ist 3771 Bytes groß, knapp 3,7 KiB. Ihr Inhalt wurde am 13. Februar 2026 zuletzt geändert; weil das mehr als ein halbes Jahr zurückliegt, zeigt `ls` das Jahr statt der Uhrzeit. Bei `ls /etc/skel` erscheint sie nicht, weil ihr Name mit einem Punkt beginnt: Sie ist eine versteckte Datei, und nur `ls -a` oder `ls -A` zeigen sie.
:::
:::

:::aufgabe Aufgabe 8 ★★ Versteckte Dateien zu Hause
<span class="anker" id="aufg-8"></span>

Vergleiche `ls ~`, `ls -a ~` und `ls -A ~`. Wie viele versteckte Einträge hat dein Heimatverzeichnis? Welche davon stammen aus `/etc/skel`? Welche Einträge zeigt `-a` zusätzlich zu `-A`, und warum hat jedes Verzeichnis genau diese beiden?

:::loesung
`ls ~` zeigt deine sichtbaren Einträge, nach diesem Kapitel etwa `linuxk3`. `ls -A ~` zeigt zusätzlich die versteckten, mindestens `.bash_logout`, `.bashrc` und `.profile`: Das sind die Kopien aus `/etc/skel`, die beim Anlegen deines Kontos entstanden sind. Dazu kommen je nach dem, was du schon benutzt hast, weitere, etwa `.bash_history` mit dem Verlauf aus [Kapitel 2, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-2). Die Zahl der versteckten Einträge ist die Zahl der Namen mit Punkt am Anfang in der Ausgabe von `ls -A`. `ls -a` zeigt zusätzlich `.` und `..`. Jedes Verzeichnis hat genau diese beiden, weil jedes Verzeichnis einen Namen für sich selbst und einen für sein übergeordnetes Verzeichnis braucht, damit relative Pfade wie `../datei` funktionieren; in der Wurzel zeigt `..` auf die Wurzel selbst.
:::
:::

:::aufgabe Aufgabe 9 ★★ Die passende Option
<span class="anker" id="aufg-9"></span>

Welche Befehlszeile zeigt (a) die Einträge von `/var/log` mit der zuletzt geänderten Datei zuerst, (b) dieselben mit der zuletzt geänderten am Ende, (c) die Angaben über das Verzeichnis `/var/log` selbst in langer Form, (d) alle Einträge von `/usr/share/common-licenses` mit lesbaren Größen, kleinste zuerst? Probiere sie aus.

:::loesung
(a) `ls -lt /var/log`: Die lange Form, nach Änderungszeit sortiert, die neueste zuerst. (b) `ls -ltr /var/log`: dieselbe Reihenfolge umgekehrt, die neueste am Ende; das ist praktisch, weil das Interessante dann direkt über der Eingabeaufforderung steht. (c) `ls -ld /var/log`: `-d` zeigt das Verzeichnis selbst statt seines Inhalts:

```console
$ ls -ld /var/log
drwxrwxr-x 9 root syslog 4096 Nov 10 03:06 /var/log
```

(d) `ls -lhSr /usr/share/common-licenses`: `-S` sortiert nach Größe mit der größten zuerst, `-r` kehrt das um; die Datei `BSD` mit 1,5 KiB steht dann als erste gewöhnliche Datei oben (davor nur die drei symbolischen Links `GPL`, `LGPL` und `GFDL`), `GPL-3` unten. Versteckte Einträge gibt es in diesem Verzeichnis nicht; sonst käme `-A` dazu.
:::
:::

:::aufgabe Aufgabe 10 ★ Gute und schlechte Dateinamen
<span class="anker" id="aufg-10"></span>

Welche Namen sind erlaubt, welche machen an der Befehlszeile Ärger, und welche würdest du für eigene Dateien wählen? (a) `einkauf.txt` (b) `Einkauf.TXT` (c) `mein einkauf.txt` (d) `-einkauf.txt` (e) `einkauf/montag.txt` (f) `einkauf_montag.txt`. Liegen (a) und (b) im selben Verzeichnis, wie viele Dateien sind es?

:::loesung
<ol class="al">

<li>

`einkauf.txt` ist erlaubt und ein guter Name.

</li>

<li>

`Einkauf.TXT` ist erlaubt, aber unpraktisch: Großbuchstaben muss man genau so tippen. Im selben Verzeichnis wie (a) ist es eine zweite, eigene Datei, denn Linux unterscheidet Groß und Klein; es sind also zwei Dateien.

</li>

<li>

`mein einkauf.txt` ist erlaubt, macht aber Ärger: Ohne Anführungszeichen wird der Name an der Befehlszeile zu zwei Wörtern.

</li>

<li>

`-einkauf.txt` ist erlaubt, wird aber von jedem Befehl für eine Option gehalten; man braucht `--` oder `./-einkauf.txt`.

</li>

<li>

`einkauf/montag.txt` ist kein Dateiname, denn der Schrägstrich ist verboten. Als Pfad gelesen ist es die Datei `montag.txt` im Verzeichnis `einkauf`.

</li>

<li>

`einkauf_montag.txt` ist erlaubt und ein guter Name: Kleinbuchstaben, Unterstrich statt Leerzeichen.

</li>

</ol>

Für eigene Dateien taugen (a) und (f).
:::
:::
