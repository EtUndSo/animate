# Bereinigung: keine Quellen- und Veranstaltungsbezüge auf der Website (22.10.2026)

Vorgabe des Users vom 22.10.2026: Auf der gesamten Website darf es keinerlei Hinweis darauf geben, dass Inhalte aus einem
Skript kommen, und auch keine Hinweise auf andere Veranstaltungen wie Vorlesungen oder Praktika („Keine Referenzen
benennen“), weil die Leserinnen und Leser die Vorlagen nicht kennen. Regel: ERKLAER_PROMPT §5.7, Test 20 in §11,
Kalibrierungsfall (k); Prüfwerkzeug `tools/quellen_check.py`. Diese Datei ist zugleich der Marker für LOOP_STIL3 (B1c).

## Ablauf

Sechs Gruppen, nacheinander (Leitfaden §0: keine Parallelität beim Bearbeiten), je ein Agent, danach von mir geprüft und
committet. Protokolle mit jeder Umformulierung (alt/neu), Wortdiffs und Originalen im Scratchpad der Sitzung,
`quellen_bereinigung/lauf1.md` bis `lauf6.md`.

| Gruppe | Dateien | Fundstellen (Werkzeug + zusätzlich) | stillschweigend korrigierte Fehler | Commit |
|---|---|---|---|---|
| 1: ET1 Kap. 2 und 10 (Stil 3) | 10 | 192 + 10 | einige, als Hinweise | 88013e6 |
| 2: ET1 Kap. 11 und 12 (Stil 3) | 12 | 483 + 146 | viele, als Hinweise | 10a4c27 |
| 3a: ET1 Kap. 3 bis 5 | 11 | 239 + 31 | 20 | 09c90fc |
| 3b: ET1 Kap. 6 bis 9 | 10 | 305 + 24 | 47 | 5df1400 |
| 5: HöMa3 Kap. 1 bis 4 | 18 | 123 + 34 | 5 | 65e59f8 |
| 6: HöMa3 Kap. 5 bis 8, mmet, GEMB | 44 | 210 + 177 | 7 | dieser Commit |

Behandlung: reine Quellenangaben gestrichen; Skriptkorrekturen stillschweigend richtig gestellt oder, wo sie typische
Irrtümer betreffen, als neutraler Hinweis ohne Quelle formuliert; Kapitel-, Satz- und Bildnummern der Vorlage durch Namen
oder Links auf eigene Artikel ersetzt (über 100 neue Links); Praktikum, Vorlesung, Übung, Modul- und Kursnamen neutral
umformuliert; das interne Wort „Zahlenwerk“ ersetzt. Fachinhalt, Formeln, Zahlen und Kennzahlen (Abbildungen,
Beispiele, Quiz, Herleitungen) blieben gleich.

Prüfung am Ende: `quellen_check.py` ohne Fundstelle für alle Dateien; Build grün; KaTeX 131 Seiten ohne Fehler;
widefind für alle 22 Stil-3-Seiten ohne Befund; gebaute Seiten und Suchindex ohne „Skript“, „Vorlesung“, „Praktikum“.

## Offene Punkte (Bericht an den User)

- **Externe Links in GEMB:** Der Agent hat 42 von 43 externen Links entfernt (21 Vorlesungs- und Hochschulseiten anderer
  Hochschulen, 17 Nachschlagequellen wie Wikipedia und OpenStax, 4 Fachquellen); nur der Link auf die
  Software-Dokumentation QuantumATK blieb. Die Adressen stehen in `lauf6.md`; Wiederherstellung der Nachschlage- und
  Fachquellen auf Wunsch des Users.
- **Zahlen aus Beispielen der Vorlage** in alten Artikeln (ET1 Kap. 6 bis 9, HöMa3 u. a. Wahlprognose n ≈ 9600,
  zweistufiges Experiment): Wortlaut eigen, Werte übernommen; sie werden beim Neuschreiben in Stil 3 durch eigene
  Beispiele ersetzt.
- **„im vorigen Artikel“** in älteren Artikeln: Verweis innerhalb der Website, kein Quellenbezug; wird beim Neuschreiben
  durch Links ersetzt.
- **Farbtest-Seiten** `web/wissen/_farbtest/` (lokal, nicht verlinkt, nicht im Repo) enthalten noch alten Text; löschen oder
  beim Farb-Umbau neu erzeugen, nach Rückmeldung des Users.
- **Navigation:** nennt weiterhin Studiengang, Semester und Modul (Gliederung der Website); die `pfad`-Zeilen sind vom
  Prüfwerkzeug ausgenommen.
