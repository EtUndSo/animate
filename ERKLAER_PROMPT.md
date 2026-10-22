# EtUndSo — Erklär-Prompt (Didaktik, Umfang, Ton und Form; verbindlich ab „Stil 3“)

Diese Datei beschreibt jeden Bestandteil eines Artikels: was hineingehört, wie viel davon, in welcher Reihenfolge, in welchem Ton und nach welchen Regeln. Lies sie vor jedem Thema vollständig. Sie gilt auch dann vollständig, wenn der Gesprächsverlauf inzwischen zusammengefasst wurde.

## 0. Geltung, Vorrang und Vorbild

**Entscheidungen des Users vom 21.10.2026:**
- Die Erklärungen des Lernskripts sind deutlich besser als die bisherigen Artikel, auch als die überarbeiteten. Ausführlichkeit, Tiefe und vor allem Hintergründe, die anderswo oft fehlen, sind gewollt.
- Die aktuellen Artikel wirken oft spielerisch bis kindisch. Gewollt ist der Ton des Lernskripts: ernst, professionell, tiefgehend, informationsreich. Analogien, Beispiele und benannte „Akteure“ gehören dazu, aber ohne kindische Form.
- **Jedes Thema bekommt zwei Fassungen:**
  - eine ausführliche, etwas kompakter als das Lernskript;
  - eine kompakte.
  
  So entscheiden die Leserinnen und Leser selbst, wie tief sie einsteigen. Der doppelte Aufwand ist in Kauf genommen.
- **Gut strukturieren, nichts doppeln, Unwichtiges aussortieren.** Die Ausführlichkeit richtet sich nach der Schwierigkeit; zu knapp darf auch die kompakte Fassung nicht sein.
- **Nichts als bekannt voraussetzen.** Erklärt wird immer so, als wüsste die Person nichts über das Thema. Themen werden erklärt, nicht aufgelistet.
- Abbildungen werden eingebaut, wo sie helfen; der Text baut auf dem Konzept auf, das sie zeigen.
- **Nur Editor-Abbildungen** (nach dem Piloten, ebenfalls 21.10.2026):
  - In allen Artikeln stehen nur Abbildungen, die der EtUndSo-Editor erzeugt.
  - Bis die nötigen Editor-Funktionen gebaut sind, steht an jeder Stelle ein Platzhalter `:::grafik` mit Bildbeschreibung.
  - Was jede Abbildung zeigen soll und welche Editor-Funktionen sie braucht, steht in `ABBILDUNGEN_LISTE.md`.
  - Funktionen und Abbildungen entstehen **nach** den Artikeln, nicht im Loop, weil neue Features oft Probleme machen (§7.5).
- Herleitungen bleiben in eigenen, ausklappbaren Kästen.
- **Fragen an Ort und Stelle,** wie im Lernskript: Die Fragen, die sich Leserinnen und Leser an einer Stelle wahrscheinlich stellen, stehen genau dort als ausklappbare Frage-Kästen. Sichtbar ist die Frage, die Antwort öffnet sich per Klick (§9.3).

**Das Vorbild:** `C:\Bücher\Praktikum_Mina\Lernskript\` (gerendert `MiNa_Lernskript.pdf`, Quellen `k0_einstieg.tex` bis `k10_selbsttest.tex`).
- **Was es vorgibt:** Ton, Erklärtiefe und Hintergründe.
- **Wie viel Text:** Seine Kapitel haben 1200 bis 2300 Wörter Fließtext; die 57 Seiten entstehen durch Abbildungen, Kästen und Formeln. Die ausführliche Fassung ist für denselben Inhalt etwas kürzer, weil sie nichts doppelt erklärt (§3).
- **Was du vorher liest:** Vor dem ersten Stil-3-Thema `k4_gleichgewicht.tex` und `k5_durchlass.tex` vollständig, bei Halbleiter-Themen jedes Mal die passenden Kapitel.

**Vorrang bei Widersprüchen:**
1. **Diese Datei:** Didaktik, Umfang, Ton, Form, Herleitungen, Abbildungen, Beispiele.
2. **`ARTIKEL_BAUPLAN.md`:** Formeln und Notation (§2), Beispiel-Seite (§3a, soweit hier nicht geändert), Block-Syntax (§5), Workflow (§6), Technik (§7), Review (§8).
3. **`ARTIKEL_LEITFADEN.md`:** Sprache (§8), Recherche (§9), Keine Kopien (§11).

Alle Änderungen am Bauplan stehen in §14.

## 1. Für wen du schreibst

**Die Leserin bzw. der Leser:**
- **weiß über das Thema des Artikels nichts.** Vorausgesetzt werden nur Schulmathematik, Schulphysik und die Themen, die der Artikel ausdrücklich als Voraussetzung verlinkt;
- hat oft das Vorlesungsskript vor sich, hat es aber nicht verstanden, oder kommt über die Suche direkt auf den Artikel;
- will das Thema verstehen, nicht auswendig lernen: in der kompakten Fassung den Kern in einer Sitzung, in der ausführlichen das ganze Thema samt Hintergründen;
- liest genau und folgt jeder Logik; Ungenauigkeit verwirrt, Präzision hilft;
- bringt die typischen Fehlvorstellungen mit;
- ist erwachsen und will ernst genommen werden.

**Ein Artikel ist gelungen, wenn diese Person danach drei Dinge kann:**
1. das Thema laut in eigenen Worten erklären, mit jedem Warum;
2. die zentrale Formel ohne Nachschlagen herleiten;
3. die typischen Fehlvorstellungen erkennen und widerlegen.

## 2. Ton: ernst, professionell, informationsreich

Schreib so, wie ein sehr guter Hochschullehrer ein Begleitskript schreibt, das er selbst gern gelesen hätte. Sachlich, präzise und dicht an Information, aber nicht trocken: Jede Aussage hat einen Grund, eine Größenordnung und eine Bedeutung.

**Das heißt konkret:**
- Jeder Satz trägt Information. Keine Füllsätze, keine Ankündigungen („Gleich sehen wir …“), keine Begeisterungsformeln.
- Neugier entsteht aus einer guten Frage und einer überraschenden Zahl, nicht aus einer Geschichte.
- Der Normalfall ist der sachliche Lehrbuchton („Man erhält …“, „Daraus folgt …“). Direkte Anrede sparsam.
- Fachsprache wird benutzt **und** beim ersten Auftreten erklärt (§5.1), nicht durch Umgangssprache ersetzt.

**Nicht erlaubt**, weil es spielerisch oder kindisch wirkt:
- **Figuren und Szenen als Erklärgerüst:** Autos in einem Parkhaus, Wanderer, springende Bälle.
- **Vermenschlichte Teilchen:** „Das Elektron möchte …“, „die Löcher fliehen“.
- **Niedliche oder reißerische Bilder:** „der Strom schießt hoch“, „ein Schwall“, „ein Rinnsal“, „rasen“.
- **Verspielte Titel:** Beispiel- und Abschnittstitel wie „Ein Elektron ohne Nägel“.
- **Ein Leitbild in jedem Absatz:** ein Bild, das durch jeden Abschnitt getragen wird, auch dort, wo es nicht passt.

**Erwünscht:**
- **Analogien als knappe, strukturgleiche Vergleiche** im Kasten (§9.1).
- **Konkrete technische Beispiele mit echten Zahlen** (§8): reale Bauteile, Schaltungen und Datenblattwerte aus Studium und Praktikum.
- **Zahlen, die verblüffen, weil sie stimmen:** „Im n-Gebiet kommen auf 10¹⁶ Elektronen pro Kubikzentimeter nur 10⁴ Löcher.“

## 3. Zwei Fassungen, Umfang und Aussortieren

Die Tiefe bleibt: Mechanismen, Herleitungen und gerade die Hintergründe, die Skripte und Lehrbücher oft weglassen, sind der Wert der Seite. Damit niemand mehr lesen muss, als er will, gibt es jedes Thema in zwei Fassungen; oben auf der Seite schaltet man um.

### 3.1 Die zwei Fassungen

| | Kompakt | Ausführlich |
|---|---|---|
| Zweck | den Kern in einer Sitzung verstehen: jedes Warum des Kerns, die Kernformeln, die Kipp-Stellen | das Thema durchdringen: zusätzlich alle Hintergründe, alle Herleitungen, Vertiefungen, Sonderfälle und Praxis |
| Inhalt (§3.2) | alles aus K; aus H nur, was der Kern braucht, je ein bis zwei Sätze | K, H und V vollständig |
| Formeln und Herleitungen | nur die Kernformeln, jede mit ihrem Herleitungskasten | jede Formel des Themas mit Herleitungskasten |
| Abbildungen | die wichtigsten, etwa 3 bis 6 | alle aus dem Abbildungsplan, etwa 6 bis 12 |
| Beispiele | 2 bis 4: zentrale Formel, tragende Zahl der Kipp-Stelle, ein Praxisbeispiel | nach §8.3 |
| Frage-Kästen | 2 bis 4: die Fragen, die sich am häufigsten stellen | etwa 4 bis 8 |
| andere Kästen | höchstens drei; eine Analogie nur, wenn sie eine Kipp-Stelle trägt | nach §9 |
| Quiz | genau 6 Fragen | genau 10 Fragen |

**Was für beide Fassungen gilt:**
- **Von null an:** Beide erklären von null an (§5.1), im selben Ton, mit denselben Zahlen, Symbolen und Abbildungen (dieselben Szenen) und mit demselben Ein-Satz-Prinzip.
- **In sich vollständig:**
  - Wer nur die kompakte Fassung liest, hat im Kern keine Lücke.
  - Die ausführliche Fassung setzt die kompakte nicht voraus.
- **Verbunden:**
  - Der Build setzt einen Umschalter an den Seitenanfang.
  - Die kompakte Fassung nennt vor dem Kernteil in einem kurzen Absatz **„In der ausführlichen Fassung:“**, was dort zusätzlich steht, mit Link.

**Arbeitsreihenfolge:**
1. Erst schreibst du die ausführliche Fassung. Sie enthält alles und sichert die Vollständigkeit.
2. Dann schreibst du die kompakte Fassung **neu**, nicht als Zusammenschnitt: dieselbe Logik in weniger Schritten, mit eigenen Übergängen. Herleitungskästen der Kernformeln übernimmt sie unverändert.

**Dateien und Kennzeichnung:**
- **Kompakte Fassung:** `<nr>-<slug>.md`. Sie behält die bisherige Adresse.
- **Ausführliche Fassung:** `<nr>-<slug>-ausfuehrlich.md`.
- **Frontmatter:** `fassung: kompakt` bzw. `fassung: ausfuehrlich`, beide mit `stil: 3`.
- **Verknüpfung:** Der Build verknüpft beide über das Frontmatter (§14).

### 3.2 Aussortieren
Vor dem Schreiben bekommt jeder mögliche Inhalt (aus Skript, Lernskript, Lehrbüchern und eigenem Wissen) in der Arbeitsnotiz (§10) eine von vier Kategorien:

| Kategorie | Kriterium | Kompakt | Ausführlich |
|---|---|---|---|
| **K: Kern** | Ohne ihn versteht man das Thema nicht oder falsch. | vollständig | vollständig |
| **H: Hintergrund** | Er beantwortet ein Warum, das sonst offen bliebe und das Skripte oft verschweigen, etwa warum man die Diffusionsspannung mit keinem Voltmeter messen kann. | nur, wenn der Kern ohne ihn falsch verstanden würde; dann in ein bis zwei Sätzen | vollständig, mit Grund und Zahl |
| **V: Vertiefung** | Er erweitert das Verständnis, ist aber nicht nötig: genaueres Modell, Sonderfall, Herkunft eines Zahlenwerts, Messtechnik, Geschichte. | nein | als Abschnitt oder Kasten `:::vertiefung` |
| **S: Streichen** | Wiederholung; gehört in einen anderen Artikel (dort verlinken); Nebenthema ohne Bezug zum Prinzip; Detail, das weder dem Verständnis noch der Prüfung dient. | nein | nein |

**Prüffrage:** Würde eine Person ohne diesen Inhalt etwas falsch verstehen oder eine Warum-Frage behalten? Ja: K oder H. Nein: V oder S.

**Frage-Kästen:** Ist ein H-Inhalt die Antwort auf eine Frage, die sich an dieser Stelle aufdrängt, steht er als Frage-Kasten (§9.3). In der kompakten Fassung ist das der bevorzugte Ort für Hintergründe. Der Text bleibt dann kurz, und wer genau diese Frage hat, findet die Antwort an Ort und Stelle.

**Vollständigkeit gegenüber der Quelle:**
- Die ausführliche Fassung enthält alle wichtigen Definitionen, Formeln und Aussagen des Skriptabschnitts.
- Die kompakte Fassung enthält alle, die zum Kern gehören.

Aussortiert werden Wiederholungen, Ausschmückungen und Nebenthemen, nicht Stoff.

### 3.3 Länge nach Schwierigkeit
Orientierung für den **Hauptpfad**, gemessen in Wörtern. Zum Hauptpfad gehört der sichtbare Text, ohne Herleitungskästen, Beispiele und Quiz. Die Lesezeit gilt bei 170 Wörtern pro Minute. Gezählt wird mit `tools/artikel_kennzahlen.py`.

| Schwierigkeit | typischer Inhalt | Kompakt | Ausführlich |
|---|---|---|---|
| leicht | eine Definition, eine Regel, eine Rechentechnik (Knotenregel, Reihenschaltung, Erwartungswert) | 500 bis 1000 Wörter (3 bis 6 min) | 1200 bis 2000 Wörter (7 bis 12 min) |
| mittel | ein Mechanismus oder eine zentrale Formel mit Anwendungen (Laden eines Kondensators, Drift im Leiter, Satz von Stokes) | 1000 bis 1800 Wörter (6 bis 11 min) | 2000 bis 3500 Wörter (12 bis 21 min) |
| schwer | mehrere zusammenwirkende Mechanismen und Kipp-Stellen (pn-Übergang, Bipolartransistor, Integralsätze im Raum) | 1800 bis 2800 Wörter (11 bis 16 min) | 3500 bis 5000 Wörter (21 bis 29 min) |

**Platz innerhalb eines Artikels** richtet sich ebenfalls nach der Schwierigkeit:
- **Definition:** zwei Sätze und ein Satz dazu, warum man sie so wählt.
- **Mechanismus:** ein bis vier Absätze.
- **Kipp-Stelle:** eine Schrittfolge (§4.5) mit Abbildung, Zahl, Herleitung und Beispiel. Eine Kipp-Stelle in zwei Sätzen ist ein Fehler, auch in der kompakten Fassung.

**Liegt ein Hauptpfad über der Spanne:**
1. Streiche zuerst Doppelungen (§3.4).
2. Verschiebe dann in der ausführlichen Fassung V-Inhalte in `:::vertiefung`-Kästen bzw. nimm in der kompakten Fassung H-Inhalte heraus.
3. Reicht das nicht, schlag dem User vor, das Thema zu teilen. Teile nicht eigenmächtig.

**Unter der Spanne zu bleiben ist kein Fehler**, solange der Neuling-Test (§11) keine Lücke findet. Zu knapp ist ein Artikel, sobald ein Begriff unerklärt bleibt, ein Schritt ohne Grund steht oder eine Formel ohne Deutung.

### 3.4 Jede Sache genau einmal (innerhalb einer Fassung)
- **Ein Ort pro Inhalt.** Jeder Mechanismus, jede Definition und jeder Hintergrund wird genau einmal erklärt, an der Stelle, an der er zuerst gebraucht wird. Später genügt ein Halbsatz mit Verweis auf den Abschnitt („wie im Abschnitt *Gleichgewicht* gezeigt, …“). Steht ein Inhalt in einem Frage-Kasten, erklärt der Text ihn nicht noch einmal.
- **Drei bewusste Verdichtungen.** Jede hat eine eigene Aufgabe. Sie wiederholen einander nicht, und keine wiederholt einen Absatz des Textes.
  - „Worum es geht“ gibt eine Vorschau, ohne Erklärung.
  - „Alles hängt an einem Prinzip“ zeigt die Verbindungen, ohne Formeln.
  - Der Kernteil `:::kern` nennt die Beziehungen zum Behalten, ohne Begründungen.
- **Jeder Ort hat seine Aufgabe:**
  - „So liest man das“ (§4.4) deutet die Formel.
  - Der Herleitungskasten (§6.3) zeigt nur, woher die Faktoren kommen.
  - Die Einordnung eines Beispiels (§8.2) deutet die konkrete Zahl.
- **Verboten:**
  - Rückblick- und Zusammenfassungsabsätze am Abschnittsende („Fassen wir zusammen …“).
  - Ein Kasten, der die Erklärung des Textes nacherzählt.
  - Ein Text, der eine Abbildung vollständig beschreibt, statt durch sie zu führen.
  - Eine Akteure-Liste, die schon eingeführte Größen noch einmal beschreibt.
- **Zwischen Artikeln:** Jeder Artikel ist für sein eigenes Thema in sich vollständig, denn viele Leserinnen und Leser kommen über die Suche direkt dorthin. Voraussetzungen aus anderen Themen ruft er dort, wo sie gebraucht werden, in einem Satz in Erinnerung und verlinkt sie: was es ist und was hier davon gebraucht wird. Neu erklärt werden sie nicht.

### 3.5 Kompakt schreiben (beide Fassungen)
- **Zahlen statt Adjektiven:** „40 000-mal kleiner“ statt „verschwindend klein“.
- **Tabellen** für Gegenüberstellungen statt paralleler Absätze (Durchlass gegen Sperr, ideal gegen real).
- **Abbildungen** statt langer Beschreibungen von Profilen, Kennlinien, Abläufen und Geometrie (§7).
- **Kurze Absätze:** ein Gedanke pro Absatz, zwei bis fünf Sätze.
- **Kein Rahmentext:** keine Ankündigungen, keine Rückblicke, keine Sätze über den Artikel selbst.
- **Hintergründe knapp:** Aussage, Grund, Zahl.

### 3.6 Struktur
- **Eine Frage pro Abschnitt:** Jeder `##`-Abschnitt beantwortet eine Frage. Die Überschrift benennt den Inhalt sachlich; die Leitfrage darunter stellt die Frage.
- **Reihenfolge nach der Vorwissen-Kette (§10):** Was ein Abschnitt braucht, steht vorher. Vorgriffe („das sehen wir später“) gibt es nicht.
- **Vom Konkreten zum Allgemeinen:** erst die Beobachtung oder eine konkrete Zahl, dann das allgemeine Gesetz.
- **Unterabschnitte:** `###` nur, wenn ein Abschnitt mehrere klar getrennte Teilfragen hat.

