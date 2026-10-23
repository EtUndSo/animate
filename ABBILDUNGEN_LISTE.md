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
- benötigte Editor-Funktionen mit Verweis auf die Abschnitte in `EDITOR_GRAFIK_FEATURES.md` (§1 bis §30);
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

## ET1 Kap. 12: Der Operationsverstärker – idealer OPV und Rückkopplung
Zahlenwerk: `notizen/get1/zahlen_opv.py` (neu; Beispiel-OPV nach Art des 741 an ±15 V: $v_D$ = 200 000, mindestens 50 000, $f_T$ = 1 MHz, 0,5 V/µs, ±14 V, 23 nV/√Hz; Differenzverstärker mit dem Beispieltransistor aus `zahlen_transistor.py`), Funktionen `u_therm`, `u_ktc`, `enbw_rc`, `i_schrot`, `u_1f`, `diffpaar`, `a_geschlossen`, `sim`, `schmitt_kette`; Ausgabe `zahlen_opv.txt`.

**get1/operationsverstaerker/01-opv-kennlinie**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltsymbol des OPV (Dreieck): links Pluseingang (nichtinvertierend) und Minuseingang (invertierend), Zählpfeil $U_D$ vom Plus- zum Minuseingang; rechts Ausgang mit $U_A$ gegen Masse; oben +15 V, unten −15 V.
- (b) $U_A$ über $U_D$ von −200 µV bis +200 µV (x in µV, y in V von −16 bis +16 V): Gerade mit Steigung 200 000 zwischen −70 µV und +70 µV, außerhalb waagrecht bei ±14 V; ±15 V grau gestrichelt; der lineare Bereich ±70 µV hellgrau hinterlegt und beschriftet.

*Kernaussage:* Proportional zur Differenz ist der Ausgang nur in einem Fenster von ±70 µV; außerhalb meldet er nur ihr Vorzeichen.

*Daten:* `bericht_opv()` (linearer Bereich 70 µV, bei $v_D$ min 280 µV).

*Editor:*
- §1 OPV-Symbol mit Zählpfeilen;
- §4 Kennlinie mit Sättigung und hinterlegtem Bereich;
- §10 Teilbilder;
- §15 optional: Schieberegler für $v_D$ (50 000 bis 1 000 000), das Fenster wird schmaler.

**get1/operationsverstaerker/01-rauschen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Rauschspannung eines 10-kΩ-Widerstands bei 300 K, Bandbreite 1 MHz, über 20 µs (y in µV, etwa ±45 µV): unregelmäßiger Verlauf um null mit festem Zufallsstartwert; waagrechte Linien bei ±12,9 µV (Effektivwert), beschriftet.
- (b) Rauschdichte in nV/√Hz über der Frequenz 0,1 Hz bis 1 MHz, beide Achsen logarithmisch: Widerstand 10 kΩ waagrecht bei 12,9 nV/√Hz (blau); Beispiel-OPV 23 nV/√Hz mit 1/f-Anstieg unterhalb der Eckfrequenz 100 Hz (rot), Stützwerte 231 nV/√Hz bei 1 Hz, 76 bei 10 Hz, 32,5 bei 100 Hz, 24,1 bei 1 kHz; Eckfrequenz markiert.

*Kernaussage:* Den Verlauf des Rauschens kann man nicht vorhersagen, seine Größe aber genau angeben: als Effektivwert und als Dichte über der Frequenz.

*Daten:* `u_therm`, Dichte des OPV aus `bericht_rauschen()` („Dichte bei …“); Zeitverlauf als gefiltertes Zufallssignal mit 12,9 µV Effektivwert.

*Editor:*
- §21 Rausch- und Zufallssignale (neu);
- §4 doppeltlogarithmische Achsen;
- §10 Teilbilder.

**get1/operationsverstaerker/01-messkette**
- Fassung: ausführlich Abb. 3 (im Beispiel).
- Status: offen.

*Inhalt:* Blockschaltbild in zwei Zeilen.
- Oben: Sensor (1 mV, 10 kΩ, Rauschen 1,82 µV, SNR 54,8 dB) → Vorverstärker (eigenes Rauschen 3,25 µV auf den Eingang bezogen, ×100; dahinter 100 mV, 373 µV, SNR 48,6 dB) → Folgestufe (+1 mV Rauschen; SNR 39,4 dB).
- Unten: Sensor direkt an die Folgestufe: SNR 0 dB.
- Unter jedem Block ein kleiner Balken für Signal (blau) und Rauschen (grau) im logarithmischen Maßstab.

*Kernaussage:* Der Verstärker verschlechtert das Verhältnis an seiner Stelle, schützt das Signal aber vor dem Rauschen dahinter.

*Daten:* `bericht_rauschen()` Punkt 6.

*Editor:*
- §19 Blockbilder mit Werten an Kästen und Pfeilen;
- §12 logarithmischer Maßstab für die Pegelbalken.

**get1/operationsverstaerker/01-differenzverstaerker**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan nach Skript Bild 12.1 mit Werten, abweichend vom Skript mit dem Emitter von Q3 an −15 V statt an Masse: Q1, Q2 (npn) mit je $R_C$ = 10 kΩ an +15 V; Emitter verbunden, Stromquelle 1 mA (Q3) nach −15 V; Eingänge $U_{e1}$, $U_{e2}$ an den Basen; $U_A$ zwischen den Kollektoren, Zählpfeil von Q1 nach Q2. Ruhewerte: je 0,499 mA, Kollektoren 10,0 V, Emitterknoten −0,635 V.
- (b) $I_{C1}$ (rot) und $I_{C2}$ (blau) in mA über $U_{e1} - U_{e2}$ von −150 bis +150 mV: gegenläufige S-Kurven, Kreuzung bei 0 mV und 0,5 mA; Summe 1 mA als graue Linie; Tangente im Nullpunkt mit 9,67 mS gestrichelt; Punkte bei ±100 mV (98 % und 2 %) und ±25,85 mV (73 %) markiert.

*Kernaussage:* Die Stromquelle hält die Summe fest, die Differenz der Eingänge verteilt sie.

*Daten:* `diffpaar(u, 0)` (vollständiges Modell), Formel $I_0/(1 + \exp(-u/U_T))$ zum Vergleich; Tabelle in `bericht_differenz()`.

*Editor:*
- §1 Schaltplan mit npn-Transistoren und Stromquelle;
- §4 zwei Kurven mit Tangente und markierten Punkten;
- §11 Datenkurven;
- §10 Teilbilder;
- §15 optional: Schieberegler für $U_{e1} - U_{e2}$, die Stromstärke in den Zweigen als Pfeilbreite (§18).

**get1/operationsverstaerker/01-gleichtakt**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Die Schaltung aus 01-differenzverstaerker dreimal nebeneinander, beide Eingänge auf −5 V, 0 V und +5 V. An den Knoten: Emitterknoten −5,633 V / −0,635 V / +4,363 V; Kollektorströme je 0,499 mA (Änderung 0,01 %); $U_A$ = 0. Die Basis-Emitter-Spannung (0,635 V) in allen drei Bildern als gleich langer Maßpfeil.

*Kernaussage:* Der Emitterknoten folgt dem Gleichtakt; die Basis-Emitter-Spannungen und damit die Ströme bleiben.

*Daten:* `diffpaar(ug, ug)` für −5, 0, +5 V.

*Editor:*
- §1 Schaltplan;
- §10 drei Teilbilder nebeneinander;
- §2 Maßpfeile;
- §8 optional: Animation, beide Eingänge wandern gemeinsam, der Emitterknoten folgt.

**get1/operationsverstaerker/01-flash-wandler**
- Fassung: ausführlich Abb. 6 (im Beispiel).
- Status: offen.

*Inhalt:* Schaltplan: vier gleiche Widerstände 1 kΩ zwischen $U_{Ref}$ = 2 V und Masse, Abgriffe 1,5 V, 1,0 V, 0,5 V an den Minuseingängen von drei Komparatoren (OPV-Symbole); $U_E$ = 1,2 V an allen Pluseingängen. Ausgänge von oben nach unten −14 V, +14 V, +14 V, beschriftet 0, 1, 1. Daneben eine Skala 0 bis 2 V mit den vier Bereichen und den Binärwerten 00 bis 11, Bereich 1,0–1,5 V (10) markiert.

*Kernaussage:* Die Zahl der Komparatoren, die „hoch“ zeigen, ist der Messwert.

*Daten:* `bericht_opv()` (Flash-Wandler).

*Editor:*
- §1 Schaltplan mit mehreren OPV-Symbolen;
- §7 Beschriftungen und Markierung des Bereichs;
- §15 optional: Schieberegler für $U_E$, die Ausgänge schalten mit.

**get1/operationsverstaerker/01-gegen-mit**
- Fassung: kompakt Abb. 4, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zwei Schaltpläne nebeneinander aus denselben Bauteilen ($R_2$ = 90 kΩ Ausgang–Teilerknoten, $R_1$ = 10 kΩ Teilerknoten–Masse).
- Links Gegenkopplung (nichtinvertierender Verstärker): Teilerknoten am Minus-, $U_E$ am Pluseingang. Darunter Wirkungskette: „$U_A$ ↑ → Minuseingang ↑ (ein Zehntel) → $U_D$ ↓ → $U_A$ steigt langsamer“, mit Minuszeichen am Rückweg.
- Rechts Mitkopplung (invertierender Schmitt-Trigger nach Skript Bild 12.6): Teilerknoten am Plus-, $U_E$ am Minuseingang. Kette: „$U_A$ ↑ → Pluseingang ↑ → $U_D$ ↑ → $U_A$ steigt schneller“, mit Pluszeichen.
- Der Rückkopplungsweg jeweils orange hervorgehoben.

*Kernaussage:* Welcher Eingang das zurückgeführte Signal bekommt, entscheidet, ob die Schaltung regelt oder kippt.

*Daten:* keine Kurven; Werte aus `bericht_rueckkopplung()`.

*Editor:*
- §1 Schaltplan mit OPV;
- §19 Wirkungsketten mit Vorzeichen;
- §7 Hervorhebung des Rückkopplungswegs;
- §10 Teilbilder.

**get1/operationsverstaerker/01-einschwingen**
- Fassung: kompakt Abb. 5, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Gegenkopplung, $k$ = 0,1, Eingangssprung 0 → 10 mV bei $t$ = 0 (klein gegen 80 mV, damit die Eingangsstufe linear arbeitet). Oben $U_A$ in mV über $t$ von 0 bis 12 µs: Anstieg auf 0,1 V (99,995 mV), 63 % bei 1,59 µs markiert, 0,1 %-Band ab 11 µs; Anfangstangente 63 mV/µs gestrichelt. Darunter, gemeinsame Zeitachse, $U_D$ logarithmisch von 10 mV bis 5,8 µV bei 12 µs; Endwert 0,5 µV gestrichelt.
- (b) Mitkopplung (Schmitt-Trigger, $U_E$ = 0), Start 0,13 mV am Ausgang, $t$ von 0 bis 50 µs, $U_A$ logarithmisch oder linear mit Ausschnitt: exponentielles Wachstum mit 1,59 µs, ab etwa 0,8 V linear mit 0,5 V/µs, 13 V nach 38 µs; gestrichelt der rein exponentielle Verlauf (13 V nach 18 µs).

*Kernaussage:* Gegenkopplung lässt jede Abweichung abklingen, Mitkopplung lässt sie mit derselben Zeitkonstante wachsen.

*Daten:* `sim("gegen", lambda t: 0.01, 12e-6, aufzeichnen=…)` und `sim("mit", lambda t: 0.0, 80e-6, ua0=1.3e-4, sr=True/False)`.

*Editor:*
- §5 Zeitverläufe mit markierter Zeitkonstante;
- §13 gestapelte Diagramme mit gemeinsamer Zeitachse;
- §12 logarithmische y-Achse;
- §11 Datenkurven;
- §8 optional: Animation, ein Punkt läuft auf der Kurve, daneben der Teilerknoten als Zahl.

