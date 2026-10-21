# Arbeitsnotiz: Halbleiter und das Bändermodell (ET1 Kap. 10.1–10.2), Stil 3

## 1. Ein-Satz-Prinzip
Ein Halbleiter hat wenige bewegliche Ladungsträger, deren Art und Zahl die Dotierung festlegt; wo ein n- und ein p-Gebiet aneinandergrenzen, baut der Dichteunterschied von selbst eine Barriere auf, deren Höhe eine äußere Spannung verschiebt.

## 2. Schwierigkeit und Längenspannen
Schwer: drei Bausteine (Bänder und Statistik, Dotierung, pn-Übergang) mit zwei Kipp-Stellen. Kompakt 1800–2800 Wörter Hauptpfad, ausführlich 3500–5000.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| Ladung, Elementarladung e, Strom als Ladungsfluss | erklärt in „Der elektrische Strom“ (verlinken) |
| Potenzial, Spannung, Energie eines Elektrons im Potenzial | erklärt in „Arbeit, Potenzial und Spannung“ (verlinken; Energie −e·φ hier in einem Satz) |
| elektrisches Feld, Kraft auf Ladungen | erklärt in „Das elektrische Feld und die Feldstärke“ (verlinken) |
| Drift im Leiter, Leitfähigkeit | erklärt in „Der ohmsche Widerstand“ (verlinken; σ = e·n·μ hier einführen) |
| Elektronenvolt | hier aufbauen (ein Satz) |
| Atom mit Elektronen auf diskreten Energien, Valenzelektronen | hier aufbauen (Schulchemie, zwei Sätze) |
| Wärmebewegung, thermische Energie k_B·T | hier aufbauen |
| Diffusion | hier aufbauen (ein Absatz) |
| Boltzmann-Verteilung | hier aufbauen (Analogie Atmosphäre, nur ausführlich als Kasten) |
| Exponentialfunktion, Logarithmus | Schulmathematik |

## 4. Fragenkatalog
| Nr. | Frage (Worte einer Person ohne Vorwissen) | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Alle Elektronen stecken in Bindungen. Woher kommen dann freie Elektronen?“ | Elektronen und Löcher | Text (K) | beide |
| 2 | „Warum leitet ein volles Band nicht, die Elektronen sind doch da?“ | Leiter, Halbleiter, Isolator | ausf.: Text; kompakt: Frage-Kasten | beide |
| 3 | „Ist ein Loch ein echtes Teilchen?“ | Löcher | Frage-Kasten | beide |
| 4 | Fehlvorstellung: „Ein n-dotierter Halbleiter ist negativ geladen.“ | Dotierung | Fehlvorstellung | beide |
| 5 | „Warum ist das fünfte Elektron so locker gebunden, wenn ein Wasserstoffatom 13,6 eV braucht?“ | Dotierung | Frage-Kasten | ausf. |
| 6 | „Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“ | Massenwirkungsgesetz | Frage-Kasten | beide |
| 7 | „Wie kann das Fermi-Niveau in der Bandlücke liegen, wenn es dort keine Zustände gibt?“ | Fermi-Niveau | Frage-Kasten | ausf. (kompakt: ein Satz im Text) |
| 8 | „Warum leitet Silizium warm besser, Kupfer aber schlechter?“ | Eigenleitung | Frage-Kasten | ausf. |
| 9 | Fehlvorstellung: „Die Atomrümpfe in der Raumladungszone sind doch neutral.“ | pn-Übergang | Fehlvorstellung | beide |
| 10 | „Warum hört die Diffusion nicht ganz auf, wenn die Barriere steht?“ | Zwei Ströme (K1) | Text (K) | beide |
| 11 | „Kann man die Diffusionsspannung mit einem Voltmeter messen?“ | pn-Übergang | Frage-Kasten | beide |
| 12 | Fehlvorstellung: „In Durchlassrichtung stößt der Pluspol die Löcher über die Barriere.“ | Durchlass (K2) | Fehlvorstellung | ausf. |
| 13 | Fehlvorstellung: „Unter 0,7 V fließt kein Strom.“ | Durchlass (K2) | Fehlvorstellung | beide |
| 14 | „Warum hängt der Sperrstrom nicht von der Sperrspannung ab?“ | Sperr (K2) | Text (K) | beide |

