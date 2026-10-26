# Arbeitsnotiz: Kleinsignalmodell des MOSFET (ST1, MOS-Feldeffekttransistoren, Thema 5)

Dateien: `content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Kleinsignalmodell des MOSFET“, pfad „Elektrotechnik / 3. Semester /
Schaltungstechnik 1 / MOS-Feldeffekttransistoren“, order 33030500, tags „Steilheit, Ausgangsleitwert, Substratsteilheit,
Kleinsignalersatzschaltbild, SPICE-Modell“. Quelle: PDF S. 88–92 (3.11–3.13) und S. 271 (Anhang B, SPICE-Modellkarten),
Volltext `st1_clean.txt` Zeilen 7089–7478 und 21137–21208. Zahlen: `zahlen_mosfet.py` Abschnitte AE bis AM.

## 1. Ein-Satz-Prinzip

Um einen festen Arbeitspunkt ersetzt man jede Kennlinie des MOSFET durch ihre Tangente: Gate, Drain und Bulk steuern
den Drainstrom dann linear, jeder mit einer eigenen Steilheit, die vom Arbeitspunkt abhängt, und für schnelle Änderungen
kommen die Kapazitäten zwischen den Anschlüssen hinzu.

## 2. Schwierigkeit und Längenspannen

**mittel**: ein Verfahren (Linearisierung) auf drei Steuergrößen und zwei Bereiche angewandt, dazu das Ersatzschaltbild;
eine Kipp-Stelle (Substratsteilheit mit Vorzeichen) und eine zweite kleinere (wie klein ist klein, Wahl der Näherung).
Spannen: kompakt 1000–3000, ausführlich 2000–5000 Wörter; erwartet kompakt um 2300, ausführlich um 4000.

## 3. Vorwissen-Kette

- Linearisierung, differentieller Leitwert, partielle Ableitungen, gesteuerte Quellen, Klein- und
  Großsignal-Ersatzschaltbild: Netzwerkanalyse, Arbeitspunkt und Linearisierung (dort hergeleitet), erinnern und
  verlinken.
- Großsignalmodell mit Triodengleichung, Quadratgesetz, Kanallängenmodulation (λ = 0,1 1/V, Early-Spannung 10 V):
  Thema 2, erinnern und verlinken.
- Substrateffekt, γ = 0,629 √V, 2Φ_F = 0,923 V, η = C'_dep/C'_ox, Sourcefolger mit Steigung 0,80: Thema 3, verlinken.
- Kapazitäten C_GS, C_GD, C_GB, C_SB, C_DB mit Werten, Miller-Effekt: Thema 4, verlinken.
- Unterschwellensteigung 83 mV/Dekade: Thema 2 (nur ausführlich, g_m/I_D).
- Modul-Test: In ET1 gibt es das Kleinsignalmodell des Bipolartransistors (Hybridform) und die Netzwerkanalyse nutzt
  g_m = 1 mS, g_o = 25 µS als gegebene Werte; dieser Artikel leitet sie her und ist tiefer.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Was soll ein Kleinsignalmodell, wenn ich doch die Kennliniengleichung habe?“ → Worum es geht und erster Abschnitt,
   Text, beide.
2. „Warum hängen g_m und g_o vom Arbeitspunkt ab, sind das nicht Eigenschaften des Transistors?“ → Text, beide.
3. Fehlvorstellung: „Die Steilheit ist eine feste Transistorkonstante wie K.“ → Fehlvorstellungs-Kasten, beide
   (1,1 mS bei 0,275 mA, 2,2 mS bei 1,1 mA).
4. „Welche der drei Formeln für g_m stimmt denn?“ (K U_ov, 2I_D/U_ov, √(2KI_D)) → So liest man das, beide.
5. „Wie klein muss ein Signal sein?“ → Text und Beispiel, beide (10 mV → 1 %).
6. „Warum ist der Faktor (1 + λU_DS) bei 1 V schon 10 % und trotzdem lässt man ihn weg?“ → Frage-Kasten, ausführlich;
   kompakt ein Satz.
7. „Warum ist der Transistor im ohmschen Bereich ein schlechter Verstärker?“ → Text, beide (g_m/g_o = 0,25 bei 0,1 V).
8. Fehlvorstellung: „Die Substratsteilheit wirkt der Steilheit entgegen, deshalb ist g_mB negativ.“ →
   Fehlvorstellungs-Kasten, beide.
9. „Woher weiß ich, in welche Richtung die g_mB-Quelle zeigt?“ → Kipp-Stelle, Text, beide.
10. „Gilt das Ersatzschaltbild auch für den PMOS?“ → Frage-Kasten, beide.
11. „Warum fehlt das Gate im statischen Ersatzschaltbild als Strompfad?“ → Text, beide.
12. „Warum vernachlässigt man R_D, R_S, R_B, aber nicht R_G?“ → Text, ausführlich mit Zahlen; kompakt ein Satz.
13. „Bis zu welcher Frequenz verstärkt ein Transistor überhaupt?“ → Vertiefung f_T, ausführlich.
14. „Was steht in einer SPICE-Modellkarte, und wie hängen die Parameter mit den Formeln zusammen?“ → Abschnitt,
    ausführlich; kompakt ein Absatz.
15. „Wie bekomme ich mit wenig Strom viel Steilheit?“ → Vertiefung g_m/I_D, ausführlich.

## 5. Kipp-Stellen

**K1: Substratsteilheit und Vorzeichen.** Schritte: (1) Der Bulk wirkt über die Verarmungsladung als zweites Gate,
mit dem Kapazitätsverhältnis η = C'_dep/C'_ox (Thema 3). (2) Steigt U_BS (Bulk höher, U_SB kleiner), sinkt die
Schwelle um η · u_BS, die Übersteuerung wächst, I_D steigt: g_mB = η g_m > 0, gleiche Richtung wie g_m. (3) Im
Ersatzschaltbild zwei Quellen gleicher Richtung D→S. (4) In der Schaltung liegt der Bulk meist fest an Masse; steigt die
Source, ist u_BS = −u_S negativ, und die Quelle nimmt Strom weg: Sie wirkt wie ein Leitwert η g_m von der Source nach
Masse. (5) Beim Sourcefolger: Verstärkung 1/(1 + η) = 0,806, Ausgangswiderstand 806 Ω statt 1 kΩ; das ist die Steigung
aus Thema 3. Abbildungen 05-substratsteilheit, 05-sourcefolger-kleinsignal. Herleitung g_mB = η g_m. Beispiel Folger.

**K2: Steigung im Arbeitspunkt und Gültigkeit.** Schritte: Tangente, drei Steigungen, Summe; Fehler wächst mit
u/(2U_ov): 10 mV → 1 %, 100 mV → 10 %. Abbildung 05-steilheit. Herleitung Linearisierung (Verweis Netzwerkanalyse).
Beispiel Linearisierungsfehler.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Linearisierung des Drainstroms nach drei Spannungen, Kleinsignalgrößen als Kleinbuchstaben | K | Formel, kurze Herleitung | Formel, Herleitung |
| Steilheit Abschnürbereich K U_ov(1+λU_DS) = 2I_D/U_ov ≈ √(2KI_D), ohmsch K U_DS(1+λU_DS) | K | Formel, Herleitung, Beispiel | dito, Abbildung |
| Ausgangsleitwert Abschnürbereich λK/2 U_ov² = I_D/(1/λ + U_DS) ≈ λI_D, ohmsch exakt und ≈ K(U_ov − U_DS) | K | Formel, Herleitung | dito, Early-Deutung |
| Substratsteilheit η g_m, η = γ/(2√(2Φ_F + U_SB)) in beiden Bereichen | K | Formel, Herleitung | dito, η über U_SB |
| Vorzeichen und Richtung der g_mB-Quelle, Wirkung im Folger | K | Kipp-Stelle, Beispiel | Kipp-Stelle, Beispiel |
| Stetigkeit an der Abschnürgrenze (g_m, g_o) | H | Satz | Satz, Zahl |
| ohmscher Bereich als schlechter Verstärker (g_m/g_o) | H | Satz mit Zahl | Text, Beispiel |
| Eigenverstärkung g_m/g_o = 2/(λU_ov) | H | Satz | Text, Zahl 40/44 |
| Linearisierungsfehler u/(2U_ov), zweite Harmonische | H | Satz mit Zahl | Beispiel |
| (1 + λU_DS) weglassen: 10 % bei 1 V, Werte der Netzwerkanalyse | H | Satz | Frage-Kasten |
| statisches Ersatzschaltbild, PMOS gleich (Vorzeichen positiv) | K | Abbildung, Text, Frage | dito |
| dynamisches Ersatzschaltbild mit sechs Kapazitäten und Bahnwiderständen, Vereinfachung | K | Abbildung, Text | Abbildung, Text, Zahlen |
| R_G mit Eingangskapazität als Tiefpass (2 kΩ ohne Silizid, 80 Ω mit) | H | Satz | Text, Zahl |
| Transitfrequenz f_T (3 GHz) | V | – | Vertiefung mit Herleitung |
| g_m/I_D, schwache Inversion 28 1/V | V | – | Vertiefung |
| SPICE-Modellkarte Level 1 mit Werten der Themen 1 bis 4 | H/V | kurzer Absatz | Abschnitt, Beispiel |
| Messung von g_m und g_o an der Kennlinie | V | – | Satz |
| Bipolar-Vergleich | S (Kapitel Bipolartransistor) | – | Ausblick |

## 7. Abbildungsplan (Szene-IDs st1/mos-feldeffekttransistoren/05-…)

| ausf. | kompakt | Szene | Inhalt |
|---|---|---|---|
| 1 | 1 | 05-tangenten-uebersicht | Kennlinien mit Tangenten im Arbeitspunkt und daneben das statische Ersatzschaltbild |
| 2 | 2 | 05-steilheit | Übertragungskennlinie bei U_DS = 1 V mit Tangente bei 1 V (1,1 mS), darunter g_m über U_GS; Linearisierungsfehler |
| 3 | – | 05-gm-id | g_m/I_D über U_GS, 28 1/V unterhalb der Schwelle, 4 1/V bei 0,5 V |
| 4 | 3 | 05-ausgangsleitwert | Ausgangskennlinie bei U_GS = 1 V, Tangente bei 1 V (25 µS) mit Schnitt bei −10 V; g_m und g_o über U_DS |
| 5 | 4 | 05-substratsteilheit | I_D über U_BS bei 1 V/1 V mit Tangente (0,36 mS); η über U_SB |
| 6 | – | 05-esb-statisch | statisches Ersatzschaltbild NMOS und PMOS, Richtungen, Zählpfeile |
| 7 | 5 | 05-sourcefolger-kleinsignal | Folger und sein Kleinsignal-Ersatzschaltbild, g_mB als Leitwert, 0,806, 806 Ω |
| 8 | 6 | 05-esb-dynamisch | vollständiges und vereinfachtes dynamisches Ersatzschaltbild mit Werten |

## 8. Zahlenwerk

Abschnitte AE bis AM in `zahlen_mosfet.py`. Arbeitspunkt U_GS = 1 V, U_DS = 1 V, U_SB = 0: I_D 0,275 mA, g_m 1,1 mS
(Näherung 1,0; 2I_D/U_ov 1,1 exakt; √(2KI_D) 1,049), g_o 25 µS (λI_D 27,5), r_o 40 kΩ, g_m/g_o 44 (Näherung 40),
η 0,327, g_mB 0,360 mS. 1,5 V/1 V: 1,1 mA, 2,2 mS, 100 µS, 22. U_DS 0,5 V: 1,05 mS, 25 µS beidseits stetig. Ohmsch bei
1 V: 0,1 V: g_m 0,202 mS, g_o 0,817 mS (Näherung 0,8), Verhältnis 0,247; 0,3 V: 0,618/0,433. Linearisierung: 10 mV →
11,11 statt 11,00 µA (+1 %), 100 mV +10 %, −100 mV −10 %; Sinus 10 mV: 2. Harmonische 0,5 %. η über U_SB 0/0,5/1/1,5/2 V:
0,327/0,264/0,227/0,202/0,184; I_D(U_BS) 0,275 mA bei 0, 0,0593 mA bei −1 V, 0,406 mA bei +0,3 V; Tangente 0,360 mS.
Folger (Thema 3, U_aus 0,783 V): η 0,2407, Verstärkung 0,806 = Großsignal-Differenzenquotient, r_aus 806 Ω (1 kΩ ohne
Substrateffekt). PMOS −1 V/−1 V: I_D −0,275 mA, g_m 1,1 mS, g_o 25 µS, η_p 0,321, g_mB 0,353 mS. Dynamisch: C_GS 49,5,
C_GD 3,45, C_SB 53,1 (+15 Kanal-Bulk), C_DB 37,8 fF; f_T 3,31 GHz (1,1 mS) bzw. 3,01 GHz; Langkanal ohne Überlappung
3,46 GHz; R_G 2 kΩ (ohne Silizid) bzw. 80 Ω, R_G C = 106 ps bzw. 4,2 ps; R_S 20 Ω → g_m −2,2 %. g_m/I_D: 4 1/V bei
0,5 V, 20 1/V bei 0,1 V, 27,9 1/V unter der Schwelle (Grenze 38,7). SPICE-Karte mit CGSO 3,45e-10 F/m, CJ 2,14e-3 F/m²,
CJSW 4,28e-10 F/m, PB 1,027, LD 50n, L = 1,1 µm gezeichnet.

## 9. Profi-Abgleich

- MIT 6.012, Lecture 10 (Kleinsignalmodell, g_m, g_o, g_mb in Sättigung): https://web.mit.edu/6.012/FALL00/www/handouts/lec10.pdf
- D. Johns (Toronto), Body Effect, g_mb = η g_m mit η = γ/(2√(2φ_F + V_SB)): https://www.eecg.utoronto.ca/~johns/ece331/lecture_notes/07b_bodyEffect.pdf
- Utah State, Small-Signal Analysis and Design: https://left.engr.usu.edu/courses/5420/Small-Signal%20Analysis%20and%20Design.html

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte:** S. 88 Linearisierung (3.26–3.30), Merksatz fester Arbeitspunkt, Steilheit Abschnürbereich (3.31) mit
≈ und √(2KI_D), U_BS = 0 angenommen; S. 89 Steilheit ohmsch (3.32), Bild 3.24, Ausgangsleitwert (3.33, 3.34);
S. 90 Bild 3.25, Substratsteilheit (3.35, 3.36), gleiches Vorzeichen; S. 91 η ~ 0,1, Vernachlässigung in
Handrechnungen, Bild 3.26, statisches ESB Bild 3.27, PMOS/NMOS, Fußnote 7; S. 92 dynamisches ESB 3.28 mit
Bahnwiderständen, R_G nicht vernachlässigt, Eingangskapazität mit Miller, vereinfachtes ESB 3.29; S. 271 SPICE-Karten.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 88 (3.31): „= √(2KI_D,A)“ als Gleichung – gilt nur ohne Kanallängenmodulation; exakt ist 2I_D/U_ov, und mit
   I_D einschließlich (1 + λU_DS) ergibt √(2KI_D) 1,049 statt 1,1 mS.
2. S. 89 (3.33): „≈ λI_D,A“ – exakt ist I_D/(1/λ + U_DS); λI_D liegt bei 1 V um 10 % zu hoch.
3. S. 90 (3.36): Zwischenschritt mit ∂U_th/∂U_BS ohne Minuszeichen; richtig −∂U_th/∂U_BS = η.
4. S. 90/91, Bild 3.26: „Rückwärtsausgangskennlinie“ über positivem U_BS (0 bis 0,5 V, Durchlassrichtung der
   Source-Bulk-Diode) und fast waagerecht, obwohl g_mB = η g_m mit η ≈ 0,1–0,3 eine deutliche Steigung verlangt.
5. S. 91: η „in der Größenordnung 0,1“ – hängt von Dotierung und Oxid ab; beim Beispiel 0,33 bei U_SB = 0, 0,18 bei 2 V.
6. S. 91, Fußnote 7: Richtung und Vorzeichen „nicht eindeutig“, der Designer müsse sicherstellen, dass g_mB der
   Steilheit entgegenwirkt – mit I_D in den Drain und g_mB = ∂I_D/∂U_BS ist alles eindeutig: beide Quellen zeigen von
   Drain nach Source, und die Gegenwirkung entsteht von selbst, weil u_BS im Folger negativ wird.
7. S. 91: „Drain beim p-Kanal-MOSFET der Anschluss mit dem niedrigeren Potential“ – richtig, aber die Parameter bleiben
   positiv; die Vorzeichen der Kleinsignalspannungen tragen die Richtung (ergänzt).
8. S. 92: „Bahnwiderstände … niederohmig, da hochohmige MOS-Technik“ – Begründung präzisiert: R_S klein gegen 1/g_m
   (20 Ω gegen 909 Ω); R_G zählt, weil er mit der Eingangskapazität einen Tiefpass bildet.
9. S. 92, Bild 3.29: „vereinfacht (C_GB = R_B = 0)“ – zusätzlich sind R_G, R_D, R_S, C_BS und C_BD weggelassen; C_DS steht
   für C_DB bei Bulk an Source.
10. S. 271, Anhang B: Modellkarten ohne Einheiten und ohne Bezug zu den Formeln (CJ in F/m², CJSW und CGSO in F/m); hier
    eigene Karte mit Bedeutung jedes Parameters.
