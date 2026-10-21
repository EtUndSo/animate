# Abbildungsliste: Abbildungen für den Editor

**Entscheidung des Users (21.10.2026):**
- In allen Artikeln stehen nur Abbildungen, die der Editor erzeugt.
- Bis dahin steht im Artikel an jeder Stelle ein Platzhalter `:::grafik`: Szene-Zeile und sichtbare Bildbeschreibung mit Kernaussage.
- Diese Liste hält fest, was jede Abbildung zeigen soll und welche Editor-Funktionen dafür nötig sind.
- Editor-Funktionen und Abbildungen kommen **nach** den Artikeln, nicht im Loop, weil neue Features oft Probleme machen.

**Aufbau eines Eintrags:**
- Szene-ID wie im Artikel;
- in welchen Fassungen und unter welcher Nummer die Abbildung vorkommt;
- Inhalt mit allen Zahlen;
- Kernaussage;
- Datenquelle;
- benötigte Editor-Funktionen mit Verweis auf die Abschnitte in `EDITOR_GRAFIK_FEATURES.md` (§1 bis §19);
- Status.

**Datenquellen:** Berechnete Kurven stammen aus dem Zahlenwerk des Oberthemas (`notizen/<modul>/zahlen_<oberthema>.py`). Für den Piloten gibt es zusätzlich Entwürfe in `notizen/get1/abb_referenz/` (Dateinummer wie in der ausführlichen Fassung) und Animationsideen in `notizen/get1/grafiken_halbleiter-und-baendermodell.md`. Für spätere Themen werden keine Entwürfe mehr gezeichnet; Animationsideen stehen dann direkt im Eintrag.

---

## ET1 Kap. 10: Halbleiter und das Bändermodell (Pilot)
Zahlenwerk: `notizen/get1/zahlen_halbleiter.py`.

**get1/halbleiterbauelemente/01-gesamtbild**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Vier Teilbilder.
- Oben drei kleine Bänderschemata:
  - (a) reines Si, $W_F$ 7 meV unter der Mitte, je 2 Elektronen und 2 Löcher;
  - (b) n-Si, $W_F$ 0,209 eV unter $W_L$, 7 Elektronen;
  - (c) p-Si, $W_F$ 0,194 eV über $W_V$, 7 Löcher.
  - In allen drei: Valenzband grau gefüllt, Maßpfeil $W_g$ = 1,12 eV in (a).
- Unten breit (d): Bandverlauf $W_L(x)$, $W_V(x)$ des pn-Übergangs im Gleichgewicht.
  - x von −0,6 bis 0,6 µm;
  - Raumladungszone grau von −0,215 bis 0,215 µm;
  - $W_F$ gestrichelt bei 0;
  - Elektronen links im Leitungsband, Löcher rechts im Valenzband;
  - Maßpfeil $e\,U_\mathrm{Diff}$ = 0,714 eV.

*Kernaussage:* wenige Ladungsträger, Dotierung verschiebt $W_F$, am Übergang entsteht eine Stufe von 0,714 eV.

*Daten:* `gleichgewicht_profil()` (WL, WV), WL_Wi, kT·ln(N_L/N_D), kT·ln(N_V/N_A).

*Editor:*
- §10 Teilbild-Layout (3 klein + 1 breit);
- §6/§16 Bänderschema;
- §11 Datenkurve;
- §4 Bereich hinterlegen;
- §2 Maßpfeil;
- §7 Labels.

**get1/halbleiterbauelemente/01-einweggleichrichter**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:*
- Links das Schaltbild: Wechselspannungsquelle, Diode D, Widerstand R = 1 kΩ, Zählpfeile $u_E$ und $u_A$.
- Rechts die Zeitverläufe über 40 ms (50 Hz):
  - $u_E(t)$ gestrichelt, Scheitelwert 10 V;
  - $u_A(t)$ kräftig: nur positive Halbwellen mit rund 9,3 V Spitze;
  - Markierung „Spitze 9,3 V statt 10 V“.

*Kernaussage:* nur positive Halbwellen, rund 0,7 V Verlust an der Diode.

*Daten:* $u_A$ aus der Shockley-Gleichung mit R (implizit gelöst; Bisektion im Entwurfsskript).

*Editor:*
- §1 Schaltplan;
- §2 Zählpfeile;
- §5 Zeitverlauf;
- §11 Datenkurve;
- §10 Teilbilder nebeneinander.

**get1/halbleiterbauelemente/01-leiter-halbleiter-isolator**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Spalten auf einer gemeinsamen Energieachse (−2 bis 11 eV).
- Metall: ein Band, bis $W_F$ gefüllt.
- Halbleiter: Valenzband gefüllt, Lücke 1,12 eV, wenige Elektronen und Löcher.
- Isolator: Lücke ≈ 9 eV.

Darunter: Namen und Zahlen der freien Ladungsträger (8,5·10²², je 10¹⁰, praktisch keine pro cm³).

*Kernaussage:* Leiten kann nur ein teilweise besetztes Band; die Lücke regelt die Zahl.

*Daten:* feste Werte aus dem Zahlenwerk.

*Editor:*
- §6/§16 Bänder auf echter Energieachse;
- §2 Maßpfeile;
- §7 Labels.

**get1/halbleiterbauelemente/01-kristallgitter**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Drei Teilbilder, je 4×2 Si-Atome (Kreise mit „Si“), Bindungen als Doppellinien.
- (a) Eine Bindung hat nur eine Linie, dort ein Loch (roter Kreis); daneben ein freies Elektron mit Pfeil.
- (b) P⁺ hell rot hinterlegt, gestrichelte Bahn, Elektron verlässt sie mit Pfeil.
- (c) B⁻ hell blau hinterlegt, Loch eine Bindung weiter.

*Kernaussage:* Bindungen, Donator, Akzeptor, feste Rümpfe.

*Editor:*
- §6/§16 Kristallgitter mit Einzelbindungen, die sich ausblenden lassen;
- §2 kleine Pfeile;
- §10 Teilbilder.

**get1/halbleiterbauelemente/01-loch-wanderung**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:*
- Drei Zeilen „Moment 1–3“ mit je 5 Bindungsplätzen: 4 Elektronen (blaue Punkte) und 1 Lücke (roter Kreis), die von Zeile zu Zeile nach rechts rückt.
- Gebogene blaue Pfeile: Ein Elektron springt jeweils von rechts nach links in die Lücke.
- Oben ein grüner Feldpfeil nach rechts, unten ein roter Pfeil „das Loch wandert mit dem Feld“.

*Kernaussage:* Die Lücke wandert mit dem Feld wie eine positive Ladung.

*Editor:*
- §2 gebogene Pfeile;
- §7 Labels;
- §8 als Animation mit umschaltbarer Feldrichtung.

**get1/halbleiterbauelemente/01-eigenleitung-temperatur**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* $n_i(T)$ von 200 bis 720 K, logarithmische y-Achse von 10⁵ bis 10¹⁸ cm⁻³.
- waagrechte gestrichelte Linie bei 10¹⁶ („Dotierung der Beispieldiode“);
- senkrechte Linie bei 655 K;
- Punkte bei 300 K (10¹⁰; +8,3 % pro K) und 400 K (525-fach; +4,7 % pro K).

*Kernaussage:* starker Temperaturgang; erst bei 655 K erreicht $n_i$ die Dotierung.

*Daten:* `ni_von_T(T)`.

*Editor:*
- §12 halblogarithmische Achse;
- §4 Hilfslinien und markierte Punkte mit Labels.

**get1/halbleiterbauelemente/01-fermi-verteilung**
- Fassung: ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) $f(W)$ linear für $W - W_F$ von −0,3 bis 0,3 eV bei 300 K, dazu die Stufe für $T = 0$ gestrichelt; Punkt bei 1/2.
- (b) logarithmisch für 0 bis 0,7 eV:
  - $f$ und die Boltzmann-Näherung gestrichelt;
  - senkrechte Linie bei 0,567 eV („$W_L$ in reinem Si“);
  - Punkt 3·10⁻¹⁰.

*Kernaussage:* $W_F$ ist der 50-%-Punkt; weit darüber exponentieller Abfall.

*Daten:* `fermi(W, WF)`.

*Editor:*
- §4 mehrere Kurven;
- §12 halblogarithmische Achse;
- §10 Teilbilder;
- §8 optional: Temperatur-Regler.

**get1/halbleiterbauelemente/01-baender-dotiert**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Bänderschemata, n- und p-Si mit 10¹⁶ cm⁻³.
- Linien: $W_L$, $W_V$, $W_i$ gepunktet, $W_F$ gestrichelt.
- n-Seite: kurze Striche bei $W_D$ (45 meV unter $W_L$); Maßpfeile 0,36 eV ($W_i$–$W_F$) und 0,21 eV ($W_F$–$W_L$).
- p-Seite: kurze Striche bei $W_A$; Maßpfeile 0,36 eV und 0,19 eV.
- Elektronen bzw. Löcher; Dichten als Text darunter.

*Kernaussage:* $W_F$ rückt 0,36 eV aus der Mitte, nicht symmetrisch (0,21 bzw. 0,19 eV).

*Daten:* WL_Wi, kT·ln(N_L/N_D), kT·ln(N_V/N_A).

*Editor:*
- §6/§16 Bänderschema mit Zusatzniveaus;
- §2 Maßpfeile;
- §7 Labels.

**get1/halbleiterbauelemente/01-rlz-entstehung**
- Fassung: kompakt Abb. 4, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Drei Zeilen.
- (a) n- und p-Block getrennt: Ionen ⊕ mit Elektron bzw. ⊖ mit Loch.
- (b) in Kontakt: Diffusionspfeile (Elektronen nach rechts, Löcher nach links), Rekombination „×“ an der Grenze, freigelegte Rümpfe.
- (c) Gleichgewicht: graue Raumladungszone mit nackten Ionen, grüner Feldpfeil von n nach p.

