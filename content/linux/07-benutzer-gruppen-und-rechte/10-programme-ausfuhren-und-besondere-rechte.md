---
title: Programme ausführen und besondere Rechte
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6121000
summary: Das dritte Recht einer Datei, das Ausführen, hatte bisher wenig zu tun.
tags: reale Benutzernummer, effektive Benutzernummer, SUID-Bit, SGID-Bit, Sticky-Bit
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Das dritte Recht einer Datei, das Ausführen, hatte bisher wenig zu tun. Dieser Abschnitt zeigt, wie es Programme startbar macht, und drei besondere Rechte, mit denen ein Programm mehr darf als der, der es startet, mit denen ein Verzeichnis seine Gruppe weitergibt und mit denen ein gemeinsames Verzeichnis die Dateien seiner Benutzer voreinander schützt.
:::

### Das Ausführungsrecht für Programme

<span class="anker" id="stufe-9-1"></span>

[Kapitel 5, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-4) hat ein kopiertes Programm mit `./` gestartet und dabei nur bemerkt, dass `cp` die Angabe übernimmt, die Datei dürfe gestartet werden. Diese Angabe ist das x-Bit.

:::definition Definition 9.1 (Ausführungsrecht für Programme)
<span class="anker" id="satz-9-1"></span>

Ein Prozess darf eine Datei nur dann als Programm starten, wenn sie für seine Klasse das Recht `x` hat. Fehlt es, meldet die Shell „Permission denied“ und den Exit-Status 126 ([Kapitel 4, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)). `chmod a+x datei` gibt das Recht allen Klassen, `chmod a-x datei` nimmt es allen.
:::