**get1/operationsverstaerker/01-schmitt-kennlinie**
- Fassung: kompakt Abb. 6, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* $U_A$ über $U_E$ von −3 V bis +3 V (y von −16 bis +16 V): oberer Ast +14 V von links bis +1,4 V, senkrechter Sprung nach −14 V; unterer Ast −14 V von rechts bis −1,4 V, Sprung nach +14 V; Pfeile auf den Ästen und Sprüngen zeigen die Laufrichtung; Schwellen ±1,4 V beschriftet, Hysterese 2,8 V als Maßpfeil; Schwellen benannt als $U_{R1,\max}$ und $U_{R1,\min}$; gestrichelt die instabile Gerade $U_A = U_E/k$ (Steigung 10) zwischen −1,4 V und +1,4 V.

*Kernaussage:* Zwischen −1,4 V und +1,4 V hängt der Ausgang davon ab, von welcher Seite der Eingang kam.

*Daten:* `bericht_schmitt()` (Schwellen).

*Editor:*
- §20 Hystereseschleifen (neu);
- §2 Maßpfeile;
- §8 optional: Animation, ein Punkt läuft mit $U_E$ hin und zurück.

**get1/operationsverstaerker/01-schmitt-rauschen**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Drei gestapelte Zeitverläufe über 40 ms, gemeinsame Zeitachse.
- Oben: Eingang 3 V · cos(2π · 50 Hz · t) plus Rauschen 0,2 V eff., gleichmäßig verteilt bis 100 kHz (fester Zufallsstartwert 1, Abtastung 200 kHz); Linien bei 0 V und ±1,4 V.
- Mitte: idealer invertierender Komparator mit Schwelle 0 V: an jedem der vier Nulldurchgänge (5, 15, 25, 35 ms) ein Bündel von 43 bis 59 Umschaltungen innerhalb von 0,6 bis 0,8 ms; ein Bündel vergrößert als Lupe.
- Unten: Schmitt-Trigger ±1,4 V: genau ein Wechsel je Nulldurchgang, 0,91 bis 1,09 ms danach; gestrichelt markiert der Zeitpunkt ohne Rauschen, 1,55 ms (27,8°).

*Kernaussage:* Eine Hysterese, die größer ist als das Rauschen, verhindert das Mehrfachschalten.

*Daten:* `bericht_schmitt()` (Simulation, `schmitt_kette`).

*Editor:*
- §21 Rauschsignale mit festem Startwert;
- §5 Rechteck- und Zeitverläufe;
- §13 gestapelt;
- §7 Lupe auf ein Bündel.

## ET1 Kap. 12: Die OPV-Grundschaltungen
Zahlenwerk: `notizen/get1/zahlen_opv.py`, Abschnitt „Thema 02“, Funktionen `a_invertierend`, `a_nichtinvertierend`, `subtrahierer`, Bericht `bericht_grundschaltungen()`; Beispieldiode aus `zahlen_halbleiter.py` ($I_S$ = 1,457·10⁻¹⁴ A, `IS_von_T`, `spannung_real`); Beispiel-OPV wie in 12/01 (±14 V an ±15 V).

**get1/operationsverstaerker/02-invertierer**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltplan nach Skript Bild 12.7: $R_1$ = 10 kΩ, $R_2$ = 20 kΩ, Pluseingang an Masse; Quelle 1 V. Strompfeil 0,1 mA durch $R_1$ und $R_2$ (orange), am Minuseingang vorbei; Knotenwerte: Minuseingang 0 V („virtuelle Masse“), Ausgang −2 V.
- (b) Zeitverläufe über zwei Perioden: Eingang Sinus 5 V Amplitude (blau); Ausgang mit $R_2$ = 20 kΩ gegenphasig ±10 V (rot); Ausgang mit $R_2$ = 30 kΩ (rot gestrichelt) bei ±14 V abgeflacht von 69° bis 111° jeder Halbwelle; Grenzen ±14 V grau gestrichelt.

*Kernaussage:* Der Strom durch $R_1$ muss durch $R_2$; das Widerstandsverhältnis bestimmt die Verstärkung, bis der Ausgang an seine Grenze stößt.

*Daten:* `bericht_grundschaltungen()` (Invertierender Verstärker).

*Editor:*
- §1 Schaltplan mit OPV;
- §2 Strompfeile mit Wert;
- §5 Zeitverläufe mit Begrenzung;
- §10 Teilbilder;
- §15 optional: Schieberegler für $R_2$ (5 bis 40 kΩ), die Begrenzung setzt ab 28 kΩ ein.

**get1/operationsverstaerker/02-rechenschema**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Ablaufdiagramm nach Skript Bild 12.22: Start → Raute „mit- oder gegengekoppelt?“; Zweig mitgekoppelt → Kasten „$U_D$ ≠ 0, Ausgang meist an $U_{A,\min}$ oder $U_{A,\max}$“; Zweig gegengekoppelt → Raute „übersteuert?“; ja → „$U_D$ ≠ 0, Ausgang an einer Grenze“; nein → „$U_D$ = 0, Ausgang zwischen den Grenzen“; alle drei → Kasten „mit Ohmschem Gesetz und Kirchhoffschen Regeln rechnen“.

*Kernaussage:* Die Regel $U_D$ = 0 ist eine Folge der Gegenkopplung, keine Eigenschaft des Bauteils.

*Daten:* keine.

*Editor:*
- §19 Blockbilder mit Entscheidungsrauten (neu ergänzt).

**get1/operationsverstaerker/02-nichtinvertierer**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Schaltplan nach Skript Bild 12.10: $R_1$ = 10 kΩ nach Masse, $R_2$ = 20 kΩ vom Ausgang; 1 V am Pluseingang; Minuseingang 1 V, 0,1 mA durch beide Widerstände, Ausgang 3 V.
- (b) Impedanzwandler nach Bild 12.19: Ausgang am Minuseingang, $U_A = U_E$.
- (c) Messaufbau: Quelle 5 V mit 100 kΩ; links Messgerät 1 MΩ direkt, Anzeige 4,545 V; rechts mit Impedanzwandler davor, Anzeige 5,000 V (mit dem Ruhestrom des 741: 4,992 V).

*Kernaussage:* In den Pluseingang fließt kein Strom; die Quelle wird nicht belastet.

*Daten:* `bericht_grundschaltungen()` (Nichtinvertierender Verstärker, Impedanzwandler).

*Editor:*
- §1 Schaltpläne mit Messgerät-Symbol;
- §7 Anzeigewerte als Beschriftung;
- §10 Teilbilder.

**get1/operationsverstaerker/02-addierer-subtrahierer**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Addierer nach Bild 12.11: Eingänge über 10 kΩ, 20 kΩ, 40 kΩ an der virtuellen Masse, $R_4$ = 10 kΩ; Eingänge 5 V, 0 V, 5 V; Ströme 0,5 mA, 0, 0,125 mA mit Pfeilbreite proportional zum Strom (§18), Summe 0,625 mA durch $R_4$; Ausgang −6,25 V.
- (b) Subtrahierer nach Bild 12.12: $R_1$ = $R_3$ = 10 kΩ, $R_2$ = $R_4$ = 100 kΩ; $U_{E1}$ = 2,500 V, $U_{E2}$ = 2,505 V; beide OPV-Eingänge 2,2773 V; Ausgang 50 mV.

*Kernaussage:* An der virtuellen Masse addieren sich Ströme; der Subtrahierer verstärkt nur die Differenz, wenn die Widerstandsverhältnisse gleich sind.

*Daten:* `bericht_grundschaltungen()` (Addierer, Subtrahierer).

*Editor:*
- §1 Schaltpläne;
- §18 Mengenpfeile für die Ströme;
- §10 Teilbilder;
- §15 optional: Schalter für die drei Bits, der Ausgang springt in Stufen von 1,25 V.

**get1/operationsverstaerker/02-integrator**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei Teilbilder, je Schaltplan oben und Zeitverlauf darunter.
- (a) Integrator nach Bild 12.13 ($R$ = 10 kΩ, $C$ = 100 nF); Eingang Rechteck ±1 V, 1 kHz (blau); Ausgang Dreieck 0,5 V Spitze-Spitze (rot), fallend während +1 V, Steigung −1 V/ms beschriftet; Zeitachse 0 bis 3 ms.
- (b) Differenzierer nach Bild 12.14 (dieselben Bauteile vertauscht), ausdrücklich mit idealem OPV beschriftet; Eingang Dreieck ±1 V, 1 kHz (Steigung ±4 V/ms); Ausgang Rechteck ∓4 V. (Mit realem OPV schwänge die Schaltung bei 12,6 kHz; das gehört nicht ins Bild.)

*Kernaussage:* Der Kondensator im Rückkopplungsweg integriert, am Eingang differenziert er.

*Daten:* `bericht_grundschaltungen()` (Integrator, Differenzierer).

*Editor:*
- §1 Schaltpläne mit Kondensator;
- §5 Rechteck, Dreieck, gestapelt;
- §13 gemeinsame Zeitachse;
- §8 optional: Animation, die Ladung des Kondensators als Balken.

**get1/operationsverstaerker/02-logarithmierer**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Logarithmierer nach Bild 12.15 (10 kΩ, Beispieldiode im Rückkopplungsweg, Anode am Minuseingang) und Exponentialschaltung nach Bild 12.16 (Diode am Eingang, Anode an $U_E$, Kathode am Minuseingang; 10 kΩ im Rückkopplungsweg).
- (b) $U_A$ in mV über $U_E$ von 10 mV bis 10 V, $U_E$ logarithmisch: Gerade durch −466, −526, −586, −645 mV, Steigung 59,5 mV je Dekade beschriftet (rot); gestrichelt die Kennlinie bei 310 K, steiler (61,5 mV je Dekade) und um 27 mV (bei 10 mV) bis 21 mV (bei 10 V) höher; dünn grau die reale Beispieldiode (bei 10 V 20 mV tiefer durch den Bahnwiderstand).

*Kernaussage:* Die Diode im Rückkopplungsweg macht aus dem Strom eine Spannung, die mit dem Logarithmus wächst.

*Daten:* `bericht_grundschaltungen()` (Logarithmierer, Exponentialfunktion), `spannung_real`, `IS_von_T(310)`.

*Editor:*
- §1 Schaltpläne mit Diode;
- §12 logarithmische x-Achse;
- §11 Datenkurven;
- §10 Teilbilder.

**get1/operationsverstaerker/02-multiplizierer**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Oben Blockschaltbild nach Skript Bild 12.17 ($U_X$, $U_Y$ → Logarithmierer → Addierer → Exponentialschaltung → Produkt). Darunter die Schaltung nach Bild 12.18 mit $R_L$ = 10 kΩ und Beispieldioden; Ergebnis $-U_X U_Y/(R_L I_S)$ mit dem Faktor 6,9·10⁹ je Volt beschriftet. Rechts ergänzt ein dritter Logarithmierer für 10 V Referenz, dessen Ausgang über einen Umkehrer (−1) in den Addierer geht und so abgezogen wird; Ergebnis $-U_X U_Y/(10\ \mathrm{V})$, Beispiel 2 V und 3 V → −0,6 V.

*Kernaussage:* Der Logarithmus macht aus dem Produkt eine Summe; brauchbar wird das Ergebnis erst mit einer Referenz.

*Daten:* `bericht_grundschaltungen()` (Multiplizierer).

*Editor:*
- §19 Blockbilder;
- §1 Schaltplan mit mehreren OPV.

**get1/operationsverstaerker/02-transimpedanz-nic**
- Fassung: kompakt Abb. 6, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Transimpedanzverstärker ($R$ = 100 kΩ), Fotodiode zwischen Masse und Minuseingang (Anode am Minuseingang, Kathode an Masse), 1 µA Fotostrom (Pfeil), Diode auf 0 V, Ausgang −0,1 V.
- (b) NIC nach Skript S. 211: zwei $R$ = 10 kΩ vom Ausgang zu beiden Eingängen, $R_2$ = 10 kΩ vom Minuseingang nach Masse; am Pluseingang parallel Stromquelle 1 mA mit 10 kΩ und Last 1 kΩ; Werte: Last 1,000 mA (ohne NIC 0,909 mA), Anschluss 1 V, OPV-Ausgang 2 V, Strom aus dem Anschluss 0,1 mA.

*Kernaussage:* Die virtuelle Masse misst Ströme ohne Spannungsabfall; der negative Widerstand hebt den Innenwiderstand der Quelle auf.

