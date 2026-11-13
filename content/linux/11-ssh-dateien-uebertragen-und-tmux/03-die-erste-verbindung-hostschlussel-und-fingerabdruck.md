---
title: Die erste Verbindung: Hostschlüssel und Fingerabdruck
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160300
summary: Bevor du dem Server etwas anvertraust, muss er beweisen, dass er der richtige ist.
tags: Hostschlüssel, Fingerabdruck, trust on first use
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bevor du dem Server etwas anvertraust, muss er beweisen, dass er der richtige ist. Dieser Abschnitt erklärt, womit er das tut, was der Fingerabdruck ist, nach dem `ssh` bei der ersten Verbindung fragt, und was eine Warnung bei einer späteren Verbindung bedeutet.
:::

:::::vorwissen Was du dafür brauchst: Prüfsumme, Schlüsselpaar und Signatur

<span class="anker" id="stufe-2-1"></span>

Drei Werkzeuge aus früheren Kapiteln tragen diesen Abschnitt.

<ul>

<li>

Eine *Prüfsumme* ist eine kurze Zahl, die ein Programm aus dem ganzen Inhalt einer Datei berechnet. Beim Verfahren SHA-256 ist sie 256 Bit lang. Ändert sich auch nur ein Byte, kommt eine völlig andere Prüfsumme heraus, und zwei verschiedene Inhalte mit gleicher Prüfsumme zu finden ist nach heutigem Wissen praktisch unmöglich ([Kapitel 1, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-5)).

</li>

<li>

