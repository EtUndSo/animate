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
- benötigte Editor-Funktionen mit Verweis auf die Abschnitte in `EDITOR_GRAFIK_FEATURES.md` (§1 bis §39); welche davon der Editor schon kann, steht in `EDITOR_WERKZEUGE.md`;
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

---

## ST1 Netzwerkanalyse: Netzwerkgleichungen systematisch aufstellen, modifizierte Knotenanalyse
Zahlenwerk: `notizen/st1/zahlen_netzwerkanalyse.py` (Ausgabe `.txt`), Abschnitte O bis Y; Beispielsysteme wie im vorigen Thema (RC-Tiefpass mit R = 1 kΩ, C = 100 nF, ω = 10⁴ 1/s; Verstärkerstufe mit g_m = 1 mS, g_o = 25 µS), dazu Schwingkreis 100 mH ∥ 100 nF, Gate-Source-Kapazität 100 fF, Gate-Drain-Kapazität 20 fF, Lastkapazität 10 pF und ein invertierender Verstärker mit 10 kΩ und 100 kΩ. Einheitensystem der Matrizen: mS, kΩ, V, mA bzw. mS, kΩ, mV, µA. Komplexe Größen unterstrichen.

**st1/netzwerkanalyse/03-netzliste-matrix**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Drei Teile nebeneinander bzw. auf dem Handy untereinander.
- (a) Schaltbild des RC-Tiefpasses: ideale Spannungsquelle $\underline U_q$ = 1 V (Zeiger 0°) zwischen Knoten 1 (+) und Masse 0; $R_1$ = 1 kΩ von 1 nach 2, $C_1$ = 100 nF von 2 nach 0, $R_2$ = 1 kΩ von 2 nach 3, $C_2$ = 100 nF von 3 nach 0; Knotennummern an den Knotenpunkten; Vermerk ω = 10⁴ 1/s.
- (b) Netzliste als Tabelle mit den Spalten Name, Knoten (+), Knoten (−), Wert: U_q 1 0 1 V; R_1 1 2 1 kΩ; C_1 2 0 100 nF; R_2 2 3 1 kΩ; C_2 3 0 100 nF.
- (c) Die 4×4-Matrix (Zeilen: Knotengleichungen 1, 2, 3 und Zweiggleichung der Quelle; Spalten $\underline U_1$, $\underline U_2$, $\underline U_3$, $\underline I_z$; Einheiten mS, kΩ, V, mA): (1; −1; 0; 1), (−1; 2 + j; −1; 0), (0; −1; 1 + j; 0), (1; 0; 0; 0); rechte Seite (0; 0; 0; 1 V). Jeder Eintrag in der Farbe des Bauteils, das ihn liefert; zusammengesetzte Einträge (2 + j aus $R_1$, $R_2$ und $C_1$; 1 + j aus $R_2$ und $C_2$) als gestapelte Farbfelder. Farben: $R_1$ blau, $C_1$ orange, $R_2$ grün, $C_2$ violett, $\underline U_q$ rot.

*Kernaussage:* Jedes Bauteil schreibt ein festes Muster in die Zeilen und Spalten seiner Knoten; die Matrix ist die Summe dieser Muster.

*Daten:* Zahlenwerk Q.

*Editor:*
- §1 Schaltplan; §31 Netzliste und Matrix-Aufbau;
- §7 Matrix-Darstellung; §10 Teilbilder.

*Animation:* Die Netzliste wird Zeile für Zeile abgearbeitet: Die Zeile und das Bauteil leuchten auf, seine Einträge fliegen in die Matrix und addieren sich zu den vorhandenen.

**st1/netzwerkanalyse/03-eintragsmuster-knoten**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei Musterkarten nebeneinander, jede mit Schaltsymbol links und Matrixausschnitt rechts.
- Admittanz $\underline Y$ zwischen den Knoten a und b, Zählpfeil $\underline I$ von a nach b: Zeilen a, b und Spalten a, b mit (+Y; −Y) und (−Y; +Y).
- Spannungsgesteuerte Stromquelle (Raute) zwischen a und b, Strom $g\,(\underline U_c - \underline U_d)$ von a durch die Quelle nach b; Steuerspannung zwischen c (+) und d (−), gestrichelt zugeordnet: Zeilen a, b und Spalten c, d mit (+g; −g) und (−g; +g).
- Unabhängige Stromquelle $\underline I_q$, Strompfeil durch die Quelle von b nach a: kein Matrixeintrag, rechte Seite +$\underline I_q$ in Zeile a und −$\underline I_q$ in Zeile b.
- Unter jeder Karte die Vorzeichenregel: am Zeilenrand + für den Knoten, den der Zählstrom verlässt, − für den, an dem er ankommt; am Spaltenrand + für den Knoten am Pluspol der steuernden Spannung, − für den am Minuspol; im Feld das Produkt.

*Kernaussage:* Ein Bauelement erscheint nur in den Zeilen der Knoten, zwischen denen sein Strom fließt, und in den Spalten der Knoten, deren Spannung diesen Strom bestimmt.

*Daten:* schematisch.

*Editor:*
- §1, §28 (Raute); §2 Zählpfeile;
- §31 Musterkarten mit Vorzeichenrand.

*Animation:* Die Vorzeichen am Zeilen- und Spaltenrand werden eingeblendet, danach erscheint ihr Produkt in jedem Feld.

**st1/netzwerkanalyse/03-vollstaendige-matrix**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Links das Kleinsignal-Ersatzschaltbild der Verstärkerstufe mit Norton-Signalquelle (1 µA parallel zu 0,1 mS zwischen G und Masse), $G_D$ und $G_L$ (je 0,1 mS) von D nach Masse, $G_S$ (1 mS) von S nach Masse, $g_o$ (0,025 mS) zwischen D und S, Raute $g_m u_{GS}$ (1 mS) von D nach S; Knoten 0 (Masse), G, D, S. Rechts die vollständige Matrix mit Zeilen und Spalten 0, G, D, S in mS: Zeile 0 (1,3; −0,1; −0,2; −1), Zeile G (−0,1; 0,1; 0; 0), Zeile D (−0,2; 1; 0,225; −1,025), Zeile S (−1; −1; −0,025; 2,025); rechte Seite in µA (−1; 1; 0; 0). Am rechten Rand die Zeilensummen, am unteren Rand die Spaltensummen, alle 0. Zeile 0 und Spalte 0 grau durchgestrichen, die verbleibende 3×3-Matrix umrahmt; daneben die Lösung 10 mV, −23,26 mV, 4,65 mV.

*Kernaussage:* In der vollständigen Matrix ist jede Zeilen- und Spaltensumme null; streicht man Zeile und Spalte des Bezugsknotens, bleibt die lösbare Leitwertmatrix.

*Daten:* Zahlenwerk O.

*Editor:*
- §1, §28; §7 Matrix;
- §31 Summenrand und Durchstreichen; §10 Teilbilder.

*Animation:* Die sechs Bauteile werden nacheinander eingetragen (Reihenfolge wie im Zahlenwerk O), dann laufen die Summen ein, zuletzt werden Zeile und Spalte 0 gestrichen.

**st1/netzwerkanalyse/03-cramer-laplace**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Drei Teile.
- (a) Leitwertmatrix der Verstärkerstufe (3×3, mS; Zeilen und Spalten G, D, S): (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025); daneben dieselbe Matrix mit Spalte D durch die rechte Seite (1; 0; 0) µA ersetzt, die ersetzte Spalte orange.
- (b) Entwicklung nach der ersetzten Spalte: Schachbrettmuster der Vorzeichen (+ − + / − + − / + − +) halbtransparent über der Matrix; der einzige Eintrag ungleich null, 1 µA oben in Spalte D, trägt das Vorzeichen −; Zeile G und Spalte D gedimmt, die Streichungsmatrix (1; −1,025 / −1; 2,025) mit der Determinante 1 hervorgehoben; Ergebnis −1. Ebenso die Determinante der Matrix selbst nach Zeile G: 0,1 · 0,43 = 0,043.
- (c) Sarrus-Schema für dieselbe Determinante: Spalten G und D rechts wiederholt, drei absteigende Diagonalen blau (Produkte 0,04556; 0; 0), drei aufsteigende rot (Produkte 0; −0,00256; 0, mit Minus gezählt); Summe 0,043.
- Unten die Zeile: Spannung am Drain = −1/0,043 mV = −23,26 mV.

*Kernaussage:* Jede Unbekannte ist ein Quotient zweier Determinanten mit demselben Nenner; man entwickelt nach der Zeile oder Spalte mit den meisten Nullen.

*Daten:* Zahlenwerk P.

*Editor:*
- §7 Matrix; §31 Spaltenersatz, Schachbrett, Streichungsmatrix, Sarrus-Diagonalen;
- §10 Teilbilder.

*Animation:* Die rechte Seite wandert in Spalte D, danach werden Zeile und Spalte gestrichen und die Teildeterminanten Schritt für Schritt ausgerechnet.

**st1/netzwerkanalyse/03-rechenaufwand**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Halblogarithmisches Diagramm. x-Achse: Zahl der Unbekannten n von 2 bis 25, linear. y-Achse: Zahl der Multiplikationen und Divisionen, logarithmisch von 1 bis 10²⁸.
- Rote Kurve: Cramersche Regel mit Laplace-Entwicklung, (n + 1)·M(n) + n mit M(2) = 2 und M(n) = n·(M(n − 1) + 1); Werte bei n = 3, 5, 10, 15, 20, 25: 39; 1235; 6,9·10⁷; 3,6·10¹³; 8,8·10¹⁹; 6,9·10²⁶.
- Blaue Kurve: Gauß-Elimination, (n³ − n)/3 + n²; Werte 17; 65; 430; 1345; 3060; 5825.
- Waagrechte gestrichelte Bezugslinien für die Rechenzeit bei 10⁹ Operationen pro Sekunde: 1 s (10⁹), 1 h (3,6·10¹²), 1 Jahr (3,2·10¹⁶). Markiert: n = 20 mit 2800 Jahren gegen 3 µs.

*Kernaussage:* Determinanten durch Entwicklung kosten rund n! Rechenschritte, die Elimination rund n³/3; die Cramersche Regel lohnt sich nur für kleine Systeme und für Formeln.

*Daten:* Zahlenwerk P (Tabelle Rechenaufwand).

*Editor:*
- §12 halblogarithmische Achsen; §11 Datenkurven; §4 Beschriftung und Bezugslinien.

*Animation:* keine.

**st1/netzwerkanalyse/03-mna-spannungsquelle**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Drei Teile.
- (a) Kennlinien im I-U-Diagramm (I in mA waagrecht von −2 bis 2, U in V senkrecht von 0 bis 2): Leitwert 1 mS als Gerade durch den Ursprung; ideale Spannungsquelle 1 V als waagrechte Linie bei U = 1 V, die jeden Strom zulässt. Beschriftung: „Strom aus der Spannung: I = G U“ bzw. „Strom nicht aus der Spannung bestimmbar“.
- (b) Ideale Spannungsquelle $\underline U_q$ zwischen den Knoten a (+) und b (−) an einem Kasten „übriges Netz“; Spannungspfeil $\underline U_q$ von a nach b; Strompfeil $\underline I_z$ von a in die Quelle hinein.
- (c) Die Leitwertmatrix als grauer Block, rechts angefügt die Spalte für $\underline I_z$ mit +1 in Zeile a und −1 in Zeile b, unten angefügt die Zeile mit +1 in Spalte a, −1 in Spalte b und 0 in der Ecke; rechte Seite $\underline U_q$ in der neuen Zeile.

*Kernaussage:* Der Strom der Quelle wird zur Unbekannten und bekommt eine Spalte, ihre Zweiggleichung wird zur neuen Zeile.

*Daten:* schematisch; Kennlinien mit 1 mS und 1 V.

*Editor:*
- §1, §2; §4 Kennlinien; §7, §31 Blockmatrix mit Zusatzzeile und -spalte;
- §10 Teilbilder.

*Animation:* Die Spalte schiebt sich von rechts, die Zeile von unten an den grauen Block.

**st1/netzwerkanalyse/03-eintragsmuster-mna**
- Fassung: kompakt Abb. 5, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Musterkarten wie in 03-eintragsmuster-knoten, je Symbol, Zweiggleichung und Matrixausschnitt (Zeilen a, b und Zusatzzeile; Spalten a, b, c, d und Zusatzspalte).
- Impedanz $\underline Z$ zwischen a und b: Zusatzspalte +1/−1, Zusatzzeile +1/−1, in der Ecke −Z, rechte Seite 0; daneben der Sonderfall Z = 0 (Kurzschluss, Strommesser, Spule bei Gleichstrom).
- Tor (Spannungsquelle $\underline U_q$ in Reihe mit $\underline Z_q$): wie die Impedanz, Ecke −Z_q, rechte Seite $\underline U_q$.
- Spannungsgesteuerte Spannungsquelle mit Faktor v: Zusatzzeile +1, −1 in den Spalten a, b und −v, +v in den Spalten c, d.
- Stromgesteuerte Stromquelle mit Faktor β, Steuerstrom $\underline I_\mathrm{St}$ als Zusatzunbekannte eines anderen Zweigs (etwa einer 0-V-Quelle): +β in Zeile a und −β in Zeile b in der Spalte von $\underline I_\mathrm{St}$; keine eigene Zeile.
- Stromgesteuerte Spannungsquelle mit Faktor $r_m$: Zusatzspalte ±1, Zusatzzeile +1/−1 und −$r_m$ in der Spalte von $\underline I_\mathrm{St}$.
- Nullor: Nullator (Oval) zwischen c und d, Norator (zwei überlappende Kreise) zwischen a und b; Zusatzspalte +1/−1 in den Zeilen a, b; Zusatzzeile +1, −1 in den Spalten c, d.

*Kernaussage:* Alle Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon geführten Strom ergibt, haben dasselbe Gerüst: eine Spalte für ihren Strom und eine Zeile für ihre Zweiggleichung.

*Daten:* schematisch.

*Editor:*
- §1, §28; §31 Musterkarten und Nullor-Symbole; §7.

*Animation:* keine.

**st1/netzwerkanalyse/03-schwingkreis**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teile.
- (a) Schaltbild: Stromquelle 1 mA in Knoten 1, parallel dazu $C$ = 100 nF und $L$ = 100 mH gegen Masse; Strompfeil $\underline I_L$ durch die Spule nach unten.
- (b) Zwei gestapelte Diagramme mit gemeinsamer x-Achse ω in 1/s von 0 bis 2·10⁴, linear. Oben die Determinante der 2×2-Matrix, ω²LC − 1 (einheitenlos im System mS, kΩ), von −1 bis 3: Parabel durch (0; −1), (5000; −0,75), (10⁴; 0), (2·10⁴; 3); Nullstelle bei 10⁴ 1/s markiert und mit „Resonanz“ beschriftet. Unten der Betrag $|\underline U_1|$ in V von 0 bis 3: 0 bei ω = 0, 0,667 V bei 5000 und bei 2·10⁴ 1/s, Pol bei 10⁴ 1/s (Achse oben abgeschnitten).

*Kernaussage:* Mit der Spule als Impedanz bleibt die Determinante bei Gleichstrom endlich; bei der Resonanzfrequenz wird sie null, und die verlustlose Schaltung hat keine eindeutige Lösung.

*Daten:* Zahlenwerk S.

*Editor:*
- §1; §11 Datenkurven; §13 gestapelte Diagramme; §10 Teilbilder.

*Animation:* Schieberegler für ω (§15): Ein Punkt läuft auf beiden Kurven, eine Anzeige zeigt die Matrix mit den aktuellen Einträgen.

**st1/netzwerkanalyse/03-strommesser-transitfrequenz**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Zwei Teile.
- (a) Ersatzschaltbild: Stromquelle $\underline I_\mathrm{ein}$ in den Gate-Knoten G; $C_{gs}$ = 100 fF von G nach Masse (Source); gestrichelt $C_{gd}$ = 20 fF von G nach D; Raute $g_m u_{GS}$ = 1 mS von D nach Masse; $g_o$ = 25 µS von D nach Masse; zwischen D und Masse eine Spannungsquelle 0 V als Strommesser, Strompfeil $\underline I_\mathrm{aus}$ von D in die Quelle.
- (b) Doppeltlogarithmisches Diagramm: x-Achse f in Hz von 10⁷ bis 10¹⁰; y-Achse $|\underline I_\mathrm{aus}/\underline I_\mathrm{ein}|$ von 0,1 bis 1000. Durchgezogen die Gerade $g_m/(2\pi f C_{gs})$: 159 bei 10 MHz, 15,9 bei 100 MHz, 1,59 bei 1 GHz, 1 bei 1,59 GHz; gestrichelt die Kurve mit $C_{gd}$ aus Zahlenwerk T: 132,6 bei 10 MHz, 13,26 bei 100 MHz, 1,337 bei 1 GHz, 1 bei 1,345 GHz, oberhalb einiger GHz flacher, 0,213 bei 10 GHz, Grenzwert 0,1667 als waagrechte gepunktete Hilfslinie; waagrechte Linie bei 1; beide Transitfrequenzen markiert.

*Kernaussage:* Die Spannungsquelle von 0 V schließt den Ausgang kurz, wie es die Definition der Transitfrequenz verlangt, und liefert den Kurzschlussstrom als Unbekannte; ohne $C_{gd}$ fällt die Stromverstärkung mit 1/f und erreicht 1 bei der Transitfrequenz.

*Daten:* Zahlenwerk T.

*Editor:*
- §1, §28; §4 doppeltlogarithmische Achsen; §11; §10.

*Animation:* keine.

**st1/netzwerkanalyse/03-nullor-verstaerker**
- Fassung: kompakt Abb. 6, ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Zwei Teile.
- (a) Invertierender Verstärker: Quelle $U_E$ = 0,1 V mit $R_1$ = 10 kΩ an Knoten 1 (Minuseingang), $R_2$ = 100 kΩ von Knoten 1 zum Ausgang A, Pluseingang an Masse. Der OPV als Nullor: Nullator (Oval) zwischen Plus- und Minuseingang, Norator (zwei überlappende Kreise) zwischen Ausgang und Masse; Strompfeile $I_E$ (von Knoten 1 in das Tor aus Quelle und $R_1$) und $I_A$ (vom Ausgang A in den Norator).
- (b) 4×4-Matrix (Spalten $U_1$, $U_A$, $I_E$, $I_A$; Einheiten mS, kΩ, V, mA): Zeile Knoten 1 (0,01; −0,01; 1; 0), Zeile Ausgang (−0,01; 0,01; 0; 1), Tor-Zeile (1; 0; −10; 0) mit rechter Seite 0,1 V, Nullator-Zeile (−1; 0; 0; 0) mit rechter Seite 0. Nullator-Zeile orange, Norator-Spalte grün. Darunter: Determinante −0,1, Zähler 0,1, $U_A$ = −1 V, Verstärkung −10; $U_1$ = 0, $I_E$ = −10 µA, $I_A$ = 10 µA.

*Kernaussage:* Ein Nullor bringt eine Zeile für die Bedingung an seinem Eingang und eine Spalte für den Strom an seinem Ausgang mit; die Ausgangsspannung ergibt sich aus der übrigen Schaltung.

*Daten:* Zahlenwerk U.

*Editor:*
- §1; §31 Nullor-Symbole; §7 Matrix; §10.

*Animation:* Schieberegler (§15) für die Leerlaufverstärkung von 10³ bis 10⁶, wobei der Nullor durch eine gesteuerte Spannungsquelle ersetzt ist: Verstärkung −9,891, −9,99945 (bei 200 000), −9,99989 nähert sich −10, die Spannung am Minuseingang 989 µV, 5 µV, 1 µV.

