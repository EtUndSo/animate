# F1 „Bildschirme und Fenster“: Funktionsliste aus dem Bedarf von Linux 7 und 8 (11.11.2026)

Grundlage: `notizen/editor_bildschirme_plan.md` (ganz), `uebergabe_kap7.md`/`uebergabe_kap8.md` (ganz), alle 58 Bildunterschriften (`\szenenabb{k7…}`/`{k8…}` in `kap7_stufen*.tex`, `kap8_stufen*.tex`), `linux_hilfen.py` (ganz), Muster-Szenen aus `linux_teil2/4/6.py`, Mitschriften `code/kap7|kap8/sitzung_kap*.txt` (Stichproben), `code/kap8/sitzung.py` (Kopf).

## Kurzbefund
- **58 Szenen, davon 4 Bildschirmbilder mit Fenster** (`k8journalfolgen`, `k8hintergrundlesen`, `k8sighup`, `k8nohup`). **10** zeigen und zerlegen Zeilen in Schreibmaschinenschrift (Datei- oder Ausgabezeilen mit Spaltenbezug). **10** sind Schemata mit einem kleinen Rasteranteil, und **34** sind reine Schemata, Diagramme oder Rechenbilder: kein F1.
- Aus der Liste „Kommend“ im Plan kommt in den Szenen vor: `ls -l` (als Zeile zum Zerlegen) und `journalctl -f` (`k8journalfolgen`). **Nicht** in den Szenen: `top`, `systemctl status`, `less`, `nano`, der Eigenschaften-Dialog und eine Passwortabfrage als Bildschirm. Diese Programme stehen nur als Konsolenblöcke im Heft.
- **In keiner Szene nötig:** ANSI-Farben, Rollen, Maus, Lupe. Die Mitschriften haben auch gar keine Farben, weil `sitzung.py` ANSI-Folgen entfernt.
- **Szenen-Quelle ist der Heftblock, nicht die Mitschrift.** In Kap. 8 stammt die Mitschrift aus einem frischen Lauf: Sie hat andere PIDs und Uhrzeiten als das Heft (Heft `[4] 659`, `654/656`, `15:29:25`; Mitschrift `663`, `658/660`, `16:10:58`). Ein Mitschrift-Import würde Bilder erzeugen, die nicht zum Text passen.
- Der größte Nutzen liegt deshalb nicht im Terminal, sondern im **Zeichenraster mit Spalten-API**. Es ersetzt `tt`/`ttz`/`sp`/`msp`/`mark`/`klammer` in 13 Szenen und in 8 weiteren als Option.

## 1. Szenen-Zuordnung
Kürzel: **RZ** Raster-/Textblock mit Spaltenanker · **FE** Felder finden (Trennzeichen/Leerraum) + Klammer mit Beschriftung · **HV** Bereich hervorheben (leuchten, Hinterlegung, Teilfarbe, Rest grau) · **AN** Anker (Zeile/Feld → Koordinate für Pfeile) · **DA** Datei-Ansicht (Textblock mit Dateiname als Titel) · **KO** Teil löst sich als Kopie und wandert · **WW** Wert wechselt an fester Spalte · **TF** Terminalfenster · **TL** Titelleiste mit × / Fenster schließen · **TI** Tippen · **ZA** zeilenweise Ausgabe · **CU** Cursor · **KZ** Zeile kürzen mit `…` · **TK** Tastenkappe. In Klammern = möglich, nicht verlangt.

