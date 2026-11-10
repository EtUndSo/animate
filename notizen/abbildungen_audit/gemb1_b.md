# Durchsicht Abbildungen und Animationen: Paket gemb1_b

Hefte: content/gemb1/07 bis 12 (Kristallwachstum und reziprokes Gitter, vom Atom zum Band, Bandstrukturen lesen, Zustandsdichte und Fermi-Verteilung, Eigenhalbleiter und Dotierung, Strom im Halbleiter). Datum: 09.11.2026. Nur Plan, nichts geändert.

Aufbau: Die Kurzbilanz-Tabellen stehen je Heft in dessen Abschnitt; Top 3 und Editor-Lücken stehen ganz oben (am Ende gefüllt).

## Gesamtbilanz Paket gemb1_b (66 deutsche Artikel)

Vorher: 18 Artikel ohne Abbildung, 48 mit genau 1. Nachher: 50 Artikel mit 1, 16 mit 2, keiner über 2 (alle im Bereich 1 bis 5). 34 neue Vorschläge: 31 mal A, 3 mal B, keine C. Davon 13 mal vorhandene Szene wiederverwenden (nur in Artikeln ohne Abbildung: Von grund auf, Überblick, Das Wichtigste) und 21 neue Animationen. Alle 48 vorhandenen Szenen eignen sich zum Animieren (siehe jeweils „Vorhandene Abbildungen“). Über dem Soll (+1, jeweils begründet): Heft 07 Art. 06 und 09 (V4, V5), Heft 08 Art. 04 und 06 (V9, V10), Heft 10 Art. 06 (V21), das sind 5 von 66 Artikeln. Die Kurzbilanz-Tabellen stehen je Heft.

Besonderheit: Fast jeder Artikel „Von grund auf“ und „Das Wichtigste“ hat bisher keine Abbildung; dort wird bevorzugt eine vorhandene Szene wiederverwendet (kein neuer Zeichenaufwand, keine Doppelung). Die Rechenbild-Pflicht (Σ/∏/Skalarprodukt mit Zahlen im Kernstück eines Beispiels) trifft in diesen Heften nur zweimal zu: V21 (Produkt der Gewichte, Heft 10) und, als Zeigerkette statt Σ, V15 (Heft 09).

## Top 3

- V9 [A] Heft 08 Art. 04 — Stehende Wellen am Zonenrand (Berge im Topf, Berge in der Barriere) — zeigt den Mechanismus der Bandlücke, den bisher nur ein Satz erklärt, und trägt alle folgenden Hefte.
- V28 [A] Heft 11 Art. 08 — Drei Temperaturbereiche im Banddiagramm (Ausfrieren, Erschöpfung, Eigenleitung mit laufender E_F-Linie) — die Hauptaussage des Hefts ist sonst nur eine Kurve.
- V15 [A] Heft 09 Art. 04 — Drei Hüpfwege löschen sich aus (Zeigerkette für |f(k)| bei Γ, M, K) — macht die Dirac-Punkte in Graphen anschaulich statt als Satz über Phasen.

## Editor-Lücken (Zahl der Vorschläge)

- L1 (Verschwinden): 1 zwingend mit Umgehung (V26 Rekombination), 3 komfortabler damit (V1, V7, V11).
- L2 (Umformen/Morph): 2 Wünsche (Übergang der Bänderkurven in Heft 08, Falten der Parabel in Heft 07).
- L3 (Parameter/Zeit animieren): 3 mit Umgehung (V15 k-Weg, V22 E_F-Wanderung, V28 Temperatur), 9 weitere Wünsche bei vorhandenen Szenen (T-, r-, V_sp-, N_D-Sweep, Punkt mit mitlaufender Tangente).
- L4 (Kamera): 2 Wünsche (3D-Zonen, E(kx,ky)-Fläche).
- L6 (Teilchen): 2 mit Umgehung (V17 Besetzung verschiebt sich, V29 Ausfrieren), 1 Wunsch (Hall-Platte).
- L9 (Zellen einzeln betonen): 1 (V10 Matrixeinträge).
- L-neu: keine. Alles Übrige ist mit dem heutigen Editor machbar (Create, FadeIn, Shift, Rotate, MoveAlongPath, Table, Vector, TextBox, Operation ∏).

## HEFT 07 Kristallwachstum und reziprokes Gitter

### Kurzbilanz Heft 07
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Vom Quarz zum Rohsilizium | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Reinigung über die Gasphase | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Der Einkristall | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06 Reziprokes Gitter in 1D | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07 Reziproke Gittervektoren | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Die Brillouin-Zone | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Netzebenen und reziproke Vektoren | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 10 Der Kristall im Überblick | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Über dem Soll (+1, begründet im Vorschlag): Art. 06 (V4), Art. 09 (V5).

### V1 [A] Vom Sand zum Wafer und zur Zone (Überblick)
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/01-kristallwachstum-und-reziprokes-gitter.md
- **Stelle:** Worum es geht — „Jeder Mikrochip beginnt als Sand. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Obere Reihe aus TextBox-Kästen: „Quarzsand SiO2“, „Rohsilizium“, „Trichlorsilan SiHCl3“, „Polysilizium“, „Einkristall“, „Wafer“; unter jedem Kasten der Fremdatomanteil als Text: 100 % SiO2 (Ausgang), 2 bis 4 %, ≈ 0 nach Destillation, 3·10^-11, 3·10^-11 (Kristall), Wafer. Untere Reihe, abgesetzt und blau: „Kristall“ → „reziprokes Gitter“ → „Brillouin-Zone“ → „Elektronen im Kristall“ (die zweite Frage des Kapitels). Ein roter Punkt („Silizium“) wandert durch die obere Reihe.
- **Ablauf:** 1. Kästen der oberen Reihe erscheinen nacheinander (FadeIn). 2. Punkt wandert (MoveAlongPath) Kasten für Kasten; unter jedem erscheint beim Eintreffen der Fremdatomwert (Write). 3. Untere Reihe baut sich auf; Pfeil „Welle sieht das Gitter“. — Haltepunkte: Schritt 2 bei „Rohsilizium → Trichlorsilan“ (Faktor 10^9).
- **Verständnisproblem:** Der Leser sieht die ganze Kette des Kapitels (Herstellung, dann Beschreibung des Gitters) nicht als zwei Fragen vor sich; die Zahlen 10^9 und die Reihenfolge der Verfahren bleiben abstrakt.
- **Szenenname:** gemb1/k7weg
- **Editor-Lücke:** machbar (Wechsel des Zahlenwerts am selben Ort wäre schöner mit L1 Verschwinden / L2 Umformen; Umgehung: Werte stehen nebeneinander und erscheinen nacheinander)

### V2 [A] Wigner-Seitz-Zelle wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/02-von-grund-auf-was-aus-teil-2-und-teil-6-gebraucht-wird.md
- **Stelle:** Von Grund auf — „⁠Gitter. Ein Kristall ist Punktgitter plus Basis. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** Szene gemb1/k6wigner aus Teil 6 (Konstruktion der Wigner-Seitz-Zelle: Mittelsenkrechten zu den Nachbarn, Zelle getönt). Szene dort zur Animation (Mittelsenkrechten erscheinen nacheinander) vorgesehen; hier unverändert zeigen.
- **Ablauf:** 1. Gitterpunkte, 2. Verbindungslinien zu den Nachbarn, 3. Mittelsenkrechten, 4. Zelle getönt. — Haltepunkt: 3.
- **Verständnisproblem:** Der Artikel nennt die Wigner-Seitz-Zelle nur in einem Satz und einer Tabelle; Teil 8 baut darauf die Brillouin-Zone, die Konstruktion muss gegenwärtig sein. Die Welle auf der Kette ist hier nur Formel, ihr Bild folgt in V4 (nicht doppeln).
- **Szenenname:** gemb1/k6wigner (vorhanden)
- **Editor-Lücke:** machbar

### V3 [A] Anlagern an den Impfkristall und Segregation (Czochralski)
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/05-der-einkristall.md
- **Stelle:** Der Einkristall — „Segregation. Ein Fremdatom hat eine andere Größe …“ (und „Die Idee. Ordnung lässt sich nicht nachträglich …“)
- **Art:** neue Animation
- **Was zu sehen ist:** Mikroskopischer Ausschnitt der Wachstumsfront: unten ein Gitter aus blauen Si-Kreisen (Kristall, quadratisches Raster als Vereinfachung des Diamantgitters, als solche beschriftet), darüber Schmelze mit ungeordnet verteilten blauen Kreisen und einigen roten Kreisen (Fremdatome, 4 von 24). Rechts Balken „Fremdatomanteil“: Kristall / Schmelze, Skala 0 bis 100 % der Ausgangskonzentration.
- **Ablauf:** 1. Schmelze mit Atomen erscheint. 2. Ein blaues Atom wandert (MoveTo) auf einen freien Gitterplatz der obersten Lage und rastet ein; Lage für Lage wiederholen (3 bis 4 Atome), die Lage setzt das Gitter fort. 3. Ein rotes Atom nähert sich, bleibt kurz am Platz und kehrt in die Schmelze zurück (Shift hin, Shift zurück, Beschriftung „passt schlechter“). 4. Der Balken der Schmelze wächst, der des Kristalls bleibt niedrig. — Haltepunkte: 2 und 3.
- **Verständnisproblem:** „Jede Atomlage setzt das Gitter fort“ und „Segregation“ sind zwei Begriffe, die nur als Text stehen; die vorhandene Abbildung zeigt die Anlage, nicht den Vorgang an der Grenzfläche. Über dem Soll nicht: Soll 2.
- **Szenenname:** gemb1/k7front
- **Editor-Lücke:** machbar (Rückkehr des roten Atoms mit Shift zurück; „verschwinden“ braucht kein L1)

