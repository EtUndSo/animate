"""Zahlenwerk für Schaltungstechnik, Oberthema Bipolartransistor (Stil 3). Thema 1: Arbeitsbereiche und
Transportmodell (Abschnitte A bis K).

Eigenes Beispielsystem (keine Aufgabe aus Skript oder Übung): ein integrierter npn-Transistor, wie er in einer
Bipolar- oder BiCMOS-Technologie neben den MOSFETs des Kapitels 3 steht. Silizium bei 300 K, U_T = 25,85 mV wie im
ET1-Zahlenwerk (notizen/get1/zahlen_halbleiter.py).

Elektrisches Modell (Transportmodell, Gummel-Poon-Form wie in Schaltungssimulatoren):
- Emitterfläche A_E = 2 µm x 10 µm = 20 µm² (der Skalierungsparameter des Bipolartransistors);
- Transportsättigungsstrom I_S = 1e-16 A (5e-18 A/µm²; der diskrete ET1-Beispieltransistor hat 1e-14 A auf
  0,015 mm², also 6,7e-19 A/µm²; der integrierte Transistor hat eine dünnere Basis und deshalb mehr Strom je Fläche);
- Normalverstärkung B_N = 100, Inversverstärkung B_I = 2 (Kollektor schwächer dotiert als der Emitter);
- Early-Spannung U_A = 50 V, Early-Faktor (1 + U_CE/U_A) auf den Transportstrom;
- nur ausführliche Fassung: Rekombinationsstrom der Basis-Emitter-Raumladungszone I_SE = 1e-13 A mit n_E = 2
  (senkt B bei kleinen Strömen), Knickstrom der starken Injektion I_KF = 50 mA (senkt B bei großen Strömen),
  Bahnwiderstände R_B = 100 Ω, R_E = 5 Ω, R_C = 20 Ω.
Aufruf: python -I zahlen_bipolar.py > zahlen_bipolar.txt
"""
import math
import sys

import numpy as np
from scipy.optimize import brentq, fsolve

sys.stdout.reconfigure(encoding="utf-8")
P = print

UT = 25.85e-3            # V, Temperaturspannung bei 300 K (wie zahlen_halbleiter.py)
IS = 1e-16               # A
BN, BI = 100.0, 2.0
UA = 50.0                # V
AE = 20.0                # µm²
ISE, NE = 1e-13, 2.0     # A, Emissionskoeffizient des Rekombinationsstroms
IKF = 50e-3              # A
RB, RE, RC = 100.0, 5.0, 20.0   # Ω

def dio(u, i0=IS):
    return i0 * math.expm1(u / UT)

def transport(ube, ubc, early=True):
    """Transportmodell: Rückgabe (I_BN, I_BI, I_T, I_C, I_B, I_E) in A; Zählpfeile I_C, I_B hinein, I_E heraus (negativ)."""
    ibn, ibi = dio(ube) / BN, dio(ubc) / BI
    it = BN * ibn - BI * ibi
    if early:
        it *= 1 + (ube - ubc) / UA          # U_CE = U_BE - U_BC
    ic = it - ibi
    ib = ibn + ibi
    ie = -(ib + ic)
    return ibn, ibi, it, ic, ib, ie

def mA(x): return f"{x*1e3:.4g} mA"
def uA(x): return f"{x*1e6:.4g} µA"

P("== A. Modellparameter des integrierten Beispiel-npn ==")
P(f"I_S = {IS:.0e} A, B_N = {BN:.0f}, B_I = {BI:.0f}, U_A = {UA:.0f} V, U_T = {UT*1e3:.2f} mV, A_E = {AE:.0f} µm² (2 µm x 10 µm)")
P(f"I_S je Fläche: {IS/AE:.2e} A/µm²; ET1-Transistor 1e-14 A / 15000 µm² = {1e-14/15000:.2e} A/µm² (Verhältnis {IS/AE/(1e-14/15000):.1f})")
P(f"A = B_N/(1+B_N) = {BN/(1+BN):.4f}; 1/A - 1 = 1/B_N = {1/BN:.4f}")
P(f"Spannung je Dekade Strom: U_T ln 10 = {UT*math.log(10)*1e3:.1f} mV; Verdopplung: U_T ln 2 = {UT*math.log(2)*1e3:.1f} mV")