*Daten:* `bericht_grundschaltungen()` (Transimpedanzverstärker, NIC).

*Editor:*
- §1 Schaltpläne mit Fotodiode und Stromquelle;
- §2 Strompfeile;
- §10 Teilbilder.

## ET1 Kap. 12: Der reale Operationsverstärker
Zahlenwerk: `notizen/get1/zahlen_opv.py`, Abschnitt „Thema 03“, Bericht `bericht_real()`, Funktionen `a_real`, `zweipol_sprung`, `ua_ruhestrom`, Simulation `sim` mit Anstiegsgrenze; Datenblattwerte LM741 (TI SNOSC25D), Ausgangswiderstand µA741 (TI, Ausgabe 2018); Beispieltransistor aus `zahlen_transistor.py`.

**get1/operationsverstaerker/03-ersatzschaltbild**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Schaltplan. In der Mitte das Dreieckssymbol eines OPV, beschriftet „$v_D$ = 200 000, ab 5 Hz fallend, $f_T$ = 1 MHz, 0,5 V/µs“. Vor dem Pluseingang eine Spannungsquelle „$U_{os}$ = 1 mV“; an beiden Eingängen Stromquellen „80 nA“ mit Pfeil in den OPV; zwischen den Eingängen ein Widerstand „$R_e$ = 2 MΩ“; in Reihe zum Ausgang „$R_a$ = 75 Ω“. Links eine hellgraue Umrandung „Quellen an den Eingängen“ um Offsetquelle und Stromquellen, rechts eine zweite „Abweichungen im Verstärker“ um Verstärkungsangabe und $R_a$. Daneben eine kleine Tabelle der Grenzen: Ausgang ±14 V, Eingänge ±13 V, Gleichtaktunterdrückung 95 dB.

*Kernaussage:* Wo eine Abweichung sitzt, entscheidet, was die Gegenkopplung mit ihr macht.

*Daten:* `bericht_real()` (Kopfzeile mit den Datenblattwerten).

*Editor:*
- §1 Schaltplan mit Strom- und Spannungsquellen;
- §7 Umrandungen und Labels.

**get1/operationsverstaerker/03-fehlerorte**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Zwei Teilbilder, je ein nichtinvertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ.
- (a) Abweichungen im Verstärker, orange markiert an OPV und $R_a$: „$v_D$ = 200 000: $A$ = 9,9995“ und „$v_D$ = 50 000: $A$ = 9,998“; „$R_a$ = 75 Ω wirkt wie 3,75 mΩ“; Rückführungspfeil vom Ausgang zum Minuseingang mit „nachgeregelt, geteilt durch 1 + k v_D“.
- (b) Abweichung am Eingang, rot markiert: Offsetquelle 1 mV vor dem Pluseingang, Eingang auf 0 V; Ausgang 10 mV; Beschriftung „verstärkt wie ein Signal, mal 10“.

*Kernaussage:* Was im Verstärker entsteht, teilt die Gegenkopplung; was am Eingang entsteht, verstärkt sie wie ein Signal.

*Daten:* `bericht_real()` Punkte 1 und 2; Thema 01 `a_geschlossen`.

*Editor:*
- §1 Schaltplan;
- §2 Pfeile mit Text;
- §10 Teilbilder.

**get1/operationsverstaerker/03-aussteuerung**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Vereinfachte Ausgangsstufe, schematisch: npn-Emitterfolger zur positiven, pnp-Emitterfolger zur negativen Versorgung (±15 V), Emitter über 25 Ω bzw. 50 Ω am Ausgang, die Basen von der vorangehenden Stufe getrieben. Rote Klammer vom Ausgang zur positiven Versorgung: „Basis-Emitter-Strecke rund 0,6 V plus Sättigungsspannung des Treibers, zusammen rund 1 V“.
- (b) Senkrechte Spannungsachse von −15 V bis +15 V mit Balken nebeneinander: Versorgung (grau, ±15 V), Ausgang an 10 kΩ (blau, ±14 V), Ausgang an 2 kΩ (hellblau, ±13 V), Eingangsbereich (orange, ±13 V, gestrichelt die garantierten ±12 V); Abstände zur Versorgung als Maßpfeile (1 V, 2 V).

*Kernaussage:* Zwischen jeder Signalspannung und der Versorgung liegen Transistorstrecken, an denen Spannung abfällt.

*Daten:* `bericht_real()` Punkt 11.

*Editor:*
- §1 Schaltplan mit npn- und pnp-Transistoren;
- §22 Bereichsbalken an einer Spannungsachse (neu);
- §10 Teilbilder.

**get1/operationsverstaerker/03-offset**
- Fassung: kompakt Abb. 2, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) $I_C$ in A, logarithmisch von 1 µA bis 10 mA, über $U_{BE}$ in V, linear von 0,45 V bis 0,75 V; Geraden nach der Transfergleichung mit $U_T$ = 25,85 mV für $I_S$ = 10⁻¹⁴ A (blau) und 1,04·10⁻¹⁴ A (rot). Bei 0,5 mA eine Ausschnittvergrößerung (Lupe, $U_{BE}$ von 0,634 V bis 0,640 V; die Geraden erreichen 0,5 mA bei 0,6359 V und 0,6369 V) mit dem waagrechten Maßpfeil „1,01 mV“, weil der Abstand im ganzen Diagramm nicht sichtbar wäre.
- (b) Schaltplan: invertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ, Eingang an Masse, Offsetquelle 1 mV vor dem Pluseingang; Knotenwerte 1 mV an beiden Eingängen des inneren OPV, Strompfeil 0,1 µA durch $R_1$ und $R_2$, Ausgang 3 mV. Rechts daneben dieselbe Schaltung umgezeichnet als nichtinvertierender Verstärker mit dem Eingang $U_{os}$ und der Verstärkung 3.

*Kernaussage:* Die Offsetspannung wird mit der Rauschverstärkung verstärkt, nicht mit der Signalverstärkung.

*Daten:* `bericht_real()` Punkt 4; `IS` aus `zahlen_transistor.py`.

*Editor:*
- §12 halblogarithmische Achse;
- §22 Ausschnittvergrößerung (neu);
- §1 Schaltplan, §2 Strompfeile;
- §10 Teilbilder;
- §8 optional: Animation des Umzeichnens (Eingang an Masse, Offsetquelle wandert vor den Pluseingang).

**get1/operationsverstaerker/03-ruhestroeme**
- Fassung: kompakt Abb. 3, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei Teilbilder, je ein invertierender Verstärker mit $R_1$ = 100 kΩ und $R_2$ = 1 MΩ, Eingang an Masse, Stromquellen von 80 nA in beide Eingänge (orange Pfeile).
- (a) Pluseingang direkt an Masse: beide Eingänge 0 V; Strompfeil 80 nA durch $R_2$ vom Ausgang zum Minuseingang; $R_1$ stromlos (grau); Ausgang 80 mV.
- (b) Mit $R_3$ = 90,9 kΩ vom Pluseingang nach Masse: Pluseingang −7,27 mV (80 nA durch $R_3$), Minuseingang −7,27 mV; Strompfeile 72,7 nA durch $R_1$ aus Masse und 7,27 nA durch $R_2$; Ausgang 0 V. Randnotiz: mit 90 nA und 70 nA statt je 80 nA ±20 mV.

*Kernaussage:* Gleiche Ströme an gleichen Widerständen heben sich auf; übrig bleibt der Unterschied der Ströme.

*Daten:* `bericht_real()` Punkt 5, `ua_ruhestrom`.

*Editor:*
- §1 Schaltplan mit Stromquellen;
- §2 Strompfeile mit Wert;
- §10 Teilbilder.

**get1/operationsverstaerker/03-gleichtakt**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Spannungsfolger mit 10 V am Eingang: beide Eingänge mit „10 V“ beschriftet, Klammer „Gleichtakt 10 V“; Ausgang „10 V ± 0,18 mV“; Hinweis „wirkt wie 0,18 mV Differenzspannung bei 95 dB“.
- (b) Invertierender Verstärker 10 kΩ/20 kΩ mit Sinus am Eingang: beide OPV-Eingänge fest auf 0 V, „kein Gleichtakt“.
- (c) Waagrechte Skala von 60 dB bis 120 dB, darunter dieselben Punkte als Verhältnis 10³ bis 10⁶; Marken bei 61 dB „Subtrahierer, 1 % Widerstandsabweichung“ (grau), 80 dB „garantiert, 10 000“ (orange), 95 dB „typisch, 56 000“ (rot); der Skriptbereich 60 bis 120 dB hell hinterlegt.

*Kernaussage:* Eine Gleichtaktspannung wirkt wie eine kleine Differenzspannung, aber nur, wo die Eingänge mit dem Signal mitlaufen.

*Daten:* `bericht_real()` Punkt 6.

*Editor:*
- §1 Schaltplan;
- §22 Skala mit Doppelbeschriftung Dezibel und Verhältnis (neu);
- §10 Teilbilder.

**get1/operationsverstaerker/03-frequenzgang**
- Fassung: kompakt Abb. 5, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Doppeltlogarithmisches Diagramm, x: Frequenz $f$ in Hz von 1 Hz bis 10 MHz, y: Verstärkung (Betrag) von 0,1 bis 10⁶. Kurven aus dem Einpolmodell: Leerlaufverstärkung, 200 000 durch √(1 + (f/5 Hz)²) (blau), mit gerundeter Ecke bei 5 Hz (141 000); Schaltungen mit der Rauschverstärkung 1, 10, 100 und 1000 (rot), berechnet als $(1/k)$ durch den Betrag von $1 + 1/(k v_D)$ mit der frequenzabhängigen Leerlaufverstärkung; Eckpunkte bei 1 MHz, 100 kHz, 10 kHz und 1 kHz mit der Marke „0,707-fach“. Senkrechter Doppelpfeil zwischen der blauen Kurve und der Kurve für 10 bei 1 kHz: „Schleifenverstärkung 100“. Achsen und Gitter grau.

*Kernaussage:* Die Bandbreite endet, wo die Schleifenverstärkung 1 wird; Rauschverstärkung mal Bandbreite ergibt die Transitfrequenz.

*Daten:* `bericht_real()` Punkt 8, `a_real`.

*Editor:*
- §4 doppeltlogarithmische Achsen;
- §11 Datenkurven;
- §2 Maßpfeil mit Text;
- §15 optional: Schieberegler für die Rauschverstärkung von 1 bis 1000.

**get1/operationsverstaerker/03-anstieg**
- Fassung: kompakt Abb. 6, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Drei Zeitverläufe übereinander, Rauschverstärkung 10, simuliert mit Anstiegsgrenze 0,5 V/µs; je zwei Perioden, y: $U_A$ in V.
- (a) 20 kHz, Eingang 0,05 V: verlangter Ausgang 0,5 V (grau gestrichelt), tatsächlich Sinus mit 0,490 V (rot); Zeitachse 0 bis 100 µs, eigener Maßstab ±0,6 V.
- (b) 5 kHz, Eingang 1 V: verlangt 10 V (grau gestrichelt), tatsächlich Sinus mit 9,99 V (rot); Tangente im Nulldurchgang „0,31 V/µs“; Zeitachse 0 bis 400 µs.
- (c) 20 kHz, Eingang 1 V: verlangt 10 V (grau gestrichelt), tatsächlich Dreieck mit ±6,0 V (rot), an einer Flanke „0,5 V/µs“; Zeitachse 0 bis 100 µs.

*Kernaussage:* Die Bandbreite begrenzt kleine Signale, die Anstiegsgeschwindigkeit große.

*Daten:* `bericht_real()` Punkt 10 (Simulation mit `sim`, $k$ = 0,1).

*Editor:*
- §5 Zeitverläufe mit begrenzter Steigung;
- §11 Datenkurven;
- §10 Teilbilder;
- §15 optional: Schieberegler für die Eingangsamplitude bei 20 kHz; ab 0,398 V Eingang (3,98 V Ausgang) erreicht der Sinus im Modell die Anstiegsgrenze und wird zum Dreieck.