## 4. Das Gerüst eines Artikels

Das Gerüst gilt für die ausführliche Fassung vollständig. Was in der kompakten Fassung entfällt oder kürzer ist, steht jeweils dabei.

### 4.1 Kopf
- **Frontmatter:** `title`, `pfad`, `order` und `tags` bleiben, wie der Bauplan sie vorgibt. Beide Fassungen haben denselben `title`, denselben `pfad` und dieselbe `order`.
- **`summary`:** zwei sachliche Sätze dazu, was die Fassung erklärt und herleitet. Kein Leitbild.
- **Zusätzliche Zeilen:** `stil: 3` und `fassung: kompakt` bzw. `fassung: ausfuehrlich`.

### 4.2 `## Worum es geht`
Das Inhaltsverzeichnis steht weiterhin am Seitenanfang (Entscheidung vom 20.10.2026). „Worum es geht“ ist der erste Abschnitt danach: zwei bis fünf Sätze, ohne Geschichte und ohne Fahrplan, denn den zeigt das Inhaltsverzeichnis.
1. **Welches Problem** löst das Thema?
2. **Das Ein-Satz-Prinzip,** an dem jede Einzelheit hängt.
3. **Was vorausgesetzt wird,** mit Links, und was auf dem Thema aufbaut.

Danach folgt die **Einstiegsabbildung** (§7). Sie zeigt das zentrale Objekt oder den zentralen Mechanismus.

### 4.3 Optional: `## Das Bild` (nur ausführlich)
Nur, wenn ein Modell oder eine Analogie das ganze Thema ordnet, zum Beispiel Potential als Höhe, mit dem Hinweis, dass Elektronen das Bild umgekehrt sehen. Dazu ein Kasten `:::analogie` (§9.1) und eine Abbildung, wenn sie die Zuordnung zeigt. Danach kommt sofort die Physik bzw. Mathematik.

### 4.4 Die Sach-Abschnitte (`##`)
Ein Abschnitt enthält in dieser Reihenfolge, was sein Inhalt braucht. Nicht jeder Abschnitt braucht alles.
1. **Leitfrage:** ein *kursiver* Satz mit der Frage, die der Abschnitt beantwortet.
2. **Abbildung,** wenn sie das Konzept trägt. Sie steht **vor** der Erklärung, die auf ihr aufbaut (§7.4).
3. **„Die Akteure:“** vor jeder Kernformel und jedem Mechanismus, nur mit neuen Größen (§5.9).
4. **„Das Zusammenspiel:“** der Mechanismus.
   - Er steht in kurzen Absätzen als Kette aus Ursache, Wirkung und Folge.
   - Er nennt die tragenden Zahlen (§5.4) und führt durch die Abbildung.
   - An Kipp-Stellen steht hier die Schrittfolge (§4.5).
