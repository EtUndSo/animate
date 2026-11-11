# Website-Ausbau: Umsetzung der Top 10 (seit 11.11.2026)

Grundlage: `notizen/website_ideen.md` (Konzept des Ideen-Agenten, 11.11.2026).
Entscheidungen des Users (11.11.2026):
- „Ok, die Top10 sind gute Ideen. Lass uns versuchen sie einzubauen.“
- **Schnell-Info-Box:** „Die Boxen sollten die wichtigsten Begriffe, Formeln und Zusammenhänge stichpunktartig zusammenfassen.“ Also drei Gruppen: Begriffe, Formeln, Zusammenhänge. Automatisch aus dem Heft-Material, ohne eigenen Heft-Kasten.
- **Platz (User, 11.11. später):** „Vielleicht sollten wir die Info-Box ganz ans Ende verschieben als eine Zusammenfassungs-Box. Also zwischen den Artikel und die Pfeile zum Wechsel auf vorherigen oder folgenden Artikel.“ Also Box „Zusammenfassung“ (Summary, Resumen, 小结, Résumé, Özet) am Artikelende vor der Navigation, immer offen; oben in der Kennzahlenzeile ein Sprunglink dorthin. An den W1-Agenten weitergegeben.
- **Lernkarten:** „sind eine gute Idee.“
- **Hosting-Tarif:** noch offen (Frage des Users „Wofür ein Hosting-Tarif?“ am 11.11. beantwortet).
- **Startseite:** Der Editor bleibt vor „Fächer & Themen“ (Umstellung des Users vom 11.11.); der Vorschlag C3 „Erklärungen vor den Editor“ entfällt.

Damit erledigt: Die Frage „offen/zugeklappt“ und der Konflikt mit „Keine Vorgriffe“ entfallen (Box am Ende, fasst nur den eigenen Artikel zusammen).

## Arbeitsweise
- **Parallel zur Englisch-Schleife.** Jede Welle arbeitet in einer eigenen Arbeitskopie (`git worktree add --detach`) mit eigenem Server auf Port 8001. Das Haupt-Repo bleibt sauber, Commit-Zeitpunkte und meine Builds der Übersetzungen werden nicht gestört.
- **Übernahme:** Am Ende liefert der Agent einen Patch nur der Quelldateien (`build_wissen.py`, `web/wissen/assets/…`, ggf. `web/index.html`). Ich prüfe ihn, spiele ihn ins Haupt-Repo ein, baue und melde dem User den Commit-Zeitpunkt.
- **Prüfen:** Nach jeder Welle prüfe ich mit Screenshots und Browser-Tests; bei großen Wellen zusätzlich ein frischer Prüf-Agent.
- **Grenzen:** wie im Konzept §„Feste Grenzen“ (keine Codeausführung, kein Herkunftsbezug, Variante B, kein Tracking, sechs Sprachen, automatisch aus den Heften).