Oft liest man kürzer `chmod +x datei`. Ohne den Teil „wer“ gilt die Angabe für alle Klassen, aber nur für die Bits, die die umask nicht sperrt (Unterabschnitt [8.4](besitz-und-voreinstellungen-chown-chgrp-und-umask.html#stufe-8-4)). Bei der umask 022 bekommen so alle drei Klassen das x-Bit, bei der umask 077 nur der Besitzer; `chmod +w` gäbe bei 022 nur dem Besitzer das Schreibrecht. Wer sicher sein will, was geschieht, schreibt den Teil „wer“ aus. Für die Versuche dieses Abschnitts brauchst du eine eigene Kopie eines kleinen Programms, das Benutzernummern anzeigt. Auf Ubuntu 26.04 ist `id` Teil des Multicall-Programms von uutils, und eine umbenannte Kopie davon startet nicht ([Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2), und [Kapitel 5, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-4)); deshalb kopierst du die GNU-Fassung `gnuid`. Auf anderen Systemen heißt sie einfach `/usr/bin/id`.

```console
$ cp /usr/bin/gnuid meinid
$ ls -l meinid
-rwxr-xr-x 1 student student 43616 Nov 10 12:34 meinid
$ ./meinid
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
$ chmod -x meinid
$ ./meinid
bash: ./meinid: Permission denied
$ echo $?
126
$ sudo ./meinid
sudo: cannot execute '/home/student/linuxk7/meinid': Permission denied (os error 13)
$ chmod +x meinid
```

Die Kopie hat das x-Bit vom Original übernommen und läuft. Ohne x-Bit verweigert der Kernel den Start, und zwar auch root: Das ist die Ausnahme im ersten Schritt der Rechteprüfung aus Unterabschnitt [5.2](wie-der-kernel-rechte-pruft.html#stufe-5-2).

⁠**Kurz gesagt:** Starten verlangt das x-Bit für die eigene Klasse, sogar von root; `chmod +x` setzt es.

### Reale und effektive Benutzernummer

<span class="anker" id="stufe-9-2"></span>

Bisher trug jeder Prozess genau eine Benutzernummer. Für die besonderen Rechte dieses Abschnitts muss man genauer hinsehen: Ein Prozess trägt zwei, die sich unterscheiden können. Das ist wie bei einer Vertretung im Büro, die mit ihrem eigenen Namen unterschreibt, aber mit der Vollmacht der Chefin handelt.

:::definition Definition 9.2 (reale und effektive Benutzernummer)
<span class="anker" id="satz-9-2"></span>

Jeder Prozess hat eine __reale Benutzernummer__; sie gibt an, wer ihn gestartet hat. Daneben hat er eine __effektive Benutzernummer__, mit der der Kernel die Rechte prüft. Für die Gruppen gibt es ebenso eine reale und eine effektive Gruppennummer. Normalerweise sind reale und effektive Nummer gleich.
:::

Die Rechteprüfung aus Unterabschnitt [5.2](wie-der-kernel-rechte-pruft.html#stufe-5-2) benutzt also genau genommen die effektive Benutzernummer und die effektive Gruppennummer. Linux führt dafür noch eine eigene Nummer für Dateizugriffe, die der effektiven automatisch folgt; im Alltag merkt man den Unterschied nicht. `id` zeigt die effektive Nummer nur, wenn sie von der realen abweicht; in allen Ausgaben bisher war das nie der Fall.

⁠**Kurz gesagt:** Ein Prozess hat eine reale Benutzernummer (wer ihn startete) und eine effektive (mit der geprüft wird); meist sind sie gleich.

### Das SUID-Bit

<span class="anker" id="stufe-9-3"></span>

Manche Aufgaben muss jeder Benutzer erledigen können, obwohl sie Dateien berühren, an die er nicht herankommen darf. Das bekannteste Beispiel ist das eigene Passwort: Es steht in `/etc/shadow`, die nur root schreiben darf. Unix löst das mit einem Bit, das einem Programm die Rechte seines Besitzers leiht.

:::definition Definition 9.3 (SUID-Bit)
<span class="anker" id="satz-9-3"></span>

Das __SUID-Bit__ (englisch „set user ID“) ist ein zusätzliches Recht einer Programmdatei. Startet ein Prozess ein Programm mit gesetztem SUID-Bit, bekommt der neue Prozess als effektive Benutzernummer die des Besitzers der Programmdatei; die reale Benutzernummer bleibt die des Aufrufers. `chmod u+s datei` setzt das Bit, `chmod u-s` nimmt es weg. `ls -l` zeigt es als `s` an der Stelle des x-Bits des Besitzers. In der Oktalschreibweise hat es den Wert 4000: eine 4 an einer vierten Stelle vor den drei bekannten Ziffern.
:::

Abbildung [25](#abb-25) zeigt, was beim Start eines SUID-Programms mit den beiden Nummern geschieht.

:::abbildung linux/k7suid 25
Links die Shell von `student` mit dem Etikett „real 1000, effektiv 1000“. Sie startet die Programmdatei `meinid` (Besitzer root, Rechte `rwsr-xr-x`, das `s` leuchtet). Rechts entsteht der neue Prozess; sein Etikett zeigt „real 1000“ (vom Aufrufer kopiert) und „effektiv 0“, wobei die 0 sichtbar vom Besitzerfeld der Datei herüberwandert. Darunter ein zweiter Start desselben Programms ohne `s`: „real 1000, effektiv 1000“.
:::

Probiere es mit deiner Kopie von `id`. Zuerst muss sie root gehören, dann bekommt sie das SUID-Bit:

```console
$ sudo chown root meinid
$ sudo chmod u+s meinid
$ ls -l meinid
-rwsr-xr-x 1 root student 43616 Nov 10 12:34 meinid
$ ./meinid
uid=1000(student) gid=1000(student) euid=0(root) groups=1000(student),27(sudo)
```

Die reale Benutzernummer ist weiterhin 1000, aber `euid=0` zeigt die effektive: Dieser Prozess hätte alle Rechte von root, obwohl `student` ihn gestartet hat. Die Reihenfolge der beiden Befehle mit `sudo` ist kein Zufall. Ein Wechsel des Besitzers löscht das SUID-Bit, damit aus einem SUID-Programm nicht unbemerkt ein Programm mit den Rechten seines neuen Besitzers wird:

```console
$ sudo chown student meinid
$ ls -l meinid
-rwxr-xr-x 1 student student 43616 Nov 10 12:34 meinid
```

⁠**Kurz gesagt:** Das SUID-Bit leiht einem Prozess die effektive Benutzernummer des Besitzers der Programmdatei; die reale bleibt die des Aufrufers.

:::warnung SUID nur zum Ausprobieren und danach löschen
Ein Programm, das SUID-root ist, kann jeder Benutzer mit allen Rechten von root laufen lassen. Bei `id`, das nur Zahlen ausgibt, ist das harmlos. Gib das SUID-Bit nie einem Programm, das Dateien schreibt, andere Programme startet oder eine Shell öffnet: Jeder auf dem Rechner würde damit root. Lösche deine Kopie, sobald du die folgenden Versuche gemacht hast.
:::

:::hintergrund Eine Idee mit Patent
Das SUID-Bit hat Dennis Ritchie erfunden, einer der beiden Schöpfer von Unix. Sein Arbeitgeber, die Bell Laboratories, meldete die Idee 1973 als Patent an, es wurde 1979 erteilt. Die Beschreibung im Patent fasst den Gedanken so zusammen: Ist das Bit gesetzt, wird die Kennung des aktuellen Benutzers durch die des Besitzers der Programmdatei ersetzt, aber nur vorübergehend; endet das Programm, gilt wieder die richtige Kennung. Bemerkenswert daran ist, dass ein einziges Bit einen Mechanismus schafft, mit dem man Rechte genau an ein Programm statt an einen Menschen binden kann: Wer das Programm benutzt, bekommt die Rechte, aber nur für das, was das Programm tut.
:::

### Wozu SUID: passwd und sudo

<span class="anker" id="stufe-9-4"></span>

Jetzt lässt sich erklären, wie ein gewöhnlicher Benutzer sein Passwort ändert und wie `sudo` überhaupt root wird. Beides sind Programme mit SUID-Bit.

```console
$ ls -l /usr/bin/passwd /etc/shadow
-rw-r----- 1 root shadow   757 Nov 10 12:33 /etc/shadow
-rwsr-xr-x 1 root root   93640 Feb  2  2026 /usr/bin/passwd
```

`passwd` gehört root und hat das SUID-Bit. Wer es startet, bekommt einen Prozess mit der effektiven Benutzernummer 0, der `/etc/shadow` schreiben darf. Dass trotzdem niemand das Passwort eines anderen ändert, stellt das Programm selbst sicher: Es fragt die reale Benutzernummer ab, ändert nur die Zeile dieses Benutzers und verlangt vorher dessen bisheriges Passwort. Das SUID-Bit gibt die Macht, das Programm setzt ihr die Grenzen.

`sudo` funktioniert genauso. `/usr/bin/sudo` ist auf Ubuntu ein symbolischer Link; `ls -lL` zeigt die Datei, auf die er zeigt (`-L` folgt dem Link):

```console
$ ls -lL /usr/bin/sudo
-rwsr-xr-x 1 root root 1082656 Mar 11  2026 /usr/bin/sudo
```

`sudo` startet also schon mit der effektiven Benutzernummer 0. Bevor es den gewünschten Befehl startet, prüft es `/etc/sudoers` und das Passwort, und erst wenn alles stimmt, setzt es auch die reale Nummer auf 0 und startet den Befehl.

Welche Programme auf einem System das SUID-Bit tragen, findet `find` mit dem Test `-perm`. `-perm -4000` bedeutet: Das Bit mit dem Wert 4000, das SUID-Bit, muss gesetzt sein, die übrigen Rechte sind egal. Fehlermeldungen für Verzeichnisse, in die `student` nicht hineindarf, verwirft `2>/dev/null`:

```console
$ find /usr -perm -4000 -type f 2>/dev/null
/usr/bin/umount
/usr/bin/su
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/mount
/usr/bin/fusermount3
/usr/bin/sudo.ws
/usr/bin/gpasswd
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/landscape/apt-update
/usr/lib/cargo/bin/su
/usr/lib/cargo/bin/sudo
```

Auf dem Testsystem sind es vierzehn Programme, jedes für eine Aufgabe, bei der gewöhnliche Benutzer eine Systemdatei berühren müssen: `su` und `sudo`, `passwd`, `chsh` und `chfn` (Shell und Kommentarfeld in `/etc/passwd` ändern), `gpasswd` (Gruppenverwaltung), `mount` und `umount` (Datenträger einhängen). Die Liste ist kurz, und das ist Absicht.

Deine Kopie von `id` brauchst du nicht mehr. Sie gehört dir wieder, und das Verzeichnis ist deins:

```console
$ rm -f meinid
```

⁠**Kurz gesagt:** `passwd` und `sudo` sind SUID-root; sie bekommen so die Macht von root und begrenzen sie selbst mit Hilfe der realen Benutzernummer.

:::hintergrund Warum es so wenige SUID-Programme gibt
Ein SUID-root-Programm ist eine Tür von gewöhnlichen Rechten zu allen Rechten, und jeder Benutzer darf an ihr klopfen. Der Aufrufer bestimmt dabei viel mit: die Argumente, die Umgebung, das Arbeitsverzeichnis, die offenen Deskriptoren. Enthält das Programm einen einzigen Fehler im Umgang damit, kann ein Angreifer es dazu bringen, mehr zu tun als vorgesehen, und wird so root. Die Geschichte von Unix kennt viele solche Fehler. Deshalb halten Distributionen die Liste der SUID-Programme so kurz wie möglich und schreiben diese Programme besonders sorgfältig. Wie Angreifer nach solchen Türen suchen, ist ein Thema der Reihe Cybersecurity.
:::

### Kein SUID für Skripte

<span class="anker" id="stufe-9-5"></span>

Ein Skript ist eine Textdatei mit Befehlen für eine Shell. Beginnt seine erste Zeile mit `#!`, nennt sie das Programm, das die Datei ausführen soll; der Kernel startet beim Aufruf mit `./` dieses Programm und gibt ihm den Namen der Datei. Das Programm öffnet die Datei dann selbst und liest die Befehle.

:::satz Satz 9.4 (SUID bei Skripten)
<span class="anker" id="satz-9-4"></span>

Linux beachtet das SUID-Bit und das SGID-Bit bei Skripten nicht. Ein Skript läuft immer mit den Nummern dessen, der es startet.
:::

Das folgende Skript besteht aus zwei Zeilen: `#!/bin/bash -p` lässt es von bash ausführen, und `id` zeigt die Nummern. Die Option `-p` verbietet bash, eine geliehene effektive Benutzernummer von sich aus abzulegen; ohne sie täte bash genau das, und der Versuch zeigte nichts über den Kernel. `printf` schreibt die beiden Zeilen in die Datei:

```console
$ printf '#!/bin/bash -p\nid\n' > zeigeid.sh
$ chmod 755 zeigeid.sh
$ ./zeigeid.sh
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
$ sudo chown root zeigeid.sh
$ sudo chmod u+s zeigeid.sh
$ ls -l zeigeid.sh
-rwsr-xr-x 1 root student 18 Nov 10 12:34 zeigeid.sh
$ ./zeigeid.sh
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
$ rm -f zeigeid.sh
```

Das Skript gehört root und hat das `s`, und trotzdem fehlt in der Ausgabe ein `euid=0`. Der Kernel hat das Bit beim Start übergangen.

⁠**Kurz gesagt:** Bei Skripten ignoriert Linux das SUID-Bit; nur echte Programmdateien können es nutzen.

:::hintergrund Warum Skripte kein SUID bekommen
Beim Start eines Skripts geschehen zwei Dinge nacheinander. Zuerst öffnet der Kernel die Datei, liest die erste Zeile, prüft die Rechte und startet das genannte Programm, etwa bash, mit dem Namen der Datei als Argument. Dann öffnet bash die Datei ein zweites Mal über diesen Namen und liest die Befehle. Zwischen den beiden Schritten liegt ein kurzer Moment. Würde der Kernel das SUID-Bit beachten, könnte ein Angreifer in diesem Moment den Namen auf ein eigenes Skript umbiegen, etwa über einen Link in einem Verzeichnis, das er beschreiben darf. bash liefe dann mit den geliehenen Rechten und läse die Befehle des Angreifers. Das ist das Muster „Prüfen und Handeln zu verschiedenen Zeitpunkten“ aus [Cybersecurity, Kapitel 1, Abschnitt 5.6](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-6). Einige Unix-Systeme lösen das, indem sie dem Programm statt des Namens einen schon geöffneten Deskriptor übergeben. Linux geht den einfacheren Weg und beachtet das Bit bei Skripten überhaupt nicht; eine Begründung dafür nennt die Linux-Dokumentation nicht, die Gefahr ist aber seit Jahrzehnten bekannt.
:::

### Das SGID-Bit

<span class="anker" id="stufe-9-6"></span>

Was das SUID-Bit für den Besitzer leistet, leistet ein zweites Bit für die Gruppe. Bei Verzeichnissen hat es außerdem eine eigene, im Alltag nützlichere Bedeutung.

:::definition Definition 9.5 (SGID-Bit)
<span class="anker" id="satz-9-5"></span>

Das __SGID-Bit__ (englisch „set group ID“) wirkt je nach Art der Datei verschieden.

<ul>

<li>

Bei einer Programmdatei bekommt der neue Prozess als effektive Gruppennummer die Gruppe der Programmdatei.

</li>

<li>

Bei einem Verzeichnis bekommen neue Einträge darin die Gruppe des Verzeichnisses statt der Hauptgruppe des Prozesses, der sie anlegt; neue Unterverzeichnisse erben zusätzlich das SGID-Bit selbst.

</li>

</ul>

`chmod g+s` setzt das Bit; `ls -l` zeigt es als `s` an der Stelle des x-Bits der Gruppe. Oktal hat es den Wert 2000.
:::

Zwei Programme des Testsystems benutzen die erste Bedeutung:

```console
$ ls -l /usr/bin/chage /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 85256 Feb  2  2026 /usr/bin/chage
-rwxr-sr-x 1 root shadow 31112 Jul 16 15:34 /usr/sbin/unix_chkpwd
```

Beide gehören der Gruppe `shadow` und laufen mit ihr als effektiver Gruppe. Damit dürfen sie `/etc/shadow` lesen, das für die Gruppe `shadow` `r--` hat, aber nicht schreiben. `unix_chkpwd` prüft ein Passwort, etwa für eine Bildschirmsperre, und braucht dafür genau das Lesen. Das ist bescheidener als SUID-root: Bricht jemand in dieses Programm ein, bekommt er nur die Rechte der Gruppe `shadow`.

Die zweite Bedeutung ist eine Ausnahme von der Regel aus Unterabschnitt [2.1](die-rechte-einer-datei.html#stufe-2-1), nach der eine neue Datei der Hauptgruppe ihres Erzeugers gehört. Abbildung [26](#abb-26) vergleicht zwei Verzeichnisse.

:::abbildung linux/k7sgid 26
Zwei Verzeichnisse nebeneinander, beide mit Gruppe `student`: links `ohne` (`rwxrwxr-x`), rechts `gemeinsam` (`rwxrwsr-x`, das `s` leuchtet). `anna` legt in beiden eine Datei an. Links trägt die neue Datei `anna anna`: Die Gruppe kommt von `anna`. Rechts trägt sie `anna student`: Ein Pfeil zeigt, wie die Gruppe vom Verzeichnis auf die Datei übergeht.
:::

```console
$ mkdir ohne gemeinsam
$ chmod 775 ohne
$ chmod 2775 gemeinsam
$ ls -ld ohne gemeinsam
drwxrwsr-x 2 student student 4096 Nov 10 12:34 gemeinsam
drwxrwxr-x 2 student student 4096 Nov 10 12:34 ohne
$ sudo -u anna touch ohne/von_anna.txt gemeinsam/von_anna.txt
$ ls -l ohne gemeinsam
gemeinsam:
total 0
-rw-r--r-- 1 anna student 0 Nov 10 12:34 von_anna.txt

ohne:
total 0
-rw-r--r-- 1 anna anna 0 Nov 10 12:34 von_anna.txt
```

Die vordere 2 in 2775 ist das SGID-Bit mit dem Wert 2000, die übrigen Ziffern sind die bekannten 775. `anna` darf in beiden Verzeichnissen anlegen, weil sie zur Gruppe `student` gehört und diese `rwx` hat. Im gewöhnlichen Verzeichnis bekommt ihre Datei ihre eigene Hauptgruppe `anna`, im Verzeichnis mit SGID-Bit die Gruppe `student`. So gehören in einem gemeinsamen Verzeichnis alle Dateien automatisch der gemeinsamen Gruppe, ganz gleich, wer sie anlegt.

⁠**Kurz gesagt:** Das SGID-Bit leiht einem Programm die Gruppe der Programmdatei; an einem Verzeichnis gibt es dessen Gruppe an alle neuen Einträge weiter.

### Das Sticky-Bit

<span class="anker" id="stufe-9-7"></span>

Nach dem Satz aus Unterabschnitt [4.4](rechte-bei-verzeichnissen.html#stufe-4-4) darf in einem Verzeichnis jeder, der es schreiben darf, jeden Namen darin streichen. Für ein Verzeichnis wie `/tmp`, in das alle Benutzer schreiben sollen, wäre das fatal: Jeder könnte die Dateien aller anderen löschen. Ein drittes Bit schließt diese Lücke.

:::definition Definition 9.6 (Sticky-Bit)
<span class="anker" id="satz-9-6"></span>

Ist bei einem Verzeichnis das __Sticky-Bit__ gesetzt, darf einen Eintrag darin nur löschen oder umbenennen, wem der Eintrag gehört, wem das Verzeichnis gehört, oder root. Das Schreib- und das Ausführungsrecht am Verzeichnis braucht man weiterhin. `chmod +t` setzt das Bit; `ls -l` zeigt es als `t` an der Stelle des x-Bits der anderen. Oktal hat es den Wert 1000.
:::

Das Sticky-Bit ist damit die Ausnahme vom Satz zum Löschen, auf die das Wort „gewöhnlich“ in Unterabschnitt [4.4](rechte-bei-verzeichnissen.html#stufe-4-4) hingewiesen hat. `/tmp` trägt es:

```console
$ ls -ld /tmp
drwxrwxrwt 7 root root 140 Nov 10 12:33 /tmp
$ mkdir ablage
$ chmod 775 ablage
$ touch ablage/von_student.txt
$ sudo -u anna rm -f ablage/von_student.txt
$ ls ablage
```

Ohne Sticky-Bit hat `anna` die Datei von `student` gelöscht: Sie gehört zur Gruppe `student`, und die darf die Tabelle von `ablage` schreiben. Mit Sticky-Bit sieht es anders aus. Abbildung [27](#abb-27) fasst zusammen, wer dann was darf.

:::abbildung linux/k7sticky 27
Das Verzeichnis `ablage` (`rwxrwxr-t`, Besitzer `student`) als Tabelle mit zwei Einträgen: `von_student.txt` (Besitzer `student`) und `von_anna.txt` (Besitzer `anna`). `anna` versucht, beide Namen zu streichen: bei ihrer eigenen Datei gelingt es (grün), bei der von `student` nicht (rot). Dann versucht `student`, die Datei von `anna` zu streichen: Es gelingt, weil ihm das Verzeichnis gehört (grün, mit dem Hinweis „Besitzer des Verzeichnisses“).
:::

```console
$ chmod +t ablage
$ ls -ld ablage
drwxrwxr-t 2 student student 4096 Nov 10 12:34 ablage
$ touch ablage/von_student.txt
$ sudo -u anna rm -f ablage/von_student.txt
rm: cannot remove 'ablage/von_student.txt': Operation not permitted
$ sudo -u anna touch ablage/von_anna.txt
$ ls -l ablage
total 0
-rw-r--r-- 1 anna    anna    0 Nov 10 12:34 von_anna.txt
-rw-r--r-- 1 student student 0 Nov 10 12:34 von_student.txt
$ rm -f ablage/von_anna.txt
$ ls ablage
von_student.txt
```

Jetzt scheitert `anna` an der Datei von `student`, darf aber eigene Dateien anlegen. `student` durfte die Datei von `anna` löschen, weil ihm das Verzeichnis gehört. Genau so schützt `/tmp` die Dateien aller Benutzer voreinander, obwohl alle hineinschreiben dürfen.

⁠**Kurz gesagt:** In einem Verzeichnis mit Sticky-Bit löscht jeder nur, was ihm gehört, außer dem Besitzer des Verzeichnisses und root.

:::hintergrund Woher der Name kommt
„Sticky“ heißt klebrig. In frühen Unix-Systemen markierte das Bit Programmdateien, die nach dem Ende des Programms im Speicher kleben bleiben sollten, damit der nächste Start schneller ging. Mit besseren Speicherverwaltungen wurde das überflüssig, und Linux beachtet das Bit bei gewöhnlichen Dateien gar nicht mehr. Die Bedeutung für Verzeichnisse kam später hinzu und ist die einzige, die heute zählt.
:::

### Die besonderen Rechte als vierte Ziffer

<span class="anker" id="stufe-9-8"></span>

SUID, SGID und Sticky sind drei weitere Bits neben den neun bekannten. Drei Bits passen nach Unterabschnitt [3.3](rechte-andern-chmod.html#stufe-3-3) in eine Oktalziffer, und genau so werden sie geschrieben.

:::definition Definition 9.7 (vierte Oktalziffer)
<span class="anker" id="satz-9-7"></span>

Vor den drei Ziffern der Oktalschreibweise darf eine vierte stehen. Sie ist die Summe aus 4 für das SUID-Bit, 2 für das SGID-Bit und 1 für das Sticky-Bit. In `ls -l` erscheinen die Bits an den Stellen der x-Bits: `s` beim Besitzer, `s` bei der Gruppe, `t` bei den anderen. Ist das darunterliegende x-Bit nicht gesetzt, steht dort ein großes `S` oder `T`.
:::

Jetzt erklärt sich auch die führende Null bei `umask` aus Unterabschnitt [8.4](besitz-und-voreinstellungen-chown-chgrp-und-umask.html#stufe-8-4): Sie ist diese vierte Ziffer.

```console
$ stat -c '%a %A %n' /usr/bin/passwd gemeinsam ablage /tmp
4755 -rwsr-xr-x /usr/bin/passwd
2775 drwxrwsr-x gemeinsam
1775 drwxrwxr-t ablage
1777 drwxrwxrwt /tmp
```

::::beispiel 2775 zerlegt
Abbildung [28](#abb-28) zerlegt die Zahl des gemeinsamen Verzeichnisses. Die vordere 2 ist das SGID-Bit, die übrigen drei Ziffern sind `rwxrwxr-x`. Weil das x-Bit der Gruppe gesetzt ist, steht an seiner Stelle ein kleines `s`.

:::abbildung linux/k7vierziffern 28
Rechenbild: die Zahl 2775 in vier Kästchen. Das erste Kästchen 2 zerfällt in die Bits `0 1 0` mit den Beschriftungen SUID, SGID, Sticky; nur SGID leuchtet. Die übrigen drei Ziffern werden zu `rwx rwx r-x`. Dann wandert das SGID-Bit auf das x der Gruppe und macht daraus ein `s`: `rwxrwsr-x`. Darunter dieselbe Zerlegung für 4755 → `rwsr-xr-x` und 1777 → `rwxrwxrwt`.
:::

Ein großes `S` sieht man, wenn das Bit ohne x gesetzt ist:

```console
$ chmod u+s einkauf.txt
$ ls -l einkauf.txt
-rwSr--r-- 1 student student 25 Nov 10 12:32 einkauf.txt
$ chmod u-s einkauf.txt
```

Bei einer Datei ohne Ausführungsrecht ist ein SUID-Bit sinnlos; das große `S` macht auf diesen Widerspruch aufmerksam.
::::

⁠**Kurz gesagt:** Die vierte, vordere Oktalziffer enthält SUID (4), SGID (2) und Sticky (1); `ls -l` zeigt sie als `s`, `s`, `t` an den Stellen der x-Bits.

### Aufräumen: Benutzer und Gruppe entfernen

<span class="anker" id="stufe-9-9"></span>

Zum Schluss entfernst du den Testbenutzer und den Kochclub wieder. Dabei zeigt sich noch einmal, dass der Kernel nur Nummern kennt.

:::definition Definition 9.8 (deluser, delgroup)
<span class="anker" id="satz-9-8"></span>

`sudo deluser --remove-home name` entfernt einen Benutzer aus `/etc/passwd`, `/etc/shadow` und allen Mitgliederlisten, löscht seine eigene Gruppe, wenn sie danach leer ist, und löscht sein Heimatverzeichnis. `sudo delgroup name` entfernt eine Gruppe. Dateien des Benutzers außerhalb seines Heimatverzeichnisses bleiben liegen.
:::

```console
$ sudo deluser --remove-home anna
$ sudo delgroup kochclub
$ ls -l gemeinsam rezept.txt
-rw-r--r-- 1 student 1002 32 Nov 10 12:33 rezept.txt

gemeinsam:
total 0
-rw-r--r-- 1 1001 student 0 Nov 10 12:34 von_anna.txt
$ find . -nouser -o -nogroup
./gemeinsam/von_anna.txt
./rezept.txt
./ohne/von_anna.txt
```

Die Datei, die `anna` in `gemeinsam` angelegt hat, gehört jetzt der bloßen Nummer 1001, das Rezept der Gruppe 1002. Der Satz aus Unterabschnitt [8.2](besitz-und-voreinstellungen-chown-chgrp-und-umask.html#stufe-8-2) zeigt seine Kehrseite: Bekäme ein neues Konto die Nummer 1001, gehörten ihm diese Dateien. Die Tests `-nouser` und `-nogroup` von `find` finden solche verwaisten Dateien; `-o` verknüpft sie mit „oder“. Räume sie auf:

```console
$ rm -f ohne/von_anna.txt gemeinsam/von_anna.txt
$ chgrp student rezept.txt
$ find . -nouser -o -nogroup
```

Löschen durftest du die Dateien von `anna`, weil die Verzeichnisse dir gehören, und das Rezept darfst du deiner eigenen Gruppe geben. Danach findet `find` nichts mehr. Hast du für Aufgabe [18](benutzer-und-gruppen-anlegen.html#aufg-18) den Benutzer `ben` angelegt und noch nicht entfernt, entferne ihn ebenso mit `sudo deluser --remove-home ben`. Außerhalb von `~/linuxk7` bleibt dann nichts mehr von den Versuchen dieses Kapitels übrig, außer den Zeilen im Protokoll.

⁠**Kurz gesagt:** `deluser --remove-home` und `delgroup` entfernen Konten; Dateien außerhalb des Heimatverzeichnisses bleiben mit bloßen Nummern zurück und lassen sich mit `find -nouser -o -nogroup` finden.

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; die Module „Untangling Users“ und „Perceiving Permissions“ passen zu diesem Kapitel. Sie laufen auf einem fremden Rechner, nicht auf deinem eigenen.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-10"></span>

:::aufgabe Aufgabe 22 ★★ Besondere Rechte lesen
<span class="anker" id="aufg-22"></span>

Was bedeuten diese Zeilen, und wie lauten die vierstelligen Oktalzahlen? `-rwsr-xr-x 1 root root … /usr/bin/passwd` `-rwxr-sr-x 1 root shadow … /usr/bin/chage` `drwxrwxrwt 7 root root … /tmp` `drwxrws--- 2 anna kochclub … rezepte` `-rwSr--r-- 1 student student … einkauf.txt`

:::loesung
<ul>

<li>

`-rwsr-xr-x root root /usr/bin/passwd`: SUID-Bit, alle dürfen das Programm starten, und es läuft dann mit der effektiven Benutzernummer 0; oktal 4755.

</li>

<li>

`-rwxr-sr-x root shadow /usr/bin/chage`: SGID-Bit, das Programm läuft mit der effektiven Gruppe `shadow` und darf deshalb `/etc/shadow` lesen; oktal 2755.

</li>

<li>

`drwxrwxrwt root root /tmp`: Alle dürfen anlegen, das Sticky-Bit erlaubt aber nur das Löschen eigener Einträge; oktal 1777.

</li>

<li>

`drwxrws--- anna kochclub rezepte`: `anna` und der Kochclub dürfen alles, andere nichts; das SGID-Bit gibt neuen Dateien die Gruppe `kochclub`; oktal 2770.

</li>

<li>

`-rwSr--r-- student student einkauf.txt`: SUID-Bit ohne Ausführungsrecht, also wirkungslos; oktal 4644. Das große `S` zeigt den Widerspruch.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 23 ★★★ Die Programme mit geliehenen Rechten
<span class="anker" id="aufg-23"></span>

(a) Suche auf deinem System alle Programme unter `/usr` mit SUID-Bit und alle mit SGID-Bit. (b) `chsh` ändert die Shell eines Benutzers, `chfn` sein Kommentarfeld. In welche Datei müssen sie schreiben, und warum brauchen sie deshalb das SUID-Bit? (c) Woran muss ein Programm wie `chsh` selbst denken, damit niemand damit die Shell eines anderen Benutzers ändert?

:::loesung
(a) Die Programme mit SUID-Bit unter `/usr` zeigt Unterabschnitt [9.4](#stufe-9-4): auf dem Testsystem vierzehn. Für das SGID-Bit ersetzt man 4000 durch 2000:

```console
$ find /usr -perm -2000 -type f 2>/dev/null
/usr/bin/crontab
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/expiry
/usr/sbin/unix_chkpwd
/usr/sbin/pam_extrausers_chkpwd
```

(b) Beide ändern Felder in `/etc/passwd`:

```console
$ ls -l /usr/bin/chsh /usr/bin/chfn /etc/passwd
-rw-r--r-- 1 root root  1439 Nov 10 12:53 /etc/passwd
-rwsr-xr-x 1 root root 72840 Feb  2  2026 /usr/bin/chfn
-rwsr-xr-x 1 root root 48936 Feb  2  2026 /usr/bin/chsh
```

`/etc/passwd` darf nur root schreiben. Damit jeder seine eigene Shell oder seinen Kommentar ändern kann, laufen `chsh` und `chfn` mit der effektiven Benutzernummer 0. (c) Das Programm muss seine Macht selbst begrenzen: Es prüft die reale Benutzernummer, ändert nur die Zeile dieses Benutzers (außer die reale Nummer ist 0), verlangt dessen Passwort und erlaubt nur zulässige Werte, bei `chsh` etwa nur Shells, die in `/etc/shells` stehen.
:::
:::

:::aufgabe Aufgabe 24 ★★ Ein Skript ohne Leserecht
<span class="anker" id="aufg-24"></span>

Lege mit `printf '#!/bin/bash\necho Hallo\n' > hallo.sh` ein Skript an und gib ihm die Rechte 111. (a) Sage voraus, ob `./hallo.sh` und `bash hallo.sh` funktionieren, prüfe und erkläre mit dem ersten Absatz von Unterabschnitt [9.5](#stufe-9-5). (b) Welche Rechte braucht ein Skript mindestens, damit sein Besitzer es mit `./` starten kann?

:::loesung
```console
$ printf '#!/bin/bash\necho Hallo\n' > hallo.sh
$ chmod 111 hallo.sh
$ ls -l hallo.sh
---x--x--x 1 student student 23 Nov 10 13:01 hallo.sh
$ ./hallo.sh
/bin/bash: ./hallo.sh: Permission denied
$ bash hallo.sh
bash: hallo.sh: Permission denied
$ chmod 500 hallo.sh
$ ls -l hallo.sh
-r-x------ 1 student student 23 Nov 10 13:01 hallo.sh
$ ./hallo.sh
Hallo
```

(a) Beide scheitern, aus verschiedenen Gründen. Bei `./hallo.sh` hat der Kernel das x-Bit gesehen und `/bin/bash` gestartet; die Meldung kommt deshalb von `/bin/bash`. bash muss die Datei dann aber über ihren Namen öffnen und lesen, und dafür fehlt `r`. Bei `bash hallo.sh` startet die Shell bash direkt, das x-Bit spielt keine Rolle, aber auch hier muss bash die Datei lesen. (b) Der Besitzer braucht `r` und `x`, also mindestens `r-x------` = 500.
:::
:::

:::aufgabe Aufgabe 25 ★★ Gemeinsam in /tmp
<span class="anker" id="aufg-25"></span>

`/tmp` hat `drwxrwxrwt` und gehört root. (a) Warum darfst du dort Dateien anlegen? (b) Warum kann ein anderer Benutzer deine Dateien dort nicht löschen, obwohl er in `/tmp` schreiben darf? (c) Wer darf deine Dateien in `/tmp` trotzdem löschen?

:::loesung
(a) `/tmp` hat `rwx` für die Klasse andere; mit `w` und `x` darf jeder Einträge anlegen. (b) Das `t` am Ende ist das Sticky-Bit: In einem solchen Verzeichnis darf nur löschen oder umbenennen, wem der Eintrag oder das Verzeichnis gehört, oder root. Ein anderer Benutzer ist weder Besitzer deiner Datei noch von `/tmp`. (c) Du selbst, weil dir der Eintrag gehört, und root, das auch Besitzer von `/tmp` ist.
:::
:::
