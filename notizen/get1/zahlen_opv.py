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


# ------------------------------------------------------------------ Thema 02: Grundschaltungen
def a_invertierend(R1, R2, vD=VD):
    """Verstärkung des invertierenden Verstärkers mit endlicher Leerlaufverstärkung."""
    return -(R2 / R1) / (1 + (1 + R2 / R1) / vD)


def a_nichtinvertierend(R1, R2, vD=VD):
    return (1 + R2 / R1) / (1 + (1 + R2 / R1) / vD)


def subtrahierer(ue1, ue2, R1, R2, R3, R4):
    """Gl. 12.6: U_A = (R1+R2)/R1 * R4/(R3+R4) * U_E2 - R2/R1 * U_E1 (idealer OPV)."""
    return (R1 + R2) / R1 * R4 / (R3 + R4) * ue2 - R2 / R1 * ue1


def bericht_grundschaltungen():
    from zahlen_halbleiter import IS as IS_DIODE, IS_von_T, spannung_real
    P("=" * 100)
    P("THEMA 02 (Kap. 12.5, 12.6, 12.8): Grundschaltungen")
    P("=" * 100)
    R1, R2 = 10e3, 20e3
    P("Invertierender Verstärker R_1 = 10 kOhm, R_2 = 20 kOhm:")
    P(f"   ideal A = {-R2/R1:.4f}; mit v_D = 200 000: {a_invertierend(R1, R2):.6f}; mit 50 000: {a_invertierend(R1, R2, VD_MIN):.6f}")
    UE = 1.0
    UA = a_invertierend(R1, R2) * UE
    P(f"   U_E = 1 V: Strom U_E/R_1 = {UE/R1*1e3:.3f} mA, U_A = {UA:.6f} V, Minuseingang (virtuelle Masse) "
      f"{-UA/VD*1e6:.2f} uV; Eingangswiderstand = R_1 = {R1/1e3:.0f} kOhm")
    for R2x in (20e3, 30e3):
        A = R2x / R1
        uhat = 5.0
        P(f"   Sinus 5 V Amplitude, A = -{A:.0f}: ideal {A*uhat:.1f} V Spitze; Grenze ±{UAMAX:.0f} V -> größte unverzerrte "
          f"Eingangsamplitude {UAMAX/A:.3f} V")
        if A * uhat > UAMAX:
            phi = math.degrees(math.asin(UAMAX / (A * uhat)))
            anteil = (180 - 2 * phi) / 180
            phim = (uhat * R2x + (-UAMAX) * R1) / (R1 + R2x)
            P(f"      begrenzt von {phi:.1f}° bis {180-phi:.1f}° jeder Halbwelle ({anteil*100:.1f} % der Zeit); im Scheitel "
              f"liegt der Minuseingang auf {phim:.3f} V statt 0 (U_D = {-phim:.3f} V)")
    P("Nichtinvertierender Verstärker mit denselben Widerständen:")
    P(f"   A = 1 + R_2/R_1 = {1+R2/R1:.4f}; mit v_D = 200 000: {a_nichtinvertierend(R1, R2):.6f}")
    k = R1 / (R1 + R2)
    P(f"   Eingangswiderstand des 741 im Folger-Betrieb etwa R_e (1 + k v_D) = {RE_OPV*(1+k*VD):.3e} Ohm (k = {k:.4f}); "
      f"Ruhestrom {IBIAS*1e9:.0f} nA dominiert")
    P("Impedanzwandler (Spannungsfolger) an einer Quelle 5 V mit 100 kOhm Innenwiderstand:")
    Uq, Rq, Rm = 5.0, 100e3, 1e6
    P(f"   Messgerät 1 MOhm direkt: {Uq*Rm/(Rq+Rm):.4f} V (Fehler {(Rm/(Rq+Rm)-1)*100:.2f} %); mit Folger (741, 80 nA "
      f"Ruhestrom): {Uq-IBIAS*Rq:.4f} V (Fehler {-IBIAS*Rq*1e3:.1f} mV = {-IBIAS*Rq/Uq*100:.2f} %); ideal 5,0000 V")
    P(f"   mit zusätzlich ±1 mV Offset: {Uq-IBIAS*Rq-1e-3:.4f} bis {Uq-IBIAS*Rq+1e-3:.4f} V")
    P("Addierer als 3-Bit-Digital-Analog-Umsetzer: R_4 = 10 kOhm, R_1 = 10 kOhm (höchstes Bit), R_2 = 20 kOhm, R_3 = 40 kOhm, "
      "Eingänge 0 oder 5 V:")
    Rs, R4 = (10e3, 20e3, 40e3), 10e3
    for code in range(8):
        bits = [(code >> 2) & 1, (code >> 1) & 1, code & 1]
        ua = -sum(R4 / r * 5.0 * b for r, b in zip(Rs, bits))
        P(f"   {bits[0]}{bits[1]}{bits[2]}: U_A = {ua:6.3f} V")
    P("Subtrahierer R_1 = R_3 = 10 kOhm, R_2 = R_4 = 100 kOhm (Verstärkung 10):")
    ua = subtrahierer(2.500, 2.505, 10e3, 100e3, 10e3, 100e3)
    P(f"   U_E1 = 2,500 V, U_E2 = 2,505 V: U_A = {ua*1e3:.3f} mV")
    for R4x in (101e3, 100.1e3):
        ua_ = subtrahierer(2.500, 2.505, 10e3, 100e3, 10e3, R4x)
        vgl = subtrahierer(1.0, 1.0, 10e3, 100e3, 10e3, R4x)
        vdiff = (subtrahierer(-0.5, 0.5, 10e3, 100e3, 10e3, R4x))
        P(f"   R_4 = {R4x/1e3:.1f} kOhm: U_A = {ua_*1e3:.3f} mV; Gleichtaktverstärkung {vgl:.5f} (bei 2,5 V: {vgl*2.5*1e3:.2f} mV); "
          f"Differenzverstärkung {vdiff:.4f}; Gleichtaktunterdrückung {abs(vdiff/vgl):.0f} = {20*math.log10(abs(vdiff/vgl)):.1f} dB")
    P("   Skript 12.8 (S. 213), Endformel mit R_3 statt R_1 in einem Nenner gegen richtige Formel, R = 1/2/3/4 kOhm, U_1 = 0, "
      "U_2 = 1 V:")
    r1, r2, r3, r4 = 1e3, 2e3, 3e3, 4e3
    richtig = (r1 + r2) / r1 * r4 / (r3 + r4)
    skript = (r1 + r2) / (r3 + r4) * r4 / r3
    P(f"   richtig {richtig:.4f} V, Skriptformel {skript:.4f} V; bei gleichen Widerständen beide {2*0.5:.1f}")
    r3 = r1
    P(f"   mit R_3 = R_1 = 1 kOhm: richtig {(r1 + r2) / r1 * r4 / (r3 + r4):.4f} V, Skriptformel "
      f"{(r1 + r2) / (r3 + r4) * r4 / r3:.4f} V (gleich)")
    Ri, Ci = 10e3, 100e-9
    tau = Ri * Ci
    P(f"Integrator R = 10 kOhm, C = 100 nF, RC = {tau*1e3:.1f} ms:")
    P(f"   U_E = 1 V: Steigung -{1/tau/1e3:.1f} V/ms, -14 V nach {UAMAX*tau*1e3:.0f} ms")
    for f in (1e3,):
        halb = 1 / (2 * f)
        P(f"   Rechteck ±1 V, {f/1e3:.0f} kHz: je Halbperiode ({halb*1e3:.2f} ms) ändert sich U_A um {1*halb/tau:.2f} V -> "
          f"Dreieck {1*halb/tau:.2f} V Spitze-Spitze")
    P(f"   Offset 1 mV integriert: Steigung {1e-3/tau:.1f} V/s, -14 V nach {UAMAX/(1e-3/tau):.0f} s")
    P(f"   Ruhestrom 80 nA lädt C: {IBIAS/Ci:.2f} V/s; mit 1 MOhm parallel: {IBIAS*1e6*1e3:.0f} mV; Offset mit 1 MOhm parallel: "
      f"(1 + R_p/R) U_os = {(1+1e6/Ri)*1e-3*1e3:.0f} mV")
    for Rp in (1e6,):
        P(f"   Widerstand {Rp/1e6:.0f} MOhm parallel zu C: Gleichspannungsverstärkung -{Rp/Ri:.0f}, Offset 1 mV -> "
          f"{Rp/Ri*1e-3*1e3:.0f} mV; Grenzfrequenz 1/(2 pi R_p C) = {1/(2*math.pi*Rp*Ci):.2f} Hz")
    P(f"Differenzierer R = 10 kOhm, C = 100 nF:")
    steig = 2.0 / 0.5e-3
    P(f"   Dreieck ±1 V, 1 kHz: Steigung ±{steig/1e3:.0f} V/ms -> Rechteck U_A = ∓{tau*steig:.1f} V")
    for f in (100.0, 1e3, 10e3, 100e3):
        P(f"   Sinus {f/1e3:7.1f} kHz: Amplitudenverhältnis 2 pi f R C = {2*math.pi*f*tau:.3f}")
    fn = math.sqrt(WT / tau) / (2 * math.pi)
    Q = math.sqrt(WT * tau)
    P(f"   mit realem OPV (Integratormodell, f_T = 1 MHz): RC s^2 + s + omega_T = 0 -> Resonanz {fn/1e3:.2f} kHz, Güte {Q:.1f}, "
      f"Abklingzeit 2RC = {2*tau*1e3:.1f} ms")
    for f in (1e3, 10e3, fn, 100e3):
        s = 2j * math.pi * f
        H = -s * tau / (1 + s / WT + s * s * tau / WT)
        P(f"      {f/1e3:7.2f} kHz: |H| = {abs(H):8.1f} (ideal {2*math.pi*f*tau:7.1f})")
    # Zeitsimulation: Dreieck ±1 V, 1 kHz, idealer und realer Differenzierer
    dt, tend = 2e-8, 5e-3
    n = int(tend / dt)
    um, ua = 0.0, 0.0
    amin, amax = 0.0, 0.0
    for i in range(n):
        tt = i * dt
        ph = (tt * 1e3) % 1.0
        due = 4e3 if ph < 0.5 else -4e3          # Steigung des Dreiecks in V/s (±4 V/ms)
        dua = -WT * um
        dum = due - (um - ua) / tau
        ua += dua * dt
        um += dum * dt
        if tt > 1e-3:
            amin, amax = min(amin, ua), max(amax, ua)
    P(f"      Dreieck ±1 V, 1 kHz, Zeitsimulation 1–5 ms: Ausgang zwischen {amin:.1f} V und {amax:.1f} V (ideal ∓4 V)")
    for Rs in (1e3,):
        tau2 = Rs * Ci
        zeta = (1 / tau + WT * tau2 / tau) / (2 * math.sqrt(WT / tau))
        P(f"   mit {Rs/1e3:.0f} kOhm in Reihe zu C: Dämpfungsgrad etwa {zeta:.2f} (statt {1/(2*Q):.4f}); Verstärkung oberhalb "
          f"1/(2 pi R_s C) = {1/(2*math.pi*tau2)/1e3:.2f} kHz auf R/R_s = {Ri/Rs:.0f} begrenzt")
    P(f"Logarithmierer R = 10 kOhm, Beispieldiode I_S = {IS_DIODE:.4e} A (ideal):")
    Rl = 10e3
    for ue in (0.01, 0.1, 1.0, 10.0):
        I = ue / Rl
        ua = -UT * math.log(I / (Rl * 0 + IS_DIODE))
        ureal = spannung_real(I)
        P(f"   U_E = {ue:6.2f} V: I = {I*1e6:9.3f} uA, U_A = {ua*1e3:8.2f} mV (reale Beispieldiode mit Rekombination und "
          f"Bahnwiderstand: {-ureal*1e3:8.2f} mV, Abweichung {(-ureal-ua)*1e3:+.2f} mV)")
    P(f"   je Dekade am Eingang: {UT*math.log(10)*1e3:.2f} mV am Ausgang")
    for TK in (310.0,):
        UTT = kB * TK / e
        P(f"   bei {TK:.0f} K: {UTT*math.log(10)*1e3:.2f} mV je Dekade (statt {UT*math.log(10)*1e3:.2f}), U_T um "
          f"{(TK/T-1)*100:.1f} % größer")
        for ue in (0.01, 0.1, 1.0, 10.0):
            I = ue / Rl
            ua300 = -UT * math.log(I / IS_DIODE)
            uaT = -UTT * math.log(I / IS_von_T(TK))
            dek = (uaT - ua300) / (UT * math.log(10))
            P(f"   U_E = {ue:6.2f} V bei {TK:.0f} K: U_A = {uaT*1e3:.2f} mV statt {ua300*1e3:.2f} mV ({(uaT-ua300)*1e3:+.2f} mV = "
              f"{dek:+.3f} Dekaden, als wäre der Eingang {10**(dek):.2f}-mal kleiner)")
    P(f"Exponentialfunktion R = 10 kOhm, Beispieldiode:")
    for ue in (0.40, 0.45, 0.50, 0.55, 0.60):
        P(f"   U_E = {ue:.2f} V: U_A = {-Rl*IS_DIODE*math.exp(ue/UT):.5f} V")
    P(f"   Grenze 14 V erreicht bei U_E = U_T ln(14 V/(R I_S)) = {UT*math.log(UAMAX/(Rl*IS_DIODE)):.4f} V; "
      f"R I_S = {Rl*IS_DIODE*1e9:.4f} nV; Strom 1 uA gegen I_S: Faktor {1e-6/IS_DIODE:.3e}")
    P(f"Multiplizierer nach Skript Bild 12.18 mit R_L = 10 kOhm: U_A = -U_X U_Y/(R_L I_S), Faktor 1/(R_L I_S) = "
      f"{1/(Rl*IS_DIODE):.3e} 1/V")
    P(f"   U_X = U_Y = 1 mV: U_A = {-(1e-3*1e-3)/(Rl*IS_DIODE):.1f} V (unmöglich); ±14 V erreichbar mit U_X = U_Y = "
      f"{math.sqrt(UAMAX*Rl*IS_DIODE)*1e6:.1f} uV")
    P(f"   mit Referenz 10 V (dritter Logarithmierer abgezogen): U_A = -U_X U_Y/10 V, z. B. 2 V und 3 V -> {-2*3/10:.2f} V")
    P("Transimpedanzverstärker R = 100 kOhm:")
    for Ie in (1e-9, 1e-6, 10e-6):
        P(f"   I_e = {Ie:.0e} A: U_a = {-Ie*100e3*1e3:.3f} mV")
    P(f"   Dunkelstrom der Fotodiode bei 0 V (ideal): I_S (exp(0) - 1) = 0; bei -5 V wären es bis zu -I_S bzw. der "
      f"Generationsstrom (Beispieldiode einige 10 pA)")
    P("NIC: R = 10 kOhm (beide), R_2 = 10 kOhm -> Eingangswiderstand -10 kOhm; reale Stromquelle 1 mA mit R_q = 10 kOhm:")
    R, Rq2, I0 = 10e3, 10e3, 1e-3
    for RL in (1e3, 2e3, 5e3):
        ohne = I0 * Rq2 / (Rq2 + RL)
        U1 = I0 * RL
        I2 = U1 / Rq2
        Va = U1 + R * I2
        rp = Rq2 * RL / (Rq2 + RL)
        kp, km = rp / (R + rp), Rq2 / (R + Rq2)
        P(f"   Last {RL/1e3:.0f} kOhm: ohne NIC {ohne*1e3:.4f} mA, mit NIC {I0*1e3:.4f} mA; U_1 = {U1:.2f} V, OPV-Ausgang "
          f"{Va:.2f} V; Rückkopplung plus {kp:.4f}, minus {km:.4f} -> {'stabil' if km > kp else 'instabil'}")
    P(f"   ohne Last: plus {Rq2/(R+Rq2):.4f}, minus {Rq2/(R+Rq2):.4f} -> Grenzfall")
    P("Kaskade zweier invertierender Verstärker R_1 = 10 kOhm, R_2 = 100 kOhm, R_3 = 10 kOhm, R_4 = 50 kOhm:")
    A1, A2 = -100e3 / 10e3, -50e3 / 10e3
    P(f"   A = ({A1:.0f}) · ({A2:.0f}) = {A1*A2:.0f}; U_E = 0,2 V -> Zwischenknoten {A1*0.2:.1f} V, U_A {A1*A2*0.2:.1f} V; "
      f"U_E = 0,3 V -> OP2 bräuchte {A1*A2*0.3:.1f} V, begrenzt auf {UAMAX:.0f} V")