5. **Die Formel** als `:::formel <Typ>` (nur Kernformeln; sonst `$$…$$` auf eigener Zeile).
6. **„So liest man das:“** zwei bis vier Sätze. Sie sagen, was aus was berechnet wird und wovon das Ergebnis wie abhängt („je größer …, desto …“), und nennen die Grenzfälle. Die Symbole sind über die Akteure schon eingeführt und werden nicht noch einmal erklärt.
7. **„Idee der Herleitung:“** ein Satz, danach der Kasten `:::herleitung` (§6).
8. **`::::beispiel`** direkt hinter der Formel bzw. der Herleitung (§8).
9. **Kästen** an der Stelle, an der die Frage entsteht: `:::fehlvorstellung`, `:::frage`, `:::merke`, in der ausführlichen Fassung auch `:::vertiefung` (§9).
10. **Gegenüberstellungen** als Tabelle.

### 4.5 Kipp-Stellen
An jeder Kipp-Stelle (§10) steht das Zusammenspiel als nummerierte Schrittfolge, auch in der kompakten Fassung.
- **Schreibweise:** `**Schritt 1**: …`, `**Schritt 2**: …`. Der Doppelpunkt steht **außerhalb** der Sternchen, sonst färbt der Build die Marke nicht ein.
- **Umfang:** Jeder Schritt löst genau ein Teilproblem, in ein bis drei Sätzen.
- **Dazu gehören:**
  - mindestens eine Abbildung, oft eine Abfolge, etwa drei Zustände nebeneinander;
  - eine tragende Zahl;
  - eine Herleitung;
  - ein Beispiel.

### 4.6 Zwei Sichtweisen
Wo Lehrbücher zwei Bilder benutzen, zeigt die ausführliche Fassung beide. Beispiele: Strom- und Spannungssicht beim Transistor, Teilchen- und Feldbild, Fermi-Niveau und Ströme.
- Sie sagt, welches Bild physikalisch primär ist und warum das andere trotzdem benutzt wird.
- Sie zeigt, am besten in einem Beispiel, dass beide zu denselben Zahlen führen.

Die kompakte Fassung benutzt das primäre Bild und erwähnt das zweite in einem Satz, wenn Skript oder Praxis es verwenden.

### 4.7 `## Alles hängt an einem Prinzip`
Pflicht ab fünf Einzelaspekten. Der Abschnitt besteht aus zwei Teilen:
- einer Tabelle „Einzelheit | welche Seite des Prinzips sie zeigt“, ohne Formeln;
- darunter noch einmal das Ein-Satz-Prinzip.

Länge: in der ausführlichen Fassung höchstens acht Zeilen, in der kompakten höchstens fünf. Dieses Zurückbinden fehlt Leserinnen und Lesern am häufigsten.

### 4.8 `## Bedeutung und Ausblick`
In der ausführlichen Fassung ein bis zwei kurze Absätze:
- die **technische Anwendung** an einem realen Bauteil oder einer realen Schaltung;
- der **Bezug zum Praktikum** oder zur Messpraxis, wo es passt;
- die **Grenzen des Modells**, je ein Satz mit Link dorthin, wo sie behandelt werden;
- der **nächste Artikel** in einem Satz.

In der kompakten Fassung genügen zwei bis drei Sätze, danach folgt der Absatz **„In der ausführlichen Fassung:“** (§3.1).

### 4.9 `:::kern` („Das Wichtigste“)
Fünf bis acht Stichpunkte, die man dauerhaft behalten muss, in der kompakten Fassung dieselben.
- Jeder Punkt ist eine Kernaussage mit höchstens einer kurzen Formel.
- Begründungen stehen im Text; hier steht nur, was bleiben muss.

### 4.10 `:::quiz`
Das Format folgt dem Bauplan: je eine Zeile `F: …` und eine Zeile `A: …`. Die ausführliche Fassung hat genau zehn Paare, die kompakte genau sechs.

**Inhalt der ausführlichen Fassung:**
- mindestens drei Warum-Fragen zu den Kipp-Stellen;
- mindestens zwei Fragen der Form „Stimmt es, dass …?“ zu Fehlvorstellungen;
- mindestens eine Rechenfrage mit Zahlen aus dem Zahlenwerk.

**Inhalt der kompakten Fassung:** je mindestens zwei Fragen der ersten beiden Arten und eine Rechenfrage.

**Woher die Antworten kommen:** Jede Antwort steht im Hauptpfad derselben Fassung oder auf ihrer Beispiel-Seite. Keine Frage verlangt ein Warum, das der Text nur behauptet.

### 4.11 Gerüst zum Abschreiben (ausführliche Fassung)

```
---
title: …
pfad: …
order: …
summary: …
tags: …
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

<Problem.> <Ein-Satz-Prinzip.> <Voraussetzungen mit Links; was darauf aufbaut.>

:::grafik
Szene: <modul>/<kapitel>/<nr>-<name> · Vorlage: <vorlage>
**Abbildung 1:** <Was gezeigt ist, mit den wichtigsten Zahlen.> <Kernaussage in einem Satz.>
:::

## <Inhalt des Abschnitts, sachlich benannt>

*<Leitfrage?>*

:::grafik
Szene: <modul>/<kapitel>/<nr>-<name> · Vorlage: <vorlage>
**Abbildung 2:** … <Kernaussage.>
:::

**Die Akteure:**

- __$…$__: <Bedeutung>; <Einheit bzw. Raum>; <Größenordnung im Beispielsystem>; <Rolle im Mechanismus>.
- __$…$__: …

**Das Zusammenspiel:** <Ursache, Wirkung, Folge; mit tragender Zahl; „Abbildung 2 zeigt links …“.>

<Weiterer kurzer Absatz, falls nötig.>

:::formel Gesetz
$$…$$
:::

**So liest man das:** <was aus was; je größer …, desto …; Grenzfälle.>

Idee der Herleitung: <ein Satz>.

:::herleitung
**Ausgangspunkt:** …
**Annahmen:** (i) … (ii) …
**Schritt 1**: <Begründung>
$$…$$
**Schritt 2**: …
$$…$$
**Ergebnis:**
$$…$$
**Woher die Faktoren kommen:** …
**Proben:** <Einheit, Grenzfall, Vorzeichen, Zahlenwert>.
**Grenzen:** <wann die Annahmen versagen>.
:::

::::beispiel <Sachlicher Titel: was berechnet wird>
**Gegeben:** …
**Gesucht:** …
**Rechnung:** …
$$…$$
**Ergebnis:** …
**Einordnung:** …
::::

:::frage
„<Die Frage, wie eine Leserin sie an dieser Stelle stellen würde?>“
<Antwort in zwei bis sechs Sätzen: Mechanismus, Zahl, Verweis auf den Abschnitt.>
:::

:::fehlvorstellung
„<Die falsche Idee in den Worten der Leserin.>“ <Warum sie naheliegt.> <Was stimmt.> <Entscheidendes Argument mit Zahl; Verweis auf den Abschnitt.>
:::

:::vertiefung
**<Was der Kasten erklärt.>** …
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| … | … |

<Ein-Satz-Prinzip.>

## Bedeutung und Ausblick

…

:::kern
- …
:::

:::quiz
F: …
A: …
:::
```

Die kompakte Fassung folgt demselben Gerüst. Abweichungen:
- **Frontmatter:** `fassung: kompakt`.
- **Entfällt:** `## Das Bild` und `:::vertiefung`.
- **Kürzer:** weniger Abschnitte, Abbildungen, Beispiele und Kästen.
- **Zusätzlich:** vor `:::kern` der Absatz „**In der ausführlichen Fassung:** …“.

## 5. Die Regeln, die eine Erklärung gut machen

### 5.1 Nichts voraussetzen
Die Person weiß über das Thema nichts (§1). Daraus folgt:
- **Fachbegriffe sofort erklären.** Jeder Fachbegriff des Themas wird bei seiner ersten Nennung erklärt, im selben oder im nächsten Satz. Das gilt auch für Begriffe, die für das Thema grundlegend wirken, etwa Dotierung, Ladungsträger, Rekombination, Bandlücke oder Gradient.
- **Symbole vor ihrem Gebrauch einführen** (§5.9).
- **Keine Sprünge.** Jeder Schritt folgt aus dem, was schon gesagt ist. Braucht ein Schritt eine Tatsache, steht sie vorher im Artikel oder wird in einem Satz in Erinnerung gerufen und verlinkt (§3.4).
- **Erst der Mechanismus in Worten, dann die Formel.** Eine Formel ohne vorherige Erklärung ist ein Sprung.
- **Verboten** sind „bekanntlich“, „offensichtlich“, „natürlich“, „wie man leicht sieht“, „trivialerweise“ und „einfach“ im Sinn von „einfach einsetzen“. Diese Wörter verstecken genau die Stellen, an denen jemand hängen bleibt.

### 5.2 Erklären statt auflisten
- **Erklärungen sind zusammenhängender Text** in kurzen Absätzen, jeweils eine Kette aus Ursache, Wirkung und Folge („Weil …, … . Dadurch …“).
- **Aufzählungen nur für echte Listen:** Akteure, Annahmen, Schritte, Kernteil, Gegenüberstellungen.
- **Eine Liste von Tatsachen ist keine Erklärung.** Enthält ein Listenpunkt ein Warum, wird er zu Fließtext.

### 5.3 Mechanismus vor Beschreibung
Zu jeder Aussage gehören vier Angaben:
- **wer oder was:** welche Teilchen, Ladungen, Felder oder Objekte;
- **welcher Antrieb:** Kraft, Gefälle, Wahrscheinlichkeit;
- **wie viel:** Größenordnung;
- **warum nicht anders.**

**Warum-Test:** Kann die Person auf einen Satz noch „Warum?“ fragen, und die Antwort steht nirgends im Hauptpfad derselben Fassung? Dann fehlt der Mechanismus.

### 5.4 Größenordnungen gehören in den Fließtext
Zahlen, die ein Argument tragen, stehen im Text, gerundet und in einem Satz. Beispiel: „Bei 0,6 V Durchlassspannung beträgt das Feld im neutralen n-Gebiet 0,09 V/cm. Über 100 µm fallen weniger als 1 mV ab; fast die ganze Spannung liegt an der Raumladungszone.“

Solche Zahlen entscheiden Fragen, die Worte allein offenlassen. Die vollständige Rechnung steht auf der Beispiel-Seite.

### 5.5 Die höheren Module leiten vollständig her
Wo das Grundstudium etwas nur plausibel macht, leitet das Fachmodul es vollständig her. Ein Fachmodul (GEMB) ist bei einem Thema **mindestens so tief** wie das Grundstudium (ET1) beim selben Thema.

Pflicht-Herleitungen in der ausführlichen GEMB-Fassung zum pn-Übergang:
- U_Diff aus J_n = 0
- Weite der Raumladungszone aus der Poisson-Gleichung
- Gesetz des Übergangs
- Minoritätsprofil aus der Kontinuitätsgleichung
- Shockley-Gleichung mit I_S
- Sperrstrom als Generationsstrom
- Sperrschichtkapazität

ET1 darf das Zwei-Ströme-Bild benutzen und für die vollständige Herleitung auf GEMB verweisen. Beide erklären ihr Thema dennoch von Grund auf (§3.4).

