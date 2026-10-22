"""Zahlenwerk für ET1 Kap. 2 „Physikalische Grundprinzipien“ (Größen und Einheiten), Stil 3.

Quellen der Konstanten: SI-Broschüre des BIPM (9. Auflage 2019, Ergänzung der Vorsätze durch die 27. CGPM 2022),
CODATA 2018 für die Gravitationskonstante; Erdmasse und mittlerer Erdradius als Näherungswerte (IAU/IUGG).
Alle Rechenbeispiele sind eigene; Rechenregeln wie M · m = k sind Allgemeinwissen. Keine Aufgaben aus Skript oder Übung.

Aufruf:  python -I zahlen_grundprinzipien.py > zahlen_grundprinzipien.txt
"""
import math
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = print

# ------------------------------------------------------------------ definierende Konstanten des SI (exakt seit 2019)
DNU_CS = 9_192_631_770          # Hz, Hyperfeinübergang Cäsium-133
C0 = 299_792_458                # m/s, Lichtgeschwindigkeit
H = 6.626_070_15e-34            # J s, Planck-Konstante
E = 1.602_176_634e-19           # C, Elementarladung
KB = 1.380_649e-23              # J/K, Boltzmann-Konstante
NA = 6.022_140_76e23            # 1/mol, Avogadro-Konstante
KCD = 683                       # lm/W, Photometrisches Strahlungsäquivalent monochromatischer Strahlung von 540e12 Hz

G_N = 9.806_65                  # m/s², Normfallbeschleunigung (Konvention)
GAMMA = 6.674_30e-11            # m³/(kg s²), Gravitationskonstante (CODATA 2018)
M_ERDE = 5.972e24               # kg
R_ERDE = 6.371e6                # m, mittlerer Radius
G_RECHEN = 9.81                 # m/s², Rechenwert in den Beispielen
G_AEQUATOR = 9.780_325          # m/s², Normalschwere am Äquator (WGS-84)
G_POL = 9.832_185               # m/s², Normalschwere an den Polen (WGS-84)

# Daten der Geschichte, die in den Artikeln vorkommen (keine Rechnung, nur Nachweis an einer Stelle)
DATEN = (
    ("Cavendish misst mit der Drehwaage die Anziehung von Bleikugeln", 1798),
    ("Urkilogramm in Sèvres wird Definition des Kilogramms", 1889),
    ("Vorsätze zetta, zepto, yotta, yocto (19. CGPM)", 1991),
    ("SI-Reform: sieben definierende Konstanten, in Kraft am 20. Mai", 2019),
    ("Vorsätze ronna, quetta, ronto, quecto (27. CGPM)", 2022),
)


