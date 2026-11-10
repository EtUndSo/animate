# Durchsicht Abbildungen und Animationen: Paket gemb1_c

Hefte: content/gemb1/13 (Diffusion, Rekombination, Grundgleichungen), 14 (p-n-Übergang), 15 (MOS-Kapazität), 16 (realer MOS-Kondensator), 17 (MOSFET), 19 (Licht und Laser). Datum: 09.11.2026. Nur Plan, nichts geändert.

**Auffälligkeit zum Stand der Dateien:** Die Ordner `content/gemb1/16-…`, `17-…`, `19-…` sind im Arbeitsverzeichnis gelöscht (git status: alle Dateien „D“, auch die Sprachfassungen); ein Heft 18 gibt es nicht, obwohl `web/szenen/gemb1/k18*.json` (8 Szenen) existieren. Ich habe die deutschen Artikel von 16, 17 und 19 deshalb aus dem letzten Commit (HEAD, nur lesend) gelesen. Heft 13, 14 und 15 liegen unverändert im Arbeitsverzeichnis. Falls die Löschung gewollt ist (Hefte werden neu geordnet), gelten die Vorschläge für 16/17/19 für die Nachfolger mit gleichem Inhalt.

Zählweise: „neu“ umfasst auch Wiederverwendung vorhandener Szenen in Artikeln ohne Abbildung (dann B oder C). Das Animieren einer vorhandenen Abbildung ändert die Zahl nicht. Alle 45 vorhandenen Abbildungen dieses Pakets sind Kandidaten zum Animieren (siehe letzter Abschnitt). Vorher: 18 Artikel ohne Abbildung, 44 mit 1 bis 2, keiner mit mehr als 5. Nachher: alle 62 Artikel mit 1 oder 2 Abbildungen, kein Artikel über dem Soll.

## Kurzbilanz je Artikel

### Heft 13 Diffusion, Rekombination, Grundgleichungen
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Warum Teilchen ohne Kraft strömen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Kontinuitätsgleichung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Quellen (unendlich/endlich) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Diffusionsstrom, Einstein | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Generation und Rekombination | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Grundgleichungen | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 09 Raumladungen, Relaxation | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 10 Diffusionslänge | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 11 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

### Heft 14 Der p-n-Übergang
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Wie Ladung die Bänder verbiegt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Übergang im Gleichgewicht | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05 Zwei Näherungen für die Ladung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Feld, Potential, Weite der Zone | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Spannung anlegen | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 08 Injektion, Minoritätsträger | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Diodenkennlinie | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 10 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

### Heft 15 Die MOS-Kapazität
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 03 Drei Stoffe, eine Energieskala | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Aufteilung der Gatespannung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Abschirmung, Akkumulation | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Verarmung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Inversion | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08 Schwellspannung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Inversionsschicht als Quantentopf | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 10 Kapazität in allen Bereichen | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 11 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

### Heft 16 Der reale MOS-Kondensator
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| 03 Verschiedene Austrittsarbeiten | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Feste Ladungen im Isolator | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Reale Bilanz, verschobene Schwelle | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Interfacezustände | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07 Kennlinien niedrige/hohe Frequenz | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08 Tiefenverarmung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Messen und Auswerten | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 10 Ergänzung CCD | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

### Heft 17 Der MOSFET
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| 03 Zwei Kontakte am MOS-Kondensator | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Barriere im Kanal | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Gradual Channel Approximation | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Ausgangskennlinien | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07 Transferkennlinie, Schwellspannung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Aus-Zustand | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Vier Typen | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 10 Ergänzung Grundschaltungen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

### Heft 19 Ergänzung: Licht und Laser
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 03 Absorption und Emission | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 04 Fluoreszenz, Nanokristalle | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Spontane und stimulierte Emission | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Besetzungsumkehr | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Der Laser | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 08 Das Wichtigste | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

Summe neu: A 13, B 9, C 8 (30 Vorschläge).

## Top 3
- V8 [A] 14/04 Übergang im Gleichgewicht — Raumladungszone bildet sich als Ladungsträgerbild (Diffusion, Rekombination, Ionen bleiben, Feld stoppt) — die Kernidee des ganzen p-n-Übergangs, bisher nur als fertiges Bänderbild.
- V19 [A] 16/07 Kennlinien niedrige/hohe Frequenz — Wechselsignal läuft durch, man sieht, welche Ladung folgt und welche nicht — der meist missverstandene Punkt der C-V-Messung.
- V23 [A] 17/06 Ausgangskennlinien — Kanal schnürt sich zum Drain hin ab, Punkt wandert gleichzeitig auf der I-V-Kurve — verbindet Querschnitt und Kennlinie.

## Editor-Lücken (nur die 30 neuen Vorschläge; die Lücken der vorhandenen Szenen stehen in der Liste am Ende)
- L1 Verschwinden: 3 (V6, V8, V30)
- L2 Umformen/Morph: 1 (V23)
- L3 Parameter/Zeit animieren: 6 (V1, V19, V23, V26, V27, V29)
- L6 Teilchen: 6 (V1, V4, V8, V9, V21, V30)
- machbar ohne neue Funktion: 17

## Vorschläge

### Heft 13 Diffusion, Rekombination, Grundgleichungen