P("\n== B. Normalbetrieb ohne Early (U_BC stark negativ): Übertragungs- und Eingangskennlinie ==")
for ube in (0.60, 0.65, 0.70, 0.75, 0.774, 0.80, 0.833, 0.85):
    ic = dio(ube)
    P(f"U_BE = {ube:.3f} V: I_C = {mA(ic):>12}, I_B = {uA(ic/BN):>12}, I_E = {mA(-(ic+ic/BN))}")
for ic in (1e-6, 10e-6, 100e-6, 1e-3, 10e-3):
    ube = UT * math.log(ic / IS + 1)
    P(f"I_C = {mA(ic):>8}: U_BE = {ube*1e3:.1f} mV, I_B = {uA(ic/BN)}")
ube1 = UT * math.log(1e-3 / IS)
P(f"Arbeitspunkt des Kapitels: I_C = 1 mA bei U_BE = {ube1*1e3:.1f} mV (U_T ln(1e13) = {UT*math.log(1e13)*1e3:.1f} mV), I_B = 10 µA, I_E = -1,01 mA")
P(f"+10 mV am Gate der Basis: Faktor exp(10/25,85) = {math.exp(0.010/UT):.3f}; +60 mV: {math.exp(0.060/UT):.2f}; +18 mV: {math.exp(0.018/UT):.3f}")
P(f"Diodengleichung mit -1: bei U_BE = 0,3 V I_C = {dio(0.3):.3e} A (gegen I_S = 1e-16 A); bei U_BE = -1 V I_C = {dio(-1.0):.3e} A")

P("\n== C. Early-Effekt: I_C(U_BE, U_CE) = I_S (exp(U_BE/U_T) - 1)(1 + U_CE/U_A) ==")
for uce in (0.5, 1.0, 2.5, 5.0, 10.0):
    ic = dio(ube1) * (1 + uce / UA)
    ib = dio(ube1) / BN                     # Basisstrom ohne Early-Faktor (Rückinjektion und Rekombination hängen nicht von W_B ab)
    P(f"U_BE = {ube1*1e3:.1f} mV, U_CE = {uce:4.1f} V: I_C = {ic*1e3:.4f} mA, I_B = {ib*1e6:.3f} µA, I_C/I_B = {ic/ib:.1f} (Faktor {1+uce/UA:.3f})")
P(f"Steigung der Ausgangskennlinie bei U_BE = {ube1*1e3:.1f} mV: I_S exp(U_BE/U_T)/U_A = {dio(ube1)/UA*1e6:.1f} µA/V = 20 µS; Tangente schneidet die Spannungsachse bei -U_A = -{UA:.0f} V")
P(f"Zum Vergleich MOSFET-Kapitel: lambda = 0,1 1/V entspricht U_A = 10 V; hier 1/U_A = {1/UA:.3f} 1/V")
P("Basisweitenmodulation (Herleitung): I_S ∝ 1/W_B; W_B(U_CB) = W_B0 (1 - U_CB/U_A) linearisiert -> I_C ∝ 1/(1 - U_CB/U_A) ≈ 1 + U_CB/U_A ≈ 1 + U_CE/U_A")
for ucb in (1.0, 5.0, 10.0):
    P(f"   U_CB = {ucb:4.1f} V: 1/(1 - U_CB/U_A) = {1/(1-ucb/UA):.4f}, Näherung 1 + U_CB/U_A = {1+ucb/UA:.4f}")

P("\n== D. Transportmodell: alle Ströme in den fünf Betriebszuständen (mit Early) ==")
faelle = [("stromlos", 0.0, 0.0), ("gesperrt", -1.0, -2.0), ("aktiv (normal)", ube1, ube1 - 2.5),
          ("Sättigung", 0.80, 0.55), ("Sättigung tief", 0.80, 0.70), ("invers", -1.0, ube1)]
