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
- **Signalprojektion über eine Kennlinie** (neu 2026-10-21): Eingangssinus unterhalb der x-Achse, Antwort rechts neben der y-Achse, Hilfslinien zeigen die Abbildung Punkt für Punkt; dazu die Tangente zum Vergleich.
Gebraucht in: RC-Laden/Entladen, Gleichrichtung, OPV-Slew-Rate; Transistor als Verstärker (get1/bipolartransistoren/03-verstaerkerstufe, 03-tangente, 03-emitterwiderstand, 03-stabilisierung).

## 6. Mikrostruktur-/Material-Diagramme  — **P2**
- **Bändermodell**: gefüllte/leere Energiebänder als Balken, Bandlücke, Elektron (Punkt) / Loch (Kreis), Übergang über die Lücke.
- **Kristallgitter**: Atome als Kreise im Raster mit Bindungen; Dotieratome (Donator/Akzeptor) hervorgehoben; freie Ladungsträger.
- **pn-Übergang**: zwei Gebiete, Raumladungszone, ortsfeste Ionen, Feldpfeil, Ladungsträgerbewegung.
Gebraucht in: Halbleiter/Bändermodell, Diode, Bipolartransistor (Querschnitt mit drei Gebieten und zwei Zonen, Schichtfolge mit Dotierungsbalken).

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

---

## Ergänzungen aus den Stil-3-Artikeln (ab 2026-10-21)

Seit dem 21.10.2026 gilt: In den Artikeln stehen **nur noch Editor-Abbildungen** (User). Jede geplante Abbildung
ist mit Inhalt, Daten und benötigten Funktionen in `ABBILDUNGEN_LISTE.md` erfasst. Die Features werden **nach**
dem Schreiben der Artikel gebaut, nicht im Loop. Die folgenden Abschnitte ergänzen §1–§9 um das, was der
Halbleiter-Pilot zusätzlich braucht.

## 10. Teilbild-Layout  — **P1**
- Mehrere Teilbilder (a), (b), … in einer Abbildung, nebeneinander oder untereinander, auch gemischt
  (drei kleine oben, eines breit darunter).
- Gemeinsame Bildunterschrift; Teilbild-Buchstaben automatisch; Achsen optional gekoppelt.
Gebraucht in: fast jeder Stil-3-Abbildung (Halbleiter-Pilot: Gesamtbild, Kristallgitter, Fermi-Verteilung,
Bänder bei Spannung, Gleichrichter).

## 11. Datenkurven aus dem Zahlenwerk  — **P1**
- Kurven aus einer **Datentabelle** (CSV/JSON) statt nur aus einer Formel: numerisch gelöste Profile
  (Poisson-Lösung am pn-Übergang), implizit gelöste Größen (Gleichrichter-Ausgang über die Shockley-Gleichung).
- Die Tabelle wird vom Zahlenwerk des Oberthemas erzeugt (`notizen/<modul>/zahlen_<oberthema>.py`), damit
  Abbildung und Text dieselben Zahlen zeigen.
Gebraucht in: Gesamtbild (d), Gleichgewichts-Profile, Gleichrichter, Bänder bei Spannung.

## 12. Halblogarithmische Achsen  — **P1**
- Logarithmische y-Achse mit Zehnerpotenz-Beschriftung (10⁵ … 10¹⁸), x linear; Hilfslinien bei Zehnerpotenzen.
- Ergänzt §4, das bisher nur doppeltlogarithmische Achsen nennt.
- Ebenso logarithmische x-Achse bei linearer y-Achse (Widerstand von 50 kΩ bis 2 MΩ).
Gebraucht in: Dichten über dem Ort, n_i(T), Fermi-Ausläufer, Diodenstrom über U (Teilströme), Spannungsgegenkopplung über $R_B$.

## 13. Gestapelte Diagramme mit gemeinsamer x-Achse  — **P2**
- Mehrere Größen über demselben Ort übereinander (Dichte, Raumladung, Feld, Potenzial, Bänder), nur unten
  beschriftete x-Achse.
- **Eine Hinterlegung, die durch alle Teilbilder geht** (Raumladungszone).
Gebraucht in: Gleichgewichts-Profile am pn-Übergang; später Transistor (Profile in Emitter/Basis/Kollektor); Spannungsgegenkopplung, Strom und $U_{CE}$ über $R_B$ (get1/bipolartransistoren/02-spannungsgk-kompromiss).

