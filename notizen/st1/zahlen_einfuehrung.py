"""Zahlenwerk für Schaltungstechnik, Einführung: „Von der Röhre zum integrierten Schaltkreis“ (Stil 3).

Quellen der Werte (Sachquellen, keine Aufgaben):
- Triode ECC83/12AX7, typische Datenblattwerte je System: U_a = 250 V, U_g = -2 V, I_a = 1,2 mA, mu = 100,
  S = 1,6 mA/V, R_i = 62,5 kOhm; Heizung 6,3 V / 0,3 A (parallel) bzw. 12,6 V / 0,15 A (Serie) für beide Systeme.
- Transistorzahlen: Herstellerangaben von Intel (zusammengestellt u. a. in der Wikipedia-Tabelle „Transistor count“);
  Core 2 Duo „Conroe“ 291 Mio., 65 nm, 143 mm², Juli 2006, E6600 2,4 GHz, TDP 65 W; Xeon 7500 „Nehalem-EX“ 2,3 Mrd.,
  45 nm, 8 Kerne, 2010; 8008: 3500 Transistoren, 10 µm, PMOS, 1972.
- Moore 1965 („Cramming more components onto integrated circuits“): Verdopplung je Jahr, 2^6 = 64 Bauelemente 1965,
  Extrapolation 2^16 = 65 536 für 1975; 1975 Revision auf zwei Jahre.
- ENIAC: 17 468 Röhren, etwa 150 kW, etwa 5 Millionen Lötstellen.
- Halbleiterdaten wie im ET1-Zahlenwerk (notizen/get1/zahlen_halbleiter.py): Si W_g = 1,12 eV, n_i = 1e10 cm^-3;
  Ge W_g = 0,66 eV, n_i = 2,0e13 cm^-3; I_S der ET1-Beispieldiode Si 1,46e-14 A, Ge 5,83e-8 A.
- Grenztemperaturen: AC128 (Ge) T_j,max = 100 °C, BC547 (Si) T_j,max = 150 °C (Datenblätter).
- UKW-Rundfunk 87,5 bis 108 MHz, Zwischenfrequenz 10,7 MHz; Mittelwelle 9 kHz Kanalraster, ZF 455 kHz.
- NMOS-Transitfrequenz im 180-nm-Knoten 50 bis 70 GHz (Literaturwerte für HF-CMOS-Prozesse).
Alle Rechenbeispiele sind eigene. Aufruf:  python -I zahlen_einfuehrung.py > zahlen_einfuehrung.txt
"""
import math
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = print
LN2 = math.log(2)


def kopf(t):
    P()
    P("=" * 100)
    P(t)
    P("=" * 100)


# ------------------------------------------------------------------ A. Triode ECC83 (ein System)
kopf("A. Triode ECC83: Steuerspannung, Durchgriff, Barkhausen, Verstärkerstufe, Leistungsbilanz")
Ua, Ug, Ia = 250.0, -2.0, 1.2e-3
mu = 100.0
D = 1 / mu
S = 1.6e-3
Ri = 62.5e3
P(f"Arbeitspunkt U_a = {Ua:.0f} V, U_g = {Ug:.1f} V, I_a = {Ia*1e3:.2f} mA; mu = {mu:.0f}, D = 1/mu = {D:.3f}")
P(f"S = {S*1e3:.2f} mA/V, R_i = {Ri/1e3:.1f} kOhm; Barkhausen S*D*R_i = {S*D*Ri:.4f}; S*R_i = {S*Ri:.1f} = mu")
P(f"1 V am Gitter wirkt wie {mu:.0f} V an der Anode; 50 V mehr an der Anode verschieben die Kennlinie um {50*D:.2f} V")

# Kennlinienmodell: I_a = K (U_g + D U_a + U_0)^(3/2), an Strom und Steilheit im Arbeitspunkt angepasst
u_ap = 1.5 * Ia / S                       # wirksame Steuerspannung, aus S = 1,5 I/u
U0 = u_ap - (Ug + D * Ua)
K = Ia / u_ap ** 1.5
P(f"Kennlinienmodell 3/2-Potenz: u_st(AP) = 1,5 I/S = {u_ap:.4f} V, U_0 = {U0:.4f} V (Kontaktspannung/Anlaufeffekt),"
  f" K = {K*1e3:.5f} mA/V^1,5")


def ia(ug, ua):
    u = ug + D * ua + U0
    return K * u ** 1.5 if u > 0 else 0.0


