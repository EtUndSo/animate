"""Zahlenwerk für Schaltungstechnik, MOS-Feldeffekttransistoren (Stil 3). Thema 1: Aufbau und Funktionsweise des
MOSFET (Abschnitte A bis K); Thema 2: Kennlinien des NMOS-Transistors (Abschnitte L bis R); Thema 3: PMOS-Transistor,
Substrateffekt und Latch-Up (Abschnitte S bis V und Nachträge am Ende). Spätere Themen des Kapitels ergänzen dieses Skript.

Eigenes Beispielsystem (keine Aufgabe aus Skript oder Übung), das Beispiel-Transistorpaar des ganzen Kapitels:
- Silizium bei T = 300 K mit den Konstanten des ET1-Zahlenwerks (notizen/get1/zahlen_halbleiter.py): U_T = 25,85 mV,
  n_i = 1e10 cm^-3, eps_r = 11,7, N_L = 3,2e19 und N_V = 1,8e19 cm^-3;
- Gateoxid SiO2 mit t_ox = 5 nm (eps_r = 3,9), daraus C'_ox = 6,91 fF/µm^2;
- NMOS: W = 10 µm, L = 1 µm, K'_n = mu_n C'_ox = 200 µA/V^2, also K_n = 2 mA/V^2 und I_D = K_n/2 (U_GS - U_th)^2 in
  Sättigung (identisch mit k = K_n/2 = 1 mA/V^2 der Netzwerkanalyse), U_th0 = 0,50 V, lambda_n = 0,1 1/V (passt zu
  g_o = 25 µS bei 0,25 mA in der Netzwerkanalyse); Gate aus n+-Polysilizium, Kanaldotierung N_A so bestimmt, dass
  U_th0 = 0,50 V wird;
- PMOS: W = 40 µm, L = 1 µm, K'_p = 50 µA/V^2, also K_p = 2 mA/V^2, U_th0,p = -0,50 V, lambda_p = 0,1 1/V; Gate aus
  p+-Polysilizium, Wannendotierung N_D so bestimmt, dass U_th0,p = -0,50 V wird.
Aufruf: python -I zahlen_mosfet.py > zahlen_mosfet.txt
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "get1"))
import zahlen_halbleiter as zh  # noqa: E402

P = print


def kopf(t):
    P()
    P("=" * 100)
    P(t)
    P("=" * 100)


# ------------------------------------------------------------------ Konstanten (aus dem ET1-Zahlenwerk)
q = zh.e                      # Elementarladung in C
kB = zh.kB
T = zh.T
UT = zh.UT                    # 25,852 mV
ni = zh.ni                    # 1e10 cm^-3
NC, NV = zh.NL, zh.NV         # effektive Zustandsdichten in cm^-3
eps0 = zh.eps0                # F/cm
eps_si = zh.eps_r * eps0      # 11,7 eps0 in F/cm
eps_ox = 3.9 * eps0           # F/cm

# ------------------------------------------------------------------ Beispieltechnologie und Transistorpaar
t_ox = 5e-7                   # cm (5 nm)
Cox = eps_ox / t_ox           # F/cm^2
Kn_s, Kp_s = 200e-6, 50e-6    # Prozessparameter mu C'_ox in A/V^2
Wn, Ln = 10e-4, 1e-4          # cm
Wp, Lp = 40e-4, 1e-4          # cm
Kn = Kn_s * Wn / Ln           # 2 mA/V^2
Kp = Kp_s * Wp / Lp           # 2 mA/V^2
Uth_n, Uth_p = 0.50, -0.50    # V
lam_n, lam_p = 0.1, 0.1       # 1/V
mu_n = Kn_s / Cox             # cm^2/(V s)
mu_p = Kp_s / Cox

phi_gate_n = UT * math.log(NC / ni)   # Fermi-Niveau im n+-Poly an der Leitungsbandkante: Abstand zu W_i in V
phi_gate_p = UT * math.log(NV / ni)   # Fermi-Niveau im p+-Poly an der Valenzbandkante


def phi_F(N):
    return UT * math.log(N / ni)


def Qdep_max(N):
    """Betrag der Verarmungsladung pro Fläche an der Schwelle (Oberflächenpotential 2 phi_F), C/cm^2."""
    return math.sqrt(2 * q * eps_si * N * 2 * phi_F(N))


def xd_max(N):
    return math.sqrt(2 * eps_si * 2 * phi_F(N) / (q * N))


def phi_MS_n(NA):
    """Kontaktspannung n+-Poly-Gate gegen p-Substrat: -(U_T ln(N_C/n_i) + phi_F) = -U_T ln(N_C N_A/n_i^2)."""
    return -(phi_gate_n + phi_F(NA))


def Uth0_n(NA, Qox=0.0, Cox_=None):
    C = Cox if Cox_ is None else Cox_
    UFB = phi_MS_n(NA) - Qox / C
    return UFB + 2 * phi_F(NA) + Qdep_max(NA) / C


def phi_MS_p(ND):
    return phi_gate_p + phi_F(ND)


def Uth0_p(ND):
    return phi_MS_p(ND) - 2 * phi_F(ND) - Qdep_max(ND) / Cox


def bisekt(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = math.sqrt(lo * hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return math.sqrt(lo * hi)


NA = bisekt(lambda N: Uth0_n(N) - Uth_n, 1e15, 1e19)
ND = bisekt(lambda N: -(Uth0_p(N) - Uth_p), 1e15, 1e19)

kopf("A. Beispieltechnologie und Beispiel-Transistorpaar (gilt für alle Themen des Kapitels)")
P(f"U_T = {UT*1e3:.3f} mV, n_i = {ni:.2e} cm^-3, eps_Si = 11,7 eps0 = {eps_si:.4e} F/cm, eps_ox = 3,9 eps0 = {eps_ox:.4e} F/cm")
P(f"t_ox = {t_ox*1e7:.1f} nm -> C'_ox = eps_ox/t_ox = {Cox:.4e} F/cm^2 = {Cox*1e7:.3f} fF/µm^2 (1 fF/µm^2 = 1e-7 F/cm^2)")
P(f"NMOS: W = {Wn*1e4:.0f} µm, L = {Ln*1e4:.0f} µm, W/L = {Wn/Ln:.0f}, K'_n = {Kn_s*1e6:.0f} µA/V^2 -> K_n = {Kn*1e3:.2f} mA/V^2;"
  f" mu_n,eff = K'_n/C'_ox = {mu_n:.1f} cm^2/(V s)")
P(f"      U_th0 = {Uth_n:.2f} V, lambda_n = {lam_n} 1/V; Gate-Oxid-Kapazität C_ox = W L C'_ox = {Wn*Ln*Cox*1e15:.2f} fF")
P(f"PMOS: W = {Wp*1e4:.0f} µm, L = {Lp*1e4:.0f} µm, W/L = {Wp/Lp:.0f}, K'_p = {Kp_s*1e6:.0f} µA/V^2 -> K_p = {Kp*1e3:.2f} mA/V^2;"
  f" mu_p,eff = {mu_p:.1f} cm^2/(V s)")
P(f"      U_th0,p = {Uth_p:.2f} V, lambda_p = {lam_p} 1/V; C_ox = {Wp*Lp*Cox*1e15:.1f} fF")
P(f"Verhältnis K'_n/K'_p = {Kn_s/Kp_s:.1f} (Beweglichkeitsverhältnis im Kanal); gleiches K bei W_p = 4 W_n")
P(f"Kontrolle Netzwerkanalyse: Sättigung bei U_GS = 1 V: I_D = K_n/2 (0,5 V)^2 = {Kn/2*0.25*1e3:.3f} mA, "
  f"g_m = K_n (U_GS - U_th) = {Kn*0.5*1e3:.3f} mS, g_o ~ lambda I_D = {lam_n*Kn/2*0.25*1e6:.1f} µS")

kopf("B. Kanaldotierung und Schwellenspannung des NMOS (n+-Poly-Gate, keine Oxidladung)")
pF = phi_F(NA)
P(f"Kanaldotierung so gewählt, dass U_th0 = 0,500 V: N_A = {NA:.4e} cm^-3 (gerundet {NA:.2g})")
P(f"Fermi-Potential phi_F = U_T ln(N_A/n_i) = {pF*1e3:.2f} mV; 2 phi_F = {2*pF*1e3:.2f} mV")
P(f"Fermi-Niveau im n+-Poly: U_T ln(N_C/n_i) = {phi_gate_n*1e3:.2f} mV über W_i (an der Leitungsbandkante)")
PMS = phi_MS_n(NA)
P(f"Kontaktspannung phi_MS = -(U_T ln(N_C/n_i) + phi_F) = -U_T ln(N_C N_A/n_i^2) = {PMS*1e3:.2f} mV "
  f"(Kontrolle {-UT*math.log(NC*NA/ni**2)*1e3:.2f} mV)")
xd = xd_max(NA)
Qd = Qdep_max(NA)
P(f"Verarmungsweite an der Schwelle x_d,max = sqrt(2 eps 2phi_F/(q N_A)) = {xd*1e7:.2f} nm")
P(f"Verarmungsladung |Q'_dep| = q N_A x_d = sqrt(2 q eps N_A 2 phi_F) = {Qd:.4e} C/cm^2 = {Qd*1e7:.3f} fC/µm^2 "
  f"(Kontrolle q N_A x_d = {q*NA*xd:.4e}); Akzeptorionen pro µm^2: {NA*xd*1e-8:.0f}")
P(f"|Q'_dep|/C'_ox = {Qd/Cox*1e3:.2f} mV")
P(f"U_th0 = phi_MS + 2 phi_F + |Q'_dep|/C'_ox = {PMS:.4f} + {2*pF:.4f} + {Qd/Cox:.4f} = {Uth0_n(NA):.4f} V")
P(f"Feld an der Oberfläche an der Schwelle E_s = |Q'_dep|/eps_Si = {Qd/eps_si:.3e} V/cm; im Oxid E_ox = |Q'_dep|/eps_ox = "
  f"{Qd/eps_ox:.3e} V/cm (Verhältnis eps_Si/eps_ox = {eps_si/eps_ox:.2f})")
P(f"Spannungsaufteilung an der Schwelle zwischen Oxid und Halbleiter: U_ox = {Qd/Cox:.4f} V, psi_s = {2*pF:.4f} V, "
  f"Summe = U_th0 - U_FB = {Qd/Cox + 2*pF:.4f} V")
gam_n = math.sqrt(2 * q * eps_si * NA) / Cox
P(f"Substratsteuerfaktor gamma_n = sqrt(2 q eps N_A)/C'_ox = {gam_n:.4f} sqrt(V) (für Thema 3)")
P("Varianten:")
for N in (1e16, 4e16, 1e17, 3e17, NA, 1e18):
    P(f"  N_A = {N:.2e}: phi_F = {phi_F(N)*1e3:6.1f} mV, phi_MS = {phi_MS_n(N)*1e3:7.1f} mV, |Q'_dep|/C'_ox = "
      f"{Qdep_max(N)/Cox*1e3:6.1f} mV, x_d,max = {xd_max(N)*1e7:6.1f} nm, U_th0 = {Uth0_n(N)*1e3:7.1f} mV")
P(f"  Skript-Typwert N_sub = 4e16: phi_F = {phi_F(4e16)*1e3:.1f} mV (mit n_i = 1,4e10 aus dem Skript: "
  f"{UT*math.log(4e16/1.4e10)*1e3:.1f} mV; angegebene 0,33 V passen zu keinem der beiden)")
# Gegenprobe Lehrbuchbeispiel (Berkeley EE105): t_ox = 20 nm, N_a = 5e16, phi_n+ = 550 mV, n_i = 1e10 -> V_T = 0,52 V
Cox20 = eps_ox / 20e-7
UFB_b = -(0.550 + phi_F(5e16))
UT_b = UFB_b + 2 * phi_F(5e16) + Qdep_max(5e16) / Cox20
P(f"Gegenprobe Lehrbuchbeispiel t_ox = 20 nm, N_A = 5e16, Gate 550 mV: U_FB = {UFB_b:.3f} V, U_th = {UT_b:.3f} V")
for dN in (0.9, 1.1):
    P(f"Empfindlichkeit: N_A x {dN}: U_th0 = {Uth0_n(NA*dN)*1e3:.1f} mV")
for tx in (4.5e-7, 5.5e-7):
    P(f"Empfindlichkeit: t_ox = {tx*1e7:.1f} nm: U_th0 = {Uth0_n(NA, Cox_=eps_ox/tx)*1e3:.1f} mV")
Qox = 5e10 * q
P(f"Positive Oxidladung 5e10 q/cm^2: Verschiebung -Q'_ox/C'_ox = {-Qox/Cox*1e3:.2f} mV; 1e11: {-2*Qox/Cox*1e3:.2f} mV")
UFB = PMS
P(f"Flachbandspannung U_FB = phi_MS = {UFB:.4f} V (ohne Oxidladung)")


# ------------------------------------------------------------------ exakter MOS-Kondensator (Poisson + Boltzmann)
pp0 = NA
np0 = ni ** 2 / NA
LDb = math.sqrt(eps_si * UT / (q * pp0))      # extrinsische Debye-Länge


def Qs_exakt(psi, mit_elektronen=True):
    """Flächenladung im Halbleiter (C/cm^2) als Funktion des Oberflächenpotentials psi (V), exakte Lösung der
    Poisson-Gleichung mit Boltzmann-Dichten (p-Substrat, vollständig ionisiert). Vorzeichen: negativ für psi > 0."""
    b = psi / UT
    F2 = (math.exp(-b) + b - 1)
    if mit_elektronen:
        F2 += (np0 / pp0) * (math.exp(b) - b - 1)
    F = math.sqrt(max(F2, 0.0))
    return -math.copysign(1.0, psi) * math.sqrt(2 * eps_si * kB * T * pp0 * 1e0) * F if psi != 0 else 0.0


# Einheitenprüfung: eps [F/cm] * kB T [J] * p [cm^-3] -> C^2/cm^4; sqrt -> C/cm^2


def UGB_von_psi(psi):
    return UFB + psi - Qs_exakt(psi) / Cox


def psi_von_UGB(U):
    lo, hi = -1.5, 1.6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if UGB_von_psi(mid) < U:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def Qinv_exakt(psi):
    return Qs_exakt(psi) - Qs_exakt(psi, mit_elektronen=False)


kopf("C. MOS-Kondensator exakt (Poisson-Gleichung mit Boltzmann-Dichten), NMOS-Gatestapel, Bulk als Bezug")
P(f"Debye-Länge im Substrat L_D = sqrt(eps U_T/(q N_A)) = {LDb*1e7:.2f} nm; n_p0 = n_i^2/N_A = {np0:.1f} cm^-3")
P(f"Exakt: U_GB bei psi_s = 2 phi_F: {UGB_von_psi(2*pF):.4f} V (Formel U_th0 = 0,5000 V)")
P(f"Exakt: U_GB bei psi_s = phi_F (Oberfläche eigenleitend, n_s = n_i): {UGB_von_psi(pF):.4f} V")
P(f"Exakt: psi_s bei U_GB = 0: {psi_von_UGB(0.0)*1e3:.1f} mV; Verarmungsnäherung: Lösung von psi + gamma sqrt(psi) = -U_FB:")
s_ = (-gam_n + math.sqrt(gam_n ** 2 + 4 * (-UFB))) / 2
P(f"  sqrt(psi) = {s_:.4f} -> psi = {s_**2*1e3:.1f} mV")
P(f"{'U_GB/V':>7} {'psi_s/mV':>9} {'n_s/cm^-3':>11} {'p_s/cm^-3':>11} {'Q_s/(fC/µm^2)':>14} {'Q_inv/(fC/µm^2)':>16}"
  f" {'Cox(U-Uth)':>11} {'Zustand':>12}")
for U in (-2.0, -1.5, UFB, -0.5, 0.0, 0.25, 0.4, 0.5, 0.6, 0.75, 1.0, 1.5, 2.0, 2.5):
    ps = psi_von_UGB(U)
    ns = np0 * math.exp(ps / UT)
    psx = pp0 * math.exp(-ps / UT)
    Qs = Qs_exakt(ps)
    Qi = Qinv_exakt(ps)
    lin = -Cox * (U - Uth_n) if U > Uth_n else 0.0
    if U < UFB - 1e-6:
        z = "Anreicherung"
    elif abs(U - UFB) < 1e-6:
        z = "Flachband"
    elif ps < 2 * pF:
        z = "Verarmung"
    else:
        z = "Inversion"
    P(f"{U:7.3f} {ps*1e3:9.1f} {ns:11.3e} {psx:11.3e} {Qs*1e7:14.4f} {Qi*1e7:16.4f} {lin*1e7:11.4f} {z:>12}")
P("Oberflächendichte n_s = n_p0 exp(psi_s/U_T) (Boltzmann):")
for ps in (0.0, 0.25, 0.5, pF, 0.6, 0.8, 2 * pF):
    P(f"  psi_s = {ps*1e3:6.1f} mV: n_s = {np0*math.exp(ps/UT):.3e} cm^-3, p_s = {pp0*math.exp(-ps/UT):.3e} cm^-3")
ps1 = psi_von_UGB(1.0)
P(f"Bei U_GB = 1 V: psi_s = {ps1*1e3:.1f} mV (= 2 phi_F + {(ps1-2*pF)*1e3:.1f} mV = 2 phi_F + {(ps1-2*pF)/UT:.2f} U_T); "
  f"Q_inv exakt = {Qinv_exakt(ps1)*1e7:.4f} fC/µm^2 gegen C'_ox (U - U_th) = {Cox*0.5*1e7:.4f} fC/µm^2 "
  f"({(Qinv_exakt(ps1)/(-Cox*0.5)-1)*100:+.1f} %)")
ps2 = psi_von_UGB(1.5)
P(f"Bei U_GB = 1,5 V: psi_s = {ps2*1e3:.1f} mV, Q_inv exakt = {Qinv_exakt(ps2)*1e7:.4f}, linear {Cox*1.0*1e7:.4f} fC/µm^2 "
  f"({(Qinv_exakt(ps2)/(-Cox*1.0)-1)*100:+.1f} %)")
# Steigung dQ_inv/dU_GB in starker Inversion -> extrapolierte Schwelle
Ua, Ub = 1.0, 1.5
Qa, Qb = Qinv_exakt(psi_von_UGB(Ua)), Qinv_exakt(psi_von_UGB(Ub))
steig = (Qb - Qa) / (Ub - Ua)
U0 = Ua - Qa / steig
P(f"Extrapolation von Q_inv(U) zwischen 1,0 und 1,5 V auf null: U = {U0:.4f} V; Steigung = {-steig/Cox:.4f} C'_ox")
P(f"psi_s-Anstieg von der Schwelle (U = 0,5 V) bis 1,0 V: {(ps1 - psi_von_UGB(0.5))*1e3:.1f} mV; bis 1,5 V: "
  f"{(ps2 - psi_von_UGB(0.5))*1e3:.1f} mV")
P(f"Verarmungsladung bei 1,0 V: {Qs_exakt(ps1, False)*1e7:.4f} fC/µm^2 (an der Schwelle exakt "
  f"{Qs_exakt(psi_von_UGB(0.5), False)*1e7:.4f}, Näherung {-Qd*1e7:.4f})")
for U in (0.5, 1.0, 1.5, 2.5):
    ps = psi_von_UGB(U)
    xdx = -Qs_exakt(ps, False) / (q * NA)
    P(f"  U_GB = {U:.1f} V: psi_s - 2 phi_F = {(ps-2*pF)*1e3:6.1f} mV = {(ps-2*pF)/UT:4.2f} U_T, Verarmungsweite "
      f"(Ladung/(q N_A)) = {xdx*1e7:.1f} nm, Elektronen/Ionen pro µm^2 = {-Qinv_exakt(ps)/q*1e-8:.0f}/"
      f"{xdx*NA*1e-8:.0f}")
P(f"Verarmungsweite bei U_GB = 0 (Näherung) x_d = sqrt(2 eps psi/(q N_A)) mit psi = 0,5655 V: "
  f"{math.sqrt(2*eps_si*psi_von_UGB(0.0)/(q*NA))*1e7:.1f} nm")

kopf("D. Kapazität des MOS-Kondensators: niederfrequent (NF) und hochfrequent (HF)")


def C_NF(U, dU=1e-4):
    return -(Qs_exakt(psi_von_UGB(U + dU)) - Qs_exakt(psi_von_UGB(U - dU))) / (2 * dU)


def C_HF(U):
    """Hochfrequent: die Inversionsladung folgt nicht; nur die Verarmungskante bewegt sich (Verarmungsnäherung mit
    eingefrorener Inversionsladung). C_dep = eps/x_d mit x_d aus der Verarmungsladung des Gleichgewichts."""
    ps = psi_von_UGB(U)
    if ps <= 0:
        return C_NF(U)
    Qb = -Qs_exakt(ps, mit_elektronen=False)
    xdx = Qb / (q * NA)
    Cdep = eps_si / max(xdx, 1e-12)
    return Cox * Cdep / (Cox + Cdep)


P(f"C'_ox = {Cox*1e7:.3f} fF/µm^2; C'_dep,min = eps/x_d,max = {eps_si/xd*1e7:.3f} fF/µm^2; Reihenschaltung = "
  f"{Cox*(eps_si/xd)/(Cox+eps_si/xd)*1e7:.3f} fF/µm^2 = {(eps_si/xd)/(Cox+eps_si/xd):.3f} C'_ox")
P(f"Flachbandkapazität: C'_FB = C'_ox eps/(eps + C'_ox L_D) mit L_D = {LDb*1e7:.2f} nm: "
  f"{Cox*eps_si/(eps_si+Cox*LDb)*1e7:.3f} fF/µm^2 = {eps_si/(eps_si+Cox*LDb):.3f} C'_ox")
P(f"{'U_GB/V':>7} {'C_NF/C_ox':>10} {'C_HF/C_ox':>10}")
for U in (-2.5, -2.0, -1.5, -1.25, UFB, -0.75, -0.5, -0.25, 0.0, 0.25, 0.4, 0.45, 0.5, 0.55, 0.6, 0.75, 1.0, 1.5, 2.0, 2.5):
    P(f"{U:7.3f} {C_NF(U)/Cox:10.4f} {C_HF(U)/Cox:10.4f}")
UU = np.linspace(-2.5, 2.5, 501)
cnf = np.array([C_NF(u) for u in UU]) / Cox
i_min = int(np.argmin(cnf))
P(f"Minimum der NF-Kurve: {cnf[i_min]:.4f} C'_ox bei U_GB = {UU[i_min]:.3f} V")

kopf("E. Woher die Kanalelektronen kommen: MOS-Kondensator ohne Source gegen Transistor")
tau = 1e-6       # Lebensdauer wie im ET1-Zahlenwerk
Qinv05 = Cox * 0.5
Jgen = q * ni * xd / (2 * tau)
P(f"Inversionsladung bei U_GS - U_th = 0,5 V: {Qinv05:.4e} C/cm^2 = {Qinv05/q:.3e} Elektronen/cm^2 = "
  f"{Qinv05/q*1e-8:.0f} pro µm^2; im Kanal W L = {Wn*Ln*1e8:.0f} µm^2: {Qinv05/q*Wn*Ln:.4e} Elektronen")
P(f"ohne Source nur thermische Generation in der Verarmungszone: J_gen = q n_i x_d/(2 tau) = {Jgen:.3e} A/cm^2 "
  f"(tau = 1 µs) -> Aufbauzeit ~ Q_inv/J_gen = {Qinv05/Jgen:.1f} s")
P(f"Elektronen im n+-Gebiet (Source, 1e20 cm^-3) gegen Kanalbedarf: Volumen mit gleich vielen Elektronen = "
  f"{Qinv05/q*Wn*Ln/1e20*1e12:.3f} µm^3")

kopf("F. Der Kanal im Transistor: Ladung an Source und Drain, Abschnürgrenze, Kanalwiderstand")
UGS = 1.0
Uov = UGS - Uth_n
P(f"U_GS = {UGS} V, Gate-Übersteuerung U_GS - U_th = {Uov} V; Source-Ende: |Q'_n(0)| = C'_ox (U_GS - U_th) = "
  f"{Cox*Uov*1e7:.4f} fC/µm^2")
for UDS in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 2.0):
    rest = Uov - UDS
    P(f"  U_DS = {UDS:.1f} V: Gate-Drain-Spannung U_GD = {UGS-UDS:+.2f} V, Drain-Ende Q'(L)/Q'(0) = "
      f"{max(rest,0)/Uov:.2f} {'(abgeschnürt)' if rest <= 0 else ''}")
P(f"Abschnürgrenze U_DS,ab = U_GS - U_th: U_GS = 0,75 / 1,0 / 1,5 / 2,5 V -> 0,25 / 0,5 / 1,0 / 2,0 V")
P("Kanalwiderstand für kleine U_DS: R_on = L/(W mu_n |Q'_n|) = 1/(K_n (U_GS - U_th)):")
for U in (0.75, 1.0, 1.5, 2.5, 3.3):
    Rsq = 1 / (mu_n * Cox * (U - Uth_n))
    P(f"  U_GS = {U:.2f} V: |Q'_n| = {Cox*(U-Uth_n)*1e7:.4f} fC/µm^2, Schichtwiderstand R_sq = {Rsq/1e3:.3f} kOhm, "
      f"R_on = R_sq L/W = {Rsq*Ln/Wn:.1f} Ohm = 1/(K_n U_ov) = {1/(Kn*(U-Uth_n)):.1f} Ohm")
P("Kontrolle Leitwert: G = W mu_n |Q'_n|/L -> Einheit: cm * cm^2/(V s) * C/cm^2 / cm = C/(V s) = S")


def kanal_profil(UGS_, UDS_, n=11):
    """Kanalpotential und relative Kanalladung längs des Kanals (Modell des allmählichen Kanals, Daten für Abbildung)."""
    uov = UGS_ - Uth_n
    ud = min(UDS_, uov)
    xs = np.linspace(0, 1, n)
    U = uov - np.sqrt(uov ** 2 - xs * (2 * uov * ud - ud ** 2))
    return xs, U, (uov - U) / uov


for UDS in (0.1, 0.3, 0.5):
    xs, Ux, qrel = kanal_profil(1.0, UDS)
    P(f"  Profil U_DS = {UDS} V: x/L = " + ", ".join(f"{x:.1f}" for x in xs[::2]))
    P("     U(x)/V    = " + ", ".join(f"{u:.3f}" for u in Ux[::2]))
    P("     Q'(x)/Q'(0) = " + ", ".join(f"{v:.3f}" for v in qrel[::2]))

kopf("G. Sperrbereich, Oxidfeld, Durchbruch, Leitungen")
for U in (0.0, 0.25, 0.4):
    ps = psi_von_UGB(U)
    P(f"U_GS = {U:.2f} V (U_SB = 0): psi_s = {ps*1e3:.1f} mV, n_s = {np0*math.exp(ps/UT):.3e} cm^-3 "
      f"(Faktor {NA/(np0*math.exp(ps/UT)):.3e} unter N_A)")
for U in (1.0, 2.5, 3.3):
    ps = psi_von_UGB(U)
    Uox = U - UFB - ps
    P(f"U_GB = {U:.1f} V: Spannung über dem Oxid U_ox = U - U_FB - psi_s = {Uox:.3f} V, E_ox = {Uox/t_ox/1e6:.2f} MV/cm")
P(f"Durchbruch SiO2 bei etwa 10 MV/cm: über 5 nm Oxid {10e6*t_ox:.1f} V")
rho_al = 2.7e-6   # Ohm cm
for d in (0.5e-4, 1e-4):
    P(f"Aluminiumbahn {d*1e4:.1f} µm dick: R_sq = rho/d = {rho_al/d*1e3:.1f} mOhm")
P("Polysilizium (Literatur): ohne Silizid etwa 100-300 Ohm/sq, mit Silizid etwa 1-10 Ohm/sq")
P(f"Gate-Leitung W = 10 µm lang, 1 µm breit = 10 Quadrate: 8 Ohm/sq -> {8*10} Ohm; 200 Ohm/sq -> {200*10} Ohm")

kopf("H. Abgeschnürte Zone, Gateladung, elektrostatische Entladung")
vsat = 1e7       # Sättigungsgeschwindigkeit der Elektronen in cm/s
for UDS in (1.0, 2.0, 3.3):
    dU = UDS - Uov
    dL = math.sqrt(2 * eps_si * dU / (q * NA))
    P(f"U_GS = 1 V, U_DS = {UDS:.1f} V: Restspannung {dU:.2f} V über der Zone, Länge (einseitige Verarmungsnäherung) "
      f"Delta L = {dL*1e7:.1f} nm ({dL/Ln*100:.1f} % von L), mittleres Feld {dU/dL:.3e} V/cm, Laufzeit bei v_sat "
      f"= {dL/vsat*1e12:.2f} ps")
QG1 = -Qs_exakt(psi_von_UGB(1.0))
P(f"Gateladung bei U_GB = 1 V: {QG1*1e7:.3f} fC/µm^2 -> {QG1*Wn*Ln*1e15:.1f} fC am Beispieltransistor "
  f"(= {QG1*Wn*Ln/q:.3e} Elementarladungen)")
C_hbm, U_hbm, R_hbm = 100e-12, 2000.0, 1500.0
Q_hbm = C_hbm * U_hbm
Q_bruch = Wn * Ln * Cox * 5.0
P(f"Prüfmodell menschlicher Körper: 100 pF auf 2 kV -> {Q_hbm*1e9:.0f} nC, Energie {0.5*C_hbm*U_hbm**2*1e3:.2f} mJ, "
  f"Spitzenstrom über 1,5 kOhm {U_hbm/R_hbm:.2f} A")
P(f"Gate des Beispieltransistors bis 5 V (Durchbruch): Q = C_ox 5 V = {Q_bruch*1e12:.3f} pC; Verhältnis "
  f"{Q_hbm/Q_bruch:.2e}")

kopf("J. Weitere Zahlen aus den Artikeln")
ps0 = psi_von_UGB(0.0)
psm2 = psi_von_UGB(-2.0)
P(f"Anreicherung bei -2 V: Löcherdichte an der Oberfläche {pp0*math.exp(-psm2/UT):.3e} cm^-3 = "
  f"{math.exp(-psm2/UT):.1f}-mal N_A")
P(f"U_GB = 0: W_i an der Oberfläche um e(psi_s - phi_F) = {(ps0-pF)*1e3:.1f} meV unter W_F; psi_s(2 phi_F) - psi_s(0) = "
  f"{(2*pF-ps0)*1e3:.1f} mV; n_s(Schwelle)/n_s(0) = {math.exp((2*pF-ps0)/UT):.3e}")
yd0 = math.sqrt(2 * eps_si * ps0 / (q * NA))
P(f"Verarmungsnäherung bei U_GB = 0: y_d = {yd0*1e7:.2f} nm, |Q'_dep| = {q*NA*yd0*1e7:.3f} fC/µm^2, Rümpfe pro µm^2 = "
  f"{NA*yd0*1e-8:.0f}; Verhältnis psi(2phi_F)/psi(0) = {2*pF/ps0:.3f}, Wurzel = {math.sqrt(2*pF/ps0):.3f}")
P(f"Phi_MS bei 4e16 gegen 5,68e17: Differenz {(phi_MS_n(4e16)-PMS)*1e3:.1f} mV (Faktor N_A {NA/4e16:.1f})")
P(f"Grunddotierung 4e16: |Q'_dep,max| = {Qdep_max(4e16):.3e} C/cm^2, /C'_ox = {Qdep_max(4e16)/Cox:.4f} V, 2 phi_F = "
  f"{2*phi_F(4e16):.4f} V")
P(f"Produkt 4 e eps N_A phi_F = {4*q*eps_si*NA*pF:.4e} C^2/cm^4")
P(f"Schalter: R_on(2,5 V) mal 1 pF = {1/(Kn*2.0)*1e-12*1e12:.0f} ps; R_on C_ox = {1/(Kn*0.5)*Wn*Ln*Cox*1e12:.0f} ps")
P(f"Schichtwiderstand Kanal bei 1 V gegen Polysilizium ohne Silizid (200 Ohm/sq): Faktor {1/(mu_n*Cox*0.5)/200:.0f}")
P(f"Empfindlichkeit Oxid: (560,4 - 500)/5 = {(Uth0_n(NA, Cox_=eps_ox/5.5e-7)-0.5)*1e3/5:.1f} mV pro 0,1 nm")

kopf("K. Gegenrechnung mit Fermi-Dirac-Statistik (Gültigkeit der Boltzmann-Werte an der Oberfläche)")
from scipy.integrate import quad  # noqa: E402

Wg_eff = UT * math.log(NC * NV / ni ** 2)     # Bandlücke, die mit n_i = 1e10 und N_L, N_V konsistent ist
dC = UT * math.log(NC / ni)                    # W_L - W_i
dV = UT * math.log(NV / ni)                    # W_i - W_V


def F12(eta):
    """normiertes Fermi-Dirac-Integral der Ordnung 1/2; für eta << 0 gleich exp(eta)."""
    if eta < -30:
        return math.exp(eta)
    f = quad(lambda x: math.sqrt(x) / (1.0 + math.exp(min(x - eta, 700.0))), 0, max(60.0, eta + 60.0), limit=200)[0]
    return 2 / math.sqrt(math.pi) * f


# Bulk-Fermi-Niveau mit Fermi-Dirac aus der Neutralität (W_F - W_V in eV)
def neutral(eFV):
    p = NV * F12(-eFV / UT)
    n = NC * F12(-(Wg_eff - eFV) / UT)
    return p - n - NA


lo_, hi_ = 0.0, 0.5
for _ in range(100):
    mid = 0.5 * (lo_ + hi_)
    if neutral(mid) > 0:
        lo_ = mid
    else:
        hi_ = mid
eFV_fd = 0.5 * (lo_ + hi_)
eFV_b = UT * math.log(NV / NA)
P(f"Bandlücke konsistent mit n_i = 1e10: {Wg_eff:.4f} eV; W_F - W_V im Inneren: Boltzmann {eFV_b*1e3:.2f} meV, "
  f"Fermi-Dirac {eFV_fd*1e3:.2f} meV")
UFB_fd = -(Wg_eff - eFV_fd)                     # n+-Gate mit W_F an W_L


def dichten_fd(phi):
    """Elektronen- und Löcherdichte bei Potential phi (gegen das Innere) mit Fermi-Dirac."""
    n = NC * F12((-(Wg_eff - eFV_fd) + phi) / UT)
    p = NV * F12((-eFV_fd - phi) / UT)
    return n, p


def Qs_fd(psi, npts=1500):
    phis = np.linspace(0.0, psi, npts)
    vals = []
    for ph in phis:
        n, p = dichten_fd(ph)
        vals.append(q * (n - p + NA))
    vals = np.array(vals)
    integral = float(np.sum((vals[1:] + vals[:-1]) / 2 * np.diff(phis)))
    return math.copysign(1.0, psi) * math.sqrt(max(2 * eps_si * integral, 0.0))


def UGB_fd(psi):
    return UFB_fd + psi + Qs_fd(psi) / Cox


def psi_fd(U, lo=-0.4, hi=1.3):
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if UGB_fd(mid) < U:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


for U in (-2.0, 1.0, 1.5):
    psf = psi_fd(U)
    nf, pf = dichten_fd(psf)
    psb = psi_von_UGB(U)
    nb, pb = np0 * math.exp(psb / UT), pp0 * math.exp(-psb / UT)
    P(f"U_GB = {U:+.1f} V: psi_s Boltzmann {psb*1e3:7.1f} mV / Fermi-Dirac {psf*1e3:7.1f} mV; n_s {nb:.3e} / {nf:.3e} "
      f"cm^-3; p_s {pb:.3e} / {pf:.3e} cm^-3; |Q_s| {abs(Qs_exakt(psb))*1e7:.3f} / {abs(Qs_fd(psf))*1e7:.3f} fC/µm^2")
    if U < 0:
        P(f"   Löcherdichte an der Oberfläche / N_A: Boltzmann {pb/NA:.1f}, Fermi-Dirac {pf/NA:.1f}")
    else:
        nfa, _ = dichten_fd(2 * pF)
        P(f"   n_s / N_A: Boltzmann {nb/NA:.1f}, Fermi-Dirac {nf/NA:.1f}; Fermi-Dirac an der Schwelle psi = 2 phi_F: "
          f"{nfa:.3e} cm^-3")
UDS25 = 2.5
dL25 = math.sqrt(2 * eps_si * (UDS25 - Uov) / (q * NA))
P(f"Abgeschnürte Zone bei U_GS = 1 V, U_DS = 2,5 V: Delta L = {dL25*1e7:.1f} nm ({dL25/Ln*100:.1f} % von L)")

kopf("I. PMOS (n-Wanne, p+-Poly-Gate)")
pFn = phi_F(ND)
P(f"Wannendotierung so gewählt, dass U_th0,p = -0,500 V: N_D = {ND:.4e} cm^-3")
P(f"phi_F,n = U_T ln(N_D/n_i) = {pFn*1e3:.2f} mV; Fermi-Niveau im p+-Poly U_T ln(N_V/n_i) = {phi_gate_p*1e3:.2f} mV unter W_i")
P(f"phi_MS,p = +(U_T ln(N_V/n_i) + phi_F,n) = {phi_MS_p(ND)*1e3:.2f} mV; |Q'_dep|/C'_ox = {Qdep_max(ND)/Cox*1e3:.2f} mV; "
  f"x_d,max = {xd_max(ND)*1e7:.2f} nm")
P(f"U_th0,p = phi_MS - 2 phi_F,n - |Q'_dep|/C'_ox = {Uth0_p(ND):.4f} V")
P(f"gamma_p = {math.sqrt(2*q*eps_si*ND)/Cox:.4f} sqrt(V)")


# ====================================================================================================================
# Thema 2: Kennlinien des NMOS-Transistors (Abschnitte L bis P)
# ====================================================================================================================


def id_l1(UGS, UDS, lam=0.0, K=Kn, Uth=Uth_n):
    """Level-1-Modell (Shichman-Hodges) des NMOS mit Source als Bezug, U_DS >= 0."""
    uov = UGS - Uth
    if uov <= 0:
        return 0.0
    if UDS < uov:
        return K * (uov * UDS - UDS ** 2 / 2) * (1 + lam * UDS)
    return K / 2 * uov ** 2 * (1 + lam * UDS)


kopf("L. Triodengleichung, Abschnürung und Quadratgesetz (Beispiel-NMOS, K_n = 2 mA/V^2, U_th = 0,5 V)")
P("Ohmscher Bereich bei U_GS = 1 V (Übersteuerung 0,5 V):")
for UDS in (0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5):
    i = id_l1(1.0, UDS)
    ilin = Kn * 0.5 * UDS
    P(f"  U_DS = {UDS:.2f} V: I_D = {i*1e3:.4f} mA; lineare Näherung U_DS/R_on = {ilin*1e3:.4f} mA; Verhältnis "
      f"{i/ilin:.3f} (= 1 - U_DS/(2 U_ov))")
P("Gleiche Rechnung bei U_GS = 0,75 V (Übersteuerung 0,25 V): Verhältnis bei 20 mV "
  f"{id_l1(0.75, 0.02)/(Kn*0.25*0.02):.3f}, bei 50 mV {id_l1(0.75, 0.05)/(Kn*0.25*0.05):.3f}")
P("Triodenformel über ihr Maximum hinaus fortgesetzt (nur zur Warnung, physikalisch falsch):")
for UDS in (0.5, 0.75, 1.0):
    P(f"  U_DS = {UDS:.2f} V: K_n (U_ov U_DS - U_DS^2/2) = {Kn*(0.5*UDS-UDS**2/2)*1e3:.4f} mA")
P("Sättigungsströme I_D = K_n/2 (U_GS - U_th)^2:")
for UGS in (0.6, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5):
    P(f"  U_GS = {UGS:.2f} V: Übersteuerung {UGS-Uth_n:.2f} V, I_D = {Kn/2*(UGS-Uth_n)**2*1e3:.4f} mA, Abschnürgrenze "
      f"{UGS-Uth_n:.2f} V")
P(f"Doppelte Gatespannung 1 V -> 2 V: Faktor {id_l1(2.0, 3.0)/id_l1(1.0, 3.0):.2f}; doppelte Übersteuerung "
  f"(1 V -> 1,5 V): Faktor {id_l1(1.5, 3.0)/id_l1(1.0, 3.0):.2f}")
P("Grenzkurve I_D = K_n/2 U_DS^2:")
for UDS in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
    P(f"  U_DS = {UDS:.2f} V: {Kn/2*UDS**2*1e3:.4f} mA")
P(f"Kontrolle Abschnürgrenze ist Maximum der Triodenparabel: dI/dU_DS = K_n (U_ov - U_DS) = 0 bei U_DS = U_ov")
P(f"MOS-Diode (Gate an Drain): U = 1 V -> I = {id_l1(1.0, 1.0)*1e3:.4f} mA = k (U - U_th)^2 mit k = K_n/2 = "
  f"{Kn/2*1e3:.1f} mA/V^2 (Arbeitspunkt der Netzwerkanalyse 1,000 V / 0,2500 mA)")

kopf("M. Kanalpotential, Feld und Geschwindigkeit längs des Kanals")
for UGS_, UDS_ in ((1.0, 0.1), (1.0, 0.3), (1.0, 0.45)):
    uov = UGS_ - Uth_n
    I = id_l1(UGS_, UDS_)
    a_ = 2 * uov * UDS_ - UDS_ ** 2
    P(f"U_GS = {UGS_} V, U_DS = {UDS_} V: I_D = {I*1e3:.4f} mA")
    for xr in (0.0, 0.25, 0.5, 0.75, 1.0):
        U = uov - math.sqrt(uov ** 2 - xr * a_)
        dUdx = a_ / (2 * Ln * math.sqrt(uov ** 2 - xr * a_))       # V/cm
        Qlen = Cox * (uov - U) * Wn                                   # C/cm
        v = mu_n * dUdx                                               # cm/s
        P(f"  x/L = {xr:.2f}: U = {U*1e3:7.2f} mV, Ladung {(uov-U)/uov*100:5.1f} %, Feld {dUdx/1e3:6.3f} kV/cm, "
          f"v = {v:.3e} cm/s, Kontrolle I = W mu |Q'| E = {mu_n*Qlen*dUdx*1e3:.4f} mA")
    # Laufzeit: Integral dx/v
    xs = np.linspace(0, 1, 20001)
    vv = mu_n * a_ / (2 * Ln * np.sqrt(uov ** 2 - xs * a_))
    t_ = float(np.sum((1 / vv[1:] + 1 / vv[:-1]) / 2 * np.diff(xs) * Ln))
    P(f"  Laufzeit Source -> Drain = {t_*1e12:.1f} ps")
tau_sat = 4 / 3 * Ln ** 2 / (mu_n * 0.5)
P(f"Laufzeit an der Abschnürgrenze (U_GS = 1 V) 4/3 L^2/(mu U_ov) = {tau_sat*1e12:.0f} ps")
v_src = mu_n * 0.5 / (2 * Ln)
P(f"Geschwindigkeit an der Source an der Abschnürgrenze: mu U_ov/(2L) = {v_src:.3e} cm/s (Sättigungsgeschw. 1e7 cm/s)")

kopf("N. Kanallängenmodulation (lambda = 0,1 1/V) und Early-Spannung")
lam = lam_n
for UDS in (0.5, 1.0, 1.5, 2.0, 2.5):
    P(f"U_GS = 1 V, U_DS = {UDS:.1f} V: ohne KLM {id_l1(1.0, UDS)*1e3:.4f} mA, mit KLM {id_l1(1.0, UDS, lam)*1e3:.4f} mA")
P(f"Steigung im Abschnürbereich lambda K_n/2 U_ov^2 = {lam*Kn/2*0.25*1e6:.1f} µA/V; Early-Spannung -1/lambda = "
  f"{-1/lam:.1f} V; |U_Early| des ET1-Bipolartransistors 70 V")
for UGS in (0.75, 1.0, 1.25, 1.5):
    P(f"  U_GS = {UGS:.2f} V: Steigung {lam*Kn/2*(UGS-Uth_n)**2*1e6:.2f} µA/V, I_D(2,5 V) = {id_l1(UGS, 2.5, lam)*1e3:.4f} mA")
# eindimensionale Abschätzung aus der Verkürzung des Kanals
for UDS in (1.0, 2.0, 2.5):
    dL = math.sqrt(2 * eps_si * (UDS - 0.5) / (q * NA))
    P(f"  1D-Abschätzung U_DS = {UDS:.1f} V: Delta L = {dL*1e7:.1f} nm, Faktor L/(L - Delta L) = {Ln/(Ln-dL):.4f}")
dL1 = math.sqrt(2 * eps_si * 0.5 / (q * NA))
dL2 = math.sqrt(2 * eps_si * 1.5 / (q * NA))
lam_1d = (Ln / (Ln - dL2) - Ln / (Ln - dL1)) / 1.0     # Anstieg je Volt, bezogen auf den Strom des Quadratgesetzes
P(f"  daraus lambda_1D zwischen 1 und 2 V = {lam_1d:.4f} 1/V (Modell 0,1 1/V, Faktor {0.1/lam_1d:.1f})")
P(f"Stetigkeit an der Abschnürgrenze mit KLM: Triode {id_l1(1.0, 0.4999999, lam)*1e3:.5f}, Sättigung "
  f"{id_l1(1.0, 0.5, lam)*1e3:.5f} mA")

kopf("O. Strom unterhalb der Schwelle (Diffusion, aus der vollständigen Rechnung)")


def Qinv_stabil(psi):
    b = psi / UT
    Fb2 = math.exp(-b) + b - 1
    ee = (np0 / pp0) * (math.exp(b) - b - 1)
    sA = math.sqrt(2 * eps_si * kB * T * pp0)
    return sA * ee / (math.sqrt(Fb2 + ee) + math.sqrt(Fb2))      # C/cm^2, Betrag


def id_unter(UGS, UDS=1.0):
    ps = psi_von_UGB(UGS)
    return mu_n * (Wn / Ln) * UT * Qinv_stabil(ps) * (1 - math.exp(-UDS / UT))


werte = {}
for UGS in (0.0, 0.1, 0.2, 0.3, 0.4, 0.45):
    werte[UGS] = id_unter(UGS)
    ps = psi_von_UGB(UGS)
    P(f"U_GS = {UGS:.2f} V: psi_s = {ps*1e3:.1f} mV, |Q_inv| = {Qinv_stabil(ps):.3e} C/cm^2, I_D = {werte[UGS]:.3e} A")
S_ = 0.2 / math.log10(werte[0.4] / werte[0.2])
ps3 = psi_von_UGB(0.3)
Cdep3 = math.sqrt(q * eps_si * NA / (2 * ps3))
n_ = 1 + Cdep3 / Cox
P(f"Unterschwellensteigung zwischen 0,2 und 0,4 V: S = {S_*1e3:.1f} mV/Dekade; n = 1 + C'_dep/C'_ox bei 0,3 V = {n_:.3f}, "
  f"n U_T ln 10 = {n_*UT*math.log(10)*1e3:.1f} mV/Dekade; ideale Grenze U_T ln 10 = {UT*math.log(10)*1e3:.1f} mV")
P(f"Ein-Aus-Verhältnis: I_D(U_GS = 2,5 V, Sättigung) / I_D(U_GS = 0) = {id_l1(2.5, 2.5)/werte[0.0]:.2e}")
P(f"Strom bei U_GS = 0 in einem Chip mit 1e9 solchen Transistoren: {werte[0.0]*1e9*1e3:.3f} mA")

kopf("P. SPICE-Parameter des Beispiel-NMOS (Level 1)")
P(f".model NMOS_BSP NMOS (LEVEL=1 VTO=0.5 KP=200u LAMBDA=0.1 TOX=5n GAMMA={gam_n:.2f} PHI={2*pF:.2f}); "
  f"UO = {mu_n:.0f} cm^2/(V s) wäre gleichwertig zu KP")


kopf("Q. Ergänzungen zu Thema 2: Fläche, Steigung, Arbeitspunkt, negative U_DS, Schwelle, Kurzkanal, lambda")
# Triodengleichung als Fläche unter der Übersteuerung über dem Kanalpotential
uov = 0.5
for UDS in (0.3, 0.5):
    flaeche = uov * UDS - UDS ** 2 / 2
    P(f"Fläche unter U_ov - U von 0 bis U_DS = {UDS} V: {flaeche:.4f} V^2; K_n * Fläche = {Kn*flaeche*1e3:.4f} mA")
streifen = [uov - (k + 0.5) * 0.1 for k in range(3)]
P(f"Drei Streifen à 0,1 V bei U_DS = 0,3 V, Höhen in der Streifenmitte {', '.join(f'{s:.2f}' for s in streifen)} V, "
  f"Summe 0,1 V * ({' + '.join(f'{s:.2f}' for s in streifen)}) = {0.1*sum(streifen):.4f} V^2")
P(f"Mittlere Übersteuerung (Source 0,5 V, Drain-Ende 0,2 V): {(0.5+0.2)/2:.2f} V; I = K_n * 0,35 V * 0,3 V = "
  f"{Kn*0.35*0.3*1e3:.4f} mA; R_on bei 0,35 V Übersteuerung = {1/(Kn*0.35):.1f} Ohm")
# örtlicher Mittelwert der Ladung (zum Vergleich mit dem Mittel über das Potential)
Ud = uov - 0.3
m_ort = 2 * (uov ** 2 + uov * Ud + Ud ** 2) / (3 * (uov + Ud))
P(f"Örtlicher Mittelwert der Ladung bei 1 V/0,3 V: {m_ort/uov*100:.1f} % der Source-Ladung (Mittel über das Potential "
  f"{(uov+Ud)/2/uov*100:.1f} %)")
# Steigung der Ausgangskennlinie im ohmschen Bereich = Leitwert mit der Drain-End-Ladung
for UDS in (0.0, 0.1, 0.3, 0.5):
    P(f"  dI_D/dU_DS bei U_GS = 1 V, U_DS = {UDS:.1f} V: K_n (U_ov - U_DS) = {Kn*(uov-UDS)*1e3:.2f} mS")
# negative U_DS (Rollen von Source und Drain vertauscht), Triodengleichung gilt weiter
for UDS in (-0.1, 0.1, -0.02, 0.02):
    P(f"  Triodengleichung U_GS = 1 V, U_DS = {UDS:+.2f} V: I_D = {Kn*(uov*UDS-UDS**2/2)*1e3:+.4f} mA")
# Schwellenbestimmung
for U0 in (1.0, 1.5):
    I0 = Kn / 2 * (U0 - Uth_n) ** 2
    s = Kn * (U0 - Uth_n)
    P(f"Tangente an die Übertragungskennlinie bei {U0} V: Steigung {s*1e3:.2f} mS, Achsenschnitt bei "
      f"{U0 - I0/s:.3f} V (= (U0 + U_th)/2); sqrt(I_D) = {math.sqrt(I0*1e3):.4f} sqrt(mA)")
P(f"sqrt-Gerade: Steigung sqrt(K_n/2) = {math.sqrt(Kn/2*1e3):.3f} sqrt(mA)/V; aus (1 V; 0,25 mA) und (1,5 V; 1 mA): "
  f"U_th = 1 - 0,5/1 = {1 - 0.5/((1.0-0.5)/0.5):.3f} V")
# Ausgangswiderstand im Abschnürbereich
P(f"Kehrwert der Steigung lambda * K_n/2 * U_ov^2 bei U_GS = 1 V: {1/(lam_n*Kn/2*0.25)/1e3:.1f} kOhm")
# lambda aus Lehrbuchwerten und 1D-Abschätzung bei kürzerem Kanal
for VAs, txt in ((5.0, "Prozesse mit 4-6 nm Oxid (Lehrbuch, NMOS)"), (10.0, "Beispielmodell")):
    P(f"  |U_Early| pro Kanallänge {VAs:.0f} V/µm ({txt}): bei L = 1 µm |U_Early| = {VAs:.0f} V, lambda = {1/VAs:.2f} 1/V")
for Lk in (1e-4, 0.5e-4, 0.25e-4):
    d1 = math.sqrt(2 * eps_si * 0.5 / (q * NA))
    d2 = math.sqrt(2 * eps_si * 1.5 / (q * NA))
    l1 = (Lk / (Lk - d2) - Lk / (Lk - d1))
    P(f"  1D-lambda zwischen 1 und 2 V bei L = {Lk*1e4:.2f} µm: {l1:.4f} 1/V")
# Geschwindigkeitssättigung
vsat = 1e7
Ekrit = vsat / mu_n
P(f"Kritisches Feld v_sat/mu_n = {Ekrit/1e3:.1f} kV/cm")
for Lk in (1e-4, 0.25e-4, 0.1e-4):
    P(f"  L = {Lk*1e4:.2f} µm, U_ov = 0,5 V: mittleres Feld U_ov/L = {0.5/Lk/1e3:.1f} kV/cm, Geschwindigkeit an der "
      f"Source mu U_ov/(2L) = {mu_n*0.5/(2*Lk):.2e} cm/s ({mu_n*0.5/(2*Lk)/vsat*100:.0f} % von v_sat)")
P(f"Grenzstrom bei voller Geschwindigkeitssättigung W C'_ox v_sat U_ov (W = 10 µm, U_ov = 0,5 V): "
  f"{Wn*Cox*vsat*0.5*1e3:.2f} mA, linear in U_ov")
# Arbeitspunkt mit Lastwiderstand
UB, RD = 2.5, 4e3


def ap(UGS, lam):
    lo, hi = 0.0, UB
    for _ in range(200):
        m = (lo + hi) / 2
        if id_l1(UGS, m, lam) - (UB - m) / RD > 0:
            hi = m
        else:
            lo = m
    return m, id_l1(UGS, m, lam)


for UGS in (1.0, 1.5):
    for lam in (0.0, lam_n):
        U, I = ap(UGS, lam)
        ber = "Abschnürbereich" if U >= UGS - Uth_n else "ohmscher Bereich"
        P(f"Arbeitspunkt U_B = 2,5 V, R_D = 4 kOhm, U_GS = {UGS} V, lambda = {lam}: U_DS = {U:.4f} V, I_D = {I*1e3:.4f} mA "
          f"({ber}, Grenze {UGS-Uth_n:.2f} V)")
U_ann = UB - RD * Kn / 2 * 1.0 ** 2
P(f"  Annahme Abschnürbereich bei U_GS = 1,5 V ohne lambda: U_DS = 2,5 V - 4 kOhm * 1 mA = {U_ann:.2f} V -> Widerspruch")
U_ann2 = (UB - RD * Kn / 2 * 1.0) / (1 + RD * Kn / 2 * 1.0 * lam_n)
P(f"  Annahme Abschnürbereich bei U_GS = 1,5 V mit lambda: U_DS = (2,5 - 4) / (1 + 0,4) = {U_ann2:.3f} V -> Widerspruch")
P(f"  Annahme Abschnürbereich bei U_GS = 1 V mit lambda: U_DS = (2,5 - 1) / (1 + 0,1) = {(UB-RD*Kn/2*0.25)/(1+RD*Kn/2*0.25*lam_n):.4f} V")
# Unterschwelle: C'_dep und Verschiebung der Schwelle
Cdep3_ = math.sqrt(q * eps_si * NA / (2 * psi_von_UGB(0.3)))
P(f"C'_dep bei U_GS = 0,3 V: {Cdep3_*1e7:.3f} fF/µm^2 (C'_ox {Cox*1e15/1e8:.3f} fF/µm^2), n = {1+Cdep3_/Cox:.3f}")
P(f"Leckstrom-Faktor bei 0,25 V kleinerer Schwelle und S = 82,8 mV/Dekade: 10^(0,25/0,0828) = {10**(0.25/0.0828):.0f}")
P(f"Exponent-Probe: I(0,4 V)/I(0,3 V) = {werte[0.4]/werte[0.3]:.2f}, 10^(0,1/0,0828) = {10**(0.1/0.0828):.2f}")
# Vergleich mit einem Kupferdraht und Zahl der Elektronen im Kanal
n_cu = 8.5e22                  # freie Elektronen pro cm^3 in Kupfer
v_cu = 1.0 / (n_cu * q * 1e-2)  # 1 A durch 1 mm^2 = 1e-2 cm^2, in cm/s
P(f"Kupferdraht 1 A/mm^2: v = {v_cu:.3e} cm/s = {v_cu*10:.3f} mm/s; Verhältnis Kanal/Kupfer {6.08e5/v_cu:.2e} bis "
  f"{1.52e6/v_cu:.2e}")
N_klein = Cox * 0.5 * Wn * Ln / q
N_03 = m_ort / uov * N_klein
P(f"Elektronen im Kanal bei U_GS = 1 V: {N_klein:.3e} bei kleiner U_DS, {N_03:.3e} bei U_DS = 0,3 V "
  f"(Laufzeit Ladung/Strom = {N_03*q/2.1e-4*1e12:.1f} ps)")
# Unterschwelle: Elektronen bei U_GS = 0, Drain-Ende, Temperatur; Widerstand im Arbeitspunkt (b)
N0 = Qinv_stabil(psi_von_UGB(0.0)) / q
P(f"Elektronen bei U_GS = 0: {N0:.3e} pro cm^2, im ganzen Kanal (W L = 1e-7 cm^2) im Mittel {N0*Wn*Ln:.4f}; "
  f"Strom 0,56 pA = {werte[0.0]/q:.2e} Elektronen pro Sekunde")
P(f"Dichte am Drain-Ende relativ zur Source bei U_DS = 0,1 V: exp(-0,1/U_T) = {math.exp(-0.1/UT):.4f}")
P(f"Temperaturfaktor von S zwischen 300 K und 373,15 K: {373.15/300:.4f}")
Ub_, Ib_ = ap(1.5, lam_n)
P(f"Arbeitspunkt (b) mit lambda: U_DS/I_D = {Ub_/Ib_:.0f} Ohm; R_on bei 1,5 V = {1/(Kn*1.0):.0f} Ohm; "
  f"Arbeitsgerade I(0) = U_B/R_D = {UB/RD*1e3:.3f} mA")


kopf("R. Nachträge aus der Faktenprüfung (Thema 2)")
# Diffusionsanteil im treibenden Feld (Ladungsmodell linear): U_T / (U_ov - U)
for U_, ort in ((0.0, "Source"), (0.3, "Drain-Ende")):
    anteil = UT / (0.5 - U_)
    E_treib = 0.21e-3 / (mu_n * Wn * Cox * (0.5 - U_))
    P(f"1 V/0,3 V, {ort}: Diffusionsanteil U_T/(U_ov - U) = {anteil*100:.1f} %, treibendes Feld {E_treib/1e3:.3f} kV/cm, "
      f"elektrostatisches Feld {E_treib*(1-anteil)/1e3:.3f} kV/cm")
# Geschwindigkeitssättigung am Drain-Ende (5,25 kV/cm) nach zwei verbreiteten Modellen
E_d = 0.21e-3 / (mu_n * Wn * Cox * 0.2)
r = E_d / Ekrit
P(f"E_Drain/E_krit = {r:.3f}: v/(mu E) = {1/math.sqrt(1+r**2):.4f} (Wurzelmodell), {1/(1+r):.4f} (Modell 1/(1+E/E_krit))")
# Verteilung eines zusätzlichen Millivolts am Drain über den Kanal (1 V/0,3 V)
for xr in (0.5, 0.75, 1.0):
    U_ = 0.5 - math.sqrt((1 - xr) * 0.25 + xr * 0.04)
    P(f"  dU(x)/dU_DS bei x/L = {xr}: {xr * 0.2 / (0.5 - U_):.3f}")
# Schwellenbestimmung im ohmschen Bereich: Achsenschnitt bei U_th + U_DS/2
for UDS_ in (0.05, 0.1):
    P(f"Ohmscher Bereich, U_DS = {UDS_} V: Gerade I_D(U_GS) schneidet die Achse bei {Uth_n + UDS_/2:.3f} V")
# Einschaltstrom mit lambda und Ein-Aus-Verhältnis; Abbildung Unterschwelle bei U_DS = 1 V mit lambda
I_ein = id_l1(2.5, 2.5, lam_n)
P(f"Einschaltstrom U_GS = U_DS = 2,5 V mit lambda: {I_ein*1e3:.3f} mA; Ein-Aus-Verhältnis {I_ein/werte[0.0]:.3e}")
P(f"Unterschwellenabbildung, U_DS = 1 V, mit lambda: {id_l1(1.0, 1.0, lam_n)*1e3:.4f} mA bei 1 V, "
  f"{id_l1(1.5, 1.0, lam_n)*1e3:.4f} mA bei 1,5 V")
# negative U_DS mit Substrateffekt (nur zur Kontrolle der Aussage „vernachlässigt“)
dUth = gam_n * (math.sqrt(2 * pF - 0.1) - math.sqrt(2 * pF))
I_neg = Kn * ((1.1 - (Uth_n + dUth)) * 0.1 - 0.1 ** 2 / 2)
P(f"U_DS = -0,1 V mit Substrateffekt: Schwelle der neuen Source {Uth_n + dUth:.4f} V, I_D = {-I_neg*1e3:.4f} mA")


# ====================================================================================================================
# Thema 3: PMOS-Transistor, Substrateffekt und Latch-Up (Abschnitte S bis V)
# ====================================================================================================================

kopf("S. PMOS-Transistor: Vorzeichenform und Betragsform (Beispiel-PMOS W/L = 40/1 µm, K_p = 2 mA/V^2, U_th0,p = -0,5 V)")


def id_p(UGS, UDS, lam=lam_p, K=Kp, Uthp=Uth_p):
    """PMOS, Level 1 in Vorzeichenform: I_D in den Drain hinein gezählt (negativ), U_GS, U_DS, U_thp negativ,
    lambda als positiver Betrag, Faktor (1 - lambda U_DS)."""
    uov = UGS - Uthp                     # negativ, wenn der PMOS leitet
    if uov >= 0:
        return 0.0
    if UDS > uov:                        # ohmscher Bereich (U_DS zwischen U_GS - U_thp und 0)
        return -K * (uov * UDS - UDS ** 2 / 2) * (1 - lam * UDS)
    return -K / 2 * uov ** 2 * (1 - lam * UDS)


P(f"Beweglichkeit der Löcher im Kanal mu_p = K'_p/C'_ox = {mu_p:.1f} cm^2/(V s), der Elektronen {mu_n:.1f}; "
  f"Verhältnis {mu_n/mu_p:.2f}; K_p = K'_p W_p/L_p = {Kp*1e3:.2f} mA/V^2 mit W_p = {Wp*1e4:.0f} µm")
P(f"Gleicher PMOS mit W = 10 µm: K = {Kp_s*10*1e3:.2f} mA/V^2; R_on bei |U_GS| = 2,5 V: {1/(Kp_s*10*2.0):.0f} Ohm "
  f"(mit W = 40 µm: {1/(Kp*2.0):.0f} Ohm)")
for UGS_, UDS_ in ((-1.0, -0.3), (-1.0, -2.0), (-1.5, -2.5), (-0.4, -1.0)):
    I_v = id_p(UGS_, UDS_)
    I_b = id_l1(-UGS_, -UDS_, lam_p, K=Kp, Uth=-Uth_p)
    I_v0 = id_p(UGS_, UDS_, lam=0.0)
    P(f"  U_GS = {UGS_} V, U_DS = {UDS_} V: I_D = {I_v*1e3:+.4f} mA (ohne lambda {I_v0*1e3:+.4f} mA); "
      f"Betragsform I_SD = {I_b*1e3:.4f} mA")
P("Kennlinienfeld (mit lambda) bei U_DS = -2,5 V:")
for UGS_ in (-0.75, -1.0, -1.25, -1.5):
    P(f"  U_GS = {UGS_} V: I_D = {id_p(UGS_, -2.5)*1e3:+.4f} mA, Grenze U_DS = U_GS - U_thp = {UGS_-Uth_p:+.2f} V")
P(f"Falsch gerechnet: NMOS-Formel mit U_GS = -1 V und U_th = +0,5 V: K/2 (U_GS - U_th)^2 = "
  f"{Kp/2*(-1.0-0.5)**2*1e3:.3f} mA statt {Kp/2*0.25*1e3:.3f} mA")
P(f"PMOS-Schalter Source an 2,5 V: Gate 0 V -> U_GS = -2,5 V, R_on = 1/(K_p (2,5 - 0,5) V) = {1/(Kp*2.0):.0f} Ohm; "
  f"Gate 2,5 V -> U_GS = 0 > U_thp: gesperrt")

kopf("T. Substrateffekt (Body-Effekt): Schwellenspannung über U_SB = -U_BS")
gam_p = math.sqrt(2 * q * eps_si * ND) / Cox
P(f"NMOS: gamma_n = {gam_n:.4f} sqrt(V), 2 phi_F = {2*pF:.4f} V; PMOS: gamma_p = sqrt(2 q eps N_D)/C'_ox = {gam_p:.4f} "
  f"sqrt(V), 2 phi_F,n = {2*pFn:.4f} V (N_D = {ND:.3e} cm^-3)")


def uth_n_body(USB):
    return Uth_n + gam_n * (math.sqrt(2 * pF + USB) - math.sqrt(2 * pF))


def uthp_betrag(UBS):
    return -Uth_p + gam_p * (math.sqrt(2 * pFn + UBS) - math.sqrt(2 * pFn))


def Qs_V(psi, V):
    """Flächenladung im Halbleiter (C/cm^2) wie Qs_exakt, aber mit um V verschobenem Quasi-Fermi-Niveau der
    Elektronen (Kanal auf dem Potential V über dem Bulk)."""
    b, bv = psi / UT, V / UT
    F2 = (math.exp(-b) + b - 1) + (np0 / pp0) * math.exp(-bv) * (math.exp(b) - b - 1)
    return -math.sqrt(2 * eps_si * kB * T * pp0) * math.sqrt(max(F2, 0.0))


def uth_exakt(USB):
    psi = 2 * pF + USB                      # Elektronendichte an der Oberfläche = N_A, bezogen auf den Kanal
    UGB = UFB + psi - Qs_V(psi, USB) / Cox
    return UGB - USB


P(f"Kontrolle: exakte Schwelle bei U_SB = 0: {uth_exakt(0.0):.4f} V (Abschnitt C: {UGB_von_psi(2*pF):.4f} V)")
P(f"{'U_SB/V':>7} {'U_th Formel/V':>14} {'U_th exakt/V':>13} {'dU_th/V':>8} {'x_d/nm':>7} {'|Q_dep|/(fC/µm2)':>17} "
  f"{'eta':>6} {'Cdep/Cox':>9} {'|U_thp|(U_BS)/V':>16}")
for USB in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5):
    xdv = math.sqrt(2 * eps_si * (2 * pF + USB) / (q * NA))
    Qdv = math.sqrt(2 * q * eps_si * NA * (2 * pF + USB))
    eta = gam_n / (2 * math.sqrt(2 * pF + USB))
    Cdepv = math.sqrt(q * eps_si * NA / (2 * (2 * pF + USB)))
    P(f"{USB:7.2f} {uth_n_body(USB):14.4f} {uth_exakt(USB):13.4f} {uth_n_body(USB)-Uth_n:8.4f} {xdv*1e7:7.1f} "
      f"{Qdv*1e7:17.3f} {eta:6.3f} {Cdepv/Cox:9.3f} {uthp_betrag(USB):16.4f}")
P(f"Zusätzliche Verarmungsladung bei U_SB = 1 V: {(math.sqrt(2*q*eps_si*NA*(2*pF+1))-Qdep_max(NA))*1e7:.3f} fC/µm^2, "
  f"geteilt durch C'_ox = {(math.sqrt(2*q*eps_si*NA*(2*pF+1))-Qdep_max(NA))/Cox:.4f} V")
for USB in (-0.2, -0.3, -0.4):
    P(f"Bulk über der Source (U_SB = {USB} V, U_BS = {-USB} V): U_th = {uth_n_body(USB):.4f} V, "
      f"exakt {uth_exakt(USB):.4f} V")
# gamma aus zwei Messpunkten
x1 = math.sqrt(2 * pF + 1.0) - math.sqrt(2 * pF)
x2 = math.sqrt(2 * pF + 2.0) - math.sqrt(2 * pF)
P(f"gamma aus zwei Schwellen: (U_th(2 V) - U_th(1 V)) / ({x2:.4f} - {x1:.4f}) = "
  f"{(uth_n_body(2.0)-uth_n_body(1.0))/(x2-x1):.4f} sqrt(V)")
for N in (1e16, 1e17, NA):
    P(f"  gamma bei N_A = {N:.2e} cm^-3 und 5 nm Oxid: {math.sqrt(2*q*eps_si*N)/Cox:.4f} sqrt(V)")

kopf("U. Sourcefolger mit Stromquelle 0,25 mA (lambda = 0), U_B = 2,5 V")
I_f = 0.25e-3
U_ov_f = math.sqrt(2 * I_f / Kn)
P(f"Übersteuerung bei 0,25 mA: sqrt(2 I/K) = {U_ov_f:.4f} V (NMOS und PMOS, K = 2 mA/V^2)")


def folger_n(Uein, body=True):
    lo, hi = -1.0, Uein
    for _ in range(200):
        m = 0.5 * (lo + hi)
        uth = uth_n_body(max(m, 0.0)) if body else Uth_n
        f = Uein - m - (uth + U_ov_f)
        if f > 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


for Uein in (1.0, 1.5, 2.0, 2.5):
    Ua = folger_n(Uein)
    eta = gam_n / (2 * math.sqrt(2 * pF + Ua))
    P(f"  NMOS-Folger, Bulk an Masse: U_ein = {Uein} V -> U_aus = {Ua:.4f} V (ohne Substrateffekt {folger_n(Uein, False):.4f} V); "
      f"U_th = {uth_n_body(Ua):.4f} V, Steigung 1/(1+eta) = {1/(1+eta):.4f}; Sättigung T2: U_DS = {2.5-Ua:.3f} V")
d = (folger_n(2.0) - folger_n(1.5)) / 0.5
P(f"  Differenzenquotient zwischen 1,5 V und 2,0 V: {d:.4f}")


def folger_p(Uein, eigene_wanne=True):
    lo, hi = Uein, 2.5
    for _ in range(200):
        m = 0.5 * (lo + hi)
        uth = -Uth_p if eigene_wanne else uthp_betrag(2.5 - m)
        f = (m - Uein) - (uth + U_ov_f)
        if f < 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


for Uein in (0.0, 0.5, 1.0):
    Ua = folger_p(Uein, False)
    eta_p = gam_p / (2 * math.sqrt(2 * pFn + 2.5 - Ua))
    P(f"  PMOS-Folger: U_ein = {Uein} V -> eigene Wanne U_aus = {folger_p(Uein):.4f} V; gemeinsame Wanne an 2,5 V: "
      f"U_aus = {Ua:.4f} V, |U_thp| = {uthp_betrag(2.5-Ua):.4f} V, Steigung 1/(1+eta) = {1/(1+eta_p):.4f}")

kopf("V. Latch-Up: einfaches Modell des parasitären Thyristors (angenommene Werte)")
Rsub, Rwell, Ube, bn, bp, Usat = 1e3, 2e3, 0.6, 5.0, 50.0, 0.2
P(f"Annahmen: R_sub = {Rsub:.0f} Ohm, R_well = {Rwell:.0f} Ohm, Einsatz der Basis-Emitter-Übergänge {Ube} V, "
  f"beta_npn (lateral) = {bn}, beta_pnp (vertikal) = {bp}, U_CE,sat = {Usat} V, U_B = 2,5 V")
P(f"Strom, ab dem ein Übergang leitet: durch das Substrat {Ube/Rsub*1e3:.2f} mA, durch die Wanne {Ube/Rwell*1e3:.2f} mA "
  f"(Zünden erst bei beiden, siehe Nachtrag); Schleifenverstärkung "
  f"beta_npn beta_pnp = {bn*bp:.0f}")
ICn = (Ube / Rwell + Ube / (bp * Rsub)) / (1 - 1 / (bn * bp))
ICp = Ube / Rsub + ICn / bn
IEp = ICp * (1 + 1 / bp)
Iges = IEp + Ube / Rwell
P(f"Haltepunkt (beide Übergänge auf {Ube} V): I_C,npn = {ICn*1e3:.3f} mA, I_C,pnp = {ICp*1e3:.3f} mA, "
  f"Strom aus U_B = {Iges*1e3:.3f} mA")
P(f"Spannung über dem gezündeten Thyristor ~ U_EB,pnp + U_CE,sat,npn = {Ube+Usat:.1f} V")
for Rq in (1.0, 10.0):
    I_l = (2.5 - (Ube + Usat)) / Rq
    P(f"  Versorgung 2,5 V mit {Rq:.0f} Ohm Innen- und Leitungswiderstand: I = {I_l:.2f} A, Leistung im Thyristor "
      f"{I_l*(Ube+Usat):.2f} W")
P(f"Gegenmaßnahmen: beta_npn = 0,01 -> Schleifenverstärkung {0.01*bp:.2f} < 1; R_sub für 100 mA Zündstrom: "
  f"{Ube/0.1:.0f} Ohm")
# Einschalten: Ladestrom der Wannen-Substrat-Kapazität (angenommene Werte)
Nsub, Nwell, A_w, t_r = 1e15, 1e17, 10e-2, 1e-6          # cm^-3, cm^-3, cm^2 (10 mm^2), s
Ubi_w = UT * math.log(Nsub * Nwell / ni ** 2)
Q0 = math.sqrt(2 * q * eps_si * Nsub * Ubi_w)
Q1 = math.sqrt(2 * q * eps_si * Nsub * (Ubi_w + 2.5))
C0 = math.sqrt(q * eps_si * Nsub / (2 * Ubi_w))
P(f"Wanne/Substrat (N_sub = {Nsub:.0e}, N_Wanne = {Nwell:.0e}): U_bi = {Ubi_w:.3f} V, C' bei 0 V = {C0*1e7:.3f} fF/µm^2")
P(f"  Ladung beim Einschalten auf 2,5 V für {A_w*100:.0f} mm^2 Wannenfläche: {(Q1-Q0)*A_w*1e9:.2f} nC; "
  f"mittlerer Strom bei {t_r*1e6:.0f} µs Anstieg: {(Q1-Q0)*A_w/t_r*1e3:.2f} mA, bei 10 ns: {(Q1-Q0)*A_w/1e-8:.2f} A")
# Nachträge Thema 3 beim Schreiben
P(f"Übersteuerung bei U_GS = 1 V und U_BS = -1 V: {1-uth_n_body(1.0):.4f} V, Sättigungsstrom {Kn/2*(1-uth_n_body(1.0))**2*1e3:.4f} mA "
  f"(ohne Substrateffekt 0,25 mA)")
P(f"C'_dep an der Schwelle bei U_BS = 0: {math.sqrt(q*eps_si*NA/(2*2*pF))*1e7:.3f} fF/µm^2")
P(f"Leckstrom 1 nA an R_sub = 1 kOhm: {1e-9*1e3*1e6:.1f} µV")
P(f"Zweites Volt Sperrspannung: U_th(2 V) - U_th(1 V) = {uth_n_body(2.0)-uth_n_body(1.0):.4f} V")
# NMOS als Verbindung zur Versorgung (Gate an 2,5 V, Drain an 2,5 V): Ausgang steigt, bis U_GS = U_th(U_aus)
lo, hi = 0.0, 2.5
for _ in range(200):
    m = 0.5 * (lo + hi)
    if 2.5 - m - uth_n_body(m) > 0:
        lo = m
    else:
        hi = m
P(f"NMOS zieht den Ausgang bei Gate und Drain an 2,5 V höchstens auf {m:.3f} V (Schwelle dort {uth_n_body(m):.3f} V); "
  f"ohne Substrateffekt auf {2.5-Uth_n:.3f} V; PMOS erreicht 2,5 V")
# Nachtrag Faktenprüfung Thema 3: Zündstrom (beide Übergänge leitend) statt Strom für einen Übergang
I_z_sub = Ube / Rsub + (Ube / Rwell) / bn
I_z_well = Ube / Rwell + (Ube / Rsub) / bp
P(f"Zünden im Modell: Einspeisung ins Substrat ab {I_z_sub*1e3:.3f} mA (0,6 mA bis der npn leitet, dazu "
  f"{(Ube/Rwell)/bn*1e3:.3f} mA Basisstrom für 0,3 mA Kollektorstrom); Entnahme aus der Wanne ab {I_z_well*1e3:.3f} mA")
P(f"Sättigungsstrom bei U_BS = -1 V relativ zu 0,25 mA: {Kn/2*(1-uth_n_body(1.0))**2/0.25e-3*100:.1f} %")
P(f"Folger-Probe: sqrt(2 phi_F + 0,783 V) = {math.sqrt(2*pF+0.7828):.4f}")
