# Arbeitsnotiz: Kennlinien des NMOS-Transistors (ST1, MOS-Feldeffekttransistoren, Thema 2)

Dateien: `content/st1/03-mos-feldeffekttransistoren/02-kennlinien.md` (kompakt) und `…-ausfuehrlich.md`. Frontmatter aus
dem Themenplan: title „Kennlinien des NMOS-Transistors“, pfad „Elektrotechnik / 3. Semester / Schaltungstechnik 1 /
MOS-Feldeffekttransistoren“, order 33030200, tags „ohmscher Bereich, Abschnürbereich, Quadratgesetz,
Kanallängenmodulation, Ausgangskennlinie“. Quelle: PDF S. 73–78 (Abschnitte 3.5 und 3.6), Volltext `st1_clean.txt`
Zeilen 6200–6526. Zahlen: `zahlen_mosfet.py` Abschnitte L bis P (Beispiel-Transistorpaar aus Thema 1).

## 1. Ein-Satz-Prinzip

Durch jeden Querschnitt des Kanals fließt derselbe Strom, Ladung pro Länge mal Geschwindigkeit der Elektronen; wo der Kanal zum
Drain hin dünner wird, laufen die Elektronen schneller, und diese Bedingung über den Kanal integriert ergibt die
Triodengleichung, die an der Abschnürgrenze ihr Maximum erreicht und von dort an als Quadratgesetz stehen bleibt; nur die
Verkürzung des Kanals lässt den Strom danach noch leicht steigen.

## 2. Schwierigkeit und Längenspannen

**schwer**: Herleitung mit Trennung der Variablen und Integration, zwei Kipp-Stellen (Strom bei abnehmender Ladung;
Ende der Triodenformel am Parabelmaximum), Kanallängenmodulation, Unterschwellenstrom (ausführlich). Spannen: kompakt
1800–4000, ausführlich 3500–7000 Wörter.

## 3. Vorwissen-Kette

- Örtliche Kanalladung Q'_n(x) = −C'_ox(U_GS − U_th − U(x)), Abschnürgrenze U_DS = U_GS − U_th, Kanalwiderstand
  R_on = 1/(K_n(U_GS − U_th)), K_n = µ_n C'_ox W/L, Schichtwiderstand, Sperrbereich, schwache Inversion, Oberflächenpotential,
  vollständige Rechnung, Beispieltransistor: Thema 1, erinnern und verlinken.
- Drift J = σE, Beweglichkeit: ET1 „Halbleiter und das Bändermodell“, erinnern.
- Diffusion (Unterschwellenstrom, ausführlich): ET1-Artikel, erinnern.
- Integral als Summe, Trennung der Variablen: Schulmathematik; hier am konkreten Fall vorführen (§5.10).
- MOS-Diode k = K_n/2 = 1 mA/V²: Netzwerkanalyse „Arbeitspunkt und Linearisierung“, verlinken.
- Early-Spannung des Bipolartransistors (70 V im ET1-Zahlenwerk): ET1 Kap. 11, verlinken.
- Modul-Test: GEMB1 „Der MOSFET“ (Gradual-Channel-Herleitung, Bereiche, 60 mV/Dekade) – dieser Artikel gleich tief oder
  tiefer (Herleitung vollständig, Profil, Geschwindigkeit, Kanallängenmodulation, Unterschwelle mit n), verlinken.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Wie kann der Strom überall gleich sein, wenn zum Drain hin weniger Elektronen im Kanal sind?“ → Kipp-Stelle K1,
   Text, beide.
2. „Warum wächst der Strom im ohmschen Bereich nicht linear weiter?“ → Text nach der Triodengleichung, beide.
3. Fehlvorstellung: „Hinter dem Maximum der Parabel nimmt der Strom wieder ab.“ → Fehlvorstellungs-Kasten, beide.
4. Fehlvorstellung: „Doppelte Gatespannung, vierfacher Strom.“ → Fehlvorstellungs-Kasten, beide.
5. „Warum ist der Sättigungsstrom quadratisch?“ → Text (zwei lineare Größen multipliziert), beide.
6. Fehlvorstellung: „Im Abschnürbereich hängt der Strom überhaupt nicht von U_DS ab.“ → Kanallängenmodulation, ausführlich
   als Kasten, kompakt im Text.
