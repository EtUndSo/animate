"""Zahlenwerk für das Oberthema „Halbleiterbauelemente“ (ET1 Kap. 10), Stil 3.

Ein Beispielsystem für alle Artikel des Oberthemas, identisch mit dem MiNa-Lernskript:
Silizium bei T = 300 K; symmetrische Beispieldiode N_A = N_D = 1e16 cm^-3, mu_n = 1250 und mu_p = 450 cm^2/(V s),
Lebensdauer tau = 1 us, Fläche A = 0,1 mm^2. Jede Zahl in Text, Abbildungen, Beispielen und Quiz stammt von hier.

Aufruf:  python -I zahlen_halbleiter.py > zahlen_halbleiter.txt
Die Abbildungsskripte importieren Konstanten und gleichgewicht_profil() aus diesem Modul.
"""
import math
import sys

import numpy as np
from scipy.linalg import solve_banded

# ------------------------------------------------------------------ Naturkonstanten (SI 2019, exakt)
e = 1.602176634e-19          # Elementarladung in C
kB = 1.380649e-23            # Boltzmann-Konstante in J/K
kB_eV = kB / e               # in eV/K
eps0 = 8.8541878128e-14      # elektrische Feldkonstante in F/cm
T = 300.0                    # K
UT = kB * T / e              # Temperaturspannung in V
kT = kB_eV * T               # thermische Energie in eV

# ------------------------------------------------------------------ Silizium (Ioffe-Datenbank, Sze)
Wg = 1.12                    # Bandlücke bei 300 K in eV
Wg0 = 1.206                  # lineare Extrapolation von 300 K auf 0 K (nur für den Temperaturgang von n_i)
N_Si = 5.0e22                # Atome pro cm^3
ni = 1e10                    # Eigenleitungsdichte in cm^-3, gerundet
ni_lit = 9.65e9              # Altermatt et al. 2003
NL, NV = 3.2e19, 1.8e19      # effektive Zustandsdichten von Leitungs- und Valenzband in cm^-3
eps_r = 11.7
eps = eps_r * eps0           # F/cm
mu_n_i, mu_p_i = 1400.0, 450.0   # Beweglichkeiten in schwach dotiertem Si, cm^2/(V s)
mu_n, mu_p = 1250.0, 450.0       # bei 1e16 cm^-3 (Beispieldiode)
WD_P = 0.045                 # Abstand Donatorniveau (Phosphor) unter W_L in eV (gemessen 45,6 meV)
WA_B = 0.045                 # Abstand Akzeptorniveau (Bor) über W_V in eV
m_eff = 0.26                 # Leitfähigkeitsmasse der Elektronen in Einheiten von m_0
a_Si = 0.543                 # Gitterkonstante in nm
d_NN = a_Si * math.sqrt(3) / 4   # Abstand nächster Nachbarn in nm

# Vergleichsmaterialien (Bandlücke in eV, n_i in cm^-3 bei 300 K)
VERGLEICH = [("Germanium", 0.66, 2.0e13), ("Silizium", Wg, ni), ("Galliumarsenid", 1.42, 2.1e6),
             ("Diamant", 5.5, None), ("Siliziumdioxid", 9.0, None)]
n_Cu = 8.5e22                # freie Elektronen in Kupfer pro cm^3 (eines je Atom)
rho_Cu = 1.68e-6             # spezifischer Widerstand Kupfer in Ohm cm

# ------------------------------------------------------------------ Beispieldiode
NA = ND = 1e16               # cm^-3
tau = 1e-6                   # s
A = 1e-3                     # cm^2 (0,1 mm^2)


def ni_von_T(TK):
    """n_i(T) relativ zu n_i(300 K) = 1e10: T^(3/2)-Vorfaktor und exp(-Wg0/(2 kB T)) mit linear genäherter Bandlücke."""
    return ni * (TK / T) ** 1.5 * np.exp(-Wg0 / (2 * kB_eV) * (1 / TK - 1 / T))


def fermi(W, WF, kTe=kT):
    """Fermi-Dirac-Besetzungswahrscheinlichkeit."""
    return 1.0 / (1.0 + np.exp((W - WF) / kTe))


# Lage des Eigenleitungsniveaus W_i: 7 meV unter der Bandmitte, weil N_V < N_L
Wi_off = kT / 2 * math.log(NV / NL)          # W_i minus Bandmitte, in eV (negativ)
WL_Wi = Wg / 2 - Wi_off                      # Abstand W_L - W_i = 0,5674 eV

