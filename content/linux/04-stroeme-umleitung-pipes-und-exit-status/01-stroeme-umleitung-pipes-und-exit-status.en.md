---
title: Overview: Streams, Redirection, Pipes and Exit Status
kurz: Overview
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090100
summary: What a running program reads and writes, how to send output into files, connect programs into chains and react to success and failure
tags: 
lang: en
---

## What this is about

One program lists files, another counts lines, a third sorts. Each of them can do exactly one thing on its own. But many everyday questions at the computer need several steps: How many programs are there in a directory? Which kinds of fruit are on a long list, each named only once? How do you keep the result of a command instead of just watching it scroll past in the window? And how do you tell whether a command worked without reading its messages?

This chapter pursues one question: How do you get small programs to work together so that they jointly solve a task that none of them can manage alone? It shows the paths by which data gets into a running program and out again, how to connect these paths to files and to other programs and how to make the next command depend on whether the previous one succeeded. Afterward, you can build small tool chains from simple commands, and you understand why they work.

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from) and derivations; you do not need them to read on. Boxes marked “Caution” state rules that always apply to practical exercises. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.
