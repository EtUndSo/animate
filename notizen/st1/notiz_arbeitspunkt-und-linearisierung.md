# Arbeitsnotiz: Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung (ST1 Netzwerkanalyse), Stil 3

Zweites ST1-Thema, 23.10.2026. Dateien: `content/st1/02-netzwerkanalyse/01-arbeitspunkt-und-linearisierung.md` (kompakt)
und `…-ausfuehrlich.md`. Frontmatter aus dem Themenplan: title „Nichtlineare Bauelemente, Arbeitspunkt und
Linearisierung“, pfad `Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse`, order 33020100, tags
nichtlineares Bauelement, Arbeitspunkt, Linearisierung, Kleinsignal, Arbeitsgerade. Zahlen:
`notizen/st1/zahlen_netzwerkanalyse.py` → `.txt` (neu, Oberthema Netzwerkanalyse).

Quelle: Skript PDF S. 15–24 (gedruckt 7–16), Abschnitte 2.1 bis 2.3 und der Schluss von 2.3 auf S. 24 (Bild 2.9).

## 1. Ein-Satz-Prinzip

**Ein nichtlineares Bauelement lässt sich nicht als Ganzes linear berechnen, aber für kleine Änderungen um einen festen
Arbeitspunkt verhält es sich wie ein lineares Bauelement, dessen Wert die Steigung seiner Kennlinie dort ist; deshalb
rechnet man jede nichtlineare Schaltung in zwei Schritten, erst den Arbeitspunkt, dann die kleinen Signale um ihn
herum, und auch der erste Schritt, das Newton-Verfahren, besteht aus nichts anderem als wiederholtem Linearisieren.**

## 2. Schwierigkeit und Längenspannen

**mittel.** Ein zentraler Mechanismus (Linearisieren im Arbeitspunkt) mit Anwendungen (Oberwellen, Arbeitspunkt
grafisch und mit Newton, Kleinsignal-Ersatzschaltbild, differentielle Kapazität und Induktivität). Spannen: kompakt
1000–3000, ausführlich 2000–5000 Wörter.

## 3. Vorwissen-Kette

- Kirchhoffsche Knotenregel, Leitwert, reale Stromquelle (Norton): ET1 verlinken; die Quelle als Gerade hier aufbauen.
- Diodenkennlinie (Shockley): [Die Diode und ihre Kennlinie] verlinken, Gleichung in Erinnerung rufen.
- Arbeitsgerade, Fixpunktiteration, differentieller Widerstand der Diode: [Arbeitspunkt und Ersatzschaltung der Diode]
  verlinken; hier allgemein und tiefer (Newton, mehrere Steuergrößen, Ladung, Fluss, Ersatzschaltbilder).
- Ableitung als Steigung, Tangente: Schulmathematik; partielle Ableitung hier aufbauen (konkret zuerst, §5.10).
- Taylor-Näherung erster Ordnung: hier aufbauen (Tangente als beste Gerade).
- sin² = (1 − cos 2x)/2: Schulmathematik (Additionstheorem), im Kasten hergeleitet.
- Kondensator Q = C U, Ladestrom: [Der Kondensator und seine Kapazität] verlinken.
- Induktionsgesetz U = dΨ/dt: kein ET1-Artikel; hier als Erfahrungsgesetz nennen, Flussverkettung erklären.
- MOS-Diode: hier als Bauelement mit quadratischer Kennlinie einführen (Aufbau des MOSFET folgt in eigenen Themen).
- Hier aufbauen: Großsignal, Kleinsignal, primäre Zustandsgrößen, differentieller Leitwert, Oberwellen, Arbeitspunkt
  als Lösung, Fehlerfunktion, Newton-Verfahren, Begleitmodell, Großsignal- und Kleinsignal-Ersatzschaltbild.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Warum gilt für eine Diode das ohmsche Gesetz nicht?“ → Text Zustandsgrößen → beide.
2. „Unter 0,7 V fließt doch kein Strom?“ (Fehlvorstellung) → Kasten, Beispieldiode 3,7 µA bei 0,5 V, 175 µA bei 0,6 V,
   60 mV je Dekade → ausführlich; kompakt ein Satz im Text.
