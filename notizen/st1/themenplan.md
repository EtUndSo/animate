# Themenplan Schaltungstechnik 1 (ST1), Stil 3

Eingerichtet am 22.10.2026 nach LOOP_STIL3 (B1d), auf Wunsch des Users vor dem Rest von ET1 vorgezogen.

**Quelle:** Skript `C:\Bücher\EtUndSo\3.Semester\ST1\Vorlesung\Skript.pdf` (279 Seiten, aus dem Vorlesungsarchiv entpackt;
dieselbe Fassung wie `C:\Bücher\Schalte1_Skript_Vorgabe\Script-ST-1-WS2025 (1).pdf`). Volltext:
`C:\Bücher\EtUndSo\_volltext\st1_clean.txt` (`tools/dump_st1.py`). Seitenangaben unten sind PDF-Seiten; gedruckte
Seitenzahl = PDF-Seite − 8.

**Als Hilfe:** eigene Zusammenfassungen des Users in `C:\Bücher\Schalte1_Skript_Erklaerung\` (Kap. 2 Netzwerkanalyse,
Kap. 3 MOSFET, Kap. 4 Bipolartransistor, Kap. 5 Grundschaltungen, Kap. 6 Stromspiegel, Kap. 7 Differenzverstärker,
Formelliste). **Nur als Ideengeber:** Übungs-, Rechenübungs-, Kleingruppen- und Klausuraufgaben (Archiv, Ordner
`Schalte1_Skript_Vorgabe`); keine Aufgaben kopieren.

**Zuschnitt:** Ein Thema hat etwa den Umfang eines ET1-Themas. Überschneidungen mit ET1 (Netzwerkanalyse Kap. 7 bis 9,
Bipolartransistor Kap. 11, Operationsverstärker Kap. 12) werden verlinkt; jeder ST1-Artikel bleibt in sich vollständig
(ERKLAER_PROMPT §3.4). Auf der Website steht kein Bezug auf Skript oder Lehrveranstaltung (§5.7).

**Entfällt:** 1.2 „Inhalt und Ziel der Vorlesung“ (Organisatorisches), Kap. 10 „Ausblick“ (beschreibt eine andere
Lehrveranstaltung; §5.7), Anhang D „LT-Spice Simulationen“ (Softwarebedienung). Die Anhänge A (Cramersche Regel), B
(SPICE-MOS-Modelle) und C (Quellensymbole) gehen in die Themen ein, die sie brauchen.

`pfad` aller Themen: `Elektrotechnik / 3. Semester / Schaltungstechnik 1 / <Kapitel>`; `order` nach dem Muster 33KKTT00.

| Dateipfad | title | Kapitel (pfad) | order | tags | Skriptseiten (PDF) |
|---|---|---|---|---|---|
| content/st1/01-einfuehrung/01-geschichte-der-schaltungstechnik.md | Von der Röhre zum integrierten Schaltkreis | Einführung | 33010100 | Elektronenröhre, Transistor, integrierte Schaltung, Mooresches Gesetz, CMOS | 9–13 (1.1) |
| content/st1/02-netzwerkanalyse/01-arbeitspunkt-und-linearisierung.md | Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung | Netzwerkanalyse | 33020100 | nichtlineares Bauelement, Arbeitspunkt, Linearisierung, Kleinsignal, Arbeitsgerade | 15–23 (2.1–2.3) |
| content/st1/02-netzwerkanalyse/02-ersatzquellen-maschen-und-knotenanalyse.md | Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse | Netzwerkanalyse | 33020200 | Thévenin, Norton, Maschenstromanalyse, Knotenpotentialanalyse, gesteuerte Quelle | 24–31 (2.4.1–2.4.3), 273–274 (Anhang C) |
| content/st1/02-netzwerkanalyse/03-modifizierte-knotenanalyse.md | Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse | Netzwerkanalyse | 33020300 | Leitwertmatrix, modifizierte Knotenpotentialanalyse, Cramersche Regel, Determinante | 32–44 (2.4.4–2.4.5), 265–270 (Anhang A) |
| content/st1/02-netzwerkanalyse/04-testquellen-und-transientenanalyse.md | Testquellen und Transientenanalyse linearer Schaltungen | Netzwerkanalyse | 33020400 | Testquelle, Eingangswiderstand, Ausgangswiderstand, Transientenanalyse, Zeitkonstante | 45–52 (2.4.6, 2.5) |
| content/st1/02-netzwerkanalyse/05-vierpole.md | Vierpole: Parameterformen und Zusammenschaltung | Netzwerkanalyse | 33020500 | Vierpol, Admittanzform, Impedanzform, Kettenform, Zusammenschaltung | 53–66 (2.6) |
| content/st1/03-mos-feldeffekttransistoren/01-aufbau-und-funktionsweise.md | Aufbau und Funktionsweise des MOSFET | MOS-Feldeffekttransistoren | 33030100 | MOSFET, Inversion, Kanal, Schwellenspannung, Schaltsymbol | 67–72 (3.1–3.4) |
| content/st1/03-mos-feldeffekttransistoren/02-kennlinien.md | Kennlinien des NMOS-Transistors | MOS-Feldeffekttransistoren | 33030200 | ohmscher Bereich, Abschnürbereich, Quadratgesetz, Kanallängenmodulation, Ausgangskennlinie | 73–78 (3.5–3.6) |
| content/st1/03-mos-feldeffekttransistoren/03-pmos-substrateffekt-latch-up.md | PMOS-Transistor, Substrateffekt und Latch-Up | MOS-Feldeffekttransistoren | 33030300 | PMOS, Substrateffekt, Body-Effekt, Latch-Up, CMOS | 79–80 (3.7–3.8), 87 (3.10) |
| content/st1/03-mos-feldeffekttransistoren/04-parasitaere-kapazitaeten.md | Parasitäre Kapazitäten des MOSFET | MOS-Feldeffekttransistoren | 33030400 | MOS-Kapazität, Gate-Kapazität, Überlappkapazität, Sperrschichtkapazität | 81–86 (3.9) |
| content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell.md | Kleinsignalmodell des MOSFET | MOS-Feldeffekttransistoren | 33030500 | Steilheit, Ausgangsleitwert, Substratsteilheit, Kleinsignalersatzschaltbild, SPICE-Modell | 88–92 (3.11–3.13), 271–272 (Anhang B) |
| content/st1/04-bipolartransistor/01-aufbau-und-transportmodell.md | Bipolartransistor: Arbeitsbereiche und Transportmodell | Bipolartransistor | 33040100 | Bipolartransistor, Arbeitsbereich, Transportmodell, Ebers-Moll, Early-Effekt | 93–100 (4.1–4.4) |
| content/st1/04-bipolartransistor/02-kleinsignalmodell.md | Kleinsignalmodell des Bipolartransistors | Bipolartransistor | 33040200 | Steilheit, Eingangswiderstand, Ausgangswiderstand, Hybrid-π, Kleinsignal | 101–104 (4.5) |
| content/st1/05-transistorgrundschaltungen/01-source-schaltung.md | Die Source-Schaltung | Transistorgrundschaltungen | 33050100 | Source-Schaltung, Spannungsverstärkung, Arbeitspunkt, Übertragungskennlinie, Kleinsignal | 105–112 (Einleitung, 5.1) |
| content/st1/05-transistorgrundschaltungen/02-gegenkopplung-und-aktive-last.md | Source-Schaltung mit Gegenkopplung und aktiver Last | Transistorgrundschaltungen | 33050200 | Stromgegenkopplung, Source-Widerstand, aktive Last, Eigenverstärkung | 113–120 (5.2–5.3) |
| content/st1/05-transistorgrundschaltungen/03-drain-schaltung.md | Die Drain-Schaltung (Source-Folger) | Transistorgrundschaltungen | 33050300 | Drain-Schaltung, Source-Folger, Ausgangswiderstand, Pegelverschiebung | 121–125 (5.4) |
| content/st1/05-transistorgrundschaltungen/04-gate-schaltung.md | Die Gate-Schaltung | Transistorgrundschaltungen | 33050400 | Gate-Schaltung, Eingangswiderstand, Stromverstärkung, Ausgangswiderstand | 126–131 (5.5) |
| content/st1/05-transistorgrundschaltungen/05-kaskode.md | Die Kaskode | Transistorgrundschaltungen | 33050500 | Kaskode, Ausgangswiderstand, Verstärkung, Aussteuerbereich | 132–139 (5.6) |
| content/st1/05-transistorgrundschaltungen/06-frequenzgang-und-miller-effekt.md | Frequenzgang der Source-Schaltung und Miller-Effekt | Transistorgrundschaltungen | 33050600 | Frequenzgang, Polstelle, Miller-Effekt, Grenzfrequenz, Bode-Diagramm | 140–145 (5.7.1–5.7.2) |
| content/st1/05-transistorgrundschaltungen/07-frequenzgang-weiterer-grundschaltungen.md | Frequenzgang von Source-Folger, Gate-Schaltung und Kaskode | Transistorgrundschaltungen | 33050700 | Frequenzgang, Source-Folger, Gate-Schaltung, Kaskode, Nullstelle | 146–155 (5.7.3–5.7.5) |
| content/st1/05-transistorgrundschaltungen/08-bipolare-grundschaltungen.md | Grundschaltungen des Bipolartransistors | Transistorgrundschaltungen | 33050800 | Emitterschaltung, Kollektorschaltung, Basisschaltung, Vergleich MOSFET | 156–162 (5.8) |
| content/st1/06-stromspiegel/01-konzept-und-basisformen.md | Stromspiegel: Konzept und Basisformen | Stromspiegel | 33060100 | Stromspiegel, Referenzstrom, Spiegelverhältnis, Ausgangswiderstand | 163–169 (6.1–6.2) |
| content/st1/06-stromspiegel/02-verbesserte-stromspiegel.md | Verbesserte MOS-Stromspiegel | Stromspiegel | 33060200 | Kaskode-Stromspiegel, Level-Shift, Wide-Swing, Strombank | 170–174 (6.3–6.4) |
| content/st1/06-stromspiegel/03-bipolar-stromspiegel.md | Bipolar-Stromspiegel | Stromspiegel | 33060300 | Bipolar-Stromspiegel, Basisstromfehler, Emitterdegeneration, Wilson | 175–182 (6.5) |
| content/st1/07-differenzverstaerker/01-differentieller-betrieb.md | Differentieller Betrieb: Differenz- und Gleichtaktspannung | Differenzverstärker | 33070100 | differentiell, Differenzspannung, Gleichtaktspannung, Störfestigkeit | 183–186 (7.1–7.2) |
| content/st1/07-differenzverstaerker/02-differenzstufe.md | Die Differenzstufe und ihre Übertragungskennlinie | Differenzverstärker | 33070200 | Differenzstufe, Übertragungskennlinie, Stromaufteilung, Aussteuerbereich | 187–194 (7.3) |
| content/st1/07-differenzverstaerker/03-kleinsignalverhalten.md | Kleinsignalverhalten des Differenzverstärkers | Differenzverstärker | 33070300 | Half-Circuit-Konzept, Differenzverstärkung, Gleichtaktverstärkung, Gleichtaktunterdrückung | 195–199 (7.4) |
| content/st1/07-differenzverstaerker/04-bipolar-und-offset.md | Bipolar-Differenzverstärker und Eingangsoffset | Differenzverstärker | 33070400 | Bipolar-Differenzstufe, Offsetspannung, Fehlanpassung, Mismatch | 200–205 (7.5–7.6) |
| content/st1/07-differenzverstaerker/05-gegenkopplung-und-aktive-lasten.md | Stromgegenkopplung und aktive symmetrische Lasten | Differenzverstärker | 33070500 | Stromgegenkopplung, aktive Last, Kaskode-Differenzstufe, Stromspiegellast | 206–216 (7.7–7.8) |
| content/st1/07-differenzverstaerker/06-gefaltete-kaskode-und-gilbert-zelle.md | Gefaltete Kaskode und Gilbert-Zelle | Differenzverstärker | 33070600 | gefaltete Kaskode, Gilbert-Zelle, Mischer, Multiplizierer | 217–226 (7.9–7.10) |
| content/st1/08-operationsverstaerker/01-zweistufiger-opv.md | Der zweistufige Operationsverstärker | Operationsverstärker | 33080100 | zweistufiger Operationsverstärker, Differenzverstärkung, Gleichtaktverstärkung, Versorgungsspannungsunterdrückung, Arbeitsbereich | 227–234 (8.1–8.3) |
| content/st1/08-operationsverstaerker/02-offset.md | Offset des Operationsverstärkers | Operationsverstärker | 33080200 | systematischer Offset, zufälliger Offset, Dimensionierung | 235–238 (8.4) |
| content/st1/09-digitale-cmos-grundschaltungen/01-cmos-inverter.md | Der CMOS-Inverter | Digitale CMOS-Grundschaltungen | 33090100 | CMOS-Inverter, Übertragungskennlinie, Stromaufnahme, Dimensionierung, Schaltschwelle | 239–248 (Einleitung, 9.1) |
| content/st1/09-digitale-cmos-grundschaltungen/02-gatter-und-transmission-gate.md | Statische CMOS-Gatter und Transmission-Gate | Digitale CMOS-Grundschaltungen | 33090200 | NAND, NOR, statisches Gatter, Transmission-Gate | 249–251 (9.2–9.3) |
| content/st1/09-digitale-cmos-grundschaltungen/03-getaktete-und-dynamische-logik.md | Getaktete und dynamische Logik | Digitale CMOS-Grundschaltungen | 33090300 | Latch, Register, Setup-Zeit, dynamisches Gatter, Precharge | 252–258 (9.4–9.5) |

35 Themen. Zahlenwerk je Kapitel: `notizen/st1/zahlen_<kapitel>.py` (B3); ein durchgehendes Beispiel-Transistorpaar
(NMOS/PMOS mit festen Modellparametern, dazu der Beispiel-Bipolartransistor aus ET1) wird beim ersten Transistorthema
festgelegt und in allen folgenden Kapiteln weiterbenutzt.
