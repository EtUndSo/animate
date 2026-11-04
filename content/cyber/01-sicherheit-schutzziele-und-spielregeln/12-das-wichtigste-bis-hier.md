---
title: Das Wichtigste bis hier
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6111200
summary: Schutzziele, Bedrohungen, Risiko und die Spielregeln aus Recht und Ethik
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Schutzgut: was Wert hat. Berechtigt ist, wer eine Handlung damit ausführen darf; können ist nicht dürfen.

</li>

<li>

Schutzziele: Vertraulichkeit (nur Berechtigte erfahren), Integrität (unverfälscht), Verfügbarkeit (nutzbar), dazu Authentizität und Verbindlichkeit; Schutzbedarf normal, hoch, sehr hoch.

</li>

<li>

Kette: Schwachstelle und Bedrohung, Angreifer, Angriff mit Exploit, Schaden; jede Gegenmaßnahme unterbricht ein Glied.

</li>

<li>

Risiko $R=H\cdot S$ in €/Jahr; eine Maßnahme lohnt sich, wenn $R_\text{vorher}-R_\text{nachher}-K>0$.

</li>

<li>

Sicher ist ein System nur gegen ein Angreifermodell. Angriffsfläche: $P=1-(1-p)^n$, jede abgeschaltete Stelle hilft.

</li>

<li>

Richtlinie sagt was, Mechanismus wie; Mechanismen verhindern, erkennen oder stellen wieder her; passive Angriffe verhindern, aktive erkennen.

</li>

<li>

Prinzipien: minimale Rechte, Aufgabentrennung, sichere Voreinstellung, lückenlose Prüfung, Prüfen und Handeln atomar (TOCTTOU), mehrere unabhängige Linien, Einfachheit, kleine vertrauenswürdige Basis, offenes Verfahren, der Mensch, von Anfang an.

</li>

<li>

CVE benennt, CWE ordnet, CVSS bewertet die Schwere (nicht das Risiko); nach der Veröffentlichung droht jedem System ohne Update der Angriff; gegen Zero-Days helfen nur Prinzipien.

</li>

<li>

StGB: § 202a (Überwindung einer Sicherung), § 202b (Abfangen), § 202c (Vorbereiten), § 202d (Hehlerei), § 303a und § 303b (Verändern, Sabotage; Versuch strafbar), § 263a (Betrug).

</li>

<li>

Erlaubnis des Verfügungsberechtigten im festgelegten Umfang macht den Test befugt; Antragsdelikt heißt nicht erlaubt; Werkzeug nicht strafbar, Einsatz ohne Erlaubnis schon; gute Absicht schützt nicht.

</li>

<li>

Funde koordiniert melden, Kontakt über `/.well-known/security.txt`; geübt wird nur nach den Spielregeln.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein System ist sicher, wenn es seine Richtlinie durchsetzt, also nur Berechtigte Schutzgüter erfahren, verändern und nutzen lässt, und zwar gegen die Angreifer eines festgelegten Angreifermodells; absolute Sicherheit gibt es nicht.

</li>

<li>

Wie viel Schutz genug ist, entscheidet das Risiko, Häufigkeit mal Schaden: Eine Maßnahme lohnt sich, wenn sie mehr erwarteten Schaden verhindert, als sie kostet, und am wirksamsten sind die bewährten Prinzipien wie minimale Rechte, lückenlose Prüfung und mehrere unabhängige Verteidigungslinien.

</li>

<li>

Wer Sicherheit lernt oder prüft, braucht die Erlaubnis des Verfügungsberechtigten: Werkzeuge sind nicht strafbar, ihr Einsatz gegen fremde Systeme ohne Erlaubnis schon, auch mit guter Absicht, und Funde meldet man koordiniert.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel ist eine Antwort auf die Frage: Wer darf was?

| Ergebnis | Woher es kommt |
|---|---|
| Schutzziele | nur Berechtigte dürfen erfahren, verändern, nutzen (Abschnitt [1](was-geschutzt-wird-schutzgut-und-schutzziele.html#stufe-1)) |
| Angriff | eine Handlung ohne Befugnis, die eine Schwachstelle ausnutzt (Abschnitt [2](von-der-schwachstelle-zum-schaden.html#stufe-2)) |
| Risiko und Angreifermodell | wie oft und von wem unbefugt gehandelt wird und was es kostet (Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3)) |
| Richtlinie und Mechanismus | die Richtlinie legt fest, wer was darf, der Mechanismus setzt es durch (Abschnitt [4](richtlinie-und-mechanismus.html#stufe-4)) |
| Minimale Rechte, sichere Voreinstellung | so wenig dürfen wie nötig, ohne Erlaubnis nichts (Abschnitt [5](sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5)) |
| Lückenlose Prüfung, TOCTTOU | bei jedem Zugriff und im Moment der Handlung prüfen, ob er darf (Abschnitt [5](sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5)) |
| Verteidigungslinien, kleine Basis | die Prüfung ob jemand darf, mehrfach und an wenigen sicheren Stellen (Abschnitt [6](sicherheitsprinzipien-systeme-robust-entwerfen.html#stufe-6)) |
| Schwachstelle, CVE, CWE, CVSS | eine Stelle, an der jemand mehr kann, als er darf, benannt und bewertet (Abschnitt [7](schwachstellen-benennen-und-bewerten.html#stufe-7)) |
| §§ 202a bis 303b StGB | strafbar ist das unbefugte Handeln (Abschnitt [8](computerstrafrecht-was-verboten-ist.html#stufe-8)) |
| Erlaubnis, Werkzeug, gute Absicht | entscheidend ist die Erlaubnis des Berechtigten, nicht Technik oder Motiv (Abschnitt [9](erlaubnis-werkzeuge-und-gute-absicht.html#stufe-9)) |
| Offenlegung und Spielregeln | auch der Finder handelt nur mit Abstimmung, geübt wird nur, wo man darf (Abschnitt [10](offenlegung-und-ethik.html#stufe-10)) |