### Kapitel 7 (28)
| Szene | Kurzinhalt | Art | Funktionen |
|---|---|---|---|
| k7passwd | passwd-Zeile (44 Z.); 6 Doppelpunkte leuchten, 7 Feldbedeutungen; Pfeil Feld 4 → group-Zeile | Raster | RZ, FE(`:`), HV, AN, DA |
| k7gruppen | passwd-Zeile links, 3 group-Zeilen rechts, Pfeile, `users` grau, `id`-Zeile (65 Z.) | Raster | RZ, FE(`:`), HV, AN, DA |
| k7prozess | Prozesskette, Etiketten, Dateien grau | Schema | kein F1 |
| k7pruefwert | Passwort → Rechenweg → Prüfwert, Vergleich | Schema | kein F1 |
| k7besitz | Inode 1000/1000; `ls -l` schlägt nach, schreibt `student`; `ls -n`-Zeile | Raster+Schema | RZ, WW (1000 → student), KO, AN, (DA) |
| k7klassen | Datei, drei Benutzer landen in u/g/o | Schema | kein F1 |
| k7rwx | Auge/Stift/Startknopf an der Datei | Schema | kein F1 (Symbole) |
| k7spalte | `ls -l`-Zeile (56 Z.), Rest grau, Klammern u/g/o, r/w/x je Stelle, Linien | Raster | RZ, FE(Leerraum + feste 3er-Gruppen), HV, AN |
| k7symbolisch | 3×3-Raster füllt/leert sich, Buchstabenfolge darunter | Schema | (RZ, WW) |
| k7oktal | Rechenbild 750 | Rechenbild | kein F1 |
| k7verzrechte | Verzeichnis als Tabelle Name/Inode, Auge, Stift | Schema | kein F1 (Tabelle) |
| k7loeschen | Tabelle + Datei mit Schlössern | Schema | kein F1 (Schloss) |
| k7pfad | Pfadkette, Punkt wandert | Schema | kein F1 |
| k7entscheidung | Entscheidungsbaum | Schema | kein F1 |
| k7oeffnen | Zeitachse `tail -f` / zweites Terminal / `cat` | Schema | (Mini-TF) |
| k7sudo | Shell uid → sudo hakt 3 Stationen ab → whoami uid 0 | Schema | kein F1 (Passwort: Abschnitt 4) |
| k7sudoers | Regel `%sudo ALL=(ALL:ALL) ALL`, 4 Teile leuchten, Pfeil → `sudo:x:27:student` | Raster | RZ, FE(freie Bereiche), HV, AN, DA |
| k7sudofalle | 2 Befehlszeilen, Ablauf Shell/sudo/tee | Schema | (RZ, AN) |
| k7susudo | `su -` gegen `sudo`, Passwortfeld durchgestrichen | Schema | kein F1 (Abschnitt 4) |
| k7adduser | Befehl in der Mitte, neue Zeilen in passwd/group/shadow, `/home/anna` | Raster | DA (×3), ZA (Zeile kommt hinzu), HV, AN |
| k7usermod | Gruppenlisten, gestrichen, Schloss | Schema | kein F1 |
| k7zweiquellen | `/etc/group` mit neuer Zeile, Shell-Etikett | Schema | (DA, HV, AN) |
| k7umask | Rechenbild | Rechenbild | kein F1 |
| k7undnicht | Rechenbild | Rechenbild | kein F1 |
| k7suid | `rwsr-xr-x` (s leuchtet), 0 wandert vom Besitzerfeld | Schema | (RZ, HV Einzelzeichen, KO) |
| k7sgid | zwei Verzeichnisse, Gruppe wandert | Schema | kein F1 |
| k7sticky | Tabelle `ablage`, Einträge streichen | Schema | kein F1 |
| k7vierziffern | Rechenbild 2775 → `rwxrwsr-x` | Rechenbild | (WW x → s) |

