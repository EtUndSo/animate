"""Zahlenwerk für Schaltungstechnik, Netzwerkanalyse (Stil 3). Thema 1: Nichtlineare Bauelemente, Arbeitspunkt und
Linearisierung. Spätere Themen des Kapitels ergänzen dieses Skript.

Eigenes Beispielsystem (keine Aufgabe aus Skript oder Übung):
- MOS-Diode (n-Kanal-MOSFET mit verbundenem Gate und Drain), I = k (U - U_th)^2 für U >= U_th, sonst 0,
  k = 1 mA/V^2, U_th = 0,5 V (Größenordnung eines integrierten NMOS mit W/L = 10 und mu_n C_ox = 200 µA/V^2);
- reale Stromquelle I_q = 0,5 mA mit Innenleitwert G_q = 0,25 mS (R_q = 4 kOhm) als Treiber;
- pn-Diode wie im ET1-Zahlenwerk (notizen/get1/zahlen_halbleiter.py): I_S = 1,46e-14 A, U_T = 25,85 mV, Sperrschicht
  C_j0 = 24,10 pF (im Artikel C_S0, weil j dort die Steuergrößen zählt), U_Diff = 0,714 V, Lebensdauer 1 µs;
  Grundschaltung 5 V und 1 kOhm;
- Spule mit Eisenkern als Modell: Psi(I) = Psi_max tanh(L_0 I/Psi_max), L_0 = 10 mH, Psi_max = 10 mVs
  (gleichwertig L_0 I_s tanh(I/I_s) mit I_s = 1 A; im Artikel mit Psi_max, weil I_S der Sättigungssperrstrom ist).
Aufruf: python -I zahlen_netzwerkanalyse.py > zahlen_netzwerkanalyse.txt
"""
import math
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
P = print


def kopf(t):
    P()
    P("=" * 100)
    P(t)
    P("=" * 100)


# ------------------------------------------------------------------ Beispielsystem
k, Uth = 1e-3, 0.5            # A/V^2, V
Iq, Gq = 0.5e-3, 0.25e-3      # A, S
Rq = 1 / Gq
kB, e = 1.380649e-23, 1.602176634e-19
UT = kB * 300 / e             # 25,85 mV
IS = 1.46e-14                 # A, Beispieldiode ET1


def i_mos(u):
    return k * (u - Uth) ** 2 if u >= Uth else 0.0


def g_mos(u):
    return 2 * k * (u - Uth) if u >= Uth else 0.0


def i_dio(u):
    return IS * (math.exp(u / UT) - 1)


def g_dio(u):
    return IS / UT * math.exp(u / UT)


# ------------------------------------------------------------------ A. Arbeitspunkt
kopf("A. Arbeitspunkt der MOS-Diode an der realen Stromquelle")
# k (U-Uth)^2 + Gq U - Iq = 0  ->  k U^2 + (Gq - 2 k Uth) U + (k Uth^2 - Iq) = 0
a_, b_, c_ = k, Gq - 2 * k * Uth, k * Uth ** 2 - Iq
UA = (-b_ + math.sqrt(b_ * b_ - 4 * a_ * c_)) / (2 * a_)
U2 = (-b_ - math.sqrt(b_ * b_ - 4 * a_ * c_)) / (2 * a_)
IA = i_mos(UA)
gA = g_mos(UA)
P(f"Quelle: I_q = {Iq*1e3:.2f} mA, G_q = {Gq*1e3:.3f} mS (R_q = {Rq/1e3:.1f} kOhm); Leerlaufspannung I_q/G_q = {Iq/Gq:.2f} V")
P(f"Quadratische Gleichung: Wurzeln {UA:.6f} V und {U2:.6f} V (die zweite liegt unter U_th und entfällt)")
P(f"Arbeitspunkt U_A = {UA:.4f} V, I_A = {IA*1e3:.4f} mA, Strom durch G_q = {Gq*UA*1e3:.4f} mA (Summe {(IA+Gq*UA)*1e3:.4f} mA)")
P(f"g(U_A) = 2 k (U_A - U_th) = {gA*1e3:.4f} mS -> r = 1/g = {1/gA:.1f} Ohm; statischer Wert U_A/I_A = {UA/IA:.1f} Ohm"
  f" (Verhältnis {UA/IA*gA:.2f})")
P(f"Kontrolle g = 2 I_A/(U_A - U_th) = {2*IA/(UA-Uth)*1e3:.4f} mS")
for u in (0.6, 0.75, 1.0, 1.25, 1.5):
    P(f"  U = {u:.2f} V: I = {i_mos(u)*1e3:.4f} mA, g = {g_mos(u)*1e3:.3f} mS, statisch U/I = {u/i_mos(u)/1e3:.2f} kOhm")
P(f"Quellengerade: I = I_q - G_q U, Punkte (0 V; {Iq*1e3:.2f} mA) und ({Iq/Gq:.1f} V; 0 mA)")

# ------------------------------------------------------------------ B. Oberwellen der MOS-Diode
kopf("B. Sinus am Arbeitspunkt: Gleichanteil, Grundwelle, 2. Harmonische (MOS-Diode, U_0 = U_A)")
U0 = UA
du = U0 - Uth
for uh in (0.010, 0.050, 0.100, 0.250, 0.400, 0.500):
    grund = 2 * k * du * uh
    harm2 = k * uh ** 2 / 2
    shift = k * uh ** 2 / 2
    P(f"  û = {uh*1e3:5.0f} mV: Grundwelle {grund*1e6:8.3f} µA, 2. Harmonische {harm2*1e6:7.3f} µA"
      f" ({harm2/grund*100:5.2f} % = û/(4(U_0-U_th)) = {uh/(4*du)*100:5.2f} %), Gleichanteil {(IA+shift)*1e6:8.3f} µA"
      f" (+{shift/IA*100:.2f} %)")
# numerische Probe mit FFT, auch jenseits der Sperrgrenze
N = 4096
t = np.arange(N) / N
for uh in (0.050, 0.400, 0.700):
    uu = U0 + uh * np.sin(2 * np.pi * t)
    ii = np.where(uu >= Uth, k * (uu - Uth) ** 2, 0.0)
    F = np.fft.rfft(ii) / N
    dc, a1, a2, a3 = F[0].real, 2 * abs(F[1]), 2 * abs(F[2]), 2 * abs(F[3])
    P(f"  FFT û = {uh*1e3:.0f} mV: DC {dc*1e6:.3f} µA, |1.| {a1*1e6:.3f} µA, |2.| {a2*1e6:.3f} µA, |3.| {a3*1e6:.3f} µA"
      f" (3. Harmonische entsteht erst, wenn die Diode zeitweise sperrt)")

# ------------------------------------------------------------------ C. Exponentielle Diode
kopf("C. pn-Diode (ET1-Beispieldiode): Kennlinie, differentieller Leitwert, Kleinheit des Signals")
for u in (0.3, 0.4, 0.5, 0.6, 0.7):
    P(f"  U = {u:.1f} V: I = {i_dio(u):.3e} A")
P(f"Dekade je U_T ln 10 = {UT*math.log(10)*1e3:.2f} mV; U_T = {UT*1e3:.2f} mV")
Ud = UT * math.log(IA / IS + 1)
P(f"Spannung bei I = {IA*1e3:.2f} mA: {Ud:.4f} V; g = (I + I_S)/U_T = {(IA+IS)/UT*1e3:.3f} mS (r = {UT/(IA+IS):.1f} Ohm)")
P(f"Vergleich bei gleichem Strom 0,25 mA: g_Diode/g_MOS = {(IA/UT)/gA:.2f}; g/I: Diode {1/UT:.1f} 1/V, MOS"
  f" {2/(UA-Uth):.1f} 1/V")
# Oberwellen der e-Funktion: exakt über FFT, Näherung û/(4 U_T)
for uh in (0.001, 0.005, 0.010, 0.026):
    uu = Ud + uh * np.sin(2 * np.pi * t)
    ii = IS * (np.exp(uu / UT) - 1)
    F = np.fft.rfft(ii) / N
    a1, a2 = 2 * abs(F[1]), 2 * abs(F[2])
    P(f"  Diode û = {uh*1e3:.0f} mV: 2./1. Harmonische exakt {a2/a1*100:.2f} %, Näherung û/(4 U_T) = {uh/(4*UT)*100:.2f} %;"
      f" Gleichanteil +{(F[0].real-IA)/IA*100:.3f} %")
P(f"1 % Klirr der Diode bei û = 0,04 U_T = {0.04*UT*1e3:.2f} mV; MOS-Diode im Beispiel bei û = 0,04 (U_A-U_th) ="
  f" {0.04*du*1e3:.0f} mV")

# ------------------------------------------------------------------ D. Newton für die MOS-Diode
kopf("D. Newton-Verfahren für den Arbeitspunkt der MOS-Diode")


def F_mos(u):
    return i_mos(u) + Gq * u - Iq


def newton(u0, Ff, Gf, nmax=60, tol=1e-12, limit=None):
    u, rows = u0, []
    for i in range(nmax):
        f, G = Ff(u), Gf(u)
        du_ = -f / G
        unew = u + du_
        if limit:
            unew = limit(u, unew)
        rows.append((i, u, f, G, unew - u))
        if abs(unew - u) < tol:
            u = unew
            break
        u = unew
    return u, rows


uN, rows = newton(0.0, F_mos, lambda u: g_mos(u) + Gq)
P(" i      U_i in V      F(U_i) in mA     G = g+G_q in mS     ΔU in V        Fehler U_i - U_A in V")
for i, u, f, G, d in rows:
    P(f" {i:2d}  {u:12.9f}  {f*1e3:14.6e}  {G*1e3:12.6f}  {d:14.6e}  {u-UA:14.6e}")
P(f"Lösung {uN:.12f} V")
err = [r[1] - UA for r in rows]
for j in range(2, len(err) - 1):
    if abs(err[j]) > 1e-10:
        P(f"  Verhältnis e_(i+1)/e_i^2 bei i = {j}: {err[j+1]/err[j]**2:.4f} 1/V (Grenzwert F''/(2F') = k/(g+G_q) ="
          f" {k/(gA+Gq):.4f} 1/V)")
P(f"Startwert aus der bei 0 V linearisierten Gleichung: U = I_q/(g(0) + G_q) = {Iq/(g_mos(0)+Gq):.3f} V")
# Fixpunktiteration (Kennlinie nach U aufgelöst) zum Vergleich
u = 2.0
P("Fixpunktiteration U_(i+1) = U_th + sqrt((I_q - G_q U_i)/k) ab 2 V (bei 2 V ist der Quellstrom null, deshalb ab 0 V):")
u = 0.0
for i in range(8):
    unew = Uth + math.sqrt(max(Iq - Gq * u, 0) / k)
    P(f"  i = {i}: U = {u:.6f} V -> {unew:.6f} V, Fehler {unew-UA:+.3e} V")
    u = unew