*Kernaussage:* Diffusion legt Rümpfe frei, deren Feld begrenzt den Vorgang.

*Editor:*
- §6 pn-Übergang (Ionen, Ladungsträger, Zone, Feldpfeil);
- §8 als Animation von (a) nach (c).

**get1/halbleiterbauelemente/01-profile-gleichgewicht**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Fünf gestapelte Diagramme mit gemeinsamer x-Achse (−0,6 bis 0,6 µm), Raumladungszone in allen grau.
- (a) $n$, $p$ logarithmisch;
- (b) $\rho/(eN)$, dazu das Kastenprofil gestrichelt;
- (c) $E$ in kV/cm (Maximum 32);
- (d) $\varphi$ in V (0 bis 0,714);
- (e) $W_L$, $W_V$ mit $W_F$ gestrichelt.

*Kernaussage:* Die ganze Stufe liegt in der verarmten Zone.

*Daten:* `gleichgewicht_profil()` (n, p, rho, E, phi, WL, WV) als Tabelle.

*Editor:*
- §13 gestapelte Diagramme mit gemeinsamer x-Achse und durchgehender Hinterlegung;
- §11 Datenkurven;
- §12 logarithmische Achse.

**get1/halbleiterbauelemente/01-hinauf-hinunter**
- Fassung: ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Schematisches Banddiagramm mit Stufe (glatter Übergang).
- Elektronenwolke im n-Leitungsband, exponentiell in der Energie verteilt, thermische Energie überzeichnet; Elektronen über der Stufe kräftig hervorgehoben.
- Wenige Minoritätselektronen (orange) auf dem p-Plateau.
- Löcher spiegelbildlich.
- Vier gebogene Pfeile mit Beschriftung: hinauf/Diffusion, hinunter/Drift für beide Sorten.
- Maßpfeil $e\,U_\mathrm{Diff}$.

*Kernaussage:* viele Ladungsträger mal winzige Erfolgsquote = wenige mal Erfolgsquote eins.

*Editor:*
- §14 Teilchenwolke nach Verteilung, mit Hervorhebung über einer Schwelle;
- §2 gebogene Pfeile;
- §6/§16 Bänderschema;
- §8 als Animation mit Zählern.

**get1/halbleiterbauelemente/01-baender-spannung**
- Fassung: kompakt Abb. 5, ausführlich Abb. 12.
- Status: offen.

*Inhalt:* Drei Bänderverläufe nebeneinander, $U$ = 0, +0,5 V, −2 V.
- Verarmungsnäherung: Weite 0,43 / 0,235 / 0,838 µm, Stufe 0,714 / 0,214 / 2,714 eV, n-Gebiet festgehalten.
- Je zwei Pfeile: hinauf (Faktor ×1, ×2,5·10⁸, ×2,5·10⁻³⁴) und hinunter (×1).

*Kernaussage:* Die Spannung verändert nur die Stufe.

*Daten:* `weite(U)`, Parabelstücke.

*Editor:*
- §15 Parameter-Schieberegler für $U$ (Kurven und Beschriftungen werden neu berechnet);
- §6/§16, §2;
- §10 Teilbilder.

**get1/halbleiterbauelemente/01-teilstroeme**
- Fassung: kompakt Abb. 6, ausführlich Abb. 13.
- Status: offen.

*Inhalt:* Ströme über $U$ (−0,3 bis 0,72 V), logarithmische y-Achse (10⁻¹⁶ bis 10⁻¹ A).
- hinauf $I_S\exp(U/U_T)$ blau gestrichelt;
- hinunter $I_S$ = 15 fA orange gestrichelt;
- Netto-Strom $|I|$ schwarz;
- Punkt „0,6 V: 0,18 mA“; Text „×10 je 59,5 mV“.

*Kernaussage:* Durchlass folgt dem Strom hinauf, Sperr dem konstanten Strom hinunter.

*Daten:* `strom(U)`, IS, UT.

*Editor:*
- §4 mehrere Kurven mit markierten Punkten;
- §12 logarithmische Achse;
- §8 optional: Umschalter linear/logarithmisch.

---

## ET1 Kap. 10: Die Diode und ihre Kennlinie
Zahlenwerk: `notizen/get1/zahlen_halbleiter.py`, Funktion `bericht_diode()`.

**get1/halbleiterbauelemente/02-aufbau-symbol**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Querschnitt von links nach rechts: Metallkontakt (Anode), p-Gebiet mit Löchern, grau die Raumladungszone, n-Gebiet mit Elektronen, Metallkontakt (Kathode).
- (b) Schaltsymbol: Dreieck zeigt auf den Querstrich, Anode A links, Kathode K rechts. Zählpfeile im Verbraucherzählpfeilsystem: Spannung $U$ von A nach K, Strom $I$ von A nach K.
- (c) Bauform (zylindrisches Gehäuse) mit Ring auf der Kathodenseite.

*Kernaussage:* In Durchlassrichtung fließt der Strom von der Anode zur Kathode, in Pfeilrichtung des Symbols.

*Editor:*
- §10 Teilbilder;
- §1 Diodensymbol mit Anschlussbeschriftung;
- §2 Zählpfeile;
- §6 pn-Struktur (Gebiete, Zone);
- §7 Labels.

**get1/halbleiterbauelemente/02-kennlinie-bereiche**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Gesamtkennlinie $I(U)$ der Beispieldiode, schematisch, mit getrennten Maßstäben je Bereich.
- Durchlassbereich (1. Quadrant): $I$ in mA bis 10 mA, $U$ von 0 bis 0,8 V, steiler Anstieg ab etwa 0,6 V.
- Sperrbereich (3. Quadrant): $I$ in pA, real −20 pA bei −1 V bis −100 pA bei −10 V (Generation in der Zone), dazu gestrichelt das ideale $-I_S$ = −15 fA.
- Durchbruch: bei etwa −100 V steil nach unten, beschriftet „Durchbruch“.
- Achsenbrüche bzw. Maßstabswechsel deutlich markiert und beschriftet („mA“, „pA“, „V“ gegen „0,1 V“).

*Kernaussage:* Die drei Bereiche liegen auf völlig verschiedenen Strom- und Spannungsskalen.

*Daten:* `strom_real(U)`, `i_rg(U)`, `IS`; Durchbruch aus der Abschätzung in `bericht_diode()`.

*Editor:*
- §17 Achsenbruch und abschnittsweiser Maßstab;
- §4 Kurven mit Bereichsbeschriftung;
- §7 Labels.

**get1/halbleiterbauelemente/02-schwelle-massstab**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Dieselbe ideale Kennlinie der Beispieldiode dreimal linear nebeneinander.
- Achsenende 10 µA, 1 mA und 100 mA; $U$ jeweils 0 bis 0,8 V.
- Die scheinbare Schwelle (1 % des Achsenendes) ist markiert: 0,407 V, 0,526 V und 0,645 V.

*Kernaussage:* Die scheinbare Schwelle wandert um 59,5 mV je Dekade des Maßstabs; eine feste Schwellspannung gibt es nicht.

*Daten:* `strom(U)`, Tabelle „Durchlassspannung (ideal)“ in `bericht_diode()`.

*Editor:*
- §10 Teilbilder nebeneinander;
- §11 Datenkurven;
- §4 markierte Punkte.

**get1/halbleiterbauelemente/02-material-vergleich**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Drei ideale Kennlinien linear bis 10 mA, gleicher Aufbau, nur $n_i$ verschieden:
- Germanium ($I_S$ = 5,8·10⁻⁸ A);
- Silizium (1,46·10⁻¹⁴ A);
- Galliumarsenid (6,4·10⁻²² A).

Punkte bei 1 mA: 0,252 V, 0,645 V, 1,083 V.

*Kernaussage:* Je größer die Bandlücke, desto kleiner $I_S$ und desto höher die Durchlassspannung.

*Daten:* Tabelle „Material bei gleichem Aufbau“ in `bericht_diode()`.

*Editor:*
- §4 mehrere Kurven mit Direktbeschriftung;
- §11 Datenkurven.

**get1/halbleiterbauelemente/02-zone-unter-spannung**
- Fassung: ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Diagramme übereinander mit gemeinsamer Ortsachse in µm, links das p-, rechts das n-Gebiet.
- (a) Raumladungsdichte als Rechtecke, $-e N_A$ auf der p-Seite und $+e N_D$ auf der n-Seite, für 0 V (Zone 0,43 µm) und für −5 V (1,22 µm) übereinander.
- (b) Betrag des Feldes als Dreieck mit der Spitze an der Grenzfläche: 3,3·10⁴ V/cm bei 0 V und 9,4·10⁴ V/cm bei −5 V. Die Fläche unter jedem Dreieck ist schraffiert und mit 0,714 V bzw. 5,714 V beschriftet.

*Kernaussage:* Eine Sperrspannung verbreitert die Zone; Weite und Höchstfeld wachsen mit der Wurzel der Spannung, und die Spannung ist die Fläche des Felddreiecks.

*Daten:* `weite(U)` und `Emax_N()` aus `bericht_diode()`.

*Editor:*
- §13 gestapelte Diagramme mit gemeinsamer x-Achse;
- §4 Flächen schraffieren, mehrere Kurven;
- §11 Datenkurven;
- §15 optional: Spannungsregler.

**get1/halbleiterbauelemente/02-kennlinie-real**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Halblogarithmisch, $U$ von 0 bis 1,0 V, $I$ von 10⁻¹³ bis 10⁻¹ A. Kurven:
- ideal gestrichelt;
- Diffusionsanteil mit $n$ = 1;
- Rekombinationsanteil mit $n$ = 2;
- reale Kennlinie kräftig, mit starker Injektion und Bahnwiderstand 18,9 Ω.

