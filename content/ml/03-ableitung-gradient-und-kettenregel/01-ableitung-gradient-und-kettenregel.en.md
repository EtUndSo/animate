---
title: Overview: Derivative, Gradient and Chain Rule
kurz: Overview
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230100
summary: How a number responds to its inputs: from the tangent line to reverse mode
tags: 
lang: en
---

## What this is about

A number often depends on many other numbers. The price that the weighted sum from [Chapter 1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) predicts for an apartment depends on every weight and every feature. The length of an error vector depends on each of its components. The result of a long calculation depends on every value it starts with. This chapter asks: how strongly and in which direction does such a number change if you change one of its inputs a little? And if there are thousands of inputs: in which direction must you shift all of them at once so that the number grows fastest or falls fastest?

On top of that comes a practical question. Often the number arises from a long chain of simple calculation steps. You could change each input a little, one at a time, and see what comes out at the end. With a million inputs, that would mean repeating the whole calculation a million times. Is there a faster way? And how do you check whether a formula for these sensitivities that you derived or programmed yourself is really correct?

The payoff: with the answers, you know which adjustable knobs a result depends on most strongly and how small measurement errors in the inputs affect the result. You can replace a complicated function near a point by a much simpler one and estimate how large the error is. And you can compute the sensitivities even when the number arises from a very long calculation with very many inputs. Almost every method that learns from data needs these tools.

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why a method works and where it comes from), derivations and proofs; you do not need them to read on. Try the exercises (★ to ★★★) yourself first and actually run the programs; the solution expands right below each exercise.
