---
title: Overview: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
kurz: Overview
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100100
summary: What the shell makes of a line before a program starts, how to control that with quotes, what a program receives from the shell and how the shell finds it
tags: 
lang: en
---

## What this is about

You type a line and press Enter. By the time a program starts, quite a lot has already happened to this line. Usually you notice none of it, but sometimes you notice something strange: a command is supposed to show the file `mein bericht.txt` (German for “my report.txt”) and complains about two files that do not exist. A program is in the current directory, `ls` shows it, and yet it cannot be started. A setting you have just made has disappeared again in the next terminal window.

This chapter pursues one question: What does the shell do with a command line before it starts a program, and what does it give the program to take along? It shows which parts of a line the shell replaces and how to prevent this deliberately, how to remember values and pass them on to programs, how the shell finds a program in the first place and how settings outlast the end of a session. Afterward, you can predict which arguments a program really receives, and you can explain the surprises above.

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from) and derivations; you do not need them to read on. Boxes marked “Caution” state rules that always apply to practical exercises. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.