Markiert:
- Schnittpunkt der Anteile bei 0,27 V und 1 nA;
- Bereich mit $m \approx 1$ zwischen etwa 0,1 µA und 1 mA;
- Abknicken oberhalb von etwa 1 mA (bei 10 mA 0,90 V statt 0,70 V).

*Kernaussage:* Nur im mittleren Bereich folgt die reale Kennlinie der idealen; unten überwiegt die Rekombination in der Zone, oben bremsen starke Injektion und Bahnwiderstand.

*Daten:* `strom_uebergang()` mit der integrierten Rekombination `i_rg()`, `strom_real()`, `spannung_real()`.

*Editor:*
- §12 halblogarithmische Achse;
- §11 Datenkurven;
- §4 mehrere Kurven, markierte Bereiche.

**get1/halbleiterbauelemente/02-temperatur**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Ideale Kennlinien bei 0, 25, 50 und 75 °C, linear bis 2 mA.
- Bei 1 mA markiert: 0,702 V, 0,649 V, 0,596 V und 0,542 V.
- Pfeil „−2,1 mV/K“.

*Kernaussage:* Mit steigender Temperatur wandert die Kennlinie nach links, bei festem Strom um rund 2 mV je Kelvin.

*Daten:* `strom_T(U, T)`, Tabelle „Temperatur“ in `bericht_diode()`.

*Editor:*
- §4 Kennlinienschar mit Parameter;
- §11 Datenkurven;
- §15 optional: Temperatur-Regler.

**get1/halbleiterbauelemente/02-durchbruch-mechanismen**
- Fassung: kompakt Abb. 4, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Banddiagramme unter hoher Sperrspannung.
- (a) Lawine, Beispieldiode bei rund 100 V: breite Zone (etwa 5 µm), schwach geneigte Bänder. Ein Elektron wird beschleunigt, stößt und erzeugt ein Paar; daraus entsteht eine Kaskade.
- (b) Zener-Effekt, Dotierung 10¹⁸ cm⁻³: schmale Zone (0,13 µm), steile Bänder. Ein waagrechter Pfeil zeigt ein Elektron, das vom Valenzband der p-Seite in das Leitungsband der n-Seite tunnelt; Maßpfeil 11 nm.

*Kernaussage:* Im Durchbruch erzeugt das Feld selbst Ladungsträger: durch Stoßionisation oder durch Tunneln.

*Daten:* Abschätzungen „Durchbruch“ in `bericht_diode()`.

*Editor:*
- §6/§16 Bänderschema mit Bandverbiegung;
- §2 Pfeile und Maßpfeile;
- §14 Teilchen;
- §8 Animation der Kaskade;
- §10 Teilbilder.

**get1/halbleiterbauelemente/02-z-diode-stabilisierung**
- Fassung: kompakt Abb. 5, ausführlich Abb. 9.
- Status: offen.

*Inhalt:*
- (a) Schaltung: Eingangsspannung $U_E$ = 12 V ± 1 V, Vorwiderstand $R_V$ = 330 Ω, Z-Diode 5,6 V parallel zum Lastwiderstand $R_L$ = 1 kΩ, Ausgangsspannung $U_A$; Zählpfeile.
- (b) Durchbruchast der Z-Diode als Betrag (Strom 0 bis 25 mA, Spannung 5,4 bis 5,9 V), Steigung 1/(20 Ω), mit drei Arbeitspunkten:
  - 11 V: 5,707 V und 10,3 mA;
  - 12 V: 5,763 V und 13,1 mA;
  - 13 V: 5,819 V und 15,9 mA.

*Kernaussage:* Ein Stromhub von 5,6 mA ändert die Spannung an der Z-Diode nur um 0,11 V.

*Daten:* Tabelle „Z-Diode als Spannungsstabilisierung“ in `bericht_diode()`.

*Editor:*
- §1 Schaltplan mit Z-Diodensymbol;
- §4 Kennlinie mit Arbeitspunkten;
- §10 Teilbilder;
- §15 optional: Regler für $U_E$.

**get1/halbleiterbauelemente/02-sperrschichtkapazitaet**
- Fassung: kompakt Abb. 6, ausführlich Abb. 10.
- Status: offen.

*Inhalt:* $C_j(U)$ der Beispieldiode für $U$ von 0 bis −25 V. Werte:
- 24,1 pF bei 0 V;
- 12,4 pF bei −2 V;
- 8,5 pF bei −5 V;
- 6,2 pF bei −10 V;
- 4,0 pF bei −25 V.

Daneben ein kleines Bild: die Zone als Plattenkondensator mit wachsendem Plattenabstand, Weite 0,43 µm bei 0 V und 1,22 µm bei −5 V.

*Kernaussage:* Mit der Sperrspannung wird die Zone breiter und die Kapazität kleiner.

*Daten:* `C_j(U)`, `weite(U)`.

*Editor:*
- §4 Funktionsgraph mit markierten Punkten;
- §10 Teilbild bzw. Einsatzbild;
- §6 pn-Struktur;
- §15 optional: Spannungsregler.

**get1/halbleiterbauelemente/02-fotodiode-quadranten**
- Fassung: kompakt Abb. 7, ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Kennlinienschar der Beispieldiode bei Fotostrom 0, 11,7, 23,3 und 35 µA (0, ⅓, ⅔ und volle Bestrahlung von 1000 W/m²), linear; $U$ von −1 bis 0,65 V, $I$ von −40 bis +20 µA.

Quadranten beschriftet:
- 1. Durchlass;
- 3. Fotodiodenbetrieb, Sperrspannung, Strom proportional zum Licht;
- 4. Solarzellenbetrieb, Leistungsabgabe.

Markiert:
- Kurzschlussstrom −35 µA;
- Leerlaufspannung 0,558 V;
- Punkt größter Leistung bei 0,481 V und −33,2 µA, das Rechteck darunter schraffiert (16 µW).

Kleines Ersatzschaltbild: Stromquelle $I_{ph}$ parallel zur Diode.

*Kernaussage:* Licht verschiebt die Kennlinie um den Fotostrom nach unten; im vierten Quadranten gibt die Diode Leistung ab.

*Daten:* `strom(U)` minus Fotostrom, Tabelle „Fotodiode und Solarzelle“ in `bericht_diode()`.

*Editor:*
- §4 Kennlinienschar, Fläche schraffieren, markierte Punkte;
- §1 Ersatzschaltbild mit Stromquelle;
- §7 Quadrantenbeschriftung;
- §15 optional: Regler für die Bestrahlung.

---

## ET1 Kap. 10: Arbeitspunkt und Ersatzschaltung der Diode
Zahlenwerk: `notizen/get1/zahlen_halbleiter.py`, Funktion `bericht_ap()`.

**get1/halbleiterbauelemente/03-arbeitsgerade**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:*
- (a) Grundschaltung: Quelle 5 V, Widerstand 1 kΩ, Beispieldiode; der lineare Rest (Quelle und Widerstand) ist gestrichelt umrahmt. Zählpfeile $U$ an der Diode und $I$.
- (b) Diagramm $I$ in mA (0 bis 5,5) über $U$ in V (0 bis 5): Arbeitsgerade von (5 V; 0) nach (0; 5 mA), Kennlinie der Beispieldiode, die bei 0,6 bis 0,7 V fast senkrecht ansteigt, Schnittpunkt AP bei 0,683 V und 4,32 mA.
- Ausschnitt (Lupe) 0,6 bis 0,75 V und 3,5 bis 5 mA mit dem Schnittpunkt.

*Kernaussage:* Der Arbeitspunkt ist der Schnittpunkt der Diodenkennlinie mit der Arbeitsgeraden des übrigen Netzes.

*Daten:* `ap_exakt(5, 1000)`, `strom(U)`.

*Editor:*
- §1 Schaltplan mit Rahmen;
- §4 Kennlinie, Gerade, Schnittpunkt;
- §10 Teilbilder und Ausschnitt;
- §11 Datenkurve;
- §15 optional: Regler für Quellenspannung und Widerstand.

**get1/halbleiterbauelemente/03-iteration**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Ausschnitt der Kennlinie und der Arbeitsgeraden um den Arbeitspunkt (0,66 bis 0,71 V, 4,2 bis 4,4 mA). Treppenweg der Fixpunktiteration ab 0,7 V:
- waagrecht zur Arbeitsgeraden: 4,300 mA;
- senkrecht zur Kennlinie: 0,68276 V;
- wieder zur Geraden: 4,3172 mA;
- dann im Rahmen der Zeichengenauigkeit im Arbeitspunkt 0,68287 V und 4,3171 mA.

*Kernaussage:* Jeder Schritt verkleinert den Fehler auf das U_T/(R I)-Fache, hier etwa 0,006.

*Daten:* `ap_iteration(5, 1000)`.

*Editor:*
- §4 Kurven und Pfeilzug;
- §8 Animation Schritt für Schritt.

**get1/halbleiterbauelemente/03-ersatzschaltungen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Teilbilder, je eine Modellkennlinie über der realen Kennlinie (grau):
- (a) ideale Diode: senkrechte Linie bei 0 V und waagrechte bei 0 A;
- (b) Diode mit Durchlassspannung $U_{F0}$ = 0,6 V;
- (c) Knickkennlinie: ab $U_{F0}$ eine Gerade mit der Steigung $1/r_F$.

Unter jedem Teilbild die Ersatzschaltbilder für „leitend“ (Kurzschluss, Spannungsquelle, Spannungsquelle mit Widerstand) und „sperrend“ (offener Schalter).

