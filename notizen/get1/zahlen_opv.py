"""Zahlenwerk für das Oberthema „Operationsverstärker“ (ET1 Kap. 12), Stil 3.

Beispiel-OPV nach Art des 741 für alle Artikel des Oberthemas, Versorgung ±15 V:
  TI LM741 (SNOSC25D): Großsignalverstärkung typ. 200 V/mV (min. 50 V/mV) bei R_L >= 2 kOhm, Ausgangshub typ. ±14 V
  bei R_L >= 10 kOhm (±13 V bei 2 kOhm), Eingangswiderstand typ. 2 MOhm, Eingangsruhestrom typ. 80 nA,
  Offsetspannung typ. 1 mV, Gleichtaktunterdrückung typ. 95 dB, Kurzschlussstrom 25 mA, Slew-Rate 0,5 V/us.
  ST UA741: Verstärkungs-Bandbreite-Produkt typ. 1 MHz, Rauschspannungsdichte 23 nV/sqrt(Hz) bei 1 kHz.
  Kompensationskondensator 30 pF auf dem Chip (Miller-Integrator der zweiten Stufe).
Transistoren des Differenzverstärkers: der Beispieltransistor aus zahlen_transistor.py (Art BC547C).
Rauschen bei T = 300 K wie in zahlen_halbleiter.py.

Aufruf:  python -I zahlen_opv.py > zahlen_opv.txt
"""
import math
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad

sys.path.insert(0, str(Path(__file__).resolve().parent))
from zahlen_halbleiter import T, UT, e, kB  # noqa: E402
from zahlen_transistor import IS, _loese, stroeme  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = print

# ------------------------------------------------------------------ Beispiel-OPV (Art 741, ±15 V)
UB = 15.0                     # Versorgung ±U_B
VD, VD_MIN = 2e5, 5e4         # Leerlaufverstärkung typ./min.
FT = 1e6                      # Transitfrequenz (Verstärkungs-Bandbreite-Produkt) in Hz
WT = 2 * math.pi * FT         # in 1/s
SR = 0.5e6                    # Anstiegsgeschwindigkeit in V/s
UAMAX, UAMIN = 14.0, -14.0    # Ausgangsgrenzen bei R_L >= 10 kOhm
RE_OPV = 2e6                  # Eingangswiderstand in Ohm
IBIAS = 80e-9                 # Eingangsruhestrom in A
UOS = 1e-3                    # Offsetspannung typ.
EN = 23e-9                    # Rauschspannungsdichte in V/sqrt(Hz) (weißer Teil)
FC_1F = 100.0                 # angenommene 1/f-Eckfrequenz eines Universal-OPV (MT-048: bis etwa 100 Hz)
CC = 30e-12                   # Kompensationskondensator in F

# ------------------------------------------------------------------ Rauschen


def u_therm(R, bw=1.0):
    """Effektivwert des thermischen Rauschens eines Widerstands R über die Bandbreite bw (bw = 1 Hz: Dichte)."""
    return math.sqrt(4 * kB * T * R * bw)


def u_ktc(C):
    """Effektivwert der Rauschspannung an einem Kondensator C, der mit irgendeinem Widerstand verbunden ist."""
    return math.sqrt(kB * T / C)


def enbw_rc(R, C):
    """Rauschbandbreite eines RC-Tiefpasses, numerisch: Integral von |H|^2 über f, mit x = 2 pi f R C."""
    val, _ = quad(lambda x: 1.0 / (1.0 + x * x), 0, np.inf)
    return val / (2 * math.pi * R * C)


def i_schrot(I, bw=1.0):
    return math.sqrt(2 * e * I * bw)


def u_1f(ew, fc, f1, f2):
    """Effektivwert von weißem Rauschen (Dichte ew) plus 1/f-Rauschen mit Eckfrequenz fc zwischen f1 und f2."""
    return ew * math.sqrt((f2 - f1) + fc * math.log(f2 / f1))


def db(p):
    return 10 * math.log10(p)


