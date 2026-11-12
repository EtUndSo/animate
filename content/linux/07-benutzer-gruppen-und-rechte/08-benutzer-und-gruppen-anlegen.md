---
title: Benutzer und Gruppen anlegen
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120800
summary: Mit nur einem Benutzer lässt sich vieles nicht ausprobieren: was die Gruppe einer Datei ausmacht, was ein anderer Mensch in deinem Verzeichnis darf.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Mit nur einem Benutzer lässt sich vieles nicht ausprobieren: was die Gruppe einer Datei ausmacht, was ein anderer Mensch in deinem Verzeichnis darf. Dieser Abschnitt legt deshalb einen zweiten Benutzer und eine Gruppe an, nimmt ihn in Gruppen auf und zeigt, wann solche Änderungen wirken.
:::

:::warnung Ein Testbenutzer auf deinem System
Die Befehle dieses Abschnitts legen ein echtes Konto namens `anna` mit Heimatverzeichnis und eine Gruppe `kochclub` an. Das Konto bekommt kein Passwort: Niemand kann sich mit einem Passwort als `anna` anmelden, du arbeitest als `anna` nur über `sudo`. Nimm Testkonten nie in die Gruppe `sudo` auf. In WSL, einer virtuellen Maschine oder einem Live-System ist das unbedenklich; auf einem Rechner, an dem sich andere über das Netz anmelden können, lege keine Testkonten an. Entfernen kannst du beides jederzeit mit `sudo deluser --remove-home anna` und `sudo delgroup kochclub`.
:::

### Einen Benutzer anlegen: adduser

<span class="anker" id="stufe-7-1"></span>

Ein neues Konto braucht mehrere Dinge zugleich: eine freie Benutzernummer, einen Datensatz in `/etc/passwd`, eine eigene Gruppe, einen Passwort-Prüfwert und ein Heimatverzeichnis. Das alles von Hand in die Dateien zu schreiben, wäre fehleranfällig. Debian und Ubuntu haben dafür ein freundliches Programm, das nachfragt.

:::definition Definition 7.1 (adduser)
<span class="anker" id="satz-7-1"></span>

`sudo adduser name` legt einen Benutzer an: Es wählt die nächste freie Benutzernummer ab 1000, legt eine gleichnamige Gruppe, möglichst mit derselben Nummer, als Hauptgruppe an, schreibt die Datensätze in `/etc/passwd`, `/etc/group` und `/etc/shadow`, legt das Heimatverzeichnis an und kopiert Vorlagen aus `/etc/skel` hinein. Ohne weitere Optionen fragt es danach nach einem Passwort und nach Angaben für das Kommentarfeld. Die Option `--disabled-password` lässt das Passwort weg, `--comment "text"` gibt den Kommentar vor; dann fragt `adduser` nichts.
:::