*Kernaussage:* Jedes Modell ersetzt die Diode je Zustand durch lineare Bauteile.

*Editor:*
- §1 Schaltsymbole (Quelle, Widerstand, offene Klemmen);
- §4 Kennlinien;
- §10 Teilbilder.

**get1/halbleiterbauelemente/03-modellvergleich**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Arbeitsgerade der Grundschaltung von 0 bis 0,8 V (5,0 bis 4,2 mA), dazu die Modellkennlinien und ihre Schnittpunkte:
- ideal: 0 V, 5,00 mA;
- 0,6 V-Modell: 4,40 mA;
- 0,7 V-Modell: 4,30 mA;
- exakt: 0,683 V, 4,317 mA.

*Kernaussage:* Der Strom hängt kaum vom Modell ab, solange die Quellenspannung groß gegen die Durchlassspannung ist.

*Daten:* Tabelle „Ersatzschaltungen in der Grundschaltung“ in `bericht_ap()`.

*Editor:*
- §4 Gerade, Kurven, markierte Punkte mit Werten.

**get1/halbleiterbauelemente/03-schutzdioden**
- Fassung: kompakt Abb. 3, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Eingangsschutz:
- Eingangsspannung $U_E$ über 1 kΩ an den Knoten A;
- D1 von A (Anode) zur Versorgung 5 V (Kathode);
- D2 von Masse (Anode) nach A (Kathode);
- Last 10 kΩ von A nach Masse.

Daneben für $U_E$ = 9 V zwei Zustände mit Potenzialen:
- „beide sperren“: A auf 8,18 V, an D1 +3,18 V, rot markiert als Widerspruch;
- „D1 leitet“: A auf 5,6 V, 3,4 mA durch den Widerstand, 0,56 mA durch die Last, 2,84 mA durch D1, an D2 −5,6 V.

*Kernaussage:* Die Probe der Annahme an den Potenzialen zeigt sofort, welche Diode leiten muss.

*Daten:* Tabelle „Schutzdioden am Eingang“ in `bericht_ap()`.

*Editor:*
- §1 Schaltplan;
- §7 Potenzial-Beschriftungen und Markierungen;
- §10 Teilbilder;
- §15 optional: Regler für $U_E$ von −5 bis +10 V mit wechselndem Zustand.

**get1/halbleiterbauelemente/03-kleinsignal**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:*
- (a) Kennlinie der Beispieldiode um den Arbeitspunkt (4,32 mA) mit der Tangente der Steigung $1/r_d$, $r_d$ = 6,0 Ω.
- Ein kleiner Sinus der Spannung (±0,6 mV) auf der Spannungsachse erzeugt einen Sinus des Stroms (±0,1 mA) auf der Stromachse; ein großer Hub (±20 mV) zum Vergleich mit sichtbarer Verzerrung.
- (b) Kleinsignal-Ersatzschaltbild: Diode durch $r_d$ ersetzt, Quelle durch ihre Änderung.

*Kernaussage:* Für kleine Änderungen verhält sich die Diode wie ein Widerstand $U_T/I$.

*Daten:* `r_diff(I)`, Kleinsignal-Werte in `bericht_ap()`.

*Editor:*
- §4 Tangente im Punkt;
- §5 Zeitverläufe an den Achsen;
- §8 Animation des wandernden Punkts;
- §1 Ersatzschaltbild.

---

## ET1 Kap. 10: Gleichrichtung und Ladungspumpe
Zahlenwerk: `notizen/get1/zahlen_halbleiter.py`, Funktionen `glaettung_sim`, `glaettung_einschalten`, `ladungspumpe`, `pumpe_sim`, `bericht_gleichrichter()`.

**get1/halbleiterbauelemente/04-bruecke-strompfade**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Brückenschaltung nach Graetz mit Wechselspannungsquelle $u_e$ (10 V Scheitel), vier Dioden D1 bis D4 und Lastwiderstand mit fester Polung von $u_a$. Nummerierung wie im Skript (Bild 10.25), jeweils von der Anode zur Kathode: D1 oberer Eingang → oberes Lastende, D4 unterer Eingang → oberes Lastende, D2 unteres Lastende → oberer Eingang, D3 unteres Lastende → unterer Eingang. Zwei Teilbilder:
- (a) positive Halbwelle: Strompfad farbig über D1, Last, D3; D2 und D4 grau;
- (b) negative Halbwelle: Strompfad vom unteren Eingang über D4, Last, D2 zum oberen Eingang.

In beiden Teilbildern fließt der Strom durch die Last in derselben Richtung (Pfeil).

*Kernaussage:* Die Brücke lenkt beide Halbwellen in derselben Richtung durch die Last; je Halbwelle leiten zwei Dioden in Reihe.

*Editor:*
- §1 Schaltplan mit Brückenanordnung;
- §2 Strompfeile;
- §10 Teilbilder;
- §8 Animation mit wechselndem Pfad.

**get1/halbleiterbauelemente/04-bruecke-zeitverlauf**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Zeitverläufe über 40 ms:
- $u_e$ gestrichelt, Scheitel ±10 V;
- $u_a$ kräftig, Betrag von $u_e$ minus 1,2 V, Spitze 8,8 V;
- um jeden Nulldurchgang eine Totzone von 0,77 ms, in der $u_a$ = 0 ist (markiert);
- waagrechte Linie für den Mittelwert 5,21 V.

*Kernaussage:* Der Ausgang ist der Betrag des Eingangs abzüglich zweier Durchlassspannungen, mit Lücken um die Nulldurchgänge.

*Daten:* Tabelle „Brücke ohne Glättung“ in `bericht_gleichrichter()`.

*Editor:*
- §5 Zeitverläufe mit abgeschnittenen Signalen;
- §4 markierte Bereiche und Hilfslinien;
- §15 optional: Regler für die Durchlassspannung.

**get1/halbleiterbauelemente/04-glaettung**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:*
- (a) Brücke mit Ladekondensator 470 µF parallel zur Last 470 Ω, Innenwiderstand der Quelle 5 Ω.
- (b) Zwei gestapelte Diagramme über 30 ms:
  - oben $u_C$ zwischen 8,05 und 8,34 V (gezoomte Achse), dazu gestrichelt der Betrag von $u_e$ minus 1,2 V;
  - unten der Diodenstrom: Pulse von 2,2 ms Dauer und 118 mA Spitze, dazu der konstante Laststrom von 17,4 mA.

*Kernaussage:* Der Kondensator wird nur kurz um die Spitzen nachgeladen; dazwischen speist er die Last allein, die Spannung sinkt um 0,29 V.

*Daten:* `glaettung_sim()`.

*Editor:*
- §1 Schaltplan;
- §13 gestapelte Diagramme;
- §11 Datenkurven aus der Simulation;
- §15 optional: Regler für C und Last.

**get1/halbleiterbauelemente/04-ladungspumpe-takte**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Die Ladungspumpe des Skripts in zwei Teilbildern: Eingang $U_e$ = 5 V, D1, R1, Knoten mit C1 nach unten zum Umschalter, R2, D2, Ausgangskondensator C2. Die Unterseite von C1 hängt nur am Umschalter; im Skriptbild ist sie zusätzlich fest an Masse gezeichnet, ein Zeichenfehler, der nicht übernommen wird.
- (a) Takt 1: Unterseite von C1 an Masse; Strompfad über D1 und R1 in C1, C1 auf 4,4 V.
- (b) Takt 2: Unterseite von C1 an $U_e$; Oberseite auf 9,4 V, D1 gesperrt (rot), Strompfad über R2 und D2 in C2; C2 nähert sich 8,8 V.

*Kernaussage:* Der geladene Kondensator wird auf die Eingangsspannung gestapelt und gibt seine Ladung an den Ausgang weiter.

*Editor:*
- §1 Schaltplan mit Umschalter;
- §2 Strompfeile;
- §7 Spannungsbeschriftungen;
- §10 Teilbilder;
- §8 Animation der beiden Takte.

**get1/halbleiterbauelemente/04-ladungspumpe-aufladen**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Spannung an C2 als Zeitverlauf (Takt 1 und Takt 2 je 50 µs), zwei Teilbilder:
- (a) ohne Last über die ersten zehn Perioden (1 ms): im ersten Takt 1 Anstieg auf 3,80 V (D2 leitet mit), am Ende der Perioden 6,30; 7,55; 8,18; 8,49; 8,64 V … gegen 8,8 V; optional gestrichelt die Schaltung mit 10 Ω (3,10 V, dann 5,74; 7,26; 8,02; 8,41; 8,60 V);
- (b) mit 1 mA Last, eingeschwungen, zwei Perioden vergrößert: in Takt 1 Abfall von 8,70 auf 8,65 V, Sprung beim Ausgleich auf 8,725 V, im Rest von Takt 2 Abfall zurück auf 8,70 V.

Hilfslinie bei 8,8 V.

*Kernaussage:* Bei C1 = C2 halbiert jede Periode den Abstand zum Endwert; unter Last liegt der Ausgang am Ende von Takt 2 um I/(f C1) darunter.

*Daten:* `ladungspumpe()` (Grenzfall schnellen Ausgleichs), `pumpe_sim()` (Schaltung mit R1 = R2 = 10 Ω).

*Editor:*
- §4 Treppenkurve mit markierten Punkten;
- §11 Datenkurve;
- §15 optional: Regler für Last und C1.

---

## ET1 Kap. 11: Der Bipolartransistor – Aufbau und Wirkungsweise
Zahlenwerk: `notizen/get1/zahlen_transistor.py` (Beispieltransistor nach Art des BC547C), Funktionen `stroeme`, `ube_bei_ib`, `ic_bei_ib`, `arbeitspunkt`, `b_von_ic`, `profil`, Bericht `bericht()`.

