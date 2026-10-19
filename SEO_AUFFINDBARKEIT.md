# Auffindbarkeit: Google- & KI-Such-Ranking — Feature-Ideen (Batch, später umsetzen)

Ziel: möglichst viele Lernende erreichen. Die Seite ist **nicht-kommerziell** (reiner Bildungsinhalt), was für
Rankings eher hilft (echter Mehrwert, keine Ad-/Affiliate-Signale). Mechanismen, die wir einbauen sollten
(User-Wunsch 2026-10-19):

## Technisches SEO (im `build_wissen.py` generierbar)
- **`sitemap.xml`** aller Wissensseiten (URLs + `lastmod`) + Eintrag in `robots.txt`.
- **`robots.txt`**: Crawling erlauben, Sitemap verlinken.
- **Canonical-URL** je Seite (`<link rel="canonical">`), saubere, sprechende URLs (haben wir schon über `pfad`).
- **Strukturierte Daten (JSON-LD)**: pro Artikel `LearningResource`/`Article` (headline, description, inLanguage=de,
  author, datePublished/Modified, isPartOf = Modul/Fach, educationalLevel). Hilft Google-Rich-Results **und**
  KI-Crawlern beim Einordnen.
- **Open-Graph-/Twitter-Card-Meta** (og:title/description/type=article/url, optional og:image = später die
  Editor-Grafik der Seite) → bessere Vorschau beim Teilen.
- **Saubere `<title>`** je Seite (Thema – Modul – EtUndSo) und sinnvolle `<meta name="description">` (haben wir;
  evtl. je Seite spezifischer). `<html lang="de">` ist gesetzt.
- **Performance & Mobile**: schnelle, statische Seiten (haben wir), Mobile-Tauglichkeit (gerade verbessert) —
  beides sind direkte Ranking-Faktoren.

## Inhalts-SEO
- **Überschriften-Hierarchie** sauber (genau ein `<h1>`, dann `<h2>/<h3>`) — wird beim Schreiben eingehalten.
- **Interne Verlinkung**: Artikel verweisen aufeinander (Voraussetzungen/weiterführend), Modul-/Oberthema-Index
  als Hub-Seiten. Stärkt Themen-Autorität.
- **Gute, fragenartige Zwischenüberschriften** (matchen Suchanfragen: „Warum …", „Wie funktioniert …").
- Eindeutige Begriffsdefinitionen (schon Teil des Stils) — gut für Featured Snippets.

## KI-Suche / LLM-Auffindbarkeit speziell
- **`llms.txt`** im Root: strukturierte Übersicht der Inhalte für KI-Crawler (Titel + kurze Beschreibung + Link
  je Modul/Artikel).
- Klartext-Inhalt ohne JS-Abhängigkeit zum Lesen (statisches HTML — haben wir; KaTeX rendert clientseitig, der
  Formel-**Quelltext** steht aber im HTML, also für Crawler lesbar).
- Konsistente, zitierfähige Fakten (Korrektheit zuerst) — LLMs bevorzugen verlässliche Quellen.

## Status
- Aufgenommen 2026-10-19. **Noch nicht umgesetzt.** Vieles (`sitemap.xml`, `robots.txt`, JSON-LD, OG-Tags,
  `llms.txt`) lässt sich zentral im Generator ergänzen, wenn der 1.-Semester-Content steht. og:image kann die
  spätere Editor-Grafik der jeweiligen Seite nutzen.