P(f"Konvergenzfaktor der Fixpunktiteration |dU_neu/dU| = G_q/g(U_A) = {Gq/gA:.3f}")

# ------------------------------------------------------------------ E. Newton für die pn-Diode (Grundschaltung ET1)
kopf("E. Newton-Verfahren für die pn-Diode an 5 V über 1 kOhm (Norton: 5 mA, 1 mS)")
U0q, R = 5.0, 1e3
Iq2, Gq2 = U0q / R, 1 / R


def F_dio(u):
    return i_dio(u) + Gq2 * u - Iq2


def G_dio(u):
    return g_dio(u) + Gq2


uE, rowsE = newton(0.0, F_dio, G_dio, nmax=400)
P(f"Start 0 V: {len(rowsE)} Schritte bis |ΔU| < 1e-12 V, Lösung {uE:.6f} V, I = {i_dio(uE)*1e3:.4f} mA")
for i, u, f, G, d in rowsE[:4]:
    P(f"  i = {i}: U = {u:.6f} V, F = {f:.3e} A, ΔU = {d:+.6f} V")
for i, u, f, G, d in rowsE[-4:]:
    P(f"  i = {i}: U = {u:.6f} V, ΔU = {d:+.3e} V")
P(f"Diodenstrom nach dem ersten Schritt bei {rowsE[1][1]:.3f} V laut Modell: {IS*math.exp(rowsE[1][1]/UT):.3e} A"
  f" (Exponent {rowsE[1][1]/UT:.1f})")
n_bis = sum(1 for r in rowsE if r[1] > 0.75)
P(f"Schritte, solange U über 0,75 V liegt: {n_bis}; typischer Schritt dort ΔU = {rowsE[10][4]*1e3:.2f} mV (U_T = {UT*1e3:.2f} mV)")
uE2, rowsE2 = newton(0.6, F_dio, G_dio, nmax=100)
P(f"Start 0,6 V: {len(rowsE2)} Schritte, Lösung {uE2:.6f} V")
for i, u, f, G, d in rowsE2:
    P(f"  i = {i}: U = {u:.9f} V, F = {f:+.3e} A, Fehler {u-uE:+.3e} V")
Ucrit = UT * math.log(UT / (math.sqrt(2) * IS))


def pnjlim(uold, unew):
    """Spannungsbegrenzung wie in SPICE: oberhalb U_crit wird der Schritt logarithmisch gestaucht."""
    if unew > Ucrit and abs(unew - uold) > 2 * UT:
        if uold > 0:
            arg = 1 + (unew - uold) / UT
            return uold + UT * math.log(arg) if arg > 0 else Ucrit
        return UT * math.log(unew / UT)
    return unew


uE3, rowsE3 = newton(0.0, F_dio, G_dio, nmax=100, limit=pnjlim)
P(f"Mit Spannungsbegrenzung (U_crit = {Ucrit:.3f} V) ab 0 V: {len(rowsE3)} Schritte, Lösung {uE3:.6f} V")
for i, u, f, G, d in rowsE3:
    P(f"  i = {i}: U = {u:.6f} V, ΔU = {d:+.4e} V")

# ------------------------------------------------------------------ F. Differentielle Kapazität
kopf("F. Differentielle Kapazität: Sperrschicht und gespeicherte Ladung der pn-Diode")
Cj0, UD, tau = 24.10e-12, 0.714, 1e-6
for u in (0.4, 0.0, -1.0, -5.0, -10.0):
    Cj = Cj0 / math.sqrt(1 - u / UD)
    Qj = -2 * Cj0 * UD * math.sqrt(1 - u / UD)
    P(f"  U = {u:+5.1f} V: C_S = {Cj*1e12:6.2f} pF, Ladung der Sperrschicht (eine Seite) Q_j = {Qj*1e12:8.2f} pC")
h = 1e-6
for u in (0.0, -1.0):
    Qp = -2 * Cj0 * UD * math.sqrt(1 - (u + h) / UD)
    Qm = -2 * Cj0 * UD * math.sqrt(1 - (u - h) / UD)
    P(f"  Probe dQ/dU numerisch bei {u:+.1f} V: {(Qp-Qm)/(2*h)*1e12:.3f} pF")
P(f"Gespeicherte Ladung der injizierten Ladungsträger bei 1 mA: tau I = {tau*1e-3*1e9:.2f} nC;"
  f" Ableitung tau I/U_T = {tau*1e-3/UT*1e9:.1f} nF (quasistatisch)")
# Ladestrom: I = C du/dt
Cj_m1 = Cj0 / math.sqrt(1 + 1 / UD)
P(f"Ladestrom bei -1 V und 1 V/µs Spannungsänderung: C_S du/dt = {Cj_m1*1e6*1e6:.2f} µA")

# ------------------------------------------------------------------ G. Differentielle Induktivität
kopf("G. Differentielle Induktivität einer Spule mit sättigendem Eisenkern (Modell)")
L0, Isat = 10e-3, 1.0
for i_ in (0.0, 0.5, 1.0, 2.0):
    Psi = L0 * Isat * math.tanh(i_ / Isat)
    Ld = L0 / math.cosh(i_ / Isat) ** 2
    Ls = Psi / i_ if i_ > 0 else L0
    P(f"  I = {i_:.1f} A: Psi = {Psi*1e3:.3f} mVs, L_diff = dPsi/dI = {Ld*1e3:.3f} mH, statisch Psi/I = {Ls*1e3:.3f} mH")
P(f"Spannung bei di/dt = 1 A/ms: bei 0 A {L0*1e3:.1f} V, bei 2 A {L0/math.cosh(2)**2*1e3:.2f} V")

# ------------------------------------------------------------------ H. Kleinsignal-Ersatzschaltbild
kopf("H. Kleinsignalrechnung im Arbeitspunkt und Vergleich mit der exakten Lösung")
iq_hat = 10e-6
u_hat = iq_hat / (gA + Gq)
P(f"Signalanteil der Quelle î_q = {iq_hat*1e6:.0f} µA: û = î_q/(g + G_q) = {u_hat*1e3:.3f} mV;"
  f" Diodenstromanteil î = g û = {gA*u_hat*1e6:.3f} µA, Anteil durch G_q {Gq*u_hat*1e6:.3f} µA")
# exakt: k (U-Uth)^2 + Gq U = Iq + iq  -> U(iq)
def U_exakt(itot):
    a2, b2, c2 = k, Gq - 2 * k * Uth, k * Uth ** 2 - itot
    return (-b2 + math.sqrt(b2 * b2 - 4 * a2 * c2)) / (2 * a2)
Up, Um = U_exakt(Iq + iq_hat), U_exakt(Iq - iq_hat)
P(f"Exakt: U bei +10 µA {Up:.6f} V (+{(Up-UA)*1e3:.4f} mV), bei -10 µA {Um:.6f} V ({(Um-UA)*1e3:.4f} mV);"
  f" Mittel der Ausschläge {(Up-Um)/2*1e3:.4f} mV gegen linear {u_hat*1e3:.4f} mV")
P(f"Klirrmaß-Abschätzung: û/(4(U_A-U_th)) mit û = {u_hat*1e3:.1f} mV: {u_hat/(4*du)*100:.2f} %")
iq_big = 0.2e-3
Up2, Um2 = U_exakt(Iq + iq_big), U_exakt(Iq - iq_big)
P(f"Großes Signal î_q = 0,2 mA: exakt +{(Up2-UA)*1e3:.1f} mV / {(Um2-UA)*1e3:.1f} mV, linear ±{iq_big/(gA+Gq)*1e3:.1f} mV")
C_ass = 1e-12
fg = (gA + Gq) / (2 * math.pi * C_ass)
P(f"Mit C = 1 pF (angenommen) parallel: Grenzfrequenz (g + G_q)/(2 pi C) = {fg/1e6:.1f} MHz")
for fr in (1e6, 10e6, fg):
    P(f"  Kapazitätsstrom C omega û bei {fr/1e6:.1f} MHz und û = {u_hat*1e3:.0f} mV: {C_ass*2*math.pi*fr*u_hat*1e6:.4f} µA"
      f" (Strom durch g + G_q: {(gA+Gq)*u_hat*1e6:.1f} µA)")
P(f"Diode: Stromzuwachs von 0,6 auf 0,7 V Faktor {i_dio(0.7)/i_dio(0.6):.1f}")
P(f"Triode aus dem Einführungsthema als Beispiel für zwei Steuerspannungen: S = 1,6 mA/V, 1/R_i = {1/62.5e3*1e6:.1f} µS")
P(f"Großsignal: Gleichspannungsquelle bleibt im Kleinsignalbild als Kurzschluss, Gleichstromquelle als Unterbrechung")

# ------------------------------------------------------------------ I. Triode: zwei Steuergrößen
kopf("I. Triode (Modell aus zahlen_einfuehrung.py, Abschnitt A): Linearisierung mit zwei Steuergrößen")
S_tr, D_tr, Ia_tr, Ug_tr, Ua_tr = 1.6e-3, 0.01, 1.2e-3, -2.0, 250.0
u_tr = 1.5 * Ia_tr / S_tr
U0_tr = u_tr - (Ug_tr + D_tr * Ua_tr)
K_tr = Ia_tr / u_tr ** 1.5


def ia_tr(ug, ua):
    u = ug + D_tr * ua + U0_tr
    return K_tr * u ** 1.5 if u > 0 else 0.0


h = 1e-6
dI_dUg = (ia_tr(Ug_tr + h, Ua_tr) - ia_tr(Ug_tr - h, Ua_tr)) / (2 * h)
dI_dUa = (ia_tr(Ug_tr, Ua_tr + h) - ia_tr(Ug_tr, Ua_tr - h)) / (2 * h)
P(f"Arbeitspunkt U_g = {Ug_tr} V, U_a = {Ua_tr:.0f} V: I_a = {ia_tr(Ug_tr, Ua_tr)*1e3:.4f} mA; "
  f"dI/dU_g = {dI_dUg*1e3:.4f} mA/V, dI/dU_a = {dI_dUa*1e6:.3f} µS")
dug, dua = 0.1, 6.25
s1 = ia_tr(Ug_tr + dug, Ua_tr) - ia_tr(Ug_tr, Ua_tr)
s2 = ia_tr(Ug_tr + dug, Ua_tr + dua) - ia_tr(Ug_tr + dug, Ua_tr)
P(f"Weg in zwei Teilschritten: +{dug} V am Gitter: exakt {s1*1e3:.4f} mA (linear {dI_dUg*dug*1e3:.4f} mA); "
  f"danach +{dua} V an der Anode: exakt {s2*1e3:.4f} mA (linear {dI_dUa*dua*1e3:.4f} mA)")
P(f"Summe exakt {(s1+s2)*1e3:.4f} mA, linear {(dI_dUg*dug + dI_dUa*dua)*1e3:.4f} mA; "
  f"neuer Strom exakt {ia_tr(Ug_tr+dug, Ua_tr+dua)*1e3:.4f} mA")
