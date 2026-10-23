# Arbeitsnotiz: Vierpole: Parameterformen und Zusammenschaltung (ST1, Netzwerkanalyse, Thema 5)

Dateien: `content/st1/02-netzwerkanalyse/05-vierpole.md` (kompakt) und `…-ausfuehrlich.md`. Frontmatter aus dem
Themenplan: title „Vierpole: Parameterformen und Zusammenschaltung“, pfad „Elektrotechnik / 3. Semester /
Schaltungstechnik 1 / Netzwerkanalyse“, order 33020500, tags „Vierpol, Admittanzform, Impedanzform, Kettenform,
Zusammenschaltung“. Quelle: PDF S. 53–65 (Abschnitt 2.6; S. 66 leer), Volltext `st1_clean.txt` Zeilen 4268–5475.

## 1. Ein-Satz-Prinzip

Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen seinen vier Torgrößen vollständig beschrieben; jede
Parameterform ordnet dieselben Gleichungen nach einem anderen Paar vorgegebener Größen, und bei einer Zusammenschaltung
nimmt man die Form, deren vorgegebene Größen allen Teilzweitoren gemeinsam sind: Dann addieren sich die Matrizen, in
der Kette multiplizieren sie sich.

## 2. Schwierigkeit und Längenspannen

**schwer**: drei Formen mit Messvorschriften und Umrechnung, Eigenschaften (reziprok, rückwirkungsfrei, aktiv), drei
Arten der Zusammenschaltung mit Gültigkeitsbedingung, Signalkette; drei Kipp-Stellen (Rückwirkung im Betrieb, Kette
statt Produkt der Übertragungen, Torbedingung). Spannen: kompakt 1800–4000, ausführlich 3500–7000 Wörter.

## 3. Vorwissen-Kette

- Zeiger (Amplitudenzeiger, Wirkleistung ½ Re{U I*}), Impedanz und Admittanz von R, L, C: ET1/Mathematische Methoden
  (zeiger-und-sinussignale), erinnern und verlinken; jωC = j1 mS bei 100 nF und 10⁴ 1/s steht in Thema 2/3.
- Überlagerungssatz linearer Netze, Ersatzquelle: ST1 Thema 2 (ersatzquellen-maschen-und-knotenanalyse), erinnern.
- Knotenleitwertmatrix, Eintragsmuster (symmetrisch für Zweipole, unsymmetrisch für gesteuerte Quellen), Inverse,
  Determinante, Cramersche Regel: ST1 Thema 3 (modifizierte-knotenanalyse), erinnern und verlinken. Im Artikel heißt die
  Knotenleitwertmatrix 𝐘_K, damit 𝐘 der Zweitormatrix vorbehalten bleibt.
- Testquellen, Eingangsadmittanz Y_ein bei offenem Ausgang, Leerlaufverstärkung A_V, Ausgangsimpedanz Z_aus,
  Ersatzzweitor aus drei Kenngrößen und seine Grenze (Rückwirkung, RC-Tiefpass −10 %): ST1 Thema 4
  (testquellen-und-transientenanalyse), erinnern und verlinken. Hier wird die Grenze aufgelöst.
- Verstärkerstufe (g_m 1 mS, g_o 25 µS, R_D 10 kΩ, R_S 1 kΩ) und ihre Variante ohne R_S mit C_gs/C_gd: Themen 2–4,
  erinnern.
- Kleinsignalmodell des Bipolartransistors (r_BE, β I_B, r_CE) und die ET1-Verstärkerstufe ohne C_E: ET1 Kap. 11
  (transistor-als-verstaerker), nur ausführlich, erinnern und verlinken.
- Zweitore im Grundstudium (Kennlinien, H-Form, Rohrkasten): ET1 Kap. 7 (zweitore), verlinken (Modul-Test: dieser
  Artikel mindestens gleich tief).
- Matrix mal Vektor, Matrixprodukt (nicht vertauschbar), Inverse einer 2×2-Matrix: im Text bei erster Nutzung an einem
  konkreten Fall zeigen (§5.10), Inverse aus Thema 3 erinnern.
- Hier aufbauen: Tor, Torbedingung, Zweitor gegen Vierpol, symmetrische Zählpfeile; vier Größen und zwei Gleichungen
  (Überlagerung), sechs Formen; Y-, Z-, A-Form mit Messvorschriften und Namen; Ersatzschaltbild der Y-Form (π plus
  gesteuerte Quelle); Umrechnungstabelle und Existenz; Eingangsadmittanz unter Last; Reziprozität (Beweis über die
  symmetrische Knotenleitwertmatrix), Rückwirkungsfreiheit, det 𝐀; aktiv/passiv über die Wirkleistung; Kette,
  Parallel-, Reihenschaltung, Torbedingung, Brune-Test; H-Form und Reihen-Parallel-Schaltung (ausführlich); Signalkette
  aus rückwirkungsfreien Stufen.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