**st1/netzwerkanalyse/03-bode**
- Fassung: ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Zwei Teile.
- (a) Ersatzschaltbild der Verstärkerstufe ohne Source-Widerstand: Norton-Signalquelle 1 µA parallel zu 0,1 mS am Gate, $C_{gs}$ = 100 fF von G nach Masse, Raute $g_m u_{GS}$ = 1 mS von D nach Masse, am Drain der Leitwert 0,225 mS ($G_D$ + $G_L$ + $g_o$) und $C_L$ = 10 pF nach Masse.
- (b) Bode-Diagramm, zwei gestapelte Diagramme mit gemeinsamer logarithmischer Frequenzachse von 10⁵ bis 10¹⁰ Hz. Oben der Betrag in dB von −100 bis +20: Kurve $|\underline U_D/\underline U_\mathrm{sig}|$ aus der Datenreihe im Zahlenwerk V (12,95 dB bei 100 kHz, 9,94 dB bei 3,58 MHz, 3,50 dB bei 10 MHz, −17,41 dB bei 100 MHz, −52,04 dB bei 1 GHz, −91,93 dB bei 10 GHz); Asymptoten gestrichelt: waagrecht bei 12,96 dB bis 3,58 MHz, dann −20 dB/Dekade bis 159 MHz, dann −40 dB/Dekade; Eckfrequenzen 3,58 MHz und 159 MHz als senkrechte Hilfslinien; −3-dB-Punkt markiert. In zweiter Farbe $|\underline U_G/\underline U_\mathrm{sig}|$: 0 dB bis 159 MHz, dann −20 dB/Dekade (−16,07 dB bei 1 GHz). Unten der Winkel von $\underline U_D/\underline U_\mathrm{sig}$ in Grad von 0 bis 180: 178,4° bei 100 kHz, 133,7° bei 3,58 MHz, 106,1° bei 10 MHz, 59,9° bei 100 MHz, 46,3° bei 159 MHz, 9,3° bei 1 GHz.

*Kernaussage:* Die Eckfrequenzen gehören zu den Polen, den Nullstellen der Determinante; oberhalb jeder fällt der Betrag um weitere 20 dB pro Dekade.

*Daten:* Zahlenwerk V (Datenreihe).

*Editor:*
- §32 Bode-Diagramm; §13 gestapelte Diagramme; §11 Datenkurven;
- §1, §28; §10 Teilbilder.

*Animation:* Schieberegler für $C_L$ (§15) von 1 pF bis 100 pF: Die untere Eckfrequenz wandert, die Verstärkung bei tiefen Frequenzen bleibt, die Frequenz mit Betrag 1 wandert mit.

---

## ST1 Netzwerkanalyse: Testquellen und Transientenanalyse linearer Schaltungen
Zahlenwerk: `notizen/st1/zahlen_netzwerkanalyse.py` (Ausgabe `.txt`), Abschnitte Z bis AF; Beispielsysteme wie in den Themen 2 und 3 (Verstärkerstufe mit g_m = 1 mS, g_o = 25 µS, R_D = R_L = 10 kΩ, R_S = 1 kΩ, Signalquelle mit 10 kΩ; zweistufiger RC-Tiefpass mit 1 kΩ und 100 nF bei ω = 10⁴ 1/s; Stufe ohne R_S mit C_gs = 100 fF und C_L = 10 pF), dazu RC-Glied 1 kΩ/100 nF und RL-Glied 1 kΩ/100 mH (beide τ = 0,1 ms) und die MOS-Diode an 0,5 mA mit 0,25 mS und 1 nF parallel. Testquellen: Teststrom orange, Testspannung blau; abgeschaltete Quellen grau mit „= 0“. Kleinsignalgrößen klein geschrieben.

**st1/netzwerkanalyse/04-uebersicht**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Grauer Block „Schaltung“ mit Eingangsknoten 1 links und Ausgangsknoten 2 rechts. Am Eingang eine Spannungsquelle $\underline U_q$ als Testspannungsquelle (blau), am Ausgang eine Stromquelle $\underline I_T$ vom Bezugsknoten in Knoten 2 als Teststromquelle (orange). Darunter das Gleichungssystem: grau hinterlegte Matrix mit dem Vermerk „bleibt“, rechts daneben drei rechte Seiten nebeneinander: „Lauf A: $\underline U_q$ = 1 V, $\underline I_T$ = 0 → Eingangsadmittanz und Übertragung“, „Lauf B: $\underline U_q$ = 0, $\underline I_T$ = 1 A → Ausgangsimpedanz“, „Betrieb: Signal am Eingang, $\underline I_T$ = 0“.
- (b) Kondensator $C$ zwischen den Knoten a und b, Gleichheitszeichen, daneben sein Begleitmodell: Leitwert $G_C = C/h$ parallel zu einer Stromquelle $G_C\,U_n$, die in a einspeist. Darunter eine Zeitachse mit $t_0, t_1, t_2, t_3$ im Abstand $h$; ein Pfeil vom gelösten Wert $U_n$ zur Stromquelle des nächsten Schritts.

*Kernaussage:* Testquellen und Zeitschritte mit fester Schrittweite ändern nur die rechte Seite des Gleichungssystems; die Schaltung bleibt dieselbe.

*Daten:* schematisch.

*Editor:*
- §1, §28; §31 Blockmatrix mit mehreren rechten Seiten;
- §33 Ersetzungsdarstellung und Zeitachse; §34 Testquellen; §10 Teilbilder.

*Animation:* Umschalten zwischen den drei rechten Seiten: aktive Quelle farbig, abgeschaltete grau mit „= 0“; in (b) läuft die Zeitachse Schritt für Schritt, und der Wert der Stromquelle wird nach jedem Schritt aktualisiert.

**st1/netzwerkanalyse/04-teststrom-ausgang**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Kleinsignal-Ersatzschaltbild der Verstärkerstufe ohne Last, Knoten G, D, S und Masse: am Gate der Innenleitwert $G_\mathrm{sig}$ = 0,1 mS der abgeschalteten Signalquelle (Quelle grau, „0 V“); Raute $g_m u_{GS}$ = 1 mS von D nach S; $g_o$ = 25 µS zwischen D und S; $R_D$ = 10 kΩ von D nach Masse; $R_S$ = 1 kΩ von S nach Masse; Teststromquelle $\underline I_T$ = 1 µA von Masse in D (orange).
- (b) Leitwertmatrix in mS (Zeilen und Spalten G, D, S): (0,1; 0; 0), (1; 0,125; −1,025), (−1; −0,025; 2,025); rechte Seite (0; 1; 0) µA mit der 1 in Orange; Lösung (0; 8,901; 0,110) mV, als Spalte D der Inversen in kΩ gekennzeichnet; daneben die Cramersche Regel: Determinante 0,02275 mS³, Unterdeterminante ohne Zeile und Spalte D 0,2025 mS², Quotient 8,90 kΩ.
- (c) Kleine Zeile: „Im Simulator mit 1 A: 8901 V, zahlenmäßig die Impedanz in Ω“.

*Kernaussage:* Eine Teststromquelle erscheint nur auf der rechten Seite; die Antwort auf den Teststrom ist eine Spalte der Inversen, ihr Diagonaleintrag die Impedanz.

*Daten:* Zahlenwerk Z.

*Editor:*
- §1, §28; §7 Matrix; §31 Spalten- und Eintragshervorhebung;
- §34 Testquellen; §10 Teilbilder.

*Animation:* Teststrom einschalten: Der Eintrag erscheint rechts, die Lösung füllt die Spalte. Danach dieselbe Quelle ans Gate setzen: 10 mV je µA, also 10 kΩ, der Innenwiderstand der abgeschalteten Signalquelle.

**st1/netzwerkanalyse/04-testspannung-eingang**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) RC-Tiefpass: ideale Spannungsquelle $\underline U_q$ zwischen Knoten 1 (+) und Masse als Testspannungsquelle (blau); $R_1$ = 1 kΩ von 1 nach 2, $C_1$ = 100 nF von 2 nach Masse, $R_2$ = 1 kΩ von 2 nach 3, $C_2$ = 100 nF von 3 nach Masse; Teststromquelle $\underline I_T$ von Masse in Knoten 3 (orange); Vermerk ω = 10⁴ 1/s. Strompfeil $\underline I_\mathrm{ein}$ aus der Quelle in Knoten 1, gestrichelt der Zusatzstrom $\underline I_z$ in den Pluspol (entgegengesetzt).
- (b) Matrix der modifizierten Knotenanalyse in mS, kΩ, V und mA (Spalten $\underline U_1$, $\underline U_2$, $\underline U_3$, $\underline I_z$): (1; −1; 0; 1), (−1; 2 + j; −1; 0), (0; −1; 1 + j; 0), (1; 0; 0; 0). Zwei rechte Seiten: Lauf A (0; 0; 0; 1 V) mit dem Ergebnis $\underline I_z$ = −(0,667 + 0,333j) mA, also $\underline Y_\mathrm{ein}$ = (0,667 + 0,333j) mS, und $\underline U_3$ = −j/3 V, also $\underline A_V$ = −j/3; Lauf B (0; 0; 1 mA; 0) mit $\underline U_3$ = (0,333 − 0,667j) V, also $\underline Z_\mathrm{aus}$ = (0,333 − 0,667j) kΩ.
- (c) Falsch, rot markiert: Quelle entfernt statt kurzgeschlossen, Knoten 1 offen, $R_1$ hängt frei; $\underline Z_\mathrm{aus}$ wäre (0,2 − 0,6j) kΩ.

*Kernaussage:* Zwei Läufe an derselben Matrix ergeben Eingangsadmittanz, Übertragung und Ausgangsimpedanz; abgeschaltet ist die Spannungsquelle ein Kurzschluss, kein Leerlauf.

*Daten:* Zahlenwerk AA.

*Editor:*
- §1, §2 Zählpfeile; §31 Blockmatrix mit zwei rechten Seiten;
- §34 Testquellen und Ersatz durch Kurzschluss; §10 Teilbilder.

*Animation:* Wechsel zwischen Lauf A und Lauf B; im Lauf B wird die Spannungsquelle grau und zeigt „0 V = Kurzschluss“.

**st1/netzwerkanalyse/04-innerer-knoten**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Teilbilder der Verstärkerstufe mit Gleichgrößen: Versorgung 5 V, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ, n-Kanal-MOSFET, Gate auf 1,25 V.
- Links: Teststromquelle am Source-Knoten mit Gleichanteil null (orange): Arbeitspunkt unverändert, $U_S$ = 0,25 V, $U_D$ = 2,5 V, $I_D$ = 0,25 mA, Sättigung; Kleinsignalwerte $g_m$ = 1 mS, Ausgangsleitwert 25 µS.
- Rechts: Spannungsquelle am Source-Knoten ohne Gleichanteil (blau, rot umrandet): $U_S$ = 0 V, Triodenbereich, $U_D$ = 0,426 V, $I_D$ = 0,457 mA; Kleinsignalwerte $g_m$ = 0,852 mS, Ausgangsleitwert 0,648 mS.
- Optional unter beiden: Ausgangskennlinienfeld mit dem jeweiligen Arbeitspunkt.

*Kernaussage:* Eine Spannungsquelle an einem inneren Knoten legt auch dessen Gleichspannung fest und verschiebt den Arbeitspunkt; eine Stromquelle ohne Gleichanteil ist für Gleichstrom ein Leerlauf.

*Daten:* Zahlenwerk AB.

*Editor:*
- §1, §24 MOSFET-Symbol; §4 Kennlinienfeld;
- §34 Testquellen; §10 Teilbilder.

*Animation:* Umschalten der Testquelle zwischen Strom- und Spannungsquelle; die Arbeitspunktwerte wechseln mit.

**st1/netzwerkanalyse/04-ersatzzweitor**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Ersatzzweitor in Thévenin-Form: am Eingangstor die Admittanz $\underline Y_\mathrm{ein}$ zwischen Eingangsklemme und Masse; am Ausgangstor eine spannungsgesteuerte Spannungsquelle $\underline A_V \underline U_\mathrm{ein}$ (Raute) in Reihe mit $\underline Z_\mathrm{aus}$. Zählpfeile $\underline U_\mathrm{ein}$, $\underline I_\mathrm{ein}$ (in den Eingang), $\underline U_\mathrm{aus}$, $\underline I_\mathrm{aus}$ (aus dem Ausgang in die Last). Links grau die Testspannungsquelle, rechts grau die Teststromquelle.
- (b) Norton-Form: gesteuerte Stromquelle $(\underline A_V/\underline Z_\mathrm{aus})\,\underline U_\mathrm{ein}$ in den Ausgangsknoten parallel zu $\underline Z_\mathrm{aus}$.
- (c) Werte der Verstärkerstufe: $\underline Y_\mathrm{ein}$ = 0, $\underline A_V$ = −4,40, $\underline Z_\mathrm{aus}$ = 8,90 kΩ, $\underline A_V/\underline Z_\mathrm{aus}$ = −0,494 mS; mit Last 10 kΩ $\underline U_\mathrm{aus}/\underline U_\mathrm{ein}$ = −2,33, bei 10 mV −23,26 mV.

*Kernaussage:* Drei Kenngrößen aus zwei Läufen derselben Matrix beschreiben eine rückwirkungsfreie Stufe vollständig.

*Daten:* Zahlenwerk Z.

*Editor:*
- §1, §28 gesteuerte Quellen; §2 Zählpfeile;
- §34; §10 Teilbilder.

*Animation:* keine.

**st1/netzwerkanalyse/04-euler-verfahren**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) $U$ in V (0 bis 1,1) über $t$ in Vielfachen von τ (0 bis 4), τ = 0,1 ms. Exakte Ladekurve 1 V (1 − exp(−t/τ)) blau: 0; 0,393; 0,632; 0,777; 0,865; 0,918; 0,950; 0,970; 0,982 V bei 0; 0,5τ; …; 4τ. Explizites Verfahren mit $h$ = τ/2 als orange Punkte: 0; 0,500; 0,750; 0,875; 0,938; 0,969; 0,984; 0,992; 0,996 V. Implizites als grüne Punkte: 0; 0,333; 0,556; 0,704; 0,802; 0,868; 0,912; 0,941; 0,961 V. Am ersten Schritt die Tangente im Startpunkt mit der Steigung $U_q/\tau$ = 10 V/ms (gestrichelt, orange) bis 0,5 V bei 0,5τ und die Gerade durch den Startpunkt mit der Steigung, die zum Endwert 0,333 V gehört (gestrichelt, grün).
- (b) $U_n$ in V über $n$ = 0 bis 5 für $h$ = 3τ: explizit 0; 3; −3; 9; −15; 33 V (orange, Zickzack, Achse oben und unten abgeschnitten mit Wertangabe); implizit 0; 0,750; 0,938; 0,984; 0,996; 0,999 V (grün); Endwert 1 V gestrichelt.

*Kernaussage:* Das explizite Verfahren nimmt die Steigung am Anfang des Schritts, das implizite die am Ende; bei großen Schritten schaukelt sich das explizite auf, das implizite bleibt stabil.

*Daten:* Zahlenwerk AC (Datenreihe $h$ = τ/2, Folgen $h$ = 3τ).

*Editor:*
- §11 Datenkurven; §29 Tangenten; §33 Zeitschritte;
- §10 Teilbilder.

*Animation:* Schieberegler für $h$/τ (§15) von 0,1 bis 3: Punkte und Steigungsstücke folgen; ab $h$ = 2τ wächst die explizite Folge.

**st1/netzwerkanalyse/04-begleitmodell-kondensator**
- Fassung: kompakt Abb. 5, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Vier Teilbilder.
- (a) Kondensator $C$ zwischen den Knoten a (oben) und b, Spannungspfeil $U_{n+1}$ von a nach b, Strompfeil $I_{n+1}$ von a nach b.
- (b) Gleichheitszeichen, daneben das Begleitmodell: Leitwert $G_C = C/h$ zwischen a und b, parallel eine Stromquelle mit dem Wert $G_C U_n$, Pfeil durch die Quelle von b nach a (speist in a ein).
- (c) Matrixausschnitt mit Zeilen und Spalten a, b: +$G_C$ auf (a, a) und (b, b), −$G_C$ auf (a, b) und (b, a); daneben grau dieselben Plätze mit $j\omega C$ aus der Wechselstromanalyse; rechte Seite +$G_C U_n$ in Zeile a, −$G_C U_n$ in Zeile b.
- (d) RC-Glied: Quelle 1 V über $R$ = 1 kΩ an $C$ = 100 nF; im Zeitschritt $h$ = 10 µs wird $C$ zu 10 mS parallel zur Stromquelle. Wertetabelle $n$ und $U_n$: 0; 0,0909; 0,1736; 0,2487; 0,3170; 0,3791 V, … , $U_{10}$ = 0,614 V gegen exakt 0,632 V.

*Kernaussage:* Im Zeitschritt wird der Kondensator zu einem Leitwert, und seine Vorgeschichte steht als Stromquelle auf der rechten Seite.

*Daten:* Zahlenwerk AD.

*Editor:*
- §1; §31 Musterkarten und Matrixausschnitt;
- §33 Ersetzungsdarstellung; §10 Teilbilder.

*Animation:* Zeitschritte nacheinander: Die Stromquelle wächst mit $U_n$, die Tabelle füllt sich.

**st1/netzwerkanalyse/04-begleitmodell-spule**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Vier Teilbilder.
- (a) Spule $L$ zwischen a und b mit $U_{n+1}$ und $I_{n+1}$ von a nach b.
- (b) Begleitmodell: Leitwert $h/L$ zwischen a und b parallel zu einer Stromquelle $I_n$, Pfeil durch die Quelle von a nach b (in Richtung des Spulenstroms).
- (c) Matrixausschnitt: $h/L$ an den Plätzen eines Leitwerts; rechte Seite −$I_n$ in Zeile a, +$I_n$ in Zeile b.
- (d) RL-Glied: Quelle 1 V über $R$ = 1 kΩ an $L$ = 100 mH, τ = 0,1 ms; im Zeitschritt $h$ = 10 µs wird $L$ zu 0,1 mS parallel zur Stromquelle; $U_1$ = 0,909 V, $I_1$ = 0,0909 mA, $I_2$ = 0,1736 mA, $I_{10}$ = 0,614 mA gegen exakt 0,632 mA.

*Kernaussage:* Die Spule wird zu einem kleinen Leitwert, und eine Stromquelle führt ihren bisherigen Strom weiter.

*Daten:* Zahlenwerk AD.

*Editor:*
- §1; §31; §33 Ersetzungsdarstellung; §10.

*Animation:* keine.

**st1/netzwerkanalyse/04-verstaerker-transiente**
- Fassung: kompakt Abb. 6, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand: am Gate eine Stromquelle 1 µA, die bei $t$ = 0 einschaltet (Sprung der Signalspannung auf 10 mV), parallel 0,1 mS und $C_{gs}$ = 100 fF; Raute $g_m u_{GS}$ = 1 mS von D nach Masse; am Drain 0,225 mS und $C_L$ = 10 pF. Darunter dieselbe Schaltung im Zeitschritt $h$ = 5 ns: $C_{gs}$ wird zu 0,02 mS parallel zu einer Stromquelle 0,02 mS · $u_{G,n}$, $C_L$ zu 2 mS parallel zu 2 mS · $u_{D,n}$; Matrix (0,12; 0 / 1; 2,225) mS mit dem Vermerk „in jedem Schritt dieselbe“.
- (b) Zwei gestapelte Diagramme über $t$ von 0 bis 300 ns. Oben $u_G$ in mV (0 bis 12): exakt 6,32 mV bei 1 ns, 9,93 mV bei 5 ns, danach 10 mV (blau); implizite Werte als Punkte 8,33; 9,72; 9,95; 9,99 mV bei 5, 10, 15, 20 ns. Unten $u_D$ in mV (0 bis −50): exakt −3,82; −8,14; −15,45; −29,68; −39,65; −43,94; −44,39 mV bei 5, 10, 20, 50, 100, 200, 300 ns (blau); implizit −3,75; −7,74; −14,76; −28,79; −39,05; −43,81; −44,37 mV (Punkte); Endwert −44,44 mV gestrichelt; Anstiegszeit 10 % bis 90 % von 97,7 ns als Maßpfeil.
- (c) Kleines Diagramm: explizites Verfahren mit derselben Schrittweite am Gate, 0; 50; −150; 650; −2550 mV nach 0 bis 4 Schritten (Betragsachse logarithmisch oder abgeschnitten, Faktor −4 je Schritt beschriftet).

*Kernaussage:* Die Matrix ist in jedem Schritt dieselbe; die schnelle Zeitkonstante von 1 ns macht das explizite Verfahren bei 5 ns instabil, das implizite rechnet stabil weiter.

*Daten:* Zahlenwerk AE.

*Editor:*
- §1, §28; §11 Datenkurven; §13 gestapelte Diagramme;
- §33 Zeitschritte; §10 Teilbilder.

*Animation:* Schieberegler für $h$ (§15) von 0,5 bis 10 ns: Die impliziten Punkte folgen der Kurve mit wachsendem Fehler, die explizite Folge wächst ab 2 ns.