**get1/bipolartransistoren/01-npn-querschnitt**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Querschnitt eines npn-Transistors im Normalbetrieb, schematisch, Dicken nicht maßstäblich (so beschriftet): Emitter n⁺, Basis p (schmal), Kollektor n, Raumladungszonen grau hinterlegt; Anschlüsse E, B, C. Werte bei 2 mA:
- breiter blauer Pfeil: Elektronen vom Emitter durch die Basis in den Kollektor, 2 mA;
- dünne rote Pfeile: Löcher aus der Basis in den Emitter (Rückinjektion, 2,5 µA), Rekombinationszeichen in der Basis (1,5 µA), Löcherzufuhr am Basisanschluss (zusammen 4 µA);
- an den Anschlüssen die technischen Stromrichtungen mit $I_C$ = 2,000 mA, $I_B$ = 4,0 µA, $I_E$ = 2,004 mA; Hinweis, dass Elektronen entgegen der technischen Stromrichtung laufen.

Farben nach ERKLAER_PROMPT §7.4: Elektronen blau, Löcher rot, Raumladungszonen grau.

*Kernaussage:* Der Kollektorstrom läuft vom Emitter durch die dünne Basis; über den Basisanschluss kommen nur Löcher für die kleinen Verluste.

*Daten:* Rückinjektion 1,25·10⁻³ und Rekombination 0,756·10⁻³ je Kollektorelektron aus `bericht()`.

*Editor:*
- §6 Querschnitt, erweitert vom pn-Übergang auf drei Gebiete mit zwei Zonen;
- §2 Pfeile mit Werten;
- §18 Pfeilbreite nach Wert;
- §14 Teilchen optional;
- §8 Animation: Elektronen wandern hindurch, einzelne rekombinieren, Löcher kommen über die Basis nach.

**get1/bipolartransistoren/01-aufbau-symbole**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) npn: drei Schichten mit Dotierung als Balken auf logarithmischer Skala (Emitter 10¹⁹, Basis 10¹⁷, Kollektor 10¹⁶ cm⁻³) und Dicken (0,5 µm, 0,5 µm, 5 µm; „nicht maßstäblich“); zwei Quellen für den Normalbetrieb (Basis positiv gegen Emitter, Kollektor positiv gegen Basis) wie Skript Bild 11.1a; daneben das Schaltsymbol mit $I_B$ und $I_C$ hinein, $I_E$ heraus, $U_{BE}$, $U_{CB}$, $U_{CE}$ wie Bild 11.1b.
- (b) pnp: Schichtfolge p, n, p mit umgekehrter Polung; Symbol mit Emitterpfeil nach innen; $I_E$ hinein, $I_B$ und $I_C$ heraus wie Skript Bild 11.30.

*Kernaussage:* Drei Gebiete, zwei Übergänge; der Emitterpfeil zeigt die Richtung des Emitterstroms, die Zählpfeile folgen dem Skript.

*Editor:*
- §1 Symbole npn und pnp, Spannungsquellen;
- §2 Zählpfeile;
- §6 Schichtfolge;
- §4 bzw. §12 logarithmischer Balken;
- §10 Teilbilder.

**get1/bipolartransistoren/01-transistoreffekt**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Teilbilder, x-Achse durch Emitter, Basis (0,5 µm) und Kollektor, schematisch gedehnt.
- (a) Leitungsbandkante $W_L$ im Gleichgewicht: Stufe 0,95 eV zwischen Emitter und Basis, 0,77 eV zwischen Basis und Kollektor.
- (b) Normalbetrieb mit $U_{BE}$ = 0,65 V und $U_{CB}$ = 5 V: Stufe vor der Basis 0,30 eV, Stufe zum Kollektor 5,77 eV (Achsenbruch); Elektronen (blau) über der Stufe, Diffusionspfeil durch die Basis, Absturz am Basis-Kollektor-Übergang.
- (c) Elektronendichte $n(x)$ in der Basis, x von 0 bis 0,5 µm, y linear in 10¹³ cm⁻³: Gerade von 8,3·10¹³ auf 0 bei 0,65 V; gestrichelt 5,75·10¹⁴ auf 0 bei 0,70 V (eigener Maßstab oder Faktor im Bild).

*Kernaussage:* Die Stufe am Emitter bestimmt, wie viele Elektronen in die Basis kommen; die Kante am Kollektor sammelt sie alle ein, unabhängig von ihrer Tiefe.

*Daten:* $U_\mathrm{Diff}$ (BE) = 0,952 V, (BC) = 0,774 V und Profil aus `profil(0.65)`, `profil(0.70)`.

*Editor:*
- §16 Bänderschema;
- §17 Achsenbruch;
- §11 Datenkurve;
- §10 Teilbilder;
- §15 Regler für $U_{BE}$ (Stufe und Profil ändern sich) und $U_{CB}$ (nur die Kante wird tiefer, das Profil bleibt);
- §8 Animation der Elektronen.

**get1/bipolartransistoren/01-stromaufteilung**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Bilanz je 10 000 Elektronen, die am Kollektor ankommen:
- vom Emitter in die Basis 10 007,6 Elektronen;
- davon rekombinieren 7,6 in der Basis;
- 12,5 Löcher gehen aus der Basis in den Emitter;
- über den Basisanschluss kommen 20,1 Löcher nach;
- Ergebnis $B$ = 10 000/20,1 ≈ 500 und $\alpha$ = 0,998.

Pfeilbreiten proportional; die kleinen Ströme in einem gekennzeichneten vergrößerten Maßstab (Lupe, Faktor 100).

*Kernaussage:* Die Stromverstärkung von 500 entsteht aus zwei kleinen Verlusten desselben Elektronenstroms.

*Daten:* η und δ aus `bericht()`.

*Editor:*
- §18 Mengenpfeile und Bilanz;
- §7 Labels;
- §2 Pfeile.

**get1/bipolartransistoren/01-zwei-sichten**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei Diagramme nebeneinander mit gemeinsamer linearer y-Achse $I_C$ in mA (0 bis 3 mA):
- links $I_C$ über $U_{BE}$ von 0,55 bis 0,70 V (Transfergleichung);
- rechts $I_C$ über $I_B$ von 0 bis 6 µA (Gerade mit Steigung 500);
- Arbeitspunkt 0,65 V, 1,66 µA, 0,831 mA in beiden markiert und waagrecht verbunden;
- gestrichelt Exemplar 2 mit $I_S$ = 2·10⁻¹⁴ A (links um 17,9 mV nach links) und $B$ = 700 (rechts steiler): bei fester Spannung 1,66 mA, bei festem Basisstrom 1,16 mA.

*Kernaussage:* Beide Sichten beschreiben denselben Zustand; sie streuen verschieden.

*Daten:* Abschnitt „Zwei Sichten“ in `bericht()`.

*Editor:*
- §13 sinngemäß (nebeneinander, gemeinsame y-Achse);
- §11 Datenkurven;
- §15 Regler für $I_S$ und $B$.

**get1/bipolartransistoren/01-kennlinien**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Drei Diagramme.
- (a) Eingangskennlinie bei $U_{CE}$ = 5 V: $I_B$ in µA über $U_{BE}$ in V (0,5 bis 0,75 V, 0 bis 20 µA); 1 µA bei 0,637 V, 4 µA bei 0,673 V, 20 µA bei 0,714 V.
- (b) Stromsteuerkennlinie doppelt logarithmisch: $I_C$ über $I_B$ (1 nA bis 1 mA); ideale Gerade mit Steigung 1, um den Faktor 500 über der gestrichelten Diagonalen; reale Kurve, an das Datenblatt des BC547C angepasst (`b_von_ic`, onsemi typisch 270/520/300 bei 10 µA/2 mA/100 mA): $B$ = 122 bei 1 µA, 260 bei 10 µA, 500 bei 2 mA, 487 bei 10 mA, 285 bei 100 mA Kollektorstrom.
- (c) Ausgangskennlinienfeld: $I_C$ in mA über $U_{CE}$ in V (0 bis 10 V) für $I_B$ = 2, 4, 6, 8, 10 µA (Tabelle im Zahlenwerk, z. B. für 4 µA 1,668 mA bei 0,2 V, 1,880 mA bei 0,5 V, 2,000 mA bei 5 V, 2,133 mA bei 10 V); gepunktet die Grenzlinie $U_{CB}$ = 0 (0,65 bis 0,70 V), gestrichelt $U_{CE,\mathrm{sat}}$ = 0,2 V; optional die Verlängerungen der Geraden bis −70 V (Early-Spannung).

*Kernaussage:* Eine Diodenkennlinie am Eingang, eine Gerade dazwischen, Stromquellenäste am Ausgang.

*Daten:* `ube_bei_ib`, `ic_bei_ib`, `b_von_ic`.

*Editor:*
- §4 Kennlinien, auch doppelt logarithmisch;
- §11 Datenkurven;
- §10 Teilbilder;
- §17 Ausschnitt nahe null optional.

**get1/bipolartransistoren/01-arbeitsgerade**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Modellkennlinien nach dem Skript: für $I_B$ = 2, 8, 20 µA waagrecht bei 1, 4 und 10 mA ab $U_{CE}$ = 0,2 V, darunter Gerade aus dem Ursprung. Dazu:
- die Arbeitsgerade von (10 V; 0) nach (0; 4,545 mA) für 2,2 kΩ an 10 V;
- die Arbeitspunkte (7,8 V; 1,0 mA), (1,2 V; 4,0 mA) und (0,2 V; 4,455 mA);
- die Bereiche hinterlegt: Sperrbereich unten, aktiver Bereich, Sättigung links von 0,2 V;
- Grenze bei $I_B$ = 8,91 µA markiert.