### V1 [A] Lichtblitz: Paare entstehen, laufen auseinander, verschwinden
- **Artikel:** content/gemb1/13-diffusion-rekombination-grundgleichungen/01-diffusion-rekombination-grundgleichungen.md
- **Stelle:** Worum es geht — „Trifft Licht auf einen Halbleiter, entstehen dort zusätzliche Elektronen und Löcher …“
- **Art:** neue Animation
- **Was zu sehen ist:** Halbleiterstab (x von 0 bis 100 µm), Licht als Pfeil von links. Darunter Achsen x / Überschussdichte Δp. Löcher als Punkte, Rekombination als Kreuz (Mark).
- **Ablauf:** 1. Licht trifft x=0, Paare erscheinen als Punktwolke bei x=0. 2. Punkte verteilen sich nach rechts (ungeordnet, Nettorichtung nach rechts). 3. Einzelne Punkte werden zu Kreuzen und verschwinden. 4. Das Profil Δp(x) wird als abfallende Kurve gezeichnet, die Tangente trifft die Achse bei L_diff. — Haltepunkte: Schritt 2, Schritt 4.
- **Verständnisproblem:** Die Leitfrage des Kapitels („wie weit kommen sie?“) hat noch kein Bild; Diffusion und Rekombination wirken gleichzeitig.
- **Szenenname:** gemb1/k13ueberblick
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte), L3 (Profil wächst); Notbehelf: 6 Punkte einzeln per Shift.

### V2 [A] Gradient und Divergenz an einem Dichteprofil
- **Artikel:** content/gemb1/13-diffusion-rekombination-grundgleichungen/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Schreibweise — „Der Gradient grad N = ∇N ist der Vektor der drei Ortsableitungen …“
- **Art:** neue Animation (HöMa 3 behandelt Divergenz allgemein, hier mit Teilchenströmen)
- **Was zu sehen ist:** Links ScalarField N(x,y) als Heatmap, Gradientenpfeile zum stärksten Anstieg. Rechts ein kleines Quadrat mit Pfeilen: links kurzer Pfeil hinein, rechts langer Pfeil hinaus, Beschriftung div a > 0.
- **Ablauf:** 1. Heatmap erscheint. 2. Gradientenpfeile wachsen an drei Stellen. 3. Rechts Quadrat, Zufluss, dann Abfluss, dann Beschriftung „netto heraus“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Gradient und Divergenz sind reine Schreibweise ohne Anschauung, werden aber ab Stufe 1 benutzt.
- **Szenenname:** gemb1/k13nabla
- **Editor-Lücke:** machbar

### V3 [B] Wenige fehlende Elektronen erzeugen ein merkliches Feld
- **Artikel:** content/gemb1/13-diffusion-rekombination-grundgleichungen/08-die-grundgleichungen-der-halbleiter.md
- **Stelle:** Beispiel — „Fehlen über 1 µm nur 10^12 cm^-3 Elektronen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen x (0 bis 3 µm), oben Ladungsdichte ρ als Kasten zwischen 0 und 1 µm; darunter E(x) als Rampe bis 1,5 kV/m, dann φ(x) mit 0,8 mV am Ende der Rampe.
- **Ablauf:** 1. Kasten ρ erscheint. 2. E(x) wird als Gerade gezeichnet, Marker 1,5 kV/m. 3. φ(x) als Parabel, Marker 0,8 mV. — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Die Rückkopplung Dichte → Feld (Kreis in Abb. 6) bleibt abstrakt.
- **Szenenname:** gemb1/k13poissonbsp
- **Editor-Lücke:** machbar

### V4 [B] Zickzackweg und Eindringtiefe eines Trägers
- **Artikel:** content/gemb1/13-diffusion-rekombination-grundgleichungen/10-die-diffusionslange.md
- **Stelle:** Frage — „Ist die Diffusionslänge der Weg eines einzelnen Trägers?“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Träger als Punkt, Zickzackspur, x-Achse mit Marke L_diff,p = 33 µm; Beschriftung „Weg 20 cm“ gegen „Tiefe 33 µm“.
- **Ablauf:** 1. Punkt startet bei x=0. 2. Spur wächst zickzack (Create), nach rechts nur langsam. 3. Spur endet (Kreuz), Pfeil von Start bis Ende beschriftet. 4. Zweiter, dritter Lauf überlagert, Tiefen streuen um L. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Weg und Tiefe werden verwechselt.
- **Szenenname:** gemb1/k13zickzack
- **Editor-Lücke:** braucht Editor-Funktion: L6 (Zufallsbewegung); Notbehelf: feste Polylinie per MoveAlongPath.

### V5 [C] Zusammenschau: der Kreis der Grundgleichungen
- **Artikel:** content/gemb1/13-diffusion-rekombination-grundgleichungen/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Teilchen werden gezählt …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k13kreis, animiert wie bei Artikel 08)
- **Was zu sehen ist / Ablauf:** Pfeile nacheinander: Dichten → Feld → Ströme → Dichteänderung.
- **Verständnisproblem:** alle Ergebnisse als Sonderfälle eines Kreises sehen.
- **Szenenname:** gemb1/k13kreis
- **Editor-Lücke:** machbar

### Heft 14 Der p-n-Übergang

