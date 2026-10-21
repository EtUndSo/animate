# Arbeitsnotiz: Der Transistor als Verstärker (ET1 Kap. 11.5 ohne Grundschaltungs-Kennlinien, und 11.6), Stil 3

Skript S. 188–193 (PDF 194–199): reale Kennlinien (Bild 11.19, 11.20), erweitertes Ersatzschaltbild „Großsignal“ (Bild 11.21),
Spannungsstabilisierung (Bild 11.28, 11.29). Die Grundschaltungen aus 11.5 (S. 190–192) stehen schon in 11/02; hier kommen sie für kleine
Signale dazu. Der Skriptabschnitt ist knapp; Kleinsignal-Ersatzschaltbild, Steilheit und Spannungsverstärkung gehören zum Kern des
Themas „linearer Verstärker“ (Allgemeinwissen, Lehrbuchstoff, im Praktikum MiNa gebraucht) und werden hier von Grund auf erklärt.

## 1. Ein-Satz-Prinzip

Ein Transistor verstärkt, weil eine kleine Änderung der Basis-Emitter-Spannung den Kollektorstrom mit der Steilheit $I_C/U_T$ ändert und ein
Widerstand diese Stromänderung in eine große Spannungsänderung verwandelt; gleichmäßig gelingt das nur für Änderungen, die klein gegen $U_T$
sind, und ein Emitterwiderstand tauscht Verstärkung gegen Linearität und Unabhängigkeit vom Transistor.

## 2. Schwierigkeit und Längenspannen

Schwer: mehrere zusammenwirkende Mechanismen (Linearisierung, Steilheit, Ersatzschaltbilder, Gegenkopplung im Signalweg, drei Grundschaltungen,
Längsregler) und drei Kipp-Stellen. Kompakt 1800–2800 Wörter, ausführlich 3500–5000 Wörter.

## 3. Vorwissen-Kette

- Transfergleichung $I_C = I_S\exp(U_{BE}/U_T)$, $B$, Early-Effekt: erklärt in 11/01 (Abschnitte *Der Transistoreffekt*, *Der Basisstrom und
  die Stromverstärkung*) → erinnern, verlinken.
- Arbeitspunkt, Stromgegenkopplung mit Teiler und $R_E$ (Beispielstufe 10 V, 330 k/68 k, 3,9 k, 1 k), Grundschaltungen, Emitterfolger: 11/02
  → erinnern, verlinken; die Beispielstufe wird hier zur Verstärkerstufe.
- Tangente, differentieller Widerstand $r_d = U_T/I$, „Kleinsignal heißt klein gegen $U_T$“, Kleinsignal-Ersatzschaltbild der Diode: 10.4/10.5
  *Der differentielle Widerstand* → erinnern, verlinken, auf den Transistor übertragen.
- Überlagerung (Gleichanteil plus Änderung, feste Quellen verschwinden für Änderungen): 07 Superposition → erinnern, verlinken.
- Kondensator sperrt Gleichstrom, Spannung ändert sich langsam (Zeitkonstante): 04 → erinnern, verlinken; für Signale „Kurzschluss“ hier aufbauen.
- Z-Diode mit $r_Z$, Stabilisierung mit Vorwiderstand (12 V ± 1 V, 330 Ω, 5,6 V, 20 Ω, Glättungsfaktor 17,8): 10.3 *Die Z-Diode* → erinnern.
- Zweitor in Hybridform (h-Parameter): 07 Zweitore → nur für den Datenblatt-Frage-Kasten verlinken.
- Hier aufbauen: Steilheit, $r_{BE}$, $r_{CE}$, erweitertes und Kleinsignal-Ersatzschaltbild des Transistors, Spannungsverstärkung, Gegenkopplung
  im Signalweg, Grundschaltungen im Kleinsignal, Längsregler.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Woher kommt die Energie für das größere Signal?“ → Spannungsverstärkung → Frage-Kasten → beide.