P("Kennlinienschar I_a(U_g) in mA (Abbildung Triodenkennlinien):")
for ua in (150.0, 200.0, 250.0):
    werte = [f"{ia(ug, ua)*1e3:5.3f}" for ug in (-4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0)]
    P(f"  U_a = {ua:3.0f} V, U_g = -4 ... 0 V in 0,5-V-Schritten: {' '.join(werte)};"
      f" Sperrpunkt U_g = {-(D*ua+U0):.3f} V")
h = 1e-4
S_num = (ia(Ug + h, Ua) - ia(Ug - h, Ua)) / (2 * h)
Ri_num = 2 * h * 100 / (ia(Ug, Ua + 100 * h) - ia(Ug, Ua - 100 * h))
P(f"Probe numerisch im AP: S = {S_num*1e3:.4f} mA/V, R_i = {Ri_num/1e3:.2f} kOhm")
P(f"Strom bei U_g = -1 V statt -2 V (U_a = 250 V): {ia(-1, 250)*1e3:.3f} mA; bei U_a = 350 V statt 250 V (U_g = -2 V):"
  f" {ia(-2, 350)*1e3:.3f} mA (350 V liegt über der Grenzspannung 300 V, nur Modellprobe)")
P(f"Gleicher Strom bei 100 V weniger Anodenspannung: U_a = 150 V, U_g = -1 V -> {ia(-1, 150)*1e3:.3f} mA"
  f" (wie 250 V, -2 V: {ia(-2, 250)*1e3:.3f} mA)")
P(f"Konkrete Steilheit: U_g -2,0 -> -1,9 V bei 250 V: Linearisierung S*0,1 V = {S*0.1*1e3:.3f} mA"
  f" (Modell: {(ia(-1.9, 250)-ia(-2.0, 250))*1e3:.4f} mA); U_a +6,25 V: 6,25 V/R_i = {6.25/Ri*1e3:.3f} mA"
  f" (Modell: {(ia(-2, 256.25)-ia(-2, 250))*1e3:.4f} mA)")
kB_eV = 8.617333262e-5
for TK in (300.0, 1000.0):
    P(f"Boltzmann-Faktor exp(-1 eV/kT) bei {TK:.0f} K: {math.exp(-1/(kB_eV*TK)):.2e}")
P(f"Verhältnis 1000 K zu 300 K: {math.exp(-1/(kB_eV*1000))/math.exp(-1/(kB_eV*300)):.2e}; 1000 K = {1000-273.15:.0f} °C")
P(f"Richardson-Gleichung J ~ T^2 exp(-W_A/kT): Verhältnis 1000 K zu 300 K = "
  f"{(1000/300)**2 * math.exp(-1/(kB_eV*1000))/math.exp(-1/(kB_eV*300)):.2e} (Faktor T^2 = {(1000/300)**2:.1f})")
P(f"Heizleistung je System 0,945 W gegen U_a I_a = 0,3 W an der Röhre: Faktor {0.945/0.3:.2f}")

Ra = 100e3
par = Ri * Ra / (Ri + Ra)
v = -S * par
P(f"Stufe mit R_a = {Ra/1e3:.0f} kOhm: R_i||R_a = {par/1e3:.2f} kOhm, v = -S (R_i||R_a) = {v:.2f};"
  f" Kontrolle mu R_a/(R_a+R_i) = {mu*Ra/(Ra+Ri):.2f}; Leerlauf (R_a -> unendlich): -mu = {-mu:.0f}")
ug_amp = 0.1
P(f"Eingang 0,1 V Amplitude -> Anodenstrom-Amplitude {S*ug_amp*1e3:.3f} mA (bei festgehaltener Anodenspannung),"
  f" Ausgangsamplitude {abs(v)*ug_amp:.3f} V")
UB = Ua + Ia * Ra
P_heiz_2 = 6.3 * 0.3
P_heiz = P_heiz_2 / 2
P_B = UB * Ia
P_sig = (abs(v) * ug_amp) ** 2 / (2 * Ra)
P(f"Betriebsspannung U_B = U_a + I_a R_a = {UB:.0f} V; Gleichleistung aus U_B: {P_B*1e3:.0f} mW;"
  f" an der Röhre U_a I_a = {Ua*Ia*1e3:.0f} mW")
