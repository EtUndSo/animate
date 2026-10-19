# Editor-Features für die Wissens-Grafiken

Lebende Liste: Welche Fähigkeiten braucht der EtUndSo-Editor, damit sich **alle** in den Artikeln
beschriebenen Grafik-Platzhalter (`:::grafik`) als echte, einheitlich gestaltete Abbildungen (und teils
Animationen) erzeugen lassen? Entstanden beim Schreiben der GET1-Artikel; wird mit jedem weiteren Modul ergänzt.

Legende Priorität: **P1** = ohne das geht fast keine ET-Grafik · **P2** = häufig gebraucht · **P3** = punktuell.

---

## 1. Schaltplan-Editor / Schaltsymbol-Bibliothek  — **P1 (wichtigstes fehlendes Feature)** — IN ARBEIT
Fast jede GET1-Grafik ist ein Schaltbild. Ziel: Schemata elektrischer Schaltungen nachbauen wie im
ET1-Skript — **Rechteck für Widerstand, Dreieck mit Strich für Diode**, usw. (User 2026-10-19).

**Symbol-Set (wie circuitikz / ET1-Skript):**
- Widerstand (Rechteck), Potentiometer; Kondensator (zwei Platten); Spule; Quelle (Spannungs-/Stromquelle,
  ideal/real, Kreis mit +/− bzw. Pfeil); Masse/Bezugsknoten.
