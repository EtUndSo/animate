# Richtlinien für die Durchsicht „Abbildungen und Animationen“ (09.11.2026)

Ziel: In allen deutschen Website-Artikeln festhalten, wo Abbildungen oder Animationen fehlen und welche es sein sollen.
Der User: „es kommt mir aktuell so vor als wäre die Anzahl sehr gering, vor allem die Anzahl der Animationen. Wir sollten
eigentlich versuchen immer Animationen für Grafiken zu nutzen und dann einen Button hinzufügen, um die Animation zu stoppen
und zu starten, dadurch können die Leser dann die ganze Animation sehen aber auch an Stellen stoppen die sie sich länger
angucken wollen.“ → **Animation ist der Normalfall.** Statisch nur, wenn Bewegung wirklich nichts bringt.
Den Abspiel-Knopf und die Technik baut ein anderer Agent; hier wird nur geplant, was gezeigt werden soll.

## Anzahl je Artikel (Vorgabe des Users)
- „Die Anzahl der Grafiken pro Artikel sollte längenabhängig sein, mit 5 als Maximum, 1 als Minimum.“
- Soll je Artikel steht in `SOLL_JE_ARTIKEL.md` (Spalte „Soll“; ≈ eine Abbildung je 450 Wörter, zugeklappte Kästen zählen halb).
  Vorhandene Abbildungen und Rechenbilder zählen mit.
- Artikel ohne Abbildung bekommen mindestens einen Vorschlag. Mehr als 5 vorhandene: sagen, welche entfallen oder
  zusammengelegt werden.
- Mehr Kandidaten als erlaubt: A vor B vor C. Was über das Soll hinausgeht, kommt nicht in die Liste (höchstens als
  einzeilige Notiz „verworfen: …“). Das Soll ist ein Richtwert: ±1 ist erlaubt, wenn begründet (z. B. ein Artikel mit
  drei Verfahren, die je ein Bild brauchen); nie unter 1, nie über 5.
- Kurze Übersichts- oder „Das Wichtigste“-Artikel: eine Zusammenschau-Abbildung oder eine vorhandene Szene des Hefts
  wiederverwenden (Art „vorhandene Szene wiederverwenden“).

## Regeln aus den Heft-Aufträgen (notizen/UEBERARBEITUNG.md §2, §2a, §3, §6)
- **Anschauung vor der Formel:** Jeder neu eingeführte Begriff bekommt ein Bild des Begriffs selbst (keine Anwendung,
  keine Schaltung), bevor die Definition kommt. Ein Begriff ohne Anschauung ist ein A-Kandidat.
- **Abbildungen zeigen den Begriff, nicht Dekoration.** Keine Bilder, die nur Text wiederholen.
- **Nur Editor-Szenen.** Keine Fotos, keine externen Bilder. Name `<modul>/k<N><name>`, N = Heftnummer
  (Ordnernummer, z. B. `ml/k3…` für ml/03-…; vorhandene Szenen liegen in `web/szenen/<modul>/`).
- **Rechenbilder (Σ, ∏, Skalarprodukt mit konkreten Zahlen):** Pflicht, wenn die Rechnung Kernstück eines Rechenbeispiels
  im Haupttext ist, auch in einem `::::beispiel`-Kasten. Keins in Beweisen, Herleitungen, Proben, Wiederholungen,
  Hintergrund-Kästen und Lösungen. Der User: „bei Beweisen, Rechnungen, etc. brauchen wir die Animationen nicht“.
  Allgemeine Formeln ohne Zahlen (Σ_j w_j x_j) bleiben Formeln. Fehlendes Pflicht-Rechenbild = A.
- **Keine Abbildungen in Lösungen, Beweisen, Herleitungen.** Hintergrund-Kästen nur ausnahmsweise (sind zugeklappt).
- **Theorie vor Praxis, keine Vorgriffe:** Ein Bild darf nichts zeigen, was der Leser an dieser Stelle noch nicht kennt.
- **Nichts doppelt:** Ist ein Begriff in einem anderen Modul vollständig erklärt (Grep in `notizen/themenkarte.md`, nicht
  ganz lesen) und hat er dort ein Bild, dann „Verweis auf <Szene>“ oder „Szene wiederverwenden“ statt neu zeichnen.
- **Sprache:** Bildtexte stehen später in sechs Sprachen; kurze Beschriftungen, Formelzeichen sprachfrei.

## Was besonders von Bewegung lebt (großzügig vorschlagen)
Verfahren und Algorithmen, Iterationen, Grenzprozesse, Transformationen, Felder, Wellen, Schaltvorgänge (Ein-/Ausschalten,
Laden/Entladen), Datenflüsse (Paket läuft durch ein Blockbild), Vektor-/Matrixoperationen, Zufallsexperimente,
Programmabläufe (Variablen ändern sich Zeile für Zeile), Energie-/Banddiagramme, die sich unter Spannung verbiegen.

## Prioritäten
- **A:** Begriff ohne Anschauung; Verfahren/Prozess/Algorithmus ohne Bild; Rechenbild-Regel verletzt; Artikel ohne Abbildung.
- **B:** deutlich hilfreich. **C:** nett.

## Form eines Vorschlags (fest)
```
### V<n> [A|B|C] <Kurztitel>
- **Artikel:** content/<modul>/<heft>/<datei>.md
- **Stelle:** <Überschrift> — „<erste Wörter des Absatzes> …“
- **Art:** neue Animation | bestehende Abbildung als Animation | neue statische Abbildung (nur wenn Bewegung nichts bringt) | vorhandene Szene wiederverwenden
- **Was zu sehen ist:** Objekte, Achsen (Bereiche), Beschriftungen, Zahlen
- **Ablauf:** 1. … 2. … n. … — Haltepunkte: <Schritte, an denen Leser voraussichtlich anhalten>
- **Verständnisproblem:** <welches>
- **Szenenname:** <modul>/k<N><name>
- **Editor-Lücke:** machbar | braucht Editor-Funktion: L<k> (<kurz>)   (Kürzel L1–L10 aus EDITOR_KANN.md; Neues als „L-neu: …“)
```

## Vorhandene Abbildungen
Für jede vorhandene `:::abbildung` eine Zeile: `- <szene> (<datei>): animieren ja/nein — Schritte: 1. … 2. … | Lücke: L<k>|machbar`.
Bei mehr als 5 in einem Artikel: welche entfallen oder zusammengelegt werden.

## Aufbau der Ergebnisdatei `notizen/abbildungen_audit/<modul>_<paket>.md`
1. Kopf: Paket, Hefte, Datum.
2. **Kurzbilanz-Tabelle je Artikel:** `| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |`
   (nachher = vorh. − entfällt + neu; muss 1–5 sein).
3. **Top 3** des Pakets: je eine Zeile `V<n> [A] <Artikel> — <was> — <warum wichtig>`.
4. **Editor-Lücken:** `L<k>: <Anzahl Vorschläge>` (und „L-neu: …“ mit Anzahl).
5. Vorschläge V1 … Vn, nach Artikel geordnet.
6. Vorhandene Abbildungen (eine Zeile je Szene).
