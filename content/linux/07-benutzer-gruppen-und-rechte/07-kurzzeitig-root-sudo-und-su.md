---
title: Kurzzeitig root: sudo und su
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120700
summary: Manche Arbeiten brauchen die Rechte von root: Konten anlegen, Dateien in /etc ändern, Besitzer wechseln.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Manche Arbeiten brauchen die Rechte von root: Konten anlegen, Dateien in `/etc` ändern, Besitzer wechseln. Dieser Abschnitt zeigt, wie man genau einen Befehl mit diesen Rechten ausführt, wer das darf, wo es festgehalten wird und warum eine bekannte Schreibweise dabei scheitert.
:::

### Der Befehl sudo

<span class="anker" id="stufe-6-1"></span>

Dauerhaft als root zu arbeiten, wäre bequem und gefährlich: Jeder Tippfehler und jedes fehlerhafte Programm hätte alle Rechte. Besser ist es, als gewöhnlicher Benutzer zu arbeiten und nur für den einen Befehl, der es braucht, root zu werden. Man kann sich das vorstellen wie bei einer Hausmeisterin, die den Generalschlüssel nur für eine bestimmte Tür herausgibt, sich vorher den Ausweis zeigen lässt und jede Ausgabe in ein Buch einträgt.

:::definition Definition 6.1 (sudo)
<span class="anker" id="satz-6-1"></span>

`sudo befehl …` führt einen einzigen Befehl als root aus. Vorher prüft `sudo`, ob der aufrufende Benutzer das darf, und verlangt in der Regel dessen eigenes Passwort, nicht das von root. Danach läuft der Befehl in einem neuen Prozess mit der Benutzernummer 0; sobald er endet, arbeitest du wieder mit deinen eigenen Rechten.
:::