7. „Warum treffen sich alle verlängerten Kennlinien in einem Punkt, der Early-Spannung?“ → Text mit Herleitung, beide.
8. „Warum ist λ größer, als die Verkürzung der Kanallänge ergibt?“ → Frage-Kasten, ausführlich.
9. „Fließt unterhalb der Schwelle Strom?“ → eigener Abschnitt ausführlich, Frage-Kasten kompakt.
10. „Wie bestimmt man U_th aus einer Messung?“ → Frage-Kasten ausführlich (√I_D über U_GS).
11. „Woher kommt der Faktor 1/2?“ → So liest man das bzw. Herleitung, beide.
12. „Gilt das Quadratgesetz auch für sehr kurze Transistoren?“ → Frage-Kasten ausführlich (Geschwindigkeitssättigung).
13. „Was rechnet ein Schaltungssimulator mit diesen Gleichungen?“ → Beispiel ausführlich (SPICE-Modell).
14. „Wie lange braucht ein Elektron durch den Kanal?“ → Beispiel ausführlich (92 ps).

## 5. Kipp-Stellen

**K1: Gleicher Strom bei abnehmender Ladung.** Schritte: (1) Strom = Ladung pro Länge × Geschwindigkeit; (2) im
stationären Zustand an jeder Stelle gleich (sonst Aufstauen); (3) Ladung sinkt zum Drain → Geschwindigkeit und Feld
steigen; (4) Feld = Gefälle des Kanalpotentials, also steigt U(x) zum Drain hin immer steiler; (5) Gleichung
I_D dx = W µ_n C'_ox (U_GS − U_th − U) dU, integriert → Triodengleichung. Tragende Zahl: U_GS = 1 V, U_DS = 0,3 V:
Ladung 100 → 40 %, Geschwindigkeit 6,1·10⁵ → 1,5·10⁶ cm/s, Strom überall 0,21 mA. Abbildung 02-kanal-geschwindigkeit.
Herleitung: Triodengleichung. Beispiel: Triodenwerte und Geschwindigkeiten.

**K2: Ende der Triodenformel, Quadratgesetz.** Schritte: (1) Triodengleichung ist eine nach unten offene Parabel in
U_DS; (2) ihr Maximum liegt genau bei U_DS = U_GS − U_th, der Abschnürgrenze; (3) jenseits davon würde die Formel fallen,
aber dort gilt ihre Voraussetzung (Kanal bis zum Drain) nicht mehr; (4) der Kanal bis zum Abschnürpunkt sieht immer
U_GS − U_th → Strom bleibt beim Maximum; (5) Wert: K_n/2 (U_GS − U_th)², quadratisch, weil Ladung und Spannungsabfall
über dem Kanal beide mit der Übersteuerung wachsen. Tragende Zahlen: 0,25 mA bei 1 V (Parabel fortgesetzt: 0,19 mA bei
0,75 V, 0 bei 1 V); 1 → 2 V Gatespannung: neunfach. Abbildung 02-triode-parabel, 02-kennlinienfeld. Herleitung:
Sättigungsstrom. Beispiel: Sättigungsströme.