**st1/netzwerkanalyse/04-spice-ablauf**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Ablaufdiagramm mit neun Kästen und zwei Rauten:
- (1) „Arbeitspunkt als Startzustand“; (2) „Begleitmodelle der nichtlinearen Bauelemente aus der aktuellen Schätzung“; (3) „Leitwerte und Ströme ins Gleichungssystem eintragen“; (4) „lineares System lösen“; (5) Raute „konvergiert?“: nein → (6) „neue Schätzung“ → zurück zu (2), innere Schleife orange beschriftet „Newton-Verfahren“; ja → (7) „Zeitschritt h wählen, $t_{n+1} = t_n + h$“; (8) Raute „Endzeit erreicht?“: ja → „Ende“; nein → (9) „Begleitmodelle der Kondensatoren und Spulen aus dem neuen Zustand“ → zurück zu (2), äußere Schleife blau beschriftet „Zeit“.
- Daneben zwei kleine gestapelte Diagramme für die MOS-Diode an 0,5 mA und 0,25 mS mit 1 nF parallel, $h$ = 0,1 µs, $t$ von 0 bis 5 µs: oben $U$ in V von 0 auf 0,991 V (Schwelle 0,5 V bei 1,15 µs markiert, Endwert 1 V gestrichelt); unten Newton-Durchläufe je Zeitschritt als Säulen: 2 bis 1,1 µs, danach 3 bis 4, ab etwa 2 µs 3.

*Kernaussage:* Außen läuft die Zeit, innen das Newton-Verfahren; beide führen jede Rechnung auf ein lineares Gleichungssystem zurück.

*Daten:* Zahlenwerk AF.

*Editor:*
- §19 Blockbilder mit Rauten; §11 Datenkurven; §13 gestapelte Diagramme; §10 Teilbilder.

*Animation:* Ein Marker läuft durch das Ablaufdiagramm, synchron dazu wächst die Kurve um einen Zeitschritt, und die Säule des Schritts zählt die Newton-Durchläufe hoch.

## ST1 Netzwerkanalyse: Vierpole, Parameterformen und Zusammenschaltung
Zahlenwerk: `notizen/st1/zahlen_netzwerkanalyse.py` (Ausgabe `.txt`), Abschnitte AH bis AP; Beispielsysteme wie in den Themen 2 bis 4 (RC-Glied 1 kΩ längs, 100 nF quer bei ω = 10⁴ 1/s, zweistufiger RC-Tiefpass als Kette zweier solcher Glieder; Verstärkerstufe mit $g_m$ = 1 mS, $g_o$ = 25 µS, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ; Stufe ohne $R_S$ mit $C_{gs}$ = 100 fF, $C_{gd}$ = 20 fF bei ω = 10⁸ 1/s), dazu zwei T-Glieder aus je drei 1-kΩ-Widerständen, der Bipolar-Beispieltransistor aus ET1 ($r_{BE}$ = 13,71 kΩ, β = 502,4, $r_{CE}$ = 79,57 kΩ, $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ) und ein Vorspannungsteiler 400 kΩ/133,3 kΩ (100 kΩ) für die Signalkette. Symmetrische Zählpfeile: Torströme in die oberen Klemmen hinein, Torspannungen von oben nach unten; in der Kettenform der Ausgangsstrom als $-\underline I_2$ hinaus. Zweitore als graue Kästen mit Klemmen 1, 1′, 2, 2′; Teilzweitore a und b; Matrizen unter den Schaltungen.

**st1/netzwerkanalyse/05-uebersicht**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Ein Zweitor als grauer Kasten mit Klemmen 1 und 1′ links (Eingangstor, Tor 1) und 2 und 2′ rechts (Ausgangstor, Tor 2). Strompfeile $\underline I_1$ in Klemme 1 hinein und an 1′ heraus, $\underline I_2$ in Klemme 2 hinein und an 2′ heraus; Spannungspfeile $\underline U_1$ und $\underline U_2$ von oben nach unten.
- (b) Drei kleine Schemata nebeneinander, je zwei Kästen a und b: Kettenschaltung (Ausgang von a an Eingang von b) mit der Beschriftung $\mathbf A = \mathbf A_\mathrm a\mathbf A_\mathrm b$; Parallelschaltung (beide Eingänge parallel, beide Ausgänge parallel, gemeinsame Spannungen hervorgehoben) mit $\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b$; Reihenschaltung (Eingänge in Reihe, Ausgänge in Reihe, gemeinsame Ströme hervorgehoben) mit $\mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$.

*Kernaussage:* Jede Zusammenschaltung wird in der Form zur Addition oder Multiplikation der Matrizen, deren vorgegebene Größen allen Teilen gemeinsam sind.

*Daten:* schematisch.

*Editor:*
- §1, §2 Zählpfeile; §35 Zweitor-Kästen und Zusammenschaltungsvorlagen;
- §10 Teilbilder.

*Animation:* Umschalten zwischen den drei Zusammenschaltungen; die gemeinsamen Größen (Strom oder Spannung) leuchten jeweils auf, die passende Matrixoperation erscheint darunter.

**st1/netzwerkanalyse/05-tor-und-vierpol**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- Links ein Vierpol als Kasten mit vier Klemmen; an drei Klemmen äußere Leitungen mit beliebig verteilten Strömen (Beispielwerte 2 mA hinein an Klemme 1, 0,5 mA heraus an 1′, 1,5 mA heraus an 2, an 2′ nichts), darunter „Summe der vier Ströme: null“.
- Rechts derselbe Kasten zwischen einer Signalquelle am Klemmenpaar 1–1′ und einer Last am Klemmenpaar 2–2′; gleich große Strompfeile an 1 hinein und 1′ heraus, an 2 und 2′ ebenso; Beschriftung $\underline I_1 = \underline I_{1'}$, $\underline I_2 = \underline I_{2'}$.

*Kernaussage:* Erst die Torbedingung macht aus vier Klemmen zwei Tore; sie hängt von der äußeren Beschaltung ab.

*Daten:* schematisch (Stromwerte links frei gewählt).

*Editor:*
- §1, §2; §35 Klemmenstrompfeile mit Werten;
- §10 Teilbilder.

*Animation:* keine.

**st1/netzwerkanalyse/05-kurzschluss-leerlauf**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Vier Teilbilder des RC-Glieds (1 kΩ von Klemme 1 nach 2, 100 nF von 2 zur unteren Leitung; ω = 10⁴ 1/s, Kondensator j·1 mS).
- (a) Ausgang kurzgeschlossen (Kurzschlussbügel an Tor 2), Spannungsquelle 1 V an Tor 1: Kondensator grau als überbrückt; $\underline I_1$ = 1 mA, $\underline I_2$ = −1 mA; Ergebnis $\underline Y_{11}$ = 1 mS, $\underline Y_{21}$ = −1 mS.
- (b) Eingang kurzgeschlossen, 1 V an Tor 2: $\underline I_1$ = −1 mA, $\underline I_2$ = (1 + j) mA; $\underline Y_{12}$ = −1 mS, $\underline Y_{22}$ = (1 + j) mS.
- (c) Ausgang offen, Stromquelle 1 mA in Tor 1: $\underline U_1$ = (1 − j) V, $\underline U_2$ = −j V; $\underline Z_{11}$ = (1 − j) kΩ, $\underline Z_{21}$ = −j kΩ.
- (d) Eingang offen, 1 mA in Tor 2: beide Spannungen −j V; $\underline Z_{12}$ = $\underline Z_{22}$ = −j kΩ.
- Unter (a) und (c) klein: „Kettenparameter aus (c) und (a): $\underline A_{11}$ = 1 + j, $\underline A_{21}$ = j·1 mS, $\underline A_{12}$ = 1 kΩ, $\underline A_{22}$ = 1“.

*Kernaussage:* Admittanzparameter misst man mit kurzgeschlossenem, Impedanzparameter mit offenem Gegentor.

*Daten:* Zahlenwerk AH.

*Editor:*
- §1, §2; §34 Kurzschluss und Leerlauf als Zustände eines Tors, Testquellen farbig;
- §35 Zweitor-Messvorlagen; §10 Teilbilder.

*Animation:* Die vier Versuche nacheinander; die Matrixeinträge füllen sich Spalte für Spalte.

**st1/netzwerkanalyse/05-ersatzschaltbild-y**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Oben das Ersatzschaltbild der Admittanzform: Querzweig $\underline Y_\text{quer1}$ von Klemme 1 zur unteren Leitung, Längszweig $\underline Y_\text{längs}$ von Klemme 1 nach 2, Querzweig $\underline Y_\text{quer2}$ von Klemme 2 zur unteren Leitung, spannungsgesteuerte Stromquelle $\underline Y_\mathrm g\,\underline U_1$ (Raute) von Klemme 2 zur unteren Leitung; gestrichelte Zuordnung zum Spannungspfeil $\underline U_1$; daneben die vier Zuordnungen $\underline Y_\text{quer1} = \underline Y_{11} + \underline Y_{12}$, $\underline Y_\text{längs} = -\underline Y_{12}$, $\underline Y_\text{quer2} = \underline Y_{22} + \underline Y_{12}$, $\underline Y_\mathrm g = \underline Y_{21} - \underline Y_{12}$. Unten drei kleine Fälle mit Werten: RC-Glied (0; 1 mS; j·1 mS; keine Quelle), Verstärkerstufe mit $R_S$ (0; 0; 0,112 mS; Quelle 0,494 mS), Stufe ohne $R_S$ bei ω = 10⁸ 1/s (j·10 µS = $j\omega C_{gs}$; j·2 µS = $j\omega C_{gd}$; 125 µS; Quelle 1 mS).

*Kernaussage:* Jede Admittanzmatrix ist ein π aus drei Admittanzen mit einer gesteuerten Quelle; bei einem umkehrbaren Zweitor entfällt die Quelle.

*Daten:* Zahlenwerk AH, AJ, AK.

*Editor:*
- §1, §28 gesteuerte Quellen; §2;
- §10 Teilbilder.

*Animation:* keine.

**st1/netzwerkanalyse/05-rueckwirkung-cgd**
- Fassung: kompakt Abb. 3, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand als Zweitor mit Tor 1 zwischen Gate und Masse und Tor 2 zwischen Drain und Masse, bei ω = 10⁸ 1/s: $C_{gs}$ = 100 fF vom Gate nach Masse, $C_{gd}$ = 20 fF vom Gate zum Drain (orange hervorgehoben als Rückwirkungspfad), Raute $g_m\underline U_1$ mit $g_m$ = 1 mS vom Drain nach Masse, $G_D + g_o$ = 125 µS am Drain; außerhalb die Last $R_L$ (verstellbar). Daneben die Admittanzmatrix j·12, −j·2, 1000 − j·2 und 125 + j·2 µS.
- (b) $C_\mathrm{ein}$ in fF (100 bis 300) über $R_L$ in kΩ (0,1 bis 1000, logarithmisch): 121,98 fF bei 0,1 kΩ, 137,78 fF bei 1 kΩ, 208,88 fF bei 10 kΩ, 268,11 fF bei 100 kΩ, 278,69 fF bei 1000 kΩ; waagrechte gestrichelte Grenzlinien 120 fF (Kurzschluss) und 279,95 fF (offen). Marker bei 10 kΩ mit „Verstärkung −4,44; $C_{gd}$ wirkt wie 109 fF“.

*Kernaussage:* Über die Gate-Drain-Kapazität sieht der Eingang die Last; die Eingangskapazität liegt zwischen 120 fF (Kurzschluss) und 280 fF (offen).

*Daten:* Zahlenwerk AK und AP (Eingangskapazität über dem Lastwiderstand).

*Editor:*
- §1, §28; §11 Datenkurven; §12 logarithmische Achse;
- §10 Teilbilder; §15 Schieberegler.

*Animation:* Schieberegler für $R_L$: Die Verstärkung und der Strom über $C_{gd}$ wachsen, der Punkt auf der Kurve wandert mit.

**st1/netzwerkanalyse/05-rc-kette**
- Fassung: kompakt Abb. 4, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Zwei RC-Glieder (je 1 kΩ längs, 100 nF quer) als Kette; über jedem Glied seine Kettenmatrix (1 + j; 1 kΩ; j·1 mS; 1), über beiden das Produkt (3j; (2 + j) kΩ; (−1 + 2j) mS; 1 + j). Am Verbindungsknoten der Strompfeil, der das erste Glied als $-\underline I_{2\mathrm a}$ verlässt und als $\underline I_{1\mathrm b}$ in das zweite fließt; ein Hinweispfeil „Last des ersten Glieds: (1 − j) kΩ“.
- (b) Betrag der Leerlauf-Spannungsübertragung über ω von 10² bis 10⁶ 1/s (logarithmische Achsen): Kette durchgezogen mit 0,9667 bei 10³, 0,3333 bei 10⁴ und 0,0097 bei 10⁵ 1/s; Produkt der Einzelübertragungen gestrichelt mit 0,9901, 0,5000 und 0,0099; senkrechte Hilfslinie bei der Eckkreisfrequenz 10⁴ 1/s mit Beschriftung „1/3 statt 1/2“.

*Kernaussage:* Das zweite Glied belastet das erste; die Kette überträgt nicht das Produkt der Einzelübertragungen, ihre Kettenmatrix ist aber das Produkt der Kettenmatrizen.

*Daten:* Zahlenwerk AI (Werte bei 10³, 10⁴, 10⁵ 1/s; Kurve aus $|1/\underline A_{11}|$ mit $x = \omega RC$: $|1/(1 - x^2 + 3jx)|$ gegen $1/(1 + x^2)$).

*Editor:*
- §1; §35 Kettenschaltung mit Matrizen; §32 Bode-Diagramm (nur Betrag, ohne Winkel);
- §11; §10 Teilbilder.

*Animation:* Ein Schalter „zweites Glied anhängen“: Die Übertragung des ersten Glieds sinkt sichtbar von 0,707 auf 0,471 (bei ω = 10⁴ 1/s).

**st1/netzwerkanalyse/05-laengs-quer**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Links ein Längsglied (Impedanz $\underline Z$ in der oberen Leitung, untere durchgehend) mit der Kettenmatrix (1; $\underline Z$; 0; 1) und ein Querglied (Admittanz $\underline Y$ zwischen den durchgehenden Leitungen) mit (1; 0; $\underline Y$; 1). Rechts zwei Anordnungen aus 1 kΩ und 100 nF bei ω = 10⁴ 1/s: das RC-Glied (Längs vor Quer) mit dem Produkt (1 + j; 1 kΩ; j·1 mS; 1) und offen 0,5 − 0,5j; das umgekehrte Glied (Quer vor Längs) mit (1; 1 kΩ; j·1 mS; 1 + j) und offen 1; mit 1 kΩ Last 0,4 − 0,2j gegen 0,5.

*Kernaussage:* Ein Kettenleiter ist das Produkt der Matrizen seiner Längs- und Querglieder in der Reihenfolge der Glieder.

*Daten:* Zahlenwerk AH.

*Editor:*
- §1; §35 Kettenschaltung mit Matrizen; §31 Matrixdarstellung;
- §10 Teilbilder.

*Animation:* Die beiden Glieder tauschen die Plätze, die Matrizen und das Produkt wechseln mit.

**st1/netzwerkanalyse/05-parallelschaltung**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Zwei Zweitore a und b mit durchgehender unterer Leitung, Eingänge parallel, Ausgänge parallel; gemeinsame Spannungen $\underline U_1$ und $\underline U_2$ hervorgehoben, Ströme $\underline I_{1\mathrm a}$ und $\underline I_{1\mathrm b}$ addieren sich zu $\underline I_1$, ebenso am Ausgang.
- (b) Die Stufe ohne Source-Widerstand bei ω = 10⁸ 1/s: oben das Transistor-Zweitor aus $C_{gs}$ (j·10 µS), Raute $g_m\underline U_1$ ($g_m$ = 1 mS) und $G_D + g_o$ (125 µS) mit der Matrix (j·10; 0; 1000; 125) µS; unten das Längsglied $C_{gd}$ mit (j·2; −j·2; −j·2; j·2) µS; rechts die Summe (j·12; −j·2; 1000 − j·2; 125 + j·2) µS.

*Kernaussage:* Ein Längsglied zwischen Eingang und Ausgang ist parallel geschaltet und erzeugt die Rückwirkung.

*Daten:* Zahlenwerk AK.

*Editor:*
- §1, §28; §35 Parallelschaltung mit Matrixsumme;
- §10 Teilbilder.

*Animation:* keine.

**st1/netzwerkanalyse/05-reihenschaltung-t**
- Fassung: kompakt Abb. 5, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Drei Teilbilder mit zwei T-Gliedern aus je drei Widerständen von 1 kΩ, Eingänge in Reihe, Ausgänge in Reihe.
- (a) Beide Glieder mit durchgehender unterer Leitung: Die untere Leitung des oberen Glieds verbindet die oberen Klemmen des unteren. Mit 1 mA in Tor 1 und offenem Tor 2 Strompfeile mit Werten: je 0,5 mA in die beiden oberen Klemmen des unteren Glieds, 1 mA aus seiner Klemme 1′ (rot markiert); Potentiale 3,5 V (Klemme 1), 2,5 V (Mitte oben), 1,5 V (untere Leitung oben), 1,0 V (Mitte unten); Matrix (3,5; 2,5; 2,5; 3,5) kΩ mit dem Vermerk „≠ Summe (4; 2; 2; 4) kΩ“.
- (b) Das untere Glied umgedreht, seine durchgehende Leitung oben an der unteren Leitung des oberen: Matrix (4; 2; 2; 4) kΩ, gleich der Summe.
- (c) Brune-Test: Eingänge in Reihe mit 1 mA gespeist, Ausgänge offen und unverbunden; Spannungsmesser zwischen den zu verbindenden Ausgangsklemmen: in Anordnung (a) 1 V (Potentiale 2 V und 1 V), in (b) 0 V.

*Kernaussage:* Ob man Impedanzmatrizen addieren darf, entscheidet die Torbedingung jedes Teils, und die hängt von der Anordnung ab.

*Daten:* Zahlenwerk AL.

*Editor:*
- §1, §2; §35 Reihenschaltung, Umdrehen eines Zweitors, Klemmenstrompfeile mit Werten, Markierung der verletzten Torbedingung;
- §34 Markierung „falsch“; §10 Teilbilder.

*Animation:* Umschalten zwischen (a) und (b): Das untere Glied klappt um, die Strompfeile und die Matrix ändern sich.

**st1/netzwerkanalyse/05-bipolar-re**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Kleinsignal-Ersatzschaltbild der Bipolarstufe ohne Emitterkondensator als Reihenschaltung: oben das Transistor-Zweitor mit $r_{BE}$ = 13,71 kΩ zwischen Basis und Emitter, stromgesteuerter Stromquelle $\beta\,\underline I_1$ (β = 502,4) vom Kollektor zum Emitter und $r_{CE}$ = 79,57 kΩ; der Emitter als gemeinsame Leitung; darunter das Querglied $R_E$ = 1 kΩ, dessen durchgehende obere Leitung am Emitter liegt; am Kollektor die Last $R_C$ = 3,9 kΩ gegen Masse. Der Basisspannungsteiler ist weggelassen (Vermerk).
- (b) Die Impedanzmatrizen in kΩ, auf vier Stellen gerundet: Transistor (13,71; 0; −39 970; 79,57) + Querglied (1; 1; 1; 1) = (14,71; 1; −39 970; 80,57); darunter Eingangsimpedanz mit Last 487,9 kΩ (ohne $R_E$ 13,71 kΩ) und Spannungsverstärkung −3,782.

*Kernaussage:* Der Emitterwiderstand liegt in Reihe mit dem Transistor-Zweitor, addiert sich zu allen vier Einträgen und hebt den Eingangswiderstand von 13,7 kΩ auf 488 kΩ.

*Daten:* Zahlenwerk AM (Kleinsignalwerte aus `notizen/get1/zahlen_transistor.py`).

*Editor:*
- §1, §28 stromgesteuerte Quelle; §35 Reihenschaltung mit Matrixsumme;
- §10 Teilbilder.

*Animation:* keine.