| # | Frage (in den Worten einer Leserin) | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Das Ersatzzweitor kam mit drei Zahlen aus, warum braucht man jetzt vier?“ | Worum es geht / Vier Größen | Text | beide |
| 2 | „Ist ein Vierpol dasselbe wie ein Zweitor?“ | Tor | Text | beide |
| 3 | „Warum zählt man auch den Ausgangsstrom in das Zweitor hinein, er fließt doch heraus?“ | Zählpfeile | Frage-Kasten | beide |
| 4 | „Y₁₁ ist doch die Eingangsadmittanz des Zweitors.“ (Fehlvorstellung) | Rückwirkung im Betrieb | Fehlvorstellung | beide |
| 5 | „Dann ist Y₁₁ einfach 1/Z₁₁.“ (Fehlvorstellung) | Impedanzform | Fehlvorstellung (ausführlich), Satz mit Zahl (kompakt) | beide |
| 6 | „Darf man zum Messen einfach den Ausgang kurzschließen, ändert das nicht die Schaltung?“ | Admittanzform | Frage-Kasten | ausführlich |
| 7 | „Passive Zweitore sind immer reziprok.“ (Fehlvorstellung) | Reziprozität | Fehlvorstellung | ausführlich (kompakt: richtige Aussage im Text) |
| 8 | „Warum steht in der Kettenform −I₂?“ | Kettenform | Text | beide |
| 9 | „Die Übertragung einer Kette ist das Produkt der Einzelübertragungen.“ (Fehlvorstellung) | Kettenschaltung | Fehlvorstellung | beide |
| 10 | „Kommt es in der Kette auf die Reihenfolge an?“ | Kettenschaltung | Text, Beispiel | beide |
| 11 | „Darf man Zweitore immer parallel oder in Reihe schalten und die Matrizen addieren?“ | Reihenschaltung | Text, Schritte, Beispiel | beide |
| 12 | „Gibt es jede Form für jedes Zweitor?“ | Umrechnung | Text | beide |
| 13 | „Wozu mehrere Formen, wenn eine das Zweitor schon vollständig beschreibt?“ | Vier Größen | Text (Prinzip) | beide |
| 14 | „Wie kann die winzige Gate-Drain-Kapazität den Eingang so stark verändern?“ | Rückwirkung im Betrieb | Text, Beispiel | beide |
| 15 | „Was ist mit der Hybridform, die man vom Transistor kennt?“ | übrige Formen | Abschnitt | ausführlich (kompakt ein Satz mit Link) |
| 16 | „Wie misst man das bei hohen Frequenzen, wo es keinen guten Kurzschluss gibt?“ | Ausblick | Satz (Streuparameter) | ausführlich |

## 5. Kipp-Stellen

**K1 Rückwirkung im Betrieb.** Schritte: (1) Y₁₁ ist unter Kurzschluss am Ausgang definiert; im Betrieb liegt dort eine
Last, U₂ ist nicht null; (2) am Ausgang I₂ = −Y_L U₂, eingesetzt U₂ = −Y₂₁ U₁/(Y₂₂ + Y_L); (3) über Y₁₂ fließt am
Eingang zusätzlich Y₁₂ U₂; (4) Y_ein = Y₁₁ − Y₁₂Y₂₁/(Y₂₂ + Y_L); (5) ohne Rückwirkung (Y₁₂ = 0) gilt Y_ein = Y₁₁ für jede
Last, das Ersatzzweitor aus Thema 4 ist exakt; (6) ein kleines Y₁₂ wirkt groß, weil es mit der Verstärkung multipliziert
wird. Zahlen: Stufe ohne R_S bei ω = 10⁸ 1/s: Y = [[j12, −j2],[1000 − j2, 125 + j2]] µS; C_ein 120 fF (Kurzschluss),
208,9 fF (10 kΩ), 280,0 fF (offen); Näherung C_gs + C_gd(1 + g_m/G) mit Faktor 5,44 bzw. 9; |Y₁₂/Y₂₁| = 0,002.
RC-Kette: Y_ein 0,600 + 0,200j (Kurzschluss), 0,600 + 0,300j (1 kΩ), 0,667 + 0,333j mS (offen). Abbildung:
05-rueckwirkung-cgd. Herleitung: Eingangsadmittanz unter Last. Beispiel: Eingangskapazität der Stufe.
Fehlvorstellung: „Y₁₁ ist die Eingangsadmittanz“.

**K2 Kette: Matrizen multiplizieren, nicht Übertragungen.** Schritte: (1) Ausgangsgrößen des ersten Glieds sind die
Eingangsgrößen des zweiten, U₂ₐ = U₁ᵦ und −I₂ₐ = I₁ᵦ (deshalb −I₂); (2) Einsetzen ergibt 𝐀 = 𝐀ₐ𝐀ᵦ; (3) das zweite Glied
belastet das erste mit seiner Eingangsimpedanz (1 − j kΩ); (4) die Einzelübertragung 1/(1 + j) gilt nur offen;
(5) Kette 1/(3j), Betrag 1/3, Produkt der Einzelübertragungen 1/2 (+50 %); (6) Reihenfolge: RC 0,707∠−45°, CR 1
(offen); Stufe vor/nach RC 0,435 gegen 1,644. Abbildung: 05-rc-kette. Herleitung: Kettenregel. Beispiel: zweistufiger
RC-Tiefpass. Fehlvorstellung: Produkt der Übertragungen.

