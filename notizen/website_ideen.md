# Ideen für die ganze Website EtUndSo (Konzept, 11.11.2026)

**Stand:** Vorschlag. Nichts davon ist beschlossen oder beauftragt.
**Anlass:** Der User am 11.11.2026: „Wir sollten einen Agenten starten, der überlegt, welche Features wir für die Webseite insgesamt noch einbauen könnten, also nicht nur auf den Editor bezogen, sondern die gesamte Webseite. Tools und Grafiken die dem Verständnis weiter helfen würden, bei jedem Artikel oben eine Box, die die wichtigsten Inhalte stichpunktartig zusammenfasst (für Leser, die nur kurz eine Info haben wollen), grafische Anpassungen um die Webseite ansehnlicher zu machen, etc.“
**Nicht hier:**
- Bildschirm- und Fensterbilder im Editor stehen in `notizen/editor_bildschirme_plan.md`.
- Fehlende Abbildungsarten L1 bis L10 stehen in `notizen/abbildungen_audit/UEBERSICHT.md`.
- Dieses Konzept verweist nur auf beide.

**Grenzen, die alle Vorschläge einhalten:**
- keine Umgebung, in der Leser Code ausführen;
- keine Herkunftsangaben;
- Design „Variante B“;
- kein Umschalter KI | Mensch, keine zwei Fassungen je Artikel;
- kein Tracking von Personen; der Rahmen ist die anonyme Zählung `/api/count`;
- alles funktioniert in sechs Sprachen;
- Inhalte entstehen möglichst automatisch aus den Heften.

**Herkunft des Inhalts:** Jeder Vorschlag sagt, woher sein Inhalt kommt. Dafür stehen drei Kürzel:
- **auto:** automatisch aus Heft oder Build;
- **einmal:** einmal von Hand, z. B. Oberflächenwörter in sechs Sprachen;
- **je Artikel:** je Artikel, Abbildung oder Aufgabe von Hand; das muss in fünf Sprachen übersetzt werden.

**Aufwand:** S bis etwa ein Tag Agentenarbeit, M einige Tage, L eine Woche und mehr.

---

## 1. Ergebnis in Kürze

**Die zehn besten Vorschläge, in dieser Reihenfolge:**

| Nr. | Vorschlag | Aufwand | Inhalt | Kernnutzen |
|---|---|---|---|---|
| 1 | Inhaltsverzeichnis aus den Unterabschnitten (B1) | S | auto | Fehlt heute in 91 % der Artikel. Die Orientierung kehrt sofort auf allen Seiten und in allen Sprachen zurück. |
| 2 | Schnell-Info „Auf einen Blick“ oben im Artikel (A1) | M | auto | Wunsch des Users. Die Box sammelt die „Kurz gesagt“-Sätze als Sprungliste, dazu neue Begriffe und Kennzahlen. |
| 3 | Lesbarkeit auf dem Handy (C1) | S–M | auto | Der Text bekommt rund 20 % mehr Breite, der Seitenkopf wird kürzer, Bilder lassen sich vergrößern. |
| 4 | Lesefortschritt nur im Browser (B3, mit B2) | S–M | auto | Häkchen „gelesen“, „Artikel 4 von 9“, „Weiterlesen“. Das gibt das Erfolgserlebnis, das der User für abgeschlossene Kapitel will. |
| 5 | Begriffe: Verzeichnis je Modul und Vorschaukarten an Links (A2, A3) | M | auto | Nachschlagen ohne den Lesefluss zu verlassen; Rückverweise werden sofort verständlich. |
| 6 | Lernkarten mit verteilter Wiederholung, lokal gespeichert (A4) | L | auto | Am besten belegter Lerneffekt: Abrufen und Verteilen. |
| 7 | Startseite und Wissensübersicht neu ordnen (C3, C4) | M | einmal + auto | Leser kommen schneller zu den Erklärungen. Die Startseite gibt es in sechs Sprachen, die Übersicht wird kürzer als heute 32 000 px. |
| 8 | Grundpaket Auffindbarkeit und Teilen (D1, D2) | S–M | auto | Sitemap, `canonical`, `x-default`, strukturierte Daten, Vorschaukarten. Titel und Beschreibungen ohne rohes TeX. |
| 9 | Rückmeldung „Hat das geholfen?“ und „Fehler melden“ (D8) | S–M | einmal | Zeigt anonym, wo Erklärungen hängen. Das ist der Nordstern der Seite. |
| 10 | Abbildungen mit Regler-Modus und Vorhersagefrage (A6) | M (+ je Szene) | auto + je Abbildung | Leser steuern einen Parameter selbst. Setzt L3 des Abbildungs-Audits voraus. |

**Schnelle Gewinne** (klein und sofort spürbar), Einzelheiten in Abschnitt 6.2:
- Inhaltsverzeichnis aus `###` (B1);
- Lesezeit, Zahl der Abbildungen und Aufgaben im Artikelkopf; `lesezeit()` gibt es schon, sie wird nur nicht angezeigt;
- `<title>` und Beschreibung ohne TeX-Reste;
- Knopf „Kopieren“ an Codeblöcken;
- Ankerlinks an Unterüberschriften;
- Druckansicht;
- Nachtmodus folgt beim ersten Besuch dem System;
- KaTeX selbst ausliefern;
- Standbild statt leerem Startbild bei Animationen;
- Abbildung antippen zum Vergrößern;
- 🚧 im Hinweisband durch Text ersetzen.

**Empfehlung zur Schnell-Info:**
- Die Box entsteht automatisch, ohne neuen Heft-Kasten. Ihr Inhalt:
  - „Worum es geht“;
  - die „Kurz gesagt“-Sätze als Liste mit Sprunglinks;
  - die neuen Begriffe;
  - eine Kennzahlenzeile.
- Wo zu wenige „Kurz gesagt“-Sätze stehen, zeigt sie die Kernformel aus dem Satz-Kasten und die Themenliste.
- Die Schreib-Agenten schreiben keine eigene Zusammenfassung. Sie halten aber jedes „Kurz gesagt“ selbsttragend.
- Einzelheiten und zwei Beispiele stehen in Abschnitt 4.

---

## 2. Bestandsaufnahme (Screenshots vom 11.11.2026)

Die Aufnahmen entstanden mit Playwright, am Desktop mit 1300 px und am Handy mit 390 px. Die Bilder liegen im Scratchpad, nicht im Repo (Pfad in Abschnitt 8). Angesehen wurden:
- die Startseite;
- `/wissen/`;
- ET3 „Pole und Nullstellen in der p-Ebene“;
- Linux 3 „Den Inhalt eines Verzeichnisses anzeigen“;
- Python 3 „Wiederholen mit while“;
- EN ET1 „Charging through a resistor“;
- der Nachtmodus;
- der Editor.

### 2.1 Was gut ist
- **Ruhige Typografie:**
  - Fließtext 17,5 px, Zeilenhöhe 1,72, Spaltenbreite 72ch (616 px);
  - Systemschriften, also keine Ladezeit für Schriften;
  - grüne Überschriften, die klar als Grün erkennbar sind.
- **Formeln:** Die Färbung (linke Seite grün, rechte Seite orange) macht Gleichungen lesbar. Die Gleichungsnummern stehen am Rand.
- **Kästen:**
  - Definitionen haben eine grüne Kante.
  - Beispiele, Hintergrund, Herleitungen und Lösungen sind zugeklappt.
  - Aufgaben haben einen grünen Kopf und Sterne für die Schwierigkeit.
  - Der Haupttext wirkt dadurch schlank.
- **Kopfleiste im Artikel:** Die Titel des vorherigen und nächsten Artikels stehen neben den Pfeilen; man weiß, was kommt.
- **Animationsspieler** (Linux):
  - Knöpfe für Start/Stopp, Neustart und Schritt;
  - Zeitleiste mit orangen Kapitelmarken;
  - Laden erst kurz vor dem Sichtbarwerden;
  - `prefers-reduced-motion` wird beachtet.
- **Nachtmodus:** sauber, mit hellen Kastenrahmen; die Formelfarben sind angepasst.
- **Abbildungen:** Alle haben Alternativtexte aus der Bildunterschrift; keine Abbildung ohne `alt` gefunden.
- **Klappkästen:** Beispiel, Vorwissen und Hintergrund sind echte `<details>`, also mit der Tastatur bedienbar.

### 2.2 Was stört (mit Befund)

