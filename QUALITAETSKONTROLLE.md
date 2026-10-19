# Qualitätskontrolle der Wissensseiten — Feature-Idee (Batch, später umsetzen)

Ziel: Ein Werkzeug, das **alle** erzeugten Wissensseiten automatisch durchgeht und Probleme findet. Zwei
getrennte Funktionen (User-Wunsch 2026-10-19):

## Funktion 1 — Korrektur / Validierung (technische Fehler finden)
Findet Seiten, die **nicht korrekt erstellt** wurden. Beispiel-Bug (vom User gesehen): ein LaTeX-Block wurde
**nicht gerendert** — man sieht nur die Zeichen (Unicode-ähnlich), nicht die Formel.

Zu prüfende Fehlerklassen (teils rein automatisch, teils KI):
- **Nicht gerenderte Formeln:** rohe `$$…$$`/`$…$` im gerenderten HTML; Mathe-Marker (`\frac`, `\sqrt`, `^`,
  `_`, `\sum`, …) außerhalb von `.katex`-Spans; KaTeX-Parse-Fehler (`.katex-error`); Formeln in Feldern, über
  die KaTeX nicht läuft (z. B. frühere `summary`/Lede-Fälle).
- **Struktur/Markup:** Streu-Absätze (`<p>-`), kaputte Listen, leere `:::`-Callouts, defekte Tabellen.
- **Links/Verweise:** tote interne Links, fehlende `:::grafik`-Beschreibung, Platzhalter ohne Inhalt.
- **Build-Konsistenz:** jede `content/*.md` hat genau eine erzeugte HTML, `pfad`/`order` gesetzt, keine
  doppelten Slugs.
Umsetzung: erst ein **deterministischer Linter** (Python über die gebauten HTML/MD, schnell, ohne KI) für die
mechanisch findbaren Fälle; der KI-Pass nur für das, was ein Linter nicht sieht.

## Funktion 2 — Optimierung (Verbesserungsstellen finden) — braucht KI
Findet Stellen, die man **besser bauen** könnte:
- bessere/klarere Erklärungen (Lücken im „Warum", fehlende Herleitungsschritte, zu knappe Stellen),
- **alternative Formeldarstellungen** als didaktischer Mehrwert (z. B. $e^x$ zusätzlich als Reihe
  $\sum x^n/n!$, Euler-Formel, Grenzwert-/Produktformen), weitere passende Grafik-Ideen,
- Konsistenz mit `ARTIKEL_LEITFADEN.md` (Stil, Farbkategorien, Kernteil, keine verbotenen Floskeln).
Umsetzung: KI liest Artikel + Leitfaden und schlägt konkrete Verbesserungen als Report vor (nichts automatisch
überschreiben — Vorschläge zur Durchsicht).

## Status
- Aufgenommen 2026-10-19. **Noch nicht umgesetzt.** Nach dem 1.-Semester-Content und vor/neben der
  Editor-Grafik-Phase sinnvoll. Siehe `ARTIKEL_LEITFADEN.md` (Soll-Standard) als Prüfmaßstab.