### Kapitel 8 (30)
| Szene | Kurzinhalt | Art | Funktionen |
|---|---|---|---|
| k8zeitteilung | Kern, Prozesse A/B/C, Zeitleiste | Schema | kein F1 |
| k8pidvergabe | Zähler „nächste PID“ (L3) | Schema | kein F1 |
| k8forkexec | zwei Spuren, fork/exec | Schema | kein F1 |
| k8baum | Prozessbaum (gezeichnet, nicht pstree) | Schema | kein F1 |
| k8psspalten | `ps aux`-Zeile (77 Z.) in 11 Spalten zerlegt; Pfeile zu den Spalten von `ps -ef` | Raster | RZ (2 Zeilen), FE(Leerraum), HV, AN |
| k8zustaende | fünf Zustandskreise | Schema | kein F1 |
| k8zombie | zwei Zeitleisten, Grabstein | Schema | kein F1 |
| k8procstatus | zwei `Uid:`-Zeilen (36 Z., Tabs), Spaltennamen, 0 wandert nach „gespeichert“ | Raster | RZ, FE, HV (grau), KO, AN |
| k8vordergrund | Zeitleisten, Prompt grau/aktiv, Tastaturpfeil | Schema | (RZ mit Grau, CU) |
| k8jobliste | `[2]+ 656 Running sleep 301 &` zerlegt (6 Teile), Job 1 darunter, `%+`/`%-` | Raster | RZ, FE, HV, AN |
| k8hintergrundlesen | Terminal mit Tastatur; `cat` angehalten; `fg`; „Hallo“ tippen, Echo | Fenster | TF, TI, ZA, CU, KO („Hallo“ wandert), AN |
| k8jobzustaende | drei Felder, Job-Kärtchen wandert (Strg+Z, bg, fg, Strg+C) | Schema | (TK) |
| k8signal | Tastatur Strg+C (grau), kill → Kärtchen → Kernel | Schema | (TK) |
| k8termkill | SIGTERM gegen SIGKILL | Schema | kein F1 |
| k8exitrechnung | Rechenbild 128 + n | Rechenbild | kein F1 |
| k8wer | Benutzernummern Absender/Ziel | Schema | kein F1 |
| k8trap | Reaktionstabelle mit Schlössern | Schema | kein F1 (Schloss) |
| k8timeout | Uhr 0–3 s, Zeitleiste | Schema | kein F1 |
| k8sighup | Terminalfenster mit Shell und 2 Jobs; Fenster zu (×); Signalkette | Fenster | TF, TL, RZ-Inhalt, AN |
| k8nohup | 3 Job-Kärtchen; Fenster wird geschlossen | Schema + Fenster | TL (Rahmen + schließen), sonst Schema |
| k8last | Lastdiagramm (L3) | Diagramm | kein F1 |
| k8lastrechnung | Rechenbild | Rechenbild | kein F1 |
| k8niceanteil | Rechenbild + Balken | Rechenbild | kein F1 |
| k8dienst | zwei Prozesse im Vergleich | Schema | kein F1 |
| k8unitdatei | Unit-Datei von cron (16 Z. × ≤ 56 Sp.), 3 Abschnitte leuchten, Pfeile ExecStart/WantedBy | Raster | DA, HV (Zeilenbereich), AN |
| k8neustart | systemd startet neu | Schema | kein F1 |
| k8enable | zwei Schalter, Link-Verzeichnis | Schema | kein F1 (Schalter: Abschnitt 4) |
| k8journal | Quellen → journald → Ablagen | Schema | kein F1 |
| k8journalfolgen | zwei Terminalfenster: links `journalctl -f` wartet, rechts `restart` getippt, links 3 Zeilen nacheinander, Strg+C | Fenster | TF ×2, TL (Titel), TI, ZA, CU, `^C`, KZ, AN, (TK) |
| k8journalrechte | zwei Ablagen, drei Leser, `adm`-Zeile | Schema | (RZ/DA, HV) |