**K3 (ausführlich ausführlicher): Kanallängenmodulation.** (1) Zone vor dem Drain wächst mit U_DS; (2) Kanal kürzer,
Strom ∝ 1/L_eff; (3) näherungsweise linear: Faktor (1 + λU_DS); (4) Geraden treffen sich bei −1/λ = −10 V; (5) λ wird
gemessen, die 1D-Abschätzung gibt nur 0,027 1/V (2D-Feld, Rückwirkung des Drains auf den Kanal). Tragende Zahl: 0,25 → 0,30 mA bei 2 V.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Kennlinienbegriffe: Ausgangskennlinie, Übertragungskennlinie, Kennlinienfeld, Parameter | K | Abschnitt | Abschnitt |
| Strom = Ladung pro Länge × Geschwindigkeit, gleich in jedem Querschnitt | K | Kipp-Stelle | Kipp-Stelle |
| Herleitung Triodengleichung (Trennung der Variablen) | K | Formel, Herleitung | dazu Beispiel |
| Kanalpotential U(x) und Geschwindigkeit längs des Kanals | H | Zahlen im Text | Formel, Herleitung, Beispiel |
| Vergleich mit R_on (Tangente im Ursprung) | K | Text | Text, Beispiel |
| Parabelmaximum = Abschnürgrenze, Fortsetzung falsch | K | Kipp-Stelle, Fehlvorstellung | dazu Beispiel |
| Quadratgesetz, Faktor 1/2, Grenzkurve K_n/2 U_DS² | K | Formel, Herleitung | dazu Beispiel |
| Übertragungskennlinie, Schwellenbestimmung √I_D | K/H | Übertragungskennlinie im Text | dazu Frage-Kasten, Abbildung |
| Fehlvorstellung doppelte Gatespannung | K | Fehlvorstellung | Fehlvorstellung |
| Bereichstabelle (Shichman-Hodges) mit (1 + λU_DS), auch im ohmschen Bereich | K | Formel | Formel |
| Kanallängenmodulation, λ, Early-Spannung, Steigung λ I_D,sat | K | Abschnitt | Abschnitt mit Herleitung |
| 1D-Abschätzung gegen λ (Faktor 3,8) | H | – | Frage-Kasten |
| Großsignal-Ersatzschaltbild (gesteuerte Stromquelle) | K | Text, Abbildung | Text, Abbildung |
| SPICE-Level-1-Parameter | V | – | Beispiel |
| Laufzeit 92 ps | V | – | Beispiel |
| Unterschwellenstrom, S = n U_T ln 10 ≈ 83 mV/Dekade, 0,56 pA | H | Frage-Kasten | Abschnitt, Herleitung, Abbildung |
| Kurzkanal (Geschwindigkeitssättigung) | V | – | Frage-Kasten/Grenzen |
| MOS-Diode der Netzwerkanalyse als Sonderfall | V | Ausblick | Beispiel |
| Kleinsignal g_m, g_DS | S (Thema 5) | – | Ausblick |
| PMOS-Gleichungen, Substrateffekt | S (Thema 3) | – | – |

## 7. Abbildungsplan (Szene-IDs st1/mos-feldeffekttransistoren/02-…)

| ausf. | kompakt | Szene | Inhalt |
|---|---|---|---|
| 1 | 1 | 02-kennlinienfeld | Ausgangskennlinienfeld ohne KLM, U_GS = 0,75/1/1,25/1,5 V, Grenzparabel, Bereiche; Übertragungskennlinie in Sättigung |
| 2 | 2 | 02-kanal-geschwindigkeit | U(x), Ladung, Geschwindigkeit längs des Kanals bei 1 V/0,3 V |
| 3 | 3 | 02-flaeche-uebersteuerung | Übersteuerung über dem Kanalpotential, Fläche 0,105 V² (0,3 V), Dreieck 0,125 V² (0,5 V und darüber) |
| 4 | 4 | 02-triode-parabel | Triodenparabel bei 1 V, fortgesetzt gestrichelt, wirklicher Verlauf, Tangente R_on |
| 5 | – | 02-schwellenbestimmung | I_D und √I_D über U_GS, Gerade schneidet bei 0,5 V |
| 6 | 5 | 02-kanallaengenmodulation | Kennlinien mit λ, Verlängerung bis −10 V |
| 7 | 6 | 02-ersatzschaltbild | Großsignal-Ersatzschaltbild und Bereichsformeln |
| 8 | 7 | 02-arbeitspunkt | im Beispiel: Schaltung mit 4 kΩ an 2,5 V, Arbeitsgerade, Arbeitspunkte 1,36 V/0,284 mA und 0,31 V/0,546 mA |
| 9 | – | 02-unterschwelle | log I_D über U_GS, 83 mV/Dekade, 0,56 pA bei 0 V |

Nachtrag beim Schreiben: Abbildung 3 (Fläche) und die Arbeitspunkt-Abbildung im Beispiel zum Großsignalmodell neu; Abbildung 3, weil sie Triodengleichung, Maximum an der Abschnürgrenze und
Quadratgesetz in einem Bild verbindet; Unterschwelle als letzter Sach-Abschnitt nach dem Großsignalmodell. Zusätzliche
Zahlen in Abschnitt Q des Zahlenwerks (Fläche, Steigung, negative U_DS, Tangente 0,75 V, 40 kΩ, Lehrbuch-λ, Kurzkanal,
Arbeitspunkt mit 4 kΩ, C'_dep). Profi-Abgleich ergänzt: Sedra/Smith, Anhang K (typische Prozessparameter, |V'_A| ≈ 5 V/µm
für Prozesse mit 4–6 nm Oxid): https://learninglink.oup.com/protected/files/content/file/1605812108812-Sedra8e_AppK.pdf

## 8. Zahlenwerk

