---
title: Bequemer verbinden und Befehle aus der Ferne
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160500
summary: Dieser Abschnitt zeigt, wie man sich mit einem kurzen Namen verbindet, statt jedes Mal alle Angaben zu tippen, und wie man einzelne Befehle auf dem Server ausführt, ohne sich interaktiv anzumelden.
tags: ~/.ssh/config
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Dieser Abschnitt zeigt, wie man sich mit einem kurzen Namen verbindet, statt jedes Mal alle Angaben zu tippen, und wie man einzelne Befehle auf dem Server ausführt, ohne sich interaktiv anzumelden. Dabei lesen zwei Shells dieselbe Zeile; wer was erweitert, entscheidet über das Ergebnis.
:::

### Die Datei ~/.ssh/config

<span class="anker" id="stufe-4-1"></span>

Für die Anmeldung am Übungsserver tippst du bisher `ssh -i uebungsschluessel localhost`, und das nur, solange du im Übungsverzeichnis stehst. Bei einem echten Server kämen der Benutzername und oft ein anderer Port hinzu, etwa `ssh -p 2222 -i ~/.ssh/id_ed25519 anna@rechner1.example.org`. Ein Bild zur Orientierung: die Kurzwahl im Telefon. Man speichert die lange Nummer einmal unter einem Namen und wählt danach nur noch den Namen.

:::definition Definition 4.1 (~/.ssh/config)
<span class="anker" id="satz-4-1"></span>

Die Datei __`~/.ssh/config`__ enthält Einstellungen des SSH-Clients für den Benutzer. Sie ist in Abschnitte gegliedert, die mit `Host name` beginnen; die Zeilen darunter gelten, wenn man sich mit diesem Namen verbindet. Die wichtigsten Einstellungen sind `HostName` (der wirkliche Name oder die Adresse des Rechners), `User` (der Benutzername dort), `Port` und `IdentityFile` (die private Schlüsseldatei).
:::

Lege die Datei mit `nano ~/.ssh/config` an und schreibe den Eintrag für den Übungsserver hinein. Die Einrückung ist nur für Menschen da; Zeilen mit `#` am Anfang sind Kommentare.

```text ~/.ssh/config
# Uebungsserver aus Linux, Kapitel 11
Host uebung
    HostName localhost
    User student
    Port 22
    IdentityFile ~/linuxk11/uebungsschluessel
```