P("Kennlinien für die Abbildung (U_g von -3 bis -1 V in 0,25-V-Schritten), I_a in mA:")
for ua in (250.0, 256.25):
    werte = [f"{ia_tr(-3 + 0.25*j, ua)*1e3:5.3f}" for j in range(9)]
    P(f"  U_a = {ua:6.2f} V: {' '.join(werte)}")
P(f"Gitterspannung des neuen Punkts -1,9 V: I_a(250 V) = {ia_tr(-1.9, 250)*1e3:.4f} mA, "
  f"I_a(256,25 V) = {ia_tr(-1.9, 256.25)*1e3:.4f} mA")

# ------------------------------------------------------------------ J. Nachträge aus der Faktenprüfung
kopf("J. Nachträge: Abbruchkriterien, reale Dioden, Gültigkeitsbereiche, Kapazität bei der Grenzfrequenz")


def newton_zaehlen(u0, Ff, Gf, krit, limit=None, nmax=400):
    """Zahl der gelösten linearen Systeme, bis die Spannungsänderung das Kriterium krit(u_alt, u_neu) erfüllt."""
    u = u0
    for n in range(1, nmax + 1):
        unew = u - Ff(u) / Gf(u)
        if limit:
            unew = limit(u, unew)
        if krit(u, unew):
            return n, unew
        u = unew
    return None, u


k_abs = lambda ua, un: abs(un - ua) < 1e-12                      # wie oben in E
k_spice = lambda ua, un: abs(un - ua) <= 1e-3 * abs(un) + 1e-6   # RELTOL 1e-3, VNTOL 1 µV
for name, lim in (("ohne Begrenzung", None), ("mit Begrenzung (pnjlim wie oben)", pnjlim)):
    n1, u1 = newton_zaehlen(0.0, F_dio, G_dio, k_abs, lim)
    n2, u2 = newton_zaehlen(0.0, F_dio, G_dio, k_spice, lim)
    P(f"Diode 5 V/1 kOhm ab 0 V, {name}: |ΔU| < 1e-12 V: {n1} Schritte; SPICE-Kriterium: {n2} Schritte "
      f"(Lösung {u2:.6f} V)")

for N in (1.0, 1.752, 1.906):
    P(f"Emissionskoeffizient N = {N}: Stromfaktor 0,6 -> 0,7 V = {math.exp(0.1/(N*UT)):.2f}, "
      f"Dekade {N*UT*math.log(10)*1e3:.1f} mV")
for u in (0.01, 0.05, 0.1, 0.2):
    P(f"  Verhältnis I(U + 59,5 mV)/I(U) bei U = {u} V: {i_dio(u + UT*math.log(10))/i_dio(u):.3f}")
for u in (-0.1, -0.2):
    P(f"  Sperrstrom bei {u} V: {i_dio(u)/IS:.5f} I_S")


def bessel_i(n, x, glieder=40):
    return sum((x / 2) ** (2 * m + n) / (math.factorial(m) * math.factorial(m + n)) for m in range(glieder))


lo, hi = 1e-4, 1.0
for _ in range(80):
    mid = (lo + hi) / 2
    if bessel_i(2, mid) / bessel_i(1, mid) < 0.01:
        lo = mid
    else:
        hi = mid
P(f"Diode: 1 % zweite Harmonische exakt bei û = {lo*UT*1e3:.4f} mV (û/U_T = {lo:.5f}); "
  f"bei 1 mV: {bessel_i(2, 1e-3/UT)/bessel_i(1, 1e-3/UT)*100:.3f} %")
P(f"1 mV / 0,7 V = {1e-3/0.7*1e3:.3f} Promille; 1 mV / 0,609 V = {1e-3/0.609*1e3:.3f} Promille")

uC = iq_hat / math.hypot(gA + Gq, 2 * math.pi * fg * C_ass)
P(f"Bei f = {fg/1e6:.1f} MHz mit 1 pF: Spannungsamplitude {uC*1e3:.4f} mV (8 mV/sqrt2 = {8/math.sqrt(2):.4f} mV), "
  f"Strom durch g + G_q {(gA+Gq)*uC*1e6:.4f} µA, durch C {2*math.pi*fg*C_ass*uC*1e6:.4f} µA")

# Fixpunktiteration: Vorzeichen und Quotienten der Fehler
uf, fehler = 0.0, []
for _ in range(8):
    uf = Uth + math.sqrt((Iq - Gq * uf) / k)
    fehler.append(uf - UA)
P("Fixpunktiteration ab 0 V, Fehler nach 1 ... 8 Schritten: " + ", ".join(f"{e:+.3e}" for e in fehler) + " V")
P("  Quotienten aufeinanderfolgender Fehler: " + ", ".join(f"{fehler[j+1]/fehler[j]:+.3f}" for j in range(7))
  + f" (Grenzwert -G_q/g = {-Gq/gA:+.3f})")
P(f"Statischer Leitwert im Arbeitspunkt I/U = {i_mos(UA)/UA*1e3:.3f} mS (Kehrwert {UA/i_mos(UA)/1e3:.1f} kOhm), "
  f"differentieller Leitwert {gA*1e3:.3f} mS (Kehrwert {1/gA/1e3:.1f} kOhm)")
P(f"Gleichanteil bei 400 mV: +{0.5*k*0.4**2/i_mos(UA)*100:.0f} %; ±160 mV / 0,5 V = {0.16/0.5:.2f}")

# ====================================================================================================================
# Thema 2: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse
# ====================================================================================================================
import cmath  # noqa: E402


def zeiger(z, einheit="", faktor=1.0):
    """Komplexe Zahl als 'a + jb (Betrag ∠ Winkel)'."""
    z = z * faktor
    return (f"{z.real:+.4f} {'+' if z.imag >= 0 else '-'} j{abs(z.imag):.4f} {einheit} "
            f"(Betrag {abs(z):.4f} {einheit}, Winkel {math.degrees(cmath.phase(z)):+.2f}°)")


# ------------------------------------------------------------------ K. Impedanzen und zweistufiger RC-Tiefpass
kopf("K. Impedanzen bei ω = 10^4 1/s und zweistufiger RC-Tiefpass (Maschen- und Knotenanalyse)")
w = 1e4
Rk, Ck, Lk = 1e3, 100e-9, 100e-3
ZR, ZC, ZL = Rk + 0j, 1 / (1j * w * Ck), 1j * w * Lk
P(f"ω = {w:.0f} 1/s, f = ω/(2π) = {w/(2*math.pi):.2f} Hz")
P(f"Z_R = {zeiger(ZR, 'Ohm')}")
P(f"Z_C (100 nF) = {zeiger(ZC, 'Ohm')}; Y_C = {zeiger(1/ZC, 'mS', 1e3)}")
P(f"Z_L (100 mH) = {zeiger(ZL, 'Ohm')}; Y_L = {zeiger(1/ZL, 'mS', 1e3)}")
for wx in (1e2, 1e3, 1e4, 1e5, 1e6):
    P(f"  ω = {wx:8.0f} 1/s: |Z_R| = {Rk:7.1f} Ohm, |Z_L| = {wx*Lk:10.1f} Ohm, |Z_C| = {1/(wx*Ck):10.1f} Ohm")

Uq = 1.0 + 0j
# Maschen I (Quelle, R1, C1) und II (C1, R2, C2), beide im Uhrzeigersinn
Zm = np.array([[Rk + ZC, -ZC], [-ZC, Rk + 2 * ZC]])
Um = np.array([Uq, 0])
detZ = np.linalg.det(Zm)
Im = np.linalg.solve(Zm, Um)
P("Maschenanalyse: Z-Matrix in kOhm: " + str(np.round(Zm / 1e3, 4).tolist()))
P(f"  det Z = {zeiger(detZ, 'Ohm^2')}")
P(f"  I_I  = {zeiger(Im[0], 'mA', 1e3)}")
P(f"  I_II = {zeiger(Im[1], 'mA', 1e3)}")
P(f"  Strom durch C1 (I_I - I_II) = {zeiger(Im[0]-Im[1], 'mA', 1e3)}")
U1m, U2m = ZC * (Im[0] - Im[1]), ZC * Im[1]
P(f"  U_1 = Z_C (I_I - I_II) = {zeiger(U1m, 'V')}; U_2 = Z_C I_II = {zeiger(U2m, 'V')}")
# Knotenanalyse nach Umwandlung von Quelle und R1 in eine Stromquelle
Gk = 1 / Rk
Iqk = Uq / Rk
Yk = np.array([[Gk + 1j * w * Ck + Gk, -Gk], [-Gk, Gk + 1j * w * Ck]])
Ik = np.array([Iqk, 0])
detY = np.linalg.det(Yk)
Uk = np.linalg.solve(Yk, Ik)
P(f"Knotenanalyse: I_q = U_q/R_1 = {zeiger(Iqk, 'mA', 1e3)}; Y-Matrix in mS: " + str(np.round(Yk * 1e3, 4).tolist()))
P(f"  det Y = {zeiger(detY, 'mS^2', 1e6)}")
P(f"  U_1 = {zeiger(Uk[0], 'V')}; U_2 = {zeiger(Uk[1], 'V')}")
P(f"  Probe: U_1 - U_1(Maschen) = {abs(Uk[0]-U1m):.2e} V, U_2 - U_2(Maschen) = {abs(Uk[1]-U2m):.2e} V")
P(f"  Übertragung U_2/U_q bei ω = 1/(RC) = {zeiger(Uk[1]/Uq)}; allgemein 1/(1 - (ωRC)^2 + 3jωRC)")
for wx in (1e3, 1e4, 1e5):
    x = wx * Rk * Ck
    H = 1 / (1 - x**2 + 3j * x)
    P(f"    ω = {wx:.0f}: |H| = {abs(H):.4f}, Winkel {math.degrees(cmath.phase(H)):+.2f}°")
# Ströme der Originalschaltung aus den Knotenpotentialen
IR1 = (Uq - Uk[0]) / Rk
P(f"  Strom durch R_1 aus den Knotenpotentialen: (U_q - U_1)/R_1 = {zeiger(IR1, 'mA', 1e3)} (= I_I)")
P("  Zählung: Quelle als eigener Zweig: k = 4, z = 5 -> k-1 = 3, z-k+1 = 2; Quelle mit R_1 als reale Quelle: "
  "k = 3, z = 4 -> k-1 = 2, z-k+1 = 2; Unbekannte 2z = 10 bzw. 8")

# ------------------------------------------------------------------ L. Verstärkerstufe mit Source-Widerstand
kopf("L. Source-Schaltung mit Source-Widerstand: Arbeitspunkt, Kleinsignal, Knotenanalyse, Ersatzquelle")
VDD, RD, RS, RL, Rq = 5.0, 10e3, 1e3, 10e3, 10e3
UGS = 1.0
ID = k * (UGS - Uth) ** 2
gm = 2 * k * (UGS - Uth)
go = 25e-6
US0 = ID * RS
UG0 = UGS + US0
UD0 = VDD - ID * RD
UDS = UD0 - US0
P(f"Arbeitspunkt: U_GS = {UGS} V, I_D = k (U_GS - U_th)^2 = {ID*1e3:.3f} mA, U_S = {US0:.3f} V, "
  f"U_G = {UG0:.3f} V, U_D = {UD0:.3f} V, U_DS = {UDS:.3f} V (Sättigung, da > U_GS - U_th = {UGS-Uth:.2f} V)")
