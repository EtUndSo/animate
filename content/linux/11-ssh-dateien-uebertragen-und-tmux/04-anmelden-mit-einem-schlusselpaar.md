---
title: Anmelden mit einem Schlüsselpaar
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160400
summary: Jetzt weist du dich beim Server aus, und zwar nicht mit einem Passwort, sondern mit einem eigenen Schlüsselpaar.
tags: Anmeldung mit öffentlichem Schlüssel, ssh-keygen, private Schlüsseldatei, öffentliche Schlüsseldatei, Passphrase, ssh-agent
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Jetzt weist du dich beim Server aus, und zwar nicht mit einem Passwort, sondern mit einem eigenen Schlüsselpaar. Dieser Abschnitt erklärt, wie das funktioniert, wie man ein Schlüsselpaar erzeugt und auf dem Server hinterlegt, warum `ssh` so genau auf Dateirechte achtet und wie man den privaten Schlüssel zusätzlich schützt.
:::

### Die Anmeldung mit öffentlichem Schlüssel

<span class="anker" id="stufe-3-1"></span>

Der Server weiß jetzt, wer er ist, aber noch nicht, wer du bist. Mit einem Passwort ginge das, hätte aber Nachteile: Man kann es erraten, viele Menschen benutzen dasselbe Passwort an mehreren Stellen, und bei jeder Anmeldung muss es zum Server, also auch zu einem falschen Server, wenn man sich bei der ersten Verbindung geirrt hat. SSH kennt ein Verfahren, bei dem gar kein Geheimnis über die Leitung geht.

Ein Bild zur Orientierung: Diesmal trägst du den Siegelring, und der Server hat in seiner Kartei einen Musterabdruck deines Wappens. Wer sich anmelden will, muss vor den Augen des Servers ein frisches Siegel auf eine Nachricht drücken, die der Server für genau diesen Besuch vorgibt.

:::definition Definition 3.1 (Anmeldung mit öffentlichem Schlüssel)
<span class="anker" id="satz-3-1"></span>

Bei der __Anmeldung mit öffentlichem Schlüssel__ (Verfahren `publickey`) ist auf dem Server der öffentliche Schlüssel eines Schlüsselpaars des Benutzers hinterlegt. Beim Anmelden signiert der Client mit dem privaten Schlüssel Daten, die zu genau dieser Verbindung gehören, und schickt die Signatur. Der Server prüft sie mit dem hinterlegten öffentlichen Schlüssel und lässt den Benutzer herein, wenn sie gültig ist.
:::

Der private Schlüssel verlässt dabei nie deinen Rechner; über die Leitung geht nur die Signatur. Das ist dieselbe Technik, mit der sich der Server in Abschnitt [2.2](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2-2) ausgewiesen hat, nur mit vertauschten Rollen. Als die erste Verbindung mit `Permission denied (publickey)` endete, hatte der Server genau dieses Verfahren angeboten, aber dein Client hatte noch keinen Schlüssel.

::::beispiel Was über die Leitung geht
Meldet sich `anna` mit einem Passwort an, schickt ihr Client (verschlüsselt) das Passwort selbst, etwa `Sommer2026!`; der Server vergleicht es mit seinem Prüfwert ([Kapitel 7, Abschnitt 1.8](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-8)). Meldet sie sich mit einem Schlüssel an, schickt ihr Client nur eine Signatur über Daten dieser einen Verbindung. Bei der nächsten Anmeldung sind die Daten andere und damit auch die Signatur; die alte nützt niemandem etwas.
::::

:::hintergrund Warum ein Schlüsselpaar sicherer ist als ein Passwort
Drei Gründe, die alle aus der Definition folgen. Erstens gibt es nichts zu erraten: Ein privater Ed25519-Schlüssel ist eine Zufallszahl mit 256 Bit, während Passwörter, die sich Menschen merken können, nur einen winzigen Teil davon ausschöpfen. Zweitens liegt auf dem Server nichts, mit dem sich ein Eindringling anmelden könnte: Er findet dort nur öffentliche Schlüssel, und die darf ohnehin jeder kennen. Wer dagegen die Prüfwerte von Passwörtern erbeutet, kann sie durchprobieren, und wer dasselbe Passwort anderswo benutzt hat, ist auch dort verwundbar. Drittens geht über die Leitung nichts, was sich wiederverwenden ließe. Selbst wer sich wie im Hintergrund von Abschnitt [2.4](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2-4) dazwischenschaltet und deine Anmeldung abfängt, bekommt nur eine Signatur über Daten seiner eigenen Verbindung mit dir; beim echten Server, mit dem er eine zweite Verbindung mit anderen Daten hat, nützt sie ihm nichts. Die Grenze des Verfahrens liegt beim privaten Schlüssel selbst: Wer die Datei mit ihm in die Hände bekommt, kann sich als du anmelden. Deshalb schützt man diese Datei mit strengen Rechten und einer Passphrase. Wie Signaturen mathematisch funktionieren und warum man den privaten Schlüssel nicht aus dem öffentlichen berechnen kann, erklärt die Reihe Cybersecurity.
:::

⁠**Kurz gesagt:** Bei der Anmeldung mit öffentlichem Schlüssel beweist der Client mit einer Signatur, dass er den privaten Schlüssel besitzt; der Server kennt nur den öffentlichen, und der private verlässt den Rechner nie.

### Ein Schlüsselpaar erzeugen: ssh-keygen

<span class="anker" id="stufe-3-2"></span>

