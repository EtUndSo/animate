# Auftrag: Lernkarten und Formelsammlung (bzw. Befehlsübersicht) für ein Heft

Du schreibst für **ein** fertiges Arbeitsheft zwei Dateien zum Lernen: eine Formelsammlung (in Informatik-Reihen eine Befehls- und Syntaxübersicht) und Lernkarten. Welches Heft und was davon schon existiert, steht in deiner Nachricht. Qualität geht vor Tempo.

## Lesen
1. `C:\Users\info\PycharmProjects\pythonanimation\notizen\lernkarten_muster.md` ganz: Kartenarten, Format, Regeln, Website-Anbindung.
2. `notizen/kurzfassung_schleife.md`, Abschnitt „Muster“: nur der Teil **Formelsammlung** (Kurzfassungen entfallen seit 11.11.). Für Informatik der Absatz „Danach Informatik“ (Befehls- und Syntaxübersicht).
3. **Das ganze Heft, alle Stufen-Dateien und die Lösungen.** Alles auf den Karten muss aus den Artikeln beantwortbar sein, Formeln wörtlich wie im Heft.
4. Als Vorbilder:
   - Lernkarten: `C:\Bücher\ET1\Arbeitshefte\kap1_karten.tex` (ein Abschnitt), `karten_def.tex`, `Kap1_Feld_Karten.tex`;
   - Formelsammlung: `C:\Bücher\ET3\Arbeitshefte\kap2_formeln.tex` (ein Abschnitt), `kurz_formeln_def.tex`, `Kap2_Laplace_Formeln.tex`.
5. Welche Artikel es gibt und welchen Schlüssel sie haben: den ersten `stufe`-Anker je Artikel aus dem Heft, sonst Dateiname ohne Nummer. Zur Kontrolle: `content/<modul>/<kapitelordner>/` im Repo, nur lesen.

## Regeln (zusätzlich zum Muster)
- **Fragen immer als ganzer Fragesatz** (User 12.11.: „Die Fragen sollten immer als ganzer Satz geschrieben sein, nicht einfach nur einzelne Begriffe“). Lieber konkret als „Was ist X?“: Die Frage nennt den Zusammenhang, in dem der Begriff gebraucht wird.
- Jeder Fachbegriff (`\fb{…}` bzw. `__…__`) eines Artikels bekommt eine Begriffskarte oder steht im Namen einer passenden Karte.
- Falsche Antworten: genau 3, plausible Fehlvorstellungen, ähnlich lang wie die richtige Antwort. Die Längenprüfung ist Pflicht: Die richtige Antwort darf nicht auffällig oft die längste sein.
- Überblick und „Das Wichtigste“ bekommen keine Karten und keine eigene Formelsammlung.
- Kein Bezug auf Skript, Uni, Vorlesung, Übung, Folien oder Praktikum. Keine Hinweise auf Prüfskripte.
- Seriöser Ton, übliche Wörter.

## Dateien (im Heftordner)
- `kap<N>_formeln.tex` und `kap<N>_karten.tex` (Format laut Muster). Gibt es eine davon schon, nicht anfassen, außer die Nachricht sagt es.
- Prüf-PDFs: `Kap<N>_<Name>_Formeln.tex/.pdf` und `Kap<N>_<Name>_Karten.tex/.pdf`.
  - Fehlen `karten_def.tex` bzw. `kurz_formeln_def.tex` im Heftordner, aus den Vorbildern übernehmen und an die Präambel des Hefts anpassen.
  - Je dreimal `pdflatex`; `python C:\Users\info\PycharmProjects\pythonanimation\tools\pdf_pruefen.py <pdf> <scratch>` muss 0 Stellen melden. Danach aux/log/out/toc löschen.

## Prüfen (Pflicht, mit Skripten im Scratchpad)
- **Formelabgleich:** Jede Formel in Karten und Formelsammlung steht wörtlich oder gleichwertig im Heft; gleichwertige mit Fundstelle. Vorlagen: `scratchpad/karten_et1k1/formelabgleich_karten.py`, `scratchpad/pilot_kurz_et3k2/formelabgleich.py`.
- **Fragen als Satz:** `python scratchpad/karten_fragen_pruefen.py <kap<N>_karten.tex>`. Es zeigt kurze Fragen; jede muss ein ganzer, sinnvoller Fragesatz sein.
- **Längenprüfung der falschen Antworten.**
- Jede Karte einmal gegen die Fundstelle im Heft lesen: Ist sie richtig und ohne Vorgriff?
- Scratchpad: `C:/Users/info/AppData/Local/Temp/claude/d2b859977628cb1f/c5e68cc8-baf1-4782-9760-867850fb6615/scratchpad/`; deine Zwischenstände in einem eigenen Unterordner.

## Grenzen
- Nur die genannten Dateien im Heftordner und der Scratchpad.
- **Nichts im Repo `pythonanimation` ändern** (kein Konverter, kein Build; das mache ich).
- Kein git.
- LaTeX und Python nur mit Write/Edit.
- Kontextregeln: jede Datei einmal mit Write, dann kleine Edits; nicht zur Kontrolle neu lesen; Ausgaben filtern.

## Bericht (knapp, deutsch)
- je Artikel: Schlüssel, Kartenzahl nach Art, Zahl der Formeln;
- Prüfergebnisse (Formelabgleich, Satzprüfung, Längenprüfung, PDF-Seiten, pdf_pruefen);
- drei Beispielkarten im Wortlaut;
- fragliche Stellen im Heft, die dir aufgefallen sind (nicht selbst ändern).