3. „Was soll eine Ladung als Zustandsgröße, Strom ist doch Strom?“ → Text, Ladestrom I_Q = dQ/dt → beide.
4. „Wie wird aus einer krummen Kennlinie eine Gerade?“ → Kipp-Stelle 1 (Text) → beide.
5. „Woher kommt die doppelte Frequenz?“ → Schritt 3 der Kipp-Stelle, sin²-Identität → beide.
6. „Klein heißt klein gegen die Gleichspannung U_0, oder?“ (Fehlvorstellung) → Kasten: klein gegen U_0 − U_th bzw.
   gegen U_T (1 mV für 1 %) → beide.
7. „Ist der Widerstand im Arbeitspunkt nicht einfach U/I?“ (Fehlvorstellung) → Kasten: 4 kΩ gegen 1 kΩ → ausführlich;
   kompakt Frage-Kasten oder Satz.
8. „Warum hat die Diode bei gleichem Strom einen zehnmal größeren Leitwert als die MOS-Diode?“ → ausführlich Text/
   Beispiel (g = I/U_T gegen 2I/(U − U_th)); kompakt ein Satz.
9. „Warum schneiden sich Quellengerade und Kennlinie nur einmal?“ → Text Arbeitspunkt (monoton) → beide.
10. „Warum rechnet man nicht einfach die Gleichung aus?“ → Text: bei Exponentialfunktion nicht geschlossen lösbar,
    bei vielen Knoten ohnehin numerisch → beide.
11. „Wie weiß das Newton-Verfahren, in welche Richtung es gehen muss?“ → Kipp-Stelle 2 (Tangente) → beide.
12. „Findet das Newton-Verfahren immer die Lösung?“ (Fehlvorstellung) → ausführlich Frage-Kasten (Diode 174 Schritte,
    Spannungsbegrenzung 12; mehrere Lösungen bei bistabilen Schaltungen); kompakt Frage-Kasten kurz.
13. „Was wird im Kleinsignalbild aus einer Batterie?“ (Fehlvorstellung: bleibt stehen) → Kipp-Stelle 3 → beide.
14. „Warum schreibt man Kleinsignalgrößen klein, aber C groß?“ → Frage-Kasten → ausführlich.
15. „Was macht ein Simulator wie SPICE eigentlich?“ → Bedeutung und Ausblick → beide (kurz).

## 5. Kipp-Stellen

**K1 Linearisieren im Arbeitspunkt (MOS-Diode mit Sinus).** Schritte: (1) U_0 + û sin; (2) in k(U − U_th)² einsetzen;
(3) sin²-Identität: Gleichanteil (mit Verschiebung k û²/2), Grundwelle 2k(U_0 − U_th)û, 2. Harmonische k û²/2; (4) für
û ≪ U_0 − U_th bleibt nur die Grundwelle, proportional zu û: linear; (5) Faktor = Steigung g = 2k(U_0 − U_th) = dI/dU.
Zahlen: U_0 = 1 V, g = 1 mS; û = 50 mV: Grundwelle 50 µA, 2. Harmonische 1,25 µA (2,5 %), Gleichanteil +0,5 %.
Abbildung: Kennlinie mit Tangente und Signalprojektion (Abb. 1), Zeitverläufe und Spektrum (Oberwellen).
Herleitung: Kasten. Beispiel: û = 50 mV und 400 mV.

**K2 Arbeitspunkt als Nullstelle, Newton als wiederholtes Linearisieren.** Schritte: (1) Knotenregel: F(U) = I(U) +
G_q U − I_q = 0; (2) grafisch: Schnitt Quellengerade/Kennlinie bei 1,0 V, 0,25 mA; (3) Newton: F durch Tangente im
Schätzwert ersetzen, Steigung g(U_i) + G_q = Leitwert der linearisierten Schaltung; (4) Nullstelle der Tangente als
neue Schätzung; (5) Fehler 1 → 0,31 → 0,051 → 0,0019 → 3·10⁻⁶ V, quadratisch. Abbildung: F(U) mit Tangenten.
Herleitung: Kasten. Beispiel: Tabelle.