### V6 [A] Strom nur in einer Richtung (Ladungsträgerbild)
- **Artikel:** content/gemb1/14-der-p-n-uebergang/01-der-p-n-uebergang.md
- **Stelle:** Worum es geht — „Ein Stück dotiertes Silizium ist ein Widerstand …“
- **Art:** neue Animation
- **Was zu sehen ist:** Block links p (Löcher als offene Kreise), rechts n (Elektronen als gefüllte Punkte), Grenze bei x=0, Batterie unten mit Pluspol am p- bzw. am n-Gebiet.
- **Ablauf:** 1. Block erscheint. 2. Durchlass: Träger beider Sorten laufen zur Grenze und weiter, Strompfeil dick. 3. Polung umgekehrt: Träger weichen von der Grenze, in der Mitte bleibt eine leere Schicht, Strompfeil nur dünn. — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Warum dasselbe Material in einer Richtung leitet und in der anderen nicht.
- **Szenenname:** gemb1/k14richtung
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Pfeile wieder entfernen), L6; Notbehelf: zwei Zustände nacheinander einblenden.

### V7 [A] Majorität, Minorität und Lage von E_F
- **Artikel:** content/gemb1/14-der-p-n-uebergang/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Dotierung — „In der Störstellenerschöpfung sind alle Fremdatome ionisiert …“
- **Art:** neue Animation (prüfen, ob gemb1/k11dotierung aus Heft 11 schon passt; dann Wiederverwendung)
- **Was zu sehen ist:** Bänder E_C, E_V (Lücke 1,12 eV), E_F wandert von Bandmitte zu E_C − 205 meV (n) bzw. E_V + 153 meV (p); daneben logarithmische Balken n und p: n=10^16 steigt, p=n_i²/N_D=7,9·10^3 fällt.
- **Ablauf:** 1. Eigenhalbleiter, E_F mittig, beide Balken n_i. 2. Donatoren: E_F steigt, Balken n wächst, p schrumpft, Produkt konstant (Klammer). 3. Dasselbe für p-Typ. — Haltepunkte: Schritt 2.
- **Verständnisproblem:** „Mehrheit/Minderheit“ und ihre Dichten sind nur Formel.
- **Szenenname:** gemb1/k14dichten
- **Editor-Lücke:** machbar (Shift, Scale)

### V8 [A] Die Raumladungszone bildet sich (Ladungsträgerbild)
- **Artikel:** content/gemb1/14-der-p-n-uebergang/04-der-ubergang-im-gleichgewicht.md
- **Stelle:** Die Idee — „In einem Gedankenexperiment berühren sich ein p-Stück links und ein n-Stück rechts. Vier Schritte laufen ab …“
- **Art:** neue Animation (ergänzt die Bänderabbildung k14kontakt um die Ursache)
- **Was zu sehen ist:** p links (Löcher, ortsfeste Akzeptoren als Minus), n rechts (Elektronen, Donatoren als Plus). Achse x −0,5 bis 0,5 µm.
- **Ablauf:** 1. Beide Stücke berühren sich. 2. Diffusion: Elektronen nach links, Löcher nach rechts. 3. Rekombination: Paare an der Grenze werden zu Kreuzen und verschwinden. 4. Ionen bleiben: Streifen mit Plus rechts, Minus links wird sichtbar (Zone grau). 5. Feldpfeil nach links erscheint, Drift-Pfeile gegen Diffusions-Pfeile, gleich lang. — Haltepunkte: 3, 4, 5.
- **Verständnisproblem:** Warum die Diffusion von selbst aufhört.
- **Szenenname:** gemb1/k14zonebildet
- **Editor-Lücke:** braucht Editor-Funktion: L6, L1 (Träger verschwinden); Notbehelf: MoveTo je Punkt.

### V9 [B] Diffusion über die Barriere, Drift hinab
- **Artikel:** content/gemb1/14-der-p-n-uebergang/07-spannung-anlegen.md
- **Stelle:** Die Idee — „Über die Zone laufen zwei gegenläufige Elektronenströme …“
- **Art:** neue Animation
- **Was zu sehen ist:** Leitungsbandkante mit Barriere (0,762 eV, dann 0,362 eV bei +0,4 V, 1,162 eV bei −0,4 V). Elektronen als Kugeln links, wenige weit oben; rechts unten Minoritätselektronen.
- **Ablauf:** 1. Barriere 0,762 eV: Pfeile hinauf und hinab gleich lang. 2. Barriere sinkt auf 0,362 eV: Pfeil hinauf viel dicker (5,2·10^6-fach), Pfeil hinab unverändert. 3. Sperrung 1,162 eV: Pfeil hinauf fast weg. — Haltepunkte: 2.
- **Verständnisproblem:** Warum die Diffusion exponentiell von der Höhe abhängt, die Drift kaum.
- **Szenenname:** gemb1/k14driftdiff
- **Editor-Lücke:** braucht Editor-Funktion: L6

### V10 [C] Zusammenschau: Barriere und Strom
- **Artikel:** content/gemb1/14-der-p-n-uebergang/10-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Die Dichte jeder Sorte folgt dem Boltzmann-Faktor …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k14spannung, animiert wie bei Artikel 07)
- **Verständnisproblem:** wo welches Niveau liegt.
- **Szenenname:** gemb1/k14spannung
- **Editor-Lücke:** machbar

### Heft 15 Die MOS-Kapazität