## Wellen
| Welle | Inhalt (Nummern aus dem Konzept) | Stand |
|---|---|---|
| **W1 Artikel lesen** | 1 Inhaltsverzeichnis aus `###`; 2 Zusammenfassung am Artikelende (Begriffe, Formeln, Zusammenhänge); Kennzahlenzeile mit Lesezeit; Titel/Beschreibung ohne TeX; 3 Lesbarkeit auf dem Handy (weniger Verschachtelung, Abbildung antippen zum Vergrößern); schnelle Gewinne (Kopierknopf, Ankerlinks, Druckansicht, Nachtmodus nach System beim ersten Besuch, Sprunglink „Zum Inhalt“, Standbild statt leerem Startbild) | **fertig 11.11., eingespielt** (Patch `scratchpad/website_w1/w1.patch`, 3 Dateien, +820/−50). Inhaltsverzeichnis de 229 statt 77 Seiten; Zusammenfassung auf 641 von 752 de-Seiten (nicht bei „Das Wichtigste“, 44 ohne Material); 0 TeX in Titeln; HTML-Menge gleich; von mir im Browser geprüft (Overlay, Box, Inhaltsverzeichnis, de/en/zh, 390/1300 px). Schwächen: Bruchstücke bei Begriffen, wenn abgesetzte Formeln Sätze teilen; ET1/GEMB1/HöMa1 fast ohne „Kurz gesagt“. Konverter-Wünsche: `b[Bestimmung]{Begriff}`, kein Absatzbruch um Formeln mitten im Satz, `summary:` als Klartext. |
| **W2 Lernen** | 4 Lesefortschritt im Browser; 5 Begriffsverzeichnis je Modul und Link-Vorschau; 6 Lernkarten mit verteilter Wiederholung (zuerst Abdeck-Modus) | **fertig 11.11., eingespielt** (Patch `scratchpad/website_w2/w2.patch`: build_wissen, wissen.css/js, index.html „Weiterlesen“, datenschutz.html §6). Fortschritt (localStorage), Begriffe- und Lernkarten-Seite je Modul und Sprache (+50 HTML, +25 JSON), Link-Vorschau, Selbsttest in der Zusammenfassung, Leitner 1/3/7/14/30. `web/` danach 14 963 Dateien. Schwächen: Seiten 250–600 KB (Seitenleiste ~143 KB je Seite), Lernstand je Gerät/Sprache ohne Export, Formeln ohne Namen fallen weg. |
| **W3a Finden I** | Wissensübersicht mit Modulkarten; Startseite in sechs Sprachen; Seitenleiste nur obere Ebenen im HTML, Rest aus `tree*.json` (Seiten ~143 KB leichter); Suchindex geteilt (Titel zuerst, Volltext je Modul) | **fertig 11.11., eingespielt** (Patch `scratchpad/website_w3a/w3a.patch`; neu `web/wissen/assets/suche.js`, Startseiten `/en/ … /tr/` werden vom Build aus `web/index.html` mit `data-i18n` erzeugt). HTML im Mittel 121 → 33 KB, `web/wissen` 218 → 78 MB; Übersicht 32 000 → 1 500 px; Suche lädt zuerst 68 KB statt 2 MB (Treffer gleich, von mir geprüft). Alte `search*.json` gelöscht (Commit muss die Löschung mitnehmen). `web/` 15 006 Dateien. |
| **W3b Finden II** (Rest von W3) | 7 Startseite in sechs Sprachen, Wissensübersicht mit Modulkarten; 8 Sitemap, `canonical`, `x-default`, strukturierte Daten, Vorschaubilder je Kapitel; KaTeX selbst ausliefern; Suchindex verkleinern | offen (Vorschaubilder hängen am Hosting-Tarif) |
| **W5 Rückmeldung und Regler** (früher W4) | 9 „Hat das geholfen?“ (Cloudflare D1) und „Fehler melden“; 10 Regler-Modus für Abbildungen (Parameter über die Zeit gibt es seit E2) | offen (Rückmelde-Adresse mit dem User klären) |

## Bereiche der Website (User, 11.11.2026 abends)
Wortlaut: „Lass uns die Lernkarten als eigenen separaten Bereich einbauen und dann unter den Artikeln Verweise zu dem passenden Bereich. Dabei soll es so sein, dass es für jeden Artikel einzeln, aber auch für alle Artikel eines Kapitel und auch eines ganzen Moduls Lernkarten gibt, also sozusagen drei verschiedene Tiefen. Als Fragen sollen Begriffe, Formeln, Herleitungen von Formeln, Zusammenhänge abgefragt werden. Wir sollten auch einen weiteren Bereich einfügen in dem es viele Aufgaben mit Lösungen gibt. Also insgesamt einen Bereich für Wissen, einen für den Editor, einen für Lernkarten/Quiz und einen für Aufgaben.“

- **Vier Bereiche:** Wissen, Editor, Lernkarten/Quiz, Aufgaben (Kopfleiste und Startseite).
- **Lernkarten/Quiz:**
  - Ein eigener Bereich mit drei Tiefen: Artikel, Kapitel, Modul.
  - Kartenarten: Begriffe, Formeln, Herleitungen (Schritte nacheinander aufdecken), Zusammenhänge.
  - Unter jedem Artikel Verweise auf die Karten dieses Artikels, Kapitels und Moduls.
  - Ersetzt die W2-Seiten `…/lernkarten.html`; Leitner-Lernstand weiter nur lokal.