# ------------------------------------------------------------------ Thema 03: der reale OPV
# weitere Datenblattwerte: TI LM741 (SNOSC25D), ±15 V, 25 °C; Ausgangswiderstand aus dem TI-Datenblatt des uA741
# (Ausgabe 2018, typ. 75 Ohm); Thermoelement Typ K: 4,096 mV bei 100 °C gegen 0 °C (NIST ITS-90)
UOS_MAX = 5e-3                    # Offsetspannung max.
UOS_ABGLEICH = 15e-3              # Abgleichbereich ±15 mV (Datenblatt: bei ±20 V)
IOS, IOS_MAX = 20e-9, 200e-9      # Offsetstrom typ./max.
IBIAS_MAX = 500e-9                # Eingangsruhestrom max.
RE_MIN = 0.3e6                    # Eingangswiderstand min.
RA = 75.0                         # Ausgangswiderstand ohne Rückkopplung
CMRR_DB, CMRR_DB_MIN = 95.0, 80.0
SVRR_DB, SVRR_DB_MIN = 96.0, 86.0
UICR, UICR_MIN = 13.0, 12.0       # Eingangsspannungsbereich (Gleichtakt) typ./min.
UAMAX_2K = 13.0                   # Ausgangshub an 2 kOhm
ISC = 25e-3                       # Kurzschlussstrom
TR_FOLGER, US_FOLGER = 0.3e-6, 0.05   # Spannungsfolger: Anstiegszeit, Überschwingen
S_TYP_K = 4.096e-3 / 100.0        # Thermoelement Typ K, mittlere Empfindlichkeit 0–100 °C in V/K
IC_EINGANG = 10e-6                # Kollektorstrom je Eingangstransistor des 741, rund (Sedra/Smith: 9,5 uA)