### V11 [A] Querschnitt: Gate-Spannung ordnet die Ladung im Halbleiter um
- **Artikel:** content/gemb1/15-die-mos-kapazitaet/01-die-mos-kapazitaet.md
- **Stelle:** Worum es geht — „Ein Kondensator aus zwei Metallplatten speichert Ladung …“
- **Art:** neue Animation
- **Was zu sehen ist:** Querschnitt Gate (oben), Oxid 20 nm, p-Substrat; Löcher als offene Kreise, Akzeptor-Ionen als Minus in Kästchen, Elektronen als Punkte; Spannungsachse V_G von −1 bis +3 V mit Marker.
- **Ablauf:** 1. V_G < 0: Gate negativ, Löcher sammeln sich an der Grenzfläche. 2. V_G = 0: gleichmäßig, neutral. 3. V_G klein positiv: Löcher weichen in die Tiefe, Zone mit Minus-Ionen wächst. 4. V_G groß: Zone hört auf zu wachsen, dünne Elektronenschicht an der Grenzfläche. Marker wandert mit. — Haltepunkte: 1, 3, 4.
- **Verständnisproblem:** Der Leser sieht, was „Halbleiter unter einer isolierten Platte“ bedeutet, bevor die Begriffe kommen.
- **Szenenname:** gemb1/k15ueberblick
- **Editor-Lücke:** machbar (Shift, FadeIn; Zurückkehren der Löcher bei Schritt 1 → 2 als Shift)

### V12 [B] Ladung biegt Bänder (Wiederholung) plus Plattenkondensator
- **Artikel:** content/gemb1/15-die-mos-kapazitaet/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Feld und Bänder — „Das Potential φ folgt aus der Poisson-Gleichung …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k14baender, animiert: Ladungsschicht, Feld linear, Band als Parabel)
- **Verständnisproblem:** Bandverbiegung ist der Schlüsselbegriff des ganzen Hefts; Ladung → Feld → Potential.
- **Szenenname:** gemb1/k14baender
- **Editor-Lücke:** machbar

### V13 [A] Inversion entsteht langsam: thermische Paarbildung in der Zone
- **Artikel:** content/gemb1/15-die-mos-kapazitaet/07-inversion.md
- **Stelle:** Die Idee — „Die Elektronen kommen weder aus dem Gate noch aus dem Substrat. Sie entstehen langsam durch thermische Paarbildung …“
- **Art:** neue Animation
- **Was zu sehen ist:** Bänderdiagramm bei φ_s = 0,8 V (E_C fällt zur Grenzfläche), Zone 183 nm, E_F waagerecht; Paar als Elektron/Loch-Punkte in der Zone.
- **Ablauf:** 1. Paar entsteht in der Zone (zwei Punkte erscheinen bei x=100 nm, Pfeil Wärme). 2. Feld trennt: Elektron rutscht zur Grenzfläche (E_C hinab), Loch wandert ins Substrat. 3. Elektron bleibt an der Grenzfläche, Schicht wächst (Zähler n(0) von 10^3 auf 10^16, Skala log). 4. Vergleich: mit n+-Gebiet seitlich geht es schnell (Pfeil von der Seite). — Haltepunkte: 2, 3.
- **Verständnisproblem:** Woher die Elektronen kommen und warum es dauert.
- **Szenenname:** gemb1/k15paarbildung
- **Editor-Lücke:** machbar (MoveTo/MoveAlongPath)

### V14 [B] Wechselsignal: wo sitzt die Ladungsänderung dQ
- **Artikel:** content/gemb1/15-die-mos-kapazitaet/10-die-kapazitat-in-allen-bereichen.md
- **Stelle:** Die Idee — „Ändert man V_G wenig, ändert sich die Ladung um dQ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei Querschnitte (Akkumulation, Verarmung, starke Inversion) mit Plattenabstand: Oxid d_IS, dazu in Verarmung Zone L_depl.
- **Ablauf:** 1. Akkumulation: kleines Gate-Plus-Signal, die Ladung dQ erscheint direkt an der Grenzfläche (Abstand d_IS) – Abstand-Klammer. 2. Verarmung: dQ sitzt am Zonenrand, Zonenrand verschiebt sich (Shift), Klammer d_IS + L_depl, Kapazität kleiner. 3. Inversion: wieder an der Grenzfläche. — Haltepunkte: 2.
- **Verständnisproblem:** Warum C in Verarmung kleiner ist und in Akkumulation/Inversion gleich (Frage am Artikelende).
- **Szenenname:** gemb1/k15dq
- **Editor-Lücke:** machbar

### V15 [C] Zusammenschau: die vier Bereiche
- **Artikel:** content/gemb1/15-die-mos-kapazitaet/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Das Gate verlangt eine Gegenladung …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k15bereiche, animiert wie bei Artikel 07)
- **Verständnisproblem:** Gegenladung in der jeweils billigsten Form.
- **Szenenname:** gemb1/k15bereiche
- **Editor-Lücke:** machbar

### Heft 16 Der reale MOS-Kondensator

### V16 [B] Die Kurve verschiebt sich um V_FB
- **Artikel:** content/gemb1/16-realer-mos-kondensator/01-realer-mos-kondensator.md
- **Stelle:** Worum es geht — „Teil 15 hat einen Kondensator berechnet, in dem Metall und Halbleiter dieselbe Austrittsarbeit haben …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k16schwelle: ideale Kurve grau, reale blau um V_FB = −0,96 V verschoben)
- **Ablauf:** 1. Ideale Kurve φ_s(V_G). 2. Pfeil um V_FB nach links, Kurve gleitet (Shift). 3. Punkte (Flachband, schwache und starke Inversion) wandern mit.
- **Verständnisproblem:** Die Botschaft des Kapitels: alles Reale ist eine Verschiebung.
- **Szenenname:** gemb1/k16schwelle
- **Editor-Lücke:** machbar

