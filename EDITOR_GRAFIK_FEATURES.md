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
Gebraucht in: Diode, Arbeitspunkt, Transistor-Kennlinienfeld, OPV-GBW (get1/operationsverstaerker/03-frequenzgang), Energie im Kondensator.

## 5. Zeitverläufe / Signalformen (Waveforms)  — **P2**
- Sinus und abgeleitete Formen; **stückweise/abgeschnittene** Signale (Einweg-/Brückengleichrichtung).
- Überlagerung geglättet + Welligkeit (Brummspannung), Rampe (Slew Rate), Rechteck-Sprungantwort.
- Lade-/Entladekurven (e-Funktion) mit markierter Zeitkonstante τ.
- **Signalprojektion über eine Kennlinie** (neu 2026-10-21): Eingangssinus unterhalb der x-Achse, Antwort rechts neben der y-Achse, Hilfslinien zeigen die Abbildung Punkt für Punkt; dazu die Tangente zum Vergleich.
Gebraucht in: RC-Laden/Entladen, Gleichrichtung, OPV-Slew-Rate (get1/operationsverstaerker/03-anstieg); Transistor als Verstärker (get1/bipolartransistoren/03-verstaerkerstufe, 03-tangente, 03-emitterwiderstand, 03-stabilisierung).

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
Gebraucht in: Dichten über dem Ort, n_i(T), Fermi-Ausläufer, Diodenstrom über U (Teilströme), Spannungsgegenkopplung über $R_B$, Transferkennlinien zweier Transistoren beim Offset (get1/operationsverstaerker/03-offset).

## 13. Gestapelte Diagramme mit gemeinsamer x-Achse  — **P2**
- Mehrere Größen über demselben Ort übereinander (Dichte, Raumladung, Feld, Potenzial, Bänder), nur unten
  beschriftete x-Achse.
- **Eine Hinterlegung, die durch alle Teilbilder geht** (Raumladungszone).
Gebraucht in: Gleichgewichts-Profile am pn-Übergang; später Transistor (Profile in Emitter/Basis/Kollektor); Spannungsgegenkopplung, Strom und $U_{CE}$ über $R_B$ (get1/bipolartransistoren/02-spannungsgk-kompromiss); Ort, Geschwindigkeit und Beschleunigung über der Zeit (get1/grundprinzipien/01-kinematik).

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
- Entscheidungsrauten mit beschrifteten Ausgängen (ja/nein), verzweigte und wieder zusammenlaufende Abläufe (Rechenschema für OPV-Schaltungen).
Gebraucht in: Stromgegenkopplung (get1/bipolartransistoren/02-gegenkopplung-kette); Signalweg der Verstärkerstufe (03-signalweg); Gegen- und Mitkopplung beim Operationsverstärker (get1/operationsverstaerker/01-gegen-mit); Messkette mit Pegeln (01-messkette); Rechenschema und Multiplizierer (02-rechenschema, 02-multiplizierer); Stammbaum der Einheiten und definierende Konstanten (get1/grundprinzipien/01-einheitenbaum, 01-si-konstanten); Ablauf der Transientenanalyse mit zwei Schleifen (st1/netzwerkanalyse/04-spice-ablauf); Signalkette aus Zweitoren (05-signalkette); absehbar Regelkreise.


## 20. Hystereseschleifen  — **P2** (neu 2026-10-22, Operationsverstärker)
- Kennlinie mit zwei Ästen, die je nach Laufrichtung gelten; senkrechte Sprünge an den Schwellen; Pfeile auf Ästen und Sprüngen.
- Instabile Zwischenlösungen gestrichelt; Schwellen und Hysteresebreite als Maßpfeile.
- Animierbar: ein Punkt folgt einer vorgegebenen Eingangsspannung hin und zurück und springt an den Schwellen.
Gebraucht in: Schmitt-Trigger (get1/operationsverstaerker/01-schmitt-kennlinie); absehbar Magnetisierungskurven (Ferromagnetismus).

