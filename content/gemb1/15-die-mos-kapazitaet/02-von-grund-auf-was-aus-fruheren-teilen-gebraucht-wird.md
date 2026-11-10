---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Die MOS-Kapazität
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat
knoten: Kapitel 15: Die MOS-Kapazität
order: 4250200
summary: Wie eine Spannung am Gate die Oberfläche eines Halbleiters umdreht
tags: Bandverbiegung, Schottky-Näherung
lang: de
---

⁠**Dichten ([Kapitel 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) und 11).** Im Gleichgewicht und im Boltzmann-Bereich gilt

<span class="anker" id="gl-0-1"></span>
$$n=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm F}{k_\mathrm BT}\Bigr),\qquad p=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm F-E_\mathrm V}{k_\mathrm BT}\Bigr),\qquad n\cdot p=n_\mathrm i^2. \tag{0.1}$$

$E_\mathrm{Fi}$ ist die Lage von $E_\mathrm F$ im reinen Kristall. Aus [(0.1)](#gl-0-1) folgt $p=n_\mathrm i\exp\bigl((E_\mathrm{Fi}-E_\mathrm F)/(k_\mathrm BT)\bigr)$. In Störstellenerschöpfung ist $p=N_\mathrm A$ im p-Gebiet und $n=N_\mathrm D$ im n-Gebiet, also

<span class="anker" id="gl-0-2"></span>
$$\text{p-Gebiet: }E_\mathrm{Fi}-E_\mathrm F=k_\mathrm BT\ln\frac{N_\mathrm A}{n_\mathrm i},\qquad\text{n-Gebiet: }E_\mathrm{Fi}-E_\mathrm F=-k_\mathrm BT\ln\frac{N_\mathrm D}{n_\mathrm i}. \tag{0.2}$$

⁠**Feld und Bänder ([Kapitel 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html) und 14).** Das Potential $\varphi$ folgt aus der Poisson-Gleichung:

<span class="anker" id="gl-0-3"></span>
$$\frac{\mathrm{d}\mathcal E}{\mathrm{d} x}=\frac{\rho}{\varepsilon},\qquad\mathcal E=-\frac{\mathrm{d}\varphi}{\mathrm{d} x},\qquad\rho=e\,\bigl(p-n+N_\mathrm D^+-N_\mathrm A^-\bigr). \tag{0.3}$$

Ein Elektron hat die potentielle Energie $-e\varphi$. Deshalb folgen alle Bänder dem Potential, das ist die __Bandverbiegung__. Im Gleichgewicht bleibt $E_\mathrm F$ waagerecht, denn es fließt kein Strom. Die __Schottky-Näherung__ ersetzt eine Raumladung durch einen Kasten: voll verarmt oder neutral.

⁠**Plattenkondensator.** Zwei Platten im Abstand $d$ mit der Permittivität $\varepsilon$ haben je Fläche die Kapazität $C'=\varepsilon/d$. Ein Strich kennzeichnet in diesem Kapitel Größen je Fläche, zum Beispiel $Q'$ in C/m$^2$.
