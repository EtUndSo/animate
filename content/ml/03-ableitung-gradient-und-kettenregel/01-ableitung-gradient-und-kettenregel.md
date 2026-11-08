---
title: Überblick: Grundlagen 3 – Ableitung, Gradient und Kettenregel
kurz: Überblick
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
knoten: Grundlagen 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230100
summary: Wie eine Zahl auf ihre Eingänge reagiert: von der Tangente bis zum Rückwärtsmodus
tags: 
lang: de
---

## Worum es geht

Eine Zahl hängt oft von vielen anderen Zahlen ab. Der Preis, den die gewichtete Summe aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) für eine Wohnung vorhersagt, hängt von jedem Gewicht und jedem Merkmal ab. Die Länge eines Fehlervektors hängt von jeder seiner Komponenten ab. Das Ergebnis einer langen Rechnung hängt von jedem Wert ab, mit dem sie beginnt. Dieses Kapitel fragt: Wie stark und in welche Richtung ändert sich eine solche Zahl, wenn man einen ihrer Eingänge ein wenig verändert? Und wenn es tausende Eingänge sind: In welche Richtung muss man alle zugleich verschieben, damit die Zahl am schnellsten wächst oder am schnellsten fällt?

Dazu kommt eine praktische Frage. Oft entsteht die Zahl durch eine lange Kette einfacher Rechenschritte. Man könnte jeden Eingang einzeln ein wenig verändern und nachsehen, was am Ende herauskommt. Bei einer Million Eingängen hieße das, die ganze Rechnung eine Million Mal zu wiederholen. Geht es schneller? Und wie prüft man, ob eine Formel für diese Empfindlichkeiten, die man selbst hergeleitet oder programmiert hat, wirklich stimmt?

Der Nutzen: Mit den Antworten weiß man, an welchen Stellschrauben ein Ergebnis am stärksten hängt und wie sich kleine Messfehler der Eingänge auf das Ergebnis auswirken. Man kann eine komplizierte Funktion in der Nähe eines Punkts durch eine viel einfachere ersetzen und abschätzen, wie groß der Fehler dabei ist. Und man kann die Empfindlichkeiten auch dann ausrechnen, wenn die Zahl aus einer sehr langen Rechnung mit sehr vielen Eingängen entsteht. Diese Werkzeuge braucht fast jedes Verfahren, das aus Daten lernt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum ein Verfahren funktioniert und woher es kommt), Herleitungen und Beweise; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst und führe Programme wirklich aus; die Lösung klappst du direkt unter der Aufgabe auf.