for name, ube, ubc in faelle:
    ibn, ibi, it, ic, ib, ie = transport(ube, ubc)
    P(f"{name:16s} U_BE = {ube:7.4f} V, U_BC = {ubc:7.4f} V, U_CE = {ube-ubc:7.4f} V: I_BN = {ibn:.4e}, I_BI = {ibi:.4e}, I_T = {it:.4e}, "
      f"I_C = {ic:.4e}, I_B = {ib:.4e}, I_E = {ie:.4e} A; I_C/I_B = {ic/ib if ib else float('nan'):.2f}")

P("\n== E. Sättigung quantitativ: Basisstrom fest, Kollektorwiderstand begrenzt den Strom ==")
UCC, RCL = 2.5, 1000.0
def saett(ib_soll):
    def f(x):
        ube, ubc = x
        ibn, ibi, it, ic, ib, ie = transport(ube, ubc)
        uce = ube - ubc
        return [ib - ib_soll, ic - (UCC - uce) / RCL]
    ube, ubc = fsolve(f, [0.78, -1.0] if ib_soll * BN < (UCC - 0.8) / RCL else [0.80, 0.6], xtol=1e-12)
    return ube, ubc, transport(ube, ubc)
P(f"Schaltung: U_CC = {UCC} V, R_C = {RCL:.0f} Ω, Basis aus Stromquelle I_B")
for ib_soll in (5e-6, 10e-6, 20e-6, 23e-6, 30e-6, 50e-6, 100e-6):
    ube, ubc, (ibn, ibi, it, ic, ib, ie) = saett(ib_soll)
    P(f"I_B = {uA(ib_soll):>8}: U_BE = {ube*1e3:.1f} mV, U_BC = {ubc*1e3:7.1f} mV, U_CE = {(ube-ubc)*1e3:7.1f} mV, I_C = {ic*1e3:.4f} mA "
      f"(B_N I_B wäre {ib_soll*BN*1e3:.2f} mA), I_BN = {uA(ibn)}, I_BI = {uA(ibi)}, I_C/I_B = {ic/ib:.1f}")
ic_max = (UCC - 0.1) / RCL
P(f"Grenze: I_C,sat ≈ (U_CC - U_CE,sat)/R_C = (2,5 - 0,1)/1 kΩ = {ic_max*1e3:.2f} mA, erreicht ab I_B ≈ I_C,sat/B_N = {ic_max/BN*1e6:.0f} µA")
# U_CE,sat aus dem Transportmodell: beide Dioden leiten, U_CE = U_BE - U_BC
P("U_CE in der Sättigung ist die Differenz zweier Durchlassspannungen:")
for ib_soll in (50e-6, 100e-6):
    ube, ubc, (ibn, ibi, it, ic, ib, ie) = saett(ib_soll)
    P(f"   I_B = {uA(ib_soll)}: U_CE,sat = {ube*1e3:.1f} - {ubc*1e3:.1f} = {(ube-ubc)*1e3:.1f} mV; Übersteuerungsfaktor B_N I_B / I_C = {BN*ib_soll/ic:.2f}")
P("Geschlossene Form aus dem Transportmodell (ohne Early) gegen die numerische Lösung mit Early:")
for ib_soll in (50e-6, 100e-6):
    ube, ubc, (ibn, ibi, it, ic, ib, ie) = saett(ib_soll)
    k = ic / ib
    uces2 = UT * math.log((1 + (1 + k) / BI) / (1 - k / BN))   # aus dem Transportmodell: x/y = (1 + (1+k)/B_I)/(1 - k/B_N)
    P(f"   I_B = {uA(ib_soll)}: k = I_C/I_B = {k:.2f}; U_CE,sat = U_T ln[(1 + (1+k)/B_I)/(1 - k/B_N)] (ohne Early) = {uces2*1e3:.1f} mV; numerisch mit Early {(ube-ubc)*1e3:.1f} mV")
P(f"Grenzfall offener Kollektor (k = 0): U_CE,sat = U_T ln(1 + 1/B_I) = {UT*math.log(1+1/BI)*1e3:.1f} mV; Grenze der Sättigung k -> B_N: U_CE,sat -> unendlich (aktiver Bereich)")