| Befund | Wo | Wirkung |
|---|---|---|
| **Kein Inhaltsverzeichnis im Artikel.** Der Build sammelt nur `##`-Überschriften (`md_to_html`, `if lvl == 2`). Artikel aus Heften haben nur `###`. 686 von 753 deutschen Artikeln haben deshalb kein Verzeichnis „Im Artikel“, keine rechte Spalte „Auf dieser Seite“ (210 px bleiben leer) und keine Themenliste in den Nachbarkarten unten. | alle Module | Ein Artikel mit 8 Unterabschnitten und 3 000 Wörtern ist eine einzige lange Karte ohne Überblick. UEBERARBEITUNG §6a verspricht das Verzeichnis. |
| **Lesezeit fehlt.** `lesezeit()` wird nur noch für den abgeschafften Umschalter kompakt/ausführlich benutzt. | Artikelkopf | Leser wissen nicht, ob 3 oder 13 Minuten vor ihnen liegen (ET1-Artikel 3 min, Linux-Artikel 13 min). |
| **`:::quiz` gibt es im Build, aber in keinem Artikel.** | content | Funktion ohne Inhalt; kein Handlungsbedarf, aber gut zu wissen. |
| **Handy: Karte in Karte.** Artikelkarte und Kastenrand ergeben auf 390 px nur 290 px Textbreite (74 %). Die Brotkrumen brauchen 3 Zeilen, der Sprachknopf eine eigene Zeile vor dem Text. | alle Artikel, Handy | Erster Bildschirm fast ohne Inhalt; sehr kurze Zeilen. |
| **Animation beginnt mit fast leerem Bild.** Beim Hinscrollen zeigt Abb. 9 in Linux 3 zwei leere Rechtecke, der Inhalt kommt erst während des Ablaufs. | Szenen mit Aufbau | Wer schnell scrollt, sieht nichts und hält die Abbildung für kaputt. |
| **Terminalbilder auf dem Handy klein.** Das SVG skaliert auf ~310 px, Monospace-Text wird winzig; vergrößern geht nicht. | Linux, Python, Cyber | Gerade die Bilder, die man lesen muss, sind am schlechtesten lesbar. |
| **Titel mit rohem TeX:** `<title>Pole und Nullstellen in der $p$-Ebene — EtUndSo`. | Browser-Tab, Suchmaschinen, Lesezeichen | wirkt kaputt |
| **Beschreibung (`meta description`, Kartentext) = erster Satz von „Worum es geht“.** Der ist oft kontextabhängig: „In allen Beispielen war S(p) ein Bruch aus zwei Polynomen in p .“ | Suche, Suchmaschinen | sagt nichts über den Artikel |
| **Keine** `sitemap.xml`, `robots.txt`, `canonical`, `x-default`, Open-Graph-Tags oder strukturierte Daten. `SEO_AUFFINDBARKEIT.md` (19.10.) plant sie, umgesetzt ist nichts. | ganze Seite | schwächer auffindbar; geteilte Links ohne Vorschau |
| **Startseite nur deutsch** (`web/index.html`, kein `/en/`). Die Wissensseiten gibt es in sechs Sprachen. | Startseite | Englischsprachige Besucher landen auf Deutsch. |
| **Startseite stellt den Editor vor die Erklärungen:** zwei Knöpfe „Editor öffnen“, der Weg zu den Artikeln („Module ansehen“) ist zweitrangig. Der Text sagt „Elektrotechnik- und Mathematik-Module — und nebenbei ein paar andere Fächer“, obwohl Informatik inzwischen vier Reihen hat. | Startseite | Lernende finden den Hauptinhalt langsamer. |
| **`/wissen/` ist 32 000 px lang:** jede Artikelüberschrift aller Module untereinander. ET1 zeigt dort noch „Stufe 1 … Stufe 10“. | Übersicht | wenig Überblick; viel Scrollen |
| **Suchindex groß:** `search.json` (de) 8,4 MB, beim ersten Öffnen der Suche ganz geladen. Komprimiert dürfte die Übertragung bei grob 1,5 MB liegen, ungeprüft. | Suche, Handy | spürbare Wartezeit und viel Speicher auf schwachen Geräten |
| **KaTeX kommt von cdnjs** (Drittanbieter), je Artikel bis zu ~200 Formeln, im Browser gesetzt. | alle Artikel | zusätzlicher fremder Server; Formeln springen beim Laden |
| **Dateibudget:** `web/` enthält 14 843 Dateien, davon 5 245 Abbildungen. Cloudflare Pages erlaubt im Gratis-Tarif 20 000 Dateien je Site, bezahlt 100 000 (Changelog 23.01.2026). Allein die geplanten 1 237 Abbildungen × 6 Sprachen sprengen den Gratis-Rahmen. | Hosting | Betrifft jeden Vorschlag, der Dateien erzeugt (Vorschaubilder, PDFs). Siehe D2 und D5. |
| **Übersetzungsstand uneinheitlich:** Die englischen ET1-Artikel heißen noch „Stage 9“, die deutschen sind teils neu gegliedert. Der Leser sieht nicht, ob eine Übersetzung dem aktuellen Stand entspricht. | en/es/… | Vertrauen; siehe D7 |
| **Keine Druckansicht** (`@media print` fehlt), **kein Sprunglink „Zum Inhalt“**, **kein Kopierknopf** an Codeblöcken. | alle Artikel | klein, aber spürbar |
| **Editor wirkt wie eine andere Seite:** Titel „animate — Editor“, Knöpfe englisch („Save scene“), daneben deutsch („Ebenen“). Kein EtUndSo-Logo, kein Rückweg zu den Artikeln; der Ansichtswürfel hat eine lila Fläche. | Editor | Bruch im Erscheinungsbild; nur als Hinweis an den Editor-Plan, nicht Teil dieses Konzepts. |

### 2.3 Zahlen, auf die sich die Schnell-Info stützt
„Kurz gesagt“-Sätze je deutschem Artikel, gezählt am 11.11.2026 in `content/`:

| Modul | Artikel | 0 | 1 | 2–6 | 7 und mehr | mit Begriffen `__…__` |
|---|---:|---:|---:|---:|---:|---:|
| cyber | 12 | 2 | 0 | 6 | 4 | 10 |
| et1 | 131 | 116 | 15 | 0 | 0 | 110 |
| et3 | 90 | 75 | 9 | 2 | 4 | 61 |
| gemb1 | 162 | 160 | 2 | 0 | 0 | 127 |
| hm1 | 110 | 109 | 1 | 0 | 0 | 89 |
| hm3 | 83 | 74 | 0 | 2 | 7 | 66 |
| linux | 61 | 12 | 0 | 31 | 18 | 46 |
| ml | 73 | 11 | 0 | 54 | 8 | 62 |
| prog | 31 | 6 | 0 | 21 | 4 | 25 |
| **Summe** | **753** | **565** | **27** | **116** | **45** | **596** |

- Die Spalte 0 enthält auch die Artikel „Überblick“ und „Das Wichtigste“, die von sich aus keine „Kurz gesagt“-Sätze haben.
- In den überarbeiteten Heften (UEBERARBEITUNG §2: „Kurz gesagt“ je Begriff) und den Informatik-Reihen haben rund 80 % der Artikel genug Material.
- In ET1, GEMB1, HöMa1 und den alten Teilen von ET3 und HöMa3 fast keiner. Das ändert sich mit der geplanten Überarbeitung von selbst.
- Die Übersetzungen tragen feste Kennwörter: „In short:“, „En resumen:“, „En bref :“, „Kısacası:“, „简而言之：“. Ein Extraktor findet sie also in allen Sprachen.

---

## 3. Was gute Lernseiten und die Lernforschung nahelegen

Zusammengefasst aus drei Recherche-Berichten (Sonnet). Die Effektstärken sind Größenordnungen aus Übersichtsarbeiten. Ein Teil davon stammt aus dem Gedächtnis der Hilfsagenten, nicht aus abgerufenen Quellen. Vor einem Zitat auf der Website also gegenprüfen.

| Prinzip | Beleg (Größenordnung) | Folge für EtUndSo |
|---|---|---|
| **Abrufen statt Wiederlesen** | Roediger & Karpicke 2006; Adesope et al. 2017 (g ≈ 0,5–0,6); Dunlosky et al. 2013: „hoch nützlich“ | Aufgaben mit zugeklappten Lösungen sind richtig. Dazu Lernkarten (A4) und den Abdeck-Modus (A5), nichts zum bloßen Markieren. |
| **Verteiltes Wiederholen** | Cepeda et al. 2006/2008: Abstand ≈ 10–20 % der gewünschten Behaltensdauer | Lernkarten mit wachsenden Abständen, gespeichert nur im Browser (A4) |
| **Ausgearbeitete Beispiele, dann Ausblenden** | Sweller; Renkl & Atkinson 2003 (d ≈ 0,5–0,9 bei Anfängern) | Beispiele vor Aufgaben (ist so); später Aufgaben mit Teillösungen (A9) |
| **Expertise-Reversal** | Kalyuga et al. 2003: Hilfen für Anfänger stören Fortgeschrittene | Alles Zusätzliche zuklappbar, nie im Lesefluss (gilt für A1, A2, A3) |
| **Signale, Segmente, Vorab-Begriffe** (Mayer) | signaling d ≈ 0,4; segmenting und Lerntempo selbst steuern d ≈ 0,8 (Mayer & Pilegard, 10 von 10 Versuchen); pretraining d ≈ 0,7 | Inhaltsverzeichnis, klare Überschriften (B1); Animationen in Schritten mit Pause (vorhanden); Begriffe vorab (A1-Begriffszeile, A2) |
| **Kohärenz:** nichts Dekoratives | Mayer (d ≈ 0,9 beim Weglassen von Zierrat) | keine Schmuckbilder, keine Icons als Kastenmarker, keine Spielelemente |
| **Text und Bild zusammen** (dual coding, Multimedia-Prinzip) | Paivio; Mayer (d ≈ 1,0) | Editor-Abbildungen direkt am Text (vorhanden), am Handy vergrößerbar (C1) |
| **Vorstrukturierung oben** (advance organizer) | Luiten et al. 1980, Stone 1983: kleiner Effekt (d ≈ 0,2–0,3), größer bei schwierigem Stoff und Anfängern | Schnell-Info oben kurz halten; die ausführliche Zusammenfassung bleibt am Kapitelende („Das Wichtigste bis hier“). |
| **Vorab-Fragen** (pretesting) | Richland et al. 2009 (d ≈ 0,3–0,5), wirkt für genau die abgefragten Inhalte | billig, aber Inhalt je Artikel; nur als Option (A10) |
| **Lead-Absatz, Seitenvorschau** (Wikipedia) | WP:LEAD: der Lead fasst eigenständig zusammen und enthält nichts, was der Text nicht ausführt. Page Previews (A/B-Tests 2016–18): gezielteres Weiterklicken, Abschaltquote ≈ 0,01 % | A1 nach den Lead-Regeln; A3 Vorschaukarten |
| **Voraussetzungen und Ziele vorn** (MDN-Lernbereich) | Prerequisites/Objectives-Tabelle; „In this article“ rechts; Brotkrumen; Zurück/Weiter oben und unten | A1-Fußzeile, B1, B5 |
| **Anschauung vor Formel; Farbe als Code** (3Blue1Brown, Better Explained „ADEPT“ und „Colorized Equations“) | Didaktische Praxis, keine Messung | Gibt es schon (UEBERARBEITUNG §2, Formelfärbung). Farbe von Formel und Abbildung künftig gleich halten (A7). |
| **Interaktion nur mit Frage** (Bret Victor, Explorable Explanations; Mayer) | Für Interaktion ohne Aufgabe gibt es keine klaren Belege; Herumspielen ohne Ziel erhöht die Belastung. | Regler nur mit Vorhersagefrage (A6), 1–2 Parameter, Wert als Zahl sichtbar |
| **Barrierefreiheit von Bewegung** | WCAG 2.2.2 (Pause/Stopp), 2.3.3 (reduced motion), W3C „complex images“ (lange Beschreibung), ARIA-Slider-Muster | Spieler erfüllt 2.2.2 und 2.3.3 schon; dazu Tastatur, Standbild, Regler als `<input type="range">` (D4) |