### V17 [C] Wiederholung: Gatespannung teilt sich auf
- **Artikel:** content/gemb1/16-realer-mos-kondensator/02-von-grund-auf-was-aus-teil-15-gebraucht-wird.md
- **Stelle:** Ideale Bilanz — „Die Gatespannung teilt sich auf: V_G = V_IS + φ_s …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k15teilung, animiert)
- **Szenenname:** gemb1/k15teilung
- **Editor-Lücke:** machbar

### V18 [A] Offene Bindungen an der Oberfläche
- **Artikel:** content/gemb1/16-realer-mos-kondensator/06-interfacezustande.md
- **Stelle:** Die Idee — „Im Kristall hat jedes Siliziumatom vier Bindungen. An einer Oberfläche fehlen die Partner …“
- **Art:** neue Animation
- **Was zu sehen ist:** Gitter aus Si-Atomen (Kreise mit je vier Strichen), unten ein Schnitt; an der Schnittfläche zwei offene Bindungen je Atom (rote Striche), später SiO2 (Sauerstoff) und Wasserstoff-Atome.
- **Ablauf:** 1. Voller Kristall, jedes Atom vier Bindungen. 2. Schnitt: Hälfte entfernt (Shift nach oben), zwei Striche je Randatom bleiben offen. 3. Oxid wächst: viele Bindungen sättigen, einzelne offen (10^11). 4. Tempern in Wasserstoff: H-Atome docken an, offene Bindungen schließen. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Was ein Interfacezustand physisch ist, bevor D_it eingeführt wird.
- **Szenenname:** gemb1/k16offenebindung
- **Editor-Lücke:** machbar

### V19 [A] Wer folgt dem Signal? Niedrige gegen hohe Frequenz
- **Artikel:** content/gemb1/16-realer-mos-kondensator/07-kennlinien-bei-niedriger-und-hoher-frequenz.md
- **Stelle:** Die Idee — „Zur Gleichspannung V_G kommt ein kleines Signal, hier 10 mV …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Querschnitte in starker Inversion (links niedrige, rechts hohe Frequenz); Sinussignal ±10 mV als Kurve über der Zeit; Elektronenschicht, Zone mit Minus-Ionen, Löcher im Substrat.
- **Ablauf:** 1. Signal schwingt. 2. Niedrige Frequenz: Elektronenschicht atmet im Takt (Ladung wechselt mit dem Signal), Kapazität C_IS. 3. Hohe Frequenz: Elektronenschicht bleibt konstant, stattdessen pendelt der Zonenrand (Löcher am Rand, Abstand L_depl,max). 4. Kurven C(V) bauen sich parallel auf, bis zum Plateau 42,6 nF/cm². — Haltepunkte: 3.
- **Verständnisproblem:** Gleichspannung langsam genug für Elektronen, das Signal nicht (Frage im Artikel).
- **Szenenname:** gemb1/k16folgen
- **Editor-Lücke:** braucht Editor-Funktion: L3 (periodisches Signal); Notbehelf: Shift hin und her.

### V20 [C] Zusammenschau: die C-V-Kurven
- **Artikel:** content/gemb1/16-realer-mos-kondensator/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Die Spannung am Gate ist eine Ladungsbilanz …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k16kennlinie, animiert wie bei Artikel 07)
- **Szenenname:** gemb1/k16kennlinie
- **Editor-Lücke:** machbar

### Heft 17 Der MOSFET

### V21 [A] Das Gate schaltet den Strom (Querschnitt)
- **Artikel:** content/gemb1/17-der-mosfet/01-der-mosfet.md
- **Stelle:** Worum es geht — „Ein MOS-Kondensator speichert nur Ladung. Er erzeugt aber an der Oberfläche des Halbleiters eine leitende Schicht …“
- **Art:** neue Animation (bewusst einfacher als der Aufbau in Artikel 03)
- **Was zu sehen ist:** Gate oben, Oxid, p-Substrat, links und rechts n+-Gebiete, Batterie zwischen den n+-Gebieten, Amperemeter-Pfeil; Spannungsachse V_GS 0 bis 3 V mit Marker.
- **Ablauf:** 1. V_GS = 0: zwischen n+ und n+ sperrt der Übergang, kein Strom. 2. V_GS steigt: Elektronenschicht entsteht unter dem Oxid (FadeIn, Grow). 3. Elektronen strömen von links nach rechts, Strompfeil wächst. 4. V_GS zurück auf 0: Kanal weg, Strom null. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Ein Gate ohne Strom steuert einen Strom.
- **Szenenname:** gemb1/k17ueberblick
- **Editor-Lücke:** braucht Editor-Funktion: L6 (strömende Elektronen), L1 (Kanal wieder verschwinden lassen); Notbehelf: zwei getrennte Zustände.

### V22 [C] Wiederholung: Inversionsladung wächst linear über V_th
- **Artikel:** content/gemb1/17-der-mosfet/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** MOS-Kondensator — „Oberhalb der Schwellspannung V_th liefert fast nur noch die Inversionsladung Q_inv ≈ −C_IS (V_G − V_th) …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k15schwelle, animiert)
- **Szenenname:** gemb1/k15schwelle
- **Editor-Lücke:** machbar