Der Name wird meist als englisch „superuser do“ gelesen, sinngemäß „als Verwalter ausführen“. Abbildung [16](#abb-16) zeigt die drei Dinge, die `sudo` vor dem Start erledigt.

:::abbildung linux/k7sudo 16
Links die Shell von `student` mit dem Etikett `uid=1000`. Ein Pfeil führt zu `sudo`, das drei Stationen nacheinander abhakt: Erlaubnis in `/etc/sudoers` nachsehen, Passwort von `student` prüfen, Eintrag ins Protokoll schreiben. Erst dann startet rechts der Befehl `whoami` mit dem Etikett `uid=0`. Nach dem Ende des Befehls ist rechts nichts mehr, links läuft die Shell unverändert mit `uid=1000`.
:::

```console
$ whoami
student
$ sudo whoami
root
$ sudo id
uid=0(root) gid=0(root) groups=0(root)
```

Derselbe Befehl `whoami` meldet einmal `student` und einmal `root`: Der zweite lief in einem Prozess mit der Benutzernummer 0, und `id` bestätigt, dass auch die Gruppen die von root waren.

Das Testsystem dieses Kapitels ist so eingerichtet, dass `sudo` nicht nach dem Passwort fragt; in den Ausgaben fehlt die Frage deshalb, und im Live-System fragt `sudo` ebenfalls nicht. In WSL oder einer virtuellen Maschine sieht der erste Aufruf so aus:

```console
$ sudo whoami
[sudo: authenticate] Password:
root
```

Du tippst dein eigenes Passwort. Für jedes getippte Zeichen erscheint ein Sternchen; ein falsches Passwort beantwortet `sudo` mit „Authentication failed, try again.“ und fragt erneut. Danach merkt sich `sudo` die Anmeldung für dieses Terminal 15 Minuten lang und fragt in dieser Zeit nicht wieder; in einem zweiten Terminalfenster fragt es neu. Die Frage `[sudo: authenticate] Password:` und die Sternchen sind der Stand der Fassung sudo-rs in Ubuntu 26.04. Das klassische `sudo` anderer Systeme fragt mit `[sudo] password for student:` und zeigt beim Tippen nichts an.

⁠**Kurz gesagt:** `sudo befehl` führt genau einen Befehl als root aus, nach einer Prüfung der Erlaubnis und deines eigenen Passworts.

:::warnung Mit sudo gibt es kein Netz
Ein Befehl mit `sudo` darf alles, auch Systemdateien überschreiben oder ganze Verzeichnisse löschen, und fragt nicht nach. Benutze `sudo` in diesem Kapitel nur für die Befehle, die dort stehen, und tippe sie genau so ab. Lies jeden Befehl mit `sudo` vor dem Abschicken noch einmal, besonders Pfade und Leerzeichen. Setze `sudo` nicht aus Gewohnheit vor Befehle, die auch ohne funktionieren.
:::

### Die Erlaubnis: sudoers und sudo -l

<span class="anker" id="stufe-6-2"></span>

Nicht jeder darf `sudo` benutzen, sonst wäre die Trennung von root und gewöhnlichen Benutzern wertlos. Wer was darf, steht in einer Konfigurationsdatei, die nur root lesen kann.

:::definition Definition 6.2 (sudoers)
<span class="anker" id="satz-6-2"></span>

Die Datei `/etc/sudoers` legt fest, wer mit `sudo` welche Befehle als welcher Benutzer ausführen darf. Eine Regel hat die Form `wer wo=(als wer) was`. Ein `%` vor dem ersten Teil meint eine Gruppe, das Wort `ALL` steht für „alle“. `sudo -l` (englisch „list“) zeigt, was der aufrufende Benutzer darf.
:::

Abbildung [17](#abb-17) zerlegt die Regel, mit der Ubuntu der Gruppe `sudo` alles erlaubt.

:::abbildung linux/k7sudoers 17
Die Regel `%sudo ALL=(ALL:ALL) ALL`. Nacheinander leuchten die Teile auf und bekommen ihre Beschriftung: `%sudo` „wer: alle Mitglieder der Gruppe sudo“, das erste `ALL` „wo: auf jedem Rechner“, `(ALL:ALL)` „als wer: als jeder Benutzer und mit jeder Gruppe“, das letzte `ALL` „was: jeder Befehl“. Zum Schluss führt ein Pfeil von `%sudo` zur Zeile `sudo:x:27:student` in `/etc/group`.
:::

```console
$ sudo grep -E '^(root|%sudo)' /etc/sudoers
root    ALL=(ALL:ALL) ALL
%sudo   ALL=(ALL:ALL) ALL
```

Die erste Regel erlaubt root alles, die zweite allen Mitgliedern der Gruppe `sudo`. Weil `student` in Unterabschnitt [1.3](benutzer-und-gruppen.html#stufe-1-3) in dieser Gruppe stand, darf er alles. `sudo -l` fasst zusammen, was für den aufrufenden Benutzer gilt:

```console
$ sudo -l
User student may run the following commands on labor:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL
```

Die erste Zeile stammt aus der Regel für die Gruppe `sudo`. Die zweite mit `NOPASSWD` ist die Einrichtung des Testsystems, die das Passwort abschaltet; auf deinem Rechner fehlt sie.

⁠**Kurz gesagt:** `/etc/sudoers` legt in Regeln der Form `wer wo=(als wer) was` fest, wer `sudo` benutzen darf; unter Ubuntu darf das die Gruppe `sudo`, und `sudo -l` zeigt die eigene Erlaubnis.

:::warnung /etc/sudoers nie mit einem gewöhnlichen Editor ändern
Ein einziger Tippfehler in `/etc/sudoers` kann `sudo` für alle unbrauchbar machen; ohne Passwort für root kommt man dann nur noch auf Umwegen an die Rechte des Verwalters. Wer die Datei ändern muss, benutzt dafür den Befehl `visudo`, der die Datei vor dem Speichern prüft. In diesem Kapitel wird sie nur gelesen.
:::

### Als anderer Benutzer: sudo -u

<span class="anker" id="stufe-6-3"></span>

Das „als wer“ in der Regel deutet es an: `sudo` kann einen Befehl nicht nur als root ausführen. Das braucht man, wenn man prüfen will, was ein anderer Benutzer darf, ohne sich als dieser anzumelden.

:::definition Definition 6.3 (sudo -u)
<span class="anker" id="satz-6-3"></span>

`sudo -u benutzer befehl …` führt den Befehl als der genannte Benutzer aus, mit dessen Benutzernummer, Hauptgruppe und Zusatzgruppen.
:::

```console
$ sudo -u nobody whoami
nobody
```

Der Befehl lief als `nobody`, das Systemkonto aus Unterabschnitt [1.4](benutzer-und-gruppen.html#stufe-1-4), das nichts besitzt.

⁠**Kurz gesagt:** `sudo -u name befehl` führt einen Befehl als beliebiger Benutzer aus.

### root und die Rechte

<span class="anker" id="stufe-6-4"></span>

Mit `sudo` lässt sich jetzt der erste Schritt der Rechteprüfung aus Unterabschnitt [5.2](wie-der-kernel-rechte-pruft.html#stufe-5-2) beobachten: Für die Benutzernummer 0 prüft der Kernel die neun Bits nicht.

::::beispiel Eine Datei ohne Rechte
Nimm der Einkaufsliste alle neun Rechte:

```console
$ chmod 000 einkauf.txt
$ cat einkauf.txt
cat: einkauf.txt: Permission denied
$ sudo cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ chmod 644 einkauf.txt
```

`student` darf nicht mehr lesen, `cat` als root schon: Für root gelten Lese- und Schreibrechte nicht.
::::

⁠**Kurz gesagt:** root liest und schreibt jede Datei, gleich welche Rechte sie hat.

:::hintergrund root ist in Einzelrechte zerlegt
Unter Linux ist „root darf alles“ genau genommen eine Abkürzung. Der Kernel kennt rund vierzig einzelne Sonderrechte, die Fähigkeiten (englisch „capabilities“). Eine erlaubt zum Beispiel, die Lese- und Schreibrechte von Dateien zu übergehen, eine andere, den Besitzer einer Datei zu ändern, eine dritte, die Uhr des Rechners zu stellen. Ein Prozess mit der Benutzernummer 0 hat normalerweise alle diese Fähigkeiten, deshalb wirkt root allmächtig. Man kann einem Programm aber auch nur einzelne Fähigkeiten geben, statt es als root laufen zu lassen. Wie das geht und was es für die Sicherheit bedeutet, ist ein Thema der Reihe Cybersecurity.
:::

### Das Protokoll

<span class="anker" id="stufe-6-5"></span>

Wenn mehrere Menschen einen Rechner verwalten, will man später nachvollziehen können, wer was mit den Rechten von root getan hat. Auch wer allein arbeitet, findet so heraus, welcher Befehl etwas verändert hat.

:::definition Definition 6.4 (Protokoll von sudo)
<span class="anker" id="satz-6-4"></span>

`sudo` schreibt jeden Aufruf in das Protokoll des Systems: wer ihn auslöste, in welchem Terminal und Verzeichnis, als welcher Benutzer und welchen Befehl, auch abgelehnte Versuche. Ubuntu legt diese Einträge in der Protokolldatei `/var/log/auth.log` ab. Sie gehört dem Systemkonto `syslog`; außer ihm dürfen sie nur root und die Gruppe `adm` lesen.
:::

Die Protokolldateien unter `/var/log` kennst du aus [Kapitel 3, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-5). Die Zeilen mit einem ausgeführten Befehl enthalten den Text `COMMAND=`:

```console
$ sudo grep COMMAND= /var/log/auth.log | tail -n 2
2026-11-10T12:33:18.501225+01:00 labor sudo: student : TTY=/dev/pts/2 ; PWD=/home/student/linuxk7 ; USER=root ; COMMAND=/usr/bin/cat einkauf.txt
2026-11-10T12:33:19.115927+01:00 labor sudo: student : TTY=/dev/pts/2 ; PWD=/home/student/linuxk7 ; USER=root ; COMMAND=/usr/bin/grep COMMAND= /var/log/auth.log
```

Jede Zeile beginnt mit Datum und Uhrzeit, dem Rechnernamen und dem Programm `sudo`. Danach folgen der Benutzer `student`, das Terminal (`TTY`), das Arbeitsverzeichnis (`PWD`), der Zielbenutzer `root` und der Befehl. Die letzte Zeile ist der Befehl, der das Protokoll gerade gelesen hat: Auch er lief mit `sudo` und steht deshalb selbst darin.

⁠**Kurz gesagt:** `sudo` protokolliert jeden Aufruf mit Benutzer, Ort und Befehl; unter Ubuntu stehen die Einträge in `/var/log/auth.log`.

### Die Umleitungsfalle: sudo und >

<span class="anker" id="stufe-6-6"></span>

Ein Satz in eine Datei schreiben, die root gehört, scheint einfach: `sudo` vor den Befehl, fertig. Genau das scheitert, und der Grund steht schon in [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html). Für den Versuch legst du mit `sudo` eine leere Datei an, die root gehört:

```console
$ sudo touch nurroot.txt
$ ls -l nurroot.txt
-rw-r--r-- 1 root root 0 Nov 10 12:33 nurroot.txt
$ sudo echo Hallo > nurroot.txt
bash: nurroot.txt: Permission denied
```

Die Meldung beginnt mit `bash:`, nicht mit `sudo:` oder `echo:`. Abbildung [18](#abb-18) zeigt, warum.

:::abbildung linux/k7sudofalle 18
Zwei Zeilen untereinander. Oben `sudo echo Hallo > nurroot.txt`: Die Shell mit `uid=1000` öffnet zuerst die Datei für `>`; der Kernel prüft mit 1000 und lehnt ab (rotes Kreuz); `sudo` und `echo` starten gar nicht. Unten `echo Hallo | sudo tee nurroot.txt`: Die Shell verbindet nur die Pipe; `tee` läuft unter `sudo` mit `uid=0` und öffnet die Datei selbst (grünes Häkchen).
:::

:::satz Satz 6.5 (Umleitung und sudo)
<span class="anker" id="satz-6-5"></span>

Eine Umleitung wie `> datei` führt die Shell aus, bevor sie den Befehl startet, und zwar mit den Rechten der Shell ([Kapitel 4, Abschnitte 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1) und [2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7)). Ein `sudo` im Befehl ändert daran nichts, denn `sudo` startet erst danach. Um als root in eine Datei zu schreiben, muss ein Programm die Datei öffnen, das selbst als root läuft.
:::

Das passende Programm ist `tee` aus [Kapitel 4, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-4): Es öffnet die Datei, die als Argument dasteht, selbst. Läuft es unter `sudo`, öffnet es sie als root:

```console
$ echo Hallo | sudo tee nurroot.txt
Hallo
$ echo Tschüss | sudo tee -a nurroot.txt > /dev/null
$ cat nurroot.txt
Hallo
Tschüss
```

Wie in [Kapitel 4, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-4) schreibt `tee` zusätzlich auf den Bildschirm, deshalb erscheint `Hallo` einmal; `-a` hängt an. Das `> /dev/null` am Ende ist hier kein Problem: Es verwirft nur, was `tee` auf den Bildschirm schreiben würde, und `/dev/null` darf jeder beschreiben.

Zum Schluss räumst du `nurroot.txt` wieder weg. Anhängen darf `student` an diese Datei nicht, sie gehört ja root und hat `rw-r--r--`. Löschen geht trotzdem:

```console
$ echo mehr >> nurroot.txt
bash: nurroot.txt: Permission denied
$ rm nurroot.txt
rm: remove write-protected regular file 'nurroot.txt'? y
$ ls nurroot.txt
ls: cannot access 'nurroot.txt': No such file or directory
```

Das ist der Satz aus Unterabschnitt [4.4](rechte-bei-verzeichnissen.html#stufe-4-4) in seiner stärksten Form: Die Datei gehört root, aber ihr Name steht in einem Verzeichnis, das `student` gehört. Wer die Tabelle schreiben darf, darf jeden Namen darin streichen.

⁠**Kurz gesagt:** `sudo befehl > datei` öffnet die Datei mit den Rechten der Shell; als root schreibt man mit `befehl | sudo tee datei`.

### su und die Shell des Verwalters

<span class="anker" id="stufe-6-7"></span>

Manchmal braucht man nicht einen Befehl, sondern eine ganze Reihe, etwa beim Aufräumen eines Systems. Dafür gibt es eine Shell, die selbst als root läuft. Der ältere Weg dorthin heißt `su`.

:::definition Definition 6.6 (su)
<span class="anker" id="satz-6-6"></span>

`su benutzer` (englisch „substitute user“) startet eine neue Shell als der genannte Benutzer; ohne Namen ist root gemeint. `su` verlangt das Passwort des Zielbenutzers, nicht das eigene. Mit der Option `-` (`su -` oder `su - name`) wird die neue Shell eine Anmelde-Shell, die im Heimatverzeichnis des Zielbenutzers beginnt ([Kapitel 5, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-3)).
:::

Auf diesen Befehl spielt auch der Name `sudo` an: Seine Entwickler schreiben ihn als „su do“. Abbildung [19](#abb-19) stellt `su` und `sudo` nebeneinander.

:::abbildung linux/k7susudo 19
Zwei Spalten. Links `su -`: Der Benutzer gibt das Passwort von root ein; es entsteht eine Shell mit `uid=0`, in der beliebig viele Befehle laufen, bis `exit` sie beendet; ins Protokoll kommt nur „root“. Rechts `sudo befehl`: Der Benutzer gibt sein eigenes Passwort ein; genau ein Befehl läuft mit `uid=0`, danach ist der Benutzer sofort wieder er selbst; ins Protokoll kommt sein Name mit dem Befehl. Zum Schluss wird links das Passwortfeld durchgestrichen: Unter Ubuntu hat root keines.
:::

Unter Ubuntu führt dieser Weg zu root ins Leere:

```console
$ su -
Password:
su: Authentication failure
```

Hier wurde einfach die Eingabetaste gedrückt. Ein Passwort, das passen könnte, gibt es nicht. Das zeigt der Prüfwert von root in der Schattendatei, den nur root selbst lesen darf:

```console
$ sudo head -n 1 /etc/shadow | cut -d: -f1,2
root:*
```

Ein `*` passt nach Unterabschnitt [1.8](benutzer-und-gruppen.html#stufe-1-8) zu keinem Passwort. Ubuntu sperrt die Anmeldung als root auf diese Weise ab und lässt nur den Weg über `sudo`. Eine Shell als root bekommt man dort mit `sudo -i`; ihre Eingabeaufforderung endet mit `#`, die Zeilen beginnen deshalb hier mit diesem Zeichen:

```console
$ sudo -i
# whoami
root
# pwd
/root
# exit
logout
```

Beim ersten Aufruf am Tag begrüßt Ubuntu dich vorher mit einigen Zeilen über das System. `exit` beendet die Shell des Verwalters, und du bist wieder in deiner eigenen.

⁠**Kurz gesagt:** `su` startet eine Shell als anderer Benutzer mit dessen Passwort; unter Ubuntu hat root keines, eine Shell als root gibt `sudo -i`.

:::warnung Eine Shell als root nur kurz
In einer Shell als root gilt die Warnung zu `sudo` für jeden Befehl, und das `#` am Zeilenanfang ist leicht zu übersehen. Erledige darin nur, was du dir vorgenommen hast, und verlasse sie sofort mit `exit`.
:::

:::hintergrund Warum sudo den Weg über su abgelöst hat
Früher meldeten sich die Verwalter mit `su` und dem Passwort von root an. Das hatte drei Nachteile. Alle, die das System pflegten, mussten dasselbe Passwort kennen; wer es einmal wusste, behielt es. Im Protokoll stand nur „root“, nicht, wer dahintersteckte. Und viele blieben bequemerweise den ganzen Tag in der Shell von root, sodass jedes Programm, das sie starteten, alle Rechte hatte. `sudo` verlangt das eigene Passwort, schreibt den echten Namen ins Protokoll, kann auf einzelne Befehle beschränkt werden und gibt die Rechte nur für einen Befehl. Das ist der Grundsatz der minimalen Rechte: genau die nötigen Rechte, nur so lange wie nötig ([Cybersecurity, Kapitel 1, Abschnitt 5.2](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-2)). Ubuntu hat diesen Weg von Anfang an zur Voreinstellung gemacht; viele andere Distributionen bieten ihn bei der Einrichtung an.
:::

:::hintergrund sudo-rs und das klassische sudo
Seit Ubuntu 25.10 ist `sudo` eine Neufassung in der Programmiersprache Rust, sudo-rs; auf dem Testsystem ist es die Fassung 0.2.13. Der Grund ist derselbe wie bei den Grundbefehlen in [Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2): Ein Programm, das root werden kann, soll so wenig Speicherfehler wie möglich enthalten. Im Alltag merkt man wenig davon: Die Passwortfrage sieht anders aus, beim Tippen erscheinen Sternchen, und wer nicht in `/etc/sudoers` steht, bekommt die Meldung „I'm sorry … I'm afraid I can't do that“. Einige selten gebrauchte Möglichkeiten fehlen, etwa die Option `-E`, die die ganze Umgebung an den Befehl weitergäbe, und das Protokoll geht immer in das Systemprotokoll. Das klassische Programm ist auf dem Testsystem unter dem Namen `sudo.ws` weiterhin installiert. Dieser Stand gilt für Ubuntu 26.04; andere Distributionen benutzen meist noch das klassische `sudo`.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-8"></span>

:::aufgabe Aufgabe 13 ★ Die eigene Erlaubnis
<span class="anker" id="aufg-13"></span>

(a) Lies mit `sudo -l` deine Erlaubnis auf deinem eigenen System und erkläre jeden Teil der Zeile in Klammern. (b) Warum fragt `sudo` beim zweiten Aufruf kurz danach nicht mehr nach dem Passwort, in einem neuen Terminalfenster aber schon?

:::loesung
(a) Auf einem gewöhnlichen Ubuntu zeigt `sudo -l` eine Zeile `(ALL : ALL) ALL` unter „User … may run the following commands on …“. Das erste `ALL` in der Klammer erlaubt, Befehle als jeder Benutzer auszuführen (`sudo -u`), das zweite, mit jeder Gruppe (`sudo -g`); das `ALL` dahinter erlaubt jeden Befehl. Den Rechner nennt die Kopfzeile. (b) `sudo` merkt sich eine gelungene Anmeldung 15 Minuten lang, und zwar je Terminal. Ein neues Terminalfenster gilt als neue Sitzung, deshalb fragt es dort erneut.
:::
:::

:::aufgabe Aufgabe 14 ★★ Die Umleitungsfalle selbst erleben
<span class="anker" id="aufg-14"></span>

(a) Lege mit `sudo touch nurroot2.txt` eine Datei an, die root gehört. Sage voraus, was `sudo echo test > nurroot2.txt` meldet, prüfe und erkläre. (b) Schreibe `test` mit `tee` hinein und hänge eine zweite Zeile an, ohne dass `tee` etwas auf dem Bildschirm ausgibt. (c) Was geschieht, wenn du `sudo echo test > neudatei.txt` mit einer Datei versuchst, die es noch nicht gibt? Wem gehört sie danach, und warum?

:::loesung
```console
$ sudo touch nurroot2.txt
$ sudo echo test > nurroot2.txt
bash: nurroot2.txt: Permission denied
$ echo test | sudo tee nurroot2.txt
test
$ echo zweite Zeile | sudo tee -a nurroot2.txt > /dev/null
$ cat nurroot2.txt
test
zweite Zeile
$ ls -l nurroot2.txt
-rw-r--r-- 1 root root 18 Nov 10 12:53 nurroot2.txt
$ rm -f nurroot2.txt
```

(a) Die Shell von `student` öffnet `nurroot2.txt` für die Umleitung, bevor `sudo` startet; die Datei gehört root und hat für andere kein `w`, also scheitert sie mit `bash: … Permission denied`. `sudo` und `echo` laufen gar nicht erst. (b) `tee` öffnet die Datei selbst und läuft als root; `-a` hängt an, `> /dev/null` verschluckt die Ausgabe von `tee` auf den Bildschirm. Die Datei gehört weiterhin root. Löschen durfte `student` sie trotzdem, denn das Verzeichnis gehört ihm.

(c) Mit einer neuen Datei klappt die Umleitung scheinbar:

```console
$ sudo echo test > neudatei.txt
$ ls -l neudatei.txt
-rw-r--r-- 1 student student 5 Nov 10 12:53 neudatei.txt
```

Die Shell legt die Datei im Übungsverzeichnis an, und dort darf `student` anlegen. Deshalb gehört sie `student`, nicht root: `sudo` hat nur `echo` als root ausgeführt, und `echo` schreibt bloß in den Deskriptor, den die Shell schon geöffnet hatte. In einem Verzeichnis, das nur root beschreiben darf, wäre derselbe Befehl gescheitert.
:::
:::

:::aufgabe Aufgabe 15 ★★ Spuren im Protokoll
<span class="anker" id="aufg-15"></span>

Finde in `/var/log/auth.log` die Einträge deiner Aufrufe von `tee` aus Aufgabe [14](#aufg-14). Achte darauf, dass dein eigener Suchbefehl nicht selbst unter den Treffern landet. Was verrät eine Zeile über dich?

:::loesung
```console
$ sudo grep COMMAND= /var/log/auth.log | grep tee | tail -n 2
2026-11-10T13:01:37.376141+01:00 labor sudo: student :  PWD=/home/student/linuxk7 ; USER=root ; COMMAND=/usr/bin/tee nurroot2.txt
2026-11-10T13:01:37.688404+01:00 labor sudo: student :  PWD=/home/student/linuxk7 ; USER=root ; COMMAND=/usr/bin/tee -a nurroot2.txt
```

Ein einfaches `sudo grep 'tee' /var/log/auth.log` fände auch sich selbst, denn der Suchbefehl läuft mit `sudo` und steht mit dem Wort `tee` im Protokoll, bevor `grep` die Datei zu Ende gelesen hat. Die Pipeline umgeht das: Der erste `grep` sucht nach `COMMAND=`, und seine eigene Zeile enthält kein `tee`; der zweite `grep` läuft ohne `sudo` und landet nicht im Protokoll. Jede Zeile verrät Datum und Uhrzeit, den Rechner, den Benutzer `student`, das Arbeitsverzeichnis, den Zielbenutzer root und den genauen Befehl samt Argumenten. Die Angabe `TTY` fehlt hier; bei diesen Aufrufen kam die Eingabe von `sudo` aus einer Pipe.
:::
:::
