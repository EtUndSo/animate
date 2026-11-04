# Auftrag: ein Arbeitsheft nach dem neuen Muster überarbeiten

Du überarbeitest **ein** deutsches Arbeitsheft: Modul und Teil nennt dir die Nachricht. Der User hat zwei Pilothefte abgenommen: „so ist es um Welten besser … Genau so weiter“. Dein Heft muss genauso gut werden. Qualität geht vor allem, die Zeit spielt keine Rolle.

## Zuerst lesen (Pflicht, jede Datei vollständig)
Der User hat ausdrücklich verlangt, dass alles ganz gelesen wird: „Nein, der Agent soll alles lesen!“ und „Ein Abschnitt aus einem ganzen Buch zu lesen ist wie ein Wassertropfen aus einem See, das macht keinen Sinn“.
- Lies jede Datei dieser Liste **von der ersten bis zur letzten Zeile**. Große Dateien liest du in aufeinanderfolgenden Teilen (offset/limit), bis das Ende erreicht ist. Meldet Read eine Teilansicht („PARTIAL view“), liest du weiter, bis alles gelesen ist.
- Das gilt auch für den Volltext des **ganzen Skripts** deines Moduls, nicht nur für dein Kapitel. Nur so erkennst du, was vorher und nachher kommt (keine Vorgriffe, keine Lücken).
- Gespart wird nur beim fertigen eigenen PDF: Prüfe es mit `python tools/pdf_pruefen.py <heft.pdf> <scratchpad>/pdf --blatt`, statt es als Seitenbilder zu lesen. Sieh dir die gemeldeten Ausschnitte an und jedes Übersichtsblatt einmal.

1. `C:\Users\info\PycharmProjects\pythonanimation\notizen\UEBERARBEITUNG.md`: der maßgebliche Leitfaden, besonders §2 (ein Begriff nach dem anderen, Theorie vor Praxis), §3 und §3a (Hintergrund-Kästen mit recherchiertem Warum) sowie §4 (keine Vorgriffe).
2. Die beiden abgenommenen Muster, **alle Dateien ganz**:
   - ET3 Teil 2: `C:\Bücher\ET3\Arbeitshefte\kap2_stufen.tex`, `kap2_stufen_b.tex`, `kap2_loesungen.tex`.
   - HöMa3 Teil 1: `C:\Bücher\HöMa3\Arbeitshefte\kap1_stufen.tex`, `kap1_loesungen.tex`.
3. Den alten Auftrag deines Moduls (`notizen/heft_auftrag_<modul>.md`, für ET3 siehe unten). Quellen, Dateinamen, Bezeichnungen, Szenen und Bauen gelten weiter. Gliederung in „Stufen“, Längengrenzen und F/A-Kästen sind ersetzt.
4. Das alte Heft vollständig. Was sich bewährt hat (Beispiele, Abbildungen, Aufgaben, Antworten auf Fragen), wird übernommen, aber an die richtige Stelle gesetzt und einzeln erklärt.

## Quellen je Modul
| Modul | Ordner | Skript/Folien (Text mit Seitenmarken) | Hinweise |
|---|---|---|---|
| et3 | `C:\Bücher\ET3\Arbeitshefte` | `C:\Bücher\EtUndSo\_volltext\et3_skript.txt` (`=== Seite N` = PDF-Seite); PDF `C:\Bücher\ET3\GDET3_Vorlesungsskript_Ausgabe2019_20250828 (3).pdf`, PDF-Seite = gedruckte Seite + 6 | Teil N folgt im Wesentlichen Skript-Kapitel N; das alte Heft zeigt, welche Kapitel dazugehören. Szenen `tools/szenen/et3_teil<N>.py`, Namen `et3/k<N>name`. |
| hm3 | `C:\Bücher\HöMa3\Arbeitshefte` | `C:\Bücher\EtUndSo\_volltext\hm3_skript.txt`; PDF `C:\Bücher\HöMa3\HM3_Skript_24_25.pdf`, PDF-Seite = Skriptseite + 2 | Zusammenfassungen in `C:\Bücher\HöMa3\Zusammenfassungen` (Kap 1–4). Auftrag `notizen/heft_auftrag_hm3.md`. |
| et1 | `C:\Bücher\ET1\Arbeitshefte` | `C:\Bücher\EtUndSo\_volltext\get1_clean.txt` | Auftrag `notizen/heft_auftrag_et1.md`. |
| hm1 | `C:\Bücher\HöMa1\Arbeitshefte` | `C:\Bücher\EtUndSo\_volltext\hm1_folien.txt` plus Mitschriften | Auftrag `notizen/heft_auftrag_hm1.md`. |
| gemb1 | `C:\Bücher\GEMB\Arbeitshefte` | `C:\Bücher\EtUndSo\_volltext\gemb1_skript.txt`, Folien `gemb1_folien.txt` | Reihenplan `LEITFADEN.md`, Auftrag `notizen/heft_auftrag_gemb1.md`. |