---

## 4. Schnell-Info „Auf einen Blick“ (Wunsch des Users)

### 4.1 Ziel und Leser
Zwei Lesertypen besuchen dieselbe Seite:
- **Nachschlager** kommen über die Suche oder einen Link und wollen in 20 Sekunden wissen, was gilt.
- **Durchleser** gehen Kapitel für Kapitel.

Die Box dient den Nachschlagern, ohne die Durchleser zu stören. Daraus folgen drei Regeln:
1. kurz;
2. jeder Punkt springt an seine Stelle im Text;
3. zuklappbar.

### 4.2 Woraus die Box automatisch entsteht

| Teil | Quelle (auto) | heute vorhanden |
|---|---|---|
| Worum es geht | `:::zweck` (wie bisher, wandert in die Box) | in fast allen Artikeln |
| Das Wichtigste | alle „Kurz gesagt“-Sätze des Artikels, wörtlich, je mit Sprunglink auf seinen `###`-Abschnitt | 161 Artikel mit ≥ 2 Sätzen, nach der Überarbeitung alle |
| Neue Begriffe | `\fb` → `__…__` (der Konverter sammelt sie schon für `tags:`), Titel der `:::definition`- und `:::satz`-Kästen | 596 Artikel |
| Kernformel (nur Ersatzfall) | erste Formel im ersten `:::satz`-Kasten, sonst im ersten `:::definition`-Kasten | die meisten ET- und Mathe-Artikel |
| Kennzahlen | Lesezeit (`lesezeit()`), Zahl der Abbildungen und Aufgaben, Position im Kapitel, Link „Kapitel-Zusammenfassung“ auf den Artikel „Das Wichtigste bis hier“ | Build kennt alles |

**Auswahlregeln:**
- **Wie viele Punkte:** Bis 6 „Kurz gesagt“-Sätze erscheinen alle. Ab 7 erscheinen die ersten 5 und „N weitere zeigen“. Am Handy erscheinen die ersten 3.
- **Ersatzfall bei 0 oder 1 Satz:** „Worum es geht“, die Kernformel und die neuen Begriffe. Fehlt auch die Kernformel, steht dort die Themenliste aus den `###`-Überschriften.
- **Kurze Artikel ohne Box:** Unter 4 Minuten Lesezeit und ohne „Kurz gesagt“ bleibt es beim heutigen Kasten „Worum es geht“, um kein Vorgeplänkel zu erzeugen. Der User hat im Oktober drei Einstiege gestrichen, weil „so viel Vorgeplänkel liest niemand“.
- **Keine Box** auf den Artikeln „Das Wichtigste bis hier“, „Überblick“ und auf Aufgaben- und Lösungsseiten.

### 4.3 Beispiel ET: „Pole und Nullstellen in der p-Ebene“ (ET3, Kapitel 2)
Daten aus `content/et3/02-laplace-transformation/04-pole-und-nullstellen-in-der-ebene.md`: 8 „Kurz gesagt“, 2 Abbildungen, 2 Aufgaben, 8 min.

```
┌─ AUF EINEN BLICK ───────────────────────────────────────────────── [zuklappen ▴] ┐
│ Worum es geht: In allen Beispielen war S(p) ein Bruch aus zwei Polynomen in p.    │
│ Dieser Abschnitt zeigt, durch welche wenigen Zahlen ein solcher Bruch festgelegt  │
│ ist, wie man sie zeichnet, wo der Konvergenzbereich liegt und welche Rechenregeln │
│ die Transformation hat.                                                           │
│                                                                                   │
│ Das Wichtigste                                                                    │
│  • Nullstellen sind die Stellen, an denen S(p) verschwindet.        › Nullstellen │
│  • Ein Polynombruch ist durch seine Pole, seine Nullstellen und den Faktor H₀     │
│    vollständig bestimmt.                                          › Produktform   │
│  • Kreuze für Pole, Kreise für Nullstellen, dazu der Konvergenzbereich: Mehr      │
│    braucht man nicht, um ein Signal mit rationaler Transformierter zu             │
│    beschreiben.                                         › Pol-Nullstellen-Diagramm │
│  • Bei einem rechtsseitigen Signal liegt der Konvergenzbereich rechts aller Pole, │
│    bei einem linksseitigen links aller Pole, bei einem zweiseitigen in einem      │
│    Streifen zwischen ihnen.                             › Wo der Konvergenzbereich │
│  • Aus der Faltung im Zeitbereich wird im Bildbereich ein Produkt.   › Faltung    │
│    3 weitere zeigen ▾  (Ableiten, Integrieren, Dirac-Impuls)                      │
│                                                                                   │
│ Neu: Nullstelle · Pol-Nullstellen-Diagramm · Faltungssatz                         │
│ 8 min · 2 Abbildungen · 2 Aufgaben · Kapitel 2, Artikel 4 von 9 ·                 │
│ Kapitel-Zusammenfassung ›                                                         │
└───────────────────────────────────────────────────────────────────────────────────┘
```
- **Urteil:** Gut genug. Die Sätze sind selbsttragend und fachlich genau, die Sprunglinks machen die Box zum Inhaltsverzeichnis mit Aussage.
- **Schwäche 1:** „Worum es geht“ beginnt mit einem Rückbezug („In allen Beispielen …“). Für Nachschlager ist das der schwächste Satz der Box.
- **Schwäche 2:** Für ET-Nachschlager fehlt die Kernformel des Faltungssatzes, ℒ{s∗h} = S·H. Deshalb **Kernformel auch im Normalfall**, wenn der Artikel einen `:::satz` hat: höchstens eine Formel, klein gesetzt.

### 4.4 Beispiel Informatik: „Den Inhalt eines Verzeichnisses anzeigen“ (Linux, Kapitel 3)
Daten aus `content/linux/03-dateien-verzeichnisse-und-pfade/04-den-inhalt-eines-verzeichnisses-anzeigen.md`: 7 „Kurz gesagt“, 4 Abbildungen, 4 Aufgaben, 13 min.

```
┌─ AUF EINEN BLICK ───────────────────────────────────────────────── [zuklappen ▴] ┐
│ Worum es geht: ls ist der Befehl, den man an der Kommandozeile am häufigsten      │
│ tippt: Er zeigt, was in einem Verzeichnis liegt. Mit wenigen Optionen verrät er   │
│ auch versteckte Einträge, die Art jedes Eintrags, Größe und Alter. Dazu gehören   │
│ die Regeln, welche Namen eine Datei überhaupt haben darf.                         │
│                                                                                   │
│ Das Wichtigste                                                                    │
│  • `ls` listet die Einträge von Verzeichnissen auf; für eine gewöhnliche Datei    │
│    nennt es ihren Namen.                                             › Der Befehl │
│  • Ein Name mit Punkt am Anfang macht eine Datei unsichtbar für das gewöhnliche   │
│    `ls`; `ls -a` zeigt alles.                                › Versteckte Datei   │
│  • `ls -F` markiert Verzeichnisse mit `/` und Programme mit `*`.     › ls -F      │
│  • `ls -l` zeigt je Eintrag Art, Rechte, Besitzer, Gruppe, Größe, Änderungszeit   │
│    und Namen; `-d` zeigt das Verzeichnis selbst statt seines Inhalts.  › ls -l    │
│  • `ls -lh` schreibt Größen mit K, M, G zu je 1024 und rundet nach oben. › ls -h  │
│    2 weitere zeigen ▾  (Sortieren, Dateinamen)                                    │
│                                                                                   │
│ Neu: ls · versteckte Datei · gewöhnliche Datei · -F · -l · -h                     │
│ 13 min · 4 Abbildungen · 4 Aufgaben · Kapitel 3, Artikel 4 von 12 ·               │
│ Kapitel-Zusammenfassung ›                                                         │
└───────────────────────────────────────────────────────────────────────────────────┘
```
- **Urteil:** Sehr gut. Das ist fast ein Spickzettel, genau das, was ein Nachschlager sucht.
- **Wo es hakt:**
  - Die Begriffszeile mischt Begriffe und Optionen. Optionen (alles, was mit `-` beginnt oder in Code steht) als Code setzen und hinter die Begriffe stellen.
  - „Worum es geht“ ist hier selbst schon eine gute Kurzfassung. Bei so langen Zweck-Texten nur den ersten Satz zeigen, den Rest mit „mehr“.