- **Aufgaben:**
  - Ein eigener Bereich mit allen Aufgaben samt Lösungen aus den Heften: am 11.11. 1 076 (de), dazu 234 Herleitungen.
  - Filter nach Modul, Kapitel und Artikel; Lösung zugeklappt; Link zum Artikel.
  - Weitere Aufgaben über die Hefte hinaus wären ein eigenes Inhaltsprojekt (offen).
- **Ergänzungen (User, 11.11.):** „1. Formelsammlung, 3. Kapitel auf einer Seite und 4. Mischtest noch ergänzen. Die anderen nicht.“
  - Formelsammlung je Modul: automatisch aus Satz- und Formelkästen, druckbar.
  - Kapitel auf einer Seite: alle Zusammenfassungen eines Kapitels als druckbarer Spickzettel.
  - Mischtest: zufällige Mischung aus Karten und Aufgaben gewählter Kapitel; Auswertung und Lösungen erst am Ende.
  - **Nicht:** „Mein Lernstand“ mit Export/Import; zusätzliche Aufgaben über die Hefte hinaus.
- **Reihenfolge:** Welle **W4 Bereiche** startet nach W3a, weil W3a Kopfleiste und Startseite umbaut. Die frühere W4 (Rückmeldung, Regler) wird W5.
- **Dateibudget:** Eine App-Seite je Bereich und Sprache plus Daten-JSON je Modul statt Tausender Einzelseiten. Statische Aufgaben-Seiten je Modul sind für Suchmaschinen sinnvoll; ihre Zahl muss im Budget bleiben.

## Drei Ansichten je Artikel (User, 11.11.2026 abends)
Wortlaut: „Wir sollten in dem Bereich Wissen auch zwischen verschiedenen Kategorien unterscheiden, die sich durch ihre Ausführlichkeit der Erklärung unterscheiden. Die aktuellen Artikel sind sehr ausführlich (war so gewollt und ist sehr gut), manche Leser wollen aber vielleicht nur kurz nachgucken und brauchen keine Details. Ich denke, dass wir zwischen "Sehr ausführlich (wie aktuell)", "Kurze Erklärungen" und "Formelsammlung" unterscheiden sollten. Diese jeweils für jeden Artikel, oben in der Leiste wo aktuell die zwei Pfeile sind umschaltbar.“
- Umsetzung als Welle **W4a „Ansichten“** (vor W4b Lernkarten/Aufgaben). Formelsammlung je Modul und „Kapitel auf einer Seite“ wandern mit hinein, weil sie dieselben Daten nutzen.
- „Kurz“ zuerst **automatisch** als Ansicht des vorhandenen Artikels (Überschriften, „Kurz gesagt“, Definitionen, Sätze, Kernformeln, Abbildungen). Ob später eigene, geschriebene Kurzfassungen kommen, entscheidet der User nach Ansicht der automatischen Fassung.
- **Entscheidung des Users (11.11. abends):** „Ja, wir sollten zu allen Artikeln die Formelsammlung und die kurze Erklärung neu erstellen. Die Formelsammlungen sollten auch einen Button zum Download haben mit Formaten png, pdf, jpg, svg (falls möglich).“
  - Also **geschriebene** Kurzfassung und Formelsammlung für jeden Artikel, als neues Inhaltsprojekt.
  - W4a legt die Haken an: Blöcke `::::kurzfassung` und `::::formelsammlung` im Artikel-Markdown ersetzen die automatische Fassung.
  - Download PNG/JPG/SVG im Browser erzeugt, PDF möglichst direkt (Bibliothek selbst ausgeliefert, erst beim Klick geladen); keine vorab gespeicherten Dateien je Artikel (Dateigrenze).
  - **Pilot ET3, Kapitel 2 (User bestätigt 11.11.), läuft seit 11.11.:** `kap2_kurz.tex`, `kap2_formeln.tex`, `kurz_formeln_def.tex`, `Kap2_Laplace_Kurz.tex`, `Kap2_Laplace_Formeln.tex` im Heftordner. Format `egin{kurzfassung}{<Schlüssel>}{<Titel>}`, `egin{formelsammlung}{…}{…}` mit `ormel{Name}{Formel}{Bedeutung; Bedingungen}`; Schlüssel = erster `stufe`-Anker des Artikels bzw. `ueberblick`. Danach: Konverter-Erweiterung (Blöcke `::::kurzfassung`/`::::formelsammlung` ins Artikel-Markdown), Bau, Abnahme durch den User.
  - Plan für das Inhaltsprojekt: je Heft zwei neue LaTeX-Dateien (`kap<N>_kurz.tex`, `kap<N>_formeln.tex`) mit einem Block je Artikel. Der Konverter schreibt daraus die Blöcke; daraus entstehen auch PDFs „Kurzfassung“ und „Formelsammlung“ je Kapitel. Ein Schreib-Agent je Heft mit Formelabgleich gegen das Heft per Skript. Zuerst ein Pilot, dann alle Hefte, parallel zur Englisch-Schleife; danach Übersetzung der neuen Dateien.
