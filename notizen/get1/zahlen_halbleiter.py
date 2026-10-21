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


# ------------------------------------------------------------------ Diode als Bauteil (Thema 02: Diode und Kennlinie)
h_P, c0 = 6.62607015e-34, 299792458.0   # Planck-Konstante in J s, Lichtgeschwindigkeit in m/s
l_bahn = 100e-4                          # Länge jedes neutralen Bahngebiets in cm (100 um), Annahme der Beispieldiode
sig_nB, sig_pB = e * ND * mu_n, e * NA * mu_p
R_Bn, R_Bp = l_bahn / (sig_nB * A), l_bahn / (sig_pB * A)
R_B = R_Bn + R_Bp                        # Bahnwiderstand in Ohm
I_KF = IS * NA * ND / ni**2              # Knickstrom der starken Injektion: Randdichte erreicht die Dotierung
E_tun = 1e6                              # Feldstärke, ab der in Si merklich getunnelt wird, V/cm (Sze: ~1e6 V/cm)
E_lawine = 4e5                           # kritische Feldstärke der Lawine bei ~1e16 cm^-3, V/cm (Literatur 3-5e5)


def i_r0(Uj):
    """Grobe obere Schranke des Vorfaktors: e n_i A w/(2 tau), als ob die ganze Zone mit der größten Rate arbeitete.
    Nur noch zum Vergleich; die Artikel benutzen i_rg() und die effektive Weite w_eff()."""
    return e * ni * A * weite(min(Uj, UDiff - 2 * UT)) / (2 * tau)


def d_rand(N):
    """Randschicht der Zone, in der die Majoritätsdichte noch über n_i liegt: Dort ist das Potenzial gegenüber dem
    neutralen Gebiet um weniger als U_T ln(N/n_i) gefallen (Parabel der Verarmungsnäherung)."""
    return math.sqrt(2 * eps * UT * math.log(N / ni) / (e * N))


def w_eff(Uj):
    """Effektive Weite für den Generations-/Rekombinationsstrom: in Sperrrichtung die Zone ohne die beiden
    Randschichten, in Durchlassrichtung die Schicht um die Mitte mit n ≈ p, deren Weite pi U_T/E_max ist."""
    U = min(Uj, UDiff - 2 * UT)
    w = weite(U)
    if Uj < 0:
        return max(w - d_rand(ND) - d_rand(NA), 0.0)
    return math.pi * UT / (2 * (UDiff - U) / w)


def i_rg(Uj, n_pts=6001):
    """Generations- bzw. Rekombinationsstrom der Zone: Netto-Rate nach Shockley-Read-Hall (Störstellen in der
    Bandmitte, gleiche Lebensdauern) über die ganze Zone integriert. Potenzial nach der Verarmungsnäherung;
    Elektronen Boltzmann-verteilt bezogen auf das n-, Löcher bezogen auf das p-Gebiet."""
    U = min(Uj, UDiff - 2 * UT)
    w = weite(U)
    xn, xp = w * NA / (NA + ND), w * ND / (NA + ND)
    x = np.linspace(-xn, xp, n_pts)
    Uz = UDiff - U                                    # Spannung über der Zone
    dphi = np.where(x < 0, e * ND / (2 * eps) * (x + xn) ** 2, Uz - e * NA / (2 * eps) * (xp - x) ** 2)
    n = ND * np.exp(-dphi / UT)
    p = NA * np.exp(-(Uz - dphi) / UT)
    R = (n * p - ni ** 2) / (tau * (n + p + 2 * ni))
    return e * A * float(np.sum((R[1:] + R[:-1]) / 2 * np.diff(x)))


def strom_uebergang(Uj, rek=True, injektion=True):
    """Strom über den Übergang bei der Übergangsspannung Uj: Diffusion (m = 1; bei starker Injektion mit dem
    Knickstrom I_KF gedämpft, Näherung wie in Schaltungssimulatoren) plus Rekombination bzw. Generation in der Zone
    (integrierte Shockley-Read-Hall-Rate, i_rg)."""
    i_d = IS * (math.exp(Uj / UT) - 1.0)
    if injektion and i_d > 0:
        i_d *= math.sqrt(I_KF / (I_KF + i_d))
    return i_d + (i_rg(Uj) if rek else 0.0)