### 4.5 Ersatzfall: ein alter ET1-Artikel („Strom und Spannung am Kondensator“, 3 min)
- **Material:** 0 „Kurz gesagt“, 1 Satz-Kasten, Begriff „Stromquelle“.
- **Ergebnis nach Regel 4.2:** Keine Box, weil der Artikel kürzer als 4 Minuten ist. Der Kasten „Worum es geht“ bleibt; die Kennzahlenzeile steht darunter.
- **Wäre der Artikel länger,** zeigte die Box die Kernformel aus Satz 3.1: i(t) = C · du(t)/dt.

Das ist ehrlich und nützlich, aber keine Zusammenfassung. Sie kommt mit der Überarbeitung von ET1 von selbst.

### 4.6 Konflikt mit „Keine Vorgriffe“ (Entscheidung des Users nötig)
- **Der Konflikt:**
  - UEBERARBEITUNG §4 verlangt: „Worum es geht“ am Anfang nennt keine Ergebnisse und keine Begriffe, die erst später erklärt werden.
  - Eine Zusammenfassung oben nennt genau das.
- **Vorschlag:**
  - Die Box ist ausdrücklich ein Nachschlage-Element außerhalb des Lesetexts. Der Haupttext bleibt frei von Vorgriffen.
  - Die Box ist ein `<details>`. Ihr Zustand wird im Browser gemerkt („Auf einen Blick immer zugeklappt“), ohne Übertragung.
- **Voreinstellung, Variante a (empfohlen):**
  - offen, wenn man von außen oder aus der Suche kommt;
  - zugeklappt, wenn man mit „Nächster Artikel“ aus dem vorigen Artikel desselben Kapitels kommt.
  - Das merkt sich ein Eintrag in `sessionStorage` beim Klick auf den Pfeil, kein Tracking.
  - So bekommt der Durchleser keinen Vorgriff, der Nachschlager sofort die Antwort.
- **Variante b:** immer offen.
- **Variante c:** immer zugeklappt, mit der Zeile „Auf einen Blick: 8 Kernaussagen ▸“.

### 4.7 Automatisch oder eigene Zusammenfassung im Heft?

| | Automatisch (empfohlen) | Eigene Box im Heft (`\begin{aufeinenblick}`) |
|---|---|---|
| Qualität | so gut wie die „Kurz gesagt“-Sätze; in den neuen Heften gut, in den alten leer | gezielt 3–5 Punkte, auch für Überblicksartikel |
| Aufwand neu | null | je Artikel einige Sätze beim Schreiben |
| Übersetzung | keine zusätzliche, die Sätze sind schon übersetzt | je Artikel in fünf Sprachen; bei neuen Heften gering, weil das ganze Heft ohnehin übersetzt wird |
| Bestand | wirkt sofort auf 161 Artikel und wächst mit der Überarbeitung | 753 Artikel × 6 Sprachen nachzurüsten |
| Doppelung | keine; dieselben Sätze, anderer Ort | doppelt die „Kurz gesagt“-Sätze; widerspricht „nichts doppeln“ |
| Gefahr | Box wird zu lang (bis 9 Sätze; daher Regel 4.2) | Box und Text laufen auseinander |

**Empfehlung:**
1. Automatisch bauen, mit den Regeln aus 4.2.
2. In UEBERARBEITUNG §2 eine Zeile ergänzen: Jedes „Kurz gesagt“ muss **ohne den Absatz davor verständlich** sein (kein „dies“, „dort“, „sie“ am Anfang), weil es auch in der Box steht.
3. Eine kleine Prüfung im Prüfwerkzeug: Sie warnt bei Artikeln mit mehr als 8 oder weniger als 2 „Kurz gesagt“ und bei „Kurz gesagt“ mit Fürwort am Anfang.
4. Optional, nur für Ausnahmen: ein Kurzbefehl `\aufeinenblick{…}` im Heft. Er ersetzt die automatische Liste, z. B. für Überblicksartikel. Im PDF erscheint er nicht.

### 4.8 Skizze im Rahmen von Variante B
```css
.kurzinfo{margin:.4em 0 1.8em;padding:14px 18px 12px;background:var(--soft);border:1px solid var(--rahmen);
  border-left:4px solid var(--accent);border-radius:12px;font-size:15.5px;line-height:1.55;}
.kurzinfo>summary{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);cursor:pointer;}
.kurzinfo ul{margin:.5em 0 .2em 1.1em;padding:0;} .kurzinfo li{margin:.28em 0;}
.kurzinfo .sprung{margin-left:.35em;font-size:13px;color:var(--muted);white-space:nowrap;}   /* „› Nullstellen“ */
.kurzinfo .kernformel{margin:.6em 0;font-size:.95em;}                                         /* höchstens eine Formel */
.kurzinfo .meta{display:flex;flex-wrap:wrap;gap:4px 14px;margin-top:10px;padding-top:8px;border-top:1px dashed var(--border);
  font-size:13.5px;color:var(--muted);}
@media(max-width:620px){ .kurzinfo{padding:12px 14px;margin-inline:-4px;} .kurzinfo li:nth-child(n+4){display:none;}
  .kurzinfo.alle li{display:list-item;} }
```
- **Farben:** nur Grün, Neutral und die vorhandenen Variablen; nachts übernimmt `--rahmen` den hellen Rand.
- **Kennzeichen:** kein Symbol, keine Emojis (Regel „kein KI-Look“).
- **Abgrenzung:** Der Kasten „Worum es geht“ (`.zweck`) geht in der Box auf. Es bleibt also bei einem Einstieg, nicht zwei.
- **Oberflächenwörter (einmal):**
  - „Auf einen Blick“, „Das Wichtigste“, „Neu“, „weitere zeigen“, „Kapitel-Zusammenfassung“;
  - in sechs Sprachen, z. B. en „At a glance“, fr „L’essentiel“; nicht „En bref“, das ist dort schon „Kurz gesagt“.

**Betroffene Dateien:**
- `build_wissen.py`: `render_article`, neue Funktion `kurzinfo(art, toc)`, `UI`, `WISSEN_CSS`, `WISSEN_JS` für Zuklappen und Merken;
- optional `tools/heft_zu_artikel.py` für `\aufeinenblick`;
- das Prüfwerkzeug unter `tools/`;
- `notizen/UEBERARBEITUNG.md` (eine Zeile).

**Bewertung:**
- Nutzen hoch für Nachschlager, klein bis mittel für Durchleser (advance organizer, signaling).
- Aufwand M, Inhalt auto, keine Übersetzung außer einmal den Oberflächenwörtern.
- Risiko: Länge. Abhilfe sind die Regeln in 4.2.

---

## 5. Vorschläge nach Feldern

Jeder Vorschlag hat eine Kennung. Die Bewertung steht als Tabelle am Ende jedes Felds.

### 5.1 Verständnis-Werkzeuge und Grafiken

**A1 Schnell-Info „Auf einen Blick“:** siehe Abschnitt 4.

**A2 Begriffsverzeichnis je Modul und Begriffskarten**
- **Begriffsverzeichnis „Begriffe A–Z“ je Modul und Sprache:**
  - Es entsteht aus `:::definition … (Begriff)` und den `\fb`-Begriffen.
  - Je Begriff: der erste Satz der Definition und ein Link auf die Stelle.
- **Suche:** Sie zeigt Begriffstreffer zuerst, als „Definition: Nullstelle (ET3, Kapitel 2)“.
- **Stufe 2, Karten an späteren Nennungen:** Ein Begriff wird an einer späteren Nennung zu einer Karte (antippen oder mit der Maus darüber), mit Definitionssatz und Link. Dafür gelten Regeln:
  - nur Begriffe, deren Definition in einem **früheren** Artikel steht (`order` kleiner); so bleibt „Keine Vorgriffe“ gewahrt;
  - nur die erste Nennung je Artikel (Hypertext-Überlast vermeiden);
  - nicht in Überschriften, Definitionen und Formeln.
- **Grenze der Stufe 2:** Wörter automatisch wiederzuerkennen ist im Deutschen (Beugung), Türkischen (Endungen) und Chinesischen (keine Wortgrenzen) unsicher.
  - Deshalb zuerst nur das Verzeichnis, die Suche und A3.
  - Stufe 2 nur für de/en/es/fr mit exakter Grundform plus Mehrzahl, oder später mit einem Heft-Kurzbefehl für spätere Nennungen (`\fbr{…}`, je Artikel von Hand).

**A3 Vorschaukarten an internen Links**
- **Was:** Rückverweise wie „Kapitel 2, Abschnitt 3.1“ und alle internen Links zeigen eine kleine Karte:
  - den Titel des Ziels;
  - dessen „Kurz gesagt“, sonst den ersten Satz von „Worum es geht“.
- **Bedienung:**
  - Am Desktop nach kurzer Verzögerung beim Darüberfahren oder beim Tastaturfokus.
  - Am Handy beim ersten Antippen, mit dem Knopf „Öffnen“.