*Kernaussage:* Auf der Arbeitsgeraden wandert der Transistor vom Sperren über den aktiven Bereich in die Sättigung; dort ändert mehr Basisstrom den Kollektorstrom nicht.

*Daten:* Abschnitt „Arbeitsbereiche“ in `bericht()`.

*Editor:*
- §4 Kennlinienfeld mit Gerade;
- §7 hinterlegte Bereiche;
- §15 Regler für $I_B$ (Punkt wandert und bleibt in der Sättigung stehen);
- §8 Animation.

**get1/bipolartransistoren/01-saettigung-fluesse**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Querschnitt wie 01-npn-querschnitt, jetzt in der Sättigung bei 20 µA Basisstrom:
- $U_{BE}$ = 0,696 V, $U_{BC}$ = 0,552 V, $U_{CE}$ = 0,144 V;
- Elektronenstrom vom Emitter zum Kollektor rund 4,5 mA (Klemme 4,48 mA);
- Basisstrom 20 µA, davon 9,6 µA für die Verluste durch Rückinjektion und Rekombination und 10,4 µA als Löcher über den Basis-Kollektor-Übergang in den Kollektor (roter Pfeil);
- Einschub $n(x)$: am Kollektorrand 0,4 % der Randdichte am Emitter.

*Kernaussage:* In der Sättigung fließt der überschüssige Basisstrom in den Kollektor ab, statt den Kollektorstrom zu erhöhen.

*Daten:* „Elektronendichte in der Basis: aktiv gegen Sättigung“ in `bericht()`.

*Editor:*
- §6 Querschnitt;
- §2 Pfeile;
- §18 Mengenpfeile;
- §10 Einschub.

**get1/bipolartransistoren/01-led-schalter**
- Fassung: kompakt Abb. 7, ausführlich Abb. 9 (jeweils im Beispiel).
- Status: offen.

*Inhalt:* Schaltplan: Mikrocontroller-Ausgang (3,3 V) über $R_B$ = 12 kΩ an die Basis eines BC547C; Emitter an Masse; Kollektor über $R_C$ = 150 Ω und eine rote Leuchtdiode (2,0 V) an +5 V. Eingetragen: $I_B$ = 0,217 mA, $I_C$ = 18,7 mA, $U_{CE}$ ≈ 0,1 V.

*Kernaussage:* Ein Ausgangsstrom von einem Prozent des Laststroms schaltet die Leuchtdiode.

*Daten:* Abschnitt „Schalter“ in `bericht()`.

*Editor:*
- §1 Symbole npn-Transistor, Leuchtdiode, Logikausgang;
- §2 Strompfeile mit Werten.

## ET1 Kap. 11: Arbeitspunkt und Grundschaltungen des Transistors
Zahlenwerk: `notizen/get1/zahlen_transistor.py` (derselbe Beispieltransistor), Funktionen `ap_einfach_basis`, `ap_voll_basis`, `ap_einfach_stromgk`, `ap_voll_stromgk`, `ap_einfach_spannungsgk`, `ap_voll_spannungsgk`, `spiegel_voll`, `inverter_voll`, `kollektorschaltung_voll`, `basisschaltung_re_voll`, Grenzwerte im Wörterbuch `BC547`, Bericht `bericht_arbeitspunkt()`.

**get1/bipolartransistoren/02-arbeitsgerade-grenzen**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder, weil die Maßstäbe weit auseinanderliegen.
- (a) Ausgangskennlinienfeld, $U_{CE}$ 0 bis 12 V, $I_C$ 0 bis 6 mA, Scharparameter $I_B$ = 2, 4, 6, 8, 10 µA; Arbeitsgerade 10 V / 2,2 kΩ von (10 V; 0) nach (0; 4,55 mA); Arbeitspunkt (5,1 V; 2,23 mA) markiert; die Endpunkte als „gesperrt“ (10 V) und „gesättigt“ (0,2 V; 4,45 mA) beschriftet.
- (b) $U_{CE}$ 0 bis 50 V, $I_C$ 0 bis 160 mA: senkrechte Grenze bei 45 V, waagrechte bei 100 mA, Hyperbel 625 mW (62,5 mA bei 10 V, 13,9 mA bei 45 V), erlaubter Bereich hell hinterlegt; die Gerade aus (a) nahe am Ursprung; zweite Gerade 30 V / 200 Ω bis 150 mA, ihr Abschnitt außerhalb rot; größte Leistung dieser Geraden 1,125 W bei 15 V und 75 mA markiert.

*Kernaussage:* Der Arbeitspunkt ist der Schnittpunkt von Kennlinie und Arbeitsgerade; jede Gerade muss in den Grenzen bleiben.

*Daten:* Kennlinien aus `ic_bei_ib`; Gerade, Mitte (11,36 mW) und Grenzen aus `bericht_arbeitspunkt()` und `BC547`.

*Editor:*
- §4 Kennlinienschar, Arbeitsgerade mit Schnittpunkt, Bereich hinterlegen;
- §11 Datenkurven;
- §10 Teilbilder;
- §15 Schieberegler optional: $R_C$ dreht die Gerade, der Arbeitspunkt wandert.

**get1/bipolartransistoren/02-ersatzschaltbilder**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei Teilbilder nebeneinander, jeweils oben das Ersatzschaltbild zwischen den Klemmen B, C, E, darunter die linearisierte Kennlinie.
- (a) Sperrbereich: alle drei Klemmen offen.
- (b) Aktiver Bereich: B–E Spannungsquelle 0,6 V; C–E gesteuerte Stromquelle $B\,I_B$ (Rautensymbol mit Pfeil).
- (c) Sättigung: B–E wie (b); C–E Spannungsquelle 0,2 V.
- Kennlinien: Eingang $I_B$ über $U_{BE}$ mit Knick bei 0,6 V; Steuerkennlinie $I_C$ über $I_B$ mit Steigung $B$, ab der Sättigung waagrecht; Ausgang $I_C$ über $U_{CE}$ mit senkrechtem Ast bei 0,2 V und waagrechten Linien $B\,I_B$.

*Kernaussage:* In jedem Bereich wird der Transistor zu Quellen, mit denen man wie in jedem linearen Netz rechnet.

*Editor:*
- §1 Symbole Spannungsquelle, gesteuerte Stromquelle, offene Klemmen;
- §4 stückweise lineare Kennlinien;
- §10 Teilbilder;
- §7 Rahmen um das Ersatzschaltbild.

**get1/bipolartransistoren/02-einstellungen**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Schaltpläne an 10 V, gleicher Maßstab.
- (a) $R_B$ = 2,2 MΩ von +10 V zur Basis, $R_C$ = 2,2 kΩ, Emitter an Masse.
- (b) Teiler $R_1$ = 330 kΩ / $R_2$ = 68 kΩ an der Basis, $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ; daneben gestrichelt umrahmt die Ersatzspannungsquelle $U_q$ = 1,71 V mit $R_i$ = 56,4 kΩ.
- (c) $R_B$ = 1 MΩ vom Kollektor zur Basis, $R_C$ = 2,2 kΩ.
- Zählpfeile $I_B$, $I_C$, $U_{CE}$ in allen drei.

*Kernaussage:* Drei Wege, den Basisstrom festzulegen, mit sehr verschiedener Abhängigkeit von $B$.

*Editor:*
- §1 Schaltplan mit npn-Symbol;
- §2 Zählpfeile;
- §7 gestrichelter Rahmen für die Ersatzquelle;
- §10 Teilbilder.

**get1/bipolartransistoren/02-gegenkopplung-kette**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Wirkungskreis aus vier Kästen mit Pfeilen im Uhrzeigersinn:
- „$I_C$ steigt“ (Auslöser daneben: wärmer oder größeres $B$);
- „Spannung an $R_E$ steigt“;
- „bei fester Basisspannung: $U_{BE}$ sinkt, Stufe am Basis-Emitter-Übergang wächst“;
- „$I_C$ sinkt zurück“, Pfeil zurück zum ersten Kasten mit Minuszeichen (Gegenkopplung).

*Kernaussage:* Jede Abweichung erzeugt ihre eigene Gegenwirkung.

*Editor:*
- §19 Wirkungskette als Kreis, Kästen mit Formeltext, Pfeile mit Vorzeichen;
- §8 Animation optional: Pfeile leuchten nacheinander auf.

**get1/bipolartransistoren/02-streuung-vergleich**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* $I_C$ über $B$ von 300 bis 1000, drei Kurven mit Legende (einfaches Modell, Schaltungen aus Abb. 3):
- Basiswiderstand: proportional, 1,28 mA bei 300 bis 4,27 mA bei 1000 (1,80 mA bei 420, 3,42 mA bei 800);
- Spannungsgegenkopplung: 1,70 bis 2,94 mA (2,05 mA bei 420, 2,72 mA bei 800);
- Stromgegenkopplung: 0,931 bis 1,048 mA (0,975 mA bei 420, 1,034 mA bei 800).
- Die Spanne des BC547C von 420 bis 800 hell hinterlegt, $B$ = 500 gestrichelt.

*Kernaussage:* Je stärker der Strom auf seine eigene Ansteuerung zurückwirkt, desto weniger zählt $B$.

*Daten:* `ap_einfach_basis`, `ap_einfach_spannungsgk`, `ap_einfach_stromgk` über $B$; Tabelle in `bericht_arbeitspunkt()`.

*Editor:*
- §4 mehrere Kurven mit Legende, Bereich hinterlegen;
- §11 Datenkurven.