### 5.6 Präzise Sprache
- **Eindeutige Symbole:** Jedes Symbol hat genau eine Bedeutung. Steht e für die Elementarladung, schreibst du die Exponentialfunktion als `\exp(…)` und die Eulersche Zahl als `\exp(1)`, nie e^{eU/kT} oder „Faktor e“.
- **Richtungen:** Teilchenfluss und Stromrichtung trennst du immer ausdrücklich. Bei Elektronen sind sie entgegengesetzt.
- **Konventionen zuerst:** Vorzeichen- und Zählpfeilkonventionen stehen vor der ersten Formel.
- **„Positiv“ und „negativ“** werden erklärt, wenn sie mehr als ein Vorzeichen meinen.
- **Messbare Aussagen:** Was passiert, steht als messbare Aussage da, mit Größe und Größenordnung, nicht als Stimmungsbild.

### 5.7 Skriptkritik
Wo das Skript falsch oder ungenau ist, benennst du es mit Seitenzahl und korrigierst es mit Begründung. Das ist ein Kernwert der Seite.

### 5.8 Konsistenz
Zahlen, Beispielsysteme und Bezeichnungen derselben Größen sind innerhalb eines Oberthemas, über Module hinweg und zwischen den beiden Fassungen gleich. Wo das Skript anders bezeichnet, sagst du es.

### 5.9 Die Akteure benennen
Vor jeder Kernformel und vor jedem Mechanismus steht die Liste **„Die Akteure:“**. Sie nennt jede beteiligte Größe bzw. jedes Objekt mit:
- Symbol und Bedeutung in einem halben Satz;
- Einheit, bei mathematischen Objekten Definitions- und Zielraum (z. B. γ: [a, b] → ℝⁿ);
- typischer Größenordnung im Beispielsystem, wo es eine gibt;
- Rolle im Mechanismus: Was treibt, was bremst, was wird gezählt?

Eine schon eingeführte Größe wird in einer späteren Liste nur genannt, nicht neu beschrieben. Symbole stehen als Namen `__$…$__` (der Build hebt sie hervor). Danach folgt **„Das Zusammenspiel:“** mit dem Mechanismus.

**Beispiel:**

*Wie hoch muss die Potentialstufe sein, damit Drift und Diffusion der Elektronen sich genau aufheben?*

**Die Akteure:**
- __$n_{n0}$__, __$n_{p0}$__: Elektronendichte im neutralen n- bzw. p-Gebiet; in cm⁻³; 10¹⁶ bzw. 10⁴. Ihr Unterschied treibt die Diffusion.
- __$\varphi(x)$__: elektrisches Potential; in V. Gesucht ist seine Stufe $U_\mathrm{Diff}$ über der Raumladungszone.
- __$U_T = kT/e$__: Temperaturspannung; 25,85 mV bei 300 K. Eine Potentialstufe der Höhe $U_T$ ändert die Elektronendichte im Gleichgewicht um den Faktor $\exp(1) \approx 2{,}72$.

**Das Zusammenspiel:** Das Dichtegefälle treibt Elektronen ins p-Gebiet. Jedes abgewanderte Elektron lässt einen positiv geladenen Donatorrumpf zurück. Die entstehende Raumladung baut ein Feld auf, das Elektronen zurücktreibt. Der Netto-Zustrom endet, wenn nach Boltzmann nur noch ein Elektron von 10¹² die Stufe überwinden kann, so viele, wie dem Dichteverhältnis entspricht:

$$U_\mathrm{Diff} = U_T \ln\frac{n_{n0}}{n_{p0}} = 25{,}85\ \mathrm{mV}\cdot\ln(10^{12}) = 0{,}714\ \mathrm{V}.$$

(Zusammenhänge stehen auch hier auf eigener Zeile, Bauplan §2; im Fließtext stehen nur Zahlen und kurze Angaben wie $U = 0{,}6\ \mathrm{V}$.)

### 5.10 Abstrakte Ausdrücke erst anschaulich, dann formal
Entscheidung des Users vom 22.10.2026: Jeder abstrakte Ausdruck wird zuerst so anschaulich und einfach wie möglich erklärt; erst danach wird er formal eingeführt und benutzt. Abstrakt heißt hier: ein Symbol, das für eine Operation, eine Zuordnung oder ein allgemeines Objekt steht und sich beim ersten Lesen nicht vorstellen lässt.

**Reihenfolge beim ersten Auftreten, in beiden Fassungen:**
1. **Ein einfacher, konkreter Fall:** Was der Ausdruck tut, zeigt ein Beispiel mit Zahlen oder einem vertrauten Vorgang, noch ohne die allgemeine Schreibweise.
2. **Die Bedeutung in Worten:** ein Satz, was der Ausdruck allgemein ist, ohne neue Fachwörter.
3. **Die formale Schreibweise** mit allen Symbolen (Akteure, §5.9); ab hier wird sie benutzt.
4. **Eigenschaften und Sätze** erst danach, jeweils an den einfachen Fällen aus Schritt 1 geprüft.

**Beispiel (ET3, Signale und Systeme):** In $g(t) = \mathrm{Tr}(s(t))$ wirkt $\mathrm{Tr}(\cdot)$ zunächst leer; man kann sich nicht vorstellen, was gemeint ist.
- *Erst:* Ein System verändert sein Eingangssignal auf irgendeine Weise. Es multipliziert es etwa mit 3, dann wird aus $s(t) = \sin t$ das Signal $3\sin t$; oder es addiert 5, dann wird aus $s(t)$ das Signal $s(t) + 5$.
- *Dann:* $\mathrm{Tr}(\cdot)$ ist nichts anderes als der Name für diese Veränderung, die das System am Eingangssignal vornimmt, und $g(t)$ ist das veränderte Signal.
- *Danach:* Eigenschaften wie Linearität und Zeitinvarianz als Eigenschaften von $\mathrm{Tr}$, an denselben Beispielen geprüft: „mal 3“ ist linear, „plus 5“ nicht, weil die 5 bei einer Summe zweier Signale nur einmal statt zweimal hinzukommt.

**Gilt entsprechend für:**
- Operatoren und Transformationen: $\nabla$, div, rot, Fourier- und Laplace-Transformation, Faltung, Erwartungswert, Normen;
- Abbildungen und Mengen: $f: D \to \mathbb{R}$, Kurven, Wahrscheinlichkeitsmaße, Zufallsvariablen;
- Matrizen und Vektoren als Ganzes, etwa $A\vec x = \vec b$;
- Kurzschreibweisen der Elektrotechnik, etwa Zeiger, Übertragungsfunktion, Rückkopplungsfaktor.

Ein konkreter Fall ersetzt keine Definition; er geht ihr voraus, damit die Definition etwas beschreibt, das die Leserin schon vor Augen hat.

### 5.11 Zusammenhänge zusätzlich in einem einfachen Satz
Entscheidung des Users vom 22.10.2026: Wo eine Formel oder Definition einen Zusammenhang ausdrückt, der sich in einem kurzen Satz in einfacher Sprache sagen lässt, steht dieser Satz zusätzlich da. Vorbild des Users aus ET3:
- **Linearität:** „Die Transformation der Summe ist gleich der Summe der Transformationen.“
- **Zeitinvarianz:** „Die Transformation der Verschiebung ist gleich der Verschiebung der Transformation.“

**Regeln:**
- **Nur, was ohne Ausnahme stimmt.** Der Satz ist bewiesen: im Artikel hergeleitet oder ein gesicherter Standardsatz. Seine Bedingungen nennt er mit („bei gleicher Einheit“, „für Kräfte, die nur vom Ort abhängen“). Gibt es an einer Stelle keinen solchen Satz, steht keiner da; nichts erzwingen.
- **Ergänzen, nicht ersetzen.** Formel bzw. Definition, Akteure, „So liest man das“ und Herleitung bleiben vollständig; der Satz kommt hinzu.
- **Ort und Form:** eine eigene Zeile **„Kurz gesagt:“** direkt nach „So liest man das“ bzw. nach der Erklärung einer Definition, ein bis zwei Sätze, in beiden Fassungen gleich. In einer Herleitung steht der Satz an dem Schritt, der ihn benutzt.
- **Aktiv suchen:** Bei jeder Formel und Definition prüfen, ob sie einen solchen Zusammenhang enthält. Typische Muster:
  - **Vertauschen zweier Operationen:** „Die Ableitung der Summe ist die Summe der Ableitungen.“ „Die Einheit des Produkts ist das Produkt der Einheiten.“
  - **Zerlegen:** „Die Arbeit über den ganzen Weg ist die Summe der Arbeiten über seine Stücke.“
  - **Umkehren:** „Integrieren macht das Ableiten rückgängig.“ „Die Arbeit auf dem Rückweg ist das Negative der Arbeit auf dem Hinweg“ (für Kräfte, die nur vom Ort abhängen).
  - **Überlagern:** „Die Antwort einer linearen Schaltung auf die Summe zweier Quellen ist die Summe ihrer Antworten.“
  - **Skalieren:** „Doppelter Abstand, ein Viertel der Kraft“, nur wenn die Proportionalität exakt gilt.
- **Gegenprobe:** Muster, die richtig klingen, aber falsch sind, gibt es oft; die Ableitung eines Produkts ist zum Beispiel **nicht** das Produkt der Ableitungen. Jeden Satz deshalb an einem Zahlenbeispiel aus dem Zahlenwerk prüfen.

## 6. Vorgaben für Herleitungen

Herleitungen stehen weiterhin **im eigenen, ausklappbaren Kasten** `:::herleitung` … `:::`. Ihre Länge belastet den Hauptpfad nicht, aber auch im Kasten steht kein überflüssiger Satz. Die kompakte Fassung übernimmt die Kästen ihrer Kernformeln unverändert aus der ausführlichen; nur ein „Zweiter Weg“, der auf Abschnitte allein der ausführlichen Fassung verweist, entfällt dort. Deshalb stützt sich der erste Weg jedes übernommenen Kastens nur auf Inhalte, die auch die kompakte Fassung erklärt.

### 6.1 Was hergeleitet wird
- **Alles, was keine Definition ist** (Bauplan §1 Nr. 7): jede Formel, Regel, Identität, Näherung, Abschätzung, jeder Satz und Spezialfall, der in der Fassung vorkommt.
- **Definitionen** bekommen statt einer Herleitung einen Satz, warum man sie so definiert.
- **Beweise über dem Kursrahmen:** Geht ein Beweis klar darüber hinaus, enthält der Kasten die Beweisidee und den ausdrücklichen Hinweis darauf.

### 6.2 Was außerhalb des Kastens steht
- **Die Ergebnisformel** (als `:::formel` oder `$$…$$`) und „So liest man das“ stehen unmittelbar davor.
- **„Idee der Herleitung: …“** nennt in einem Satz das Prinzip des Weges. Beispiel: „Man setzt Drift- und Diffusionsstrom gleich und integriert über die Zone.“

