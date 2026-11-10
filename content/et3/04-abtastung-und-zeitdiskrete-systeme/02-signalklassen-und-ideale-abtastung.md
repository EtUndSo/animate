---
title: Stufe 1: Signalklassen und ideale Abtastung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240200
summary: Welche Arten von Signalen gibt es, und wie beschreibt man das Abtasten mathematisch?
tags: analoges, zeitdiskretes, digitales, ideale Abtaster
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Welche Arten von Signalen gibt es, und wie beschreibt man das Abtasten mathematisch?
:::

**Vier Klassen.** Zeit und Amplitude können jeweils kontinuierlich oder diskret sein. Ein __analoges__ Signal ist in beiden kontinuierlich. Ein __zeitdiskretes__ Signal hat Werte nur zu den Zeiten $nT$, diese aber beliebig genau. Ein __digitales__ Signal ist zusätzlich in der Amplitude gestuft (quantisiert), weil ein Rechner nur endlich viele Zahlen darstellen kann. Dieses Kapitel behandelt die Diskretisierung der Zeit. Die Quantisierung der Amplitude ist ein eigenes Thema.

**Vom realen zum idealen Abtaster.** Ein realer Abtaster schließt in jedem Takt für die kurze Zeit $T_0$ einen Schalter:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

Macht man $T_0$ immer kürzer, bleiben nur noch die Werte $s(nT)$ übrig. Mathematisch ersetzt man das Rechteck durch einen Dirac-Impuls. Das ist der __ideale Abtaster__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

Das abgetastete Signal ist eine Folge von Dirac-Impulsen, jeder mit einem Abtastwert als Gewicht. Der zweite Schritt ist die Siebeigenschaft $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. In dieser Form lassen sich abgetastete Signale mit allen Werkzeugen für kontinuierliche Signale behandeln.