**K3 Großsignal- und Kleinsignal-Ersatzschaltbild.** Schritte: (1) Arbeitspunkt berechnen; (2) jedes nichtlineare
Element durch g (und C, L) im Arbeitspunkt ersetzen; (3) konstante Quellen auf null setzen (Spannungsquelle →
Kurzschluss, Stromquelle → Unterbrechung), weil sich ihr Wert nicht ändert; (4) lineare Schaltung für die Änderungen
lösen: î_q = 10 µA → û = 8 mV; (5) Gesamtlösung = Arbeitspunkt + Änderung; Probe exakt 8,0007 mV. Abbildung:
Ersatzschaltbilder. Herleitung: Linearisierung der Knotengleichung. Beispiel.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| drei Zustandsgrößen Strom, Ladung, Fluss mit Steuergrößen | K | Abschnitt, Tabelle/Formeln | Abschnitt, Formeln |
| Diode U ≠ R I, spannungsgesteuerte Stromquelle | K | Text | Text |
| 0,7-V-Irrtum | H | 1 Satz mit Link | Fehlvorstellung |
| Ladestrom dQ/dt, Induktionsgesetz dΨ/dt, Flussverkettung | K | knapp | Text |
| Hysterese: Ψ(I) keine Funktion | V | – | Satz |
| MOS-Diode quadratisch | K | Text | Text |
| Oberwellen-Rechnung, sin² | K | Kipp-Stelle | Kipp-Stelle |
| 3. Harmonische nur beim zeitweisen Sperren | V | – | Satz im Beispiel |
| Kleinheitsmaß û/(4(U_0 − U_th)), Diode û/(4U_T) | K/H | Fehlvorstellung | Fehlvorstellung + Beispiel |
| differentieller Leitwert = Ableitung, statisch gegen differentiell | K | Text + Frage | Text + Fehlvorstellung |
| g = I/U_T gegen 2I/(U − U_th) | H | 1 Satz | Beispiel + Kurz gesagt |
| partielle Ableitungen, Taylor erster Ordnung, g_i, C_i, L_i | K | Formel + Kasten | Formel + Kasten |
| differentielle Kapazität (Sperrschicht 24,1/15,6/8,5 pF; 1 nC bei 1 mA) | H | 1–2 Sätze | Unterabschnitt + Beispiel |
| differentielle Induktivität (Sättigung) | V | 1 Satz | Unterabschnitt |
| Arbeitspunkt grafisch, Eindeutigkeit | K | Text | Text |
| Newton-Verfahren, Iterationsvorschrift, Startwert | K | Kipp-Stelle | Kipp-Stelle |
| quadratische Konvergenz, Kurz gesagt | K | Satz | Text + Beispiel |
| Begleitmodell (g parallel Ersatzstromquelle) | H | – | Text + Formel |
| Fixpunktiteration (Faktor 0,25) zum Vergleich | V | – | Vertiefung oder Satz |
| Newton bei der Diode, Spannungsbegrenzung, mehrere Lösungen | V | kurzer Frage-Kasten | Frage-Kasten |
| mehrere Knoten: Leitwertmatrix | H | 1 Satz | 2 Sätze |
| Großsignal-/Kleinsignal-ESB, Quellen auf null, Überlagerung | K | Kipp-Stelle | Kipp-Stelle |
| Schreibweise klein/groß, C nicht klein | H | – | Frage |
| zwei Schritte, Simulator | K | Text | Text + Ausblick |
| Organisatorisches („im Rahmen dieser Veranstaltung“) | S | – | – |

## 7. Abbildungsplan (Szene-IDs st1/netzwerkanalyse/01-…)