2. „Warum darf das Eingangssignal nur wenige Millivolt groß sein?“ → Groß- und Kleinsignal → Text (K1) → beide.
3. „Ist die Spannungsverstärkung nicht einfach B?“ (Fehlvorstellung) → Spannungsverstärkung → Fehlvorstellungs-Kasten → beide.
4. „Warum verschwinden die Gleichspannungsquellen im Kleinsignal-Ersatzschaltbild?“ → Kleinsignal-Ersatzschaltbild → Text → beide.
5. „Warum ist r_BE so groß, der Übergang hat vom Emitter aus doch nur 13 Ω?“ → reale Kennlinien → Frage-Kasten → ausführlich.
6. „r_BE und r_CE sind doch Widerstände im Halbleiter?“ (Fehlvorstellung) → reale Kennlinien → Fehlvorstellungs-Kasten → ausführlich.
7. „Wozu die drei Kondensatoren?“ → Spannungsverstärkung → Text (Schritt 1) → beide.
8. „Wie groß müssen die Kondensatoren sein?“ → Spannungsverstärkung → Frage-Kasten → ausführlich.
9. „Warum kehrt die Emitterschaltung das Signal um?“ → Spannungsverstärkung → Text → beide.
10. „Kleinsignal heißt, dass auch das Ausgangssignal klein ist?“ (Fehlvorstellung) → Groß- und Kleinsignal → Fehlvorstellungs-Kasten → beide.
11. „Warum nimmt man für die Stabilisierung nicht die Z-Diode allein?“ → Stabilisierung → Text → beide.
12. „Warum U_Z − U_BE, das Skript schreibt doch +?“ → Stabilisierung → Text mit Skriptkorrektur → beide.
13. „Was bedeuten h_ie, h_fe, h_oe im Datenblatt?“ → reale Kennlinien → Frage-Kasten → ausführlich.
14. „Warum heißt das Ersatzschaltbild im Skript Großsignal-Ersatzschaltbild, wenn es nur nahe am Arbeitspunkt gilt?“ → erweitertes
    Ersatzschaltbild → Frage-Kasten → ausführlich.
15. „Was passiert, wenn die Eingangsspannung des Reglers zu weit sinkt?“ → Stabilisierung → Text/Beispiel → ausführlich.

## 5. Kipp-Stellen

**K1 Steilheit und Kleinsignal am Transistor.** Schritte: Transfergleichung erinnern; Änderung $u_{be}$ multipliziert $I_C$ mit
$\exp(u_{be}/U_T)$, unabhängig vom Arbeitspunkt; für $u_{be} \ll U_T$ Tangente $i_c = (I_C/U_T)\,u_{be}$; Steilheit $g_m = I_C/U_T$;
größere Änderungen asymmetrisch (+47 %/−32 % bei 10 mV) → Verzerrung. Abbildung 03-tangente. Zahlen: 36,6 mS bei 0,947 mA, 77,4 mS bei
2 mA; 1 mV → +3,94 %/−3,79 %; Fehler der Tangente 2 % bzw. 22 %; k2 0,88 % bei 1 mV, 8,7 % bei 10 mV (Stufe mit C_E). Herleitung: Ableitung
der Transfergleichung; ausführlich zusätzlich k2 ≈ û/(4U_T) über den quadratischen Taylor-Term. Beispiel: Steilheit der Stufe.

**K2 Spannungsverstärkung der Emitterschaltung.** Schritte: C_1/C_2 trennen Gleichspannungen, C_E hält den Emitter; $u_{ein}$ wird ganz
zu $u_{be}$; $i_c = g_m u_{be}$; $u_{aus} = -i_c (R_C \| r_{CE})$, Minus aus dem Spannungsabfall; $v_u = -g_m R_C = -U_{RC}/U_T$, B kommt nicht
vor. Abbildung 03-signalweg. Zahlen: −142,9 ohne r_CE, −136,2 mit, −99,3 mit 10 kΩ Last; 1 mV → 36,6 µA → 136 mV. Herleitung aus dem
Kleinsignal-Ersatzschaltbild. Beispiel: die Stufe.