def _bisekt(f, lo, hi, n=200):
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return 0.5 * (lo + hi)


def spannung_real(I, rek=True, injektion=True, RB=None):
    """Klemmenspannung der realen Beispieldiode beim Strom I (I > 0): Übergangsspannung plus I R_B."""
    RB = R_B if RB is None else RB
    Uj = _bisekt(lambda u: strom_uebergang(u, rek, injektion) - I, -1.0, 1.2)
    return Uj + I * RB


def strom_real(U, rek=True, injektion=True, RB=None):
    """Strom der realen Beispieldiode bei der Klemmenspannung U (löst U = Uj + I R_B nach I)."""
    RB = R_B if RB is None else RB
    Uj = _bisekt(lambda u: u + strom_uebergang(u, rek, injektion) * RB - U, -abs(U) - 1.0, max(U, 0.0) + 1.0)
    return strom_uebergang(Uj, rek, injektion)


def IS_von_T(TK):
    """I_S(T) proportional n_i^2 (schwache T-Abhängigkeit von D/L vernachlässigt)."""
    return IS * (float(ni_von_T(TK)) / ni) ** 2


def strom_T(U, TK):
    """Ideale Kennlinie bei der Temperatur TK."""
    return IS_von_T(TK) * (math.exp(U / (kB * TK / e)) - 1.0)


def dUdT(U, TK=T):
    """Temperaturkoeffizient der Durchlassspannung bei festem Strom (U >> U_T): (U - 3 U_T - W_g0/e)/T."""
    return (U - 3 * kB * TK / e - Wg0) / TK


def weite_N(N_A, N_D, Uges):
    """Zonenweite bei der gesamten Spannung Uges = U_Diff - U über der Zone (Verarmungsnäherung)."""
    return math.sqrt(2 * eps * Uges * (N_A + N_D) / (e * N_A * N_D))


def Emax_N(N_A, N_D, Uges):
    """Maximales Feld am Übergang: Fläche des Felddreiecks = Uges, also E_max = 2 Uges / w."""
    return 2 * Uges / weite_N(N_A, N_D, Uges)


def C_j(U, Aq=A):
    """Sperrschichtkapazität eps A / w(U) in F."""
    return eps * Aq / weite(U)


def empfindlichkeit(lam_nm, eta):
    """Fotostrom je Lichtleistung in A/W: eta e lambda/(h c)."""
    return eta * e * lam_nm * 1e-9 / (h_P * c0)