Abbildung [20](#abb-20) zeigt, wohin `adduser` überall schreibt.

:::abbildung linux/k7adduser 20
In der Mitte der Befehl `sudo adduser` für `anna`, mit den Optionen von oben. Von ihm gehen nacheinander Pfeile aus: zu `/etc/passwd` (neue Zeile `anna:x:1001:1001:Anna Berg:/home/anna:/bin/bash`), zu `/etc/group` (neue Zeile `anna:x:1001:` und `anna` in der Liste von `users`), zu `/etc/shadow` (neue Zeile `anna:!:…`, ohne Passwort) und zu `/home/anna` (neues Verzeichnis, gefüllt aus `/etc/skel`).
:::

```console
$ sudo adduser --disabled-password --comment "Anna Berg" anna
```

Der Befehl meldet nichts, wenn alles klappt. Was entstanden ist, zeigen die beiden Textdateien und `id`:

```console
$ grep anna /etc/passwd /etc/group
/etc/passwd:anna:x:1001:1001:Anna Berg:/home/anna:/bin/bash
/etc/group:users:x:100:anna
/etc/group:anna:x:1001:
$ ls -ld /home/anna
drwxr-x--- 2 anna anna 4096 Nov 10 12:33 /home/anna
$ id anna
uid=1001(anna) gid=1001(anna) groups=1001(anna),100(users)
```

`anna` hat die nächste freie Nummer 1001 und eine eigene Gruppe mit derselben Nummer; im Kommentarfeld steht ihr Name. `adduser` nimmt unter Ubuntu jeden neuen Benutzer außerdem in die Gruppe `users` auf. Das Heimatverzeichnis gehört `anna` und hat `rwxr-x---`; andere Benutzer kommen also nicht hinein. In `/etc/shadow` steht bei `anna` statt eines Prüfwerts nur `!`, und das passt nach Unterabschnitt [1.8](benutzer-und-gruppen.html#stufe-1-8) zu keinem Passwort.

Wer ein Konto für einen Menschen anlegt, lässt die beiden Optionen weg. Dann fragt `adduser` zweimal nach dem Passwort, wobei beim Tippen nichts erscheint, danach nach dem vollen Namen, nach Raum und Telefonnummern, die man mit der Eingabetaste leer lassen kann, und zum Schluss, ob alles stimmt.

⁠**Kurz gesagt:** `sudo adduser name` legt Benutzer, eigene Gruppe, Eintrag in der Schattendatei und Heimatverzeichnis in einem Schritt an.

:::hintergrund adduser und useradd
`adduser` ist ein Programm von Debian und Ubuntu. Es ruft im Hintergrund schlichtere Befehle auf, die es auf fast allen Distributionen gibt: `useradd` legt ein Konto an, `groupadd` eine Gruppe, `usermod` ändert ein Konto. Diese fragen nichts und tun nur, was ihre Optionen sagen; ohne Optionen legt `useradd` zum Beispiel unter vielen Distributionen kein Heimatverzeichnis an. Auf Distributionen ohne `adduser` sind sie der übliche Weg.
:::

### Einen Benutzer in eine Gruppe aufnehmen

<span class="anker" id="stufe-7-2"></span>

`anna` soll in deinem Übungsverzeichnis mitlesen dürfen. Das geht im Moment nicht:

```console
$ sudo -u anna ls ~/linuxk7
ls: cannot open file '/home/student/linuxk7': Permission denied
```

Die Meldung ist der Stand der uutils-Fassung in Ubuntu 26.04; die GNU-Fassung schreibt „cannot access“. Der Grund ist der Pfad aus Unterabschnitt [5.1](wie-der-kernel-rechte-pruft.html#stufe-5-1): `/home/student` hat `rwxr-x---`, und `anna` gehört zur Klasse andere, die nicht hindurchgehen darf. Die Gruppe `student` dürfte es. Die Rechte deines eigenen Heimatverzeichnisses zeigt `ls -ld ~`; hat es `rwxr-xr-x`, kommt `anna` schon jetzt hinein. Also nimmst du `anna` in deine Gruppe auf, so wie man jemandem einen Schlüssel für die Wohnung gibt.

:::definition Definition 7.2 (Benutzer in eine Gruppe aufnehmen)
<span class="anker" id="satz-7-2"></span>

`sudo adduser name gruppe` trägt einen vorhandenen Benutzer in die Mitgliederliste einer vorhandenen Gruppe ein; die Gruppe wird damit eine seiner Zusatzgruppen. Dasselbe leistet `sudo usermod -aG gruppe name` (englisch „append“, anhängen, und „groups“).
:::

```console
$ sudo adduser anna student
$ id anna
uid=1001(anna) gid=1001(anna) groups=1001(anna),100(users),1000(student)
$ grep '^student:' /etc/group
student:x:1000:anna
```

`anna` steht jetzt in der Mitgliederliste der Gruppe `student`, und `id anna` zählt die Gruppe 1000 zu ihren Gruppen.

⁠**Kurz gesagt:** `sudo adduser name gruppe` oder `sudo usermod -aG gruppe name` nimmt einen Benutzer in eine Gruppe auf.

:::warnung usermod -G nie ohne -a
`usermod -G gruppe name` ohne `-a` ersetzt die ganze Liste der Zusatzgruppen: Der Benutzer gehört danach nur noch zu den genannten Gruppen und verliert alle anderen. Trifft das dich selbst und verlierst du so die Gruppe `sudo`, kannst du spätestens ab der nächsten Anmeldung keine Befehle mehr als root ausführen und den Fehler nur noch auf Umwegen beheben. Schreibe deshalb immer `-aG`, oder nimm `adduser name gruppe`, das nur hinzufügt.
:::

Abbildung [21](#abb-21) stellt die beiden Fälle nebeneinander.

:::abbildung linux/k7usermod 21
Zwei Spalten mit der Gruppenliste von `anna` vorher: `users`, `student`. Links `usermod -aG kochclub anna`: `kochclub` kommt unten hinzu, die alten Einträge bleiben. Rechts `usermod -G kochclub anna`: `kochclub` kommt hinzu, `users` und `student` werden rot durchgestrichen und verblassen: Sie gehören nicht mehr dazu. Unter der rechten Spalte erscheint ein Schloss vor `/home/student`.
:::

### Eine Gruppe anlegen: addgroup

<span class="anker" id="stufe-7-3"></span>

Für eine Wohngemeinschaft oder einen Verein, der Dateien teilt, legt man eine eigene Gruppe an, statt jemanden in die persönliche Gruppe eines anderen aufzunehmen.

:::definition Definition 7.3 (addgroup)
<span class="anker" id="satz-7-3"></span>

`sudo addgroup name` legt eine neue Gruppe ohne Mitglieder an und gibt ihr die nächste freie Gruppennummer.
:::

Für einen Kochclub, in dem `anna` Mitglied wird:

```console
$ sudo addgroup kochclub
$ sudo usermod -aG kochclub anna
$ id anna
uid=1001(anna) gid=1001(anna) groups=1001(anna),100(users),1000(student),1002(kochclub)
```

Die Gruppe hat die Nummer 1002 bekommen, und `anna` gehört jetzt zu vier Gruppen.

⁠**Kurz gesagt:** `sudo addgroup name` legt eine Gruppe an; Mitglieder kommen mit `usermod -aG` oder `adduser name gruppe` dazu.

### Neue Gruppen gelten ab der nächsten Anmeldung

<span class="anker" id="stufe-7-4"></span>

Nach Unterabschnitt [1.6](benutzer-und-gruppen.html#stufe-1-6) trägt jeder Prozess eine Kopie seiner Gruppen, die er bei der Anmeldung bekommen hat. Was bedeutet das für eine Gruppe, die erst danach hinzukommt?

:::satz Satz 7.4 (Gruppen und Anmeldung)
<span class="anker" id="satz-7-4"></span>

Eine Änderung in `/etc/group` wirkt für jeden Prozess, der seine Gruppen danach neu bekommt: bei einer neuen Anmeldung und bei `sudo -u`. Prozesse, die schon laufen, auch deine Shell, behalten ihre alte Liste, bis sie enden.
:::

Abbildung [22](#abb-22) zeigt, warum zwei Fragen nach denselben Gruppen verschiedene Antworten geben können.

:::abbildung linux/k7zweiquellen 22
Links die Datei `/etc/group`, in der gerade eine neue Mitgliedschaft hinzukommt (die Zeile leuchtet auf). Rechts die laufende Shell mit ihrem Etikett von der Anmeldung, auf dem die neue Gruppe fehlt. `id` mit Namen (`$USER`) schickt einen Pfeil nach links und findet die neue Gruppe; `id` ohne Namen schickt einen Pfeil nach rechts und findet sie nicht. Unten startet ein neuer Prozess über eine Anmeldung oder `sudo -u`; sein Etikett wird frisch aus `/etc/group` gefüllt und enthält die neue Gruppe.
:::

`sudo -u` stellt die Gruppen beim Start neu zusammen, deshalb sieht ein Befehl als `anna` den Kochclub sofort:

```console
$ sudo -u anna id
uid=1001(anna) gid=1001(anna) groups=1001(anna),100(users),1000(student),1002(kochclub)
```

Was eine neue Anmeldung für deine eigene Shell bedeutet, hängt davon ab, wie du arbeitest. Unter WSL stellt WSL die Gruppen für jedes neu geöffnete Terminal frisch zusammen; dort genügt ein neues Terminalfenster (auf dem Testsystem geprüft). An einem Desktop, also in einer virtuellen Maschine oder im Live-System, genügt das nicht: Ein neues Fenster entsteht aus der laufenden Sitzung und erbt deren alte Liste. Dort meldest du dich ab und wieder an. Überall sofort wirkt `sudo -iu "$USER"`: `-i` aus Unterabschnitt [6.7](kurzzeitig-root-sudo-und-su.html#stufe-6-7) zusammen mit `-u` startet eine Anmelde-Shell als du selbst ([Kapitel 5, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-3)), deren Gruppen frisch zusammengestellt sind; `exit` führt zurück.

::::beispiel Sich selbst in eine Gruppe aufnehmen
Nimm dich vorübergehend selbst in den Kochclub auf. `$USER` ist dein Benutzername aus der Umgebung ([Kapitel 5, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-7)):

```console
$ sudo adduser "$USER" kochclub
$ id "$USER"
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo),1002(kochclub)
$ id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
$ sudo -u "$USER" id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo),1002(kochclub)
$ sudo deluser "$USER" kochclub
$ id "$USER"
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
```

`id "$USER"` liest die Dateien und findet den Kochclub. `id` ohne Namen fragt den Kernel nach den Gruppen der eigenen Shell, und die kennt ihn nicht. Der Prozess, den `sudo -u "$USER"` startet, bekommt seine Gruppen neu und kennt den Kochclub. `sudo deluser "$USER" kochclub` nimmt dich wieder heraus; der Kochclub bleibt `anna` vorbehalten.
::::

⁠**Kurz gesagt:** Neue Gruppen wirken erst in Prozessen, die ihre Gruppen nach der Änderung neu bekommen; für die eigene Shell heißt das: neu anmelden, etwa mit `sudo -iu "$USER"`.

### Die Klassen mit zwei Benutzern

<span class="anker" id="stufe-7-5"></span>

Mit `anna` lassen sich jetzt die Klassen aus Abschnitt [2](die-rechte-einer-datei.html#stufe-2) von der anderen Seite ansehen. `anna` ist Mitglied der Gruppe `student`, für deine Dateien gehört sie also zur Klasse Gruppe.

::::beispiel Ein Aushang, den die Gruppe nicht lesen darf
```console
$ sudo -u anna ls ~/linuxk7
einkauf.txt  fach  tagebuch.txt  weg
$ printf 'Hoffest am Samstag\n' > aushang.txt
$ sudo -u anna cat aushang.txt
Hoffest am Samstag
$ chmod 604 aushang.txt
$ ls -l aushang.txt
-rw----r-- 1 student student 19 Nov 10 12:33 aushang.txt
$ sudo -u anna cat aushang.txt
cat: aushang.txt: Permission denied
$ chmod 644 aushang.txt
```

Jetzt kommt `anna` in dein Übungsverzeichnis, denn die Gruppe `student` darf durch `/home/student` hindurch. Mit 644 liest sie den Aushang über die Gruppenrechte `r--`. Mit 604 hat die Gruppe `---`, alle anderen `r--`: `anna` passt auf die Klasse Gruppe, also zählen nur deren Bits, und sie darf nicht lesen, obwohl alle anderen dürften. Das ist die erste passende Klasse aus Unterabschnitt [5.2](wie-der-kernel-rechte-pruft.html#stufe-5-2), diesmal auf der Ebene der Gruppe.
::::

⁠**Kurz gesagt:** Für einen anderen Benutzer gelten deine Dateien je nach Klasse anders; mit `sudo -u` prüfst du, was er wirklich darf.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-6"></span>

:::aufgabe Aufgabe 16 ★★ Das vergessene -a
<span class="anker" id="aufg-16"></span>

Stell dir vor, statt `sudo usermod -aG kochclub anna` hättest du `sudo usermod -G kochclub anna` getippt. Welche Gruppen hätte `anna` danach? Was könnte sie in deinem Übungsverzeichnis nicht mehr, und warum? Führe den Befehl nicht aus.

:::loesung
Ohne `-a` ersetzt `usermod -G kochclub anna` die ganze Liste der Zusatzgruppen durch `kochclub`. `anna` hätte danach nur noch ihre Hauptgruppe `anna` und die Zusatzgruppe `kochclub`; `users` und `student` wären weg. Ohne die Gruppe `student` fiele sie für `/home/student` in die Klasse andere, die dort `---` hat. Sie käme also nicht mehr durch dein Heimatverzeichnis hindurch und sähe nichts mehr in `~/linuxk7`.
:::
:::

:::aufgabe Aufgabe 17 ★★ Zwei Antworten von id
<span class="anker" id="aufg-17"></span>

Jemand hat sich mit `sudo adduser "$USER" kochclub` in eine Gruppe aufgenommen. `id "$USER"` zeigt den Kochclub, `id` nicht. (a) Woher holt jede der beiden Fassungen ihre Antwort? (b) Was muss die Person tun, damit ihre Shell die Gruppe kennt? (c) Warum reicht es nicht, `/etc/group` erneut zu lesen?

:::loesung
(a) `id "$USER"` bekommt einen Namen und schlägt dessen Gruppen in `/etc/passwd` und `/etc/group` nach. `id` ohne Namen fragt den Kernel nach den Gruppen des eigenen Prozesses, und die hat er als Kopie von der Shell geerbt, die ihre Liste bei der Anmeldung bekommen hat. (b) Die Person braucht eine Shell aus einer neuen Anmeldung. Sofort und überall geht das mit `sudo -iu "$USER"`, einer Anmelde-Shell als sie selbst; `exit` führt zurück. Unter WSL genügt auch ein neues Terminalfenster, auf dem Testsystem kannte es die Gruppe sofort. An einem Desktop muss sie sich ab- und wieder anmelden, denn neue Fenster erben die Gruppen der laufenden Sitzung. (c) Die Gruppenliste eines Prozesses ist kein Inhalt einer Datei, sondern ein Teil des Prozesses im Kernel. Ein gewöhnlicher Prozess kann sie nicht erweitern; das dürfen nur Programme mit den Rechten von root wie die Anmeldung, `su` oder `sudo`, und die tun es nur beim Start einer neuen Sitzung.
:::
:::

:::aufgabe Aufgabe 18 ★★ Ein zweiter Testbenutzer
<span class="anker" id="aufg-18"></span>

Lege einen Benutzer `ben` ohne Passwort an: `sudo adduser --disabled-password --comment "Ben Test" ben`. (a) Welche Gruppen hat `ben`? (b) Darf `ben` den Inhalt von `/home/student/linuxk7` sehen? Prüfe mit `sudo -u ben` und begründe mit den Rechten von `/home/student`. (c) Entferne `ben` wieder mit `sudo deluser --remove-home ben`.

:::loesung
```console
$ sudo adduser --disabled-password --comment "Ben Test" ben
$ id ben
uid=1001(ben) gid=1001(ben) groups=1001(ben),100(users)
$ sudo -u ben ls ~/linuxk7
ls: cannot open file '/home/student/linuxk7': Permission denied
$ sudo -u ben ls -ld ~
drwxr-x--- 15 student student 4096 Nov 10 12:52 /home/student
$ sudo deluser --remove-home ben
$ id ben
id: 'ben': no such user
```

(a) `ben` hat seine eigene Gruppe `ben` und, wie jeder neue Benutzer unter Ubuntu, `users`. (b) Nein. `/home/student` hat `rwxr-x---`; `ben` ist weder Besitzer noch in der Gruppe `student`, für ihn gilt `---`. Ohne `x` kommt er nicht hindurch, also auch nicht an `linuxk7`. Die Angaben zu `/home/student` selbst darf er sehen, denn dafür braucht er nur das Ausführungsrecht an `/home`. (c) Nach `deluser` kennt das System `ben` nicht mehr. Weil `ben` kein Passwort hatte, konnte sich in der Zwischenzeit niemand mit einem Passwort als `ben` anmelden.
:::
:::