**get1/bipolartransistoren/02-spannungsgk-kompromiss**
- Fassung: ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei gestapelte Diagramme über $R_B$ von 50 kΩ bis 2 MΩ, x logarithmisch, je eine Kurve für $B$ = 420 und $B$ = 800 (Spannungsgegenkopplung an 10 V, $R_C$ = 2,2 kΩ, einfaches Modell):
- oben $I_C$: bei 100 kΩ 3,85 und 4,04 mA, bei 1 MΩ 2,05 und 2,72 mA;
- unten $U_{CE}$: bei 100 kΩ 1,52 und 1,10 V, bei 1 MΩ 5,48 und 4,00 V; Sättigungsgrenze 0,2 V und Mitte 5,1 V als waagrechte Hilfslinien.
- Senkrechte Markierungen bei 100 kΩ und 1 MΩ durch beide Diagramme.

*Kernaussage:* Unabhängigkeit von $B$ gibt es bei dieser Schaltung nur nahe der Sättigung.

*Daten:* `ap_einfach_spannungsgk` über $R_B$; Empfindlichkeit 0,043 bis 0,645 aus `bericht_arbeitspunkt()`.

*Editor:*
- §13 gestapelte Diagramme mit gemeinsamer x-Achse;
- §12 logarithmische x-Achse;
- §11 Datenkurven;
- §15 Schieberegler optional für $R_B$.

**get1/bipolartransistoren/02-stromspiegel**
- Fassung: kompakt Abb. 4, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan wie Skript Bild 11.15: +10 V, $R_\mathrm{ref}$ = 10 kΩ zum Kollektor von $T_1$, Kollektor und Basis von $T_1$ verbunden, Basen verbunden, Emitter an Masse; $T_2$ mit Last $R_L$ an +10 V; Ströme $I_\mathrm{ref}$, $I_{C1}$, $I_{B1}$, $I_{B2}$, $I_{C2}$ als Pfeile.
- (b) $I_{C2}$ über $U_{CE2}$ von 0 bis 10 V (vollständiges Modell) und waagrecht $I_\mathrm{ref}$ = 0,935 mA: 0,926 mA bei 0,3 V, 0,935 mA bei 1 V, 0,988 mA bei 5 V, 1,054 mA bei 10 V; Bereich unter 0,3 V als Sättigung hinterlegt.

*Kernaussage:* Der Spiegel liefert den Referenzstrom an jede Last, solange $T_2$ im aktiven Bereich bleibt.

*Daten:* `spiegel_voll` über $U_{CE2}$; Verhältnisse 0,991 / 1,0006 / 1,057 / 1,1275 aus `bericht_arbeitspunkt()`.

*Editor:*
- §1 Schaltplan mit zwei npn-Symbolen;
- §2 Strompfeile;
- §4 Kurve mit waagrechter Bezugslinie und hinterlegtem Bereich;
- §11 Datenkurve;
- §10 Teilbilder;
- §15 Schieberegler optional: $R_L$ verschiebt den Arbeitspunkt auf der Kurve.

**get1/bipolartransistoren/02-inverter**
- Fassung: kompakt Abb. 5, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan wie Skript Bild 11.16: Eingang über $R_B$ = 10 kΩ an die Basis, $R_C$ = 1 kΩ an +5 V, Ausgang am Kollektor.
- (b) $U_\mathrm{aus}$ über $U_\mathrm{ein}$ von 0 bis 2 V. Modell durchgezogen: 5 V bis 0,6 V, Gerade mit Steigung −50 bis 0,2 V bei 0,696 V, danach 0,2 V. Vollständiges Modell gestrichelt: 4,890 V bei 0,60 V, 4,459 V bei 0,65 V, 3,405 V bei 0,70 V, 1,894 V bei 0,75 V, 0,250 V bei 0,80 V, 0,129 V bei 1 V, 0,084 V bei 2 V. Die drei Bereiche (Sperrbereich, aktiv, Sättigung) als Streifen hinterlegt.

*Kernaussage:* Der Arbeitspunkt durchläuft alle drei Bereiche; zwischen den Pegeln liegt ein schmaler Übergang.

*Daten:* `inverter_voll`; Modellkante 0,714 / 0,696 / 0,660 V für $B$ = 420 / 500 / 800.

*Editor:*
- §1 Schaltplan;
- §4 zwei Kurven, Bereiche hinterlegen;
- §11 Datenkurve;
- §10 Teilbilder;
- §15 Schieberegler optional: $U_\mathrm{ein}$ bewegt den Arbeitspunkt zugleich im Kennlinienfeld.

**get1/bipolartransistoren/02-grundschaltungen**
- Fassung: kompakt Abb. 6, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Drei Spalten, oben Schaltplan, unten Gleichspannungskennlinie (vollständiges Modell), alle an 5 V; der gemeinsame Anschluss farbig hervorgehoben.
- (a) Emitterschaltung: Eingang über 10 kΩ an der Basis, $R_C$ = 1 kΩ; Kennlinie wie Abb. 02-inverter (b).
- (b) Kollektorschaltung: Kollektor an +5 V, Eingang an der Basis, $R_E$ = 1 kΩ nach Masse, Ausgang am Emitter; $U_\mathrm{aus}$ über $U_\mathrm{ein}$ von 0 bis 5 V: 1,337 V bei 2 V, 4,306 V bei 5 V, Steigung 0,985; Hilfslinie $U_\mathrm{aus} = U_\mathrm{ein}$.
- (c) Basisschaltung: Basis an Masse, Eingang über 1 kΩ am Emitter, $R_C$ = 1 kΩ; $U_\mathrm{ein}$ von −5 bis 0 V: 0,703 V bei −5 V, 1,693 V bei −4 V, 2,682 V bei −3 V, 3,665 V bei −2 V, 4,630 V bei −1 V, 5 V ab etwa −0,5 V; Steigung 0,98.

*Kernaussage:* Welcher Anschluss Ein- und Ausgang gemeinsam ist, bestimmt, ob die Schaltung umkehrt, folgt oder nicht umkehrend überträgt.

*Daten:* `inverter_voll`, `kollektorschaltung_voll`, `basisschaltung_re_voll`.

*Editor:*
- §1 Schaltpläne;
- §7 Hervorhebung des gemeinsamen Anschlusses;
- §4 Kennlinien mit Hilfslinie;
- §11 Datenkurven;
- §10 Teilbilder im Raster 3 × 2.

## ET1 Kap. 11: Der Transistor als Verstärker
Zahlenwerk: `notizen/get1/zahlen_transistor.py` (derselbe Beispieltransistor; Z-Diode wie in `zahlen_halbleiter.py`), Funktionen `kleinsignal`, `stufe_ap`, `stufe_mit_ce`, `stufe_ohne_ce`, `stufe_teil`, `harmonische`, `stabilisierung`, `nur_z_diode`, dazu `stroeme`, `ube_bei_ib`, `ic_bei_ib`, `kollektorschaltung_voll`; Bericht `bericht_verstaerker()` (Abschnitt „Thema 03“).

**get1/bipolartransistoren/03-verstaerkerstufe**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan: +10 V; $R_1$ = 330 kΩ von +10 V zur Basis, $R_2$ = 68 kΩ von der Basis nach Masse; $R_C$ = 3,9 kΩ; $R_E$ = 1 kΩ parallel $C_E$ = 470 µF; Signalquelle über $C_1$ = 1 µF an der Basis; Ausgang über $C_2$ = 1 µF am Kollektor. Ruhewerte an den Knoten: Basis 1,602 V, Emitter 0,949 V, Kollektor 6,306 V, $I_C$ = 0,947 mA.
- (b) Drei gestapelte Zeitverläufe über 2 ms bei 1 kHz: Basispotenzial 1,602 V ± 1 mV; Kollektorpotenzial 6,306 V ± 136 mV, gegenphasig; Ausgang hinter $C_2$ ± 136 mV um null. Signale blau, Ruhewerte als graue gestrichelte Linien.

*Kernaussage:* Eine Änderung von einem Millivolt an der Basis erscheint 136-fach vergrößert und umgekehrt am Kollektor.

*Daten:* `stufe_ap()`, `stufe_mit_ce(d, ap)` für d = 1 mV · sin.

*Editor:*
- §1 Schaltplan mit npn, Kondensatoren, Quelle;
- §5 Zeitverläufe, gestapelt;
- §13 gemeinsame Zeitachse;
- §10 Teilbilder;
- §8 Animation optional: Punkt läuft synchron durch die drei Verläufe.

**get1/bipolartransistoren/03-tangente**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* $I_C$ über $U_{BE}$ von 0,60 bis 0,70 V (vollständiges Modell bei $U_{CE}$ = 5,36 V), Arbeitspunkt (0,653 V; 0,947 mA) markiert, Tangente mit 36,6 mS gestrichelt orange. Unter der U-Achse zwei Eingangssinusse (1 mV und 10 mV Amplitude, Zeitachse nach unten), rechts die Stromverläufe: bei 1 mV +3,94 %/−3,79 %, bei 10 mV +47,2 %/−32,1 % des Ruhestroms; bei 10 mV die Tangentenwerte (±38,7 %) gestrichelt daneben.

*Kernaussage:* Im Kleinen ist die Kennlinie eine Gerade, im Großen verzerrt sie das Signal.

*Daten:* `stroeme`; Prozentwerte aus `bericht_verstaerker()` („Kleinsignal: …“).

*Editor:*
- §4 Kennlinie mit Tangente und Arbeitspunkt;
- §5 Signalprojektion über die Kennlinie (Eingangssinus unten, Ausgangssinus rechts);
- §11 Datenkurve;
- §15 Schieberegler für die Eingangsamplitude (0,5 bis 20 mV), die Asymmetrie wächst sichtbar.

