# Schleife: Lernkarten und Formelsammlung je Heft (Loop C2, seit 12.11.2026)

Auftrag des Users:
- 11.11.: Formelsammlungen für alle Artikel neu erstellen.
- 12.11. zum Lernkarten-Pilot ET1 Kap. 1: „Die Fragen sollten immer als ganzer Satz geschrieben sein, nicht einfach nur einzelne Begriffe. Sonst alles gut, kannst damit dann weitermachen.“
- Kurzfassungen entfallen (11.11. spät).

## Regeln
- **Ein Agent je Heft**, Opus, nach `notizen/karten_formeln_brief.md`. Er schreibt nur in den Heftordner (`kap<N>_formeln.tex`, `kap<N>_karten.tex`, Prüf-PDFs), nie ins Repo.
- **Zweite Spur neben der Hefte-Schleife** (`hefte_schleife.md`), wie früher die Übersetzungen: höchstens ein Agent dieser Schleife zur Zeit.
- **Einspielen mache ich selbst:** Konverter `--kap N`, dann `build_wissen.py`, nur wenn gerade kein 2b-Agent baut (sonst gleichzeitige Builds). Danach kurze Browser-Probe (`/lernen/?m=<modul>&k=N`, Formeln-Ansicht eines Artikels).
- **Muster:**
  - Lernkarten: `lernkarten_muster.md`; Fragen **immer als ganzer Fragesatz**.
  - Formelsammlung: `kurzfassung_schleife.md`, Abschnitt „Muster“, nur der Teil Formelsammlung.
  - Informatik: Befehls- und Syntaxübersicht statt Formeln.
- **Ausgelassen:**
  - HöMa3 Kap. 3 (Überarbeitung angehalten);
  - GEMB1 ab 16 (nie umwandeln);
  - Linux 8 und 9 erst, wenn sie veröffentlicht sind.
- **Nach jedem Heft:** Stand unten eintragen, dem User kurz berichten mit Commit-Hinweis.

## Warteschlange (ET1 zuerst, weil der Pilot dort steht; dann formelreiche Module, dann Informatik)
| # | Heft | braucht | Stand |
|---|---|---|---|
| 1 | ET1 Kap. 1 und 2 | Kap. 1: Formeln (+ kurze Fragen im Pilot konkreter); Kap. 2: Formeln + Karten | **fertig 12.11.** (Kap. 1: 48 Formeln, 12 Fragen konkreter; Kap. 2: 109 Karten, 40 Formeln; alle Prüfungen 0; umgewandelt, Build steht aus bis nach Linux 8 2b-2) |
| 2 | ET1 Kap. 3–11 | je Formeln + Karten | Kap. 3 **fertig 12.11.** (97 Karten, 37 Formeln; + 9 Kap.-1-Fragen konkreter; umgewandelt); **Kap. 4 läuft** |
| 3 | ET3 Kap. 1–3 | je Karten (Formeln fertig) | offen |
| 4 | ET3 Kap. 4–8 | je Formeln + Karten | offen |
| 5 | HöMa1 Kap. 1–10 | je Formeln + Karten | offen |
| 6 | HöMa3 Kap. 1, 2, 4–8 | je Formeln + Karten | offen |
| 7 | ML-Grundlagen 1–5 | je Formeln + Karten | offen |
| 8 | GEMB1 Kap. 1–15 | je Formeln + Karten | offen |
| 9 | Linux 1–7 (später 8, 9 …) | je Übersicht + Karten | offen |
| 10 | Python 1–3 | je Übersicht + Karten | offen |
| 11 | Cybersecurity 1 | Übersicht + Karten | offen |

## Stand
- 12.11.2026: Pilot ET1 Kap. 1 (98 Karten) vom User abgenommen. Build: Kapitel mit geschriebenen Karten zeigen keine automatischen Karten mehr; automatische Karten anderswo haben einen Fragesatz als Vorderseite („Was bedeutet „X“?“).

## Fragliche Stellen in den Heften (von den Karten-Agenten gemeldet, nicht geändert)
- ET1 Kap. 3: „Feldenergie“ und „Zeitkonstante“ nur in der Kernbox des Überblicks als Fachbegriff markiert (Website: in `12-das-wichtigste.md`); Stufe 5 benutzt „Leckstrom“ vor seiner Erklärung (Selbstentladung); Stufe 2 nennt ε_r von Keramik vor Stufe 4 (mit Verweis).
- ET1 Kap. 1–3: Heft-PDFs nennen noch die Prüfskripte („Alle Zahlen rechnet `rechnung_kap<N>.py` nach“); auf der Website filtert der Konverter das.
