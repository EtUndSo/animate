# Überarbeitung aller Arbeitshefte (ab 03.11.2026)

Diese Regeln gelten für jedes Heft. Sie haben Vorrang vor den älteren Aufträgen `heft_auftrag_*.md`, soweit sie ihnen widersprechen (Gliederung in „Stufen“, Längengrenzen, F/A-Kästen). Alles andere aus den alten Aufträgen gilt weiter: Quellen, Dateien, Bezeichnungen, Bauen, Szenen, Bericht.

Anlass, in den Worten des Users:
- „so versteht man als neuer Leser nichts und ist nur verwirrt“
- „zu viel Input gleichzeitig für ein menschliches Gehirn“

Der Leser ist neu. Er kennt nur die früheren Teile der Reihe und das, was das Heft selbst erklärt hat.

**Ton.** Seriös und professionell, aber nicht steif: locker genug, dass die Leser dranbleiben und gut verstehen, ohne flapsig zu werden. Der Ton der bisherigen Hefte trifft das bereits.

**Qualität vor allem.** Die Artikel müssen qualitativ sehr hochwertig, klar strukturiert und hilfreich für das Verständnis sein. Der Zeitaufwand fürs Schreiben ist egal; der User hat das mehrfach betont. Lieber ein Heft gründlich als drei schnell.

## 1. Gliederung wie im Skript
- Jedes `\section` entspricht einem Abschnitt des Skripts, in derselben Reihenfolge.
  - Der Titel ist sachlich und benennt das Thema, z. B. „Pole und Nullstellen in der p-Ebene“. Kein „Stufe N:“, keine Skriptnummer.
- Innerhalb eines Abschnitts bekommt jedes Teilthema ein eigenes `\subsection`.
- Inhalte, die das Skript erst spät bringt, stehen auch im Heft erst dort. Beispiel: Die Umkehrformel der Laplace-Transformation steht im Skript in den Tabellen am Ende, also auch im Heft.
  - Was als Hintergrund früher hilft, steht als Hintergrund-Kasten an der Stelle, an der es gebraucht wird, siehe Abschnitt 3.
- Wie bisher nennt das Heft nie Skript, Vorlesung, Übung, Uni oder Seiten- und Satznummern.

## 2. Ein neuer Begriff nach dem anderen
Jeder Begriff, den das Heft neu einführt, bekommt seinen eigenen Unterabschnitt. Der Unterabschnitt geht in dieser Reihenfolge vor:
1. **Wozu:** ein bis zwei Sätze in Alltagsworten. Welche Frage beantwortet der Begriff?
2. **Anschauung:** ein Bild oder eine Abbildung des Begriffs selbst, bevor die Formel kommt. Das ist keine Anwendung und keine Schaltung.
3. **Definition:** formal und exakt (`definition` oder `satz`).
4. **Einfachstes Beispiel:** vollständig durchgerechnet, mit Zahlen.
5. **Kurz gesagt:** ein Satz.

Erst danach kommt der nächste Begriff. Dazu fünf feste Regeln:
- **Ein Satz führt höchstens einen neuen Begriff ein.** Nie zwei neue Begriffe im selben Satz, nie einen neuen Begriff in einer Klammer oder einem Nebensatz.
- **Was der Leser braucht, wird erklärt, nicht vorausgesetzt.** Das gilt auch, wenn es aus einem früheren Modul stammt (HöMa3 setzt z. B. die partielle Ableitung voraus). Es kommt als eigener kurzer Unterabschnitt „Was du dafür brauchst: …“ zu Beginn des Abschnitts, mit Erklärung und Beispiel.
- **Kein Bündel.** Ein Kasten oder Absatz, der fünf Begriffe auf einmal klärt (Vektorfeld, Skalarfunktion, Nabla, partielle Ableitung, Jacobi-Matrix), wird in fünf Unterabschnitte zerlegt. Jeder ist ausführlich, jeder hat ein eigenes Beispiel.
- **Ausführlich statt knapp.** Lieber zwei Absätze und ein Beispiel mehr. Es gibt keine Zeichen- oder Seitengrenze. Die Website teilt lange Abschnitte selbst an den `\subsection`.
- **Formeln erst nach der Anschauung.** Jede Größe in einer Formel ist erklärt, bevor oder direkt nachdem die Formel dasteht, mit Einheit, wo es eine gibt.
- **Theorie vor Praxis.** Anwendungsbeispiele (Schaltungen wie der RC-Tiefpass, physikalische Systeme, Messungen) kommen erst, wenn die Theorie, die sie brauchen, erklärt ist.
  - Es gibt kein „Rechenmodell“ und keinen Beispielkasten am Anfang des Hefts oder eines Abschnitts.
  - Ein Beispiel steht dort, wo der Leser es mit dem bis dahin Erklärten verstehen kann. Bei der Laplace-Transformation ist das nach der Definition der Transformation, nicht vorher.
  - Der User sagte dazu: „Beispiele direkt am Anfang zu nennen … ist reine Verwirrung.“