P(f"Kleinsignal: g_m = 2k(U_GS - U_th) = {gm*1e3:.3f} mS, g_o = {go*1e6:.1f} µS (angenommen, r_o = {1/go/1e3:.1f} kOhm)")
GD, GS, GL, Gqv = 1 / RD, 1 / RS, 1 / RL, 1 / Rq
uq = 10e-3


def verstaerker(GLx, uqx=uq):
    """Knotenanalyse G, D, S; Quelle uq mit Rq als Norton-Quelle am Gate."""
    Y = np.array([[Gqv, 0, 0],
                  [gm, GD + GLx + go, -(gm + go)],
                  [-gm, -go, gm + go + GS]])
    I = np.array([uqx * Gqv, 0, 0])
    return Y, I, np.linalg.solve(Y, I)


Yv, Iv, Uv = verstaerker(GL)
P("Y-Matrix (Zeilen G, D, S) in mS: " + str(np.round(Yv * 1e3, 4).tolist()))
P(f"  symmetrisch? {np.allclose(Yv, Yv.T)}; ohne g_m-Anteile symmetrisch? "
  f"{np.allclose(Yv - gm*np.array([[0,0,0],[1,0,-1],[-1,0,1]]), (Yv - gm*np.array([[0,0,0],[1,0,-1],[-1,0,1]])).T)}")
P(f"  det Y = {np.linalg.det(Yv)*1e9:.6f} mS^3")
P(f"  mit R_L = 10 kOhm, u_q = 10 mV: U_G = {Uv[0]*1e3:.4f} mV, U_D = {Uv[1]*1e3:.4f} mV, U_S = {Uv[2]*1e3:.4f} mV; "
  f"Verstärkung U_D/u_q = {Uv[1]/uq:.4f}")
P(f"  Näherung ohne g_o: -g_m (R_D||R_L)/(1 + g_m R_S) = {-gm*(RD*RL/(RD+RL))/(1+gm*RS):.4f}")
Y0, I0, U0v = verstaerker(0.0)
ULL = U0v[1]
P(f"Ohne Last: Leerlaufspannung U_LL = U_D = {ULL*1e3:.4f} mV (Verstärkung {ULL/uq:.4f}), U_S = {U0v[2]*1e3:.4f} mV")
# Kurzschluss am Ausgang: U_D = 0 -> nur G und S unbekannt
YKS = np.array([[Gqv, 0], [-gm, gm + go + GS]])
UKS = np.linalg.solve(YKS, np.array([uq * Gqv, 0]))
IKS = -(gm * (UKS[0] - UKS[1]) + go * (0 - UKS[1]))   # Strom aus Klemme D in den Kurzschluss
P(f"Kurzschluss D-Masse: U_G = {UKS[0]*1e3:.4f} mV, U_S = {UKS[1]*1e3:.4f} mV, I_KS (aus D heraus) = {IKS*1e6:.4f} µA")
Zi = ULL / IKS
P(f"Innenwiderstand Z_i = U_LL/I_KS = {Zi/1e3:.4f} kOhm, Y_i = {1/Zi*1e3:.5f} mS")
# Testquelle: u_q = 0, U_T am Drain, Strom I_T in den Drain-Knoten
UT_ = 1.0
US_T = go * UT_ / (GS + gm + go)
IT = GD * UT_ + gm * (0 - US_T) + go * (UT_ - US_T)
P(f"Testquelle (u_q = 0, U_T = 1 V): U_S = {US_T:.6f} V, I_T = {IT*1e3:.6f} mA, Z_i = U_T/I_T = {UT_/IT/1e3:.4f} kOhm")
rT = 1 / go + 1 / GS + gm / go / GS
P(f"Transistor mit R_S allein: r_o (1 + g_m R_S) + R_S = {rT/1e3:.3f} kOhm; parallel R_D: "
  f"{1/(GD + 1/rT)/1e3:.4f} kOhm")
rfalsch = 1 / go + 1 / GS
P(f"Falsch (gesteuerte Quelle mit abgeschaltet): r_o + R_S = {rfalsch/1e3:.1f} kOhm; parallel R_D: "
  f"{1/(GD + 1/rfalsch)/1e3:.4f} kOhm (Fehler {(1/(GD+1/rfalsch)-Zi)/Zi*100:+.2f} %)")
Ulast = ULL * RL / (RL + Zi)
Ulast_f = ULL * RL / (RL + 1 / (GD + 1 / rfalsch))
P(f"Mit Last 10 kOhm über die Ersatzquelle: U = U_LL R_L/(R_L + Z_i) = {Ulast*1e3:.4f} mV (Knotenanalyse "
  f"{Uv[1]*1e3:.4f} mV); mit falschem Z_i {Ulast_f*1e3:.4f} mV ({(Ulast_f-Ulast)/Ulast*100:+.2f} %)")
IA = Uv[1] / RL
P(f"  Klemmenstrom I_A = U/R_L = {IA*1e6:.4f} µA; Probe U_LL - Z_i I_A = {(ULL - Zi*IA)*1e3:.4f} mV")
P(f"  Norton: I_KS = {IKS*1e6:.4f} µA, Y_i = {1/Zi*1e3:.5f} mS; I_A = I_KS - Y_i U = {(IKS - Uv[1]/Zi)*1e6:.4f} µA")
P("  Zählung Kleinsignalschaltung (reale Signalquelle als ein Zweig): Knoten G, D, S, Masse -> k = 4; Zweige "
  "Quelle, g_m, g_o, R_D, R_L, R_S -> z = 6; k-1 = 3, z-k+1 = 3")
P(f"Quelle am Gate ideal (R_q = 0): U_G = u_q bekannt, es bleiben 2 Unbekannte; Ergebnis U_D gleich, da der Gate-Strom "
  f"null ist")

# ------------------------------------------------------------------ M. Zählung und Wahl des Verfahrens
kopf("M. Zählung: Knoten- gegen Maschengleichungen")
for name, kk, zz in (("RC-Tiefpass, reale Quelle", 3, 4), ("Verstärkerstufe", 4, 6),
                     ("drei reale Quellen und eine Last parallel", 2, 4), ("Brücke mit Quelle (Wheatstone)", 4, 6)):
    P(f"  {name}: k = {kk}, z = {zz}: Knotengleichungen k-1 = {kk-1}, Maschengleichungen z-k+1 = {zz-kk+1}, "
      f"Unbekannte insgesamt 2z = {2*zz}")
# Parallelschaltung: drei reale Spannungsquellen (Leerlaufspannungen 12, 11, 10 V; Innenwiderstände 1, 2, 4 Ohm) an 10 Ohm
Uqs, Rqs, Rlast = (12.0, 11.0, 10.0), (1.0, 2.0, 4.0), 10.0
Uknoten = sum(u / r for u, r in zip(Uqs, Rqs)) / (sum(1 / r for r in Rqs) + 1 / Rlast)
P(f"  Parallelschaltung: eine Knotengleichung, U = Summe(U_q/R_q)/(Summe(1/R_q) + 1/R_L) = {Uknoten:.4f} V")

# ------------------------------------------------------------------ N. Ergänzungen für Text, Fragen und Vertiefung
kopf("N. Ergänzungen: Überlagerung, ideale Stromquelle, Reziprozität, Verlustleistung, Testquelle je Volt")
_, _, U20 = verstaerker(GL, 20e-3)
P(f"Verstärkerstufe mit 20 mV statt 10 mV: U_D = {U20[1]*1e3:.4f} mV (doppelt: {2*Uv[1]*1e3:.4f} mV)")
_, _, Um5 = verstaerker(GL, -5e-3)
_, _, Usum = verstaerker(GL, 15e-3)
P(f"Überlagerung: 10 mV und -5 mV einzeln {Uv[1]*1e3:.4f} + {Um5[1]*1e3:.4f} = {(Uv[1]+Um5[1])*1e3:.4f} mV, "
  f"Summe 5 mV direkt: {verstaerker(GL, 5e-3)[2][1]*1e3:.4f} mV")
# RC-Tiefpass mit idealer Stromquelle 1 mA in Knoten 1 (statt U_q mit R_1)
Iideal = 1e-3
I_II_ideal = ZC * Iideal / (Rk + 2 * ZC)
P(f"RC-Tiefpass mit idealer Stromquelle 1 mA an Knoten 1: Masche I hat I_I = 1 mA; Masche II: "
  f"-Z_C I_I + (R + 2 Z_C) I_II = 0 -> I_II = {zeiger(I_II_ideal, 'mA', 1e3)}")
P(f"  U_2 = Z_C I_II = {zeiger(ZC*I_II_ideal, 'V')}; Spannung an der Stromquelle U_1 = Z_C (I_I - I_II) = "
  f"{zeiger(ZC*(Iideal-I_II_ideal), 'V')}")
# Probe über Knotenanalyse
Yid = np.array([[1j * w * Ck + Gk, -Gk], [-Gk, Gk + 1j * w * Ck]])
Uid = np.linalg.solve(Yid, np.array([Iideal, 0]))
P(f"  Probe Knotenanalyse: U_1 = {zeiger(Uid[0], 'V')}, U_2 = {zeiger(Uid[1], 'V')}")
# Reziprozität
Zrc = np.linalg.inv(Yk)
P("RC-Tiefpass: Y^-1 in kOhm: " + str(np.round(Zrc / 1e3, 4).tolist())
  + f"; Z_12 = {zeiger(Zrc[0,1], 'Ohm')}, Z_21 = {zeiger(Zrc[1,0], 'Ohm')}")
Zv = np.linalg.inv(Yv)
P("Verstärkerstufe: Y^-1 in kOhm (Zeilen/Spalten G, D, S): " + str(np.round(Zv / 1e3, 4).tolist()))
P(f"  1 µA in G eingespeist -> U_D = {Zv[1,0]*1e-6*1e3:.4f} mV; 1 µA in D eingespeist -> U_G = {Zv[0,1]*1e-6*1e3:.4f} mV")
# Verlustleistung bei der Quellenumwandlung (Amplitude 1 V, Effektivleistung Û²/(2R))
P(f"Quellenumwandlung RC-Quelle (1 V, 1 kOhm <-> 1 mA, 1 mS), Leerlauf: Spannungsform 0 W im Innenwiderstand, "
  f"Stromform (1 V)^2/(2 kOhm) = {1.0**2/(2*Rk)*1e3:.2f} mW im Innenleitwert; Kurzschluss: Spannungsform "
  f"{(1e-3)**2*Rk/2*1e3:.2f} mW, Stromform 0 W")