def bericht_rauschen():
    P("=" * 100)
    P("THEMA 01 (Kap. 12.1–12.4): Rauschen")
    P("=" * 100)
    P(f"T = {T:.0f} K, kT = {kB*T:.4e} J, U_T = {UT*1e3:.2f} mV")
    P("1) Thermisches Rauschen, Dichte sqrt(4kTR) und Effektivwerte")
    for R in (100.0, 1e3, 10e3, 100e3, 1e6):
        d = u_therm(R)
        P(f"   R = {R:9.0f} Ohm: Dichte {d*1e9:7.2f} nV/sqrt(Hz) (|u|^2 = {d**2:.3e} V^2/Hz); "
          f"20 kHz: {u_therm(R, 20e3)*1e6:7.3f} uV; 1 MHz: {u_therm(R, 1e6)*1e6:7.2f} uV")
    P(f"   Einheitenprobe: kT*R in J*Ohm = V^2*s; 4kTR bei 1 kOhm = {4*kB*T*1e3:.4e} V^2/Hz")
    f77 = math.sqrt(77 / T)
    P(f"   Kühlung auf 77 K: Faktor sqrt(77/300) = {f77:.4f}; 10 kOhm, 20 kHz: {u_therm(10e3, 20e3)*f77*1e6:.3f} uV")
    for us in (1e-3, 10e-6):
        P(f"   Signal {us*1e6:7.1f} uV gegen 10 kOhm/20 kHz: SNR {db((us/u_therm(10e3, 20e3))**2):.1f} dB")
    P("2) kT/C-Rauschen und Herleitung von 4kTR über die Rauschbandbreite des RC-Tiefpasses")
    for C in (1e-12, 10e-12, 100e-12):
        P(f"   C = {C*1e12:5.0f} pF: sqrt(kT/C) = {u_ktc(C)*1e6:6.2f} uV (unabhängig von R)")
    for R, C in ((10e3, 10e-12), (1e3, 10e-12), (1e6, 10e-12)):
        bw = enbw_rc(R, C)
        fg = 1 / (2 * math.pi * R * C)
        P(f"   R = {R:8.0f} Ohm, C = 10 pF: Grenzfrequenz {fg/1e6:7.4f} MHz, Rauschbandbreite numerisch {bw/1e6:7.4f} MHz, "
          f"1/(4RC) = {1/(4*R*C)/1e6:7.4f} MHz, Verhältnis {bw/fg:.4f} (pi/2 = {math.pi/2:.4f}); "
          f"sqrt(4kTR*bw) = {u_therm(R, bw)*1e6:6.2f} uV")
    P("   Thermische Grenzfrequenz, oberhalb der 4kTR nicht mehr gilt: kT/h = "
      f"{kB*T/6.62607015e-34/1e12:.2f} THz")
    P("3) Schrotrauschen sqrt(2eI)")
    for I in (1e-3, 1e-6, 1e-9, 1e-12):
        d = i_schrot(I)
        r = i_schrot(I, 20e3)
        P(f"   I = {I:8.0e} A: Dichte {d*1e12:9.4f} pA/sqrt(Hz); 20 kHz: {r:.3e} A eff, relativ {r/I*100:.4f} %")
    tau = 1 / (2 * 20e3)
    N = 1e-3 * tau / e
    P(f"   Zählmodell: 1 mA, Fenster tau = 1/(2*20 kHz) = {tau*1e6:.1f} us: N = {N:.4e} Ladungen, sqrt(N) = {math.sqrt(N):.4e}, "
      f"relative Schwankung {1/math.sqrt(N)*100:.5f} % (= {i_schrot(1e-3, 20e3)/1e-3*100:.5f} % aus 2eI)")
    P("4) 1/f-Rauschen: gleiche Leistung je Dekade; OPV mit 23 nV/sqrt(Hz) weiß und angenommener Eckfrequenz 100 Hz")
    dek = EN * math.sqrt(FC_1F * math.log(10))
    P(f"   1/f-Anteil je Dekade: {dek*1e9:.1f} nV eff (Dichte^2 * f_c * ln 10)")
    for f in (1.0, 10.0, 100.0, 1e3):
        P(f"   Dichte bei {f:6.0f} Hz: {EN*math.sqrt(1+FC_1F/f)*1e9:.1f} nV/sqrt(Hz)")
    for f1, f2 in ((0.1, 10.0), (10.0, 1e3), (1e3, 20e3), (20.0, 20e3)):
        w = EN * math.sqrt(f2 - f1)
        g = u_1f(EN, FC_1F, f1, f2)
        P(f"   {f1:7.1f} Hz bis {f2:8.0f} Hz: nur weiß {w*1e9:8.1f} nV, mit 1/f {g*1e9:8.1f} nV")
    P("5) Unabhängige Quellen addieren sich quadratisch: OPV-Rauschen 23 nV/sqrt(Hz) + Quelle 10 kOhm")
    d10 = u_therm(10e3)
    P(f"   sqrt({EN*1e9:.1f}^2 + {d10*1e9:.2f}^2) = {math.hypot(EN, d10)*1e9:.2f} nV/sqrt(Hz) "
      f"(lineare Summe wäre {(EN+d10)*1e9:.1f})")
    P("6) Signal-Rausch-Verhältnis einer Messkette (20 kHz Bandbreite)")
    US = 1e-3
    ur_q = u_therm(10e3, 20e3)
    ur_opv = EN * math.sqrt(20e3)
    snr_q = (US / ur_q) ** 2
    ur_ein = math.hypot(ur_q, ur_opv)
    snr_ein = (US / ur_ein) ** 2
    P(f"   Sensor: Signal {US*1e3:.0f} mV eff, Innenwiderstand 10 kOhm -> Rauschen {ur_q*1e6:.3f} uV, "
      f"SNR {snr_q:.3e} = {db(snr_q):.1f} dB")
    P(f"   Verstärker (23 nV/sqrt(Hz) -> {ur_opv*1e6:.3f} uV am Eingang): Gesamtrauschen am Eingang {ur_ein*1e6:.3f} uV, "
      f"SNR {snr_ein:.3e} = {db(snr_ein):.1f} dB (um {db(snr_q)-db(snr_ein):.1f} dB schlechter)")
    v = 100.0
    P(f"   Verstärkung {v:.0f}: Ausgang {US*v*1e3:.0f} mV, Rauschen {ur_ein*v*1e6:.1f} uV, SNR unverändert {db(snr_ein):.1f} dB")
    un = 1e-3
    snr_ohne = US**2 / (ur_q**2 + un**2)
    snr_mit = (US * v) ** 2 / ((ur_ein * v) ** 2 + un**2)
    P(f"   Folgestufe mit 1 mV Eigenrauschen: ohne Vorverstärker SNR {snr_ohne:.3f} = {db(snr_ohne):.1f} dB; "
      f"mit Vorverstärker {snr_mit:.1f} = {db(snr_mit):.1f} dB")
    for v2 in (1000.0,):
        snr2 = (US * v2) ** 2 / ((ur_ein * v2) ** 2 + un**2)
        P(f"   Variation Verstärkung {v2:.0f}: hinter der Folgestufe {db(snr2):.1f} dB")
    P(f"   Verhältnis Signal/Rauschen hinter der Folgestufe (mit, Verstärkung 100): {math.sqrt(snr_mit):.1f}")
    P(f"   dB-Probe: Faktor 10 in der Spannung = {db(100):.0f} dB, Faktor 2 = {20*math.log10(2):.2f} dB")
    P("7) Effektivwert und Quadrat-Mittel: Sinus 1 V Amplitude -> 1/sqrt(2) = "
      f"{1/math.sqrt(2):.4f} V; Summe zweier Sinus 1 V (50 Hz) + 1 V (150 Hz): "
      f"{math.sqrt(np.mean((np.sin(2*np.pi*50*np.linspace(0,0.02,200001)) + np.sin(2*np.pi*150*np.linspace(0,0.02,200001)))**2)):.4f} V "
      f"(sqrt(0,5+0,5) = 1)")