### V4 [A] Eine Welle, zwei Wellenzahlen: dieselben Punkte (Aliasing der Kette)
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/06-das-reziproke-gitter-in-einer-dimension.md
- **Stelle:** Das reziproke Gitter in einer Dimension — „Die Idee. Eine Kette tastet eine Welle nur an den Punkten …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achse x von 0 bis 5a mit a = 0,2 nm, Punkte bei x = ℓa (ℓ = 0…5). Blaue Kosinus-Welle mit k1 = 0,25·(2π/a), rote Welle mit k2 = k1 + 2π/a (4-fach so dichte Schwingung: Faktor 1,25 vs 0,25 in Einheiten 2π/a). Unter der Achse Zahlenstrahl k mit Marke bei k1, k2, Gitterpunkte des k-Raums 0, 2π/a, 4π/a. Beschriftung „Re ψ_ℓ = cos(k ℓ a)“.
- **Ablauf:** 1. Achse mit Punkten, 2. blaue Welle zeichnet sich (Create), Werte an den Punkten als Markierungen. 3. Rote Welle zeichnet sich durch dieselben Markierungen. 4. Zahlenstrahl: Pfeil von k1 nach k2 mit Beschriftung „+2π/a = G“. 5. Text: „gleiche Zahlen an allen Punkten, also dieselbe Welle“. — Haltepunkte: 3 und 4.
- **Verständnisproblem:** Warum alles in k periodisch ist (Satz 4.2) bleibt Formel; die vorhandene Abbildung zeigt schon die Folge (Kosinus-Band und Parabelkopien), aber nicht ihre Ursache. Über Soll +1, begründet: Ursache und Folge sind zwei verschiedene Bilder; die Ursache ist die zentrale Idee der Stufe.
- **Szenenname:** gemb1/k7alias
- **Editor-Lücke:** machbar (Schritt 4 sauberer mit L3 Parameter-Sweep: k2 gleitet von k1 hoch, Punkte bleiben; Umgehung: zwei Wellen nacheinander)

### V5 [A] Bragg-Reflexion an Netzebenen und der Zonenrand
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/09-netzebenen-und-reziproke-vektoren.md
- **Stelle:** Zonenrand und Reflexion — „Eine Welle trifft unter dem Winkel θ zur Ebene auf parallele Netzebenen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei waagerechte Netzebenen als Linien im Abstand d (0,3136 nm, Silizium (111)), Gitterpunkte darauf. Einfallender Strahl unter θ = 14,2° (grüner Pfeil) für λ = 0,1541 nm, reflektierte Teilstrahlen von Ebene 1 und Ebene 2; der Umweg 2d sinθ als dick markierter Streckenzug (Measure). Daneben Text „2d sinθ = νλ“.
- **Ablauf:** 1. Ebenen und Gitterpunkte. 2. Strahl trifft Ebene 1, reflektierter Teil geht weg. 3. Zweiter Strahl trifft Ebene 2; der Umweg wird als Doppelstück markiert, Text „= λ“. 4. Beide Teilwellen als gleich phasige Wellenzüge, Vermerk „verstärkt“. 5. Rechts: k-Raum-Skizze mit Zonenrand-Mittelebene und Vektor k mit |k| sinθ = π/d = 10,02 nm^-1. — Haltepunkte: 3 und 5.
- **Verständnisproblem:** Der Satz, dass der Zonenrand die Bragg-Bedingung ist und dort die Gruppengeschwindigkeit verschwindet, hängt an einer Umweg-Überlegung ohne Bild. Über Soll +1, begründet: neuer Begriff (Bragg) mit Verfahren, und das vorhandene Bild zeigt nur die Ebenenscharen.
- **Szenenname:** gemb1/k7bragg
- **Editor-Lücke:** machbar (laufende Wellenzüge bräuchten L3; hier Strahlen als Pfeile mit Create)

### V6 [A] Zusammenschau wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/07-kristallwachstum-und-reziprokes-gitter/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Das Gitter ist die Vorlage, und alles muss zu ihm passen …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** Die Szene gemb1/k7weg aus V1, am Ende alle Kästen sichtbar; so schließt der Artikel den Bogen zum Überblick.
- **Ablauf:** wie V1, hier ohne Zahlenspalte; Haltepunkt: letzter Schritt.
- **Verständnisproblem:** Die Tabelle „Ergebnis – Woher es kommt“ ist reiner Text; die Kette der Verfahren fehlt als Bild.
- **Szenenname:** gemb1/k7weg (aus V1)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 07
- gemb1/k7ofen (03): animieren ja — Schritte: 1. Ofen und Zonen erscheinen, 2. Lichtbogen, 3. SiO-Gas steigt (MoveAlongPath, blau), 4. Festes sinkt (rot), 5. Silizium sammelt sich unten | Lücke: machbar
- gemb1/k7siede (04): animieren ja — Schritte: 1. Siedetemperaturen als Balken erscheinen, SiHCl3 rot, 2. Stab erscheint, 3. Gas strömt zum Stab, Stab wird dicker (Scale) | Lücke: machbar
- gemb1/k7ziehen (05): animieren ja — Schritte: 1. Impfkristall taucht ein, 2. Hals (schnell), 3. Durchmesser wächst, Kristall wandert nach oben (Shift), 4. Versetzungen (rot) laufen im Hals zum Rand | Lücke: machbar
- gemb1/k7periodisch (06): animieren ja — Schritte: 1. Kosinus-Band zeichnet sich, 2. Kopien in den Nachbarzonen, 3. Parabel mit Kopien, 4. Abschnitte 1, 2, 3 falten sich in die Zone (Shift) | Lücke: machbar (Falten als Morph wäre L2)
- gemb1/k7rezi2d (07): animieren ja — Schritte: 1. a1, a2 im Ortsgitter, 2. b1, b2 erscheinen, senkrecht auf dem jeweils anderen a, 3. reziproke Zelle getönt, 4. zentriertes Gitter | Lücke: machbar
- gemb1/k7zonen (08): animieren ja — Schritte: 1. reziproke Gitterpunkte, 2. Verbindungslinien zu den Nachbarn (Create), 3. Mittelsenkrechte (Create), 4. Zone getönt; unten 3D-Zonen nacheinander | Lücke: machbar (3D-Drehen L4)
- gemb1/k7ebenen (09): animieren ja — Schritte: 1. Rechteckgitter, 2. Schar (1 1) erscheint, d markiert, 3. Pfeil G im reziproken Gitter, 4. Schar (2 1), längerer Pfeil | Lücke: machbar
- gemb1/k7ueberblick (10): animieren ja — Schritte: 1. Bindung, 2. Struktur, 3. Gitter und Basis, 4. rechte Spalte (reziprokes Gitter, Zone) mit Pfeilen | Lücke: machbar

## HEFT 08 Vom Atom zum Band

### Kurzbilanz Heft 08
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Was aus der Periodizität folgt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Bänder und Lücken | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05 Zwei Atome | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Vier Atome und die Matrix | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07 Viele Atome | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Bandbreite, Abstand, Besetzung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Zwei Orbitale je Atom | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 10 Das Rezept | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Über dem Soll (+1, begründet im Vorschlag): Art. 04 (V9), Art. 06 (V10).

### V7 [A] Von einem Niveau zum Band (Überblick)
- **Artikel:** content/gemb1/08-vom-atom-zum-band/01-vom-atom-zum-band.md
- **Stelle:** Worum es geht — „Ein einzelnes Atom hat scharfe Energieniveaus …“
- **Art:** neue Animation
- **Was zu sehen ist:** Senkrechte Energieachse E von -6,2 bis -3,8 eV (Rechenmodell E_s = -5 eV, V_ss = 0,5 eV), Spalten für N = 1, 2, 4, 20 Atome (unten je eine Reihe Kreise = Atome), waagerechte Niveaustriche, gestrichelt bei E_s ± 2V_ss = -6 und -4 eV der Rand des späteren Bands.
- **Ablauf:** 1. N = 1: ein Strich bei -5 eV. 2. N = 2: zweiter Atomkreis erscheint, der Strich teilt sich in -5,5 und -4,5 eV (zwei Linien wandern auseinander, Shift). 3. N = 4: Striche bei -5,809; -5,309; -4,691; -4,191 eV. 4. N = 20: zwanzig Striche zwischen -5,989 und -4,011 eV. 5. Das Band zwischen den gestrichelten Linien wird getönt, Beschriftung „N Zustände, Breite 4V_ss“. — Haltepunkte: 2 und 4. Vereinfachung kennzeichnen: Kette, ein s-Orbital je Atom, nur nächste Nachbarn.
- **Verständnisproblem:** Die Leitfrage („Was geschieht mit den Niveaus, wenn viele Atome nebeneinander sitzen?“) hat kein Bild; „Niveau wird Band“ bleibt ein Satz bis Stufe 5.
- **Szenenname:** gemb1/k8aufspalt
- **Editor-Lücke:** machbar (Wechsel von N ohne Verschwinden der alten Gruppe: Spalten nebeneinander; sauberer mit L1)

