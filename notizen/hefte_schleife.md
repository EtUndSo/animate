# Schleife: neue Hefte schreiben (Loop C4, seit 11.11.2026 spät)

Auftrag des Users (11.11.2026, spät abends): „starte die Loop zum Schreiben der Hefte“. Damit läuft C4 aus `aufgabenliste.md` jetzt, parallel zur Editor-Welle F1 (Werkzeug-Agent in eigener Arbeitskopie).

## Regeln (aus `koordination.md`, `heft_auftrag_zusatzreihen.md`)
- **Höchstens ein Schreib-Agent zur Zeit** (Opus). Dazu zählen Phase 1, 2a, 2b und Vorbereitungen wie der Lernpfad-Umbau. Werkzeug-Agenten in Arbeitskopien und Recherche-Agenten zählen nicht.
- **Phasen je Heft:** 1 (Schreiben) → 2a (Prüfen) → 2b (Abbildungen und Bau; ab etwa 30 Szenen 2b-1 und 2b-2).
- **2b erst, wenn F1 eingespielt ist** (F1 eingespielt 12.11., alle Tests grün; **Pilot vom User abgenommen 12.11.**, Datei-Ansicht bleibt hell): Die Terminalbilder entstehen mit dem neuen dunklen, Ubuntu-artigen Terminal (Entscheidung des Users 11.11.). Solange F1 läuft oder nicht eingespielt ist, wartet jedes 2b, und die Schleife zieht stattdessen das nächste Phase 1/2a vor.
- **Vorrang, sobald F1 eingespielt ist:** zuerst die liegengebliebenen 2b von Linux 7 und 8 (Aufgabenliste B9; Linux 8 dabei um echte Bildschirm-Szenen `top`, `systemctl status` erweitern, k8journalfolgen untereinander), dann die 2b der neuen Hefte in Reihenfolge.
- **Nach jedem Bericht:** Prüfroutine aus `koordination.md` (nach Phase 1 nur Lese-Nachweis und Übergabe), Stand unten eintragen, dem User knapp berichten mit Commit-Hinweis, dann den nächsten Schritt beauftragen.
- **Commit-Hinweis:** Sicher nur, wenn kein Agent Dateien im Haupt-Repo ändert (Phase 1/2a schreiben nur in `C:\Bücher`; 2b ändert das Repo) und der Build ohne Warnung lief.
- **Übersetzungen** der fertigen Hefte laufen in eigenen Schleifen (C1 Englisch, C3 weitere Sprachen), nicht hier.

## Warteschlange (Reihenfolge des Users, `zusatzreihen_stand.md` 09.11.)
| # | Schritt | Stand |
|---|---|---|
| 0 | **Cyber-LERNPFAD auf 12 Hefte** umstellen (Vorschlag `Programmieren\Recherche\ZUSAMMENFASSUNG.md`, Entscheidung 06.11.: T03/T04 entfallen, T05 → „Linux-Sicherheit“ als neues Teil 3, T08 → „Python für die Sicherheitsarbeit“, T09 → „Speicherfehler“, T02 → „Schutzgrenzen in Hardware und Betriebssystem“), `MODULE["cyber"]` in `tools/heft_zu_artikel.py` (sechs Sprachen) anpassen, WISSEN-Datei für das neue Teil 2 prüfen und bei Lücken gezielt ergänzen | **fertig 12.11.**: Stamm 12 Teile (Kap1_Sicherheit … Kap12_Webangriffe), `WISSEN_Teil02_schutzgrenzen.md` neu, `MODULE["cyber"]` umgestellt; Sicherung alter Lernpfad `scratchpad/LERNPFAD_cyber_vor_umstellung.md`. Vor dem Schreiben von Teil 2 prüfen: UEFI-Spezifikation (403), SBAT/BlackLotus/`copy_from_user` nur über Zusammenfassungen, BSI-Kennungen Edition 2023 |
| 1 | **Cybersecurity, Kapitel 2** „Schutzgrenzen in Hardware und Betriebssystem“: Phase 1, 2a, 2b | offen |
| 2 | **Linux, Kapitel 9**: Phase 1, 2a, 2b | Phase 1 und **2a fertig 12.11.** (47 Szenen: 2b-1 = Abschnitte 1–5, 24 Szenen; 2b-2 = 6–10, 23 Szenen; 90/92 Blöcke ohne Abweichung, `hello` echt installiert und entfernt, Zustand identisch). **2b: `heft_pruefen.py --ohne-lauf`**, weil unattended-upgrades in der WSL bald 86 Sicherheitsupdates einspielt | 
| 3 | **Linux, Kapitel 10**: Phase 1, 2a, 2b | offen |
| 3a | **Linux, Kapitel 11** „SSH, Dateien übertragen, tmux“: Phase 1, 2a, 2b (User 12.11.: vor Cyber 3, weil dessen OverTheWire-Übungen SSH brauchen) | offen |
| 4 | **Cybersecurity, Kapitel 3** „Linux-Sicherheit“: Phase 1, 2a, 2b | offen |
| 5 | **Cybersecurity, Kapitel 4–5** (Netzwerke): je Phase 1, 2a, 2b | offen |
| 6 | **Cybersecurity, Kapitel 6** (Python für die Sicherheitsarbeit; setzt Python 1–11 voraus, fehlende Python-Hefte vorher), dann **Kapitel 9–12** (Krypto, Web) **vor 7–8** (User 12.11.: „Erst Krypto/Web“); Kapitel 7–8 erst nach der C-Reihe C 1–9 | offen |
| 7 | danach Python 4/5/12/13, ML-Pfad (T08), GEMB1 ab Teil 16 (eigener Auftrag `heft_auftrag_gemb1.md`) | offen |