### V23 [A] Der Kanal schnürt ab, während V_DS steigt
- **Artikel:** content/gemb1/17-der-mosfet/06-ausgangskennlinien.md
- **Stelle:** Die Idee — „Mit wachsendem V_DS sinkt die Spannung zwischen Gate und Kanal am Drain-Ende. Erreicht sie V_th, verschwindet dort die Inversionsschicht …“
- **Art:** neue Animation (ergänzt die Kennlinienabbildung k17ausgang; Querschnitt und Punkt auf der Kennlinie laufen zusammen)
- **Was zu sehen ist:** Links Querschnitt (V_GS = 3 V), Kanal als Streifen unter dem Oxid, dessen Dicke zum Drain hin abnimmt. Rechts I_D(V_DS) für V_GS = 3 V (0 bis 5 V, Sättigung 3,09 mA, V_DS,sat = 2,68 V) mit Marker.
- **Ablauf:** 1. V_DS = 0: gleichmäßig dicker Kanal, Marker im Ursprung. 2. V_DS = 1 V: Kanal zum Drain dünner, Marker auf der Kurve (1,88 mA). 3. V_DS = V_DS,sat: Kanaldicke am Drain null (Punkt). 4. V_DS = 5 V: verarmte Strecke von ~320 nm am Drain, Feldpfeil mit 15 MV/m, Elektronen werden mitgerissen, Strom konstant. — Haltepunkte: 3, 4.
- **Verständnisproblem:** „Abgeschnürt, aber Strom fließt trotzdem.“
- **Szenenname:** gemb1/k17abschnuerung
- **Editor-Lücke:** braucht Editor-Funktion: L2 (Kanalform ändert sich), L3 (V_DS als Parameter); Notbehelf: vier feste Zustände mit Überblendung.

### V24 [B] Anreicherungs- und Verarmungstyp bei V_GS = 0
- **Artikel:** content/gemb1/17-der-mosfet/09-vier-typen-von-mosfets.md
- **Stelle:** Die Idee — „Zwei Entscheidungen sind unabhängig voneinander …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Querschnitte nebeneinander (n-Kanal): links ohne, rechts mit n-Schicht; Spannungsachse V_GS von −2 bis +2 V; V_th = +0,32 bzw. −1 V.
- **Ablauf:** 1. V_GS = 0: links kein Kanal, rechts Kanal vorhanden. 2. V_GS sinkt: rechts verschwindet der Kanal bei V_th = −1 V. 3. V_GS steigt: links entsteht der Kanal bei +0,32 V. — Haltepunkte: 1.
- **Verständnisproblem:** Was „Anreicherung“ und „Verarmung“ am Bauelement bedeuten.
- **Szenenname:** gemb1/k17anreichverarm
- **Editor-Lücke:** machbar

### V25 [C] Zusammenschau: Kennlinienfeld
- **Artikel:** content/gemb1/17-der-mosfet/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Das Gate legt fest, wie viele Elektronen zwischen Source und Drain sitzen …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k17ausgang, animiert wie bei Artikel 06)
- **Szenenname:** gemb1/k17ausgang
- **Editor-Lücke:** machbar

### Heft 19 Ergänzung: Licht und Laser

### V26 [A] Ein Photon wird geschluckt, später wieder abgegeben
- **Artikel:** content/gemb1/19-ergaenzung-licht-und-laser/01-ergaenzung-licht-und-laser.md
- **Stelle:** Worum es geht — „Eine Leuchtdiode gibt Licht ab, eine Solarzelle nimmt es auf …“
- **Art:** neue Animation (ohne Zahlen, die Zahlen kommen in Artikel 03)
- **Was zu sehen ist:** Zwei waagerechte Niveaus E_1 (unten) und E_2 (oben), ein Elektron als Punkt, ein Photon als Wellenzug mit Pfeil.
- **Ablauf:** 1. Photon fliegt von links ein. 2. Es verschwindet, das Elektron springt von E_1 nach E_2. 3. Pause. 4. Elektron fällt, ein Photon fliegt in zufälliger Richtung ab. — Haltepunkte: 2 und 4.
- **Verständnisproblem:** Absorption und Emission als Tausch eines ganzen Pakets zwischen Licht und Elektron.
- **Szenenname:** gemb1/k19ueberblick
- **Editor-Lücke:** braucht Editor-Funktion: L3 (laufende Welle); Notbehelf: Wellenzug als Kurve per Shift.

### V27 [B] Besetzung nach Fermi: Wiederholung für Teil 19
- **Artikel:** content/gemb1/19-ergaenzung-licht-und-laser/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Besetzung — „Im thermischen Gleichgewicht ist ein Zustand der Energie E mit der Wahrscheinlichkeit …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k10fermi aus Heft 10, animiert mit wachsender Temperatur)
- **Szenenname:** gemb1/k10fermi
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Temperatur als Parameter)

### V28 [A] Vom Niveau zum Band: Überschuss wird Wärme
- **Artikel:** content/gemb1/19-ergaenzung-licht-und-laser/03-absorption-und-emission.md
- **Stelle:** Vom Niveau zum Band — „Ein Atom hat scharfe Linien. Im Kristall findet dagegen jedes Photon mit ħω ≥ E_g …“
- **Art:** neue Animation
- **Was zu sehen ist:** Valenzband, Leitungsband, Lücke E_g; ein Photon mit ħω > E_g.
- **Ablauf:** 1. Photon trifft ein Elektron im Valenzband. 2. Elektron springt hoch ins Leitungsband, über der Kante. 3. Es rutscht in kleinen Stufen zur Kante (Wärme als kleine Wellenpfeile ans Gitter). 4. Loch sinkt analog zur Valenzbandkante. — Haltepunkte: 3.
- **Verständnisproblem:** Warum das Photon ganz geschluckt wird und der Überschuss ħω − E_g danach als Wärme abgeht.
- **Szenenname:** gemb1/k19band
- **Editor-Lücke:** machbar