# ------------------------------------------------------------------ Differenzverstärker
UCC_D, UEE_D, RC_D, I0_D = 15.0, -15.0, 10e3, 1e-3


def diffpaar(ue1, ue2, I0=I0_D, RT=None, RC=RC_D, UCC=UCC_D, UEE=UEE_D):
    """Differenzverstärker mit dem vollständigen Transistormodell. Fußpunkt: ideale Stromquelle I0 oder Widerstand RT
    nach UEE. Unbekannte: Emitterknoten uE und die Kollektorpotentiale uc1, uc2."""
    def f(x):
        uE, uc1, uc2 = x
        ic1, ib1 = stroeme(ue1 - uE, uc1 - uE)
        ic2, ib2 = stroeme(ue2 - uE, uc2 - uE)
        itail = I0 if RT is None else (uE - UEE) / RT
        return [(ic1 + ib1 + ic2 + ib2 - itail) * 1e3, uc1 - (UCC - RC * ic1), uc2 - (UCC - RC * ic2)]
    x0 = [max(ue1, ue2) - 0.62, UCC - RC * 0.5e-3, UCC - RC * 0.5e-3]
    uE, uc1, uc2 = _loese(f, x0)
    ic1, ib1 = stroeme(ue1 - uE, uc1 - uE)
    ic2, ib2 = stroeme(ue2 - uE, uc2 - uE)
    return dict(uE=uE, uc1=uc1, uc2=uc2, ic1=ic1, ic2=ic2, ib1=ib1, ib2=ib2, uA=uc1 - uc2)