## ET1 Kap. 2: Physikalische Größen und Einheiten
Zahlenwerk: `notizen/get1/zahlen_grundprinzipien.py`, Bericht `bericht()`; Konstanten nach SI-Broschüre (BIPM, 9. Auflage 2019, Vorsätze 2022), Gravitationskonstante nach CODATA 2018.

**get1/grundprinzipien/01-einheitenbaum**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Blockbild als Stammbaum, von unten nach oben.
- Unterste Reihe: sieben graue Kästen mit den Basiseinheiten m, kg, s, A, K, mol, cd und ihren Namen.
- Darüber die abgeleiteten Einheiten als Kästen mit ihrer Gleichung und Pfeilen zu den Einheiten, aus denen sie entstehen: N („F = m a“; von kg, m, s), J („W = F s“; von N, m), W („P = W/t“; von J, s), C („Q = I t“; von A, s), V („P = U I“; von W, A), Ω („R = U/I“; von V, A), F („C = Q/U“; von C, V), Wb („V s“; von V, s), T („Wb/m²“; von Wb, m).
- Mechanik links in Blau, Elektrotechnik rechts in Orange; K, mol und cd ohne Abkömmlinge in diesem Bild, schwächer gezeichnet.

*Kernaussage:* Jede SI-Einheit ist ein Produkt von Potenzen der Basiseinheiten.

*Daten:* `bericht()` Punkt 4.

*Editor:*
- §19 Blockbilder (Kästen in Ebenen, Pfeile);
- §7 Labels und Farbgruppen.

*Animation:* Die Ebenen erscheinen von unten nach oben. Beim Volt leuchten alle Pfeile bis zu den Basiseinheiten auf, und daneben erscheint kg m² s⁻³ A⁻¹.

**get1/grundprinzipien/01-zahlenwert-einheit**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Schema in drei Zeilen untereinander: „U = 230 · 1 V“, „U = 0,23 · 1 kV“, „U = 230 000 · 1 mV“. Zahlenwert in Blau und Einheit in Orange als getrennte Kästen. Zwischen den Zeilen Pfeile: am Zahlenwert „: 1000“ bzw. „· 1000“, an der Einheit gegenläufig „· 1000“ bzw. „: 1000“. Rechts eine Klammer über alle drei Zeilen: „dieselbe Größe“.

*Kernaussage:* Zahlenwert und Einheit ändern sich gegenläufig, die Größe bleibt dieselbe.

*Daten:* `bericht()` Punkt 3.

*Editor:*
- §2 Pfeile mit Text;
- §7 Container und Klammern.

**get1/grundprinzipien/01-si-konstanten**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Blockbild.
- Links sieben Kästen mit den definierenden Konstanten und ihren exakten Werten: Δν_Cs = 9 192 631 770 Hz; c = 299 792 458 m/s; h = 6,626 070 15·10⁻³⁴ J s; e = 1,602 176 634·10⁻¹⁹ C; k = 1,380 649·10⁻²³ J/K; N_A = 6,022 140 76·10²³ mol⁻¹; K_cd = 683 lm/W (für Licht der Frequenz 540·10¹² Hz).
- Rechts die sieben Basiseinheiten. Kräftige Pfeile: Δν_Cs → s, c → m, h → kg, e → A, k → K, N_A → mol, K_cd → cd.
- Dünne graue Hilfspfeile für die Einheiten, die zusätzlich gebraucht werden: s für m und A; m und s für kg; kg, m und s für K und cd.
- Unten eine Zeitleiste: 1889 Urkilogramm als Definition, 20. Mai 2019 Festlegung über Konstanten.

*Kernaussage:* Seit 2019 hängen alle Einheiten an exakt festgelegten Konstanten, nicht mehr an Gegenständen.

*Daten:* `bericht()` Punkte 1 und 11.

*Editor:*
- §19 Blockbilder;
- §7 Labels; Zeitleiste als einfache Skala (§22).

**get1/grundprinzipien/01-vorsaetze**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Waagrechte logarithmische Achse der Stromstärke von 1 pA bis 10 A, Teilstriche je Zehnerpotenz, beschriftet 1 pA, 1 nA, 1 µA, 1 mA, 1 A.
- Darüber farbige Bänder je drei Zehnerpotenzen: Piko (1 pA bis 1 nA), Nano, Mikro, Milli, ab 1 A ohne Vorsatz.
- Marken mit Beschriftung: 1 pA „6,24 Millionen Elementarladungen je Sekunde“; 20 pA „Sperrstrom der Beispieldiode bei −1 V“; 80 nA „Eingangsruhestrom eines 741“; 20 mA „Leuchtdiode“; 9,13 A „Föhn, 2100 W an 230 V“.
- Doppelpfeil über die ganze Achse: „knapp 13 Zehnerpotenzen“.

*Kernaussage:* Vorsätze sind Zehnerpotenzen und machen sehr verschiedene Werte lesbar.

*Daten:* `bericht()` Punkte 2 und 4.

*Editor:*
- §12 logarithmische Achse;
- §22 Skala mit hinterlegten Bereichen;
- §7 Labels.

**get1/grundprinzipien/01-kinematik**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Drei gestapelte Diagramme mit gemeinsamer Zeitachse von 0 bis 6 s, nur unten beschriftet.
- Oben $s(t)$ in m, 0 bis 90: Parabel $s = \tfrac{1}{2}\cdot 4{,}63\ \mathrm{m/s^2}\cdot t^2$ bis 83,3 m. Punkte bei 3 s (20,8 m) und 5 s (57,9 m), Sekante durch beide (orange, „Steigung 18,52 m/s“), Tangente bei 3 s (blau, „Steigung 13,89 m/s“).
- Mitte $v(t)$ in m/s, 0 bis 30: Gerade bis 27,8 m/s; das Dreieck darunter schraffiert, „Fläche = 83,3 m“; gestrichelte Hilfslinie bei 3 s und 13,89 m/s.
- Unten $a(t)$ in m/s², 0 bis 5: waagrechte Linie bei 4,63.

*Kernaussage:* Die Geschwindigkeit ist die Steigung der Ortskurve, der Weg die Fläche unter der Geschwindigkeitskurve.

*Daten:* `bericht()` Punkt 7 (Wertetabelle, Sekanten).

*Editor:*
- §13 gestapelte Diagramme;
- §11 Datenkurven;
- §4 Sekante und Tangente als Hilfsgeraden durch Kurvenpunkte;
- §7 Schraffur.

*Animation:* Der zweite Punkt der Sekante wandert von 5 s auf 3 s zu; die Steigungsanzeige läuft über 18,52, 16,20, 14,12 und 13,91 m/s und rastet bei der Tangente mit 13,89 m/s ein (§15). Danach füllt sich die Fläche unter $v(t)$ mit der Zeit, gleichzeitig mit dem Punkt auf $s(t)$.

**get1/grundprinzipien/01-arbeit**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Links eine Treppe aus sechs Stufen zu je 0,5 m, zusammen 3 m. Koffer (20 kg) unten und oben; an einem senkrechten Stück die Kraft der Hand nach oben, „196,2 N“, und die Gewichtskraft nach unten. Waagrechte Stücke mit „0 J“, senkrechte mit „98,1 J“, Summe „588,6 J“. Rechts eine Rampe, 12 m lang und 3 m hoch, Winkel 14,5°; Kraftpfeil der Hand längs der Rampe „49,05 N“, Beschriftung „49,05 N · 12 m = 588,6 J“; senkrecht zur Rampe die Kraft der Rampe auf den Koffer, „190,0 N, 0 J“. An beiden Wegen zusätzlich die Schwerkraft „196,2 N“ mit „−588,6 J“.
- (b) Schlitten auf waagrechtem Boden, Schnur unter 30°. Kraftpfeil 50 N längs der Schnur, gestrichelt zerlegt in 43,3 N längs des Bodens und 25 N senkrecht dazu; Wegpfeil 20 m; „866 J“ am Längsanteil, „0 J“ am senkrechten.
- (c) Zwei kleine Szenen: Koffer waagrecht getragen (Kraft nach oben, Weg waagrecht, „0 J“); Koffer 3 m abgesetzt (Kraft nach oben, Weg nach unten, „−588,6 J“).

*Kernaussage:* Nur der Kraftanteil längs des Wegs verrichtet Arbeit; im Schwerefeld zählt nur der Höhenunterschied.

*Daten:* `bericht()` Punkt 10.

*Editor:*
- §23 Mechanik-Skizzen (neu);
- §2 Kraftpfeile und Zerlegung;
- §10 Teilbilder.

*Animation:* Ein Koffer wandert die Treppe hinauf; ein Zähler addiert Arbeit nur auf den senkrechten Stücken und erreicht 588,6 J. Gleichzeitig fährt ein zweiter Koffer die Rampe hinauf; sein Zähler wächst gleichmäßig und endet ebenfalls bei 588,6 J.

---

## ST1 Einführung: Von der Röhre zum integrierten Schaltkreis
Zahlenwerk: `notizen/st1/zahlen_einfuehrung.py` (Ausgabe `.txt`), Abschnitte A bis H; Datenblattwerte ECC83, Transistorzahlen nach Herstellerangaben (Intel).

**st1/einfuehrung/01-drei-ventile**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Oben eine Zeitachse von 1900 bis 2010 mit drei Epochenbalken: Röhre (1906 bis etwa 1960), diskreter Transistor (ab 1947), integrierte Schaltung (ab 1958/59). Marken mit kurzem Text: 1906 Lieben-Patent, 1910 Gittersteuerung, 1913 Hochvakuum und Rückkopplung, 1947 Spitzentransistor, 1948 Flächentransistor, 1958/59 integrierte Schaltung, 1959/60 MOSFET, 1963 CMOS, 1971 Mikroprozessor, 2006 Core 2 Duo (291 Mio. Transistoren). Darunter drei Schaltbilder gleicher Bauart, je mit Arbeitswiderstand an der Versorgung $U_B$:
- (a) Triode mit Heizfaden, Kathode K, Gitter G, Anode A, Arbeitswiderstand $R_a$;
- (b) npn-Bipolartransistor mit Basis B, Kollektor C, Emitter E, Widerstand $R_C$;
- (c) n-Kanal-MOSFET mit Gate G, Drain D, Source S, Widerstand $R_D$.

Steuergröße ($U_g$, $U_{BE}$, $U_{GS}$) als blauer Spannungspfeil, gesteuerter Strom ($I_a$, $I_C$, $I_D$) als orangefarbener Strompfeil. Unter jedem Bild die Steuerart („Feld, kein Gleichstrom“, „Spannung, Basisstrom etwa $I_C$/500“, „Feld, kein Gleichstrom“) und die typische Größe („Glaskolben einige cm“, „Gehäuse einige mm“, „Knoten 65 nm, Gatelänge 35 nm, 2006“).

*Kernaussage:* In allen drei Generationen steuert eine kleine Größe am Steueranschluss einen großen Strom aus der Versorgung; geändert haben sich Größe, Leistungsbedarf und Herstellung.

*Daten:* schematisch; Jahreszahlen aus der Arbeitsnotiz `notizen/st1/notiz_geschichte-der-schaltungstechnik.md`, Basisstromanteil aus Zahlenwerk E.

*Editor:*
- §1 und §24 Schaltsymbole (Triode und MOSFET neu);
- §26 Zeitleisten (neu);
- §10 Teilbilder; §2 Pfeile mit Text.

*Animation:* Eine Marke läuft über die Zeitachse; das jeweils aktuelle Ventil hebt sich hervor, die Größenangabe schrumpft mit.

**st1/einfuehrung/01-triode-aufbau**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* (a) Schnitt durch eine Triode, schematisch: links das Kathodenröhrchen mit Heizfaden (orange glühend), davor eine dichte Wolke von Elektronen (blaue Punkte, Dichte nach rechts abnehmend), dicht davor die Gitterdrähte als kleine Kreise im Schnitt, rechts die Anode; einzelne Elektronenbahnen zwischen den Gitterdrähten hindurch zur Anode. (b) Darunter der Potentialverlauf von der Kathode ($x = 0$) zur Anode, schematisch, für $U_a$ = 250 V und die Gitterspannungen −2 V und −1 V: flaches Potentialminimum knapp unter null direkt vor der Kathode, von der Raumladung selbst erzeugt, Absenkung in der Gitterebene, dann Anstieg bis 250 V an der Anode; die Kurve für −1 V liegt im Bereich vor der Kathode höher. Potentialachse mit Bruch zwischen wenigen Volt und 250 V. Zusatz „schematisch“: Abstände und die Tiefe der Mulde überzeichnet.