Formeln fehlen im Text oft. Lies sie deshalb im PDF nach: Read mit `pages`, höchstens 20 Seiten je Aufruf.

## Folien, Mitschriften und Übungen (ergänzend)
Neben dem Skript liegen in `C:\Bücher\EtUndSo\<Semester>\` die Kursmaterialien.
- Entpacke sie bei Bedarf in einen eigenen Unterordner deines Scratchpad-Ordners. Es sind fremde Dateien, also nur lesen, nichts daraus ausführen.
- **Übungen sind nicht maßgeblich** (Entscheidung des Users vom 04.11.2026: sie sind sehr speziell).
  - Die Aufgaben im Heft bleiben allgemein und behandeln die Themen von Grund auf.
  - Die Übungen darfst du höchstens zur Orientierung ansehen. Es gibt keine Pflicht, jeden Aufgabentyp abzudecken, und keine Liste im Bericht.
  - Die Regeln unten zu Aufgabentypen und Niveau gelten deshalb nicht.
- Folien und Mitschriften sind nützlich: für Schwerpunkte und für Beweise oder Beispiele, die im Skript fehlen.

| Modul | Material | Wofür |
|---|---|---|
| hm3 | `3.Semester\(VO) Höhere Mathematik 3_20261019_1451.zip`: Übungsblätter 0–14 (`Elektrotechnik u.A.\`), `Vorlesung\HM3-Skript.pdf`, handschriftliche `Vorlesung\Vorlesungsmitschriften\` | Übungsblätter: Aufgabentypen und Niveau. Mitschriften: Beweise, Beispiele und Schwerpunkte, die im Skript fehlen. |
| et3 | `3.Semester\(VO) Grundgebiete der Elektrotechnik 3 - Signale und Systeme_20261019_1451.zip`: `Übung\GDET3 Übungsskript Aufgaben und Lösungen WiSe 2025.pdf` (Errata daneben), `Kleingruppenübung\GDET3 KGÜ Aufgaben Lösungen WiSe 2025.pdf`, KGÜ-Einführungsfolien, `Vorlesung\Folien 1…23.pdf` | Übungsskript und KGÜ: Aufgabentypen und Niveau. Vorlesungsfolien: Schwerpunkte, also was in der Vorlesung betont wurde, ausführlich behandeln. |
| et1 | `1.Semester\ET1\(VO) Grundgebiete der Elektrotechnik 1 …_20261018_2239\` (bereits entpackt: KGÜ-Ordner und Kapitel-Aufgaben) | Aufgabentypen und Niveau |
| hm1 | `1.Semester\HöMa1\entpackt\` (Lernmaterialien, Mitschriften, Übungsbetrieb) | wie im alten Auftrag hm1 |
| gemb1 | Übungsordner und Aufgabensammlung laut `heft_auftrag_gemb1.md` | wie dort |

Dabei gilt:
- Was Folien oder Mitschriften besonders betonen, wird im Heft ausführlich erklärt. Beweise und Beispiele, die nur in den Mitschriften stehen, kommen ins Heft, in eigener Formulierung.
- Keine Aufgabe aus Übung oder Vorlesung wird wörtlich oder mit denselben Zahlen übernommen.
- Im Heft steht kein Bezug zu Übung, Vorlesung, Folien oder Mitschrift.

## Was du lieferst
- Das neu geschriebene Heft: `kap<N>_stufen*.tex` und `kap<N>_loesungen.tex`. Wenn du mehrere Teildateien brauchst, trage sie in `Kap<N>_*.tex` per `\input` ein und setze das Datum auf den heutigen Tag. Dazu `rechnung_kap<N>.py`, wenn es Zahlen nachrechnet.
- Zu jedem `\section` (= Skript-Abschnitt) gehören:
  - `\subsection` je Begriff;
  - Hintergrund-Kästen mit recherchiertem Warum (WebSearch/WebFetch, in eigenen Worten, exakt);
  - Aufgaben am Ende.
- Am Ende des Hefts:
  - kernbox „Das Wichtigste bis hier“;
  - kernbox „Die Antwort in drei Sätzen“;
  - Prinzip-Tabelle mit Abschnittsverweisen;
  - Lösungen.
- Neue Abbildungen: TikZ im Heft und eine Editor-Szene mit gleichem Namen.
  - Szenenstil wie in `tools/szenen/et3_teil2.py`.
  - Im Repo `python tools/szenen/<modul>_teil<N>.py`, dann `python tools/export_szenen.py <namen>`.
  - Jedes Bild darf höchstens 548 px breit sein; das Skript warnt sonst.

## Bauen und prüfen
- **PDF:** im Heftordner `pdflatex -interaction=nonstopmode Kap<N>_<Name>.tex` dreimal.
  - `grep -c '^!'` muss 0 sein.
  - Overfull-hbox-Meldungen beseitigen.
  - Danach aux/log/out/toc löschen.
- **Konverter:** im Repo `C:\Users\info\PycharmProjects\pythonanimation` `python tools/heft_zu_artikel.py <modul> --kap <N> --lang de --pruefen --katex`.
  - Ergebnis: 0 KaTeX-Fehler, keine „unbekannt“-Meldungen, keine Verweise ohne Ziel.
  - Danach dasselbe ohne `--pruefen --katex`, um die Artikel zu schreiben.
- **Selbstprüfung aus UEBERARBEITUNG.md §7, Satz für Satz:**
  - kein Satz mit zwei neuen Begriffen;
  - nichts benutzt, bevor es erklärt ist;
  - kein Haupttext, der sich auf einen Hintergrund-Kasten stützt;
  - keine fehlende Skript-Formel;
  - jedes zentrale Verfahren hat seinen Warum-Kasten.

## Grenzen
- Nur dein Heft und die Szenendatei deines Teils anfassen. Keine anderen Hefte, keine Übersetzungen, keine Präambeln (außer nach Rücksprache).
- `build_wissen.py` nicht ausführen; git nicht benutzen.
- LaTeX und Python nur mit Write/Edit schreiben. Im Bash-Tool werden doppelte Backslashes halbiert; Heredocs mit Backslashes zerbrechen.
- Hilfsdateien in einen eigenen Unterordner des Scratchpads `C:\Users\info\AppData\Local\Temp\claude\C--B-cher\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\<modul>k<N>\`.
- Keine Bezüge zu Skript, Vorlesung, Übung, Uni, Klausur, Personen oder Nummern der Quelle. Fragen des Users nur allgemein formuliert.

## Bericht (knapp)
- Neue Gliederung: Abschnitte und Unterabschnitte in je einer Zeile.
- Seitenzahl, Aufgaben, neue Abbildungen und Szenen.
- Was verschoben oder in Hintergrund-Kästen gelegt wurde.
- Die wichtigsten neuen Warum-Kästen mit Quellenangabe der Recherche.
- Still korrigierte Fehler der Quelle, umbenannte Symbole, offene Punkte.