### V29 [B] Besetzung gegen Pumprate (Schwelle der Umkehr)
- **Artikel:** content/gemb1/19-ergaenzung-licht-und-laser/07-der-laser.md
- **Stelle:** Beispiel — „Im Rechenmodell mit Variante 2 beginnt die Umkehr bei r_P = 1000 s^-1 …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen r_P (0 bis 5000 s^-1) gegen N_2/N (0 bis 1); Kurve; rechts Balken N_1, N_2.
- **Ablauf:** 1. Kurve wird gezeichnet, Marker läuft vom Ursprung. 2. Bei 1000 s^-1: N_2 = N_1 (Gleichstand, Schwelle). 3. Bei 3000 s^-1: N_2 = 3/4 N, N_1 = 1/4 N; α_P = −0,15 cm^-1 erscheint (Verstärkung). 4. Grenzwert N_2 → N gestrichelt. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Wie viel Pumpen für Verstärkung nötig ist.
- **Szenenname:** gemb1/k19pumprate
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Parameter-Sweep); Notbehelf: MoveAlongPath eines Markers.

### V30 [C] Zusammenschau: Licht wächst nur bei Umkehr
- **Artikel:** content/gemb1/19-ergaenzung-licht-und-laser/08-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Licht tauscht mit einem Elektron nur ganze Pakete …“
- **Art:** vorhandene Szene wiederverwenden (gemb1/k19umkehr, animiert wie bei Artikel 06)
- **Szenenname:** gemb1/k19umkehr
- **Editor-Lücke:** braucht Editor-Funktion: L1 (geschluckte Photonen verschwinden), L6

## Vorhandene Abbildungen

Alle 45 sind Kandidaten zum Animieren. Lücke gilt für die vollständige Animation.

### Heft 13
- gemb1/k13fick (03): animieren ja — Schritte: 1. Teilchen links dichter, rechts dünner. 2. Pfeile von beiden Seiten durch die rote Ebene, links mehr. 3. Netto-Pfeil und Dichte N(x) rechts. | Lücke: L6
- gemb1/k13kontinuitaet (04): animieren ja — Schritte: 1. Volumen, Zufluss links groß, Abfluss rechts klein. 2. Dichte steigt. 3. Dichtestufe ebnet sich über t0..t4 (Kurven nacheinander). | Lücke: machbar (CurveFamily)
- gemb1/k13quellen (05): animieren ja — Schritte: 1. unendliche Quelle: Oberfläche N0, Kurven für drei Eindringtiefen wachsen. 2. endliche Quelle: halbe Gauß-Kurve flacht ab, Fläche gleich. | Lücke: machbar
- gemb1/k13vorzeichen (06): animieren ja — Schritte: 1. Drift: Feld, beide Sorten in Gegenrichtung. 2. Diffusion: beide Sorten gleiche Richtung. 3. Stromrichtungen. | Lücke: machbar
- gemb1/k13rekomb (07): animieren ja — Schritte: 1. Licht an, Δp wächst mit 1−e^(−t/τ). 2. Abschalten bei 6τ, Zerfall, Tangente trifft Achse bei τ. | Lücke: machbar (Marker auf Kurve)
- gemb1/k13kreis (08): animieren ja — Schritte: Dichten → Feld → Ströme → Änderung der Dichten, dann Pfeile von außen (Ionen, G, R). | Lücke: machbar
- gemb1/k13relax (09): animieren ja — Schritte: 1. Ladungswolke, Feld. 2. Elektronen eilen voraus, Mitte positiv. 3. Gemeinsames Fortschreiten (ambipolar). | Lücke: L6
- gemb1/k13laenge (10): animieren ja — Schritte: 1. Licht, Profil e^(−x/L) zeichnet sich, Tangente. 2. Dünne Platte, sinh-Profil. 3. Lichtblitz: Paket breiter, Fläche schrumpft zu drei Zeiten. | Lücke: machbar

### Heft 14
- gemb1/k14baender (03): animieren ja — Schritte: 1. Ladungsschicht 200 nm. 2. Feld linear. 3. Bandkanten Parabel 0,31 eV. | Lücke: machbar
- gemb1/k14kontakt (04): animieren ja — Schritte: 1. getrennte Stücke. 2. Kontakt, E_F gleich. 3. p-Bänder um 0,762 eV hoch. 4. Vorzeichen der Ionen. | Lücke: machbar
- gemb1/k14schottky (05): animieren ja — Schritte: 1. Dichten fallen 13 Dekaden. 2. Raumladung. 3. Kasten darüber. | Lücke: machbar
- gemb1/k14verlauf (06): animieren ja — Schritte: Kasten → Feld (Integral) → Potential (Integral) → Bänder. | Lücke: machbar
- gemb1/k14spannung (07): animieren ja — Schritte: 1. 0 V. 2. +0,4 V: p-Seite sinkt, Barriere 0,362 eV. 3. −0,4 V: p-Seite steigt, 1,162 eV. | Lücke: machbar (Shift); stetig mit L3
- gemb1/k14injektion (08): animieren ja — Schritte: Durchlass +0,5 V: Randdichte ×2,5·10^8, Profile klingen ab; dann Sperrung −0,2 V. | Lücke: machbar
- gemb1/k14strom (09): animieren ja — Schritte: Anteile von Löchern und Elektronen am Gesamtstrom über dem Ort wandern (77/23 an der Zone). | Lücke: machbar
- gemb1/k14kennlinie (09): animieren ja — Schritte: 1. linear: scheinbar Schwelle. 2. logarithmisch: Gerade. Punkt wandert (0,433 V → 1 µA). | Lücke: machbar (MoveAlongPath)

