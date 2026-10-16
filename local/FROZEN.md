# local/ — FROZEN (eingefroren seit 2026-10-16)

Die lokale (Nicht-Web-)Variante ist **stillgelegt**, damit die Entwicklung sich ganz auf die
**Web-Version** (`../web/`) konzentriert.

**Warum:** Die lokale Engine ist eine 2D-Teilmenge, die per Cairo/ffmpeg Videos rendert — also genau
das, was **Manim** bereits (und umfangreicher) kann (kein 3D, keine Updater/ValueTracker, kein
Transform, kein MathTex). Eine eigene Reimplementierung davon bringt keinen Mehrwert.

**Status:** eingefroren, nicht gelöscht. Keine neuen Features hier. Bugfixes nur, falls nötig.

**Falls später ein Offline-/Code-Renderpfad gewünscht ist:** NICHT diese Reimplementierung
weiterführen, sondern **direkt auf Manim aufbauen** (unsere Erweiterungen als Manim-Plugin/Mobjects)
— dann entwickeln wir aktiv Manim weiter, statt es nachzubauen.

Die gesamte aktive Entwicklung (3D, Transform, MathTex via MathJax, Editor, Computations,
Manim-kompatible API) läuft in `../web/`.
