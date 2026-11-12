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
| 3 | ET3 Kap. 1–3 | je Karten (Formeln fertig) | Kap. 1 **fertig 12.11.** (97 Karten; `karten_def.tex` angelegt); **Kap. 2 läuft** |
| 4 | ET3 Kap. 4–8 | je Formeln + Karten | offen |
| 5 | HöMa1 Kap. 1–10 | je Formeln + Karten | offen |
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