**K3 Torbedingung bei Parallel- und Reihenschaltung.** Schritte: (1) Reihenschaltung: dieselben Torströme durch beide
Teile, Spannungen addieren sich, 𝐙 = 𝐙ₐ + 𝐙ᵦ, vorausgesetzt jedes Teil hat seine Torbedingung; (2) die durchgehende
untere Leitung des ersten T-Glieds verbindet die oberen Klemmen des zweiten; (3) Strom teilt sich 0,5/0,5 mA hinein,
1 mA heraus; (4) Z = [[3,5; 2,5],[2,5; 3,5]] statt [[4; 2],[2; 4]] kΩ; (5) zweites Glied umgedreht: gemeinsame Leitungen
aufeinander, Summe stimmt; Brune-Test: 1 V zwischen den zu verbindenden Klemmen (1 mA). Parallelschaltung zweier
Zweitore mit gemeinsamer Masseleitung (Dreipole) stets zulässig: Transistorstufe ∥ Längsglied C_gd. Abbildung:
05-reihenschaltung-t. Herleitung: Summenregeln mit Annahme. Beispiel: T-Glieder.

## 6. Aussortier-Liste

| Inhalt | Kat. | Kompakt | Ausführlich |
|---|---|---|---|
| Tor, Torbedingung, Zweitor gegen Vierpol | K | Text | Text, Abb. 2 |
| symmetrische Zählpfeile, Kettenpfeil nur in der Kettenform | K | Text, Frage-Kasten | ebenso |
| linear, keine unabhängigen Quellen innen, gesteuerte mit innerer Steuergröße erlaubt | K | Satz | Text |
| vier Größen, zwei Gleichungen (Überlagerung), sechs Formen als Tabelle | K | Text, H1 | ebenso |
| Y-Form: Definition, Kurzschlussversuche, Namen | K | Formel, Abb., Beispiel | ebenso |
| Y der Verstärkerstufe = Ersatzzweitor aus Thema 4 (A_V = −Y₂₁/Y₂₂, Z_aus = 1/Y₂₂) | H | Absatz | Absatz, Beispiel |
| Ersatzschaltbild der Y-Form: π plus Quelle (Y₂₁ − Y₁₂)U₁ | H | nein (Hinweis „In der ausführlichen Fassung“) | Text, Formel, H, Abb. 4, Beispiel |
| Kurzschluss im Kleinsignal, nicht im Arbeitspunkt (Koppelkondensator) | H | Frage-Kasten | Frage-Kasten |
| Z-Form: Definition, Leerlaufversuche, Namen, Querglied | K | Formel, Text | ebenso, Beispiel |
| Y₁₁ ≠ 1/Z₁₁ (Kurzschluss- gegen Leerlaufwert) | H | Satz mit Zahl | Fehlvorstellung |
| A-Form mit −I₂, Messvorschriften, Namen, ABCD | K | Formel, Text | ebenso |
| Längs- und Querglied, RC als Produkt, Reihenfolge CR | K | Text, H, Beispiel | ebenso, Abb. 5 |
| Umrechnung Y, Z, A (Tabelle) und Existenzbedingungen | K | Formel, H | ebenso, Beispiel |
| Eingangsadmittanz unter Last, Rückwirkung (K1), Miller-Zahlen | K | Schritte, Formel, H, Abb., Beispiel | ebenso |
| Ausgangsadmittanz mit Quellenadmittanz (dual) | H | Satz mit Formel | Satz mit Formel |
| Reziprozität Y₁₂ = Y₂₁ ⇔ Z₁₂ = Z₂₁ ⇔ det 𝐀 = 1, für R, L, C, Übertrager | K | Text, H | ebenso, Beweis |
| passiv ≠ reziprok (Gyrator, Zirkulator) | H | nein (richtige Aussage im Text) | Fehlvorstellung |
| rückwirkungsfrei Y₁₂ = 0 ⇔ det 𝐀 = 0 | K | Text | ebenso |
| aktiv/passiv über ½ Re{U₁I₁* + U₂I₂*} | H | Satz | Text, Formel, Beispiel |
| Kette 𝐀 = 𝐀ₐ𝐀ᵦ (K2), Reihenfolge | K | Schritte, Formel, H, Abb., Beispiel | ebenso |
| Parallelschaltung 𝐘 = 𝐘ₐ + 𝐘ᵦ, Beispiel C_gd | K | Formel, H | ebenso, Beispiel |
| Reihenschaltung 𝐙 = 𝐙ₐ + 𝐙ᵦ, Torbedingung (K3) | K | Schritte, Formel, H, Abb., Beispiel | ebenso |
| Brune-Test, Abhilfe (umdrehen, Übertrager) | H | Schritt 5 | Text („So liest man das“) |
| Bipolarstufe mit R_E als Reihenschaltung, −3,782 und 488 kΩ | H | nein | Beispiel |
| H-Form, inverse Formen, Reihen-Parallel-Schaltung | V | Satz mit Link | Abschnitt mit Beispiel |
| Signalkette: Teiler am Eingang, −Y₂₁(R_aus ∥ R_L), Kette rückwirkungsfreier Stufen | K | Formel, H, Text | ebenso, Abb., Beispiel |
| Streuparameter bei hohen Frequenzen | V | nein | Satz im Ausblick |
| Beispielschaltungen der Vorlage (π mit Y₁…Y₃, C₁/C₂/g₁/g₂, R₁/g₁/R₂, Bild 2.47–2.49) | S | nein | nein (eigene) |
| „Maschenstromverfahren“ als einziger Weg, normierte ABCD-Matrix, Transmissionsmatrix A·B·C·D | S | nein | nein |
| Kennlinien eines Zweitors | S | nein | nein (ET1 verlinkt) |