## 3. Nichts Verwirrendes zu früh: Hintergrund-Kästen
Manche Information ist richtig und wichtig, braucht aber Wissen, das an dieser Stelle noch fehlt. Beispiel: bei der Jacobi-Matrix die Näherung „Änderung ≈ Ableitung mal Schritt“, bevor die partielle Ableitung verstanden ist. Solche Informationen stehen nicht im Haupttext, sondern:
- an der ersten Stelle, an der alle Voraussetzungen erklärt sind, oder
- in einem Kasten `hintergrund` direkt danach.

```latex
\begin{hintergrund}{Titel als Frage oder Aussage}
...
\end{hintergrund}
```

Was in Hintergrund-Kästen gehört:
- warum etwas gerade so ist;
- woher eine Formel kommt, als Idee; der formale Weg steht weiter in `herleitung` oder `beweis`;
- Verbindungen zu anderen Themen;
- Antworten auf typische Fragen;
- Vertiefungen.

Was dabei gilt:
- Auf der Website ist der Kasten zugeklappt.
- Der Haupttext muss ohne ihn vollständig und verständlich sein. Ein Begriff, den der Haupttext später benutzt, darf nicht nur in einem Hintergrund-Kasten erklärt sein.
- Die alten Kästen `qa`, `frage` und `vertiefung` werden zu `hintergrund`.
  - Die Frage oder das Thema wird zum Titel.
  - Fragen des Users stehen nur allgemein formuliert da, nie wörtlich.
- `herleitung`, `beweis` und `ltspice` bleiben, wie sie sind; sie sind auf der Website ebenfalls zugeklappt.
- In einem Kasten steht keine Gleitumgebung (`abb`). Stattdessen: `\begin{center}…\captionof{figure}{…}\label{fig:…}\end{center}`.

## 3a. Das eigentliche Hintergrundwissen: warum es funktioniert (Pflicht bei jedem Thema)
Das ist der Teil, der die Hefte über das Skript hinaushebt: von „Formel auswendig lernen und anwenden“ zu „das ist der Hintergrund, deswegen machen wir es so, deswegen funktioniert es“. Der User nennt das „sehr sehr wichtig“; es gehört zu jedem Thema.
- Für jeden Abschnitt und jedes zentrale Verfahren wird **recherchiert**: Lehrbücher, gute Vorlesungsnotizen, anerkannte Erklärseiten (WebSearch/WebFetch).
  - Gesucht ist die Idee, die erklärt, *warum* die Methode funktioniert und *wozu* man sie so baut.
  - Nichts wird kopiert. Ins Heft kommt eine eigene, exakte Erklärung.