## 2. Funktionsliste F1, nach Häufigkeit
| # | Funktion | Szenen (Pflicht + optional) | Beispiele | Stufe |
|---|---|---|---|---|
| 1 | **Raster-/Textblock** ohne Fenster: mehrzeilig, feste Zellen, `x(spalte)`, `mitte(a, b)`, mehrere Leerzeichen bleiben; ein `<text>` je Zeile mit Abschnitten | 13 + 8 | k7passwd, k8psspalten | Pflicht |
| 2 | **Anker**: Zeile, Feld oder Bereich → Szenenkoordinaten (Kanten und Mitte) für Pfeile und Linien, auch aus einem Fenster heraus | 13 + 4 | k7gruppen (Feld 4 → Gruppe), k8journalfolgen | Pflicht |
| 3 | **Hervorheben** eines Bereichs (Spalten a–b oder ganzer Zeilen): Hinterlegung, leuchten (BETONE), Teilfarbe; „Rest grau“ | 10 + 5 | k7passwd (Doppelpunkte nacheinander), k7spalte | Pflicht |
| 4 | **Felder finden + Klammer**: Felder nach Trennzeichen (`:`) oder Leerraum, Klammer über/unter a–b mit Beschriftung (`s.tr`), auch für Einzelzeichen | 7 + 1 | k8psspalten (11), k7spalte (3 + 9) | Pflicht |
| 5 | **Datei-Ansicht**: Textblock mit Rahmen und Dateiname als Titel; eine Zeile kommt hinzu oder leuchtet | 5 + 3 | k7adduser (3 Dateien), k8unitdatei | Pflicht |
| 6 | **zeilenweise Ausgabe**: neue Zeile unten einblenden, Cursor springt mit | 4 | k8journalfolgen, k7adduser | Pflicht |
| 7 | **Terminalfenster**: Rahmen, Inhaltsbereich mit Raster (Nr. 1), Prompt | 3 + 2 | k8hintergrundlesen, k8sighup | Pflicht |
| 8 | **Teil löst sich**: deckungsgleiche Kopie eines Spaltenbereichs als eigenes Objekt (wandern, ersetzen) | 3 + 1 | k8procstatus (0 → „gespeichert“), k7besitz | Pflicht |
| 9 | **Titelleiste mit Titel und ×**, Fenster als Gruppe ein- und ausblenden, schließen | 3 | k8sighup, k8nohup | Pflicht |
| 10 | **Tippen**: Zeichen für Zeichen, Cursor läuft mit, Eingabetaste | 2 | k8journalfolgen (`systemctl --user restart …`), k8hintergrundlesen („Hallo“) | Pflicht |
| 11 | **Cursor**: Block, blinkt 2–3-mal („wartet“), dann ruhig, aus beim Ende | 2 + 1 | k8journalfolgen, k8vordergrund | Pflicht |
| 12 | **Wert wechselt an fester Spalte** (`s.ersetzen` auf einen Teil, Rest bleibt stehen) | 1 + 2 | k7besitz (1000 → student), k7vierziffern | Pflicht (klein) |
| 13 | **Zeile kürzen** mit `…` am Ende oder in der Mitte | 1 | k8journalfolgen (84 Z. in ≈ 38 Sp.) | Pflicht, nur bei „nebeneinander“ (Frage 3) |
| 14 | Schriftgröße aus Spalten × Breite, Warnung unter der Mindestgröße | alle Raster/Fenster | – | Pflicht (Leitplanke) |
| 15 | Editor: Palette-Eintrag „Terminal / Textblock“, Inhalt als Textfeld; Vertragstest Export = Editor | – | – | Pflicht (Leitplanke) |
| 16 | **Tastenkappe** (Strg+C, Strg+Z, Eingabe; Strg/Ctrl je Sprache), ohne Druckanimation | 0 + 4 | k8jobzustaende, k8signal | Kür (`taste()` aus `linux_teil2.py` nach `linux_hilfen.py` genügt) |
| 17 | Tabulator → Leerzeichen (Tabstopp 8) | 0 + 1 | k8procstatus (Heftblock schon mit Leerzeichen) | Kür |
| 18 | Inhalt aus dem **Heftblock** lesen (`.tex`, erste Befehlszeile als Schlüssel) | 0 | alle Raster/Fenster | Kür (Text einfügen genügt, 1–16 Zeilen je Szene) |