P(f"Testquelle je Volt am Drain: Strom durch R_D {GD*1e3:.4f} mA, in den Transistorzweig {(IT-GD)*1e6:.4f} µA; "
  f"darin g_m u_GS = {gm*(0-US_T)*1e6:.4f} µA und g_o-Anteil {go*(UT_-US_T)*1e6:.4f} µA; "
  f"ohne gesteuerte Quelle {UT_/rfalsch*1e6:.4f} µA")
P(f"  Probe Summe: 100 - {gm*US_T*1e6:.4f} + {go*(UT_-US_T)*1e6:.4f} = {(GD - gm*US_T + go*(UT_-US_T))*1e6:.4f} µA; "
  f"Drain-Source-Strecke allein (U_T - U_S)/I = {(UT_-US_T)/(IT-GD)/1e3:.3f} kOhm gegen r_o = {1/go/1e3:.1f} kOhm "
  f"ohne gesteuerte Quelle (Faktor {(UT_-US_T)/(IT-GD)*go:.3f})")
P(f"Summe der Zeilen D und S: (G_D + G_L) U_D + G_S U_S = {((GD+GL)*Uv[1] + GS*Uv[2])*1e9:.3e} (null): U_S = "
  f"{-(GD+GL)/GS:.2f} U_D")
P(f"Leerlauf: G_D U_D + G_S U_S = 0 -> U_S = {-GD/GS:.2f} U_D")
UL100 = ULL * 100e3 / (100e3 + Zi)
P(f"Ersatzquelle an 100 kOhm: {UL100*1e3:.4f} mV (Verlust gegen Leerlauf {(1-UL100/ULL)*100:.1f} %)")
P(f"Verstärkung ohne g_o mit R_S: {-gm*(RD*RL/(RD+RL))/(1+gm*RS):.4f}; ohne g_o und ohne R_S: {-gm*(RD*RL/(RD+RL)):.4f}; "
  f"mit g_o ohne R_S: {-gm/(GD+GL+go)*1e-3*1e3:.4f}")
P(f"Drei Quellen parallel: Strom in die 10-V-Quelle ({Uknoten:.4f} V - 10 V)/4 Ohm = {(Uknoten-10)/4:.4f} A")


# ======================================================================================================================
# Thema 3: Netzwerkgleichungen systematisch aufstellen (Eintragsmuster, Cramersche Regel, modifizierte Knotenanalyse)
# Beispielsysteme wie oben (Verstärkerstufe, RC-Tiefpass), dazu: Schwingkreis 100 mH ∥ 100 nF an 1 mA;
# Gate-Source-Kapazität 100 fF und Gate-Drain-Kapazität 20 fF (angenommen); Lastkapazität 10 pF (Tastkopf bzw.
# nächste Stufe); invertierender Verstärker R_1 = 10 kOhm, R_2 = 100 kOhm, Leerlaufverstärkung 200 000 (741 typisch).
# ======================================================================================================================
def fz(z, nk=4):
    """Komplexe Zahl kurz als a + jb."""
    z = complex(z)
    if abs(z.imag) < 10 ** (-nk - 2):
        return f"{z.real:.{nk}f}"
    if abs(z.real) < 10 ** (-nk - 2):
        return f"{z.imag:.{nk}f}j"
    return f"({z.real:.{nk}f} {'+' if z.imag >= 0 else '-'} {abs(z.imag):.{nk}f}j)"


def mat_str(A, nk=4):
    return "[" + ", ".join("[" + ", ".join(fz(x, nk) for x in row) + "]" for row in np.asarray(A)) + "]"


class MNA:
    """Modifizierte Knotenanalyse mit Eintragsmustern. Knoten '0' ist der Bezugsknoten (Zeile und Spalte entfallen).
    Zusatzströme fließen von i durch das Element nach k (in den Pluspol hinein)."""

    def __init__(self, knoten, zusatz=()):
        self.kn = {k: j for j, k in enumerate(knoten)}
        self.n = len(knoten)
        self.zs = {z: self.n + j for j, z in enumerate(zusatz)}
        N = self.n + len(zusatz)
        self.M = np.zeros((N, N), dtype=complex)
        self.r = np.zeros(N, dtype=complex)

    def _k(self, k):
        return None if k == "0" else self.kn[k]

    def _add(self, a, b, w):
        if a is not None and b is not None:
            self.M[a, b] += w

    def admittanz(self, i, k, y):
        a, b = self._k(i), self._k(k)
        self._add(a, a, y), self._add(b, b, y), self._add(a, b, -y), self._add(b, a, -y)

    def vccs(self, i, k, p, q, g):
        """Strom g (U_p - U_q) fließt von i durch die Quelle nach k."""
        a, b, c, d = self._k(i), self._k(k), self._k(p), self._k(q)
        self._add(a, c, g), self._add(a, d, -g), self._add(b, c, -g), self._add(b, d, g)

    def stromquelle(self, i, k, iq):
        """Quellenstrom iq fließt durch die Quelle von k nach i, also in Knoten i hinein."""
        a, b = self._k(i), self._k(k)
        if a is not None:
            self.r[a] += iq
        if b is not None:
            self.r[b] -= iq

    def _spalte(self, i, k, name):
        z = self.zs[name]
        self._add(self._k(i), z, 1.0), self._add(self._k(k), z, -1.0)
        return z

    def spannungszweig(self, i, k, name, uq=0.0, zq=0.0):
        """Ideale Spannungsquelle (zq = 0), Impedanz (uq = 0) oder Tor: U_i - U_k - zq I = uq."""
        z = self._spalte(i, k, name)
        self._add(z, self._k(i), 1.0), self._add(z, self._k(k), -1.0)
        self.M[z, z] -= zq
        self.r[z] += uq

    def vcvs(self, i, k, p, q, name, v):
        """U_i - U_k - v (U_p - U_q) = 0."""
        z = self._spalte(i, k, name)
        self._add(z, self._k(i), 1.0), self._add(z, self._k(k), -1.0)
        self._add(z, self._k(p), -v), self._add(z, self._k(q), v)

    def cccs(self, i, k, steuer, beta):
        """Strom beta I_steuer fließt von i durch die Quelle nach k."""
        s = self.zs[steuer]
        self._add(self._k(i), s, beta), self._add(self._k(k), s, -beta)

    def ccvs(self, i, k, steuer, name, rm):
        """U_i - U_k - rm I_steuer = 0."""
        z = self._spalte(i, k, name)
        self._add(z, self._k(i), 1.0), self._add(z, self._k(k), -1.0)
        self.M[z, self.zs[steuer]] -= rm

    def nullor(self, p, q, i, k, name):
        """Nullator zwischen p (+) und q (-): U_p - U_q = 0, kein Strom; Norator zwischen i und k: Strom 'name'."""
        z = self._spalte(i, k, name)
        self._add(z, self._k(p), 1.0), self._add(z, self._k(q), -1.0)

    def loesen(self):
        return np.linalg.solve(self.M, self.r)


def laplace(A, zaehler):
    """Determinante durch Entwicklung nach der ersten Zeile; zaehler[0] zählt die Multiplikationen."""
    A = np.asarray(A, dtype=complex)
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    if n == 2:
        zaehler[0] += 2
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    s = 0
    for j in range(n):
        minor = np.delete(np.delete(A, 0, axis=0), j, axis=1)
        zaehler[0] += 1
        s += (-1) ** j * A[0, j] * laplace(minor, zaehler)
    return s


def entwicklung(A, zeile=None, spalte=None):
    """Summanden der Laplace-Entwicklung nach einer Zeile oder Spalte (Index ab 0)."""
    A = np.asarray(A, dtype=complex)
    terme = []
    n = A.shape[0]
    for t in range(n):
        mu, nu = (zeile, t) if zeile is not None else (t, spalte)
        minor = np.delete(np.delete(A, mu, axis=0), nu, axis=1)
        terme.append((-1) ** (mu + nu) * A[mu, nu] * np.linalg.det(minor))
    return terme


def cramer(A, b):
    A = np.asarray(A, dtype=complex)
    D = np.linalg.det(A)
    Ds = []
    for nu in range(A.shape[0]):
        An = A.copy()
        An[:, nu] = b
        Ds.append(np.linalg.det(An))
    return D, Ds


# ------------------------------------------------------------------ O. Eintragsmuster
kopf("O. Eintragsmuster: vollständige Leitwertmatrix der Verstärkerstufe (Knoten 0, G, D, S), Streichen des Bezugs")
# Einheiten: mS, mV, µA
kn4 = ["0", "G", "D", "S"]
idx4 = {k_: j for j, k_ in enumerate(kn4)}
Yf = np.zeros((4, 4))
If = np.zeros(4)


def f_adm(i, k_, y):
    a, b = idx4[i], idx4[k_]
    Yf[a, a] += y
    Yf[b, b] += y
    Yf[a, b] -= y
    Yf[b, a] -= y


def f_vccs(i, k_, p, q, g):
    a, b, c, d = idx4[i], idx4[k_], idx4[p], idx4[q]
    Yf[a, c] += g
    Yf[a, d] -= g
    Yf[b, c] -= g
    Yf[b, d] += g


schritte = [("Signalquelle (Norton): 1 µA in G, G_sig = 0,1 mS zwischen G und 0", lambda: (f_adm("G", "0", 0.1),
                                                                                          If.__setitem__(1, If[1] + 1),
                                                                                          If.__setitem__(0, If[0] - 1))),
            ("R_D: 0,1 mS zwischen D und 0", lambda: f_adm("D", "0", 0.1)),
            ("R_L: 0,1 mS zwischen D und 0", lambda: f_adm("D", "0", 0.1)),
            ("R_S: 1 mS zwischen S und 0", lambda: f_adm("S", "0", 1.0)),
            ("g_o: 0,025 mS zwischen D und S", lambda: f_adm("D", "S", 0.025)),
            ("g_m (U_G - U_S) von D nach S, 1 mS", lambda: f_vccs("D", "S", "G", "S", 1.0))]
for txt, fn in schritte:
    fn()
    P(f"  nach {txt}:")
    P(f"    Y (Zeilen/Spalten 0, G, D, S) = {np.round(Yf, 4).tolist()}, I_q = {np.round(If, 4).tolist()}")
P(f"Zeilensummen {np.round(Yf.sum(axis=1), 12).tolist()}, Spaltensummen {np.round(Yf.sum(axis=0), 12).tolist()}, "
  f"Summe I_q = {If.sum():.1f}")
P(f"det (vollständig, 4x4) = {np.linalg.det(Yf):.3e} (singulär); Y·(1,1,1,1) = {np.round(Yf @ np.ones(4), 12).tolist()}")
Yred = Yf[1:, 1:]
P(f"nach Streichen von Zeile und Spalte 0: {np.round(Yred, 4).tolist()} = Matrix aus L? "
  f"{np.allclose(Yred * 1e-3, Yv)}")