### 6.3 Aufbau im Kasten, immer in dieser Reihenfolge
1. **Ausgangspunkt:** das Grundgesetz bzw. die Definition mit Namen, etwa „Poisson-Gleichung“ oder „Elektronenstromgleichung (Drift plus Diffusion)“. Ein Ergebnis aus einem anderen Artikel ist nur erlaubt, wenn es dort tatsächlich hergeleitet ist; dann mit Link.
2. **Annahmen:** nummeriert (i), (ii), …, jeweils mit physikalischer Bedeutung und Gültigkeitsbereich. Beispiel: „(ii) schwache Injektion: Die Randdichten bleiben klein gegen die Dotierung, bei der Beispieldiode bis etwa 0,65 V.“
3. **Schritte:** `**Schritt 1**: …`, `**Schritt 2**: …`.
   - Jeder Schritt hat einen Satz Begründung („Einsetzen von …“, „weil … konstant ist“, „mit der Einstein-Beziehung“) und eine Formelzeile `$$…$$`.
   - Jede Umformung ist sichtbar; „nach kurzer Rechnung“ gibt es nicht.
   - Bei Ableitungen steht, was konstant gehalten wird; bei Integralen, worüber und in welchen Grenzen integriert wird.
   - Der Schritt, an dem die Idee greift, wird als **entscheidender Schritt** markiert.
4. **Ergebnis:** die Endformel, identisch mit der sichtbaren Formel.
5. **Woher die Faktoren kommen:** welcher Schritt welchen Faktor liefert. Hier steht nur, was die Herleitung zusätzlich zeigt; die Deutung steht in „So liest man das“.
6. **Proben:** Einheit, mindestens ein Grenz- oder Spezialfall, Vorzeichen und der Zahlenwert aus dem Zahlenwerk, der zum Beispiel passt.
7. **Grenzen:** wann die Annahmen versagen und was dann passiert, in einem Satz mit Verweis.

### 6.4 Länge und Zuschnitt
- **Teilen:** Ab etwa zwölf Schritten teilst du an einem natürlichen Zwischenergebnis in zwei Kästen. Das Zwischenergebnis wird eine eigene, benannte Formel.
- **Zweiter Weg:** Gibt es einen zweiten aufschlussreichen Weg, steht er in der ausführlichen Fassung als „Zweiter Weg:“ im selben Kasten, nach dem ersten. Beispiel: U_Diff über J_n = 0 und über gleiche Fermi-Niveaus.

### 6.5 Verboten
- **Verweis-Herleitung:** „Nach dem vorigen Artikel gilt …“, ohne dass dort hergeleitet wird.
- **Übersprungene Schritte:** „Summiert man …, ergibt sich …“.
- **Zirkelschluss:** das Ergebnis benutzen, um es herzuleiten.
- **Unerklärte Symbole:** neue Symbole ohne Einführung.
- **Falsche Form:** Formelketten im Fließtext (Bauplan §2) und verschachtelte Blöcke im Kasten.

## 7. Vorgaben für Abbildungen

### 7.1 Zweck
Eine Abbildung zeigt das Konzept, auf dem der Text dann aufbaut. Was man sehen kann, soll man sehen: Profile, Kennlinien, Felder, Schaltungen, Abläufe, Geometrie. Eine gute Abbildung ersetzt Absätze, statt sie zu ergänzen. Jede beantwortet eine Frage und hat eine Kernaussage.

### 7.2 Häufigkeit
- **Einstiegsabbildung:** Jede Fassung hat genau eine, in „Worum es geht“. Sie zeigt das zentrale Objekt oder den zentralen Mechanismus.
- **Sach-Abschnitte:** In jedem Sach-Abschnitt steht mindestens eine Abbildung, sobald er einen Mechanismus, ein Orts- oder Zeitprofil, eine Kennlinie, eine Schaltung, ein geometrisches Objekt oder eine Gegenüberstellung behandelt.
- **Kipp-Stellen:** Zu jeder gehört mindestens eine Abbildung, oft eine Abfolge, etwa Gleichgewicht, Durchlass und Sperr nebeneinander.
- **Formeln:** Jede `:::formel`, die einen Zusammenhang zwischen Größen beschreibt, bekommt einen Graphen mit den Werten des Beispielsystems. Ausnahme: Der Zusammenhang ist trivial oder schon in einer anderen Abbildung zu sehen.
- **Schaltungen:** Jede besprochene Schaltung bekommt ihr Schaltbild.
- **Richtwert:** eine Abbildung je 300 bis 500 Wörter Hauptpfad.
  - kompakte Fassung: etwa 3 bis 6 Abbildungen;
  - ausführliche Fassung: etwa 6 bis 12 Abbildungen.
- **Gemeinsame Szenen:** Beide Fassungen benutzen dieselben Abbildungen, also dieselben Szene-IDs. Die Nummer in der Bildunterschrift zählt je Fassung neu.
- **Platzhalter zählen:** Solange eine Abbildung nur als Platzhalter steht (§7.5), zählt sie für diese Richtwerte voll.
- **Beispiele:** Abbildungen dürfen auch in Beispielen stehen, wenn das Beispiel ein Bild braucht, etwa Arbeitsgerade und Arbeitspunkt.

### 7.3 Inhalt: welche Abbildung wofür

| Inhalt im Text | Abbildung |
|---|---|
| Ladungsverteilung, Entstehung einer Zone | Querschnitt mit festen Ionen, beweglichen Ladungsträgern und Feldpfeilen; Entstehung als Abfolge von zwei bis drei Zuständen |
| Größen über dem Ort | gestapelte Profile mit gemeinsamer x-Achse (Dichten logarithmisch, Raumladung, Feld, Potential, Bänder), berechnet |
| Energieverhältnisse, Barrieren | Banddiagramm mit Ladungsträgern und Flusspfeilen, mehrere Fälle nebeneinander |
| Kennlinien | linear und halblogarithmisch nebeneinander; Arbeitspunkt mit Arbeitsgerade; Kennlinienschar mit benanntem Parameter |
| Größe hängt von zwei Variablen ab | zwei Schnitte mit gemeinsamer Achse (wie das Kennlinienfeld als zwei Schnitte) |
| Schaltungen | Schaltbild mit allen Bauteilen und Werten, Zählpfeilen und benannten Knoten |
| Zeitverhalten | Zeitverläufe mit markierten Phasen und Zeitkonstanten |
| Wechselgrößen | Zeigerdiagramm bzw. komplexe Ebene, daneben der Zeitverlauf |
| Felder | Feldlinien und Äquipotentiallinien |
| Extreme Verhältnisse | logarithmische Skalen (etwa 10¹⁶ gegen 10⁴) |
| Mathematik | Funktionsgraphen, Höhenlinien mit Gradienten, Kurven mit Tangente, Integrationsgebiete schraffiert, Vektorfelder, Flächen mit Normalen, Folgen von Funktionsgraphen bei Konvergenz |
| Strukturgleiche Analogie | Zwillingsdarstellung, etwa Luftdichte über der Höhe neben Elektronendichte über der Energie |

### 7.4 Gestaltung
Diese Regeln gelten für die fertige Editor-Abbildung. Bildbeschreibung und Listeneintrag (§7.5) legen sie schon beim Schreiben fest: Daten, Achsen, Farben und Kernaussage.

- **Echte Daten.** Kurven werden aus dem Zahlenwerk berechnet, nicht frei gezeichnet. Schematische Abbildungen tragen den Zusatz „schematisch“, und die Bildunterschrift sagt, was überzeichnet ist (etwa „thermische Energien stark vergrößert“).
- **Achsen.** Jede Achse trägt Größe und Einheit, etwa „I in mA“. Ein Diagramm hat nie zwei y-Achsen; zwei Größen mit verschiedenen Einheiten stehen in zwei gestapelten Diagrammen mit gemeinsamer x-Achse.
- **Beschriftung.** Wo möglich direkt an den Kurven statt in einer Legende, auf Deutsch und auch bei 360 px Breite lesbar.
- **Farben mit fester Bedeutung.** Wo Ladungsträger vorkommen: Elektronen blau, Löcher rot, Minoritätsträger orange, Feldpfeile grün, Raumladungszone grau hinterlegt (wie im Lernskript). Sonst folgen die Farben der Palette der Webseite. Text und Achsen sind dunkelgrau, nicht in Kurvenfarben.
- **Stil.** Dünne Linien, keine 3D-Effekte, keine Cliparts, keine Figuren, weißer Hintergrund. So bleibt das Bild im Nachtmodus als helle Karte lesbar.
- **Bildunterschrift.** Sie beginnt mit „Abbildung n:“, sagt, was gezeigt ist, und endet mit der Kernaussage in einem Satz. Sie wiederholt nicht den Text.
- **Der Text baut auf der Abbildung auf.**
  - Die Abbildung steht vor der Erklärung, die sie benutzt.
  - Der Text verweist ausdrücklich darauf („Abbildung 3 zeigt …“).
  - Er führt durch sie hindurch: worauf man links, in der Mitte und rechts achten muss und was daraus folgt.
  - Was man ohnehin sieht, beschreibt er nicht noch einmal vollständig.

### 7.5 Herstellung: nur mit dem Editor
**Entscheidung des Users (21.10.2026):**
- In den Artikeln stehen nur Abbildungen, die der EtUndSo-Editor erzeugt.
- Keine Bilddateien aus anderen Werkzeugen, also kein matplotlib und kein handgeschriebenes SVG.
- Die nötigen Editor-Funktionen und die Abbildungen selbst entstehen **nach** den Artikeln, in einer eigenen Phase mit dem User und nicht im Loop, weil neue Features oft Probleme machen.

**Beim Schreiben entstehen für jede Abbildung drei Dinge:**
1. **Der Platzhalter im Artikel,** an der Stelle, an der die Abbildung stehen wird:
   ```
   :::grafik
   Szene: <modul>/<kapitel>/<nr>-<name> · Vorlage: <vorlage>
   **Abbildung n:** <Was gezeigt ist, mit den wichtigsten Zahlen.> <Kernaussage in einem Satz.>
   :::
   ```
   - Die **Szene-ID** ist eindeutig und in beiden Fassungen gleich, zum Beispiel `get1/halbleiterbauelemente/01-teilstroeme`.
   - Die **Vorlage** nennt den Abbildungstyp, zum Beispiel `kennlinie-semilog` oder `banddiagramm-parameter`.
   - Die **Bildbeschreibung** ist sichtbar; der Build zeigt sie als „Abbildung in Vorbereitung“.
     - Sie beginnt mit „**Abbildung n:**“.
     - Sie sagt, was gezeigt ist, mit den wichtigsten Zahlen.
     - Sie endet mit der Kernaussage.
     - Solange das Bild fehlt, muss der Text mit ihr verständlich bleiben.