## 5. Kipp-Stellen
**K1 Zwei Ströme im Gleichgewicht** (warum die Barriere genau U_Diff hoch wird).
- **Schritte:** zwei Gruppen von Elektronen; Zufallsbewegung; hinauf (Erfolgsquote 10⁻¹²); hinunter (jedes); Gleichheit 10¹⁶·10⁻¹² = 10⁴.
- **Akteure:** n_n0, n_p0, U_Diff, U_T.
- **Abbildungen:** A12, A1c.
- **Zahl:** 10⁻¹².
- **Herleitung:** U_Diff aus Boltzmann (Zweiter Weg: J_n = 0).
- **Beispiel:** U_Diff der Beispieldiode mit Variation.
- **Analogie:** Atmosphäre (ausführlich).

**K2 Wirkung der äußeren Spannung.**
- **Schritte:**
  - Spannung fällt an der Zone ab (0,09 V/cm im neutralen Gebiet);
  - Barriere U_Diff − U;
  - hinauf mal exp(U/U_T);
  - hinunter unverändert;
  - Netto-Strom;
  - Sperr: hinauf bei −0,1 V nur noch 2 %, Rest I_S = 15 fA.
- **Akteure:** U, I_S.
- **Abbildungen:** A13, A14.
- **Zahlen:** Faktor 10 je 59,5 mV; 0,6 V → 0,18 mA.
- **Herleitung:** I = I_S·(exp(U/U_T) − 1).
- **Beispiel:** Ströme bei 0,4/0,6/0,7 V und −1 V.
- **Analogie:** Wasserfall (ausführlich).

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Einweggleichrichter als Motivation (Skript 10.1) | K | 2 Sätze in „Worum es geht“ | eigener kurzer Abschnitt mit A2 |
| diskrete Niveaus → Bänder, VB, LB, W_g | K | Text | Text |
| Valenzband exakt voll (Plätze = Valenzelektronen) | H | 1 Satz | Text |
| Niveauabstand 10⁻²² eV | V | – | 1 Satz |
| volles Band leitet nicht (Symmetrie, keine freien Plätze) | H | Frage-Kasten | Text |
| Leiter/Halbleiter/Isolator mit Zahlen | K | Text + A4 | Text + A4 + Tabelle |
| Elektronen und Löcher, Generation | K | Text | Text |
| Loch-Mechanismus, Ladung +e | K | Text, A5 | Text, A5, A6 |
| n_i = 10¹⁰, 5·10¹² Atome je Elektron | K | Text | Text |
| n_i-Formel mit N_L, N_V | V | – | Formel, Beweisidee (GEMB) |
| Massenwirkungsgesetz n·p = n_i² | K | Formel + Herleitung | Formel + Herleitung |
| Temperaturgang n_i (8,3 %/K) | H | 1 Satz | Text + A7 + Frage 8 |
| Fermi-Verteilung f(W), 50-%-Punkt | K (Skript nutzt W_F) | 2–3 Sätze | Abschnitt + A8 |
| W_i 7 meV unter der Mitte | V | – | 1 Satz |
| Donator, Akzeptor, Majorität, Minorität, feste Rümpfe | K | Text | Text |
| 99,6 % ionisiert, E_D = 45 meV | H | 1 Satz | Text |
| Wasserstoffmodell des Donators | V | – | in Frage 5 |
| Leitfähigkeit ×680 000 durch Dotierung | H | 1 Satz | Text |
| W_F-Verschiebung 0,357 eV | K (Skript Bild 10.5) | 1 Satz | Formel + Herleitung + A9 |
| Entstehung der RLZ, Feld, Selbstbegrenzung | K | Text + A10 | Text + A10 |
| U_Diff-Formel und Wert | K | Formel + Herleitung | Formel + Herleitung (2 Wege) |
| Profile (Weite 0,43 µm, Feld 3,2·10⁴ V/cm) | H | – | A11 mit Lesehilfe |
| U_Diff nicht messbar | H | Frage 11 | Frage 11 |
| zwei Ströme (K1) | K | Schritte (kurz) | Schritte + A12 + Tabelle |
| Durchlass/Sperr (K2) | K | Schritte + A13 + A14 | Schritte + A13 + A14 |
| Skriptkorrekturen „Durchlassspannung“, „Diffusionsstrom“ | K | ein Absatz | ein Absatz |
| Grenzen: starke Injektion ab ~0,65 V, Bahnwiderstand, Durchbruch | H | 1 Satz | Ausblick |
| Debye-Länge, dielektrische Relaxation, indirekter Halbleiter, RLZ-Weite-Formel | S | – | – (GEMB) |