## 21. Rausch- und Zufallssignale  — **P2** (neu 2026-10-22, Operationsverstärker)
- Zeitverläufe aus Zufallszahlen mit festem Startwert, vorgegebenem Effektivwert und begrenzter Bandbreite (weißes, gefiltertes und 1/f-Rauschen).
- Überlagerung mit deterministischen Signalen (Sinus plus Rauschen); Hilfslinien beim Effektivwert.
- Dazu die Rauschdichte über der Frequenz, doppelt logarithmisch (§4).
Gebraucht in: Rauschen eines Widerstands (get1/operationsverstaerker/01-rauschen), Komparator gegen Schmitt-Trigger (01-schmitt-rauschen).

## 22. Skalen, Bereichsbalken und Ausschnittvergrößerung  — **P2** (neu 2026-10-22, realer OPV)
- Eine einzelne Skala (Zahlenstrahl) mit zwei Beschriftungen derselben Größe, etwa Dezibel oben und Verhältnis unten (60 dB = 10³ bis 120 dB = 10⁶), mit Marken und hinterlegten Bereichen.
- Bereichsbalken an einer gemeinsamen Spannungsachse: mehrere senkrechte Balken nebeneinander (Versorgung, Ausgangsbereich mit und ohne Last, Eingangsbereich), Abstände als Maßpfeile.
- Ausschnittvergrößerung in einem Diagramm: Rahmen um einen kleinen Bereich, daneben vergrößert dargestellt und mit Linien verbunden, damit sehr kleine Abstände sichtbar werden (1 mV bei 0,6 V).
Gebraucht in: realer OPV (get1/operationsverstaerker/03-gleichtakt, 03-aussteuerung, 03-offset); logarithmische Stromskala mit Vorsätzen (get1/grundprinzipien/01-vorsaetze).

## 23. Mechanik-Skizzen  — **P2** (neu 2026-10-22, Größen und Einheiten)
- Einfache Körper (Kasten, Koffer, Schlitten) auf Unterlagen: waagrechter Boden, Treppe mit wählbarer Stufenzahl und Stufenhöhe, schiefe Ebene mit Winkel; Seil oder Schnur unter einem Winkel.
- Kraftpfeile am Körper, Länge proportional zum Betrag, mit Zerlegung in Anteile längs und senkrecht zum Weg (gestrichelt) und Winkelbogen mit Gradzahl.
- Wegstücke mit eigener Beschriftung (etwa „0 J“ waagrecht, „98,1 J“ senkrecht) und Summenzeile.
- Animierbar: Körper entlang eines Wegs bewegen, mit mitlaufendem Zähler.
Gebraucht in: Arbeit an Treppe, Rampe und Schlitten (get1/grundprinzipien/01-arbeit); absehbar Kraft auf Ladungen im Feld (ET1 Kap. 3) und Lorentzkraft.

## 24. Symbolbibliothek: Röhre, MOSFET und Funkblöcke  — **P1** (neu 2026-10-23, Schaltungstechnik Einführung)
- Elektronenröhren: Diode und Triode mit Heizfaden, Kathode, Gitter (gestrichelt) und Anode im Kreis bzw. Kolben; optional Schirmgitter (Tetrode).
- MOS-Feldeffekttransistoren: n- und p-Kanal (Anreicherung) mit Anschlüssen G, D, S, wahlweise mit Substratanschluss; Kreis am Gate für PMOS.
- Magnetisch gekoppelte Spulen mit Wicklungspunkten (Polung der Rückkopplung).
- Funkblöcke: Mischer (Kreis mit Kreuz), Oszillator (Kreis mit Sinus, wahlweise mit Pfeil „abstimmbar“), Filter (Kasten mit Tief-, Band- oder Hochpasssymbol), Verstärker (Dreieck), 90°-Phasenschieber, Analog-Digital-Umsetzer, Antenne, Lautsprecher, Summierstelle.
- Rahmen für eine Chipgrenze (gestrichelt), Bauteile innerhalb und außerhalb.
Gebraucht in: st1/einfuehrung/01-drei-ventile, 01-rueckkopplung, 01-ueberlagerung, 01-cmos-inverter, 01-direktumsetzer; absehbar in allen MOSFET-Themen der Schaltungstechnik.

