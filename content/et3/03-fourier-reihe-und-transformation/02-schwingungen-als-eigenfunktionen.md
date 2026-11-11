---
title: Stufe 1: Schwingungen als Eigenfunktionen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
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

::::kurzfassung
Die Fourier-Beschreibung benutzt von den Bausteinen $\mathrm{e}^{pt}$ nur die reinen Schwingungen. Ein LTI-System ändert eine solche Schwingung nicht in ihrer Form, es multipliziert sie nur mit einer komplexen Zahl.

Für rein imaginäres $p=\mathrm{j}2\pi f$ wird der Baustein zur Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$. Ihre Amplitude ist konstant, sie wächst weder, noch klingt sie ab. Sie ist eine __Eigenfunktion__ jedes LTI-Systems mit der Impulsantwort $h(t)$: Am Ausgang erscheint dieselbe Funktion, nur mit einem Faktor.

$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Der Faktor $H(f)$ heißt __Frequenzgang__ oder Übertragungsfunktion; er existiert, wenn das Integral konvergiert. Sein Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, seine Phase, wie weit sie verschoben wird. Zwei Systeme in Kette ergeben $H(f)=H_1(f)H_2(f)$. Wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

Der Grund: Die Faltung setzt den Ausgang aus verzögerten, gewichteten Kopien des Eingangs zusammen. Eine Verzögerung um $\tau$ macht aus der Schwingung dieselbe Schwingung mal $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$. Jede Kopie ist also die ursprüngliche Schwingung mal einer Zahl, und die mit $h$ gewichtete Summe dieser Zahlen ist $H(f)$.

Falle: Ein reeller Kosinus ist im Allgemeinen keine Eigenfunktion. Verschiebt das System seine Phase, ist der verschobene Kosinus kein Vielfaches des ursprünglichen. Man rechnet deshalb mit $\mathrm{e}^{\mathrm{j}2\pi ft}$ und setzt den Kosinus aus zwei solchen Schwingungen zusammen.
::::

::::formelsammlung
**Reine Schwingung**

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$$

Baustein $\mathrm{e}^{pt}$ mit rein imaginärem $p=\mathrm{j}2\pi f$; $f$ reelle Frequenz. Die Amplitude ist konstant, die Schwingung wächst weder, noch klingt sie ab.

**Schwingung als Eigenfunktion**

$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}$$

Für jedes LTI-System mit der Impulsantwort $h(t)$, dessen Frequenzgang existiert. Grund: Verzögern um $\tau$ ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$.

**Frequenzgang (Übertragungsfunktion)**

$$H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$$

Sofern das Integral existiert. Betrag von $H(f)$: Verstärkung oder Schwächung der Schwingung der Frequenz $f$; Phase von $H(f)$: ihre Verschiebung.

**Kettenschaltung**

$$H(f)=H_1(f)H_2(f)$$

Zwei LTI-Systeme hintereinander multiplizieren ihre Frequenzgänge.

**Zusammenhang mit der Laplace-Transformierten**

$$H(f)=H(p)|_{p=\mathrm{j}2\pi f}$$

Nur wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, die imaginäre Achse also im Konvergenzbereich liegt.
::::