### V8 [A] Bindendes und antibindendes Orbital wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/08-vom-atom-zum-band/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Von Grund auf — „Teil 4 und 5. Ein Orbital ist die Wellenfunktion eines Elektrons im Atom. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k5molekuel (Niveau 1s spaltet in H2 auf, bindend unten, antibindend oben, Dichte auf der Kernachse). Genau diese Aufspaltung setzt das Heft auf viele Atome fort.
- **Ablauf:** 1. zwei getrennte Niveaus, 2. Atome rücken zusammen, 3. Aufspaltung in zwei, 4. beide Elektronen unten. — Haltepunkt: 3.
- **Verständnisproblem:** Der Rückblick zählt fünf Teile in Formeln auf; die Aufspaltung zweier Niveaus ist Grundlage von Stufe 3 und soll bildlich gegenwärtig sein.
- **Szenenname:** gemb1/k5molekuel (vorhanden)
- **Editor-Lücke:** machbar

### V9 [A] Stehende Wellen am Zonenrand: Berge im Topf oder in der Barriere
- **Artikel:** content/gemb1/08-vom-atom-zum-band/04-bander-und-lucken.md
- **Stelle:** Bänder und Lücken — „Die Idee. An jeder Barriere wird ein kleiner Teil der Welle zurückgeworfen. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Kammpotential mit a = 1,2 nm (b = 0,2 nm, Töpfe w = 1 nm, V_B = 1 eV), vier Perioden, x von 0 bis 4,8 nm. Dazu die Dichten cos²(πx/a) (Berge in den Töpfen, blau) und sin²(πx/a) (Berge in den Barrieren, orange). Rechts ein kleines E(k)-Bild mit den beiden Energien am Zonenrand: unten 268 meV, oben 535 meV, Lücke dazwischen (Tabelle b = 0,2 nm).
- **Ablauf:** 1. Kammpotential. 2. Hin- und rücklaufende Welle als zwei Pfeile, „Umweg 2a = λ“. 3. cos²-Dichte zeichnet sich (Create), Marker tief auf der Energieachse (268 meV). 4. sin²-Dichte zeichnet sich, Marker hoch (535 meV). 5. Zwischenraum grau: „keine Lösung“. — Haltepunkte: 3 und 4.
- **Verständnisproblem:** Warum sich gerade am Zonenrand eine Lücke öffnet, steht nur als Satz („zwei stehende Wellen, die zweite spürt das hohe Potential“); k8baender zeigt das Ergebnis, nicht den Mechanismus. Über Soll +1, begründet: Mechanismus der Lücke, zentral für alle Folgekapitel.
- **Szenenname:** gemb1/k8stehend
- **Editor-Lücke:** machbar

### V10 [A] Wie ein Matrixeintrag entsteht und welche wegfallen
- **Artikel:** content/gemb1/08-vom-atom-zum-band/06-vier-atome-und-die-matrix.md
- **Stelle:** Vier Atome und die Matrix — „Welche Einträge bleiben. Die Orbitale klingen exponentiell ab, das entscheidet alles.“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben vier Atome ℓ = 1…4 im Abstand a mit je einer exponentiell abfallenden Orbitalkurve φ_ℓ. Darunter die 4×4-Matrix H als Table: E_s (Diagonale), -V_ss (Nebendiagonale), 0 (sonst).
- **Ablauf:** 1. Atome und Orbitale erscheinen. 2. Eintrag (1,1) leuchtet, Atom 1 markiert: „⟨1|H|1⟩ ≈ E_s“. 3. Eintrag (1,2): Atome 1 und 2 verbunden, Überlappfläche getönt, Eintrag „-V_ss“. 4. Eintrag (1,3): Überlappfläche kaum sichtbar, Faktor e^(-κa) = 0,057 mit κ = 11,5 nm^-1, Eintrag wird grau „≈ 0“. 5. Übrige Einträge füllen sich, das Tridiagonalmuster entsteht. — Haltepunkte: 3 und 4.
- **Verständnisproblem:** Matrix, Orbitalüberlapp und Nächste-Nachbar-Näherung bleiben getrennt; der Leser sieht nicht, dass jeder Eintrag ein Atompaar ist. Über Soll +1, begründet: Aufbau der Matrix ist der Kern des Verfahrens, k8vier zeigt nur die Lösung.
- **Szenenname:** gemb1/k8matrix
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zellen einzeln betonen; Umgehung mit Rechtecken über der Table)

### V11 [A] Warum das p-Band auf dem Kopf steht: Vorzeichen in der Kette
- **Artikel:** content/gemb1/08-vom-atom-zum-band/09-zwei-orbitale-je-atom.md
- **Stelle:** Zwei Orbitale je Atom — „So liest man das: … Das p-Band steht auf dem Kopf: Bei k=0 treffen sich gleich ausgerichtete p-Orbitale …“
- **Art:** neue Animation
- **Was zu sehen ist:** Vier Atome in einer Reihe, je ein s-Orbital (Kreis) und ein p-Orbital (Keulen links blau +, rechts rot -). Zwei Zeilen (s, p), zwei Zustände: k = 0 (alle Faktoren e^(jkℓa) = +1) und k = π/a (Faktoren +1, -1, +1, -1; Farben wechseln). Rechts Energiemarker: bei k = 0 s-Band am Boden (-6 eV), p-Band oben (+0,5 eV); bei k = π/a s oben (-4 eV), p unten (-2,5 eV).
- **Ablauf:** 1. s-Reihe bei k = 0: alle blau, gleiches Vorzeichen, „bindend“. 2. p-Reihe bei k = 0: rote Keule von ℓ trifft blaue von ℓ+1, „antibindend“. 3. Wechsel zu k = π/a: Orbitale wechseln abwechselnd die Farbe, p-Paare treffen gleiche Farben, „bindend“, s-Paare „antibindend“. 4. Energiemarker rücken in die Bandkanten. — Haltepunkte: 2 und 3.
- **Verständnisproblem:** Die Umkehrung des p-Bands und die Lücke am Zonenrand sind nur sprachlich begründet; die Regel „gleiches Vorzeichen bindet“ muss an der Kette gesehen werden. k8sp zeigt nur einen Nachbarn und das Ergebnis.
- **Szenenname:** gemb1/k8pband
- **Editor-Lücke:** machbar (zwei Zeilen statt Farbwechsel; sauberer mit L1)

### V12 [A] Zusammenschau wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/08-vom-atom-zum-band/11-das-wichtigste.md
- **Stelle:** Die Antwort in drei Sätzen — „Rücken Atome zusammen, überlappen ihre Orbitale, und jedes Niveau spaltet …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k8aufspalt aus V7, zum Schluss mit den drei Aussagen beschriftet (zwei Atome → zwei Niveaus; N Atome → Band; Breite 4V_ss).
- **Ablauf:** wie V7; Haltepunkt: N = 20.
- **Verständnisproblem:** Die Reihenfolge Niveau → Aufspaltung → Band steht nur in Worten.
- **Szenenname:** gemb1/k8aufspalt (aus V7)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 08
- gemb1/k8bloch (03): animieren ja — Schritte: 1. Kammpotential, 2. Einhüllende cos(kx) zeichnet sich, 3. periodische Funktion u_k, 4. Produkt Re ψ, 5. Dichte |ψ|² mit Periode a | Lücke: machbar
- gemb1/k8baender (04): animieren ja — Schritte: 1. Parabel, 2. Bänder b = 0,2 nm getönt, Lücke grau, 3. Bänder b = 0,4 nm schmaler, Lücke breiter | Lücke: machbar (Übergang als Morph: L2)
- gemb1/k8doppel (05): animieren ja — Schritte: 1. zwei Töpfe, 2. bindender Zustand (Dichte in der Barriere), 3. antibindender (Knoten), 4. rechts: Niveau 190,8 meV teilt sich in 175,5 und 205,0 meV | Lücke: machbar
- gemb1/k8vier (06): animieren ja — Schritte: 1. Koeffizienten n = 1 bis 4 nacheinander (Vorzeichenwechsel zählen), 2. Einhüllende sin(nπℓ/5), 3. Energien erscheinen auf dem Kosinus | Lücke: machbar
- gemb1/k8leiter (07): animieren ja — Schritte: 1. Niveaus für N = 2, 4, 8, 20, 2. Band mit 20 Zuständen, 3. Zustand am Boden (gleichphasig), 4. Zustand oben (gegenphasig) | Lücke: machbar (N als Zeit: L3)
- gemb1/k8abstand (08): animieren ja — Schritte: 1. Kurven E_s ± 2V_ss(r) von großem r zu kleinem r (Create läuft von rechts nach links), 2. Marker r läuft mit, Niveau wird Band, 3. bei kleinem r überlappen beide Bänder, 4. rechts: Besetzung Metall, Isolator, Halbleiter nacheinander | Lücke: machbar (r als Sweep: L3)
- gemb1/k8sp (09): animieren ja — Schritte: 1. Kopplung zum rechten Nachbarn, Vorzeichen, 2. s- und p-Band bei V_sp = 0 (gestrichelt), 3. Mischung: Bänder stoßen sich ab | Lücke: machbar (V_sp-Sweep: L3)
- gemb1/k8rezept (10): animieren ja — Schritte: 1. Zickzackkette, zentrale Zelle grau, 2. Kopplungen A-B (Mitte, links, rechts), 3. Bänder ±V·sqrt(2(1+cos ka)) zeichnen sich, 4. Berührung am Zonenrand | Lücke: machbar