| Nr. kompakt / ausführlich | Szene-ID | Vorlage | Inhalt und Kernaussage |
|---|---|---|---|
| 1 / 1 | 01-tangente | kennlinie-tangente | Kennlinie der MOS-Diode 0,4–1,6 V, Arbeitspunkt (1,0 V; 0,25 mA), Tangente 1 mS; Sinus ±50 mV unten, Strom ±50 µA rechts. Kleine Signale sehen nur die Tangente. |
| 2 / 2 | 01-zustandsgroessen | kennlinien-dreifach | I(U) von pn-Diode und MOS-Diode, Q_S(U) der Sperrschicht, Ψ(I) einer Spule mit Sättigung (Hysterese gestrichelt). Drei Größen beschreiben jedes Bauelement. |
| 3 / 3 | 01-oberwellen | zeitverlauf-spektrum | Strom für û = 50 und 400 mV über zwei Perioden, zerlegt in Gleichanteil, Grundwelle, 2. Harmonische; Spektren. Die Krümmung erzeugt Gleichanteilverschiebung und doppelte Frequenz, beide wachsen mit û². |
| 4 / 4 | 01-zwei-steuergroessen | kennlinienfeld-schritte | Triodenkennlinien für 250 und 256,25 V, Weg in zwei Teilschritten (+0,1 V Gitter: 0,164 mA, Tangente 0,16; +6,25 V Anode: 0,106 mA, linear 0,10); Summe 0,269 gegen 0,26 mA. Bei kleinen Änderungen addieren sich die Beiträge näherungsweise. |
| – / 5 | 01-kapazitaet-induktivitaet | kennlinie-gestapelt | Q_S(U) mit Tangenten bei 0 V und −5 V und C_S(U) darunter; Ψ(I) und L(I) darunter. Die Steigung der Ladungs- bzw. Flusskennlinie ist C bzw. L. |
| 5 / 6 | 01-arbeitspunkt-grafisch | schaltung-und-kennlinie | Schaltung (I_q 0,5 mA, R_q 4 kΩ, MOS-Diode); Quellengerade (0 V; 0,5 mA)–(2 V; 0) und Kennlinie, Schnitt (1,0 V; 0,25 mA). |
| 6 / 7 | 01-newton | funktion-tangenten | F(U) von 0 bis 2,2 V mit Tangenten in 0, 2, 1,308, 1,051 V; Nullstelle 1,0 V. Jede Tangente ist die linearisierte Schaltung. |
| 7 / 8 | 01-ersatzschaltbilder | schaltbild-vergleich | (a) Großsignal-ESB im Arbeitspunkt; (b) Kleinsignal-ESB mit î_q, G_q, g = 1 mS, C; Quellen auf null. |

Kompakt 7, ausführlich 8 (01-zwei-steuergroessen bei der Selbstprüfung ergänzt: Formel-Regel §7.2 und Richtwert Wörter je Abbildung). Die zunächst geplante Szene 01-newton-diode entfällt: Der Frage-Kasten „Findet das Newton-Verfahren immer den Arbeitspunkt?“ trägt den Inhalt mit allen Zahlen. Reihenfolge in der Tabelle wie in der ausführlichen Fassung.

## 8. Zahlenwerk

`notizen/st1/zahlen_netzwerkanalyse.py`: A Arbeitspunkt (1,000 V; 0,250 mA; g = 1 mS; U/I = 4 kΩ), B Oberwellen
(Formel und FFT), C pn-Diode (Kennlinie, g = 9,67 mS bei 0,25 mA, Kleinheit 1 mV), D Newton MOS-Diode (Tabelle,
Konvergenz 0,8 1/V, Fixpunkt 0,25), E Newton pn-Diode (174 Schritte, 24 ab 0,6 V, 12 mit Begrenzung), F Kapazität
(C_S 24,10/15,55/8,52 pF, 1 nC), G Induktivität (10/7,86/4,20/0,71 mH), H Kleinsignal (8,000 gegen 8,0007 mV;
großes Signal +143,5/−188,4 mV gegen ±160 mV; 199 MHz bei 1 pF), I Triode mit zwei Steuergrößen (Teilschritte 0,1635 und 0,1057 mA, Summe 0,2692 gegen linear 0,26 mA; Kennlinienwerte für die Abbildung).