P(f"Heizleistung: beide Systeme {P_heiz_2:.2f} W, je System {P_heiz:.3f} W")
P(f"Signalleistung im Arbeitswiderstand (Amplitude {abs(v)*ug_amp:.2f} V): {P_sig*1e3:.3f} mW;"
  f" Anteil an Heiz- plus Gleichleistung {P_sig/(P_heiz+P_B):.2e}")

# ------------------------------------------------------------------ B. Rückkopplung
kopf("B. Rückkopplung: v' = A/(1 - kA) (Mitkopplung), v' = A/(1 + kA) (Gegenkopplung)")
A = abs(v)
for kA in (0.0, 0.5, 0.9, 0.99):
    P(f"  kA = {kA:4.2f}: Mitkopplung v'/A = {1/(1-kA):7.2f}, v' = {A/(1-kA):8.1f};"
      f" Gegenkopplung v'/A = {1/(1+kA):.4f}, v' = {A/(1+kA):6.2f}")
P(f"Selbsterregung bei kA = 1: k = 1/A = {1/A:.5f} = {100/A:.2f} % des Ausgangs zurückführen")
kG = 0.1
for dA in (0.2,):
    A2 = A * (1 - dA)
    P(f"Gegenkopplung k = {kG}: v' = {A/(1+kG*A):.4f}; A um {dA*100:.0f} % kleiner ({A2:.2f}) -> v' = {A2/(1+kG*A2):.4f}"
      f" ({(A2/(1+kG*A2))/(A/(1+kG*A))*100-100:+.2f} %)")

# ------------------------------------------------------------------ C. Mischung und Überlagerungsempfänger
kopf("C. Überlagerungsempfänger: Mischprodukte, Zwischenfrequenz, Spiegelfrequenz, Güte")
fE, fZF = 100.0, 10.7
fLO = fE + fZF
P(f"UKW: f_E = {fE} MHz, f_LO = {fLO} MHz -> Differenz {fLO-fE:.1f} MHz, Summe {fLO+fE:.1f} MHz;"
  f" Spiegelfrequenz f_LO + f_ZF = {fLO+fZF:.1f} MHz = f_E + 2 f_ZF")
band = (87.5, 108.0)
P(f"Band {band[0]} bis {band[1]} MHz, Breite {band[1]-band[0]:.1f} MHz < 2 f_ZF = {2*fZF:.1f} MHz;"
  f" Spiegel des untersten Senders {band[0]+2*fZF:.1f} MHz, des obersten {band[1]+2*fZF:.1f} MHz")
B_UKW = 0.2
P(f"Güte für B = {B_UKW*1e3:.0f} kHz: bei f_E {fE/B_UKW:.0f}, bei der ZF {fZF/B_UKW:.1f}")
hub = 0.075
P(f"Frequenzhub UKW ±{hub*1e3:.0f} kHz: Sender {fE-hub:.3f} bis {fE+hub:.3f} MHz -> ZF {fLO-(fE+hub):.3f} bis"
  f" {fLO-(fE-hub):.3f} MHz (Hub bleibt ±75 kHz, Richtung gespiegelt bei LO oberhalb)")
fE_MW, fZF_MW, B_MW = 1000.0, 455.0, 9.0
P(f"Mittelwelle: f_E = {fE_MW:.0f} kHz, f_LO = {fE_MW+fZF_MW:.0f} kHz, Spiegel {fE_MW+2*fZF_MW:.0f} kHz;"
  f" Güte für {B_MW:.0f} kHz: {fE_MW/B_MW:.0f} bei f_E, {fZF_MW/B_MW:.1f} bei der ZF")
# Probe der Identität an einem Zeitpunkt
t = 1.234e-9
a, b = 2 * math.pi * fLO * 1e6 * t, 2 * math.pi * fE * 1e6 * t
P(f"Probe cos a cos b = 1/2 cos(a-b) + 1/2 cos(a+b) bei t = 1,234 ns: {math.cos(a)*math.cos(b):.6f} ="
  f" {0.5*math.cos(a-b)+0.5*math.cos(a+b):.6f}")

# ------------------------------------------------------------------ D. Röhre gegen Transistor
kopf("D. Röhre gegen Transistor: Heizleistung, ENIAC")
N_C2D = 291e6
P_C2D = 65.0
P(f"291 Mio. Triodensysteme zu {P_heiz:.3f} W Heizleistung: {N_C2D*P_heiz/1e6:.0f} MW;"
  f" Verhältnis zur Aufnahme des Core 2 Duo ({P_C2D:.0f} W): {N_C2D*P_heiz/P_C2D:.2e}")