## 25. Spektren  — **P2** (neu 2026-10-23, Schaltungstechnik Einführung)
- Frequenzachse (linear oder logarithmisch) mit Spektrallinien, deren Höhe die Amplitude angibt; Linien einzeln beschriftet und gefärbt.
- Hinterlegte Bänder (UKW-Band 87,5 bis 108 MHz), Abstandspfeile zwischen Linien mit Wert, gestrichelte Linien für unerwünschte Anteile.
- Überlagerte Filterkurven (Durchlassbereich) und Lupe auf einen schmalen Bereich (mit §22).
Gebraucht in: st1/einfuehrung/01-ueberlagerung; absehbar Modulation, Abtastung und Aliasing, Signale und Systeme.

## 26. Zeitleisten  — **P3** (neu 2026-10-23, Schaltungstechnik Einführung)
- Zeitachse mit Jahresmarken, Ereignissen (Punkt und kurzer Text, automatisch versetzt, damit sich Texte nicht überdecken) und Epochenbalken.
- Kopplung an darunterliegende Teilbilder (§10), etwa ein Schaltbild je Epoche.
Gebraucht in: st1/einfuehrung/01-drei-ventile.

## 27. Technologie-Querschnitte  — **P2** (neu 2026-10-23, Schaltungstechnik Einführung)
- Geschichtete Querschnitte durch Halbleiterbauelemente: Substrat, dotierte Gebiete mit Farbe nach Dotierart (n blau, p rot, n⁺/p⁺ kräftiger), Oxid, Polysilizium, Metall, Fotolack; Masken mit Öffnungen und Lichtpfeile.
- Prozessschritte als Folge von Teilbildern (Oxidieren, Belichten, Ätzen, Dotieren, Metallisieren), wahlweise als Animation.
- Maßpfeile für Längen ($L$, $t_\mathrm{ox}$), Feldpfeile, Skalierung eines ganzen Querschnitts mit einem Faktor bei gleich langen Pfeilen.
- Ebenso einfache Querschnitte von Röhren (Kathode, Gitterdrähte im Schnitt, Anode).
Gebraucht in: st1/einfuehrung/01-planartechnik, 01-skalierung, 01-triode-aufbau; absehbar MOSFET-Aufbau, Latch-Up und parasitäre Kapazitäten.

## 28. Gesteuerte Quellen, nichtlineare Zweipole und Kleinsignal-Ersatzschaltbilder  — **P1** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Gesteuerte Quellen als Raute: spannungs- und stromgesteuerte Strom- und Spannungsquelle; Beschriftung mit dem Steuerausdruck ($g\,u$, $\beta\,i_B$, $v\,u_1$) und gestrichelte Zuordnung zur Steuergröße (Spannungspfeil oder Strompfeil an anderer Stelle der Schaltung).
- Nichtlinearer Zweipol: Widerstandsrechteck mit schräger, geknickter Linie, beschriftet mit der Kennlinienfunktion; ebenso nichtlineare Kapazität.
- Gegenüberstellung Großsignal- und Kleinsignal-Ersatzschaltbild: dieselbe Anordnung in zwei Teilbildern (§10), Bauteile paarweise farbig gekoppelt; Gleichspannungsquelle wird zum Kurzschluss, Gleichstromquelle zur Unterbrechung, wahlweise als Animation (§8).
Gebraucht in: st1/netzwerkanalyse/01-ersatzschaltbilder; st1/netzwerkanalyse/05-ersatzschaltbild-y, 05-rueckwirkung-cgd, 05-parallelschaltung, 05-bipolar-re, 05-signalkette; absehbar alle Kleinsignal-Ersatzschaltbilder von Diode, Bipolartransistor und MOSFET, modifizierte Knotenanalyse.

## 29. Iterationsdarstellungen  — **P2** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Folge von Tangenten an eine Funktion: Nullstelle jeder Tangente auf der Achse markiert, senkrechte Hilfslinie zurück zur Kurve, nummerierte Schätzwerte $U^{(0)}, U^{(1)}, \ldots$; schrittweise einblendbar (§8).
- Ebenso die einfache Iteration als Treppen- oder Spinnwebdiagramm zwischen Funktion und Winkelhalbierender.
- Synchron dazu eine Wertetabelle, deren Zeile beim jeweiligen Schritt hervorgehoben wird; Startwert per Schieberegler (§15).
Gebraucht in: st1/netzwerkanalyse/01-newton, 04-euler-verfahren (Steigungsstücke der Euler-Verfahren); absehbar numerische Verfahren (Numerik).