**st1/netzwerkanalyse/05-signalkette**
- Fassung: kompakt Abb. 6, ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- Oben ein Blockbild: Sensor oder Antenne als Quelle mit Innenwiderstand, dann Verstärker, Filter, Leitung und ein A/D-Umsetzer als Last; jeder Block als Zweitor-Kasten.
- Unten zwei Verstärkerstufen als rückwirkungsfreie Zweitore zwischen einer Signalquelle (1 mV, $R_\mathrm{sig}$ = 10 kΩ) und einer Last $R_L$ = 10 kΩ: jede Stufe mit $R_G$ = 100 kΩ am Eingang, Raute 0,494 mS mal Eingangsspannung und $R_\mathrm{aus}$ = 8,90 kΩ am Ausgang; an jeder Schnittstelle ein farbig hervorgehobener Teiler mit seinem Faktor (0,909 am Eingang, 0,918 zwischen den Stufen, 0,529 am Ausgang); Pegelanzeigen 1 mV, 0,909 mV am ersten Gate, −3,67 mV am zweiten, 8,53 mV an der Last.

*Kernaussage:* An jeder Schnittstelle einer Kette geht Signal in einem Teiler verloren; ohne Rückwirkung ist die Gesamtverstärkung das Produkt der belasteten Stufenverstärkungen.

*Daten:* Zahlenwerk AO.

*Editor:*
- §19 Blockbilder; §1, §28; §35 Kettenschaltung;
- §10 Teilbilder.

*Animation:* Schieberegler für $R_G$ und $R_L$: Die Teilerfaktoren und die Pegel ändern sich mit.

## ST1 MOS-Feldeffekttransistoren: Aufbau und Funktionsweise des MOSFET
Zahlenwerk: `notizen/st1/zahlen_mosfet.py` (Ausgabe `.txt`), Abschnitte A bis I. Beispiel-Transistorpaar des Kapitels: Gateoxid 5 nm ($C'_\mathrm{ox}$ = 6,91 fF/µm²); NMOS mit $W$ = 10 µm, $L$ = 1 µm, $K_n$ = 2 mA/V², $U_{th0}$ = 0,50 V, Gate aus n⁺-Polysilizium, Kanaldotierung $N_A$ = 5,7·10¹⁷ cm⁻³; PMOS in n-Wanne mit $W$ = 40 µm, $L$ = 1 µm, $K_p$ = 2 mA/V², $U_{th0}$ = −0,50 V, Gate aus p⁺-Polysilizium. Kennwerte: $\Phi_F$ = 0,462 V, $U_\mathrm{FB}$ = −1,027 V, $x_{d,\max}$ = 45,8 nm. Farben nach ERKLAER_PROMPT §7.4: Elektronen blau, Löcher rot, Verarmungszonen grau, Feldpfeile grün; n-Gebiete blau, p-Gebiete rot (n⁺/p⁺ kräftiger), Oxid hellgrau, Polysilizium dunkelrot schraffiert, Metall dunkelgrau.

**st1/mos-feldeffekttransistoren/01-querschnitt**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Querschnitt des NMOS, schematisch (Oxid stark vergrößert): p-Substrat, unter dem Gate Kanaldotierung $N_A$ = 5,7·10¹⁷ cm⁻³; links und rechts je ein n⁺-Gebiet (10²⁰ cm⁻³), links Source, rechts Drain, Abstand $L$ = 1 µm; Gateoxid mit Maßpfeil $t_\mathrm{ox}$ = 5 nm; darüber das Gate aus n⁺-Polysilizium; ganz links ein p⁺-Bulkkontakt; Anschlüsse B, S, G, D mit Metallkontakten. Eingeschalteter Zustand mit $U_{GS}$ = 1 V, $U_{DS}$ = 0,1 V, Source und Bulk an Masse: dünne Elektronenschicht (blau) unter dem Oxid von Source bis Drain, darunter die graue Verarmungszone (rund 48 nm) mit festen Akzeptorionen (−). Pfeil „Elektronen“ von Source nach Drain, Zählpfeil $I_D$ in den Drainanschluss hinein.
- (b) Draufsicht (Layout): aktives n-Gebiet (grün) als Rechteck, Polysilizium-Streifen (rot) quer darüber; der Kreuzungsbereich ist der Transistor mit Maßpfeil $W$ = 10 µm quer und $L$ = 1 µm in Stromrichtung; Kontaktlöcher (kleine Quadrate) auf Source, Drain und Gate-Ende; p⁺-Bulkkontakt (gelb) daneben. Gestrichelte Linie A–A′ zeigt die Schnittebene von (a).

*Kernaussage:* Das Gate liegt isoliert über dem Bereich zwischen Source und Drain und steuert ihn nur über sein Feld; der Transistor entsteht dort, wo sich Polysilizium und aktives Gebiet kreuzen.

*Daten:* Zahlenwerk A und B (Abmessungen, Dotierung, Verarmungsweite); sonst schematisch.

*Editor:*
- §27 Technologie-Querschnitte mit Maßpfeilen; §36 Ladungsschichten, Layout-Draufsicht;
- §2 Pfeile; §10 Teilbilder.

*Animation:* Schieberegler $U_{GS}$ von 0 bis 1,5 V: unter 0,5 V nur die Verarmungszone, darüber wächst die Elektronenschicht; Umschalten Querschnitt/Draufsicht mit gemeinsamer Markierung des Kanalbereichs.

**st1/mos-feldeffekttransistoren/01-cmos-wanne**
- Fassung: ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Querschnitt eines CMOS-Prozesses. Links der NMOS im p-Substrat (n⁺-Source und -Drain, Gate aus n⁺-Polysilizium, p⁺-Bulkkontakt an Masse), rechts der PMOS in einer n-Wanne (p⁺-Source und -Drain, Gate aus p⁺-Polysilizium, n⁺-Wannenkontakt an $U_B$ = 2,5 V). In den Querschnitt eingezeichnet die pn-Übergänge als Diodensymbole: n⁺-Source und n⁺-Drain gegen das p-Substrat (Anode im Substrat), p⁺-Source und p⁺-Drain gegen die n-Wanne (Kathode in der Wanne), Wanne gegen Substrat. Beschriftung: alle Dioden gesperrt oder ohne Spannung, solange alle Knoten zwischen 0 und $U_B$ liegen.

*Kernaussage:* Weil das Substrat an der niedrigsten und die Wanne an der höchsten Spannung liegt, bleibt jeder pn-Übergang gesperrt, und die Transistoren sind voneinander isoliert.

*Daten:* schematisch.

*Editor:*
- §27; §36 pn-Dioden im Querschnitt;
- §1 Diodensymbol; §2.

*Animation:* Bulk testweise auf +1 V: Die Dioden von Source und Drain des NMOS leuchten als leitend auf, ein Strompfeil ins Substrat erscheint.

**st1/mos-feldeffekttransistoren/01-schaltzeichen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Tabelle mit zwei Zeilen (NMOS oben, PMOS unten) und drei Spalten:
- (a) bipolarähnlich: Pfeil an der Source wie am Emitter, beim NMOS nach außen, beim PMOS nach innen;
- (b) Digitaltechnik: ohne Pfeil, beim PMOS ein Kreis am Gate;
- (c) DIN: senkrechte Kanallinie aus drei Stücken (unterbrochen = selbstsperrend), eigener Bulkanschluss B mit Pfeil, beim NMOS zum Kanal hin (p-Bulk, n-Kanal), beim PMOS vom Kanal weg.
In jedem Symbol die Zählpfeile: $U_{GS}$ von G nach S, $U_{DS}$ von D nach S, $I_D$ in den Drain hinein; NMOS mit Drain oben, PMOS mit Source oben. Rechts daneben klein ein selbstleitender NMOS in DIN-Form (durchgezogene Kanallinie).

*Kernaussage:* Alle Schreibweisen bezeichnen dasselbe Bauteil; Spannungen zählen vom ersten zum zweiten Index, Ströme in den Anschluss hinein, und beim PMOS steht die Source oben, weil sie das höhere Potential hat.

*Daten:* schematisch.

*Editor:*
- §24 MOSFET-Symbole; §36 Symbolvarianten;
- §2 Zählpfeile; §10 Tabelle aus Teilbildern.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/01-mos-zustaende**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Vier Querschnitte des MOS-Kondensators nebeneinander (Gate n⁺-Polysilizium, Oxid 5 nm, p-Silizium mit 5,7·10¹⁷ cm⁻³, Bulk an Masse), darunter jeweils $U_{GB}$, Oberflächenpotential $\psi_s$ und die Flächenladung im Silizium:
- (a) Anreicherung, $U_{GB}$ = −2 V: Gate negativ geladen, dichte Löcherschicht (rot) an der Oberfläche, 5,94 fC/µm², $\psi_s$ = −0,11 V;
- (b) Flachband, $U_{GB}$ = $U_\mathrm{FB}$ = −1,03 V: keine Ladung, $\psi_s$ = 0;
- (c) Verarmung, $U_{GB}$ = 0: Gate positiv, Löcher in die Tiefe verdrängt, graue Zone mit festen Akzeptorionen (−), 35 nm tief, 3,19 fC/µm², $\psi_s$ = 0,57 V;
- (d) Inversion, $U_{GB}$ = 1 V: Gate stärker positiv, dünne Elektronenschicht (blau) direkt unter dem Oxid (2,55 fC/µm²), darunter die Zone mit Ionen, 48 nm, 4,35 fC/µm²; $\psi_s$ = 1,03 V.
Feldpfeile (grün) im Oxid vom Gate zur Gegenladung bzw. umgekehrt.

*Kernaussage:* Zur Ladung des Gates gehört immer eine gleich große Gegenladung im Silizium; mit wachsender Spannung besteht sie erst aus Löchern, dann aus festen Akzeptorionen, und oberhalb der Schwelle kommen bewegliche Elektronen hinzu; schon bei 0 V ist die Oberfläche verarmt.

*Daten:* Zahlenwerk C (psi_von_UGB, Qs_exakt, Qinv_exakt; Verarmungsweite aus der Ladung; Poisson-Gleichung mit Boltzmann-Verteilung, Fermi-Dirac-Gegenrechnung in Abschnitt K); schematische Teilchendarstellung.

*Editor:*
- §27; §36 Ladungsschichten aus Daten; §14 Teilchen;
- §2 Feldpfeile; §10 Teilbilder.

*Animation:* Schieberegler $U_{GB}$ von −2,5 bis 2,5 V: Schichten und Zone folgen dem Zahlenwerk, $\psi_s$ läuft als Zahl mit.

**st1/mos-feldeffekttransistoren/01-oberflaechenpotential**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Drei gestapelte Diagramme über $U_{GB}$ von −2 bis 1,5 V (Poisson-Gleichung mit Boltzmann-Verteilung gelöst), senkrechte Marken bei $U_\mathrm{FB}$ = −1,03 V und $U_{th0}$ = 0,50 V:
- (a) Oberflächenpotential $\psi_s$ in V: −0,11 V bei −2 V, 0 bei −1,03 V, 0,57 V bei 0, 0,92 V bei 0,50 V, danach fast waagerecht: 1,03 V bei 1 V, 1,06 V bei 1,5 V; gestrichelte Waagerechten bei $\Phi_F$ = 0,46 V und $2\Phi_F$ = 0,92 V.
- (b) Elektronendichte $n_s$ (blau) und Löcherdichte $p_s$ (rot) an der Oberfläche, logarithmisch 10⁰ bis 10²⁰ cm⁻³: $n_s$ = 176 cm⁻³ im Flachband, Kreuzung mit $p_s$ bei 10¹⁰ cm⁻³ (−0,15 V), 5,6·10¹¹ cm⁻³ bei 0, 5,7·10¹⁷ cm⁻³ = $N_A$ bei 0,50 V (Waagerechte $N_A$), 3,3·10¹⁹ cm⁻³ bei 1 V (mit Fermi-Dirac 2,8·10¹⁹ cm⁻³, Zahlenwerk K); Bereich über 10¹⁹ cm⁻³ schraffiert („Boltzmann-Näherung ungenau“).
- (c) Beträge der Flächenladungen in fC/µm²: Löcher (rot) links des Flachbands, Verarmungsladung (grau) bis 4,11 bei 0,50 V, danach fast konstant (4,35 bei 1 V, 4,41 bei 1,5 V); Elektronen (blau) ab 0,50 V fast linear (2,55 bei 1 V, 5,75 bei 1,5 V); gestrichelt das Ladungsmodell $C'_\mathrm{ox}(U_{GB}-U_{th0})$ (3,45 bei 1 V, 6,91 bei 1,5 V).

*Kernaussage:* Bis zur Schwelle wächst das Oberflächenpotential mit der Gatespannung; danach steigt die Elektronendichte so steil, dass das Potential fast stehen bleibt und jede weitere Gateladung als Elektronenschicht erscheint.

*Daten:* Zahlenwerk C (psi_von_UGB, Qs_exakt, Qinv_exakt).

*Editor:*
- §13 gestapelte Diagramme; §11 Datenkurven; §12 halblogarithmisch;
- §15 Schieberegler.

*Animation:* senkrechter Cursor bei $U_{GB}$, gekoppelt an die Zustandsquerschnitte (01-mos-zustaende).

**st1/mos-feldeffekttransistoren/01-baender**
- Fassung: ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Drei Banddiagramme über der Tiefe $x$ von 0 bis 100 nm unter dem Oxid (Oxid und Gate links als Kästen): $W_L$, $W_V$, $W_i$ (gepunktet), $W_F$ (gestrichelt, waagerecht, Bezug ist das Substrat):
- (a) Verarmung, $U_{GB}$ = 0: Bänder an der Oberfläche um 0,57 eV nach unten gebogen, Biegung reicht 35 nm tief; $W_i$ an der Oberfläche 0,10 eV unter $W_F$;
- (b) Schwelle, $U_{GB}$ = 0,50 V: Biegung 0,92 eV über 45 nm; Maßpfeile: im Substrat liegt $W_i$ um 0,46 eV über $W_F$, an der Oberfläche um 0,46 eV darunter;
- (c) starke Inversion, $U_{GB}$ = 1 V: Biegung 1,03 eV, Leitungsbandkante an der Oberfläche nahe $W_F$, Elektronen (blau) als dünne Schicht im Knick.

*Kernaussage:* Inversion heißt im Banddiagramm: Das Eigenleitungsniveau taucht an der Oberfläche unter das Fermi-Niveau; die Schwelle ist erreicht, wenn es dort so weit darunter liegt wie im Substrat darüber.

*Daten:* Zahlenwerk B und C ($\psi_s$, $\Phi_F$, Verarmungsweiten); Bandverlauf in Verarmungsnäherung parabolisch.

*Editor:*
- §16 Bänderschema über dem Ort; §11;
- §10 Teilbilder.

*Animation:* Schieberegler $U_{GB}$; die Biegung wächst bis zur Schwelle und danach kaum noch.

**st1/mos-feldeffekttransistoren/01-schwellenspannung**
- Fassung: kompakt Abb. 5, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Spannungsbilanz als Treppendiagramm: Start bei 0 V; Balken Flachbandspannung $U_\mathrm{FB} = \Phi_\mathrm{MS}$ = −1,027 V nach unten (hebt die Kontaktspannung von 1,027 V auf); Balken $2\Phi_F$ = +0,923 V nach oben („Oberflächenpotential bis zur starken Inversion“); Balken $|Q'_\mathrm{dep}|/C'_\mathrm{ox}$ = +0,604 V nach oben („Spannung über dem Oxid“); Ergebnisbalken $U_{th0}$ = 0,500 V.
- (b) $U_{th0}$ über der Kanaldotierung $N_A$, logarithmisch 10¹⁶ bis 10¹⁸ cm⁻³: −0,14 V bei 10¹⁶, −0,025 V bei 4·10¹⁶, 0,09 V bei 10¹⁷, 0,31 V bei 3·10¹⁷, 0,50 V bei 5,7·10¹⁷ (Punkt markiert), 0,72 V bei 10¹⁸; Bereich unter der Nulllinie hinterlegt („selbstleitend“); dünn zwei weitere Kurven für $t_\mathrm{ox}$ = 4,5 und 5,5 nm (beim Beispielwert 0,44 bzw. 0,56 V).

*Kernaussage:* Die Schwellenspannung ist eine Spannungsbilanz aus Flachbandspannung, Oberflächenpotential und Oxidspannung; über die Kanaldotierung lässt sie sich um mehr als 0,8 V verschieben.

*Daten:* Zahlenwerk B (Funktion Uth0_n, auch mit anderem $C'_\mathrm{ox}$).

*Editor:*
- §36 Spannungsbilanz als Treppendiagramm; §11; §12 logarithmische x-Achse;
- §10 Teilbilder; §15 Schieberegler.

*Animation:* Schieberegler $N_A$ und $t_\mathrm{ox}$: Balken und Kurvenpunkt bewegen sich gemeinsam.

**st1/mos-feldeffekttransistoren/01-cv-kurve**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* $C/C'_\mathrm{ox}$ über $U_{GB}$ von −2,5 bis 2,5 V, niederfrequent (durchgezogen) und hochfrequent (gestrichelt): 0,96 bei −2,5 V, 0,73 im Flachband (−1,03 V), 0,30 bei 0; niederfrequent Minimum 0,26 bei 0,35 V (schwache Inversion), danach 0,40 bei 0,5 V, 0,92 bei 1 V, 0,98 bei 2,5 V; hochfrequent weiter sinkend, 0,25 an der Schwelle, 0,23 bei 2,5 V. Waagerechte Hilfslinien bei 1 ($C'_\mathrm{ox}$ = 6,91 fF/µm²) und 0,247 (Reihenschaltung mit der Verarmungszone an der Schwelle nach der Verarmungsnäherung, 2,26 fF/µm²). Senkrechte Marken bei $U_\mathrm{FB}$ und $U_{th0}$. Über der Kurve kleine Ersatzschaltbilder: Anreicherung $C_\mathrm{ox}$; Verarmung $C_\mathrm{ox}$ in Reihe mit $C_\mathrm{dep}$; Inversion niederfrequent $C_\mathrm{ox}$; Inversion hochfrequent $C_\mathrm{ox}$ in Reihe mit $C_\mathrm{dep}$ der kaum noch wachsenden Zone.

*Kernaussage:* In der Verarmung liegt die Kapazität der Zone in Reihe mit dem Oxid; in der Inversion kehrt die Kapazität nur dann auf $C'_\mathrm{ox}$ zurück, wenn die Elektronen der Messspannung folgen können.

*Daten:* Zahlenwerk D (C_NF, C_HF).

*Editor:*
- §4, §11 Kennlinien aus Daten;
- §1 kleine Kondensator-Schaltbilder; §10.

*Animation:* Umschalten niederfrequent/hochfrequent; ein Cursor zeigt das Ersatzschaltbild des jeweiligen Zustands.

**st1/mos-feldeffekttransistoren/01-betriebsbereiche**
- Fassung: kompakt Abb. 6, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Zwei Zeilen.
- Oben drei Querschnitte des Beispieltransistors, Source und Bulk an Masse: (a) Sperrbereich, $U_{GS}$ = 0,3 V, $U_{DS}$ = 1 V: kein Kanal, graue Verarmungszonen um Source, Drain (breiter, gesperrt) und unter dem Gate; (b) ohmscher Bereich, $U_{GS}$ = 1 V, $U_{DS}$ = 0,3 V: durchgehender Kanal, zum Drain hin keilförmig auf 40 % verdünnt; (c) Abschnürung, $U_{GS}$ = 1 V, $U_{DS}$ = 2 V: Kanal endet vor dem Drain am Abschnürpunkt, dahinter eine kurze graue Zone (58 nm), Elektronenpfeile durch die Zone.
- Unten die relative Kanalladung $Q'_n(x)/Q'_n(0)$ über $x/L$ von 0 bis 1 bei $U_{GS}$ = 1 V für $U_{DS}$ = 0,1 V (am Drain 0,80), 0,3 V (0,40) und 0,5 V (0, Abschnürung); Werte bei $x/L$ = 0; 0,2; 0,4; 0,6; 0,8; 1: 1; 0,96; 0,93; 0,89; 0,84; 0,80 bzw. 1; 0,91; 0,81; 0,70; 0,57; 0,40 bzw. 1; 0,89; 0,77; 0,63; 0,45; 0.

*Kernaussage:* Die Drainspannung hebt das Kanalpotential zum Drain hin an und verdünnt dort den Kanal; bei $U_{DS} = U_{GS}-U_{th}$ verschwindet er am Drain-Ende, und der Rest der Spannung fällt über einer kurzen Zone ab.

*Daten:* Zahlenwerk F (kanal_profil) und H (Länge der abgeschnürten Zone).

*Editor:*
- §27; §36 Kanal mit veränderlicher Dicke und Abschnürpunkt;
- §11; §10.

*Animation:* Schieberegler $U_{DS}$ von 0 bis 2 V bei $U_{GS}$ = 1 V: Der Keil wird spitzer, ab 0,5 V löst sich das Kanalende vom Drain, und die Zone wächst.

**st1/mos-feldeffekttransistoren/01-kanalwiderstand**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) $I_D$ über $U_{DS}$ von 0 bis 20 mV als nahezu gerade Linien durch den Ursprung für $U_{GS}$ = 0,75 / 1 / 1,5 / 2,5 V mit den Steigungen 0,5 / 1 / 2 / 4 mS (bei 20 mV: 10 / 20 / 40 / 80 µA; bei 0,75 V weicht der Strom am Bereichsende um höchstens 4 % von der Geraden ab); für $U_{GS}$ ≤ 0,5 V die Nulllinie.
- (b) $R_\mathrm{on}$ über $U_{GS}$ von 0,6 bis 2,5 V: Hyperbel $1/(K_n(U_{GS}-0{,}5\ \mathrm V))$ mit den Punkten 2000 Ω (0,75 V), 1000 Ω (1 V), 500 Ω (1,5 V), 250 Ω (2,5 V).