### Genaue Anforderungen
| Punkt | Bedarf aus den Szenen |
|---|---|
| Spalten | Rasterzeilen 25–77 Zeichen: sudoers 25, Uid 36, passwd 44, adduser 47, `jobs -l` 49, `ls -l` 56, Unit-Datei 56, `ps -ef` 62, `id` 65, `ps aux` 77. Fensterinhalt: Journalzeile 84, Befehle 37–41. Standardbreite 72 (Pseudoterminal der Sitzungen). |
| Zeilen | Raster 1–3 Zeilen, Unit-Datei 16. Fenster: k8journalfolgen links 6 (Befehl, alte Zeile, 3 neue, `^C`), rechts 2; k8hintergrundlesen ≈ 4–8; k8sighup ≈ 6 (`$ sleep 901 &`, `[1] 732`, angehaltener Job im Format `[n]+  Stopped …` wie in der Mitschrift `s3_strgz`). Kein Fenster braucht mehr als 8 Zeilen, also kein Rollen. |
| Schriftgröße | Bisher genutzt: 17,7–22 Szenenpixel; die kleinste ist 17,7 (k6, `E2 = 0.15`). Damit passen über die ganze Breite (548 px) höchstens ≈ 85 Spalten, je Fenster nebeneinander ≈ 38. |
| Prompt | `$ ` (Kurzform wie in Heft und Linux 2–6) in allen Szenen. Die Langform `student@labor:~/linuxk8$` nur als Fenstertitel `student@labor: ~/linuxk8`. `#`/root: keine Szene (Kür: Prompt frei wählbar). |
| Farben und Attribute | Kein ANSI, kein fett/invers/unterstrichen. Teilfarben aus der Szenenpalette: SCHWARZ, GRAU (ausgegraut), ORANGE (Hervorhebung, `^C`), GRUEN/ROT (erlaubt/verboten), BLAU. Hinterlegung mit Deckkraft 0,25–0,4 wie `mark`. Cursor als Block (DUNKEL) wie in k6tailf. |
| Vollbild-Programme | keine (`top`, `less`, `nano` und `systemctl status` kommen in keiner Szene vor) |
| Unicode | Umlaute (`Eieruhr zum Üben` in den Journalzeilen) und `…` (Kürzung; k7spalte „25 … einkauf.txt“). Sonst ASCII inklusive `% & $ ! ' " [ ] + \| > ~ ^ : = ( ) ,`. Keine Rahmenzeichen (`└─`, `───`), kein `●`/`○`. |
| Sprachen | Raster- und Fensterinhalt sowie Fenstertitel sind in allen Sprachen gleich (roh). Beschriftungen laufen über `s.tr`. |

### Animationsarten
| Art | Szenen | Anforderung |
|---|---|---|
| Tippen | k8journalfolgen, k8hintergrundlesen | Tempo einstellbar; als Textersatz (Spur `h`) oder Abdeckung, nicht ein Objekt je Zeichen |
| Zeilenweise Ausgabe | k8journalfolgen (3 Zeilen einzeln), k8hintergrundlesen, k8sighup, k7adduser | Zeile erscheint, nichts rückt |
| Rollen | – | nicht nötig |
| Wert ändert sich | k7besitz, (k7symbolisch, k7vierziffern) | Teil an fester Spalte ersetzen |
| Teil wandert | k8procstatus, k7besitz, k8hintergrundlesen, (k7suid) | Kopie startet deckungsgleich |
| Leuchten / ausgrauen | k7passwd, k7spalte, k7sudoers, k8psspalten, k8unitdatei, k8journalfolgen | Bereich a–b oder Zeilenbereich; nacheinander |
| Cursor wartet | k8journalfolgen, k8hintergrundlesen, (k8vordergrund) | blinken, dann ruhig |
| Fenster öffnen/schließen | k8journalfolgen, k8sighup, k8nohup | als Gruppe; schließen: × leuchtet, Fenster blendet aus |