## 30. Netzwerkgraphen  — **P3** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Eine Schaltung auf ihren Graphen reduziert: Knoten als Punkte, Zweige als beschriftete Linien (Bauteilname statt Symbol), Bezugsknoten hervorgehoben.
- Baum und Verbindungszweige farbig getrennt; zu jedem Verbindungszweig der gebogene Umlaufpfeil seiner Masche (§2).
- Kopplung an das Schaltbild daneben (§10): Auswahl eines Zweigs hebt ihn in beiden Darstellungen hervor.
Gebraucht in: st1/netzwerkanalyse/02-topologie; absehbar modifizierte Knotenanalyse und Topologie in ET1.

## 31. Netzlisten, Eintragsmuster und Matrix-Aufbau  — **P2** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Netzliste als Tabelle (Name, Knoten, Wert), zeilenweise mit dem Schaltbild gekoppelt: Auswahl einer Zeile hebt das Bauteil hervor (§1, §10).
- Matrix mit Zeilen- und Spaltenbeschriftung (Knotennamen, Zusatzströme); Einträge als Summe farbiger Beiträge je Bauteil (gestapelte Teilfelder); Aufbau Bauteil für Bauteil als Animation (§8).
- Musterkarten: Schaltsymbol, Zählpfeile, Zweiggleichung und Matrixausschnitt nebeneinander; Vorzeichenfaktoren am Zeilen- und Spaltenrand, ihr Produkt im Feld.
- Rand mit Zeilen- und Spaltensummen; Durchstreichen einer Zeile und Spalte (Bezugsknoten); Blockmatrix mit angefügter Zusatzzeile und -spalte und grau hinterlegtem Kernblock.
- Determinanten-Schemata: ersetzte Spalte hervorgehoben, Schachbrettmuster der Vorzeichen als Überlagerung, Streichungsmatrix mit gedimmter Zeile und Spalte, Sarrus-Diagonalen in zwei Farben.
- Symbole Nullator (Oval) und Norator (zwei überlappende Kreise) für die Symbolbibliothek (§1).
Gebraucht in: st1/netzwerkanalyse/03-netzliste-matrix, 03-eintragsmuster-knoten, 03-vollstaendige-matrix, 03-cramer-laplace, 03-mna-spannungsquelle, 03-eintragsmuster-mna, 03-nullor-verstaerker; Kettenmatrizen von Längs- und Querglied (05-laengs-quer); absehbar Transientenanalyse (Begleitmodelle).

## 32. Bode-Diagramme  — **P1** für die Frequenzgang-Themen (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Betrag in dB über logarithmischer Frequenzachse, darunter der Winkel in Grad auf derselben Achse (§13).
- Asymptoten gestrichelt mit Steigungsangabe (0, −20, −40 dB pro Dekade); Eckfrequenzen als senkrechte Hilfslinien mit Beschriftung; −3-dB-Punkt markiert.
- Mehrere Übertragungsfunktionen in einem Diagramm, direkt an den Kurven beschriftet; Werte aus dem Zahlenwerk (§11).
Gebraucht in: st1/netzwerkanalyse/03-bode, 05-rc-kette (nur Betrag); absehbar Frequenzgang der Transistorgrundschaltungen, Miller-Effekt, OPV-Frequenzgang.

## 33. Zeitschritte, Integrationsverfahren und Begleitmodelle  — **P2** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Zeitraster mit Punkten je Zeitschritt über einer exakten Kurve (§11); Steigungsstücke je Schritt, wahlweise am Schrittanfang (explizit) oder am Schrittende (implizit), gestrichelt in der Farbe des Verfahrens.
- Folgen mit wachsenden Ausschlägen: Achse automatisch abschneiden und Werte am Rand angeben oder Betrag logarithmisch; Faktor je Schritt als Beschriftung.
- Ersetzungsdarstellung „Bauteil = Ersatzschaltung“: zwei Schaltungsteile mit Gleichheitszeichen dazwischen (Kondensator gleich Leitwert parallel Stromquelle), gemeinsame Knotennamen; dazu der Matrixausschnitt (§31) mit dem Vergleich zur Wechselstromanalyse in Grau.
- Wertetabelle synchron zu den Punkten; Zeitachse mit Schrittmarken $t_0, t_1, \ldots$ und Pfeil vom Ergebnis eines Schritts zur Quelle des nächsten.
Gebraucht in: st1/netzwerkanalyse/04-uebersicht, 04-euler-verfahren, 04-begleitmodell-kondensator, 04-begleitmodell-spule, 04-verstaerker-transiente; absehbar numerische Verfahren (Numerik für Elektrotechnik).

