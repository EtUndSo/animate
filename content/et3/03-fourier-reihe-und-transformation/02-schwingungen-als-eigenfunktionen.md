---
title: Stufe 1: Schwingungen als Eigenfunktionen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3230200
summary: Von den Bausteinen e pt werden jetzt nur die reinen Schwingungen benutzt.
tags: Frequenzgang
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Von den Bausteinen $\mathrm{e}^{pt}$ werden jetzt nur die reinen Schwingungen benutzt. Diese Stufe zeigt, was ein LTI-System mit ihnen macht.
:::

Für rein imaginäres $p=\mathrm{j}2\pi f$ wird der Baustein zur Schwingung mit konstanter Amplitude:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Wie jeder Baustein ist sie eine Eigenfunktion jedes LTI-Systems (Verzögern ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ heißt __Frequenzgang__ oder Übertragungsfunktion. Sein Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, seine Phase, wie weit sie verschoben wird. Zwei Systeme in Kette multiplizieren nacheinander: $H(f)=H_1(f)H_2(f)$. Wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**Kurz gesagt:** Der Frequenzgang ist die Zahl, mit der ein LTI-System eine reine Schwingung multipliziert.
