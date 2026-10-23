# Arbeitsnotiz: Aufbau und Funktionsweise des MOSFET (ST1, MOS-Feldeffekttransistoren, Thema 1)

Dateien: `content/st1/03-mos-feldeffekttransistoren/01-aufbau-und-funktionsweise.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Aufbau und Funktionsweise des MOSFET“, pfad „Elektrotechnik / 3. Semester /
Schaltungstechnik 1 / MOS-Feldeffekttransistoren“, order 33030100, tags „MOSFET, Inversion, Kanal, Schwellenspannung,
Schaltsymbol“. Quelle: PDF S. 67–73 (Kapiteleinleitung, Abschnitte 3.1–3.4; die Formeln zu 3.4 stehen auf S. 73),
Volltext `st1_clean.txt` Zeilen 5475–6199. Erstes Transistorthema: Hier wird das Beispiel-Transistorpaar des ganzen
Kapitels festgelegt (Zahlenwerk Abschnitt A).

## 1. Ein-Satz-Prinzip

Gate, Oxid und Halbleiter bilden einen Kondensator: Die Spannung zwischen Gate und Halbleiter legt fest, wie viel
Gegenladung unter dem Oxid sitzt, und oberhalb der Schwellenspannung kommt jede weitere Gegenladung als Schicht
beweglicher Elektronen hinzu, die Source und Drain als Kanal verbinden; an jeder Stelle des Kanals bestimmt die örtliche
Spannung zwischen Gate und Kanal, wie viel Ladung dort den Strom tragen kann. (Fassung nach der Faktenprüfung: Die Rümpfe
der Verarmungszone bleiben in der Inversion erhalten, bei 1 V sind 63 % der Gegenladung Rümpfe.)

## 2. Schwierigkeit und Längenspannen

**schwer**: mehrere zusammenwirkende Mechanismen (vier Zustände der MOS-Struktur, Boltzmann-Anstieg der
Elektronendichte, Kontaktspannung, Schwellenspannung als Spannungsbilanz, örtlich veränderliche Kanalladung,
Abschnürung) und zwei Kipp-Stellen. Spannen: kompakt 1800–4000, ausführlich 3500–7000 Wörter.

## 3. Vorwissen-Kette

- Dotierung, Akzeptoren als feste negative Rümpfe, Löcher als Majoritätsträger, Minoritätsträger, n·p = n_i²
  (n_i = 10¹⁰ cm⁻³): ET1 Kap. 10 „Halbleiter und das Bändermodell“, erinnern und verlinken.
- Lage des Fermi-Niveaus W_F − W_i = k_B T ln(n/n_i), Boltzmann-Verteilung (Faktor 10 je 59,5 mV), U_T = 25,85 mV,
  Diffusionsspannung U_Diff = U_T ln(N_A N_D/n_i²) mit zweitem Weg über gleiches Fermi-Niveau: dort hergeleitet,
  erinnern und verlinken (Herleitungen dürfen sich darauf stützen, §6.3).
- Raumladungszone, Rümpfe ohne Gegenpart, Verarmungsnäherung, Poisson-Gleichung: dort und im Diodenartikel
  („Die Raumladungszone unter Spannung“), erinnern; die einseitige Verarmungszone unter dem Gate wird hier hergeleitet.
- Drift, Beweglichkeit, J = σE: ET1 Kap. 10 bzw. Grundprinzipien, erinnern (für R_on).
- Plattenkondensator Q = CU, C = εA/d, Reihenschaltung von Kapazitäten: Schulphysik, hier aus dem Gaußschen Gesetz in
  einem kurzen Kasten herleiten.
- Sperrgepolter pn-Übergang zieht jeden Minoritätsträger am Rand hinüber („hinunter“): ET1-Diodenartikel, erinnern
  (Abschnürung, Bulkregel).
- Zählpfeile, Knotenpotentiale: ST1 Netzwerkanalyse; MOS-Diode mit I = k(U − U_th)², k = 1 mA/V², U_th = 0,5 V schon im
  Artikel „Arbeitspunkt und Linearisierung“ benutzt: ausführlich im Ausblick verlinken (k = K_n/2).
- Bipolartransistor und seine Sättigung: ET1 Kap. 11, verlinken (Fehlvorstellung „Sättigung“).
- Technologieknoten, Polysilizium-Gate, CMOS-Geschichte: ST1 Einführung „Von der Röhre zum integrierten Schaltkreis“,
  verlinken.
- Modul-Test: GEMB1 „Die MOS-Kapazität“ und „Der MOSFET“ (alte Artikel): dieser Artikel ist bei MOS-Zuständen,
  Inversionskriterium, Schwellenspannung, C-V-Kurve mindestens gleich tief (zusätzlich Herleitungen, Zahlen,
  Kontaktspannung, Abschnürung) und verlinkt beide.
- Hier aufbauen: Oberflächenpotential ψ_s, Fermi-Potential Φ_F, Kontaktspannung Φ_MS, Flachbandspannung, Verarmung
  unter dem Gate, Inversionskriterium 2Φ_F, Schwellenspannung, Inversionsladung, Kanalpotential U(x), örtliche
  Kanalladung, Abschnürung, Kanalwiderstand, Steilheitskoeffizient K_n.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Wie kann eine Spannung am Gate einen Strom steuern, wenn durch das Oxid gar kein Strom fließt?“ → Worum es geht
   und MOS-Kondensator, Text (K), beide.
2. „Woher kommen die Elektronen des Kanals? Das Substrat ist doch p-dotiert.“ → Inversion/Kanal, Frage-Kasten (H),
   beide (kompakt kurz: aus der Source; ausführlich mit Generation im Kondensator, 94 s).
3. „Sind Source und Drain verschiedene Anschlüsse? Was passiert, wenn ich sie vertausche?“ → Aufbau, Text (K), beide.
4. Fehlvorstellung: „Bei U_GS = 0 sind die Bänder flach, das Substrat unter dem Gate ist neutral.“ → Zustände,
   Fehlvorstellungs-Kasten, beide (Kontaktspannung −1,03 V; bei 0 V ψ_s = 0,57 V).
5. Fehlvorstellung: „Die Verarmungszone entsteht, weil Löcher und Elektronen an der Oberfläche rekombinieren.“ →
   Verarmung, Fehlvorstellungs-Kasten, ausführlich; kompakt: richtiger Mechanismus im Text.
6. „Warum liegt die Schwelle bei 2Φ_F, wenn die Oberfläche schon bei Φ_F n-leitend ist?“ → Inversion, Frage-Kasten (H),
   ausführlich.
7. „Warum wächst die Raumladungszone oberhalb der Schwelle nicht weiter?“ → Inversion, Text (K), beide.
8. „Das Gate wirkt senkrecht, die Drainspannung waagerecht. Wie kann die Drainspannung den Kanal dünner machen?“
   (sinngemäß aus den Fragen des Users zu Kap. 3) → Kanal, Text (K), beide.
9. Fehlvorstellung: „Ist der Kanal abgeschnürt, fließt kein Strom mehr.“ → Abschnürung, Fehlvorstellungs-Kasten,
   beide.
10. „Warum muss der Bulk an die negativste Spannung?“ → Aufbau/CMOS, Text (K mit Grund), beide.
11. „Darf man U_GS immer auf die Source beziehen oder nur, wenn die Source an Masse liegt?“ (Frage des Users) →
    Zählpfeile, Text (K), beide; ausführlich mit Begründung, warum die Source der natürliche Bezug ist.
12. Fehlvorstellung: „Sättigung beim MOSFET ist dasselbe wie Sättigung beim Bipolartransistor.“ → Abschnürung,
    Fehlvorstellungs-Kasten ausführlich, kompakt ein Satz.
13. „Gibt es auch MOSFETs, die ohne Gatespannung leiten?“ → Schaltzeichen (selbstleitend), Text, beide; ausführlich
    mit Grund, warum man sie kaum noch anbietet.
14. „Was heißt „32-nm-Technologie“, ist der Kanal wirklich 32 nm lang?“ → Aufbau, Frage-Kasten, ausführlich.
15. „Warum besteht das Gate aus Polysilizium und nicht aus Metall?“ → Aufbau, Frage-Kasten, ausführlich.
16. „Im Datenblatt eines Einzeltransistors steht U_GS(th) = 0,8 bis 3,0 V bei 1 mA. Ist das dieselbe Schwelle?“ →
    Schwellenspannung, Frage-Kasten, ausführlich.
17. „Warum misst man bei hoher Frequenz eine kleinere Kapazität?“ → C-V-Abschnitt, Text, ausführlich.
18. „Warum hat ein einzelner MOSFET nur drei Anschlüsse?“ → CMOS/Bulk, Frage-Kasten, ausführlich (Inversdiode).

## 5. Kipp-Stellen

**K1: Inversion und Schwellenspannung.** Wie aus einer p-Oberfläche eine Elektronenschicht wird und warum danach nur
noch sie wächst.
- Schritte: (1) Boltzmann: n_s = n_p0 exp(ψ_s/U_T), je 59,5 mV Faktor 10; (2) bei U_GB = 0 schon ψ_s = 0,57 V,
  n_s = 5,6·10¹¹ cm⁻³ (Kontaktspannung); (3) bei ψ_s = Φ_F = 0,46 V ist die Oberfläche eigenleitend (U_GB = −0,15 V);
  (4) bei ψ_s = 2Φ_F = 0,92 V ist n_s = N_A = 5,7·10¹⁷ cm⁻³: Definition der Schwelle (U_GB = 0,50 V); (5) darüber
  wächst n_s um den Faktor 10 je 60 mV, die Elektronen nehmen die zusätzliche Gateladung auf, ψ_s steigt bis 1 V
  Gatespannung nur noch um 0,105 V (4 U_T), die Verarmungszone bleibt bei rund 46 nm; (6) Q'_n ≈ −C'_ox (U − U_th).
- Akteure: ψ_s, n_s, p_s, Φ_F, N_A, Q'_dep, Q'_n.
- Abbildungen: 01-mos-zustaende, 01-oberflaechenpotential (berechnet), ausführlich zusätzlich 01-baender.
- Tragende Zahlen: 15 Zehnerpotenzen Elektronendichte zwischen Flachband und Schwelle; U_th0 = −1,027 + 0,923 + 0,604 V.
- Herleitungen: n_s (Boltzmann) mit Kriterium, x_d/Q'_dep (Poisson), Kontaktspannung, Schwellenspannung, Q'_n.
- Beispiele: Elektronendichte an der Oberfläche; Schwellenspannung (mit Variation N_A = 4·10¹⁶ → −0,025 V).
- Analogie: keine nötig (Boltzmann-Exponentialfunktion erklärt das Festhalten von ψ_s direkt).

**K2: Keilförmiger Kanal und Abschnürung.** Wie die Drainspannung über das Kanalpotential die Ladung am Drain-Ende
verringert, warum der Kanal bei U_DS = U_GS − U_th abschnürt und warum der Strom trotzdem weiterfließt.
- Schritte: (1) Kanalpotential U(x) steigt von 0 (Source) auf U_DS (Drain); (2) örtliche Gate-Kanal-Spannung
  U_GS − U(x) sinkt; (3) Ladung ∝ U_GS − U_th − U(x), Keil; (4) am Drain-Ende null bei U_GD = U_th, also
  U_DS = U_GS − U_th; (5) darüber endet der Kanal am Abschnürpunkt mit U(x_p) = U_GS − U_th, der Kanal sieht
  unverändert U_GS − U_th, Strom in erster Näherung konstant; (6) der Rest der Spannung fällt über einer kurzen
  Verarmungszone ab (bei 2 V: 1,5 V über rund 58 nm, Feld 2,6·10⁵ V/cm), die die Elektronen zum Drain zieht;
  (7) die Zone verkürzt den Kanal etwas: leichter Stromanstieg (Kanallängenmodulation).
- Abbildungen: 01-betriebsbereiche (Querschnitte und berechnete Ladungsprofile), ausführlich 01-abschnuerung.
- Tragende Zahlen: bei U_GS = 1 V Ladung am Drain-Ende 80/40/0 % bei 0,1/0,3/0,5 V; R_on 1 kΩ.
- Herleitungen: örtliche Kanalladung und Abschnürgrenze; R_on; ΔL im Beispiel (gleiche Formel wie x_d).
- Beispiele: Kanal bei U_GS = 1 V (Ladung, Grenze); abgeschnürte Zone bei 2 V.

## 6. Aussortier-Liste (K/H/V/S; Fassung → Ort)

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Aufbau NMOS: p-Substrat, n⁺-Source/Drain, Poly-Gate, Oxid wenige nm, L, W, Bulkkontakt p⁺ | K | Aufbau | Aufbau, Abb. 1 |
| Source/Drain baugleich, Benennung nach Potential; Elektronen fließen S→D, Strom D→S | K | Aufbau | Aufbau |
| Dotierung, Akzeptor, Loch (+e) kurz erinnert | K (erinnern) | Aufbau | Aufbau |
| PMOS in n-Wanne, CMOS, p⁺-Poly-Gate | K | Aufbau (Text) | eigener Abschnitt, Abb. 2 |
| Bulkregel mit Grund (Sperrpolung der Dioden) | K/H | Text | Text, Abb. 2 |
| Einzeltransistor: Bulk an Source, Inversdiode | H | – | Frage-Kasten |
| Verdrahtung Al/Cu, Poly als Leitung mit Schichtwiderstand | V | – | ein Satz im Aufbau |
| Technologieknoten (Name ≠ Gatelänge) | H | – | Frage-Kasten mit Link |
| Polysilizium statt Metall, High-k-Metallgate | V | – | Frage-Kasten |
| Layout mit Guard-Ring (W = 120 nm, L = 90 nm) | V | – | ein Satz (W, L im Layout) |
| Schaltzeichen (3 Varianten), Pfeile, Kreis, DIN-Unterbrechung | K | Abschnitt, Abb. 2 | Abschnitt, Abb. 3 |
| Zählpfeile: Spannung vom ersten zum zweiten Index, Ströme hinein | K | Text | Text |
| Nur Spannungsdifferenzen zählen, Source als Bezug | K | Text | Text mit Grund |
| selbstsperrend/selbstleitend | K | Text | Text mit Grund |
| Bulk nicht gezeichnet: NMOS an GND, PMOS an U_B | K | Text | Text |
| Kondensatorprinzip: Gateladung = Gegenladung im Halbleiter, C'_ox = ε_ox/t_ox | K | Formel, Herleitung | Formel, Herleitung, Beispiel |
| Vier Zustände mit Ladungsart | K | Abschnitt, Abb. 3 | Abschnitt, Abb. 4 |
| Kontaktspannung, Flachbandspannung ≈ −1 V (Korrektur „Flachband bei 0 V“) | K | Formel, Fehlvorstellung | Formel, Herleitung, Beispiel, Fehlvorstellung |
| Verarmung: Löcher weggedrängt (nicht Rekombination), x_d(ψ), Q'_dep | K | Formel, Herleitung | dazu Fehlvorstellung, Beispiel |
| Inversion: Boltzmann-Anstieg, Kriterium 2Φ_F, Festhalten von ψ_s, Q'_n linear | K | Kipp-Stelle | Kipp-Stelle mit Beispielen |
| Schwache Inversion (n_s > p_s schon bei U_GB = −0,15 V) | H | – | Frage-Kasten „warum 2Φ_F“ |
| Banddiagramm als zweite Sichtweise | H | ein Satz | Abbildung und Absatz |
| Schwellenspannung U_th0 = U_FB + 2Φ_F + Q'_dep/C'_ox, Einstellung über Dotierung (Implantation) | K | Formel, Herleitung, Beispiel | dazu Variationen, Abb. U_th(N_A) |
| Oxidladungen verschieben U_FB | V | – | Satz in Annahmen/So liest man das |
| U_th positiv bei NMOS, negativ bei PMOS, typisch einige 100 mV; U_BS ≠ 0 erhöht |U_th| | K | Text | Text |
| Datenblatt-Schwelle (Stromkriterium, Streuung) | H | – | Frage-Kasten (2N7000) |
| Grenzen des Ladungsmodells (ψ_s steigt noch 4 U_T, −26 %) | H | Grenzen im Kasten | Grenzen im Kasten und Beispiel |
| Kapazität: Reihenschaltung C_ox/C_dep, NF/HF, Minimum | K/H (Skript) | zwei Sätze | eigener Abschnitt, Abb., Formel, Beispiel |
| Herkunft der Kanalelektronen (Source; im Kondensator Generation, 94 s) | H | Frage-Kasten kurz | Frage-Kasten mit Zahl |
| Sperrbereich: kein Kanal, n_s 10⁶-fach kleiner bei U_GS = 0 | K | Text | Text |
| Örtliche Kanalladung Q'_n(x), Keil | K | Kipp-Stelle | Kipp-Stelle |
| Ohmscher Bereich: R_on = 1/(K_n (U_GS − U_th)), Steilheitskoeffizient K_n | K | Formel, Herleitung, Beispiel | dazu Abb. Kanalwiderstand |
| Abschnürgrenze U_DS = U_GS − U_th, U_GD = U_th | K | Kipp-Stelle | Kipp-Stelle |
| Strom fließt nach Abschnürung weiter, abgeschnürte Zone | K | Fehlvorstellung | Fehlvorstellung, Beispiel, Abb. |
| Kanallängenmodulation (Erwähnung) | H | ein Satz | ein Satz |
| Bezeichnung Sättigung MOS vs. BJT | K/H | ein Satz | Fehlvorstellung |
| Stromgleichungen in ohmschem Bereich und Sättigung, Quadratgesetz | S (Thema 2) | Ausblick | Ausblick |
| Unterschwellenstrom quantitativ, EKV | S (Thema 2) | – | – |
| Oxiddurchbruch 10 MV/cm, ESD-Schutz | V | – | Beispiel (Praxis) |
| Geschichte (Shockley, Kilby, µA709/741, 800 Mio. Transistoren) | S (Einführung) | – | – |
| Gate-Leckstrom dünner Oxide, High-k | V | – | Frage-Kasten Polysilizium |

## 7. Abbildungsplan (Szene-IDs st1/mos-feldeffekttransistoren/01-…)

| Nr. ausf. | Nr. kompakt | Szene | Vorlage | Inhalt, Kernaussage | Abschnitt |
|---|---|---|---|---|---|
| 1 | 1 | 01-querschnitt | querschnitt-layout | NMOS-Querschnitt (eingeschaltet, mit Kanal) und Draufsicht mit W, L, t_ox; Kernaussage: Das Gate liegt isoliert über dem Bereich zwischen Source und Drain und steuert ihn nur über sein Feld. | Worum es geht |
| 2 | – | 01-cmos-wanne | querschnitt | NMOS im p-Substrat, PMOS in n-Wanne, Bulk- und Wannenkontakte, pn-Dioden eingezeichnet; Bulk an GND bzw. U_B hält alle Dioden gesperrt. | NMOS und PMOS |
| 3 | 2 | 01-schaltzeichen | schaltsymbol-tabelle | 3 Varianten × NMOS/PMOS mit Zählpfeilen, dazu selbstleitend | Schaltzeichen |
| 4 | 3 | 01-mos-zustaende | querschnitt-folge | vier Zustände bei U_GB = −2 / −1,03 / 0 / +1 V mit Ladungsart, ψ_s, x_d | MOS-Kondensator |
| 5 | 4 | 01-oberflaechenpotential | gestapelte-kennlinien | ψ_s(U_GB), n_s halblog., Q'_dep und Q'_n über U_GB, exakt berechnet | Inversion |
| 6 | – | 01-baender | banddiagramm-folge | Bandverbiegung für Verarmung, Schwelle, starke Inversion | Inversion |
| 7 | 5 | 01-schwellenspannung | bilanz-und-kennlinie | Spannungsbilanz −1,03 + 0,92 + 0,60 = 0,50 V; U_th0(N_A) | Schwellenspannung |
| 8 | – | 01-cv-kurve | kennlinie | C/C'_ox über U_GB, NF und HF | Kapazität |
| 9 | 6 | 01-betriebsbereiche | querschnitt-folge + kennlinie | drei Bereiche bei U_GS = 1 V, Ladungsprofile für U_DS = 0,1/0,3/0,5 V | Kanal/Abschnürung |
| 10 | – | 01-kanalwiderstand | kennlinie | I_D(U_DS) nahe null als Geraden für U_GS = 0,75/1/1,5/2,5 V (0,5/1/2/4 mS) | Ohmscher Bereich |
| 11 | – | 01-abschnuerung | querschnitt-detail | Kanalende, Abschnürpunkt, Zone ΔL = 58 nm bei U_DS = 2 V, Potential längs des Weges | Abschnürung |

Prüfung §7.2: Einstieg 1; jeder Sach-Abschnitt mit Abbildung; Kipp-Stellen K1 (4, 5, 6) und K2 (9, 11); jede
Zusammenhangsformel mit Graph (U_th: 7, n_s/Q'_n: 5, C: 8, R_on: 10, Q'(x): 9; C'_ox und Φ_MS trivial bzw. in 7).
Kompakt 6 (Richtwert 3–6), ausführlich 11 (6–12).

## 8. Zahlenwerk

`notizen/st1/zahlen_mosfet.py` → `zahlen_mosfet.txt` (neu für das Kapitel). Konstanten aus dem ET1-Zahlenwerk
(`zahlen_halbleiter.py`): U_T = 25,852 mV, n_i = 10¹⁰ cm⁻³, ε_r = 11,7, N_L = 3,2·10¹⁹, N_V = 1,8·10¹⁹ cm⁻³.
Beispiel-Transistorpaar: t_ox = 5 nm (C'_ox = 6,906 fF/µm²); NMOS W = 10 µm, L = 1 µm, K'_n = 200 µA/V², K_n = 2 mA/V²,
U_th0 = 0,50 V, λ_n = 0,1 1/V, n⁺-Poly-Gate, Kanaldotierung N_A = 5,68·10¹⁷ cm⁻³ (so bestimmt, dass U_th0 = 0,500 V);
PMOS W = 40 µm, L = 1 µm, K'_p = 50 µA/V², K_p = 2 mA/V², U_th0,p = −0,50 V, λ_p = 0,1 1/V, p⁺-Poly-Gate,
N_D = 5,44·10¹⁷ cm⁻³. Konsistent mit der Netzwerkanalyse (k = K_n/2 = 1 mA/V², g_m = 1 mS und I_D = 0,25 mA bei
U_GS = 1 V, g_o = 25 µS).

Kernzahlen: Φ_F = 461,6 mV, 2Φ_F = 923,2 mV, Φ_MS = U_FB = −1,027 V, x_d,max = 45,8 nm, |Q'_dep| = 4,17 fC/µm²
(26 000 Ionen/µm²), |Q'_dep|/C'_ox = 0,604 V; ψ_s(U_GB = 0) = 565,5 mV (n_s = 5,6·10¹¹); n_s = n_i bei −0,15 V;
oberhalb: ψ_s(1 V) = 1028,5 mV, Q'_n exakt 2,55 statt 3,45 fC/µm² (−26 %), extrapolierte Schwelle 0,60 V;
C_min,HF = 0,247 C'_ox, NF-Minimum 0,264 C'_ox bei 0,35 V, C_FB = 0,734 C'_ox; Aufbau der Inversionsschicht ohne
Source ≈ 94 s; Q'_n(1 V) = 3,45 fC/µm² = 21 550 Elektronen/µm², 215 500 im Kanal; R_on 2000/1000/500/250/179 Ω bei
0,75/1/1,5/2,5/3,3 V; Drain-Ende 80/40/0 %; E_ox 2,0/4,9/6,5 MV/cm bei 1/2,5/3,3 V; Durchbruch ≈ 5 V.
Varianten: N_A = 4·10¹⁶ → U_th0 = −24,9 mV; Gegenprobe Lehrbuch (20 nm, 5·10¹⁶) → 0,515 V.

## 9. Profi-Abgleich

- Niknejad/Muller, EECS 105 Spring 2017, Module 3 „MOS Capacitors“ (UC Berkeley,
  https://rfic.eecs.berkeley.edu/courses/ee105/pdf/module3-1_MOSCap.pdf): n⁺-Poly-Gate auf p-Substrat,
  V_FB = −(φ_n⁺ − φ_p) = −0,95 V für 5·10¹⁶ cm⁻³, Schwelle bei n_s = N_a (φ_s = −φ_p ab Bezug W_i, also 2Φ_F über
  dem Bulk), „depletion region stops growing“, V_T = V_FB − 2φ_p + √(2qε_sN_a(−2φ_p))/C_ox = 0,52 V bei t_ox = 20 nm;
  C-V-Ersatzschaltbilder (C_ox, Reihe mit C_dep). Unser Zahlenwerk reproduziert das Beispiel mit 0,515 V.
- onsemi, Datenblatt 2N7000 (https://www.onsemi.com/download/data-sheet/pdf/2n7000-d.pdf): V_GS(th) 0,8 bis 3,0 V bei
  V_DS = V_GS, I_D = 1 mA; I_GSSF höchstens 10 nA bei 15 V (für Frage-Kasten Datenblatt-Schwelle).
- Schichtwiderstände: silizidiertes Polysilizium unter 10 Ω/□, ohne Silizid etwa 100 bis 300 Ω/□ (Patentschriften
  zur Silizidierung, Suche 23.10.2026); Aluminium ρ/d = 54 mΩ/□ bei 0,5 µm.
- Tsividis-Sichtweise (Oberflächenpotential in starker Inversion etwa 2Φ_F plus einige U_T) durch die exakte Rechnung
  bestätigt (+4,1 U_T bei 1 V, +6,3 U_T bei 2,5 V).

## 10. Skript-Abgleich (PDF-Seiten; gedruckt = PDF − 8)

**Inhalte (Vollständigkeit):**
- S. 67: Kapiteleinleitung Geschichte (S, im Einführungsartikel); Wafer, Grunddotierung p mit Bor, Dotierung
  (Definition), Akzeptor −q fest, Loch +q.
- S. 67–68: n-Wanne für PMOS, viele PMOS je Wanne, meist p-Substrat; Bild 3.2 Gitter mit Bor.
- S. 68: selbstsperrender NMOS, selbstleitende Typen heute kaum angeboten; Bild 3.3 Querschnitt und Layout (Masken);
  zwei stark n-dotierte Gebiete in schwach p-dotiertem Gebiet; Source = negativere, Drain = positivere Spannung.
- S. 69: Poly-Gate steuert Strom zwischen Source und Drain; Kanal unter dem Gate; SiO₂ wenige nm; L = Abstand
  Drain–Source, minimale L charakterisiert die Technologie („32-nm-Technologie“); W nur im Layout; Bulkkontakt p⁺ an
  GND/V_SS; nicht jeder Transistor eigener Bulkanschluss; Verdrahtung Al/Cu mehrlagig; Poly als Leitung; Name MOSFET,
  ursprünglich Al-Gate; CMOS. Bild 3.4 Layout W = 120 nm, L = 90 nm, Guard-Ring, p-Wanne, aktive Fläche = Schnitt aus
  n-aktiv und Poly.
- S. 70: Symbole (a) bipolarähnlich, (b) Digitaltechnik/Programme, (c) DIN (unterbrochene Linie = selbstsperrend,
  Pfeil = Schichtfolge np); Spannungen vom ersten zum zweiten Index, Ströme hinein positiv; Drain/Source baugleich,
  Benennung nach Potential (NMOS Drain höher, PMOS niedriger); Bulk nicht gezeichnet: PMOS an U_B, NMOS an GND.
- S. 71: MOS-Struktur als Kondensator mit spannungsabhängiger Kapazität; Anreicherung, Flachband, Verarmung (C_RLZ in
  Reihe), Inversion (Kanal, Schwellenspannung als Übergang, RLZ dehnt sich nicht weiter aus, NF C_ox, HF Reihe, weil
  Elektronen durch Generation zu langsam entstehen); Bild 3.6.
- S. 72: Sperrbereich (U_GS < U_th, selbstsperrend, Anreicherung/Flachband/Verarmung), ohmscher Bereich mit Bedingung,
  linear für kleine U_DS, keilförmiger Kanal; Sättigungs-/Abschnürbereich mit Bedingung, Elektronen über die RLZ,
  Strom begrenzt, Stromquelle; Fußnoten Sättigung MOS/BJT und Kanallängenmodulation; Bild 3.7; Definition
  Schwellenspannung (merkliche Inversionsschicht, Leitfähigkeit).
- S. 73: U_th,0 = Φ_MS + 2Φ_F + Q_dep/C_ox; Φ_F = kT/q ln(N_sub/n_i); Q_dep = √(4qε_Si|Φ_F|N_sub); Konstanten und
  Typwerte (C'_ox ≈ 7 fF/µm², N_sub ≈ 4·10¹⁶, n_i ≈ 1,4·10¹⁰); U_th,0 für U_BS = 0, Substrateffekt vergrößert |U_th|;
  Einstellung über N_sub; NMOS positiv, PMOS negativ; modern ±400 mV.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 68, Bild 3.2: „Loch: Ladung −q“; richtig +e (Text sagt +q).
2. S. 69: Poly „vergleichsweise hochohmig (R□ ≈ 20 mΩ/□)“; 20 mΩ/□ ist Metallniveau. Richtig: mit Silizid etwa
   1–10 Ω/□, ohne 100–300 Ω/□.
3. S. 69: „32-nm-Technologie = Kanallänge 32 nm“; seit den 1990er-Jahren sind die Gates kürzer als der Knotenname,
   heutige Namen zählen nur noch die Generationen weiter (65-nm-Prozess: rund 35 nm Gatelänge; Einführungsartikel).
4. S. 69: „Stromfluss vom Source zum Drain“: Elektronen fließen von Source zu Drain, der Strom von Drain zu Source.
5. S. 71, Bild 3.6 (b) und S. 72: Flachband bei U_G = 0 bzw. U_GS = 0; richtig U_FB = Φ_MS (− Q'_ox/C'_ox), beim
   n⁺-Poly-Gate etwa −1 V; bei 0 V ist die Oberfläche bereits verarmt (ψ_s = 0,57 V).
6. S. 71: im Flachband „nur C_ox wirksam“: bei 5 nm Oxid ist C_FB = 0,73 C_ox (Debye-Länge); nicht als Aussage
   übernommen (Abbildung zeigt exakte Werte).
7. S. 71: Verarmung „durch Rekombination von Löchern und Elektronen“; richtig: das Feld drängt die Löcher ins Substrat
   (Drift), zurück bleiben die Akzeptorrümpfe.
8. S. 71: Inversion „keine weiteren Löcher zur Rekombination … übrige freie Elektronen sammeln sich“; richtig:
   Boltzmann-Anstieg der Elektronendichte mit ψ_s, Elektronen aus der Source bzw. aus thermischer Generation.
9. S. 72: Abschnürung „über die Schwellenspannung hinweg (U_DS > U_th)“; richtig U_DS > U_GS − U_th.
10. S. 72: „die Feldstärke im pn-Übergang schnürt den Kanal ab“; richtig: am Drain-Ende reicht die Gate-Kanal-Spannung
    U_GD nicht mehr für Inversion; die Elektronen durchqueren die kurze Verarmungszone durch Drift.
11. S. 73: Φ_F = 0,33 V passt nicht zu N_sub = 4·10¹⁶ (0,39 V mit n_i = 10¹⁰, 0,38 V mit 1,4·10¹⁰).
12. S. 73: N_sub als „Elektronenkonzentration“; richtig Akzeptordichte (Dotierung) des Substrats.
13. S. 73: ε_Si = 11,9 als „Permittivität“; das ist die relative Permittivität (hier 11,7 wie im ET1-Zahlenwerk);
    q als „Ladung eines Elektrons“: Elementarladung (Elektron −e).
14. S. 73: Q_dep/C_ox mit C_ox: beide müssen flächenbezogen sein (Q'_dep/C'_ox).
15. S. 73: Φ_MS „abhängig vom Arbeitsbereich des Transistors“; richtig: abhängig von Gatematerial und Dotierung.
16. S. 73: Mit den eigenen Typwerten (4·10¹⁶, 7 fF/µm², n⁺-Poly) ergibt die Formel U_th,0 ≈ −0,02 V, also keinen
    selbstsperrenden Transistor; erst eine höhere Kanaldotierung (Implantation) gibt einige 100 mV.
17. S. 73: „Nullfeld-Schwellenspannung“ ist kein verbreiteter Begriff; im Artikel „Schwellenspannung ohne
    Substratvorspannung“ U_th0 (SPICE: VTO), Hinweis auf „Einsatzspannung“.
18. S. 67 (nur Notiz, Thema S): µA741 stammt von Fairchild (1968), nicht von Texas Instruments; „Walter Brittain“
    heißt Brattain; den Spitzentransistor bauten Bardeen und Brattain.

## 11. Selbstprüfung und Faktenprüfung

**Selbstprüfung (ERKLAER_PROMPT §11, beide Fassungen):** Neuling-Test fand Fermi-Niveau, Eigenleitungsniveau,
Bandkanten und Banddiagramm ohne Erinnerung im Flachband-Abschnitt (jetzt eigener Erinnerungsabsatz mit Link), den
unbenannten Begriff Massenwirkungsgesetz und „Poisson-Gleichung“ in drei Kästen (ersetzt durch „vollständige Rechnung“,
im Abschnitt MOS-Kondensator erklärt). Listen-Test: Warum-Satz zur Beweglichkeit aus der Akteure-Liste in den Fließtext.
Sprache: mehrdeutiges „weiter(e) Transistoren“ ersetzt. Handy: eine zu breite Formelzeile im Schwellen-Beispiel der
kompakten Fassung geteilt. Herleitungskästen von Abbildungsnummern befreit (Nummern zählen je Fassung). Alle übrigen
Tests ohne Befund: Umfang in der Spanne (kompakt 4016, 0,4 % über 4000 nach den Ergänzungen), keine Doppelungen,
Gerüst vollständig, Kipp-Stellen K1 (Inversion/Schwelle) und K2 (Keil/Abschnürung) je mit Schritten, Abbildung, Zahl,
Herleitung und Beispiel; Zusammenhangssätze (Kurz gesagt) geprüft: C'_ox halbe Dicke doppelte Kapazität; Kontaktspannung
als Summe der Fermi-Strecken (nur n⁺ auf p); y_d Wurzelgesetz; n_s Faktor 10 je 59,5 mV; Schwelle als Summe dreier
Spannungen; Kehrwerte in Reihe (nur ausführlich); R_on halbiert bei doppelter Übersteuerung; Abschnürung bei U_GD = U_th.

**Faktenprüfung (Agent, Bericht scratchpad/faktencheck_mos1.md):** alle Zahlen bestätigt, 2 FALSCH, 20 UNGENAU, alles
selbst nachgerechnet und eingearbeitet (108 Ersetzungen im Text, 14 in der Abbildungsliste):
- F1 Polysilizium „ähnlich gut wie ein Metall“ → leitet viel schlechter, für eine Elektrode ohne Gleichstrom genügt es.
- F2 „Kontaktspannung“ mit zwei Vorzeichen → Φ_MS heißt jetzt Austrittsarbeitsdifferenz (= U_FB = −1,027 V), die
  Kontaktspannung ist ihr Negatives (+1,027 V, Gate über Substrat); Bilanz, Abbildung und Quiz auf „Flachbandspannung“.
- U1 Prinzip „oberhalb der Schwelle besteht die Ladung aus Elektronen“ → „kommt jede weitere Gegenladung als Elektronen
  hinzu“ (Prinzip, Abbildung 4/3, Kern, Tabellen).
- U2 Verarmungstiefen einheitlich: Text/Abbildungen 35/45/48/49 nm (vollständige Rechnung), Formelwerte 36/46 nm
  ausdrücklich gekennzeichnet; C-V an der Schwelle statt „größte Tiefe“.
- U3 „ohne Näherung“ → „vollständig gerechnet (ohne Verarmungsnäherung, mit Boltzmann)“; Fermi-Dirac-Gegenrechnung im
  Zahlenwerk K: Anreicherung 58-fach statt 78-fach N_A (gut 3·10¹⁹ statt 4,4·10¹⁹), n_s(1 V) 2,85·10¹⁹ statt 3,34·10¹⁹;
  Ladungen ändern sich um 1 %.
- U4 Kurz gesagt Kontaktspannung auf n⁺-Gate/p-Substrat eingeschränkt; U5 Bereich der Verarmungsladung; U6 C-V-Minimum
  nur NF bei 0,35 V (schwache Inversion), HF sinkt bis 0,23; U7 Kanalwiderstand-Geraden nur bis 20 mV; U8 Umladezeit als
  Größenordnung (tatsächlich länger wegen Abschnürbereich: 322 ps bis zur halben Spannung gegen 173 ps RC); U9 Datenblatt-
  Schwelle je nach Transistorgröße; U10 Grund für Metallgates (Polysilizium-Verarmung, Verträglichkeit mit High-k);
  U11 „große Prozessoren“; U12 Source-Übergang „ohne Durchlassspannung“ statt „gesperrt“ (kompakt); U13 Voraussetzungen
  und Begriffe der kompakten Fassung; U14 fast das Siebzigfache; U15 Abbildung 5c nur bis 1,5 V; U16 Querverweis
  Inversdiode; U17 0,566 eV „mit n_i = 10¹⁰ gerechnet“; U18 4·10¹⁶ als Wannendotierung statt „Grunddotierung eines
  Wafers“; U19 3,3-V-Punkte gestrichen (Oxid 6,45 MV/cm), abgeschnürte Zone bei 2,5 V (68 nm); U20 Selbstjustierung mit
  kleiner seitlicher Ausdehnung.

**Hinweis für Thema 2 (Kennlinien):** Die eindimensionale Abschätzung der abgeschnürten Zone (33,7/58,4/67,5 nm bei
U_DS = 1/2/2,5 V) ergibt nur λ_eff ≈ 0,03 1/V; das Zahlenwerk setzt λ_n = 0,1 1/V (passend zu g_o = 25 µS der
Netzwerkanalyse). Im Kennlinienartikel erklären, warum die Kanallängenmodulation stärker ist (zweidimensionales Feld,
Ladungsteilung zwischen Gate und Drain) und λ als gemessener Parameter gilt. Dort auch das Quadratgesetz mit
K_n/2 = k = 1 mA/V² an die MOS-Diode der Netzwerkanalyse anbinden und die Umladezeit (322 ps) als Beispiel nutzen.

## 12. Kennzahlen (Stand Commit)

- kompakt: 4016 Wörter, 24 min; 9 Herleitungen (identisch mit der ausführlichen Fassung), 4 Beispiele, 6 Abbildungen,
  2 Frage-Kästen, 2 Fehlvorstellungen, 6 Quizfragen, 7 Kurz-gesagt-Sätze.
- ausführlich: 6601 Wörter, 39 min; 10 Herleitungen, 11 Beispiele, 11 Abbildungen, 6 Frage-Kästen, 4 Fehlvorstellungen,
  1 Vertiefung, 10 Quizfragen, 8 Kurz-gesagt-Sätze.
- Checks: Build grün, Quiz 6/10, Beispielkarten 4/4 und 11/11, KaTeX 0 Fehler, widefind/widefind_open/widefind_bsp leer,
  splitalign „Fehler: keine“, Abbildungsliste vollständig, quellen_check leer, audit_inline 0.