## HEFT 09 Bandstrukturen lesen

### Kurzbilanz Heft 09
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Das Band in der Ebene | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Graphen | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05 Silizium | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06 GaAs, direkte und indirekte Lücke | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Die effektive Masse im Kristall | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Masse und Richtung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Das Loch | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 10 Was man an einer Bandstruktur abliest | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Kein Artikel über dem Soll.

### V13 [A] Die vier Größen an einer Bandstruktur (Überblick)
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/01-bandstrukturen-lesen.md
- **Stelle:** Worum es geht — „Wer das kann, sieht einem Stoff an, ob er leitet … Vier Größen tragen das Kapitel.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen E (eV) über k (von -π/a bis π/a); ein Valenzband (blau, Maximum bei k = 0) und ein Leitungsband (rot, Minimum bei k = 0), schematisch und als „qualitativ, nicht gerechnet“ gekennzeichnet; vier Beschriftungen: „Bandlücke E_g“, „Krümmung = effektive Masse“, „Loch“, „Entartung“.
- **Ablauf:** 1. Achsen und beide Bänder zeichnen sich (Create). 2. Doppelpfeil (Measure) zwischen Valenzbandmaximum und Leitungsbandminimum, „E_g“. 3. Kleine Parabel (grün, gestrichelt) an der Leitungsbandkante, Text „enge Parabel = kleine Masse“. 4. Im Valenzband erscheint ein offener Kreis mit „+“ (leerer Zustand = Loch). 5. Ein zweites Valenzband mit anderer Krümmung erscheint, beide treffen sich bei k = 0: „zwei Bänder, gleiche Energie = Entartung 2“. — Haltepunkte: 2 bis 5.
- **Verständnisproblem:** Vier Fachbegriffe werden in einem Absatz eingeführt, ohne dass der Leser sie an einem Diagramm sieht; das Kapitel handelt vom Lesen eines Diagramms, das es erst später zeigt.
- **Szenenname:** gemb1/k9vier
- **Editor-Lücke:** machbar

### V14 [A] Steigung und Krümmung von E(k) wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Von Grund auf — „Teil 2. Geschwindigkeit und effektive Masse folgen aus Steigung und Krümmung von E(k).“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k2kosinus (Kosinus-Band, v(k), freie Parabel gestrichelt).
- **Ablauf:** 1. Band zeichnet sich, 2. Tangente läuft entlang, Steigung = ħv, 3. v(k) darunter. — Haltepunkt: 2.
- **Verständnisproblem:** Der Rückblick gibt v und m* nur als Formel; das ganze Heft liest Steigung und Krümmung aus Diagrammen ab.
- **Szenenname:** gemb1/k2kosinus (vorhanden)
- **Editor-Lücke:** machbar

### V15 [A] Drei Hüpfwege löschen sich aus: |f(k)| als Zeigerkette
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/04-graphen.md
- **Stelle:** Graphen — „So liest man das: … Bei Γ addieren sich die drei Wege, |f|=3. Bei M ist |f|=1. Bei K haben die drei Summanden von f die Phasen 0, 240° und 120° …“
- **Art:** neue Animation
- **Was zu sehen ist:** Komplexe Ebene (Re von -1 bis 3, Im von -2 bis 2) mit drei Einheitszeigern f = 1 + e^(jk·a1) + e^(jk·a2), aneinandergesetzt. Drei Zustände nebeneinander: Γ, M, K. Darunter der Betrag |f| und die Energien E± = E_p ± V·|f| in eV für V_ppπ = 2,8 eV: ±8,4; ±2,8; 0. Daneben Skizze der Zone mit dem laufenden Punkt k.
- **Ablauf:** 1. Γ: alle drei Zeiger bei Phase 0, Kette ist 3 lang, Energien ±8,4 eV. 2. M: zweiter und dritter Zeiger drehen auf 180° (Rotate), Summe -1, |f| = 1, ±2,8 eV. 3. K: Zeiger zwei auf 240°, Zeiger drei auf 120° (Rotate um den Anfang des jeweiligen Zeigers), die Kette schließt sich zum Dreieck, Summe 0. 4. Die beiden Bänder berühren sich bei E_p. — Haltepunkte: 2 und 3.
- **Verständnisproblem:** „Die drei Wege löschen sich aus“ ist der Kern der Dirac-Punkte, steht aber nur als Satz; die Summe dreier komplexer Phasen mit konkreten Winkeln ist Kernstück der Argumentation. Rechenbild für ein Σ mit komplexen Zahlen gibt es im Editor nicht (Σ/∏ nur für reelle Terme), daher die Zeigerdarstellung.
- **Szenenname:** gemb1/k9fzeiger
- **Editor-Lücke:** braucht Editor-Funktion: L3 (k als Parameter entlang des Wegs Γ→M→K; Umgehung: drei feste Stationen)

### V16 [A] Von acht Orbitalen zu acht Bändern: Zählen und Füllen
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/05-silizium.md
- **Stelle:** Silizium — „Die Idee. Zuerst wird gezählt. Silizium hat die Konfiguration 1s² 2s² 2p⁶ 3s² 3p² …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Energieachse mit den Niveaus eines Si-Atoms (3s und 3p), rechts zwei Atome A und B der Zelle (je 4 Außenelektronen = 8 Elektronen). Mitte: 8 Striche (Orbitale), die sich zu 8 Bändern verbreitern, untere vier (bindend, blau) und obere vier (antibindend, rot). Elektronen als kleine Punkte.
- **Ablauf:** 1. Zwei Atome mit je vier Orbitalen: 8 Striche. 2. Aufspaltung in 4 bindende und 4 antibindende Bänder (Striche wandern auseinander, zur Bandbreite verbreitert, mit Lücke dazwischen als Vereinfachung gezeichnet). 3. Acht Elektronen als Punkte fallen nacheinander in die unteren Bänder, je zwei pro Band (Pauli). 4. Beschriftung „4 volle Bänder, 4 leere“, Lücke E_g = 1,12 eV. — Haltepunkte: 3.
- **Verständnisproblem:** Die Zählregel (Bänder = Orbitale der Zelle, volle Bänder = Elektronen / 2) bleibt abstrakt; die Frage „Woher kommen die Elektronen im vollen Valenzband?“ wird nur im Fragekasten beantwortet.
- **Szenenname:** gemb1/k9zaehlen
- **Editor-Lücke:** machbar

### V17 [A] Warum nur teilgefüllte Bänder leiten: das Feld verschiebt die Besetzung
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/10-was-man-an-einer-bandstruktur-abliest.md
- **Stelle:** Was man an einer Bandstruktur abliest — „Die Idee. … Leitung heißt: Ein Feld ändert k, also muss ein Elektron in einen benachbarten freien Zustand wechseln können.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Bänder nebeneinander als E(k)-Diagramm mit Zuständen als Kreisen (15 Zustände, k von -π/a bis π/a): links halbgefülltes Band (Metall), rechts volles Band mit leerem Band darüber (Halbleiter/Isolator, Lücke). Besetzte Zustände blau, leere grau. Pfeil „Feld“ (Kraft auf k).
- **Ablauf:** 1. Beide Diagramme mit Besetzung bis E_F. 2. Das Feld schaltet ein: links verschiebt sich die ganze Besetzung um ein, zwei Zustände nach rechts (Shift), mehr Elektronen bei +k als bei -k, „Strom“. 3. Rechts: Die Besetzung kann nicht ausweichen, jeder Platz ist belegt (Mark ✗); Nettoverschiebung ändert nichts, „kein Strom“. 4. Bei T > 0: ein Elektron springt über die Lücke (Halbleiter), erzeugt Loch und freien Platz, beide verschieben sich. — Haltepunkte: 2 und 3. Vereinfachung kennzeichnen: ohne Stöße gezeigt, die Besetzung driftet nur anfangs weiter.
- **Verständnisproblem:** Warum ein volles Band nicht leitet, ein halbes aber doch, ist das Kriterium für alle fünf Ablese-Schritte, wird aber nur in Worten und in einem Fragekasten (Teil 8) erklärt.
- **Szenenname:** gemb1/k9feld
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte; Umgehung: 15 Kreise als einzelne Objekte, Shift als Gruppe)