def bericht_differenz():
    P("=" * 100)
    P("THEMA 01: Differenzverstärker (U_CC = +15 V, U_EE = -15 V, R_C = 10 kOhm, Fußstrom I_0 = 1 mA)")
    P("=" * 100)
    r = diffpaar(0.0, 0.0)
    gm = r["ic1"] / UT
    P(f"Ruhe (U_e1 = U_e2 = 0): I_C = {r['ic1']*1e3:.4f} mA je Zweig, I_B = {r['ib1']*1e6:.3f} uA, "
      f"Emitterknoten {r['uE']:.4f} V, U_BE = {-r['uE']:.4f} V, U_C = {r['uc1']:.4f} V, U_CE = {r['uc1']-r['uE']:.3f} V")
    P(f"   U_RC = {RC_D*r['ic1']:.4f} V; Steilheit g_m = I_C/U_T = {gm*1e3:.3f} mS (mit 0,5 mA: {0.5e-3/UT*1e3:.3f} mS)")
    d = 1e-4
    a = diffpaar(+d, 0.0)
    b = diffpaar(-d, 0.0)
    vu = (a["uA"] - b["uA"]) / (2 * d)
    vu2 = ((a["uc2"]) - (b["uc2"])) / (2 * d)
    vu1 = ((a["uc1"]) - (b["uc1"])) / (2 * d)
    dic1 = (a["ic1"] - b["ic1"]) / (2 * d)
    due = (a["uE"] - b["uE"]) / (2 * d)
    P(f"Kleinsignal (U_e1 um ±0,1 mV, U_e2 fest): dU_A/dU_e1 = {vu:.2f} (Differenzausgang); "
      f"U_a1 allein {vu1:.2f}, U_a2 allein {vu2:.2f}")
    P(f"   Emitterknoten folgt mit {due:.4f} (halbe Eingangsänderung); dI_C1/dU_e1 = {dic1*1e3:.3f} mS = g_m * {dic1/gm:.4f}")
    P(f"   Formel -g_m R_C = {-0.5e-3/UT*RC_D:.1f} (ideal, 0,5 mA); mit r_CE: r_CE = (70 V + U_CE)/I_C = "
      f"{(70+r['uc1']-r['uE'])/r['ic1']/1e3:.1f} kOhm, -g_m (R_C||r_CE) = "
      f"{-gm*(RC_D*((70+r['uc1']-r['uE'])/r['ic1'])/(RC_D+(70+r['uc1']-r['uE'])/r['ic1'])):.1f}")
    P(f"   Skriptformel -2 S R = {-2*0.5e-3/UT*RC_D:.1f} (Faktor 2 zu groß)")
    P(f"   Obergrenze mit Widerstandslast: U_RC/U_T = {RC_D*0.5e-3/UT:.0f}; mit der ganzen Versorgung 15 V/U_T = {15/UT:.0f}")
    P("Großsignal: Stromaufteilung über U_e1 - U_e2 (vollständiges Modell gegen Formel I_0/(1+exp(-U/U_T)))")
    for ud in (0.0, 0.005, 0.010, UT, 0.050, 0.100, 0.150):
        rr = diffpaar(ud, 0.0)
        anteil = rr["ic1"] / (rr["ic1"] + rr["ic2"])
        formel = 1 / (1 + math.exp(-ud / UT))
        lin = 0.5 + ud / (4 * UT)
        P(f"   {ud*1e3:7.2f} mV: I_C1/(I_C1+I_C2) = {anteil:.4f} (Formel {formel:.4f}, Gerade {lin:.4f}); "
          f"I_C1/I_C2 = {rr['ic1']/rr['ic2']:.4f} (exp {math.exp(ud/UT):.4f}); U_A = {rr['uA']:.3f} V; "
          f"tanh-Fehler gegen lineare Näherung {(math.tanh(ud/(2*UT))/(ud/(2*UT)) - 1)*100 if ud else 0:.2f} %")
    P("Gleichtakt (beide Eingänge gleich verschoben), ideale Stromquelle:")
    for ug in (-5.0, 0.0, 5.0):
        rr = diffpaar(ug, ug)
        P(f"   U_Gl = {ug:+.1f} V: I_C1 = {rr['ic1']*1e3:.5f} mA, Emitterknoten {rr['uE']:.4f} V, U_a1 = {rr['uc1']:.5f} V, "
          f"U_A = {rr['uA']*1e6:.3f} uV")
    rp, rm = diffpaar(1.0, 1.0), diffpaar(-1.0, -1.0)
    P(f"   Gleichtaktverstärkung am Einzelausgang (±1 V): {(rp['uc2']-rm['uc2'])/2:.2e} (über die Basisströme/Early)")
    RT = (r["uE"] - UEE_D) / I0_D
    RT_r = round(RT / 100) * 100
    P(f"Fußpunkt mit Widerstand statt Stromquelle: R_T = {RT/1e3:.3f} kOhm für 1 mA, gerundet {RT_r/1e3:.1f} kOhm")
    r0 = diffpaar(0.0, 0.0, RT=RT_r)
    rp, rm = diffpaar(1.0, 1.0, RT=RT_r), diffpaar(-1.0, -1.0, RT=RT_r)
    a = diffpaar(+d, 0.0, RT=RT_r)
    b = diffpaar(-d, 0.0, RT=RT_r)
    vgl = (rp["uc2"] - rm["uc2"]) / 2
    vdiff_e = (a["uc2"] - b["uc2"]) / (2 * d)
    P(f"   Ruhe: I_C = {r0['ic1']*1e3:.4f} mA; Gleichtakt ±1 V: Fußstrom {(rp['uE']-UEE_D)/RT_r*1e3:.4f} / "
      f"{(rm['uE']-UEE_D)/RT_r*1e3:.4f} mA, U_a2-Verstärkung {vgl:.4f} (Formel -R_C/(2R_T) = {-RC_D/(2*RT_r):.4f}), "
      f"Differenzausgang U_A {((rp['uA']-rm['uA'])/2)*1e6:.3f} uV/V")
    P(f"   Einzelausgang: Differenzverstärkung {vdiff_e:.2f}, Gleichtakt {vgl:.4f}, Verhältnis {abs(vdiff_e/vgl):.0f} "
      f"= {20*math.log10(abs(vdiff_e/vgl)):.1f} dB")
    P("Stromspiegel als Last (Abschätzung): g_m (r_CE2 || r_CE4) mit r_CE = (70 V + 10 V)/0,5 mA = 160 kOhm: "
      f"{0.5e-3/UT*80e3:.0f}")