P(f"  Zeile 0 = -(Summe der Zeilen G, D, S)? {np.allclose(Yf[0], -Yf[1:].sum(axis=0))}")
Uf = np.linalg.solve(Yred, If[1:])
P(f"  Lösung U_G, U_D, U_S = {np.round(Uf, 4).tolist()} mV")
P(f"  Probe Zeile 0 mit der Lösung: Summe = {Yf[0, 1:] @ Uf:.4f} µA = I_q(0) = {If[0]:.1f} µA")
P(f"  Potentiale alle um 1 V angehoben: Ströme unverändert, da Y·(1,1,1,1) = 0")
# Strom durch R_S und Zählrichtung
P(f"  Strom durch R_S von S nach 0: G_S U_S = {1.0*Uf[2]:.4f} µA; von 0 nach S gezählt {-1.0*Uf[2]:.4f} µA")
P(f"  Strom durch R_D von D nach 0: {0.1*Uf[1]:.4f} µA (negativ: fließt von Masse in den Drain)")

# ------------------------------------------------------------------ P. Determinanten und Cramersche Regel
kopf("P. Determinanten, Cramersche Regel, Rechenaufwand, Transponierte und Adjunkte")
Ym = Yred.astype(complex)   # mS
bm = If[1:].astype(complex)  # µA
for z_ in range(3):
    t_ = entwicklung(Ym, zeile=z_)
    P(f"  Entwicklung nach Zeile {['G','D','S'][z_]}: Summanden {[round(x.real, 6) for x in t_]} -> {sum(t_).real:.6f} mS^3")
for s_ in range(3):
    t_ = entwicklung(Ym, spalte=s_)
    P(f"  Entwicklung nach Spalte {['G','D','S'][s_]}: Summanden {[round(x.real, 6) for x in t_]} -> {sum(t_).real:.6f} mS^3")
a = Ym.real
sar = [a[0, 0]*a[1, 1]*a[2, 2], a[0, 1]*a[1, 2]*a[2, 0], a[0, 2]*a[1, 0]*a[2, 1],
       -a[2, 0]*a[1, 1]*a[0, 2], -a[2, 1]*a[1, 2]*a[0, 0], -a[2, 2]*a[1, 0]*a[0, 1]]
P(f"  Sarrus: Summanden {[round(x, 7) for x in sar]} -> {sum(sar):.6f} mS^3")
D_, Ds_ = cramer(Ym, bm)
P(f"Cramer: D = {D_.real:.6f} mS^3; D_G = {Ds_[0].real:.6f}, D_D = {Ds_[1].real:.6f}, D_S = {Ds_[2].real:.6f} mS^2 µA")
P(f"  U_G = {Ds_[0].real/D_.real:.4f} mV, U_D = {Ds_[1].real/D_.real:.4f} mV, U_S = {Ds_[2].real/D_.real:.4f} mV")
for nu, name in enumerate(["G", "D", "S"]):
    An = Ym.copy()
    An[:, nu] = bm
    P(f"  Y_{name} (Spalte {name} durch I_q ersetzt) = {np.round(An.real, 4).tolist()}")
P(f"  Kofaktoren D_D: Spalte D enthält nur oben 1 µA -> (-1)^(1+2)·1·det[[1, -1,025], [-1, 2,025]] = "
  f"{-(1*2.025 - (-1.025)*(-1)):.4f}")
P(f"  Kofaktoren D_S: Spalte S enthält nur oben 1 µA -> (+1)·det[[1, 0,225], [-1, -0,025]] = "
  f"{(1*(-0.025) - 0.225*(-1)):.4f}")
# 2x2: RC-Tiefpass aus K (Einheiten mS, mA, V)
Y2 = Yk * 1e3
D2_, Ds2_ = cramer(Y2, np.array([1.0, 0.0]))
P(f"RC-Tiefpass 2x2: Y = {mat_str(Y2)} mS; D = (2+j)(1+j) - (-1)(-1) = {fz(D2_)} mS^2")
P(f"  D_1 = det[[1, -1], [0, 1+j]] = {fz(Ds2_[0])}; D_2 = det[[2+j, 1], [-1, 0]] = {fz(Ds2_[1])}")
P(f"  U_1 = {fz(Ds2_[0]/D2_)} V, U_2 = {fz(Ds2_[1]/D2_)} V")
# Elimination 2x2 allgemein: x1 = (b1 a22 - a12 b2)/(a11 a22 - a12 a21)
P("  2x2 allgemein: x_1 = (b_1 a_22 - a_12 b_2)/(a_11 a_22 - a_12 a_21), x_2 = (a_11 b_2 - a_21 b_1)/(a_11 a_22 - a_12 a_21)")
# Rechenaufwand
P("Rechenaufwand (Multiplikationen und Divisionen):")
P("   n | Laplace eine Det. | Cramer (n+1 Det. + n Div.) | Gauß (n^3 - n)/3 + n^2 | Zeit Cramer bei 1e9/s")
for n_ in (2, 3, 4, 5, 10, 15, 20, 25):
    Mn = 0
    for m_ in range(2, n_ + 1):
        Mn = 2 if m_ == 2 else m_ * (Mn + 1)
    cr = (n_ + 1) * Mn + n_
    ga = (n_ ** 3 - n_) // 3 + n_ ** 2
    sek = cr / 1e9
    zeit = (f"{sek:.2e} s" if sek < 3600 else f"{sek/3600:.2e} h" if sek < 3.15e7 else f"{sek/3.156e7:.2e} Jahre")
    P(f"  {n_:3d} | {Mn:.3e} | {cr:.3e} | {ga} | {zeit}")
cnt = [0]
laplace(Ym, cnt)
P(f"  Probe Zähler laplace(3x3) = {cnt[0]} Multiplikationen")
P(f"  1e6 Knoten, vollbesetzt: Gauß ≈ {(1e6**3)/3:.2e} Multiplikationen = {(1e18/3)/1e9/3.156e7:.1f} Jahre bei 1e9/s")
# Transponierte und Adjunkte
P(f"det(Y^T) = {np.linalg.det(Ym.T).real:.6f} = det(Y) = {np.linalg.det(Ym).real:.6f} mS^3")
adj2 = np.array([[Y2[1, 1], -Y2[0, 1]], [-Y2[1, 0], Y2[0, 0]]])
P(f"Tiefpass: adj(Y) = {mat_str(adj2)}; Y^-1 = adj/det = {mat_str(adj2/D2_)} kOhm; "
  f"numpy: {mat_str(np.linalg.inv(Y2))}")
cof = np.zeros((3, 3), dtype=complex)
for mu in range(3):
    for nu in range(3):
        cof[mu, nu] = (-1) ** (mu + nu) * np.linalg.det(np.delete(np.delete(Ym, mu, 0), nu, 1))
adj3 = cof.T
P(f"Verstärkerstufe: adj(Y) = {np.round(adj3.real, 6).tolist()} (mS^2)")
P(f"  Y^-1 = adj/det = {np.round((adj3/D_).real, 4).tolist()} kOhm; numpy {np.round(np.linalg.inv(Ym).real, 4).tolist()}")
P(f"  Spalte G von Y^-1 = Spannungen je µA in G: U_D = {(adj3/D_)[1,0].real:.4f} mV; Spalte D, Zeile G: "
  f"{(adj3/D_)[0,1].real:.4f} mV")
# Transponiertes System: Y^T x = b, Zähler über Zeilenersatz in Y
xT = np.linalg.solve(Ym.T, bm)
P(f"Transponiertes System Y^T x = (1, 0, 0) µA: x = {np.round(xT.real, 4).tolist()}")
for z_ in range(3):
    Az = Ym.copy()
    Az[z_, :] = bm
    P(f"  Zeile {z_+1} von Y durch b^T ersetzt: det = {np.linalg.det(Az).real:.6f} -> x_{z_+1} = "
      f"{np.linalg.det(Az).real/D_.real:.4f}")

# ------------------------------------------------------------------ Q. MNA: RC-Tiefpass mit idealer Spannungsquelle
kopf("Q. Modifizierte Knotenanalyse: RC-Tiefpass mit idealer Spannungsquelle (Einheiten mS, kOhm, V, mA)")
yc = 1j * w * Ck * 1e3     # j·1 mS
q = MNA(["1", "2", "3"], ["I_q"])
q.spannungszweig("1", "0", "I_q", uq=1.0)
q.admittanz("1", "2", 1.0)       # R_1
q.admittanz("2", "0", yc)        # C_1
q.admittanz("2", "3", 1.0)       # R_2
q.admittanz("3", "0", yc)        # C_2
P(f"M (Spalten U_1, U_2, U_3, I_q) = {mat_str(q.M)}; rechte Seite {mat_str([q.r])}")
xq = q.loesen()
Dq, Dsq = cramer(q.M, q.r)
P(f"  det M = {fz(Dq)}; Zähler D_1..D_4 = {[fz(d) for d in Dsq]}")
P(f"  U_1 = {zeiger(xq[0], 'V')}; U_2 = {zeiger(xq[1], 'V')}; U_3 = {zeiger(xq[2], 'V')}")
P(f"  I_q (in den Pluspol hinein) = {zeiger(xq[3], 'mA')}; abgegebener Strom -I_q = {zeiger(-xq[3], 'mA')}")
P(f"  Probe gegen K: U_2 = Knoten 1 dort {zeiger(Uk[0], 'V')}, U_3 = Ausgang dort {zeiger(Uk[1], 'V')}, "
  f"I_I = {zeiger(Im[0], 'mA', 1e3)}")
t_ = entwicklung(q.M, zeile=3)
P(f"  Entwicklung von det M nach der Quellenzeile: Summanden {[fz(x) for x in t_]}")
minor41 = np.delete(np.delete(q.M, 3, 0), 0, 1)
P(f"  Streichungsmatrix (Zeile 4, Spalte 1) = {mat_str(minor41)}, det = {fz(np.linalg.det(minor41))}")
# Variante: Quelle mit R_1 als Tor zwischen Knoten 2 und 0
qt = MNA(["2", "3"], ["I_q"])
qt.spannungszweig("2", "0", "I_q", uq=1.0, zq=1.0)
qt.admittanz("2", "0", yc)
qt.admittanz("2", "3", 1.0)
qt.admittanz("3", "0", yc)
xqt = qt.loesen()
Dqt, Dsqt = cramer(qt.M, qt.r)
P(f"Tor-Variante (Quelle mit R_1): M = {mat_str(qt.M)}, rechte Seite {mat_str([qt.r])}")
P(f"  det = {fz(Dqt)}; D_U2 = {fz(Dsqt[0])}, D_U3 = {fz(Dsqt[1])}, D_Iq = {fz(Dsqt[2])}")
P(f"  U_2 = {zeiger(xqt[0], 'V')}, U_3 = {zeiger(xqt[1], 'V')}, I_q = {zeiger(xqt[2], 'mA')}")
# Leistung der Quelle (Amplituden: P = 1/2 Re{U I*})
Pq = 0.5 * (1.0 * np.conj(-xq[3])).real
P(f"  Wirkleistung der Quelle 1/2 Re(U_q (-I_q)*) = {Pq:.4f} mW; in R_1: 1/2 |I|^2 R_1 = {0.5*abs(xq[3])**2*1.0:.4f} mW, "
  f"in R_2: {0.5*abs(xq[1]-xq[2])**2*1.0:.4f} mW")