### V18 [A] Zusammenschau wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/09-bandstrukturen-lesen/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Eine Bandstruktur ist E(k) plus Besetzung. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k9lesen (Metall, Halbleiter, Isolator, Graphen mit E_F), animiert wie unter den vorhandenen Abbildungen.
- **Ablauf:** 1. Metall, 2. Halbleiter, 3. Isolator (nur Lücke größer), 4. Graphen. — Haltepunkt: 2.
- **Verständnisproblem:** „E(k) plus Besetzung“ wird als Satz gesagt; die Gegenüberstellung steht in Teil 10, nicht neben der Zusammenfassung.
- **Szenenname:** gemb1/k9lesen (vorhanden)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 09
- gemb1/k9quadrat (03): animieren ja — Schritte: 1. Zone mit Linien konstanter Energie, 2. Weg Γ→X→M→Γ als Pfeile (Create), 3. Punkt läuft auf dem Weg und zugleich auf der Bandstruktur rechts (zwei MoveAlongPath), 4. Sattel bei X markiert | Lücke: machbar (3D-Fläche mit Kameradrehung wäre L4)
- gemb1/k9graphen (04): animieren ja — Schritte: 1. Wabe, Zelle dunkelgrau, Nachbarzellen hellgrau, 2. Zone mit Weg Γ→M→K→Γ, 3. Bänder zeichnen sich, 4. Berührung bei K, Kegel | Lücke: machbar
- gemb1/k9silizium (05): animieren ja — Schritte: 1. Valenzbänder (blau), 2. Leitungsbänder (rot), Lücke grau, 3. Bandkanten markiert, 4. rechts Schnitt k_z = 0: vier Täler erscheinen nacheinander, dann die zwei auf der k_z-Achse | Lücke: machbar
- gemb1/k9gaas (06): animieren ja — Schritte: 1. GaAs: Kante über Kante, Photon als senkrechter Pfeil, 2. Nebentäler L, X, 3. Silizium: Photon senkrecht, dann Phonon waagerecht (zwei Pfeile nacheinander), 4. Summe = Sprung | Lücke: machbar
- gemb1/k9masse (07): animieren ja — Schritte: 1. drei Kurven E, v, m* erscheinen, 2. ein Punkt läuft gleichzeitig auf E(k) und v(k) von der Unterkante zur Oberkante (zwei MoveAlongPath), Steigung und Krümmung sichtbar, 3. bei |ka| = π/2: m* springt von +∞ nach -∞, rot getönte Bereiche, 4. Zonenrand erreicht, der Punkt erscheint links wieder (Bloch-Schwingung, als Vereinfachung ohne Stöße) | Lücke: machbar (Punkt auf Kurve mit mitlaufender Tangente: L3)
- gemb1/k9ellipse (08): animieren ja — Schritte: 1. Silizium-Ellipse (0,79 und 0,36 nm^-1) und GaAs-Kreis (0,21 nm^-1), 2. rechts Parabeln, 3. Zusatz: Kraftpfeil unter 45° zur Längsachse erscheint, dann der Beschleunigungspfeil bei 78,3° (Vektor, FadeIn) aus dem Beispiel | Lücke: machbar
- gemb1/k9loch (09): animieren ja — Schritte: 1. volles Band, symmetrisch, 2. ein Elektron fehlt (rot), Loch bei -k_e, 3. Ortsbild: Feld an, Elektronen rücken nacheinander nach links (Shift), der leere Platz wandert nach rechts | Lücke: machbar
- gemb1/k9lesen (10): animieren ja — Schritte: 1. Metall (Band schneidet E_F), 2. Halbleiter (kleine Lücke), 3. Isolator (große Lücke), 4. Graphen (Berührung) | Lücke: machbar

## HEFT 10 Zustandsdichte und Fermi-Verteilung

### Kurzbilanz Heft 10
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Warum man Zustände zählt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Kreisring und Kugelschale | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Leitungsband und Valenzband | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Anordnungen zählen | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07 Die Fermi-Verteilung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Temperatur und Boltzmann-Näherung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Elektronen und Löcher im Gleichgewicht | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 10 Ergänzung: Das Metall als Potentialtopf | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Über dem Soll (+1, begründet im Vorschlag): Art. 06 (V21).

### V19 [A] Sitze mal Belegung: Plätze auf Energiestufen (Überblick)
- **Artikel:** content/gemb1/10-zustandsdichte-und-fermi-verteilung/01-zustandsdichte-und-fermi-verteilung.md
- **Stelle:** Worum es geht — „Der Weg führt über acht Begriffe. Ladungsträger sind bewegliche Ladungen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Waagerechte Energiestufen (E_C und fünf Stufen darüber, Abstand k_BT), auf jeder Stufe Kreise = Plätze (unten viele, nach oben mehr, dann dichter, schematisch), gefüllte Kreise = besetzt. Rechts ein Balken „Zahl der Plätze“, ein zweiter „Anteil besetzt“, darunter „n = Σ (Plätze × Anteil)“. Als Vereinfachung gekennzeichnet (qualitativ, nicht Silizium-Zahlen).
- **Ablauf:** 1. Stufen erscheinen von unten, Plätze als leere Kreise. 2. Auf jeder Stufe füllen sich Kreise in der Reihenfolge: unten fast alle, oben fast keine (Elektronen fallen ein, FadeIn). 3. Eine Stufe wird markiert: Plätze g_i, Anteil f_i, Produkt N_i. 4. Alle Produkte addieren sich zum Gesamtbalken n. — Haltepunkte: 3.
- **Verständnisproblem:** Acht Begriffe werden in einem Absatz eingeführt, ohne dass der Leser die Grundidee „Plätze × Besetzung“ gesehen hat; das Stadionbild steht erst in Stufe 1.
- **Szenenname:** gemb1/k10sitze
- **Editor-Lücke:** machbar

### V20 [A] Zustandsdichte in 1D, 2D und 3D wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/10-zustandsdichte-und-fermi-verteilung/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Von Grund auf — „Erlaubte Wellenvektoren. In einem großen Kristall der Kantenlänge L sind die Zustände laufende Wellen. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k2dichte aus Teil 2 (Zustände der quadratischen Box im k-Raum, rot die unter einem Radius; mittlere Dichte in 1D, 2D, 3D).
- **Ablauf:** 1. Raster der k-Werte, 2. Kreis mit Radius n' = 6 wächst (Scale), die roten Punkte werden gezählt, 3. rechts die mittlere Dichte. — Haltepunkt: 2.
- **Verständnisproblem:** Die Wiederholung verlangt Raster, Spin und D(E) auf einmal, ohne ein Bild vom Abzählen.
- **Szenenname:** gemb1/k2dichte (vorhanden)
- **Editor-Lücke:** machbar

### V21 [A] Statistisches Gewicht als Produkt (Rechenbild ∏)
- **Artikel:** content/gemb1/10-zustandsdichte-und-fermi-verteilung/06-anordnungen-zahlen.md
- **Stelle:** Anordnungen zählen — „Beispiel. Zwei Gruppen gleicher Energie mit je g=4 Plätzen teilen sich vier Elektronen. Für N₁=0,…,4 ist W=1,16,36,16,1 …“
- **Art:** neue Animation (Rechenbild, Operation ∏)
- **Was zu sehen ist:** Das Produkt W = ∏ C(g_i, N_i) mit zwei Faktoren für die Verteilung N₁ = 2, N₂ = 2: C(4,2) = 6 und C(4,2) = 6, Ergebnis 36. Die Faktoren erscheinen als Kästen mit je 6 Mikrozuständen (kleine Platzreihen mit zwei gefüllten von vier Plätzen); weitere Fälle N₁ = 0, 1, 3, 4 mit W = 1·1, 4·4 = 16, 16, 1 und Gesamtzahl 70.
- **Ablauf:** 1. Gruppe 1: vier Plätze, zwei Elektronen, die sechs Möglichkeiten werden aufgezählt (Table), Faktor 6. 2. Gruppe 2 ebenso, Faktor 6. 3. Produkt-Rechenbild: 6 × 6 = 36 (Fläche 6×6 aus 36 Quadraten). 4. Die Fälle N₁ = 0…4 wiederholen sich als Balken 1, 16, 36, 16, 1; der Balken 36 trägt „51 % von 70“. — Haltepunkte: 3 und 4.
- **Verständnisproblem:** Warum sich die Gruppen zu einem Produkt verbinden und woher 36 kommt, steht nur in der Formel; es ist Kernstück des Beispiels, also nach Regel ein Rechenbild. Über Soll +1, begründet: Rechenbild-Pflicht, das vorhandene k10mikro zeigt nur die Gruppe und das Ergebnis.
- **Szenenname:** gemb1/k10gewicht
- **Editor-Lücke:** machbar (Operation ∏ im Editor)

