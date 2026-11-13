# Schleife: Lernkarten und Formelsammlung je Heft (Loop C2, seit 12.11.2026)

Auftrag des Users:
- 11.11.: Formelsammlungen für alle Artikel neu erstellen.
- 12.11. zum Lernkarten-Pilot ET1 Kap. 1: „Die Fragen sollten immer als ganzer Satz geschrieben sein, nicht einfach nur einzelne Begriffe. Sonst alles gut, kannst damit dann weitermachen.“
- Kurzfassungen entfallen (11.11. spät).

## Regeln
- **Ein Agent je Heft**, Opus, nach `notizen/karten_formeln_brief.md`. Er schreibt nur in den Heftordner (`kap<N>_formeln.tex`, `kap<N>_karten.tex`, Prüf-PDFs), nie ins Repo.
- **Zweite Spur neben der Hefte-Schleife** (`hefte_schleife.md`), wie früher die Übersetzungen: höchstens ein Agent dieser Schleife zur Zeit.
- **Einspielen mache ich selbst:** Konverter `--kap N`, dann `build_wissen.py`, nur wenn gerade kein 2b-Agent baut (sonst gleichzeitige Builds). Danach kurze Browser-Probe (`/lernen/?m=<modul>&k=N`, Formeln-Ansicht eines Artikels).
- **Muster:**
  - Lernkarten: `lernkarten_muster.md`; Fragen **immer als ganzer Fragesatz**.
  - Formelsammlung: `kurzfassung_schleife.md`, Abschnitt „Muster“, nur der Teil Formelsammlung.
  - Informatik: Befehls- und Syntaxübersicht statt Formeln.
- **Ausgelassen:**
  - HöMa3 Kap. 3 (Überarbeitung angehalten);
  - GEMB1 ab 16 (nie umwandeln);
  - Linux 8 und 9 erst, wenn sie veröffentlicht sind.
- **Nach jedem Heft:** Stand unten eintragen, dem User kurz berichten mit Commit-Hinweis.

## Warteschlange (ET1 zuerst, weil der Pilot dort steht; dann formelreiche Module, dann Informatik)
| # | Heft | braucht | Stand |
|---|---|---|---|
| 1 | ET1 Kap. 1 und 2 | Kap. 1: Formeln (+ kurze Fragen im Pilot konkreter); Kap. 2: Formeln + Karten | **fertig 12.11.** (Kap. 1: 48 Formeln, 12 Fragen konkreter; Kap. 2: 109 Karten, 40 Formeln; alle Prüfungen 0; umgewandelt, Build steht aus bis nach Linux 8 2b-2) |
| 2 | ET1 Kap. 3–11 | je Formeln + Karten | Kap. 3 **fertig 12.11.** (97 Karten, 37 Formeln; + 9 Kap.-1-Fragen konkreter); Kap. 4 **fertig 12.11.** (80 Karten, 27 Formeln); Kap. 5 **fertig 12.11.** (106 Karten, 36 Formeln); Kap. 6 **fertig 12.11.** (120 Karten, 47 Formeln); Kap. 7 **fertig 12.11.** (75 Karten, 29 Formeln); Kap. 8 **fertig 12.11.** (106 Karten, 32 Formeln); Kap. 9 **fertig 12.11.** (121 Karten, 40 Formeln); Kap. 10 **fertig 12.11.** (135 Karten, 44 Formeln); Kap. 11 **fertig 12.11.** (120 Karten, 50 Formeln). **ET1 komplett** (11 Kapitel, 1 167 Karten, 430 Formeln) |
| 3 | ET3 Kap. 1–3 | je Karten (Formeln fertig) | Kap. 1 **fertig 12.11.** (97 Karten; `karten_def.tex` angelegt); Kap. 2 **fertig 13.11.** (117 Karten); Kap. 3 **fertig 13.11.** (114 Karten, keine echten Fehler) |
| 4 | ET3 Kap. 4–8 | je Formeln + Karten | Kap. 4 **fertig 13.11.** (96 Karten, 54 Formeln); Kap. 5 **fertig 13.11.** (87 Karten, 46 Formeln); Kap. 6 **fertig 13.11.** (61 Karten, 25 Formeln); Kap. 7 **fertig 13.11.** (112 Karten, 49 Formeln; 1 echter Fehler); Kap. 8 **fertig 13.11.** (40 Karten, 19 Formeln). **ET3 komplett** (8 Kapitel: 724 Karten; Formeln Kap. 4–8 neu, 1–3 aus dem Pilot) |
| 5 | HöMa1 Kap. 1–10 | je Formeln + Karten | Kap. 1 **fertig 13.11.** (147 Karten, 75 Formeln; `karten_def`/`kurz_formeln_def` angelegt; 1 echter Fehler); Kap. 2 **fertig 13.11.** (66 Karten, 35 Formeln); Kap. 3 **fertig 13.11.** (114 Karten, 46 Formeln; 1 echter Fehler; `karten_def.tex` ohne verwaiste Überschriften); Kap. 4 **fertig 13.11.** (99 Karten, 48 Formeln; kein echter Fehler); Kap. 5 **fertig 13.11.** (107 Karten, 67 Formeln; kein echter Fehler; umgewandelt + gebaut nach Linux 11); Kap. 6 **fertig 13.11.** (77 Karten, 43 Formeln; kein echter Fehler); **Kap. 7 läuft** |
| 6 | HöMa3 Kap. 1, 2, 4–8 | je Formeln + Karten | offen |
| 7 | ML-Grundlagen 1–5 | je Formeln + Karten | offen |
| 8 | GEMB1 Kap. 1–15 | je Formeln + Karten | offen |
| 9 | Linux 1–7 (später 8, 9 …) | je Übersicht + Karten | offen |
| 10 | Python 1–3 | je Übersicht + Karten | offen |
| 11 | Cybersecurity 1 | Übersicht + Karten | offen |