Ein *Schlüsselpaar* besteht aus einem geheimen Schlüssel, den nur sein Besitzer hat, und einem öffentlichen, den jeder haben darf; aus dem öffentlichen lässt sich der geheime praktisch nicht berechnen ([Kapitel 9, Abschnitt 7.4](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/warum-man-den-paketen-trauen-kann.html#stufe-7-4)).

</li>

<li>

Eine *digitale Signatur* berechnet ein Programm aus einem Inhalt und dem geheimen Schlüssel. Jeder, der den öffentlichen Schlüssel hat, kann prüfen, dass sie zu genau diesem Inhalt gehört und mit dem geheimen Schlüssel erzeugt wurde; herstellen kann sie nur der Besitzer des geheimen Schlüssels ([Kapitel 9, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/warum-man-den-paketen-trauen-kann.html#stufe-7-5)).

</li>

</ul>

Bei SSH heißt der geheime Schlüssel meist *privater Schlüssel*, und so nennt ihn auch `ssh` in seinen Meldungen (*private key*). Beide Wörter meinen dasselbe; dieses Kapitel sagt von hier an „privater Schlüssel“.

::::beispiel Wer was prüfen kann
Ubuntu signiert seine Paketlisten mit dem geheimen Archivschlüssel, und jeder Ubuntu-Rechner prüft die Signatur mit dem öffentlichen Archivschlüssel, der bei der Installation mitkam ([Kapitel 9, Abschnitt 7.6](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/warum-man-den-paketen-trauen-kann.html#stufe-7-6)). Fälschen könnte die Signatur nur, wer den geheimen Schlüssel hat. Genau dieselbe Rollenverteilung kommt in diesem Abschnitt wieder, nur dass jetzt ein SSH-Server den geheimen Schlüssel besitzt.
::::

⁠**Kurz gesagt:** Eine Prüfsumme erkennt jede Änderung, eine Signatur beweist zusätzlich, dass der Besitzer eines privaten Schlüssels sie erzeugt hat; prüfen kann sie jeder mit dem öffentlichen Schlüssel.

:::::

### Der Hostschlüssel

<span class="anker" id="stufe-2-2"></span>

Wenn `ssh` eine Verbindung zu `localhost` oder zu `rechner1` aufbaut, woher weiß es, dass am anderen Ende wirklich dieser Rechner antwortet? Namen und Adressen lassen sich umleiten, zum Beispiel von einem WLAN, das jemand mit böser Absicht betreibt. Der Server braucht etwas, das nur er besitzt und das er trotzdem vorzeigen kann, ohne es herzugeben.

Ein Bild zur Orientierung: der Siegelring aus [Kapitel 9](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/software-installieren-paketverwaltung.html). Der Server drückt bei jeder Verbindung sein Siegel auf eine Nachricht, und der Client vergleicht das Wappen mit einem Musterabdruck, den er kennt.

:::definition Definition 2.1 (Hostschlüssel)
<span class="anker" id="satz-2-1"></span>

Der __Hostschlüssel__ eines SSH-Servers ist ein Schlüsselpaar, das zu diesem Rechner gehört. Der private Hostschlüssel liegt in `/etc/ssh/ssh_host_`*typ*`_key` und ist nur für root lesbar, der öffentliche in derselben Datei mit der Endung `.pub`. Bei jeder Verbindung signiert der Server mit dem privaten Hostschlüssel Daten, die zu genau dieser Verbindung gehören, und der Client prüft die Signatur mit dem öffentlichen Hostschlüssel.
:::

Weil die signierten Daten bei jeder Verbindung andere sind, nützt es einem Angreifer nichts, eine alte Signatur aufzuzeichnen und später vorzuspielen. Wie die Signatur im Einzelnen in den Aufbau der verschlüsselten Verbindung eingebaut ist, ist Stoff der Reihe Cybersecurity. Dein Übungsserver hat seine Hostschlüssel bei der Installation erzeugt, gleich drei Paare:

```console
$ ls -l /etc/ssh/ssh_host_*
-rw------- 1 root root  505 Nov 13 03:06 /etc/ssh/ssh_host_ecdsa_key
-rw-r--r-- 1 root root  172 Nov 13 03:06 /etc/ssh/ssh_host_ecdsa_key.pub
-rw------- 1 root root  399 Nov 13 03:06 /etc/ssh/ssh_host_ed25519_key
-rw-r--r-- 1 root root   92 Nov 13 03:06 /etc/ssh/ssh_host_ed25519_key.pub
-rw------- 1 root root 2590 Nov 13 03:06 /etc/ssh/ssh_host_rsa_key
-rw-r--r-- 1 root root  564 Nov 13 03:06 /etc/ssh/ssh_host_rsa_key.pub
```

Die drei Typen gehören zu drei Signaturverfahren: RSA ist das älteste und am weitesten verbreitet, ECDSA und Ed25519 sind neuer und kommen mit viel kürzeren Schlüsseln aus. Der Server hat alle drei, damit auch ältere Clients etwas finden, das sie verstehen; ein heutiger Client nimmt Ed25519. Die Rechte folgen [Kapitel 7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-gruppen-und-rechte.html): Die privaten Schlüssel haben 600 und gehören root, die öffentlichen haben 644. Abbildung [6](#abb-6) zeigt, wie der Server sich damit ausweist.

:::abbildung linux/k11hostschluessel 6
Der Server weist sich aus. Rechts der Server mit Tresor: darin der private Hostschlüssel (Datei `ssh_host_ed25519_key`, Schloss, `rw-------`, root); daneben der öffentliche (`.pub`). Links der Client mit einem Karteikasten „bekannte Rechner“. Ablauf: (1) Client und Server einigen sich auf Daten, die nur für diese Verbindung gelten (Kärtchen mit wechselnder Nummer). (2) Der Server signiert das Kärtchen mit dem privaten Hostschlüssel (Siegel erscheint) und schickt es mit dem öffentlichen Hostschlüssel zum Client. (3) Der Client prüft das Siegel mit dem öffentlichen Schlüssel (Haken) und vergleicht den öffentlichen Schlüssel mit dem Eintrag im Karteikasten. Der private Schlüssel verlässt den Tresor nie.
:::

⁠**Kurz gesagt:** Der Hostschlüssel ist das Schlüsselpaar des Servers; mit dem privaten Teil signiert er jede Verbindung, mit dem öffentlichen prüft der Client.

### Der Fingerabdruck

<span class="anker" id="stufe-2-3"></span>

Ein öffentlicher Schlüssel ist eine lange Zeichenkette; beim Typ Ed25519 sind es 68 Zeichen, bei RSA über 500. Solche Ketten vergleicht niemand gern von Auge. Deshalb vergleicht man eine kurze Prüfsumme des Schlüssels, so wie die lange Hexadezimalzahl, an der man in [Kapitel 9, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/warum-man-den-paketen-trauen-kann.html#stufe-7-5) den Archivschlüssel erkannte.

:::definition Definition 2.2 (Fingerabdruck)
<span class="anker" id="satz-2-2"></span>

Der __Fingerabdruck__ eines öffentlichen Schlüssels ist seine Prüfsumme. OpenSSH berechnet sie mit SHA-256 und schreibt sie in der Base64-Schreibweise mit der Vorsilbe `SHA256:`, also als 43 Zeichen aus Buchstaben, Ziffern, `+` und `/`.
:::

Die *Base64-Schreibweise* stellt Bytes mit 64 verschiedenen Zeichen dar: den 26 Großbuchstaben, den 26 Kleinbuchstaben, den 10 Ziffern und den Zeichen `+` und `/`. Jedes Zeichen steht für 6 Bit, denn $2^6=64$. Eine Prüfsumme von 256 Bit braucht damit $256/6\approx 42{,}7$, also 43 Zeichen: 42 Zeichen tragen 252 Bit, das letzte trägt die übrigen 4, aufgefüllt mit zwei Null-Bits. Das gewöhnliche Base64 hängt außerdem ein Füllzeichen `=` an, damit die Zahl der Zeichen durch 4 teilbar ist; OpenSSH lässt es weg. Das ist kürzer als die 64 Hexadezimalziffern, mit denen `sha256sum` dieselbe Zahl schreiben würde ([Kapitel 1, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-5)), weil eine Hexadezimalziffer nur 4 Bit trägt.

Berechnet wird die Prüfsumme über die Bytes des Schlüssels selbst. In der `.pub`-Datei stehen sie in Base64; die 68 Zeichen eines Ed25519-Schlüssels stehen für $68\cdot 6/8=51$ Bytes. Über diese 51 Bytes rechnet OpenSSH SHA-256, nicht über die ganze Textzeile; `sha256sum` über die Datei liefert deshalb einen anderen Wert.

::::beispiel Der Fingerabdruck des Übungsservers
`ssh-keygen -l -f datei` zeigt den Fingerabdruck des öffentlichen Schlüssels in einer Datei (`-l` für „list“):

```console
$ ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pub
256 SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw root@labor (ED25519)
```

Die Zeile nennt die Länge des Schlüssels in Bit (256), den Fingerabdruck, einen Kommentar (hier `root@labor`, wer den Schlüssel auf welchem Rechner erzeugt hat) und den Typ. Derselbe Fingerabdruck stand schon in der Ausgabe der Installation in Abschnitt [1.5](entfernte-anmeldung-client-server-und-ein-ubungsserver.html#stufe-1-5).
::::

:::abbildung linux/k11fingerabdruck 7
Vom Schlüssel zum Fingerabdruck. Oben die Zeile aus `ssh_host_ed25519_key.pub` (`ssh-ed25519 AAAAC3Nza…`, 68 Zeichen Schlüssel). Die 68 Base64-Zeichen werden zu 51 Bytes. Ein Trichter „SHA-256“ macht daraus 32 Bytes (256 Bit, als Reihe von Kästchen). Die Kästchen werden in Sechsergruppen von Bits zerlegt; jede Gruppe wird zu einem Zeichen, die letzte Gruppe hat nur 4 Bit und zwei Null-Bits. Unten entsteht der Fingerabdruck aus dem Text, `SHA256:wNZ8…Ynw`, Zähler „43 Zeichen“, daneben ein durchgestrichenes `=`. Am Rand eine kleine Tabelle: `A`–`Z` = 0–25, `a`–`z` = 26–51, `0`–`9` = 52–61, `+` = 62, `/` = 63.
:::

:::hintergrund Warum ältere Anleitungen Doppelpunkte zeigen
In älteren Büchern und Anleitungen sieht ein Fingerabdruck anders aus, etwa `2e:37:27:7a:…`: 16 Bytes als Hexadezimalzahlen mit Doppelpunkten dazwischen. Das ist eine Prüfsumme nach dem älteren Verfahren MD5. Seit OpenSSH 6.8 aus dem Jahr 2015 zeigt `ssh` SHA-256, weil MD5 nicht mehr als sicher gilt: Man kann inzwischen gezielt zwei verschiedene Inhalte mit gleicher MD5-Prüfsumme erzeugen. Die alte Form gibt es weiter, wenn man sie ausdrücklich verlangt (Aufgabe [6](#aufg-6)); vergleichen kann man nur Fingerabdrücke, die mit demselben Verfahren berechnet wurden.
:::

⁠**Kurz gesagt:** Der Fingerabdruck ist die SHA-256-Prüfsumme eines öffentlichen Schlüssels in 43 Base64-Zeichen; an ihm erkennt man einen Schlüssel.

### Die erste Verbindung

<span class="anker" id="stufe-2-4"></span>

Jetzt verbindest du dich zum ersten Mal mit deinem Übungsserver. `ssh localhost` meldet dich unter deinem eigenen Benutzernamen an `localhost` an:

```console
$ ssh localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is: SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
student@localhost: Permission denied (publickey).
$ echo $?
255
```

Zeile für Zeile: `ssh` kann die Echtheit des Rechners nicht feststellen, weil es seinen Hostschlüssel noch nie gesehen hat. Es zeigt den Fingerabdruck, den der Server geschickt hat, und fragt, ob du weitermachen willst. Ein Vergleich mit dem Beispiel in Abschnitt [2.3](#stufe-2-3) zeigt: Es ist derselbe Fingerabdruck wie der des Hostschlüssels in `/etc/ssh`. Also antwortest du mit `yes`, und `ssh` merkt sich den Schlüssel dauerhaft. Abbildung [8](#abb-8) zeigt den Vergleich.

:::abbildung linux/k11ersteverbindung 8
Terminalbild (dunkel, wie Ubuntu, Prompt `student@labor:~/linuxk11$`): oben der Aufruf `ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pub` mit der Zeile `256 SHA256:wNZ8…Ynw root@labor (ED25519)` aus dem Text, darunter `ssh localhost` mit der Frage aus dem Text bis `(yes/no/[fingerprint])?`. Die beiden Fingerabdrücke werden Zeichen für Zeichen mit einem Lineal verglichen und grün markiert; dann erscheint `yes` und die Zeile `Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.`, zuletzt `Permission denied (publickey).`
:::

Danach scheitert die Anmeldung trotzdem: `Permission denied (publickey)`. Der Server hat sich ausgewiesen, du dich aber noch nicht. Passwörter hast du auf dem Übungsserver verboten, und einen Schlüssel hast du noch nicht; in Klammern nennt der Server die Verfahren, die er noch anbietet, hier nur `publickey`. Der Exit-Status 255 ist die Zahl, mit der `ssh` meldet, dass die Verbindung oder die Anmeldung selbst gescheitert ist.

:::definition Definition 2.3 (Vertrauen bei der ersten Verbindung)
<span class="anker" id="satz-2-3"></span>

Kennt der Client den Hostschlüssel eines Servers noch nicht, zeigt er dessen Fingerabdruck und fragt den Benutzer. Bestätigt der Benutzer, speichert der Client den öffentlichen Hostschlüssel und verlangt bei jeder späteren Verbindung, dass der Server sich mit genau diesem Schlüssel ausweist. Dieses Verfahren heißt „Vertrauen bei der ersten Verbindung“, englisch __trust on first use__, kurz TOFU.
:::

Die Frage ist also keine Formalität. Bevor du `yes` tippst, vergleichst du den angezeigten Fingerabdruck mit einem, den du auf einem anderen Weg bekommen hast. Bei deinem eigenen Server liest du ihn mit `ssh-keygen -l` selbst ab. Bei einem fremden Server bekommst du ihn von der Person, die ihn betreut, oder von einer Webseite des Betreibers; viele Hochschulen und Anbieter veröffentlichen die Fingerabdrücke ihrer Server. Statt `yes` darf man auch den erwarteten Fingerabdruck einfügen; dann vergleicht `ssh` selbst Zeichen für Zeichen (`[fingerprint]` in der Frage, Aufgabe [7](#aufg-7)).

Nebenbei zeigt die erste Verbindung die Socket-Aktivierung aus Abschnitt [1.6](entfernte-anmeldung-client-server-und-ein-ubungsserver.html#stufe-1-6) bei der Arbeit. systemd hat beim ersten Anruf `sshd` gestartet, und der Dienst läuft seitdem:

```console
$ systemctl is-active ssh.service
active
```

:::hintergrund Warum es gerade auf die erste Verbindung ankommt
Angenommen, jemand sitzt zwischen dir und dem Server, etwa weil er das WLAN betreibt, in dem du gerade bist. Er fängt deine Verbindung ab und antwortet selbst, mit einem Hostschlüssel, den er sich erzeugt hat. Die Signaturprüfung besteht er mühelos, denn er signiert mit seinem eigenen privaten Schlüssel, und der Client prüft mit dem öffentlichen Schlüssel, den er mitschickt. Zugleich baut er eine zweite Verbindung zum echten Server auf und reicht alles hin und her. Diesen Angriff nennt man *Man-in-the-Middle-Angriff*, englisch für „Mann in der Mitte“. Meldest du dich bei ihm mit einem Passwort an, hat er es, und alles, was du tippst, liest er mit. Das Einzige, was ihn verrät, ist der falsche Fingerabdruck bei der ersten Verbindung. Hast du den Schlüssel des echten Servers einmal gespeichert, fällt jeder spätere Versuch auf, denn dann passt der Schlüssel nicht mehr zum gespeicherten Eintrag. Der ganze Schutz hängt deshalb an dem einen Augenblick, in dem man `yes` tippt. Das Verfahren ist ein Kompromiss: Ein Client, der vor dem ersten Kontakt schon alle Schlüssel kennen müsste, wäre sicherer, aber kaum zu benutzen. Wie Webbrowser dieses Problem mit Zertifikaten lösen, gehört in die Reihe Cybersecurity.
:::

⁠**Kurz gesagt:** Bei der ersten Verbindung zeigt `ssh` den Fingerabdruck des Hostschlüssels; erst nach einem Vergleich auf anderem Weg bestätigt man, und von da an verlangt `ssh` bei jeder Verbindung denselben Schlüssel.

### Die Liste der bekannten Rechner: known_hosts

<span class="anker" id="stufe-2-5"></span>

Mit `yes` hat `ssh` den Hostschlüssel gespeichert. Die Liste liegt in einem versteckten Verzeichnis `.ssh` in deinem Heimatverzeichnis, das `ssh` bei Bedarf selbst anlegt.

:::definition Definition 2.4 (known_hosts)
<span class="anker" id="satz-2-4"></span>

Die Datei __`~/.ssh/known_hosts`__ enthält für jeden Rechner, dessen Hostschlüssel der Benutzer bestätigt hat, eine Zeile: den Namen des Rechners, den Typ des Schlüssels und den öffentlichen Hostschlüssel in Base64. Bei jeder Verbindung sucht `ssh` dort den Eintrag zum Rechnernamen und vergleicht.
:::

::::beispiel Der Eintrag für localhost
```console
$ ls -la ~/.ssh
total 12
drwx------  2 student student 4096 Nov 13 03:18 .
drwxr-x--- 16 student student 4096 Nov 13 03:18 ..
-rw-r--r--  1 student student  142 Nov 13 03:18 known_hosts
$ cat ~/.ssh/known_hosts
|1|plxWO27Yo4dtbmZo0bgV0WfLaHo=|1dCnqs8a0nMi7VhJCi3Ks3idVhg= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAo/cgLpIheFYzbh2ILLxezHxP0EQX6fpHHVx64eG9nE
$ ssh-keygen -F localhost
```

```text
# Host localhost found: line 1
|1|plxWO27Yo4dtbmZo0bgV0WfLaHo=|1dCnqs8a0nMi7VhJCi3Ks3idVhg= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAo/cgLpIheFYzbh2ILLxezHxP0EQX6fpHHVx64eG9nE
```

Das Verzeichnis `.ssh` hat die Rechte 700, nur du darfst hinein. Die Zeile hat drei Teile, durch Leerzeichen getrennt. Vorne steht nicht `localhost`, sondern eine unkenntlich gemachte Form des Namens, die mit `|1|` beginnt; dann der Typ `ssh-ed25519` und der öffentliche Hostschlüssel, dieselben 68 Zeichen wie in `/etc/ssh/ssh_host_ed25519_key.pub` auf dem Server. Weil man den Namen nicht mehr lesen kann, sucht man einen Eintrag mit `ssh-keygen -F name` („find“).
::::

Die unkenntliche Form kommt von einer Einstellung, die Ubuntu und Debian für alle Benutzer in `/etc/ssh/ssh_config` setzen: `HashKnownHosts yes`. Zwischen den senkrechten Strichen stehen eine Zufallszahl und eine Prüfsumme aus dieser Zufallszahl und dem Namen. `ssh` kann prüfen, ob ein gegebener Name passt, indem es die Prüfsumme nachrechnet; aus der Zeile allein lässt sich der Name nicht ablesen. Abbildung [9](#abb-9) zerlegt die Zeile.

:::abbildung linux/k11knownhosts 9
Dateiansicht (hell) von `~/.ssh/known_hosts` mit der einen Zeile aus dem Text. Darunter ihre drei Teile auf eigenen Zeilen, mit Klammern: über `|1|plxWO…=|1dCnq…=` „Zufallszahl“ und „Prüfsumme aus Zufallszahl und Name“, darunter zusammen „unkenntlicher Name“; „Typ“ über `ssh-ed25519`; „öffentlicher Hostschlüssel“ über `AAAAC3Nza…`. Darunter eine kleine Maschine: Eingabe `localhost` + Zufallszahl → Prüfsumme → Vergleich mit der Datei → Haken; Eingabe `rechner1` → anderes Ergebnis → kein Treffer.
:::

Bei der zweiten Verbindung fragt `ssh` nicht mehr, denn der Schlüssel steht in der Liste und passt. Die Anmeldung scheitert noch aus demselben Grund wie zuvor:

```console
$ ssh localhost
student@localhost: Permission denied (publickey).
$ echo $?
255
```

:::hintergrund Warum die Namen unkenntlich sind
Die Liste verrät, mit welchen Rechnern jemand arbeitet. Gelingt es einem Angreifer, ein Benutzerkonto zu übernehmen, wäre eine lesbare `known_hosts` für ihn ein Wegweiser zu den nächsten Rechnern, auf denen er es versuchen kann. Mit unkenntlichen Namen kann er nur noch prüfen, ob ein Name, den er ohnehin vermutet, darin steht. Genauer ist die Zufallszahl 20 Bytes lang, ein sogenanntes *Salz*, und die Prüfsumme entsteht mit dem Verfahren HMAC-SHA1, das aus dem Salz und dem Namen 20 Bytes berechnet; in Base64 sind beide je 28 Zeichen lang. Weil jede Zeile ihr eigenes Salz hat, sieht derselbe Name in jeder Zeile und in jeder Datei anders aus, und ein Angreifer muss jeden vermuteten Namen für jede Zeile einzeln durchrechnen. Vor dem Raten schützt das nur begrenzt: Alle Adressen eines kleinen Netzes durchzuprobieren, dauert für einen Rechner nur einen Augenblick. Der Preis: Auch du selbst kannst die Datei nicht mehr einfach lesen und musst zum Suchen und Löschen `ssh-keygen` benutzen. Andere Distributionen lassen die Einstellung aus; dort steht der Name im Klartext vorn in der Zeile.
:::

⁠**Kurz gesagt:** In `~/.ssh/known_hosts` stehen die bestätigten Hostschlüssel; unter Ubuntu mit unkenntlichen Namen, die man mit `ssh-keygen -F` sucht.

### Wenn sich der Hostschlüssel ändert

<span class="anker" id="stufe-2-6"></span>

Was geschieht, wenn ein Server sich bei einer späteren Verbindung mit einem anderen Hostschlüssel meldet als dem gespeicherten? Das lässt sich gefahrlos nachstellen, ohne den Server zu verändern: mit einer eigenen, absichtlich falschen Liste. Die Option `-o Name=Wert` setzt für einen einzelnen Aufruf eine beliebige Einstellung des Clients; `UserKnownHostsFile` nennt die Datei mit der Liste. Zuerst erzeugst du mit `ssh-keygen` ein beliebiges fremdes Schlüsselpaar in den Dateien `fremd` und `fremd.pub`; die Optionen `-N ""` und `-q` lassen das Programm ohne Rückfragen und ohne Meldungen arbeiten. Dann schreibst du dessen öffentlichen Schlüssel als angeblichen Schlüssel von `localhost` in die Datei `falsch_known_hosts`:

```console
$ ssh-keygen -t ed25519 -f fremd -N "" -q
$ echo "localhost $(cut -d ' ' -f 1,2 fremd.pub)" > falsch_known_hosts
$ ssh -o UserKnownHostsFile=falsch_known_hosts localhost
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw.
Please contact your system administrator.
Add correct host key in falsch_known_hosts to get rid of this message.
Offending ED25519 key in falsch_known_hosts:1
  remove with:
  ssh-keygen -f 'falsch_known_hosts' -R 'localhost'
Host key for localhost has changed and you have requested strict checking.
Host key verification failed.
$ echo $?
255
```

Die Warnung ist bewusst laut. Sie sagt: Der Server hat einen anderen Schlüssel geschickt als den, der in der Liste steht (Zeile 1 der Datei, `Offending ... key`). Vielleicht hört jemand mit (*man-in-the-middle attack*), vielleicht wurde der Schlüssel aber auch nur ausgetauscht. `ssh` bricht ab, bevor es sich anmeldet: Weder ein Passwort noch sonst etwas, das dich ausweist, geht an die Gegenseite. Der Exit-Status ist 255.

:::satz Satz 2.5 (Ein geänderter Hostschlüssel)
<span class="anker" id="satz-2-5"></span>

Passt der Hostschlüssel, den ein Server schickt, nicht zum gespeicherten Eintrag, verweigert `ssh` in der Voreinstellung die Verbindung. Es gibt zwei mögliche Ursachen: Jemand schaltet sich dazwischen, oder der Server hat einen neuen Schlüssel bekommen, etwa weil er neu installiert wurde. Welche zutrifft, lässt sich nur auf einem anderen Weg klären.
:::

Die harmlose Ursache ist die häufigere; ein Server, dessen Betriebssystem neu installiert wurde, erzeugt bei der Installation neue Hostschlüssel. Trotzdem gilt: erst fragen, dann löschen. Hat die Person, die den Server betreut, den neuen Fingerabdruck bestätigt, entfernst du den alten Eintrag mit `ssh-keygen -R name` („remove“) und verbindest dich neu, wobei du den neuen Fingerabdruck wie bei einer ersten Verbindung prüfst. Mit `-f` arbeitet `ssh-keygen` an einer anderen Datei als `~/.ssh/known_hosts`, hier an der Übungsliste:

```console
$ ssh-keygen -f falsch_known_hosts -R localhost
```

```text
# Host localhost found: line 1
falsch_known_hosts updated.
Original contents retained as falsch_known_hosts.old
```

```console
$ ls falsch_known_hosts*
falsch_known_hosts  falsch_known_hosts.old
```

`ssh-keygen` hebt die alte Fassung als `.old` auf. Die Übungsdateien brauchst du danach nicht mehr; lösche sie mit `rm fremd fremd.pub falsch_known_hosts*`. Abbildung [10](#abb-10) fasst die Entscheidung zusammen.

:::abbildung linux/k11warnung 10
Terminalbild (dunkel, wie Ubuntu): die Warnung aus `ssh -o UserKnownHostsFile=falsch_known_hosts localhost` mit dem Kasten aus `@`-Zeichen, darunter `Host key verification failed.` Darunter ein Ablaufschema: „Fingerabdruck geändert“ → zwei Pfeile: „Server neu installiert?“ (grün, nach Bestätigung durch den Betreuer: `ssh-keygen -R`, neu verbinden, neuen Fingerabdruck prüfen) und „unbekannt“ (rot: nicht verbinden, nachfragen).
:::

:::warnung Die Warnung nie einfach wegräumen
Den alten Eintrag zu löschen und beim nächsten Versuch `yes` zu tippen, ohne nachzufragen, ist genau das, was sich jemand wünscht, der sich dazwischenschaltet: Du würdest seinen Schlüssel als echt speichern. Auf Übungsplattformen, die ihre Server gelegentlich neu aufsetzen, steht der neue Fingerabdruck meist auf der Webseite; vergleiche ihn, bevor du bestätigst.
:::

⁠**Kurz gesagt:** Ein geänderter Hostschlüssel lässt `ssh` abbrechen; den alten Eintrag entfernt man mit `ssh-keygen -R` erst, wenn auf anderem Weg geklärt ist, dass der neue Schlüssel echt ist.

:::aufgabe Aufgabe 4 ★ Alle drei Fingerabdrücke
<span class="anker" id="aufg-4"></span>

Zeige mit `ssh-keygen -l -f` die Fingerabdrücke aller drei öffentlichen Hostschlüssel deines Übungsservers. Vergleiche sie mit den Zeilen, die bei der Installation erschienen sind. Warum zeigte `ssh` bei der ersten Verbindung nur einen davon?

:::loesung
```console
$ ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub
3072 SHA256:thkYzoobvxKHDY9kDns2MuqB1KOmZOdJ3d9c5f/KTD0 root@labor (RSA)
$ ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub
256 SHA256:RClt9obROtQy/l0z77CeHnNCom2A5tzJTEIpgT0Lt+0 root@labor (ECDSA)
$ ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pub
256 SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw root@labor (ED25519)
```

Alle drei stimmen mit den Zeilen `Creating SSH2 … key` der Installation überein. Bei der ersten Verbindung zeigte `ssh` nur den Ed25519-Schlüssel, weil sich Client und Server auf ein einziges Signaturverfahren einigen; ein heutiger Client bevorzugt Ed25519. Die beiden anderen Schlüssel hat der Server erst nach der erfolgreichen Anmeldung mitgeteilt (Abschnitt [3.6](anmelden-mit-einem-schlusselpaar.html#stufe-3-6)).
:::
:::

:::aufgabe Aufgabe 5 ★★ Was tun?
<span class="anker" id="aufg-5"></span>

Entscheide in jedem Fall, ob du `yes` tippst, und begründe:

<ol>

<li>

Du verbindest dich zum ersten Mal mit dem Rechenserver deiner Hochschule. Der Fingerabdruck in der Frage stimmt mit dem auf der Webseite des Rechenzentrums überein.

</li>

<li>

Wie in 1, aber du bist im WLAN eines Cafés, und die Webseite hast du noch nicht angesehen.

</li>

<li>

Seit Monaten meldest du dich ohne Frage an einem Server an. Heute erscheint die Warnung `REMOTE HOST IDENTIFICATION HAS CHANGED`. Eine Rundmail kündigte gestern an, dass der Server neu installiert wurde, und nannte den neuen Fingerabdruck; er stimmt mit dem in der Warnung überein.

</li>

<li>

Wie in 3, aber es gab keine Ankündigung.

</li>

</ol>

:::loesung
<ol>

<li>

`yes`: Der Fingerabdruck stimmt mit einem überein, den du auf einem anderen Weg bekommen hast. Am besten fügt man ihn gleich statt `yes` ein (Aufgabe [7](#aufg-7)).

</li>

<li>

Nicht bestätigen, bevor du die Webseite geöffnet und verglichen hast. Gerade in einem fremden WLAN könnte jemand dazwischensitzen. Die Webseite des Rechenzentrums ruft man über eine verschlüsselte Verbindung auf, deren Echtheit der Browser prüft; auch im Café ist sie deshalb ein brauchbarer zweiter Weg.

</li>

<li>

Den alten Eintrag mit `ssh-keygen -R rechnername` entfernen und neu verbinden, dabei den neuen Fingerabdruck wieder mit dem aus der Rundmail vergleichen. Ankündigung, Zeitpunkt und Fingerabdruck passen zusammen.

</li>

<li>

Nicht verbinden und die Person fragen, die den Server betreut. Ohne Erklärung ist ein geänderter Schlüssel genau das, wovor die Warnung schützen soll.

</li>

</ol>
:::
:::

:::aufgabe Aufgabe 6 ★★ Wie lang ist ein Fingerabdruck?
<span class="anker" id="aufg-6"></span>

(a) Wie viele Base64-Zeichen bräuchte ein Fingerabdruck, wenn er mit SHA-512 (512 Bit) berechnet würde? (b) Ein MD5-Fingerabdruck hat 128 Bit. Wie viele Zeichen hat er, wenn er als Hexadezimalziffern mit einem Doppelpunkt nach jedem Byte geschrieben wird? (c) Prüfe (b) mit `ssh-keygen -l -E md5 -f /etc/ssh/ssh_host_ed25519_key.pub`.

:::loesung
(a) $512/6\approx85{,}3$, also 86 Zeichen. (b) 128 Bit sind 16 Bytes, jedes Byte zwei Hexadezimalziffern: 32 Ziffern, dazu 15 Doppelpunkte zwischen den 16 Paaren, zusammen 47 Zeichen. (c) `-E md5` wählt das Verfahren:

```console
$ ssh-keygen -l -E md5 -f /etc/ssh/ssh_host_ed25519_key.pub
256 MD5:2e:37:27:7a:56:82:45:2b:62:63:b3:8f:e5:c6:bb:9f root@labor (ED25519)
```

Hinter `MD5:` stehen 16 Paare und 15 Doppelpunkte, 47 Zeichen. Derselbe Schlüssel hat also zwei ganz verschieden aussehende Fingerabdrücke; vergleichen kann man nur gleichartige.
:::
:::

:::aufgabe Aufgabe 7 ★★★ Fingerabdruck statt yes
<span class="anker" id="aufg-7"></span>

Verbinde dich mit `ssh -o UserKnownHostsFile=probe_known_hosts localhost` so mit dem Übungsserver, als wäre es das erste Mal. Antworte auf die Frage nicht mit `yes`, sondern füge den Fingerabdruck ein, den du mit `ssh-keygen -l` vom Hostschlüssel abgelesen hast. Was meldet `ssh`? Was würde geschehen, wenn du dich beim Abschreiben um ein Zeichen vertippst? Lösche danach `probe_known_hosts`.

:::loesung
Mit der eigenen, leeren Liste kennt `ssh` den Server nicht und fragt. Fügt man den richtigen Fingerabdruck ein, vergleicht `ssh` selbst und nimmt den Schlüssel in die Liste auf; die Anmeldung scheitert danach wie in Abschnitt [2.4](#stufe-2-4), weil noch kein Schlüssel genannt ist. Bei einem Tippfehler (hier ein `X` statt `w` am Ende) fragt `ssh` erneut, und mit `no` bricht man ab:

```console
$ ssh -o UserKnownHostsFile=probe_known_hosts localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is: SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
student@localhost: Permission denied (publickey).
$ echo $?
255
$ wc -l probe_known_hosts
1 probe_known_hosts
$ rm probe_known_hosts
$ ssh -o UserKnownHostsFile=probe_known_hosts localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is: SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnX
Please type 'yes', 'no' or the fingerprint:no
Host key verification failed.
$ echo $?
255
$ ls probe_known_hosts
ls: cannot access 'probe_known_hosts': No such file or directory
```

Ein falscher Fingerabdruck wird nicht als „ja“ gewertet, und die Liste bleibt leer. Der Vorteil gegenüber `yes`: Das Vergleichen übernimmt das Programm, das sich nicht verliest.
:::
:::