## 3. Nicht nötig für Linux 7/8 (Vorrat)
| Teil des Plans | später für |
|---|---|
| ANSI-Farben 16/256, fett/invers/unterstrichen | Linux 9 (apt-Ausgaben), Linux 10 (`grep --color`, ShellCheck, `bash -x`), Cyber (git diff, Scanner), Nachrüstung k6grep/k6diff. Dafür müsste `sitzung.py` die Rohausgabe zusätzlich speichern. |
| TUI: `top`, `less`/`man`, `nano`, whiptail, Bootmenü | Linux 10 (nano für Skripte), Linux 11 (tmux mit Statusleiste und Bereichen), Nachrüstung Linux 1 (Installer, Bootmenü), Linux 8 nur bei Zusatzszenen (Frage 1) |
| Rollen | Linux 9 (`apt update/upgrade`), Linux 10 (Schleifenausgaben) |
| Shell-Bedienung: markieren, Tab-Vervollständigung, Verlauf ↑, Strg+R | Nachrüstung Linux 2 (k2tab, k2verlauf, k2rsuche, k2tasten), Linux 10/11 |
| Mitschrift-Import mit festgelegten Uhrzeiten/PIDs | ab Heften, deren Blöcke aus einem einzigen Lauf stammen (Linux 9–11, Cyber). Für Kap. 8 ungeeignet (siehe Kurzbefund). |
| Stile Ubuntu, PowerShell/Windows-Terminal | Linux 1 (WSL-Einrichtung), Linux 11 (ssh von Windows), Python 1 (Einrichtung) |
| Maus (Zeiger, Klick, Ziehen), Tasten mit Druckanimation und Tastenfolgen | F3/F4 (Linux 1: VirtualBox-Assistent; Cyber: Browser, Phishing), Linux 11 (tmux-Präfix) |
| Lupe, Scheinwerfer, nummerierte Schrittmarken | Cyber (ähnliche Domains), Dialoge in F3 (Ausgrauen geht heute mit `schleier`) |
| Ausschnitt mit ausgeblendeter Kante, 2D-Zoom | Linux 9 (lange Ausgaben), Cyber (Browser) |
| Leisten, Steuerelemente, Formular, Wörterbuch für Oberflächenwörter, Symbolsatz (außer Schloss und ×) | F3/F4 |
| mehrere überlappende Fenster mit Fokus, Desktop | Linux 11 (lokal/entfernt), Cyber |

## 4. Benötigtes außerhalb von F1
| Bedarf | Szenen | Vorschlag |
|---|---|---|
| Passwortabfrage | k7sudo (Station „Passwort prüfen“), k7susudo (Passwortfeld, durchgestrichen) | Beide Bildunterschriften verlangen nur Schema. Bei Bedarf als Rasterzeile `[sudo: authenticate] Password: ****` bzw. `Password:`, mit Tippen (Option `verdeckt="*"` oder ohne Echo). Kein F3-Textfeld. |
| Schloss (offen/zu) | k7loeschen, k7usermod, k8termkill, k8trap, k8journalrechte | klein in F1 mitnehmen (Teil des Symbolsatzes, zusammen mit dem × der Titelleiste) |
| Auge, Stift, Startknopf, Grabstein, Telefonhörer, Pause, Eintrittskarte | k7rwx, k7verzrechte, k8zombie, k8sighup, k8hintergrundlesen, k7oeffnen | als Helfer in `linux_hilfen.py` (zu speziell für F1) |
| Schalter an/aus | k8enable | vorerst Grundformen in der Szene (Kasten, Kreis, VER); das Steuerelement bleibt F3 |
| Tabelle mit Kopf (Name/Inode, Reaktionstabelle, `ablage`) | k7verzrechte, k7loeschen, k7sticky, k8trap | vorerst wie `k3tabelle` aus Kästen und Text; die Tabellen-Vorlage bleibt F3 |
| Eigenschaften-Dialog mit Rechten | keine Szene (nur im Plan unter „Ausgangslage“) | bleibt F3 |
| Tastatur, Prozesskarten, Etiketten, Kernel-Fläche, Zähler/Uhr | viele | schon vorhanden (`linux_hilfen.py`, L3) |

