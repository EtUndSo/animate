---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
order: 4210200
summary: Wie viele Ladungsträger ein Halbleiter hat und wie man ihre Zahl festlegt
tags: 
lang: de
---

⁠**Bänder ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) und 9).** Bei $T=0$ ist das Valenzband voll und das Leitungsband leer. $E_\mathrm V$ ist die Oberkante des Valenzbands, $E_\mathrm C$ die Unterkante des Leitungsbands, $E_\mathrm g=E_\mathrm C-E_\mathrm V$ die Bandlücke. Am Bandrand bewegt sich ein Elektron wie ein Teilchen mit der effektiven Masse $m^*$. Im Silizium-Tal ist sie längs $m_\mathrm h^*=0{,}92\,m_0$ und quer $m_\mathrm l^*=0{,}19\,m_0$, im Valenzband gibt es schwere und leichte Löcher mit $m_\mathrm{hh}^*=0{,}49\,m_0$ und $m_\mathrm{lh}^*=0{,}16\,m_0$.

⁠**Wasserstoff ([Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html)).** Das Elektron im Coulomb-Feld des Protons hat den Grundzustand $E_1=-m_0e^4/(8\varepsilon_0^2h^2)=-13{,}6$ eV. Der Bohr-Radius ist $r_1=0{,}0529$ nm.

⁠**Dichten ([Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html)).** Ein Platz ist mit der Wahrscheinlichkeit $f(E)=1/\bigl(1+\exp\frac{E-E_\mathrm F}{k_\mathrm BT}\bigr)$ besetzt, das Verhältnis von besetzt zu leer ist also $f/(1-f)=\exp\bigl(-\frac{E-E_\mathrm F}{k_\mathrm BT}\bigr)$. Plätze mal Besetzung ergibt die Dichte der Elektronen und der Löcher:

<span class="anker" id="gl-0-1"></span>
$$n=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm F}{k_\mathrm BT}\Bigr),\quad p=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm F-E_\mathrm V}{k_\mathrm BT}\Bigr),\quad N_\mathrm{C,V}=2\Bigl(\frac{2\pi m_\mathrm{C,V}^*k_\mathrm BT}{h^2}\Bigr)^{3/2}. \tag{0.1}$$

Das gilt, wenn $E_\mathrm F$ mindestens $3k_\mathrm BT$ von beiden Bandrändern entfernt liegt (Boltzmann-Näherung). Beim Multiplizieren fällt $E_\mathrm F$ heraus, das ist das Massenwirkungsgesetz:

<span class="anker" id="gl-0-2"></span>
$$n\cdot p=N_\mathrm CN_\mathrm V\,\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}. \tag{0.2}$$