N_ENIAC, P_ENIAC = 17468, 150e3
P(f"ENIAC: {N_ENIAC} Röhren, {P_ENIAC/1e3:.0f} kW -> {P_ENIAC/N_ENIAC:.1f} W je Röhre (ganze Anlage);"
  f" etwa 5 Millionen Lötstellen -> {5e6/N_ENIAC:.0f} je Röhre")

# ------------------------------------------------------------------ E. Germanium gegen Silizium
kopf("E. Germanium gegen Silizium")
ni_Si, ni_Ge = 1e10, 2.0e13
P(f"n_i: Si {ni_Si:.1e}, Ge {ni_Ge:.1e} cm^-3 -> Verhältnis {ni_Ge/ni_Si:.0f}, Quadrat {(ni_Ge/ni_Si)**2:.1e}")
IS_Si, IS_Ge = 1.46e-14, 5.83e-8
P(f"I_S der ET1-Beispieldiode: Si {IS_Si:.2e} A, Ge {IS_Ge:.2e} A -> Verhältnis {IS_Ge/IS_Si:.2e}")
I_gen_Si = 19.9e-12            # Generationsstrom der ET1-Beispieldiode bei -1 V (zahlen_halbleiter.txt)
I_gen_Ge = I_gen_Si * ni_Ge / ni_Si   # Generationsstrom proportional n_i (gleiche Zonenweite und Lebensdauer angenommen)
I_rev_Si, I_rev_Ge = I_gen_Si + IS_Si, I_gen_Ge + IS_Ge
P(f"Sperrstrom bei -1 V mit Generation: Si {I_rev_Si:.3e} A (Generation {I_gen_Si:.2e} A, ideal {IS_Si:.2e} A);"
  f" Ge {I_rev_Ge:.3e} A (Generation {I_gen_Ge:.2e} A, ideal {IS_Ge:.2e} A) -> Verhältnis {I_rev_Ge/I_rev_Si:.0f}")
P("Schmelzpunkte: Ge 938 °C, Si 1414 °C; T_j,max AC128 (Ge) 90 bis 100 °C (Angaben schwanken), BC547 (Si) 150 °C")
P("Beweglichkeiten bei 300 K (schwach dotiert, cm^2/(V s)): Ge Elektronen 3900, Löcher 1900; Si Elektronen 1400,"
  f" Löcher 450 -> Elektronen Faktor {3900/1400:.1f}, Löcher {1900/450:.1f}")
B_BC547 = 500
P(f"Bipolartransistor wie im ET1-Zahlenwerk: B = {B_BC547}, Basisstrom = Kollektorstrom/{B_BC547}"
  f" = {100/B_BC547:.1f} % des Kollektorstroms")

# ------------------------------------------------------------------ F. Mooresches Gesetz
kopf("F. Mooresches Gesetz: Verdopplungszeit, Gegenproben")
P(f"Moore 1965: 2^6 = {2**6} (1965) -> zehn Verdopplungen -> 2^16 = {2**16} (1975)")
daten = [(1971, 2300, "4004"), (1972, 3500, "8008"), (1974, 4500, "8080"), (1978, 29000, "8086"),
         (1982, 134000, "80286"), (1985, 275000, "80386"), (1989, 1180235, "80486"), (1993, 3.1e6, "Pentium"),
         (1997, 7.5e6, "Pentium II"), (2000, 42e6, "Pentium 4"), (2006, 291e6, "Core 2 Duo"),
         (2010, 2.3e9, "Xeon 7500 (8 Kerne)")]
for j, n, name in daten:
    P(f"  {j}  {name:22s} {n:14,.0f}  log2 = {math.log2(n):6.3f}")
# Ausgleichsgerade log2 N = a + t/T2
xs = [j for j, _, _ in daten]
ys = [math.log2(n) for _, n, _ in daten]
xm, ym = sum(xs) / len(xs), sum(ys) / len(ys)
steig = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)
P(f"Ausgleichsgerade durch alle {len(daten)} Punkte (log2 N über dem Jahr): Steigung {steig:.4f} je Jahr"
  f" -> T_2 = {1/steig:.2f} Jahre; Wachstum je Jahr Faktor {2**steig:.3f}")