## 5. Pilotszenen
| Kap. | Datei, Funktion | Szene | Handfassung heute | prüft | Muster für |
|---|---|---|---|---|---|
| 2 | `tools/szenen/linux_teil2.py`, `k2sitzungen()` (Z. 331) | `linux/k2sitzungen` | 35 Zeilen Code, Formel-tt, 114 KB `.svg` / 139 KB `.anim.svg` | zwei Fenster mit Titel, Prompt in Langform wechselt mit `cd`, Befehl erscheint, Shell endet (Schleier) | k8journalfolgen, k8sighup, k8nohup |
| 4 | `tools/szenen/linux_teil4.py`, `k4cateingabe()` (Z. 149) | `linux/k4cateingabe` | 52 Zeilen, Formel-tt, 79 / 116 KB | Terminal mit Tastatur, „Hallo“ getippt, Echo, Strg+D, Prompt zurück, Anker für die Ströme, Teil wandert | k8hintergrundlesen (fast dieselbe Handlung) |
| 6 | `tools/szenen/linux_teil6.py`, `k6awkfelder()` (Z. 1492) | `linux/k6awkfelder` | 47 Zeilen, Text-tt, 11 / 21 KB | Zeile nach Trennzeichen in Felder zerlegt, Trennzeichen leuchten, Klammer + Beschriftung je Feld, Pfeil auf ein Feld | k7passwd (fast gleich), k7gruppen, k7sudoers, k8psspalten, k8jobliste, k8procstatus |

Begründung der Auswahl:
- k6awkfelder steht für den häufigsten Bedarf (10 Raster-Szenen), die beiden anderen für drei der vier Fenster-Szenen.
- Zusammen prüfen sie die Funktionen 1–4, 6–8, 10 und Fenstertitel (aus 9).
- Nicht abgedeckt sind Datei-Ansicht (5), Cursor (11) und Wertwechsel (12). Die ersten beiden bringt der Ersatz k6tailf mit.

Ersatz:
- `k2id` statt `k2sitzungen`, wenn zuerst nur das Raster geprüft werden soll.
- `k6tailf` statt `k6awkfelder`, wenn wartender Cursor, neue Zeile, `^C` und Datei-Ansicht im Vordergrund stehen sollen (Muster für k8journalfolgen).

Hinweis zum Vergleich: k2 und k4 nutzen noch Formel-tt. Ein großer Teil ihres Größengewinns käme schon von `schreibmaschine("text")`. Deshalb den Gewinn durch F1 getrennt ausweisen (Codezeilen, Spaltengenauigkeit). Für die Größe aussagekräftig ist k6, das schon Text-tt nutzt.

Nicht im Pilot abgedeckt, weil es in Kap. 2–6 keine Vorlage gibt: Fenster mit × schließen und Zeilen kürzen. Beides wird an der ersten neuen Szene (`k8sighup`, `k8journalfolgen`) geprüft.

## 6. Offene Fragen an den User
1. **Umfang:** Die 58 Szenen brauchen kein `top`/`systemctl status`-Bild und keine Farben. F1 schlank bauen (Raster, Datei-Ansicht, kleines Terminalfenster mit Titelleiste) und TUI/ANSI/Import/Maus/Lupe als Vorrat lassen? Oder für Linux 8 zusätzliche Bildschirm-Szenen aufnehmen (etwa `top` mit sich ändernden Werten in 2.7, `systemctl status cron` mit `●`/`└─` in 7.4)? Dann gehören TUI `top` und Rahmenzeichen in F1. Empfehlung: schlank.
2. **Stil:** Terminal hell wie in Linux 2–6 (Hintergrund `#f6f6f4`, grauer Rahmen, schlanke Titelleiste nur mit Titel und ×)? Oder an Ubuntu angelehnt (dunkel, Titelleiste mit –, □, ×)? Empfehlung: hell, einheitlich mit den vorhandenen Linux-Bildern.
3. **k8journalfolgen:** Fenster nebeneinander wie in der Bildunterschrift? Dann werden die Journalzeilen auf ≈ 38 Spalten gekürzt, etwa `Nov 10 15:29:25 … Stopping …`, und „Zeile kürzen“ wird Pflicht. Oder untereinander mit dem vollen Wortlaut (84 Spalten) und angepasster Bildunterschrift?