## Stand
- 12.11.2026: Pilot ET1 Kap. 1 (98 Karten) vom User abgenommen. Build: Kapitel mit geschriebenen Karten zeigen keine automatischen Karten mehr; automatische Karten anderswo haben einen Fragesatz als Vorderseite („Was bedeutet „X“?“).

## Fragliche Stellen in den Heften (von den Karten-Agenten gemeldet, nicht geändert)
- ET1 Kap. 3: „Feldenergie“ und „Zeitkonstante“ nur in der Kernbox des Überblicks als Fachbegriff markiert (Website: in `12-das-wichtigste.md`); Stufe 5 benutzt „Leckstrom“ vor seiner Erklärung (Selbstentladung); Stufe 2 nennt ε_r von Keramik vor Stufe 4 (mit Verweis).
- ET1 Kap. 1–3: Heft-PDFs nennen noch die Prüfskripte („Alle Zahlen rechnet `rechnung_kap<N>.py` nach“); auf der Website filtert der Konverter das.
- ET1 Kap. 4: Fachbegriffe Innenwiderstand, Messwerk, Messbereich nur im Überblick markiert; Kernbox-Begriffe (Amperemeter, Voltmeter, strom-/spannungsrichtige Messung, Wheatstonesche Messbrücke, Abgleich) in den erklärenden Artikeln nicht markiert; Kelvin-Messung ohne Markierung; Lösung `a:k4falsch` nennt Shunt vor Stufe 2; Überblick benutzt „Bereichsendwert“ vor Stufe 1; Stufe 4 „Dieselben Werte ergibt I_q=150 µA an R_L=20 kΩ“ missverständlich (nur Spannung und Voltmeterstrom gleich).
- ET1 Kap. 5: Kernbox-Begriffe (Superposition, Leerlaufspannung, Innenwiderstand, Ersatzquelle, Kurzschluss) in den erklärenden Artikeln nicht markiert; Fachbegriff „$\pi$-Schaltung“ enthält eine Formel (besser „Pi-Schaltung“); „Zweitoren“ in Stufe 3 markiert, aber erst in Kap. 6 erklärt; Stufe 2 stützt Regel 2 auf Stufe 8 (Vorgriff).
- ET1 Kap. 6: „Tor“/„Zweitor“ nur im Überblick, Torbedingung/Zweitorparameter/Impedanz-/Admittanz-/Hybrid-/Kettenform nur in der Kernbox markiert; `kap6_stufen.tex:418` Satz zu G_3=0 ohne erkennbaren Zweck („Das“ unklar); `:434` „Dasselbe trifft die ideale stromgesteuerte Stromquelle“ unklar (Z- und Y-Form); „Kurzschlusseingangswiderstand“ in Stufe 4 unmarkiert = H_11 aus Stufe 7, Gleichheit nicht gesagt; „Elementarzweitore“ in Stufe 1 nur genannt; Bindestrich-Schreibweisen uneinheitlich.
- ET1 Kap. 7: Fachbegriffe (Innenwiderstand, Last, Leistung, Stromwärme, Leistungsanpassung, Wirkungsgrad, Spannungs-/Stromanpassung) nur im Überblick markiert; `kap7_stufen.tex:337` „mehr als ein Viertel davon erreicht keine Last“ mehrdeutig; `:124` „Hyperbel“ als Fachbegriff fraglich; `:177` „Effektivwert“ nur im Vertiefungskasten.
- ET1 Kap. 8: acht Kernbox-Begriffe (Maschenstrom, Maschenstromverfahren, Widerstandsmatrix, Bezugsknoten, Knotenpotential, Knotenpotentialverfahren, Leitwertmatrix, modifizierte Knotenanalyse) in den Artikeln nicht als Fachbegriff gesetzt; Widerstands-/Leitwertmatrix in Stufe 3/5 gar nicht genannt (nur Z, Y); `kap8_stufen.tex:223` GZS-Klammer missverständlich; doppelt benutzte Symbole (k Knotenzahl/Index, q, U_i, b/e); `:80` „Am Ende des Baums …“ unklar; Zählung realer Quellen Stufe 1 vs. 6 kann verwirren.
- ET1 Kap. 9: Symbole doppelt (T Periodendauer/Temperatur; c dreifach; n Dichte/Anzahl; U_R vs U_\mathrm R; u_D zwei Bedeutungen); `kap9_stufen.tex:381` „denselben Faktor, r/R“ ohne Bezug und Vorgriff; `:438` U_2 vor Einführung, „die Hälfte“ wovon; `:120` „springt mit ebenfalls 45 meV“ unklar.
- ET1 Kap. 10: Index E doppelt (Eingang/Emitter, Z. 484–499) und U_E/U_A statt U_ein/U_aus; Index „ein“ doppelt (U_BE,ein / U_ein); Schwellspannung uneinheitlich (U_BE vs U_BE,ein, Z. 303, 337–348); S, A, T, B doppelt belegt; „Übertragungskennlinie“ zwei Bedeutungen (Z. 191/608); „Stromverstärkung“ B vs 1+B; Z. 169 abgeholter vs zurückgeschickter Anteil vertauscht; Z. 425 „das 47-Fache“ unklar; Z. 12/579 Vorzeichen der Verstärkung fehlt (−U_RC/U_T).
- ET1 Kap. 11: „differenzieller“ (Kap. 11) vs. „differentieller“ (Kap. 9) Widerstand; `kap11_stufen.tex:459/461` NIC-Widerstand „obere“/„linke“ R; `:538` Rauschdichte in nV/√Hz ohne Erklärung der Wurzelform; `:586` (und 42, 202) OPV-Name „V“ neben Einheit V; T Temperatur/Transistor, I_E Eingangsstrom vs. Emitterstrom; `:591` SNR ohne „eff“.
- ET3 Kap. 1: „Doppelimpuls“ doppelt (`kap1_stufen.tex:295` Rechteckpaar vs. `:647` δ'); T vierfach belegt (Dehnfaktor, Periodendauer, Zeitkonstante, Zeitpunkt); g als Testfunktion `:610–614`; s_0/g_0 doppelt (`:276/295` vs. `:325`); `:645` vertauschte Rollen unklar; Lösung (f) Stufe 3 Vorgriff auf Stufe 8; `:703` Betrag eines Dirac-Impulses; `:760` fehlendes Leerzeichen; x doppelt (Stufe 2/10).

## Echte Fehler in Heften (Korrektur-Stapel, alle Sprachfassungen + PDFs + Artikel)
- HöMa1 Kap. 1 `kap1_stufen.tex:498`: „Gleichwertig zu (V) ist die Forderung, dass jede Cauchy-Folge konvergiert“ – falsch; (V) ⇔ Cauchy-vollständig **und** archimedisch (es gibt nicht-archimedische, Cauchy-vollständige angeordnete Körper).
- ET3 Kap. 7 `kap7_stufen_a.tex:142` (Stufe 4): „Enthält der Prozess keine periodischen Anteile, werden weit auseinanderliegende Werte unabhängig: φss→m_s², μss→0“ – so allgemein falsch (Gegenbeispiel aus Stufe 2, Prozess s(t)=c_k); Voraussetzung „ergodisch“ ergänzen.
- ET3 Kap. 2 `kap2_stufen.tex:513` (Kurz gesagt): „Der Realteil der Pole ist die Abklingrate“ – richtig: der *negative* Realteil (vgl. `kap2_stufen_b.tex:1122`).
- ET3 Kap. 2 `kap2_stufen_b.tex:494`: „ξ<0: Der Realteil −ξω_0 der Pole ist positiv“ gilt nur für −1<ξ<0; für ξ<−1 reelle Pole −ξω_0±ω_0√(ξ²−1).
- ET1 Kap. 10 `kap10_stufen.tex:12/579`: Verstärkung der Emitterschaltung ohne Minuszeichen (−U_RC/U_T; gemeint ist |A|).
- ET1 Kap. 10 `kap10_stufen.tex:169`: abgeholter und zurückgeschickter Anteil verwechselt.
- ET3 Kap. 2 (sonst): `kap2_stufen_b.tex:225` ε(t) bzw. „rechtsseitig“ fehlt; Symbole R, b, β, H_1/H_2, A mehrfach belegt; „Integrator“ vs. „Integrierer“; Kernbox `:1171–1172` p_r statt p_{P,r}; Stufe 5 ohne markierten Fachbegriff.
- ET3 Kap. 3: Unschärfen `kap3_stufen_b.tex:165` (Re/Im von s₊ „wieder Hilbert-Transformierte“; genau: Im = H{Re}, Re = −H{Im}); `kap3_stufen_a.tex:156` Begründung „verschiedene Frequenzen orthogonal“ passt nicht (1,5F vs F); `:62` Eigenfunktion ohne Bedingung „H(f) existiert“. **Karten-Nacharbeit:** drei Kartenteile stützen sich nur auf die (nicht mehr gezeigte) Kurzfassung: Bestimmung „idealer Tiefpass“, „Nebenzipfel“, Falle ½δ(f) beim Sprung (Karte „Fourier aus Laplace“, stufe-11) – Heft ergänzen oder Karten anpassen.
- ET3 Kap. 4: Unschärfen `kap4_stufen_a.tex:230/232` Fenster rect(Ft) schneidet nur |t|<1/(2F) aus; `:26` Überblick „Faltungsintegral über Dirac-gewichtete Abtastwerte“ vs. Herleitung über si-Reihen; Stufe 10 „Dezimation“ nie mit „Herabtasten“ verbunden, „Interpolationsfilter“ nur in Bildunterschrift (Vorschlag `\fb{Interpolationsfilter}`); `kap4_stufen_b.tex:13` „stabil, wenn“ statt „genau dann, wenn“.
- ET3 Kap. 5: Unschärfen `kap5_stufen_b.tex:17` Hüllkurve Faktor 2; `kap5_stufen_a.tex:113` f_g·t_m=konst. nur bei gleicher Form; `:193` lineare Phase nur bei positivem Faktor (Phasensprung π im Sperrbereich); `kap5_stufen_b.tex:131` Bandbedingung nur hinreichend; `kap5_stufen_a.tex:9` Kernbox „linear fallende Phase“ ohne „durch den Ursprung“.
- ET3 Kap. 6: `kap6_stufen.tex:55` Leistungssignal-Definition ohne 0<L<∞; `:97` „hier nicht gespiegelt“ nach „gespiegeltem Signal“ widersprüchlich; `:291` Abtasttheorem-Bedingung fehlt; `:302` Mindestperiode 2N−1 nicht genannt; `:299` hochgestelltes E bei periodischer Korrelation; `:293` leerer Beispieltitel; Stufe 5/6 ohne `\fb` (Wiener-Khintchine, Wiener-Lee, Parseval nicht markiert).
- ET3 Kap. 7 (Unschärfen): `kap7_stufen_b.tex:147` „gaußverteilt“ setzt gaußverteiltes Rauschen voraus; `:238` Kernbox Exponent ohne Klammer (2σ²); `kap7_stufen_a.tex:113` Multimeter AC zeigt σ nur bei True RMS; `kap7_stufen_b.tex:129` T ≥ Signaldauer setzt Beginn bei 0 voraus.
- ET3 Kap. 8: `kap8_stufen.tex:9` Kernbox Energie = Summe der Koeffizientenquadrate nur bei vollständigem System; `:79` „lang gegenüber der Wellenlänge“ zu streng; `:125` γ vor Einführung (Z. 134); `:53` Kreuzkorrelation nur für reelle Signale.
- HöMa1 Kap. 1: `\fb{Satz von Archimedes:}` mit Doppelpunkt (Z. 507); Stufe 7 nutzt 2^{n−1}≥n aus Stufe-9-Aufgabe (Vorwärtsverweis, Z. 563/726); Z. 571 „nach sechs Schritten“ = fünf Halbierungen.
- HöMa1 Kap. 2: `kap2_stufen.tex:368` konjugiertes Lösungspaar = gedämpfte Schwingung nur für p>0; `:31` Überblick „jede Zahl hat eine Wurzel“ vs. Stufe 6; `:296` „untere Dreiecksungleichung“ über allen drei Ungleichungen; `:299` Gleichheitsfall unvollständig (z=0, w=0). Karten-PDF: Abschnittsüberschrift allein am Seitenende → **behoben 13.11.** (`karten_def.tex`: `\nopagebreak` nach Überschrift und Schlüsselzeile; Kap. 1–2 neu gebaut, 0 verwaiste Überschriften; Prüfskript `scratchpad/kf_hm1_k3/verwaist.py`).
- HöMa1 Kap. 3 **echter Fehler** `kap3_stufen.tex:580`: „ganze Nullstellen nur Teiler von a₀, denn a₀ ist bis aufs Vorzeichen das Produkt der Nullstellen“ – Begründung im Reellen falsch (x³−8: a₀=−8, Produkt der reellen Nullstellen 2) und Produkt allein gibt keine Teilbarkeit; richtig: P(x₀)=0 ⇒ a₀ = −x₀(x₀^{n−1}+…+a₁).
- HöMa1 Kap. 3 (Unschärfen): `:573` „das Polynom mit nur einer Nullstelle“ (auch x(x²+1)) → „dessen einzige Nullstelle x₀ ist, n-fach“; `:255` „Summe und Produkt … etwa (h/b)(2)=−5“ ist ein Quotient; `:186–193`, `:137–142` y doppelt belegt (Element von A und Ausgang in B); `:332`, `:380` Nullfunktion hat nach `:329` keinen Grad, ist also kein Polynom; Stufe 6 ohne `\fb` (rationale Funktion), Stufe 8 „Linearfaktor“ nur `\emph`.
- HöMa1 Kap. 4 (Unschärfen): `kap4_stufen.tex:8` Überblick „Monotonie … ein Ziel“ ohne „beschränkt“ (Kernbox `:14` richtig); `:242` „heißt dann Majorante“ lässt offen, ob a_n→0 zur Definition gehört; `:327` „ab n=5 fällt die Folge unter jede Toleranz“ missverständlich; `:651` Verweis auf Stufe 3 (dort √(n+4)−√n, nicht √(n+1)−√n).
- HöMa1 Kap. 5 (Unschärfen): `kap5_stufen.tex:475–480/491` limsup/liminf ohne Fall x_n→−∞ („für jede Folge erklärt“ stimmt so nicht); `:643–648` „Sekantenverfahren (regula falsi)“ gleichgesetzt, Fall f(α)=0 fehlt; `:348` indirekter Beweis ε-δ: x_n ∈ (a,b) nicht gesichert; `:625` uneigentlicher Funktionsgrenzwert P(x)→+∞ nicht eingeführt; `:53` „streng monotone f auf 𝒲(f) bijektiv“ knapp (gemeint f: 𝒟(f)→𝒲(f)).
- HöMa1 Kap. 6 (Unschärfen): `kap6_stufen.tex:63` „In der Elektrotechnik heißt er meist log x“ fraglich (ISO 80000-2: ln; log ohne Basis oft Basis 10); `:349` Blöcke „halbieren sich“ – genau nur B_k ≤ q^k (Bildunterschrift `:351` richtig); `:375` „genau q“ → |q|; `:568` Indexversatz Cauchy-Kriterium (N₁ := N₀+1).