def bericht():
    P("=" * 100)
    P("ET1 Kap. 2: Physikalische Größen und Einheiten")
    P("=" * 100)

    P("1) Definierende Konstanten (exakt):")
    for name, wert in (("Delta nu_Cs in Hz", DNU_CS), ("c in m/s", C0), ("h in J s", H), ("e in C", E),
                       ("k in J/K", KB), ("N_A in 1/mol", NA), ("K_cd in lm/W", KCD)):
        P(f"   {name}: {wert}")
    P(f"   1 s = {DNU_CS} Schwingungen des Cs-Übergangs; Licht legt 1 m in 1/{C0} s = {1/C0*1e9:.4f} ns zurück")

    P("2) Ampere über die Elementarladung:")
    pro_a = 1 / E
    P(f"   1 A = {pro_a:.9e} Elementarladungen je Sekunde")
    for name, i in (("Sperrstrom der Beispieldiode 20 pA", 20e-12), ("1 pA", 1e-12), ("OPV-Ruhestrom 80 nA", 80e-9),
                    ("LED 20 mA", 20e-3), ("1 fA (Elektrometer)", 1e-15)):
        P(f"   {name}: {i/E:.3e} Elementarladungen je Sekunde")
    n_us = 1e-12 * 1e-6 / E
    P(f"   1 pA in 1 µs: im Mittel {n_us:.2f} Ladungen; relative Schwankung 1/sqrt(N) = {1/math.sqrt(n_us):.2f} "
      "(Poisson, Schrotrauschen)")

    P("3) Zahlenwert mal Einheit, Netzspannung 230 V:")
    U = 230.0
    P(f"   {U} V = {U/1e3} kV = {U*1e3:.0f} mV = {U*1e3:.1e} mV; Zahlenwert und Einheit ändern sich gegenläufig")

    P("4) Abgeleitete Einheiten: Volt aus P = U I, Ohm aus R = U/I (Basiseinheiten):")
    P("   W = J/s = N m/s = kg m^2 s^-3;  V = W/A = kg m^2 s^-3 A^-1;  Ohm = V/A = kg m^2 s^-3 A^-2")
    P("   F = C/V = A s/V = A^2 s^4 kg^-1 m^-2;  H = V s/A = kg m^2 s^-2 A^-2;  Wb = V s;  T = Wb/m^2 = kg s^-2 A^-1")
    P_foehn, U_netz = 2100.0, 230.0
    P(f"   Föhn 2100 W an 230 V: I = P/U = {P_foehn/U_netz:.3f} A; R = U/I = {U_netz/(P_foehn/U_netz):.2f} Ohm")

    P("5) Vorsätze:")
    for name, faktor, einheit in (("1 km^2", 1e3**2, "m^2"), ("1 mm^2", 1e-3**2, "m^2"), ("1 cm^3", 1e-2**3, "m^3"),
                                  ("1 dm^3 (1 Liter)", 1e-1**3, "m^3")):
        P(f"   {name} = {faktor:.0e} {einheit}")
    P(f"   eigene Beispiele: 1 M * 1 m = {1e6*1e-3:.0e} (k); 1 m * 1 k = {1e-3*1e3:.0f}; 1 u * 1 u = {1e-6*1e-6:.0e} (p)")
    P(f"   7 N + 2 kN = {7 + 2000} N = {(7 + 2000)/1000} kN (nicht 9 kN); 2 A * 12 V = {2*12} V A = {2*12} W; "
      f"6 N m / 3 m = {6/3:.0f} N")
    P(f"   100 km/h * (1000 m/km) * (1 h/3600 s) = {100*1000/3600:.3f} m/s")
    P("   Vorsätze 1991 neu: zetta/zepto 1e21/1e-21, yotta/yocto 1e24/1e-24 (19. CGPM); 2022 neu (27. CGPM): ronna R 1e27, "
      "quetta Q 1e30, ronto r 1e-27, quecto q 1e-30")

    P("6) Energie eines Smartphone-Akkus, 4000 mAh bei 3,85 V Nennspannung:")
    Q_mAh, U_akku = 4000.0, 3.85
    Q_C = Q_mAh * 1e-3 * 3600
    W_Wh = Q_mAh * 1e-3 * U_akku
    P(f"   Ladung {Q_mAh} mAh = {Q_mAh*1e-3} Ah = {Q_C:.0f} C; Energie {W_Wh:.2f} Wh = {W_Wh*3600:.0f} J = {W_Wh*3600/1e3:.1f} kJ")
    P(f"   zum Vergleich: 1 kWh = {3.6e6:.1e} J; der Akku enthält {W_Wh/1000:.4f} kWh; ein Föhn mit 2100 W setzt das in "
      f"{W_Wh*3600/2100:.1f} s um")
    P(f"   Elementarladungen in 4000 mAh: {Q_C/E:.2e}")

    P("7) Kinematik: E-Auto von 0 auf 100 km/h in 6,0 s, konstante Beschleunigung:")
    v_end, t_end = 100 / 3.6, 6.0
    a = v_end / t_end
    P(f"   100 km/h = {v_end:.3f} m/s; a = {a:.3f} m/s^2 = {a/G_N:.3f} g")
    for t in (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
        P(f"   t = {t:.0f} s: v = {a*t:.2f} m/s = {a*t*3.6:.1f} km/h, s = {0.5*a*t*t:.2f} m")
    P(f"   Weg nach 6 s: 1/2 a t^2 = {0.5*a*t_end**2:.2f} m; mittlere Geschwindigkeit mal Zeit: {v_end/2*t_end:.2f} m")
    s = lambda t: 0.5 * a * t * t  # noqa: E731
    for t1, t2 in ((3.0, 5.0), (3.0, 4.0), (3.0, 3.1), (3.0, 3.01)):
        P(f"   Sekante [{t1}, {t2}] s: (s2 - s1)/dt = {(s(t2)-s(t1))/(t2-t1):.3f} m/s")
    P(f"   Tangente bei 3 s: v(3 s) = {a*3:.3f} m/s")
    P(f"   falsche Formel s = a t ergäbe {a*t_end:.2f} 'm' – Einheit m/s, kein Weg")
    P(f"   wörtliches Doppelintegral des Skripts mit innerer Grenze t1: a (t1 - t0)^2 = {a*t_end**2:.1f} m statt {0.5*a*t_end**2:.1f} m")

    P("8) Freier Fall eines Smartphones aus 1,5 m (ohne Luftwiderstand):")
    h = 1.5
    t_fall = math.sqrt(2 * h / G_RECHEN)
    P(f"   t = sqrt(2 h/g) = {t_fall:.3f} s; v = g t = {G_RECHEN*t_fall:.2f} m/s = {G_RECHEN*t_fall*3.6:.1f} km/h")

    P("9) Kraft und Gravitation:")
    P(f"   Gewichtskraft 1 kg: {1*G_RECHEN:.2f} N; 20 kg: {20*G_RECHEN:.1f} N")
    g_aus_gesetz = GAMMA * M_ERDE / R_ERDE**2
    P(f"   g aus dem Gravitationsgesetz: gamma M/R^2 = {g_aus_gesetz:.3f} m/s^2 (Normwert {G_N}; Abweichung durch "
      "Erdrotation und Abplattung)")
    f_11 = GAMMA * 1 * 1 / 1**2
    P(f"   zwei Massen je 1 kg im Abstand 1 m: F = {f_11:.3e} N; Gewichtskraft von 1 kg ist {G_RECHEN/f_11:.2e}-mal größer")
    P(f"   Einheit von gamma: m^3/(kg s^2) = N m^2/kg^2")
    P(f"   Normalschwere WGS-84: Äquator {G_AEQUATOR} m/s^2, Pole {G_POL} m/s^2 (gerundet 9,78 und 9,83); "
      f"Normwert {G_N} liegt dazwischen")
    P(f"   in 6371 km Höhe (doppelter Abstand vom Mittelpunkt): g/4 = {g_aus_gesetz/4:.3f} m/s^2")

    P("10) Arbeit: Koffer 20 kg auf 3 m Höhe, über Treppe oder Rampe (12 m lang):")
    m, hh, L = 20.0, 3.0, 12.0
    W = m * G_RECHEN * hh
    sin_a = hh / L
    alpha = math.degrees(math.asin(sin_a))
    F_rampe = m * G_RECHEN * sin_a
    P(f"   W = m g h = {W:.1f} J; Rampe: Steigungswinkel {alpha:.2f} Grad, Kraft längs der Rampe {F_rampe:.2f} N, "
      f"mal 12 m = {F_rampe*L:.1f} J")
    P(f"   Treppe: senkrechte Anteile zusammen 3 m -> {W:.1f} J, waagrechte Anteile 0 J; Abbildung mit 6 Stufen zu "
      f"0,5 m: je {m*G_RECHEN*0.5:.1f} J")
    P(f"   Absenken um 3 m: Arbeit der Hand {-W:.1f} J; waagrecht tragen über 10 m: 0 J")
    ca = math.cos(math.radians(alpha))
    lw = math.sqrt(L**2 - hh**2)
    P(f"   Rampe, Kräfte (Faktenprüfung F2): Normalkraft {m*G_RECHEN*ca:.2f} N; Handkraft waagrecht {F_rampe*ca:.2f} N, "
      f"senkrecht {F_rampe*sin_a:.2f} N; waagrechter Weg {lw:.2f} m; Arbeit der Hand waagrecht {F_rampe*ca*lw:.1f} J + "
      f"senkrecht {F_rampe*sin_a*hh:.1f} J = {F_rampe*ca*lw + F_rampe*sin_a*hh:.1f} J; Schwerkraft {-W:.1f} J auf jedem Weg")
    F_zug, s_zug, winkel = 50.0, 20.0, 30.0
    P(f"   Schlitten: 50 N unter 30 Grad über 20 m: W = F s cos(alpha) = {F_zug*s_zug*math.cos(math.radians(winkel)):.1f} J; "
      f"Kraftanteil längs des Weges {F_zug*math.cos(math.radians(winkel)):.2f} N")
    P(f"   Leistung: Treppe in 5 s: {W/5:.1f} W; Rampe in 15 s: {W/15:.1f} W")
    P(f"   Energie in Wattsekunden: {W:.1f} J = {W:.1f} W s = {W/3600:.4f} Wh")
    P("   Skript-Beispiel Bild 2.4 (nur zur Prüfung der Korrektur): 13 m in Feldrichtung, 1 kg, g = 10 m/s^2 -> "
      f"Arbeit der Schwerkraft {1*10*13} J, potentielle Energie nimmt um {1*10*13} J ab")

    P("11) Daten:")
    for was, jahr in DATEN:
        P(f"   {jahr}: {was}")
    P("12) Literaturwerte (nicht gerechnet): Kopien des Urkilogramms wichen über rund 100 Jahre um etwa 50 µg ab "
      "(Vergleiche des BIPM 1889 bis 1989/1992); Neudefinition der Sekunde über optische Übergänge in Vorbereitung "
      "(CIPM-Fahrplan)")


if __name__ == "__main__":
    bericht()