def bericht_diode():
    P = print
    P("\n== Diode als Bauteil (Thema 02) ==")
    P(f"Schreibweise des Skripts: kB T = {kT*1e3:.2f} meV ist eine Energie; U_T = kB T/e = {UT*1e3:.2f} mV")
    P("Durchlassspannung (ideal) bei gegebenem Strom; scheinbare Schwelle = 1 % des Achsenendes:")
    for I in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0):
        P(f"   I = {I:.0e} A: U = U_T ln(I/I_S + 1) = {UT*math.log(I/IS+1):.4f} V;"
          f"  Achse bis {I:.0e} A -> scheinbare Schwelle {UT*math.log(0.01*I/IS+1):.3f} V")
    P(f"Dekade je U_T ln 10 = {UT*math.log(10)*1e3:.1f} mV")
    P("Material bei gleichem Aufbau, I_S ~ n_i^2 (D, L, Beweglichkeiten gleich gesetzt):")
    for name, wg, nn in VERGLEICH[:3]:
        IS_m = IS * (nn / ni) ** 2
        P(f"   {name:15s} Wg = {wg:.2f} eV, n_i = {nn:.1e}: I_S = {IS_m:.2e} A, U(1 mA) = {UT*math.log(1e-3/IS_m+1):.3f} V")
    P(f"\nBahnwiderstand (je {l_bahn*1e4:.0f} um): n-Seite {R_Bn:.2f} Ohm, p-Seite {R_Bp:.2f} Ohm, zusammen R_B = {R_B:.2f} Ohm")
    P(f"Knickstrom der starken Injektion I_KF = I_S N_A N_D/n_i^2 = {I_KF*1e3:.2f} mA (entspricht U_j = U_Diff = {UDiff:.3f} V)")
    P(f"e n_i A = {e*ni*A:.4e} C/cm; grobe Schranke e n_i A w0/(2 tau) = {e*ni*A*w0/(2*tau):.3e} A")
    P(f"Randschicht mit Majoritätsdichte > n_i: d = sqrt(2 eps U_T ln(N/n_i)/(e N)) = {d_rand(ND)*1e4:.4f} um je Seite"
      f" (Potenzialabfall U_T ln(N/n_i) = {UT*math.log(ND/ni):.3f} V)")
    P("Anteile bei der Übergangsspannung Uj (ohne Bahnwiderstand); Rekombination integriert (SRH), "
      "Schätzung mit w_eff = pi U_T/E_max, grobe Schranke mit voller Weite:")
    for Uj in (0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7):
        i_d = IS * (math.exp(Uj / UT) - 1)
        i_r = i_rg(Uj)
        i_est = e * ni * A * w_eff(Uj) / (2 * tau) * (math.exp(Uj / (2 * UT)) - 1)
        i_grob = i_r0(Uj) * (math.exp(Uj / (2 * UT)) - 1)
        Uz = UDiff - min(Uj, UDiff - 2 * UT)
        P(f"   Uj = {Uj:.2f} V: Diffusion {i_d:.3e} A, Rekombination {i_r:.3e} A (Schätzung {i_est:.2e}, Schranke "
          f"{i_grob:.2e}), Anteil Rek. {i_r/(i_d+i_r)*100:5.1f} %, w = {weite(min(Uj, UDiff-2*UT))*1e4:.3f} um, "
          f"E_max = {2*Uz/weite(UDiff-Uz):.3e} V/cm, w_eff = {w_eff(Uj)*1e4:.4f} um")
    Ux = _bisekt(lambda u: IS * (math.exp(u / UT) - 1) - i_rg(u), 0.05, 0.7)
    P(f"Rekombination = Diffusion bei Uj = {Ux:.3f} V, I = {IS*(math.exp(Ux/UT)-1)+i_rg(Ux):.3e} A")
    P("Klemmenspannung der realen Beispieldiode (Rekombination, starke Injektion, R_B):")
    for I in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 3e-2, 1e-1):
        U_id = UT * math.log(I / IS + 1)
        U_re = spannung_real(I)
        Uj = U_re - I * R_B
        dl = 1e-4
        n_eff = (spannung_real(I * (1 + dl), RB=0.0) - spannung_real(I, RB=0.0)) / (UT * math.log(1 + dl))
        P(f"   I = {I:.0e} A: ideal {U_id:.4f} V, real {U_re:.4f} V (Übergang {Uj:.4f} V, I R_B = {I*R_B:.4f} V);"
          f" lokaler Emissionskoeffizient des Übergangs n = {n_eff:.2f}")
    P(f"Sperrbereich: Generationsstrom integriert, Schätzung e n_i A w_eff/(2 tau) mit w_eff = w - 2 d, grobe Schranke:")
    for U in (-0.1, -1.0, -2.0, -5.0, -10.0, -50.0, -100.0):
        ig = i_rg(U)
        P(f"   U = {U:+6.1f} V: w = {weite(U)*1e4:.3f} um, w_eff = {w_eff(U)*1e4:.3f} um, I_gen = {ig*1e12:.1f} pA "
          f"(Schätzung {-e*ni*A*w_eff(U)/(2*tau)*(1-math.exp(U/(2*UT)))*1e12:.1f} pA, Schranke {-i_r0(U)*1e12:.1f} pA),"
          f" ideal -I_S = {-IS*1e15:.1f} fA, Verhältnis {ig/-IS:.0f}")
    P("\nTemperatur:")
    dlnIS = 3 / T + Wg0 / (kB_eV * T**2)
    P(f"   d ln I_S/dT = 3/T + W_g0/(kB T^2) = {dlnIS*100:.1f} %/K, Verdopplung alle {math.log(2)/dlnIS:.1f} K")
    dlnni = 1.5 / T + Wg0 / (2 * kB_eV * T**2)
    P(f"   Generationsstrom ~ n_i: {dlnni*100:.2f} %/K, Verdopplung alle {math.log(2)/dlnni:.1f} K")
    U1 = UT * math.log(1e-3 / IS + 1)
    P(f"   U(1 mA) = {U1:.4f} V; dU/dT = {dUdT(U1)*1e3:.2f} mV/K;  bei 0,6 V {dUdT(0.6)*1e3:.2f}, bei 0,7 V {dUdT(0.7)*1e3:.2f} mV/K")
    P(f"   bei fester Spannung U = {U1:.3f} V: d ln I/dT = {dlnIS*100:.1f} - {U1/(UT*T)*100:.1f} = {(dlnIS - U1/(UT*T))*100:.1f} %/K")
    for TC in (0, 25, 50, 75, 100):
        TK = 273.15 + TC
        U_T1 = _bisekt(lambda u: strom_T(u, TK) - 1e-3, 0.0, 1.0)
        P(f"   {TC:3d} °C: I_S = {IS_von_T(TK):.2e} A, U(1 mA) = {U_T1:.4f} V, n_i = {float(ni_von_T(TK)):.2e}")
    P("\nDurchbruch (Abschätzungen, Verarmungsnäherung):")
    N_eff = NA * ND / (NA + ND)
    Uges_BR = eps * E_lawine**2 / (2 * e * N_eff)
    P(f"   Beispieldiode: Lawine bei E = {E_lawine:.0e} V/cm -> Spannung über der Zone {Uges_BR:.1f} V, "
      f"äußere Sperrspannung {Uges_BR-UDiff:.1f} V, w = {weite_N(NA, ND, Uges_BR)*1e4:.2f} um")
    for Ek in (3.5e5, 4.5e5):
        P(f"      mit E = {Ek:.1e} V/cm: {eps*Ek**2/(2*e*N_eff)-UDiff:.0f} V")
    UZ = 5.6
    Nz = 1e18
    for _ in range(50):
        UD_z = UT * math.log(Nz * Nz / ni**2)
        Neff_z = eps * E_tun**2 / (2 * e * (UD_z + UZ))
        Nz = 2 * Neff_z
    P(f"   Z-Diode 5,6 V (symmetrisch): N_A = N_D = {Nz:.2e} cm^-3, U_Diff = {UD_z:.3f} V, "
      f"w = {weite_N(Nz, Nz, UD_z+UZ)*1e7:.0f} nm, Tunnelstrecke W_g/(e E) = {Wg/E_tun*1e7:.1f} nm")
    P(f"   Kontrolle E_max(1e18, 1e18, U_Diff+5,6 V) = {Emax_N(1e18, 1e18, UT*math.log(1e36/ni**2)+UZ):.3e} V/cm")
    P(f"   Beispieldiode: E_max bei -5 V = {Emax_N(NA, ND, UDiff+5):.2e} V/cm, bei -50 V = {Emax_N(NA, ND, UDiff+50):.2e} V/cm")
    P(f"   W_g/e = {Wg:.2f} V: 4 W_g/e = {4*Wg:.1f} V, 6 W_g/e = {6*Wg:.1f} V")
    P("\nZ-Diode als Spannungsstabilisierung (Beispiel): U_E = 12 V +- 1 V, R_V = 330 Ohm, R_L = 1 kOhm,"
      " U_Z = 5,6 V bei 5 mA, r_Z = 20 Ohm")
    RV, RL, rZ, UZ5 = 330.0, 1000.0, 20.0, 5.6
    UZ0 = UZ5 - rZ * 5e-3
    for UE in (11.0, 12.0, 13.0):
        # Knoten: (UE - UA)/RV = UA/RL + (UA - UZ0)/rZ
        UA = (UE / RV + UZ0 / rZ) / (1 / RV + 1 / RL + 1 / rZ)
        IZ = (UA - UZ0) / rZ
        P(f"   U_E = {UE:.0f} V: U_A = {UA:.4f} V, I_RV = {(UE-UA)/RV*1e3:.2f} mA, I_L = {UA/RL*1e3:.2f} mA,"
          f" I_Z = {IZ*1e3:.2f} mA, P_Z = {UA*IZ*1e3:.0f} mW")
    rp = rZ * RL / (rZ + RL)
    P(f"   Glättungsfaktor 1 + R_V/(r_Z || R_L) = {1+RV/rp:.1f};  ohne Last: U_E = 13 V -> I_Z = "
      f"{(13-UZ0)/(RV+rZ)*1e3:.1f} mA, P_Z = {((13-UZ0)/(RV+rZ))*(UZ0+rZ*(13-UZ0)/(RV+rZ))*1e3:.0f} mW")
    P("\nSperrschichtkapazität (A = 0,1 mm^2) und Schwingkreis mit L = 1 uH:")
    for U in (0.0, -1.0, -2.0, -5.0, -10.0, -25.0):
        Cj = C_j(U)
        P(f"   U = {U:+5.1f} V: w = {weite(U)*1e4:.3f} um, C_j = {Cj*1e12:.2f} pF, f = {1/(2*math.pi*math.sqrt(1e-6*Cj))/1e6:.1f} MHz")
    P(f"   Plattenkondensator-Kontrolle: eps A / w0 = {eps*A/w0*1e12:.2f} pF")
    P(f"Gespeicherte Ladung bei 1 mA: tau I = {tau*1e-3*1e9:.2f} nC; Diffusionskapazität lange Diode (Kleinsignal, "
      f"omega tau << 1): tau I/(2 U_T) = {tau*1e-3/(2*UT)*1e9:.1f} nF (quasistatisch tau I/U_T = {tau*1e-3/UT*1e9:.1f} nF);"
      f" Speicherzeit bei I_F = I_R: tau ln 2 = {tau*math.log(2)*1e6:.2f} us")
    P("\nFotodiode und Solarzelle:")
    P(f"   Grenzwellenlänge h c/W_g = {h_P*c0/(Wg*e)*1e9:.0f} nm; h c/e = {h_P*c0/e*1e9:.1f} nm V")
    for lam, eta in ((850, 0.8), (650, 0.7), (950, 0.85)):
        P(f"   lambda = {lam} nm, Photonenenergie {h_P*c0/(lam*1e-9)/e:.3f} eV, eta = {eta}: S = {empfindlichkeit(lam, eta):.3f} A/W;"
          f" 1 mW -> {empfindlichkeit(lam, eta)*1e-3*1e3:.3f} mA, Photonen/s {1e-3/(h_P*c0/(lam*1e-9)):.2e}")
    J_ph = 35e-3                                   # A/cm^2 bei 1000 W/m^2 (gute Si-Zelle)
    for anteil in (1.0, 0.1, 0.01):
        Iph = J_ph * A * anteil
        UL_id = UT * math.log(Iph / IS + 1)
        UL_re = _bisekt(lambda u: strom_uebergang(u, True, True) - Iph, 0.0, 1.0)
        P(f"   Bestrahlung {anteil*1000:5.0f} W/m^2: I_ph = I_K = {Iph*1e6:.2f} uA, U_L ideal {UL_id:.4f} V, "
          f"mit Rekombination {UL_re:.4f} V")
    Iph = J_ph * A
    us = np.linspace(0, UT * math.log(Iph / IS + 1), 200001)
    pw = us * (Iph - IS * (np.exp(us / UT) - 1))
    k = int(np.argmax(pw))
    UL = UT * math.log(Iph / IS + 1)
    P(f"   MPP (ideal, 1000 W/m^2): U = {us[k]:.4f} V, I = {(Iph-IS*(math.exp(us[k]/UT)-1))*1e6:.2f} uA, "
      f"P = {pw[k]*1e6:.2f} uW, Füllfaktor {pw[k]/(UL*Iph):.3f}, Lichtleistung {1000*A*1e-4*1e3:.3f} mW, "
      f"Wirkungsgrad {pw[k]/(1000*A*1e-4)*100:.1f} %")
    P(f"   U_L-Zuwachs je Dekade Licht: {UT*math.log(10)*1e3:.1f} mV")


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
    bericht_diode()
