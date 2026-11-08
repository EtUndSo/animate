---
title: Overview: Foundations 2 – Projection, Eigenvalues and Decompositions
kurz: Overview
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
knoten: Foundations 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15220100
summary: Nearest points, natural directions and the building blocks of a matrix
tags: 
lang: en
---

## What this is about

In Foundations 1 one question was left open. Four apartments are described by their floor area and their number of rooms, and their prices are known. We are looking for two weights with which the weighted sum hits every price. Such weights do not exist: four equations in two unknowns contradict one another. With measured data this is almost always the case. You have more measurements than unknowns, every measurement is slightly inaccurate, and the system of equations has no solution. Still, you need weights, namely the ones that are off by as little as possible.

This chapter pursues this question and two more that turn out to be closely related. Are there directions in which a matrix only makes an arrow longer or shorter without rotating it, and what do these directions reveal about the matrix? And can every matrix be split into a few simple building blocks, ordered by importance, so that the unimportant ones can be left out? On top of that comes a practical question: how much does the result of a calculation change when the data are slightly wrong?

The payoff: with the answers, you fit a line or another simple rule to measured values so that the error is as small as possible. You can tell whether a function of several variables has a hollow, a ridge or a saddle. You approximate an image or a large table with a few numbers and know how much is lost in the process. And you can judge whether a computed result can be trusted. The tools of this chapter show up in almost all later parts of the series.

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why a method works and where it comes from), derivations and proofs; you do not need them to read on. Try the exercises (★ to ★★★) yourself first and actually run the programs; the solution expands right below each exercise.
