---
title: Warum man den Paketen trauen kann
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140800
summary: apt lädt Pakete von Spiegelservern, die fremden Leuten gehören, über unverschlüsselte Verbindungen, und installiert sie dann mit den Rechten von root .
tags: Release-Datei, Schlüsselpaar, digitale Signatur, Schlüsselbund
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
`apt` lädt Pakete von Spiegelservern, die fremden Leuten gehören, über unverschlüsselte Verbindungen, und installiert sie dann mit den Rechten von `root`. Dieser Abschnitt zeigt die Kette von Prüfungen, die das trotzdem sicher macht, und prüft sie Glied für Glied von Hand nach.
:::

:::::vorwissen Was du dafür brauchst: die Prüfsumme

<span class="anker" id="stufe-7-1"></span>

[Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hat die Prüfsumme eingeführt, um ein heruntergeladenes Abbild zu prüfen ([Kapitel 1, Abschnitte 5.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-5) bis 5.7). Das Wichtigste daraus:

<ul>

<li>

Eine Prüfsumme nach dem Verfahren SHA-256 ist eine Zahl aus 256 Bit, geschrieben als 64 Hexadezimalziffern, die aus allen Bytes einer Datei berechnet wird. `sha256sum datei` berechnet sie.

</li>

<li>

Ändert sich auch nur ein Byte der Datei, ändert sich die Prüfsumme völlig. Eine zweite Datei mit derselben Prüfsumme gezielt herzustellen, ist praktisch unmöglich.

</li>

<li>

Eine Prüfsumme beweist deshalb, dass eine Datei unverändert ist, wenn man den richtigen Wert aus einer vertrauenswürdigen Quelle kennt. Woher die Datei stammt, beweist sie allein nicht: Wer die Datei fälscht, kann auch eine falsche Prüfsumme danebenlegen.

</li>

</ul>

In den Listen der Paketverwaltung kommen außerdem ältere Prüfsummen vor: MD5 mit 32 und SHA-1 mit 40 Hexadezimalziffern. Beide gelten heute als zu schwach, um Fälschungen auszuschließen; `apt` verlässt sich auf SHA-256.

⁠**Kurz gesagt:** Eine SHA-256-Prüfsumme belegt, dass eine Datei unverändert ist, sobald man den richtigen Wert aus einer vertrauenswürdigen Quelle hat.

:::::

### Die Prüfsumme der Paketdatei

<span class="anker" id="stufe-7-2"></span>

Unterabschnitt [3.5](paketquellen-und-paketlisten.html#stufe-3-5) hat gezeigt, dass die Paketliste zu jedem Paket eine Prüfsumme nennt. Das ist das erste Glied der Kette.

:::definition Definition 7.1 (Prüfung der Paketdatei)
<span class="anker" id="satz-7-1"></span>

Nach dem Herunterladen berechnet `apt` die SHA-256-Prüfsumme jeder Paketdatei und vergleicht sie mit dem Wert im Feld `SHA256` der Paketliste. Stimmen sie nicht überein, benutzt `apt` die Datei nicht.
:::

::::beispiel Die Prüfsumme von hello von Hand
Die heruntergeladene Datei aus Unterabschnitt [5.1](ein-paket-von-innen.html#stufe-5-1) und der Eintrag in der Paketliste:

```console
$ sha256sum hello_2.10-5build1_amd64.deb
b6e9bef3c865aa17757cd9ffa820c05a37833f8a6b58287afc9f32dedb345965  hello_2.10-5build1_amd64.deb
$ apt-cache show hello | grep -E '^(Filename|Size|SHA256):'
Filename: pool/main/h/hello/hello_2.10-5build1_amd64.deb
Size: 26068
SHA256: b6e9bef3c865aa17757cd9ffa820c05a37833f8a6b58287afc9f32dedb345965
```

Die beiden Werte stimmen in allen 64 Ziffern überein. Ändert man in einer Kopie ein einziges Byte, ist das vorbei:

```console
$ cp hello_2.10-5build1_amd64.deb gefaelscht.deb
$ printf 'X' | dd of=gefaelscht.deb bs=1 seek=20000 conv=notrunc status=none
$ cmp hello_2.10-5build1_amd64.deb gefaelscht.deb
hello_2.10-5build1_amd64.deb gefaelscht.deb differ: byte 20001, line 113
$ sha256sum hello_2.10-5build1_amd64.deb gefaelscht.deb
b6e9bef3c865aa17757cd9ffa820c05a37833f8a6b58287afc9f32dedb345965  hello_2.10-5build1_amd64.deb
7d4be4c4cec37ebd84b1f39b1c47b64d73d1ed783e0e79b692079208ca6e2db7  gefaelscht.deb
$ rm gefaelscht.deb
```

`dd` schreibt hier ein einzelnes `X` in die Kopie, und zwar hinter die ersten 20 000 Byte, ohne die Datei zu kürzen. `cmp` ([Kapitel 6, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-2)) meldet deshalb den ersten Unterschied bei Byte 20 001. Die Prüfsumme der Fälschung hat mit der echten nichts mehr gemein. `apt` würde diese Datei ablehnen.
::::

⁠**Kurz gesagt:** Jede Paketdatei ist über ihre SHA-256-Prüfsumme in der Paketliste verankert; eine veränderte Datei fällt beim Vergleich auf.

### Die Release-Datei

<span class="anker" id="stufe-7-3"></span>

Die Prüfsumme in der Paketliste hilft nur, wenn die Paketliste selbst echt ist. Wer eine Paketdatei austauscht, könnte ja auch den Eintrag in der Liste ändern. Also braucht auch die Liste eine Prüfsumme, und die muss wieder irgendwo stehen.

:::definition Definition 7.2 (Release-Datei)
<span class="anker" id="satz-7-2"></span>

Die __Release-Datei__ ist die oberste Datei einer Ausgabe. Sie nennt Herkunft, Ausgabe, Codename, Datum, Architekturen und Bereiche und enthält für jede Paketliste der Ausgabe deren Größe und Prüfsumme, unter anderem nach SHA-256. Auf dem Server liegt sie als `dists/ausgabe/InRelease`; `apt` speichert sie in `/var/lib/apt/lists` als `…_InRelease`.
:::

::::beispiel Die Paketliste gegen die Release-Datei prüfen
Zuerst die Prüfsumme der Paketliste von `main` auf der Platte und der passende Eintrag in der Release-Datei von `resolute`:

```console
$ cd /var/lib/apt/lists
$ sha256sum *_resolute_main_binary-amd64_Packages
92eb335c0ed27983d41a5a0efdf0edce3e67bfa34e8e987af9df260ca72d9bf9  archive.ubuntu.com_ubuntu_dists_resolute_main_binary-amd64_Packages
$ grep ' main/binary-amd64/Packages$' *_resolute_InRelease
 fe88014eb741aa4822e1c1f3599a3c89          7581722 main/binary-amd64/Packages
 d0b61ca682c19bb2087ac611a2fc87be77e6c621          7581722 main/binary-amd64/Packages
 92eb335c0ed27983d41a5a0efdf0edce3e67bfa34e8e987af9df260ca72d9bf9          7581722 main/binary-amd64/Packages
```

Die Release-Datei nennt die Paketliste von `main` dreimal: mit MD5 (32 Ziffern), SHA-1 (40) und SHA-256 (64), jeweils mit der Größe 7 581 722 Byte. Die SHA-256-Prüfsumme stimmt mit der Liste auf der Platte überein. So beginnt die Datei:

```console
$ head -n 14 archive.ubuntu.com_ubuntu_dists_resolute_InRelease
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Origin: Ubuntu
Label: Ubuntu
Suite: resolute
Version: 26.04
Codename: resolute
Date: Thu, 23 Apr 2026 17:07:15 UTC
Architectures: amd64 amd64v3 arm64 armhf i386 ppc64el riscv64 s390x
Components: main restricted universe multiverse
Description: Ubuntu Resolute 26.04
MD5Sum:
 c91a39fd4665cfbf3c6c1eafb1d84f34        924878869 Contents-amd64
```

Das Datum ist der Erscheinungstag. Die erste Zeile verrät schon, dass diese Datei unterschrieben ist; was das heißt, erklären die nächsten beiden Unterabschnitte.
::::

:::abbildung linux/k9kette 30
Die Kette der Prüfsummen von oben nach unten. Oben die Release-Datei `dists/resolute/InRelease` mit einem Siegel; in ihr leuchtet die Zeile „`92eb335c…` main/binary-amd64/Packages“. Der Wert wandert in eine Vergleichszeile neben der Paketliste `main/binary-amd64/Packages` und trifft dort auf deren berechnete Prüfsumme `92eb335c…`: grünes Gleichheitszeichen. In der Paketliste leuchtet der Eintrag von `hello` mit „SHA256: `b6e9bef3…`“; der Wert wandert neben die Paketdatei, deren berechnete Prüfsumme ebenfalls `b6e9bef3…` ist: grünes Gleichheitszeichen. Zum Schluss darunter eine gefälschte Paketdatei `gefaelscht.deb` mit einem geänderten Byte und der Prüfsumme `7d4be4c4…`: Das Gleichheitszeichen ist rot und durchgestrichen, „abgelehnt“.
:::

⁠**Kurz gesagt:** Die Release-Datei enthält die Prüfsummen aller Paketlisten, die Paketlisten enthalten die Prüfsummen aller Paketdateien; wer der Release-Datei traut, kann jeder Paketdatei trauen.

### Das Schlüsselpaar

<span class="anker" id="stufe-7-4"></span>

Die Kette endet bei der Release-Datei. Für sie gibt es keine weitere Liste mit Prüfsummen, und eine Prüfsumme allein beweist nicht, woher eine Datei stammt. Gebraucht wird ein Verfahren, mit dem Ubuntu eine Datei so kennzeichnen kann, dass jeder die Kennzeichnung prüfen, aber niemand sonst sie herstellen kann.

:::definition Definition 7.3 (Schlüsselpaar)
<span class="anker" id="satz-7-3"></span>

Ein __Schlüsselpaar__ besteht aus zwei zusammengehörigen Schlüsseln, langen Zahlen, die ein Programm gemeinsam erzeugt. Den *geheimen Schlüssel* behält sein Besitzer für sich. Den *öffentlichen Schlüssel* darf jeder kennen; aus ihm lässt sich der geheime nach heutigem Wissen praktisch nicht ausrechnen.
:::

Wie die beiden Schlüssel mathematisch zusammenhängen, erklärt die Kryptographie; hier genügt, was man mit ihnen tun kann. Ubuntu besitzt für seine Paketquellen ein solches Paar, den *Archivschlüssel*. Der geheime Teil liegt bei Ubuntu, der öffentliche auf jedem Ubuntu-Rechner. Abbildung [31](#abb-31) zeigt die Aufteilung.

:::abbildung linux/k9schluesselpaar 31
Ein Programm erzeugt aus einer Zufallszahl zwei zusammengehörige Schlüssel, gleich gefärbt. Ein grüner Pfeil vom geheimen zum öffentlichen Schlüssel steht für „beim Erzeugen berechnet“, ein roter Pfeil zurück wird durchgestrichen: „zurück: praktisch nicht ausrechenbar“. Dann schließt sich um den geheimen Schlüssel ein Tresor bei Ubuntu, und Kopien des öffentlichen wandern auf die Rechner (Datei `ubuntu-archive-keyring.gpg` auf jedem Ubuntu-Rechner).
:::

⁠**Kurz gesagt:** Ein Schlüsselpaar besteht aus einem geheimen Schlüssel, den nur sein Besitzer hat, und einem öffentlichen, den jeder haben darf.

### Die digitale Signatur

<span class="anker" id="stufe-7-5"></span>

Mit dem Schlüsselpaar lässt sich die Release-Datei kennzeichnen. Ein Bild zur Orientierung: ein Siegel aus Wachs mit dem Siegelring eines Notars. Jeder kann das Wappen im Wachs mit einem Musterabdruck vergleichen, aber nur wer den Ring besitzt, kann es herstellen, und ein aufgebrochenes Siegel bemerkt jeder. Das Bild hinkt an einer Stelle: Ein Wachssiegel kann man nachschnitzen, eine digitale Signatur ohne den geheimen Schlüssel nach heutigem Wissen nicht herstellen.

:::definition Definition 7.4 (Digitale Signatur)
<span class="anker" id="satz-7-4"></span>

Eine __digitale Signatur__ ist eine Zahl, die ein Programm aus dem Inhalt einer Datei und einem geheimen Schlüssel berechnet. Mit dem passenden öffentlichen Schlüssel kann jeder prüfen, dass die Signatur zu genau diesem Inhalt gehört und mit dem geheimen Schlüssel erzeugt wurde. Ändert sich der Inhalt auch nur um ein Byte, schlägt die Prüfung fehl.
:::

Ubuntu signiert jede Release-Datei mit dem geheimen Archivschlüssel. Bei `InRelease` stehen Text und Signatur in derselben Datei: oben der Text zwischen `BEGIN PGP SIGNED MESSAGE` und `BEGIN PGP SIGNATURE`, unten die Signatur. Das Format heißt OpenPGP; die Zeile `Hash: SHA512` nennt das Prüfsummenverfahren, das beim Signieren benutzt wurde.

::::beispiel Die Signatur der Release-Datei von Hand prüfen
Das Ende der Datei ist die Signatur:

```console
$ tail -n 4 archive.ubuntu.com_ubuntu_dists_resolute_InRelease
T1I/xJKnkiNhZfgrM0ww0lvAxOQ1+Tw8saAt02QN1Qkur3rOhxWIQWyIu4OLzQW2
43BaDciqYoThL5ZQV+ADjemG3v2zl5gzeDVsMn6YOyrbQ4aTcxw=
=JYDG
-----END PGP SIGNATURE-----
$ grep -c '' archive.ubuntu.com_ubuntu_dists_resolute_InRelease
1364
```

Die Datei hat 1 364 Zeilen. Geprüft wird sie mit `gpgv`, demselben Programm, das `apt` dafür aufruft; `--keyring` nennt die Datei mit den öffentlichen Schlüsseln:

```console
$ gpgv --keyring /usr/share/keyrings/ubuntu-archive-keyring.gpg archive.ubuntu.com_ubuntu_dists_resolute_InRelease
gpgv: Signature made Thu Apr 23 19:07:30 2026 CEST
gpgv:                using RSA key F6ECB3762474EDA9D21B7022871920D1991BC93C
gpgv: Good signature from "Ubuntu Archive Automatic Signing Key (2018) <ftpmaster@ubuntu.com>"
$ echo $?
0
$ cd ~/linuxk9
```

`Good signature` heißt: Der Inhalt ist unverändert und wurde mit dem geheimen Archivschlüssel signiert, den Ubuntu 2018 erzeugt hat. Die lange Hexadezimalzahl ist der Fingerabdruck dieses Schlüssels, eine Prüfsumme des öffentlichen Schlüssels, an der man ihn eindeutig erkennt.
::::

:::abbildung linux/k9signatur 32
Zwei Seiten. Links bei Ubuntu: die Release-Datei und der geheime Archivschlüssel (Schlüssel mit Schloss) gehen in eine Maschine „signieren“, heraus kommt die Release-Datei mit angehängter Signatur. Rechts auf dem eigenen Rechner: Release-Datei mit Signatur und der öffentliche Schlüssel gehen in eine Maschine „prüfen“ (`gpgv`), heraus kommt „Good signature“. Zweiter Durchgang: Ein Byte der Datei wird unterwegs geändert, die Prüfmaschine zeigt „BAD signature“ in Rot. Der geheime Schlüssel verlässt die linke Seite nie.
:::

⁠**Kurz gesagt:** Eine digitale Signatur kann nur der Besitzer des geheimen Schlüssels erzeugen, aber jeder mit dem öffentlichen prüfen; sie belegt Herkunft und Unversehrtheit zugleich.

### Der Schlüsselbund und Signed-By

<span class="anker" id="stufe-7-6"></span>

Die Prüfung ist nur so gut wie der öffentliche Schlüssel, mit dem man prüft. Wer einem Rechner einen falschen öffentlichen Schlüssel unterschiebt, kann alles signieren. Woher hat das System also den richtigen, und für welche Quellen gilt er?

:::definition Definition 7.5 (Schlüsselbund, Signed-By)
<span class="anker" id="satz-7-5"></span>

Ein __Schlüsselbund__ (englisch „keyring“) ist eine Datei mit einem oder mehreren öffentlichen Schlüsseln. Ubuntus Archivschlüssel liegen in `/usr/share/keyrings/ubuntu-archive-keyring.gpg`. Das Feld `Signed-By` in der Quellenliste legt fest, dass `apt` die Release-Dateien dieser Quelle nur mit den Schlüsseln aus diesem Schlüsselbund annimmt.
:::

::::beispiel Wo die Schlüssel herkommen
```console
$ ls -l /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 3607 Nov 26  2023 /usr/share/keyrings/ubuntu-archive-keyring.gpg
$ dpkg -S /usr/share/keyrings/ubuntu-archive-keyring.gpg
ubuntu-keyring: /usr/share/keyrings/ubuntu-archive-keyring.gpg
$ ls /etc/apt/trusted.gpg.d /etc/apt/keyrings
/etc/apt/keyrings:

/etc/apt/trusted.gpg.d:
ubuntu-keyring-2012-cdimage.gpg  ubuntu-keyring-2018-archive.gpg
```

Der Schlüsselbund ist selbst ein Paket, `ubuntu-keyring`; er kam mit der Installation auf den Rechner. Er enthält drei öffentliche Schlüssel, darunter den Archivschlüssel von 2018. Was in `/etc/apt/trusted.gpg.d` liegt, gilt für *alle* Quellen ohne eigenes `Signed-By`; `apt` erklärt dieses Verzeichnis inzwischen für veraltet und rät, jeder Quelle ihr eigenes `Signed-By` zu geben. Das Verzeichnis `/etc/apt/keyrings` ist für Schlüssel gedacht, die der Verwalter für zusätzliche Quellen ablegt; auf dem Testsystem ist es leer.
::::

:::abbildung linux/k9signedby 33
Zwei Einträge der Quellenliste, `ubuntu.sources` und `beispiel.sources`. Von jedem führt eine Leine `Signed-By` zu genau einem Schlüsselbund: `/usr/share/keyrings/ubuntu-archive-keyring.gpg` mit drei Schlüsseln (orange) bzw. `/etc/apt/keyrings/beispiel.gpg` mit einem (blau). Eine Release-Datei der zusätzlichen Quelle mit blauem Siegel wird angenommen (grüner Haken); dieselbe Signatur auf einer Release-Datei, die vorgibt, von Ubuntu zu kommen, prallt am Schlüsselbund von Ubuntu ab (rotes Kreuz). Zum Vergleich darunter der alte Zustand ohne `Signed-By`: ein gemeinsamer Schlüsselbund für alle Quellen, in dem jeder Schlüssel für jede Quelle gilt; dort wird auch die Fälschung angenommen.
:::

Abbildung [33](#abb-33) zeigt, was die Bindung an einen Schlüsselbund verhindert.

⁠**Kurz gesagt:** `Signed-By` bindet eine Quelle an genau einen Schlüsselbund; für Ubuntus Quellen ist das die Datei `ubuntu-archive-keyring.gpg` aus dem Paket `ubuntu-keyring` mit den öffentlichen Archivschlüsseln.

:::hintergrund Wem man am Anfang vertraut
Jede Kette braucht einen Anfang, dem man ohne weitere Prüfung vertraut. Bei Ubuntu ist das der Schlüsselbund auf dem Installationsmedium: Wer Ubuntu installiert, übernimmt ihn von dort. Deshalb lohnt die Prüfung des heruntergeladenen Abbilds aus [Kapitel 1, Abschnitt 5.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-6); Ubuntu signiert dafür auch seine Liste der Prüfsummen `SHA256SUMS` mit einer Datei `SHA256SUMS.gpg`. Neue Schlüssel kommen später als Update des Pakets `ubuntu-keyring`, also selbst über die geprüfte Kette. Früher legte man Schlüssel für fremde Quellen mit dem Befehl `apt-key` in einen Schlüsselbund, der für alle Quellen galt. Ein Schlüssel einer kleinen Fremdquelle hätte so auch Release-Dateien unterschreiben dürfen, die vorgeben, von Ubuntu zu kommen. In Ubuntu 26.04 gibt es `apt-key` nicht mehr; `Signed-By` schränkt jeden Schlüssel auf seine Quelle ein.
:::

### Der Weg eines Pakets

<span class="anker" id="stufe-7-7"></span>

Jetzt lassen sich alle Teile zusammensetzen: vom Programmierer, der ein Programm schreibt, bis zur Datei auf deinem Rechner. Abbildung [34](#abb-34) zeigt den ganzen Weg.

:::abbildung linux/k9weg 34
Der Weg eines Pakets von links nach rechts in fünf Stationen. 1 Entwickler: Quelltext von GNU hello. 2 Distribution: Ein Paketbetreuer baut die Paketdatei `hello_….deb`; die Paketliste `Packages` bekommt ihre Prüfsumme (`SHA256`), die Release-Datei die Prüfsumme der Liste, und der geheime Archivschlüssel setzt ein Siegel auf die Release-Datei. 3 Hauptserver `archive.ubuntu.com`. 4 Spiegelserver (fremder Betreiber, Verbindung über `http`, gestrichelt). 5 Dein Rechner: `apt update` prüft das Siegel mit dem öffentlichen Schlüssel, dann die Prüfsumme der Liste; `apt install` prüft die Prüfsumme der Paketdatei; erst dann packt `dpkg` aus. Unter Station 4 ein Kästchen „Angreifer“, das beim Spiegel eine Datei austauscht; bei Station 5 wird die Fälschung rot aussortiert.
:::

:::definition Definition 7.6 (Sichere Paketverwaltung)
<span class="anker" id="satz-7-6"></span>

`apt` nimmt eine Release-Datei nur an, wenn ihre Signatur mit einem Schlüssel aus dem Schlüsselbund der Quelle gültig ist. Eine Paketliste nimmt es nur an, wenn ihre Prüfsumme mit der Release-Datei übereinstimmt, eine Paketdatei nur, wenn ihre Prüfsumme mit der Paketliste übereinstimmt. Schlägt eine Prüfung fehl, verwirft `apt` die Datei und meldet einen Fehler: `apt update` behält dann die alten Listen dieser Quelle, `apt install` bricht ab, bevor `dpkg` etwas auspackt.
:::

Das Verfahren heißt in der Debian-Welt „secure APT“ und gehört seit vielen Jahren fest zu `apt`.

⁠**Kurz gesagt:** Eine einzige Signatur auf der Release-Datei sichert über zwei Stufen von Prüfsummen jede einzelne Paketdatei; der Server, von dem die Dateien kommen, muss dafür nicht vertrauenswürdig sein.

:::hintergrund Warum man die Liste signiert und nicht jedes Paket
Man könnte auch jede einzelne Paketdatei signieren. Ubuntu signiert stattdessen nur die Release-Datei einer Ausgabe, und das hat Gründe. Erstens genügt eine Signaturprüfung je Ausgabe; danach muss `apt` nur noch Prüfsummen berechnen, was viel schneller geht. Zweitens bleibt der geheime Schlüssel an einer einzigen, gut geschützten Stelle, denn er wird nur für eine Datei je Änderung gebraucht und nicht für Zehntausende Pakete. Drittens kann dadurch jeder einen Spiegelserver betreiben: Er kopiert nur Dateien und muss nichts unterschreiben, und er kann auch nichts fälschen, ohne dass es auffällt. Deshalb genügt auch unverschlüsseltes `http`. Wer unterwegs eine Datei verändert, ändert ihre Prüfsumme, und die Kette reißt. Die Kette ist dabei genauso stark wie eine Signatur auf jeder Datei, solange niemand zu einer gegebenen Prüfsumme eine zweite Datei herstellen kann, und das ist bei SHA-256 nach heutigem Wissen ausgeschlossen.
:::

### Was die Prüfung nicht leistet

<span class="anker" id="stufe-7-8"></span>

Die Kette belegt, dass eine Paketdatei von Ubuntu stammt und unverändert ist. Das ist viel, aber nicht alles, und wer die Grenzen kennt, schätzt die übrigen Schutzmaßnahmen richtig ein.

:::definition Definition 7.7 (Grenzen der Paketprüfung)
<span class="anker" id="satz-7-7"></span>

Die Prüfung der Signaturen und Prüfsummen schützt nicht davor,

<ul>

<li>

dass Dritte mitlesen: Über `http` sieht jeder auf dem Weg, welche Pakete ein Rechner lädt;

</li>

<li>

dass ein Server eine *alte*, aber echt signierte Release-Datei ausliefert, in der nur alte Versionen mit bekannten Lücken stehen; die Signatur ist ja echt;

</li>

<li>

dass ein Paket selbst Fehler enthält: Die Signatur belegt, wer das Paket gebaut hat, nicht, dass es gut ist.

</li>

</ul>
:::

Gegen veraltete Listen tragen manche Distributionen ein Ablaufdatum `Valid-Until` in ihre Release-Dateien ein; danach lehnt `apt` die Datei ab. Ubuntus Release-Dateien haben auf dem Testsystem keins, wie `grep -c '^Valid-Until'` zeigt. Bei Ubuntu kommen dafür die Sicherheitsupdates direkt vom Server `security.ubuntu.com` des Herstellers und nicht über einen fremden Spiegel (Unterabschnitt [3.2](paketquellen-und-paketlisten.html#stufe-3-2)), und das Feld `Date` der Release-Datei zeigt, wie alt eine Liste ist.

⁠**Kurz gesagt:** Signaturen und Prüfsummen sichern Herkunft und Unversehrtheit, aber weder Vertraulichkeit noch Aktualität noch die Qualität der Software.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-9"></span>

:::aufgabe Aufgabe 21 ★★ Die Kette für sl nachprüfen
<span class="anker" id="aufg-21"></span>

Prüfe die Kette aus Abbildung [30](#abb-30) für das Paket `sl` aus Aufgabe [15](ein-paket-von-innen.html#aufg-15). (a) Vergleiche die Prüfsumme der Paketdatei mit der Paketliste. (b) `sl` steht im Bereich `universe`. Vergleiche die Prüfsumme dieser Paketliste mit der Release-Datei von `resolute`. (c) Wie prüfst du das letzte Glied, die Release-Datei?

:::loesung
```console
$ sha256sum sl_*.deb
93a663b136328d7e0950089e8c1fc5f4aeed87774be3fde1eb68cc4878721f1c  sl_5.02-1build1_amd64.deb
$ apt-cache show sl | grep -E '^(Filename|SHA256):'
Filename: pool/universe/s/sl/sl_5.02-1build1_amd64.deb
SHA256: 93a663b136328d7e0950089e8c1fc5f4aeed87774be3fde1eb68cc4878721f1c
$ cd /var/lib/apt/lists
$ sha256sum *_resolute_universe_binary-amd64_Packages
9c009342905706a05822f6e751f5b1ac34b687f054bfca9a0a652178445fc44c  archive.ubuntu.com_ubuntu_dists_resolute_universe_binary-amd64_Packages
$ grep ' universe/binary-amd64/Packages$' *_resolute_InRelease | tail -n 1
 9c009342905706a05822f6e751f5b1ac34b687f054bfca9a0a652178445fc44c         76792699 universe/binary-amd64/Packages
$ cd ~/linuxk9
```

(a) Die Prüfsumme der Paketdatei stimmt mit dem Feld `SHA256` der Paketliste überein. (b) Die Prüfsumme der Paketliste von `universe` stimmt mit der Zeile in der Release-Datei überein; `tail -n 1` nimmt die letzte der drei Zeilen, die nach SHA-256. Die Liste ist 76 792 699 Byte groß, mehr als zehnmal so groß wie die von `main`. (c) Mit `gpgv --keyring /usr/share/keyrings/ubuntu-archive-keyring.gpg` und der Release-Datei, wie in Unterabschnitt [7.5](#stufe-7-5); erst `Good signature` schließt die Kette.
:::
:::

:::aufgabe Aufgabe 22 ★ Was ein Spiegelbetreiber fälschen müsste
<span class="anker" id="aufg-22"></span>

Der Betreiber eines Spiegelservers will dir eine veränderte Fassung von `hello` unterschieben. (a) Welche Dateien müsste er verändern, damit dein `apt` die Fälschung annimmt? (b) An welcher Stelle scheitert er, und warum? (c) Was könnte er stattdessen tun, ohne dass die Prüfung anschlägt? Denke an Unterabschnitt [7.8](#stufe-7-8).

:::loesung
(a) Er müsste die Paketdatei austauschen, in der Paketliste deren Prüfsumme anpassen, in der Release-Datei die Prüfsumme der Paketliste anpassen und dann die Release-Datei neu signieren.

(b) Am letzten Schritt: Eine gültige Signatur kann nur erzeugen, wer den geheimen Archivschlüssel hat, und der liegt bei Ubuntu. Jede Änderung an Release-Datei, Paketliste oder Paketdatei bricht die Kette an genau einer Stelle, und `apt` lehnt ab.

(c) Er kann Dateien zurückhalten oder alte, echt signierte Listen ausliefern, sodass dein Rechner von neuen Versionen nichts erfährt (Unterabschnitt [7.8](#stufe-7-8)); er sieht, welche Pakete du lädst; und er kann den Dienst ganz verweigern. Fälschen kann er nichts.
:::
:::

:::aufgabe Aufgabe 23 ★★ Nur http
<span class="anker" id="aufg-23"></span>

Deine Quellenliste benutzt `http`, nicht `https`. (a) Was kann jemand, der im selben WLAN mitliest, über dein System erfahren? (b) Was kann er nicht, und warum? (c) Würde `https` die Kette aus Prüfsummen und Signatur überflüssig machen? Begründe.

:::loesung
(a) Wer mitliest, sieht die Adressen und Dateien: welche Paketlisten dein Rechner holt und welche Pakete in welcher Version er herunterlädt. Daraus lässt sich ablesen, welche Software installiert wird und welche Updates noch fehlen. (b) Er kann keine Datei unbemerkt verändern, denn jede Änderung bricht die Kette aus Signatur und Prüfsummen. (c) Nein. `https` verschlüsselt nur den Weg zu dem Server, mit dem man spricht. Es belegt, dass man mit diesem Server spricht, nicht, dass dessen Dateien echt sind. Ein Spiegel mit gültigem Zertifikat könnte trotzdem veränderte Pakete ausliefern; das erkennt nur die Kette. `https` würde aber das Mitlesen aus (a) erschweren.
:::
:::