## 14. Teilchenwolken  — **P2**
- Viele Punkte/Kreise, zufällig nach einer Verteilung gesetzt (exponentiell in der Energie über einer Bandkante,
  gleichverteilt im Ort); fester Zufallsstartwert, damit die Abbildung reproduzierbar ist.
- Hervorhebung nach Bedingung („Energie über der Barriere“) in eigener Farbe.
- Animierbar: Zufallsbewegung, Zähler für übergewechselte Teilchen.
Gebraucht in: „hinauf und hinunter“ (Diffusion gegen Drift), später Diodenstrom, Transistor-Basis.

## 15. Parameter-Schieberegler  — **P2**
- Ein Parameter (Diodenspannung U, Temperatur T) wird live verändert; abhängige Kurven, Maßpfeile und
  Beschriftungen (Barrierenhöhe, Faktoren wie ×2,5·10⁸) werden neu berechnet.
- Für die statische Abbildung: feste Stützwerte als Teilbilder (§10).
Gebraucht in: Bänder bei Spannung, Fermi-Verteilung (T), später Kennlinie und Arbeitspunkt.

## 16. Bänderschema mit Zusatzniveaus  — **P2** (Ausbau von §6)
- Kurze Strichniveaus für Donator/Akzeptor ($W_D$, $W_A$), gepunktetes Eigenleitungsniveau $W_i$,
  gestricheltes Fermi-Niveau $W_F$, Maßpfeile zwischen Niveaus mit Zahlenwert.
- Bänder auf **echter Energieachse** (Metall/Halbleiter/Isolator maßstäblich) oder als **Verlauf über dem Ort**
  (Bandverbiegung aus Datentabelle, §11).
- Kristallgitter (§6) mit einzeln ausblendbaren Bindungen (Loch) und hervorgehobenen Dotieratomen.
Gebraucht in: Gesamtbild, Leiter/Halbleiter/Isolator, dotierte Bänder, Kristallgitter, Loch-Wanderung.

## 17. Achsenbruch und abschnittsweiser Maßstab  — **P2** (neu 2026-10-21, Diode)
- Eine Achse mit sichtbarem Bruch bzw. getrennten Maßstäben je Abschnitt, z. B. Strom in mA oberhalb und in pA unterhalb der Nulllinie, Spannung in 0,1 V rechts und in 10 V links.
- Die Beschriftung macht die Maßstabswechsel unübersehbar.
Gebraucht in: Gesamtkennlinie der Diode (Durchlass, Sperr, Durchbruch); später Transistor-Kennlinienfelder mit Sperrbereich; Ausgangskennlinien bis zur Early-Spannung −70 V (get1/bipolartransistoren/03-reale-kennlinien).

## 18. Mengenpfeile und Bilanzdiagramme  — **P2** (neu 2026-10-21, Bipolartransistor)
- Pfeile, deren Breite proportional zu einem Wert ist (Ströme, Teilchenflüsse), mit der Zahl am Pfeil; Verzweigen und Zusammenführen wie in einem Sankey-Diagramm.
- Sehr ungleiche Flüsse (10 000 gegen 12,5) mit gekennzeichneter Lupe bzw. eigenem Maßstab für die kleinen Pfeile.
Gebraucht in: Stromaufteilung und Trägerflüsse im Bipolartransistor, aktiv und gesättigt (get1/bipolartransistoren/01-…).

## 19. Wirkungsketten und Blockbilder  — **P2** (neu 2026-10-21, Arbeitspunkt)
- Kästen mit Text und Formeln, verbunden durch Pfeile; Anordnung als Kette oder als geschlossener Kreis, Pfeile folgen der Anordnung automatisch.
- Vorzeichen oder Symbole an Pfeilen und Kästen (+/−, steigt/sinkt), damit Mit- und Gegenkopplung unterscheidbar sind; Auslöser als Kasten außerhalb des Kreises.
Gebraucht in: Stromgegenkopplung (get1/bipolartransistoren/02-gegenkopplung-kette); Signalweg der Verstärkerstufe (03-signalweg); absehbar Gegenkopplung beim Operationsverstärker und Regelkreise.

## Vorgehensvorschlag nach den Artikeln (Stand 2026-10-21)
1. Teilbild-Layout, Datenkurven, halblogarithmische Achsen (§10–§12) zusammen mit §4: schalten die meisten
   Kennlinien- und Profil-Abbildungen frei.
2. Bänderschema/Kristallgitter/pn-Übergang (§6, §16) und Pfeile (§2).
3. Gestapelte Diagramme, Teilchenwolken, Schieberegler (§13–§15), Animationen (§8) zuletzt.