## 7. Abbildungsplan
Bildnummern gelten für die ausführliche Fassung. Die kompakte nutzt A1, A4, A5, A10, A13 und A14 und zählt sie als Abb. 1 bis 6.

| Datei | Inhalt | Kernaussage | Abschnitt | kompakt |
|---|---|---|---|---|
| …-1 | Gesamtbild: Bänder (a) rein, (b) n und p, (c) pn-Übergang | wenige Träger, Dotierung verschiebt W_F, am Übergang Stufe e·U_Diff | Worum es geht | ja |
| …-2 | Einweggleichrichter: Schaltung, u_E(t), u_A(t) | nur positive Halbwellen, 0,7 V Verlust | Wozu | nein |
| …-3 | Leiter/Halbleiter/Isolator mit Besetzung | teilweise besetztes Band nötig; Lücke regelt Zahl | Leiter … | ja |
| …-4 | Gitter: rein, P, B (schematisch) | Bindungen, Donator, Akzeptor, feste Rümpfe | Elektronen und Löcher | ja |
| …-5 | Wanderung eines Lochs in drei Momenten | Lücke wandert mit dem Feld | Elektronen und Löcher | nein |
| …-6 | n_i(T) halblogarithmisch, Linie N_D | 8 %/K, erst bei 655 K gleich der Dotierung | Eigenleitung | nein |
| …-7 | Fermi-Verteilung linear und logarithmisch | 50-%-Punkt, Boltzmann-Schwanz | Fermi-Niveau | nein |
| …-8 | Bänder n- und p-Si mit W_D, W_A, W_F, W_i | W_F um 0,357 eV verschoben | Dotierung | nein |
| …-9 | Entstehung der RLZ in drei Zuständen | Diffusion legt Rümpfe frei, Feld begrenzt | pn-Übergang | ja |
| …-10 | Profile gestapelt (Poisson numerisch) | 0,43 µm, 3,2·10⁴ V/cm, 0,714 V | pn-Übergang | nein |
| …-11 | hinauf/hinunter im Banddiagramm | viele × winzig = wenige × eins | Zwei Ströme | nein |
| …-12 | Banddiagramme bei 0, +0,5 V, −2 V | nur die Barriere ändert sich | Durchlass/Sperr | ja |
| …-13 | Teilströme über U, logarithmisch | hinauf ×10 je 60 mV, hinunter konstant | Durchlass/Sperr | ja |

Damit hat die ausführliche Fassung 13 Abbildungen, die kompakte 6.

## 8. Zahlenwerk
`notizen/get1/zahlen_halbleiter.py` → `zahlen_halbleiter.txt`. Das Beispielsystem ist dasselbe wie im MiNa-Lernskript.

