# Englisch-Schleife: alle bisherigen Hefte ins Englische (seit 11.11.2026)

Auftrag des Users (11.11.2026): „Lasse den aktuellen Agenten fertig laufen. Starte danach eine loop in der alle bisher erstellten Artikel ins Englische übersetzt werden.“
Entscheidungen des Users (11.11.2026):
- **Erst übersetzen:** Linux 7 und 8 (Phase 2b) warten, bis die Schleife fertig ist. Nur ein Übersetzer zur Zeit, kein anderer Schreib-Agent daneben.
- **HöMa3, Kapitel 3 vorerst auslassen:** Die Überarbeitung ist halb fertig und pausiert. Übersetzt wird erst nach der Überarbeitung.

## Warteschlange (41 Kapitel, in dieser Reihenfolge)
Status: offen · läuft · fertig (Datum, Artikel en, Seiten en). Ein Kapitel gilt als fertig, wenn ich es geprüft und die Website gebaut habe.

| # | Modul | Kap | Hauptdatei (de) | Status |
|---|---|---|---|---|
| 1 | prog | 1 | Kap1_Programme.tex | fertig 11.11. (8 Artikel, 46 S.; „Linux, Chapter 2“ noch ohne Link) |
| 2 | prog | 2 | Kap2_Werte.tex | läuft seit 11.11. |
| 3 | prog | 3 | Kap3_Kontrollfluss.tex | offen |
| 4 | linux | 1 | Kap1_Uebungslinux.tex | offen |
| 5 | linux | 2 | Kap2_Shell.tex | offen |
| 6 | linux | 3 | Kap3_Dateien.tex | offen |
| 7 | linux | 4 | Kap4_Stroeme.tex | offen |
| 8 | linux | 5 | Kap5_Expansion.tex | offen |
| 9 | linux | 6 | Kap6_Textwerkzeuge.tex | offen |
| 10 | cyber | 1 | Kap1_Sicherheit.tex | offen |
| 11 | ml | 4 | Kap4_Wahrscheinlichkeit.tex | offen |
| 12 | ml | 5 | Kap5_Statistik.tex | offen |
| 13 | hm1 | 4 | Kap4_Folgen.tex | offen |
| 14 | hm1 | 5 | Kap5_Stetigkeit.tex | offen |
| 15 | hm1 | 6 | Kap6_Reihen.tex | offen |
| 16 | hm1 | 7 | Kap7_Potenzreihen.tex | offen |
| 17 | hm1 | 8 | Kap8_Vektoren.tex | offen |
| 18 | hm1 | 9 | Kap9_Basen.tex | offen |
| 19 | hm1 | 10 | Kap10_Matrizen.tex | offen |
| 20 | hm3 | 1 | Kap1_Vektorfelder.tex | offen |
| 21 | hm3 | 2 | Kap2_Integrale.tex | offen |
| 22 | hm3 | 4 | Kap4_Koordinaten.tex | offen |
| 23 | hm3 | 5 | Kap5_Integralsaetze.tex | offen |
| 24 | hm3 | 6 | Kap6_Funktionenfolgen.tex | offen |
| 25 | hm3 | 7 | Kap7_Fourier.tex | offen |
| 26 | hm3 | 8 | Kap8_Wahrscheinlichkeit.tex | offen |
| 27–41 | gemb1 | 1–15 | Kap1_Schroedinger.tex … Kap15_MOS.tex (nur die 15 Kapitel mit Artikeln; Kap16, 17, 19 haben noch keine) | offen |

Heftordner: prog `C:\Bücher\EtUndSo\Programmieren\Arbeitshefte`, linux `C:\Bücher\EtUndSo\Linux\Arbeitshefte`, cyber `C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte`, ml `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte`, hm1 `C:\Bücher\HöMa1\Arbeitshefte`, hm3 `C:\Bücher\HöMa3\Arbeitshefte`, gemb1 `C:\Bücher\GEMB\Arbeitshefte`.