2. **Ein Eintrag in `ABBILDUNGEN_LISTE.md`:**
   - Szene-ID, Fassung(en) und Nummer;
   - Inhalt mit allen Zahlen, Wertebereichen, Achsen und Farben (§7.4);
   - Kernaussage;
   - Datenquelle: die Funktion im Zahlenwerk, die die Kurve liefert;
   - benötigte Editor-Funktionen mit Verweis auf die Abschnitte von `EDITOR_GRAFIK_FEATURES.md`;
   - wo sinnvoll die Animationsidee: was sich bewegt, was interaktiv ist;
   - Status „offen“.
3. **Neue Editor-Funktionen,** die noch nicht in `EDITOR_GRAFIK_FEATURES.md` stehen, bekommen dort einen eigenen Abschnitt mit „Gebraucht in“.

**Nicht mehr nötig:** Abbildungs-Skripte und Referenzentwürfe. Die matplotlib-Entwürfe des Piloten liegen nur noch als Vorlage in `notizen/get1/abb_referenz/`.

## 8. Vorgaben für Beispiele (Beispiel-Seite)

### 8.1 Wo sie stehen
Wie im Bauplan §3a als `::::beispiel <Titel>` … `::::`, direkt hinter der Formel oder Aussage, die sie zeigen.
- Nie zwei Beispiele direkt hintereinander; dann wird es ein Beispiel mit Teilen **(a)**, **(b)**.
- Im Text steht nie „Beispiel 3“; verwiesen wird über den Inhalt.

### 8.2 Aufbau eines Beispiels
1. **Titel:** sachlich; er sagt, was berechnet oder gezeigt wird, zum Beispiel „Driftgeschwindigkeit in einem Kupferdraht bei 1 A“.
2. **Gegeben:** alle Größen mit Wert, Einheit und Herkunft (Zahlenwerk, Datenblatt, Skript-Annahme). Jedes Beispiel ist selbsttragend und nennt die Werte selbst.
3. **Gesucht:** in einem Satz.
4. **Rechnung:** jeder Schritt auf eigener Zeile (`$$…$$`), davor ein halber Satz Begründung. Einheiten werden mitgeführt, Zwischenwerte auf drei gültige Stellen gerundet.
5. **Ergebnis:** eine Zeile, fett.
6. **Einordnung:** Was bedeutet diese Zahl? Ein Vergleich mit einer anderen Größe, der Intuition oder einer Fehlvorstellung, dazu die Plausibilität der Größenordnung. Die Formel wird hier nicht noch einmal gedeutet.
7. **Optional „Variation“:** Was ändert sich, wenn man eine Größe ändert? Mit einem nachgerechneten Wert, etwa: „Doppelter Strom (2 mA statt 1 mA) halbiert r_d von 26 Ω auf 13 Ω.“

### 8.3 Welche Beispiele die ausführliche Fassung braucht
- zu **jeder `:::formel`** ein Zahlenbeispiel;
- zu **jeder Kipp-Stelle** ein Beispiel, das die tragende Zahl aus dem Fließtext vollständig nachrechnet;
- zu **jeder Fehlvorstellung** möglichst ein Beispiel, das sie mit einer Zahl widerlegt, etwa: „Bei 0,4 V fließen durch die Beispieldiode 76 nA. Es fließt also Strom, nur wenig.“;
- wo möglich ein **Praxisbeispiel** mit realem Bauteil und Datenblattwert (BC547C, 1N4148, Audioverstärker, Netzteil, Oszilloskop);
- wo eine Aussage „nicht immer“ gilt, ein **Gegenbeispiel** mit Rechnung.

Ein Beispiel darf mehrere dieser Zwecke zugleich erfüllen. Besser wenige vollständige Beispiele an einem durchgehenden System als viele kleine.

**Kompakte Fassung:** zwei bis vier Beispiele, in dieser Reihenfolge der Wichtigkeit:
1. die zentrale Formel;
2. die tragende Zahl der wichtigsten Kipp-Stelle;
3. ein Praxisbeispiel.

### 8.4 Regeln
- **Eigene Beispiele:** Keine Aufgaben aus Skript, Übung oder Klausur übernehmen (Leitfaden §11).
- **Zahlenwerk:** Alle Zahlen stammen aus dem Zahlenwerk (§10). Dasselbe Beispielsystem zieht sich durch das Thema.
- **Erlaubte Blöcke:** Im Beispiel sind `:::herleitung` und Abbildungen erlaubt, aber keine `:::formel`-Boxen und keine `##`-Überschriften (Bauplan §3a).

## 9. Vorgaben für die Kästen

### 9.1 `:::analogie` … `:::`
Eine Analogie ist ein Werkzeug zur Orientierung, kein Erzählrahmen.
- **Häufigkeit:** In der ausführlichen Fassung meist eine, höchstens zwei, an einer Kipp-Stelle oder in `## Das Bild`. In der kompakten Fassung höchstens eine, an einer Kipp-Stelle.
- **Aufbau:**
  1. **Der Vergleich** in zwei bis vier Sätzen: was was entspricht und welcher gemeinsame Mechanismus den Vergleich trägt.
  2. **Die Zuordnung**, bei mehr als zwei Größen als Tabelle „Im Vergleich | In der Physik“.
  3. **„Wo der Vergleich nicht stimmt:“** in ein bis zwei Sätzen.
- **Strukturgleich:** Gute Analogien haben dieselbe Mathematik oder denselben Mechanismus. Die beste Sorte sind echte physikalische Parallelen:
  - Raumladungszone und Erdatmosphäre: Kraft gegen Wärmebewegung, die Dichte fällt exponentiell mit der potentiellen Energie;
  - Potential und Höhe im Schwerefeld;
  - Kondensator und Federspeicher;
  - Sperrstrom und ein Wasserfall, dessen Durchfluss der Zufluss begrenzt, nicht die Fallhöhe;
  - Differenzverstärker und Balkenwaage.

  Hydraulische Netzwerkanalogien sind erlaubt, wenn ihre Grenzen genannt sind.
- **Danach** geht es mit der Physik weiter. Die Analogie wird später nur dort aufgegriffen, wo sie einen weiteren Punkt **richtig** erklärt, und nie in einen Bereich getragen, in dem sie falsch wird.

### 9.2 `:::fehlvorstellung` … `:::`
Steht an der Stelle, an der die Fehlvorstellung entsteht. Aufbau:
1. **Die falsche Idee** in Anführungszeichen, in den Worten der Leserin.
2. **Warum sie naheliegt**, in einem Satz.
3. **Was stimmt.**
4. **Das entscheidende Argument**, am besten eine Zahl oder ein Herleitungsergebnis, mit Verweis auf den Abschnitt, der es ausführt.

### 9.3 `:::frage` … `:::` (ausklappbar)
Nach dem Vorbild der Frage-Kästen im Lernskript: Fragen, die sich an einer Stelle aufdrängen, werden genau dort beantwortet. Beispiel: „Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“
- **Darstellung:** Die erste Zeile ist die Frage in Anführungszeichen. Der Build zeigt sie als Überschrift des Kastens; die Antwort öffnet sich per Klick.
- **Wortlaut der Frage:** so, wie eine Person sie an dieser Stelle tatsächlich stellen würde. Die echten Fragen aus dem Fragenkatalog (§10) sind die beste Quelle. Sie darf eine falsche Vermutung enthalten; dann korrigiert die Antwort sie ausdrücklich.
- **Antwort:**
  - zwei bis sechs Sätze;
  - der Mechanismus und eine Zahl;
  - ein Verweis auf den Abschnitt, falls dort mehr steht.
- **Inhalt:** Hintergrund (H), naheliegende Zweifel, Abgrenzungen und Verbindungen zu anderen Themen. **Nie Kernstoff (K):** Was jede Person zum Verständnis braucht, steht im Text. Er darf sich nicht hinter einem Klick verstecken.
- **Position:** direkt hinter dem Satz oder der Abbildung, bei der die Frage entsteht, nicht gesammelt am Abschnittsende.
- **Nur echte Fragen,** keine rhetorischen und keine Wissensabfragen; die gehören ins Quiz.
- **Anzahl:** in der ausführlichen Fassung etwa 4 bis 8, in der kompakten 2 bis 4, selten mehr als zwei pro Abschnitt.

### 9.4 `:::merke` … `:::`
Für eine Aussage, die man genau an dieser Stelle festhalten muss. Höchstens drei pro Artikel, keine Wiederholung des Kernteils.

### 9.5 `:::vertiefung` … `:::` (nur ausführlich)
Für V-Inhalte und lange H-Inhalte (§3.2), die den Lesefluss unterbrechen würden.
- **Titel:** Die erste Zeile ist ein fetter Titelsatz, der sagt, was der Kasten erklärt. Beispiel: „**Warum man die Diffusionsspannung nicht messen kann.**“
- **Inhalt:** Ein Vertiefungskasten enthält nie etwas, das der Hauptpfad braucht.
- **Anzahl:** höchstens drei pro Artikel.

**Obergrenzen:**
- **Fehlvorstellungen:** in der ausführlichen Fassung höchstens vier, in der kompakten höchstens zwei.
- **Merke:** höchstens drei bzw. einer.
- **Frage-Kästen:** Die Anzahl steht in §9.3.

## 10. Vor dem Schreiben: die Arbeitsnotiz (Pflicht, eine pro Thema)

Lege vor jedem Thema im Repo `notizen/<modul>/notiz_<slug>.md` an und committe sie mit den Artikeln. Inhalt:

1. **Ein-Satz-Prinzip.** Beispiel pn-Übergang: „Ein Gleichgewicht zweier Teilchenströme über eine Barriere; die Spannung verändert nur die Höhe der Barriere, und die beiden Ströme reagieren völlig verschieden darauf.“
2. **Schwierigkeit und Längenspannen** beider Fassungen (§3.3), mit einem Satz Begründung.
3. **Vorwissen-Kette.** Was muss die Person können, bevor sie den Kern versteht? Zu jedem Punkt notierst du entweder „erklärt in Artikel X“ (nur erinnern und verlinken) oder „hier aufbauen“.
4. **Fragenkatalog.** 10 bis 15 Fragen in den Worten einer Person, die vom Thema nichts weiß. Mindestens drei davon sind Fehlvorstellungen. Zu jeder Frage notierst du drei Dinge:
   - die Stelle, an der sie entsteht;
   - den Antwortort: im Text, wenn die Antwort Kernstoff ist; sonst Frage-Kasten oder Fehlvorstellungs-Kasten;
   - die Fassung.

   Echte Beispiele aus Gesprächen mit dem User:
   - „Die Atomrümpfe in der Raumladungszone sind doch neutral, wie können sie wirken?“
   - „Stößt in Durchlassrichtung der Pluspol die Löcher über die Barriere?“
   - „Wenn man U_CE anlegt, entsteht dadurch I_C.“
   - „Unter 0,7 V fließt kein Strom.“
   - „Wie kann ein Anschluss positiv sein, der Leiter ist doch neutral?“
   - „Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“

   Quellen für weitere Fragen:
   - die eigene Prüfung („Wo hätte ich als Anfänger gehakt?“);
   - Schwachstellen des Skripts;
   - Lehrbücher;
   - die Übungen.