Wartende 2b (erst nach F1): Linux 7 (2b), Linux 8 (2b-1, 2b-2), dann die 2b der Hefte oben.

## Ablauf je Durchgang
1. Läuft ein Schreib-Agent? Dann nichts tun (die Fertigmeldung weckt die Schleife).
2. Liegt ein neuer Bericht vor: Prüfroutine, Stand eintragen, dem User berichten.
3. Nächsten Schritt wählen: das erste wartende 2b, wenn F1 eingespielt ist; sonst das nächste Phase 1/2a der Warteschlange.
4. Auftrag nach `koordination.md` („Auftrag an einen Schreib-Agenten“) schreiben und starten, Stand eintragen.
5. Ist die Warteschlange leer: Abschluss melden, Schleife beenden.

## Stand
- 11.11.2026 spät: Schleife gestartet; Schritt 0 (Lernpfad-Umbau) läuft. Parallel: Werkzeug-Agent F1 in `scratchpad/wt_f1` (Patch `scratchpad/website_f1/f1.patch`).
- 12.11.2026: Linux 9 Phase 1 gestartet (vorgezogen). Offene Frage an den User: darf `hello` in der WSL einmal echt installiert und wieder entfernt werden? Antwort an den Linux-9-Agenten weitergeben.
- 12.11.2026: Schritt 0 fertig; F1 eingespielt (28 Engine-Tests, 2 JS-Tests, 4 Editor-UI-Tests grün); Linux 9 Phase 1 fertig, 2a läuft. Danach: Linux 7 2b, Linux 8 2b-1/2b-2 (nach Pilot-Abnahme), Cyber 2 Phase 1, Linux 9 2b-1/2b-2.
- 12.11.2026: User-Entscheidungen: F1-Stil passt (Linux 7/8/9 damit, Linux 1–6 im Nachrüst-Loop), Datei-Ansicht hell, Linux 11 vor Cyber 3, Cyber 9–12 vor 7–8. Linux 9 2a nach Netzwerkabbruch fortgesetzt.
- 12.11.2026: Linux 9 2a fertig. **Linux 7 2b läuft** (28 Szenen, F1-Terminal). Danach Linux 8 2b-1/2b-2 (mit neuen Szenen `top`, `systemctl status`), dann Cyber 2 Phase 1, dann Linux 9 2b-1/2b-2.
- 12.11.2026: **Linux 7 2b fertig** (28 Szenen in 6 Sprachen, PDF 69 S., 0 Fehler, pdf_pruefen 1 Fehlalarm `-?????????`; 11 Artikel, URL +11). Von mir: drei Bildunterschriften an die Bilder angepasst (k7adduser, k7usermod, k7zweiquellen), PDF und Artikel neu, Themenkarte-Kopfzeile, Vorschaubild-Fingerabdruck auf LF normalisiert (`tools/vorschaubilder.py`), alle 162 Bilder stabil. **Linux 8 2b-1 läuft** (Abschnitte 1–4, 16 Szenen + neue Bildschirm-Szene `top`).
- 12.11.2026: **Linux 8 2b-1 fertig** (17 Szenen inkl. neuer `k8topbild` in 2.7, 6 Sprachen, 102 Bilder, ohne Warnung; Heftzeilen 23/23 wörtlich). Von mir: Kontaktblatt der Bildschirm-Szenen angesehen, gut. **Linux 8 2b-2 läuft** (14 Szenen + neue `k8statusbild` in 7.4, PDF, Konverter, Build).
- 12.11.2026: **Linux 8 2b-2 fertig, Linux 8 online** (32 Szenen inkl. `k8topbild`, `k8statusbild` (Pager wie `less -F`: 10 von 11 Zeilen), `k8journalfolgen` untereinander; PDF 77 S., 0 Fehler, pdf_pruefen 0; 10 Artikel, Sitemap 1935 → 1945). Fünf Satzreparaturen im Heft (Unicode-Minus, `\verb` mit `|`, `\textbullet`, Backslash, Zeilenumbruch). Von mir: Kontaktblatt, Build, Themenkarte. **Nächster Schritt: Cyber 2 Phase 1.** Wartende 2b danach: Linux 9 (2b-1, 2b-2).
