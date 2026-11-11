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
| **W1 Artikel lesen** | 1 Inhaltsverzeichnis aus `###`; 2 Zusammenfassung am Artikelende (Begriffe, Formeln, Zusammenhänge); Kennzahlenzeile mit Lesezeit; Titel/Beschreibung ohne TeX; 3 Lesbarkeit auf dem Handy (weniger Verschachtelung, Abbildung antippen zum Vergrößern); schnelle Gewinne (Kopierknopf, Ankerlinks, Druckansicht, Nachtmodus nach System beim ersten Besuch, Sprunglink „Zum Inhalt“, Standbild statt leerem Startbild) | läuft seit 11.11. |
| **W2 Lernen** | 4 Lesefortschritt im Browser; 5 Begriffsverzeichnis je Modul und Link-Vorschau; 6 Lernkarten mit verteilter Wiederholung (zuerst Abdeck-Modus) | offen |
| **W3 Finden** | 7 Startseite in sechs Sprachen, Wissensübersicht mit Modulkarten; 8 Sitemap, `canonical`, `x-default`, strukturierte Daten, Vorschaubilder je Kapitel; KaTeX selbst ausliefern; Suchindex verkleinern | offen (Vorschaubilder hängen am Hosting-Tarif) |
| **W4 Rückmeldung und Regler** | 9 „Hat das geholfen?“ (Cloudflare D1) und „Fehler melden“; 10 Regler-Modus für Abbildungen (Parameter über die Zeit gibt es seit E2) | offen (Rückmelde-Adresse mit dem User klären) |

## Dateibudget (Cloudflare Pages)
- `web/` hatte am 11.11. 14 843 Dateien. Laut Cloudflare-Doku sind im Gratis-Tarif 20 000 Dateien je Site erlaubt, bezahlt 100 000.
- Wachstum: Englisch-Schleife, Linux 7/8, später es/zh/fr/tr für alle Hefte. Die Grenze ist absehbar.
- Wege: bezahlter Tarif, oder Dateien sparen (z. B. eine Datei je Abbildung statt `.svg` + `.anim.svg`; Abbildungen in R2).
</content>