# ------------------------------------------------------------------ R. MNA: Verstärkerstufe mit Signalquelle als Tor
kopf("R. Modifizierte Knotenanalyse: Verstärkerstufe, Signalquelle 10 mV mit 10 kOhm als Tor (mS, kOhm, mV, µA)")
r_ = MNA(["G", "D", "S"], ["I_sig"])
r_.spannungszweig("G", "0", "I_sig", uq=10.0, zq=10.0)
r_.admittanz("D", "0", 0.1)
r_.admittanz("D", "0", 0.1)
r_.admittanz("S", "0", 1.0)
r_.admittanz("D", "S", 0.025)
r_.vccs("D", "S", "G", "S", 1.0)
xr = r_.loesen()
Dr, Dsr = cramer(r_.M, r_.r)
P(f"M (Spalten U_G, U_D, U_S, I_sig) = {np.round(r_.M.real, 4).tolist()}; rechte Seite {np.round(r_.r.real, 4).tolist()}")
P(f"  det M = {Dr.real:.6f}; D_D = {Dsr[1].real:.6f}; U_D = {Dsr[1].real/Dr.real:.4f} mV")
P(f"  Lösung U_G = {xr[0].real:.4f} mV, U_D = {xr[1].real:.4f} mV, U_S = {xr[2].real:.4f} mV, I_sig = {xr[3].real:.4f} µA")

# ------------------------------------------------------------------ S. MNA: Spule als Impedanz, Gleichstrom und Resonanz
kopf("S. Spule in der modifizierten Knotenanalyse: Schwingkreis 100 mH ∥ 100 nF an 1 mA (mS, kOhm, V, mA)")
for wx in (0.0, 5e3, 1e4, 2e4):
    s_ = MNA(["1"], ["I_L"])
    s_.stromquelle("1", "0", 1.0)
    s_.admittanz("1", "0", 1j * wx * Ck * 1e3)
    s_.spannungszweig("1", "0", "I_L", zq=1j * wx * Lk / 1e3)
    Ds_ = np.linalg.det(s_.M)
    if abs(Ds_) < 1e-12:
        P(f"  ω = {wx:7.0f} 1/s: M = {mat_str(s_.M)}, det = {fz(Ds_)} -> keine eindeutige Lösung (Resonanz)")
        continue
    xs_ = s_.loesen()
    P(f"  ω = {wx:7.0f} 1/s: M = {mat_str(s_.M)}, det = ω²LC - 1 = {fz(Ds_)}; U_1 = {fz(xs_[0])} V, I_L = {fz(xs_[1])} mA, "
      f"I_C = {fz(1j*wx*Ck*1e3*xs_[0])} mA")
P(f"  ω_0 = 1/sqrt(LC) = {1/math.sqrt(Lk*Ck):.1f} 1/s; Knotenanalyse: Y = jωC + 1/(jωL) wird bei ω -> 0 unendlich")
for wx in (1.0, 10.0, 100.0):
    P(f"    ω = {wx:5.0f} 1/s: |1/(jωL)| = {1/(wx*Lk)*1e3:.1f} mS")

# ------------------------------------------------------------------ T. Strommesser als 0-V-Quelle, Transitfrequenz
kopf("T. Strommesser als Spannungsquelle 0 V: Stromverstärkung und Transitfrequenz (SI-Einheiten)")
Cgs, Cgd = 100e-15, 20e-15


def beta_mna(wx, cgd=0.0):
    t = MNA(["G", "D"], ["I_out"])
    t.stromquelle("G", "0", 1.0)                 # I_in = 1 A (Bezug)
    t.admittanz("G", "0", 1j * wx * Cgs)
    if cgd:
        t.admittanz("G", "D", 1j * wx * cgd)
    t.vccs("D", "0", "G", "0", gm)
    t.admittanz("D", "0", go)
    t.spannungszweig("D", "0", "I_out", uq=0.0)   # Strommesser
    return t, t.loesen()


t1, xt1 = beta_mna(2 * math.pi * 100e6)
P(f"M bei 100 MHz (Spalten U_G, U_D, I_out) = {mat_str(t1.M, 6)}")
Dt, Dst = cramer(t1.M, t1.r)
P(f"  det = {fz(Dt, 9)} (= -jωC_gs = {fz(-1j*2*math.pi*100e6*Cgs, 9)}); D_Iout = {fz(Dst[2], 6)} (= g_m I_in)")
P(f"  β = I_out/I_in = {fz(xt1[2])} (Betrag {abs(xt1[2]):.3f}); Formel -g_m/(jωC_gs) = {fz(-gm/(1j*2*math.pi*100e6*Cgs))}")
wT = gm / Cgs
P(f"ω_T = g_m/C_gs = {wT:.3e} 1/s, f_T = {wT/(2*math.pi)/1e9:.4f} GHz")
for fx in (10e6, 100e6, 1e9, wT / (2 * math.pi), 10e9):
    _, x_ = beta_mna(2 * math.pi * fx)
    P(f"  f = {fx/1e6:9.1f} MHz: |β| = {abs(x_[2]):8.3f}, Winkel {math.degrees(cmath.phase(x_[2])):+.1f}°")
wT2 = gm / math.sqrt(Cgs ** 2 + 2 * Cgs * Cgd)
P(f"mit C_gd = 20 fF: β = -(g_m - jωC_gd)/(jω(C_gs + C_gd)); |β| = 1 bei ω_T = g_m/sqrt(C_gs(C_gs + 2C_gd)) = "
  f"{wT2:.4e} 1/s, f_T = {wT2/(2*math.pi)/1e9:.4f} GHz; Näherung g_m/(2π(C_gs+C_gd)) = "
  f"{gm/(2*math.pi*(Cgs+Cgd))/1e9:.4f} GHz ({(gm/(Cgs+Cgd)-wT2)/wT2*100:+.2f} %)")
_, x_ = beta_mna(wT2, Cgd)
P(f"  Probe MNA bei ω_T: |β| = {abs(x_[2]):.6f}")
for fx in (10e6, 100e6, 1e9, 10e9):
    _, x_ = beta_mna(2 * math.pi * fx, Cgd)
    P(f"  mit C_gd: f = {fx/1e6:8.1f} MHz: |β| = {abs(x_[2]):.4f}")
P(f"  mit C_gd: Grenzwert für hohe Frequenzen C_gd/(C_gs + C_gd) = {Cgd/(Cgs+Cgd):.4f}")
# ohne Strommesser wäre der Drain offen: U_D = -g_m U_G/g_o
P(f"  ohne Strommesser (Drain offen, nur g_o): U_D = -g_m/g_o · U_G = {-gm/go:.1f} · U_G; mit Strommesser U_D = 0")

# ------------------------------------------------------------------ U. Nullor: invertierender Verstärker
kopf("U. Nullor: invertierender Verstärker R_1 = 10 kOhm, R_2 = 100 kOhm, U_E = 0,1 V (mS, kOhm, V, mA)")
u_ = MNA(["1", "2"], ["I_E", "I_o"])
u_.spannungszweig("1", "0", "I_E", uq=0.1, zq=10.0)     # Quelle mit R_1 als Tor
u_.admittanz("1", "2", 0.01)                           # R_2
u_.nullor("0", "1", "2", "0", "I_o")                    # Pluseingang an Masse, Minuseingang Knoten 1, Ausgang Knoten 2
xu = u_.loesen()
Du, Dsu = cramer(u_.M, u_.r)
P(f"M (Spalten U_1, U_2, I_E, I_o) = {np.round(u_.M.real, 4).tolist()}; rechte Seite {np.round(u_.r.real, 4).tolist()}")
P(f"  det M = {Du.real:.6f} (= -R_1 G_2 = {-10*0.01:.4f}); D_2 = {Dsu[1].real:.6f} (= U_E)")
P(f"  U_1 = {xu[0].real:.6f} V, U_2 = {xu[1].real:.6f} V, I_E = {xu[2].real*1e3:.4f} µA, I_o = {xu[3].real*1e3:.4f} µA; "
  f"Verstärkung {xu[1].real/0.1:.4f}")
t_ = entwicklung(u_.M, zeile=3)
P(f"  Entwicklung nach der Nullor-Zeile: {np.round(np.real(t_), 6).tolist()}")
M2 = u_.M.copy()
M2[:, 1] = u_.r
P(f"  M_2 = {np.round(M2.real, 4).tolist()}, Entwicklung nach Zeile 4: {np.round(np.real(entwicklung(M2, zeile=3)), 6).tolist()}")
for vD in (1e3, 2e5, 1e6):
    uv = MNA(["1", "2"], ["I_E", "I_o"])
    uv.spannungszweig("1", "0", "I_E", uq=0.1, zq=10.0)
    uv.admittanz("1", "2", 0.01)
    uv.vcvs("2", "0", "0", "1", "I_o", vD)              # U_2 = v_D (U_+ - U_-) mit U_+ = 0, U_- = U_1
    xv = uv.loesen()
    formel = -10 / (1 + 11 / vD)
    P(f"  endliche Leerlaufverstärkung v_D = {vD:.0e}: U_2/U_E = {xv[1].real/0.1:.6f} (Formel -10/(1 + 11/v_D) = "
      f"{formel:.6f}), U_1 = {xv[0].real*1e6:.3f} µV, Abweichung {(xv[1].real/0.1+10)/10*100:+.4f} %")
uv = MNA(["1", "2"], ["I_E", "I_o"])
uv.spannungszweig("1", "0", "I_E", uq=0.1, zq=10.0)
uv.admittanz("1", "2", 0.01)
uv.vcvs("2", "0", "0", "1", "I_o", 2e5)
P(f"  M mit VCVS v_D = 2e5: Zeile 4 = {np.round(uv.M[3].real, 4).tolist()}; geteilt durch v_D: "
  f"{np.round(uv.M[3].real/2e5, 6).tolist()}")
# Mitkopplung: Eingänge vertauscht (Plus an Knoten 1, Minus an Masse)
um = MNA(["1", "2"], ["I_E", "I_o"])
um.spannungszweig("1", "0", "I_E", uq=0.1, zq=10.0)
um.admittanz("1", "2", 0.01)
um.nullor("1", "0", "2", "0", "I_o")
xm = um.loesen()
P(f"  Eingänge vertauscht (mitgekoppelt), Nullor: det = {np.linalg.det(um.M).real:.4f}, U_2 = {xm[1].real:.6f} V, "
  f"I_E = {xm[2].real*1e3:.4f} µA (statische Lösung wie gegengekoppelt)")