Abschnitte L bis P in `zahlen_mosfet.py`: Triodenwerte (0,09/0,16/0,21/0,24/0,25 mA bei 0,1–0,5 V; Verhältnis zur
linearen Näherung 1 − U_DS/(2U_ov)); Sättigungsströme 0,01/0,0625/0,25/0,5625/1/2,25/4 mA bei 0,6–2,5 V; Faktor 9 bei
doppelter Gatespannung, 4 bei doppelter Übersteuerung; Grenzkurve; Profil, Feld, Geschwindigkeit, Laufzeit (122 ps bei
0,3 V, 92 ps an der Grenze); KLM 0,2625/0,275/0,30/0,3125 mA bei 0,5/1/2/2,5 V, Steigung 25 µA/V, Early −10 V,
1D-λ 0,027 (bezogen auf den Strom des Quadratgesetzes); Unterschwelle 0,56 pA/8,1 pA/0,12 nA/2,0 nA/32 nA bei 0/0,1/0,2/0,3/0,4 V, S = 82,8 mV/Dekade, n = 1,36,
Ein-Aus-Verhältnis 7·10⁹; SPICE-Zeile.

## 9. Profi-Abgleich

- Berkeley EECS 105 (Niknejad/Muller), MOSFET-I-V-Herleitung im selben Kursmaterial wie Thema 1 (Gradual Channel,
  Sättigung, Kanallängenmodulation als (1 + λV_DS)).
- Shichman, Hodges: „Modeling and simulation of insulated-gate field-effect transistor switching circuits“, IEEE JSSC
  1968 (Level-1-Modell) – Herkunft der Gleichungen mit (1 + λU_DS).
- Die Unterschwellensteigung n U_T ln 10 mit n = 1 + C_dep/C_ox ist Standard (Tsividis, Sze).

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte:** S. 73 Sperrbereich I_D ≈ 0, Hinweis auf Unterschwellenmodelle (EKV) und Leckströme in großen
Digitalschaltungen; Langkanal-Annahme; S. 74 Ladung je Länge W C'_ox (U_GS − U_th), Bild 3.8; S. 74–75 örtliche Ladung,
Strom als Ladung mal Geschwindigkeit, v = µ dU/dl, Integration (3.9), Triodengleichung (3.10/3.11), Bild 3.10
(Parabeln mit gestrichelter Fortsetzung); S. 76 Abschnürbereich mit U_GD < U_th, Ersetzen U_DS → U_GS − U_th,
Quadratgesetz (3.14), Zusammenfassung mit K_n = K'_n W/L (Steilheitskoeffizient), K'_n = µ_n C'_ox; S. 77 Bild 3.11
(Ausgangs- und Übertragungskennlinie, Tangente zur Schwelle), Kanallängenmodulation, Bild 3.12, Early-Spannung,
Bild 3.13; S. 78 λ = 1/|U_Early|, Level 1/Shichman-Hodges (3.16) mit (1 + λU_DS) in beiden Bereichen,
Großsignal-Ersatzschaltbild Bild 3.14.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 74: „Ladungsdichte je nm Kanallänge“ → Ladung pro Länge (Einheit C/m).
2. S. 74 (3.6): Herleitung „I_D = Q_ges/t = Q_d(l)·l/t“ unsauber (l als Weg pro Zeit) → Strom = Ladung pro Länge mal
   Geschwindigkeit.
3. S. 74 (3.7): „v_n = µ_n E(l) = µ_n dU/dl“ mischt Vorzeichen: Das Feld ist −dU/dl, Elektronen laufen gegen das Feld,
   ihre Geschwindigkeit zum Drain ist µ_n dU/dl.
4. S. 75 (3.10): U_D und U_DS gemischt.
5. S. 77: Early-Spannung „bei sehr kleinen Werten (−100 V)“ bzw. für Kurzkanal „vergleichsweise groß (> −5 V)“ – Betrag
   bei Langkanal und BJT groß (z. B. 100 V), bei Kurzkanal klein (einige V).
6. S. 77, Bild 3.11 b: Tangente an die Übertragungskennlinie in Sättigung trifft die Achse nicht bei U_th (Quadratgesetz:
   bei (U_GS0 + U_th)/2); richtig ist die Gerade √I_D über U_GS oder die Extrapolation im ohmschen Bereich.
7. S. 76: „das horizontale elektrische Feld hängt nicht mehr von U_DS ab“ – im Kanal ja, in der Zone vor dem Drain nicht
   (präzisiert).
