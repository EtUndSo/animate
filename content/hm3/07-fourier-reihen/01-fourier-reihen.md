---
title: Überblick: Fourier-Reihen
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170100
summary: Wie eine periodische Kurve in reine Schwingungen zerfällt
tags: Fourier-Reihe, Fourier-Koeffizient, Fourier-Polynom, Bestapproximation, Parseval-Identität, Faltung, Dirichlet-Kern, Poisson-Kern
lang: de
---

## Worum es geht

Die Netzspannung, ein Geigenton und das Taktsignal eines Prozessors haben eines gemeinsam: Ihr Verlauf wiederholt sich. Die Frage dieses Kapitels lautet: *Lässt sich jede periodische Kurve aus reinen Schwingungen zusammensetzen, und in welchem Sinn stimmt die Summe dann mit der Kurve überein?* Der Nutzen: Eine reine Schwingung ist leicht zu behandeln, denn eine lineare Schaltung ändert nur ihre Höhe und ihre Verschiebung. Wer ein Signal in Schwingungen zerlegen kann, rechnet jede für sich und setzt das Ergebnis wieder zusammen. Dasselbe Werkzeug bestimmt die Temperatur in einer runden Platte, von der man nur den Rand kennt.

Der Weg führt über acht Begriffe. Eine __Fourier-Reihe__ ist eine unendliche Summe von Schwingungen. Ein __Fourier-Koeffizient__ sagt, wie stark eine Schwingung in einer Funktion steckt. Ein __Fourier-Polynom__ ist eine endliche Teilsumme der Reihe. Die __Bestapproximation__ ist die beste Näherung aus einer vorgegebenen Menge von Funktionen. Die __Parseval-Identität__ vergleicht die Energie einer Funktion mit den Energien ihrer Schwingungen. Die __Faltung__ ist ein gleitender, gewichteter Mittelwert. Der __Dirichlet-Kern__ ist das Gewicht, mit dem ein Fourier-Polynom mittelt. Der __Poisson-Kern__ ist das Gewicht, mit dem die Randwerte einer Kreisscheibe in ihr Inneres wirken.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Die Rechenmodelle für dieses Kapitel
Alle drei Funktionen werden mit der Periode $2\pi$ auf ganz $\mathbb{R}$ fortgesetzt.

<ul>

<li>

⁠**Rechteck** $q$: $q(x)=1$ auf $(0,\pi)$, $q(x)=-1$ auf $(\pi,2\pi)$, $q(0)=q(\pi)=0$.

</li>

<li>

⁠**Dreieck** $w$: $w(x)=|x|$ auf $[-\pi,\pi]$. Der Buchstabe sieht aus wie das Zickzack.

</li>

<li>

⁠**Sägezahn** $s$: $s(x)=\frac{\pi-x}2$ auf $(0,2\pi)$, $s(0)=0$.

</li>

</ul>

Vorausgesetzt werden komplexe Zahlen, die Eulersche Formel $\mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x$, partielle Integration und aus [Teil 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html) gleichmäßige Konvergenz, der M-Test und das quadratische Mittel, dazu Parameterintegrale ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) und der Laplace-Operator in Polarkoordinaten ([Teil 4](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/koordinatentransformationen.html)).
:::