*Kernaussage:* Das Gitter steuert das Potential vor der Kathode und damit den Anodenstrom; weil es negativ ist, landet kein Elektron auf ihm.

*Daten:* schematisch; Arbeitspunkt aus Zahlenwerk A.

*Editor:*
- §27 Querschnitte (neu, hier für eine Röhre);
- §14 Teilchenwolken;
- §4 Kurven, §17 Achsenbruch;
- §10 Teilbilder.

*Animation:* Schieberegler für die Gitterspannung (§15) von −3,1 V bis 0 V: Die Mulde wird flacher, mehr Elektronen fliegen zur Anode, ein Zähler zeigt $I_a$ nach dem Kennlinienmodell aus Zahlenwerk A (0 bis 5,6 mA).

**st1/einfuehrung/01-triodenkennlinien**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Diagramm $I_a$ in mA (0 bis 6) über $U_g$ in V (−4 bis 0). Drei Kurven für $U_a$ = 150, 200 und 250 V aus dem Kennlinienmodell $I_a = K\,(U_g + D\,U_a + U_0)^{3/2}$ mit $K$ = 1,00566 mA/V^1,5, $D$ = 0,01, $U_0$ = 0,625 V; Stützwerte in 0,5-V-Schritten (250 V: 0; 0; 0,044; 0,497; 1,200; 2,083; 3,115; 4,277; 5,556 mA), Sperrpunkte bei −2,125, −2,625 und −3,125 V. Markiert: Arbeitspunkt (−2 V; 1,2 mA) auf der 250-V-Kurve mit Tangente der Steigung 1,6 mA/V; Punkt (−1 V; 1,2 mA) auf der 150-V-Kurve; waagrechter Doppelpfeil zwischen beiden: „100 V weniger an der Anode = 1 V mehr am Gitter“. Kurven direkt beschriftet.

*Kernaussage:* Ein Volt am Gitter wirkt wie hundert Volt an der Anode; die Kennlinien sind verschobene Kopien derselben Kurve.

*Daten:* Zahlenwerk A, Funktion `ia(ug, ua)`.

*Editor:*
- §4 Kennlinienscharen und Tangente;
- §11 Datenkurven.

*Animation:* Schieberegler für $U_a$ (100 bis 300 V): Die Kurve gleitet seitlich, je 50 V um 0,5 V.

**st1/einfuehrung/01-rueckkopplung**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* (a) Signalflussbild: $u_1$ → Summierstelle (+) → Verstärker $v_u$ (Dreieck) → $u_2$; Rückführung $k$ von $u_2$ zurück zur Summierstelle; Beschriftung „Schleifenverstärkung $k v_u$“. (b) Graph $A/v_u$ über $k v_u$ von −2 bis 1, Kurve $1/(1 - k v_u)$: Werte 0,33 bei −2, 0,5 bei −1, 1 bei 0, 2 bei 0,5, 10 bei 0,9; senkrechte Asymptote bei 1; y-Achse 0 bis 12; links „Gegenkopplung“ (blau hinterlegt), rechts „Mitkopplung“ (orange hinterlegt). (c) Meißner-Schaltung: Triode, Parallelschwingkreis aus Spule und Kondensator zwischen Anode und $+U_B$, magnetisch gekoppelte Koppelspule zwischen Gitter und Kathode, Wicklungspunkte so gesetzt, dass die Rückführung das Vorzeichen umkehrt.

*Kernaussage:* Bei der Schleifenverstärkung 1 entsteht eine Ausgangsspannung ohne Eingangsspannung, die Anordnung schwingt; Gegenkopplung macht die Verstärkung kleiner.

*Daten:* Zahlenwerk B.

*Editor:*
- §19 Blockbilder (Summierstelle, Signalfluss);
- §4 Funktionsgraph mit Asymptote und hinterlegten Bereichen;
- §1 und §24 Schaltsymbole (Triode, gekoppelte Spulen mit Wicklungspunkten);
- §10 Teilbilder.

*Animation:* Schieberegler für $k v_u$: Der Punkt auf dem Graphen wandert; bei Werten knapp über 1 läuft im Zeitverlauf (§5) eine Schwingung aus Rauschen an und begrenzt sich.

**st1/einfuehrung/01-ueberlagerung**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* (a) Blockbild: Antenne → Vorfilter (Bandpass 87,5 bis 108 MHz) → Mischer (Kreis mit Kreuz), in den der Lokaloszillator (Kreis mit Sinus, Pfeil „abstimmbar“) einspeist → Zwischenfrequenzfilter 10,7 MHz → Zwischenfrequenzverstärker → Demodulator → Lautsprecher. (b) Spektrum auf einer Frequenzachse von 0 bis 220 MHz: UKW-Band 87,5 bis 108 MHz grau hinterlegt; Linien beim Sender 100 MHz (blau), beim Oszillator 110,7 MHz (orange), bei den Mischprodukten 10,7 MHz (grün, „Zwischenfrequenz“) und 210,7 MHz (grau, „Summe, ausgefiltert“); Spiegelfrequenz 121,4 MHz rot gestrichelt; Doppelpfeile „10,7 MHz“ zwischen 100 und 110,7 sowie zwischen 110,7 und 121,4 MHz. Lupe um 10,7 MHz mit der Durchlasskurve des Zwischenfrequenzfilters, 200 kHz breit.

*Kernaussage:* Das Mischen schiebt den gewünschten Sender auf die feste Zwischenfrequenz; abgestimmt wird nur der Oszillator, und der Spiegel liegt außerhalb des Bandes.

*Daten:* Zahlenwerk C.

*Editor:*
- §19 Blockbilder; §24 Funkblock-Symbole (neu);
- §25 Spektren (neu);
- §22 Ausschnittvergrößerung.

*Animation:* Schieberegler für die Senderfrequenz von 87,5 bis 108 MHz: Der Oszillator folgt im Abstand von 10,7 MHz, die Zwischenfrequenzlinie bleibt stehen, der Spiegel wandert zwischen 108,9 und 129,4 MHz, immer außerhalb des grauen Bandes.

**st1/einfuehrung/01-planartechnik**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Oben fünf kleine Querschnitte nebeneinander: (a) Siliziumscheibe mit Oxidschicht (hellgrau) oben; (b) Fotolack (gelb), darüber die Maske (schwarz mit Öffnung) und Lichtpfeile; (c) Fenster im Oxid geätzt, Lack entfernt; (d) Dotierstoff dringt durch das Fenster ein, dotiertes Gebiet farbig (n blau, p rot), seitlich unter das Oxid etwas verbreitert; (e) Aluminium (dunkelgrau) aufgedampft und zu einer Bahn geätzt. Unten breit der fertige Querschnitt: n-Kollektorgebiet, darin p-Basis und n⁺-Emitter (npn-Transistor), daneben ein p-Widerstandsstreifen; Oxid mit Kontaktfenstern; eine Aluminiumbahn auf dem Oxid verbindet den Emitter mit dem Widerstand. Zusatz „schematisch, nicht maßstäblich“.

*Kernaussage:* Alle Bauelemente und ihre Verbindungen entstehen in denselben Schritten auf derselben Scheibe.

*Daten:* schematisch.

*Editor:*
- §27 Technologie-Querschnitte (neu);
- §10 Teilbilder; §7 Labels.

*Animation:* Die Schritte laufen nacheinander ab: Oxid wächst, Licht fällt durch die Maske, das Fenster öffnet sich, Dotierstoffpunkte wandern ein, Metall legt sich auf.

**st1/einfuehrung/01-cmos-inverter**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* (a) Schaltbild: PMOS oben (Source an $U$), NMOS unten (Source an Masse), Gates verbunden als Eingang, Drains verbunden als Ausgang, Kondensator $C$ = 1 fF vom Ausgang nach Masse. (b) Die beiden Ruhezustände als kleine Bilder, leitender Transistor als geschlossener Schalter (grün), sperrender als offener Schalter (grau); der unterbrochene Weg von der Versorgung zur Masse ist markiert. (c) Drei gestapelte Zeitverläufe mit gemeinsamer Zeitachse über zwei Perioden von 333 ps (3 GHz): Eingangsspannung als Rechteck zwischen 0 und 1 V, Ausgangsspannung umgekehrt mit kurzen Flanken, Strom aus der Versorgung mit schmalen Spitzen nur beim Wechsel des Ausgangs von 0 auf 1, sonst null; die Fläche einer Spitze ist mit „$C U$ = 1 fC“ beschriftet.

*Kernaussage:* Strom fließt nur beim Umschalten; je Lade-Entlade-Zyklus kostet ein Knoten $C U^2$ = 1 fJ.

*Daten:* Zahlenwerk G.

*Editor:*
- §1 und §24 MOSFET-Symbole (neu);
- §5 Zeitverläufe; §13 gestapelte Diagramme;
- §10 Teilbilder.

*Animation:* Der Eingang schaltet; Ladungspunkte fließen beim Laden von der Versorgung durch den PMOS auf den Kondensator und beim Entladen durch den NMOS zur Masse; zwei Zähler zeigen je ½ $C U^2$ als Wärme im PMOS und im NMOS.

**st1/einfuehrung/01-moore**
- Fassung: kompakt Abb. 7, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Halblogarithmisches Diagramm: Transistorzahl je Chip von 1 bis 10¹¹ (logarithmisch) über den Jahren 1959 bis 2010. Zwölf Punkte mit Namen: 4004 (1971, 2300), 8008 (1972, 3500), 8080 (1974, 4500), 8086 (1978, 29 000), 80286 (1982, 134 000), 80386 (1985, 275 000), 80486 (1989, 1 180 235), Pentium (1993, 3,1 Mio.), Pentium II (1997, 7,5 Mio.), Pentium 4 (2000, 42 Mio.), Core 2 Duo (2006, 291 Mio.), Xeon 7500 mit acht Kernen (2010, 2,3 Mrd.). Ausgleichsgerade mit der Verdopplungszeit 2,04 Jahre (3,12·10³ im Jahr 1972, 3,33·10⁸ im Jahr 2006, 1,30·10⁹ im Jahr 2010), beschriftet „Verdopplung alle 2,04 Jahre“. Gestrichelt Moores Gerade von 1965: Verdopplung jedes Jahr von 1 (1959) über 64 (1965) bis 65 536 (1975). Gepunktet die 18-Monate-Gerade ab dem 8008 (3500 im Jahr 1972) bis 2,33·10¹⁰ im Jahr 2006.

*Kernaussage:* Auf der logarithmischen Achse wird exponentielles Wachstum zur Geraden; die Transistorzahl verdoppelte sich rund alle zwei Jahre, nicht alle 18 Monate.

*Daten:* Zahlenwerk F (Datenliste `daten`, Ausgleichsgerade, Gegenproben).

*Editor:*
- §12 halblogarithmische Achsen;
- §11 Datenkurven; §7 Labels an Punkten.

*Animation:* Die Punkte erscheinen in zeitlicher Reihenfolge; ein Schieberegler für die Verdopplungszeit dreht eine Gerade um den Punkt des 8008.

**st1/einfuehrung/01-skalierung**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* (a) Querschnitt eines MOSFET: Gate (dunkel), Gateoxid der Dicke $t_\mathrm{ox}$ (hellgrau), Source und Drain (n⁺, blau), Kanal der Länge $L$, Weite $W$ perspektivisch angedeutet; Gatespannung $U$; grüne Feldpfeile senkrecht im Oxid und waagrecht im Kanal. (b) Derselbe Transistor um den Faktor $\kappa$ verkleinert, mit $L/\kappa$, $t_\mathrm{ox}/\kappa$, $U/\kappa$, die Feldpfeile gleich lang wie in (a). (c) Tabelle „Größe | Faktor | für $\kappa = \sqrt2$“: Längen und Spannung $1/\kappa$, 0,71; Dotierung $\kappa$, 1,41; Feldstärke 1, 1; Kapazität $1/\kappa$, 0,71; Strom $1/\kappa$, 0,71; Schaltzeit $1/\kappa$, 0,71; Frequenz $\kappa$, 1,41; Leistung je Transistor $1/\kappa^2$, 0,5; Transistoren je Fläche $\kappa^2$, 2; Leistung je Fläche 1, 1.