*Kernaussage:* Für kleine Drain-Source-Spannungen ist der Kanal ein Widerstand, dessen Leitwert proportional zur Gate-Übersteuerung wächst.

*Daten:* Zahlenwerk F.

*Editor:*
- §4, §11;
- §10.

*Animation:* Schieberegler $U_{GS}$: Die Gerade dreht sich um den Ursprung, der Punkt in (b) läuft mit.

**st1/mos-feldeffekttransistoren/01-abschnuerung**
- Fassung: ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Zwei Teilbilder für $U_{GS}$ = 1 V und $U_{DS}$ = 2 V.
- (a) Vergrößerter Querschnitt am Drain-Ende: Die Elektronenschicht (blau) wird zum Abschnürpunkt hin dünn und endet 58 nm vor dem Drain; dazwischen die graue Zone mit Feldpfeilen (grün) vom Drain zum Abschnürpunkt; Elektronen als Punkte, die die Zone zum Drain hin durchqueren.
- (b) Potential $U(x)$ längs des Weges von der Source (0 V) zum Drain (2 V): im Kanal von 0 auf 0,5 V am Abschnürpunkt, dann auf 58 nm steil auf 2 V; gestrichelt zum Vergleich der Verlauf an der Abschnürgrenze $U_{DS}$ = 0,5 V.

*Kernaussage:* Was über $U_{GS}-U_{th}$ hinausgeht, fällt über der kurzen abgeschnürten Zone ab; der Kanal selbst sieht weiter nur 0,5 V, und das starke Feld der Zone zieht jedes ankommende Elektron zum Drain.

*Daten:* Zahlenwerk F (kanal_profil) und H (Delta L = 58,4 nm, mittleres Feld 2,6·10⁵ V/cm).

*Editor:*
- §27; §36 Kanal mit Abschnürpunkt; §2 Feldpfeile;
- §11; §22 Ausschnittvergrößerung; §10.

*Animation:* Schieberegler $U_{DS}$ von 0,5 bis 2,5 V: Die Zone wächst von 0 auf 68 nm, das Potential am Abschnürpunkt bleibt bei 0,5 V.

## ST1 MOS-Feldeffekttransistoren: Kennlinien des NMOS-Transistors
Zahlenwerk: `notizen/st1/zahlen_mosfet.py` (Ausgabe `.txt`), Abschnitte L bis Q; Beispiel-NMOS aus Thema 1 ($K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, $W$ = 10 µm, $L$ = 1 µm, λ = 0,1 1/V). Kennlinien mit dem Modell der Abschnitte L und N (Funktion id_l1); Bereiche: Sperrbereich grau, ohmscher Bereich hellblau, Abschnürbereich hellorange; Grenzparabel gestrichelt; Elektronen blau.

**st1/mos-feldeffekttransistoren/02-kennlinienfeld**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Ausgangskennlinienfeld ohne Kanallängenmodulation: $I_D$ in mA über $U_{DS}$ von 0 bis 2,5 V für $U_{GS}$ = 0,75 / 1 / 1,25 / 1,5 V; Sättigungsströme 0,0625 / 0,25 / 0,5625 / 1 mA, erreicht bei 0,25 / 0,5 / 0,75 / 1 V; die Grenzparabel $I_D = K_n U_{DS}^2/2$ gestrichelt durch die Übergangspunkte, an denen die Kurven waagerecht werden; links davon der ohmsche Bereich (hellblau), rechts der Abschnürbereich (hellorange); Beschriftung jeder Kurve mit $U_{GS}$.
- (b) Übertragungskennlinie im Abschnürbereich: $I_D$ über $U_{GS}$ von 0 bis 1,5 V, null bis 0,5 V, dann die Parabel bis 1 mA; markiert 0,25 mA bei 1 V.

*Kernaussage:* Jede Kennlinie steigt im ohmschen Bereich bis zur Grenzparabel an und bleibt dann waagerecht; der Sättigungsstrom wächst quadratisch mit der Gate-Übersteuerung.

*Daten:* Zahlenwerk L (id_l1, Grenzkurve).

*Editor:*
- §4 Kennlinienscharen, Bereiche hinterlegen; §11 Datenkurven; §37 Grenzkurve durch die Knickpunkte, Bereiche entlang einer Kurve;
- §10 Teilbilder; §15 Schieberegler; §37 gekoppelte Punkte in zwei Diagrammen.

*Animation:* Schieberegler $U_{GS}$: eine hervorgehobene Kennlinie wandert, ihr Übergangspunkt läuft auf der Grenzparabel, der Punkt in (b) läuft mit.

**st1/mos-feldeffekttransistoren/02-kanal-geschwindigkeit**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei gestapelte Diagramme über $x/L$ von 0 bis 1 für $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V ($I_D$ = 0,21 mA): (a) Kanalpotential $U(x)$ in mV: 0 / 56 / 119 / 196 / 300 bei $x/L$ = 0 / 0,25 / 0,5 / 0,75 / 1, nach rechts immer steiler; (b) Elektronenladung in Prozent des Werts an der Source: 100 / 89 / 76 / 61 / 40; (c) mittlere Geschwindigkeit der Elektronen in 10⁵ cm/s: 6,1 / 6,8 / 8,0 / 10,0 / 15,2. Darüber als Band der Kanal, dessen Dicke der Ladung folgt, mit Elektronen als Punkte, die nach rechts dichter laufen. Beschriftung „Strom überall 0,21 mA“.

*Kernaussage:* Wo der Kanal dünner ist, laufen die Elektronen schneller; das Produkt aus Ladung und Geschwindigkeit, der Strom, ist überall gleich.

*Daten:* Zahlenwerk M (Profil, Feld, Geschwindigkeit).

*Editor:*
- §13 gestapelte Diagramme; §11; §36 Kanalband mit veränderlicher Dicke;
- §14 Teilchen (bewegte Punkte).

*Animation:* Elektronen laufen als Punkte durch den Kanal, mit der berechneten Geschwindigkeit; Schieberegler $U_{DS}$ von 0 bis 0,5 V.

**st1/mos-feldeffekttransistoren/02-flaeche-uebersteuerung**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Drei Teilbilder nebeneinander, jeweils für $U_{GS}$ = 1 V: x-Achse Kanalpotential $U$ von 0 bis 0,8 V, y-Achse örtliche Übersteuerung $U_{GS} - U_{th} - U$ in V (proportional zur Elektronenladung pro Fläche, $|Q'_n|/C'_\mathrm{ox}$), eine fallende Gerade von 0,5 V bei $U$ = 0 auf null bei $U$ = 0,5 V, rechts davon gestrichelt und grau ins Negative fortgesetzt mit dem Vermerk „keine Elektronen“. (a) $U_{DS}$ = 0,3 V: Fläche von 0 bis 0,3 V hellblau, in drei Streifen von je 0,1 V mit den Höhen 0,45 / 0,35 / 0,25 V in der Streifenmitte; Fläche 0,105 V², $I_D = K_n \cdot$ Fläche = 0,21 mA. (b) $U_{DS}$ = 0,5 V: das volle Dreieck, 0,125 V², 0,25 mA. (c) $U_{DS}$ = 0,75 V: dasselbe Dreieck; zwischen 0,5 und 0,75 V keine Fläche, weil dort kein Kanal ist (Abschnürzone), Strom weiter 0,25 mA.

*Kernaussage:* Der Drainstrom ist $K_n$ mal der Fläche unter der Übersteuerung über dem Kanalpotential; diese Fläche wächst nur, bis die Übersteuerung am Drain-Ende null wird, und bleibt danach gleich.

*Daten:* Zahlenwerk Q (Fläche, Streifen) und L.

*Editor:*
- §4 Fläche unter einer Kurve schraffieren, Gerade mit gestrichelter Fortsetzung; §10 Teilbilder;
- §15 Schieberegler; §37 ungültige Fortsetzung.

*Animation:* Schieberegler $U_{DS}$ von 0 bis 1 V: Die Fläche wächst als Trapez, wird zum Dreieck und wächst dann nicht mehr; daneben ein Zeiger auf der Ausgangskennlinie, der mitläuft.

**st1/mos-feldeffekttransistoren/02-triode-parabel**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* $I_D$ in mA über $U_{DS}$ von 0 bis 1,2 V bei $U_{GS}$ = 1 V: die Triodenparabel durchgezogen bis zum Maximum 0,25 mA bei 0,5 V; ihre Fortsetzung gestrichelt und rot durchgestrichen bis 0 bei 1 V (0,1875 mA bei 0,75 V); der tatsächliche Verlauf ab 0,5 V waagerecht bei 0,25 mA (ohne Kanallängenmodulation); die Tangente im Ursprung mit 1 mS ($R_\mathrm{on}$ = 1 kΩ), die bei 0,1 V 0,1 mA statt 0,09 mA anzeigt. Senkrechte Marke „Abschnürgrenze 0,5 V“.

*Kernaussage:* Die Triodengleichung erreicht ihr Maximum genau an der Abschnürgrenze; dahinter gilt sie nicht mehr, und der Strom bleibt beim Maximum stehen.

*Daten:* Zahlenwerk L.

*Editor:*
- §4 Tangente, Markierungen; §11; §37 ungültige Fortsetzung gestrichelt und durchgestrichen.

*Animation:* Ein Punkt läuft mit wachsendem $U_{DS}$ die Kurve entlang; am Maximum verzweigt die gestrichelte Fortsetzung und wird ausgeblendet.

**st1/mos-feldeffekttransistoren/02-schwellenbestimmung**
- Fassung: ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Zwei gestapelte Diagramme über $U_{GS}$ von 0 bis 1,5 V im Abschnürbereich: (a) $I_D$ in mA, Parabel bis 1 mA, dazu gestrichelt die Tangente bei 1 V (Steigung 1 mS), die die Achse bei 0,75 V statt bei 0,5 V trifft; (b) $\sqrt{I_D}$ in $\sqrt{\mathrm{mA}}$: Gerade mit der Steigung $\sqrt{K_n/2}$ = 1 √(mA)/V, die die Achse bei 0,5 V schneidet.

*Kernaussage:* Die Wurzel des Sättigungsstroms ist eine Gerade, die die Spannungsachse genau bei der Schwellenspannung schneidet; eine Tangente an die Parabel selbst trifft sie nicht.

*Daten:* Zahlenwerk L.

*Editor:*
- §13; §4 Tangente; §11; §37 Wurzel-Achse.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/02-kanallaengenmodulation**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Ausgangskennlinien mit λ = 0,1 1/V für $U_{GS}$ = 0,75 / 1 / 1,25 / 1,5 V, $U_{DS}$ von 0 bis 2,5 V (bei 2,5 V: 0,078 / 0,3125 / 0,703 / 1,25 mA); die Geraden des Abschnürbereichs gestrichelt nach links verlängert bis zum gemeinsamen Schnittpunkt bei $U_{DS}$ = −10 V (Early-Spannung), mit gebrochener Achse zwischen −10 und 0 V; Steigungen 6,25 / 25 / 56,25 / 100 µA/V an den Kurven. Kleines Einsatzbild: Kanal mit Abschnürpunkt, Verkürzung Δ$L$ = 34 nm bei 1 V und 58 nm bei 2 V.

*Kernaussage:* Weil der Kanal mit wachsender Drainspannung kürzer wird, steigen die Kennlinien im Abschnürbereich leicht an; im Modell treffen sie sich verlängert bei −1/λ.

*Daten:* Zahlenwerk N.

*Editor:*
- §4 Geraden ins Kennlinienfeld; §17 Achsenbruch; §11; §36 Einsatzbild Kanal; §37 Extrapolation auf den gemeinsamen Schnittpunkt.

*Animation:* Schieberegler λ: Die Steigungen und der Schnittpunkt wandern.

**st1/mos-feldeffekttransistoren/02-arbeitspunkt**
- Fassung: kompakt Abb. 7, ausführlich Abb. 8 (jeweils im Beispiel zum Großsignalmodell).
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Schaltbild: Versorgungsspannung $U_B$ = 2,5 V, Widerstand $R_D$ = 4 kΩ von $U_B$ zum Drain, NMOS mit Source an Masse und Bulk an Masse, Gate an einer Spannungsquelle $U_{GS}$; Zählpfeile $I_D$ (in den Drain) und $U_{DS}$.
- (b) $I_D$ in mA (0 bis 0,7) über $U_{DS}$ in V (0 bis 2,5): Ausgangskennlinien mit λ = 0,1 1/V für $U_{GS}$ = 1 V und 1,5 V, die Arbeitsgerade $I_D = (2{,}5\ \mathrm V - U_{DS})/4\ \mathrm{k\Omega}$ von 0,625 mA bei 0 V nach null bei 2,5 V, gestrichelt die Grenzparabel $K_n U_{DS}^2/2 \cdot (1 + \lambda U_{DS})$; Arbeitspunkte A₁ (1,364 V; 0,284 mA) im Abschnürbereich und A₂ (0,314 V; 0,546 mA) im ohmschen Bereich, beschriftet.

*Kernaussage:* Der Arbeitspunkt liegt im Schnitt von Kennlinie und Arbeitsgerade; auf welcher Seite der Grenzparabel er liegt, entscheidet über den Bereich.

*Daten:* Zahlenwerk Q (Arbeitspunkt, Funktion ap) und L/N (id_l1).

*Editor:*
- §1 Schaltplan; §4 Arbeitsgerade und Schnittpunkte; §10 Teilbilder; §11; §37 Grenzkurve.

*Animation:* Schieberegler $U_{GS}$ von 0,5 bis 2 V: Der Arbeitspunkt wandert auf der Arbeitsgeraden und wechselt beim Überqueren der Grenzparabel den Bereich (Farbwechsel des Punkts).

**st1/mos-feldeffekttransistoren/02-unterschwelle**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* $I_D$ halblogarithmisch von 10⁻¹³ bis 10⁻² A über $U_{GS}$ von 0 bis 1,5 V bei $U_{DS}$ = 1 V: unterhalb der Schwelle eine Gerade (0,56 pA bei 0 V, 8,1 pA bei 0,1 V, 0,12 nA bei 0,2 V, 2,0 nA bei 0,3 V, 32 nA bei 0,4 V; Steigung 83 mV pro Dekade, Steigungsdreieck), oberhalb der Übergang in das Großsignalmodell mit Kanallängenmodulation (0,275 mA bei 1 V, 1,1 mA bei 1,5 V); gestrichelte Vergleichsgerade mit 59,5 mV pro Dekade; senkrechte Marke $U_{th}$ = 0,5 V.

*Kernaussage:* Unterhalb der Schwelle sinkt der Strom nicht auf null, sondern exponentiell um eine Zehnerpotenz je 83 mV.

*Daten:* Zahlenwerk O (Diffusionsstrom aus der vollständigen Rechnung), L und N (Großsignalmodell mit λ, Nachtrag R).

*Editor:*
- §12 halblogarithmisch; §11; §37 Steigungsdreieck in Dekaden.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/02-ersatzschaltbild**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Links das Schaltzeichen des NMOS mit $U_{GS}$, $U_{DS}$, $U_{BS}$ und $I_D$; rechts das Großsignal-Ersatzschaltbild: Gate offen (kein Strom), zwischen Drain und Source eine gesteuerte Stromquelle $I_D(U_{GS}, U_{DS})$, Bulk getrennt. Darunter die drei Bereichsformeln mit dem Faktor $(1 + \lambda U_{DS})$ als Tabelle.

*Kernaussage:* Für große Signale ist der MOSFET eine Stromquelle zwischen Drain und Source, deren Strom Gate-Source- und Drain-Source-Spannung festlegen, bei stromlosem Gate.

*Daten:* schematisch.

*Editor:*
- §1, §24 Schaltzeichen; §28 gesteuerte Quelle; §10.

*Animation:* keine.

## ST1 MOS-Feldeffekttransistoren: PMOS-Transistor, Substrateffekt und Latch-Up
Zahlenwerk: `notizen/st1/zahlen_mosfet.py` (Ausgabe `.txt`), Abschnitte S bis V; Beispiel-Transistorpaar aus Thema 1 (NMOS $K_n$ = 2 mA/V², $U_{th0}$ = 0,5 V, γ_n = 0,629 √V; PMOS $W$ = 40 µm, $K_p$ = 2 mA/V², $U_{th0,p}$ = −0,5 V, γ_p = 0,615 √V; λ = 0,1 1/V). Farben wie in Thema 1: p-Gebiete gelb, n-Gebiete grün, Verarmungszonen grau, Elektronen blau, Löcher rot; parasitäre Bauelemente violett gestrichelt.

**st1/mos-feldeffekttransistoren/03-cmos-ueberblick**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* CMOS-Querschnitt, schematisch: links ein NMOS im p-Substrat mit p⁺-Substratkontakt an Masse, rechts ein PMOS in der n-Wanne mit n⁺-Wannenkontakt an $U_B$ = 2,5 V. Alle pn-Übergänge als kleine Diodensymbole (n⁺ gegen Substrat, p⁺ gegen Wanne, Wanne gegen Substrat), gesperrt grau. Drei nummerierte Hervorhebungen: (1) PMOS als Spiegelbild: Löcherkanal, Spannungen negativ gegen die Source; (2) NMOS mit Source 1 V über dem Substrat: Verarmungszone unter dem Gate breiter (66 statt 46 nm); (3) gestrichelter Pfad p⁺ (PMOS-Source) → n-Wanne → p-Substrat → n⁺ (NMOS-Source) als pnpn-Schichtfolge.

*Kernaussage:* Die Transistoren einer CMOS-Schaltung sind nur durch gesperrte pn-Übergänge voneinander getrennt, und das Potential von Substrat und Wanne wirkt auf jeden Transistor mit.

*Daten:* Zahlenwerk T (Verarmungsweiten), schematisch sonst.

*Editor:*
- §27 Technologie-Querschnitte; §36 Ladungsschichten, pn-Übergänge als Dioden; §38 parasitärer Pfad;
- §10 nummerierte Hervorhebungen.

*Animation:* Die drei Hervorhebungen erscheinen nacheinander; bei (2) wächst die Verarmungszone mit einem Schieberegler für $U_{SB}$ von 0 bis 2,5 V.

**st1/mos-feldeffekttransistoren/03-pmos-kennlinien**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Schaltzeichen des PMOS mit Gate, Drain, Source und Bulk, Zählpfeile wie beim NMOS: $U_{GS}$ und $U_{DS}$ von Gate bzw. Drain zur Source, $U_{BS}$ vom Bulk zur Source, $I_D$ in den Drain hinein; daneben das Großsignal-Ersatzschaltbild mit gesteuerter Stromquelle zwischen Source und Drain und offenem Gate. Dazu klein die Betragsgrößen $U_{SG}$, $U_{SD}$ und $I_{SD}$ = −$I_D$ mit ihren Pfeilen.
- (b) Ausgangskennlinien mit Vorzeichen im dritten Quadranten: $I_D$ von 0 bis −1,3 mA über $U_{DS}$ von 0 bis −2,5 V für $U_{GS}$ = −0,75 / −1 / −1,25 / −1,5 V, mit λ = 0,1 1/V (bei −2,5 V: −0,078 / −0,3125 / −0,703 / −1,25 mA); gestrichelt die Grenze $U_{DS} = U_{GS} - U_{th,p}$ bei −0,25 / −0,5 / −0,75 / −1 V.
- (c) dieselben Kennlinien in Betragsdarstellung, $I_{SD}$ über $U_{SD}$ im ersten Quadranten, gleich den NMOS-Kennlinien.

