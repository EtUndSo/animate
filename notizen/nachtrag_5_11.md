# Nachtrag ERKLAER_PROMPT §5.11: „Kurz gesagt“ in den fertigen Stil-3-Themen (22.10.2026)

Vorgabe des Users vom 22.10.2026: Zusammenhänge zusätzlich in einem einfachen Satz angeben, nach dem Muster „Die
Transformation der Summe ist gleich der Summe der Transformationen“, nur wenn sie ohne Ausnahme stimmen, und auch an
anderen Stellen danach suchen. Diese Datei ist zugleich der Marker für LOOP_STIL3 (B1b): Solange sie fehlt, ist der
Nachtrag offen.

Vorgehen: Vier Agenten haben die zehn Themen aus ET1 Kap. 10 bis 12, je beide Fassungen, Formel für Formel durchsucht
und jeden Kandidaten am Zahlenwerk geprüft (Berichte im Scratchpad der Sitzung, `nachtrag_5_11/kap10a.md`, `kap10b.md`,
`kap11.md`, `kap12.md`). Jeder übernommene Satz ist danach von mir nachgerechnet. Im Hauptpfad stehen die Sätze als
eigene Zeile „**Kurz gesagt:**“ hinter „So liest man das“; in Herleitungskästen stehen sie ohne Etikett an dem Schritt,
der sie benutzt. Eingefügt mit `scratchpad/einfuegen_5_11.py` (Anker ohne Sonderzeichen gesucht, Zahlen mit U+202F).

## Übernommen (14 Sätze, 22 Stellen)

| Artikel | Stelle | Fassungen | Satz (gekürzt) | Probe |
|---|---|---|---|---|
| 10/01 Halbleiter und Bändermodell | Der pn-Übergang, nach der Definition von $U_T$ | beide | Im Gleichgewicht und mit Boltzmann-Verteilung addieren sich die Höhen hintereinanderliegender Potenzialstufen, die Dichtefaktoren multiplizieren sich | 2 · 59,5 mV ändern die Dichte um 10 · 10 = 100 |
| 10/01 | Herleitung $n_i(T)$, Temperaturgang | ausführlich | Logarithmus des Produkts = Summe der Logarithmen, Ableitung der Summe = Summe der Ableitungen | 0,50 % + 7,78 % = 8,28 % je K |
| 10/01 | Herleitung $U_\mathrm{Diff}$, zweiter Weg | ausführlich | Die Stufe ist die Summe der beiden Verschiebungen des Fermi-Niveaus aus dem Eigenleitungsniveau | 0,357 + 0,357 = 0,714 eV |
| 10/02 Diode und Kennlinie | Herleitung $\mathrm{d}U/\mathrm{d}T$, Schritt 2 | ausführlich | Produktregel in Worten | +2,15 − 4,28 = −2,13 mV/K bei 1 mA |
| 10/02 | Herleitung Glättungsfaktor, Schritt 1 | ausführlich | Die Änderung einer Summe ist die Summe der Änderungen; Knotenregel auch für Änderungen | 0,11 + 5,61 = 5,72 mA |
| 10/04 Gleichrichtung | Graetz-Brücke | beide | Bei vier gleichen Dioden ändert das Vertauschen der Quellenanschlüsse an der Last nichts | ±10 V ergeben beide 8,5986 V |
| 10/04 | Mittelwert | ausführlich | Ohne Ladekondensator sinkt der Mittelwert um weniger als $2U_{F0}$ | 6,3662 − 5,2121 = 1,154 V < 1,2 V |
| 11/01 Bipolartransistor | Transfergleichung | beide | Spannungsschritte addieren sich, ihre Stromfaktoren multiplizieren sich | 17,9 + 59,5 = 77,4 mV ergeben Faktor 2 · 10 = 20 |
| 11/02 Arbeitspunkt | Herleitung Stromgegenkopplung, Schritt 3 | beide | Im Basiskreis wirkt $R_E$ wie ein $(B + 1)$-mal so großer Widerstand | 1 kΩ wie 501 kΩ; 0,9944 mA |
| 11/03 Transistor als Verstärker | Kleinsignal-Ersatzschaltbild | beide | Die Wirkungen von $u_{be}$ und $u_{ce}$ überlagern sich, genau im Ersatzschaltbild, am echten Transistor näherungsweise | 77,36 + 2,67 = 80,03 µA (Modell 81,65 µA) |
| 12/01 idealer OPV | Ruhezustand | beide | Der nichtinvertierende Verstärker macht rückgängig, was sein Teiler tut: Verstärkung = Kehrwert des Rückkopplungsfaktors | $k$ = 0,1: 9,9995 → 10 |
| 12/02 Grundschaltungen | nichtinvertierender Verstärker | beide | dasselbe mit dem Anteil, den der Teiler zurückgibt | 1/3 → 3 |
| 12/02 | Addierer | beide | Antwort auf alle Eingänge = Summe der Antworten auf jeden allein | −5 V + (−1,25 V) = −6,25 V |
| 12/02 | Differenzierer | beide | Ein Differenzierer hinter einem Integrator mit demselben $RC$ macht ihn rückgängig, umgekehrt nur bis auf eine Konstante | −1 ms · (−1 V/ms) = +1 V |

## Geprüft und verworfen (Auswahl der Gründe)

Insgesamt 147 Kandidaten verworfen (Kap. 10a: 32, Kap. 10b: 44, Kap. 11: 34, Kap. 12: 37), dazu 10 Vorschläge der Agenten:
- **Doppelt** (häufigster Grund): „So liest man das“, der Satz vor der Formel oder „Woher die Faktoren kommen“ sagt schon dasselbe, z. B. Massenwirkungsgesetz („wird eine Sorte häufiger, wird die andere im selben Verhältnis seltener“), 59,5 mV je Dekade, Wurzelgesetz der Raumladungszone, Kettenschaltung („die Verstärkungen multiplizieren sich“), Verstärkungs-Bandbreite-Produkt, alle Formeln des realen OPV.
- **Nur näherungsweise:** „halbe Dotierung, doppelte Durchbruchspannung“ (206,3 statt 205,5 V), „zehnfache Rauschverstärkung, zehnfacher Fehler“, Klirrfaktor proportional zur Amplitude.
- **Falsche Muster** (als Gegenprobe vermerkt): Logarithmierer „Ausgang des Produkts = Summe der Ausgänge“ (−466,5 mV gegen −1052 mV); Exponentialschaltung „Summe am Eingang = Produkt der Ausgänge“ (Einheit V²); „Produkt der Ableitungen“ (falsche Einheit).
- **Von mir verworfene Vorschläge:** 10/01 Exponentialregel in der Shockley-Herleitung (dasselbe Gesetz wie die Potenzialstufen); 10/02 Höchstfeld = doppeltes mittleres Feld (die 2 erklärt der Kasten), Grenzwellenlänge ∝ 1/W_g (direkt ablesbar), Leerlaufspannung unabhängig von der Fläche (steht im Beispiel); 10/03 Prüfregel der Knickkennlinie (Verfahrenshinweis, kein Zusammenhang; steht im Probe-Schritt), Maschenregel am Arbeitspunkt (elementar), Kontraktionsfaktor der Iteration (steht in „So liest man das“); 11/01 $B = \alpha/(1-\alpha)$ als Anteile (steht im Kasten); 11/02 $P_\mathrm{max} \propto U_{CC}^2$ (Nebenresultat, erzwungen).

Die kompakten Vorlagen im Scratchpad sind seit diesem Nachtrag veraltet; maßgeblich sind die Dateien in `content/`.
