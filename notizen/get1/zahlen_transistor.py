"""Zahlenwerk für das Oberthema „Bipolartransistoren“ (ET1 Kap. 11), Stil 3.

Ein Beispieltransistor für alle Artikel des Oberthemas, in der Größenordnung des BC547C aus dem Praktikum MiNa.
Datenblatt (onsemi BC546/D, Fairchild BC547): h_FE 420 bis 800 bei I_C = 2 mA und U_CE = 5 V (Gruppe C),
U_BE(on) 0,55 bzw. 0,58 bis 0,70 V bei 2 mA, U_CE(sat) typ. 0,09 V und höchstens 0,25 V bei 10 mA und 0,5 mA,
f_T typ. 300 MHz, I_C höchstens 100 mA, U_CEO 45 V. Komplementärtyp BC557C (pnp) mit derselben h_FE-Gruppe.

Physikalisches Modell (npn, eindimensional, gleichmäßig dotierte Gebiete, Silizium bei 300 K, n_i = 1e10 cm^-3 wie
in zahlen_halbleiter.py; Bandlückenverengung im hoch dotierten Emitter vernachlässigt):
  Emitter   n+  N_E = 1e19 cm^-3, neutrale Dicke W_E = 0,5 um bis zum Kontakt (kurzer Emitter)
  Basis     p   N_B = 1e17 cm^-3, neutrale Weite W_B = 0,5 um (bei U_CE = 5 V), Elektronen-Lebensdauer 80 ns
  Kollektor n   N_C = 1e16 cm^-3 (wie die Beispieldiode), neutrale Dicke W_C = 5 um bis zum n+-Substrat
  Emitterfläche A = 1,5e-4 cm^2 (0,015 mm^2)
  Minoritätsbeweglichkeiten (gerundete Literaturwerte): Elektronen in der Basis 800, Löcher im Emitter 100,
  Löcher im Kollektor 450 cm^2/(V s) (wie in der Beispieldiode).

Elektrisches Modell (Ebers-Moll in Transportform, wie in Schaltungssimulatoren): I_S = 1e-14 A und B = 500, beide
gerundet aus dem physikalischen Modell; Rückwärtsverstärkung B_R = 1,8; Early-Effekt als Faktor (U_A + U_CE)/(U_A + 5 V)
auf den Transferstrom, U_A = 70 V, so dass I_C/I_B bei U_CE = 5 V (Datenblattbedingung) genau B ist.

Aufruf:  python -I zahlen_transistor.py > zahlen_transistor.txt
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from zahlen_halbleiter import UT, Wg0, _bisekt, dUdT, e, eps, ni, weite_N  # noqa: E402

# ------------------------------------------------------------------ physikalisches Modell
NE, NB, NC = 1e19, 1e17, 1e16            # Dotierungen in cm^-3
WE, WB, WC = 0.5e-4, 0.5e-4, 5e-4        # neutrale Dicken in cm
A_E = 1.5e-4                             # Emitterfläche in cm^2
tau_n = 80e-9                            # Lebensdauer der Elektronen in der Basis in s
mu_nB, mu_pE, mu_pC = 800.0, 100.0, 450.0
DnB, DpE, DpC = mu_nB * UT, mu_pE * UT, mu_pC * UT
LnB = math.sqrt(DnB * tau_n)             # Diffusionslänge der Elektronen in der Basis
nB0, pE0, pC0 = ni**2 / NB, ni**2 / NE, ni**2 / NC
tau_t = WB**2 / (2 * DnB)                # Transitzeit durch die Basis
UDiff_BE = UT * math.log(NE * NB / ni**2)
UDiff_BC = UT * math.log(NB * NC / ni**2)

# Ströme je Faktor (exp(U_BE/U_T) - 1), exakte Lösung der Diffusionsgleichung in der Basis mit n(W_B) = 0
_s = WB / LnB
K_nC = e * A_E * DnB * nB0 / (LnB * math.sinh(_s))            # Elektronenstrom am Kollektorrand = I_S
K_nE = e * A_E * DnB * nB0 / LnB * math.cosh(_s) / math.sinh(_s)  # Elektronenstrom am Emitterrand
K_pE = e * A_E * DpE * pE0 / WE                                 # Löcher in den Emitter (kurzer Emitter)
IS_phys = K_nC
IS_duenn = e * A_E * DnB * ni**2 / (NB * WB)                    # Näherung dünne Basis
alpha_T = K_nC / K_nE                                           # Transportfaktor = 1/cosh(W_B/L_n)
gamma = K_nE / (K_nE + K_pE)                                    # Emitterwirkungsgrad
alpha_phys = gamma * alpha_T
B_phys = alpha_phys / (1 - alpha_phys)
delta = WB**2 / (2 * LnB**2)                                    # Rekombinationsanteil, = tau_t/tau_n
eta = DpE * NB * WB / (DnB * NE * WE)                           # Rückinjektionsanteil
eta_R = DpC * NB * WB / (DnB * NC * WC)                         # Löcher in den Kollektor im Inversbetrieb
B_R_phys = 1 / (eta_R + delta)

# ------------------------------------------------------------------ elektrisches Modell
IS, B, BR, UA, UCE_REF = 1e-14, 500.0, 1.8, 70.0, 5.0


def early(UCE):
    """Early-Faktor: alle Ausgangskennlinien laufen nach -U_A zusammen; bei U_CE = 5 V gleich 1."""
    return (UA + UCE) / (UA + UCE_REF)


def stroeme(UBE, UCE, Is=IS, Bf=B, Br=BR):
    """Kollektor- und Basisstrom (npn, beide in den Transistor hinein gezählt) nach Ebers-Moll in Transportform."""
    UBC = UBE - UCE
    icc = Is * (math.exp(UBE / UT) - 1.0)
    iec = Is * (math.exp(UBC / UT) - 1.0)
    IC = (icc - iec) * early(UCE) - iec / Br
    IB = icc / Bf + iec / Br
    return IC, IB


def ube_bei_ib(IB, UCE, **kw):
    return _bisekt(lambda u: stroeme(u, UCE, **kw)[1] - IB, -0.5, 1.2)


def ic_bei_ib(IB, UCE, **kw):
    return stroeme(ube_bei_ib(IB, UCE, **kw), UCE, **kw)[0]


def arbeitspunkt(IB, UCC, RC, U_last=0.0):
    """Arbeitspunkt mit Kollektorwiderstand RC an UCC (optional mit fester Lastspannung, etwa einer Leuchtdiode):
    gesucht U_CE mit I_C(U_CE) = (UCC - U_last - U_CE)/RC. Rückgabe: U_CE, I_C, U_BE."""
    f = lambda u: ic_bei_ib(IB, u) - (UCC - U_last - u) / RC
    uce = _bisekt(f, 0.0, UCC - U_last)
    return uce, (UCC - U_last - uce) / RC, ube_bei_ib(IB, uce)


def _b_gp(IC, BF, ISE, IKF):
    def ic_von_u(u):
        icc = IS * math.exp(u / UT)
        return 2 * icc / (1 + math.sqrt(1 + 4 * icc / IKF))
    u = _bisekt(lambda x: ic_von_u(x) - IC, 0.0, 1.2)
    ib = IS / BF * math.exp(u / UT) + ISE * math.exp(u / (2 * UT))
    return IC / ib


def b_von_ic(IC, ISE=6.4e-13, IKF=0.11):
    """Stromverstärkung über dem Strom mit Rekombination in der Basis-Emitter-Zone (ISE, Emissionskoeffizient 2)
    und starker Injektion (Knickstrom IKF), wie im Gummel-Poon-Modell; U_CE = 5 V. ISE und IKF sind an den Verlauf
    des BC547C angepasst (onsemi: Gruppe C typisch 270 bei 10 uA, 520 bei 2 mA, 300 bei 100 mA), der ideale Wert BF
    so gewählt, dass B bei 2 mA genau 500 ist. Das physikalische Modell allein erreicht starke Injektion erst um 1 A."""
    BF = _bisekt(lambda bf: _b_gp(2e-3, bf, ISE, IKF) - B, 100.0, 2000.0, n=80)
    return _b_gp(IC, BF, ISE, IKF)


def profil(UBE, n_pts=6):
    """Elektronendichte in der Basis (exakt, n(W_B) = 0) an n_pts Stellen von 0 bis W_B."""
    n0 = nB0 * math.exp(UBE / UT)
    return [(WB * k / (n_pts - 1), n0 * math.sinh((WB - WB * k / (n_pts - 1)) / LnB) / math.sinh(_s))
            for k in range(n_pts)]


def e12(R):
    """Nächster Normwert der Reihe E12."""
    reihe = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10.0]
    dek = 10 ** math.floor(math.log10(R))
    return min((w * dek for w in reihe), key=lambda w: abs(math.log(w / R)))


# ------------------------------------------------------------------ Bericht
def bericht():
    sys.stdout.reconfigure(encoding="utf-8")
    P = print
    P("== Beispieltransistor: physikalisches Modell ==")
    P(f"N_E = {NE:.0e}, N_B = {NB:.0e}, N_C = {NC:.0e} cm^-3; W_E = {WE*1e4:.1f} um, W_B = {WB*1e4:.1f} um, "
      f"W_C = {WC*1e4:.0f} um; A = {A_E:.1e} cm^2 = {A_E*100:.3f} mm^2")
    P(f"D_n(Basis) = {DnB:.2f} cm^2/s, D_p(Emitter) = {DpE:.3f}, D_p(Kollektor) = {DpC:.2f}; tau_n = {tau_n*1e9:.0f} ns; "
      f"L_n = {LnB*1e4:.2f} um; W_B/L_n = {WB/LnB:.4f}")
    P(f"Minoritätsdichten im Gleichgewicht: Elektronen in der Basis {nB0:.0e}, Löcher im Emitter {pE0:.0e}, "
      f"im Kollektor {pC0:.0e} cm^-3")
    P(f"U_Diff(BE) = {UDiff_BE:.3f} V, U_Diff(BC) = {UDiff_BC:.3f} V (Emitter mit 1e19: Boltzmann-Näherung nur grob)")
    P(f"Transitzeit W_B^2/(2 D_n) = {tau_t*1e12:.1f} ps; Grenzfrequenz 1/(2 pi tau_t) = {1/(2*math.pi*tau_t)/1e9:.2f} GHz "
      f"(Datenblatt BC547: f_T typ. 300 MHz, also 1/(2 pi f_T) = {1/(2*math.pi*300e6)*1e9:.2f} ns Gesamtverzögerung: "
      f"Transitzeit des realen Transistors plus Umladen der Sperrschichtkapazitäten)")
    P(f"Knickstrom der starken Injektion im physikalischen Modell e A D_n N_B / W_B = {e*A_E*DnB*NB/WB:.2f} A")
    P(f"I_S exakt (sinh) = {IS_phys:.4e} A, Näherung dünne Basis e A D_n n_i^2/(N_B W_B) = {IS_duenn:.4e} A")
    P(f"Transportfaktor alpha_T = 1/cosh(W_B/L_n) = {alpha_T:.6f} (1 - W_B^2/(2 L_n^2) = {1-delta:.6f}); "
      f"Rekombinationsanteil delta = tau_t/tau_n = {delta:.3e}")
    P(f"Rückinjektion eta = (D_p N_B W_B)/(D_n N_E W_E) = {eta:.3e} (= mu_p/mu_n {mu_pE/mu_nB:.3f} x N_B/N_E "
      f"{NB/NE:.0e} x W_B/W_E {WB/WE:.1f}); Emitterwirkungsgrad gamma = {gamma:.6f}")
    P(f"alpha = gamma alpha_T = {alpha_phys:.6f}; B = alpha/(1-alpha) = {B_phys:.1f}; Näherung 1/(eta+delta) = "
      f"{1/(eta+delta):.1f}")
    P(f"   Auf 10 000 Elektronen am Kollektor: Rückinjektion {eta*1e4:.1f} Löcher, Rekombination {delta*1e4:.2f}, "
      f"zusammen {(eta+delta)*1e4:.1f} -> B = {1/(eta+delta):.0f}")
    for W in (0.25e-4, 0.5e-4, 1.0e-4):
        d = W**2 / (2 * LnB**2)
        h = DpE * NB * W / (DnB * NE * WE)
        P(f"   Basisweite {W*1e4:.2f} um: delta {d:.2e}, eta {h:.2e}, B ~ {1/(d+h):.0f}, I_S ~ "
          f"{e*A_E*DnB*ni**2/(NB*W):.2e} A")
    for NEx in (1e18, 1e19, 1e20):
        h = DpE * NB * WB / (DnB * NEx * WE)
        P(f"   Emitterdotierung {NEx:.0e} (gleiche D_p): eta {h:.2e}, B ~ {1/(delta+h):.0f}")
    for Wmm in (0.01, 1.0):
        W = Wmm * 0.1
        P(f"   'Basis' {Wmm*1e3:.0f} um lang (zwei getrennte Dioden): Transportfaktor 1/cosh = "
          f"{1/math.cosh(W/LnB):.3e}")
    P(f"Inversbetrieb: Löcher in den Kollektor eta_R = (D_pC N_B W_B)/(D_n N_C W_C) = {eta_R:.3f} -> "
      f"B_R ~ {B_R_phys:.2f} (Modell: 1,8)")
    for IC in (1e-3, 2e-3, 10e-3, 100e-3):
        n0 = IC * WB / (e * A_E * DnB)
        P(f"   I_C = {IC*1e3:6.1f} mA: Randdichte n(0) = {n0:.2e} cm^-3 = {n0/NB*100:.2f} % von N_B; "
          f"Basisladung tau_t I_C = {tau_t*IC*1e12:.3g} pC; Stromdichte {IC/A_E:.1f} A/cm^2")
    U = 0.65
    P(f"   bei U_BE = {U} V: n(0) = n_B0 exp(U/U_T) = {nB0*math.exp(U/UT):.3e} cm^-3; Profil (x in um, n): " +
      ", ".join(f"{x*1e4:.1f}: {n:.3e}" for x, n in profil(U)))
    wBC = weite_N(NB, NC, UDiff_BC + 5.0)
    xB = wBC * NC / (NB + NC)
    Cj = eps / wBC
    UA_est = e * NB * WB / Cj
    P(f"BC-Zone bei U_CB = 5 V: Weite {wBC*1e4:.3f} um, davon in der Basis {xB*1e4:.3f} um, im Kollektor "
      f"{(wBC-xB)*1e4:.3f} um; C' = {Cj*1e9:.2f} nF/cm^2; Early-Spannung e N_B W_B/C' = {UA_est:.0f} V")
    for Ucb in (1.0, 10.0):
        w2 = weite_N(NB, NC, UDiff_BC + Ucb)
        P(f"   U_CB = {Ucb:4.0f} V: Eindringtiefe in die Basis {w2*NC/(NB+NC)*1e4:.4f} um")

    P("\n== Elektrisches Modell: I_S = 1e-14 A, B = 500, B_R = 1,8, U_A = 70 V ==")
    for U in (0.55, 0.60, 0.65, 0.70):
        ic, ib = stroeme(U, 5.0)
        P(f"   U_BE = {U:.2f} V, U_CE = 5 V: I_C = {ic*1e3:.4g} mA, I_B = {ib*1e6:.4g} uA")
    for IC in (1e-6, 1e-5, 1e-4, 1e-3, 2e-3, 1e-2):
        P(f"   I_C = {IC*1e3:g} mA braucht U_BE = {UT*math.log(IC/IS)*1e3:.1f} mV")
    P(f"   Verdopplung {UT*math.log(2)*1e3:.1f} mV, Dekade {UT*math.log(10)*1e3:.1f} mV, 1 mV mehr: "
      f"+{(math.exp(1e-3/UT)-1)*100:.2f} %")
    U2 = UT * math.log(2e-3 / IS)
    k = dUdT(U2)
    P(f"   Temperatur bei 2 mA: dU_BE/dT = {k*1e3:.2f} mV/K; bei fester U_BE pro Kelvin x{math.exp(-k/UT):.3f}, "
      f"über 10 K x{math.exp(-10*k/UT):.2f}")
    for IB in (0.1e-6, 1e-6, 2e-6, 4e-6, 10e-6, 20e-6):
        P(f"   Eingangskennlinie U_CE = 5 V: I_B = {IB*1e6:5.1f} uA bei U_BE = {ube_bei_ib(IB, 5.0)*1e3:.1f} mV")
    P("Ausgangskennlinien I_C in mA (Zeilen I_B, Spalten U_CE in V):")
    Us = (0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0, 5.0, 10.0)
    P("   I_B    " + " ".join(f"{u:>7}" for u in Us))
    for IB in (2e-6, 4e-6, 6e-6, 8e-6, 10e-6):
        P(f"   {IB*1e6:3.0f} uA " + " ".join(f"{ic_bei_ib(IB, u)*1e3:7.3f}" for u in Us))
    IB = 8e-6
    for u in (0.1, 0.143, 0.2, 0.25, 0.3, 0.65):
        ube = ube_bei_ib(IB, u)
        icc = IS * math.exp(ube / UT)
        iec = IS * (math.exp((ube - u) / UT) - 1)
        P(f"   I_B = 8 uA, U_CE = {u} V: I_C/(B I_B) = {ic_bei_ib(IB, u)/(B*IB):.3f}; Anteil des Basisstroms im "
          f"BC-Übergang {iec/BR/IB*100:.2f} %; U_BE = {ube*1e3:.1f} mV, U_BC = {(ube-u)*1e3:.1f} mV")
    P(f"   halber Basisstrom in den BC-Übergang bei U_CE = U_T ln(B/B_R) = {UT*math.log(B/BR)*1e3:.0f} mV")
    P("   bei U_CB = 0 (U_CE = U_BE) sammelt der BC-Übergang weiter alles ein (Randdichte n_B0 statt 0), injiziert aber nichts")
    P("Stromverstärkung über dem Strom (Gummel-Poon-Form, an das BC547C-Datenblatt angepasst, ISE = 6,4e-13 A, "
      "IKF = 110 mA):")
    P("   " + ", ".join(f"{ic*1e3:g} mA: {b_von_ic(ic):.0f}" for ic in
                        (1e-6, 1e-5, 1e-4, 1e-3, 2e-3, 1e-2, 18.7e-3, 3e-2, 48e-3, 1e-1)))
    P("   Datenblatt onsemi Gruppe C: typ. 270 (10 uA), 520 (2 mA), 300 (100 mA); skaliert auf 500 bei 2 mA: "
      f"{270*500/520:.0f}, 500, {300*500/520:.0f}")

    P("\n== Zwei Sichten auf denselben Arbeitspunkt ==")
    U = 0.65
    ic, ib = IS * math.exp(U / UT), IS * math.exp(U / UT) / B
    P(f"   U_BE = 0,65 V: I_C = {ic*1e3:.3f} mA, I_B = {ib*1e6:.3f} uA; umgekehrt aus I_B: U_BE = "
      f"{UT*math.log(ib*B/IS)*1e3:.1f} mV")
    P(f"   doppelter Strom: +{UT*math.log(2)*1e3:.1f} mV bzw. doppelter Basisstrom")
    ic2u = 2e-14 * math.exp(U / UT)
    P(f"   zweites Exemplar I_S = 2e-14 A, B = 700: gleiche U_BE -> {ic2u*1e3:.3f} mA (+{(ic2u/ic-1)*100:.0f} %), "
      f"gleicher I_B -> {700*ib*1e3:.3f} mA (+{(700/B-1)*100:.0f} %)")
    P(f"   +10 K bei fester U_BE, linearisiert: x{math.exp(-10*dUdT(U)/UT):.2f}")
    T1, T2 = 300.0, 310.0
    UT2 = UT * T2 / T1
    fak = (T2 / T1) ** 3 * math.exp(Wg0 / (UT / T1) * (1 / T1 - 1 / T2)) * math.exp(U / UT2 - U / UT)
    P(f"   +10 K exakt (I_S ~ T^3 exp(-W_g0/(k_B T)), U_T(T)): x{fak:.3f}; B steigt grob 0,5 bis 1 % je K: x1,05 bis x1,10")

    P("\n== Arbeitsbereiche: U_CC = 10 V, R_C = 2,2 kOhm, Basisstrom vorgegeben ==")
    UCC, RC = 10.0, 2.2e3
    P(f"   Grenze aktiv/Sättigung (einfaches Modell, U_CE,sat = 0,2 V): I_B = {(UCC-0.2)/RC/B*1e6:.2f} uA "
      f"(I_C = {(UCC-0.2)/RC*1e3:.3f} mA)")
    for IB in (0.0, 2e-6, 8e-6, 20e-6):
        ic_a = B * IB
        uce_a = UCC - RC * ic_a
        if IB == 0:
            txt = "Sperrbereich: I_C = 0, U_CE = 10 V"
        elif uce_a >= 0.2:
            txt = f"aktiv: I_C = {ic_a*1e3:.2f} mA, U_CE = {uce_a:.2f} V (>= 0,2 V, Probe hält)"
        else:
            ic_s = (UCC - 0.2) / RC
            txt = (f"aktiv verlangte U_CE = {uce_a:.1f} V, Widerspruch; Sättigung: I_C = {ic_s*1e3:.3f} mA <= "
                   f"B I_B = {B*IB*1e3:.1f} mA, erzwungenes I_C/I_B = {ic_s/IB:.0f}")
        P(f"   I_B = {IB*1e6:4.0f} uA: {txt}")
        if IB > 0:
            uce, icm, ube = arbeitspunkt(IB, UCC, RC)
            P(f"      volles Modell: U_CE = {uce*1e3:.1f} mV, I_C = {icm*1e3:.4f} mA, U_BE = {ube*1e3:.1f} mV, "
              f"U_BC = {(ube-uce)*1e3:.1f} mV")

    P("Elektronendichte in der Basis: aktiv (I_B = 8 uA) gegen Sättigung (I_B = 20 uA), lineares Profil:")
    for IBx in (8e-6, 20e-6):
        uce, icm, ube = arbeitspunkt(IBx, UCC, RC)
        n0 = nB0 * math.exp(ube / UT)
        nW = nB0 * math.exp((ube - uce) / UT)
        Q = e * A_E * (n0 + nW) * WB / 2
        P(f"   I_B = {IBx*1e6:2.0f} uA: n(0) = {n0:.3e}, n(W_B) = {nW:.3e} cm^-3 ({nW/n0*100:.1f} % von n(0)); "
          f"Ladung in der Basis {Q*1e12:.3f} pC; Ladung je mA Kollektorstrom {Q/icm*1e-3*1e12:.3f} pC/mA; "
          f"Gefälle-Strom e A D_n (n(0)-n(W_B))/W_B = {e*A_E*DnB*(n0-nW)/WB*1e3:.3f} mA")
        icc = IS * (math.exp(ube / UT) - 1)
        iec = IS * (math.exp((ube - uce) / UT) - 1)
        P(f"      Aufteilung des Basisstroms: Verluste durch Rückinjektion und Rekombination I_S e^(U_BE/U_T)/B = "
          f"{icc/B*1e6:.2f} uA, über den "
          f"BC-Übergang (vor allem Löcher in den Kollektor) {iec/BR*1e6:.2f} uA; Sättigungsgrenze bei 0,2 V: "
          f"I_C/B = {(UCC-0.2)/RC/B*1e6:.2f} uA")

    P("\n== Schalter: Leuchtdiode an 5 V, angesteuert von einem 3,3-V-Mikrocontroller-Ausgang ==")
    UF, IL, Bmin = 2.0, 20e-3, 420.0
    RCr = (5.0 - UF - 0.2) / IL
    RCn = e12(RCr)
    ICs = (5.0 - UF - 0.2) / RCn
    IBmin = ICs / Bmin
    IBz = 5 * IBmin
    RBr = (3.3 - 0.7) / IBz
    RBn = e12(RBr)
    IBn = (3.3 - 0.7) / RBn
    P(f"   R_C = (5 V - 2,0 V - 0,2 V)/20 mA = {RCr:.0f} Ohm -> E12 {RCn:.0f} Ohm, I_C = {ICs*1e3:.2f} mA")
    P(f"   B_min = 420: I_B,min = {IBmin*1e6:.1f} uA; fünffach: {IBz*1e3:.3f} mA -> R_B = (3,3 V - 0,7 V)/I_B = "
      f"{RBr/1e3:.2f} kOhm -> E12 {RBn/1e3:.0f} kOhm, I_B = {IBn*1e3:.3f} mA (Übersteuerung "
      f"{IBn/IBmin:.1f}, erzwungenes I_C/I_B = {ICs/IBn:.0f})")
    uce, icm, ube = arbeitspunkt(IBn, 5.0, RCn, U_last=UF)
    P(f"   volles Modell: U_CE = {uce*1e3:.1f} mV, I_C = {icm*1e3:.2f} mA, U_BE = {ube*1e3:.0f} mV; Verlust "
      f"{uce*icm*1e3:.2f} mW + {ube*IBn*1e3:.2f} mW = {(uce*icm+ube*IBn)*1e3:.2f} mW (Modellwerte: {0.2*ICs*1e3:.2f} mW + "
      f"{0.7*IBn*1e3:.2f} mW = {(0.2*ICs+0.7*IBn)*1e3:.2f} mW); Pin liefert {IBn*1e3:.3f} mA statt {ICs*1e3:.1f} mA")
    P(f"   B des Modells bei {ICs*1e3:.1f} mA: {b_von_ic(ICs):.0f} (B_min 420 gilt bei 2 mA)")

    P("\n== pnp-Schalter an +5 V (BC557C, B_min = 420), Last 100 Ohm nach Masse, Ansteuerung 0 V = ein ==")
    ICp = (5.0 - 0.2) / 100.0
    IBpmin = ICp / Bmin
    IBpz = 4 * IBpmin
    RBp = e12((5.0 - 0.7) / IBpz)
    IBp = (5.0 - 0.7) / RBp
    P(f"   I_C = (5 V - 0,2 V)/100 Ohm = {ICp*1e3:.0f} mA; I_B,min = {IBpmin*1e3:.3f} mA; vierfach {IBpz*1e3:.3f} mA "
      f"-> R_B = {(5.0-0.7)/IBpz/1e3:.2f} kOhm -> E12 {RBp/1e3:.1f} kOhm, I_B = {IBp*1e3:.3f} mA; "
      f"B_min I_B = {Bmin*IBp*1e3:.0f} mA >= {ICp*1e3:.0f} mA; I_E = {(ICp+IBp)*1e3:.2f} mA")
    IB33 = (5.0 - 0.7 - 3.3) / RBp
    P(f"   aus: Steuerpin 5 V -> U_BE = 0. Ein 3,3-V-Pin ließe 1,7 V über R_B und Emitter-Basis-Strecke; diese leitet "
      f"mit rund 0,7 V, an R_B blieben 1,0 V, I_B = {IB33*1e3:.3f} mA -> B_min I_B = {Bmin*IB33*1e3:.0f} mA, "
      f"B I_B = {B*IB33*1e3:.0f} mA: der Transistor bliebe leitend")
    P(f"   B des Modells bei {ICp*1e3:.0f} mA: {b_von_ic(ICp):.0f}")


# ------------------------------------------------------------------ Thema 02: Arbeitspunkt und Grundschaltungen
UBE_EIN, UCE_SAT = 0.6, 0.2          # Modellwerte des Skripts
BC547 = dict(UCEO=45.0, UCBO=50.0, UEBO=6.0, ICmax=0.1, Ptot=0.625, RthJA=200.0, TJmax=150.0)  # onsemi BC546/D


def _loese(f, x0):
    from scipy.optimize import fsolve
    x, info, ok, msg = fsolve(f, x0, full_output=True, xtol=1e-13)
    if ok != 1:
        raise RuntimeError(msg)
    return x


def ap_einfach_basis(UCC, UE, RB, RC, Bf=B):
    """Einfaches Modell (Skript): Basiswiderstand RB an UE, Kollektorwiderstand RC an UCC."""
    IB = max(0.0, (UE - UBE_EIN) / RB)
    IC, UCE = Bf * IB, UCC - RC * Bf * IB
    if UCE < UCE_SAT:
        UCE, IC = UCE_SAT, (UCC - UCE_SAT) / RC
    return IB, IC, UCE


def ap_voll_basis(UCC, UE, RB, RC, Bf=B):
    def f(x):
        ub, uc = x
        ic, ib = stroeme(ub, uc, Bf=Bf)
        return [(UE - ub) / RB - ib, (UCC - uc) / RC - ic]
    ub, uc = _loese(f, [0.66, UCC / 2])
    ic, ib = stroeme(ub, uc, Bf=Bf)
    return ib, ic, uc, ub


def ap_einfach_stromgk(UCC, R1, R2, RC, RE, Bf=B, ube=UBE_EIN):
    Uq, Ri = UCC * R2 / (R1 + R2), R1 * R2 / (R1 + R2)
    IC = (Uq - ube) / (RE * (1 + 1 / Bf) + Ri / Bf)
    return Uq, Ri, IC, UCC - RC * IC - RE * IC * (1 + 1 / Bf)


def ap_voll_stromgk(UCC, R1, R2, RC, RE, Bf=B):
    def f(x):
        ub, ue, uc = x
        ic, ib = stroeme(ub - ue, uc - ue, Bf=Bf)
        return [(UCC - ub) / R1 - ub / R2 - ib, ue / RE - (ic + ib), (UCC - uc) / RC - ic]
    ub, ue, uc = _loese(f, [1.6, 1.0, UCC / 2])
    ic, ib = stroeme(ub - ue, uc - ue, Bf=Bf)
    return ic, uc - ue, ub - ue


def ap_einfach_spannungsgk(UCC, RB, RC, Bf=B, ube=UBE_EIN):
    IC = (UCC - ube) / (RC * (1 + 1 / Bf) + RB / Bf)
    return IC, ube + IC / Bf * RB


def ap_voll_spannungsgk(UCC, RB, RC, Bf=B):
    def f(x):
        ub, uc = x
        ic, ib = stroeme(ub, uc, Bf=Bf)
        return [(uc - ub) / RB - ib, (UCC - uc) / RC - ic - ib]
    ub, uc = _loese(f, [0.66, UCC / 2])
    ic, ib = stroeme(ub, uc, Bf=Bf)
    return ic, uc, ub


def spiegel_voll(UCC, R, UCE2, Bf=B, Is2=IS):
    """Stromspiegel: T1 als Diode geschaltet (U_CE1 = U_BE), T2 mit fester U_CE2; Referenzstrom über R aus UCC."""
    def f(x):
        ube = x[0]
        ic1, ib1 = stroeme(ube, ube, Bf=Bf)
        ic2, ib2 = stroeme(ube, UCE2, Is=Is2, Bf=Bf)
        return [(UCC - ube) / R - (ic1 + ib1 + ib2)]
    ube = _loese(f, [0.65])[0]
    ic1, _ = stroeme(ube, ube, Bf=Bf)
    ic2, _ = stroeme(ube, UCE2, Is=Is2, Bf=Bf)
    return (UCC - ube) / R, ic1, ic2, ube


def inverter_voll(Uein, UCC, RB, RC, Bf=B):
    """Verschachtelte Bisektion: zu jedem Basispotenzial das Kollektorpotenzial aus der Kollektormasche (monoton),
    dann das Basispotenzial aus der Basismasche (monoton fallend)."""
    def uc_von(ub):                    # _bisekt erwartet eine steigende Funktion
        return _bisekt(lambda uc: stroeme(ub, uc, Bf=Bf)[0] - (UCC - uc) / RC, 0.0, UCC + 0.5)

    def h(ub):
        return (Uein - ub) / RB - stroeme(ub, uc_von(ub), Bf=Bf)[1]
    ub = _bisekt(lambda u: -h(u), min(Uein, 0.0) - 0.1, max(Uein, 0.0) + 0.1)
    return uc_von(ub), ub


def emitterschaltung_voll(Uein, UCC, RC):
    return _bisekt(lambda u: stroeme(Uein, u)[0] - (UCC - u) / RC, 0.0, UCC + 0.5)


def kollektorschaltung_voll(Uein, UCC, RE):
    def g(ue):
        ic, ib = stroeme(Uein - ue, UCC - ue)
        return ue / RE - (ic + ib)
    return _bisekt(g, -0.5, max(Uein, 0.0) + 0.5)


def basisschaltung_voll(Uein, UCC, RC):
    """Basis an Masse, Eingangsspannung direkt am Emitter (negativ), RC an UCC."""
    def g(uc):                         # steigend in uc, wie _bisekt es erwartet
        ic, ib = stroeme(-Uein, uc - Uein)
        return ic - (UCC - uc) / RC
    return _bisekt(g, Uein, UCC + 0.5)


def basisschaltung_re_voll(Uein, UCC, RE, RC, Bf=B):
    """Basis an Masse, Eingangsspannung über den Widerstand RE am Emitter, RC an UCC (verschachtelte Bisektion)."""
    def uc_von(ue):
        return _bisekt(lambda uc: stroeme(-ue, uc - ue, Bf=Bf)[0] - (UCC - uc) / RC, ue, UCC + 0.5)

    def h(ue):                         # Emitterstrom aus dem Transistor minus Strom durch RE; steigend in ue
        ic, ib = stroeme(-ue, uc_von(ue) - ue, Bf=Bf)
        return (ue - Uein) / RE - (ic + ib)
    ue = _bisekt(h, min(Uein, 0.0) - 0.1, 0.1)
    return uc_von(ue), ue


def bericht_arbeitspunkt():
    P = print
    P("\n== Thema 02: Arbeitspunkt und Grundschaltungen (Modellwerte 0,6 V und 0,2 V; vollständiges Modell zum Vergleich) ==")
    UCC, RC = 10.0, 2.2e3
    P(f"Arbeitsgerade 10 V, 2,2 kOhm: Kurzschlussstrom {UCC/RC*1e3:.3f} mA; Mitte U_CE = (U_CC + U_CE,sat)/2 = "
      f"{(UCC+UCE_SAT)/2:.2f} V, I_C = {(UCC-(UCC+UCE_SAT)/2)/RC*1e3:.3f} mA, P = {(UCC+UCE_SAT)/2*(UCC-(UCC+UCE_SAT)/2)/RC*1e3:.2f} mW")
    P(f"   größte Verlustleistung auf der Geraden bei U_CC/2: U_CC^2/(4 R_C) = {UCC**2/(4*RC)*1e3:.2f} mW; "
      f"Erwärmung {UCC**2/(4*RC)*BC547['RthJA']:.1f} K mit R_thJA = 200 K/W")
    P(f"   gesättigt bei 4,455 mA: {UCE_SAT*(UCC-UCE_SAT)/RC*1e3:.2f} mW; gesperrt: 0")
    P(f"BC547 Grenzwerte: U_CEO {BC547['UCEO']:.0f} V, I_C {BC547['ICmax']*1e3:.0f} mA, P_tot {BC547['Ptot']*1e3:.0f} mW "
      f"(25 °C); Hyperbel: 10 V -> {BC547['Ptot']/10*1e3:.1f} mA, 45 V -> {BC547['Ptot']/45*1e3:.1f} mA; "
      f"Erwärmung bei P_tot: {BC547['Ptot']*BC547['RthJA']:.0f} K")
    for U, R in ((30.0, 200.0), (24.0, 1e3)):
        P(f"   Gerade {U:.0f} V/{R:.0f} Ohm: Kurzschlussstrom {U/R*1e3:.0f} mA, größte Leistung {U**2/(4*R)*1e3:.0f} mW bei "
          f"{U/2:.0f} V und {U/(2*R)*1e3:.0f} mA")
    P("Bereiche aus gemessenen Werten (B = 500): I_B = 20 uA, I_C = 4,45 mA -> B I_B = 10 mA > I_C: Sättigung; "
      "I_B = 4 uA, U_CE = 5 V -> aktiv, I_C = 2 mA; U_BE = 0,3 V -> gesperrt")

    P("Basiswiderstand an U_E = U_CC = 10 V, R_C = 2,2 kOhm, Mitte:")
    UCEm = (UCC + UCE_SAT) / 2
    ICm = (UCC - UCEm) / RC
    IBm = ICm / B
    RBr = (UCC - UBE_EIN) / IBm
    RBn = e12(RBr)
    P(f"   I_C = {ICm*1e3:.3f} mA, I_B = {IBm*1e6:.3f} uA, R_B = {RBr/1e6:.3f} MOhm -> E12 {RBn/1e6:.1f} MOhm")
    for Bx in (420, 500, 800):
        ib, ic, uce = ap_einfach_basis(UCC, UCC, RBn, RC, Bf=Bx)
        ibv, icv, ucv, ubv = ap_voll_basis(UCC, UCC, RBn, RC, Bf=Bx)
        P(f"   B = {Bx}: einfach I_B = {ib*1e6:.3f} uA, I_C = {ic*1e3:.3f} mA, U_CE = {uce:.2f} V; voll I_C = {icv*1e3:.3f} mA, "
          f"U_CE = {ucv:.2f} V, U_BE = {ubv*1e3:.0f} mV")

    P("Stromgegenkopplung, einfachster Fall: Basis fest auf 1,6 V, R_E = 1 kOhm:")
    for Bx in (420, 500, 800):
        IE = (1.6 - UBE_EIN) / 1e3
        P(f"   B = {Bx}: I_E = {IE*1e3:.3f} mA, I_C = {IE*Bx/(Bx+1)*1e3:.4f} mA")
    R1, R2, RCs, RE = 330e3, 68e3, 3.9e3, 1e3
    P(f"Stromgegenkopplung mit Basisspannungsteiler: U_CC = 10 V, R1 = 330 kOhm, R2 = 68 kOhm, R_C = 3,9 kOhm, R_E = 1 kOhm")
    for Bx in (420, 500, 800):
        Uq, Ri, ic, uce = ap_einfach_stromgk(UCC, R1, R2, RCs, RE, Bf=Bx)
        icv, ucev, ubev = ap_voll_stromgk(UCC, R1, R2, RCs, RE, Bf=Bx)
        P(f"   B = {Bx}: U_q = {Uq:.4f} V, R_i = {Ri/1e3:.2f} kOhm, einfach I_C = {ic*1e3:.4f} mA, U_CE = {uce:.2f} V; "
          f"voll I_C = {icv*1e3:.4f} mA, U_CE = {ucev:.2f} V, U_BE = {ubev*1e3:.0f} mV")
    Uq, Ri, ic5, _ = ap_einfach_stromgk(UCC, R1, R2, RCs, RE)
    P(f"   Nenner R_E(1+1/B) + R_i/B = {RE*(1+1/B):.1f} + {Ri/B:.1f} Ohm; Querstrom durch R2 ~ {(UBE_EIN+RE*ic5*(1+1/B))/R2*1e6:.1f} uA "
      f"= {(UBE_EIN+RE*ic5*(1+1/B))/R2/(ic5/B):.1f} I_B")
    P(f"   Skript Gl. 11.1 ohne U_BE: U_CC R2/(R_E (R1+R2)) = {UCC*R2/(RE*(R1+R2))*1e3:.3f} mA "
      f"(statt {ic5*1e3:.3f} mA, +{(UCC*R2/(RE*(R1+R2))/ic5-1)*100:.0f} %)")
    dT = abs(dUdT(0.655)) / (RE * (1 + 1 / B) + Ri / B)
    P(f"   Temperatur: dI_C/dT = |dU_BE/dT|/(Nenner) = {dT*1e6:.2f} uA/K = {dT/ic5*100:.2f} %/K (feste U_BE: 8 %/K); "
      f"|dU_BE/dT| bei rund 1 mA (U_BE = 0,655 V) = {abs(dUdT(0.655))*1e3:.2f} mV/K")
    S_B = (RE / B + Ri / B) / (RE * (1 + 1 / B) + Ri / B)
    tk_lo, tk_hi = dT / ic5 * 100 + 0.5 * S_B, dT / ic5 * 100 + 1.0 * S_B
    P(f"   Temperatur gesamt, dazu B mit 0,5 bis 1 %/K mal Empfindlichkeit {S_B:.3f}: {tk_lo:.2f} bis {tk_hi:.2f} %/K; "
      f"gegenüber 8 %/K Faktor {8/tk_hi:.0f} bis {8/tk_lo:.0f}")
    P(f"   U_BE-Unsicherheit 50 mV ändert I_C um {0.05/(RE*(1+1/B)+Ri/B)/ic5*100:.1f} % ")

    P("Spannungsgegenkopplung: U_CC = 10 V, R_C = 2,2 kOhm, R_B vom Kollektor zur Basis:")
    for RB in (1.0e6, 100e3):
        for Bx in (420, 500, 800):
            ic, uce = ap_einfach_spannungsgk(UCC, RB, RC, Bf=Bx)
            icv, ucv, ubv = ap_voll_spannungsgk(UCC, RB, RC, Bf=Bx)
            P(f"   R_B = {RB/1e3:.0f} kOhm, B = {Bx}: einfach I_C = {ic*1e3:.3f} mA, U_CE = {uce:.2f} V; voll I_C = "
              f"{icv*1e3:.3f} mA, U_CE = {ucv:.2f} V")
    RBm = (UCEm - UBE_EIN) / ((UCC - UCEm) / (RC * (1 + 1 / B)) / B)
    P(f"   R_B für die Mitte (B = 500): {RBm/1e6:.3f} MOhm")
    P("   Kompromiss, einfaches Modell (R_B in kOhm: I_C in mA und U_CE in V für B = 420 / 800; Empfindlichkeit "
      "(U_CE - U_BE)/(U_CC - U_BE) bei B = 500):")
    for RB in (50e3, 100e3, 200e3, 500e3, 1e6, 2e6):
        a = ap_einfach_spannungsgk(UCC, RB, RC, Bf=420)
        b = ap_einfach_spannungsgk(UCC, RB, RC, Bf=800)
        m = ap_einfach_spannungsgk(UCC, RB, RC, Bf=500)
        P(f"      {RB/1e3:6.0f}: {a[0]*1e3:.3f}/{b[0]*1e3:.3f} mA, {a[1]:.2f}/{b[1]:.2f} V; "
          f"Empfindlichkeit {(m[1]-UBE_EIN)/(UCC-UBE_EIN):.3f}")
    P("I_C über B (einfaches Modell) für die drei Einstellungen: B: Basiswiderstand 2,2 MOhm / Spannungs-GK 1 MOhm / "
      "Strom-GK Teiler")
    for Bx in (300, 420, 500, 600, 800, 1000):
        P(f"   {Bx:5d}: {ap_einfach_basis(UCC, UCC, 2.2e6, RC, Bf=Bx)[1]*1e3:.3f} / "
          f"{ap_einfach_spannungsgk(UCC, 1e6, RC, Bf=Bx)[0]*1e3:.3f} / "
          f"{ap_einfach_stromgk(UCC, 330e3, 68e3, 3.9e3, 1e3, Bf=Bx)[2]*1e3:.4f} mA")
    Uq, Ri, _, _ = ap_einfach_stromgk(UCC, 330e3, 68e3, 3.9e3, 1e3)
    P(f"   Empfindlichkeit Strom-GK (R_E/B + R_i/B)/Nenner bei B = 500: {(1e3/500 + Ri/500)/(1e3*(1+1/500)+Ri/500):.3f}; "
      f"Basiswiderstand: 1; Temperatur Basiswiderstand über U_BE: {2.04e-3/(UCC-UBE_EIN)*100:.3f} %/K, über B 0,5 bis 1 %/K")
    dev = []
    for Bx in (420, 500, 800):
        _, ic, uce = ap_einfach_basis(UCC, UCC, RBn, RC, Bf=Bx)
        _, icv, ucv, _ = ap_voll_basis(UCC, UCC, RBn, RC, Bf=Bx)
        dev.append(("Basiswiderstand", Bx, icv / ic - 1, ucv - uce))
        _, _, ic, uce = ap_einfach_stromgk(UCC, R1, R2, RCs, RE, Bf=Bx)
        icv, ucv, _ = ap_voll_stromgk(UCC, R1, R2, RCs, RE, Bf=Bx)
        dev.append(("Strom-GK", Bx, icv / ic - 1, ucv - uce))
        for RB in (1e6, 100e3):
            ic, uce = ap_einfach_spannungsgk(UCC, RB, RC, Bf=Bx)
            icv, ucv, _ = ap_voll_spannungsgk(UCC, RB, RC, Bf=Bx)
            dev.append((f"Spannungs-GK {RB/1e3:.0f} kOhm", Bx, icv / ic - 1, ucv - uce))
    mi = max(dev, key=lambda d: abs(d[2]))
    mu = max(dev, key=lambda d: abs(d[3]))
    P(f"   Abweichung vollständiges gegen einfaches Modell (alle Arbeitspunkte oben): größte bei I_C {mi[2]*100:+.1f} % "
      f"({mi[0]}, B = {mi[1]}), größte bei U_CE {mu[3]:+.2f} V ({mu[0]}, B = {mu[1]})")

    P("Stromspiegel: U_CC = 10 V, R = 10 kOhm (einfach: I_ref = (U_CC - 0,6 V)/R):")
    Iref = (UCC - UBE_EIN) / 10e3
    for Bx in (420, 500, 800):
        P(f"   B = {Bx}: I_ref = {Iref*1e3:.3f} mA, I_C2 = I_ref/(1+2/B) = {Iref/(1+2/Bx)*1e3:.4f} mA "
          f"(-{(1-1/(1+2/Bx))*100:.2f} %)")
    for UCE2 in (0.3, 0.65, 1.0, 5.0, 10.0):
        Ir, ic1, ic2, ube = spiegel_voll(UCC, 10e3, UCE2)
        P(f"   voll, U_CE2 = {UCE2:4.2f} V: I_ref = {Ir*1e3:.4f} mA, I_C1 = {ic1*1e3:.4f} mA, I_C2 = {ic2*1e3:.4f} mA "
          f"(I_C2/I_ref = {ic2/Ir:.4f}), U_BE = {ube*1e3:.1f} mV")
    Ir, ic1, ic2, ube = spiegel_voll(UCC, 10e3, 5.0, Is2=1.1e-14)
    P(f"   T2 mit 10 % größerem I_S (U_CE2 = 5 V): I_C2/I_ref = {ic2/Ir:.4f}")
    P(f"   Last bis U_CE2 = 0,3 V: R_L,max = (10 V - 0,3 V)/I_C2 = {(UCC-0.3)/(Iref/(1+2/B))/1e3:.1f} kOhm")
    ube0 = spiegel_voll(UCC, 10e3, 0.65)[3]
    Ir, _, ic2b, _ = spiegel_voll(UCC, 10e3, ube0)
    ic21, ic25 = spiegel_voll(UCC, 10e3, 1.0)[2], spiegel_voll(UCC, 10e3, 5.0)[2]
    P(f"   Early: I_C2 bei U_CE2 = U_BE ({ube0*1e3:.1f} mV) = {ic2b*1e3:.4f} mA; bei 5 V {(ic25/ic2b-1)*100:.1f} % darüber; "
      f"Anstieg {(ic25-ic21)/4/Ir*100:.2f} % des Referenzstroms je Volt")
    P(f"   Streuung von B zwischen 420 und 800 (einfach): Kopie ändert sich um "
      f"{(Iref/(1+2/800)-Iref/(1+2/420))/(Iref/(1+2/B))*100:.3f} %")

    P("Inverter: U_CC = 5 V, R_C = 1 kOhm, R_B = 10 kOhm:")
    for Bx in (420, 500, 800):
        P(f"   B = {Bx}: U_E,sat = (U_CC - U_CE,sat) R_B/(B R_C) + U_BE = {(5-UCE_SAT)*10e3/(Bx*1e3)+UBE_EIN:.3f} V; "
          f"Steigung -B R_C/R_B = {-Bx*1e3/10e3:.0f}")
    pts = (0.0, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 1.0, 2.0, 3.3, 5.0)
    P("   voll (B = 500): " + ", ".join(f"{u:.2f} V -> {inverter_voll(u, 5.0, 10e3, 1e3)[0]:.3f} V" for u in pts))
    for u in (3.3, 5.0):
        ib = (u - 0.7) / 10e3
        P(f"   Eingang {u} V: I_B = {ib*1e3:.3f} mA, nötig für Sättigung mit B_min 420: {4.8e-3/420*1e6:.1f} uA "
          f"-> {ib/(4.8e-3/420):.0f}-fach übersteuert")
    P(f"   Skript Gl. 11.4 nur um R_C ergänzt, ohne Klammer: U_CC - U_CE,sat R_B/(B R_C) + U_BE = "
      f"{5.0 - UCE_SAT*10e3/(B*1e3) + UBE_EIN:.3f} V (richtig {(5.0-UCE_SAT)*10e3/(B*1e3)+UBE_EIN:.3f} V)")

    P("Grundschaltungen (U_CC = 5 V, R_C = R_E = 1 kOhm, vollständiges Modell):")
    P("   Emitterschaltung, Eingang direkt an der Basis: " +
      ", ".join(f"{u:.2f} V -> {emitterschaltung_voll(u, 5.0, 1e3):.3f} V" for u in (0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.75)))
    P("   Kollektorschaltung: " + ", ".join(f"{u:.1f} V -> {kollektorschaltung_voll(u, 5.0, 1e3):.3f} V"
                                         for u in (0.5, 0.7, 1.0, 2.0, 3.0, 4.0, 5.0, 5.5)))
    ue2 = kollektorschaltung_voll(2.0, 5.0, 1e3)
    ic, ib = stroeme(2.0 - ue2, 5.0 - ue2)
    P(f"      bei 2 V: U_BE = {(2.0-ue2)*1e3:.0f} mV, I_E = {(ic+ib)*1e3:.3f} mA, I_B = {ib*1e6:.2f} uA, Stromverstärkung "
      f"I_E/I_B = {(ic+ib)/ib:.0f}; mittlere Steigung (Sekante) zwischen 2 und 3 V: "
      f"{(kollektorschaltung_voll(3.0,5.0,1e3)-kollektorschaltung_voll(2.0,5.0,1e3)):.4f}")
    P("   Basisschaltung, Eingang direkt am Emitter: " +
      ", ".join(f"{u:.2f} V -> {basisschaltung_voll(u, 5.0, 1e3):.3f} V" for u in (0.0, -0.5, -0.55, -0.6, -0.62, -0.64, -0.66, -0.68, -0.7, -1.0)))
    import numpy as np

    def fe(u):
        return emitterschaltung_voll(u, 5.0, 1e3)

    def fb(u):
        return basisschaltung_voll(u, 5.0, 1e3)

    def steig(f, u, h=1e-4):
        return (f(u + h) - f(u - h)) / (2 * h)
    ue_e = _bisekt(lambda u: 2.5 - fe(u), 0.6, 0.75)      # fe fällt, 2,5 V - fe steigt
    ue_b = _bisekt(lambda u: fb(u) - 2.5, -0.75, -0.6)    # fb steigt mit dem Eingang
    P(f"   Steigungen bei U_aus = 2,5 V (I_C = 2,5 mA), Ansteuerung ohne Vorwiderstand: voll Emitterschaltung "
      f"{steig(fe, ue_e):.1f}, Basisschaltung {steig(fb, ue_b):+.1f}; ideal -/+ R_C I_C/U_T = {1e3*2.5e-3/UT:.1f}")
    for name, f, a, b in (("Emitterschaltung", fe, 0.6, 0.75), ("Basisschaltung", fb, -0.75, -0.6)):
        us = np.linspace(a, b, 3001)
        ys = np.array([f(u) for u in us])
        d = np.gradient(ys, us)
        i = int(np.argmax(np.abs(d)))
        P(f"   größte Steigung {name} (ohne Vorwiderstand): {d[i]:+.0f} bei U_aus = {ys[i]:.2f} V, "
          f"I_C = {(5.0-ys[i]):.2f} mA (Rand der Sättigung)")
    P("   Basisschaltung mit R_E = 1 kOhm vor dem Emitter (U_CC = 5 V, R_C = 1 kOhm): " +
      ", ".join(f"{u:.1f} V -> {basisschaltung_re_voll(u, 5.0, 1e3, 1e3)[0]:.3f} V" for u in (0.0, -0.5, -1.0, -2.0, -3.0, -4.0, -5.0, -6.0)))
    P(f"      einfaches Modell: Steigung alpha R_C/R_E = {B/(B+1):.3f}; Sättigung, wenn U_aus auf U_E + 0,2 V = -0,4 V fällt: "
      f"U_ein = {-0.6-(5.0+0.4)/(B/(B+1)):.2f} V")
    P("   Emitterschaltung mit R_B = 10 kOhm = Inverter (oben); Kollektorschaltung einfaches Modell U_aus = U_ein - 0,6 V")


# ------------------------------------------------------------------ Thema 03: Transistor als Verstärker
# Datenblattwerte Gruppe C bei U_CE = 5 V, I_C = 2 mA, f = 1 kHz: Vishay BC546/547/548 (Dok. 85113, Rev. 1.2) und onsemi BC546/D
HIE_C = (6e3, 8.7e3, 15e3)            # Eingangsimpedanz h_ie min/typ/max (Vishay)
HOE_C = (60e-6, 110e-6)               # Ausgangsleitwert h_oe typ/max (Vishay)
HRE_C = 3e-4                          # Spannungsrückwirkung h_re typ (Vishay)
HFE_C = (450, 600, 900)               # Kleinsignal-Stromverstärkung h_fe min/typ/max (onsemi; Vishay typ 600)
R1S, R2S, RCS, RES, UCCS = 330e3, 68e3, 3.9e3, 1e3, 10.0     # Verstärkerstufe = Stromgegenkopplung aus Thema 02
UZ_N, RZ_N, IZ_N = 5.6, 20.0, 5e-3    # Z-Diode wie in zahlen_halbleiter.py: 5,6 V bei 5 mA, r_Z = 20 Ohm
UZ_K = UZ_N - RZ_N * IZ_N             # Knickspannung des Geradenmodells: 5,5 V


def kleinsignal(UBE, UCE, Bf=B, h=1e-6):
    """Kleinsignalparameter des vollständigen Modells durch numerisches Ableiten im Arbeitspunkt:
    g_m = dI_C/dU_BE (U_CE fest), r_BE = dU_BE/dI_B (U_CE fest), r_CE = dU_CE/dI_C (U_BE fest), beta = g_m r_BE."""
    icp, ibp = stroeme(UBE + h, UCE, Bf=Bf)
    icm, ibm = stroeme(UBE - h, UCE, Bf=Bf)
    gm, rbe = (icp - icm) / (2 * h), 2 * h / (ibp - ibm)
    rce = 2 * h / (stroeme(UBE, UCE + h, Bf=Bf)[0] - stroeme(UBE, UCE - h, Bf=Bf)[0])
    return gm, rbe, rce, gm * rbe


def stufe_ap(UCC=UCCS, R1=R1S, R2=R2S, RC=RCS, RE=RES, Bf=B):
    """Arbeitspunkt der Verstärkerstufe (Basisspannungsteiler, R_E, R_C): Knotenpotenziale und Ströme."""
    def f(x):
        ub, ue, uc = x
        ic, ib = stroeme(ub - ue, uc - ue, Bf=Bf)
        return [(UCC - ub) / R1 - ub / R2 - ib, ue / RE - (ic + ib), (UCC - uc) / RC - ic]
    ub, ue, uc = _loese(f, [1.6, 1.0, UCC / 2])
    ic, ib = stroeme(ub - ue, uc - ue, Bf=Bf)
    return ub, ue, uc, ic, ib


def stufe_mit_ce(du, ap, RL=None, UCC=UCCS, RC=RCS, Bf=B):
    """Kollektorpotenzial, wenn die Basis um du gegen den Ruhewert verschoben ist und der Emitter über C_E fest
    bleibt; eine Last RL hängt über einen großen Koppelkondensator am Kollektor (er hält die Ruhespannung)."""
    ub, ue, uc0 = ap[0], ap[1], ap[2]

    def g(uc):                         # steigend in uc
        il = 0.0 if RL is None else (uc - uc0) / RL
        return stroeme(ub + du - ue, uc - ue, Bf=Bf)[0] + il - (UCC - uc) / RC
    return _bisekt(g, ue - 0.5, UCC + 1.0)


def stufe_ohne_ce(du, ap, RL=None, UCC=UCCS, RC=RCS, RE=RES, Bf=B):
    """Wie stufe_mit_ce, aber ohne Emitterkondensator: Emitter- und Kollektorpotenzial stellen sich frei ein."""
    ub, uc0 = ap[0] + du, ap[2]

    def uc_von(ue):
        def g(uc):                     # steigend in uc
            il = 0.0 if RL is None else (uc - uc0) / RL
            return stroeme(ub - ue, uc - ue, Bf=Bf)[0] + il - (UCC - uc) / RC
        return _bisekt(g, ue - 0.5, UCC + 1.0, n=60)

    def h(ue):                         # steigend in ue: mehr Emitterpotenzial, weniger U_BE und Strom
        ic, ib = stroeme(ub - ue, uc_von(ue) - ue, Bf=Bf)
        return ue / RE - (ic + ib)
    return uc_von(_bisekt(h, ub - 1.0, ub, n=60))


def stufe_teil(du, ap, RE1, RL=None, UCC=UCCS, RC=RCS, RE=RES, Bf=B):
    """Teilweise überbrückter Emitterwiderstand: R_E1 bleibt im Signalweg, der Rest R_E - R_E1 liegt parallel zu C_E,
    dessen Fußpunkt deshalb auf seiner Ruhespannung bleibt."""
    ub, uc0 = ap[0] + du, ap[2]
    ux0 = (ap[3] + ap[4]) * (RE - RE1)        # Ruhespannung am überbrückten Teil

    def uc_von(ue):
        def g(uc):
            il = 0.0 if RL is None else (uc - uc0) / RL
            return stroeme(ub - ue, uc - ue, Bf=Bf)[0] + il - (UCC - uc) / RC
        return _bisekt(g, ue - 0.5, UCC + 1.0, n=60)

    def h(ue):
        ic, ib = stroeme(ub - ue, uc_von(ue) - ue, Bf=Bf)
        return (ue - ux0) / RE1 - (ic + ib)
    return uc_von(_bisekt(h, ub - 1.0, ub, n=60))


def harmonische(fun, uhat, N=256):
    """Antwort auf u_ein = uhat sin(wt) über eine Periode: Amplituden der 1. bis 3. Harmonischen, größter Ausschlag
    nach oben und unten gegen den Ruhewert, Verschiebung des Mittelwerts."""
    import numpy as np
    y0 = fun(0.0)
    y = np.array([fun(uhat * math.sin(2 * math.pi * k / N)) for k in range(N)])
    A = np.abs(np.fft.rfft(y)) / N * 2
    return A[1], A[2], A[3], y.max() - y0, y0 - y.min(), y.mean() - y0


def stabilisierung(UE, R1, RL, Bf=B):
    """Längsregler nach Skript Bild 11.28: R1 von U_E zur Basis, Z-Diode (Knick 5,5 V, r_Z = 20 Ohm) von der Basis
    nach Masse, Kollektor an U_E, Ausgang am Emitter mit RL nach Masse."""
    def iz(u):
        return max(0.0, (u - UZ_K) / RZ_N)

    def f(x):
        uk, ua = x
        ic, ib = stroeme(uk - ua, UE - ua, Bf=Bf)
        return [(UE - uk) / R1 - iz(uk) - ib, ua / RL - (ic + ib)]
    uk, ua = _loese(f, [5.55, 4.8])
    ic, ib = stroeme(uk - ua, UE - ua, Bf=Bf)
    return uk, ua, ic, ib, iz(uk)


def nur_z_diode(UE, RV, RL):
    """Z-Diode allein mit Vorwiderstand RV und Last RL (Geradenmodell wie oben)."""
    ua = UE * RL / (RV + RL)
    if ua <= UZ_K:
        return ua, 0.0
    ua = (UE / RV + UZ_K / RZ_N) / (1 / RV + 1 / RL + 1 / RZ_N)
    return ua, (ua - UZ_K) / RZ_N


def stufe_frequenzgang(f, gm, rbe, rce, C1=1e-6, C2=1e-6, CE=470e-6, RL=10e3, RC=RCS, RE=RES):
    """Kleinsignal-Frequenzgang der Verstärkerstufe (ideale Quelle über C_1, Last über C_2, R_E parallel C_E):
    Knotenanalyse mit komplexen Leitwerten, Unbekannte Basis, Emitter, Kollektor, Ausgang; Rückgabe u_aus/u_ein."""
    import numpy as np
    w = 2 * math.pi * f
    R12 = R1S * R2S / (R1S + R2S)
    Y1, Y2, YE = 1j * w * C1, 1j * w * C2, 1 / RE + 1j * w * CE
    A = np.array([
        [Y1 + 1 / R12 + 1 / rbe, -1 / rbe, 0, 0],
        [-1 / rbe - gm, 1 / rbe + gm + 1 / rce + YE, -1 / rce, 0],
        [gm, -gm - 1 / rce, 1 / rce + 1 / RC + Y2, -Y2],
        [0, 0, -Y2, Y2 + 1 / RL]], dtype=complex)
    b = np.array([Y1, 0, 0, 0], dtype=complex)
    return np.linalg.solve(A, b)[3]


def bericht_verstaerker():
    global UA                          # wird für einen Vergleich ohne Early-Effekt kurz umgestellt
    P = print
    P("\n== Thema 03: Transistor als Verstärker (vollständiges Modell, U_T = %.3f mV) ==" % (UT * 1e3))
    # --- Kleinsignalparameter am Datenblattpunkt
    ube2 = UT * math.log(2e-3 / IS + 1)
    gm, rbe, rce, beta = kleinsignal(ube2, 5.0)
    P(f"Datenblattpunkt I_C = 2 mA, U_CE = 5 V: U_BE = {ube2*1e3:.2f} mV, I_B = {2e-3/B*1e6:.2f} uA")
    P(f"   g_m = {gm*1e3:.2f} mS (I_C/U_T = {2e-3/UT*1e3:.2f} mS), r_e = 1/g_m = {1/gm:.2f} Ohm, beta = g_m r_BE = {beta:.1f}")
    P(f"   r_BE = {rbe/1e3:.3f} kOhm (U_T/I_B = {UT/(2e-3/B)/1e3:.3f} kOhm), r_CE = {rce/1e3:.2f} kOhm "
      f"((U_A + U_CE)/I_C = {(UA+5)/2e-3/1e3:.2f} kOhm), 1/r_CE = {1/rce*1e6:.1f} uS")
    P(f"   Datenblatt Gruppe C: h_fe {HFE_C[0]}/{HFE_C[1]}/{HFE_C[2]}; h_ie {HIE_C[0]/1e3:.1f}/{HIE_C[1]/1e3:.1f}/{HIE_C[2]/1e3:.0f} kOhm "
      f"(h_fe typ/g_m = {HFE_C[1]/gm/1e3:.2f} kOhm); h_oe typ {HOE_C[0]*1e6:.0f} uS -> {1/HOE_C[0]/1e3:.1f} kOhm, "
      f"max {HOE_C[1]*1e6:.0f} uS -> {1/HOE_C[1]/1e3:.1f} kOhm; h_re {HRE_C:.0e}")
    U0 = ube2 - UT
    B0 = B * UA / (UA + 5.0)
    P(f"   erweitertes Ersatzschaltbild (Tangente im Arbeitspunkt): U_0 = U_BE - U_T = {U0*1e3:.2f} mV, R_BE = r_BE, "
      f"Quelle B_0 I_B mit B_0 = B U_A/(U_A + 5 V) = {B0:.1f}, R_CE = U_A/(B_0 I_B) = {UA/(B0*2e-3/B)/1e3:.2f} kOhm")
    for ibx in (1e-6, 2e-6, 8e-6, 16e-6):
        u_esb = U0 + rbe * ibx
        u_echt = UT * math.log(ibx * B / IS + 1)
        P(f"      I_B = {ibx*1e6:4.0f} uA: Ersatzschaltbild U_BE = {u_esb*1e3:.1f} mV, Modell {u_echt*1e3:.1f} mV, "
          f"Fehler {(u_esb-u_echt)*1e3:+.1f} mV")
    P(f"   Ausgang als Tangentialebene: I_C = beta I_B + (U_CE - 5 V)/r_CE, also Quelle beta I_B minus U_CE,AP/r_CE = "
      f"{5.0/rce*1e3:.4f} mA, parallel r_CE (die Form B_0 I_B + U_CE/r_CE ergäbe für Änderungen {B0:.1f} statt beta = {beta:.1f})")
    for ibx in (2e-6, 8e-6):
        for ucex in (1.0, 10.0):
            ic_mod = B * ibx * early(ucex)
            ic_esb = beta * ibx + (ucex - 5.0) / rce
            P(f"      I_B = {ibx*1e6:.0f} uA, U_CE = {ucex:4.1f} V: Modell {ic_mod*1e3:.4f} mA, Ersatzschaltbild "
              f"{ic_esb*1e3:.4f} mA ({(ic_esb/ic_mod-1)*100:+.1f} %); bei 5 V stimmt es für jeden Basisstrom")
    # --- Groß- und Kleinsignal: Exponentialkennlinie gegen Tangente
    P("Kleinsignal: i_c/I_C = exp(u/U_T) - 1 gegen Tangente u/U_T:")
    for u in (1e-3, 2e-3, 5e-3, 10e-3, 20e-3, 26e-3):
        x = u / UT
        P(f"   u = {u*1e3:4.0f} mV: Tangente {x*100:6.2f} %, exakt +{(math.exp(x)-1)*100:6.2f} % / -{(1-math.exp(-x))*100:5.2f} %, "
          f"Fehler der Tangente {((math.exp(x)-1)/x-1)*100:5.2f} % (Näherung u/(2U_T) {x/2*100:5.2f} %)")
    # --- Verstärkerstufe aus Thema 02
    ap = stufe_ap()
    ub, ue, uc, ic, ib = ap
    gm, rbe, rce, beta = kleinsignal(ub - ue, uc - ue)
    P(f"Verstärkerstufe (10 V; 330 k/68 k; R_C 3,9 k; R_E 1 k): U_B = {ub:.4f} V, U_E = {ue:.4f} V, U_C = {uc:.4f} V, "
      f"U_CE = {uc-ue:.3f} V, I_C = {ic*1e3:.4f} mA, I_B = {ib*1e6:.3f} uA, U_RC = {RCS*ic:.3f} V")
    P(f"   g_m = {gm*1e3:.2f} mS, r_e = {1/gm:.2f} Ohm, r_BE = {rbe/1e3:.2f} kOhm, beta = {beta:.1f}, r_CE = {rce/1e3:.1f} kOhm")
    Rp = RCS * rce / (RCS + rce)
    Ri = R1S * R2S / (R1S + R2S)
    P(f"   mit C_E: v_u = -g_m (R_C || r_CE) = {-gm*Rp:.1f} (ohne r_CE: -g_m R_C = {-gm*RCS:.1f} = -U_RC/U_T = "
      f"{-RCS*ic/UT:.1f}); numerisch {(stufe_mit_ce(1e-5, ap)-stufe_mit_ce(-1e-5, ap))/2e-5:.1f}")
    for RL in (10e3,):
        Rpl = 1 / (1 / RCS + 1 / rce + 1 / RL)
        P(f"   mit C_E und Last {RL/1e3:.0f} kOhm: v_u = {-gm*Rpl:.1f}; numerisch "
          f"{(stufe_mit_ce(1e-5, ap, RL)-stufe_mit_ce(-1e-5, ap, RL))/2e-5:.1f}")
    v_ohne = -beta * RCS / (rbe + (beta + 1) * RES)
    P(f"   ohne C_E: v_u = -beta R_C/(r_BE + (beta+1) R_E) = {v_ohne:.3f} (r_CE vernachlässigt); Näherung -R_C/(R_E + r_e) = "
      f"{-RCS/(RES+1/gm):.3f}; -R_C/R_E = {-RCS/RES:.2f}; numerisch "
      f"{(stufe_ohne_ce(1e-4, ap)-stufe_ohne_ce(-1e-4, ap))/2e-4:.3f}")
    P(f"   ohne C_E wirkt r_CE vergrößert: r_CE (1 + beta R_E/(r_BE + R_E)) = {rce*(1+beta*RES/(rbe+RES))/1e6:.2f} MOhm, "
      f"deshalb bleibt R_C allein im Zähler; Faktor 1 + g_m R_E = {1+gm*RES:.1f}")
    RE1 = 100.0
    P(f"   Teilüberbrückung (R_E1 = 100 Ohm im Signalweg, 900 Ohm überbrückt): v_u = -beta R_C/(r_BE + (beta+1) R_E1) = "
      f"{-beta*RCS/(rbe+(beta+1)*RE1):.2f}; Näherung -R_C/(R_E1 + r_e) = {-RCS/(RE1+1/gm):.2f}; numerisch "
      f"{(stufe_teil(1e-4, ap, RE1)-stufe_teil(-1e-4, ap, RE1))/2e-4:.2f}; Eingangswiderstand "
      f"{1/(1/Ri+1/(rbe+(beta+1)*RE1))/1e3:.1f} kOhm")
    IR1 = (UCCS - ub) / R1S
    v_last = -gm / (1 / RCS + 1 / rce + 1 / 10e3)
    p_ein = (1e-3) ** 2 / (2 * 1 / (1 / Ri + 1 / rbe))
    p_aus = (abs(v_last) * 1e-3) ** 2 / (2 * 10e3)
    P(f"   Leistung: Versorgung U_CC (I_C + I_R1) = 10 V ({ic*1e3:.4f} + {IR1*1e3:.4f}) mA = {UCCS*(ic+IR1)*1e3:.2f} mW; "
      f"Signal 1 mV: Eingang {p_ein*1e12:.1f} pW, an 10 kOhm Last {p_aus*1e9:.0f} nW, Leistungsverstärkung {p_aus/p_ein:.0f}")
    rin_mit = 1 / (1 / Ri + 1 / rbe)
    rin_ohne = 1 / (1 / Ri + 1 / (rbe + (beta + 1) * RES))
    P(f"   Eingangswiderstand: mit C_E R_1||R_2||r_BE = {rin_mit/1e3:.2f} kOhm (r_BE allein {rbe/1e3:.2f}); ohne C_E "
      f"R_1||R_2||(r_BE + (beta+1) R_E) = {rin_ohne/1e3:.1f} kOhm (Transistor allein {(rbe+(beta+1)*RES)/1e3:.0f} kOhm); "
      f"Teiler R_1||R_2 = {Ri/1e3:.2f} kOhm")
    P(f"   Ausgangswiderstand mit C_E: R_C || r_CE = {Rp/1e3:.3f} kOhm")
    rce_typ = 1 / (HOE_C[0] * ic / 2e-3)      # typischer Datenblattwert, proportional zum Strom umgerechnet
    P(f"   mit typischem h_oe des BC547C (60 uS bei 2 mA, proportional zu I_C): r_CE = {rce_typ/1e3:.1f} kOhm, "
      f"v_u = {-gm/(1/RCS+1/rce_typ):.1f} ({(gm/(1/RCS+1/rce_typ))/(gm*Rp)*100-100:+.1f} %)")
    for Bx in (420, 800):
        apx = stufe_ap(Bf=Bx)
        gmx, rbex, rcex, betax = kleinsignal(apx[0] - apx[1], apx[2] - apx[1], Bf=Bx)
        Rpx = RCS * rcex / (RCS + rcex)
        P(f"   Exemplar B = {Bx}: I_C = {apx[3]*1e3:.4f} mA ({(apx[3]/ic-1)*100:+.1f} %), v_u mit C_E = {-gmx*Rpx:.1f} "
          f"({(gmx*Rpx/(gm*Rp)-1)*100:+.1f} %), r_BE = {rbex/1e3:.2f} kOhm, "
          f"Eingangswiderstand mit C_E {1/(1/Ri+1/rbex)/1e3:.2f} kOhm, ohne C_E v_u = "
          f"{-betax*RCS/(rbex+(betax+1)*RES):.3f}")
    # Koppel- und Emitterkondensatoren: untere Grenzfrequenzen
    for C1 in (1e-6, 10e-6):
        P(f"   C_1 = {C1*1e6:.0f} uF am Eingang ({rin_mit/1e3:.1f} kOhm): f_u = {1/(2*math.pi*C1*rin_mit):.1f} Hz")
    P(f"   C_2 = 1 uF vor 10 kOhm Last (R_C || r_CE + R_L = {(Rp+10e3)/1e3:.2f} kOhm): f_u = {1/(2*math.pi*1e-6*(Rp+10e3)):.1f} Hz; "
      f"Obergrenze der Verstärkung einer Stufe an 10 V: U_CC/U_T = {UCCS/UT:.1f}; mit Stromquelle als Last statt R_C: "
      f"g_m r_CE = {gm*rce:.0f} (= (U_A + U_CE)/U_T = {(UA+uc-ue)/UT:.0f})")
    vmid = abs(stufe_frequenzgang(1e5, gm, rbe, rce))
    P(f"   Frequenzgang mit C_1 = C_2 = 1 uF, C_E = 470 uF, 10 kOhm Last (mittlere Frequenzen |v_u| = {vmid:.1f}):")
    for fx in (10.0, 14.4, 20.0, 30.0, 50.0, 100.0, 1000.0):
        P(f"      {fx:7.1f} Hz: |v_u| = {abs(stufe_frequenzgang(fx, gm, rbe, rce)):.1f} "
          f"({abs(stufe_frequenzgang(fx, gm, rbe, rce))/vmid*100:.0f} %)")
    f3 = _bisekt(lambda fx: abs(stufe_frequenzgang(fx, gm, rbe, rce)) / vmid - 2 ** -0.5, 1.0, 1000.0, n=60)
    f3c1 = _bisekt(lambda fx: abs(stufe_frequenzgang(fx, gm, rbe, rce, C2=1.0, CE=1.0)) / vmid - 2 ** -0.5, 0.1, 1000.0, n=60)
    P(f"      untere Grenzfrequenz der Stufe (71 %): {f3:.1f} Hz; nur C_1 wirksam: {f3c1:.1f} Hz")
    for CE in (100e-6, 470e-6):
        rq = 1 / (1 / RES + gm)       # Widerstand, den C_E sieht (ideale Quelle am Eingang): R_E || r_e
        P(f"   C_E = {CE*1e6:.0f} uF sieht R_E || r_e = {rq:.1f} Ohm: f_u = {1/(2*math.pi*CE*rq):.1f} Hz")
    # Verzerrung: Ausschläge und 2. Harmonische
    P("   Verzerrung mit C_E (Eingangsamplitude -> Ausgangsamplitude 1. Harmonische, k2 = A2/A1, Ausschlag ab/auf):")
    for uh in (1e-3, 2e-3, 5e-3, 7.34e-3, 10e-3):
        a1, a2, a3, auf, ab, dm = harmonische(lambda d: stufe_mit_ce(d, ap), uh)
        P(f"      {uh*1e3:4.0f} mV: A1 = {a1*1e3:7.1f} mV, k2 = {a2/a1*100:5.2f} % (Näherung u/(4U_T) {uh/(4*UT)*100:5.2f} %), "
          f"k3 = {a3/a1*100:5.2f} %, Ausgang nach unten {ab:.3f} V, nach oben {auf:.3f} V, Mittelwert {dm*1e3:+.1f} mV")
    uh1 = _bisekt(lambda u: (lambda h: h[1] / h[0])(harmonische(lambda d: stufe_mit_ce(d, ap), u)) - 0.01,
                  0.5e-3, 3e-3, n=30)
    a1_1 = harmonische(lambda d: stufe_mit_ce(d, ap), uh1)[0]
    P(f"   für k2 = 1 %: Eingangsamplitude {uh1*1e3:.2f} mV, Ausgangsamplitude {a1_1:.3f} V (Näherung 4 k2 U_RC = "
      f"{4*0.01*RCS*ic:.3f} V); Platz am Kollektor bis zur Versorgung {RCS*ic:.2f} V, bis U_CE = 0,2 V {uc-ue-0.2:.2f} V")
    UA_alt = UA
    UA = 1e12                          # Early-Effekt abgeschaltet: Stufe wie reine Exponentialfunktion
    ap_ohne_early = stufe_ap()
    k2_oe = [harmonische(lambda d: stufe_mit_ce(d, ap_ohne_early), uh) for uh in (1e-3, 10e-3)]
    UA = UA_alt
    P(f"   zum Vergleich ohne Early-Effekt: k2 = {k2_oe[0][1]/k2_oe[0][0]*100:.3f} % bei 1 mV, "
      f"{k2_oe[1][1]/k2_oe[1][0]*100:.3f} % bei 10 mV; Faktor (1 + R_C/r_CE)^2 = {(1+RCS/rce)**2:.3f}")
    P("   ohne C_E, gleiche Ausgangsamplitude:")
    for uh in (0.0105, 0.0263, 0.0527, 0.263):
        a1, a2, a3, auf, ab, dm = harmonische(lambda d: stufe_ohne_ce(d, ap), uh)
        P(f"      {uh*1e3:6.1f} mV: A1 = {a1*1e3:7.1f} mV, k2 = {a2/a1*100:6.3f} %, k3 = {a3/a1*100:6.3f} %, "
          f"nach unten {ab:.3f} V, nach oben {auf:.3f} V")
    # --- Grundschaltungen für kleine Signale bei gleichem Ruhestrom
    P(f"Grundschaltungen im Kleinsignal bei I_C = {ic*1e3:.4f} mA (g_m = {gm*1e3:.2f} mS, beta = {beta:.1f}), Widerstand 3,9 kOhm:")
    P(f"   Emitterschaltung: v_u = {-gm*Rp:.1f}, r_ein = r_BE = {rbe/1e3:.2f} kOhm, r_aus = R_C || r_CE = {Rp/1e3:.2f} kOhm, "
      f"Stromverstärkung bei kurzgeschlossenem Ausgang beta = {beta:.0f}, in R_C beta r_CE/(r_CE + R_C) = "
      f"{beta*rce/(rce+RCS):.0f}")
    vcc = RCS / (RCS + 1 / gm)
    Rcc = Rp                           # am Emitter liegen für Signale R_E und r_CE parallel
    P(f"   Kollektorschaltung (R_E = 3,9 kOhm): v_u = R_E/(R_E + r_e) = {vcc:.4f}, mit r_CE parallel {Rcc/(Rcc+1/gm):.4f}; "
      f"r_ein = r_BE + (beta+1) R_E = {(rbe+(beta+1)*RCS)/1e6:.2f} MOhm, mit R_E || r_CE = {Rcc/1e3:.3f} kOhm: "
      f"{(rbe+(beta+1)*Rcc)/1e6:.3f} MOhm; r_aus = r_e + R_q/(beta+1) = {1/gm:.1f} Ohm + R_q/{beta+1:.0f}; "
      f"mit R_q = 10 kOhm: {1/gm+10e3/(beta+1):.1f} Ohm; Stromverstärkung beta + 1 = {beta+1:.0f}")
    alpha = beta / (beta + 1)
    P(f"   Basisschaltung: v_u = +g_m (R_C || r_CE) = {gm*Rp:.1f}, r_ein = 1/(g_m + 1/r_BE) = {1/(gm+1/rbe):.1f} Ohm, "
      f"r_aus mit idealer Quelle R_C || r_CE = {Rp/1e3:.2f} kOhm, Stromverstärkung alpha = {alpha:.4f}")
    # Emitterfolger aus Thema 02 (5 V, R_E 1 kOhm, Eingang 2 V)
    s = (kollektorschaltung_voll(2.0 + 1e-5, 5.0, 1e3) - kollektorschaltung_voll(2.0 - 1e-5, 5.0, 1e3)) / 2e-5
    ua2 = kollektorschaltung_voll(2.0, 5.0, 1e3)
    gm2, rbe2, rce2, beta2 = kleinsignal(2.0 - ua2, 5.0 - ua2)
    P(f"   Emitterfolger aus Thema 02 (5 V, 1 kOhm, Eingang 2 V): Kleinsignal-Steigung {s:.4f}; R_E/(R_E + r_e) = "
      f"{1e3/(1e3+1/gm2):.4f}; r_e = {1/gm2:.2f} Ohm; r_ein = {(rbe2+(beta2+1)*1e3)/1e3:.0f} kOhm")
    # --- Spannungsstabilisierung (Skript 11.6)
    R1z, RLz = 1e3, 200.0
    P(f"Spannungsstabilisierung (Skript Bild 11.28): U_E = 12 V +- 1 V, R_1 = {R1z/1e3:.0f} kOhm, Z-Diode 5,6 V bei 5 mA "
      f"(r_Z = 20 Ohm, Knick {UZ_K:.2f} V), Last {RLz:.0f} Ohm")
    res = {}
    for UEx in (11.0, 12.0, 13.0):
        uk, ua, icx, ibx, izx = stabilisierung(UEx, R1z, RLz)
        res[UEx] = ua
        P(f"   U_E = {UEx:.0f} V: U_Z = {uk:.4f} V, U_A = {ua:.4f} V, U_BE = {(uk-ua)*1e3:.1f} mV, I_L = {ua/RLz*1e3:.2f} mA, "
          f"I_B = {ibx*1e6:.1f} uA, I_Z = {izx*1e3:.2f} mA, P_T = {(UEx-ua)*icx*1e3:.0f} mW")
    dA = res[13.0] - res[11.0]
    P(f"   Brummhub am Ausgang {dA*1e3:.1f} mV für 2 V am Eingang: Glättungsfaktor {2/dA:.1f} (Näherung 1 + R_1/r_Z = "
      f"{1+R1z/RZ_N:.0f})")
    uk12, ua12 = stabilisierung(12.0, R1z, RLz)[:2]
    P(f"   Skriptformel U_Z + U_BE ergäbe {uk12+(uk12-ua12):.3f} V statt U_Z - U_BE = {ua12:.3f} V")
    p13 = (13.0 - res[13.0]) * stabilisierung(13.0, R1z, RLz)[2]
    P(f"   Erwärmung bei {p13*1e3:.0f} mW: onsemi (625 mW, 200 K/W) {p13*BC547['RthJA']:.1f} K; "
      f"Vishay (500 mW, 250 K/W) {p13*250.0:.1f} K")
    for RLx in (1e4, 1e3, 500.0, 200.0, 100.0):
        uk, ua, icx, ibx, izx = stabilisierung(12.0, R1z, RLx)
        P(f"   Last {RLx:7.0f} Ohm: U_A = {ua:.4f} V, I_L = {ua/RLx*1e3:6.2f} mA, U_BE = {(uk-ua)*1e3:.1f} mV, "
          f"I_Z = {izx*1e3:.2f} mA, P_T = {(12.0-ua)*icx*1e3:.0f} mW (bei 13 V {(13.0-stabilisierung(13.0,R1z,RLx)[1])*stabilisierung(13.0,R1z,RLx)[2]*1e3:.0f} mW)")
    # kleinste Eingangsspannung, bei der die Z-Diode noch 1 mA führt
    UEmin = _bisekt(lambda u: stabilisierung(u, R1z, RLz)[4] - 1e-3, 6.0, 12.0)
    P(f"   kleinste Eingangsspannung für I_Z >= 1 mA bei 200 Ohm: {UEmin:.3f} V (U_A dann {stabilisierung(UEmin, R1z, RLz)[1]:.3f} V)")
    gmz, rbez, rcez, betaz = kleinsignal(*(lambda r: (r[0] - r[1], 12.0 - r[1]))(stabilisierung(12.0, R1z, RLz)))
    P(f"   Ausgangswiderstand r_e + (R_1 || r_Z)/(beta+1) = {1/gmz:.3f} + {(R1z*RZ_N/(R1z+RZ_N))/(betaz+1):.3f} Ohm")
    P("   zum Vergleich Z-Diode allein (R_V = 330 Ohm wie im Diodenartikel) an derselben Last 200 Ohm:")
    for UEx in (11.0, 12.0, 13.0):
        ua, izx = nur_z_diode(UEx, 330.0, RLz)
        P(f"      U_E = {UEx:.0f} V: U_A = {ua:.3f} V, I_Z = {izx*1e3:.2f} mA")
    P(f"   Lastkennlinie bei 12 V (Längsregler | Z-Diode allein mit 330 Ohm); Z allein leitet bis R_L > "
      f"{UZ_K*330.0/(12.0-UZ_K):.0f} Ohm, also I_L < {UZ_K/(UZ_K*330.0/(12.0-UZ_K))*1e3:.1f} mA:")
    for RLx in (1e4, 2e3, 1e3, 500.0, 300.0, 250.0, 200.0, 150.0, 100.0):
        ua_t = stabilisierung(12.0, R1z, RLx)[1]
        ua_z, iz_z = nur_z_diode(12.0, 330.0, RLx)
        P(f"      R_L = {RLx:6.0f} Ohm: Regler U_A = {ua_t:.4f} V (I_L {ua_t/RLx*1e3:6.2f} mA) | Z allein U_A = {ua_z:.3f} V "
          f"(I_L {ua_z/RLx*1e3:6.2f} mA, I_Z {iz_z*1e3:5.2f} mA)")


if __name__ == "__main__":
    bericht()
    bericht_arbeitspunkt()
    bericht_verstaerker()