# ------------------------------------------------------------------ idealer OPV, Komparator, Flash-Wandler
def bericht_opv():
    P("=" * 100)
    P("THEMA 01: Beispiel-OPV (Art 741, ±15 V), Komparator, Flash-Wandler")
    P("=" * 100)
    P(f"v_D = {VD:.0f} (min {VD_MIN:.0f}); Ausgang ±{UAMAX:.0f} V; linearer Bereich |U_D| <= U_A,max/v_D = "
      f"{UAMAX/VD*1e6:.1f} uV (bei v_D min: {UAMAX/VD_MIN*1e6:.0f} uV)")
    P(f"   Offsetspannung {UOS*1e3:.0f} mV = {UOS/(UAMAX/VD):.1f}-fache des linearen Bereichs")
    P(f"   Eingangswiderstand {RE_OPV/1e6:.0f} MOhm; Ruhestrom {IBIAS*1e9:.0f} nA; Strom durch R_e bei 70 uV: "
      f"{70e-6/RE_OPV*1e12:.0f} pA")
    P("Komparator: Ausgang +14 V für U_D > 70 uV, -14 V für U_D < -70 uV")
    Uref, n = 2.0, 2
    schw = [Uref * m / 2**n for m in range(1, 2**n)]
    UEx = 1.2
    code = "".join("1" if UEx > s else "0" for s in reversed(schw))
    P(f"Flash-Wandler {n} Bit, U_Ref = {Uref} V, {2**n} gleiche Widerstände: Schwellen {schw} V; U_E = {UEx} V -> "
      f"Komparatoren (oben nach unten) {code} -> {code.count('1')} = binär {format(code.count('1'), '02b')}, "
      f"Bereich {code.count('1')*Uref/2**n} bis {(code.count('1')+1)*Uref/2**n} V; Stufe {Uref/2**n} V")
    for nb in (2, 3, 8, 10):
        P(f"   {nb:2d} Bit: {2**nb-1:4d} Komparatoren, {2**nb:4d} Widerstände")