## 7. Abbildungsplan (Szene-IDs st1/netzwerkanalyse/05-…)

| Nr. ausf. | Nr. kompakt | Szene | Vorlage | Inhalt | Kernaussage | Abschnitt |
|---|---|---|---|---|---|---|
| 1 | 1 | 05-uebersicht | blockbild | Zweitor als Kasten mit Toren und symmetrischen Zählpfeilen; darunter Kette, Parallel- und Reihenschaltung mit passender Form (𝐀 mal, 𝐘 plus, 𝐙 plus) | jede Zusammenschaltung hat ihre Form | Worum es geht |
| 2 | – | 05-tor-und-vierpol | schaltbild-vergleich | links Vierpol mit beliebig verteilten Klemmenströmen, rechts Zweitor zwischen Quelle und Last mit I₁ = I₁′, I₂ = I₂′ | Torbedingung macht aus vier Klemmen zwei Tore | Tor |
| 3 | 2 | 05-kurzschluss-leerlauf | schaltbild-messung | RC-Glied: zwei Kurzschlussversuche (Y) und zwei Leerlaufversuche (Z) mit Zahlen; Kettenparameter aus denselben Versuchen | Y im Kurzschluss, Z im Leerlauf | Admittanzform |
| 4 | – | 05-ersatzschaltbild-y | schaltbild | π aus Y_quer1, Y_längs, Y_quer2 plus Quelle (Y₂₁ − Y₁₂)U₁; RC-Glied, Stufe mit R_S, Stufe mit C_gd | die Y-Matrix ist ein π mit einer gesteuerten Quelle | Admittanzform |
| 5 | 3 | 05-rueckwirkung-cgd | schaltbild-kurve | Stufe ohne R_S mit C_gs, C_gd, g_m, G_D + g_o = 125 µS, Last; C_ein über R_L: 120…209…280 fF | Rückwirkung macht den Eingang lastabhängig | Rückwirkung im Betrieb |
| 6 | 4 | 05-rc-kette | schaltbild-kurve | zwei RC-Glieder in Kette, Belastung des ersten; |H| Kette gegen Produkt über ω (10³…10⁵) | Kette ≠ Produkt der Einzelübertragungen | Kettenschaltung |
| 7 | – | 05-laengs-quer | schaltbild-matrix | Längsglied, Querglied mit Kettenmatrizen; RC = Längs mal Quer; umgekehrte Reihenfolge | Kettenleiter = Produkt der Gliedmatrizen | Kettenschaltung |
| 8 | – | 05-parallelschaltung | schaltbild-matrix | zwei Zweitore parallel; Stufe = Transistor-Zweitor + Längsglied C_gd, Matrixsumme | ein Längsglied ist parallel geschaltet und erzeugt Rückwirkung | Parallelschaltung |
| 9 | 5 | 05-reihenschaltung-t | schaltbild-vergleich | zwei T-Glieder in Reihe, beide mit Masse unten gegen das zweite umgedreht; Ströme 0,5/0,5/1 mA; Z-Matrizen; Brune-Test 1 V | Torbedingung entscheidet, ob Z addiert werden darf | Reihenschaltung |
| 10 | – | 05-bipolar-re | schaltbild-matrix | Bipolartransistor-Zweitor (r_BE, β I₁, r_CE) in Reihe mit R_E; Last R_C; Matrizen | Gegenkopplung als Reihenschaltung | Reihenschaltung |
| 11 | 6 | 05-signalkette | blockbild-schaltbild | Quelle 10 kΩ → zwei Stufen (R_G 100 kΩ, Y₂₁, R_aus) → 10 kΩ; Teiler an jeder Schnittstelle; Pegel 1 → 0,909 → −3,67 → 8,53 mV | an jeder Schnittstelle ein Teiler | Signalverarbeitung |

Ausführlich 11 Abbildungen (Richtwert 6–12), kompakt 6 (3–6). Jede besprochene Schaltung hat ihr Schaltbild: RC-Glied
(3, 7), RC-Kette (6), Stufe mit C_gd (4, 5, 8), T-Glieder (9), Bipolarstufe (10), Signalkette mit der Verstärkerstufe (4,
11). Die kompakte Fassung zeigt das Zweitor selbst in Abbildung 1 a und die Parallelschaltung nur im Text.

## 8. Zahlenwerk

`notizen/st1/zahlen_netzwerkanalyse.py`, neue Abschnitte AH bis AP (Ausgabe `.txt`):
- AH: RC-Glied bei ω = 10⁴ 1/s: 𝐘 = [[1; −1],[−1; 1 + j]] mS (Kurzschlussversuche, 1 mA und −1 mA), 𝐙 = [[1 − j; −j],
  [−j; −j]] kΩ, 𝐀 = [[1 + j; 1 kΩ],[j1 mS; 1]] = Längs mal Quer; det 𝐘 = j mS², det 𝐙 = −j kΩ², det 𝐀 = 1; Y₁₁ = 1 mS
  gegen 1/Z₁₁ = 0,5 + 0,5j mS; Leerlauf 0,5 − 0,5j (0,707∠−45°); CR: 𝐀 = [[1; 1 kΩ],[j mS; 1 + j]], offen 1; mit 1 kΩ RC
  0,4 − 0,2j, CR 0,5; π-Ersatz 0, 1, j1 mS; (𝐘 + 𝐘ᴴ)/2 Eigenwerte 0 und 2 mS; Leistungsproben.