def lin(d):
    """dB-Wert eines Spannungsverhältnisses in das Verhältnis."""
    return 10 ** (d / 20)


def a_real(a_ideal, k, f=0.0, vD=VD):
    """Verstärkung mit endlicher, frequenzabhängiger Leerlaufverstärkung (Einpolmodell): A_ideal/(1 + 1/(k v_D(jf)))."""
    vdj = vD / complex(1, f / (FT / vD))
    return a_ideal / (1 + 1 / (k * vdj))


def zweipol_sprung(k, f2, sprung, t_end=4e-6, dt=1e-10):
    """Sprungantwort mit zweiter Verzögerung f2 (Modell): tau1 dx/dt = v_D U_D - x, tau2 dU_A/dt = x - U_A."""
    tau1, tau2 = VD / WT, 1 / (2 * math.pi * f2)
    x = ua = 0.0
    werte = []
    for _ in range(int(round(t_end / dt)) + 1):
        ud = sprung - k * ua
        x += (VD * ud - x) / tau1 * dt
        ua += (x - ua) / tau2 * dt
        werte.append(ua)
    return np.array(werte)


def ua_ruhestrom(ibp, ibm, R1, R2, R3):
    """Ausgangsspannung eines Verstärkers mit R_1 (Minuseingang–Masse bzw. –Quelle 0 V), R_2 (Rückkopplung), R_3
    (Pluseingang–Masse) allein durch die Ruheströme I_B+ und I_B- (in die Eingänge hinein gezählt)."""
    return R2 * ibm - ibp * R3 * (1 + R2 / R1)