# ------------------------------------------------------------------ Rückkopplung
R1_K, R2_K = 10e3, 90e3
K = R1_K / (R1_K + R2_K)


def a_geschlossen(vD, k=K):
    return vD / (1 + k * vD)


def sim(kind, ue_func, t_end, dt=1e-9, ua0=0.0, k=K, vD=VD, sr=True, grenzen=True, aufzeichnen=None):
    """Einpoliges OPV-Modell tau0 dU_A/dt = v_D U_D - U_A (tau0 = v_D/omega_T), optional mit Slew-Rate und Ausgangsgrenzen.
    kind 'gegen': U_D = U_E - k U_A (Pluseingang an U_E, Teiler an Minus); 'mit': U_D = k U_A - U_E (invertierender
    Schmitt-Trigger)."""
    tau0 = vD / WT
    n = int(round(t_end / dt))
    ua = ua0
    out = []
    for i in range(n + 1):
        t = i * dt
        ue = ue_func(t)
        ud = (ue - k * ua) if kind == "gegen" else (k * ua - ue)
        if aufzeichnen and i % aufzeichnen == 0:
            out.append((t, ue, ua, ud))
        dua = (vD * ud - ua) / tau0
        if sr:
            dua = max(-SR, min(SR, dua))
        ua += dua * dt
        if grenzen:
            ua = max(UAMIN, min(UAMAX, ua))
    return ua, out