- Früher (bis 28.10.) gab es zwei geschriebene Fassungen je Thema; sie wurden mit dem Wechsel zu den Arbeitsheften abgelöst. Die automatische Ansicht kostet keine Schreib- und Übersetzungsarbeit.

## Idee: Konten mit Fortschritt auf dem Server (User, 11.11.2026) — PAUSIERT
User 11.11.: „Die Anmelde-Funktion pausieren wir erstmal, ich bin noch nicht sicher.“ Nicht von selbst wieder anstoßen.
Wortlaut: „Wenn wir es später sowieso auf einem Pi umsetzen, dann könnten wir dort auch lokal eine Datenbank anlegen in der wir Nutzerdaten speichern. Dann könnten sich Nutzer auf der Webseite auch anmelden und erst dann würden Funktionen, die den Stand des Fortschritts messen auch Sinn machen.“
- **Meine Empfehlung (11.11.):** Konten nur freiwillig. Ohne Anmeldung bleibt alles lokal wie in W2. Mit Anmeldung wird derselbe Stand geräteübergreifend gespeichert (Fortschritt, Lernkarten, gelöste Aufgaben).
- **Daten sparsam:** Nutzername, Passwort-Hash (Argon2id), optional E-Mail für das Zurücksetzen. Kein Auswerten einzelner Nutzer.
- **Technik:** kleiner Dienst auf dem Pi (z. B. Python/FastAPI) mit SQLite hinter dem Tunnel; `/api/*` vom Cloudflare-Zwischenspeicher ausnehmen; Sitzungs-Cookie `HttpOnly`, `Secure`, `SameSite=Lax`; Begrenzung der Anmeldeversuche.
- **Pflichten:** Datenschutzerklärung, Auskunft, Löschen und Export auf Wunsch, Meldepflicht bei Datenpannen. Verschlüsselte Sicherung außer Haus, denn der Pi hätte dann Daten, die nicht im Repo stehen.
- **Alternative ohne Pi:** Cloudflare Worker mit D1-Datenbank (Gratis-Tarif).
- **Zeitpunkt:** frühestens nach dem Umzug auf den Pi (zurückgestellt) oder vorher mit D1; Entscheidung des Users offen.

## Dateibudget (Cloudflare Pages)
- **Korrektur 11.11. abends:** Die bisherigen Zahlen (14 843, 15 006) zählten den lokalen Ordner `web/labor` mit (6 787 Dateien, 142 MB; v86/Alpine/xterm, über `.git/info/exclude` ausgeschlossen, also nie veröffentlicht). Veröffentlicht werden etwa **8 200 Dateien, 429 MB**. Bis zur Grenze von 20 000 ist also viel mehr Platz als gedacht.
- `web/` hatte am 11.11. 14 843 Dateien. Laut Cloudflare-Doku sind im Gratis-Tarif 20 000 Dateien je Site erlaubt, bezahlt 100 000.
- Wachstum: Englisch-Schleife, Linux 7/8, später es/zh/fr/tr für alle Hefte. Die Grenze ist absehbar.
- Wege: bezahlter Tarif, oder Dateien sparen (z. B. eine Datei je Abbildung statt `.svg` + `.anim.svg`; Abbildungen in R2).
</content>
