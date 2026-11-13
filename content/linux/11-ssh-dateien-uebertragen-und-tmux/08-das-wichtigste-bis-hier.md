---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160800
summary: Wie man sich sicher auf einem anderen Rechner anmeldet, Dateien hin- und herschickt und lange Arbeiten über einen Verbindungsabbruch hinweg weiterlaufen lässt
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Bei einer entfernten Anmeldung läuft die Shell auf dem anderen Rechner. SSH verbindet den Client `ssh` mit dem Server `sshd` (Port 22): Der Server weist sich aus, die Verbindung ist verschlüsselt, der Benutzer weist sich aus.

</li>

<li>

Ein Übungsserver auf dem eigenen Rechner: eigene Datei in `/etc/ssh/sshd_config.d` (nur `localhost`, keine Passwörter), dann `openssh-server`. Unter Ubuntu lauscht systemd mit `ssh.socket` und startet `sshd` bei der ersten Verbindung.

</li>

<li>

Der Hostschlüssel beweist die Identität des Servers. Bei der ersten Verbindung vergleicht man seinen Fingerabdruck (SHA-256, 43 Base64-Zeichen) auf anderem Weg; `known_hosts` merkt ihn sich. Eine Warnung über einen geänderten Schlüssel klärt man, bevor man mit `ssh-keygen -R` löscht.

</li>

<li>

`ssh-keygen -t ed25519` erzeugt ein Schlüsselpaar; der öffentliche Schlüssel kommt in `~/.ssh/authorized_keys` auf dem Server (`ssh-copy-id`), der private bleibt mit 600 zu Hause. Die Anmeldung beweist den Besitz mit einer Signatur; der private Schlüssel verlässt den Rechner nie.

</li>

<li>

`ssh` verweigert zu offene Rechte am privaten Schlüssel, der Server an `authorized_keys`, `~/.ssh` und dem Heimatverzeichnis. Eine Passphrase schützt die Datei, der `ssh-agent` merkt sich den entschlüsselten Schlüssel.

</li>

<li>

`~/.ssh/config` gibt Servern kurze Namen. `ssh rechner 'befehl'` führt einen Befehl dort aus; zwei Shells lesen die Zeile, einfache Anführungszeichen schützen sie für den Server; Ausgaben und Exit-Status kommen zurück, 255 heißt „ssh gescheitert“; `-t` erzwingt ein Terminal.

</li>

<li>

`scp` kopiert (Doppelpunkt = andere Seite), `sftp` erlaubt Umsehen und Holen, `rsync -av` gleicht ab und überträgt nur Änderungen; Schrägstrich am Quellverzeichnis = nur der Inhalt; `--delete` nur nach `-n`.

</li>

<li>

Endet die Verbindung, bekommt die Shell auf dem Server SIGHUP und reißt ihre Jobs mit. `nohup` und `disown` retten einzelne Programme ohne Terminal; tmux (Sitzung > Fenster > Bereich, Strg+B, dann `d`, `tmux attach`) hält ganze Shells am Leben, wenn es auf dem Server läuft.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Mit SSH arbeitet man in der Shell eines anderen Rechners über eine verschlüsselte Verbindung; dass es der richtige Rechner ist, beweist sein Hostschlüssel, dessen Fingerabdruck man bei der ersten Verbindung auf anderem Weg vergleicht.

</li>

<li>

Man selbst weist sich mit einem Schlüsselpaar aus, dessen privater Teil mit strengen Rechten und Passphrase zu Hause bleibt, und überträgt Dateien mit `scp`, `sftp` oder `rsync`, das nur Änderungen schickt.

</li>

<li>

Programme auf dem Server sterben mit der Verbindung, weil die Shell dort SIGHUP bekommt; `nohup` und `disown` retten einzelne Programme, eine tmux-Sitzung auf dem Server hält ganze Shells am Leben und lässt sich nach einer neuen Anmeldung wieder anhängen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Vertrauen entsteht durch Besitz, nicht durch Weitergabe. Server und Benutzer beweisen ihre Identität mit einer Signatur aus einem privaten Schlüssel, der seinen Rechner nie verlässt; geprüft wird mit öffentlichen Schlüsseln, die man einmal auf einem sicheren Weg bekommen und dann gespeichert hat. Zweitens: Ein Programm lebt so lange wie das Terminal, an dem es hängt, es sei denn, es ignoriert SIGHUP. Die Shell einer SSH-Anmeldung hängt an einem Pseudoterminal auf dem Server, das mit der Verbindung verschwindet; tmux stellt Pseudoterminals bereit, die an keiner Verbindung hängen.

