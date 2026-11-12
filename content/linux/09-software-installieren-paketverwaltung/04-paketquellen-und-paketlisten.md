---
title: Paketquellen und Paketlisten
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140400
summary: Bisher ging es um Pakete, die schon installiert sind.
tags: Paketquelle, Spiegelserver, Ausgabe, Bereich, Quellenliste, Paketliste
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bisher ging es um Pakete, die schon installiert sind. Neue Pakete holt `apt` von Servern der Distribution. Dieser Abschnitt zeigt, wie diese Server aufgebaut sind, wo dein System einträgt, welche es benutzt, und wie `apt` erfährt, welche Pakete es dort gibt.
:::

### Die Paketquelle

<span class="anker" id="stufe-3-1"></span>

Pakete liegen nicht verstreut auf den Webseiten ihrer Entwickler, sondern gesammelt bei der Distribution. Ein Bild zur Orientierung: ein Versandhaus mit Lager und Katalog. Neben den Waren selbst gibt es ein Verzeichnis, was es gibt, in welcher Ausführung und in welchem Regal.

:::definition Definition 3.1 (Paketquelle)
<span class="anker" id="satz-3-1"></span>

Eine __Paketquelle__ (englisch „repository“) ist ein Server, auf dem eine Distribution ihre Paketdateien bereitstellt, zusammen mit Listen, die jedes Paket mit seiner Beschreibung und dem Ort seiner Paketdatei aufführen. Die Paketdateien liegen dort im Verzeichnis `pool`, die Listen im Verzeichnis `dists`.
:::

Ubuntus wichtigste Paketquelle ist `http://archive.ubuntu.com/ubuntu/`. Unter `pool/main/h/hello/` liegt dort zum Beispiel die Paketdatei von `hello`; das `h` ist der Anfangsbuchstabe, damit kein Verzeichnis Zehntausende Einträge bekommt.

:::abbildung linux/k9quelle 11
Eine Paketquelle als Lagerhaus mit zwei Bereichen. Links `pool`: Regale nach Anfangsbuchstaben, im Fach `h/hello` die Datei `hello_2.10-5build1_amd64.deb`. Rechts `dists`: ein Katalog je Ausgabe (`resolute`, `resolute-updates`, `resolute-security`), darin Listen je Bereich und Architektur. Eine Katalogzeile „hello, 2.10-5build1, Filename: pool/main/h/hello/…“ leuchtet, ein Pfeil führt von ihr ins richtige Regal.
:::

⁠**Kurz gesagt:** Eine Paketquelle ist ein Server mit Paketdateien (`pool`) und Listen, die beschreiben, welche Pakete es gibt und wo ihre Dateien liegen (`dists`).

### Der Spiegelserver

<span class="anker" id="stufe-3-2"></span>

Millionen Rechner holen täglich Pakete. Ein einzelner Server wäre damit überlastet, und für weit entfernte Rechner wäre er langsam.

:::definition Definition 3.2 (Spiegelserver)
<span class="anker" id="satz-3-2"></span>

Ein __Spiegelserver__ (englisch „mirror“) ist ein Server, der eine Paketquelle regelmäßig vollständig kopiert und dieselben Dateien unter einer eigenen Adresse bereitstellt. Spiegelserver betreiben oft Universitäten, Firmen oder Vereine.
:::