- Ein Hintergrund-Kasten erklärt den **Mechanismus**. Nur die Rechnung noch einmal zu wiederholen genügt nicht.
- Musterbeispiel Laplace-Transformation: Ein Signal ist eine Überlagerung komplexer e-Funktionen.
  - Das Integral ∫ s(t) e^{-pt} dt multipliziert das Signal mit einer Probe-Exponentialfunktion und mittelt; es wirkt wie ein Suchfilter, ähnlich einem Lock-in-Verstärker oder einem Radioempfänger.
  - Ein Anteil A·e^{p₀t} wird dabei zu A·e^{(p₀−p)t}. Für p = p₀ bleibt eine Konstante übrig, das Integral wächst über alle Grenzen: Dort sitzt der Pol, und A ist der Partialbruchkoeffizient.
  - Deshalb verraten die Pole, welche e-Funktionen im Signal stecken.
  - Dahinter steht: Die e-Funktionen sind die Eigenfunktionen aller LTI-Systeme. Im Bildbereich ist ein LTI-System „diagonal“, so wie eine Matrix in ihrer Eigenbasis.
- Weitere Beispiele dieser Art:
  - Nullstellen sind die e-Funktionen, die das System vollständig sperrt; Pole sind Eigenschwingungen, die ohne Eingang bestehen können.
  - Rückkopplung mit großer Vorwärtsverstärkung macht das System unabhängig vom Verstärker (H ≈ 1/H₂); das ist der Grund für Gegenkopplung.
  - Passive RLC-Netze sind immer stabil, weil der Widerstand Energie verbraucht.
- Jede solche Aussage muss exakt stimmen. Analogien werden als Bild gekennzeichnet, mit ihren Grenzen.
- Nur das gehört an die frühe Stelle, was der Leser dort verstehen kann. Die volle Erklärung, die spätere Begriffe braucht, kommt als Hintergrund dort, wo diese Begriffe eingeführt sind; dazu ein Rückverweis auf die frühere Stelle.

## 4. Keine Vorgriffe
- Jeder Satz muss verständlich sein, wenn der Leser genau bis dorthin gelesen hat.
- Kein „später“, kein Verweis auf spätere Abschnitte, kein Begriff aus einem späteren Abschnitt, auch nicht im Hintergrund-Kasten.
- Rückverweise sind erwünscht.
- „Worum es geht“ am Anfang nennt nur die Frage des Hefts und ihren Nutzen. Es nennt keine Ergebnisse und keine Begriffe, die erst später erklärt werden.

## 5. Vollständigkeit und Präzision
- Jede Definition, jeder Satz und jede Formel des Skript-Kapitels kommt vor, auch Zwischenschritte von Herleitungen.
- Fehler der Quelle werden still korrigiert und im Bericht genannt.
- Kein Symbol bedeutet zweierlei, auch dann nicht, wenn das Skript es doppelt benutzt.
  - Dann wird umbenannt und im Bericht vermerkt.
  - Beispiel: ω₀ als Resonanzkreisfrequenz und ω₀ als Schwingungsfrequenz eines Polpaars.
- Differentiale haben die richtige Ordnung.

## 6. Aufgaben, Abbildungen, Ende des Hefts
- Aufgaben stehen am Ende des Abschnitts, zu dem sie gehören, und benutzen nur, was bis dahin erklärt ist.
- Bestehende Aufgaben bleiben, wo sie passen; sonst werden sie angepasst oder verschoben.
- Jeder Abschnitt hat mindestens eine Aufgabe. Die Lösungen stehen ausführlich in `kap<N>_loesungen.tex`, in der Reihenfolge der Aufgaben.
- Bestehende Abbildungen werden wiederverwendet. Für jede neue Abbildung gilt:
  - TikZ im Heft, Label `fig:<name>`;
  - eine Editor-Szene mit demselben Namen (`<modul>/k<N><name>` in `tools/szenen/<modul>_teil<N>.py`), dann `python tools/export_szenen.py <namen>`.