- AI: Kette 𝐀² = [[3j; 2 + j],[−1 + 2j; 1 + j]], H = −j/3 gegen −j/2 (+50 %); Z₁₁ = 1,2 − 0,6j kΩ (Y 0,667 + 0,333j mS),
  1/Y₂₂ = 0,333 − 0,667j kΩ (= AA); 𝐘_ges = [[0,6 + 0,2j; −0,4 + 0,2j],[−0,4 + 0,2j; 0,6 + 1,2j]] mS; mit 1 kΩ Y_ein
  0,6 + 0,3j, U₂/U₁ 0,1 − 0,2j; zweites Glied belastet das erste mit 1 − j kΩ: 0,333 − 0,333j mal 0,5 − 0,5j;
  ω = 10³/10⁴/10⁵: 0,9667/0,3333/0,0097 gegen 0,9901/0,5/0,0099.
- AJ: Stufe mit R_S: 𝐘 = [[0; 0],[0,49383; 0,11235]] mS, det 0, keine Z-Form; 𝐀 = [[−0,2275; −2,025 kΩ],[0; 0]],
  1/A₁₁ = −4,3956 = A_V, 1/Y₂₂ = 8,9011 kΩ; mit 10 kΩ −2,3256; 10 mV: 27,04 nW an der Last, 0 W am Eingang; (𝐘 + 𝐘ᵀ)/2
  Eigenwerte −0,197 und 0,309 mS; zwei Stufen 19,32 offen, 10,22 mit 10 kΩ; RC vor Stufe 1,644∠135°, Stufe vor RC
  0,435∠101,4°.
- AK: Stufe ohne R_S, ω = 10⁸ 1/s (15,9 MHz): 𝐘_T = [[j10; 0],[1000; 125]] µS, 𝐘_F = j2[[1; −1],[−1; 1]] µS, Summe =
  direkte Rechnung; C_ein 120,0/208,9/280,0 fF, U₂/U₁ −4,444 (10 kΩ), −8,00 (offen); |det 𝐀| = 0,002; π-Ersatz j10, j2,
  125 µS, Quelle 1000 µS; C_ein bei 10⁷/10⁸/10⁹: 208,89/208,88/208,04 fF.
- AL: T-Glieder (1 kΩ): 𝐙 = [[2; 1],[1; 2]] kΩ, Summe [[4; 2],[2; 4]]; falsch [[3,5; 2,5],[2,5; 3,5]], 0,5/0,5 mA
  hinein, 1 mA heraus, Potentiale 3,5/2,5/1,5/1,0 V; umgedreht = Summe; Brune 1 V bei 1 mA.
- AM: ET1-Transistor (I_C 0,9471 mA): g_m 36,636 mS, r_BE 13,713 kΩ, r_CE 79,57 kΩ, β 502,4; 𝐙_T = [[13,713; 0],
  [−39 972,6; 79,566]] kΩ, 𝐙_E = 1 kΩ·[[1; 1],[1; 1]], Summe = direkte Rechnung; mit R_C 3,9 kΩ: Eingang 487,94 kΩ,
  Verstärkung −3,7824 (= ET1 numerisch −3,7824; Näherung 517,1 kΩ und −3,789); Kollektor kurz 510,85 kΩ, offen 14,713 kΩ;
  Ausgang 2797 kΩ (ET1 2,80 MΩ); H: h₁₁ 13,713 kΩ, h₂₁ 502,4, h₂₂ 12,57 µS.
- AN: Umrechnungstabelle an einer Testmatrix bestätigt; det 𝐀 = Y₁₂/Y₂₁ = Z₁₂/Z₂₁; det 𝐙 · det 𝐘 = 1; Existenz
  Längs-/Querglied.
- AO: Teiler 400 kΩ/133,3 kΩ an 5 V: 1,25 V, R_G = 100 kΩ; Kette Quelle 10 kΩ → zwei Stufen → 10 kΩ: 8,5335; Teiler
  0,9091, Stufe 1 an 100 kΩ −4,0363 (Zwischenteiler 0,9183, −8,2 %), Stufe 2 an 10 kΩ −2,3256; ohne Teiler 10,22;
  Pegel 1 mV → 0,909 → −3,669 → 8,534 mV.

- AP: Kurzschluss über 10 µF bei 1 kHz 15,92 Ω (0,18 % von 8,90 kΩ); Gyrator g = 1 mS: Leistung je Tor ±0,25 mW bei 1 V/0,5 V, Summe 0; mit 100 nF am Ausgang Eingang induktiv, 100 mH; C_ein über R_L (0,1/1/10/100/1000 kΩ, offen): 121,98/137,78/208,88/268,11/278,69/279,95 fF; Eingangsecke an 10 kΩ: 159,2 MHz (nur C_gs), 132,6 (Kurzschluss), 76,2 (10 kΩ), 56,9 MHz (offen); Miller-Anteil 108,89 fF.

## 9. Profi-Abgleich

