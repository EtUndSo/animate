# Arbeitsnotiz: Bipolartransistor: Arbeitsbereiche und Transportmodell (ST1, Bipolartransistor, Thema 1)

Dateien: `content/st1/04-bipolartransistor/01-aufbau-und-transportmodell.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Bipolartransistor: Arbeitsbereiche und Transportmodell“, pfad „Elektrotechnik /
3. Semester / Schaltungstechnik 1 / Bipolartransistor“, order 33040100, tags „Bipolartransistor, Arbeitsbereich,
Transportmodell, Ebers-Moll, Early-Effekt“. Quelle: PDF S. 93–100 (4.1–4.4), Volltext `st1_clean.txt` Zeilen 7479–7976.
Zahlen: `zahlen_bipolar.py` Abschnitte A bis K (neues Oberthema, eigener integrierter Beispiel-npn).

## 1. Ein-Satz-Prinzip

Der Bipolartransistor ist eine spannungsgesteuerte Stromquelle mit einem Nebenstrom: Die Basis-Emitter-Spannung legt
über eine Diodengleichung den Transportstrom vom Kollektor zum Emitter fest, die Basis liefert davon nur den festen
Bruchteil 1/B_N als Basisstrom, und das Transportmodell fasst beide pn-Übergänge und beide Stromrichtungen in zwei
Dioden und einer gesteuerten Quelle zusammen, sodass alle fünf Betriebszustände aus demselben Modell folgen.

## 2. Schwierigkeit und Längenspannen

**schwer**: mehrere zusammenwirkende Mechanismen (Transistoreffekt in Kurzform, Stromaufteilung, Sättigung als
Zusammenspiel zweier leitender Dioden, Early-Effekt, Gummel-Plot) und zwei Kipp-Stellen (Spannungs- gegen
Stromsteuerung, Sättigung im Transportmodell). Spannen: kompakt 1800–4000, ausführlich 3500–7000 Wörter; erwartet
kompakt um 2600, ausführlich um 4300.

## 3. Vorwissen-Kette

- pn-Übergang, Diodengleichung mit I_S und U_T, Sperr- und Durchlassbetrieb, Minoritätsträger: ET1 „Halbleiter und das
  Bändermodell“ und „Die Diode und ihre Kennlinie“, erinnern und verlinken.
- Transistoreffekt physikalisch (dünne Basis, Diffusion der Minoritäten, Rückinjektion und Rekombination als Quelle
  des Basisstroms, Herleitung von I_S und B aus Dotierung und Basisweite): ET1 „Der Bipolartransistor – Aufbau und
  Wirkungsweise“; hier in Kurzform als Mechanismus-Kette (K), die vollständige Herleitung dort verlinkt.
- Arbeitspunkt, Linearisierung, gesteuerte Quellen als Netzwerkelemente: ST1 Netzwerkanalyse Thema 1 und 2, verlinken.
- MOSFET-Kennlinien, Kanallängenmodulation λ = 0,1 1/V, Sättigungsbereich des MOSFET: ST1 MOSFET Themen 2 und 5,
  verlinken (Wortgebrauch „Sättigung“, Early gegen λ, g_m/I).
- Modul-Test: ET1 Kap. 11 behandelt Aufbau, Effekt, Kennlinien, Arbeitsbereiche mit einfachem Modell (U_BE 0,6 V,
  U_CE,sat 0,2 V). Dieser Artikel ist beim Transportmodell, bei der Sättigung (quantitativ aus zwei Dioden), beim
  Early-Effekt und beim Gummel-Plot tiefer; beim physikalischen Transistoreffekt verweist er auf ET1.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Warum heißt er Bipolar-Transistor?“ → Aufbau, Text, beide.
2. „Warum kann man den diskreten Aufbau nicht integrieren, und wozu der buried layer?“ → Aufbau, Text (ausführlich),
   Frage-Kasten (kompakt).
3. „Warum liegt das Substrat an der negativsten Versorgung?“ → Frage-Kasten, beide.
4. Fehlvorstellung: „Der Basisstrom fließt durch den Transistor und wird B-fach verstärkt; der Kollektorstrom ist
   der verstärkte Basisstrom.“ → Kipp-Stelle K1, Fehlvorstellungs-Kasten, beide.
5. „Wenn U_BE den Strom festlegt, wozu dann überhaupt B?“ → K1, Text, beide.
6. „Warum fließt der Kollektorstrom durch einen gesperrten Übergang?“ → Funktionsweise, Text, beide (Kurzform;
   ausführlich mit Link ET1).
7. „Was unterscheidet I_C = I_S(e − 1) von einer gewöhnlichen Diode?“ → Text, beide.
8. „Warum ist die Verstärkung im Inversbetrieb so klein?“ → Text, beide; Zahl B_I = 2.
9. Fehlvorstellung: „Sättigung heißt beim Bipolartransistor dasselbe wie beim MOSFET.“ → Fehlvorstellungs-Kasten,
   beide (beim MOSFET der Verstärkerbereich, beim BJT der Schalterbereich).
10. „Warum hängt der Kollektorstrom in der Sättigung nicht mehr vom Basisstrom ab?“ → Kipp-Stelle K2, Schritte,
    Beispiel mit Transportmodell, beide.
11. „Wie kommt die Sättigungsspannung von 0,1 V zustande, wenn beide Dioden 0,7 V haben?“ → K2, Text, beide.
12. „Wozu zwei Dioden plus Quelle, wenn im Normalbetrieb eine Diode und eine Quelle reichen?“ → Transportmodell,
    Text, beide.
13. „Ist die Quelle im Transportmodell strom- oder spannungsgesteuert?“ → K1, Text, beide.
14. Fehlvorstellung: „Weil I_E ≈ I_C, kann man den Basisstrom immer vernachlässigen.“ → Fehlvorstellungs-Kasten,
    beide (10 µA bei 1 mA: egal für den Emitterstrom, nicht für den Eingangswiderstand und für Stromspiegel).
15. „Warum steigt der Kollektorstrom mit U_CE, obwohl der Kollektorübergang sperrt?“ → Early-Effekt, Text mit
    Basisweitenmodulation, beide; Herleitung ausführlich, kompakt übernommen.
16. „Warum ist B im Datenblatt eine Kurve und keine Zahl?“ → Gummel-Plot, ausführlich Abschnitt; kompakt ein Satz.
17. „Warum stört ein Emitterwiderstand von 5 Ω, ein Basiswiderstand von 100 Ω aber kaum?“ → Großsignalmodell,
    ausführlich; Beispiel.

## 5. Kipp-Stellen

**K1: Spannungs- oder Stromsteuerung.** Schritte: (1) Beide Übergänge liegen entgegengesetzt in Reihe; mit U_CE > 0
und offener Basis sperrt der Kollektorübergang, nur Sperrstrom. (2) U_BE > 0 senkt die Barriere des Emitterübergangs;
Elektronen diffundieren in die dünne Basis (0,1 µm beim Beispiel, kürzer als die Diffusionslänge). (3) Sie erreichen
den gesperrten Kollektorübergang, dessen Feld sie einsammelt; der Kollektorstrom folgt der Diodengleichung mit U_BE,
nicht mit U_CE. (4) Die Basis ersetzt nur die Verluste (Rückinjektion, Rekombination): ein fester Bruchteil 1/B_N,
beim Beispiel 10 µA zu 1 mA. (5) Folge: Die gesteuerte Quelle des Transportmodells ist spannungsgesteuert
(I_T = I_S(e^{U_BE/U_T} − e^{U_BC/U_T})); die Schreibweise B_N I_B,N ist dieselbe Größe, nur über den Basisstrom
ausgedrückt. In Schaltungen sieht man beides: „stromgesteuert“ ist eine Rechenabkürzung, die stimmt, solange B_N fest
ist. Abbildungen 01-einstieg, 01-transportmodell. Herleitung H1 (Kollektorstrom aus dem Diffusionsstrom durch die
Basis, Kurzform mit Link ET1) und H2 (Transportmodell). Beispiel: Ströme bei 773,8 mV (1 mA, 10 µA, −1,01 mA) und
+18 mV → Verdopplung, +60 mV → Faktor 10.

**K2: Sättigung im Transportmodell.** Schritte: (1) Der Kollektorkreis lässt höchstens (U_CC − U_CE)/R_C zu, bei
2,5 V und 1 kΩ rund 2,4 mA. (2) Mehr Basisstrom hebt U_BE, der Transportstrom wächst, U_CE sinkt; bei U_CE unter etwa
0,3 V leitet auch die Kollektordiode. (3) Jetzt teilt sich der Basisstrom: I_B,N treibt die Quelle, I_B,I fließt
über die Kollektordiode ab; der Transportstrom ist B_N I_B,N − B_I I_B,I. (4) Bei I_B = 50 µA: I_B,N = 24,7 µA,
I_B,I = 25,3 µA, I_C = 2,40 mA statt 5 mA; U_CE = 797 − 697 = 100 mV. (5) U_CE,sat ist die Differenz zweier
Durchlassspannungen; mehr Basisstrom drückt sie nur noch logarithmisch (75 mV bei 100 µA). Abbildungen
01-arbeitsbereiche, 01-saettigung-stroeme (ausführlich). Herleitung H2 (Transportmodell) und H4 (U_CE,sat aus dem
Transportmodell, ausführlich). Beispiel: Sättigung bei 50 µA.

**K3 (kleiner): Early-Effekt als Basisweitenmodulation.** Schritte: Sperrschicht des Kollektorübergangs wächst mit
U_CB und frisst Basisweite; I_S ∝ 1/W_B; linearisiert Faktor (1 + U_CE/U_A); Tangenten schneiden bei −U_A = −50 V.
Abbildung 01-early-effekt. Herleitung H3. Beispiel: 1,00 → 1,10 mA zwischen U_CE = 0 und 5 V.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Aufbau npn: drei Gebiete, zwei Übergänge, Dotierungsfolge n⁺/p/n, Name „bipolar“ | K | Text, Abbildung | Text, Abbildung |
| diskreter Aufbau mit Rückseitenkollektor; warum nicht integrierbar | H | Satz | Text |
| integrierter Aufbau: buried layer, p⁺-Substratanschluss, Substratdiode gesperrt, Isolation | H | Frage-Kasten | Text, Abbildung, Frage |
| Emitterfläche als Skalierungsparameter, I_S ∝ A_E | K | Satz mit Zahl | Text, Zahl (ET1-Vergleich) |
| Schaltsymbole npn/pnp, Diodenersatz, Zählpfeile und Vorzeichen (alle Ströme hinein, I_E < 0) | K | Abbildung, Text | Abbildung, Text |
| Funktionsweise: Übergänge entgegengesetzt in Reihe, Sperren bei offener Basis, Diffusion durch die dünne Basis, Einsammeln am Kollektor, Basisstrom aus Rekombination | K | Kipp-Stelle K1 | K1, ausführlicher, Link ET1 |
| Knotengleichung I_E = −(I_B + I_C) | K | Formel | Formel |
| I_C = I_S(exp − 1), B = I_C/I_B, A = −I_C/I_E, A = B/(1+B) | K | Formel, Herleitung, Beispiel | dito |
| Inversbetrieb, B_I klein (Dotierung) | K | Satz, Zahl | Text, Zahl, Beispiel F |
| fünf Betriebszustände (stromlos, gesperrt, aktiv, Sättigung, invers), U_BE/U_BC-Ebene | K | Tabelle, Abbildung | Tabelle, Abbildung |
| Wortgebrauch „Sättigung“ MOS gegen BJT | K | Fehlvorstellung | Fehlvorstellung |
| Transportmodell: zwei Dioden I_B,N, I_B,I, Quelle I_T = B_N I_B,N − B_I I_B,I, I_B = Summe | K | Formel, Herleitung, Abbildung | dito |
| Quelle spannungsgesteuert, Schreibweise über Basisstrom | K | K1 | K1 |
| vereinfachtes Transportmodell für den Normalbetrieb | K | Abbildung, Text | dito |
| Übertragungs- und Eingangskennlinie, I_B = I_C/B_N, 60 mV je Dekade | K | Formel, Abbildung, Beispiel | dito |
| Emitterstrom −(1 + 1/B_N) I_C, Näherung I_E ≈ I_C, „Basisstrom nicht allgemein vernachlässigbar“ | K | Formel, Fehlvorstellung | dito |
| Sättigung quantitativ (Kollektorwiderstand, Aufteilung des Basisstroms, U_CE,sat) | K | K2, Beispiel | K2, Beispiel, Herleitung U_CE,sat |
| Early-Effekt: Ausgangskennlinie, U_A ↔ 1/λ, Faktor (1 + U_CE/U_A), Wirkung auf I_B | K | Formel, Herleitung, Abbildung | dito, Beispiel |
| Mechanismus Basisweitenmodulation | H | zwei Sätze (in H3) | Text, Herleitung |
| U_CB statt U_CE im Early-Faktor (1,5 % Unterschied) | V | – | Satz |
| Gummel-Plot, B nicht konstant: kleine Ströme (Rekombinationsstrom n = 2), große Ströme (starke Injektion) | H/V | Satz | Abschnitt, Abbildung, Vertiefung |
| Großsignalmodell mit I_B,E-Diode und Bahnwiderständen; R_E als Stromgegenkopplung; vereinfachtes Modell | H | Satz | Abschnitt, Abbildung, Beispiel |
| Vergleich mit dem MOSFET (exponentiell gegen quadratisch, Basisstrom, g_m/I, HF-Eignung) | H | Tabelle kurz | Tabelle, Text |
| Technologie-Motivation (60/77 GHz, 180 nm gegen 65 nm) | H | Satz in Bedeutung | Bedeutung |
| pnp-Transistor in Zahlen, Lateral-pnp | S (später bei Stromspiegeln) | – | Satz |
| Kleinsignalparameter g_m, r_π, r_o | S (Thema 2) | Ausblick | Ausblick |

## 7. Abbildungsplan (Szene-IDs st1/bipolartransistor/01-…)

| ausf. | kompakt | Szene | Vorlage | Inhalt |
|---|---|---|---|---|
| 1 | 1 | 01-einstieg | querschnitt-mit-modell | npn im Normalbetrieb: Elektronenfluss durch die Basis, Löcherstrom der Basis, daneben das vereinfachte Transportmodell mit 1 mA / 10 µA |
| 2 | – | 01-aufbau-diskret-integriert | technologie-querschnitt | diskreter Transistor (Rückseitenkollektor) und integrierter mit buried layer, Substratanschluss, Layout-Draufsicht |
| 3 | 2 | 01-symbole-zaehlpfeile | aufbau-und-symbol | npn und pnp: Schichtfolge mit Diodenersatz, Symbol, Zählpfeile, Vorzeichen im Normalbetrieb |
| 4 | 3 | 01-kennlinien | kennlinie-semilog-paar | Übertragungskennlinie I_C(U_BE) linear und halblogarithmisch, Eingangskennlinie I_B(U_BE); Arbeitspunkt 773,8 mV |
| 5 | 4 | 01-arbeitsbereiche | zustandsebene-und-kennlinienfeld | U_BE/U_BC-Ebene mit den fünf Zuständen; Ausgangskennlinienfeld mit Sättigungsgrenze bei etwa 0,1 bis 0,3 V |
| 6 | 5 | 01-transportmodell | ersatzschaltbild-paar | vollständiges Transportmodell (zwei Dioden, Quelle) und vereinfachtes für den Normalbetrieb, mit Werten bei 1 mA |
| 7 | – | 01-saettigung-stroeme | mengenpfeile-schaltung | Ströme im Transportmodell bei I_B = 50 µA an 2,5 V / 1 kΩ: 24,7 / 25,3 µA, 2,40 mA, U_CE = 100 mV |
| 8 | 6 | 01-early-effekt | kennlinienfeld-extrapolation | Ausgangskennlinien mit Tangenten bis −50 V; daneben Basisweite über U_CB |
| 9 | – | 01-gummel-plot | kennlinie-semilog-gestapelt | Gummel-Plot I_C, I_B über U_BE (log) und B über I_C (log) |
| 10 | – | 01-grossignalmodell | ersatzschaltbild-paar | Großsignalmodell mit I_B,E-Diode und R_B, R_E, R_C; vereinfachtes Modell |

Kompakt 6 Abbildungen, ausführlich 10 (§7.2: je eine pro Sach-Abschnitt, Kipp-Stellen mit Abbildung).

## 8. Zahlenwerk

`zahlen_bipolar.py`, Abschnitte A bis K. Beispiel-npn (integriert): I_S = 1e-16 A, B_N = 100, B_I = 2, U_A = 50 V,
A_E = 20 µm² (5e-18 A/µm² gegen 6,7e-19 beim diskreten ET1-Transistor); U_T = 25,85 mV, 59,5 mV je Dekade, 17,9 mV je
Verdopplung. Arbeitspunkt 1 mA bei 773,8 mV, I_B = 10 µA, I_E = −1,01 mA; A = 0,990. +10 mV → Faktor 1,47; 0,7 V →
57,6 µA; 0,8 V → 2,76 mA; 10 mA bei 833 mV. Early: 1,00/1,02/1,05/1,10 mA bei 0/1/2,5/5 V, Steigung 20 µS, Schnitt
−50 V; exakt 1/(1 − U_CB/U_A) gegen Näherung (1,111 gegen 1,100 bei 5 V). Transportmodell: aktiv 2,5 V: I_T = 1,05 mA,
I_B,I = −5e-17; Sättigung U_BE 0,80/U_BC 0,55: I_B,I = 87 nA; tief 0,80/0,70: I_B,N 27,6 µA, I_B,I 28,8 µA, I_C
2,68 mA, I_C/I_B 47. Sättigungsschaltung 2,5 V/1 kΩ: I_B 5/10/20/23/30/50/100 µA → I_C 0,52/1,03/2,02/2,28/2,36/2,40/
2,43 mA, U_CE 1980/1471/481/217/136/100/75 mV; bei 50 µA I_B,N 24,7, I_B,I 25,3 µA; Grenze ≈ 24 µA. Invers: U_BC 773,8 mV:
I_E = +1,00 mA, I_B = 0,50 mA, B_I = 2. Gummel (I_SE 1e-13 A, n = 2, I_KF 50 mA): B = 3 bei 1 nA, 50 bei 1 µA, 91 bei
0,1 mA, Maximum 95 bei 0,85 mA, 83 bei 10 mA, 62 bei 30 mA, 33 bei 100 mA.
Bahnwiderstände 100/5/20 Ω: bei 1 mA 5 mV an R_E, 1 mV an R_B, Faktor 0,824 bzw. 82,6 % bei fester äußerer Spannung;
bei 10 mA 50 mV, 39,7 %. Vergleich MOSFET 1 mA: g_m 38,7 mS gegen 2 mS (Faktor 19), Faktor 10 im Strom für 59,5 mV
gegen 2,16 V Übersteuerung.

## 9. Profi-Abgleich

- MIT 6.012 (2005), Lecture 18, Ebers-Moll/Transportmodell, Sättigung als Überlagerung von Vorwärts- und Rückwärtsteil:
  https://www.ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/8ea0ef3d8b148059bf82426fea197241_lec18.pdf
- MIT 6.012 (2000), Lecture 17, Großsignalmodell des BJT (Hybrid-π, nichtlinear):
  https://web.mit.edu/6.012/FALL00/www/handouts/lec17.pdf
- Purdue ECE 606, Lecture 19 (Kirk-Effekt, Hochinjektion, Stromverstärkung):
  https://engineering.purdue.edu/~ee606/downloads/ECE606_f12_Lecture19.pdf
- All About Circuits, Performance Limitations of Bipolar Transistors (B über dem Strom):
  https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-devices/performance-limitations-of-bipolar-transistors/

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte:** S. 93 Motivation (HF, 180/250 nm Bipolar gegen 65 nm CMOS), Transportmodell als Fokus, Basisstrom als
Unterschied zum FET; Bild 4.1 diskreter Querschnitt, Dotierungsfolge, Rückseitenkollektor. S. 94 Bild 4.2 integrierter
Querschnitt und Layout, buried layer, Substratanschluss an die negative Versorgung, Emitterfläche als
Skalierungsparameter; 4.2 Funktionsweise, Bild 4.3. S. 95 (4.1) Knotengleichung, (4.2) Diodengleichung, (4.3) B,
(4.4) A, Inversbetrieb B_I. S. 96 Bild 4.4 Symbole, Bild 4.5 Vorzeichen npn/pnp. S. 97 fünf Betriebszustände,
Fußnote Sättigung MOS/BJT, Bild 4.6 Transportmodell. S. 98 (4.5)–(4.7), Bild 4.7 Kennlinien, (4.8), (4.9).
S. 99 (4.10), (4.11), Bild 4.8 Ausgangskennlinie, Early (4.12)–(4.14). S. 100 Bild 4.9 Gummel-Plot und B, Bild 4.10
Großsignalmodell mit Bahnwiderständen.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 94: „Der Kollektorstrom ist direkt proportional zum Basisstrom“ als Tatsache; gilt nur im idealen Modell mit
   festem B_N, die eigene Darstellung auf S. 100 zeigt B zwischen 10 und 125. Hier: B_N als Modellkonstante
   eingeführt, Abweichungen im Gummel-Abschnitt.
2. S. 95 (4.2): „Diodengleichung für den Basis-Emitter-Übergang“ für den Kollektorstrom; das ist der Transportstrom
   durch die Basis, nicht der Strom der Basis-Emitter-Diode (der ist I_E). Hier sauber getrennt.
3. S. 97, Zustand 4: „Die Kollektordiode wird dabei zeitweise in Flussrichtung geschaltet, wodurch diese gesättigt
   wird. Es fließt ein Kollektorstrom, der unabhängig vom Basisstrom ist.“ Nicht zeitweise, sondern bei U_BC > 0;
   gesättigt ist nicht die Diode, sondern der Transistor (Strom vom äußeren Kreis begrenzt); I_C steigt mit mehr
   Basisstrom noch schwach (2,28 → 2,43 mA), weil U_CE,sat sinkt. Hier quantitativ aus dem Transportmodell.
4. S. 97, Bild 4.6/Text: Transportstrom „durch eine stromgesteuerte Stromquelle modelliert“; physikalisch ist die
   Quelle spannungsgesteuert, I_T = I_S(e^{U_BE/U_T} − e^{U_BC/U_T}); die Schreibweise B_N I_B,N − B_I I_B,I ist nur
   eine Umformung (die Einleitung sagt selbst „spannungsgesteuerte Stromquelle“). Hier Kipp-Stelle K1.
5. S. 98, Bild 4.7: Übertragungskennlinie (7 mA bei 1,1 V) und Eingangskennlinie (10 µA bei 0,85 V) passen nicht
   zum selben Transistor mit festem B; hier beide Kurven aus einem Parametersatz.
6. S. 99 (4.13): Early-Faktor mit U_CE statt U_CB; Simulatoren benutzen 1 − U_BC/U_A; Unterschied beim Beispiel
   1,5 %. Hier U_CE wie üblich, Hinweis in der ausführlichen Fassung.
7. S. 99: Early-Effekt nur als „äquivalentes Verhalten“ zur Kanallängenmodulation; der Mechanismus
   (Basisweitenmodulation) fehlt. Hier hergeleitet.
8. S. 100: Abnahme von B bei kleinen Strömen „weil ein kleiner Anteil des Basisstroms nicht zur Steuerung beiträgt“;
   der Grund (Rekombinationsstrom der Raumladungszone mit n = 2, der langsamer fällt als I_C) fehlt, ebenso der
   Abfall bei großen Strömen (starke Injektion). Hier in der Vertiefung mit Zahlen.
9. S. 100: Bahnwiderstände ohne Zahlen; „Emitterwiderstand negative Auswirkungen … Stromgegenkopplung“ ohne Maß.
   Hier 5 Ω → 5 mV → Faktor 0,82 bei 1 mA.
10. S. 95: Bild 4.3(b) zeigt I_B als Zufluss zur Basis, aber die Elektronen in der Basis als Punkte ohne Richtung;
    die Rollen von Elektronen (Transport) und Löchern (Basisstrom) werden nicht getrennt. Hier mit Farben.