Schon hinter dem Namen `archive.ubuntu.com` stehen mehrere Server; dazu gibt es Länderspiegel wie `de.archive.ubuntu.com` und viele unabhängige Spiegel. Die Sicherheitsupdates kommen dagegen in der Voreinstellung direkt vom Server `security.ubuntu.com` des Herstellers. So erreichen sie jeden Rechner sofort und nicht erst, wenn der Spiegel das nächste Mal kopiert hat. Abbildung [12](#abb-12) zeigt beide Wege.

:::abbildung linux/k9spiegel 12
Oben die Hauptquelle von Ubuntu mit `archive.ubuntu.com` und `security.ubuntu.com`. Darunter drei Spiegelserver (Universität, Firma, Verein), die in Abständen eine Kopie ziehen; eine Uhr an jedem Spiegel zeigt den Stand der letzten Kopie. Darunter Rechner, die ihre Pakete vom Spiegel in ihrer Nähe holen. Ein neues Sicherheitsupdate erscheint in der Hauptquelle: Über den direkten Pfeil von `security.ubuntu.com` erreicht es alle Rechner sofort, während die Spiegel es erst bei ihrer nächsten Kopie bekommen.
:::

⁠**Kurz gesagt:** Ein Spiegelserver ist eine vollständige Kopie einer Paketquelle an einem anderen Ort; er verteilt die Last, ist aber ein fremder Server.

:::hintergrund Warum man einem fremden Spiegel überhaupt Pakete abnimmt
Ein Spiegelserver gehört nicht der Distribution. Wer ihn betreibt, könnte Dateien austauschen, und die Verbindung dorthin läuft in der Voreinstellung über unverschlüsseltes `http`. Trotzdem nimmt `apt` von jedem Spiegel Pakete an. Das geht nur, weil `apt` nicht dem Server vertraut, sondern jede Datei, die es von dort bekommt, selbst prüft, bevor es sie benutzt.
:::

### Ausgabe und Bereich

<span class="anker" id="stufe-3-3"></span>

Eine Paketquelle enthält Pakete für mehrere Versionen der Distribution, und darin wieder Pakete, für die Ubuntu verschieden stark einsteht. Beides muss man auswählen können.

:::definition Definition 3.3 (Ausgabe, Bereich)
<span class="anker" id="satz-3-3"></span>

Eine __Ausgabe__ (englisch „suite“) ist ein Teil der Paketquelle mit einer eigenen Paketliste, benannt nach dem Codenamen einer Version der Distribution und gegebenenfalls einem Zusatz. Ein __Bereich__ (englisch „component“) teilt jede Ausgabe nach Lizenz und Betreuung auf.
:::

Ubuntu 26.04 hat den Codenamen `resolute` ([Kapitel 2, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-1)). Seine Ausgaben sind:

<ul>

<li>

`resolute`: die Pakete am Erscheinungstag, dem 23. April 2026; diese Ausgabe ändert sich danach nicht mehr;

</li>

<li>

`resolute-updates`: Fehlerkorrekturen, die nach dem Erscheinen dazukommen;

</li>

<li>

`resolute-security`: Korrekturen von Sicherheitslücken;

</li>

<li>

`resolute-backports`: neuere Programmversionen, die nur wenig geprüft sind und keine Sicherheitsupdates bekommen.

</li>

</ul>

Abbildung [13](#abb-13) zeigt, wie die Ausgaben mit der Zeit wachsen, Tabelle [1](#tab-1) die vier Bereiche.

:::abbildung linux/k9ausgaben 13
Eine Zeitachse vom 23. April 2026 bis zum 12. November 2026, dem Stand dieses Kapitels. Die Ausgabe `resolute` ist ein fester Block am Anfang, der danach unverändert bleibt. Darüber wachsen zwei Spuren mit der Zeit: `resolute-updates` (Fehlerkorrekturen) und `resolute-security` (Sicherheitskorrekturen); einzelne Pakete wie `sudo-rs` bekommen darin neue Versionen. Eine dritte, blassere Spur `resolute-backports` mit neueren Programmversionen. Rechts, durch eine Klammer mit allen Ausgaben verbunden, die vier Bereiche `main`, `restricted`, `universe`, `multiverse` als Schichten: Jede Ausgabe hat alle vier.
:::

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Die vier Bereiche der Ubuntu-Paketquellen (nach den Erklärungen in `ubuntu.sources`).

| Bereich | Inhalt |
|---|---|
| `main` | freie Software, die Ubuntu selbst pflegt und mit Sicherheitsupdates versorgt |
| `restricted` | Software, die nicht unter einer freien Lizenz steht oder durch Patente geschützt ist, die Ubuntu aber unterstützt, etwa Treiber |
| `universe` | freie Software, die Freiwillige aus der Gemeinschaft pflegen; mit einem Abonnement von Ubuntu Pro gibt Canonical darauf zehn Jahre Sicherheitspflege |
| `multiverse` | Software mit eingeschränkten Rechten, ausdrücklich ohne jede Unterstützung durch Ubuntu |

::::beispiel Wie viel in den Bereichen steckt
Auf dem Testsystem verzeichnet die Liste von `resolute` im Bereich `main` 6 487 Pakete, im Bereich `universe` 66 741. Der weitaus größte Teil der Software stammt also aus der Gemeinschaft, nicht von Ubuntu selbst.
::::

⁠**Kurz gesagt:** Eine Ausgabe wählt die Version der Distribution und die Art der Pakete (Erscheinungstag, Korrekturen, Sicherheit, neuere Versionen), ein Bereich wählt nach Lizenz und Betreuung.

### Die Quellenliste

<span class="anker" id="stufe-3-4"></span>

Woher weiß `apt`, welche Server, Ausgaben und Bereiche es benutzen soll? Das steht in einer Textdatei unter `/etc/apt`.

:::definition Definition 3.4 (Quellenliste)
<span class="anker" id="satz-3-4"></span>

Die __Quellenliste__ ist die Einstellung, aus der `apt` seine Paketquellen liest. Unter Ubuntu 26.04 steht sie in der Datei `/etc/apt/sources.list.d/ubuntu.sources`. Jeder Eintrag ist ein Block aus Zeilen `Feld: Wert`, Einträge sind durch eine Leerzeile getrennt:

<ul>

<li>

`Types:` `deb` für Pakete zum Installieren (`deb-src` für Quelltexte);

</li>

<li>

`URIs:` die Adresse der Paketquelle;

</li>

<li>

`Suites:` die Ausgaben;

</li>

<li>

`Components:` die Bereiche;

</li>

<li>

`Signed-By:` eine Datei, mit der `apt` prüft, dass die Listen dieser Quelle wirklich von Ubuntu stammen.

</li>

</ul>
:::

Dieses Format heißt *deb822*, weil seine Zeilen `Feld: Wert` dem Aufbau von E-Mail-Köpfen nach dem alten Standard RFC 822 folgen; dieselbe Form haben die Paketbeschreibungen. Weitere Dateien mit der Endung `.sources` im Verzeichnis `/etc/apt/sources.list.d` sind weitere Quellen.

::::beispiel Die Quellenliste des Testsystems
Ohne die Kommentarzeilen sieht die Datei so aus:

```console
$ grep -v '^#' /etc/apt/sources.list.d/ubuntu.sources

Types: deb
URIs: http://archive.ubuntu.com/ubuntu/
Suites: resolute resolute-updates resolute-backports
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: http://security.ubuntu.com/ubuntu/
Suites: resolute-security
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

Der erste Eintrag holt drei Ausgaben vom allgemeinen Server, der zweite die Sicherheitsausgabe vom eigenen Server. Beide nehmen alle vier Bereiche und denselben Schlüssel. Aus einem Eintrag setzt `apt` die Adressen der Listen zusammen: Adresse, dann `dists`, Ausgabe, Bereich und Architektur, also zum Beispiel `http://archive.ubuntu.com/ubuntu/dists/resolute/main/binary-amd64/`.
::::

:::abbildung linux/k9quellenliste 14
Oben die Datei `ubuntu.sources` mit beiden Einträgen. Darunter entsteht aus dem ersten Eintrag Stück für Stück eine Adresse: `URIs` liefert `http://archive.ubuntu.com/ubuntu/`, dann kommt `dists/`, aus `Suites` das Wort `resolute`, aus `Components` `main`, dazu `binary-amd64`. Rechts die Zählung: 3 Ausgaben mal 4 Bereiche ergeben 12 Listen; der zweite Eintrag liefert 4 weitere, zusammen 16. `Signed-By` hängt als Schloss an beiden Einträgen.
:::

⁠**Kurz gesagt:** Die Quellenliste `/etc/apt/sources.list.d/ubuntu.sources` nennt in Blöcken Adresse, Ausgaben, Bereiche und Schlüssel jeder Paketquelle.

:::hintergrund Das alte Format mit einer Zeile je Quelle
Bis Ubuntu 23.10 stand die Quellenliste in der Datei `/etc/apt/sources.list`, mit einer Zeile je Kombination, etwa `deb http://archive.ubuntu.com/ubuntu/ resolute main universe`. Ein Schlüssel ließ sich dort in eckigen Klammern angeben: `deb [signed-by=/pfad/schluessel.gpg] adresse ausgabe bereich`. Ubuntu 26.04 versteht dieses Format noch, Dateien mit der Endung `.list` im Verzeichnis `sources.list.d` sind ebenfalls erlaubt. Die alte Datei enthält nur noch einen Hinweis:

```console
$ cat /etc/apt/sources.list
```

```text
# Ubuntu sources have moved to the /etc/apt/sources.list.d/ubuntu.sources
# file, which uses the deb822 format. Use deb822-formatted .sources files
# to manage package sources in the /etc/apt/sources.list.d/ directory.
# See the sources.list(5) manual page for details.
```

Laut der Handbuchseite `sources.list(5)` gilt das alte Format als veraltet und soll frühestens 2029 entfallen. Das neue Format ist leichter maschinell zu bearbeiten, und ein Eintrag lässt sich mit der Zeile `Enabled: no` abschalten, statt ihn auszukommentieren.
:::

### Die Paketliste

<span class="anker" id="stufe-3-5"></span>

`apt` kann nicht bei jeder Frage alle Server abfragen; es braucht eine Kopie der Kataloge auf dem eigenen Rechner. Diese Kopie ist es, die `apt` durchsucht, wenn es ein Paket finden oder Abhängigkeiten auflösen soll.

:::definition Definition 3.5 (Paketliste)
<span class="anker" id="satz-3-5"></span>

Eine __Paketliste__ ist eine Textdatei mit den Paketbeschreibungen aller Pakete eines Bereichs einer Ausgabe, jeweils ergänzt um den Ort der Paketdatei (`Filename`), ihre Größe (`Size`) und ihre Prüfsumme (`SHA256`). Die Listen heißen auf dem Server `Packages`. `apt` legt Kopien davon im Verzeichnis `/var/lib/apt/lists` ab; zu jeder Ausgabe kommt eine Datei `InRelease` hinzu, die die ganze Ausgabe zusammenfasst.
:::

::::beispiel Der Eintrag von hello in der Paketliste
```console
$ ls /var/lib/apt/lists | head -n 6
archive.ubuntu.com_ubuntu_dists_resolute-backports_InRelease
archive.ubuntu.com_ubuntu_dists_resolute-backports_main_cnf_Commands-amd64
archive.ubuntu.com_ubuntu_dists_resolute-backports_main_dep11_Components-amd64.yml.gz
archive.ubuntu.com_ubuntu_dists_resolute-backports_multiverse_cnf_Commands-amd64
archive.ubuntu.com_ubuntu_dists_resolute-backports_multiverse_dep11_Components-amd64.yml.gz
archive.ubuntu.com_ubuntu_dists_resolute-backports_restricted_cnf_Commands-amd64
$ ls /var/lib/apt/lists | wc -l
65
```

Die Dateinamen sind die Adressen der Listen, mit `_` statt `/`. Neben den Paketlisten liegen dort Listen für die Hilfe bei unbekannten Befehlen (`Commands`), für grafische Softwarezentren (`Components`) und für Übersetzungen der Beschreibungen. Im Verzeichnis der Listen findet `grep` den Eintrag von `hello`; die Option `-A 25` gibt zu jedem Treffer die 25 folgenden Zeilen mit aus, ein zweites `grep` behält davon nur sechs Felder:

```console
$ cd /var/lib/apt/lists
$ grep -A 25 '^Package: hello$' *_resolute_main_binary-amd64_Packages | grep -E '^(Package|Version|Depends|Filename|Size|SHA256):'
Package: hello
Version: 2.10-5build1
Depends: libc6 (>= 2.38)
Filename: pool/main/h/hello/hello_2.10-5build1_amd64.deb
Size: 26068
SHA256: b6e9bef3c865aa17757cd9ffa820c05a37833f8a6b58287afc9f32dedb345965
Package: hfsplus
```

Die letzte Zeile gehört schon zum nächsten Paket. `Filename` ist der Ort im `pool` aus Unterabschnitt [3.1](#stufe-3-1). Wie viele Pakete eine Liste verzeichnet, zählt `grep -c` ([Kapitel 6, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/suchen-mit-grep.html#stufe-5-2)):

```console
$ grep -c '^Package: ' *_resolute_main_binary-amd64_Packages *_resolute_universe_binary-amd64_Packages
archive.ubuntu.com_ubuntu_dists_resolute_main_binary-amd64_Packages:6487
archive.ubuntu.com_ubuntu_dists_resolute_universe_binary-amd64_Packages:66741
$ cd ~/linuxk9
```
::::

⁠**Kurz gesagt:** Eine Paketliste verzeichnet alle Pakete eines Bereichs mit Beschreibung, Ort, Größe und Prüfsumme der Paketdatei; `apt` hält Kopien davon in `/var/lib/apt/lists`.

### Die Paketlisten holen: apt update

<span class="anker" id="stufe-3-6"></span>

Die Kopien der Paketlisten veralten. Kommt auf dem Server ein Sicherheitsupdate hinzu, erfährt dein Rechner davon erst, wenn er die Listen neu holt. Dafür gibt es einen eigenen Befehl.

:::definition Definition 3.6 (apt update)
<span class="anker" id="satz-3-6"></span>

`sudo apt update` lädt für jede Paketquelle der Quellenliste die aktuelle Datei `InRelease` und alle Paketlisten, die sich seit dem letzten Mal geändert haben, prüft sie und ersetzt damit die Kopien in `/var/lib/apt/lists`. Danach meldet es, wie viele installierte Pakete sich aktualisieren lassen. An der installierten Software ändert es nichts.
:::

`apt update` braucht `root`, weil es Dateien unter `/var/lib/apt/lists` schreibt, die `root` gehören.

:::warnung Der erste Befehl, der etwas verändert
`sudo apt update` ersetzt die Paketlisten deines Systems durch neuere. Das ist ungefährlich und genau das, was Ubuntu ohnehin regelmäßig von selbst tut; installiert, entfernt oder aktualisiert wird dabei nichts. Der Befehl braucht eine Netzverbindung und fragt nach deinem Passwort ([Kapitel 7, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-1)).
:::

::::beispiel Die Listen des Testsystems auffrischen
```console
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu resolute InRelease
Get:2 http://security.ubuntu.com/ubuntu resolute-security InRelease [137 kB]
Get:3 http://archive.ubuntu.com/ubuntu resolute-updates InRelease [137 kB]
Get:4 http://security.ubuntu.com/ubuntu resolute-security/main amd64 Packages [717 kB]
Get:5 http://archive.ubuntu.com/ubuntu resolute-backports InRelease [137 kB]
Get:6 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 Packages [868 kB]
...
Get:21 http://archive.ubuntu.com/ubuntu resolute-backports/universe amd64 Components [1056 B]
Fetched 5008 kB in 1s (8536 kB/s)
126 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

`Hit` heißt: Die Datei auf dem Server ist unverändert, `apt` behält seine Kopie. `Get` heißt: Sie ist neu und wird geladen; dahinter steht die Größe. Die Ausgabe `resolute` vom Erscheinungstag ändert sich nicht mehr, deshalb kommt dort nur `Hit`. Auf dem Testsystem lagen die Listen acht Tage zurück; seitdem waren 5 008 kB an Änderungen aufgelaufen, und 126 installierte Pakete haben neuere Versionen.
::::

:::abbildung linux/k9update 15
Links die Server `archive.ubuntu.com` und `security.ubuntu.com` mit ihren Katalogen, rechts der eigene Rechner mit dem Ordner `/var/lib/apt/lists` und daneben dem Verzeichnisbaum mit den installierten Programmen. Bei `apt update` wandern Kataloge vom Server in den Ordner; unveränderte (`Hit`) bleiben stehen und werden nur abgehakt, geänderte (`Get`) werden ersetzt. Der Verzeichnisbaum mit den Programmen bleibt die ganze Zeit unverändert und grau; am Ende erscheint die Zeile „126 packages can be upgraded“.
:::

⁠**Kurz gesagt:** `sudo apt update` holt die aktuellen Paketlisten aller Quellen; es installiert nichts, sorgt aber dafür, dass `apt` neue Versionen überhaupt kennt.

:::hintergrund apt, apt-get und apt-cache
`apt` gibt es seit 2014. Davor bediente man die Paketverwaltung mit `apt-get` (installieren, entfernen, aktualisieren) und `apt-cache` (suchen und anzeigen). `apt` fasst die häufigsten Befehle beider zusammen und ist für Menschen am Terminal gemacht: mit Fortschrittsanzeige, Farben und übersichtlicher Ausgabe. Seine Handbuchseite sagt ausdrücklich, dass sich diese Ausgabe von Version zu Version ändern darf. Für Skripte, die die Ausgabe weiterverarbeiten, sind deshalb `apt-get` und `apt-cache` gedacht, deren Ausgabe stabil bleibt. Leitet man die Ausgabe von `apt` in eine Pipe oder Datei, warnt es davor auf der Standardfehlerausgabe.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Aufgabe 9 ★ Die Quellenliste lesen
<span class="anker" id="aufg-9"></span>

Lies die Quellenliste deines Systems wie in Unterabschnitt [3.4](#stufe-3-4). (a) Aus welchen Ausgaben und Bereichen kann dein System Pakete installieren? (b) Wie viele Paketlisten für die Architektur `amd64` ergeben sich daraus? (c) Wie lautet die vollständige Adresse des Verzeichnisses mit der Paketliste für `resolute-security` im Bereich `universe`?

:::loesung
(a) Die Ausgaben `resolute`, `resolute-updates` und `resolute-backports` kommen vom Server `archive.ubuntu.com`, die Ausgabe `resolute-security` vom Server `security.ubuntu.com`; jeweils alle vier Bereiche `main`, `universe`, `restricted` und `multiverse`.

(b) Je Ausgabe und Bereich gibt es eine Paketliste für `amd64`: $3 \cdot 4 + 1 \cdot 4 = 16$ Paketlisten.

(c) Adresse, `dists`, Ausgabe, Bereich, Architektur: [http://security.ubuntu.com/ubuntu/dists/resolute-security/universe/binary-amd64/](http://security.ubuntu.com/ubuntu/dists/resolute-security/universe/binary-amd64/). Darin liegt die Liste als `Packages`, auch in mehreren komprimierten Fassungen.
:::
:::

:::aufgabe Aufgabe 10 ★★ Warum ein eigener Server für Sicherheitsupdates?
<span class="anker" id="aufg-10"></span>

Der zweite Eintrag der Quellenliste benutzt `security.ubuntu.com` statt `archive.ubuntu.com`. (a) Was würde sich ändern, wenn man dort einen Spiegelserver in der Nähe einträgt? (b) Warum sagt der Kommentar in `ubuntu.sources`, man solle im Sicherheitseintrag nur Adresse und Ausgabe anders wählen als im ersten Eintrag, aber dieselben Bereiche?

:::loesung
(a) Ein Spiegel kopiert die Hauptquelle nur in Abständen. Sicherheitsupdates kämen dann erst nach der nächsten Kopie an, unter Umständen Stunden später, und ein Spiegel, der eine Weile nicht kopiert, hielte sie ganz zurück. Fälschen könnte er sie nicht; die Prüfung aus Abschnitt [7](warum-man-den-paketen-trauen-kann.html#stufe-7) gilt für jeden Server.

(b) Sicherheitsupdates eines Pakets erscheinen im selben Bereich wie das Paket. Nimmt man im Sicherheitseintrag einen Bereich weg, etwa `universe`, bekommen alle Pakete aus diesem Bereich keine Sicherheitsupdates mehr, obwohl sie installiert sind.
:::
:::

:::aufgabe Aufgabe 11 ★ Was apt update verändert
<span class="anker" id="aufg-11"></span>

Ein Mitbewohner sagt: „Ich habe `apt update` gemacht, jetzt ist mein System aktuell.“ Was stimmt daran, was nicht? Welche Dateien hat der Befehl verändert, welche nicht?

:::loesung
Richtig ist: Das System weiß jetzt, welche neueren Versionen es gibt; `apt` meldet am Ende, wie viele Pakete sich aktualisieren lassen. Falsch ist: Aktuell ist dadurch nichts, denn `apt update` installiert nichts. Geändert wurden nur die Dateien in `/var/lib/apt/lists`, also die Release-Dateien und Paketlisten; Programme, Bibliotheken und Einstellungen unter `/usr` und `/etc` sind unverändert. Aktuell wird das System erst mit `sudo apt upgrade`.
:::
:::