- **Summen, Produkte und Skalarprodukte als Editor-Abbildung** (Wunsch des Users, 04.11.2026). Der User: „Summen und Skalarprodukte … nicht als Formeln ausgeschrieben, sondern durch eine, durch den Editor erzeugte Abbildung repräsentiert“, „genau so dargestellt und detailliert ausgeführt … wie die Operationen bei Summenzeichen und Produktzeichen“.
  - **Was:** Jede Summe Σ, jedes Produkt ∏ und jedes Skalarprodukt, das mit konkreten Zahlen ausgerechnet wird, bekommt zusätzlich zur Formel eine Abbildung. Darin steht die Rechnung Schritt für Schritt: Kopf, ausgeschriebene Summanden, eingesetzte Zahlen, Werte, Ergebnis.
  - **Bausteine in `tools/szenen_lib.py`:**
    - `s.summe(term, von, bis, …)`, z. B. `s.summe("1/i^2", von=1, bis=4)`;
    - `s.produkt(term, von, bis, …)`;
    - `s.skalarprodukt(u, v, namen=("w", "x"), index="j", obere="", vektoren=True, …)`, z. B. `s.skalarprodukt([3, 10, -4], [120, 3, 25])`;
    - für jede andere Formel `s.formel(tex, …)`.
    - Beispiele stehen in `tools/szenen/beispiel_summen.py`.
  - **Im Heft:** Die Abbildung steht direkt nach der Rechnung. Wie jede Abbildung ist sie eine `abb`-Umgebung mit Bildunterschrift und Label `fig:k<N><name>`. Statt TikZ enthält sie dieselben Schritte als `align*`: Kopf = Summanden = eingesetzte Zahlen = Werte = Ergebnis, bei Skalarprodukten vorweg die beiden Vektoren als Spalten. Die Szene trägt denselben Namen. Auf der Website erscheint das Editor-Bild mit dem Knopf „Szene im Editor öffnen“, dort läuft die Rechnung animiert ab.
  - **Grenze:** Allgemeine Formeln ohne Zahlen (Definitionen wie $\sum_j w_j x_j$) bleiben Formeln.
- Am Ende des Hefts in dieser Reihenfolge, die Website verschiebt sie selbst:
  1. kernbox „Das Wichtigste bis hier“;
  2. kernbox „Die Antwort in drei Sätzen“;
  3. Prinzip-Tabelle;
  4. Lösungen.

## 6a. Website
- Sobald ein Heft Hintergrund-Kästen hat, macht `heft_zu_artikel.py` aus jedem `\section` einen Artikel; die Unterabschnitte erscheinen im Inhaltsverzeichnis der Seite.
  - Grund: Einzelne Unterabschnitte sind als eigene Seiten zu klein. Die Gliederung entspricht dann genau dem Skript.
- Tabellen als `table` mit `\caption` und `\label{tab:…}`.
- Fußnotenzeichen in Tabellen als `$^{\mathrm a}$`, nicht `\textsuperscript`.
- Stile für Blockschaltbilder (`blk`, `gn`, `sm`, `kn`, `vz`) stehen in der ET3-Präambel. Muster für Szenen: `tools/szenen/et3_teil2.py` (Klasse `Block`).
- Pilot und Muster für alles: ET3 Teil 2 (Laplace), Stand 03.11.2026.

## 7. Ablauf je Heft
1. Den Skript-Abschnitt und das alte Heft ganz lesen. Liste anlegen: Skript-Abschnitte, darin alle Begriffe in der Reihenfolge ihrer Einführung.
2. Neue Gliederung festlegen: `\section` je Skript-Abschnitt, `\subsection` je Begriff.
3. Text schreiben. Was sich bewährt hat (Beispiele, Abbildungen, Rechenmodell, Aufgaben), wird übernommen.
4. Bauen: pdflatex dreimal, Hilfsdateien löschen. Prüfen mit `python tools/heft_zu_artikel.py <modul> --kap <N> --lang de --pruefen --katex`.
5. Selbstprüfung, Satz für Satz:
   - Steht in einem Satz mehr als ein neuer Begriff?
   - Wird ein Begriff benutzt, bevor er erklärt ist?
   - Steht im Haupttext etwas, das Wissen braucht, das noch fehlt?
   - Fehlt eine Formel aus dem Skript?
6. Zuerst nur Deutsch. Die Übersetzungen (en, es, zh) folgen, wenn das Modul freigegeben ist.
7. Es arbeitet höchstens ein Agent gleichzeitig. Die Hefte werden nacheinander bearbeitet, Qualität geht vor Tempo.