**K3 Emitterwiderstand im Signalweg (Gegenkopplung).** Schritte: ohne C_E folgt der Emitter; $u_{be} = u_{ein} - i_e R_E$; fast alles fällt an
R_E ab; $v_u \approx -R_C/(R_E + r_e)$; unabhängig von B, I_C, Temperatur; linear; Preis Faktor $1 + g_m R_E = 37{,}6$. Abbildung
03-emitterwiderstand. Zahlen: −3,789 (Formel), −3,782 (numerisch), −3,80 Näherung; B 420/800: −3,786/−3,796 statt −133,8/−141,2; k2 bei 1 V
Ausgang 0,18 % statt 6,4 %; r_ein 50,8 kΩ statt 11,0 kΩ; r_CE wirkt vergrößert (2,8 MΩ). Teilüberbrückung 100 Ω: −30,6. Herleitung aus dem
Ersatzschaltbild mit R_E. Beispiel: Stufe ohne C_E. Nach dem Faktencheck: Verstärkung sinkt mit r_CE um den Faktor 36 (37,6 nur ohne r_CE); die Linearität kommt daher, dass die gekrümmte Kennlinie nur noch u_be bestimmt, ein 37,6stel der Eingangsspannung (bei gleicher Ausgangsamplitude ist u_be in beiden Stufen etwa gleich groß).

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Groß-/Kleinsignal-Schreibweise (Ruhewert + Änderung) | K | Text | Text |
| Steilheit g_m = I_C/U_T, Tangente, Kleinsignal-Kriterium | K | Formel + Herleitung + Beispiel | dito |
| Asymmetrie/Verzerrung in Zahlen | K | Text (Zahlen) | Text + Formel k2 ≈ û/(4U_T) + Beispiel |
| reale Kennlinien, G_CE ≠ 0, R_BE ≠ 0 (S. 188/189) | K | Text kurz | Text + Abbildung |
| r_BE = U_T/I_B = β/g_m, r_CE = (U_A + U_CE)/I_C, Early-Mechanismus (erinnern) | K | Formel + Herleitung | dito + Beispiel Datenblatt |
| erweitertes Ersatzschaltbild (Bild 11.21), U_0 = U_BE − U_T, B_0, Gültigkeit | K | 2 Sätze | Formel + Herleitung + Beispiel |
| Kleinsignal-Ersatzschaltbild, feste Quellen fallen weg (Überlagerung), zwei Sichten β i_b = g_m u_be | K | Text + Formel | dito |
| r_e = 1/g_m „dieselbe Barriere vom Emitter aus“ | H | – | Frage-Kasten |
| h-Parameter des Datenblatts, Zweitor | H | – | Frage-Kasten |
| Datenblattvergleich (h_fe 450/600/900, h_ie 6/8,7/15 kΩ, h_oe 60/110 µS) | H | 1 Satz | Beispiel |
| Stufe: Koppel- und Emitterkondensatoren, v_u = −g_m(R_C‖r_CE‖R_L) = −U_RC/U_T | K | Schritte + Formel + Beispiel | dito |
| Ein- und Ausgangswiderstand der Stufe | K | Text (Zahlen) | Beispiel |
| Energie aus der Versorgung | H | Frage-Kasten | Frage-Kasten |
| Größe der Kondensatoren, Grenzfrequenzen | V | – | Frage-Kasten |
| Emitterwiderstand im Signalweg, v_u ≈ −R_C/(R_E + r_e), Linearität, B-Unabhängigkeit | K | Schritte + Formel + Beispiel | dito + Variation Teilüberbrückung |
| Grundschaltungen im Kleinsignal (Tabelle), Emitterfolger als Impedanzwandler | K | Tabelle | Tabelle + Abbildung + Herleitungen + Beispiel |
| Längsregler: U_A = U_Z − U_BE, Z liefert nur Basisstrom, Glättungsfaktor ≈ 1 + R_1/r_Z | K | Schritte + Formeln + Beispiel | dito |
| Lastabhängigkeit 60 mV je Zehnfaches, r_aus 1,1 Ω, Lastkennlinie gegen Z allein | V | – | Text + Abbildung |
| kleinste Eingangsspannung 6,57 V (Skript: nur U_E > U_Z) | H | 1 Satz | Text |
| Verlustleistung des Längstransistors 149–198 mW | H | 1 Satz | Beispiel |
| Rückwirkung h_re, Bahnwiderstände, Kapazitäten, f_T | S | – | Halbsatz im Ausblick |

## 7. Abbildungsplan (Szene-IDs get1/bipolartransistoren/03-…)