### V22 [A] Massenwirkungsgesetz: E_F wandert, n·p bleibt
- **Artikel:** content/gemb1/10-zustandsdichte-und-fermi-verteilung/09-elektronen-und-locher-im-gleichgewicht.md
- **Stelle:** Elektronen und Löcher im Gleichgewicht — „So liest man das: Beim Multiplizieren addieren sich die Exponenten, und E_F fällt heraus. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Banddiagramm (E_C oben, E_V unten, Lücke 1,12 eV) mit einer verschiebbaren waagerechten Linie E_F. Rechts zwei waagerechte Balken auf logarithmischer Achse (1 bis 10^20 cm^-3): n (rot) und p (blau); darunter das Produkt n·p = 7,89·10^19 cm^-6 als konstanter Wert.
- **Ablauf:** 1. E_F in der Mitte (E_C - E_F = 0,56 eV): n = 1,10·10^10, p = 7,16·10^9. 2. E_F steigt (Shift) auf E_C - E_F = 0,2 eV: Balken n wächst auf 1,23·10^16, p schrumpft auf 6,41·10^3, die Summe der Balkenlängen (log) bleibt gleich. 3. Text „n·p = const“. — Haltepunkte: 1 und 2. Vereinfachung kennzeichnen: gültig solange E_F mehr als 3 k_BT von den Rändern entfernt ist.
- **Verständnisproblem:** Dass sich n und p gegenläufig ändern und ihr Produkt von E_F unabhängig ist, steht als Rechnung mit Exponenten; die Gegenläufigkeit ist die Grundlage für Dotierung im nächsten Heft. Das vorhandene k10dichte zeigt nur eine Lage von E_F.
- **Szenenname:** gemb1/k10gesetz
- **Editor-Lücke:** braucht Editor-Funktion: L3 (E_F als Parameter über die Zeit; Umgehung: zwei Stationen mit Shift der Linie und zweitem Balkenpaar)

### V23 [A] Plätze mal Besetzung wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/10-zustandsdichte-und-fermi-verteilung/11-das-wichtigste.md
- **Stelle:** Die Antwort in drei Sätzen — „Die Dichte der Ladungsträger ist die Summe über alle Plätze mal ihrer Besetzung …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k10dichte (D(E), f und 1-f, Produkt am Rand mit der Fläche n), animiert wie unten.
- **Ablauf:** 1. D(E) wächst als Wurzel, 2. f fällt exponentiell, 3. Produkt erscheint als Spitze bei E_C + k_BT/2, Fläche = n getönt. — Haltepunkt: 3.
- **Verständnisproblem:** Die drei Sätze fassen Zählen, Besetzen und Multiplizieren zusammen, ein Bild der Multiplikation fehlt beim Ergebnis.
- **Szenenname:** gemb1/k10dichte (vorhanden)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 10
- gemb1/k10band (03): animieren ja — Schritte: 1. Kosinus-Band mit Punkten auf der k-Achse, 2. ein Energiefenster wandert nach oben (Shift) und schneidet unten ein langes, in der Mitte ein kurzes k-Stück aus, 3. rechts wächst die Zustandsdichte Punkt für Punkt, Parabel gestrichelt | Lücke: machbar (Fenster als Sweep: L3)
- gemb1/k10kugel (04): animieren ja — Schritte: 1. Zustände einer Energie: zwei Punkte, Kreis, Kugel, 2. Fenster dk rot, 3. Folge für D(E) unten: E^(-1/2), konstant, E^(1/2) | Lücke: machbar (Wachsen von Ring/Schale: Scale)
- gemb1/k10kante (05): animieren ja — Schritte: 1. sechs Ellipsoide, 2. Rechts D(E) von E_C aus, 3. Vergleich GaAs: Kugel, 65-mal weniger | Lücke: machbar
- gemb1/k10mikro (06): animieren ja — Schritte: 1. Energiegruppen, 2. die sechs Mikrozustände von g = 4, N = 2 erscheinen nacheinander, 3. Balken für N₁ = 0…4 | Lücke: machbar
- gemb1/k10abzaehlen (07): animieren ja — Schritte: 1. 40 Niveaus, 20 Elektronen, 2. die Punkte der Auszählung erscheinen, 3. Fermi-Kurve legt sich darüber | Lücke: machbar
- gemb1/k10fermi (08): animieren ja — Schritte: 1. Stufe bei 0 K, 2. Kurve 300 K weicht auf, Aufweichzone 103 meV, 3. Kurve 1000 K, Tangente trifft E_F ± 2 k_BT, 4. rechts logarithmisch, Boltzmann-Faktor ab 3 | Lücke: machbar (T als Sweep: L3)
- gemb1/k10dichte (09): animieren ja — Schritte: 1. D(E) links, 2. f und 1-f in der Mitte, 3. Produkt rechts als Spitze, Fläche = n | Lücke: machbar
- gemb1/k10metall (10): animieren ja — Schritte: 1. Topf mit Potential der Rümpfe, 2. Fermi-Kugel füllt sich von innen (Scale), 3. Rand wird bei T > 0 unscharf, 4. rechts D und D·f | Lücke: machbar

## HEFT 11 Eigenhalbleiter und Dotierung

### Kurzbilanz Heft 11
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Welche Stoffe Halbleiter sind | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Der reine Kristall | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05 Fremdatome im Gitter | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Warum die Bindung so schwach ist | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Besetzung und Ladungsneutralität | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 08 Hohe und mittlere Temperaturen | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 09 Tiefe Temperaturen, Lage von E_F | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 10 Hohe Dotierstoffdichten | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Kein Artikel über dem Soll.

### V24 [A] Was ein Elektron kostet: Paar, Donator, Akzeptor (Überblick)
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/01-eigenhalbleiter-und-dotierung.md
- **Stelle:** Worum es geht — „Der Weg führt über acht Begriffe. Ein Halbleiter ist ein Kristall, dessen Bandlücke so klein ist …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Banddiagramm (Energie senkrecht, maßstäblich für Silizium bei 300 K): Leitungsband oben (E_C), Valenzband unten (E_V), Lücke E_g = 1,12 eV; Donatorniveau 45 meV unter E_C (Punkte mit Elektron), Akzeptorniveau 45 meV über E_V (leere Plätze). Drei Pfeile mit Energieangabe: Wärme k_BT = 26 meV als kurzer Pfeil.
- **Ablauf:** 1. Bänder, Donator- und Akzeptorniveau erscheinen (FadeIn), Begriffe daneben. 2. Ein Elektron springt vom Valenzband ins Leitungsband (Pfeil 1,12 eV, groß, sehr selten): es entsteht ein Paar, Beschriftung „Eigenleitung: Elektron und Loch zugleich“. 3. Ein Elektron löst sich vom Donator (Pfeil 45 meV, klein): nur ein Elektron, zurück bleibt ein ortsfestes +. 4. Ein Elektron aus dem Valenzband fällt auf den Akzeptor (Pfeil 45 meV): nur ein Loch, zurück bleibt ein ortsfestes -. 5. Der Wärmepfeil 26 meV daneben als Maßstab. — Haltepunkte: 2 und 3.
- **Verständnisproblem:** Acht Begriffe in einem Absatz; dass Fremdatome Träger fast kostenlos liefern, ein Paar aber 1,12 eV kostet, ist die Grundidee des Kapitels und im Überblick nicht zu sehen.
- **Szenenname:** gemb1/k11ueberblick
- **Editor-Lücke:** machbar (Elektronensprünge per MoveAlongPath)

### V25 [A] Plätze mal Besetzung wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Von Grund auf — „Dichten (Teil 10). Ein Platz ist mit der Wahrscheinlichkeit f(E) … besetzt …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k10dichte (D(E), f und 1-f, Produkt am Rand, Fläche n).
- **Ablauf:** 1. D(E) wächst als Wurzel, 2. f fällt exponentiell, 3. Produkt mit der Fläche n. — Haltepunkt: 3.
- **Verständnisproblem:** Gleichung (0.1) wird als Formel wiederholt; das ganze Kapitel baut darauf, das Bild des Produkts fehlt.
- **Szenenname:** gemb1/k10dichte (vorhanden)
- **Editor-Lücke:** machbar

### V26 [A] Generation und Rekombination im Kristall
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/04-der-reine-kristall.md
- **Stelle:** Der reine Kristall — „Die Idee. Wärme hebt laufend Elektronen aus dem Valenz- ins Leitungsband, das heißt Generation. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Bindungsbild des Si-Kristalls (Quadratraster als Vereinfachung des Diamantgitters, jede Bindung zwei kleine Elektronen). Rechts das passende Banddiagramm (E_V, E_C, Lücke 1,12 eV). Pfeil „Wärme“ als Wellenlinie.
- **Ablauf:** 1. Wärme trifft eine Bindung: Ein Elektron löst sich, läuft frei durchs Gitter (MoveAlongPath), im Banddiagramm springt es von E_V nach E_C. Zurück bleibt ein offener Kreis (Loch). 2. Ein Nachbarelektron rückt in die Lücke, das Loch wandert (Shift). 3. Das freie Elektron trifft das Loch, fällt zurück, Energie als Zickzackpfeil ans Gitter (Rekombination), im Banddiagramm fällt es nach E_V. 4. Zwei Pfeile gleicher Länge „Generation = Rekombination“, danach n_i = 8,9·10^9 cm^-3, ein Paar auf 5,6·10^12 Atome. — Haltepunkte: 1 und 3. Lebensdauer τ_rec als mittlere Zeit zwischen 1 und 3.
- **Verständnisproblem:** „Dynamisches Gleichgewicht“ und „Elektronen und Löcher entstehen nur paarweise, also n = p“ sind der Ausgangspunkt von E_Fi und n_i, aber nur als Text da; k11ni zeigt nur das Ergebnis über der Temperatur.
- **Szenenname:** gemb1/k11paar
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Elektron und Loch verschwinden bei der Rekombination; Umgehung: das Elektron wandert ins Loch und beide färben sich grau)