def bericht_rueckkopplung():
    P("=" * 100)
    P(f"THEMA 01: Rückkopplung mit Teiler R_1 = {R1_K/1e3:.0f} kOhm, R_2 = {R2_K/1e3:.0f} kOhm, k = {K}")
    P("=" * 100)
    for vD in (VD_MIN, VD, 1e6):
        A = a_geschlossen(vD)
        P(f"   v_D = {vD:9.0f}: A = U_A/U_E = {A:.6f}, Abweichung von 1/k = {(A*K-1)*100:.5f} %, k v_D = {K*vD:.0f}, "
          f"U_D/U_E = 1/(1+k v_D) = {1/(1+K*vD):.3e}")
    dA = (a_geschlossen(VD) - a_geschlossen(VD_MIN)) / a_geschlossen(VD) * 100
    P(f"   v_D von 200 000 auf 50 000 (-75 %): A ändert sich um {dA:.4f} %")
    P(f"   U_D bei U_A = 5 V: {5/VD*1e6:.1f} uV; bei 14 V: {14/VD*1e6:.1f} uV; Eingangsstrom über R_e bei 25 uV: "
      f"{25e-6/RE_OPV*1e12:.1f} pA")
    P(f"   Sättigung: U_E = 2 V, A = 10 -> U_A wäre 20 V, begrenzt auf 14 V: U_D = 2 V - 0,1*14 V = {2-K*14:.2f} V")
    tau0 = VD / WT
    taug = 1 / (K * WT)
    P(f"Dynamik: omega_T = {WT:.4e} 1/s; Leerlauf-Zeitkonstante tau_0 = v_D/omega_T = {tau0*1e3:.2f} ms "
      f"(Grenzfrequenz {1/(2*math.pi*tau0):.2f} Hz)")
    P(f"   mit Rückkopplung tau = 1/(k omega_T) = {taug*1e6:.4f} us (einpolig exakt tau_0/(1+k v_D) = "
      f"{tau0/(1+K*VD)*1e6:.4f} us); 63 % nach {taug*1e6:.2f} us, 0,1 % nach {taug*math.log(1000)*1e6:.2f} us")
    P(f"   Anstieg zu Beginn = omega_T U_E; linear bis U_E = SR/omega_T = {SR/WT*1e3:.1f} mV")
    P(f"   omega_T * 1 mV = {WT*1e-3/1e3:.2f} V/ms; Sprung 50 mV: Anfangssteigung {WT*0.05/1e6:.3f} V/us")
    P(f"   Spannungsfolger k = 1: tau = {1/WT*1e6:.4f} us; k = 0,1: {1/(0.1*WT)*1e6:.4f} us")
    P(f"   Integratormodell: G_m1 = omega_T C_c = {WT*CC*1e3:.4f} mS; größter Ladestrom SR C_c = {SR*CC*1e6:.1f} uA")
    IMAX = SR * CC
    GM1 = WT * CC
    P(f"   Nichtlineare Eingangsstufe (Strom = I_max tanh(G_m1 U_D/I_max), I_max = {IMAX*1e6:.1f} uA, G_m1 = {GM1*1e3:.4f} mS):")
    for ud in (0.01, 0.05, SR / WT):
        lin = GM1 * ud
        nl = IMAX * math.tanh(GM1 * ud / IMAX)
        P(f"      U_D = {ud*1e3:5.1f} mV: linear {lin*1e6:6.3f} uA, tanh {nl*1e6:6.3f} uA ({(nl/lin-1)*100:+.2f} %), "
          f"Anfangssteigung {nl/CC/1e6:.4f} V/us statt {lin/CC/1e6:.4f}")
    for UE in (0.01, 0.05):
        _, rec = sim("gegen", lambda t: UE, 12e-6, aufzeichnen=200)
        P(f"   Sprung U_E = {UE*1e3:.0f} mV (Gegenkopplung), Endwert {UE*a_geschlossen(VD):.6f} V, End-U_D "
          f"{UE/(1+K*VD)*1e6:.3f} uV, Anfangssteigung {WT*UE/1e6:.4f} V/us:")
        for t, ue, ua, ud in rec[::5]:
            if t <= 12e-6 + 1e-12:
                P(f"      t = {t*1e6:5.2f} us: U_A = {ua:.5f} V, U_D = {ud*1e6:10.3f} uV, "
                  f"Integratormodell {UE/K*(1-math.exp(-t/taug)):.5f} V")
    P("   Mitkopplung (invertierender Schmitt-Trigger, U_E = 0), Start mit kleiner Abweichung von der Ruhelage U_A = 0:")
    for ua0, srflag in ((1.3e-4, False), (1.3e-4, True), (1e-2, True)):
        _, rec = sim("mit", lambda t: 0.0, 80e-6, ua0=ua0, sr=srflag, aufzeichnen=10)
        t13 = next((t for t, ue, ua, ud in rec if abs(ua) >= 13.0), None)
        P(f"      U_A(0) = {ua0*1e3:.3f} mV, Slew-Rate {'an' if srflag else 'aus'}: |U_A| erreicht 13 V nach "
          f"{t13*1e6 if t13 else float('nan'):.1f} us (Exponentialphase allein: tau ln(13 V/U_A0) = "
          f"{taug*math.log(13/ua0)*1e6:.1f} us)")
    P(f"   thermisches Rauschen 10 kOhm über 1 MHz: {u_therm(10e3, 1e6)*1e6:.1f} uV (am Eingang; U_A0 = U_D/k = "
      f"{u_therm(10e3, 1e6)/K*1e3:.3f} mV)")
    P("Zyklenbild des Skripts (Ausgang springt je Zyklus auf v_D U_D), Gegenkopplung, U_E = 0,5 V, Start U_A = 0:")
    ua = 0.0
    for nz in range(1, 5):
        ua = VD * (0.5 - K * ua)
        P(f"   Zyklus {nz}: U_A = {ua:.4e} V")
    P(f"   Faktor je Zyklus -k v_D = {-K*VD:.0f}; Ruhelage {0.5*a_geschlossen(VD):.5f} V")
    R1i, R2i = 10e3, 90e3
    ki = R1i / (R1i + R2i)
    ua = 0.0
    P(f"   invertierender Verstärker (Skript Bild 12.7) mit R_2/R_1 = 9, U_E = 0,5 V: Faktor je Zyklus -v_D R_1/(R_1+R_2) = "
      f"{-VD*ki:.0f}")
    for nz in range(1, 4):
        ua = VD * (-(0.5 * R2i + ua * R1i) / (R1i + R2i))
        P(f"   Zyklus {nz}: U_A = {ua:.4e} V")


# ------------------------------------------------------------------ Schmitt-Trigger
def schmitt_kette(ue, oben, unten, start_hoch=True):
    """Invertierender Schmitt-Trigger als Zustandsautomat (ideal schnell): hoch -> tief, wenn U_E > oben; tief -> hoch,
    wenn U_E < unten."""
    hoch = start_hoch
    aus = np.empty_like(ue)
    for i, u in enumerate(ue):
        if hoch and u > oben:
            hoch = False
        elif not hoch and u < unten:
            hoch = True
        aus[i] = UAMAX if hoch else UAMIN
    return aus