- **Daten:** Der Build schreibt die Vorschautexte der in der Seite vorkommenden Links in ein `<template>` am Seitenende. Kein zusätzlicher Abruf, kleine Datenmenge.
- **Beleg:** Wikipedia Page Previews, siehe Abschnitt 3.

**A4 Lernkarten mit verteilter Wiederholung** (lokal, ohne Konto)
- **Karten, automatisch aus dem Heft:**
  - Definition: Vorderseite „Was ist eine versteckte Datei?“ bzw. der Begriff, Rückseite der Definitionstext;
  - Satz: Vorderseite „Faltungssatz“, Rückseite die Aussage;
  - „Kurz gesagt“: Vorderseite der Abschnittstitel als Frage, Rückseite der Satz;
  - optional die Punkte von „Das Wichtigste bis hier“.
- **Ablauf:**
  - Leitner mit Abständen 0/1/3/7/16/40 Tage. Die Lernkartei-App in `C:\Bücher\Lernkartei` hat das Muster schon erprobt.
  - Speichern in `localStorage`, Export und Import als Datei.
  - Am Artikel: „Karten dieses Kapitels lernen“.
  - Auf der Startseite: „12 Karten fällig“, nur lokal berechnet.
- **Beleg:** der stärkste Lerneffekt der Liste (Abrufen + Verteilen).
- **Risiken:**
  - Karten, die ohne Zusammenhang unverständlich sind (Definition mit „sie“ oder „wie oben“). Abhilfe: Prüfwerkzeug, Karten mit Rückbezug aussortieren.
  - KaTeX auf Karten ist nötig.
  - Kein Spielkram: keine Punkte, keine Serien, keine Abzeichen.
  - Die Daten hängen am Gerät; Export und Import mildern das.

**A5 Abdeck-Modus im Artikel** (Selbsttest)
- **Was:** Ein Schalter im Artikelkopf deckt die „Kurz gesagt“-Sätze, die Definitionstexte und die Punkte in „Das Wichtigste bis hier“ ab.
  - Der Leser formuliert zuerst selbst und deckt dann mit einem Tipp auf.
  - Das ist die Hand über der Buchseite, als Funktion.
- **Inhalt:** auto, keine Übersetzung außer drei Oberflächenwörtern.
- **Abgrenzung zu A4:** A5 ist der kleine, sofort nutzbare Schritt zum Abrufen; A4 bringt das Verteilen über Tage dazu.

**A6 Abbildungen mit Regler-Modus und Vorhersagefrage**
- **Regler-Modus:**
  - Der Spieler hat schon eine Zeitleiste. Läuft in einer Szene ein Parameter von a nach b (L3 im Abbildungs-Audit, ValueTracker), zeigt die Zeitleiste statt Sekunden den Wert, z. B. „R = 2,2 kΩ“.
  - Ziehen am Regler stellt den Parameter ein. Das ist ein Schieberegler ohne neuen Renderweg und ohne Codeausführung.
  - Bedienung als `<input type="range">` mit Beschriftung: Pfeiltasten, Pos1 und Ende gehen dann von selbst.
- **Vorhersagefrage (optional):**
  - Eine Zeile in der Abbildung, z. B. `\vorhersage{Was passiert mit dem Pol, wenn R verdoppelt wird?}`, je Abbildung von Hand.
  - Erscheint vor dem ersten Abspielen. Erst nach „Abspielen“ läuft die Antwort.
- **Beleg:** Lerntempo selbst steuern (Mayer); Interaktion nur mit Frage (Victor). 1–2 Parameter, Wert als Zahl sichtbar.
- **Abhängigkeit:** L3 („Parameter über die Zeit“, `UEBERSICHT.md` §7 Schritt 5). Ohne L3 nur für vorhandene Zeitabläufe.

**A7 Formeln mit erklärten Symbolen**
- **Wo Farben schon gleich sind,** bleiben sie gleich: Symbol in Formel und Abbildung in derselben Farbe (Better Explained „Colorized Equations“).
- **Zur Seite:** Eine Symbol-Legende unter **Kernformeln** in Satz-Kästen.
  - Im Heft als `\symbole{H_0/Faktor der höchsten Koeffizienten; p_{N,q}/Nullstellen}`, je Formel von Hand.
  - Nur in neuen Heften, nur für die eine Kernformel je Abschnitt.
- **Nicht empfohlen:** automatisches Hervorheben gleicher Symbole quer durch den Artikel. Teuer, fehleranfällig, kleiner Nutzen.

**A8 Rechenhelfer** (ohne Codeausführung)
- **Wenige, fest gebaute Werkzeuge,** jedes aus den Artikeln verlinkt, wo es gebraucht wird:
  - **Linux:** Rechte-Rechner `chmod`, also Oktal ↔ `rwx` ↔ Häkchen. Passt zu Linux 7.
  - **Informatik:** Zahlensysteme und Bitmasken (dezimal/binär/hex, AND/OR/XOR, Zweierkomplement).
  - **ET und Mathe:** komplexe Zahl kartesisch ↔ polar mit Zeigerbild; SI-Vorsilben und Einheiten.
  - **ET3:** Pol-Nullstellen-Spielwiese. Pole ziehen, Sprungantwort sehen. Erst nach L3 und A6 prüfen, ob A6 dasselbe leistet.
- **Kein Regex-Tester:** Er würde Eingaben der Leser als Muster ausführen, und das ist zu nah an einer Ausführungsumgebung.
- **Beleg:** keiner direkt; Nutzen als Werkzeug beim Üben.
- **Risiko:**
  - Jedes Werkzeug muss exakt rechnen und gepflegt werden. Daher höchstens drei, mit Tests.
  - Ein Werkzeug-Zoo ist nicht das Ziel.

**A9 Ergebnis prüfen bei Zahlenaufgaben**
- **Was:** Aufgaben mit Zahlenergebnis bekommen ein Eingabefeld „Dein Ergebnis“ mit sofortiger Rückmeldung, mit Toleranz und Einheit.
  - Im Heft `\ergebnis{0.9}{mA}{2\%}` in der Aufgabe, je Aufgabe von Hand.
  - Zahlen und Einheiten müssen nicht übersetzt werden.
- **Beleg:** Abrufen mit Rückmeldung.
- **Grenze:** nur Zahlenaufgaben; der Lösungsweg bleibt im zugeklappten Kasten.

**A10 Vorab-Frage je Abschnitt:**
- **Was:** eine Frage vor dem Abschnitt („Was vermutest du …?“), aufklappbar beantwortet.
- **Beleg:** pretesting (Richland 2009).
- **Kosten:** Inhalt je Artikel von Hand und in fünf Sprachen; widerspricht leicht „keine Vorgriffe“. Nur als Option für neue Hefte.

| Kennung | Nutzen fürs Verständnis | Aufwand | Inhalt | Übersetzung / Bestand | Risiken | Dateien |
|---|---|---|---|---|---|---|
| A1 | hoch für Nachschlager | M | auto | keine / sofort 161 Artikel, wächst | Länge, Vorgriff (4.6) | `build_wissen.py`, Prüfwerkzeug |
| A2 | mittel–hoch (pretraining, Nachschlagen) | M (Verzeichnis S) | auto | keine / alle Module | Wiedererkennung in tr/zh | `build_wissen.py`, `heft_zu_artikel.py` (Begriffe mit Anker ausgeben) |
| A3 | mittel (weniger Kontextwechsel) | S–M | auto | keine / sofort alle | Überladung bei vielen Links; Abhilfe: Verzögerung, nur interne Links | `build_wissen.py`, `WISSEN_JS` |
| A4 | sehr hoch (beste Belege) | L | auto | Oberflächenwörter einmal / alle Module | Kartenqualität; Daten am Gerät | neues `web/wissen/lernen.html`, Karten-JSON je Sprache aus dem Build |
| A5 | hoch (Abrufen), sehr billig | S–M | auto | keine / sofort alle | wirkt nur, wenn man es nutzt | `WISSEN_JS`, `WISSEN_CSS` |
| A6 | hoch bei Prozessen und Parametern | M + je Szene | auto + je Abbildung (Frage) | Frage je Abbildung übersetzen / nur neue Szenen | hängt an L3 | Spieler in `wissen.js`, Szenen-Export, `szenen_lib.py` |
| A7 | mittel | S je Formel | je Artikel | ja / nur neue Hefte | Mehraufwand beim Schreiben | `heft_zu_artikel.py`, Präambeln |
| A8 | mittel, beim Üben | M je Werkzeug | einmal | wenige Wörter / – | Korrektheit, Pflege | neue Seiten unter `web/werkzeuge/` |
| A9 | mittel–hoch (Rückmeldung) | M | je Aufgabe | keine (Zahlen) / nachrüstbar | falsche Musterlösung wird sichtbar; Toleranzen | `heft_zu_artikel.py`, `build_wissen.py` |
| A10 | mittel | S je Artikel | je Artikel | ja | Vorgriff | Hefte |

### 5.2 Orientierung und Navigation

**B1 Inhaltsverzeichnis aus den Unterabschnitten**
- **Was:** Hat ein Artikel keine `##`, nimmt der Build die `###` als Ebene des Verzeichnisses. Dann erscheinen von selbst:
  - das Verzeichnis „Im Artikel“ oben, oder in der Schnell-Info über die Sprunglinks;
  - die rechte Spalte „Auf dieser Seite“ mit Markierung des aktuellen Abschnitts (`.toc a.active` ist im CSS schon vorhanden);
  - die Themenlisten in den Nachbarkarten unten.