### V27 [B] Der Donator hat drei Möglichkeiten: warum 2/3 statt 1/2
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/07-besetzung-und-ladungsneutralitat.md
- **Stelle:** Besetzung und Ladungsneutralität — „Herleitung: Woher die Faktoren kommen. Ein Platz im Band hat zwei Zustände, leer oder besetzt …“ (und Fragekasten „Bei E = E_F ist f = 1/2 …“)
- **Art:** neue Animation
- **Was zu sehen ist:** Oben: Ein Bandplatz mit zwei Kästchen (leer, besetzt) und ein Donatorplatz mit drei Kästchen (leer, besetzt mit Spin ↑, besetzt mit Spin ↓). Unten: Achse (E_F - E_D)/(k_BT) von -6 bis 6, zwei Kurven: f (blau, Platz im Band, bei 0 gleich 1/2) und f_D = 1/(1+½·exp((E_D-E_F)/(k_BT))) (orange, Anteil neutraler Donatoren, bei 0 gleich 2/3), beide Punkte markiert.
- **Ablauf:** 1. Bandplatz: zwei Möglichkeiten gleiches Gewicht → 1/2. 2. Donator: drei Möglichkeiten, die zwei besetzten zählen doppelt → 2:1 → 2/3. 3. Kurve f zeichnet sich, 4. Kurve f_D zeichnet sich, Markierung bei 0. — Haltepunkt: 2. (Ein zweites Elektron kommt nicht hinein, Coulomb-Abstoßung: so vermerken.)
- **Verständnisproblem:** Der Faktor 2 im Nenner der Störstellenbesetzung und die Zahl g_A erscheinen als Rechenregel; der Grund (Spin-Zählung) braucht ein Bild. Vorhandenes k11neutral zeigt nur die Ladungsbilanz.
- **Szenenname:** gemb1/k11donator
- **Editor-Lücke:** machbar

### V28 [A] Drei Temperaturbereiche im Banddiagramm
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/08-hohe-und-mittlere-temperaturen.md
- **Stelle:** Hohe und mittlere Temperaturen — „Die Idee. Abb. 6 zeigt die numerische Lösung. Bei hohen Temperaturen übertrifft die Paarbildung …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Banddiagramm (E_V, E_C, Donatorniveau 45 meV unter E_C, Fermi-Energie als waagerechte Linie) mit schematisch 10 Donatorpunkten (Anzahl nicht maßstäblich). Rechts ein kleiner Verlauf n über 1000/T (Si, N_D = 10^16 cm^-3) mit einer laufenden Marke; Bereiche I (rot), II (grün), III (blau), Grenzen 719 K und 95 K.
- **Ablauf:** 1. Start bei tiefer Temperatur (Bereich III, 40 K): fast alle Donatoren neutral, E_C - E_F = 32 meV, wenig Elektronen im Leitungsband. 2. Temperatur steigt, Marke wandert (MoveAlongPath), Elektronen heben sich von den Donatoren ins Leitungsband; E_F-Linie sinkt. 3. Bereich II (300 K): alle Donatoren leer (+), n = N_D = 10^16 cm^-3, E_C - E_F = 205 meV, n bleibt konstant, Plateau. 4. Bereich I (über 719 K): Elektronen aus dem Valenzband hinzu, Löcher erscheinen, n steigt wieder, E_F nähert sich der Mitte (E_Fi). — Haltepunkte: 1, 3 und 4. Vereinfachung kennzeichnen: Punktzahl schematisch, Lücke und Niveaus maßstäblich.
- **Verständnisproblem:** Warum n erst steigt, dann stehen bleibt und dann wieder steigt, und wie sich E_F dabei bewegt, ist aus der Kurve allein nicht abzulesen; die Bereiche sind das Hauptergebnis des Hefts.
- **Szenenname:** gemb1/k11stationen
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Temperatur als Parameter; Umgehung: drei Stationen mit Shift der E_F-Linie und Elektronen-Gruppen)

### V29 [B] Ausfrieren: die Donatoren fangen ihre Elektronen zurück
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/09-tiefe-temperaturen-und-die-lage-von.md
- **Stelle:** Tiefe Temperaturen und die Lage von E_F — „Die Idee. Unterhalb der Erschöpfung teilen sich die Donatoren in ionisierte und neutrale …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Raster 10×10 aus 100 Kreisen (Donatoren, schematisch), darüber ein Feld „Leitungsband“ mit freien Elektronen als Punkte; Zähler n/N_D. Vier Stationen aus dem Beispiel (Probe N_D = 10^16 cm^-3): 300 K: 100 %, 95 K: 62 %, 77 K: 36 %, 40 K: 1,2 %. Darunter die Reaktion D^0 ⇌ D^+ + e^-.
- **Ablauf:** 1. 300 K: alle Donatoren leer (rot +), 100 freie Elektronen im Band. 2. Temperatur sinkt auf 95 K: 38 Elektronen fallen auf Donatoren zurück (MoveTo), die Kreise werden neutral. 3. 77 K: weitere fallen zurück, 36 frei. 4. 40 K: nur noch ein bis zwei freie Elektronen. 5. Beschriftung: „Reserve“, K_1 = N_C/2·exp(-ΔE_D/k_BT). — Haltepunkt: 4.
- **Verständnisproblem:** „Reserve“ und „Ausfrieren“ als Prozess; die Steigung ΔE_D/2 statt ΔE_D bleibt Formel, das Bild zeigt wenigstens den Prozess. Über Soll nicht.
- **Szenenname:** gemb1/k11ausfrieren
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte; Umgehung: Gruppen von Punkten per Shift)

### V30 [A] Zusammenschau wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/11-eigenhalbleiter-und-dotierung/11-das-wichtigste.md
- **Stelle:** Die Antwort in drei Sätzen — „Die Neutralität bestimmt dann E_F und ergibt drei Bereiche …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k11bereiche (n und E_F über 1000/T mit den Bereichen I, II, III), animiert wie unter den vorhandenen Abbildungen.
- **Ablauf:** 1. Bereich III, 2. Bereich II (Plateau), 3. Bereich I (Eigenleitung). — Haltepunkt: 2.
- **Verständnisproblem:** Die Zusammenfassung nennt die Bereiche nur in Worten und in der Tabelle.
- **Szenenname:** gemb1/k11bereiche (vorhanden)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 11
- gemb1/k11material (03): animieren ja — Schritte: 1. Bindungsbild: Si, jedes Atom vier Bindungen mit je zwei Elektronen, 2. GaAs: Ga drei, As fünf Elektronen, 3. rechts Balken der Bandabstände wachsen, brauchbarer Bereich 0,1 bis 3 eV grün | Lücke: machbar
- gemb1/k11ni (04): animieren ja — Schritte: 1. Achsen 1000/T, n_i logarithmisch, 2. Kurve Ge, Si, GaAs nacheinander (Create), steiler bei größerer Lücke, 3. rechts E_g(T) | Lücke: machbar
- gemb1/k11dotierung (05): animieren ja — Schritte: 1. P ersetzt ein Si-Atom, vier Bindungen, 2. das fünfte Elektron löst sich und läuft weg (MoveAlongPath), ortsfestes +, 3. B nimmt ein Elektron aus der Nachbarbindung, Loch wandert, ortsfestes -, 4. rechts die Niveaus der Donatoren und Akzeptoren | Lücke: machbar
- gemb1/k11wasserstoff (06): animieren ja — Schritte: 1. Coulomb-Potential und Grundzustand von H, 2. Achsen skalieren (Energie 1/720, Radius 62-fach), Si-Modell, 3. graue Punkte der Gitterkonstanten | Lücke: machbar (Skalieren: Scale)
- gemb1/k11neutral (07): animieren ja — Schritte: 1. Zustandsdichte mit Donatorpfeil, 2. Kurven n, p, N_D^+ über der gedachten E_F, 3. Summe p + N_D^+ gestrichelt, 4. Schnittpunkt mit n markiert: dort liegt E_F | Lücke: machbar
- gemb1/k11bereiche (08): animieren ja — Schritte: 1. Achsen, 2. n über 1000/T zeichnet sich von links nach rechts (Create), Bereiche I, II, III nacheinander eingefärbt, 3. unten E_F, 4. Grenzen 719 K und 95 K | Lücke: machbar
- gemb1/k11fermi (09): animieren ja — Schritte: 1. N_D von 10^14, 10^16, 10^18, 2. E_F-Kurven (blau, n-Typ) laufen von hoher Temperatur zu tiefer, 3. in die Mitte zwischen Kante und Niveau, 4. rote Kurven (p-Typ) | Lücke: machbar
- gemb1/k11hoch (10): animieren ja — Schritte: 1. Donatoren mit Bahnen bei 10^17 cm^-3, scharfes Niveau, 2. Dichte steigt auf 10^18: Bahnen nähern sich, Band entsteht, 3. 10^19: Verschmelzung mit dem Leitungsband, Lücke E_g^eff, E_F im Band | Lücke: machbar (Dichte als Sweep: L3)

## HEFT 12 Strom im Halbleiter