| ausf. | komp. | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 03-verstaerkerstufe · schaltung-und-zeitverlauf | Stufe aus 11/02 mit C_1, C_2, C_E, Quelle 1 mV; Basis 1,602 V ± 1 mV, Kollektor 6,306 V ± 136 mV gegenphasig | kleine Basisänderung, 136-fach und umgekehrt am Kollektor |
| 2 | 2 | 03-tangente · kennlinie-tangente | I_C(U_BE) um 0,947 mA mit Tangente 36,6 mS; Sinus 1 mV und 10 mV, +3,9/−3,8 % bzw. +47/−32 % | im Kleinen gerade, im Großen verzerrt |
| 3 | 3 | 03-reale-kennlinien · kennlinie-ideal-real | (a) Eingang ideal/real, Tangente bei 4 µA (U_0 = 646,9 mV, r_BE = 6,46 kΩ); (b) Ausgang ideal/real, Geraden durch −70 V | endliche Steigungen r_BE und 1/r_CE |
| 4 | 4 | 03-ersatzschaltbilder · schaltung-zustaende | (a) erweitertes ESB bei 2 mA, (b) Kleinsignal-ESB | für Änderungen bleiben r_BE, gesteuerte Quelle, r_CE |
| 5 | 5 | 03-signalweg · schaltung-signalfluss | Kleinsignal-ESB der Stufe mit C_E, 1 mV → 36,6 µA → −136 mV | Verstärkung = Steilheit mal Kollektorwiderstand |
| 6 | 6 | 03-emitterwiderstand · kennlinie-parameter | Übertragungskennlinien mit/ohne C_E; 1 V Ausgang mit 6,4 % gegen 0,18 % | Gegenkopplung tauscht Verstärkung gegen Linearität |
| 7 | 7 | 03-grundschaltungen-kleinsignal · schaltung-zustaende | drei Kleinsignal-ESB bei 0,947 mA | gemeinsamer Anschluss bestimmt v_u, r_ein, r_aus |
| 8 | 8 | 03-stabilisierung · schaltung-und-zeitverlauf | Bild 11.28 mit Werten; U_E 11–13 V, U_A 4,870–4,910 V; Z allein 4,15–4,91 V | Ausgang folgt der Z-Spannung, Brummen 50-mal kleiner |
| 9 | – | 03-lastkennlinie · kennlinie-parameter | U_A über I_L (0,5–49 mA, log), Regler gegen Z allein (Knick 19,7 mA) | Transistor liefert den Laststrom |

Kompakt 8, ausführlich 9; Richtwert erfüllt (kompakt eine je 320 Wörter, ausführlich eine je 470 Wörter).

## 8. Zahlenwerk

`notizen/get1/zahlen_transistor.py`, Funktionen `kleinsignal`, `stufe_ap`, `stufe_mit_ce`, `stufe_ohne_ce`, `harmonische`, `stabilisierung`,
`nur_z_diode`, Bericht `bericht_verstaerker()` (Abschnitt „Thema 03“ in `zahlen_transistor.txt`). Beispieltransistor wie in 11/01 und 11/02
(I_S = 1e-14 A, B = 500 bei 5 V, U_A = 70 V); Z-Diode wie im Diodenartikel (5,6 V bei 5 mA, r_Z = 20 Ω).

## 9. Profi-Abgleich

- D. L. Lau, EE461 Lecture 7 (University of Kentucky): https://web.engr.uky.edu/~dllau/page0/ee461/lectures/Lecture07.pdf — g_m als
  Tangentensteigung I_C/V_T, A_v = −g_m R_C, Early-Linien bei −V_A, r_o = V_A/I_C (Näherung zu (U_A + U_CE)/I_C).
- Vishay BC546/547/548, Dok. 85113 Rev. 1.2: h-Parameter Gruppe C bei 5 V, 2 mA, 1 kHz: h_fe typ 600, h_ie 6/8,7/15 kΩ, h_oe typ 60, max
  110 µS, h_re 3·10⁻⁴; onsemi BC546/D: h_fe Gruppe C 450/600/900.
- Ergebnis: Physik und Formeln stimmen mit dem Plan; der Beispieltransistor hat mit 26,7 µS einen schwächeren Early-Effekt als der typische
  BC547C (60 µS); das wird im Text gesagt, das Modell bleibt (Konsistenz mit 11/01 und 11/02).