- **Abschnittskarten:** Auf Wunsch dazu die Abschnitte als einzelne Karten, so wie bei `##`. Das gliedert die langen Linux- und ML-Artikel sichtbar.
- **Doppelung vermeiden:** Hat ein Artikel die Schnell-Info mit Sprunglinks, entfällt das obere Verzeichnis „Im Artikel“; die rechte Spalte bleibt.
- **Aufwand:** S, auto, wirkt sofort auf 686 Artikel in allen Sprachen.
- **Datei:** `build_wissen.py` (`md_to_html`, `render_article`, `_topics`).

**B2 Position im Kapitel**
- **Was:** Unter den Brotkrumen steht „Kapitel 3 · Artikel 4 von 12“ mit einer schmalen Punktleiste. Ein Punkt je Artikel, der aktuelle ist grün, gelesene haben einen Haken (B3).
- **Inhalt:** auto. Aufwand S.

**B3 Lesefortschritt nur im Browser**
- **Häkchen „gelesen“:** Ein Artikel wird automatisch abgehakt, wenn das Ende des Haupttexts sichtbar war, oder von Hand mit dem Knopf „Als gelesen markieren“.
- **Wo das sichtbar wird:**
  - Häkchen im Themenbaum;
  - „7/12“ an Kapiteln in der Wissensübersicht;
  - „Weiterlesen: Linux, Kapitel 3, Dateien ansehen“ auf Startseite und Übersicht.
- **Speicher:** `localStorage`, nichts wird übertragen. In der Datenschutzerklärung ein Satz dazu.
- **Begründung:** Der User am 02.11.2026: Kapitel abzuschließen gibt „ein Erfolgserlebnis“. Khan Academy und Brilliant zeigen Fortschritt, brauchen dafür aber ein Konto. Hier genügt der Browser.
- **Aufwand:** S–M, auto.
- **Risiko:** Mehrere Geräte sehen verschiedene Stände. Akzeptabel; Export/Import wie bei A4.

**B4 Kürzere Brotkrumen**
- **Kurzname:** Der Modulname erscheint als „ET3“, der volle Name als `title`.
- **Handy:** nur die letzten zwei Glieder („ET3 › Kapitel 2: Laplace-Transformation“). Das spart am Handy zwei Zeilen.
- **Aufwand:** S, auto.

**B5 Voraussetzungen und Lernpfade**
- **Je Kapitel automatisch:**
  - „Baut auf: Python, Kapitel 1–2; Grundlagen, Kapitel 1“ aus den Kapitel-Verweisen im Heft (die Wendungen aus `themenkarte.md` werden schon zu Links);
  - umgekehrt „Wird gebraucht in: …“.
  - Beides steht im ersten Artikel des Kapitels und in der Wissensübersicht.
- **Je Bereich eine Lernpfad-Seite:**
  - Inhalt: die empfohlene Reihenfolge der Reihen, z. B. Informatik: Python → Linux → Cybersecurity / Machine Learning, mit den Querbezügen.
  - Herkunft: aus `MODULE` und den Lernpfad-Notizen, die Einleitung einmal von Hand.
- **Als Liste, nicht als Netzgrafik:** Netzgrafiken mit vielen Knoten werden schnell unlesbar. Eine schlichte Stufenleiste je Bereich genügt.
- **Aufwand:** M.

**B6 Suche verbessern**
- **Trefferliste:** Begriffstreffer zuerst (A2). Als Ausschnitt dient das passende „Kurz gesagt“, Filter nach Bereich (ET, Mathe, Informatik).
- **Index teilen:** Titel, Begriffe und „Kurz gesagt“ sofort laden, wohl einige 100 kB; den Volltext erst bei Bedarf.
- **Aufwand:** M, auto.

**B7 Ankerlinks an Unterüberschriften**
- **Was:** Beim Darüberfahren erscheint „#“; Klick kopiert den Link auf den Abschnitt, zum Teilen einer Stelle.
- **Aufwand:** S, auto.

| Kennung | Nutzen | Aufwand | Inhalt | Übersetzung / Bestand | Risiken | Dateien |
|---|---|---|---|---|---|---|
| B1 | hoch (signaling, Orientierung) | S | auto | keine / sofort 686 Artikel | keine nennenswerten | `build_wissen.py` |
| B2 | mittel | S | auto | Wörter einmal / alle | – | `build_wissen.py`, CSS |
| B3 | mittel–hoch (Motivation, Wiedereinstieg) | S–M | auto | Wörter einmal / alle | Gerätebindung; Hinweis im Datenschutz | `WISSEN_JS`, `web/index.html`, `datenschutz.html` |
| B4 | mittel (Handy) | S | auto | – | – | `build_wissen.py` |
| B5 | mittel–hoch für Selbstlerner | M | auto + einmal | Einleitung einmal je Bereich | Querverweise unvollständig | `build_wissen.py`, `heft_zu_artikel.py` |
| B6 | mittel | M | auto | – | – | `build_wissen.py`, `WISSEN_JS` |
| B7 | klein | S | auto | – | – | `build_wissen.py`, CSS |

### 5.3 Optik

**C1 Lesbarkeit auf dem Handy** (bis 620 px)
- **Karte in Karte auflösen:** Die Abschnittskarte verliert Rand, Schatten und Innenabstand; Kästen behalten ihren Rahmen. Die Textbreite steigt von 290 auf etwa 350 px. Als Skizze:
  ```css
  @media(max-width:620px){
    .sect{border:0;box-shadow:none;background:transparent;padding:0;}
    .callout,.zweck,details.beispiel,details.hintergrund,details.vorwissen{padding:12px 14px;}
    .article{padding:16px 16px 56px;}
  }
  ```
  Die genauen Klassennamen sind beim Bau zu prüfen.
- **Kopf straffen:** Der Sprachknopf zieht in die Kopfleiste, als Menüeintrag hinter dem Logo oder als kleines „DE“ neben „Suchen“. Dazu B4.
- **Abbildung vergrößern:** Antippen öffnet die Abbildung bildschirmfüllend, mit Zoom durch Spreizen und mit Spieler.
  - Das hilft besonders bei Terminal- und Codebildern.
  - Am Desktop ebenso, für große Schaltbilder.
- **Aufwand:** S–M, auto.

**C2 Artikelkopf**
- **Reihenfolge:** Brotkrumen, Titel, dann eine Zeile „8 min · 2 Abbildungen · 2 Aufgaben · Stand 03.11.2026“, dann die Schnell-Info.
- **Schildchen „KI-generiert“:** bleibt (Transparenz), aber in die Kennzahlenzeile statt neben die Brotkrumen.
- **Aufwand:** S.

**C3 Startseite**
- **Hauptknopf „Zu den Erklärungen“** und ein Suchfeld im oberen Teil; „Editor öffnen“ wird der zweite Knopf.
- **Darunter drei Bereichskarten:** Elektrotechnik, Mathematik, Informatik. Je Karte:
  - die Reihen;
  - die Zahl der Kapitel;
  - „Hier anfangen“;
  - mit B3 „Weiterlesen“.
- **„Neu auf EtUndSo“:** die letzten fünf neuen oder überarbeiteten Kapitel, automatisch aus dem Build.
- **Startseite in sechs Sprachen:** `/en/` usw. Die Texte einmal übersetzen, rund 30 Sätze. Dazu `hreflang` und die Sprachwahl wie im Wissensbereich.
- **Kopfzeile:** „Elektrotechnik und So“ bleibt als Marke. Die Unterzeile nennt Mathematik und Informatik gleichrangig, statt „nebenbei ein paar andere Fächer“.
- **Hinweisband:** 🚧 entfernen (Regel: keine Emojis als Marker); der Text genügt.
- **Aufwand:** M; einmal + auto.

**C4 Wissensübersicht `/wissen/`**
- **Statt aller Artikeltitel:** Bereichs- und Modulkarten, darunter die Kapitel zugeklappt. Je Kapitel:
  - Zahl der Artikel;
  - Summe der Lesezeit;
  - Fortschritt (B3).
- **Die Artikelliste** öffnet sich erst beim Aufklappen. Die Seite schrumpft von 32 000 px auf wenige Bildschirmhöhen.
- **Aufwand:** M, auto.

**C5 Abbildungen**
- **Standbild:** Bis zum Start zeigt die Animation ihr Endbild, kein leeres Anfangsbild; bei `prefers-reduced-motion` ebenso.
- **Knopf zum Editor:** „Szene im Editor öffnen“ wird ein kleiner Textlink in der Bildunterschrift statt eines umrandeten Knopfs. Das macht die Abbildung ruhiger.
- **Aufwand:** S.

**C6 Nachtmodus**
- **Was:** Beim ersten Besuch folgt die Seite `prefers-color-scheme`. Danach gilt die Wahl des Lesers wie bisher.
- **Aufwand:** S, eine Zeile im Kopf-Skript.

**C7 Druckansicht**
- **Was:** `@media print` blendet Leiste, Baum, Nachbarkarten und Spieler aus. Beispiele, Hintergrund und Herleitungen werden aufgeklappt gedruckt, Lösungen bleiben weg. Schwarzer Text, Links mit Adresse, Abbildungen als Endbild.
- **Aufwand:** S.

**Typografie:** Am Desktop nichts ändern; Schriftgröße, Zeilenhöhe und Spaltenbreite sind gut.
- **Was sich ändert:** Die rechte Spalte (210 px) ist künftig durch B1 gefüllt statt leer.
- **Keine Symbole an Kästen:** Die Textbeschriftungen der Kästen bleiben ohne Symbole (Regel „kein KI-Look“, Mayer-Kohärenz).