*Kernaussage:* Bei gleicher Feldstärke wird der kleinere Transistor schneller und sparsamer, und die Leistung je Fläche bleibt gleich.

*Daten:* Zahlenwerk H.

*Editor:*
- §27 Technologie-Querschnitte (neu); §2 Pfeile;
- §7 Tabellen; §10 Teilbilder.

*Animation:* Schieberegler für $\kappa$ von 1 bis 2: Der rechte Transistor schrumpft, die Pfeile bleiben gleich lang, die Tabelle rechnet mit.

**st1/einfuehrung/01-direktumsetzer**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Zwei Blockbilder untereinander, jeweils mit gestricheltem Rahmen für den Chip. (a) Überlagerungsempfänger: rauscharmer Verstärker, Mischer, Oszillator, Zwischenfrequenzverstärker und Demodulator im Rahmen; Spiegelfrequenzfilter und Zwischenfrequenzfilter (keramisch bzw. Oberflächenwellenfilter) außerhalb des Rahmens als eigene Bauteile. (b) Direktumsetzer: Antenne, Bandfilter und Quarz außerhalb, im Rahmen rauscharmer Verstärker, Aufteilung in I- und Q-Zweig mit je einem Mischer, Oszillator bei der Empfangsfrequenz mit Ausgängen 0° und 90°, je ein Tiefpass und ein Analog-Digital-Umsetzer, danach die digitale Verarbeitung im Basisband. Beschriftung zwischen I- und Q-Zweig: „Gleichlauf etwa 1 % und 1°“.

*Kernaussage:* Der Direktumsetzer kommt ohne Zwischenfrequenzfilter aus und passt bis auf Antenne, Bandfilter und Quarz auf den Chip.

*Daten:* schematisch; Gleichlauf aus Zahlenwerk H (Matching, Spiegelunterdrückung 40 dB bei 1 % und 1°).

*Editor:*
- §19 Blockbilder; §24 Funkblock-Symbole (neu);
- §7 Rahmen und Container.

*Animation:* Ein Signalspektrum wandert durch die Blöcke; in (a) erscheint es nach dem Mischer bei 10,7 MHz, in (b) direkt um 0 Hz, getrennt in I und Q.

## ST1 Netzwerkanalyse: Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung
Zahlenwerk: `notizen/st1/zahlen_netzwerkanalyse.py` (Ausgabe `.txt`), Abschnitte A bis H; eigenes Beispielsystem: MOS-Diode mit $k$ = 1 mA/V² und $U_\mathrm{th}$ = 0,5 V an einer realen Stromquelle (0,5 mA, 4 kΩ), die ET1-Beispieldiode, ein Spulenmodell mit Sättigung.

**st1/netzwerkanalyse/01-tangente**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Diagramm $I$ in mA (0 bis 1,4) über $U$ in V (0,4 bis 1,6). Kennlinie der MOS-Diode: null bis 0,5 V, darüber $I = k\,(U - U_\mathrm{th})^2$ (0,25 mA bei 1,0 V, 1,0 mA bei 1,5 V, 1,21 mA bei 1,6 V). Arbeitspunkt (1,0 V; 0,25 mA) markiert, Tangente mit der Steigung 1 mS (schneidet die Spannungsachse bei 0,75 V). Signalprojektion: unter der Spannungsachse eine Sinusspannung ±50 mV um 1,0 V über zwei Perioden (Zeit nach unten), rechts neben dem Diagramm der Strom über der Zeit (Zeit nach rechts), mit Hilfslinien Punkt für Punkt über die Kennlinie abgebildet: zwischen 0,2025 und 0,3025 mA (Spitzen +52,5 µA und −47,5 µA um 0,25 mA), Grundwelle 50 µA. Zum Vergleich dünn die Projektion über die Tangente (genau ±50 µA); beide Kurven fallen fast zusammen.

*Kernaussage:* Kleine Änderungen um den Arbeitspunkt sehen von der Kennlinie nur die Tangente.

*Daten:* Zahlenwerk A (Arbeitspunkt, $g$), B (Sinus 50 mV).

*Editor:*
- §4 Tangente im Punkt;
- §5 Signalprojektion über eine Kennlinie;
- §11 Datenkurven.

*Animation:* Schieberegler für die Amplitude (§15) von 10 mV bis 450 mV: Bei großen Amplituden trennen sich die Projektion über die Kennlinie (oben schmal und hoch, unten breit und flach) und die über die Tangente sichtbar; eine Anzeige nennt das Verhältnis zweite Harmonische zu Grundwelle, $\hat u$ geteilt durch 2 V.

**st1/netzwerkanalyse/01-zustandsgroessen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei Teilbilder nebeneinander, je mit dem Symbol des Bauelements in der Ecke.
- (a) Strom über Spannung, $U$ von 0 bis 1,5 V, $I$ von 0 bis 2 mA: die Beispieldiode, $I = I_S\,[\exp(U/U_T) - 1]$ mit $I_S$ = 1,46·10⁻¹⁴ A und $U_T$ = 25,85 mV, verlässt das Bild bei 0,663 V (2 mA), ein Pfeil am Rand „8,4 mA bei 0,7 V“; die MOS-Diode, null bis 0,5 V, dann Parabel bis 1,0 mA bei 1,5 V. Direkt beschriftet.
- (b) Ladung über Spannung, $U$ von −10 V bis +0,4 V: Sperrschichtladung der Beispieldiode auf der p-Seite (negativ wegen der Akzeptorrümpfe; null bei $U_\mathrm{Diff}$ = 0,714 V, wo die Zone in der Näherung verschwindet, Formel $Q = -2\,C_\mathrm{S0}\,U_\mathrm{Diff}\sqrt{1 - U/U_\mathrm{Diff}}$), −133,3 pC bei −10 V, −97,4 pC bei −5 V, −53,3 pC bei −1 V, −34,4 pC bei 0 V, −22,8 pC bei +0,4 V; die Kurve wird zur Durchlassrichtung hin steiler.
- (c) Flussverkettung über Strom, $I$ von 0 bis 2 A: Spulenmodell $\Psi = \Psi_\mathrm{max}\tanh(L_0 I/\Psi_\mathrm{max})$ mit $L_0$ = 10 mH und $\Psi_\mathrm{max}$ = 10 mV s: 4,62 mV s bei 0,5 A, 7,62 mV s bei 1 A, 9,64 mV s bei 2 A; gestrichelte Asymptote bei 10 mV s; dünn gestrichelt eine schematische Hystereseschleife um die Kurve (Beschriftung „mit Hysterese“).

*Kernaussage:* Jedes Bauelement lässt sich durch Strom, Ladung und Fluss als Funktionen seiner Steuergrößen beschreiben.

*Daten:* Zahlenwerk C (Diode), A (MOS-Diode), F (Ladung), G (Fluss); Hystereseschleife schematisch.

*Editor:*
- §10 Teilbilder;
- §4 mehrere Kurven, direkte Beschriftung;
- §11 Datenkurven;
- §20 Hystereseschleifen;
- §1 und §24 kleine Symbole (Diode, MOS-Diode, Spule).

*Animation:* Ein Punkt läuft gleichzeitig auf allen drei Kennlinien, während die jeweilige Steuergröße steigt; das Symbol des Bauelements leuchtet dabei auf.

**st1/netzwerkanalyse/01-oberwellen**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei Spalten, oben Zeitverläufe über zwei Perioden, unten Spektren.
- Links, $\hat u$ = 50 mV: Strom zwischen 0,2025 und 0,3025 mA um den Mittelwert 0,25125 mA, fast sinusförmig; gepunktet die Gerade 0,25 mA.
- Rechts, $\hat u$ = 400 mV: Strom zwischen 0,01 und 0,81 mA, oben schmale, hohe, unten breite, flache Halbwellen; dünn die Zerlegung: Gleichanteil 0,33 mA (gestrichelt, gepunktet zum Vergleich 0,25 mA), Grundwelle 0,4 mA·sin ωt, zweite Harmonische −0,08 mA·cos 2ωt.
- Spektren als Linien bei 0, $f$ und $2f$, mit Werten beschriftet: links 251,25 µA, 50 µA, 1,25 µA; rechts 330 µA, 400 µA, 80 µA.

*Kernaussage:* Die Krümmung der Kennlinie erzeugt eine Schwingung doppelter Frequenz und verschiebt den Gleichanteil, beide wachsen mit dem Quadrat der Amplitude.

*Daten:* Zahlenwerk B (Formel und numerische Zerlegung).

*Editor:*
- §5 Zeitverläufe;
- §25 Spektren;
- §10 Teilbilder;
- §11 Datenkurven.

*Animation:* Schieberegler für $\hat u$ (§15) von 0 bis 700 mV: Die $2f$-Linie wächst quadratisch, die $f$-Linie linear; oberhalb von 500 mV wird der Strom unten abgeschnitten, und eine $3f$-Linie erscheint (bei 700 mV 7 µA).

**st1/netzwerkanalyse/01-zwei-steuergroessen**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Diagramm Anodenstrom $I_a$ in mA (0 bis 3,5) über der Gitterspannung $U_g$ in V (−3 bis −1) für $U_a$ = 250 V und 256,25 V aus dem Kennlinienmodell $I_a = K\,(U_g + D\,U_a + U_0)^{3/2}$ mit $K$ = 1,00566 mA/V^1,5, $D$ = 0,01, $U_0$ = 0,625 V. Stützwerte in 0,25-V-Schritten von −3 V bis −1 V: für 250 V 0,044; 0,231; 0,497; 0,823; 1,200; 1,621; 2,083; 2,582; 3,115 mA, für 256,25 V 0,082; 0,291; 0,573; 0,913; 1,301; 1,733; 2,205; 2,712; 3,254 mA. Arbeitspunkt (−2 V; 1,2 mA) auf der 250-V-Kurve mit Tangente 1,6 mA/V. Der Weg in zwei Teilschritten als Pfeile:
- (1) entlang der 250-V-Kurve nach −1,9 V, 1,3635 mA (Zuwachs 0,164 mA; die Tangente sagt 0,16 mA);
- (2) senkrecht hinauf zur 256,25-V-Kurve, 1,4692 mA (Zuwachs 0,106 mA; 16 µS mal 6,25 V ergibt 0,10 mA).

Lupe um (−1,9 V; 1,4 mA). Beschriftung der Summe: „0,269 mA, aus den Steigungen 0,26 mA“. Kurven direkt beschriftet.

*Kernaussage:* Bei kleinen Änderungen mehrerer Steuergrößen ist die Gesamtänderung näherungsweise die Summe der Beiträge, jeder mit seiner eigenen Steigung.

*Daten:* Zahlenwerk I (Kennlinienmodell wie im Zahlenwerk der Einführung, Abschnitt A).

*Editor:*
- §4 Kennlinienscharen und Tangente;
- §2 Pfeile mit Text;
- §22 Ausschnittvergrößerung;
- §11 Datenkurven.

*Animation:* Schieberegler für die beiden Schrittweiten (§15): Mit kleineren Schritten nähert sich die exakte Summe der aus den Steigungen; eine Anzeige zeigt die Abweichung, die mit dem Quadrat der Schrittweite schrumpft.

**st1/netzwerkanalyse/01-kapazitaet-induktivitaet**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei Spalten mit je zwei gestapelten Diagrammen und gemeinsamer x-Achse.
- Links oben: Sperrschichtladung der Beispieldiode über $U$ von −10 V bis +0,4 V (Werte wie in 01-zustandsgroessen), Tangenten bei 0 V (Steigung 24,1 pF) und bei −5 V (8,5 pF). Links unten: ihre Steigung $C_\mathrm{S}(U) = C_\mathrm{S0}/\sqrt{1 - U/U_\mathrm{Diff}}$ mit $C_\mathrm{S0}$ = 24,10 pF und $U_\mathrm{Diff}$ = 0,714 V: 6,2 pF bei −10 V, 8,5 pF bei −5 V, 15,6 pF bei −1 V, 24,1 pF bei 0 V, 36,3 pF bei +0,4 V; die beiden Tangentenpunkte als Punkte auf dieser Kurve.
- Rechts oben: Flussverkettung der Spule über $I$ von 0 bis 2 A (Modell wie in 01-zustandsgroessen), Tangenten bei 0 A (10 mH) und 1 A (4,2 mH). Rechts unten: $L(I) = L_0/\cosh^2(L_0 I/\Psi_\mathrm{max})$: 10 mH bei 0 A, 7,86 mH bei 0,5 A, 4,20 mH bei 1 A, 0,71 mH bei 2 A.