# abgeleitete Größen der Beispieldiode
Dn, Dp = mu_n * UT, mu_p * UT
Ln, Lp = math.sqrt(Dn * tau), math.sqrt(Dp * tau)
nn0, pp0 = ND, NA
pn0, np0 = ni**2 / ND, ni**2 / NA
JS = e * (Dn * np0 / Ln + Dp * pn0 / Lp)
IS = JS * A
UDiff = UT * math.log(NA * ND / ni**2)
w0 = math.sqrt(2 * eps * UDiff * (NA + ND) / (e * NA * ND))
xn0, xp0 = w0 * NA / (NA + ND), w0 * ND / (NA + ND)
Emax0 = 2 * UDiff / w0
LD = math.sqrt(eps * UT / (e * ND))


def strom(U):
    """Shockley-Form aus dem Zwei-Ströme-Bild: I = I_S (exp(U/U_T) - 1)."""
    return IS * (np.exp(np.asarray(U) / UT) - 1.0)


def weite(U):
    """Weite der Raumladungszone bei angelegter Spannung U (Verarmungsnäherung, nur für U < U_Diff sinnvoll;
    darüber bricht die Näherung zusammen: starke Injektion und Bahnwiderstand bestimmen dann das Verhalten)."""
    return w0 * math.sqrt((UDiff - U) / UDiff) if U < UDiff else float("nan")


def gleichgewicht_profil(xmax=0.6e-4, n_pts=2401):
    """Exakte Lösung der Poisson-Gleichung mit Boltzmann-Dichten (wie im Lernskript).
    Links (x<0) n-Gebiet, rechts p-Gebiet. Rückgabe: dict mit x in cm, n, p in cm^-3, rho/(eN), E in V/cm,
    phi in V (p-Gebiet = 0), W_L und W_V in eV relativ zum Fermi-Niveau."""
    N = ND
    L = math.sqrt(eps * UT / (e * N))
    x = np.linspace(-xmax, xmax, n_pts)
    h = (x[1] - x[0]) / L
    Nd = np.where(x < 0, ND, 0.0)
    Na = np.where(x > 0, NA, 0.0)
    Nd[x == 0] = ND / 2
    Na[x == 0] = NA / 2
    uL, uR = math.log(ND / ni), -math.log(NA / ni)
    psi_dep = np.where(x < -xn0, UDiff,
              np.where(x < 0, UDiff - e * ND / (2 * eps) * (x + xn0)**2,
              np.where(x < xp0, e * NA / (2 * eps) * (xp0 - x)**2, 0.0)))
    u = (psi_dep - UDiff) / UT + uL
    for _ in range(200):
        n_ = ni * np.exp(u)
        p_ = ni * np.exp(-u)
        F = np.zeros_like(u)
        F[1:-1] = (u[2:] - 2 * u[1:-1] + u[:-2]) / h**2 - (n_[1:-1] - p_[1:-1] - Nd[1:-1] + Na[1:-1]) / N
        diag = np.full_like(u, 1.0)
        diag[1:-1] = -2 / h**2 - (n_[1:-1] + p_[1:-1]) / N
        up = np.zeros_like(u)
        lo = np.zeros_like(u)
        up[2:] = 1 / h**2
        lo[:-2] = 1 / h**2
        up[1] = 0.0
        lo[-2] = 0.0
        du = solve_banded((1, 1), np.vstack([up, diag, lo]), -F)
        du = np.clip(du, -1.0, 1.0)
        u += du
        u[0], u[-1] = uL, uR
        if np.max(np.abs(du)) < 1e-10:
            break
    psi = u * UT                                 # Potential relativ zum Eigenleitungsniveau
    n_eq, p_eq = ni * np.exp(u), ni * np.exp(-u)
    WLx = WL_Wi - psi                            # W_L relativ zum Fermi-Niveau, in eV
    return {"x": x, "n": n_eq, "p": p_eq, "rho": (p_eq - n_eq + Nd - Na) / N, "E": -np.gradient(psi, x),
            "phi": psi - psi[-1], "WL": WLx, "WV": WLx - Wg}


