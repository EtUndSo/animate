---
title: Überblick: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
kurz: Überblick
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100100
summary: Was die Shell aus einer Zeile macht, bevor ein Programm startet, wie man das mit Anführungszeichen steuert, was ein Programm von der Shell mitbekommt und wie die Shell es findet
tags: 
lang: de
---

## Worum es geht

Du tippst eine Zeile und drückst die Eingabetaste. Bis ein Programm startet, ist mit dieser Zeile schon einiges geschehen. Meistens merkt man davon nichts, manchmal aber etwas Seltsames: Ein Befehl soll die Datei `mein bericht.txt` anzeigen und beschwert sich über zwei Dateien, die es nicht gibt. Ein Programm liegt im aktuellen Verzeichnis, `ls` zeigt es an, und trotzdem lässt es sich nicht starten. Eine Einstellung, die du eben vorgenommen hast, ist im nächsten Terminalfenster wieder verschwunden.

Dieses Kapitel geht der Frage nach: Was macht die Shell mit einer Befehlszeile, bevor sie ein Programm startet, und was gibt sie ihm mit auf den Weg? Es zeigt, welche Teile einer Zeile die Shell ersetzt und wie man das gezielt verhindert, wie man sich Werte merkt und an Programme weiterreicht, wie die Shell ein Programm überhaupt findet und wie Einstellungen das Ende einer Sitzung überdauern. Danach kannst du vorhersagen, welche Argumente ein Programm wirklich bekommt, und die Überraschungen von oben erklären.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt) und Herleitungen; zum Weiterlesen braucht man sie nicht. Kästen „Achtung“ nennen Regeln, die bei praktischen Übungen immer gelten. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.