for vD in (2e5, 1e6):
    um2 = MNA(["1", "2"], ["I_E", "I_o"])
    um2.spannungszweig("1", "0", "I_E", uq=0.1, zq=10.0)
    um2.admittanz("1", "2", 0.01)
    um2.vcvs("2", "0", "1", "0", "I_o", vD)
    xm2 = um2.loesen()
    P(f"  Eingänge vertauscht, VCVS v_D = {vD:.0e}: U_2/U_E = {xm2[1].real/0.1:.6f} (endlich)")

# ------------------------------------------------------------------ V. Frequenzgang: Determinante im Nenner
kopf("V. Frequenzgang der Verstärkerstufe: Pole als Nullstellen der Determinante (SI-Einheiten)")
CL = 10e-12
Gout = GD + GL + go
wi, wo = Gqv / Cgs, Gout / CL
A0 = -gm / Gout
P(f"ohne R_S (Source an Masse): G_sig = {Gqv*1e3:.1f} mS, C_gs = 100 fF, G_out = G_D + G_L + g_o = {Gout*1e3:.3f} mS, "
  f"C_L = 10 pF")
P(f"  D = (G_sig + jωC_gs)(G_out + jωC_L); U_G = I_sig/(G_sig + jωC_gs); U_D = -g_m I_sig/D")
P(f"  ω_i = G_sig/C_gs = {wi:.4e} 1/s (f_i = {wi/2/math.pi/1e6:.3f} MHz); ω_o = G_out/C_L = {wo:.4e} 1/s "
  f"(f_o = {wo/2/math.pi/1e6:.4f} MHz)")
P(f"  Gleichspannungsverstärkung -g_m/G_out = {A0:.4f} = {20*math.log10(abs(A0)):.3f} dB")


def H_ohneRS(wx):
    return A0 / ((1 + 1j * wx / wi) * (1 + 1j * wx / wo))


def H_mna(wx):
    v_ = MNA(["G", "D"], [])
    v_.stromquelle("G", "0", 10e-3 * Gqv)
    v_.admittanz("G", "0", Gqv + 1j * wx * Cgs)
    v_.vccs("D", "0", "G", "0", gm)
    v_.admittanz("D", "0", Gout + 1j * wx * CL)
    x_ = v_.loesen()
    return x_[1] / 10e-3, x_[0] / 10e-3, np.linalg.det(v_.M)


for fx in (100e3, 1e6, wo / 2 / math.pi, 10e6, 100e6, wi / 2 / math.pi, 1e9, 10e9):
    wx = 2 * math.pi * fx
    H, HG, Dv = H_mna(wx)
    P(f"  f = {fx/1e6:10.4f} MHz: |U_D/u_sig| = {abs(H):.5f} ({20*math.log10(abs(H)):+7.2f} dB), Winkel "
      f"{math.degrees(cmath.phase(H)):+8.2f}°; Formel {abs(H_ohneRS(wx)):.5f}; |U_G/u_sig| = {abs(HG):.5f}")
# Einsfrequenz
lo, hi = 1e6, 1e9
for _ in range(200):
    mid = math.sqrt(lo * hi)
    if abs(H_ohneRS(2 * math.pi * mid)) > 1:
        lo = mid
    else:
        hi = mid
P(f"  |U_D/u_sig| = 1 bei f = {lo/1e6:.3f} MHz; Verstärkungs-Bandbreite-Produkt |A_0| f_o = {abs(A0)*wo/2/math.pi/1e6:.3f} MHz "
  f"= g_m/(2π C_L) = {gm/(2*math.pi*CL)/1e6:.3f} MHz")
P(f"  Asymptoten: oberhalb f_o fällt |H| um 20 dB/Dekade: f = 35,81 MHz -> {20*math.log10(abs(H_ohneRS(2*math.pi*wo/2/math.pi*10))):.2f} dB, "
  f"bei f_o selbst {20*math.log10(abs(H_ohneRS(wo))):.2f} dB (Asymptote {20*math.log10(abs(A0)):.2f} dB, Differenz "
  f"{20*math.log10(abs(H_ohneRS(wo)))-20*math.log10(abs(A0)):.3f} dB)")
P(f"  Einzelpol: |1/(1 + j)| = {1/math.sqrt(2):.5f} = {20*math.log10(1/math.sqrt(2)):.4f} dB, Winkel -45°")
P(f"  Gatespannung bei ω_G: 10 mV · |1/(1 + j)| = {10*abs(1/(1+1j)):.3f} mV")
# nur G_L verdoppelt
Gout2 = GD + 2 * GL + go
P(f"  nur G_L verdoppelt: G_out = {Gout2*1e3:.3f} mS, Verstärkung {gm/Gout2:.4f}, f_D = {Gout2/CL/2/math.pi/1e6:.4f} MHz, "
  f"Produkt {gm/Gout2*Gout2/CL/2/math.pi/1e6:.3f} MHz; ganzer Leitwert am Drain verdoppelt: Verstärkung "
  f"{gm/(2*Gout):.4f}, f_D = {2*Gout/CL/2/math.pi/1e6:.4f} MHz")
# Bode-Datenreihe für die Abbildung
P("  Datenreihe (f in Hz, |H| in dB, Winkel in Grad, |U_G/u_sig| in dB):")
for ex in np.arange(5, 10.01, 0.5):
    fx = 10 ** ex
    H, HG, _ = H_mna(2 * math.pi * fx)
    P(f"    {fx:9.3e} {20*math.log10(abs(H)):+8.2f} {math.degrees(cmath.phase(H)):+8.2f} {20*math.log10(abs(HG)):+8.2f}")
# mit R_S: drei Knoten, C_gs zwischen G und S
P("mit R_S = 1 kOhm (C_gs zwischen G und S, C_L an D):")


def Y_mitRS(s):
    Y = np.array([[Gqv + s * Cgs, 0, -s * Cgs],
                  [gm, GD + GL + go + s * CL, -(gm + go)],
                  [-gm - s * Cgs, -go, gm + go + GS + s * Cgs]], dtype=complex)
    return Y


# det als Polynom in s (Grad 2): an drei Stellen auswerten und anpassen
ss = np.array([0.0, 1e8, 2e8])
dets = np.array([np.linalg.det(Y_mitRS(s)) for s in ss])
koeff = np.polyfit(ss, dets.real, 2)
wurzeln = np.roots(koeff)
P(f"  det Y(s) = {koeff[0]:.4e} s^2 + {koeff[1]:.4e} s + {koeff[2]:.4e} (S^3); Nullstellen s = "
  f"{[f'{x.real:.4e}' for x in wurzeln]} 1/s -> Eckfrequenzen {[f'{-x.real/2/math.pi/1e6:.3f} MHz' for x in wurzeln]}")
for fx in (100e3, 1e6, 10e6, 100e6):
    s = 2j * math.pi * fx
    U = np.linalg.solve(Y_mitRS(s), np.array([10e-3 * Gqv, 0, 0]))
    P(f"  f = {fx/1e6:7.2f} MHz: |U_D/u_sig| = {abs(U[1])/10e-3:.4f}")

# ------------------------------------------------------------------ W. Singuläre Fälle
kopf("W. Singuläre Fälle")
w_ = MNA(["1"], ["I_a", "I_b"])
w_.spannungszweig("1", "0", "I_a", uq=1.0)
w_.spannungszweig("1", "0", "I_b", uq=2.0)
P(f"Zwei ideale Spannungsquellen 1 V und 2 V parallel: M = {np.round(w_.M.real, 1).tolist()}, det = {np.linalg.det(w_.M).real:.1f}")
w_ = MNA(["1"], ["I_a", "I_b"])
w_.spannungszweig("1", "0", "I_a", uq=1.0)
w_.spannungszweig("1", "0", "I_b", uq=1.0)
P(f"  zwei gleiche (1 V und 1 V): det = {np.linalg.det(w_.M).real:.1f}, Gleichungen widerspruchsfrei, Aufteilung des Stroms "
  f"unbestimmt")
P("Vollständige Leitwertmatrix (mit Bezugsknoten): det = 0, weil Y·(1,…,1) = 0 (Abschnitt O)")
# Zusatz: Strom-gesteuerte Quellen (Probe der Muster)
kopf("X. Probe der Muster für stromgesteuerte Quellen")
x_ = MNA(["1", "2"], ["I_m"])
x_.stromquelle("1", "0", 0.001)               # 1 µA in Knoten 1
x_.spannungszweig("1", "0", "I_m", uq=0.0, zq=1.0)   # 1 kOhm als Impedanz mit Strom I_m (Steuerstrom)
x_.cccs("2", "0", "I_m", 100.0)               # 100 I_m von Knoten 2 nach Masse
x_.admittanz("2", "0", 0.1)                   # 10 kOhm Last
xx = x_.loesen()
P(f"CCCS β = 100: Steuerstrom I_m = {xx[2].real*1e3:.4f} µA durch 1 kOhm, Strom der Quelle {100*xx[2].real*1e3:.1f} µA, "
  f"U_2 = {xx[1].real:.4f} V (Formel -100·1 µA·10 kOhm = -1 V)")
y_ = MNA(["1", "2"], ["I_m", "I_h"])
y_.stromquelle("1", "0", 0.001)
y_.spannungszweig("1", "0", "I_m", uq=0.0, zq=1.0)
y_.ccvs("2", "0", "I_m", "I_h", 5.0)          # U_2 = 5 kOhm · I_m
y_.admittanz("2", "0", 0.1)
xy = y_.loesen()
P(f"CCVS r_m = 5 kOhm: U_2 = {xy[1].real*1e3:.4f} mV (Formel 5 kOhm · 1 µA = 5 mV), Strom der CCVS I_h = "
  f"{xy[3].real*1e3:.4f} µA")

# ------------------------------------------------------------------ Y. Begleitmodell als Eintragsmuster (Abschnitt D)
kopf("Y. Newton-Schritt der MOS-Diode als Eintragsmuster: Leitwert g und Stromquelle I_eq (mS, V, mA)")
Uk_ = 2.0                                   # Schätzung U^(1) aus Abschnitt D
g_ = g_mos(Uk_) * 1e3
Ieq_ = i_mos(Uk_) * 1e3 - g_ * Uk_
P(f"Schätzung U = {Uk_:.4f} V: I = {i_mos(Uk_)*1e3:.4f} mA, g = {g_:.4f} mS, I_eq = I - g U = {Ieq_:.4f} mA")
yb = MNA(["1"], [])
yb.stromquelle("1", "0", Iq * 1e3)          # 0,5 mA in den Knoten
yb.admittanz("1", "0", Gq * 1e3)            # 0,25 mS
yb.admittanz("1", "0", g_)                  # Begleitmodell: Leitwert ...
yb.stromquelle("0", "1", Ieq_)              # ... und Strom I_eq von Knoten 1 nach 0 durch das Bauelement
xb = yb.loesen()
P(f"  Muster: Y = {fz(yb.M[0,0])} mS, rechte Seite = {fz(yb.r[0])} mA -> neue Schätzung U = {fz(xb[0])} V "
  f"(Abschnitt D: 1,3077 V)")