P("\n== F. Inversbetrieb ==")
ibn, ibi, it, ic, ib, ie = transport(-1.0, ube1, early=False)
P(f"U_BC = {ube1*1e3:.1f} mV, U_BE = -1 V (ohne Early): I_T = {it*1e3:.4f} mA (vom Kollektor zum Emitter, negativ = Emitter->Kollektor), I_E = {ie*1e3:.4f} mA, I_B = {ib*1e3:.4f} mA, I_C = {ic*1e3:.4f} mA; |I_E|/I_B = {abs(ie)/ib:.2f} = B_I")

P("\n== G. Gummel-Plot und Stromverstärkung (nur ausführlich): I_B = I_C/B_N + I_SE (exp(U_BE/(n_E U_T)) - 1), I_C mit Knickstrom I_KF ==")
def ic_hoch(ube):
    x = IS * math.expm1(ube / UT)
    qb = 0.5 * (1 + math.sqrt(1 + 4 * x / IKF))
    return x / qb
P("U_BE [V] | I_C ideal | I_C mit I_KF | I_B ideal | I_B mit I_SE | B")
for ube in np.arange(0.40, 1.0001, 0.05):
    ici, ic = dio(ube), ic_hoch(ube)
    ibi_, ib = ici / BN, ici / BN + ISE * math.expm1(ube / (NE * UT))   # Basisstrom ohne Knick (Gummel-Poon)
    P(f"{ube:5.2f} | {ici:.3e} | {ic:.3e} | {ibi_:.3e} | {ib:.3e} | {ic/ib:7.1f}")
P("B über I_C:")
for ic_ziel in (1e-9, 10e-9, 100e-9, 1e-6, 10e-6, 100e-6, 1e-3, 3e-3, 10e-3, 30e-3, 100e-3):
    ube = brentq(lambda u: ic_hoch(u) - ic_ziel, 0.2, 1.5)
    ib = dio(ube) / BN + ISE * math.expm1(ube / (NE * UT))
    P(f"   I_C = {ic_ziel:.0e} A: U_BE = {ube*1e3:.1f} mV, I_B = {ib:.3e} A, B = {ic_ziel/ib:.1f}, Anteil I_SE-Strom am Basisstrom {ISE*math.expm1(ube/(NE*UT))/ib*100:.1f} %")
ub_max = max(np.arange(0.3, 1.2, 0.001), key=lambda u: ic_hoch(u) / (dio(u) / BN + ISE * math.expm1(u / (NE * UT))))
icm = ic_hoch(ub_max)
P(f"Maximum von B: {icm/(dio(ub_max)/BN+ISE*math.expm1(ub_max/(NE*UT))):.1f} bei I_C = {icm*1e3:.3f} mA (U_BE = {ub_max*1e3:.0f} mV)")
P(f"Steigung im Gummel-Plot: I_C 60 mV je Dekade (n = 1), I_SE-Strom {NE*UT*math.log(10)*1e3:.0f} mV je Dekade (n = 2)")

P("\n== H. Bahnwiderstände und Stromgegenkopplung durch R_E (nur ausführlich) ==")
P(f"R_B = {RB:.0f} Ω, R_E = {RE:.0f} Ω, R_C = {RC:.0f} Ω")
for ic0 in (1e-3, 10e-3):
    ube_ext = UT * math.log(ic0 / IS) + ic0 * RE + ic0 / BN * RB      # äußere Spannung, die ohne Widerstände ic0 gäbe ... hier: Spannung für ic0 MIT Widerständen
    # Vergleich: dieselbe äußere Spannung ohne Widerstände
    ic_ohne = IS * math.exp(ube_ext / UT)
    # mit Widerständen bei äußerer Spannung U_T ln(ic0/IS) (also der Spannung, die ohne Widerstände ic0 gäbe):
    u_ext0 = UT * math.log(ic0 / IS)
    f = lambda ic: UT * math.log(ic / IS) + ic * RE + ic / BN * RB - u_ext0
    ic_mit = brentq(f, 1e-9, 1.0)
    P(f"I_C = {mA(ic0)}: innere U_BE = {u_ext0*1e3:.1f} mV; Abfall an R_E = {ic0*RE*1e3:.1f} mV, an R_B = {ic0/BN*RB*1e3:.2f} mV, an R_C = {ic0*RC*1e3:.0f} mV; "
      f"äußere U_BE für denselben Strom {ube_ext*1e3:.1f} mV. Bei fester äußerer Spannung {u_ext0*1e3:.1f} mV fließen mit Widerständen nur {mA(ic_mit)} ({ic_mit/ic0*100:.1f} %)")
