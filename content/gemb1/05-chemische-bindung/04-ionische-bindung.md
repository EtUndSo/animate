---
title: Stufe 2: Ionische Bindung
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Chemische Bindung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung
knoten: Kapitel 5: Chemische Bindung
order: 4150400
summary: Die Energiekurve ließ offen, woher die Anziehung stammt.
tags: Ionenkristall, stöchiometrisch
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Energiekurve ließ offen, woher die Anziehung stammt. Diese Stufe behandelt den übersichtlichsten Fall: Ein Atom gibt ein Elektron ab, ein anderes nimmt es auf, und zwei Ladungen ziehen sich an.
:::

**Die Idee.** Atome mit niedriger Elektronegativität geben ihre äußersten Elektronen leicht ab und erreichen die Konfiguration des vorigen Edelgases. Atome mit hoher Elektronegativität nehmen Elektronen auf bis zur Konfiguration des nächsten Edelgases. Kalium ist [Ar] 4s$^1$, Chlor [Ne] 3s$^2$ 3p$^5$. Wechselt ein Elektron, haben beide Ionen die Konfiguration von Argon (Abb. [2](#abb-2)). Ebenso gibt Lithium, $1\mathrm s^2\,2\mathrm s^1$, sein 2s-Elektron an Fluor, $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^5$: Li$^+$ gleicht Helium, F$^-$ gleicht Neon.

Der Tausch allein lohnt sich aber nie. Er kostet bei Kalium 4,34 eV und bringt bei Chlor 3,61 eV. Selbst das günstigste Paar aus Cäsium (3,89 eV) und Chlor bleibt um 0,28 eV im Minus. Bezahlt wird er erst durch die Anziehung der entstandenen Ionen. So entstehen Salze wie NaCl, LiF, KCl und KI.

:::abbildung gemb1/k5bilanz 2
Links: Ein Elektron wechselt von Kalium zu Chlor. Die Kreise geben die Ionenradien im Maßstab wieder (0,138 nm und 0,181 nm). Rechts: Energiebilanz in eV je Ionenpaar.
:::

:::satz Satz 2.1 (Energiebilanz der ionischen Bindung)
<span class="anker" id="satz-2-1"></span>

Gegenüber den neutralen Atomen ist die Bindungsenergie eines Ionenpaars

<span class="anker" id="gl-2-1"></span>
$$E_\mathrm{B,A}=E_\mathrm{B}-\bigl(\Delta E_\mathrm{IE}+\Delta E_\mathrm{EA}\bigr). \tag{2.1}$$

Im __Ionenkristall__, einem festen Stoff aus regelmäßig angeordneten Ionen, tritt an die Stelle von $E_\mathrm B$ die Summe aller Energien zwischen den Ionen, $E_\mathrm{Kr}$ je Ionenpaar.
:::

⁠**So liest man das:** $E_\mathrm B$ aus [(1.2)](die-energiekurve-der-bindung.html#gl-1-2) ist der Gewinn gegenüber getrennten Ionen, die Klammer der Preis für den Tausch. Im Kristall ist jedes Kation von Anionen umgeben und umgekehrt. Gleichnamige Ionen stoßen sich ab, sitzen aber weiter weg, die Anziehung der nächsten Nachbarn überwiegt. Typisch sind 5 bis 10 eV je Ionenpaar. **Gültigkeit:** Grenzfall der vollständigen Übergabe, also große Differenz der Elektronegativität.

::::beispiel
Für KCl kostet der Tausch $4{,}34\,\mathrm{eV}-3{,}61\,\mathrm{eV}=0{,}73$ eV. Das Ionenpaar gewinnt 4,79 eV (Stufe [1](die-energiekurve-der-bindung.html#stufe-1)), also $E_\mathrm{B,A}=4{,}06$ eV. Im Salzkristall ist $E_\mathrm{Kr}=7{,}17$ eV, das 1,5-fache des Paars, obwohl der Abstand mit 0,315 nm größer ist. Das ergibt $-6{,}44$ eV gegenüber den Atomen.
::::

⁠**Grenzfall:** Die Coulomb-Energie deckt den Tausch erst unterhalb von $r_\mathrm c=1{,}44\,\mathrm{eV\,nm}/0{,}73\,\mathrm{eV}=1{,}97$ nm. Trennt man KCl weiter, entstehen deshalb neutrale Atome, keine Ionen.

**Eigenschaften.** Ionen mit Edelgashülle sind kugelsymmetrisch, die Bindung ist ungerichtet. Die Ionen packen sich dicht, wie dicht, bestimmt das Verhältnis von Kationen- zu Anionenradius. Weil die Ladungszahlen fest sind, ist es auch das Zahlenverhältnis der Ionen. Solche festen Verhältnisse heißen __stöchiometrisch__, zum Beispiel 1:1 in NaCl, 1:2 in CaF$_2$, 2:3 in Al$_2$O$_3$. Das zweite Elektron des Kaliums käme aus der vollen Argonschale und kostet 31,6 eV, das 7,3-fache des ersten. Die Ionenladung ist zugleich die Valenz aus [Kapitel 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html).

:::frage Geht das Elektron wirklich vollständig über?
Im Modell ja, in der Wirklichkeit fast. Gemessene Elektronendichten zeigen auch in Salzen einen kleinen Rest zwischen den Ionen. Die vollständige Übergabe ist ein Grenzfall, der die Bindung auf das Coulomb-Gesetz zurückführt.
:::

:::aufgabe Aufgabe 2 ★★ Ein LiF-Molekül
<span class="anker" id="aufg-2"></span>

Für das Ionenpaar gilt $E_\mathrm{pot}(r)=-1{,}44\,\mathrm{eV\,nm}/r+K_\mathrm{ab}/r^9$ mit $K_\mathrm{ab}=5{,}6\cdot10^{-8}$ eV nm$^9$. Gegeben sind $\Delta E_\mathrm{IE}(\mathrm{Li})=5{,}39$ eV, $\Delta E_\mathrm{EA}(\mathrm F)=-3{,}40$ eV.

<ol class="al">

<li>

Skizziere beide Anteile und die Summe über $r$.

</li>

<li>

Berechne $r_0$ und $E_\mathrm{pot}(r_0)$.

</li>

<li>

Welche Energie zerlegt das Molekül in neutrale Atome?

</li>

<li>

Unterhalb welchen Abstands deckt die Coulomb-Energie den Tausch?

</li>

<li>

Grenzfall: Wie groß wäre $E_\mathrm B$ bei gleichem $r_0$ für $\gamma_\mathrm{ab}=12$ und für eine harte Wand?

</li>

</ol>

:::loesung
(a) Die Coulomb-Energie steigt von $-\infty$ gegen null, die Abstoßung fällt steil von $+\infty$ gegen null, die Summe hat ein Minimum. (b) $r_0=(9K_\mathrm{ab}/1{,}44\,\mathrm{eV\,nm})^{1/8}=0{,}156$ nm. Coulomb-Energie $-9{,}23$ eV, Abstoßung $+1{,}03$ eV, also $E_\mathrm{pot}(r_0)=-8{,}21$ eV. (c) Der Tausch kostet $5{,}39\,\mathrm{eV}-3{,}40\,\mathrm{eV}=1{,}99$ eV. Also $E_\mathrm{B,A}=8{,}21\,\mathrm{eV}-1{,}99\,\mathrm{eV}=6{,}22$ eV. (d) $r_\mathrm c=1{,}44\,\mathrm{eV\,nm}/1{,}99\,\mathrm{eV}=0{,}72$ nm. (e) $\gamma_\mathrm{ab}=12$: 8,46 eV. Harte Wand: 9,23 eV.
:::
:::

:::aufgabe Aufgabe 3 ★★ Ladungen zählen, Ionen aufreihen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Gib Ionen und Zahlenverhältnis an für Magnesium mit Chlor, Aluminium mit Fluor, Calcium mit Sauerstoff, Lithium mit Sauerstoff.

</li>

<li>

Ionen $+e$ und $-e$ sitzen abwechselnd auf einer langen Kette im Abstand $r$. Zeige mit $\ln2=1-\frac12+\frac13-\dots$, dass die Coulomb-Energie je Ionenpaar $-2\ln2\cdot e^2/(4\pi\varepsilon_0r)$ beträgt. Vergleiche für $r=0{,}30$ nm mit einem einzelnen Paar.

</li>

</ol>

:::loesung
(a) Mg$^{2+}$ und Cl$^-$: MgCl$_2$, 1:2. Al$^{3+}$ und F$^-$: AlF$_3$, 1:3. Ca$^{2+}$ und O$^{2-}$: CaO, 1:1. Li$^+$ und O$^{2-}$: Li$_2$O, 2:1. Die Gesamtladung muss null sein. (b) Ein Ion hat links und rechts je einen Nachbarn im Abstand $r$ (Gegenladung), $2r$ (gleiche Ladung), $3r$ und so weiter. Seine Energie ist $-2\frac{e^2}{4\pi\varepsilon_0r}(1-\frac12+\frac13-\dots)$. Jede Paarenergie gehört zwei Ionen, je Ion zählt also die Hälfte, je Ionenpaar das Ganze: $-2\ln2\cdot e^2/(4\pi\varepsilon_0r)$. Für $r=0{,}30$ nm sind das 6,65 eV gegen 4,80 eV, das 1,39-fache.
:::
:::