Ein Schlüsselpaar für SSH erzeugt das Programm `ssh-keygen`, das zu `openssh-client` gehört. Es fragt dabei nach einer *Passphrase*: einem Kennwort, mit dem `ssh-keygen` den privaten Schlüssel verschlüsselt, bevor es ihn in die Datei schreibt. Wer die Datei später benutzen will, muss die Passphrase eingeben. Für den Übungsschlüssel dieses Kapitels drückst du bei beiden Fragen nur die Eingabetaste, also ohne Passphrase; er gilt nur für deinen Übungsserver und wird am Ende gelöscht.

:::definition Definition 3.2 (ssh-keygen)
<span class="anker" id="satz-3-2"></span>

__ssh-keygen__ erzeugt ein Schlüsselpaar und speichert es in zwei Dateien: den privaten Schlüssel in der Datei, die `-f` nennt, den öffentlichen in derselben Datei mit angehängtem `.pub`. `-t` wählt den Typ; `ed25519` ist heute die Voreinstellung und die übliche Wahl. Ohne `-f` schlägt `ssh-keygen` `~/.ssh/id_ed25519` vor, die Stelle, an der `ssh` von selbst nach einem Schlüssel sucht.
:::

Den Schlüssel für die Übungen legst du im Übungsverzeichnis an, damit am Ende ein `rm -r ~/linuxk11` alles entfernt. Einen Schlüssel für echte Server erzeugst du später ohne `-f` am vorgeschlagenen Ort und mit Passphrase.

```console
$ ssh-keygen -t ed25519 -f uebungsschluessel
Generating public/private ed25519 key pair.
Enter passphrase for "uebungsschluessel" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in uebungsschluessel
Your public key has been saved in uebungsschluessel.pub
The key fingerprint is:
SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4 student@labor
The key's randomart image is:
+--[ED25519 256]--+
|      o+o.o..oo o|
|     +.o...... o |
|    . o o  . .. .|
|       . . +++oo |
|        S .oOo=..|
|         o * O.+.|
|        . o O.o.o|
|         . +..E. |
|        .o=.  .. |
+----[SHA256]-----+
```