**get1/bipolartransistoren/03-reale-kennlinien**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei Teilbilder nach Skript Bild 11.19/11.20.
- (a) $I_B$ über $U_{BE}$ (0,55 bis 0,72 V, 0 bis 12 µA): idealisiert grau (senkrecht bei 0,6 V), real rot (Exponentialkurve); Tangente im Arbeitspunkt (0,673 V; 4 µA) gestrichelt, Schnitt mit der Achse bei 0,647 V markiert, Steigung 1/(6,46 kΩ).
- (b) $I_C$ über $U_{CE}$ (−75 bis 12 V, mit abgesetztem negativem Teil bzw. Achsenbruch): idealisiert waagrecht ab 0,2 V (grau), real für $I_B$ = 2, 4, 6, 8 µA leicht steigend (rot); Verlängerungen gestrichelt bis zum gemeinsamen Punkt −70 V; Steigung im Punkt 2 mA/5 V als 1/(37,5 kΩ) beschriftet.

*Kernaussage:* Die realen Kennlinien haben endliche Steigungen; ihre Kehrwerte sind der Eingangs- und der Ausgangswiderstand.

*Daten:* `ube_bei_ib`, `stroeme`; Tangente aus `bericht_verstaerker()` (U_0 = 646,9 mV).

*Editor:*
- §4 Kennlinien und Kennlinienschar, Tangente;
- §17 Achsenbruch für den Bereich bis −70 V;
- §10 Teilbilder;
- §11 Datenkurven.

**get1/bipolartransistoren/03-ersatzschaltbilder**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Schaltbilder nebeneinander, Klemmen B, C, E.
- (a) erweitertes Ersatzschaltbild (Skript Bild 11.21) mit Tangentenwerten: B–E Spannungsquelle 0,647 V in Reihe mit 6,46 kΩ; C–E gesteuerte Stromquelle 500 · $I_B$ − 0,133 mA parallel 37,5 kΩ.
- (b) Kleinsignal-Ersatzschaltbild: B–E $r_{BE}$ = 6,46 kΩ mit $u_{be}$ und $i_b$; C–E Stromquelle $g_m u_{be}$ (77,4 mS) = $\beta i_b$ (500) parallel $r_{CE}$ = 37,5 kΩ; Zählpfeile für $u_{ce}$, $i_c$.

*Kernaussage:* Für Änderungen fallen die festen Quellen weg; übrig bleiben Eingangswiderstand, gesteuerte Quelle und Ausgangswiderstand.

*Daten:* `bericht_verstaerker()` (Datenblattpunkt).

*Editor:*
- §1 Spannungs- und gesteuerte Stromquelle, Widerstände, Klemmen;
- §2 Zählpfeile;
- §10 Teilbilder;
- §8 Animation optional: die feste Quelle in (a) wird beim Übergang zu (b) durch einen Kurzschluss ersetzt.

**get1/bipolartransistoren/03-signalweg**
- Fassung: kompakt Abb. 5, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Kleinsignal-Ersatzschaltbild der Stufe mit $C_E$: Quelle $u_\mathrm{ein}$; parallel zum Eingang 330 kΩ, 68 kΩ und $r_{BE}$ = 13,7 kΩ; Stromquelle $g_m u_{be}$ (36,6 mS); am Ausgang $r_{CE}$ = 79,6 kΩ und $R_C$ = 3,9 kΩ parallel nach Masse. Entlang des Signalwegs Pfeile mit den Werten für 1 mV: 1 mV → 36,6 µA → −136 mV. Kondensatoren und Versorgung als Kurzschlüsse angedeutet (blasse Symbole mit Verbindungslinie).

*Kernaussage:* Die Verstärkung ist die Steilheit mal dem Widerstand, in den die Stromänderung fließt.

*Daten:* `bericht_verstaerker()` (Verstärkerstufe).

*Editor:*
- §1 Schaltplan;
- §2 Pfeile mit Werten;
- §19 Wirkungskette entlang des Signalwegs;
- §7 Hervorhebung der kurzgeschlossenen Bauteile.

**get1/bipolartransistoren/03-emitterwiderstand**
- Fassung: kompakt Abb. 6, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Übertragungskennlinien, Änderung des Kollektorpotenzials über der Änderung des Basispotenzials (vollständiges Modell): mit $C_E$ von −10 bis +10 mV (Steigung −136; −1,63 V bei +10 mV, +1,15 V bei −10 mV); ohne $C_E$ von −263 bis +263 mV (Steigung −3,78; −1,00 V und +0,99 V). Zwei x-Maßstäbe, deshalb zwei Teilachsen übereinander oder normierte x-Achse (Eingang geteilt durch Eingang für 1 V Ausgang).
- (b) Ausgangsspannung über eine Periode bei 1 V Amplitude: mit $C_E$ aus 7,34 mV, −1,14 V/+0,88 V, Klirrfaktor 6,4 %; ohne $C_E$ aus 263 mV, −1,00 V/+0,99 V, 0,18 %; idealer Sinus grau gestrichelt.

*Kernaussage:* Der Emitterwiderstand tauscht Verstärkung gegen Linearität.

*Daten:* `stufe_mit_ce`, `stufe_ohne_ce`, `harmonische`.

*Editor:*
- §4 zwei Kennlinien;
- §5 Zeitverläufe;
- §11 Datenkurven;
- §10 Teilbilder;
- §15 Schieberegler für den überbrückten Anteil von $R_E$ (0 bis 1 kΩ im Signalweg).

**get1/bipolartransistoren/03-grundschaltungen-kleinsignal**
- Fassung: kompakt Abb. 7, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Drei Kleinsignal-Ersatzschaltbilder nebeneinander, Transistor jeweils als $r_{BE}$, $g_m u_{be}$ (36,6 mS), $r_{CE}$; Ruhestrom 0,947 mA, $\beta$ = 502.
- (a) Emitterschaltung: Emitter an Masse, $R_C$ = 3,9 kΩ; Werte −136, 13,7 kΩ, 3,72 kΩ.
- (b) Kollektorschaltung: Kollektor an Masse, $R_E$ = 3,9 kΩ am Emitter (für Signale parallel $r_{CE}$), Quelle mit 10 kΩ; Werte 0,993, 1,88 MΩ, 47,2 Ω.
- (c) Basisschaltung: Basis an Masse, Eingang am Emitter, $R_C$ = 3,9 kΩ; Werte +136, 27,2 Ω, 3,72 kΩ.
Gemeinsamer Anschluss jeweils farbig hervorgehoben.

*Kernaussage:* Welcher Anschluss gemeinsam ist, bestimmt, wie Spannung, Strom und Widerstände übertragen werden.

*Daten:* `bericht_verstaerker()` („Grundschaltungen im Kleinsignal …“).

*Editor:*
- §1 Ersatzschaltbilder;
- §7 Hervorhebung des gemeinsamen Anschlusses, Wertetafeln;
- §10 Teilbilder.

**get1/bipolartransistoren/03-stabilisierung**
- Fassung: kompakt Abb. 8, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan wie Skript Bild 11.28: Eingang $U_\mathrm{ein}$ (12 V ± 1 V); $R_1$ = 1 kΩ von der Eingangsschiene zur Basis; Z-Diode 5,6 V von der Basis nach Masse; npn mit Kollektor an der Eingangsschiene, Emitter = Ausgang; Last 200 Ω. Zählpfeile $U_Z$ (Basisknoten nach Masse), $U_{BE}$ (Basis zum Emitter), $U_\mathrm{aus}$; Werte 5,627 V, 0,737 V, 4,890 V; Ströme 24,5 mA, 48 µA, 6,3 mA.
- (b) Zwei gestapelte Zeitverläufe über 40 ms mit Brummen (Sägezahn wie hinter einem Gleichrichter, 100 Hz): oben $U_\mathrm{ein}$ 11 bis 13 V; unten $U_\mathrm{aus}$ 4,870 bis 4,910 V (eigener Maßstab) und gestrichelt die Z-Diode allein (330 Ω, 200 Ω Last) mit 4,15 bis 4,91 V.

*Kernaussage:* Der Transistor gibt die Spannung der Z-Diode, um $U_{BE}$ vermindert, an die Last weiter; das Brummen wird 50-mal kleiner.

*Daten:* `stabilisierung(U_ein, 1e3, 200)`, `nur_z_diode(U_ein, 330, 200)` über den Verlauf von $U_\mathrm{ein}$.

*Editor:*
- §1 Schaltplan mit Z-Diode und npn;
- §2 Zählpfeile;
- §5 Zeitverläufe;
- §13 gestapelt mit gemeinsamer Zeitachse;
- §10 Teilbilder;
- §15 Schieberegler optional für die Last.

**get1/bipolartransistoren/03-lastkennlinie**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* $U_\mathrm{aus}$ über $I_L$ (logarithmisch, 0,5 bis 50 mA) bei 12 V Eingang. Längsregler: 4,991 V (0,50 mA), 4,950 V (2,47 mA), 4,932 V (4,93 mA), 4,914 V (9,83 mA), 4,901 V (16,3 mA), 4,890 V (24,5 mA), 4,882 V (32,6 mA), 4,871 V (48,7 mA); Steigung 60 mV je Zehnfaches. Z-Diode allein mit 330 Ω: 5,860 V (0,59 mA), 5,763 V (5,76 mA), 5,658 V (11,3 mA), 5,524 V (18,4 mA), 5,172 V (20,7 mA), 4,528 V (22,6 mA), 2,791 V (27,9 mA); Knick bei 19,7 mA markiert.

*Kernaussage:* Der Transistor liefert den Laststrom; die Ausgangsspannung hängt nur noch über $U_{BE}$ schwach von ihm ab.

*Daten:* `bericht_verstaerker()` („Lastkennlinie bei 12 V …“).

*Editor:*
- §4 zwei Kurven;
- §12 logarithmische x-Achse;
- §11 Datenkurven.
