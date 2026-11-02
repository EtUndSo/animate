---
title: Von Grund auf: Was aus Teil 2 und Teil 6 gebraucht wird
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170200
summary: Wie aus Sand ein Einkristall wird und wie eine Welle sein Gitter sieht
tags: 
lang: de
---

⁠**Gitter.** Ein Kristall ist Punktgitter plus Basis. Die Gitterpunkte sind die Gittervektoren

<span class="anker" id="gl-0-1"></span>
$$\boldsymbol R=\ell_1\boldsymbol a_1+\ell_2\boldsymbol a_2+\ell_3\boldsymbol a_3,\qquad\ell_1,\ell_2,\ell_3\ \text{ganz}, \tag{0.1}$$

mit den primitiven Gittervektoren $\boldsymbol a_i$. Die primitive Einheitszelle hat den Inhalt $\Omega=|\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)|$. Die Wigner-Seitz-Zelle eines Gitterpunkts enthält alle Orte, die ihm näher sind als jedem anderen Gitterpunkt. Man erhält sie aus den Mittelsenkrechten (im Raum Mittelebenen) der Verbindungslinien zu den Nachbarn. Für die kubischen Gitter mit der Würfelkante $a$ gilt:

| Gitter | primitive Gittervektoren | $\Omega$ | Wigner-Seitz-Zelle |
|---|---|---|---|
| SC | $(a,0,0)$, $(0,a,0)$, $(0,0,a)$ | $a^3$ | Würfel |
| BCC | $\frac a2(1,1,-1)$, $\frac a2(-1,1,1)$, $\frac a2(1,-1,1)$ | $a^3/2$ | abgestumpftes Oktaeder |
| FCC | $\frac a2(1,1,0)$, $\frac a2(1,0,1)$, $\frac a2(0,1,1)$ | $a^3/4$ | Rhombendodekaeder |

Netzebenen sind Scharen paralleler Ebenen durch Gitterpunkte. Ihre Millerschen Indizes $(hkl)$ sind die Kehrwerte der Achsenabschnitte, als teilerfremde ganze Zahlen.

⁠**Welle auf der Kette.** Ein Elektron auf einer Kette aus Punkten $x_\ell=\ell a$ hat die Amplituden $\psi_\ell=A\,\mathrm{e}^{\mathrm{j} k\ell a}$ mit der Wellenzahl $k$ und, mit dem Hüpfparameter $t_0$,

<span class="anker" id="gl-0-2"></span>
$$E(k)=2t_0\bigl(1-\cos(ka)\bigr)+V_0,\qquad v(k)=\frac{2t_0a}{\hbar}\sin(ka),\qquad t_0=\frac{\hbar^2}{2ma^2}. \tag{0.2}$$

Das ist das Kosinus-Band. $k$ und $k+2\pi/a$ liefern an allen Punkten dieselben Zahlen, sie sind dieselbe Welle. Den eindeutigen Bereich $-\pi/a\le k\le\pi/a$ nannte [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) erste Brillouin-Zone, kurz Zone. Im Raum lautet die ebene Welle $\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol r}$ mit dem Wellenvektor $\boldsymbol k$ und $\lambda=2\pi/|\boldsymbol k|$.