*Kernaussage:* Kapazität und Induktivität sind die Steigungen der Ladungs- und der Flusskennlinie und hängen vom Arbeitspunkt ab.

*Daten:* Zahlenwerk F, G.

*Editor:*
- §13 gestapelte Diagramme;
- §4 Tangente im Punkt;
- §10 Teilbilder;
- §11 Datenkurven.

*Animation:* Schieberegler für den Arbeitspunkt (§15): Die Tangente gleitet über die obere Kurve, der zugehörige Punkt auf der unteren Kurve wandert mit; Anzeige von $C$ bzw. $L$.

**st1/netzwerkanalyse/01-arbeitspunkt-grafisch**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:*
- (a) Schaltbild: ideale Stromquelle $I_q$ = 0,5 mA, parallel der Innenwiderstand $R_q$ = 4 kΩ ($G_q$ = 0,25 mS) und das Beispielbauelement als MOS-Diode (n-Kanal-MOSFET, Gate mit Drain verbunden); Knotenspannung $U$ als Spannungspfeil; Strompfeile $G_q U$ durch den Innenwiderstand und $I(U)$ durch das Bauelement.
- (b) Diagramm $I$ in mA (0 bis 0,6) über $U$ in V (0 bis 2,2): die fallende Gerade der Quelle von (0 V; 0,5 mA) bis (2 V; 0 mA), Endpunkte beschriftet „Kurzschlussstrom 0,5 mA“ und „Leerlaufspannung 2 V“; die Kennlinie des Bauelements, null bis 0,5 V, dann Parabel (0,25 mA bei 1,0 V, 0,5625 mA bei 1,25 V); Schnittpunkt (1,0 V; 0,25 mA) markiert und beschriftet.

*Kernaussage:* Der Arbeitspunkt ist der einzige Punkt, an dem das Angebot der Quelle und die Kennlinie des Bauelements übereinstimmen.

*Daten:* Zahlenwerk A.

*Editor:*
- §1 Schaltplan, §24 MOSFET-Symbol;
- §4 Gerade ins Kennlinienfeld und Schnittpunkt;
- §10 Teilbilder;
- §2 Zählpfeile.

*Animation:* Schieberegler für $I_q$ und $R_q$ (§15): Die Gerade verschiebt sich bzw. kippt um ihren Achsenpunkt, der Schnittpunkt wandert auf der Kennlinie; die Werte $U_A$ und $I_A$ werden live aus der Knotengleichung berechnet.

**st1/netzwerkanalyse/01-newton**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Diagramm Fehlerstrom $F(U) = I(U) + G_q U - I_q$ in mA (−0,6 bis 3) über $U$ in V (0 bis 2,2): von −0,5 mA bei 0 V gerade ansteigend auf −0,375 mA bei 0,5 V, dann parabelförmig durch null bei 1,0 V bis 2,25 mA bei 2 V und 2,94 mA bei 2,2 V. Newton-Schritte, nummeriert:
- Tangente bei $U^{(0)}$ = 0 V (Steigung 0,25 mS, fällt mit dem geraden Stück zusammen), Nullstelle $U^{(1)}$ = 2 V;
- senkrechte Hilfslinie zur Kurve, Tangente bei 2 V ($F$ = 2,25 mA, 3,25 mS), Nullstelle $U^{(2)}$ = 1,3077 V;
- Tangente bei 1,3077 V ($F$ = 0,479 mA, 1,865 mS), Nullstelle $U^{(3)}$ = 1,0508 V;
- Tangente bei 1,0508 V ($F$ = 0,066 mA, 1,352 mS), Nullstelle $U^{(4)}$ = 1,0019 V.
Lupe um 1,0 V für die letzten beiden Schritte. Daneben die Tabelle des Beispiels ($U^{(\nu)}$, $F(U^{(\nu)})$, $g + G_q$, Fehler).

*Kernaussage:* Jede Tangente ist die bei der jeweiligen Schätzung linearisierte Schaltung, und ihre Nullstellen laufen schnell auf 1,0 V zu.

*Daten:* Zahlenwerk D (Tabelle).

*Editor:*
- §29 Iterationsdarstellungen (neu);
- §4 Tangente im Punkt;
- §22 Ausschnittvergrößerung;
- §11 Datenkurven.

*Animation:* Schritt für Schritt (§8): Tangente erscheint, ihre Nullstelle wird markiert, die senkrechte Hilfslinie führt zur Kurve, die passende Tabellenzeile leuchtet auf. Startwert per Schieberegler (§15) von 0 bis 2 V wählbar.

**st1/netzwerkanalyse/01-ersatzschaltbilder**
- Fassung: kompakt Abb. 7, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Schaltbilder gleicher Anordnung nebeneinander.
- (a) Großsignal-Ersatzschaltbild im Arbeitspunkt: Gleichstromquelle 0,5 mA, Innenwiderstand 4 kΩ, das Bauelement als nichtlinearer Zweipol mit Kennlinie $I(U)$; Knotenspannung 1,0 V, Ströme 0,25 mA durch den Innenwiderstand und 0,25 mA durch das Bauelement.
- (b) Kleinsignal-Ersatzschaltbild: Signalstromquelle $i_q$ (Amplitude 10 µA), Innenleitwert 0,25 mS, das Bauelement ersetzt durch den Leitwert $g$ = 1 mS; daneben klein die gleichwertige Darstellung als spannungsgesteuerte Stromquelle $g\,u$, gesteuert von der eigenen Spannung; gestrichelt die Kapazität $C(U_A)$ (im Beispiel angenommen 1 pF, nur für schnelle Signale). An der Stelle der Gleichstromquelle eine Unterbrechung mit Vermerk „konstant, Änderung null“. Spannung $u$ = 8 mV, Ströme 8 µA durch $g$ und 2 µA durch den Innenleitwert.
- Unten eine Legende: Gleichspannungsquelle wird zum Kurzschluss, Gleichstromquelle zur Unterbrechung.

*Kernaussage:* Im Kleinsignalbild steht nur, was sich ändert.

*Daten:* Zahlenwerk A, H.

*Editor:*
- §28 gesteuerte Quellen, nichtlinearer Zweipol, Gegenüberstellung Groß- und Kleinsignalbild (neu);
- §1 Schaltplan;
- §10 Teilbilder, §7 Container.

*Animation:* Übergang von (a) nach (b): Die Gleichstromquelle verblasst zur Unterbrechung, das Bauelementsymbol wird zum Leitwert $g$, die Zahlenwerte wechseln von Gleich- zu Kleinsignalgrößen.

## ST1 Netzwerkanalyse: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse
Zahlenwerk: `notizen/st1/zahlen_netzwerkanalyse.py` (Ausgabe `.txt`), Abschnitte K bis N; Beispielsysteme: zweistufiger RC-Tiefpass (R = 1 kΩ, C = 100 nF, ω = 10⁴ 1/s) und Source-Schaltung mit Source-Widerstand (derselbe Transistor wie die MOS-Diode aus Thema 1, g_m = 1 mS, g_o = 25 µS). Komplexe Größen unterstrichen.

**st1/netzwerkanalyse/02-verstaerker-kleinsignal**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Drei Teilbilder nebeneinander bzw. auf dem Handy untereinander.
- (a) Source-Schaltung: n-Kanal-MOSFET, Drain über $R_D$ = 10 kΩ an $V_{DD}$ = 5 V, Source über $R_S$ = 1 kΩ an Masse; am Gate in Reihe gegen Masse die Gleichspannungsquelle 1,25 V, die Signalquelle $u_\mathrm{sig}$ (Sinus, 10 mV Amplitude) und $R_\mathrm{sig}$ = 10 kΩ; am Drain über einen Koppelkondensator die Last $R_L$ = 10 kΩ. Arbeitspunkt klein annotiert: $I_D$ = 0,25 mA, $U_S$ = 0,25 V, $U_D$ = 2,5 V.
- (b) Kleinsignal-Ersatzschaltbild: Knoten G, D, S und Masse (Punkte, beschriftet); $u_\mathrm{sig}$ mit $R_\mathrm{sig}$ zwischen Masse und G; spannungsgesteuerte Stromquelle $g_m u_{GS}$ (Raute, 1 mS) von D nach S; $g_o$ = 25 µS (40 kΩ) zwischen D und S; $R_D$ und $R_L$ von D nach Masse ($V_{DD}$ ist im Kleinsignalbild Masse, der Koppelkondensator ein Kurzschluss); $R_S$ von S nach Masse. An den Knoten die Zeiger der Knotenpotentiale: 10 mV, −23,26 mV, 4,65 mV; der Drain schwingt mit 23,26 mV Amplitude gegenphasig zum Signal.
- (c) Ersatzquelle am Ausgang: Spannungsquelle $U_{LL}$ = −43,96 mV in Reihe mit $Z_i$ = 8,90 kΩ, daran $R_L$ = 10 kΩ mit −23,26 mV.

*Kernaussage:* Eine lineare Schaltung ist durch ihre Knotenpotentiale bestimmt, und vom Ausgang aus gesehen genügen zwei Zahlen.

*Daten:* Zahlenwerk L.

*Editor:*
- §1 Schaltplan, §24 MOSFET, §28 gesteuerte Quelle (Raute);
- §10 Teilbilder; §2 Zählpfeile.

*Animation:* Übergang (a) → (b) → (c): Gleichquellen werden zu Kurzschlüssen, der Transistor zu Raute und $g_o$, dann schrumpft alles links von D zur Ersatzquelle.

**st1/netzwerkanalyse/02-quellensymbole**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Tabelle mit drei Spalten (Symbol, Gleichung, im Kleinsignalbild):
- Gleichspannungsquelle (Kreis, Strich in Leitungsrichtung, Pfeil der Quellenspannung) – $U = U_q$ – Kurzschluss;
- Gleichstromquelle (Kreis, Strich quer, Strompfeil) – $I = I_q$ – Unterbrechung;
- Kleinsignal-Spannungs- und Stromquelle (Kreis mit Sinus) – $u = u_q(t)$ bzw. $i = i_q(t)$ – bleiben;
- vier gesteuerte Quellen als Rauten: spannungsgesteuerte Spannungsquelle $u_2 = v\,u_1$, spannungsgesteuerte Stromquelle $i_2 = g_m u_1$, stromgesteuerte Spannungsquelle $u_2 = r_m i_1$, stromgesteuerte Stromquelle $i_2 = \beta\,i_1$ – bleiben, mit ihrer Steuergröße an anderer Stelle der Schaltung (gestrichelte Zuordnung).

*Kernaussage:* Gleichquellen legen den Arbeitspunkt fest und verschwinden im Kleinsignalbild; Kleinsignalquellen regen an; gesteuerte Quellen beschreiben die Verstärkung.

*Daten:* schematisch.

*Editor:*
- §1, §24, §28 Symbolbibliothek;
- §7 Tabellen-Darstellung.

*Animation:* keine.
**st1/netzwerkanalyse/02-impedanzen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei gestapelte Diagramme mit gemeinsamer, logarithmischer ω-Achse von 10² bis 10⁶ 1/s.
- Oben, doppeltlogarithmisch: Betrag der Impedanz in Ω (10 bis 10⁶) für $R$ = 1 kΩ (waagrecht), $L$ = 100 mH (Steigung +1, 10 Ω bei 10² 1/s bis 100 kΩ bei 10⁶ 1/s) und $C$ = 100 nF (Steigung −1, 100 kΩ bis 10 Ω). Alle drei schneiden sich bei 10⁴ 1/s und 1 kΩ (markiert, $f$ = 1,59 kHz).
- Unten: Winkel der Impedanz in Grad, 0° für $R$, +90° für $L$, −90° für $C$.
- Beschriftung am Schnittpunkt: $\underline Z_R$ = 1 kΩ, $\underline Z_L$ = +j·1 kΩ, $\underline Z_C$ = −j·1 kΩ.