- Diode (Dreieck + Strich) und Varianten (Z-Diode, LED, Schottky, Photodiode); Bipolartransistor npn/pnp;
  Operationsverstärker (Dreieck, +/−); Messgeräte (Kreis „A"/„V"/„G"); Schalter; Klemmen/Knotenpunkte.
- Beschriftung je Bauteil ($R_1$, $U_0$ …) über das vorhandene MathTex.

**Verdrahtung + Linien-Winkelraster (User 2026-10-19):**
- Leitungen zwischen Bauteilen/Knoten; Knotenpunkt (Lötpunkt) vs. Kreuzung ohne Verbindung.
- **Einstellbar: automatische Ausrichtung der Geraden auf horizontal / vertikal / 45°.**
  **Standard: AN** (Linien rasten auf 0°/45°/90°), **kann ausgeschaltet werden** (dann freie Winkel).

**Grid + Clipping (User 2026-10-19):**
- **Einstellbar: ob ein darunterliegendes Grid angezeigt wird** und ob es **mit Clipping/Snap** genutzt wird
  (Bauteile/Linienenden rasten auf Gitterpunkte). Ein/aus schaltbar.

Referenz: circuitikz-Umfang, ET1-Skript-Optik. Umsetzung als neues Objekt-/Werkzeug-Set (SVG-Symbole +
Verdrahtungs-/Snap-Logik). Gebraucht in: praktisch allen Kapiteln 4–12.
**→ Wird aktuell parallel in einem eigenen Worktree gebaut.**

## 2. Beschriftete Pfeile / Vektoren (Zählpfeile, Kräfte, Felder)  — **P1**
- Gerade **Pfeile mit Label** (Strom-, Spannungs-, Kraft-, Feldstärkepfeile) frei platzierbar.
- Doppelpfeile (Maß-/Abstandspfeile, z. B. $d$, $r$), gebogene Umlaufpfeile (Maschenumlauf, Rückkopplung).
- Pfeilpaare für actio=reactio; Vorzeichen-/Richtungsumkehr-Darstellung.
Gebraucht in: Coulombkraft, Feldstärke, Zählpfeile/VZS-EZS, Kirchhoff-Maschen, Transistor-/OPV-Rückkopplung.

## 3. Feldlinien & Vektorfelder  — **P2**
- Radiale Feldlinien (Punktladung ±), parallele Feldlinien (Plattenkondensator, mit Randfeld-Option).
- Äquipotentiallinien (senkrecht zu Feldlinien), Dichte = Feldstärke.
- Allgemeines Vektorfeld (Pfeilgitter) für Stromdichte $\vec J$.
Gebraucht in: Feld/Feldstärke, Potenzial/Äquipotential, Stromdichte, pn-Übergang.

## 4. Erweiterte Funktions-/Kennliniengrafiken  — **P1**
Der Editor kann Funktionsgraphen; es fehlen:
- **Mehrere Kurven** in einem Achsensystem + Legende (Kennlinienscharen, z. B. Transistor-Ausgangskennlinienfeld mit $I_B$-Scharen).
- **Fläche unter/zwischen Kurven schraffieren** (Energie = Dreieck unter $Q$-$U$; Integral).
- **Gerade ins Kennlinienfeld legen** (Arbeits-/Lastgerade) und **Schnittpunkt markieren** (Arbeitspunkt).
- **Tangente im Punkt** (differentieller Widerstand / Kleinsignal-Linearisierung).
- Achsen frei beschriften mit Einheiten; markierte Punkte mit Koordinaten/Labels; Bereiche farbig hinterlegen (Sperr-/aktiver/Sättigungsbereich).
- **Doppeltlogarithmische Achsen** (OPV: Verstärkung über Frequenz, GBW).
Gebraucht in: Diode, Arbeitspunkt, Transistor-Kennlinienfeld, OPV-GBW, Energie im Kondensator.

## 5. Zeitverläufe / Signalformen (Waveforms)  — **P2**
- Sinus und abgeleitete Formen; **stückweise/abgeschnittene** Signale (Einweg-/Brückengleichrichtung).
- Überlagerung geglättet + Welligkeit (Brummspannung), Rampe (Slew Rate), Rechteck-Sprungantwort.
- Lade-/Entladekurven (e-Funktion) mit markierter Zeitkonstante τ.
Gebraucht in: RC-Laden/Entladen, Gleichrichtung, OPV-Slew-Rate.

## 6. Mikrostruktur-/Material-Diagramme  — **P2**
- **Bändermodell**: gefüllte/leere Energiebänder als Balken, Bandlücke, Elektron (Punkt) / Loch (Kreis), Übergang über die Lücke.
- **Kristallgitter**: Atome als Kreise im Raster mit Bindungen; Dotieratome (Donator/Akzeptor) hervorgehoben; freie Ladungsträger.
- **pn-Übergang**: zwei Gebiete, Raumladungszone, ortsfeste Ionen, Feldpfeil, Ladungsträgerbewegung.
Gebraucht in: Halbleiter/Bändermodell, Diode.

## 7. Hervorhebungen, Labels, Container  — **P2**
- Textlabels mit LaTeX/Formelsatz an beliebiger Stelle (nutzt vorhandenes MathTex).
- Geschweifte Klammern (brace) zum Zusammenfassen; Callout-/Sprechblasen; farbige Markierungsrahmen/Flächen.
- „Black Box"/beschriftete Rechtecke (Zweitor, Ersatzschaltbild-Rahmen); Tabellen-/Matrix-Darstellung mit hervorgehobenen Einträgen (Widerstands-/Leitwertmatrix).
- Durchstreichen / rotes Kreuz (Falschbeispiele), Haken (richtig).

## 8. Animationen  — **P2/P3** (Editor kann seek(t); Inhalte fehlen)
- Elektronen-Drift (viel Zittern, kleine Nettobewegung); Stromfluss entlang Leitungen.
- Kondensator laden/entladen (Füllstand + Kurve synchron); AC-Halbwellen durch Gleichrichter.
- **Rotierender Zeiger / Phasor in der komplexen Ebene** (→ MMET/Wechselstrom, sehr wahrscheinlich bald gebraucht).
- Arbeitspunkt wandert bei Parameteränderung; Signal „reitet" auf Kennlinie (Kleinsignal).

---

## Für kommende Module absehbar
- **MMET / Signalverarbeitung**: komplexe Ebene + Zeiger/Phasoren (animiert), Ortskurven, Spektren/Balkendiagramme (Fourier), Faltung, Pol-Nullstellen-Diagramme, 3D-Betragsflächen komplexer Funktionen.
- **HM1 / Mathe**: allg. Funktionsplots (hat der Editor), Vektorgeometrie, Grenzwert-/Folgen-Darstellungen, Flächen/Volumina.
- **Physik I**: Mechanik-Vektoren, Bewegungsdiagramme, Schwingungen/Wellen.
- **GdI1 / Informatik**: Graphen/Bäume, Automaten, Zeitdiagramme — eher kein Editor-Fall, evtl. eigenes Diagramm-Tooling.

## Vorgehensvorschlag (Priorisierung)
1. **Schaltplan-Bibliothek + Verdrahtung** (P1) — schaltet die meisten GET1-Grafiken frei.
2. **Beschriftete Pfeile/Vektoren** (P1) und **erweiterte Kennliniengrafiken** (P1).
3. Feldlinien, Waveforms, Material-Diagramme (P2).
4. Animations-Bausteine zuletzt.

---

## 9. Templates + Figur-Verweise  — **P2** (Zukunftsplan, User 2026-10-19)
Die Szenen, mit denen die Grafiken/Animationen erzeugt werden, als **Templates im Editor** bereitstellen. Jede
Abbildung im Artikel bekommt einen **anklickbaren Link zum zugehörigen Template** (Klick → öffnet die Szene im
Editor).
- **Nummerierung statt Baum:** Im Editor ist wenig Platz für eine grafische Baumstruktur → Templates einfach
  **durchnummerieren**, aber in **sinnvoller Reihenfolge**: Templates desselben Moduls hintereinander (modulweise
  gruppiert, fortlaufende Nummern).
- **Umnummerierbar halten:** Die Nummerierung wird später vermutlich mehrfach angepasst → Template-Referenz
  flexibel/indirekt (nicht hart verdrahten), damit Umnummerieren leicht bleibt.
- Greift erst, wenn der Editor echte Grafiken/Templates erzeugt; bis dahin `:::grafik`-Platzhalter mit
  Bildbeschreibung. Später: im Build je `:::grafik` optional ein Template-Link/-Nummer-Feld.