5. **Kipp-Stellen.** Ein bis drei Stellen, an denen das Verständnis kippt. Plane für jede:
   - Schritte;
   - Akteure;
   - Abbildungen;
   - tragende Zahlen;
   - Herleitung;
   - Beispiel;
   - gegebenenfalls eine Analogie.
6. **Aussortier-Liste.** Alle möglichen Inhalte mit Kategorie K, H, V oder S (§3.2) und mit der Angabe, in welche Fassung sie kommen und wohin dort (Abschnitt, Kasten, Beispiel).
7. **Abbildungsplan.** Alle Abbildungen mit Nummer, Szene-ID, Vorlage, Inhalt, Kernaussage und Abschnitt, mit Vermerk, welche davon die kompakte Fassung benutzt. Geprüft gegen §7.2. Aus dem Plan entstehen die Platzhalter und die Einträge in `ABBILDUNGEN_LISTE.md` (§7.5).
8. **Zahlenwerk.**
   - Ein konsistentes Beispielsystem pro Oberthema, berechnet mit `notizen/<modul>/zahlen_<oberthema>.py`; die Ausgabe steht in `zahlen_<oberthema>.txt`.
   - Das Skript legst du beim ersten Thema des Oberthemas an und erweiterst es danach.
   - Jede Zahl in Text, Abbildungen, Beispielen und Quiz stammt daraus.
9. **Profi-Abgleich.** Ein bis zwei Fachquellen (Lehrbuch, Vorlesung, WebSearch), um Physik bzw. Mathematik zu prüfen und den besten Erklärweg zu finden. Die Quellen nennst du im Bericht an den User.
10. **Skript-Abgleich.** Zwei Listen mit Seitenzahl:
    - alle Definitionen, Formeln und Aussagen des Quellabschnitts, für die Vollständigkeit;
    - alle Fehler und Ungenauigkeiten des Skripts.

## 11. Selbstprüfung vor dem Commit (für jede Fassung, zusätzlich zu Bauplan §8)

Das Ergebnis kommt in die Zeile in `REVIEW_OPUS55.md`.

1. **Neuling-Test.** Lies die Fassung als Person, die über das Thema nichts weiß.
   - Markiere jeden Begriff, jedes Symbol und jede Tatsache, die benutzt wird, bevor sie erklärt ist.
   - Markiere jeden Schritt ohne Grund.
   - Markiere jeden abstrakten Ausdruck (Operator, Abbildung, allgemeines Symbol), der formal dasteht, bevor ein einfacher, konkreter Fall gezeigt hat, was er tut (§5.10).
   - Beantworte jede Frage des Fragenkatalogs, die zur Fassung gehört, aus ihrem Hauptpfad und notiere den Abschnitt.
   - Ergänze, wo nötig.
2. **Umfang-Test.** Der Hauptpfad liegt in der Spanne aus der Arbeitsnotiz (`tools/artikel_kennzahlen.py`). Liegt er darüber, gilt §3.3.
3. **Doppelungs-Test.**
   - Wird jeder Mechanismus und jede Tatsache genau einmal erklärt?
   - Überschneiden sich „Worum es geht“, die Prinzip-Tabelle und der Kernteil?
   - Erzählen Kästen den Text nach?
   - Beschreibt der Text Abbildungen vollständig, statt durch sie zu führen?
4. **Fassungs-Test.**
   - Die kompakte Fassung enthält jeden K-Inhalt, ist neu geschrieben (kein Zusammenschnitt) und hat den Absatz „In der ausführlichen Fassung“.
   - Die ausführliche Fassung enthält alle K-, H- und V-Inhalte der Aussortier-Liste.
   - Zahlen, Symbole und Abbildungen (Szene-IDs) sind in beiden gleich.
5. **Listen-Test.** Kein Listenpunkt enthält eine Erklärung, die als Fließtext stehen müsste.
6. **Ton-Test.**
   - Gibt es Figuren, Szenen, vermenschlichte Teilchen, verspielte Titel oder niedliche bzw. reißerische Bilder?
   - Steht ein Wort der Verbotsliste aus §5.1 im Text?
   - Gibt es einen Satz ohne Information?
7. **Gerüst-Test.** Alle Bestandteile aus §4 sind vorhanden und stehen in der richtigen Reihenfolge.
8. **Akteure-Test.** Vor jeder Kernformel und jedem Mechanismus stehen die Akteure mit Einheit bzw. Raum und Größenordnung, ohne Wiederholungen.
9. **Kipp-Stellen-Test.** Jede Kipp-Stelle ist in Schritten erklärt, mit Abbildung, tragender Zahl, Herleitung und Beispiel. Sie bekommt mehr Platz als die einfachen Teile.
10. **Herleitungs-Test.**
    - Jede nicht-definitorische Formel der Fassung hat einen Kasten nach §6.3.
    - Ausgangspunkt, Annahmen, Schritte, Ergebnis, Herkunft der Faktoren, Proben und Grenzen sind vorhanden.
    - Es gibt keine Verweis-Herleitung.
11. **Abbildungs-Test.**
    - Die Häufigkeit nach §7.2 ist erreicht; es gibt keine `<figure>`-Zeilen, nur Platzhalter `:::grafik`.
    - Jeder Platzhalter hat die Szene-Zeile und eine Bildbeschreibung mit Inhalt, wichtigsten Zahlen und Kernaussage. Ihre Zahlen stimmen mit dem Text und dem Zahlenwerk überein.
    - Jede Szene hat ihren Eintrag in `ABBILDUNGEN_LISTE.md` mit Inhalt, Daten, Achsen und benötigten Editor-Funktionen. Fehlende Funktionen sind in `EDITOR_GRAFIK_FEATURES.md` ergänzt.
    - Der Text führt durch jede Abbildung und bleibt mit der Bildbeschreibung allein verständlich.
12. **Beispiel-Test.** Die Beispiele erfüllen §8.3, und jedes hat Gegeben, Gesucht, Rechnung, Ergebnis und Einordnung.
13. **Zahlen-Test.** Jede Zahl stammt aus `zahlen_<oberthema>.txt`; Literaturwerte sind abgeglichen.
14. **Analogie-Test.** Die Höchstzahl ist eingehalten. Jede Analogie steht im Kasten, ist strukturgleich, hat Zuordnung und „Wo der Vergleich nicht stimmt“ und wird nirgends benutzt, wo sie falsch ist.
15. **Fragen- und Fehlvorstellungs-Test.**
    - Jede Frage des Katalogs ist an der Stelle beantwortet, an der sie entsteht.
    - Jede Fehlvorstellung ist in der ausführlichen Fassung aufgelöst, die wichtigsten auch in der kompakten; mindestens zwei kommen im Quiz vor.
    - Kein Frage-Kasten enthält Kernstoff, und jede Frage ist so formuliert, wie eine Leserin sie stellen würde.
16. **Ein-Satz-Test.** Das Prinzip steht in „Worum es geht“ und in „Alles hängt an einem Prinzip“, und jeder Abschnitt lässt sich darauf zurückführen.
17. **Sprach-Test.** Leitfaden §8, besonders:
    - Gedankenstrich-Dichte;
    - die Formel „nicht X, sondern Y“;
    - Ankündigungssätze.
18. **Modul-Test.** Ist dasselbe Thema in einem anderen Modul behandelt, ist dieser Artikel mindestens gleich tief und verlinkt dorthin.
19. **Zusammenhangs-Test (§5.11).**
    - Ist jede Formel und Definition darauf geprüft, ob sich ihr Zusammenhang in einem einfachen Satz sagen lässt?
    - Stimmt jeder „Kurz gesagt“-Satz ohne Ausnahme, mit seinen Bedingungen, und ist er an einem Zahlenbeispiel geprüft?
    - Ergänzt er die formale Erklärung, statt sie zu ersetzen?

## 12. Kalibrierung: schwach gegen gut

Die Fälle (a) bis (e) stammen aus einer Prüfung der Live-Artikel vom 21.10.2026, (f) und (g) aus den Rückmeldungen des Users zum Lernskript, (i) und (j) aus Vorgaben des Users vom 22.10.2026.

**(a) Mechanismus**
- *Schwach:* „In Sperrrichtung steigt die Barriere, die Diffusion versiegt, es bleibt nur ein winziger, spannungsunabhängiger Sättigungsstrom.“ Das Quiz fragt dann „Warum spannungsunabhängig?“, der Text sagt es nicht.
- *Gut:* in Schritten, mit Abbildung der Minoritätsprofile:
  1. Der Strom „hinauf“ fällt schon bei −0,1 V auf 2 % seines Gleichgewichtswerts.
  2. Am Rand der Zone ist die Minoritätsdichte deshalb praktisch null.
  3. Davor entsteht eine Delle, etwa eine Diffusionslänge breit (57 µm).
  4. In der Delle überwiegt die Generation.
  5. Der Strom ist die Netto-Generation in diesem Streifen: e·n_p0·L_n/τ_n = e·n_p0·D_n/L_n (hergeleitet).
  6. Mehr Sperrspannung macht die Randdichte nicht kleiner als null; deshalb ist der Strom konstant.

  In der ausführlichen Fassung kommt ein Analogie-Kasten dazu: ein Wasserfall, dessen Durchfluss der Zufluss begrenzt, nicht die Fallhöhe. Grenze des Vergleichs: Die Minoritätsträger wandern zufällig; der Netto-Fluss entsteht nur, weil an der Kante keiner zurückkommt.

**(b) Herleitung**
- *Schwach:* „Der Diffusionsstrom am Rand ist proportional zum Überschuss; summiert man den Elektronen- und den Löcherbeitrag, ergibt sich die Shockley-Diodengleichung.“
- *Gut:* Ausgangspunkt sind Kontinuitäts- und Stromgleichungen, dazu die Annahmen (i) bis (v). Dann die Schritte:
  1. Gesetz des Übergangs aus J_n ≈ 0 in der Zone. Begründung: Drift- und Diffusionsstromdichte sind dort je bis zu etwa 4·10³ A/cm² (numerisch; die Näherung mit scharf begrenzter Zone überschätzt sie mit 8·10³ A/cm²), der Netto-Strom bei 0,6 V nur 0,18 A/cm².
  2. Kontinuitätsgleichung im neutralen Gebiet, daraus Δn(x′) = Δn(0)·exp(−x′/L_n).
  3. Strom am Rand.
  4. Gleichheit mit der Rekombinationsrate.
  5. Summe beider Anteile.

  Am Ende stehen das Ergebnis, die Herkunft jedes Faktors von I_S, die Proben (Einheit, Sperrgrenzfall, Zahlenwert 1,46·10⁻¹⁴ A) und die Grenzen (starke Injektion, Bahnwiderstand).