## 34. Testquellen und Schaltzustände  — **P2** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Quellen mit Zustand „aktiv“ oder „abgeschaltet“: abgeschaltete Quelle grau mit „= 0“, wahlweise ersetzt durch ihren Ersatz (Stromquelle durch Leerlauf, Spannungsquelle durch Kurzschluss, gestrichelt); Testquellen farblich abgesetzt (Teststrom orange, Testspannung blau).
- Umschalten zwischen Läufen derselben Schaltung als Animation (§8): Die aktive Quelle wechselt, die zugehörige rechte Seite der Matrix wechselt mit (§31), die Matrix bleibt stehen.
- Markierung „falsch“ (rot umrandet oder durchgestrichen) für Gegenbeispiele wie eine entfernte statt kurzgeschlossene Quelle.
Gebraucht in: st1/netzwerkanalyse/04-uebersicht, 04-teststrom-ausgang, 04-testspannung-eingang, 04-innerer-knoten, 04-ersatzzweitor; st1/netzwerkanalyse/05-kurzschluss-leerlauf (Kurzschluss und Leerlauf an einem Tor), 05-reihenschaltung-t (Markierung „falsch“).

## 35. Zweitore und ihre Zusammenschaltungen  — **P2** (neu 2026-10-23, Schaltungstechnik Netzwerkanalyse)
- Zweitor als Kasten mit den Klemmen 1, 1′, 2, 2′ und symmetrischen Zählpfeilen; wahlweise der Ausgangsstrom als $-\underline I_2$ hinaus (Kettenform). Inhalt des Kastens ausblendbar (nur Torverhalten) oder als Schaltbild (§1).
- Vorlagen für die Zusammenschaltung zweier Kästen a und b: Kette, Parallel, Reihe, Reihen-Parallel; die Verbindungsleitungen werden automatisch geführt, auch gekreuzt; ein Kasten lässt sich umdrehen (obere und untere Leitung tauschen).
- Messvorlagen an einem Tor: Kurzschlussbügel, offenes Tor, ideale Spannungs- oder Stromquelle (§34), dazu die abgelesenen Größen.
- Klemmenstrompfeile mit Zahlenwerten an allen vier Klemmen; Markierung, wenn an einem Tor hinein und heraus verschiedene Ströme fließen (Torbedingung verletzt, rot); Spannungsmesser zwischen zwei Klemmen für den Brune-Test.
- Matrizen unter den Schaltungen mit der Operation dazwischen (Produkt bzw. Summe) und dem Ergebnis; Einträge mit Einheit; Übereinstimmung oder Abweichung gegenüber der direkt berechneten Matrix farbig.
Gebraucht in: st1/netzwerkanalyse/05-uebersicht, 05-tor-und-vierpol, 05-kurzschluss-leerlauf, 05-rc-kette, 05-laengs-quer, 05-parallelschaltung, 05-reihenschaltung-t, 05-bipolar-re, 05-signalkette; absehbar Transistorgrundschaltungen (Stufen als Zweitore in Ketten) und Leitungen.

## Vorgehensvorschlag nach den Artikeln (Stand 2026-10-21)
1. Teilbild-Layout, Datenkurven, halblogarithmische Achsen (§10–§12) zusammen mit §4: schalten die meisten
   Kennlinien- und Profil-Abbildungen frei.
2. Bänderschema/Kristallgitter/pn-Übergang (§6, §16) und Pfeile (§2).
3. Gestapelte Diagramme, Teilchenwolken, Schieberegler (§13–§15), Animationen (§8) zuletzt.
