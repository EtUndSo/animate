---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Der p-n-Übergang
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang
knoten: Kapitel 14: Der p-n-Übergang
order: 4240200
summary: Wie aus zwei dotierten Gebieten ein Ventil für Strom wird
tags: 
lang: de
---

⁠**Dichten ([Kapitel 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) und 11).** Liegt $E_\mathrm F$ mindestens $3k_\mathrm BT$ von beiden Bandkanten entfernt, gilt

<span class="anker" id="gl-0-1"></span>
$$n=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm F}{k_\mathrm BT}\Bigr),\qquad p=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm F-E_\mathrm V}{k_\mathrm BT}\Bigr),\qquad n\,p=n_\mathrm i^2=N_\mathrm CN_\mathrm V\,\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}. \tag{0.1}$$

⁠**Dotierung ([Kapitel 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html) und 13).** In der Störstellenerschöpfung sind alle Fremdatome ionisiert. Die häufigere Sorte heißt Majoritätsträger oder Mehrheit, die seltenere Minoritätsträger oder Minderheit. Der Buchstabe nennt die Trägersorte, der Index das Gebiet, die 0 den Zustand im Gleichgewicht und ohne Raumladung. Im n-Gebiet ist $n_\mathrm{n0}=N_\mathrm D$ und $p_\mathrm{n0}=n_\mathrm i^2/N_\mathrm D$, im p-Gebiet $p_\mathrm{p0}=N_\mathrm A$ und $n_\mathrm{p0}=n_\mathrm i^2/N_\mathrm A$. Im Rechenmodell sind das $10^{16}$ und $7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$ sowie $5\cdot10^{16}$ und $1{,}6\cdot10^{3}\,\mathrm{cm^{-3}}$.

⁠**Strom ([Kapitel 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html) und 13).** Die Stromdichten bestehen aus Drift und Diffusion:

<span class="anker" id="gl-0-2"></span>
$$j_\mathrm n=e\,n\,\mu_\mathrm n\mathcal E+e\,D_\mathrm n\frac{\mathrm{d} n}{\mathrm{d} x},\qquad j_\mathrm p=e\,p\,\mu_\mathrm p\mathcal E-e\,D_\mathrm p\frac{\mathrm{d} p}{\mathrm{d} x},\qquad D_\mathrm n=\frac{k_\mathrm BT}{e}\,\mu_\mathrm n,\quad D_\mathrm p=\frac{k_\mathrm BT}{e}\,\mu_\mathrm p. \tag{0.2}$$

In einem feldfreien Gebiet klingt ein Überschuss an Minoritätsträgern durch Diffusion und Rekombination exponentiell ab, im n-Gebiet $\Delta p_\mathrm n(x)=\Delta p_\mathrm n(0)\,\mathrm{e}^{-x/L_\text{diff,p}}$ mit der Diffusionslänge $L_\text{diff,p}=\sqrt{D_\mathrm p\tau_{\text{rec},\mathrm p}}$. Im Rechenmodell ist $D_\mathrm n=23{,}9\,\mathrm{cm^2/s}$ und $D_\mathrm p=10{,}8\,\mathrm{cm^2/s}$, also $L_\text{diff,n}=48{,}9$ µ m und $L_\text{diff,p}=32{,}9$ µ m.
