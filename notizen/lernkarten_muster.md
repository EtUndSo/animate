# Lernkarten neu: Muster (seit 11.11.2026)

**Auftrag des Users** (11.11.2026): „Die Inhalte der Lernkarten machen keinen Sinn. Zum Beispiel Frage: Spannung, Antwort: Auf einer Blockbatterie steht 9 V. Diese Angabe ist eine Spannung. Wir sollten die Lernkarten nochmal in Ruhe überarbeiten, wenn kein anderer Agent läuft, um wirklich sinnvolle Karteikarten zu erhalten mit sinnvollen Fragen und Antworten.“

**Entscheidungen des Users** (11.11.2026):
- **Kartenarten:** vier, alle neu geschrieben: Begriff, Formel, Herleitung, Zusammenhang.
- **Quiz:** eigens geschriebene falsche Antworten, also typische Fehlvorstellungen.
- **Pilot:** ET1, Kapitel 1 (Ladung, Feld und Potenzial).

## Inhalt
- **Umfang:** je Artikel etwa 6–12 Karten, je nach Inhalt. Kurze Artikel bekommen weniger Karten. Überblick und „Das Wichtigste“ bekommen keine.
- **Begriff:** Die Frage zielt auf die Bedeutung, z. B. „Was gibt die Spannung zwischen zwei Punkten an?“. Die Antwort ist eine echte Bestimmung (Oberbegriff + Merkmal), kein Beispiel, 1–3 Sätze, ggf. mit Formel und Einheit. Diese Antwort dient auch als Bestimmung im Begriffsverzeichnis und in der Zusammenfassung.
- **Formel:** Die Frage zielt auf den Zusammenhang oder die Formel, z. B. „Wie hängen Spannung, Arbeit und Ladung zusammen?“. Die Antwort enthält die Formel, die Bedeutung der Größen und die Gültigkeit.
- **Herleitung:** nur, wo der Artikel etwas herleitet. Die Frage nennt Ausgangspunkt und Ziel. Die Antwort besteht aus 3–6 Schritten, jeder mit Begründung („weil …“).
- **Zusammenhang:** Die Frage fragt „Warum …?“, „Was passiert mit …, wenn …?“ oder „Woran liegt es, dass …?“. Die Antwort ist eine kurze Begründung mit dem Mechanismus.
- **Falsche Antworten (Quiz):** je Begriff-, Formel- und Zusammenhangskarte genau 3.
  - Sie sind plausibel, also typische Fehlvorstellungen oder Verwechslungen, aber für jemanden, der den Artikel verstanden hat, eindeutig falsch.
  - Länge und Stil sind ähnlich wie bei der richtigen Antwort, damit die richtige nicht an der Form erkennbar ist.
  - Kein „keine der Antworten“, keine Fangfragen über Wortlaut.
  - Herleitungskarten haben keine falschen Antworten.
  - Erlaubt und oft am besten: eine richtige Formel mit falscher Aussage (z. B. „gilt für Körper jeder Größe“).
  - **Längenprüfung in jedem Durchgang:** Die richtige Antwort darf nicht auffällig oft die längste sein (Pilot: erst 49 von 91, nach dem Ausgleich 24 von 91, also etwa Zufall). Das Prüfskript zählt das.
- **Fachbegriffe abdecken:** Jeder Fachbegriff (`__…__`) des Artikels soll eine Begriffskarte bekommen oder im Kartennamen einer passenden Karte stehen (z. B. „Masse und Erde“). Der Name ist der Begriff in der Form des Artikels; Plural und Beugung erkennt der Build. Kartennamen enthalten keine Formeln, weil sie in der Kopfzeile `:::karte` stehen.
- **Allgemein:**
  - Alles muss aus dem Artikel beantwortbar sein, ohne Vorgriffe. Bestimmungen aus früheren Artikeln desselben Kapitels (auch aus dem Überblick) dürfen verwendet werden.
  - Bezeichnungen, Symbole und Formeln exakt wie im Heft.
  - Seriöser Ton.
  - Kein Bezug auf Skript, Uni, Vorlesung, Übung, Folien oder Praktikum, auch kein Hinweis auf Prüfskripte.