P(f"5 mV an R_E bei 1 mA: Faktor exp(-5/25,85) = {math.exp(-0.005/UT):.3f} (ohne die kleine Rückwirkung über R_B)")

P("\n== I. Vergleich mit dem MOSFET des Kapitels 3 (Arbeitspunkt 1 mA) ==")
P(f"Bipolar: g_m = I_C/U_T = {1e-3/UT*1e3:.1f} mS bei 1 mA, g_m/I_C = 1/U_T = {1/UT:.1f} 1/V; Basisstrom 10 µA")
P(f"MOSFET (K = 2 mA/V², Übersteuerung für 1 mA: sqrt(2 I/K) = {math.sqrt(2*1e-3/2e-3):.0f} V): g_m = 2I/U_ü = {2*1e-3/1.0*1e3:.1f} mS, g_m/I_D = {2/1.0:.0f} 1/V; Gatestrom 0")
P(f"Verhältnis g_m bipolar/MOS bei 1 mA: {(1e-3/UT)/(2e-3):.1f}")
P(f"Stromverhältnis für Faktor 10: Bipolar {UT*math.log(10)*1e3:.1f} mV; MOSFET sqrt(10) in der Übersteuerung: 1 V -> {math.sqrt(10):.2f} V, also {(math.sqrt(10)-1)*1e3:.0f} mV")

P("\n== J. Substratdiode und Isolation (integrierter Transistor) ==")
P("Substrat an der negativsten Versorgung (z. B. -2,5 V oder Masse); Kollektor-Potential stets höher -> Substratdiode (p-Substrat/n-Kollektor) gesperrt.")
P(f"Sperrstrom-Größenordnung: Diode mit I_S,sub = 1e-15 A bei -2,5 V: {dio(-2.5, 1e-15):.2e} A (praktisch null gegen 1 mA)")

P("\n== K. Zahlen für die Abbildungen ==")
P("Übertragungskennlinie I_C(U_BE) 0,5 bis 0,9 V, linear und halblog (ohne Early):")
for ube in np.arange(0.50, 0.9001, 0.05):
    P(f"   {ube:.2f} V: I_C = {dio(ube)*1e3:.4g} mA, I_B = {dio(ube)/BN*1e6:.4g} µA")
P("Ausgangskennlinienfeld I_C(U_CE) für U_BE = 0,70 / 0,75 / 0,774 / 0,80 V, U_CE 0 bis 5 V (Transportmodell mit Early):")
for ube in (0.70, 0.75, ube1, 0.80):
    zeile = []
    for uce in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.5, 5.0):
        ic = transport(ube, ube - uce)[3]
        zeile.append(f"{uce:g} V: {ic*1e3:.3f}")
    P(f"   U_BE = {ube*1e3:.0f} mV -> " + ", ".join(zeile) + " mA")
P("Sättigungsgrenze U_CE,sat (I_C 90 % des aktiven Werts) je Kurve:")
for ube in (0.70, 0.75, ube1, 0.80):
    ic_akt = transport(ube, ube - 1.0)[3] / (1 + 1.0 / UA)
    u90 = brentq(lambda uce: transport(ube, ube - uce, early=False)[3] - 0.9 * ic_akt, 0.01, 1.0)
    P(f"   U_BE = {ube*1e3:.0f} mV: U_CE,sat(90 %) = {u90*1e3:.0f} mV")