Symbole im Artikel (keine Doppelbelegung): Sperrschichtkapazität C_S statt C_j, weil j die Steuergrößen zählt (in der ET1-Diode heißt sie C_j, im Beispiel vermerkt); Ladestrom I_C und Spulenspannung U_L statt I_Q und U_Ψ, weil I_q der Quellstrom ist; Spulenmodell Ψ = Ψ_max tanh(L_0 I/Ψ_max) mit Ψ_max = 10 mV s statt des Parameters I_s, weil I_S der Sättigungssperrstrom ist. Näherungen durchgehend mit ≈ (i ≈ g u, u ≈ i_q/(g + G_q), Taylor-Glieder im Newton-Kasten). Nach der Faktenprüfung zusätzlich: Arbeitspunkt durchgehend U_A, I_A (Q_A, Ψ_A) statt U_0/I_0; Newton-Schätzungen U^(ν) (Klammer-Hochzahl), weil U_1 … U_n die Steuerspannungen und i der Kleinsignalstrom ist; Fehler e_ν; Begleitmodell I_eq,ν; Kennlinienfunktion in der Herleitung f_I statt f (f ist die Frequenz); Amplituden î_q, û ausdrücklich.

## 9. Profi-Abgleich

- Newton-Raphson in Schaltungssimulatoren, Begleitmodell, Spannungsbegrenzung (SPICE2, Nagel 1975):
  https://en.wikipedia.org/wiki/SPICE (Abschnitt DC analysis) und Lehrbuchwissen (Vlach/Singhal, Computer Methods for
  Circuit Analysis and Design).
- Kleinsignalmodell, differentielle Größen, Oberwellen quadratischer Kennlinien: Razavi, Design of Analog CMOS
  Integrated Circuits, Kap. 2; Tietze/Schenk, Halbleiter-Schaltungstechnik (Kleinsignalbetrieb).

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte (Vollständigkeit):**
- S. 15: Diode als nichtlineares Element (Bild 2.1); Kenngrößen: Strom als Antwort auf Spannungen, gespeicherte Ladung,
  magnetischer Fluss.
- S. 16: Strom fließt ab „circa 0,7 V“, exponentiell; Diodengleichung (2.1) mit I_S „≈ 10 pA … 10 µA“, U_T ≈ 25 mV;
  rückwärts „kein Strom“; U ≠ R I (2.2); spannungsgesteuerte Stromquelle; ideale Diode ohne Durchbruch, „I = I_S e^{U/U_T}
  für alle U“; Großsignalbetrieb; resistives Element I(U_1…U_n) = f_I (2.3), Strom als primäre Zustandsgröße; Ladung
  Q(U) (Bild 2.3), Q = f_Q (2.4), I_Q = dQ/dt (2.5); resistive und kapazitive Typen fast ausreichend.
- S. 17: Fluss für Maschinen, Transformatoren, Spulen „aufgrund der Hysterese“, Φ(I_1…I_n) (2.6), U_Φ = dΦ/dt (2.7);
  Übersicht (2.8); Großsignaleigenschaften aus Strom, Ladung, Fluss, daraus Arbeitspunkt. 2.2: Kleinsignalberechnung;
  Bild 2.5: U_0 + û sin an Diode, Punkte 1 bis 3.
- S. 18–19: MOS-Diode (Fußnote: Gate und Drain verbunden, MOS-Gleichung); (2.9) quadratische Kennlinie; (2.10),
  (2.11) Zerlegung mit sin², 1. Oberwelle k û²/2 cos 2ωt, Gleichanteilverschiebung; (2.12) Kleinsignalbetrieb
  „û ≪ U_0 − U_th und û² ≪ û“; Arbeitspunkt (U_0, I_0); (2.13) î = 2k(U_0 − U_th)û; (2.14) g(U_0); (2.15)–(2.17).
- S. 20: (2.18) g = dI/dU; Linearisierung im Arbeitspunkt als grundlegendes Verfahren; (2.19) Linearisierung von Strom,
  Ladung, Fluss mit partiellen Ableitungen; (2.20) g_i, C_i, L_i; zwei Schritte (Arbeitspunkt, Wechselspannungsanalyse).
- S. 21: Kasten Kleinsignalberechnung; 2.3 Schaltung Bild 2.7 (I_q = 1 A, G_q = 1 S, „k = 2 S“, U_th = 0,5 V);
  grafische Lösung Bild 2.8, Gerade durch (0; I_q) und (R_q I_q; 0).