*Kernaussage:* Der PMOS verhält sich wie ein NMOS mit umgekehrten Vorzeichen aller Spannungen und Ströme.

*Daten:* Zahlenwerk S (Funktion id_p).

*Editor:*
- §24 Schaltzeichen; §28 gesteuerte Quelle; §2 Zählpfeile; §4, §11 Kennlinienschar;
- §37 dritter Quadrant und gespiegelte Darstellung; §10 Teilbilder.

*Animation:* Umschalten zwischen (b) und (c) als Spiegelung an beiden Achsen.

**st1/mos-feldeffekttransistoren/03-substrateffekt-querschnitt**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei Querschnitte des Beispiel-NMOS unter dem Gate, jeweils genau an der Schwelle, maßstäblich in der Tiefe. (a) $U_{SB}$ = 0: Oberfläche 0,923 V über dem Inneren, Verarmungszone 45,8 nm, 4,17 fC/µm² feste Ladung, Schwelle 0,500 V. (b) $U_{SB}$ = 1 V (Source und Kanal 1 V über dem Bulk): Oberfläche 1,923 V über dem Inneren, Verarmungszone 66,2 nm, 6,02 fC/µm², Schwelle 0,768 V gegen die Source. Rechts je ein Balken der Gateladung, in (b) um 1,85 fC/µm² höher. Darunter klein der Potentialverlauf über der Tiefe für beide Fälle.

*Kernaussage:* Liegt die Source über dem Bulk, muss die Oberfläche höher angehoben werden; die breitere Verarmungszone bindet mehr Gateladung, und die Schwelle steigt.

*Daten:* Zahlenwerk T (x_d, |Q'_dep|).

*Editor:*
- §36 Ladungsschichten mit Daten; §27; §10 Teilbilder; §15 Schieberegler $U_{SB}$.

*Animation:* Schieberegler $U_{SB}$ von 0 bis 2,5 V: Die Zone wächst bis 88 nm, die Gateladung mit ihr, eine Anzeige zeigt die Schwelle.

**st1/mos-feldeffekttransistoren/03-schwelle-ubs**
- Fassung: kompakt Abb. 4, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Schwellenspannung in V (0,3 bis 1,1) über der Sperrspannung zwischen Source und Bulk in V (−0,4 bis 2,5): NMOS $U_{th}$ über $U_{SB}$: 0,351 / 0,392 / 0,431 / 0,500 / 0,646 / 0,768 / 0,875 / 0,971 / 1,059 V bei −0,4 / −0,3 / −0,2 / 0 / 0,5 / 1 / 1,5 / 2 / 2,5 V; PMOS $|U_{th,p}|$ über $U_{BS}$ (0 bis 2,5 V): 0,500 / 0,643 / 0,762 / 0,867 / 0,961 / 1,048 V. Gestrichelt die Tangente bei 0 mit der Steigung η = 0,327; Bereich links von 0 grau hinterlegt mit „Bulk über Source, Diode leitet zunehmend“.

*Kernaussage:* Die Schwelle wächst mit der Wurzel der Sperrspannung zwischen Source und Bulk; jedes weitere Volt hebt sie weniger.

*Daten:* Zahlenwerk T (uth_n_body, uthp_betrag).

*Editor:*
- §4, §11 Datenkurven; §4 Tangente; §4 Bereich hinterlegen.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/03-sourcefolger**
- Fassung: kompakt Abb. 5, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) NMOS-Sourcefolger: T2 mit Drain an $U_B$ = 2,5 V, Gate an $U_\mathrm{ein}$, Source am Ausgang, Bulk an Masse; darunter die Stromquelle 0,25 mA (T1).
- (b) PMOS-Sourcefolger: T3 mit Drain an Masse, Gate an $U_\mathrm{ein}$, Source am Ausgang, Bulk wahlweise an der Source (eigene Wanne) oder an $U_B$ (gemeinsame Wanne); darüber die Stromquelle 0,25 mA (T4).
- (c) Übertragungskennlinien $U_\mathrm{aus}$ über $U_\mathrm{ein}$: NMOS ohne Substrateffekt Gerade $U_\mathrm{ein}$ − 1 V (0,5 / 1,0 / 1,5 V bei 1,5 / 2 / 2,5 V), mit Substrateffekt 0,385 / 0,783 / 1,190 V, Steigung um 0,8; PMOS in eigener Wanne $U_\mathrm{ein}$ + 1 V, in gemeinsamer Wanne 1,305 / 1,714 V bei 0 / 0,5 V.

*Kernaussage:* Der Substrateffekt lässt den Ausgang des Folgers nur mit etwa 0,8 statt 1 folgen; eine eigene Wanne beseitigt ihn beim PMOS.

*Daten:* Zahlenwerk U (folger_n, folger_p).

*Editor:*
- §1 Schaltplan; §10 Teilbilder; §11 Datenkurven; §15 Schieberegler $U_\mathrm{ein}$.

*Animation:* Schieberegler $U_\mathrm{ein}$: Punkte auf den Kennlinien wandern, die Schwellenspannung von T2 wird angezeigt.

**st1/mos-feldeffekttransistoren/03-wannen-varianten**
- Fassung: ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Vier Querschnitte, schematisch: (a) NMOS T1 und T2 im gemeinsamen p-Substrat an Masse, Source von T2 am Ausgang: Substrateffekt bei T2; (b) PMOS T3 und T4 in einer gemeinsamen n-Wanne an $U_B$: Substrateffekt bei T3; (c) T3 in eigener n-Wanne, Wannenkontakt an seiner Source: kein Substrateffekt, dafür mehr Fläche und eine zusätzliche Kapazität zwischen Wanne und Substrat am Ausgang; (d) NMOS in einer isolierten p-Wanne in einer tiefen n-Wanne (Triple-Well), p-Wanne an der Source.

*Kernaussage:* Den Substrateffekt vermeidet nur ein eigenes, mit der Source verbundenes Gebiet; beim PMOS ist das eine eigene Wanne, beim NMOS braucht es eine tiefe n-Wanne.

*Daten:* schematisch.

*Editor:*
- §27 Technologie-Querschnitte; §10 Teilbilder; §36.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/03-latchup-struktur**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Querschnitt: p⁺-Substratkontakt an Masse, NMOS-Source n⁺ an Masse, n-Wanne mit n⁺-Kontakt an $U_B$ und PMOS-Source p⁺ an $U_B$; eingezeichnet der laterale npn (Emitter NMOS-Source, Basis Substrat, Kollektor Wanne), der vertikale pnp (Emitter PMOS-Source, Basis Wanne, Kollektor Substrat), $R_\mathrm{sub}$ zwischen Basis des npn und Substratkontakt, $R_\mathrm{well}$ zwischen Basis des pnp und Wannenkontakt.
- (b) Ersatzschaltbild: npn und pnp über Kreuz verbunden zwischen $U_B$ und Masse, $R_\mathrm{well}$ von $U_B$ an die Basis des pnp, $R_\mathrm{sub}$ von der Basis des npn nach Masse; der Mitkopplungsring als umlaufender Pfeil mit „β_npn · β_pnp“.
- (c) die Schichtfolge p⁺–n–p–n⁺ als Thyristor.

*Kernaussage:* Die Gebiete einer CMOS-Schaltung bilden zwei parasitäre Bipolartransistoren, von denen jeder den anderen ansteuert: einen Thyristor zwischen Versorgung und Masse.

*Daten:* schematisch; Werte des Beispiels (1 kΩ, 2 kΩ, β 5 und 50) als Beschriftung, Zahlenwerk V.

*Editor:*
- §27; §38 parasitäre Bauelemente im Querschnitt, Mitkopplungsring; §1 Schaltplan mit Bipolarsymbolen; §10.

*Animation:* Stromfluss nacheinander: Störstrom ins Substrat, npn leitet, Strom durch $R_\mathrm{well}$, pnp leitet, Strom zurück ins Substrat; die Pfeile werden mit jedem Umlauf dicker.

**st1/mos-feldeffekttransistoren/03-latchup-kennlinie**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Schematisch: Strom zwischen $U_B$ und Masse über der Spannung zwischen beiden (0 bis 3 V): gesperrter Ast mit sehr kleinem Strom, Zündpunkt (gestrichelt markiert), Rücksprung, leitender Ast im einfachen Modell ab rund 0,8 V steil ansteigend; Haltepunkt bei rund 1 mA; die Arbeitsgerade einer 2,5-V-Versorgung mit 1 Ω Innenwiderstand schneidet den leitenden Ast bei 1,7 A. Achsen mit Bruch zwischen mA und A.

*Kernaussage:* Nach dem Zünden hält sich der Thyristor mit rund 1 V selbst (im einfachen Modell 0,8 V); nur Abschalten oder ein Strom unter dem Haltestrom beendet den Zustand.

*Daten:* Zahlenwerk V (Haltepunkt, 0,8 V, 1,7 A), sonst schematisch.

*Editor:*
- §38 Kennlinie mit Rücksprung; §4 Arbeitsgerade, Schnittpunkt; §17 Achsenbruch.

*Animation:* Der Arbeitspunkt springt beim Zünden vom gesperrten auf den leitenden Ast und bleibt dort, wenn der Störstrom endet.

**st1/mos-feldeffekttransistoren/03-latchup-gegenmassnahmen**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Querschnitt wie in 03-latchup-struktur, ergänzt um: p⁺-Ring um den NMOS an Masse und n⁺-Ring um den PMOS an $U_B$ (Schutzringe), viele Substrat- und Wannenkontakte dicht an den Transistoren, eine dünne, schwach dotierte Epitaxieschicht auf hoch dotiertem p⁺-Substrat, größerer Abstand zwischen n⁺ und Wanne; Beschriftung der Wirkung: kleinere $R_\mathrm{sub}$ und $R_\mathrm{well}$, kleinere Stromverstärkungen, Abfangen der Ladungsträger. Kleines Einsatzbild: SOI-Querschnitt ohne gemeinsames Substrat.

*Kernaussage:* Gegen Latch-Up senkt man die Widerstände, damit kein Störstrom 0,6 V erzeugt, und die Stromverstärkungen, damit die Schleife unter 1 bleibt.

*Daten:* schematisch; Beschriftung 6 Ω für 100 mA (Zahlenwerk V).

*Editor:*
- §27; §38; §10 Einsatzbild.

*Animation:* keine.