def bericht_schmitt():
    P("=" * 100)
    P("THEMA 01: Invertierender Schmitt-Trigger (R_1 = 10 kOhm nach Masse, R_2 = 90 kOhm vom Ausgang, k = 0,1)")
    P("=" * 100)
    Uo, Uu = K * UAMAX, K * UAMIN
    P(f"Schwellen: U_S,o = k U_A,max = {Uo:.2f} V (hoch -> tief), U_S,u = k U_A,min = {Uu:.2f} V (tief -> hoch); "
      f"Hysteresebreite {Uo-Uu:.2f} V")
    P(f"   Datenblatt-Minimum ±12 V: Schwellen ±{K*12:.2f} V")
    P(f"   Ruhelage U_A = U_E/k existiert (z. B. U_E = 0,5 V -> {0.5/K:.1f} V), ist aber instabil")
    fs = 200e3
    t = np.arange(0, 0.04, 1 / fs)
    rng = np.random.default_rng(1)
    rausch = 0.2 * rng.standard_normal(t.size)
    ue = 3.0 * np.cos(2 * np.pi * 50 * t) + rausch
    komp = np.where(ue < 0, UAMAX, UAMIN)
    sch = schmitt_kette(ue, Uo, Uu, start_hoch=True)
    wk = np.count_nonzero(np.diff(komp))
    ws = np.count_nonzero(np.diff(sch))
    nulld = np.count_nonzero(np.diff(np.sign(np.cos(2 * np.pi * 50 * t))) != 0)
    P(f"Verrauschter Eingang: Sinus 3 V, 50 Hz, Rauschen 0,2 V eff. (Abtastung 200 kHz), 40 ms: "
      f"{nulld} Nulldurchgänge des Sinus")
    P(f"   Komparator (Schwelle 0): {wk} Umschaltungen; Schmitt-Trigger (±1,4 V): {ws} Umschaltungen")
    idx = np.flatnonzero(np.diff(komp))
    gruppen, start = [], idx[0]
    last = idx[0]
    for i in idx[1:]:
        if t[i] - t[last] > 2e-3:
            gruppen.append((start, last))
            start = i
        last = i
    gruppen.append((start, last))
    zahlen = [int(np.count_nonzero((idx >= a) & (idx <= b))) for a, b in gruppen]
    breiten = [float((t[b] - t[a]) * 1e3) for a, b in gruppen]
    P(f"   Umschaltungen je Nulldurchgang (Komparator): {zahlen}; Dauer der Unruhe in ms: "
      f"{[round(x, 2) for x in breiten]}")
    phi = math.degrees(math.asin(Uo / 3.0))
    P(f"   Ohne Rauschen schaltet der Schmitt-Trigger bei ±1,4 V, also {phi:.1f}° nach dem Nulldurchgang ({phi/360*20:.2f} ms)")
    sauber = 3.0 * np.cos(2 * np.pi * 50 * t)
    nd = np.flatnonzero(np.diff(np.sign(sauber)) != 0)
    ws_idx = np.flatnonzero(np.diff(sch))
    for i in ws_idx:
        vor = nd[nd <= i]
        dt_ms = (t[i] - t[vor[-1]]) * 1e3 if vor.size else float("nan")
        P(f"   Schmitt-Wechsel bei t = {t[i]*1e3:7.3f} ms: {dt_ms:.2f} ms nach dem Nulldurchgang, Signal ohne Rauschen "
          f"{sauber[i]:+.3f} V, mit Rauschen {ue[i+1]:+.3f} V; zum Zurückschalten nötiger Rauschausschlag "
          f"{abs(sauber[i] - (Uu if sauber[i] > 0 else Uo)):.2f} V = {abs(sauber[i] - (Uu if sauber[i] > 0 else Uo))/0.2:.1f} Effektivwerte")
    P(f"   Rauschen 0,2 V eff: Hysterese 2,8 V = {2.8/0.2:.0f} Effektivwerte")


if __name__ == "__main__":
    bericht_rauschen()
    bericht_differenz()
    bericht_opv()
    bericht_rueckkopplung()
    bericht_schmitt()