## Ablauf je Durchgang (Haupt-Agent)
1. Läuft ein Übersetzer? Dann nichts tun (die Fertigmeldung weckt mich).
2. Bericht des letzten Übersetzers prüfen:
   - `uebersetzung_struktur_check.py` laut Bericht ohne Abweichung; `pdf_pruefen` auf dem en-PDF selbst nachprüfen;
   - `content/<modul>/<kap>/*.en.md`: Zahl = Zahl der deutschen Artikel;
   - grep-Stichproben: keine deutschen Reste (` und `, ` der `, `Abschnitt`, `Aufgabe`), Kästen `:::::vorwissen`, `::::beispiel`;
   - `git status`: nur `content/<modul>/<kap>/*.en.md`, Szenen und `web/abbildungen/en/…` dieses Kapitels sowie Glossar/Notizen geändert.
3. `PYTHONIOENCODING=utf-8 python build_wissen.py`: Die HTML-Menge wächst genau um die en-Seiten des Kapitels. Danach Browser-Stichprobe auf zwei en-Seiten (390 px: HTTP 200, keine Konsolenfehler, kein waagrechtes Scrollen, `[data-anim]` vorhanden).
4. Status oben eintragen, Fehler im deutschen Original unten sammeln, dem User kurz berichten mit Commit-Hinweis (sicher bis zur Repo-Phase des nächsten Übersetzers, siehe Brief).
5. Nächstes Kapitel starten (Brief unten, Platzhalter ersetzen).
6. Nach dem letzten Kapitel: alle en-Fassungen der Schleife neu umwandeln, damit Verweise auf später übersetzte Kapitel Links werden (nur Link-Unterschiede erlaubt, wie bei den Linux-Heften), bauen, dann Schleife beenden und Linux 7 2b starten.

## Fehler im deutschen Original (von Übersetzern gemeldet, gesammelt)
- Python 1: keine.

## Festlegungen aus den Durchgängen
- Python 1: Zeichenketten im Code bleiben deutsch (ihre Ausgaben stehen im Text und in den Szenen), Kommentare übersetzt; kurze Glosse wie ``Zeile 1'' (German for ``line 1''). „übersetzen“ = translate/translator, nur die Spracheigenschaft heißt compiled/interpreted. Euro als €4.49. Prüfskripte `code_vergleich.py` und `formeln_b.py` im Scratchpad `en_prog1` (Formelvergleich ohne die `$`-Prompts in Code; das Struktur-Werkzeug meldet dort ein Artefakt).

## Brief für den Übersetzer (Vorlage)
Vollständiger Brief des neuesten Durchgangs (seit Python 2, mit den Hilfsmitteln aus Python 1): `notizen/uebersetzung_en_brief.md`. Für jedes Kapitel anpassen: Modul, Kapitel, Dateinamen, Heftordner, Szenen-Datei, Scratchpad `en_<modul><kap>`, Regeln und Glossarort wie folgt, Stilvorbild (für ET-Module die en-Fassungen von HöMa1 1–3).
Platzhalter: {MODUL} {KAP} {HAUPTDATEI} {ORDNER} {REGELN}. {REGELN}:
- prog, linux, cyber, ml: `notizen/heft_uebersetzung.md` und `notizen/uebersetzung_brief_zusatzreihen.md` (Glossar, feste Wendungen); Glossar-Zusätze dort als Block „Ergänzt bei <Modul> <Kap> (en)“.
- hm1: `notizen/heft_uebersetzung.md` und `notizen/heft_uebersetzung_hm1.md`; Vorbild `Kap1_Zahlen_en.tex` usw. im Heftordner; Glossar-Zusätze in `notizen/glossar_en_module.md`, Abschnitt hm1.
- hm3, gemb1: `notizen/heft_uebersetzung.md`, für hm3 zusätzlich die Mathematik-Regeln aus `notizen/heft_uebersetzung_hm1.md`; Vorbild die en-Fassungen von HöMa1 und ET1/ET3; Glossar in `notizen/glossar_en_module.md`, Abschnitt des Moduls (beim ersten Kapitel anlegen).
</content>