`ssh-keygen` meldet, wohin es die beiden Teile gespeichert hat (*identification* ist der private Schlüssel), und zeigt den Fingerabdruck des neuen öffentlichen Schlüssels mit dem Kommentar `student@labor`: Ohne `-C kommentar` nimmt es Benutzer und Rechnernamen. Darunter steht ein Bild aus Zeichen. Abbildung [11](#abb-11) zeigt den Ablauf.

:::abbildung linux/k11keygen 11
Terminalbild (dunkel, wie Ubuntu, Prompt `student@labor:~/linuxk11$`): der Aufruf `ssh-keygen -t ed25519 -f uebungsschluessel` mit der vollständigen Ausgabe aus diesem Abschnitt, einschließlich der beiden Passphrase-Fragen (leer) und des Bildes aus Zeichen. Rechts neben dem Bild aus Zeichen erscheinen nacheinander zwei Dateikärtchen: `uebungsschluessel` mit Schloss („privat, bleibt hier“) und `uebungsschluessel.pub` („öffentlich, darf weitergegeben werden“).
:::

:::hintergrund Wozu das Bild aus Zeichen dient
Das Bild (englisch *randomart*) ist eine zweite Darstellung des Fingerabdrucks. `ssh-keygen` lässt dafür einen gedachten Läufer über ein Feld von 17 mal 9 Kästchen wandern; je zwei Bits des Fingerabdrucks bestimmen einen Schritt schräg nach links oder rechts, oben oder unten. Wie oft ein Kästchen betreten wurde, zeigt das Zeichen darin, `S` markiert den Start, `E` das Ende. Menschen erkennen ein bekanntes Bild schneller wieder als 43 Zeichen; OpenSSH zeigt es seit 2008. Sicher vergleicht man trotzdem den Fingerabdruck selbst.
:::

⁠**Kurz gesagt:** `ssh-keygen -t ed25519 -f datei` erzeugt ein Schlüsselpaar in `datei` (privat) und `datei.pub` (öffentlich).

### Privater und öffentlicher Schlüssel

<span class="anker" id="stufe-3-3"></span>

Die beiden Dateien sehen sich ähnlich, haben aber ganz verschiedene Aufgaben. Ein Blick hinein:

```console
$ ls -l uebungsschluessel*
-rw------- 1 student student 399 Nov 13 03:18 uebungsschluessel
-rw-r--r-- 1 student student  95 Nov 13 03:18 uebungsschluessel.pub
$ cat uebungsschluessel.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH6kClePZwRp489Dols0j/kBW9643WAmkWzUBIw1Fr32 student@labor
$ head -n 1 uebungsschluessel
-----BEGIN OPENSSH PRIVATE KEY-----
$ ssh-keygen -l -f uebungsschluessel.pub
256 SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4 student@labor (ED25519)
```

:::definition Definition 3.3 (Die beiden Schlüsseldateien)
<span class="anker" id="satz-3-3"></span>

Die __private Schlüsseldatei__ enthält den privaten Schlüssel, bei Bedarf mit einer Passphrase verschlüsselt, und dazu eine Kopie des öffentlichen Schlüssels und den Kommentar. Nur ihr Besitzer darf sie lesen; `ssh-keygen` legt sie mit den Rechten 600 an. Die __öffentliche Schlüsseldatei__ mit der Endung `.pub` enthält eine einzige Zeile aus drei Teilen: den Typ, den öffentlichen Schlüssel in Base64 und den Kommentar. Sie darf jeder lesen.
:::

Die Zeile in `uebungsschluessel.pub` zählt 95 Bytes: 12 für `ssh-ed25519` mit Leerzeichen, 68 für den Schlüssel, eines für das Leerzeichen, 13 für `student@labor` und eines für das Zeilenende. Der Fingerabdruck ist derselbe wie bei der Erzeugung; er gehört zum Schlüssel, nicht zur Datei. Weil die private Datei den öffentlichen Schlüssel mitenthält, kann man eine verlorene `.pub`-Datei jederzeit wiederherstellen, umgekehrt nicht.

::::beispiel Was man womit tun darf
`uebungsschluessel.pub` darfst du per E-Mail verschicken, auf eine Webseite hochladen oder ausdrucken; wer sie hat, kann nur prüfen, ob eine Signatur von dir stammt. `uebungsschluessel` gibst du niemandem, nicht dem Betreuer eines Servers und nicht einer Webseite, die danach fragt. Eine Anleitung, die dich bittet, deinen privaten Schlüssel zu schicken, ist entweder falsch oder ein Betrugsversuch.
::::

⁠**Kurz gesagt:** Die Datei ohne Endung ist privat und bleibt mit Rechten 600 auf deinem Rechner, die `.pub`-Datei ist öffentlich und wandert zu den Servern.

### Die Datei authorized_keys

<span class="anker" id="stufe-3-4"></span>

Damit der Server deinen Schlüssel annimmt, muss er den öffentlichen Teil kennen. Er sucht ihn an einer festen Stelle im Heimatverzeichnis des Kontos, an dem du dich anmeldest.

:::definition Definition 3.4 (authorized_keys)
<span class="anker" id="satz-3-4"></span>

Die Datei __`~/.ssh/authorized_keys`__ auf dem Server enthält die öffentlichen Schlüssel, mit denen man sich an diesem Benutzerkonto anmelden darf, je Schlüssel eine Zeile im Format der `.pub`-Dateien.
:::

Auf deinem Übungsserver ist das Konto dein eigenes, und das Heimatverzeichnis liegt auf demselben Rechner. Du kannst den öffentlichen Schlüssel deshalb direkt anhängen; `>>` hängt an, statt zu überschreiben ([Kapitel 4, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-2)). Danach setzt du die Rechte auf 600:

```console
$ cat uebungsschluessel.pub >> ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys
$ ls -l ~/.ssh
total 8
-rw------- 1 student student  95 Nov 13 03:18 authorized_keys
-rw-r--r-- 1 student student 142 Nov 13 03:18 known_hosts
```

Achte auf die zwei spitzen Klammern: Mit einer einzigen würdest du alle Schlüssel überschreiben, die schon in der Datei stehen. Auf einem Server, an dem mehrere deiner Rechner Zugang haben, steht in `authorized_keys` für jeden Rechner ein eigener Schlüssel; wird ein Laptop gestohlen, löscht man nur seine Zeile (Abbildung [12](#abb-12)).

:::abbildung linux/k11authorizedkeys 12
Dateiansicht (hell) von `~/.ssh/authorized_keys` auf einem Server, drei Zeilen im Format der `.pub`-Dateien: `ssh-ed25519 AAAA… student@labor` (die Zeile aus diesem Abschnitt), `ssh-ed25519 AAAA… Laptop von Anna`, `ssh-ed25519 AAAA… Arbeitsrechner`. Links neben jeder Zeile ein kleines Gerät mit seinem privaten Schlüssel (Schloss). Dann wird das Gerät „Laptop von Anna“ rot durchgestrichen („gestohlen“), seine Zeile verschwindet, die beiden anderen Geräte kommen weiter herein. Oben die Rechte `rw-------`.
:::

⁠**Kurz gesagt:** Ein öffentlicher Schlüssel in `~/.ssh/authorized_keys` auf dem Server öffnet dem Besitzer des passenden privaten Schlüssels dieses Konto.

### Einen Schlüssel auf einen Server bringen: ssh-copy-id

<span class="anker" id="stufe-3-5"></span>

Bei einem echten Server liegt `authorized_keys` auf einem anderen Rechner, und du kommst ohne Schlüssel nicht hinein. Erlaubt der Server zunächst Passwörter, hilft ein kleines Programm.

:::definition Definition 3.5 (ssh-copy-id)
<span class="anker" id="satz-3-5"></span>

`ssh-copy-id -i schluessel.pub benutzer@rechner` meldet sich am Server an, mit Passwort oder einem schon vorhandenen Schlüssel, und hängt den öffentlichen Schlüssel an `~/.ssh/authorized_keys` an. Fehlt das Verzeichnis `.ssh`, legt es dieses an, und zwar so, dass nur der Besitzer Zugriff hat. Vorher prüft es, ob der Schlüssel schon eingetragen ist, und überspringt ihn dann.
:::

Die Form `benutzer@rechner` wählt das Konto auf dem Server; ohne `benutzer@` nimmt `ssh` deinen eigenen Benutzernamen, wie bei allen Aufrufen in diesem Kapitel. Auf deinem Übungsserver ist der Schlüssel schon eingetragen, deshalb tut `ssh-copy-id` dort nichts:

```console
$ ssh-copy-id -i uebungsschluessel.pub localhost
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "uebungsschluessel.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed

/usr/bin/ssh-copy-id: WARNING: All keys were skipped because they already exist on the remote system.
                (if you think this is a mistake, you may want to use -f option)
```

Es hat sich zur Probe mit dem Schlüssel angemeldet, festgestellt, dass das gelingt, und nichts verändert. Viele Server und Übungsplattformen erlauben gar keine Passwörter. Dann gibt man den öffentlichen Schlüssel auf einem anderen Weg ab: Man schickt die `.pub`-Datei an die Person, die den Server betreut, oder fügt ihren Inhalt in ein Formular auf der Webseite der Plattform ein.

⁠**Kurz gesagt:** `ssh-copy-id` trägt einen öffentlichen Schlüssel in `authorized_keys` auf einem Server ein, an dem man sich schon anmelden kann.

### Die erste Anmeldung mit dem Schlüssel

<span class="anker" id="stufe-3-6"></span>

Jetzt klappt die Anmeldung. Weil der Schlüssel nicht am üblichen Ort liegt, nennst du ihn mit `-i datei` („identity“). Nach der Anmeldung laufen die Befehle in der Shell auf dem Server, bis `exit` sie beendet:

```console
$ ssh -i uebungsschluessel localhost
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
Last login: Fri Nov 13 03:13:01 2026 from 127.0.0.1
$ echo "$SSH_CONNECTION"
127.0.0.1 55314 127.0.0.1 22
$ ps -o pid,ppid,user,tty,args -C sshd-session
    PID    PPID USER     TT       COMMAND
    575     477 root     ?        sshd-session: student [priv]
    603     575 student  ?        sshd-session: student@pts/3
$ ps -o pid,ppid,tty,args -p $$
    PID    PPID TT       COMMAND
    604     603 pts/3    -bash
$ exit
logout
Connection to localhost closed.
```

Der Server begrüßt dich mit einer Übersicht über das System und dem Zeitpunkt der letzten Anmeldung an diesem Konto; bei der allerersten Anmeldung fehlt diese Zeile (auf dem Testsystem lief die Übung vorher schon einmal). Die Variable `SSH_CONNECTION` setzt der Server für jede Sitzung: Adresse und Port des Clients, dann Adresse und Port des Servers. Der Port des Clients, hier 55 314, ist eine beliebige freie Nummer, die das System für diese eine Verbindung vergeben hat; der Port des Servers ist 22.

Die beiden `ps`-Befehle zeigen, wer auf dem Server für dich arbeitet. Für jede Verbindung startet `sshd` einen Prozess `sshd-session` unter root, der die Anmeldung überwacht und alles erledigt, wofür root-Rechte nötig sind (`[priv]` für „privilegiert“), und dieser einen zweiten unter deinem Benutzer, der das Terminal `pts/3` auf dem Server verwaltet. Dessen Kind ist deine Shell, eine Anmelde-Shell, wie das Minuszeichen in `-bash` verrät ([Kapitel 5, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-3)). Das Terminal `pts/3` ist ein Pseudoterminal ([Kapitel 2, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-2)): Was `sshd-session` aus der Verbindung empfängt, schreibt es dort hinein, als hätte jemand an einer Tastatur am Server getippt.

Bei der ersten erfolgreichen Anmeldung hat `ssh` außerdem still dazugelernt. Der Server hat ihm seine übrigen Hostschlüssel mitgeteilt, und `ssh` hat sie zum bestätigten Ed25519-Schlüssel in die Liste geschrieben:

```console
$ wc -l ~/.ssh/known_hosts
3 /home/student/.ssh/known_hosts
$ ssh-keygen -l -f ~/.ssh/known_hosts
256 SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw |1|ySQGAe9qe3R4zGcHsIh/DimhcNE=|vQphKx9KwrZp6bEuTx10GF8Rb6s= (ED25519)
3072 SHA256:thkYzoobvxKHDY9kDns2MuqB1KOmZOdJ3d9c5f/KTD0 |1|W/A/6YRMY/g6nNqBS8O95vaW3Xs=|iw521E2cs7Kl6gt0b/oGs0LZL8M= (RSA)
256 SHA256:RClt9obROtQy/l0z77CeHnNCom2A5tzJTEIpgT0Lt+0 |1|sCzPV/7WJFYM0e0ANWUYuUwbHH4=|hrepLF8BjkDgxp8wfBYhE1xf/O4= (ECDSA)
```

Das ist unbedenklich, denn die Nachricht kam über die schon geprüfte Verbindung; ändert der Betreuer später den Typ des Hostschlüssels, kennt der Client den neuen schon.

Was beim Anmelden geschieht, zeigt `ssh -v` („verbose“, ausführlich) Schritt für Schritt auf der Fehlerausgabe. Die meisten der vielen Zeilen interessieren hier nicht; `grep` wählt die drei aus, die zur Definition der Anmeldung mit öffentlichem Schlüssel passen:

```console
$ ssh -v -i uebungsschluessel localhost true 2>&1 | grep -E 'Offering|Server accepts|Authenticated to'
debug1: Offering public key: uebungsschluessel ED25519 SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4 explicit
debug1: Server accepts key: uebungsschluessel ED25519 SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4 explicit
Authenticated to localhost ([127.0.0.1]:22) using "publickey".
```

Der Client bietet den öffentlichen Schlüssel an (*offering*), der Server findet ihn in `authorized_keys` und nimmt das Angebot an (*accepts*), dann schickt der Client die Signatur, und der Server meldet die Anmeldung als gelungen. `explicit` heißt, dass der Schlüssel ausdrücklich mit `-i` genannt wurde. Der Befehl `true` am Ende lässt die Sitzung sofort wieder enden. Abbildung [13](#abb-13) zeigt beide Schlüsselpaare, das des Servers und deines, an ihren Plätzen.

:::abbildung linux/k11schluesselpaar 13
Client und Server mit ihren Schlüsselpaaren. Links der eigene Rechner: `~/linuxk11/uebungsschluessel` (privat, mit Schloss, 600) und `uebungsschluessel.pub`; dazu `~/.ssh/known_hosts` mit dem öffentlichen Hostschlüssel des Servers. Rechts der Server: `/etc/ssh/ssh_host_ed25519_key` (privat, Schloss, root) und `.pub`; dazu `~/.ssh/authorized_keys` mit einer Kopie von `uebungsschluessel.pub`. Ablauf in vier Schritten mit Pfeilen über die Verbindung: (1) Server signiert mit dem privaten Hostschlüssel, Client prüft gegen `known_hosts`; (2) Client bietet seinen öffentlichen Schlüssel an, Server findet ihn in `authorized_keys`; (3) Client signiert mit dem privaten Schlüssel; (4) Server prüft, Haken, eine Shell `-bash` erscheint rechts. Beide privaten Schlüssel bleiben die ganze Zeit an ihrem Platz.
:::

⁠**Kurz gesagt:** Mit `ssh -i schluessel rechner` meldet man sich mit einem Schlüssel an; auf dem Server startet dann `sshd-session` eine Anmelde-Shell an einem eigenen Pseudoterminal.

### Warum ssh auf strenge Rechte achtet

<span class="anker" id="stufe-3-7"></span>

Client und Server prüfen vor jeder Anmeldung die Rechte der beteiligten Dateien und weigern sich, mit zu offenen Rechten zu arbeiten. Das lässt sich auf beiden Seiten vorführen. Zuerst auf der Seite des Clients: Die private Schlüsseldatei bekommt die Rechte 644, die für gewöhnliche Dateien üblich sind:

```console
$ chmod 644 uebungsschluessel
$ ssh -i uebungsschluessel localhost true
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'uebungsschluessel' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "uebungsschluessel": bad permissions
student@localhost: Permission denied (publickey).
$ echo $?
255
$ chmod 600 uebungsschluessel
```

`ssh` lädt den Schlüssel gar nicht erst und versucht die Anmeldung ohne ihn, die dann scheitert. Nun die Seite des Servers: `authorized_keys` wird für alle anderen beschreibbar.

```console
$ chmod o+w ~/.ssh/authorized_keys
$ ls -l ~/.ssh/authorized_keys
-rw-----w- 1 student student 95 Nov 13 03:29 /home/student/.ssh/authorized_keys
$ ssh -i uebungsschluessel localhost true
student@localhost: Permission denied (publickey).
$ sudo journalctl -u ssh.service -o cat --no-pager | grep refused | tail -n 1
Authentication refused: bad ownership or modes for file /home/student/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys
$ ssh -i uebungsschluessel localhost true
$ echo $?
0
```

Diesmal lehnt der Server ab, und von außen sieht man nur `Permission denied`. Den Grund schreibt `sshd` in sein Protokoll, das Journal der Unit `ssh.service` ([Kapitel 8, Abschnitt 8.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/protokolle-das-journal.html#stufe-8-2)); als normaler Benutzer liest du es unter Ubuntu mit `sudo`. `-o cat` lässt Datum und Prozessnummer weg, `grep` sucht die Zeile mit `refused` („abgelehnt“). Nach `chmod 600` klappt die Anmeldung wieder.

:::satz Satz 3.6 (Die Rechte, die ssh verlangt)
<span class="anker" id="satz-3-6"></span>

<ul>

<li>

Der Client lehnt eine private Schlüsseldatei ab, sobald Gruppe oder andere irgendein Recht daran haben; üblich ist 600.

</li>

<li>

Der Server lehnt `authorized_keys` ab, wenn die Datei, das Verzeichnis `~/.ssh` oder das Heimatverzeichnis einem anderen Benutzer als dem Besitzer des Kontos oder root gehört oder wenn Gruppe oder andere sie beschreiben dürfen. Unter Ubuntu und Debian ist Schreibrecht für die Gruppe erlaubt, wenn die Gruppe nur den Besitzer selbst enthält. Üblich sind 600 für die Datei und 700 für `~/.ssh`.

</li>

<li>

Öffentliche Schlüsseldateien und `known_hosts` darf jeder lesen; üblich ist 644. Hier prüft `ssh` nichts, schreiben sollte trotzdem nur der Besitzer dürfen.

</li>

</ul>
:::

Die Abbildung [14](#abb-14) stellt die Dateien mit ihren Rechten zusammen.

:::abbildung linux/k11rechte 14
Die Dateien von SSH und ihre Rechte, als Tabelle mit Ampeln. Zeilen: privater Schlüssel (`rw-------`, grün; daneben `rw-r--r--`, rot: „ssh lädt ihn nicht“); `~/.ssh` (`rwx------`, grün); `authorized_keys` (`rw-------`, grün; daneben `rw-----w-`, rot: „Server verweigert“); `.pub` und `known_hosts` (`rw-r--r--`, grün). Rechts zu jeder roten Zeile ein kleines Bild der Gefahr: ein anderer Benutzer, der den Schlüssel kopiert bzw. eine eigene Zeile in `authorized_keys` schreibt. Darunter: Unter Ubuntu/Debian erlaubt der Server Schreibrecht für die Gruppe, wenn sie nur dich enthält.
:::

:::hintergrund Warum ssh lieber ablehnt
Beide Prüfungen schützen vor dem Fehler, der am leichtesten passiert: einer Datei, die versehentlich zu offene Rechte hat. Darf ein anderer Benutzer deinen privaten Schlüssel lesen, kann er ihn kopieren und sich überall als du anmelden, wo der Schlüssel gilt. Darf er `authorized_keys` beschreiben, braucht er gar nichts von dir: Er hängt seinen eigenen öffentlichen Schlüssel an und meldet sich an deinem Konto an. Dasselbe gelingt ihm, wenn er `~/.ssh` oder dein Heimatverzeichnis beschreiben darf, denn dann kann er die Datei durch eine eigene ersetzen ([Kapitel 7, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/rechte-bei-verzeichnissen.html#stufe-4-4): Löschen und Anlegen ändert das Verzeichnis). Würde `ssh` solche Dateien still benutzen, bliebe der Fehler unsichtbar, bis ihn jemand ausnutzt. Die Handbuchseite von `sshd_config` begründet die Server-Prüfung, die `StrictModes` heißt, genau so: Anfänger lassen ihr Verzeichnis oder ihre Dateien manchmal versehentlich für alle beschreibbar. Ubuntu und Debian machen eine Ausnahme: Schreibrecht für die Gruppe erlauben sie, wenn die Gruppe nur den Besitzer selbst enthält, also die eigene Gruppe, die jeder Benutzer bei der Einrichtung bekommt ([Kapitel 7, Abschnitte 1.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-4) und [2.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/die-rechte-einer-datei.html#stufe-2-3)). Eine Gruppe, in der niemand anderes ist, ist keine Gefahr.
:::

⁠**Kurz gesagt:** `ssh` benutzt keinen privaten Schlüssel, den andere lesen können, und der Server keine `authorized_keys`, die andere ändern können; so fallen zu offene Rechte sofort auf, statt später ausgenutzt zu werden.

### Den privaten Schlüssel mit einer Passphrase schützen

<span class="anker" id="stufe-3-8"></span>

Strenge Rechte schützen den privaten Schlüssel vor anderen Benutzern desselben Rechners, nicht aber vor jemandem, der die Datei auf anderem Weg bekommt: aus einer Sicherungskopie, von einem gestohlenen Laptop oder einem Rechner, den jemand übernommen hat. Dagegen hilft die Passphrase aus Abschnitt [3.2](#stufe-3-2). Mit `ssh-keygen -p` („passphrase“) setzt oder ändert man sie nachträglich. Die Eingaben erscheinen nicht auf dem Bildschirm:

```console
$ ssh-keygen -p -f uebungsschluessel
Key has comment 'student@labor'
Enter new passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved with the new passphrase.
$ ssh -i uebungsschluessel localhost true
Enter passphrase for key 'uebungsschluessel':
$ echo $?
0
```

Nach dem Setzen fragt `ssh` bei jeder Anmeldung nach der Passphrase, entschlüsselt damit den privaten Schlüssel im Arbeitsspeicher und signiert. Wer die Datei ohne Passphrase hat, kann nichts mit ihr anfangen:

```console
$ ssh-keygen -y -f uebungsschluessel
Enter passphrase for "uebungsschluessel":
Load key "uebungsschluessel": incorrect passphrase supplied to decrypt private key
$ echo $?
255
```

`ssh-keygen -y` („yield“) würde aus der privaten Datei den öffentlichen Schlüssel ausgeben; mit einer falschen Passphrase kann es die Datei nicht entschlüsseln.

:::definition Definition 3.7 (Passphrase)
<span class="anker" id="satz-3-7"></span>

Eine __Passphrase__ ist ein Kennwort, mit dem `ssh-keygen` den privaten Schlüssel in seiner Datei verschlüsselt. Ohne sie lässt sich der Schlüssel nicht benutzen. Die Passphrase verlässt den eigenen Rechner nie; der Server erfährt nicht einmal, ob es eine gibt.
:::

Anders als ein Passwort für einen Server kann man eine Passphrase durchprobieren, wenn man die Datei hat, und zwar beliebig oft und ohne dass es jemand bemerkt. `ssh-keygen` macht deshalb jeden einzelnen Versuch absichtlich langsam. Trotzdem sollte die Passphrase lang sein; mehrere Wörter, die nicht als Satz in einem Buch stehen, sind leichter zu merken als ein kurzes Wort mit Sonderzeichen und schwerer zu erraten.

⁠**Kurz gesagt:** Eine Passphrase verschlüsselt den privaten Schlüssel in seiner Datei; wer die Datei stiehlt, braucht zusätzlich die Passphrase.

### Der ssh-agent

<span class="anker" id="stufe-3-9"></span>

Mit Passphrase fragt `ssh` bei jeder Verbindung, und ein Skript, das zehnmal `ssh` aufruft, fragt zehnmal. Bequemer wäre es, die Passphrase einmal am Morgen einzugeben.

:::definition Definition 3.8 (ssh-agent)
<span class="anker" id="satz-3-8"></span>

Der __ssh-agent__ ist ein Programm, das entschlüsselte private Schlüssel im Arbeitsspeicher hält. `ssh-add datei` fragt einmal nach der Passphrase und übergibt dem Agenten den entschlüsselten Schlüssel. Danach lässt `ssh` die Signaturen vom Agenten berechnen, statt nach der Passphrase zu fragen. Den Weg zum Agenten findet `ssh` über die Umgebungsvariable `SSH_AUTH_SOCK`.
:::

Gestartet wird der Agent mit `eval "$(ssh-agent -s)"`. `ssh-agent -s` startet den Agenten im Hintergrund und gibt Befehle aus, die `SSH_AUTH_SOCK` und die Prozessnummer des Agenten in `SSH_AGENT_PID` setzen und exportieren. `eval` ist ein eingebauter Befehl, der seinen Text als Befehlszeile in der laufenden Shell ausführt; so landet die Variable in deiner Shell und wird an `ssh` vererbt ([Kapitel 5, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-5)).

```console
$ eval "$(ssh-agent -s)"
Agent pid 829
$ ssh-add uebungsschluessel
Enter passphrase for uebungsschluessel:
Identity added: uebungsschluessel (student@labor)
$ ssh-add -l
256 SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4 student@labor (ED25519)
$ ssh -i uebungsschluessel localhost true
$ echo $?
0
$ eval "$(ssh-agent -k)"
Agent pid 829 killed
$ ls -A ~/.ssh
agent  authorized_keys  known_hosts  known_hosts.old
```

`ssh-add -l` („list“) zeigt die Schlüssel im Agenten mit ihrem Fingerabdruck. Die Anmeldung danach fragt nicht mehr. `ssh-agent -k` („kill“) beendet den Agenten; mit `eval` entfernt es zugleich die Variablen wieder. Seine Verbindungsstelle, einen Socket, hat der Agent im neuen Unterverzeichnis `~/.ssh/agent` angelegt; so macht es OpenSSH seit Version 10.1, ältere Fassungen legen den Socket unter `/tmp` an. Die Datei `known_hosts.old` ist eine Sicherungskopie, die `ssh` anlegte, als es die übrigen Hostschlüssel des Servers in die Liste schrieb. Abbildung [15](#abb-15) zeigt, wer hier mit wem spricht.

:::abbildung linux/k11agent 15
Der ssh-agent. Links die Datei `uebungsschluessel` mit Schloss (verschlüsselt). `ssh-add` fragt einmal nach der Passphrase (Sprechblase mit Sternchen), öffnet das Schloss und legt den entschlüsselten Schlüssel in einen Kasten „ssh-agent (Arbeitsspeicher)“. Dann drei Aufrufe von `ssh` hintereinander: Jeder schickt eine Bitte „bitte signieren“ an den Agenten (über `SSH_AUTH_SOCK`) und bekommt die Signatur zurück, ohne Frage. Die Datei auf der Platte bleibt verschlossen. Zum Schluss `ssh-agent -k`: Der Kasten leert sich.
:::

Damit die folgenden Übungen nicht bei jedem Befehl fragen, entfernst du die Passphrase vom Übungsschlüssel wieder: Auf die Frage nach der alten Passphrase antwortest du mit ihr, auf die beiden Fragen nach der neuen nur mit der Eingabetaste.

```console
$ ssh-keygen -p -f uebungsschluessel
Enter old passphrase:
Key has comment 'student@labor'
Enter new passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved with the new passphrase.
```

Für einen echten Schlüssel ist die Kombination aus Passphrase und Agent die übliche: Die Datei ist geschützt, und man tippt die Passphrase einmal je Sitzung. Auf vielen Desktop-Systemen startet die Anmeldung einen Agenten von selbst.

⁠**Kurz gesagt:** Der ssh-agent hält entschlüsselte Schlüssel im Speicher; nach einem `ssh-add` mit Passphrase signiert er für jedes `ssh`, ohne erneut zu fragen.

:::aufgabe Aufgabe 8 ★ Welche Datei wohin?
<span class="anker" id="aufg-8"></span>

Anna will sich von ihrem Laptop aus am Server `rechner1` mit einem Schlüssel anmelden. Ordne jede Datei einem der beiden Rechner zu und gib die üblichen Rechte an: `id_ed25519`, `id_ed25519.pub`, `authorized_keys` mit Annas öffentlichem Schlüssel, `known_hosts` mit dem Hostschlüssel von `rechner1`, `ssh_host_ed25519_key`. Welche dieser Dateien darf Anna gefahrlos per E-Mail verschicken?

:::loesung
Auf Annas Laptop: `id_ed25519` (privat, 600), `id_ed25519.pub` (644) und `known_hosts` mit dem Hostschlüssel von `rechner1` (644). Auf `rechner1`: `authorized_keys` in Annas Heimatverzeichnis (600, in `~/.ssh` mit 700) und `ssh_host_ed25519_key` (privater Hostschlüssel, 600, root). Gefahrlos verschicken darf Anna alles Öffentliche: `id_ed25519.pub`, `known_hosts` und `authorized_keys`, denn darin stehen nur öffentliche Schlüssel. Wobei `known_hosts` verrät, mit welchen Rechnern sie arbeitet, wenn die Namen nicht unkenntlich gemacht sind. Die beiden privaten Dateien gibt man nie heraus; den privaten Hostschlüssel hat Anna ohnehin nicht.
:::
:::

:::aufgabe Aufgabe 9 ★★ Ein zweites Schlüsselpaar
<span class="anker" id="aufg-9"></span>

Erzeuge im Übungsverzeichnis ein Schlüsselpaar `zweitschluessel` mit dem Kommentar „Laptop von Anna“ und einer Passphrase. Prüfe die Rechte beider Dateien, zeige Typ und Kommentar aus der `.pub`-Datei an und kontrolliere mit `ssh-keygen -y`, dass die Passphrase gilt. Lösche das Paar danach.

:::loesung
```console
$ ssh-keygen -t ed25519 -f zweitschluessel -C "Laptop von Anna"
Generating public/private ed25519 key pair.
Enter passphrase for "zweitschluessel" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in zweitschluessel
Your public key has been saved in zweitschluessel.pub
The key fingerprint is:
SHA256:KY9s2ZSiVoV0fPIEjBjSnSyRjuOidMfC6XeSvhccG50 Laptop von Anna
The key's randomart image is:
+--[ED25519 256]--+
|  ..oB.=o.       |
|   .=.=o+ o      |
|   o .. o=.      |
|  o .  + E.      |
| ...o = S        |
|...= * %         |
|o.o = * +        |
|.  o = o         |
|    oo=          |
+----[SHA256]-----+
$ ls -l zweitschluessel*
-rw------- 1 student student 464 Nov 13 03:32 zweitschluessel
-rw-r--r-- 1 student student  97 Nov 13 03:32 zweitschluessel.pub
$ cut -d ' ' -f 1,3- zweitschluessel.pub
ssh-ed25519 Laptop von Anna
$ ssh-keygen -y -f zweitschluessel
Enter passphrase for "zweitschluessel":
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJAVbw3esl/Q4q/Y0D/cV8+KWqLgdq1n+IpyruGTsTQv Laptop von Anna
$ rm zweitschluessel zweitschluessel.pub
```

Der Kommentar mit Leerzeichen steht in Anführungszeichen, damit er ein Argument bleibt ([Kapitel 5, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5)). `cut` mit Leerzeichen als Trenner gibt Feld 1 und alles ab Feld 3 aus ([Kapitel 6, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-1)), also Typ und Kommentar ohne den langen Schlüssel. Die private Datei ist mit Passphrase größer (464 statt 399 Bytes), weil sie zusätzlich die Angaben für die Verschlüsselung enthält; die `.pub`-Datei ist zwei Bytes länger, weil der Kommentar 15 statt 13 Zeichen hat. `ssh-keygen -y` gibt nach der richtigen Passphrase den öffentlichen Schlüssel aus.
:::
:::

:::aufgabe Aufgabe 10 ★★ Rechte vorhersagen
<span class="anker" id="aufg-10"></span>

Sage voraus, ob die Anmeldung am Übungsserver gelingt, und prüfe es danach (stelle zwischen den Versuchen den Ausgangszustand wieder her): (a) private Schlüsseldatei mit 640; (b) `~/.ssh` mit 755 und `authorized_keys` mit 644; (c) `authorized_keys` mit 664. Erkläre jedes Ergebnis.

:::loesung
```console
$ chmod 640 uebungsschluessel
$ ssh uebung true
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0640 for '/home/student/linuxk11/uebungsschluessel' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/home/student/linuxk11/uebungsschluessel": bad permissions
student@localhost: Permission denied (publickey).
$ chmod 600 uebungsschluessel
$ chmod 755 ~/.ssh
$ chmod 644 ~/.ssh/authorized_keys
$ ssh uebung 'echo angemeldet'
angemeldet
$ chmod 664 ~/.ssh/authorized_keys
$ ssh uebung 'echo angemeldet'
angemeldet
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
$ ssh uebung 'echo angemeldet'
angemeldet
```

(a) Abgelehnt: Schon ein Leserecht für die Gruppe ist dem Client zu viel, denn wer in der Gruppe ist, könnte den Schlüssel kopieren. (b) Erlaubt: Der Server verlangt nur, dass niemand außer dem Besitzer schreiben darf; lesen dürfen andere `~/.ssh` und `authorized_keys`, denn darin stehen nur öffentliche Schlüssel. Üblich bleiben trotzdem 700 und 600. (c) Erlaubt, aber nur wegen der Ausnahme von Ubuntu und Debian: Die Gruppe `student` enthält nur den Benutzer `student` selbst (Hintergrund in Abschnitt [3.7](#stufe-3-7)). Auf einem System ohne diese Ausnahme, oder wenn die Gruppe weitere Mitglieder hätte, würde der Server ablehnen. Im Text wurde mit `chmod o+w` geprüft, was für andere Benutzer gilt; das lehnt der Server immer ab.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Eine aufgezeichnete Anmeldung
<span class="anker" id="aufg-11"></span>

Angenommen, jemand könnte eine Anmeldung mit Schlüssel vollständig und unverschlüsselt mitschneiden. Erkläre, warum er sich damit trotzdem nicht selbst anmelden kann, und vergleiche mit einer mitgeschnittenen Anmeldung per Passwort. Was müsste er stattdessen erbeuten?

:::loesung
Bei einer Anmeldung mit Schlüssel geht nur eine Signatur über die Leitung, und sie gilt für Daten, die zu genau dieser einen Verbindung gehören. Wer sie aufzeichnet und später vorspielt, hat eine neue Verbindung mit anderen Daten; die alte Signatur passt nicht dazu, und der Server lehnt ab. Den privaten Schlüssel, mit dem man eine neue Signatur berechnen könnte, enthält die Aufzeichnung nicht, und aus dem öffentlichen lässt er sich nicht berechnen. Bei einer Anmeldung per Passwort wandert dagegen das Passwort selbst zum Server (in SSH verschlüsselt, im angenommenen Mitschnitt also lesbar); wer es hat, kann sich beliebig oft anmelden, auch an anderen Diensten, falls es dort ebenfalls benutzt wird. Für eine Anmeldung mit Schlüssel müsste ein Angreifer stattdessen die private Schlüsseldatei erbeuten und, falls sie geschützt ist, auch die Passphrase.
:::
:::