for jj in (1971, 1972, 1990, 2006, 2010):
    P(f"  Ausgleichsgerade im Jahr {jj}: N = {2 ** (ym + steig * (jj - xm)):.3e}")


def t2(t1, n1, t2_, n2):
    return (t2_ - t1) * LN2 / math.log(n2 / n1)


f1 = 291e6 / 3500
P(f"8008 (1972, 3500) -> Core 2 Duo (2006, 291 Mio.): Faktor {f1:,.0f}, log2 = {math.log2(f1):.3f}"
  f" Verdopplungen in 34 Jahren -> T_2 = {t2(1972, 3500, 2006, 291e6):.3f} Jahre")
f2 = 2.3e9 / 3500
P(f"8008 (1972) -> Xeon 7500 (2010, 2,3 Mrd.): Faktor {f2:,.0f}, log2 = {math.log2(f2):.3f} in 38 Jahren"
  f" -> T_2 = {t2(1972, 3500, 2010, 2.3e9):.3f} Jahre")
P(f"Mit genauen Daten April 1972 -> Juli 2006 (34,25 Jahre): T_2 = {34.25*LN2/math.log(f1):.3f} Jahre")
for T in (1.0, 1.5, 2.0):
    n = 3500 * 2 ** (34 / T)
    P(f"  Gegenprobe 1972 -> 2006 mit T_2 = {T} Jahre: {n:.3e} Transistoren, Faktor {n/291e6:.3g} gegenüber 291 Mio.")
P(f"Vorhersage 2010 aus Core 2 Duo mit T_2 = 2,08 Jahre: {291e6*2**(4/t2(1972,3500,2006,291e6)):.3e}")
P(f"Verdopplung alle 2 Jahre: Faktor je Jahr {2**0.5:.4f} (+{(2**0.5-1)*100:.1f} %), in 10 Jahren {2**5}, in 20 Jahren {2**10}")
P(f"Dichte Core 2 Duo: {291e6/143:.3e} Transistoren je mm² -> {143e6/291e6:.3f} µm² je Transistor"
  f" (Quadrat mit {math.sqrt(143e6/291e6):.3f} µm Kantenlänge, Verdrahtung und Speicher eingerechnet)")
k_node = 10e-6 / 65e-9
P(f"Strukturgröße 10 µm -> 65 nm: Faktor {k_node:.1f}, Fläche {k_node**2:,.0f}; Generationen zu 0,7: "
  f"{math.log(k_node)/math.log(1/0.7):.1f} in 34 Jahren -> {34/(math.log(k_node)/math.log(1/0.7)):.2f} Jahre je Generation")
P(f"0,7 linear -> Fläche {0.7**2:.2f}; Knotenfolge 180 -> 130 -> 90 -> 65 -> 45 nm, Verhältnisse "
  + ", ".join(f"{b/a:.3f}" for a, b in ((180, 130), (130, 90), (90, 65), (65, 45))))

# ------------------------------------------------------------------ G. CMOS: Umladeleistung
kopf("G. CMOS: Energie je Umschaltung, Leistung, Ruhestrom, Skalierung")
C, U, f = 1e-15, 1.0, 3e9
P(f"Knoten C = 1 fF, U = 1 V: aus der Quelle je Laden Q U = C U^2 = {C*U*U*1e15:.2f} fJ, gespeichert"
  f" {0.5*C*U*U*1e15:.2f} fJ, im PMOS verheizt {0.5*C*U*U*1e15:.2f} fJ; beim Entladen im NMOS {0.5*C*U*U*1e15:.2f} fJ")
P(f"P = C U^2 f bei 3 GHz: {C*U*U*f*1e6:.2f} µW je Knoten, der in jeder Periode einmal lädt und entlädt")
N, alpha = 1e8, 0.1
P(f"Chip: {N:.0e} Knoten, Anteil {alpha} lädt je Takt: P = alpha N C U^2 f = {alpha*N*C*U*U*f:.1f} W")
I_ruhe = 1e-6
P(f"Hypothetischer Ruhestrom 1 µA je Gatter bei 1 V: {N*I_ruhe*U:.0f} W")
P(f"Skalieren: doppelte Spannung -> Faktor {2**2}, doppelte Frequenz -> Faktor 2, halbe Kapazität -> Faktor 0,5")
P(f"Core 2 Duo E6600: 65 W auf 143 mm² = {65/1.43:.1f} W/cm²; Herdplatte 2 kW auf 18 cm Durchmesser:"
  f" {2000/(math.pi*9**2):.2f} W/cm² -> Verhältnis {65/1.43/(2000/(math.pi*9**2)):.1f}")