def bericht():
    sys.stdout.reconfigure(encoding="utf-8")
    P = print
    P("== Konstanten ==")
    P(f"U_T = kB T/e = {UT*1e3:.3f} mV;  kB T = {kT*1e3:.2f} meV;  U_T ln10 = {UT*math.log(10)*1e3:.1f} mV")
    P("\n== Bänder ==")
    P(f"Wg = {Wg} eV = {Wg/kT:.1f} kB T;  Wg/2 = {Wg/2:.2f} eV = {Wg/2/kT:.2f} kB T")
    P(f"Valenzelektronen = Plätze im Valenzband: 4 * N_Si = {4*N_Si:.1e} cm^-3")
    P(f"Niveauabstand bei ~12 eV Bandbreite: {12/(4*N_Si):.0e} eV")
    P("\n== Leiter / Halbleiter / Isolator (300 K) ==")
    for name, wg, nn in VERGLEICH:
        fak = math.exp(-wg / (2 * kT))
        est = math.sqrt(NL * NV) * fak
        P(f"{name:15s} Wg = {wg:4.2f} eV  exp(-Wg/2kT) = {fak:.1e}  n_i(Abschätzung) = {est:.1e}  Literatur: {nn}")
    P(f"Kupfer: n = {n_Cu:.1e} cm^-3, rho = {rho_Cu:.2e} Ohm cm, sigma = {1/rho_Cu:.2e} S/cm")
    P(f"V_Erde = 1.08e27 m^3 = 1.08e33 cm^3; SiO2-Elektronen darin: {math.sqrt(NL*NV)*math.exp(-9.0/(2*kT))*1.08e33:.0e}")
    P("\n== Eigenleitung ==")
    P(f"n_i = {ni:.0e} cm^-3 (Literatur {ni_lit:.3g}); n_i aus N_L, N_V: {math.sqrt(NL*NV)*math.exp(-Wg/(2*kT)):.2e}")
    P(f"Atome je freies Elektron: {N_Si/ni:.0e}")
    dln = 1.5 / T + Wg0 / (2 * kB_eV * T**2)
    P(f"Temperaturgang: d ln n_i/dT = {dln*100:.2f} %/K; Verdopplung alle {math.log(2)/dln:.1f} K")
    for TK in (250, 300, 350, 400, 500):
        P(f"   n_i({TK} K) = {float(ni_von_T(TK)):.2e} cm^-3")
    Ts = np.linspace(300, 900, 60001)
    P(f"   n_i = N_D = 1e16 bei T = {Ts[np.argmin(abs(np.log(ni_von_T(Ts)/1e16)))]:.0f} K")
    Wi_off = kT / 2 * math.log(NV / NL)
    P(f"Eigenleitungsniveau W_i liegt {Wi_off*1e3:+.1f} meV neben der Bandmitte")
    P(f"f(W_L) bei W_F = W_i: {math.exp(-(Wg/2 - Wi_off)/kT):.1e}")
    sig_i = e * ni * (mu_n_i + mu_p_i)
    P(f"sigma_i = {sig_i:.2e} S/cm, rho_i = {1/sig_i:.2e} Ohm cm")
    P(f"G = R im n-Gebiet: p_n0/tau = {pn0/tau:.0e} cm^-3 s^-1")
    P("\n== Fermi-Verteilung ==")
    for dW in (-3, -1, 0, 1, 3, 5, 10):
        P(f"   f(W_F {dW:+d} kT) = {float(fermi(dW*kT, 0.0)):.4f}   Boltzmann exp(-dW) = {math.exp(-dW):.4f}")
    P("\n== Dotierung (N_D = N_A = 1e16) ==")
    P(f"Fremdatom je Si-Atome: {N_Si/ND:.0e};  mittlerer Abstand N^(-1/3) = {ND**(-1/3)*1e7:.0f} nm")
    P(f"n = {nn0:.0e}, p = n_i^2/N_D = {pn0:.0e}; Verhältnis {nn0/pn0:.0e}")
    dWF = kT * math.log(ND / ni)
    WL_WF = kT * math.log(NL / ND)
    P(f"W_F - W_i = kT ln(N_D/n_i) = {dWF:.3f} eV;  W_L - W_F = kT ln(N_L/N_D) = {WL_WF:.3f} eV")
    P(f"p-Seite: W_F - W_V = kT ln(N_V/N_A) = {kT*math.log(NV/NA):.3f} eV (über n_i und W_i: {Wg - WL_Wi - dWF:.3f} eV);"
      f" n-Seite über n_i und W_i: W_L - W_F = {WL_Wi - dWF:.3f} eV")
    f_D = 1 / (1 + 0.5 * math.exp((WL_WF - WD_P) / kT))
    P(f"W_D - W_F = {WL_WF - WD_P:.3f} eV; neutrale (besetzte) Donatoren: {f_D*100:.2f} %  -> ionisiert {100-f_D*100:.2f} %")
    P(f"E_D/kT = {WD_P/kT:.2f};  Wg/E_D = {Wg/WD_P:.0f}")
    EH = 13.606 * m_eff / eps_r**2
    aB = 0.0529 * eps_r / m_eff
    P(f"Wasserstoffmodell: E_D = 13,6 eV m*/eps_r^2 = {EH*1e3:.0f} meV; Bahnradius = {aB:.2f} nm = {aB/d_NN:.0f} Bindungslängen;"
      f" Atome in der Kugel: {4/3*math.pi*(aB*1e-7)**3*N_Si:.0f}")
    sig_n = e * ND * mu_n
    P(f"sigma(n, 1e16) = {sig_n:.2f} S/cm, rho = {1/sig_n:.2f} Ohm cm; Faktor gegen undotiert: {sig_n/sig_i:.1e};"
      f" Kupfer leitet {1/rho_Cu/sig_n:.1e}-mal besser")
    P(f"dielektrische Relaxationszeit eps/sigma = {eps/sig_n*1e12:.2f} ps")
    P("\n== pn-Übergang im Gleichgewicht ==")
    P(f"U_Diff = U_T ln(N_A N_D/n_i^2) = {UDiff:.3f} V = {UDiff/UT:.1f} U_T; Boltzmann-Faktor exp(-U_Diff/U_T) = {math.exp(-UDiff/UT):.1e}")
    for na, nd in ((1e15, 1e15), (1e16, 1e16), (1e17, 1e17), (1e19, 1e16), (1e20, 1e17)):
        P(f"   N_A = {na:.0e}, N_D = {nd:.0e}:  U_Diff = {UT*math.log(na*nd/ni**2):.3f} V")
    P(f"w = {w0*1e4:.3f} um, x_n = x_p = {xn0*1e4:.3f} um, E_max = {Emax0:.2e} V/cm, Debye-Länge {LD*1e7:.0f} nm")
    pr = gleichgewicht_profil()
    P(f"Poisson numerisch: U_Diff = {pr['phi'][0]:.4f} V, E_max = {pr['E'].max():.2e} V/cm, "
      f"n = p in der Mitte: {pr['n'][len(pr['n'])//2]:.2e} cm^-3")
    rho_C = e * ND
    P(f"Raumladung e N_D = {rho_C:.2e} C/cm^3; Feld nach 0,2 um: {e*ND*0.2e-4/eps:.2e} V/cm")
    P("\n== Ströme ==")
    P(f"D_n = {Dn:.1f}, D_p = {Dp:.1f} cm^2/s; L_n = {Ln*1e4:.0f} um, L_p = {Lp*1e4:.0f} um")
    P(f"J_S = {JS:.3e} A/cm^2 (Elektronen {e*Dn*np0/Ln:.2e}, Löcher {e*Dp*pn0/Lp:.2e}); I_S = {IS:.3e} A")
    for U in (-5.0, -1.0, -0.1, 0.0, 0.1, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7):
        P(f"   U = {U:+.2f} V: Faktor hinauf exp(U/U_T) = {math.exp(U/UT):.3e}, I = {float(strom(U)):+.3e} A,"
          f" Barriere {UDiff-U:.3f} V, w = {weite(U)*1e4:.3f} um")
    J06 = float(strom(0.6)) / A
    P(f"J(0,6 V) = {J06:.3f} A/cm^2; Feld im neutralen n-Gebiet J/sigma = {J06/sig_n:.3f} V/cm;"
      f" Spannung über 100 um: {J06/sig_n*0.01*1e3:.2f} mV")
    P("\n== Einweggleichrichter (Motivation): U_E = 10 V Spitze, R = 1 kOhm ==")
    UA = 9.3
    for _ in range(50):
        UA = 10.0 - UT * math.log(UA / 1e3 / IS + 1)
    P(f"U_A,Spitze = {UA:.2f} V, Diodenspannung {10-UA:.3f} V, Strom {UA/1e3*1e3:.2f} mA")
    P("\n== Atmosphäre (Analogie) ==")
    H = kB * 288 / (29 * 1.66054e-27 * 9.81)
    P(f"Skalenhöhe H = kB T/(m g) = {H/1e3:.1f} km; Mount Everest 8,85 km: {math.exp(-8.85e3/H):.2f}")


if __name__ == "__main__":
    bericht()