## 10. Skript-Abgleich

**Inhalte des Quellabschnitts (Vollständigkeit):**
- S. 188: Bild 11.19 ideales/reales Ausgangskennlinienfeld; „Verstärkung abhängig von U_CE“, „Ausgangswiderstand endlich“.
- S. 189: idealer Transistor ab U_CE ≥ 0,2 V ideale Stromquelle, G_CE = ∂I_C/∂U_CE = 0; real G_CE ≠ 0. Bild 11.20 ideale/reale
  Eingangskennlinie, R_BE = ∂U_BE/∂I_B = 0 ideal, real ≠ 0. Bild 11.21 „Großsignal Ersatzschaltbild“: U und R_BE in Reihe, I parallel R_CE.
- S. 190: Linearbetrieb im Bereich nahezu konstanter Steigung, möglichst großer Spannungshub (Grundschaltungen, schon in 11/02).
- S. 192/193: 11.6 Spannungsstabilisierung (Bild 11.28): R_1, Z-Diode, npn; Ripple (Bild 11.29); Bedingung U_E > U_Z; U_A = U_Z + U_BE.

**Fehler und Ungenauigkeiten des Skripts:**
1. S. 193: „U_A = U_Z + U_BE“ — Vorzeichenfehler; nach Bild 11.28 (Zählpfeil U_BE von der Basis zum Emitter, Ausgang am Emitter) gilt
   U_A = U_Z − U_BE; im Beispiel 4,890 V statt 6,363 V.
2. S. 193: „Das funktioniert nur für U_E > U_Z“ — notwendig, aber nicht hinreichend: Die Z-Diode braucht ihren Mindeststrom über R_1, also
   U_E > U_Z + R_1 (I_Z,min + I_B); im Beispiel 6,57 V für 1 mA.
3. S. 189: Bild 11.21 („Großsignal-Ersatzschaltbild“) nennt keine Werte für U und I. Mit Tangentenwerten gilt es nur nahe dem
   Arbeitspunkt (Eingang 5 mV bei halbem, 42 mV bei vierfachem Basisstrom; Ausgang exakt bei 5 V, bis 10 V auf gut 6 %); das folgt
   aus der Wahl der Tangente, nicht aus dem Bild, denn man kann die Geraden auch über einen Bereich anpassen. Die Quelle muss für
   Änderungen das β-Fache liefern (500), nicht B_0 = 467: richtige Form I_C = β I_B + (U_CE − U_CE,AP)/r_CE (Faktencheck).
4. S. 188: „In der Realität ist die Verstärkung nicht konstant, sondern abhängig von U_CE“ — gemeint ist die Stromverstärkung B (Early-Effekt);
   präzisieren.
5. S. 189: R_BE und G_CE als Großbuchstaben für differentielle Größen (Kleinschreibung r_BE, r_CE nach DIN 5483/Skript-Diodenteil); nur
   Notationshinweis, kein Fehler.

## Faktencheck (21.10.2026)

4 Fehler, 18 Ungenauigkeiten, alle nachgeprüft und eingearbeitet: erweitertes Ersatzschaltbild am Ausgang mit β statt B_0 (Tangentialebene); Linearität der Gegenkopplung richtig begründet; Ausgangsgrenze hängt von der Verstärkung ab (mit C_E bei 1 % Klirrfaktor nur 0,155 V); Praktikumsverstärker hat einen kleinen, nicht überbrückten Emitterwiderstand (Schaltbild Skript_IAS_MiNa S. 27 geprüft, keine Bauteilwerte im Artikel). Dazu: Ruhewerte statt „Großsignal = Ruhewerte“, Grenzfrequenz der Stufe 29,6 Hz mit allen drei Kondensatoren, Abweichungen −1,9/+3,9 % statt ±3 %, Faktor 36, Kollektorschaltung mit r_CE (1,88 MΩ), Basisschaltung r_aus 3,72 kΩ, Klirrfaktor gegen k_2, Z-Diode nimmt Strom auf statt ihn zu liefern, 100 Hz Brummen, Vishay 500 mW/250 K/W, Ausblick ohne Übertreibung, Early-Effekt nicht vorausgesetzt. Im Artikel 02 die Sekante 0,985 von der Tangente 0,981 getrennt.
