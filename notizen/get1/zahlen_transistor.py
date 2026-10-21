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


if __name__ == "__main__":
    bericht()