### Heft 15
- gemb1/k15aufbau (03): animieren ja — Schritte: Metall, Isolator, Halbleiter erscheinen, E_vac, Φ, χ, flache Bänder. | Lücke: machbar
- gemb1/k15teilung (04): animieren ja — Schritte: V_G = 0,6 V, Bänder biegen, 0,31 V am Isolator, 0,29 V im Halbleiter, Ladungen +/−. | Lücke: L3 (V_G stetig); sonst Zustände
- gemb1/k15debye (05): animieren ja — Schritte: Kurve Δp(x), Tangente, L_D = 23,6 nm; rechts L_D(N). | Lücke: machbar
- gemb1/k15verarmung (06): animieren ja — Schritte: Löcher weichen, Ionen bleiben (ρ), Feld Dreieck, Potential Parabel, Zonenrand 114 nm. | Lücke: machbar
- gemb1/k15bereiche (07): animieren ja — Schritte: vier Zustände φ_s = −0,15 / 0,25 / 0,58 / 0,86 V nacheinander. | Lücke: L2 (Morph der Bandkanten); sonst Austausch
- gemb1/k15schwelle (08): animieren ja — Schritte: Punkt läuft auf φ_s(V_G) und bleibt über V_th stehen; Q_SC sättigt, Q_inv linear. | Lücke: machbar
- gemb1/k15topf (09): animieren ja — Schritte: Topf, Niveaus E_1, E_2, Treppe der Zustandsdichte, E_F steigt. | Lücke: machbar
- gemb1/k15kapazitaet (10): animieren ja — Schritte: Ersatzschaltbild, Kurve C(φ_s) zeichnet sich, Minimum 46,2 nF/cm². | Lücke: machbar

### Heft 16
- gemb1/k16austritt (03): animieren ja — Schritte: 1. vor Kontakt, E_vac gemeinsam. 2. Draht, Elektronen fließen. 3. E_F gleich, E_vac fällt 0,90 eV. | Lücke: machbar
- gemb1/k16ladung (04): animieren ja — Schritte: Zeilen a, b, c nacheinander; links V_G=0, rechts V_G=V_FB. | Lücke: machbar
- gemb1/k16schwelle (05): animieren ja — Schritte: ideale Kurve, Verschiebung um V_FB. | Lücke: machbar
- gemb1/k16zustaende (06): animieren ja — Schritte: Zustände wandern mit den Bändern, E_F kreuzt E_CNL, Besetzung wechselt. | Lücke: machbar
- gemb1/k16kennlinie (07): animieren ja — Schritte: niedrig/hoch Frequenz, dann mit D_it. | Lücke: machbar
- gemb1/k16tief (08): animieren ja — Schritte: Sprung auf 3 V, Kapazität fällt unter Plateau, Rückkehr über der Zeit. | Lücke: machbar
- gemb1/k16auswertung (09): animieren ja — Schritte: Ablesewerte nacheinander (Write), dann 1/C² mit Gerade. | Lücke: machbar
- gemb1/k16ccd (10): animieren ja — Schritte: Takt a, b, c, Ladungspaket rutscht. | Lücke: machbar (Shift)

### Heft 17
- gemb1/k17aufbau (03): animieren ja — Schritte: Substrat, Oxid, n+, Gate, Kanal, Pfeile, Schaltzeichen. | Lücke: machbar
- gemb1/k17barriere (04): animieren ja — Schritte: Barriere 0,91 eV, Gate senkt auf 0,37 eV, V_DS senkt rechte Seite. | Lücke: L2
- gemb1/k17kanal (05): animieren ja — Schritte: Kanal in Stücken, V(y) für drei V_DS, Ladung fällt. | Lücke: machbar
- gemb1/k17ausgang (06): animieren ja — Schritte: Kurven nacheinander, Grenze V_DS,sat, ohmsche Näherung. | Lücke: machbar
- gemb1/k17schwelle (07): animieren ja — Schritte: Punkt wandert über Transferkennlinie, Farbe wechselt. | Lücke: machbar
- gemb1/k17unterschwelle (08): animieren ja — Schritte: Teiler, δφ_s, Gerade 60 mV/Dekade. | Lücke: machbar
- gemb1/k17typen (09): animieren ja — Schritte: vier Typen nacheinander. | Lücke: machbar
- gemb1/k17inverter (10): animieren ja — Schritte: V_in läuft, Arbeitspunkt wandert auf der Lastgeraden. | Lücke: L3

### Heft 19
- gemb1/k19uebergaenge (03): animieren ja — Schritte: Absorption 1→2, 1→3, 1→2→3; dann Emission. | Lücke: machbar
- gemb1/k19nanokristall (04): animieren ja — Schritte: UV hebt Elektron, strahlungslos hinab, Emission; 7 nm und 4 nm; Kurve ħω(L). | Lücke: machbar
- gemb1/k19drei (05): animieren ja — Schritte: Absorption, spontane Emission (Zufallsrichtung), stimulierte (zwei Photonen). | Lücke: L3
- gemb1/k19umkehr (06): animieren ja — Schritte: Gleichgewicht, Licht schwächer; Umkehr, Licht stärker; N_2(t). | Lücke: L1, L6
- gemb1/k19laser (07): animieren ja — Schritte: Pumpen, Variante 1 und 2, Photonen laufen zwischen Spiegeln, Auskopplung. | Lücke: L1, L6