## ST1 MOS-Feldeffekttransistoren: Parasitäre Kapazitäten des MOSFET
Zahlenwerk: `notizen/st1/zahlen_mosfet.py` (Ausgabe `.txt`), Abschnitte W bis AD; Beispiel-NMOS aus Thema 1 ($W/L$ = 10/1 µm, $t_\mathrm{ox}$ = 5 nm, $C'_\mathrm{ox}$ = 6,91 fF/µm², $C_\mathrm{ox}$ = 69,1 fF, $U_{th}$ = 0,5 V, $N_A$ = 5,68·10¹⁷ cm⁻³), Überlappung 50 nm je Seite ($C_\mathrm{ov}$ = 3,45 fF), Draingebiet 10 × 2 µm, 0,2 µm tief. Farben wie in Thema 1: p-Gebiete gelb, n-Gebiete grün, Verarmungszonen grau, Elektronen blau, Löcher rot; Kapazitätssymbole dunkelgrau, Werte daneben.

**st1/mos-feldeffekttransistoren/04-kapazitaeten-uebersicht**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Querschnitt des Beispiel-NMOS, schematisch, nicht maßstäblich: n⁺-Polysilizium-Gate über 5 nm Oxid, 1,1 µm lang über einem 1 µm langen Kanal, sodass es Source und Drain je 50 nm überlappt; n⁺-Source und -Drain 0,2 µm tief im p-Gebiet; Bulkkontakt. Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, $U_{SB}$ = 0 (Abschnürbereich): Kanal als Keil, der vor dem Drain endet. Kapazitätssymbole an den Orten der Ladung: zwei feste Überlappungskapazitäten an den Gatekanten (je 3,45 fF), spannungsabhängige $C_{GS}$ (46,0 fF) und $C_{GD}$ (0) vom Gate zum Kanal, $C_{GB}$ (praktisch 0) durch die Verarmungszone zum Bulk, $C_{SB}$ (53,1 fF bei 0 V) und $C_{DB}$ (37,8 fF bei 1 V) an Boden und Rand der n⁺-Gebiete. Jede Kapazität mit einer dünnen Linie zu dem Anschluss, aus dem ihre Gegenladung kommt.
- (b) Schaltzeichen des NMOS mit den fünf Kapazitäten zwischen den Anschlüssen: $C_{GS}$ = 49,5 fF (mit Überlappung), $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF, $C_{DB}$ = 37,8 fF.

*Kernaussage:* Zwischen allen vier Anschlüssen liegen Kapazitäten; ihr Wert hängt davon ab, wo die Ladung sitzt, und ändert sich mit dem Betriebsbereich.

*Daten:* Zahlenwerk Y ($C_\mathrm{ov}$, Bereiche), AA ($C_{SB}$, $C_{DB}$).

*Editor:*
- §27 Technologie-Querschnitte; §36 Kanalprofil; §39 Kondensatorsymbole im Querschnitt mit Anschlusszuordnung;
- §24, §1 Schaltzeichen mit Bauteilen zwischen den Anschlüssen; §10 Teilbilder.

*Animation:* Umschalten zwischen gesperrt ($U_{GS}$ = 0: $C_{GB}$ 20,7 fF, $C_{GS}$ = $C_{GD}$ = 3,45 fF), Abschnürbereich (Werte oben) und ohmschem Bereich (je 38,0 fF); die Symbole wachsen und schrumpfen mit ihrem Wert.

**st1/mos-feldeffekttransistoren/04-gatekapazitaet**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2.
- Status: offen.

*Inhalt:* Kapazität des Gates bezogen auf $C_\mathrm{ox}$ (0 bis 1,05; rechts angeschrieben: 1 entspricht 69,1 fF) über $U_{GS}$ in V (−2,5 bis 2,5) bei $U_{DS}$ = 0 und $U_{SB}$ = 0. Obere Kante: gesamte Gatekapazität $C_G$: 0,964 / 0,946 / 0,901 / 0,734 / 0,406 / 0,300 / 0,264 (Minimum) / 0,396 / 0,545 / 0,675 / 0,849 / 0,922 / 0,959 / 0,978 bei −2,5 / −2 / −1,5 / −1,03 / −0,5 / 0 / 0,35 / 0,5 / 0,55 / 0,6 / 0,75 / 1 / 1,5 / 2,5 V. Darunter als gestapelte Flächen der Bulkanteil $C_{GB}$ (grau): bis 0 V gleich der Gesamtkurve, dann 0,198 bei 0,5 V, 0,098 bei 0,6 V, 0,039 bei 0,75 V, 0,015 bei 1 V, 0,002 bei 2,5 V; und der Kanalanteil $C_{GS} + C_{GD}$ (blau, je zur Hälfte Source und Drain, durch eine Mittellinie geteilt): 0,198 bei 0,5 V, 0,577 bei 0,6 V, 0,811 bei 0,75 V, 0,907 bei 1 V, 0,953 bei 1,5 V, 0,976 bei 2,5 V. Gestrichelt grau der MOS-Kondensator ohne Source und Drain bei hoher Frequenz: 0,249 bei 0,5 V, 0,239 bei 1 V, 0,234 bei 2,5 V. Senkrechte Marken bei der Flachbandspannung −1,03 V und der Schwelle 0,5 V, darüber die Bereichsnamen Anreicherung, Verarmung, Inversion.

*Kernaussage:* Unterhalb der Schwelle liegt die Gegenladung im Bulk, oberhalb liefern Source und Drain die Elektronen; im Transistor kehrt die Gatekapazität deshalb auch bei hoher Frequenz auf $C_\mathrm{ox}$ zurück, und der Bulkanteil verschwindet.

*Daten:* Zahlenwerk W (gate_anteile, C_HF).

*Editor:*
- §4, §11 Datenkurven; §39 gestapelte Anteile; §10 Bereichsmarken.

*Animation:* Schieberegler $U_{GS}$; darüber ein kleiner Querschnitt, in dem die Gegenladung an der richtigen Stelle pendelt: Löcher an der Oberfläche, Rand der Verarmungszone, Kanalelektronen mit Pfeilen aus Source und Drain.

**st1/mos-feldeffekttransistoren/04-kanalladung-aufteilung**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* Zwei Zeilen, Ladung pro Fläche in fC/µm² über $x/L$ von 0 (Source) bis 1 (Drain).
- (a) Ohmscher Bereich, $U_{GS}$ = 1,5 V, $U_{DS}$ nahe 0: Kanalladung gleichmäßig 6,91 fC/µm². Links: Source um 10 mV angehoben, Gate, Drain und Bulk fest: Die Ladung sinkt an der Source um 0,069 fC/µm², linear auf null am Drain; die Differenzfläche ist ein Dreieck, ihr Mittelwert 1/2 als waagerechte Linie. Rechts: Drain angehoben, das gespiegelte Dreieck, ebenfalls 1/2.
- (b) Abschnürbereich, $U_{GS}$ = 1 V, $U_{DS}$ = 1 V: Kanalladung 3,45 fC/µm² mal $\sqrt{1 - x/L}$, also 3,45 / 2,99 / 2,44 / 1,73 / 0 fC/µm² bei 0 / 0,25 / 0,5 / 0,75 / 1. Links: Source 10 mV höher, die Ladung sinkt überall um 0,069 fC/µm² mal $\sqrt{1 - x/L}$, Mittelwert 2/3. Rechts: Drain höher, keine Änderung; die verarmte Zone am Drain nimmt die Spannung auf.

*Kernaussage:* Eine Anschlussspannung ändert die Kanalladung nur dort, wo das Kanalpotential ihr folgt; daraus folgen die Anteile 1/2 und 1/2 im ohmschen Bereich und 2/3 und 0 im Abschnürbereich.

*Daten:* Zahlenwerk X (Profile der Ladungsänderung).

*Editor:*
- §36 Kanalprofil aus Daten; §39 Profil mit Änderung, Differenzfläche und Mittelwertlinie; §10 Teilbilder.

*Animation:* Ein Anschluss wird angehoben, das Profil sinkt, die Differenzfläche füllt sich, und der Mittelwert erscheint als Balken.

**st1/mos-feldeffekttransistoren/04-cgs-cgd-uds**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* $C_{GS}$, $C_{GD}$ und ihre Summe in fF (0 bis 80) über $U_{DS}$ in V (0 bis 2) bei $U_{GS}$ = 1,5 V, nach dem Modell der Kennlinien ohne Überlappung: $C_{GS}$ 34,5 / 35,7 / 37,6 / 40,9 / 44,2 / 45,7 / 46,0 fF und $C_{GD}$ 34,5 / 33,3 / 31,0 / 25,6 / 16,6 / 8,0 / 0 fF bei 0 / 0,1 / 0,25 / 0,5 / 0,75 / 0,9 / 1 V, danach konstant 46,0 und 0 fF; Summe von 69,1 auf 46,0 fF. Gestrichelt dieselben Kurven mit je 3,45 fF Überlappung, $C_{GD}$ endet dann bei 3,45 fF. Senkrechte Marke an der Abschnürgrenze 1 V, links „ohmscher Bereich“, rechts „Abschnürbereich“; über dem Diagramm drei kleine Kanalbilder bei 0, 0,5 und 1 V.

*Kernaussage:* Mit wachsender Drain-Source-Spannung wandert die Gatekapazität vom Drain zur Source; ab der Abschnürgrenze gehört zum Drain nur noch die Überlappung.

*Daten:* Zahlenwerk X (Funktion meyer), Y ($C_\mathrm{ov}$).

*Editor:*
- §4, §11; §37 Bereichsgrenze; §36 kleine Kanalbilder; §10.

*Animation:* Schieberegler $U_{DS}$; der Abschnürpunkt wandert zum Drain und bleibt dort stehen, die Kurvenpunkte laufen mit.

**st1/mos-feldeffekttransistoren/04-ueberlappung**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Ausschnitt um die drainseitige Gatekante, in der Höhe gestreckt: Gate über 5 nm Oxid; das n⁺-Draingebiet reicht 50 nm unter die Gatekante (seitliche Diffusion beim Ausheilen). Feldlinien vom Gate in das n⁺-Gebiet: unter der Überlappung dicht und parallel (Plattenkondensator, $C_\mathrm{ov}$ = 3,45 fF bei 10 µm Weite), dazu gebogene Linien von der Gateflanke zur Drainoberfläche, beschriftet „Randfeld“. Links davon der Kanal mit abgeschnürtem Ende, damit sichtbar ist, dass die Überlappung unabhängig von der Abschnürung besteht.

*Kernaussage:* Die Überlappung ist ein kleiner Plattenkondensator zwischen Gate und Drain, den keine Abschnürung abschaltet.

*Daten:* Zahlenwerk Y.

*Editor:*
- §27; §3 Feldlinien; §39 Kondensatorsymbol.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/04-sperrschicht-geometrie**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Zwei Teilbilder.
- (a) Aufsicht auf das Draingebiet: Rechteck $W$ = 10 µm entlang der Gatekante mal $b$ = 2 µm, Gatekante an einer Längsseite; Fläche $A_D$ = 20 µm² schraffiert, Umfang $P_D$ = 24 µm als dicke Randlinie, Maßpfeile.
- (b) Querschnitt quer zur Gatekante: n⁺-Gebiet 0,2 µm tief, umgeben von der Verarmungszone (grau, 48,4 nm ohne Spannung, 67,9 nm bei 1 V); Kondensatorsymbole am Boden ($C'_{jF}$ = 2,14 fF/µm²) und an den Seitenwänden ($C'_{jS}$ = 0,428 fF/µm); an der Gatekante grenzt die Seitenwand an das p-Gebiet unter dem nur wenige Nanometer dicken Kanal. Werte ohne Spannung: Boden 42,9 fF, Rand 10,3 fF.

*Kernaussage:* Die Kapazität eines Source- oder Draingebiets besteht aus Boden und Rand; der Boden zählt mit seiner Fläche, der Rand mit seiner Länge.

*Daten:* Zahlenwerk AA.

*Editor:*
- §27; §36 Layout-Aufsicht mit Maßpfeilen und Schnittlinie; §39 Kondensatorsymbole; §10.

*Animation:* Umschalten auf ein Gebiet von einem Viertel der Kantenlänge (2,5 × 0,5 µm): Boden 2,68 fF, Rand 2,57 fF; der Randanteil steigt von 19 % auf 49 %.

**st1/mos-feldeffekttransistoren/04-sperrschicht-spannung**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zwei gestapelte Diagramme mit gemeinsamer x-Achse $U_{DB}$ in V (0 bis 2,5).
- Oben: $C_{DB}$ in fF (0 bis 60), als gestapelte Flächen Boden (42,9 / 35,1 / 30,5 / 27,3 / 25,0 / 23,1 fF) und Rand (10,3 / 8,4 / 7,3 / 6,6 / 6,0 / 5,5 fF), Summe 53,1 / 43,6 / 37,8 / 33,9 / 31,0 / 28,7 fF bei 0 / 0,5 / 1 / 1,5 / 2 / 2,5 V. Gestrichelt die Summe mit $m_j$ = 1/3 bei gleichem Wert ohne Spannung (Faktor 0,797 statt 0,712 bei 1 V, 0,663 statt 0,540 bei 2,5 V).
- Unten: Breite der Zone in nm: 48,4 / 59,0 / 67,9 / 75,8 / 83,0 / 89,6.

*Kernaussage:* Mit der Sperrspannung wird die Zone breiter und die Kapazität kleiner, beim abrupten Übergang mit der Wurzel der Spannung über der Zone.

*Daten:* Zahlenwerk AA (Funktion c_diff).

*Editor:*
- §4, §11; §13 gestapelte Diagramme; §39 gestapelte Anteile.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/04-finger-layout**
- Fassung: ausführlich Abb. 8 (im Beispiel zur Sperrschichtkapazität).
- Status: offen.

*Inhalt:* Zwei Layout-Aufsichten bei gleicher Gesamtweite 10 µm. (a) Ein Finger: Source 10 × 2 µm, Gate 10 µm breit, Drain 10 × 2 µm. (b) Zwei Finger zu je 5 µm in der Folge Source, Gate, Drain, Gate, Source: Der Drain in der Mitte (5 × 2 µm) gehört zu beiden Gates, die beiden Sources liegen außen und sind verbunden. Werte bei $U_{DB}$ = 1 V: $C_{DB}$ = 37,8 fF gegen 19,5 fF.

*Kernaussage:* Teilen sich zwei Gates einen Drain, halbiert sich fast die Drainkapazität bei unverändertem Strom.

*Daten:* Zahlenwerk AA.

*Editor:*
- §36 Layout-Aufsicht; §10.

*Animation:* Der eine Finger klappt in zwei Hälften um den Drain; der Wert läuft von 37,8 auf 19,5 fF.

**st1/mos-feldeffekttransistoren/04-leitung-randfeld**
- Fassung: ausführlich Abb. 9.
- Status: offen.

*Inhalt:* Querschnitt einer Metallbahn, $b_M$ = 2 µm breit, $t_M$ = 0,5 µm dick, $h$ = 1 µm über dem Substrat, Oxid dazwischen; das Substrat als leitende Ebene. Feldlinien unter der Bahn senkrecht und gleichmäßig (Plattenanteil), von den Flanken und der Oberseite in Bögen zur Ebene (Randfeld). Je Millimeter Länge: Plattenkondensator 69,1 fF, mit Randfeld 162 fF (Faktor 2,35). Kleine Tabelle daneben für 1 / 2 / 4 µm Breite: Faktor 3,55 / 2,35 / 1,75.

*Kernaussage:* Je schmaler eine Bahn im Verhältnis zu ihrem Abstand vom Substrat, desto mehr trägt das Randfeld zu ihrer Kapazität bei.

*Daten:* Zahlenwerk AB (Formel von Sakurai und Tamaru).

*Editor:*
- §3 Feldlinien; §27; §39.

*Animation:* Schieberegler für die Breite von 1 bis 4 µm; Plattenanteil und Randanteil als Balken.

**st1/mos-feldeffekttransistoren/04-miller**
- Fassung: kompakt Abb. 6, ausführlich Abb. 10.
- Status: offen.

*Inhalt:* Drei Teilbilder.
- (a) Source-Schaltung: NMOS mit Source und Bulk an Masse, $R_D$ = 10 kΩ zur Versorgung, Signalquelle mit 10 kΩ Innenwiderstand am Gate; eingezeichnet $C_{GS}$ = 49,5 fF (Gate nach Masse), $C_{GD}$ = 3,45 fF (Gate zum Drain), $C_{DB}$ = 37,8 fF (Drain nach Masse); Kleinsignalwerte $g_m$ = 1 mS, $g_o$ = 25 µS, $A_V$ = −8. Spannungsbalken: Gate +10 mV, Drain −80 mV, über $C_{GD}$ 90 mV.
- (b) Miller-Ersatz: $C_{GD}$ aufgeteilt in $C_{GD}(1 - A_V)$ = 31,1 fF vom Gate nach Masse und $C_{GD}(A_V - 1)/A_V$ = 3,88 fF vom Drain nach Masse; am Eingang zusammen 80,6 fF statt 52,9 fF, am Ausgang 41,7 fF.
- (c) Balken der Eingangskapazität für $A_V$ = 0 (52,9 fF), −8 (80,6 fF) und −40 (191,1 fF), der Anteil aus $C_{GD}$ farbig (3,45 / 31,1 / 141,6 fF).

*Kernaussage:* Weil sich die Spannung über $C_{GD}$ neunmal so stark ändert wie am Gate, wirkt sie am Eingang neunmal so groß.

*Daten:* Zahlenwerk AC.

*Editor:*
- §1 Schaltplan; §28 Kleinsignalgrößen; §39 Miller-Umformung mit Spannungsbalken; §18 Balken; §10.

*Animation:* Das Gate steigt um 10 mV, der Drain fällt um 80 mV, ein Ladungspfeil durch $C_{GD}$ wächst auf 0,311 fC; dann die Umformung von (a) nach (b).

**st1/mos-feldeffekttransistoren/04-miller-kompensation**
- Fassung: ausführlich Abb. 11.
- Status: offen.

*Inhalt:* Zweistufiger Verstärker als Blockbild: erste Stufe mit Ausgangswiderstand 1 MΩ, zweite Stufe invertierend mit $A_2$ = −50; $C_M$ = 1 pF zwischen Ein- und Ausgang der zweiten Stufe. Darunter der Ersatz: 51 pF vom Ausgang der ersten Stufe nach Masse. Rechts maßstäblich zwei Quadrate für die Kondensatorfläche bei 1 fF/µm²: 32 µm Seitenlänge für 1 pF, 226 µm für 51 pF.

*Kernaussage:* Über den Miller-Effekt wirkt ein kleiner Kondensator wie ein 51-mal größerer; das spart Chipfläche.

*Daten:* Zahlenwerk AD (angenommene Werte).

*Editor:*
- §19 Blockbilder; §1; §39 Miller-Umformung, Flächenvergleich.

*Animation:* keine.

## ST1 MOS-Feldeffekttransistoren: Kleinsignalmodell des MOSFET
Zahlenwerk: `notizen/st1/zahlen_mosfet.py` (Ausgabe `.txt`), Abschnitte AE bis AM; Beispiel-NMOS aus Thema 1 ($K_n$ = 2 mA/V², $U_{th0}$ = 0,5 V, λ = 0,1 1/V, γ = 0,629 √V), Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, $U_{SB}$ = 0 mit 0,275 mA. Farben: Kennlinien dunkelblau, Tangenten orange gestrichelt, Arbeitspunkt rot; gesteuerte Quellen wie in §28.

**st1/mos-feldeffekttransistoren/05-tangenten-uebersicht**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Drei kleine Diagramme nebeneinander bzw. auf dem Handy untereinander, jeweils mit rotem Arbeitspunkt und oranger Tangente: (a) $I_D$ über $U_{GS}$ bei $U_{DS}$ = 1 V, Tangente mit 1,1 mS; (b) $I_D$ über $U_{DS}$ bei $U_{GS}$ = 1 V, Tangente mit 25 µS; (c) $I_D$ über $U_{BS}$ bei $U_{GS}$ = $U_{DS}$ = 1 V, Tangente mit 0,36 mS. Daneben das statische Kleinsignal-Ersatzschaltbild: offenes Gate, zwischen Drain und Source die Quellen $g_m u_{GS}$ und $g_{mB} u_{BS}$ und der Leitwert $g_o$, jede Steigung mit Pfeil zu ihrem Bauelement.

*Kernaussage:* Jede Steigung im Arbeitspunkt wird ein Bauelement des Ersatzschaltbilds.

*Daten:* Zahlenwerk AE, AH.

*Editor:*
- §4, §11 Kennlinien; §37 Steigungsdreieck; §28 Kleinsignal-Ersatzschaltbild; §10 Teilbilder.

*Animation:* Der Arbeitspunkt wandert auf (a); die Tangente und der Wert $g_m$ im Ersatzschaltbild ändern sich mit.

**st1/mos-feldeffekttransistoren/05-steilheit**
- Fassung: kompakt Abb. 3, ausführlich Abb. 3.
- Status: offen.

*Inhalt:* Zwei gestapelte Diagramme über $U_{GS}$ von 0 bis 2 V bei $U_{DS}$ = 1 V. Oben $I_D$ in mA: 0 bis 0,5 V null, 0,275 mA bei 1 V, 1,1 mA bei 1,5 V; Tangente in 1 V mit 1,1 mS, sie trifft die Achse bei 0,75 V; schattiert der Abstand zwischen Kurve und Tangente bei ±100 mV (+10 % bzw. −10 %) und ±10 mV (±1 %). Unten $g_m$ in mS: null bis 0,5 V, dann linear bis 2,2 mS bei 1,5 V (Abschnürbereich bis 1,5 V, weil $U_{DS}$ = 1 V); darüber gestrichelt die Näherung $K(U_{GS} - U_{th})$ ohne den Faktor 1,1.

*Kernaussage:* Die Steilheit ist die Steigung der Übertragungskennlinie im Arbeitspunkt und wächst mit der Übersteuerung.

*Daten:* Zahlenwerk AE, AG.

*Editor:*
- §4, §11; §13 gestapelte Diagramme; §37 Steigungsdreieck; §39 Flächenanteile (Abweichung).

*Animation:* Schieberegler für die Signalamplitude: Der Bereich um den Arbeitspunkt wächst, die Abweichung wird angezeigt.

**st1/mos-feldeffekttransistoren/05-gm-id**
- Fassung: ausführlich Abb. 4.
- Status: offen.

*Inhalt:* $g_m/I_D$ in 1/V über $U_{GS}$ von 0,2 bis 1,5 V bei $U_{DS}$ = 1 V, halblogarithmisch oder linear: unterhalb der Schwelle waagerecht bei 27,9 1/V (Grenze $1/U_T$ = 38,7 1/V gestrichelt), oberhalb $2/(U_{GS} - U_{th})$: 20 1/V bei 0,6 V, 8 bei 0,75 V, 4 bei 1 V, 2 bei 1,5 V. Übergangsbereich um die Schwelle als „im Modell nicht beschrieben“ markiert.

*Kernaussage:* Je kleiner die Übersteuerung, desto mehr Steilheit gibt ein Milliampere Strom; unterhalb der Schwelle ist das Verhältnis am größten.

*Daten:* Zahlenwerk AL.

*Editor:*
- §4, §11; §12 halblogarithmische Achse; §37.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/05-ausgangsleitwert**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Oben $I_D$ in mA über $U_{DS}$ von −10 V bis 2,5 V (Achsenbruch zwischen −10 und 0 V) bei $U_{GS}$ = 1 V: ohmscher Bereich bis 0,5 V (0,0909 mA bei 0,1 V), Abschnürbereich mit Steigung 25 µS (0,275 mA bei 1 V, 0,3 mA bei 2 V); Tangente bei 1 V, verlängert bis zur Achse bei −10 V (Early-Spannung). Unten $g_m$ und $g_o$ in mS über $U_{DS}$ von 0 bis 2,5 V: $g_o$ fällt von 1 mS bei 0 V über 0,817 bei 0,1 V und 0,433 bei 0,3 V auf 0,025 mS ab 0,5 V; $g_m$ steigt von 0 über 0,202 und 0,618 auf 1,05 mS bei 0,5 V und 1,1 mS bei 1 V. Marke an der Abschnürgrenze, beide Kurven stetig.

*Kernaussage:* Im Abschnürbereich ist der Ausgangsleitwert klein und die Steilheit groß, im ohmschen Bereich umgekehrt.

*Daten:* Zahlenwerk AE, AF.

*Editor:*
- §4, §11; §13; §17 Achsenbruch; §37 Extrapolation bis zum Schnittpunkt.

*Animation:* Schieberegler $U_{DS}$; der Arbeitspunkt wandert, beide Werte laufen mit.

**st1/mos-feldeffekttransistoren/05-substratsteilheit**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* Oben $I_D$ in mA über $U_{BS}$ von −2,5 bis +0,3 V bei $U_{GS}$ = 1 V und $U_{DS}$ = 1 V: 0 bei −2,5 V, 0,0593 mA bei −1 V, 0,138 bei −0,5 V, 0,275 bei 0, 0,406 bei +0,3 V; Tangente bei 0 mit 0,36 mS; Bereich $U_{BS}$ > 0 grau, „Diode in Durchlassrichtung“. Unten η über $U_{SB}$ von 0 bis 2 V: 0,327 / 0,264 / 0,227 / 0,202 / 0,184.

*Kernaussage:* Der Bulk steuert den Strom wie ein zweites, schwächeres Gate; sein Anteil η sinkt mit der Sperrspannung.

*Daten:* Zahlenwerk AH.

*Editor:*
- §4, §11; §13; §37.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/05-esb-statisch**
- Fassung: ausführlich Abb. 7.
- Status: offen.

*Inhalt:* Zwei Ersatzschaltbilder nebeneinander. (a) NMOS: Gate offen, zwischen Drain und Source die Quellen $g_m u_{GS}$ und $g_{mB} u_{BS}$, beide vom Drain zur Source gerichtet, parallel $g_o$; Kleinsignalspannungen $u_{GS}$, $u_{DS}$, $u_{BS}$ mit Zählpfeilen zur Source, $i_D$ in den Drain. Werte 1,1 mS, 0,36 mS, 25 µS. (b) PMOS: dasselbe Bild, der Drain liegt unten (niedrigeres Potential); Werte 1,1 mS, 0,353 mS, 25 µS, alle positiv.

*Kernaussage:* NMOS und PMOS haben dasselbe Kleinsignal-Ersatzschaltbild mit positiven Parametern.

*Daten:* Zahlenwerk AE, AJ.

*Editor:*
- §1, §28; §2 Zählpfeile; §10.

*Animation:* keine.

**st1/mos-feldeffekttransistoren/05-sourcefolger-kleinsignal**
- Fassung: kompakt Abb. 6, ausführlich Abb. 8.
- Status: offen.

*Inhalt:* (a) NMOS-Sourcefolger: Drain an $U_B$ = 2,5 V, Source über eine ideale Stromquelle 0,25 mA an Masse, Bulk an Masse; $U_\mathrm{ein}$ = 2 V, $U_\mathrm{aus}$ = 0,783 V. (b) Kleinsignal-Ersatzschaltbild: Drain an Masse (Versorgung fest), Quelle $g_m u_{GS}$ mit $u_{GS} = u_\mathrm{ein} - u_\mathrm{aus}$, Quelle $g_{mB} u_{BS}$ mit $u_{BS} = -u_\mathrm{aus}$; daneben umgezeichnet als Leitwert $g_{mB}$ = 0,241 mS von der Source nach Masse. (c) Ergebnis: Verstärkung 0,806, Ausgangswiderstand 806 Ω statt 1 kΩ.

*Kernaussage:* Weil der Bulk festliegt, wirkt die Substratsteilheit im Folger wie ein zusätzlicher Leitwert am Ausgang.

*Daten:* Zahlenwerk AI.

*Editor:*
- §1, §28; §10; §39 Umformung (Quelle → Leitwert).

*Animation:* Umformung der gesteuerten Quelle in einen Leitwert.

**st1/mos-feldeffekttransistoren/05-esb-dynamisch**
- Fassung: kompakt Abb. 7, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* (a) Vollständiges dynamisches Kleinsignal-Ersatzschaltbild: inneres statisches Ersatzschaltbild zwischen inneren Knoten G′, D′, S′, B′; außen die Bahnwiderstände $R_G$, $R_D$, $R_S$, $R_B$; Kapazitäten $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF (dazu rund 15 fF Kanal–Bulk), $C_{DB}$ = 37,8 fF. (b) Vereinfacht für Bulk an Source: $C_{GS}$, $C_{GD}$, $g_m u_{GS}$, $g_o$ und $C_{DB}$ zwischen Drain und Source.

*Kernaussage:* Für schnelle Änderungen kommen zum statischen Modell die Kapazitäten hinzu; die meisten Bahnwiderstände sind vernachlässigbar, der Gatewiderstand nicht immer.

*Daten:* Zahlenwerk AK und Thema 4 (Y, AA).

*Editor:*
- §1, §28; §39 Kondensatorsymbole; §10.

*Animation:* Umschalten zwischen vollständig und vereinfacht.

## ST1 Bipolartransistor: Arbeitsbereiche und Transportmodell
Zahlenwerk: `notizen/st1/zahlen_bipolar.py` (Ausgabe `.txt`), Abschnitte A bis K; integrierter Beispiel-npn mit $I_S$ = 10⁻¹⁶ A, $B_N$ = 100, $B_I$ = 2, $U_A$ = 50 V, Emitterfläche 20 µm², Arbeitspunkt 1 mA bei $U_{BE}$ = 773,8 mV. Farben nach ERKLAER_PROMPT §7.4: Elektronen blau, Löcher rot, Raumladungszonen grau; n-Gebiete blau, p-Gebiete rot hinterlegt (§27); Kennlinien dunkelblau, Tangenten orange gestrichelt, Arbeitspunkt rot.

**st1/bipolartransistor/01-einstieg**
- Fassung: kompakt Abb. 1, ausführlich Abb. 1.
- Status: offen.

*Inhalt:* Links der npn-Querschnitt im Normalbetrieb, schematisch (Basis 0,1 µm nicht maßstäblich): Emitter n⁺ unten, Basis p, Kollektor n oben, beide Raumladungszonen grau; Elektronen (blau) laufen vom Emitter durch die Basis in den Kollektor, Mengenpfeil 1 mA; Löcher (rot) kommen über den Basisanschluss nach, Mengenpfeil 10 µA mit eigenem Maßstab; äußere Zählpfeile $I_C$ = 1 mA hinein, $I_B$ = 10 µA hinein, $I_E$ = −1,01 mA. Rechts das vereinfachte Transportmodell: Diode zwischen Basis und Emitter mit $I_B$ = 10 µA, gesteuerte Quelle $I_C$ = $B_N I_B$ = 1 mA vom Kollektor zum Emitter, $U_{BE}$ = 773,8 mV; gestrichelte Zuordnung der Quelle zu $U_{BE}$.

*Kernaussage:* Die Basis-Emitter-Spannung legt den Kollektorstrom fest; die Basis liefert nur ein Hundertstel davon.

*Daten:* Zahlenwerk A, B.

*Editor:*
- §27 Querschnitt mit Dotierfarben; §14 Teilchen; §18 Mengenpfeile mit zwei Maßstäben; §28 gesteuerte Quelle mit Steuerzuordnung; §2 Zählpfeile; §10 Teilbilder.

*Animation:* Schieberegler $U_{BE}$ (0,70 bis 0,80 V): Elektronendichte in der Basis, beide Mengenpfeile und die Zahlen im Modell laufen mit (57,6 µA bis 2,76 mA).

**st1/bipolartransistor/01-aufbau-diskret-integriert**
- Fassung: ausführlich Abb. 3.
- Status: offen.

*Inhalt:* (a) Diskreter npn: n⁺-Substrat als Kollektorkontakt auf der Rückseite (C), darüber n-Epitaxie (Kollektor), p-Basis, n⁺-Emitter; Kontakte E und B oben. (b) Integrierter npn: p-Substrat, darin n-Wanne (Kollektor) mit vergrabener n⁺-Schicht („buried layer“) und n⁺-Kollektorkontakt oben, p-Basisgebiet, n⁺-Emitter darin; p⁺-Substratkontakte S links und rechts; Diodensymbol zwischen Substrat und Kollektor, als gesperrt eingefärbt, Substrat an der negativsten Versorgung (−2,5 V oder Masse). (c) Layout-Draufsicht von (b): Emitterfläche 2 µm × 10 µm hervorgehoben, Basis- und Kollektorkontakte daneben, Substratring; Maßpfeile.

*Kernaussage:* Der buried layer bringt den Kollektor nach oben, die gesperrte Substratdiode trennt die Transistoren; die Emitterfläche ist der Skalierungsparameter.

*Daten:* Zahlenwerk A, J.

*Editor:*
- §27 Technologie-Querschnitte (n⁺ vergraben); §36 pn-Übergang als Diodensymbol im Querschnitt, Layout-Draufsicht mit Schnittlinie; §10 Teilbilder.

*Animation:* Umschalten zwischen Querschnitt und Draufsicht mit Schnittlinie.

**st1/bipolartransistor/01-symbole-zaehlpfeile**
- Fassung: kompakt Abb. 3, ausführlich Abb. 4.
- Status: offen.

*Inhalt:* (a) npn: Schichtfolge n (C), p (B), n (E) als drei Balken mit zwei Diodensymbolen (Kollektordiode zeigt von B nach C, Emitterdiode von B nach E), daneben das Schaltsymbol mit Emitterpfeil nach außen; Zählpfeile $I_B$ und $I_C$ in den Transistor, $I_E$ aus dem Emitter heraus gezählt als negativ (Pfeil hinein, Wert −1,01 mA), Spannungspfeile $U_{BE}$ von B nach E, $U_{CE}$ von C nach E, $U_{BC}$ von B nach C; Werte im Normalbetrieb $U_{BE}$ = 0,774 V, $U_{CE}$ = 2,5 V, $U_{BC}$ = −1,73 V, $I_B$ = 10 µA, $I_C$ = 1,05 mA. (b) pnp: Schichtfolge p, n, p, Emitterpfeil nach innen, dieselben Zählpfeile (alle Ströme hinein gezählt), Werte mit umgekehrten Vorzeichen: $U_{BE}$ = −0,774 V, $U_{CE}$ = −2,5 V, $I_B$ = −10 µA, $I_C$ = −1,05 mA, $I_E$ = +1,06 mA.

*Kernaussage:* Alle Ströme werden in den Transistor hinein gezählt, deshalb ist der Emitterstrom des npn negativ; der pnp ist derselbe Transistor mit umgekehrten Vorzeichen.

*Daten:* Zahlenwerk B, D (aktiv 2,5 V).

*Editor:*
- §1 Symbole npn und pnp; §2 Zählpfeile; §6 Schichtfolge; §36 Diodensymbole im Querschnitt; §10 Teilbilder.

*Animation:* keine.

**st1/bipolartransistor/01-kennlinien**
- Fassung: kompakt Abb. 4, ausführlich Abb. 5.
- Status: offen.

*Inhalt:* Drei Diagramme über $U_{BE}$ von 0,5 bis 0,9 V. (a) $I_C$ in mA linear: 0,058 mA bei 0,70 V, 0,40 mA bei 0,75 V, 1,0 mA bei 0,774 V, 2,76 mA bei 0,80 V, 19 mA bei 0,85 V (Achse bis 5 mA, Kurve verlässt das Bild); Arbeitspunkt rot. (b) $I_C$ halblogarithmisch von 10 nA bis 100 mA: Gerade mit 59,5 mV je Dekade, Steigungsdreieck. (c) $I_B$ in µA linear, dieselbe Form wie (a) mit 1/100 der Werte: 10 µA bei 0,774 V, 27,6 µA bei 0,80 V. Keine Early-Abhängigkeit (U_CE fest 2,5 V, oder Werte ohne Early-Faktor; im Bild ohne Early).

*Kernaussage:* Übertragungs- und Eingangskennlinie sind dieselbe Exponentialfunktion, um den Faktor $B_N$ = 100 verschoben; 60 mV mehr geben zehnmal so viel Strom.

*Daten:* Zahlenwerk B, K.

*Editor:*
- §4, §11 Datenkurven; §12 halblogarithmische Achse; §37 Steigungsdreieck („eine Dekade je 60 mV“); §10 Teilbilder.

*Animation:* Punkt auf (a) wandert, der zugehörige Punkt auf (b) und (c) läuft mit (§37 gekoppelte Punkte).

**st1/bipolartransistor/01-arbeitsbereiche**
- Fassung: kompakt Abb. 5, ausführlich Abb. 6.
- Status: offen.

*Inhalt:* (a) Ebene mit $U_{BE}$ waagerecht und $U_{BC}$ senkrecht, je −1 bis +1 V: vier Quadranten farbig hinterlegt und beschriftet: gesperrt (beide negativ), aktiv normal ($U_{BE}$ > 0, $U_{BC}$ < 0), Sättigung (beide positiv), invers ($U_{BE}$ < 0, $U_{BC}$ > 0); der Ursprung als „stromlos“; die Diagonale $U_{BC}$ = $U_{BE}$ als Linie $U_{CE}$ = 0; der Arbeitspunkt (0,774 V, −1,73 V) als roter Punkt im aktiven Quadranten, der Sättigungspunkt (0,797 V, 0,697 V) als zweiter Punkt. (b) Ausgangskennlinienfeld $I_C$ über $U_{CE}$ von 0 bis 3 V für $U_{BE}$ = 0,70, 0,75, 0,774 und 0,80 V: steiler Anstieg bis etwa 0,1 V (0,784 mA bei 0,05 V, 0,971 mA bei 0,1 V, 1,003 mA bei 0,2 V für 0,774 V), dann flach mit Early-Steigung (1,02 mA bei 1 V, 1,05 mA bei 2,5 V); Sättigungsbereich links der gestrichelten Grenze $U_{CE}$ ≈ 0,1 bis 0,3 V grau hinterlegt, aktiver Bereich rechts; Kurven beschriftet mit $U_{BE}$.

*Kernaussage:* Welche der beiden Dioden leitet, legt den Betriebszustand fest; im Kennlinienfeld ist die Sättigung der schmale Streifen links, der aktive Bereich die flachen Geraden.

*Daten:* Zahlenwerk D, K.

*Editor:*
- §4 Bereiche in einer Ebene (farbige Quadranten mit Beschriftung); §11 Datenkurven; §37 Bereichsgrenze entlang einer Kurve, Kennlinienschar mit benanntem Parameter; §10 Teilbilder.

*Animation:* Ein Punkt in (a) lässt sich ziehen; in (b) erscheint der zugehörige Punkt ($I_C$, $U_{CE}$), und das Transportmodell (Szene 01-transportmodell) zeigt die Ströme.

**st1/bipolartransistor/01-transportmodell**
- Fassung: kompakt Abb. 6, ausführlich Abb. 7.
- Status: offen.

*Inhalt:* (a) Vollständiges Transportmodell: Knoten B links, C oben, E unten; von B nach C die Kollektordiode mit Strom $I_{B,I}$ (Pfeil von B nach C), von B nach E die Emitterdiode mit $I_{B,N}$; zwischen C und E die gesteuerte Stromquelle $I_T$ = $B_N I_{B,N}$ − $B_I I_{B,I}$, Pfeil von C nach E, gestrichelte Zuordnung zu beiden Diodenspannungen; Spannungspfeile $U_{BE}$ und $U_{BC}$; Zählpfeile $I_B$, $I_C$ hinein, $I_E$; Werte im Arbeitspunkt (1 mA, 2,5 V): $I_{B,N}$ = 10 µA, $I_{B,I}$ ≈ 0 (−5·10⁻¹⁷ A), $I_T$ = 1,05 mA. (b) Vereinfachtes Transportmodell für den Normalbetrieb: nur Emitterdiode mit $I_B$ und Quelle $I_C$ = $B_N I_B$; $I_E$ = −(1 + $B_N$) $I_B$ = −1,01 mA ohne Early-Faktor.

*Kernaussage:* Zwei Dioden beschreiben die Basis, eine gesteuerte Quelle den Transportstrom durch sie; im Normalbetrieb bleibt eine Diode und eine Quelle übrig.

*Daten:* Zahlenwerk D.

*Editor:*
- §1 Dioden; §28 gesteuerte Quelle mit Steuerausdruck und gestrichelter Zuordnung, Gegenüberstellung vollständig/vereinfacht; §2 Zählpfeile; §10 Teilbilder.

*Animation:* Beim Übergang zu (b) blasst die Kollektordiode aus (Strom 10⁻¹⁷ A) und der Steuerausdruck vereinfacht sich.

**st1/bipolartransistor/01-saettigung-stroeme**
- Fassung: ausführlich Abb. 8.
- Status: offen.

*Inhalt:* Schaltung: Basis aus Stromquelle $I_B$ = 50 µA, Kollektor über $R_C$ = 1 kΩ an 2,5 V, Emitter an Masse; der Transistor als vollständiges Transportmodell gezeichnet. Mengenpfeile mit Zahlen: $I_{B,N}$ = 24,7 µA in die Emitterdiode, $I_{B,I}$ = 25,3 µA in die Kollektordiode, $I_T$ = 2,42 mA (100 · 24,7 µA − 2 · 25,3 µA mit Early-Faktor), $I_C$ = 2,40 mA, $I_E$ = −2,45 mA; Spannungen $U_{BE}$ = 797 mV, $U_{BC}$ = 697 mV, $U_{CE}$ = 100 mV; am Widerstand 2,40 V. Daneben klein derselbe Transistor bei $I_B$ = 10 µA (aktiv: $I_{B,I}$ ≈ 0, $U_{CE}$ = 1,47 V, $I_C$ = 1,03 mA).

*Kernaussage:* In der Sättigung teilt sich der Basisstrom auf beide Dioden; der Kollektorstrom bleibt bei dem Wert, den der Widerstand zulässt, und $U_{CE}$ ist die Differenz zweier Durchlassspannungen.

*Daten:* Zahlenwerk E.

*Editor:*
- §1 Schaltbild mit Transportmodell; §28 gesteuerte Quelle; §18 Mengenpfeile mit zwei Maßstäben (µA und mA); §10 Teilbilder.

*Animation:* Schieberegler $I_B$ von 5 bis 100 µA: Aufteilung, $U_{CE}$ und $I_C$ laufen mit (Tabelle E).

**st1/bipolartransistor/01-early-effekt**
- Fassung: kompakt Abb. 7, ausführlich Abb. 9.
- Status: offen.

*Inhalt:* (a) Ausgangskennlinien $I_C$ über $U_{CE}$ für $U_{BE}$ = 0,75, 0,774 und 0,80 V von −50 V bis 5 V mit Achsenbruch zwischen −50 und 0 V; im aktiven Bereich Geraden mit Steigung $I_C$/($U_A$ + $U_{CE}$) (20 µS bei 1 mA), nach links verlängert bis zum gemeinsamen Schnittpunkt −$U_A$ = −50 V; Werte 1,00 mA bei 0 V (extrapoliert), 1,02 bei 1 V, 1,05 bei 2,5 V, 1,10 bei 5 V. (b) Querschnitt der Basis, schematisch: p-Basis zwischen den beiden Raumladungszonen; bei $U_{CB}$ = 1 V und 5 V dringt die Kollektor-Raumladungszone tiefer in die Basis, die neutrale Basisweite schrumpft (beschriftet $W_B$); daneben der Minoritätsverlauf in der Basis als Gerade, die bei kürzerer Basis steiler wird.

*Kernaussage:* Mehr Kollektorspannung verbreitert die Kollektor-Raumladungszone, verkürzt die Basis und steigert den Strom; alle Tangenten treffen sich bei −$U_A$.

*Daten:* Zahlenwerk C, K.

*Editor:*
- §4, §11; §17 Achsenbruch; §37 Extrapolation zum gemeinsamen Schnittpunkt, Steigung je Kurve; §27 Querschnitt mit Raumladungszonen, an $U_{CB}$ gekoppelt (§15); §10 Teilbilder.

*Animation:* Schieberegler $U_{CB}$: die Zone wächst, $W_B$ schrumpft, der Punkt auf der Kennlinie wandert.

**st1/bipolartransistor/01-gummel-plot**
- Fassung: ausführlich Abb. 10.
- Status: offen.

*Inhalt:* (a) Gummel-Plot: $I_C$ und $I_B$ in A, logarithmisch von 10⁻¹² bis 10⁻¹, über $U_{BE}$ von 0,4 bis 1,0 V; $I_C$ als Gerade mit 59,5 mV je Dekade bis etwa 0,8 V, darüber abknickend (2,62 mA bei 0,80 V ideal 2,76; 14,7 mA bei 0,85 V ideal 19,1; 60,0 mA bei 0,90 V ideal 132); $I_B$ mit zwei Teilen: unten flacher (119 mV je Dekade, Rekombinationsstrom mit $n$ = 2, $I_{SE}$ = 10⁻¹³ A), oben parallel zu $I_C$ im Abstand Faktor 100; der Abstand zwischen beiden Kurven als Pfeil „B“. (b) $B$ über $I_C$ (logarithmisch 1 nA bis 100 mA): 3 bei 1 nA, 9 bei 10 nA, 24 bei 100 nA, 50 bei 1 µA, 76 bei 10 µA, 91 bei 100 µA, Maximum 95 bei 0,85 mA, 83 bei 10 mA, 62 bei 30 mA, 33 bei 100 mA; gestrichelt der Modellwert 100.

*Kernaussage:* Die Stromverstärkung ist nur in der Mitte konstant: Bei kleinen Strömen frisst der Rekombinationsstrom der Raumladungszone den Basisstrom, bei großen die starke Injektion den Kollektorstrom.

*Daten:* Zahlenwerk G.

*Editor:*
- §4, §11; §12 halblogarithmisch (zwei Kurven, Abstand als Pfeil); §37 Steigungsdreieck auf logarithmischer Achse; §13 bzw. §10 Teilbilder.

*Animation:* keine.

**st1/bipolartransistor/01-grossignalmodell**
- Fassung: ausführlich Abb. 11.
- Status: offen.

*Inhalt:* (a) Vollständiges statisches Großsignalmodell: äußere Anschlüsse B′, E′, C′ über Bahnwiderstände $R_B$ = 100 Ω, $R_E$ = 5 Ω, $R_C$ = 20 Ω an die inneren Knoten B, E, C; innen die Emitterdiode $I_{B,N}$, parallel dazu die Rekombinationsdiode $I_{B,E}$ ($n$ = 2), die Kollektordiode $I_{B,I}$ und die Quelle $I_T$; dazu die Substratdiode vom Substrat S zum Kollektor, gesperrt. Werte bei 1 mA: Abfälle 1 mV an $R_B$, 5 mV an $R_E$, 20 mV an $R_C$. (b) Vereinfachtes Großsignalmodell: nur $R_B$ bleibt, Emitter und Kollektor direkt; Substratdiode bleibt.

*Kernaussage:* Zwischen den Anschlüssen und dem inneren Transistor liegen Bahnwiderstände; der Emitterwiderstand wirkt als Stromgegenkopplung, deshalb wird er technologisch klein gemacht, und nur der Basiswiderstand bleibt im Modell.

*Daten:* Zahlenwerk H.

*Editor:*
- §1 Dioden und Widerstände; §28 gesteuerte Quelle, Gegenüberstellung vollständig/vereinfacht; §10 Teilbilder.

*Animation:* Umschalten zwischen (a) und (b); Schieberegler $I_C$ zeigt die Spannungsabfälle (5 mV bei 1 mA, 50 mV bei 10 mA).

**st1/bipolartransistor/01-grundlagen**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2 (Grundlagen-Abschnitt nach §5.12, nachgerüstet 27.10.2026).
- Status: offen.

*Inhalt:* (a) pn-Übergang: Querschnitt p (rot) | Raumladungszone (grau) | n (blau), daneben die Diodenkennlinie mit $I_S$ = 10⁻¹⁶ A linear (0 bis 2 mA über 0,6 bis 0,8 V, 1 mA bei 774 mV) und halblogarithmisch (10 nA bis 10 mA, 59,5 mV je Dekade), Sperrbereich mit −10⁻¹⁶ A. (b) Elektronendichte in einer 0,1 µm dünnen p-Schicht: Gerade von einem hohen Wert links auf null rechts, blaue Pfeile bergab, Beschriftung „Strom ∝ Gefälle“. (c) Schaltzeichen der spannungsgesteuerten Stromquelle (Raute) mit Strompfeil $I$ und gestrichelter Zuordnung zu einer Spannung an anderer Stelle.

*Kernaussage:* Diode, Diffusion durch eine dünne Schicht und gesteuerte Quelle sind die drei Bausteine des Transistormodells.

*Daten:* Zahlenwerk A, B.

*Editor:*
- §27 Querschnitt; §4, §11, §12 Kennlinie linear und halblogarithmisch; §14 Teilchen, §2 Pfeile; §28 gesteuerte Quelle; §10 Teilbilder.

*Animation:* Schieberegler $U$ an der Diode: Kennlinienpunkt und Dichtegefälle in (b) laufen mit.

**st1/mos-feldeffekttransistoren/05-grundlagen-tangente**
- Fassung: kompakt Abb. 2, ausführlich Abb. 2 (Grundlagen-Abschnitt nach §5.12, nachgerüstet 27.10.2026).
- Status: offen.

*Inhalt:* (a) $I_D$ über $U_{GS}$ von 0,5 bis 1,5 V bei $U_{DS}$ = 1 V (0 bis 1,1 mA), Arbeitspunkt (1 V, 0,275 mA) rot, Tangente orange mit Steigungsdreieck 1,1 mS. (b) Ausschnitt 0,9 bis 1,1 V, 0,17 bis 0,40 mA: Kurve und Tangente fast deckungsgleich; Marken bei +10 mV (11,11 gegen 11,00 µA) und +100 mV (121 gegen 110 µA). (c) Raute der spannungsgesteuerten Stromquelle mit $g_m u_{GS}$, gestrichelte Zuordnung zu $u_{GS}$.

*Kernaussage:* Nahe am Arbeitspunkt ist die Kennlinie ihre Tangente, und die Steigung wird zum Strom einer gesteuerten Quelle.

*Daten:* Zahlenwerk AE, AG.

*Editor:*
- §4, §11; §37 Steigungsdreieck; §22 Ausschnittvergrößerung; §28 gesteuerte Quelle; §10 Teilbilder.

*Animation:* Zoomfaktor als Schieberegler: Je näher heran, desto gerader die Kurve.
