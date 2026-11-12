---
title: Überblick: Schutzgrenzen in Hardware und Betriebssystem
kurz: Überblick
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120100
summary: Wer darf was, und wo wird geprüft? Privilegstufen, der Weg in den Kernel, Zeitgeber, Seitentabellen und eine gesicherte Startkette
tags: 
lang: de
---

## Worum es geht

Auf einem Rechner laufen gleichzeitig Dutzende Programme: der Browser, ein Textprogramm, Hilfsprogramme des Systems, vielleicht ein Spiel aus einer unbekannten Quelle. Manche davon gehören verschiedenen Benutzern, manche haben Fehler, und einem davon könnte jemand Schadcode untergeschoben haben. Trotzdem soll keines die Dateien eines anderen lesen, den Rechner für sich allein beanspruchen oder sich so einnisten, dass es beim nächsten Start vor allen anderen läuft.

Dieses Kapitel geht der Frage nach, wer diese Grenzen zieht, womit sie durchgesetzt werden und wie fest sie sind. Bei jeder Grenze lautet die Frage: Wer darf was, und an welcher Stelle prüft wer?

Der Nutzen: Wer weiß, wo eine Grenze sitzt und was sie trägt, kann einschätzen, was ein Angreifer erreicht, der nur ein gewöhnliches Programm kontrolliert, und was ihm noch fehlt. Fast jede Sicherheitsfrage über einen Rechner beginnt mit dieser Einschätzung.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt) und Herleitungen; zum Weiterlesen braucht man sie nicht. Kästen „Achtung“ nennen Regeln, die bei praktischen Übungen immer gelten. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.