# ------------------------------------------------------------------ H. Skalierung (Dennard) und Laufzeit
kopf("H. Skalierung bei konstanter Feldstärke (Dennard) und Laufzeit")
for kappa in (math.sqrt(2), 2.0):
    P(f"kappa = {kappa:.3f}: Länge, Spannung, Kapazität x{1/kappa:.3f}; Strom x{1/kappa:.3f};"
      f" Schaltzeit x{1/kappa:.3f}, Frequenz x{kappa:.3f}; Leistung je Transistor x{1/kappa**2:.3f};"
      f" Transistoren je Fläche x{kappa**2:.3f}; Leistung je Fläche x{(1/kappa**2)*kappa**2:.3f}")
C0, U0g, f0 = 2e-15, 1.4, 1e9
k2 = math.sqrt(2)
P0 = C0 * U0g ** 2 * f0
P1 = (C0 / k2) * (U0g / k2) ** 2 * (f0 * k2)
P(f"Beispielgatter 2 fF, 1,4 V, 1 GHz: P = {P0*1e6:.3f} µW; nach einem Knoten (kappa = sqrt 2): C = {C0/k2*1e15:.3f} fF,"
  f" U = {U0g/k2:.3f} V, f = {f0*k2/1e9:.3f} GHz, P = {P1*1e6:.3f} µW (Verhältnis {P1/P0:.3f})")
P(f"Umladeleistung 5 V statt 1 V: Faktor {5**2/1**2:.0f}; Chipbeispiel 30 W -> {30*25:.0f} W")
d_NN = 0.543 * math.sqrt(3) / 4
P(f"Abstand nächster Nachbarn im Siliziumgitter: {d_NN:.3f} nm (Gitterkonstante 0,543 nm)")
vsat = 1e7          # cm/s, Sättigungsgeschwindigkeit der Elektronen in Si
L180 = 180e-7       # cm
tau = L180 / vsat
P(f"Laufzeit durch 180 nm bei v_sat = 1e7 cm/s: {tau*1e12:.2f} ps -> 1/(2 pi tau) = {1/(2*math.pi*tau)/1e9:.0f} GHz"
  " (obere Schranke, real 50 bis 70 GHz wegen parasitärer Kapazitäten)")
P(f"f_T 50 bis 70 GHz gegen 2 GHz Mobilfunk: Faktor {50/2:.0f} bis {70/2:.0f}; gegen 2,4 GHz Bluetooth:"
  f" {50/2.4:.0f} bis {70/2.4:.0f}")
UT = 1.380649e-23 * 300 / 1.602176634e-19
P(f"Unterschwellsteigung ideal U_T ln 10 bei 300 K: {UT*math.log(10)*1e3:.1f} mV je Dekade")
P(f"Takt Desktop-Prozessoren: 1990 rund 33 MHz (i486), 2004 3,8 GHz (Pentium 4): Faktor {3.8e9/33e6:.0f};"
  f" 2023/24 Spitzentakt etwa 6 GHz: Faktor {6/3.8:.2f} in rund 20 Jahren")
P(f"Periode bei 3 GHz: {1/3e9*1e12:.0f} ps")
P(f"Matching: absolute Toleranz integrierter Widerstände 10 bis 20 %, Verhältnis benachbarter gleicher etwa 0,1 %"
  f" -> Faktor {10/0.1:.0f} bis {20/0.1:.0f}; ganze I/Q-Zweige ohne Abgleich etwa 1 % und 1°")
eps, th = 0.01, math.radians(1)
P(f"Spiegelunterdrückung I/Q etwa 4/(eps^2 + theta^2) bei 1 % und 1°: {4/(eps**2+th**2):.0f}"
  f" = {10*math.log10(4/(eps**2+th**2)):.1f} dB")
P("Intel 65-nm-Prozess (Core 2 Duo): Gatelänge 35 nm; Prozessorleistung von wenigen W (8086, i486) bis rund 100 W"
  " (Pentium 4, 2004, bis 115 W TDP); Versorgungsspannung 5 V bis Anfang der 1990er-Jahre")
P(f"Rückkopplungsbeispiel gerundet: -61,5/0,5 = {-61.5/0.5:.1f}, -61,5/0,1 = {-61.5/0.1:.1f}")
