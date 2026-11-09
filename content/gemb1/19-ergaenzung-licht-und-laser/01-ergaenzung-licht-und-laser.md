---
title: Überblick: Ergänzung: Licht und Laser
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290100
summary: Wie Elektronen Licht aufnehmen und abgeben und wie daraus ein Verstärker für Licht wird
tags: Absorption, spontane Emission, stimulierte Emission, Fluoreszenz, Lebensdauer, Besetzungsumkehr, Pumpen, Laser
lang: de
---

## Worum es geht

Eine Leuchtdiode gibt Licht ab, eine Solarzelle nimmt es auf, und ein Laserpointer wirft einen dünnen Strahl aus einer einzigen Farbe an die Wand. Überall wechselt ein Elektron seine Energie und tauscht dabei ein Lichtteilchen aus. Die Frage dieses Kapitels lautet: *Wie tauschen Elektronen Energie mit Licht aus, und wie wird aus diesem Austausch ein Verstärker für Licht?* Wer das kann, sagt aus den Energien eines Stoffs die Farbe seines Lichts voraus und versteht, warum ein Laser ohne ständige Energiezufuhr nicht arbeitet.

Der Weg führt über acht Begriffe. __Absorption__ heißt: Ein Elektron nimmt ein Lichtteilchen auf und steigt. Die __spontane Emission__ ist das Zurückfallen von selbst, dabei entsteht ein Lichtteilchen. Die __stimulierte Emission__ ist das Zurückfallen, das ein vorbeifliegendes Lichtteilchen auslöst. __Fluoreszenz__ ist das Leuchten eines Stoffs in anderer Farbe, nachdem er Licht aufgenommen hat. Die __Lebensdauer__ ist die mittlere Zeit, die ein Elektron oben bleibt. __Besetzungsumkehr__ heißt, dass oben mehr Elektronen sitzen als unten, __Pumpen__ ist die Energiezufuhr, die das herstellt. Ein __Laser__ ist ein Gerät, das Licht durch stimulierte Emission verstärkt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Drei Niveaus:** Jedes Atom hat ein Elektron und die Energien $E_1=0$, $E_2=1{,}80$ eV, $E_3=2{,}40$ eV. Die mittlere Verweilzeit beträgt auf $E_2$ eine Millisekunde, $\tau_{21}=1$ ms, auf $E_3$ zehn Nanosekunden, $\tau_{32}=10$ ns.

</li>

<li>

⁠**Stab:** ein Kristall der Länge 10 cm mit $N=10^{19}\,\mathrm{cm^{-3}}$ solcher Atome. Ein Elektron bietet einem passenden Lichtteilchen die Trefffläche $A_\mathrm{Ph}=3\cdot10^{-20}\,\mathrm{cm^2}$.

</li>

<li>

⁠**Nanokristall:** ein Würfel aus CdSe mit direkter Bandlücke $E_\mathrm g=1{,}74$ eV und den effektiven Massen $m_\mathrm C^*=0{,}13\,m_0$, $m_\mathrm V^*=0{,}45\,m_0$.

</li>

<li>

⁠**Konstanten:** $hc=1240\,\mathrm{eV\,nm}$, $\hbar^2\pi^2/(2m_0)=0{,}376\,\mathrm{eV\,nm^2}$, $k_\mathrm B=8{,}617\cdot10^{-5}$ eV/K, bei 300 K also $k_\mathrm BT=25{,}85$ meV. Alle Zahlen rechnet `rechnung_kap19.py` nach.

</li>

</ul>
:::