| Ergebnis | Woher es kommt |
|---|---|
| der Übungsserver ist nur für dich erreichbar | er lauscht nur an `127.0.0.1` und `::1` (Abschnitt [1](entfernte-anmeldung-client-server-und-ein-ubungsserver.html#stufe-1)) |
| `ssh.service` läuft erst nach der ersten Verbindung | systemd hält den Socket und startet den Dienst bei Bedarf (Abschnitt [1](entfernte-anmeldung-client-server-und-ein-ubungsserver.html#stufe-1)) |
| bei der ersten Verbindung fragt `ssh` | der Hostschlüssel ist noch unbekannt; nur ein Vergleich auf anderem Weg verrät jemanden, der sich dazwischenschaltet (Abschnitt [2](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2)) |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | der Server signiert mit einem anderen Schlüssel als dem gespeicherten (Abschnitt [2](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2)) |
| ein Fingerabdruck hat 43 Zeichen | 256 Bit SHA-256, 6 Bit je Base64-Zeichen (Abschnitt [2](die-erste-verbindung-hostschlussel-und-fingerabdruck.html#stufe-2)) |
| eine mitgeschnittene Anmeldung ist wertlos | die Signatur gilt nur für diese eine Verbindung (Abschnitt [3](anmelden-mit-einem-schlusselpaar.html#stufe-3)) |
| `UNPROTECTED PRIVATE KEY FILE` | wer den privaten Schlüssel lesen kann, kann sich als du anmelden (Abschnitt [3](anmelden-mit-einem-schlusselpaar.html#stufe-3)) |
| `Authentication refused: bad ownership or modes` | wer `authorized_keys` schreiben kann, kann sich Zugang verschaffen (Abschnitt [3](anmelden-mit-einem-schlusselpaar.html#stufe-3)) |
| `ssh uebung echo *.txt` zeigt lokale Dateien | die eigene Shell erweitert, bevor `ssh` startet (Abschnitt [4](bequemer-verbinden-und-befehle-aus-der-ferne.html#stufe-4)) |
| `ssh` endet mit 255 | die Verbindung oder Anmeldung selbst ist gescheitert (Abschnitt [4](bequemer-verbinden-und-befehle-aus-der-ferne.html#stufe-4)) |
| für einen Befehl gibt es kein Terminal | ein Terminal würde Daten verändern (Abschnitt [4](bequemer-verbinden-und-befehle-aus-der-ferne.html#stufe-4)) |
| `scp datei uebung` kopiert lokal | ohne Doppelpunkt ist `uebung` ein Dateiname (Abschnitt [5](dateien-ubertragen-scp-sftp-und-rsync.html#stufe-5)) |
| der zweite `rsync`-Lauf überträgt keine Datei | gleiche Größe und Zeit gelten als unverändert (Abschnitt [5](dateien-ubertragen-scp-sftp-und-rsync.html#stufe-5)) |
| 726 statt 1 288 902 Bytes gesendet | nur Blöcke, die in der alten Fassung fehlen, werden geschickt (Abschnitt [5](dateien-ubertragen-scp-sftp-und-rsync.html#stufe-5)) |
| `urlaub` und `urlaub/` ergeben verschiedene Ziele | der Schrägstrich wählt den Inhalt statt des Verzeichnisses (Abschnitt [5](dateien-ubertragen-scp-sftp-und-rsync.html#stufe-5)) |
| die Rechnung stirbt mit dem Fenster | die Shell auf dem Server bekommt SIGHUP und gibt es an ihre Jobs weiter (Abschnitt [6](programme-weiterlaufen-lassen-nohup-disown-und-tmux.html#stufe-6)) |
| die Rechnung in tmux läuft weiter | sie hängt an einem Pseudoterminal des tmux-Servers, nicht an der Verbindung (Abschnitt [6](programme-weiterlaufen-lassen-nohup-disown-und-tmux.html#stufe-6)) |
