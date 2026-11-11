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
| 2 | prog | 2 | Kap2_Werte.tex | fertig 11.11. (12 Artikel, 87 S.) |
| 3 | prog | 3 | Kap3_Kontrollfluss.tex | fertig 11.11. (11 Artikel, 83 S.) |
| 4 | linux | 1 | Kap1_Uebungslinux.tex | fertig 11.11. (11 Artikel, 62 S., 13 Abbildungen en neu) |
| 5 | linux | 2 | Kap2_Shell.tex | fertig 11.11. (9 Artikel, 60 S.; nach Netzabbruch fortgesetzt) |
| 6 | linux | 3 | Kap3_Dateien.tex | läuft seit 11.11. |
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
6. Nach dem letzten Kapitel: alle en-Fassungen der Schleife neu umwandeln, damit Verweise auf später übersetzte Kapitel Links werden (nur Link-Unterschiede erlaubt, wie bei den Linux-Heften), bauen, dann Schleife beenden. **Danach (User 11.11.):** erst die Editor-Änderungen für Bildschirme und Fenster (`notizen/editor_bildschirme_plan.md`, Welle F1, effizient nach dem Abschnitt „Effizient umsetzen“; vorher mit dem User den Weg abstimmen), dann Linux 7 2b, 8 2b-1, 8 2b-2 mit dem neuen Terminal.

## Fehler im deutschen Original (von Übersetzern gemeldet, gesammelt)
- Python 1: keine.
- Python 3: keine.
- Linux 2 (von mir behoben 11.11., PDF und Artikel de neu): `kap2_loesungen.tex` Z. 281 Speicher und Kerne „die du der Maschine zugeteilt hast“ gilt nur für die VM; im Live-System die des Rechners.
- Linux 1 (von mir behoben 11.11., PDFs de/en und Artikel neu): `kap1_stufen.tex` Z. 219 „In den Jahren dazwischen erscheinen Zwischenversionen“ → „Dazwischen …“ (Zwischenversionen auch im Oktober von LTS-Jahren). Dazu en-Titel „A Linux to Practise On“ → „Practice“ (amerikanisch) in `MODULE["linux"]` und `Kap1_Uebungslinux_en.tex`.
- Python 2 (von mir im Deutschen behoben 11.11., PDF und Artikel de neu gebaut): `kap2_stufen_b.tex` Z. 239 alte Verweisform „Python~1“ → „Kapitel~1, Abschnitt~5.3“ (jetzt Link); Z. 1317 IEEE 754 rundet „bei Gleichstand“ zur geraden Mantisse; `kap2_loesungen.tex` Z. 809 falsche Begründung (−1,5 + 0,5 = −1,0, `int` schneidet nichts ab) ersetzt.

## Festlegungen aus den Durchgängen
- Python 1: Zeichenketten im Code bleiben deutsch (ihre Ausgaben stehen im Text und in den Szenen), Kommentare übersetzt; kurze Glosse wie ``Zeile 1'' (German for ``line 1''). „übersetzen“ = translate/translator, nur die Spracheigenschaft heißt compiled/interpreted. Euro als €4.49. Prüfskripte `code_vergleich.py` und `formeln_b.py` im Scratchpad `en_prog1` (verbessert in `en_prog2`, `en_prog3`) (Formelvergleich ohne die `$`-Prompts in Code; das Struktur-Werkzeug meldet dort ein Artefakt).
- Python 3: Flussdiagramme zeigen Programmausgaben wie im Code deutsch (“fertig”, “zu kalt”), mit Glosse im Text; dafür `en=` in `prog_teil3.py` angepasst (es/zh/fr/tr entscheiden ihre Übersetzer). „effektiver Jahreszins“ = effective annual interest rate (nicht APR).

## Brief für den Übersetzer (Vorlage)
Vollständiger Brief des neuesten Durchgangs (seit Python 2, mit den Hilfsmitteln aus Python 1): `notizen/uebersetzung_en_brief.md`. Für jedes Kapitel anpassen: Modul, Kapitel, Dateinamen, Heftordner, Szenen-Datei, Scratchpad `en_<modul><kap>`, Regeln und Glossarort wie folgt, Stilvorbild (für ET-Module die en-Fassungen von HöMa1 1–3).
Platzhalter: {MODUL} {KAP} {HAUPTDATEI} {ORDNER} {REGELN}. {REGELN}:
- prog, linux, cyber, ml: `notizen/heft_uebersetzung.md` und `notizen/uebersetzung_brief_zusatzreihen.md` (Glossar, feste Wendungen); Glossar-Zusätze dort als Block „Ergänzt bei <Modul> <Kap> (en)“.
- hm1: `notizen/heft_uebersetzung.md` und `notizen/heft_uebersetzung_hm1.md`; Vorbild `Kap1_Zahlen_en.tex` usw. im Heftordner; Glossar-Zusätze in `notizen/glossar_en_module.md`, Abschnitt hm1.
- hm3, gemb1: `notizen/heft_uebersetzung.md`, für hm3 zusätzlich die Mathematik-Regeln aus `notizen/heft_uebersetzung_hm1.md`; Vorbild die en-Fassungen von HöMa1 und ET1/ET3; Glossar in `notizen/glossar_en_module.md`, Abschnitt des Moduls (beim ersten Kapitel anlegen).
</content>