## Quelle: `kap<N>_karten.tex` je Heft (Heftordner), Übersetzungen `kap<N>_karten_<lang>.tex`
```
\begin{karten}{<Schlüssel>}{<Artikeltitel>}
\karte{begriff}{<Begriff>}{<Frage>}{<Antwort>}{<falsch 1>}{<falsch 2>}{<falsch 3>}
\karte{formel}{<Name>}{<Frage>}{<Antwort>}{<falsch 1>}{<falsch 2>}{<falsch 3>}
\karte{zusammenhang}{<Stichwort>}{<Frage>}{<Antwort>}{<falsch 1>}{<falsch 2>}{<falsch 3>}
\begin{herleitungskarte}{<Name>}{<Frage mit Ausgangspunkt und Ziel>}
\schritt{<Schritt mit Begründung>}
\schritt{…}
\end{herleitungskarte}
\end{karten}
```
- **Schlüssel:** der erste `stufe`-Anker des Artikels. Ein Artikel ohne `stufe`-Anker hat als Schlüssel seinen Dateinamen ohne Nummer, z. B. `von-grund-auf-was-elektrotechnik-ist-und-woher-ladung-kommt`.
- **Formeln** in `$…$` bzw. `\[…\]` wie im Heft; `\fb{}` ist erlaubt.
- **Prüf-PDF:** `Kap<N>_<Name>_Karten.tex` mit `karten_def.tex` (Umgebungen und Befehle) zeigt jede Karte mit Frage, Antwort und den falschen Antworten (als falsch gekennzeichnet), zur Durchsicht.

## Website (Konverter und Build)
- **Konverter:** schreibt die Karten als Block in das Artikel-Markdown:
  ```
  ::::lernkarten
  :::karte begriff Spannung
  Frage
  ---
  Antwort
  --- falsch
  falsche Antwort 1
  --- falsch
  falsche Antwort 2
  --- falsch
  falsche Antwort 3
  :::
  :::karte herleitung Name
  Frage
  ---
  Schritt 1
  ---
  Schritt 2
  :::
  ::::
  ```
  Der Name nach der Art ist optional (Begriff, Formelname, Stichwort).
- **Build:**
  - Der Bereich Lernkarten nutzt für solche Artikel nur diese Karten.
  - Das Quiz nimmt die geschriebenen falschen Antworten.
  - Begriffsverzeichnis und Zusammenfassung nehmen die Bestimmung aus den Begriffskarten (`karten_bestimmungen`).
    - Abgleich: Kartenname = Fachbegriff, erst genau, dann mit Beugung (`_gleicher_stamm`). „A und B“ gilt für beide.
    - Eine Karte ohne passenden Fachbegriff im Fließtext (etwa nur im Beispiel- oder Zusatzkasten) wird ein eigener Eintrag, der auf den Artikelanfang verlinkt.
    - Fachbegriffe ohne Karte behalten den Satz aus dem Text.
    - Der Build meldet „Begriffskarten: N Bestimmungen übernommen; ohne Fachbegriff im Artikel: …“.
  - Der Schlüssel `stufe-N` ist nur innerhalb eines Kapitels eindeutig. Der Konverter liest je Kapitel `kap<N>_karten.tex` und ordnet nur die Artikel dieses Kapitels zu.
- **Prüf-PDF:** `karten_def.tex` mit boxsep=0 und 4 pt Innenabstand, sonst meldet `pdf_pruefen` die Kastenrahmen als „ragt über den Rand“.

## Stand
- **11.11.2026 Pilot ET1 Kap. 1:** 98 Karten (37 B, 21 F, 33 Z, 7 H), PDF `C:\Bücher\ET1\Arbeitshefte\Kap1_Feld_Karten.pdf` (30 S.), auf der Website eingebaut. Abnahme durch den User offen.
- **Umfang:** etwa 100 Karten je Kapitel, also rund 1100 allein für ET1.
  - Das Format aus W4b (`:::karte <art>` / `---`) bleibt gültig; `--- falsch` und der Name sind Erweiterungen.