| Kennung | Nutzen | Aufwand | Inhalt | Übersetzung / Bestand | Risiken | Dateien |
|---|---|---|---|---|---|---|
| C1 | hoch (Handy-Leser) | S–M | auto | – / alle | Klassen genau treffen; an je einem Artikel jedes Moduls prüfen | `WISSEN_CSS`, `WISSEN_JS`, `lang_switch` |
| C2 | mittel | S | auto | Wörter einmal | – | `render_article`, `UI` |
| C3 | mittel–hoch (Einstieg) | M | einmal + auto | ~30 Sätze × 5 Sprachen | Startseite muss mit dem Build Schritt halten | `web/index.html` bzw. Erzeugung im Build |
| C4 | mittel | M | auto | – | – | `render_index` |
| C5 | mittel | S | auto | – | Endbild verrät den Ablauf; vertretbar | Spieler in `WISSEN_JS`, CSS |
| C6 | klein | S | auto | – | – | `page_shell` |
| C7 | klein–mittel | S | auto | – | – | `WISSEN_CSS` |

### 5.4 Technik und Reichweite

**D1 Grundpaket Auffindbarkeit**
- **Dateien und Kopfangaben:**
  - `sitemap.xml` mit `lastmod` je Sprache und `robots.txt`;
  - `<link rel="canonical">`;
  - `hreflang` mit `x-default` (→ de).
- **Strukturierte Daten (JSON-LD):** `LearningResource`/`Article` mit `inLanguage`, `isPartOf` (Modul), `educationalLevel`, `teaches` (aus den Begriffen) und `dateModified`.
- **Titel:** `<title>` ohne TeX, z. B. „Pole und Nullstellen in der p-Ebene – ET3 – EtUndSo“.
- **Beschreibung:** das erste „Kurz gesagt“ oder der Satz aus „Worum es geht“, der mit „Dieser Abschnitt zeigt …“ beginnt, statt des ersten Satzes.
- **Optional `llms.txt`.**
- **Grundlage:** Alles steht schon als Plan in `SEO_AUFFINDBARKEIT.md`.
- **Aufwand:** S–M, auto.

**D2 Vorschaubilder für soziale Medien** (`og:image`)
- **Format:** Netzwerke lesen kein SVG, also PNG 1200×630.
  - Grüne Leiste mit Titel und Modul, daneben das Endbild der ersten Abbildung.
- **Dateibudget beachten:**
  - Je Artikel und Sprache ein Bild wären etwa 4 500 Dateien. Das sprengt den Gratis-Rahmen von 20 000 Dateien.
  - Deshalb **ein Bild je Kapitel und Sprache** (rund 450), oder ein Bild je Artikel nur auf Deutsch und Englisch.
- **Erzeugung:** im Export (`tools/export_szenen.py`, Rasterung über Playwright, das schon für die Prüfwerkzeuge dient).
- **Aufwand:** M.

**D3 Ladezeit**
- **KaTeX selbst ausliefern:** Unter `/wissen/assets/katex/`, kein fremder Server mehr. Das ist auch für den Datenschutz einfacher. Aufwand S.
- **Formeln beim Build setzen:** KaTeX im Build vorrendern, dann ohne Springen und ohne Rechenzeit am Handy. Aufwand M; braucht Node mit KaTeX im Build.
- **Suchindex teilen:** wie in B6.
- **Themenbaum:** Er steht in jeder Seite (784 Links, ~180 kB unkomprimiert je Artikel). Er bleibt so, weil er Suchmaschinen die Verlinkung zeigt; komprimiert ist er klein.

**D4 Barrierefreiheit**
- **Sprunglink** „Zum Inhalt springen“.
- **Spieler mit Tastatur:** Leertaste = Start/Stopp, Pfeile = Schritt. Der Zeitstand wird angesagt, z. B. „Schritt 3 von 8“.
- **Sprachauszeichnung:** `lang` an fremdsprachigen Code- und Zitatstellen.
- **Fokusrahmen** überall sichtbar.
- **Lange Beschreibung:** Für Animationen ist die Bildunterschrift der Text. Wo der Ablauf wichtig ist, nennt die Bildunterschrift Anfang, Ablauf und Endzustand. Das ist eine Schreibregel, kein Bau.
- **Kontraste:** Die Farben erfüllen 4,5 : 1; Orange auf Grau in Kästen beim Bau nachmessen.
- **Aufwand:** S.

**D5 PDF je Kapitel**
- **Was:** Knopf „Kapitel als PDF“ im ersten und im letzten Artikel des Kapitels. Die Hefte gibt es schon als PDF, nach denselben Regeln: keine Herkunftsangaben.
- **Bedingungen:**
  - nur Hefte, deren PDF zum Stand der Website passt (Datum vergleichen);
  - nur die Sprachen, für die ein PDF gebaut ist.
- **Dateien:** rund 75 Hefte × Sprachen, das ist unkritisch für das Dateibudget.
- **Aufwand:** S–M.
- **Risiko:**
  - PDF und Website laufen auseinander. Daher den Build prüfen lassen, ob das PDF jünger ist als das Heft.
  - Dateigröße: Die Grenze von 25 MiB je Datei einhalten.

**D6 Offline lesen**
- **Was:** Ein Service Worker hält die zuletzt gelesenen Artikel samt Abbildungen und Assets vor.
- **Bewertung:** Aufwand M, Nutzen klein (Bahn, Hörsaal). Die Seite liefert bewusst mit `Cache-Control: no-cache` aus; ein Service Worker muss das sauber versionieren, sonst sehen Leser alte Stände. Niedrige Priorität.

**D7 Übersetzungsstand sichtbar**
- **Was:** Ist eine Übersetzung älter als das deutsche Heft, steht oben ein unauffälliger Satz, z. B. „This translation reflects an earlier version of the German article“, mit Link.
- **Herkunft:** Der Build vergleicht einen `stand:`-Eintrag (Datum oder Prüfsumme des deutschen Hefts), den der Übersetzungsschritt setzt.
- **Aufwand:** S–M; auto, mit einem Satz je Sprache einmal.

**D8 Rückmeldung je Artikel** (anonym)
- **Frage am Artikelende:** „Hat dir das geholfen? Ja · Teilweise · Nein“.
  - Gezählt wird nur die Summe je Artikel und Antwort, ohne IP, Cookie oder Kennung, wie bei `/api/count`.
  - Eine Stimme je Artikel und Browser sperrt `localStorage`.
- **„Fehler melden“:** Link per E-Mail mit Betreff „Fehler in <Artikeladresse>“. Kein Formular, das Texte speichert, also keine personenbezogenen Daten und keine Moderation.
- **Auswertung:** Eine kleine Liste für den User zeigt die Artikel mit den meisten „Nein“. Das sind die Stellen, die nach dem Nordstern („wer hängengeblieben ist, versteht es danach“) zuerst überarbeitet gehören.
- **Technik und Grenzen:**
  - Workers KV erlaubt im Gratis-Tarif etwa 1 000 Schreibvorgänge pro Tag. Das teilt sich die Zählung mit dem Seitenzähler, der schon je Besuch schreibt.
  - Für viele Artikel ist D1 (SQLite bei Cloudflare) besser geeignet.
- **Aufwand:** S–M.
- **Risiko:** Manipulierbar, weil es keine Identität gibt. Für ein Signal „wo hakt es“ genügt das.

| Kennung | Nutzen | Aufwand | Inhalt | Übersetzung / Bestand | Risiken | Dateien |
|---|---|---|---|---|---|---|
| D1 | Reichweite hoch | S–M | auto | – / alle | – | `build_wissen.py` (`page_shell`, neue Sitemap) |
| D2 | Reichweite mittel | M | auto | – | Dateibudget | `tools/export_szenen.py`, `page_shell` |
| D3 | mittel (Handy, Datenschutz) | S / M | auto | – | Node im Build (nur Vorrendern) | `page_shell`, `web/wissen/assets/` |
| D4 | Pflicht für Zugänglichkeit | S | auto | Wörter einmal | – | `build_wissen.py`, Spieler |
| D5 | mittel (Lernen auf Papier) | S–M | auto | nur gebaute Sprachen | Stand von PDF und Website | `build_wissen.py`, Kopierschritt der PDFs |
| D6 | klein | M | auto | – | alte Stände | neuer Service Worker |
| D7 | mittel (Vertrauen) | S–M | auto + einmal | Satz je Sprache | Übersetzungsschritt muss `stand:` setzen | `heft_zu_artikel.py`, `build_wissen.py` |
| D8 | hoch für die Autoren, indirekt für die Leser | S–M | einmal | Wörter einmal | KV-Grenzen, Manipulation | `web/functions/api/`, `WISSEN_JS`, `datenschutz.html` |

### 5.5 Was sonst auffiel
- **E1 Knopf „Kopieren“ an Codeblöcken:**
  - kopiert nur die Befehlszeilen, ohne Prompt (`student@labor:~$ `) und ohne Ausgabe;
  - erlaubt, denn es führt nichts aus;
  - S, auto.
- **E2 Datum „Stand“ je Artikel:** aus dem Heft, wie der „Stand“ in der Titelzeile; S, auto.
- **E3 Editor als Teil der Seite (nur Hinweis an den Editor-Plan):**
  - EtUndSo-Logo, Rückweg „← Zurück zum Artikel“, wenn man aus einem Artikel kommt;
  - Oberfläche in der Sprache der Seite;
  - Ansichtswürfel ohne Lila.