## 9. Profi-Abgleich
- **Altermatt et al. 2003:** n_i(300 K) = 9,65·10⁹ cm⁻³ statt 1,00·10¹⁰ (UNSW, https://unsworks.unsw.edu.au/entities/publication/2c330f15-ece8-4dfd-b035-ec5d867c1d8d/full; PVEducation, https://pveducation.org/es/fotovoltaica/intrinsic-carrier-concentration).
- **Ioffe-Datenbank Si:** W_g = 1,12 eV, N_C = 3,2·10¹⁹, N_V = 1,8·10¹⁹ cm⁻³, n_i = 1·10¹⁰ cm⁻³ (https://www-f9.ijs.si/~matevz/silikon/Semicond/Si/bandstr.html).
- **Phosphor-Donator:** 45,59 meV (Sci. Rep. 2017, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5519722/). Für den Bor-Akzeptor gilt nach Sze 45 meV.

## 10. Skript-Abgleich (GET1 WS 24/25, Seiten 159–161 = PDF 165–167)
**Inhalte:**
- Motivation mit Einweggleichrichter (Bild 10.1–10.3).
- Diskrete Niveaus, Bänder durch Kopplung, erlaubte und verbotene Bänder.
- Valenzband als oberstes bei 0 K besetztes Band, Leitungsband darüber.
- W_g als Mindestenergie; nur Leitungsband-Elektronen und Löcher leiten.
- W_F (bei 0 K der höchste besetzte Zustand), undotiert in der Mitte (Bild 10.4).
- Metall W_g = 0; Isolator große, Halbleiter kleine Lücke; Anregung durch Wärme, Licht und Spannung; Löcher.
- Dotierung: Si mit 4 Valenzelektronen, P (5) als Donator, W_D knapp unter LB, W_F nach oben (Bild 10.5); B (3) als Akzeptor.
- pn-Übergang: Diffusion, ionisierte Rümpfe, Feld, Potentialunterschied.
- Durchlass (p positiv): Feld wird geschwächt; Sperr: Feld wird verstärkt; Sättigungssperrstrom I_S.
- Fußnote zur Diffusion.

**Korrekturen:**
1. **S. 161 „Halbmetall Silizium“:** In der Festkörperphysik ist ein Halbmetall etwas anderes (überlappende Bänder, etwa Bismut). Silizium ist ein Halbleiter. In der Chemie heißt es Halbmetall im Sinn von Metalloid.
2. **S. 161 „kohärente Bindung“:** richtig ist „kovalente Bindung“.
3. **S. 161 Bor:** „bleibt ein Elektron beim Silizium-Atom übrig“. Gemeint ist: Einer Bindung fehlt ein Elektron. Ein Elektron aus einer Nachbarbindung füllt sie und hinterlässt dort ein Loch.
4. **S. 160 Fermi-Niveau „in der Mitte der Bandlücke definiert“:** Es ist nicht so definiert; seine Lage folgt aus n = p und liegt 7 meV unter der Mitte. „Bis zu dem Zustände besetzt sein können“ gilt nur bei T = 0. Allgemein ist W_F die Energie mit Besetzungswahrscheinlichkeit 1/2.
5. **S. 161 „das wieder den höchsten besetzten Zustand kennzeichnet“:** Das ist im dotierten Halbleiter bei T > 0 falsch. W_F liegt 0,21 eV unter W_L in der Lücke; besetzt sind Zustände darüber (Leitungsband) und darunter.
6. **S. 160 „Auch die Halbleiter gehören zu den Isolatoren“:** Keine Korrektur, nur eine Präzisierung. Im Bänderbild ist das die übliche Einteilung: Bei T = 0 sind Halbleiter Isolatoren mit kleiner Lücke. Bei 300 K hat reines Si aber ρ ≈ 3,4·10⁵ Ωcm und leitet um viele Zehnerpotenzen besser als SiO₂.
7. **S. 160 Anregung durch „elektrische Spannung“:** Gewöhnliche Spannungen erzeugen keine Ladungsträger, sie bewegen vorhandene. Paare durch Feld entstehen erst im Durchbruch (Zener, Lawine).
8. **S. 161 „Potentialunterschied … beschreibt die Durchlassspannung“:** Das ist die Diffusionsspannung U_Diff = 0,714 V. Sie ist nicht messbar und keine Kennlinienablesung.
9. **S. 161 „Überschreitet die angelegte Spannung die Durchlassspannung, so fließt ein Strom“:** Strom fließt bei jeder positiven Spannung und wächst exponentiell; bei 0,4 V sind es 76 nA.
10. **S. 161 „sehr kleiner Diffusionsstrom (Sättigungssperrstrom)“:** Keine Korrektur, das ist die übliche Bezeichnung. Die Größe von I_S bestimmt die Diffusion der Minoritätsträger in den neutralen Gebieten; über die Zone gelangen sie durch Drift. Der Artikel erklärt beides.
11. **S. 159 „nur positive Spannungen (Û_E > 0)“:** Û_E ist der Scheitelwert. Gemeint ist der Augenblickswert u_E(t) > 0, praktisch erst ab etwa 0,6 V.
12. **S. 162 (Folgeartikel):**
    - U_T = k_B·T/e, nicht „das Produkt k_B·T“.
    - Die Shockley-Gleichung im Skript fehlt das „−1“.

## 11. Unabhängige Faktenprüfung (21.10.2026, zweiter Agent)

**Fehler, behoben:**
- Elektronen gewinnen Geschwindigkeit gegen das Feld, nicht in Feldrichtung.
- Fermi-Niveau im p-Silizium liegt 0,19 eV über W_V, nicht 0,21 eV, weil N_V < N_L; Abbildungen 1 und 8 sind angepasst.
- Die Ausläufer der Fermi-Verteilung sind nicht gleich groß, nur N_L·f und N_V·(1−f) sind es.
- „680 000-fach“ gilt nur fürs n-Gebiet; das p-Gebiet leitet 240 000-fach besser, das Feld dort ist bei 0,6 V 0,24 V/cm.
- Die numerische Probe für U_Diff war zirkulär, weil die Randbedingungen den Wert enthalten; der Grenzfall „Dotierung gleich n_i“ war falsch.

**Ungenau, präzisiert:**
- Ionisationsgrad, begründet mit N_L ≫ N_D.
- Zustände in der Lücke beim dotierten Si (Donatorniveaus).
- Ursache der Löcherbeweglichkeit (wirksame Masse).
- Modellcharakter von R ∝ n·p (in Si über Störstellen); Grenze „nicht entartet“.
- Temperaturgang: 8,3 %/K gilt bei 300 K, bei 400 K sind es 4,7 %/K.
- Boltzmann-Ausläufer erst ab etwa 3 k_BT.
- Ideales Modell und reale Diode: Generationsstrom der Zone 53 pA bei −1 V statt 15 fA; Rekombination in der Zone.
- Gleichrichterbeispiel jenseits 0,65 V nur „im idealen Modell, rund 9,3 V“.
- Hinauf/hinunter von den örtlichen Drift- und Diffusionsströmen (4·10³ A/cm²) abgegrenzt.
- Shockley-Annahmen (ii) und (v) ergänzt.
- „Spannung in Durchlassrichtung“ statt „Durchlassspannung“.
- U_Diff indirekt messbar (Sperrschichtkapazität).
- Raumladung als zwei Rechtecke beschrieben.
- Kleinigkeiten: 0,7 % statt „drei Stellen“, Bose-Einstein-Hinweis, 31 meV aus der Effektivmassentheorie, Heißleiter „verwandter Effekt“.

**Folgefehler im Lernskript, dem Nutzer gemeldet:**
- k4/k5 nennt für die örtlichen Strömungsdichten „bis zu 8·10³ A/cm²“; das ist der Wert der Verarmungsnäherung, numerisch sind es 4·10³ A/cm².