- S. 22: Arbeitspunkt ≈ 0,81 V, 0,2 A; grafisch nur eine Unbekannte, ungenau; Simulation: Newton + linearisiertes
  Ersatznetzwerk; (2.21)–(2.27) Knotenregel, F(U), Newton-Linearisierung, Fehlerstrom, n-dimensionales System, Update;
  (2.28) G = ∂F/∂U.
- S. 23: (2.29) G = g + G_q; (2.30), (2.31) Iterationsvorschrift; Tabellen 2.1 (Start 0) und 2.2 (Start 1 V aus der bei
  0 linearisierten Gleichung, (2.32)–(2.34)); Linearisierung im Arbeitspunkt für Kleinsignalanalyse, g reicht statisch.
- S. 24: Bild 2.9 statisches Großsignal-ESB und dynamisches Kleinsignal-ESB mit C(U) = ∂Q/∂U; Kleinbuchstaben für
  Kleinsignalgrößen, nicht für C, L; Überlagerung beider ESB beschreibt die linearisierten Eigenschaften vollständig.
- Das Zahlenbeispiel der Vorlage (1 A, 1 S, 2 A/V², 0,5 V) wird nicht übernommen; eigenes Beispiel (0,5 mA, 4 kΩ,
  1 mA/V², 0,5 V).

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 16: Strom fließt „wenn eine Spannung von circa 0,7 V überschritten wird“ – Schwellenvorstellung; der Strom wächst
   exponentiell, je 59,5 mV um den Faktor 10.
2. S. 16: „In der Rückwärtsrichtung … fließt kein Strom“ – es fließt der kleine Sperrstrom (−I_S plus Generation).
3. S. 16: „I_S ≈ 10 pA … 10 µA“ – für Siliziumdioden mit idealer Kennlinie viel kleiner (fA bis pA; Beispieldiode
   1,46·10⁻¹⁴ A); nA-Werte nur in Modellen mit Emissionskoeffizient über 1.
4. S. 16: „U_T ≈ 25 mV“ – 25,85 mV bei 300 K.
5. S. 16: „Somit gilt I = I_S e^{U/U_T} für alle anliegenden Spannungen“ – ohne „−1“ falsch für U ≤ 0; gilt nur für U
   von einigen U_T an.
6. S. 17: Fluss „aufgrund der Hysterese“ nötig – nötig ist er für jede Spule (Energie im Magnetfeld); Eisen macht Ψ(I)
   nichtlinear, Hysterese macht es sogar von der Vorgeschichte abhängig.
7. S. 19: Bedingung „û² ≪ û“ – Größen verschiedener Einheit; richtig: û ≪ U_0 − U_th (2. Harmonische/Grundwelle =
   û/(4(U_0 − U_th))).
8. S. 21: „k = 2 S“ – Einheit von k ist A/V².
9. S. 20: (2.19) mit Amplituden û_i statt Momentan-Änderungen u_i.
10. S. 21: „infinitesimal kleine Auslenkungen“ – klein genug, nicht infinitesimal; Maß wie in 7.
11. S. 22: „Kirchoff’sche“ – Schreibweise Kirchhoff.
12. S. 16, Bild 2.3: Die Ladungskennlinie zeigt nur die Sperrschichtladung; im Durchlass überwiegt die gespeicherte Ladung der eingespeisten Ladungsträger (Beispieldiode bei 1 mA rund 1 nC gegen einige 10 pC in der Sperrschicht).
13. S. 17, (2.6)/(2.7): Fluss Φ statt Flussverkettung Ψ; die Spannung einer Spule mit N Windungen ist dΨ/dt, bei gleichem Fluss je Windung N dΦ/dt.

## 11. Faktenprüfung (23.10.2026, unabhängiger Agent, Bericht im Sitzungs-Scratchpad)

Über 150 Zahlen unabhängig nachgerechnet (exakte Brüche, FFT, Besselfunktionen, Lambert W): keine falsch. Befunde, alle
selbst nachgerechnet (Zahlenwerk J) und eingearbeitet:

- **F1 falsch:** „Knick an der Schwelle“: Die Parabel ist dort stetig differenzierbar mit Steigung 0; Tangente existiert
  (waagerecht), nur die Krümmung springt. Jetzt: Knick-Beispiel = aus Geradenstücken zusammengesetzte Ersatzkennlinie;
  an der Schwelle sagt die Linearisierung mit g = 0 nichts voraus, obwohl k u² fließt (Herleitungen, Ausblick).