- **E4 Vereinheitlichung von „Worum es geht“:** Mehrere Zweck-Texte sagen „Dieser Abschnitt“ oder „Diese Stufe“, obwohl der Leser einen Artikel sieht. Bei der Überarbeitung „Dieser Artikel“ bevorzugen, damit die Schnell-Info stimmig liest. Das ist eine Schreibregel, keine Technik.

---

## 6. Priorisierung

### 6.1 Die zehn besten, in Reihenfolge
1. **B1 Inhaltsverzeichnis aus `###`.** Der Mangel betrifft 91 % der Artikel, der Aufwand ist klein, und es ist die Voraussetzung für die Sprunglinks der Schnell-Info.
2. **A1 Schnell-Info „Auf einen Blick“.** Wunsch des Users; automatisch und ohne Übersetzungskosten. Sie füllt sich mit jeder Überarbeitung weiter.
3. **C1 Handy-Lesbarkeit** (mit B4). Mehr Textbreite, kürzerer Kopf, vergrößerbare Abbildungen; reine CSS- und JS-Arbeit.
4. **B3 Lesefortschritt mit B2 (Position im Kapitel).** Ohne Konto und ohne Übertragung; gibt das Erfolgserlebnis beim Abschließen von Kapiteln.
5. **A2 + A3 Begriffsverzeichnis und Vorschaukarten.** Automatisch aus den Definitionen, gut belegt (pretraining, Page Previews), passt zu „Rückverweise sind erwünscht“.
6. **A4 Lernkarten mit verteilter Wiederholung.** Der größte belegte Lerneffekt. Groß im Bau, aber ohne Inhaltsaufwand. Davor als kleiner Schritt A5 (Abdeck-Modus).
7. **C3 + C4 Startseite und Wissensübersicht.** Die Erklärungen kommen nach vorn, die Startseite gibt es in sechs Sprachen, die Übersicht wird kurz.
8. **D1 + D2 Auffindbarkeit und Vorschaubilder.** Ohne sie findet kaum jemand die Seite. D2 mit Blick auf das Dateibudget.
9. **D8 Rückmeldung „Hat das geholfen?“ und „Fehler melden“.** Zeigt, wo die Erklärungen hängen, und bleibt dabei anonym.
10. **A6 Regler-Modus mit Vorhersagefrage.** Der wichtigste Schritt zu interaktiven Grafiken. Erst nach L3 im Editor, deshalb an zehnter Stelle.

### 6.2 Schnelle Gewinne (klein, sofort spürbar, alle auto)

| Was | Aufwand | Datei |
|---|---|---|
| B1 Inhaltsverzeichnis aus `###` | S | `build_wissen.py` |
| C2 Kennzahlenzeile (Lesezeit gibt es schon) | S | `render_article` |
| D1 (Teil) `<title>` und Beschreibung ohne TeX, bessere Beschreibung | S | `page_shell`, `collect` |
| E1 Kopierknopf an Codeblöcken | S | `code_html`, `WISSEN_JS` |
| B7 Ankerlinks an Unterüberschriften | S | `md_to_html` |
| C7 Druckansicht | S | `WISSEN_CSS` |
| C6 Nachtmodus folgt dem System | S | `page_shell` |
| D3 (Teil) KaTeX selbst ausliefern | S | `page_shell`, `assets/` |
| C5 Standbild statt leerem Startbild | S | Spieler |
| C1 (Teil) Abbildung antippen zum Vergrößern | S | `WISSEN_JS`, CSS |
| C3 (Teil) 🚧 im Hinweisband durch Text ersetzen | S | `web/index.html`, `editor.html` |
| D4 (Teil) Sprunglink „Zum Inhalt“ | S | `topbar` |

### 6.3 Bewusst nicht empfohlen

| Idee | Grund |
|---|---|
| Code im Browser ausführen (Online-Python, Web-Terminal, Regex-Tester) | feste Grenze; der Regex-Tester führt Eingaben der Leser als Muster aus |
| Umschalter KI \| Mensch, Fassungen kompakt/ausführlich | vom User abgeschafft |
| Eigene, je Artikel geschriebene Zusammenfassung als Pflicht im Heft | doppelt „Kurz gesagt“; 753 × 6 Fassungen nachzurüsten; läuft auseinander (4.7) |
| Zusammenfassungen beim Build von einem Sprachmodell erzeugen lassen | nicht nachprüfbar, nicht reproduzierbar, laufende Kosten, Fehler gehen ungeprüft online |
| Kommentare, Forum, Konten, Fortschritt auf dem Server | personenbezogene Daten, Moderation; der Fortschritt im Browser genügt |
| Punkte, Serien, Abzeichen, Ranglisten | widerspricht dem seriösen Ton; äußerer Anreiz statt Verstehen |
| Symbole oder Emojis als Kastenmarker, dekorative Bilder | Regel „kein KI-Look“; Mayer-Kohärenz |
| Lila oder Rot als neue Kastenfarben | Variante B |
| Scrollytelling (Abbildung ändert sich beim Scrollen) | Leser verliert die Kontrolle über das Tempo, schlecht zugänglich; Knopfsteuerung ist besser |
| Große interaktive Netzgrafik aller Voraussetzungen | wird bei vielen Knoten unlesbar; Listen je Kapitel (B5) leisten mehr |
| Automatisches Hervorheben gleicher Formelsymbole im ganzen Artikel | teuer, fehleranfällig, kleiner Nutzen (A7) |
| Chat-Assistent auf der Seite | Drittanbieter, Kosten, keine Gewähr für Korrektheit, Datenschutz |
| Fremde Statistik- oder Videodienste (Google Analytics, eingebettetes YouTube) | Tracking; Videos, wenn sie kommen, selbst ausliefern |
| Maschinelle Live-Übersetzung im Browser | Qualität; die sechs geprüften Sprachen sind der Anspruch |
| Je Artikel und Sprache ein eigenes Vorschaubild | Dateibudget von Cloudflare Pages (D2) |

---

## 7. Offene Fragen an den User
1. **Schnell-Info, Voreinstellung:**
   - a) offen außer beim Weiterklicken im Kapitel (empfohlen);
   - b) immer offen;
   - c) immer zugeklappt.
   - Und ist die Ausnahme von „Keine Vorgriffe“ für diese Box in Ordnung (4.6)?
2. **Kernformel in der Box** bei Artikeln mit Satz-Kasten: ja oder nein?
3. **Startseite:** Sollen die Erklärungen vor den Editor rücken (C3)? Soll die Unterzeile Informatik gleichrangig nennen?
4. **Lernkarten (A4):** gewünscht? Wenn ja, zuerst der Abdeck-Modus (A5) als kleiner Schritt?
5. **Rückmeldung je Artikel (D8):** gewünscht? Dafür wäre eine Cloudflare-D1-Datenbank nötig.
6. **Hosting-Tarif:** Gratis (20 000 Dateien) oder bezahlt (100 000)? Das entscheidet über Vorschaubilder je Artikel und betrifft auch die geplanten 1 237 Abbildungen in sechs Sprachen.

---

## 8. Anhang
- **Screenshots:** 14 Bilder und `metrik.json` im Scratchpad dieser Sitzung, nicht im Repo:
  - Ordner `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\website_ideen\shots\`;
  - darin 01–02 Startseite, 03 Wissen, 04–06 ET3, 07–08 Linux-Abbildung, 09 Python, 10 Englisch, 11–12 ET3 Formeln/Nacht, 13 Editor, 14 Linux-Ende.
- **Zählskripte:** `zaehlen.py`, `kennzahlen.py` im selben Scratchpad-Ordner.
- **Quellen der Recherche** (Prinzipien, nichts übernommen):
  - **Lead und Seitenvorschau:**
    - Wikipedia Manual of Style/Lead section: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
    - Page Previews: https://www.mediawiki.org/wiki/Page_Previews
  - **MDN-Lernbereich:** https://developer.mozilla.org/en-US/docs/Learn_web_development
  - **Lesen am Bildschirm:** NN/g F-Pattern: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/
  - **Erklären mit Bild und Farbe:**
    - Better Explained, ADEPT und Colorized Equations: https://betterexplained.com/articles/adept-method/ und https://betterexplained.com/articles/colorized-math-equations/
    - Distill „Research Debt“: https://distill.pub/2017/research-debt/
    - Bret Victor: https://worrydream.com/ExplorableExplanations/ und https://worrydream.com/LadderOfAbstraction/
    - Seeing Theory: https://seeing-theory.brown.edu
  - **Barrierefreiheit:**
    - WCAG 2.2.2: https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide
    - WCAG 2.3.3: https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions
    - Komplexe Bilder: https://www.w3.org/WAI/tutorials/images/complex/
    - ARIA-Slider: https://www.w3.org/WAI/ARIA/apg/patterns/slider/
  - **Lernpsychologie** (Zahlen aus Übersichtsarbeiten, vor Zitat prüfen):
    - Dunlosky et al. 2013, doi:10.1177/1529100612453266
    - Roediger & Karpicke 2006, doi:10.1111/j.1467-9280.2006.01693.x
    - Cepeda et al. 2006, doi:10.1037/0033-2909.132.3.354
    - Kalyuga et al. 2003, doi:10.1207/S15326985EP3801_4
    - Richland et al. 2009, doi:10.1037/a0016978
    - Mayer, Multimedia Learning (3. Aufl. 2021)
    - Luiten, Ames & Ackerson 1980
  - **Hosting-Grenzen:** Cloudflare Pages, Changelog 23.01.2026: https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/ und https://developers.cloudflare.com/pages/platform/limits
