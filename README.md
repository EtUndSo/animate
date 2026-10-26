# animate

Two **independent** animation projects in one repo. Same features, different rendering backend.
Pick one or use both — each works entirely on its own.

| Project | Folder | Backend | Use |
|---|---|---|---|
| **Local** | `local/` | Cairo + ffmpeg | code-only, renders PNG/MP4 on your machine |
| **Web**   | `web/`   | HTML5 Canvas (Pyodide) | runs in the browser; later with editor/GUI |

Code is intentionally duplicated between them (each has its own `engine/`), so the two stay
fully separate.

## Local project (`local/`)
Requirements: Python 3, then `pip install pycairo imageio-ffmpeg numpy`.
```bash
cd local
python run.py          # renders the demo scene -> local/output_videos/ and local/output_images/
```
Write a scene in `local/scenes/` (subclass `Scene`, override `construct()`), point `run.py` at it.

## Web project (`web/`)
A static site. It needs a web server (Pyodide fetches the `.py` files over HTTP):
```bash
cd web
python -m http.server 8000      # then open http://localhost:8000
```
You should see "Hello Sine" rendered by the Python engine via Canvas instead of Cairo.

Deployed with **Cloudflare Pages** — set the project's *Root directory* to `web`; every push to
`main` on GitHub auto-deploys.

## Eigene Artikel von Hand (Umschalter „KI | Mensch“ im Wissensbereich)
Neben jeder KI-Fassung kann eine von Hand geschriebene Fassung desselben Themas stehen. Dateien liegen im
selben Ordner wie die KI-Fassung, mit demselben `pfad:` und `order:`, nur der Dateiname bekommt den Suffix
`-mensch` (optional dazu `autor: mensch` im Kopf; der Suffix allein genügt):

```
content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell.md                     KI, kompakt (steht im Baum)
content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell-ausfuehrlich.md        KI, ausführlich
content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell-mensch.md              von Hand
content/st1/03-mos-feldeffekttransistoren/05-kleinsignalmodell-mensch-ausfuehrlich.md von Hand, ausführlich (optional)
```

Kopf einer Hand-Fassung (Beispiel):
```
---
title: Kleinsignalmodell des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030500
summary: Ein Satz für Übersicht und Suche.
tags: Steilheit, Ausgangsleitwert
autor: mensch
---
```
Danach `python build_wissen.py`. Der Umschalter sitzt in der Kopfleiste neben dem Logo (auf dem Handy unter dem
Titel und oben im Themenbaum): Er wechselt zwischen KI- und Hand-Fassung desselben Themas; ohne Gegenstück ist
der Knopf grau. Die Wahl wird im Browser gemerkt, Themen-Links im Baum und in der Übersicht folgen ihr. Eine
Hand-Fassung ohne KI-Gegenstück erscheint als eigener Eintrag im Baum. Dieselbe Markdown-Syntax wie die
KI-Artikel (Kästen `:::formel`, `:::herleitung`, `::::beispiel`, `:::quiz` usw., Formeln in `$…$`/`$$…$$`).