Die Tilde in `IdentityFile` ersetzt `ssh` selbst durch dein Heimatverzeichnis; hier ist keine Shell beteiligt. `Port 22` und `User student` wären auch ohne Eintrag so, schaden aber nicht und machen den Eintrag zum Muster für andere Server. Weil in dieser Datei auch Befehle stehen dürfen, die `ssh` beim Verbinden ausführt, verlangt es, dass nur ihr Besitzer sie schreiben darf (mit derselben Ausnahme für die eigene Gruppe wie in Abschnitt [3.7](anmelden-mit-einem-schlusselpaar.html#stufe-3-7)); mit 600 bist du auf der sicheren Seite:

```console
$ chmod 600 ~/.ssh/config
```

Danach genügt der kurze Name, und zwar von jedem Verzeichnis aus. Auf dem Server fragt `hostname` nach dem Rechnernamen:

```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ hostname
labor
$ exit
logout
Connection to localhost closed.
```

Welche Werte `ssh` für einen Namen am Ende benutzt, zeigt `ssh -G name`, ohne eine Verbindung aufzubauen. Die Ausgabe hat über hundert Zeilen; `grep` wählt vier aus:

```console
$ ssh -G uebung | grep -E '^(hostname|user|port|identityfile) '
user student
hostname localhost
port 22
identityfile ~/linuxk11/uebungsschluessel
```

Die Datei gilt nicht nur für `ssh`: Auch `scp`, `sftp` und `rsync` benutzen den Namen `uebung` mit allen Angaben. Abbildung [16](#abb-16) zeigt, wie aus dem Namen die vollständige Verbindung wird.

:::abbildung linux/k11config 16
Dateiansicht (hell): die Datei `~/.ssh/config` mit dem Eintrag `Host uebung` wie im Text. Darunter der kurze Befehl `ssh uebung`. Nacheinander leuchten die vier eingerückten Zeilen auf, und aus jeder wandert ein Teil in einen langen Befehl, der sich darunter zusammensetzt: `ssh -p 22 -i ~/linuxk11/uebungsschluessel student@localhost`. Schild: „Beides bewirkt dasselbe.“
:::

:::hintergrund Wer gewinnt, wenn eine Einstellung mehrfach vorkommt
`ssh` liest seine Einstellungen aus drei Quellen, in dieser Reihenfolge: den Optionen auf der Befehlszeile, der Datei `~/.ssh/config` und der Datei `/etc/ssh/ssh_config` für alle Benutzer. Für jede Einstellung gilt der *erste* Wert, den es findet; spätere Werte für dieselbe Einstellung übersieht es. Ausnahmen sind wieder Einstellungen, die mehrere Werte sammeln, etwa `IdentityFile`: Alle genannten Schlüsseldateien kommen in eine Liste, die `ssh` der Reihe nach probiert. Deshalb schlägt `ssh -p 2222 uebung` den Port aus der Datei (Aufgabe [12](#aufg-12)). Innerhalb einer Datei gilt dasselbe: Passen mehrere `Host`-Abschnitte, etwa ein besonderer und einer mit `Host *` für alle Rechner, gewinnt bei jeder Einstellung der Abschnitt, der weiter oben steht. Allgemeine Voreinstellungen gehören deshalb ans Ende der Datei, besondere nach oben. Die Datei `/etc/ssh/ssh_config` von Ubuntu hat genau so einen Abschnitt `Host *` mit `HashKnownHosts yes` aus Abschnitt [2.5](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2-5).
:::

⁠**Kurz gesagt:** In `~/.ssh/config` gibt man einem Server einen kurzen Namen samt Rechner, Benutzer, Port und Schlüssel; `ssh`, `scp`, `sftp` und `rsync` benutzen ihn.

### Einen Befehl auf dem Server ausführen

<span class="anker" id="stufe-4-2"></span>

Oft will man auf dem Server nur einen einzigen Befehl ausführen, etwa nachsehen, ob eine Datei angekommen ist. Dafür muss man sich nicht anmelden, eine Zeile tippen und wieder abmelden.

:::definition Definition 4.2 (Befehl auf dem Server)
<span class="anker" id="satz-4-2"></span>

Stehen hinter dem Rechnernamen weitere Wörter, `ssh rechner befehl ...`, verbindet `ssh` sie mit Leerzeichen zu einer Befehlszeile und schickt diese zum Server. Dort führt die Shell des Benutzers sie aus wie `bash -c 'befehlszeile'` ([Kapitel 5, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-1)). Die Ausgaben kommen zurück, und `ssh` endet, sobald der Befehl endet. Eine interaktive Anmeldung mit Begrüßung findet nicht statt.
:::

::::beispiel Kurze Fragen an den Server
```console
$ ssh uebung hostname
labor
$ ssh uebung 'whoami; pwd'
student
/home/student
```

Der zweite Befehl besteht aus zwei Befehlen, getrennt durch ein Semikolon ([Kapitel 4, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-1)). Die einfachen Anführungszeichen sorgen dafür, dass die eigene Shell das Semikolon nicht selbst als Trenner liest, sondern als Teil eines Arguments an `ssh` weitergibt; sonst liefe `pwd` auf deinem eigenen Rechner. Der Befehl beginnt auf dem Server im Heimatverzeichnis, nicht in dem Verzeichnis, in dem du gerade lokal stehst.
::::

Eine Befehlszeile für den Server lesen also zwei Shells nacheinander: zuerst deine eigene, die sie in Wörter zerlegt und erweitert ([Kapitel 5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-quoting-variablen-und-umgebung.html)), dann die Shell auf dem Server, die das zusammengesetzte Ergebnis noch einmal liest. Wo eine Variable ersetzt wird, hängt davon ab, welche der beiden sie sieht. `SSH_CONNECTION` gibt es nur in Sitzungen, die `sshd` gestartet hat:

```console
$ ssh uebung 'echo "Verbindung: $SSH_CONNECTION"'
Verbindung: 127.0.0.1 57032 127.0.0.1 22
$ ssh uebung "echo \"Verbindung: $SSH_CONNECTION\""
Verbindung:
```

In einfachen Anführungszeichen lässt die eigene Shell `$SSH_CONNECTION` stehen; erst die Shell auf dem Server ersetzt die Variable und findet ihren Wert. In doppelten Anführungszeichen ersetzt schon deine eigene Shell die Variable, und dort ist sie leer, denn deine Shell wurde nicht von `sshd` gestartet. Zum Server geht dann nur noch `echo "Verbindung: "`. Abbildung [17](#abb-17) zeigt den Weg der Zeile.

:::abbildung linux/k11zweishells 17
Zwei Shells lesen eine Zeile. Zwei Bahnen, jede mit ihrem Befehl darüber und zwei Kästen: links „deine Shell“, rechts „Shell auf dem Server (bash -c)“, dazwischen `ssh`. Erste Bahn: `ssh uebung 'echo "Verbindung: $SSH_CONNECTION"'` – die eigene Shell entfernt nur die einfachen Anführungszeichen, das Kärtchen `echo "Verbindung: $SSH_CONNECTION"` wandert unverändert zum Server, dort wird `$SSH_CONNECTION` zu `127.0.0.1 57032 127.0.0.1 22`. Zweite Bahn: dieselbe Zeile mit doppelten Anführungszeichen – schon die eigene Shell ersetzt die Variable durch nichts (ihr Platz im Kärtchen bleibt leer, „hier leer“), zum Server geht `echo "Verbindung: "`. Rechts die beiden Ausgaben.
:::

⁠**Kurz gesagt:** `ssh rechner 'befehl'` führt einen Befehl auf dem Server aus; die Zeile lesen zwei Shells nacheinander, und einfache Anführungszeichen heben alles für die Shell auf dem Server auf.

### Muster für Dateinamen: wer erweitert?

<span class="anker" id="stufe-4-3"></span>

Dieselbe Frage stellt sich bei Mustern wie `*.txt` ([Kapitel 5, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3)). Im Übungsverzeichnis liegt die Datei `einkauf.txt`, im Heimatverzeichnis auf dem Server, wo Befehle beginnen, liegt keine Datei mit der Endung `.txt`:

```console
$ ls *.txt
einkauf.txt
$ ssh uebung echo *.txt
einkauf.txt
$ ssh uebung 'echo *.txt'
*.txt
```

Ohne Anführungszeichen erweitert deine eigene Shell das Muster, bevor `ssh` startet, und zwar mit den Dateien deines Verzeichnisses. Zum Server geht `echo einkauf.txt`, eine Liste deiner Dateien, nicht seiner. Mit Anführungszeichen erweitert erst die Shell auf dem Server; sie findet keine passende Datei, und ein Muster ohne Treffer bleibt stehen ([Kapitel 5, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-5)). Abbildung [18](#abb-18) zeigt beide Wege.

:::abbildung linux/k11fernmuster 18
Wer erweitert `*.txt`? Links das lokale Verzeichnis `~/linuxk11` mit `einkauf.txt`, rechts das Heimatverzeichnis auf dem Server ohne `.txt`-Datei. Obere Bahn `ssh uebung echo *.txt`: Das Muster bleibt links an der eigenen Shell hängen und wird dort zu `einkauf.txt`; über die Verbindung geht `echo einkauf.txt`, Ausgabe `einkauf.txt`. Untere Bahn `ssh uebung 'echo *.txt'`: Das Muster reist in den Anführungszeichen unverändert nach rechts, die Shell dort findet nichts, Ausgabe `*.txt`.
:::

:::satz Satz 4.3 (Befehle für den Server in einfache Anführungszeichen)
<span class="anker" id="satz-4-3"></span>

Ein Befehl, der auf dem Server ausgeführt werden soll, gehört als Ganzes in einfache Anführungszeichen. Dann erreicht er die Shell auf dem Server Zeichen für Zeichen so, wie man ihn getippt hat, und Muster, Variablen und Sonderzeichen beziehen sich auf den Server. Das gilt, solange er selbst kein einfaches Anführungszeichen enthält ([Kapitel 5, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)).
:::

Hier liefen beide Seiten auf demselben Rechner, und trotzdem kam Verschiedenes heraus. Bei einem echten Server ist der Unterschied noch tückischer, denn dort gibt es die Datei `einkauf.txt` vielleicht gar nicht, und ein `rm *.txt` ohne Anführungszeichen würde auf dem Server genau die Namen löschen wollen, die zufällig in deinem lokalen Verzeichnis stehen.

⁠**Kurz gesagt:** Ohne Anführungszeichen erweitert die eigene Shell Muster und Variablen mit den eigenen Dateien und Werten; in einfachen Anführungszeichen erweitert erst der Server.

### Ströme und Exit-Status über die Verbindung

<span class="anker" id="stufe-4-4"></span>

Für die eigene Shell ist `ssh uebung 'befehl'` ein gewöhnlicher Befehl mit Standardausgabe, Fehlerausgabe und Exit-Status ([Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html)). Was der Befehl auf dem Server ausgibt, schreibt `ssh` auf seine eigene Standardausgabe, Fehlermeldungen auf seine Fehlerausgabe. Deshalb lassen sich Pipes und Umleitungen über die Verbindung hinweg verwenden:

```console
$ ssh uebung 'cat linuxk11/einkauf.txt' | sort
Brot
Kaffee
Milch
Äpfel
$ ssh uebung 'ls /etc/ssh' > ssh_dateien.txt
$ wc -l ssh_dateien.txt
12 ssh_dateien.txt
```

`cat` läuft auf dem Server, `sort` auf deinem Rechner; dazwischen liegt die Verbindung. Ebenso schreibt die Umleitung `>` außerhalb der Anführungszeichen in eine Datei auf deinem Rechner. Stünde `> ssh_dateien.txt` innerhalb der Anführungszeichen, entstünde die Datei auf dem Server.

:::satz Satz 4.4 (Der Exit-Status von ssh)
<span class="anker" id="satz-4-4"></span>

Führt `ssh` einen Befehl auf dem Server aus, endet es mit dessen Exit-Status. Scheitert dagegen die Verbindung oder die Anmeldung, endet `ssh` mit 255.
:::

::::beispiel Status 3 und Status 255
```console
$ ssh uebung 'exit 3'
$ echo $?
3
$ ssh -p 2222 localhost true
ssh: connect to host localhost port 2222: Connection refused
$ echo $?
255
```

Im ersten Fall endete die Shell auf dem Server mit 3, und `ssh` reicht die Zahl durch. Im zweiten lauscht am Port 2222 niemand; der Rechner lehnt die Verbindung ab (*connection refused*), und `ssh` meldet seinen eigenen Fehler mit 255. Weil ein Befehl auf dem Server zufällig auch mit 255 enden könnte, ist die Unterscheidung nicht ganz sicher; in Skripten ([Kapitel 10, Abschnitt 8.1](/wissen/informatik/linux-und-kommandozeile/shell-skripte/fehler-erkennen-und-melden.html#stufe-8-1)) behandelt man 255 meist als Verbindungsfehler.
::::

Abbildung [19](#abb-19) zeigt die Pipe über die Verbindung.

:::abbildung linux/k11fernstroeme 19
Eine Pipe über zwei Rechner. Rechts der Server mit `cat linuxk11/einkauf.txt`, sein Rohr 1 führt in `sshd-session`; durch die Verbindung gelangen die vier Zeilen (Milch, Brot, Äpfel, Kaffee) zum Client `ssh`, aus dessen Rohr 1 in eine Pipe zu `sort` auf dem eigenen Rechner; heraus kommt die sortierte Liste. Unten ein zweites Rohr vom Server: Der Exit-Status 3 von `bash -c 'exit 3'` wandert als Zettel zu `ssh` (`$? = 3`); darunter ein `ssh`, dessen Verbindung an einem Blitz endet, mit `$? = 255` und „255: ssh selbst gescheitert“.
:::

⁠**Kurz gesagt:** Die Ausgaben eines Befehls auf dem Server kommen als Ausgaben von `ssh` an und lassen sich lokal umleiten und weiterverarbeiten; der Exit-Status kommt mit, 255 heißt „ssh selbst ist gescheitert“.

### Mit und ohne Terminal: ssh -t

<span class="anker" id="stufe-4-5"></span>

Bei der interaktiven Anmeldung bekam die Shell auf dem Server ein Pseudoterminal, `pts/3` in Abschnitt [3.6](anmelden-mit-einem-schlusselpaar.html#stufe-3-6). Bei einem einzelnen Befehl ist das anders. `tty` gibt den Namen des Terminals aus, an dem es läuft ([Kapitel 8, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-1)):

```console
$ ssh uebung tty
not a tty
```

:::satz Satz 4.5 (Wann ssh ein Terminal anfordert)
<span class="anker" id="satz-4-5"></span>

Ohne Befehl fordert `ssh` auf dem Server ein Pseudoterminal an, sofern es selbst in einem Terminal läuft; mit einem Befehl fordert es keines an. Die Option `-t` erzwingt auch für einen Befehl ein Pseudoterminal, ebenfalls nur, wenn `ssh` selbst in einem Terminal läuft; doppelt, als `-tt`, auch ohne.
:::

Mit `ssh -t uebung tty` meldet `tty` deshalb ein Pseudoterminal wie `/dev/pts/3`, und nach dem Ende schreibt `ssh` zusätzlich `Connection to localhost closed.` Ein Terminal brauchen alle Programme, die den ganzen Bildschirm benutzen oder einzelne Tasten lesen: `ssh -t uebung top` zeigt die Prozessliste des Servers ([Kapitel 8, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-7)), `ssh -t uebung nano notiz.txt` öffnet den Editor dort. Ohne `-t` beschweren sich solche Programme oder verhalten sich seltsam. Abbildung [20](#abb-20) stellt die drei Fälle nebeneinander.

:::abbildung linux/k11tty 20
Drei Aufrufe, drei Antworten von `tty`. (1) `ssh uebung` ohne Befehl: auf dem Server erscheint zwischen `sshd-session` und `-bash` ein Pseudoterminal `pts/3`. (2) `ssh uebung tty`: kein Pseudoterminal, die Ausgabe läuft als gerades Rohr zurück, Antwort `not a tty`. (3) `ssh -t uebung tty`: wieder ein Pseudoterminal, Antwort `/dev/pts/3`. Daneben ein Byte `10` (Zeilenende), das im Rohr unverändert bleibt und im Terminal zu `13 10` wird.
:::

:::hintergrund Warum ssh für Befehle kein Terminal anfordert
Ein Terminal ist keine neutrale Leitung. Sein Treiber im Kernel verändert, was durchläuft: Er macht aus jedem Zeilenende einen Wagenrücklauf mit Zeilenende ([Kapitel 6, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4)), er deutet Strg+C als Abbruch und Strg+D als Ende der Eingabe ([Kapitel 2, Abschnitte 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4) und [5.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5)), und er schickt Eingaben als Echo zurück. Für einen Menschen am Bildschirm ist das richtig. Für Daten wäre es verheerend: Ein Archiv, das `tar` auf dem Server in die Standardausgabe schreibt und das lokal ein zweites `tar` auspackt (Aufgabe [15](#aufg-15)), wäre nach dem Weg durch ein Terminal kaputt, weil jedes Byte mit dem Wert 10 ein Byte 13 davor bekäme. Ohne Terminal reicht `ssh` jedes Byte unverändert durch. Deshalb entscheidet `ssh` nach der Art des Aufrufs: interaktive Anmeldung mit Terminal, Befehl ohne.
:::

⁠**Kurz gesagt:** Für einen einzelnen Befehl gibt es auf dem Server kein Terminal, damit Daten unverändert durchlaufen; Programme, die ein Terminal brauchen, startet man mit `ssh -t`.

:::aufgabe Aufgabe 12 ★★ Wer gewinnt?
<span class="anker" id="aufg-12"></span>

Sage voraus, welchen Port `ssh -G -p 2222 uebung` meldet, obwohl in `~/.ssh/config` `Port 22` steht, und prüfe es mit `ssh -G -p 2222 uebung | grep '^port '`. Begründe mit der Reihenfolge, in der `ssh` seine Einstellungen liest.

:::loesung
`ssh` liest zuerst die Befehlszeile, dann `~/.ssh/config`, dann `/etc/ssh/ssh_config`, und für jede Einstellung gilt der erste Wert. `-p 2222` steht auf der Befehlszeile und gewinnt:

```console
$ ssh -G uebung | grep '^port '
port 22
$ ssh -G -p 2222 uebung | grep '^port '
port 2222
```

So kann man einen Eintrag der Datei für einen einzelnen Aufruf überstimmen, ohne die Datei zu ändern.
:::
:::

:::aufgabe Aufgabe 13 ★★ Wer ersetzt die Variable?
<span class="anker" id="aufg-13"></span>

Sage die Ausgaben voraus und prüfe sie: `ssh uebung echo "[$SSH_CONNECTION]"` und `ssh uebung 'echo "[$SSH_CONNECTION]"'`. Erkläre für beide, welche Shell die Variable ersetzt.

:::loesung
```console
$ ssh uebung echo "[$SSH_CONNECTION]"
[]
$ ssh uebung 'echo "[$SSH_CONNECTION]"'
[127.0.0.1 57522 127.0.0.1 22]
```

Im ersten Aufruf stehen doppelte Anführungszeichen, und die eigene Shell ersetzt die Variable; in ihr ist sie leer, also bekommt `ssh` das Argument `[]`. Auf dem Server gibt `echo` das aus. (Dass die Shell auf dem Server `[]` nicht als Muster deutet, liegt daran, dass eine Klammer ohne Inhalt kein gültiger Klammerausdruck ist.) Im zweiten Aufruf schützen die einfachen Anführungszeichen alles; erst die Shell auf dem Server ersetzt `$SSH_CONNECTION` durch ihren Wert. Die Portnummer des Clients ist bei jeder Verbindung eine andere.
:::
:::

:::aufgabe Aufgabe 14 ★★ Hier zählen oder dort?
<span class="anker" id="aufg-14"></span>

Bestimme die Zahl der Zeilen von `/etc/passwd` auf dem Server auf zwei Wegen: einmal zählt `wc` auf dem Server, einmal auf deinem Rechner. Liefern beide dasselbe? Miss mit `wc -c`, wie viele Bytes in beiden Fällen über die Verbindung kommen, und erkläre, warum man bei großen Dateien auf dem Server filtert.

:::loesung
```console
$ ssh uebung 'wc -l < /etc/passwd'
29
$ ssh uebung 'cat /etc/passwd' | wc -l
29
$ ssh uebung 'cat /etc/passwd' | wc -c
1494
$ ssh uebung 'wc -l < /etc/passwd' | wc -c
3
```

Beide Wege liefern 29 Zeilen. Zählt `wc` auf dem Server, kommen nur drei Bytes über die Verbindung (`29` und das Zeilenende); zählt es auf deinem Rechner, kommt die ganze Datei mit 1 494 Bytes, fast fünfhundertmal so viel. Bei einer Protokolldatei mit vielen Millionen Zeilen ist der Unterschied der zwischen einem Augenblick und einer langen Übertragung. Deshalb filtert man auf dem Server, mit dem ganzen Befehl in einfachen Anführungszeichen, und überträgt nur das Ergebnis. Die Umleitung `< /etc/passwd` steht hier innerhalb der Anführungszeichen; sie öffnet die Datei auf dem Server, und `wc` gibt deshalb keinen Dateinamen aus.
:::
:::

:::aufgabe Aufgabe 15 ★★★ Ein Verzeichnis durch die Verbindung
<span class="anker" id="aufg-15"></span>

Mit `tar` ([Kapitel 10, Abschnitt 9.1](/wissen/informatik/linux-und-kommandozeile/shell-skripte/aufraumen-temporare-dateien-und-trap.html#stufe-9-1)) lässt sich ein ganzes Verzeichnis als ein einziger Datenstrom übertragen: Auf dem Server schreibt `tar -czf -` das Archiv in die Standardausgabe (`-` als Dateiname steht für die Standardausgabe), lokal liest `tar -xzf -` es aus der Standardeingabe. Lege dafür auf dem Server mit Befehlen über `ssh` ein Verzeichnis `linuxk11/server/urlaub` mit zwei kleinen Dateien `tag1.txt` und `tag2.txt` an. Zeige zuerst nur die Liste der Dateien im übertragenen Archiv an und packe es dann in ein lokales Verzeichnis `angekommen` aus. Warum funktioniert das nur, weil `ssh` für Befehle kein Terminal anfordert? Lösche zum Schluss `linuxk11/server` auf dem Server und `angekommen` lokal wieder; der nächste Abschnitt legt `linuxk11/server` neu an.

:::loesung
Zur Vorbereitung legen drei Befehle das Verzeichnis und die beiden Dateien auf dem Server an; die Umleitungen stehen innerhalb der Anführungszeichen und wirken deshalb dort (Abschnitt [4.4](#stufe-4-4)):

```console
$ ssh uebung 'mkdir -p linuxk11/server/urlaub'
$ ssh uebung 'echo Anreise > linuxk11/server/urlaub/tag1.txt'
$ ssh uebung 'echo See > linuxk11/server/urlaub/tag2.txt'
```

Dann die Übertragung:

```console
$ ssh uebung 'tar -czf - -C linuxk11/server urlaub' | tar -tzf -
urlaub/
urlaub/tag1.txt
urlaub/tag2.txt
$ mkdir angekommen
$ ssh uebung 'tar -czf - -C linuxk11/server urlaub' | tar -xzf - -C angekommen
$ ls angekommen/urlaub
tag1.txt  tag2.txt
```

Auf dem Server wechselt `tar` mit `-C` in `linuxk11/server`, packt `urlaub` ein, komprimiert es (`-z`) und schreibt das Archiv in die Standardausgabe (`-f -`). `ssh` reicht die Bytes zu seiner Standardausgabe weiter, und das lokale `tar` liest sie aus der Pipe. Das klappt nur, weil kein Terminal dazwischen liegt: Ein Terminal würde aus jedem Byte mit dem Wert 10 die zwei Bytes 13 und 10 machen (Abschnitt [4.5](#stufe-4-5)), und das komprimierte Archiv wäre danach unbrauchbar. Zum Schluss räumst du auf, damit der nächste Abschnitt mit leeren Verzeichnissen beginnt: `ssh uebung 'rm -r linuxk11/server'` und `rm -r angekommen`.
:::
:::
