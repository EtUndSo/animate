---
title: Überblick: Fourier-Reihe und Fourier-Transformation
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230100
summary: Jedes Signal als Überlagerung von Schwingungen
tags: Spektrum
lang: de
---

## Worum es geht

[Kapitel 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) hat gezeigt: Jedes Signal ist eine Überlagerung von Bausteinen $\mathrm{e}^{pt}$, und ein LTI-System multipliziert jeden Baustein nur mit einer Zahl. Die Fourier-Beschreibung benutzt davon nur die Bausteine auf der imaginären Achse, $p=\mathrm{j}2\pi f$: reine Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$, die weder wachsen noch abklingen. Das hat einen großen Vorteil. Eine Schwingung hat eine Frequenz, die man hören, messen und filtern kann. Das __Spektrum__ $S(f)$ sagt, mit welcher Amplitude und Phase jede Frequenz im Signal steckt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Rechteckschwingung** zwischen 0 und 1 mit der Periode $T=2\pi$ s und dem Tastgrad $\frac12$: 1 für $|t|\le T/4$, 0 für $T/4<|t|\le T/2$, periodisch fortgesetzt. Grundfrequenz $F=1/T=0{,}159$ Hz, also $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**RC-Tiefpass** mit $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. Bei der $k$-ten Harmonischen der Rechteckschwingung (ihrem Anteil mit der Frequenz $kF$) ist $2\pi kF\cdot RC=k$, also $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Rechteckimpuls** $\operatorname{rect}(t)$ und $\operatorname{si}(x)=\sin(x)/x$, an der Stelle null durch den Grenzwert $\operatorname{si}(0)=1$ ergänzt.

</li>

</ul>

:::