def bericht_real():
    from zahlen_halbleiter import _bisekt
    from zahlen_transistor import UA as UA_EARLY
    P("=" * 100)
    P("THEMA 03 (Kap. 12.7): Der reale Operationsverstärker")
    P("=" * 100)
    P(f"Beispiel-OPV (LM741, ±15 V): v_D {VD:.0f} (min {VD_MIN:.0f}); U_os {UOS*1e3:.0f} mV (max {UOS_MAX*1e3:.0f} mV, "
      f"Abgleich ±{UOS_ABGLEICH*1e3:.0f} mV); I_B {IBIAS*1e9:.0f} nA (max {IBIAS_MAX*1e9:.0f} nA); I_os {IOS*1e9:.0f} nA "
      f"(max {IOS_MAX*1e9:.0f} nA); R_e {RE_OPV/1e6:.0f} MOhm (min {RE_MIN/1e6:.1f}); R_a {RA:.0f} Ohm; Ausgang ±{UAMAX:.0f} V "
      f"an 10 kOhm, ±{UAMAX_2K:.0f} V an 2 kOhm; I_K {ISC*1e3:.0f} mA; Eingangsbereich ±{UICR:.0f} V (min ±{UICR_MIN:.0f} V); "
      f"CMRR {CMRR_DB:.0f} dB (min {CMRR_DB_MIN:.0f}); SVRR {SVRR_DB:.0f} dB (min {SVRR_DB_MIN:.0f}); f_T {FT/1e6:.0f} MHz; "
      f"SR {SR/1e6:.1f} V/us; Folger: Anstiegszeit {TR_FOLGER*1e6:.1f} us, Überschwingen {US_FOLGER*100:.0f} %")

    P("1) Verstärkungsfehler: A = A_ideal/(1 + 1/(k v_D)), k = R_1/(R_1 + R_2) bei beiden Schaltungen")
    faelle = (("invertierend 10k/20k", 10e3, 20e3, True), ("nichtinvertierend 10k/90k", 10e3, 90e3, False),
              ("invertierend 1k/100k", 1e3, 100e3, True), ("nichtinvertierend 1k/100k", 1e3, 100e3, False),
              ("nichtinvertierend 100 Ohm/100k", 100.0, 100e3, False))
    for name, R1, R2, inv in faelle:
        k = R1 / (R1 + R2)
        aid = -R2 / R1 if inv else 1 + R2 / R1
        for vd in (VD, VD_MIN):
            a = a_real(aid, k, vD=vd).real
            P(f"   {name}: k = {k:.6f} (1/k = {1/k:.0f}), A_ideal = {aid:.0f}, v_D = {vd:.0f}: k v_D = {k*vd:.1f}, "
              f"A = {a:.5f}, Fehler {(a/aid-1)*100:.4f} %")
    P(f"   Kontrolle mit Thema 02: a_invertierend(10k, 20k) = {a_invertierend(10e3, 20e3):.6f}")
    a_typ, a_min = a_real(-100, 1 / 101).real, a_real(-100, 1 / 101, vD=VD_MIN).real
    P(f"   A = -100: v_D 200 000 -> 50 000 (-75 %) ändert A um {(a_min/a_typ-1)*100:.3f} %; Verhältnis "
      f"{0.75/(1-a_min/a_typ):.0f}")

    P("2) Ausgangswiderstand mit Gegenkopplung, R_a/(1 + k v_D(jf)):")
    for k in (1.0, 0.1, 1 / 101):
        P(f"   k = {k:.4f}: {RA/(1+k*VD)*1e3:.3f} mOhm")
    il = 5.0 / 1e3
    P(f"   5 V an 1 kOhm (5 mA): ohne Rückkopplung fielen {il*RA:.3f} V an R_a ab ({RA/(RA+1e3)*100:.1f} %), mit k = 0,1 "
      f"{il*RA/(1+0.1*VD)*1e6:.1f} uV")
    for f in (100.0, 1e3, 10e3, 100e3):
        vdj = VD / complex(1, f / (FT / VD))
        P(f"   k = 0,1, f = {f/1e3:g} kHz: |Z_a| = {RA/abs(1+0.1*vdj):.4f} Ohm")

    P("3) Eingangswiderstand des nichtinvertierenden Verstärkers, k = 0,1:")
    rein = RE_OPV * (1 + 0.1 * VD)
    P(f"   R_e (1 + k v_D) = {rein/1e9:.1f} GOhm; bei 1 V Eingang fließen {1/rein*1e12:.1f} pA durch R_e, "
      f"der Ruhestrom ist {IBIAS/(1/rein):.0f}-mal größer")

    P("4) Offsetspannung:")
    for r in (1.01, 1.04):
        P(f"   I_S-Verhältnis {r:.2f}: Delta U_BE = U_T ln(r) = {UT*math.log(r)*1e3:.3f} mV")
    P(f"   1 mV verlangt ein I_S-Verhältnis von {math.exp(1e-3/UT):.4f}")
    ube1, ube2 = UT * math.log(0.5e-3 / IS), UT * math.log(0.5e-3 / (1.04 * IS))
    P(f"   Lupe für Abbildung 03-offset: bei 0,5 mA U_BE = {ube1:.4f} V (I_S = 1e-14 A) und {ube2:.4f} V (4 % größeres I_S); "
      f"bei 1 uA {UT*math.log(1e-6/IS):.3f} V, bei 10 mA {UT*math.log(10e-3/IS):.3f} V")
    P(f"   Drift, wenn der Offset aus ungleichen I_S stammt: U_os/T = {UOS/T*1e6:.2f} uV/K, je 10 K {UOS/T*10*1e6:.1f} uV; "
      f"LM741A: höchstens 15 uV/K")
    for name, R1, R2 in (("Umkehrer 10k/10k", 10e3, 10e3), ("invertierend 10k/20k", 10e3, 20e3),
                         ("invertierend 1k/100k", 1e3, 100e3), ("nichtinvertierend 1k/100k", 1e3, 100e3)):
        g = 1 + R2 / R1
        P(f"   {name}: Rauschverstärkung {g:.0f}; U_A = {g*UOS*1e3:.1f} mV (typ), {g*UOS_MAX*1e3:.0f} mV (max)")
    A = 101
    P("   Thermoelement Typ K an nichtinvertierendem Verstärker 1 kOhm/100 kOhm (A = 101):")
    P(f"      Empfindlichkeit {S_TYP_K*1e6:.2f} uV/K; 100 °C: {S_TYP_K*100*1e3:.3f} mV -> U_A {A*S_TYP_K*100*1e3:.1f} mV; "
      f"am Ausgang {A*S_TYP_K*1e3:.3f} mV/K")
    P(f"      Offset 1 mV -> {A*UOS*1e3:.0f} mV am Ausgang = {UOS/S_TYP_K:.1f} K; 5 mV -> {UOS_MAX/S_TYP_K:.0f} K")
    P(f"      Drift {UOS/T*1e6:.2f} uV/K -> {UOS/T/S_TYP_K:.3f} K Messfehler je K Umgebung, {UOS/T/S_TYP_K*10:.2f} K je 10 K")
    P(f"      Ruhestrom: I_B- R_2 = {IBIAS*100e3*1e3:.1f} mV am Ausgang = {IBIAS*100e3/A*1e6:.1f} uV am Eingang = "
      f"{IBIAS*100e3/A/S_TYP_K:.2f} K")
    kk = 1 / 101
    a = a_real(101, kk).real
    P(f"      Verstärkungsfehler {(a/101-1)*100:.4f} % -> bei 100 °C {abs(a/101-1)*100:.4f} K")
    P(f"      Bandbreite k f_T = {kk*FT/1e3:.2f} kHz")

    P("5) Eingangsruheströme:")
    P(f"   Basisstrom: {IC_EINGANG*1e6:.0f} uA Kollektorstrom / {IBIAS*1e9:.0f} nA -> B = {IC_EINGANG/IBIAS:.0f}")
    R1, R2 = 100e3, 1e6
    R3 = R1 * R2 / (R1 + R2)
    P(f"   invertierend R_1 = 100 kOhm, R_2 = 1 MOhm (A = -10): R_3 = R_1||R_2 = {R3/1e3:.2f} kOhm")
    P(f"      ohne R_3, I_B- = 80 nA: U_A = {ua_ruhestrom(IBIAS, IBIAS, R1, R2, 0.0)*1e3:.1f} mV")
    P(f"      mit R_3, beide 80 nA: U_A = {ua_ruhestrom(IBIAS, IBIAS, R1, R2, R3)*1e6:.3f} uV; Pluseingang "
      f"{-IBIAS*R3*1e3:.3f} mV; Strom durch R_1 {IBIAS*R3/R1*1e9:.2f} nA, durch R_2 {(IBIAS-IBIAS*R3/R1)*1e9:.2f} nA")
    P(f"      I_B+ = 90 nA, I_B- = 70 nA: ohne R_3 {ua_ruhestrom(90e-9, 70e-9, R1, R2, 0.0)*1e3:.1f} mV, mit R_3 "
      f"{ua_ruhestrom(90e-9, 70e-9, R1, R2, R3)*1e3:.1f} mV (= -I_os R_2)")
    P(f"      Höchstwerte: I_B 500 nA -> {IBIAS_MAX*R2:.2f} V; I_os 200 nA -> {IOS_MAX*R2:.2f} V")
    P(f"      Offset 1 mV mal Rauschverstärkung 11: {11*UOS*1e3:.0f} mV")
    P(f"   invertierend 10k/20k: I_B R_2 = {IBIAS*20e3*1e3:.2f} mV gegen Offset mal 3 = {3*UOS*1e3:.0f} mV")
    P(f"   invertierend 10k/100k: ohne R_3 {IBIAS*100e3*1e3:.1f} mV, mit R_3 {IOS*100e3*1e3:.1f} mV")
    P(f"   Integrator 10 kOhm/100 nF (Thema 02): Ruhestrom lädt C mit {IBIAS/100e-9:.2f} V/s")

    P("6) Gleichtaktunterdrückung:")
    for d in (60.0, 80.0, CMRR_DB, 120.0):
        P(f"   {d:.0f} dB: CMRR = {lin(d):.0f}, Kehrwert {1/lin(d):.2e}")
    P(f"   Skript S. 212: 120 dB entspricht {1/lin(120):.0e}, nicht 1e-4; 1e-4 wären {20*math.log10(1e4):.0f} dB")
    P(f"   Gleichtaktverstärkung v_Gl = v_D/CMRR = {VD/lin(CMRR_DB):.2f} (typ), {VD/lin(CMRR_DB_MIN):.1f} (80 dB)")
    for ugl in (1.0, 10.0):
        P(f"   Gleichtakt {ugl:.0f} V wirkt wie U_D = {ugl/lin(CMRR_DB)*1e6:.1f} uV (typ), {ugl/lin(CMRR_DB_MIN)*1e6:.0f} uV "
          f"(80 dB)")
    P(f"   nichtinvertierend A = 10 mit 1 V Eingang: {1/lin(CMRR_DB)*10*1e6:.0f} uV am Ausgang gegen Offset mal 10 = "
      f"{10*UOS*1e3:.0f} mV; als Verstärkungsfehler {1/lin(CMRR_DB)*1e6:.1f} ppm")
    uce3 = diffpaar(0.0, 0.0)["uE"] - UEE_D
    r0 = (UA_EARLY + uce3) / I0_D
    di = 1.0 / r0
    du = RC_D * di / 2
    vgl_d = 0.01 * du
    P(f"   Differenzverstärker aus Thema 01: Q3 mit U_CE = {uce3:.2f} V, Early-Spannung {UA_EARLY:.0f} V -> "
      f"r_CE = {r0/1e3:.1f} kOhm; 1 V Gleichtakt: Fußpunktstrom +{di*1e6:.2f} uA, je Kollektor {di/2*1e6:.2f} uA, "
      f"Kollektorpotentiale je {du*1e3:.1f} mV")
    P(f"      1 % Unterschied der R_C: {vgl_d*1e3:.3f} mV je V zwischen den Kollektoren; mit v_u = 193: CMRR = "
      f"{193/vgl_d:.0f} = {20*math.log10(193/vgl_d):.1f} dB")
    P(f"      Ausgang an einem Kollektor: v_Gl = {du:.4f}, v_u/2 = 96,5 -> CMRR {96.5/du:.0f} = "
      f"{20*math.log10(96.5/du):.1f} dB")
    P(f"   Subtrahierer mit 1 % Widerstandsfehler (Thema 02): 61 dB, der OPV selbst {CMRR_DB:.0f} dB")

    P("7) Betriebsspannungsunterdrückung:")
    P(f"   {SVRR_DB:.0f} dB -> {1/lin(SVRR_DB)*1e6:.1f} uV/V; {SVRR_DB_MIN:.0f} dB -> {1/lin(SVRR_DB_MIN)*1e6:.1f} uV/V")
    P(f"   Versorgung sinkt langsam um 100 mV (z. B. Batterie): Offset {0.1/lin(SVRR_DB)*1e6:.2f} uV (typ), mal 101 "
      f"{101*0.1/lin(SVRR_DB)*1e6:.0f} uV am Ausgang")
    svrr100 = SVRR_DB - 20 * math.log10(math.sqrt(1 + (100 / (FT / VD)) ** 2))
    P(f"   nur Abschätzung (MT-043: Abfall ab der Eckfrequenz der Leerlaufverstärkung): bei 100 Hz {svrr100:.1f} dB, "
      f"100 mV Brummen wie {0.1/lin(svrr100)*1e6:.0f} uV am Eingang, mal 101 {101*0.1/lin(svrr100)*1e3:.1f} mV; "
      "im Artikel nur qualitativ")

    P("8) Frequenzgang (Einpolmodell):")
    f1 = FT / VD
    P(f"   erste Eckfrequenz f_T/v_D = {f1:.1f} Hz; |v_D|: " + ", ".join(
        f"{f:g} Hz {abs(VD/complex(1, f/f1)):.0f}" for f in (1.0, 5.0, 100.0, 1e3, 10e3, 100e3, 1e6)))
    for k in (1.0, 0.5, 1 / 3, 0.1, 1 / 11, 1 / 101, 1 / 1001):
        fg = f1 * (1 + k * VD)
        P(f"   k = {k:.5f} (1/k = {1/k:.0f}): f_g = {fg/1e3:.3f} kHz (k f_T = {k*FT/1e3:.3f} kHz), tau = "
          f"{1/(2*math.pi*fg)*1e6:.3f} us, Anstiegszeit 2,2 tau = {2.2/(2*math.pi*fg)*1e6:.3f} us")
    for f in (5e3, 10e3, 20e3, 100e3):
        a = a_real(10.0, 0.1, f)
        P(f"   A = 10 (k = 0,1) bei {f/1e3:g} kHz: |A| = {abs(a):.4f}, Phase {math.degrees(math.atan2(a.imag, a.real)):.1f} Grad")
    a1 = a_real(-100.0, 1 / 101, 20e3)
    a2 = a_real(-10.0, 1 / 11, 20e3)
    fg1, fg2 = f1 * (1 + VD / 101), f1 * (1 + VD / 11)
    P(f"   Audio, A = -100: einstufig f_g = {fg1/1e3:.2f} kHz, bei 20 kHz |A| = {abs(a1):.1f}; zweistufig je -10: f_g je "
      f"{fg2/1e3:.2f} kHz, gesamt {fg2*math.sqrt(math.sqrt(2)-1)/1e3:.1f} kHz, bei 20 kHz |A| = {abs(a2)**2:.1f}")
    P(f"      zwei gleiche Stufen: je Stufe auf 2^(-1/4) = {2**-0.25:.4f} gefallen bei f/f_g = sqrt(sqrt(2) - 1) = "
      f"{math.sqrt(math.sqrt(2)-1):.4f}; Bandbreite je Stufe {fg2/fg1:.2f}-mal so groß wie einstufig")
    P(f"   Rauschverstärkung 101 mit 23 nV/sqrt(Hz): {EN*101*1e6:.2f} uV/sqrt(Hz) am Ausgang, Rauschbandbreite "
      f"pi/2 f_g = {math.pi/2*fg1/1e3:.1f} kHz -> {EN*101*math.sqrt(math.pi/2*fg1)*1e3:.2f} mV eff.")

    P("9) Überschwingen als Spannungsfolger (Datenblatt 5 %) mit einer zweiten Verzögerung (Modell):")
    ln_us = math.log(US_FOLGER)
    zeta = -ln_us / math.sqrt(math.pi**2 + ln_us**2)
    f2 = 4 * zeta**2 * FT
    P(f"   Dämpfungsgrad aus 5 %: {zeta:.3f}; zweite Verzögerung f_2 = 4 zeta^2 f_T = {f2/1e6:.3f} MHz")
    fc = _bisekt(lambda x: 1 - FT / (x * math.sqrt(1 + (x / f2) ** 2)), 1e4, 1e7)
    P(f"   k = 1: Schleifenverstärkung 1 bei {fc/1e6:.3f} MHz; Phasenreserve 90 - atan(f_c/f_2) = "
      f"{90 - math.degrees(math.atan(fc/f2)):.1f} Grad")
    for k in (1.0, 0.5, 0.1):
        ua = zweipol_sprung(k, f2, 20e-3 * k, t_end=8e-6 if k < 1 else 4e-6)
        end = 20e-3 * a_real(1.0, k).real if k == 1.0 else 20e-3 * k * a_real(1 / k, k).real
        P(f"   k = {k}: zeta = {0.5*math.sqrt(f2/(k*FT)):.3f}, Endwert {end*1e3:.4f} mV, Simulation: Überschwingen "
          f"{max(0.0, (ua.max()/end-1)*100):.2f} %")
    ua = zweipol_sprung(1.0, f2, 20e-3)
    t10 = np.argmax(ua >= 0.1 * 20e-3) * 1e-10
    t90 = np.argmax(ua >= 0.9 * 20e-3) * 1e-10
    P(f"   k = 1: Anstiegszeit 10–90 % im Modell {(t90-t10)*1e6:.3f} us (Datenblatt 0,3 us, Einpolmodell "
      f"{2.2/WT*1e6:.3f} us)")

    P("10) Anstiegsgeschwindigkeit 0,5 V/us:")
    for u in (1.0, 5.0, 10.0, 14.0):
        P(f"   Amplitude {u:g} V: Leistungsbandbreite SR/(2 pi U) = {SR/(2*math.pi*u)/1e3:.2f} kHz")
    P(f"   Übergang Bandbreite/Anstieg bei k = 0,1: U = SR/(2 pi k f_T) = {SR/(2*math.pi*0.1*FT):.3f} V")
    P(f"   U_D, bei der die Eingangsstufe ganz umschaltet: SR/omega_T = {SR/WT*1e3:.1f} mV")
    for ue_amp, f in ((1.0, 20e3), (1.0, 5e3), (0.05, 20e3)):
        def ue_func(t, a=ue_amp, fr=f):
            return a * math.sin(2 * math.pi * fr * t)
        _, out = sim("gegen", ue_func, 8 / f, dt=2e-9, k=0.1, sr=True, grenzen=True, aufzeichnen=5)
        arr = np.array(out)
        letzte = arr[arr[:, 0] >= 6 / f]
        P(f"   A = 10, Eingang {ue_amp:g} V bei {f/1e3:g} kHz: verlangt {10*ue_amp:g} V, Steigung bis "
          f"{2*math.pi*f*10*ue_amp/1e6:.3f} V/us; Ausgang {letzte[:, 2].max():.3f} V / {letzte[:, 2].min():.3f} V")
    P(f"   Dreieck bei 20 kHz: Amplitude SR/(4 f) = {SR/(4*20e3):.3f} V; Viertelperiode {1/(4*20e3)*1e6:.1f} us")
    P(f"   bei 20 kHz beginnt die Verzerrung ab U_A = SR/(2 pi 20 kHz) = {SR/(2*math.pi*20e3):.2f} V, also "
      f"{SR/(2*math.pi*20e3)/10:.3f} V am Eingang (Rauschverstärkung 10)")

    P("11) Aussteuergrenzen:")
    P(f"   Abstand zur Versorgung: {UB-UAMAX:.0f} V an 10 kOhm, {UB-UAMAX_2K:.0f} V an 2 kOhm (Laststrom "
      f"{UAMAX_2K/2e3*1e3:.1f} mA); Kurzschlussstrom {ISC*1e3:.0f} mA -> an 200 Ohm höchstens {ISC*200:.1f} V")
    P(f"   Eingangsbereich ±{UICR:.0f} V: Abstand {UB-UICR:.0f} V (garantiert ±{UICR_MIN:.0f} V, {UB-UICR_MIN:.0f} V)")


if __name__ == "__main__":
    bericht_rauschen()
    bericht_differenz()
    bericht_opv()
    bericht_rueckkopplung()
    bericht_schmitt()
    bericht_grundschaltungen()
    bericht_real()
