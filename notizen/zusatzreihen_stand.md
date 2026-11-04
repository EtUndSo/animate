# Stand der Zusatzreihen Cybersecurity und Machine Learning (ab 04.11.2026)

Auftrag je Heft: `heft_auftrag_zusatzreihen.md`, Regeln: `UEBERARBEITUNG.md`. Es schreibt immer nur ein Agent (Opus); Recherche-Unteragenten höchstens 3 gleichzeitig auf Sonnet. Zuerst nur Deutsch, Übersetzungen erst nach Freigabe der Reihe durch den User.

Reihenfolge: Pilot cyber 1, ml 1 → Abnahme durch den User → danach abwechselnd ein Cybersecurity-Heft, ein ML-Heft; erst der Stamm (cyber T01–T14, ml T01–T22), dann die Äste (cyber A zuerst, G vorletzt, H zuletzt; ml A → B → F, E parallel, C, D, G).

## Infrastruktur (04.11.2026)
- Heftordner `C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte`, `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte`, je mit `praeambel.tex`: Kästen wie ET3 (hintergrund, herleitung, beweis, kernbox, aufgabe …), neu `warnung` (immer offen), Code-Umgebungen `konsole bash python ccode cppcode asm gas ausgabe` (listings, Inconsolata, optionaler Titel), TikZ-Stile `blk geraet zelle fluss kn`; ML zusätzlich Makros `\vx \mX \T \E \Var \argmin …` nach den Notationsentscheidungen.
- `tools/heft_zu_artikel.py`: Module `cyber` und `ml` (Pfad „Informatik / Cybersecurity“ bzw. „Informatik / Machine Learning“ in vier Sprachen, alle Stamm-Hefte eingetragen, Äste später ab Nummer 101). Code-Umgebungen werden zu ```` ```<sprache> <titel> ````-Blöcken (bis zum Schluss als Platzhalter, damit kein Textschritt den Code verändert), `%` in Code, `\verb`, `\lstinline` und `\url` ist kein Kommentar mehr, `\texttt` setzt Sonderzeichen richtig, `warnung` → `:::warnung`, Makros ohne Argument kommen aus der Modul-Präambel, eigener Lesehinweis je Reihe, Teil-Links nur auf vorhandene Hefte, fehlende Hefte werden übersprungen, KaTeX-Prüfung ohne Code-Blöcke. Rückwärtsprüfung an et3/hm3/gemb1/et1/hm1: Ausgabe unverändert.
- `build_wissen.py`: Code-Blöcke mit Kopfzeile (Titel, Sprache) und Farben über Pygments (Tag und Nacht, Prompt nicht markierbar), Kasten `:::warnung` („Achtung“, rot), UI-Wörter warnung/konsole in vier Sprachen.
- Szenen-Gerüste `tools/szenen/cyber_teil1.py`, `tools/szenen/ml_teil1.py`.
- Prüfumgebung (nur für die Agenten, nur auf dem Rechner des Users): Ubuntu 26.04 LTS unter WSL 2 (`student@labor`, sudo ohne Passwort, systemd, Werkzeuge siehe Auftrag; uutils coreutils und sudo-rs!), dazu Git Bash, MinGW gcc/g++/gdb, CMake, Python 3.13 mit NumPy 2.3 und scikit-learn 1.9, kein PyTorch.
- Regel des Users (04.11.2026): Die Leser richten ihre Übungsumgebung selbst nach den Anleitungen der Hefte ein; die Website stellt keine Umgebung bereit (keine Online-Terminals/Sandboxes), wegen der Sicherheitsrisiken.

## Hefte

| Reihe | Teil | Thema | Stand |
|---|---|---|---|
| cyber | 1 | Sicherheit, Schutzziele und Spielregeln | fertig 04.11. (68 S., 10 Abschnitte, 20 Aufgaben, 8 Abb.; Website de gebaut), wartet auf Abnahme |
| ml | 1 | Vektoren und Matrizen | Pilot in Arbeit |

Hinweis cyber 1: Die Sitzung, die den Schreib-Agenten gestartet hatte, wurde kurz vor seinem Bericht beendet. Schlussprüfung deshalb vom Haupt-Agenten: PDF 0 Fehler, keine Overfull-Boxen, Konverter 0 KaTeX-Fehler, Szenen neu exportiert und angesehen, Rechtsteil gegen die Recherche-Notizen geprüft (Wortlaute, Strafrahmen, §§ 205/303c, BVerfG 2009, Reformstand). Recherche-Notizen des Agenten: `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\cb2b5ccc-18ac-4325-87ef-8fa3464a919a\scratchpad\cyberk1\recherche_notizen.md` (temporär).

## Entscheidungen des Users (04.11.2026)
- Eigene Zusammenfassungen in `C:\Bücher\allgemeineThemen` werden nicht korrigiert; es geht nur um die Website.
- ML-Ast F6 (TinyML) wird allgemein für einen typischen Mikrocontroller geschrieben, nicht für ein bestimmtes Board des Users.
- Linux zum Testen: ja → Ubuntu 26.04 unter WSL.