- **F2 falsch:** statischer Widerstand als „Steigung der Ursprungsgeraden“: im I-U-Diagramm ist das der statische
  Leitwert (0,25 mS); Widerstand ist der Kehrwert. Fehlvorstellung (A) und Frage-Kasten (K) korrigiert.
- **U1:** Faktor 48 von 0,6 auf 0,7 V nur bei idealer Kennlinie; reale Kleinsignaldioden (1N4148, N = 1,75 … 1,9)
  etwa 8- bis 9-fach (9,10 bzw. 7,61, Zahlenwerk J).
- **U2:** Prinzipsatz „jede nichtlineare Schaltung“ → „eine nichtlineare Schaltung, die kleine Signale verarbeitet“;
  „Jeder Verstärker“ → „Jeder Kleinsignalverstärker“.
- **U3:** Konvergenzquotienten in der Probe 0,54/0,74/0,80 (passend zu beiden Tabellen).
- **U4:** Beispiel (c): bei 199 MHz 5,66 mV und je 7,07 µA durch Leitwerte und Kapazität, 90° verschoben.
- **U5:** Newton-Schritt 3 (K): Nullstelle ist die neue Schätzung, nicht die Spannungsänderung.
- **U6:** „≈“ statt „=“ im Konvergenzschritt (jetzt mit exaktem Zwischenschritt ½F''e²/(F' + F''e)) und bei g ≈ I/U_T.
- **U7:** Symbole (siehe Abschnitt 8).
- **U8:** Schrittzahlen hängen vom Abbruchkriterium ab (174/171 ohne, 12/9 mit Begrenzung) → „gut 170“, „rund zehn“.
- **U9:** Bedingungen: „oberhalb der Schwelle“, „mindestens mit dem Quadrat“, stetige zweite Ableitungen,
  Ladestrom nur bei einer Steuerspannung.
- **U10:** Shockley: ×10 je 59,5 mV erst ab etwa 0,1 V; Sperrstrom nähert sich −I_S; g hängt bis auf I_S nur von
  Strom und Temperatur ab.
- **U11:** 1 mV sind knapp anderthalb Promille von 0,7 V (exakt 1 % bei 1,034 mV).
- **U12:** Bipolartransistor steiler als MOSFET „im quadratischen Bereich“.
- **U13:** 1 nC = Lebensdauer 1 µs mal 1 mA, Lebensdauer jetzt genannt.
- **U14:** Vorzeichen und Nullpunkt der Sperrschichtladung in Abbildung 2b und in der Liste erklärt.
- **U15:** genau ein Schnittpunkt: höchstens einer (Gerade fällt, Kennlinie fällt nirgends), mindestens einer
  (Vorzeichenwechsel zwischen 0 V und 2 V).
- **U16:** Absatz „In der ausführlichen Fassung“ und Summary der kompakten Fassung bereinigt.
- **U17:** 32 % statt „ein Drittel“, „knapp ein Drittel“, Fixpunktfaktor −0,25 erst nahe der Lösung, sechs
  Fehlerwerte, Spitzen +52,5/−47,5 µA in Abbildung 1, „fast genau“ U_T je Schritt.
- Zusätzlich (Hinweis des Agenten): Lambertsche W-Funktion als geschlossene Lösung für eine einzelne Masche erwähnt;
  Ψ im Rechtsschraubensinn zum Strompfeil gezählt.

## 12. Kennzahlen (Stand Commit)

Kompakt 2538 Wörter (15 min), 7 Abbildungen, 3 Beispiele, 6 Quizfragen, 4 Herleitungskästen (identisch mit der
ausführlichen Fassung). Ausführlich 3913 Wörter (23 min), 8 Abbildungen, 5 Beispiele, 10 Quizfragen, 5 Herleitungen,
1 Vertiefung. Checks: Build, KaTeX 0, widefind ×3 leer, splitalign ohne Fehler, Tabellen ≤ 330 px, Quellen-Check leer,
Inline-Formeln 0, Verbotsliste 0, Abbildungsliste vollständig.