- [Brune test (Wikipedia)](https://en.wikipedia.org/wiki/Brune_test): Prüfung der Reihen- und Parallelschaltung
  (Eingänge zusammenschalten, Spannung zwischen den noch offenen, zu verbindenden Klemmen messen); hinreichend, nicht
  notwendig; typischer Fehler: die durchgehende untere Leitung des ersten Zweitors schließt einen Teil des zweiten kurz;
  Abhilfe durch Umdrehen eines Zweitors oder ideale Übertrager. Bestätigt K3 und das eigene T-Glied-Beispiel.
- [Gyrator (Wikipedia)](https://en.wikipedia.org/wiki/Gyrator): passives, verlustloses, nichtreziprokes Zweitor
  (Tellegen 1948); Netze aus R, L, C und idealen Übertragern sind reziprok. Bestätigt die Korrektur „passiv ⇒ reziprok“.
- [Zweitor (Wikipedia, deutsch)](https://de.wikipedia.org/wiki/Zweitor): Namen der Parameter, Umkehrbarkeit
  (Z₁₂ = Z₂₁, Y₁₂ = Y₂₁, H₁₂ = −H₂₁, det 𝐀 = 1), Rückwirkungsfreiheit (… det 𝐀 = 0), Existenz der Matrizen nur bei
  unabhängig wählbaren Größen, gemischtes Zählpfeilsystem (symmetrisch für Z, Y, H; Kettenpfeil für die Kettenform).
- ET1-Artikel zweitore (eigene Website): Tiefe für den Modul-Test (Torbedingung mit Beispiel, Y/Z/H/A, Umrechnung,
  Eigenschaften, Zusammenschaltung kurz); dieser Artikel ergänzt Rückwirkung im Betrieb, Gültigkeit der
  Zusammenschaltung mit Beispiel und Gegenbeispiel, Beweis der Reziprozität, Ersatzschaltbild als π, Signalkette.

## 10. Skript-Abgleich (PDF-Seiten; gedruckt = PDF − 8)

**Definitionen, Formeln, Aussagen (Vollständigkeit):**
- S. 53: Darstellung über Ein- und Ausgangsgrößen; Vierpol bzw. Zweitor mit vier Anschlüssen, je zwei als Klemmenpaar;
  Bild 2.42 (Tor 1: 1–1′, Tor 2: 2–2′, symmetrische Zählpfeile); innen beliebige Bauelemente, gesteuerte Quellen,
  keine starren Quellen; (2.95) I₁ = I₁′, I₂ = I₂′; lineares Zweitor; passiv/aktiv. → Abschnitt Tor (beide).
- S. 54: aktiv mit Energie aus Betriebsspannungen (Transistoren, OPV); Vorteil der Vierpoldarstellung; Gleichungen aus
  dem Netzwerk; sechs Formen, drei vorgestellt; 2.6.1 Admittanzform (2.96)–(2.98), Kurzschlussversuche, vier Namen.
  → Vier Größen, Admittanzform (beide).
- S. 55: π-Schaltung (Bild 2.43) mit Y-Matrix; Umkehrungssatz, reziprok; aktives Beispiel (Bild 2.44) mit
  Y₁₁ = jω(C₁ + C₂), Y₁₂ = −jωC₂, Y₂₁ = g₁ − jωC₂, Y₂₂ = g₂ + jωC₂; nicht reziprok; ohne C₂ rückwirkungsfrei.
  → RC-Glied als π, Stufe mit C_gs/C_gd (eigene Werte, gleiche Struktur), Reziprozität (beide).
- S. 56: 2.6.2 Impedanzform (2.99)–(2.101), Leerlaufversuche, vier Namen. → Impedanzform (beide).
- S. 57: Querwiderstand (Bild 2.45), alle Z_ij = R₁ (2.102); Z₁₂ = Z₂₁; 2.6.3 Kettenform (2.103)–(2.105); Name aus der
  Kettenschaltung. → Querglied, Kettenform (beide).
- S. 58: Messvorschriften und Namen der A_ij; Beispiel (2.106) (R₁, g₁U₁, R₂); ABCD-Matrix; drei weitere Formen (Hybrid,
  invers Hybrid, inverse Kette); 2.6.4 Äquivalenzbeziehungen; Beispiel A → Z. → Kettenform, Umrechnung, übrige Formen.
- S. 59: Tabelle 2.3 (alle Einträge nachgerechnet, richtig); (2.107), |𝐀| = 0, (2.108) Z = [[R₁; 0],[−g₁R₁R₂; R₂]];
  2.6.5 Zusammenschaltung (Parallel, Reihe, Kette). → Umrechnung (Tabelle als Formel), Stufe als eigenes Beispiel.
- S. 60: Kettenschaltung (Bild 2.47), U₁₂ = U₂₁, −I₁₂ = I₂₁, (2.109), (2.110) 𝐀_ges = 𝐀₁𝐀₂𝐀₃…; Reihenfolge, nicht
  kommutativ. → Kettenschaltung (beide).
- S. 61: (2.111)–(2.113) Beispielkette mit Querwiderstand; Parallelschaltung (Bild 2.48): gleiche Spannungen, Ströme
  addieren sich. → Parallelschaltung (beide).
- S. 62: (2.114), (2.115) 𝐘_ges = Σ𝐘; (2.116)–(2.118) Beispiel mit Längskondensator; Reihenschaltung: gleiche Ströme,
  Spannungen addieren sich. → Parallel-/Reihenschaltung (beide); Längsglied C_gd als eigenes Beispiel.
- S. 63: (2.119), (2.120) 𝐙_ges = Σ𝐙; Beispiel Z₁ aus (2.108). → Reihenschaltung (beide).
- S. 64: Z₂ (Querwiderstand), (2.121) Z_ges; 2.6.6 Kaskade (Bild 2.50: Quelle mit R_q, Vierpole, Last/A-D-Umsetzer);
  Verstärker, Filter, Leitungen; rückwirkungsfreies Zweitor mit gesteuerter Stromquelle (Bild 2.51), Teiler am Eingang,
  v_L = g_m v_ein R_aus R_L/(R_aus + R_L); Verstärkerkette auf Transistorebene (Bild 2.52); Simulation gegen
  Verständnis. → Signalverarbeitung (beide).
- S. 65: Bild 2.52 (vier Source-Stufen mit Spannungsteilern am Gate und Koppelkondensatoren). → Signalkette mit R_G.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 53: gesteuerte Quellen dürften „nur von den Spannungen und Strömen der Tore gesteuert werden“: zu eng; jede Größe
   im Inneren ist als Steuergröße zulässig (z. B. u_GS der Stufe mit R_S, keine Torgröße). Nicht zulässig sind
   Steuerung von außen und unabhängige Quellen.
2. S. 53/54: Vierpol und Zweitor als Synonyme; ein Vierpol ist erst mit erfüllter Torbedingung ein Zweitor, und die hängt
   von der Beschaltung ab (K3).
3. S. 54: „Aktive Elemente stellen stets gesteuerte Quellen dar“: Umkehrung gilt nicht (idealer Übertrager, Gyrator
   enthalten im Modell gesteuerte Quellen und sind passiv). Aktiv präzise: die insgesamt aufgenommene Wirkleistung
   ½ Re{U₁I₁* + U₂I₂*} kann negativ werden.
4. S. 55, 57: „In passiven Zweitoren gilt stets Y₁₂ = Y₂₁“ bzw. „passive Zweitore sind reziprok“: falsch; reziprok sind
   Netze aus R, L, C, gekoppelten Spulen und idealen Übertragern; passive nichtreziproke Gegenbeispiele: Gyrator,
   Zirkulator/Isolator mit vormagnetisiertem Ferrit.
5. S. 58: ABCD-Matrix sei eine Matrix mit „normalisierten“ Elementen: Sie ist die Kettenmatrix mit anderen Namen;
   normiert wird nur in speziellen HF-Darstellungen. „Transmissionsmatrix“ entfällt (Verwechslung mit der
   Streu-Transfermatrix).
6. S. 58: „Jeder Vierpol wird durch jedes der … Gleichungssysteme eindeutig beschrieben“: falsch; Querglied ohne
   Y-Form, Längsglied ohne Z-Form, idealer Übertrager ohne beide, MOS-Stufe ohne Gate-Strom ohne Z-Form, A-Form nur bei
   Y₂₁ ≠ 0.
7. S. 59: |𝐀| = 0 berechnet, aber nicht gedeutet: det 𝐀 = Y₁₂/Y₂₁ = 0 heißt rückwirkungsfrei (ergänzt).
8. S. 61 (2.113): 𝐀₂ als [[1; 0],[1/R₂₁; −1]] mit Vektor (U₂; I₂) statt (U₂; −I₂): rechnerisch gleichwertig, aber gegen
   die eigene Kettenform-Konvention; im Artikel überall mit −I₂.
9. S. 62: Bildverweis „figure:nwa-vierpol-reihenschaltung“ defekt (gemeint Bild 2.49).
10. S. 61–63: Parallel- und Reihenschaltung ohne Gültigkeitsbedingung (Torbedingung der Teilzweitore, Brune-Test);
    ergänzt mit Beispiel und Gegenbeispiel (K3).
11. S. 63: „Impendanzmatrix“, doppeltes „wurde“.
12. S. 64, Bild 2.51: Stromquelle vom oberen Ausgangsknoten nach Masse gerichtet, Formel ohne Minus; mit dieser Richtung
    gilt v_L = −g_m v_ein (R_aus ∥ R_L). Im Artikel: Y₂₁ = g_m, Quelle Y₂₁U₁ von Klemme 2 nach 2′, U₂ = −Y₂₁(R_aus ∥ R_L)U₁.
13. S. 64: abgebrochenes Wort „Leitungen“, „Kaskadierten Zweitore“, „Kette“; Quellwiderstand einmal R_q, einmal R_S (im
    Artikel R_sig, weil R_S der Source-Widerstand ist).
14. S. 54: Gleichungen „indem das Maschenstromverfahren … angewendet wird“: jedes Analyseverfahren, im Artikel
    Testquellen/Knotenanalyse.

## 11. Selbstprüfung und Faktenprüfung

**Selbstprüfung (B6, 20 Tests):**
- Neuling-Test: ergänzt „Transponierte“ (an der Diagonalen gespiegelte Matrix), Messvorschriften der Kettenform als
  eigener Herleitungsschritt, exakte Umordnung des Miller-Faktors (Y_ein = jωC_gs + jωC_gd(1 − U₂/U₁)).
- Doppelungen beseitigt: Existenz von Längs- und Querglied nur noch im Abschnitt *Umrechnung*; Querglied/Längsglied
  einmal definiert (Impedanzform), in der Kettenform nur aufgegriffen.
- Vorgriffe beseitigt: Leistungsbeispiel rechnet mit dem Ersatzschaltbild statt mit der erst später hergeleiteten
  Lastformel; Proben im Herleitungskasten K1 mit dem RC-Glied statt der RC-Kette; Abbildungsnummern aus übernommenen
  Kästen entfernt (Fassungen nummerieren verschieden).
- Formeln im Fließtext: Rechenketten im Klartext (z. B. „1 mS · 0,5 V = 0,5 mA“) in Worte gefasst; audit_inline 0.
- Handy: Formen-Tabelle auf zwei Spalten (vorher 491 px), zwei breite Formeln in aligned; 2-px-Überstand am letzten
  Teil geteilter Formelzeilen durch ein dünnes Leerzeichen am Formelende behoben (scratchpad/qquad_abstand.py).

**Faktenprüfung (Hintergrund-Agent, Bericht scratchpad/faktencheck_vierpole.md):** 3 FALSCH, 20 UNGENAU, alle
übrigen Zahlen bestätigt; alle Befunde nachgerechnet (Zahlenwerk AP, Zeilen „Faktenprüfung“) und eingearbeitet
(scratchpad/faktenfix_vp.py, 51 Ersetzungen):
- F1 „Tiefpass dämpft fast zehnmal stärker“ falsch: Faktor 0,707 gegen 0,187 (3,8-fach), Kondensator sieht 4,98 kΩ
  statt 1 kΩ, Eckfrequenz ein Fünftel; beide Fassungen.
- F2 Zirkulator ist ein Dreitor: Beispiele jetzt Richtungsleitung (passiv, verlustbehaftet, nicht reziprok) und
  Ferrit-Gyrator; Quiz angepasst.
- F3 falscher Abschnittsverweis in der kompakten Fassung.
- U1 Reziprozitätsbeweis: Y_K invertierbar als Annahme, galvanisch getrennte Tore über 1′–2′ verbinden; U19 gekoppelte
  Spulen über die inverse Induktivitätsmatrix; U17 „soweit die jeweilige Form existiert“.
- U2 „nicht zwangsläufig aktiv“; U3 Bedingung für das Produkt der Einzelübertragungen (keine Belastung: kein
  Eingangsstrom oder lastunabhängige Ausgangsspannung); U10 rückwirkungsfrei als Grenzfall nur mit Y₂₁ ≠ 0; U11
  A₂₁ ≠ 0 für die Impedanzform.
- U4 Bipolartransistor: β·I_B als Modellschreibweise, physikalisch steuert U_BE.
- U5 Frage-Kasten Torbedingung mit Anregung; U6 „1,74-Fache“ statt „fast das Doppelte“.
- U7 Ausgangsadmittanz mit Einsetzschritten und Annahme Y₁₁ + Y_sig ≠ 0; U8 Spannungsverhältnis der Bipolarstufe
  ausgerechnet; U9 Verstärkung −4,444 + 0,048j vor ihrer Verwendung berechnet, Text hinter $$ entfernt.
- U12 g_m, g_o, G_D, R_D erklärt, Quelle als g_m U₁, Tore benannt; U13 Z_T-Glied umbenannt; U14 Y_K in der kompakten
  Fassung eingeführt; U15 Summenregel statt „Impedanzmatrix beschreibt nicht“; U16 Gültigkeit für RLC-Netze bei jeder
  Amplitude; U18 Brune-Test für die Parallelschaltung in der kompakten Fassung.
- U20 Synonyme Leitwert- und Widerstandsform, Summen für mehr als zwei Teile, Namen der Kettenparameter und
  π-Schaltung in der kompakten Fassung.
- Rundung Bipolarbeispiel: Gegeben jetzt mit 13,713 kΩ, 502,38 und 79,566 kΩ, damit −39 970 kΩ aus den gezeigten
  Ziffern folgt.

**Bewusst beibehalten:** Datenblattwerte des BC547C (h_ie 8,7 kΩ, h_fe 600, h_oe 60 µS, h_re 3·10⁻⁴) wie im
ET1-Zahlenwerk; laut Prüfung plausibel, aber nicht in jedem Datenblatt als typisch angegeben.

## 12. Kennzahlen (Stand Commit)

- Ausführlich: Hauptpfad 5961 Wörter (35 min, Spanne 3500–7000), 13 Herleitungen, 12 Beispiele, 11 Abbildungen,
  5 Frage-Kästen, 4 Fehlvorstellungen, 10 Quizfragen, 13 Formel-Boxen.
- Kompakt: Hauptpfad 4174 Wörter (25 min; Spanne 1800–4000, um 4 % überschritten durch die Ergänzungen der
  Faktenprüfung, nach ERKLAER_PROMPT §3.3 Vollständigkeit vor Länge), 10 Herleitungen (identisch mit der
  ausführlichen), 4 Beispiele, 6 Abbildungen, 2 Frage-Kästen, 2 Fehlvorstellungen, 6 Quizfragen.
- Checks: KaTeX 0 Fehler, audit_inline 0, quellen_check leer, widefind/widefind_open/widefind_bsp leer, Beispielkarten
  12/12 und 4/4, splitalign „Fehler: keine“, Abbildungsliste vollständig.