### Kurzbilanz Heft 12
| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---|---|---|---|---|---|---|
| 01 Überblick | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02 Von Grund auf | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 03 Strom aus besetzten Zuständen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 04 Ohne Stöße kein Gleichstrom | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05 Vom Wellenpaket zur Verteilungsfunktion | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06 Was das Gleichgewicht verlangt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07 Der Streuterm und die Relaxationszeit | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08 Der stationäre Strom | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 09 Beweglichkeit und Leitfähigkeit | 2 | 1 | 0 | 1 | 0 | 0 | 2 |
| 10 Ergänzung: Der Hall-Effekt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 11 Das Wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Kein Artikel über dem Soll. Hinweis: Der Drift-Zickzack im Realraum (Elektron stößt, wird beschleunigt) steht schon als gemb1/k1drude in Heft 01; hier nicht neu gezeichnet.

### V31 [A] Strom ist eine Schieflage der Besetzung (Überblick, Szene wiederverwenden)
- **Artikel:** content/gemb1/12-strom-im-halbleiter/01-strom-im-halbleiter.md
- **Stelle:** Worum es geht — „Ein Stück Silizium liegt an einer Spannung, und es fließt Strom. … Wie wird aus besetzten Zuständen ein Strom …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k12besetzung (Kosinus-Band mit wenigen Plätzen, links symmetrisch j = 0, rechts um zwei Plätze verschoben, j < 0).
- **Ablauf:** 1. symmetrische Besetzung, Geschwindigkeiten ± heben sich auf, 2. Feld schaltet ein, die Besetzung rutscht um zwei Plätze (Shift), 3. Beschriftung „mehr Elektronen bei v > 0: Strom“. — Haltepunkt: 2. Als Vereinfachung kennzeichnen: wenige Plätze, übertriebene Verschiebung.
- **Verständnisproblem:** Die Leitfrage „wie wird aus besetzten Zuständen ein Strom?“ ist die Idee des Kapitels; achtmal Fachbegriffe, aber kein Bild der Grundidee.
- **Szenenname:** gemb1/k12besetzung (vorhanden)
- **Editor-Lücke:** machbar

### V32 [A] Gasmodell der Leitung wiederverwenden (Von grund auf)
- **Artikel:** content/gemb1/12-strom-im-halbleiter/02-von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.md
- **Stelle:** Von Grund auf — „Teil 1. Es gilt j = σ𝓔. Das Gasmodell (Drude-Modell) lässt Elektronen nach der Zeit τ stoßen …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k1drude (Weg eines Elektrons zwischen Atomrümpfen, ohne und mit Feld).
- **Ablauf:** 1. ohne Feld: Zickzack ohne Ziel, 2. mit Feld: kleine Verschiebung je Stoß (roter Pfeil). — Haltepunkt: 2.
- **Verständnisproblem:** Der Rückblick fasst Drude in einem Satz; das Kapitel stellt das Modell um (Stoßpartner sind nicht die Rümpfe), der Leser braucht das Ausgangsbild.
- **Szenenname:** gemb1/k1drude (vorhanden)
- **Editor-Lücke:** machbar

### V33 [B] Warum Ionen bei Wärme weniger streuen, Phononen mehr
- **Artikel:** content/gemb1/12-strom-im-halbleiter/09-beweglichkeit-und-leitfahigkeit.md
- **Stelle:** Beweglichkeit und Leitfähigkeit — „Die Idee. Wärme erzeugt mehr Phononen und macht die Träger schneller, beides verkürzt die Zeit … An geladenen Störstellen wirkt sie umgekehrt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links: ein ortsfestes Ion (rot, +) bei (0, 0) und zwei Elektronenbahnen aus demselben Stoßabstand b: eine langsame (stark abgelenkte, gebogene Bahn) und eine schnelle (fast gerade). Rechts: eine Atomreihe, oben bei tiefem T mit kleinen Schwingungsamplituden (Elektron läuft durch), unten bei hohem T mit großen Amplituden (Elektron wird abgelenkt). Beschriftung: Ablenkwinkel nimmt mit der Bewegungsenergie ab, Phononenzahl wächst mit T.
- **Ablauf:** 1. Ion und Beschriftung „Coulomb-Kraft“. 2. Das langsame Elektron fliegt ein (MoveAlongPath), wird stark abgelenkt. 3. Das schnelle fliegt auf derselben Linie ein, kaum abgelenkt: Wärme macht Ionenstreuung schwächer, μ_ion ∝ T^(+3/2). 4. Rechts: kalte Atomreihe, Elektron fliegt durch; 5. heiße Atomreihe schwingt stärker, Elektron wird abgelenkt: μ_ph ∝ T^(-3/2). — Haltepunkte: 3 und 5. Vereinfachung kennzeichnen: klassische Bahnen, qualitativ, Atomschwingung übertrieben.
- **Verständnisproblem:** Die gegenläufigen Exponenten und das Maximum der Beweglichkeit werden nur in einer kurzen Herleitung begründet; k12beweglichkeit zeigt die Kurven, nicht den Mechanismus.
- **Szenenname:** gemb1/k12streuarten
- **Editor-Lücke:** machbar (Schwingung der Atome als Hin-und-Her-Shift; saubere Bahnen per MoveAlongPath auf ParametricCurve)

### V34 [A] Schub gegen Abbau wiederverwenden (Das Wichtigste)
- **Artikel:** content/gemb1/12-strom-im-halbleiter/11-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Eine Kraft baut eine Abweichung vom Gleichgewicht auf, Stöße bauen sie ab. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** gemb1/k12verschoben (Gleichgewichtsverteilung gestrichelt, stationäre verschobene Verteilung, darunter die Abweichung f - f^0), animiert wie unter den vorhandenen Abbildungen.
- **Ablauf:** 1. f^0 gestrichelt, 2. Feld schiebt (Pfeil F/ħ), 3. Stöße ziehen zurück (Pfeil 1/τ), 4. stationäre Verschiebung δk. — Haltepunkt: 3.
- **Verständnisproblem:** Das Prinzip „Schub gegen Abbau“ steht in einem Satz.
- **Szenenname:** gemb1/k12verschoben (vorhanden)
- **Editor-Lücke:** machbar

### Vorhandene Abbildungen Heft 12
- gemb1/k12besetzung (03): animieren ja — Schritte: 1. symmetrische Besetzung im Leitungs- und Valenzband, j = 0, 2. Feld, alle Plätze rutschen um δk (Shift), 3. Elektronen bei v > 0 und fehlende Elektronen bei v < 0 geben beide j < 0 | Lücke: machbar
- gemb1/k12bloch (04): animieren ja — Schritte: 1. ohne Stöße: k läuft, springt am Zonenrand von π/a nach -π/a, v pendelt (Punkt auf Kurve), 2. mit Stößen: Sägezahn, jeder Stoß setzt k zurück, 3. mittlere Verschiebung F·τ/ħ | Lücke: machbar (Punkt mit mitlaufender Marke: L3)
- gemb1/k12phasenraum (05): animieren ja — Schritte: 1. Wellenpaket mit Hülle, 2. daneben Kästchen in der x-k-Ebene, 3. Kästchen wandert längs der Bahn (Shift in x durch v, in k durch F/ħ), 4. Rückblick: was bei (x, k) sitzt, saß vorher bei (x - v dt, k - F dt/ħ) | Lücke: machbar
- gemb1/k12gleichgewicht (06): animieren ja — Schritte: 1. links: Dotierung fällt von 10^17 auf 10^15 cm^-3, Bandkante steigt, Elektronen (Punkte) verteilen sich, E_F bleibt waagerecht, 2. Pfeile Drift und Diffusion gleich lang, entgegengesetzt, 3. rechts: homogen, 100 mV, E_F neigt sich, Strom fließt | Lücke: machbar
- gemb1/k12streuung (07): animieren ja — Schritte: 1. Zustand k, Zufluss und Abfluss als Pfeile, 2. Abweichung δf zeichnet sich als Abfall e^(-t/τ) (Create), 3. Gesamtkurve unter den Einzelkurven (Matthiessen) | Lücke: machbar
- gemb1/k12verschoben (08): animieren ja — Schritte: 1. f^0 (gestrichelt), 2. Feld schaltet ein, f verschiebt sich (Shift) um δk, 3. Stöße ziehen zurück, Verschiebung bleibt stehen, 4. unten die Abweichung f - f^0; Metall: nur die Fermi-Kanten ±k_F | Lücke: machbar (Aufbau über die Zeit: L3)
- gemb1/k12beweglichkeit (09): animieren ja — Schritte: 1. μ_n über T für drei Dotierungen zeichnen sich nacheinander, gestrichelt Phononen- und Ionenanteil für 10^16 cm^-3, 2. daneben μ über der Dotierung, 3. unten σ über 1000/T mit Bereichen I, II, III, 4. ρ bei 300 K. Mehr als vier Teilbilder: beim Animieren in zwei Szenen teilen (μ; σ) | Lücke: machbar
- gemb1/k12hall (10): animieren ja — Schritte: 1. Platte mit Stromrichtung, B aus der Bildebene, 2. Elektronen laufen (MoveAlongPath), Lorentz-Kraft lenkt sie nach unten, 3. Randladungen sammeln sich, das Feld E_H wächst (Pfeil), 4. Gleichgewicht: Kräfte heben sich auf, U_H; rechts |R_H| von Silizium mit Nulldurchgang bei 1000/T = 1,53 | Lücke: machbar (viele Elektronen: L6)