**(c) Ton und Analogie**
- *Schwach (spielerisch):* „Das Leitbild bleibt: das Parkhaus mit der Rampe. Den Hinstrom bilden Autos, die die Rampe hinauffahren …“, fortgesetzt bis zu Autos, die beim Zener-Effekt durch eine Wand fahren.
- *Gut (sachlich):* ein Kasten mit dem Atmosphären-Vergleich, Zuordnungstabelle und Grenze, daneben eine Zwillingsabbildung (Luftdichte über der Höhe, Elektronendichte über der Energie). Danach sofort die Physik: Boltzmann-Verteilung, J_n = 0, U_Diff = U_T·ln(N_A·N_D/n_i²) mit Zahlen.

**(d) Fehlvorstellung**
- Ein Kasten `:::fehlvorstellung` zur Aussage „Die Atomrümpfe in der Raumladungszone sind doch neutral.“
  - **Warum das naheliegt:** Ein dotiertes Gebiet ist insgesamt neutral.
  - **Was stimmt:** P⁺ trägt +e, B⁻ trägt −e. Neutral ist ein Gebiet nur, solange jeder Rumpf seinen beweglichen Gegenpart in der Nähe hat; in der Zone ist dieser fortdiffundiert.
  - **Zahl:** 10¹⁶ unkompensierte Rümpfe pro cm³ erzeugen über 0,2 µm ein Feld von über 3·10⁴ V/cm.

**(e) Beispiel**
- *Schwach:* Titel „Ein Elektron ohne Nägel“, die Rechnung im Erzählton.
- *Gut:* Titel „Driftgeschwindigkeit in einem Kupferdraht bei 1 A“.
  - Gegeben: I = 1 A, A = 1 mm², n = 8,5·10²⁸ m⁻³.
  - Gesucht: v.
  - Rechnung: v = I/(n·e·A) in einer Zeile.
  - Ergebnis: v = 7,3·10⁻⁵ m/s.
  - Einordnung: 0,07 mm/s, also rund 26 cm pro Stunde. Das Signal breitet sich dennoch mit einem großen Bruchteil der Lichtgeschwindigkeit aus, weil sich das Feld ausbreitet, nicht die einzelnen Elektronen.

**(f) Umfang**
- *Schwach (zu lang):*
  - Die Boltzmann-Verteilung wird im Gleichgewichts-, im Durchlass- und im Sperrabschnitt jeweils neu erklärt.
  - Jeder Abschnitt endet mit einem zusammenfassenden Absatz.
  - Eine Abbildung wird Satz für Satz nacherzählt.
  - Die Messtechnik der Kennlinie steht in der kompakten Fassung.
- *Gut:*
  - Die Boltzmann-Verteilung wird einmal erklärt, im Gleichgewichtsabschnitt. Später heißt es „nach der Boltzmann-Verteilung (Abschnitt *Gleichgewicht*)“.
  - Es gibt keine Abschnittszusammenfassungen.
  - Der Text sagt, worauf man in der Abbildung achten muss und was daraus folgt.
  - Die Messtechnik steht nur in der ausführlichen Fassung, als `:::vertiefung`.

**(g) Nichts voraussetzen**
- *Schwach:* „Im n-Gebiet sind die Elektronen Majoritätsträger, die Löcher Minoritätsträger.“
- *Gut:* „Im n-Gebiet sind die Elektronen die **Majoritätsträger**, also die Ladungsträgersorte in der Überzahl: Auf 10¹⁶ Elektronen pro Kubikzentimeter kommen nur 10⁴ Löcher, die **Minoritätsträger**.“

**(h) Frage-Kasten**
- *Schwach:*
  - „Frage: Was ist eine Raumladungszone?“ Das ist Kernstoff und gehört in den Text.
  - „Frage: Ist das nicht erstaunlich?“ Das ist eine rhetorische Frage.
- *Gut*, direkt hinter dem Satz, der n·p = n_i² einführt:
  - **Frage:** „Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“
  - **Antwort:** Sie rekombinieren ständig, aber die Wärmebewegung erzeugt im selben Takt neue Paare. Die Rekombinationsrate wächst mit dem Produkt n·p, denn ein Elektron muss ein Loch treffen. Die Erzeugungsrate hängt nur von der Temperatur ab. Im Gleichgewicht sind beide gleich, und genau das legt n·p = n_i² fest. Im n-Gebiet der Beispieldiode lebt ein Loch im Mittel etwa 1 µs; pro Sekunde und Kubikzentimeter entstehen und verschwinden dort 10¹⁰ Paare.

**(i) Abstrakter Ausdruck**
- *Schwach:* „Ein System ist eine Abbildung $\mathrm{Tr}$, die jedem Eingangssignal $s(t)$ ein Ausgangssignal $g(t) = \mathrm{Tr}(s(t))$ zuordnet. Es heißt linear, wenn $\mathrm{Tr}(a s_1 + b s_2) = a\,\mathrm{Tr}(s_1) + b\,\mathrm{Tr}(s_2)$ gilt.“ Der Ausdruck steht da, bevor man weiß, wofür er steht.
- *Gut:* Erst zwei einfache Systeme: Eines verdreifacht das Eingangssignal, aus $\sin t$ wird $3\sin t$; eines addiert 5. Dann der Satz, dass $\mathrm{Tr}$ nur der Name für diese Veränderung durch das System ist. Dann die Schreibweise $g(t) = \mathrm{Tr}(s(t))$ und die Linearität, an beiden Systemen geprüft: Beim Verdreifachen gilt sie, beim Addieren von 5 nicht, denn für die Summe zweier Signale käme die 5 nur einmal hinzu, in der Summe der Einzelergebnisse aber zweimal.

**(j) Zusammenhang in einem Satz**
- *Schwach:* Die Linearität steht nur als Formel $\mathrm{Tr}(a s_1 + b s_2) = a\,\mathrm{Tr}(s_1) + b\,\mathrm{Tr}(s_2)$ mit einer Erklärung der Symbole; was sie im Kern sagt, muss die Leserin selbst herauslesen. Ebenso schwach, weil falsch: ein Satz, der nur dem Muster folgt, etwa „die Ableitung des Produkts ist das Produkt der Ableitungen“.
- *Gut:* Nach Formel und Erklärung zusätzlich die Zeile „**Kurz gesagt:** Die Transformation der Summe ist die Summe der Transformationen, und die Transformation des Vielfachen ist das Vielfache der Transformation.“ Geprüft am System „mal 3“; am System „plus 5“ zeigt dieselbe Zeile, warum es nicht linear ist.

## 13. Was sich gegenüber den bisherigen Artikeln ändert (Kurzfassung)

- **Zwei Fassungen pro Thema:** kompakt und ausführlich, umschaltbar. Die ausführliche ist etwas kompakter als das Lernskript, die kompakte etwa halb so lang wie die ausführliche.
- **Aussortieren nach K/H/V/S;** keine Doppelungen; Länge nach Schwierigkeit.
- **Erklären von null an:** jeder Begriff beim ersten Auftreten erklärt, Fließtext statt Aufzählung.
- **Abstrakte Ausdrücke erst anschaulich:** ein einfacher, konkreter Fall, dann die Bedeutung in Worten, dann die formale Schreibweise (§5.10).
- **Zusammenhänge zusätzlich in einem Satz:** Wo eine Formel einen Zusammenhang ausdrückt (Vertauschen, Zerlegen, Umkehren, Überlagern), steht zusätzlich die Zeile „Kurz gesagt:“ in einfacher Sprache, nur wenn sie ohne Ausnahme stimmt (§5.11).
- **Sachlicher Ton** statt Leitbild-Erzählung; Analogien knapp im Kasten, mit Grenzen.
- **„Worum es geht“** als kurzer Sachabschnitt nach dem Inhaltsverzeichnis, mit Einstiegsabbildung.
- **Akteure** vor jeder Kernformel und jedem Mechanismus, danach „Das Zusammenspiel“.
- **Abbildungen in fester Häufigkeit,** mit Inhalt, Daten und Kernaussage geplant. Sie stehen zunächst als `:::grafik`-Platzhalter mit Bildbeschreibung im Artikel und werden später ausschließlich mit dem Editor erzeugt (`ABBILDUNGEN_LISTE.md`).
- **Fester Aufbau** für Herleitungen und Beispiele.
- **Fehlvorstellungen und typische Fragen** werden ausdrücklich beantwortet.
- **Zahlen aus einem Zahlen-Skript**, eine Arbeitsnotiz pro Thema im Repo.

## 14. Was diese Datei am Bauplan ändert

- **Bauplan §1 Nr. 10** („Im Bild“ an jeder Stelle, ein durchgehendes Leitbild): aufgehoben. Ersetzt durch §2 und §9.1.
- **Bauplan §3** (Bogen „Anschaulich → …“): ersetzt durch §3 und §4 dieser Datei. Das Inhaltsverzeichnis bleibt der Seitenanfang; „Worum es geht“ ist der erste Abschnitt danach.
- **Bauplan §3 Quiz „genau 10“:** gilt für die ausführliche Fassung; die kompakte hat genau 6.
- **Bauplan §3a:** Größenordnungen, die ein Argument tragen, bleiben im Fließtext (§5.4), als Zahl bzw. kurze Angabe; Gleichungen stehen weiterhin auf eigener Zeile (Bauplan §2). Der Aufbau der Beispiele folgt §8.
- **Bauplan §4** (`:::grafik`-Platzhalter, keine Grafiken im Loop): gilt wieder (Entscheidung vom 21.10.2026), präzisiert durch §7.5.
  - Platzhalter mit Szene-Zeile und Bildbeschreibung, dazu je ein Eintrag in `ABBILDUNGEN_LISTE.md`.
  - Für Farben und Gestaltung gilt §7.4, nicht die Farblogik aus Bauplan §4.
  - Editor-Funktionen und Abbildungen entstehen nach den Artikeln, nicht im Loop.
  - Der kurzzeitige Weg über matplotlib-SVGs (Pilot) ist aufgehoben.
- **Bauplan §8:** ergänzt durch §11 dieser Datei.
- **Neue Kastentypen:**
  - `:::analogie`, `:::fehlvorstellung` und `:::vertiefung` stellt der Build ohne Codeänderung dar; die Überschrift ergibt sich aus dem Namen.
  - `:::frage` wird ausklappbar: Die erste Zeile (die Frage) ist sichtbar, die Antwort klappt auf.
- **Build-Ergänzungen mit dem Pilot-Thema:**
  - Er erkennt `fassung:`.
  - Er führt jedes Thema im Navigationsbaum nur einmal.
  - Er setzt den Umschalter „Kompakt | Ausführlich“ mit Lesezeiten an den Seitenanfang und merkt sich die Wahl der Leserin.
  - Er bekommt eine CSS-Regel für `figure.fig img` (derzeit ungenutzt).
  - Er zeigt `:::grafik` als „Abbildung in Vorbereitung“: die Bildbeschreibung als Text, die Szene-Zeile klein darunter.