*Kernaussage:* Spule und Kondensator verhalten sich bei Sinusgrößen wie Widerstände, deren Betrag mit der Frequenz steigt bzw. fällt, mit +90° bzw. −90° Phasenverschiebung.

*Daten:* Zahlenwerk K.

*Editor:*
- §4 doppeltlogarithmische Achsen, mehrere Kurven, direkte Beschriftung;
- §13 gestapelte Diagramme.

*Animation:* Schieberegler für ω (§15): Ein Punkt läuft auf jeder Kurve mit, eine Anzeige zeigt die drei komplexen Impedanzen.

**st1/netzwerkanalyse/02-topologie**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Links das Kleinsignal-Ersatzschaltbild der Verstärkerstufe (wie 02-verstaerker-kleinsignal b), rechts sein Graph: Knoten G, D, S, 0 als Punkte, die sechs Zweige als beschriftete Linien (Quelle G–0, $g_m$ D–S, $g_o$ D–S, $R_D$ D–0, $R_L$ D–0, $R_S$ S–0). Ein Baum aus drei Zweigen (Quelle, $R_D$, $R_S$) kräftig hervorgehoben; die drei Verbindungszweige ($g_m$, $g_o$, $R_L$) dünn, jeder mit dem gebogenen Pfeil der Masche, die er zusammen mit Baumzweigen schließt. Darunter die Zählung: 2z = 12 Unbekannte; 6 Zweiggleichungen, k − 1 = 3 Knotengleichungen, z − k + 1 = 3 Maschengleichungen.

*Kernaussage:* Von den Knotengleichungen ist eine überzählig, und jeder Verbindungszweig schließt genau eine neue Masche; zusammen sind es genau so viele unabhängige Gleichungen wie Unbekannte.

*Daten:* Zahlenwerk L und M (Zählung).

*Editor:*
- §30 Netzwerkgraphen (neu);
- §2 gebogene Umlaufpfeile; §10 Teilbilder.

*Animation:* Der Baum wird Zweig für Zweig aufgebaut, dann schließt jeder Verbindungszweig mit einem Aufleuchten seine Masche.

**st1/netzwerkanalyse/02-ersatzquelle-ueberlagerung**
- Fassung: kompakt Abb. 3, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Vier Teilbilder.
- (a) Ein lineares Netz als Kasten mit Klemmen A und B, darin symbolisch unabhängige Quellen, eine gesteuerte Quelle (Raute) und Impedanzen; die Last ist durch eine Stromquelle $I_A$ ersetzt; Klemmenspannung $U_{AB}$.
- (b) Teil 1: $I_A$ = 0 (Klemmen offen), innere unabhängige Quellen aktiv; Ergebnis $U_{LL}$.
- (c) Teil 2: innere unabhängige Quellen null (Spannungsquelle als Kurzschluss, Stromquelle als Unterbrechung gezeichnet), die gesteuerte Quelle farbig hervorgehoben aktiv, nur $I_A$ wirkt; Ergebnis $-Z_i I_A$.
- (d) Die zwei gleichwertigen Ersatzschaltungen mit den Zahlen der Verstärkerstufe: Thévenin ($U_{LL}$ = −43,96 mV in Reihe mit $Z_i$ = 8,90 kΩ) und Norton ($I_{KS}$ = −4,94 µA parallel zu $Y_i$ = 0,112 mS).

*Kernaussage:* Die Klemmenspannung ist die Summe zweier Beiträge, einer unabhängig vom Klemmenstrom, einer ihm proportional; deshalb beschreiben zwei Zahlen das Netz von außen vollständig.

*Daten:* Zahlenwerk L (Ersatzquelle).

*Editor:*
- §1 Schaltplan, §28 gesteuerte Quellen und Gegenüberstellung;
- §7 Rahmen (Netz als Kasten); §10 Teilbilder.

*Animation:* (b) und (c) überlagern sich zu (a); Schieberegler für $I_A$ (§15) zeigt, wie $U_{AB}$ linear fällt.

**st1/netzwerkanalyse/02-innenwiderstand**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder nebeneinander, jeweils das Kleinsignal-Ersatzschaltbild der Verstärkerstufe ohne $R_L$, mit $u_\mathrm{sig}$ = 0 ($u_\mathrm{sig}$ durch Kurzschluss ersetzt, $R_\mathrm{sig}$ bleibt, $U_G$ = 0) und einer Testspannung $U_T$ am Drain.
- (a) Richtig: gesteuerte Quelle aktiv; $U_S$ = 0,0123 $U_T$; Ströme: durch $R_D$ 0,1 mS·$U_T$, in den Zweig aus Transistor und $R_S$ 0,0123 mS·$U_T$; $Z_i = U_T/I_T$ = 8,90 kΩ; dieser Zweig allein 81 kΩ, seine Drain-Source-Strecke 80 kΩ.
- (b) Falsch: gesteuerte Quelle entfernt (Unterbrechung, rot durchgestrichen): Zweig aus Transistor und $R_S$ nur $r_o + R_S$ = 41 kΩ, die Drain-Source-Strecke $r_o$ = 40 kΩ; zusammen 8,04 kΩ (9,7 % zu klein).

*Kernaussage:* Gesteuerte Quellen bleiben beim Bestimmen der Innenimpedanz aktiv; der Source-Widerstand macht die Drain-Source-Strecke doppelt so hochohmig.

*Daten:* Zahlenwerk L (Testquelle, falsch) und N (Testquelle je Volt, Drain-Source-Strecke).

*Editor:*
- §1, §28 (gesteuerte Quelle, Gegenüberstellung);
- §2 Strompfeile mit Werten; §10 Teilbilder.

*Animation:* Schieberegler für $R_S$ (0 bis 5 kΩ, §15): Der Zweig aus Transistor und $R_S$ wächst als $r_o(1 + g_m R_S) + R_S$, die falsche Rechnung nur als $r_o + R_S$.

**st1/netzwerkanalyse/02-maschenstroeme**
- Fassung: kompakt Abb. 5, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zweistufiger RC-Tiefpass: Quelle $\underline U_q$ = 1 V (Zeiger 0°) gegen Masse, $R_1$ = 1 kΩ, $C_1$ = 100 nF gegen Masse, $R_2$ = 1 kΩ, $C_2$ = 100 nF gegen Masse, Ausgang $\underline U_2$ an $C_2$. Maschenströme $\underline I_\mathrm{I}$ (Quelle, $R_1$, $C_1$) und $\underline I_\mathrm{II}$ ($C_1$, $R_2$, $C_2$), beide im Uhrzeigersinn als gebogene Pfeile; im gemeinsamen Zweig $C_1$ der Zweigstrom $\underline I_\mathrm{I} - \underline I_\mathrm{II}$. An den Bauteilen die Impedanzen bei ω = 10⁴ 1/s: 1 kΩ bzw. −j·1 kΩ. Daneben die Matrixgleichung mit $\begin{pmatrix} 1 - j & j \\ j & 1 - 2j \end{pmatrix}$ kΩ und rechter Seite (1 V, 0).

*Kernaussage:* Zwei Maschenströme beschreiben alle Zweigströme; die Knotenregel ist von selbst erfüllt.

*Daten:* Zahlenwerk K.

*Editor:*
- §1 Schaltplan; §2 gebogene Umlaufpfeile;
- §7 Matrix-Darstellung mit hervorgehobenen Einträgen.

*Animation:* Die Maschenströme laufen als Punkte um; im Zweig $C_1$ heben sie sich teilweise auf, eine Anzeige zeigt die Differenz.

**st1/netzwerkanalyse/02-knotenpotentiale**
- Fassung: kompakt Abb. 6, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Derselbe Tiefpass nach Umwandlung von $\underline U_q$ und $R_1$ in eine Stromquelle $\underline I_q$ = 1 mA parallel zu $G_1$ = 1 mS. Knoten 1 (zwischen $R_1$, $C_1$, $R_2$) und Knoten 2 (Ausgang), Bezugsknoten Masse mit Erdsymbol; an den Kondensatoren die Admittanzen j·1 mS. Daneben die Matrixgleichung mit $\begin{pmatrix} 2 + j & -1 \\ -1 & 1 + j \end{pmatrix}$ mS und rechter Seite (1 mA, 0), darunter das Ergebnis $\underline U_1 = (1 - j)/3$ V, $\underline U_2 = -j/3$ V.

*Kernaussage:* Zwei Knotenpotentiale beschreiben alle Spannungen; die Maschenregel ist von selbst erfüllt.

*Daten:* Zahlenwerk K.

*Editor:*
- §1 Schaltplan (Quellenumwandlung als Vorher/Nachher);
- §7 Matrix-Darstellung; §10 Teilbilder.

*Animation:* Umwandlung der Spannungsquelle in die Stromquelle als Übergang; danach füllt sich die Matrix Eintrag für Eintrag, jeweils mit Aufleuchten des zugehörigen Bauteils.

**st1/netzwerkanalyse/02-zeigerbild**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Zwei komplexe Ebenen nebeneinander. Links Spannungen (Maßstab 1 V): $\underline U_q$ = 1 V bei 0°, $\underline U_1$ = 0,471 V bei −45° (= (1 − j)/3 V), $\underline U_2$ = 0,333 V bei −90°; gestrichelt $R_1 \underline I_\mathrm{I}$ von der Spitze von $\underline U_1$ zur Spitze von $\underline U_q$. Rechts Ströme (Maßstab 1 mA): $\underline I_\mathrm{I}$ = 0,745 mA bei +26,6°, $\underline I_\mathrm{II}$ = 0,333 mA bei 0°, Strom durch $C_1$ 0,471 mA bei +45° als Differenz, gestrichelt konstruiert.

*Kernaussage:* Beide Verfahren liefern dieselben Zeiger; bei ω = 1/(RC) eilt der Ausgang dem Eingang um 90° nach und hat ein Drittel der Amplitude.

*Daten:* Zahlenwerk K.

*Editor:*
- §8 Zeiger in der komplexen Ebene (statisch, mehrere Zeiger, zwei Maßstäbe);
- §2 Pfeile mit Text; §10 Teilbilder.

*Animation:* Die Zeiger rotieren gemeinsam mit ω; die Projektionen zeichnen die drei Zeitverläufe daneben.

**st1/netzwerkanalyse/02-gesteuerte-quelle-matrix**
- Fassung: kompakt Abb. 7, ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Links das Kleinsignal-Ersatzschaltbild der Verstärkerstufe mit Knoten G, D, S (wie 02-verstaerker-kleinsignal b). Rechts die Leitwertmatrix (Zeilen und Spalten G, D, S) in mS: Zeile G (0,1; 0; 0), Zeile D (1; 0,225; −1,025), Zeile S (−1; −0,025; 2,025). Einträge der passiven Leitwerte blau (sie sind symmetrisch), die vier Anteile der gesteuerten Quelle orange: +1 (Zeile D, Spalte G), −1 (Zeile D, Spalte S), −1 (Zeile S, Spalte G), +1 (Zeile S, Spalte S). Pfeile: von der Steuerspannung $u_{GS}$ zu den Spalten G und S, vom Quellenstrom zu den Zeilen D und S. Darunter das Ergebnis 10 mV, −23,26 mV, 4,65 mV und die Verstärkung −2,33.

*Kernaussage:* Eine gesteuerte Quelle steht in den Zeilen der Knoten, zwischen denen ihr Strom fließt, und in den Spalten der Knoten, deren Spannung sie steuert; deshalb ist die Matrix nicht mehr symmetrisch.

*Daten:* Zahlenwerk L.

*Editor:*
- §1, §28 gesteuerte Quelle;
- §7 Matrix-Darstellung mit farbig hervorgehobenen Einträgen; §2 Pfeile.

*Animation:* Die vier orangefarbenen Einträge erscheinen nacheinander, während die Raute und die Knoten G, S (Steuerung) bzw. D, S (Strom) aufleuchten.

