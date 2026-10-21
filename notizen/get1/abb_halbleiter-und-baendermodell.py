"""Abbildungen zum Thema „Halbleiter und das Bändermodell“ (beide Fassungen).

Alle Zahlen kommen aus zahlen_halbleiter.py. Ausgabe: SVG nach web/wissen/img/get1/, PNG-Vorschau in den Ordner,
der als erstes Argument übergeben wird (sonst neben dieses Skript in _vorschau/).
Aufruf:  python -I abb_halbleiter-und-baendermodell.py <vorschau-ordner> [nummer …]
"""
import math
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
import numpy as np                                    # noqa: E402
import matplotlib                                     # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                       # noqa: E402
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Polygon   # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator   # noqa: E402
import zahlen_halbleiter as Z                         # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
SLUG = "halbleiter-und-baendermodell"
OUT = HIER.parents[1] / "web" / "wissen" / "img" / "get1"
OUT.mkdir(parents=True, exist_ok=True)
VOR = Path(sys.argv[1]) if len(sys.argv) > 1 else HIER / "_vorschau"
VOR.mkdir(parents=True, exist_ok=True)
NUR = {int(a) for a in sys.argv[2:]}

C_E, C_H, C_MIN, C_FELD = "#1f5fbf", "#c0392b", "#e08a1e", "#2e8b57"
C_RLZ, C_BAND, C_TXT, C_GRAU = "#ebebeb", "#333333", "#222222", "#6b6b6b"
C_VOLL = "#cfd8e6"                                    # besetzte Zustände
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12, "mathtext.fontset": "dejavusans",
    "axes.linewidth": 0.8, "axes.edgecolor": "#555", "axes.labelcolor": C_TXT, "text.color": C_TXT,
    "xtick.color": "#555", "ytick.color": "#555", "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "path", "savefig.facecolor": "white", "figure.facecolor": "white"})
KOMMA = FuncFormatter(lambda v, p: f"{v:g}".replace(".", ","))


def speichern(fig, n):
    fig.savefig(OUT / f"{SLUG}-{n}.svg", bbox_inches="tight", pad_inches=0.08)
    fig.savefig(VOR / f"{SLUG}-{n}.png", dpi=110, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("geschrieben:", f"{SLUG}-{n}")


def elektron(ax, x, y, r=0.022, farbe=C_E, z=5):
    ax.add_patch(Circle((x, y), r, color=farbe, zorder=z))


def loch(ax, x, y, r=0.024, farbe=C_H, z=5):
    ax.add_patch(Circle((x, y), r, facecolor="white", edgecolor=farbe, lw=1.4, zorder=z))


def pfeil(ax, a, b, farbe, lw=1.6, stil="-|>", ms=12, rad=0.0, z=6):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=stil, mutation_scale=ms, color=farbe, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}", zorder=z, shrinkA=0, shrinkB=0))


def doppelpfeil(ax, x, y0, y1, farbe=C_GRAU, lw=1.0):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="<|-|>", mutation_scale=9, color=farbe, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=6))


# ---------------------------------------------------------------- 1: Gesamtbild
def abb1():
    fig = plt.figure(figsize=(6.4, 5.9))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 1.15], hspace=0.42, wspace=0.12)
    rng = np.random.default_rng(3)

    def kleinbild(ax, titel, WF, ne, nh):
        ax.set_xlim(0, 1.3)
        ax.set_ylim(-0.5, 1.62)
        ax.axis("off")
        ax.add_patch(Rectangle((0.04, -0.5), 0.92, 0.5, color=C_VOLL, lw=0))
        ax.plot([0.04, 0.96], [0, 0], color=C_BAND, lw=1.5)
        ax.plot([0.04, 0.96], [Z.Wg, Z.Wg], color=C_BAND, lw=1.5)
        ax.plot([0.04, 0.96], [WF, WF], color=C_GRAU, lw=1.1, ls=(0, (4, 3)))
        ax.text(0.65, 1.72, titel, ha="center", va="bottom", fontsize=11.5)
        ax.text(1.0, Z.Wg, "$W_L$", fontsize=10.5, va="center", ha="left")
        ax.text(1.0, 0.0, "$W_V$", fontsize=10.5, va="center", ha="left")
        ax.text(1.0, WF, "$W_F$", fontsize=10.5, va="center", ha="left", color=C_GRAU)
        xs = np.linspace(0.12, 0.86, max(ne, 1))
        for i in range(ne):
            elektron(ax, xs[i] + rng.uniform(-0.03, 0.03), Z.Wg + 0.07 + rng.uniform(0, 0.12), r=0.03)
        xs = np.linspace(0.12, 0.86, max(nh, 1))
        for i in range(nh):
            loch(ax, xs[i] + rng.uniform(-0.03, 0.03), -0.07 - rng.uniform(0, 0.12), r=0.032)

    a1, a2, a3 = (fig.add_subplot(gs[0, i]) for i in range(3))
    WFn = Z.Wg - Z.kT * math.log(Z.NL / Z.ND)        # 0,209 eV unter W_L
    WFp = Z.kT * math.log(Z.NV / Z.NA)               # 0,194 eV über W_V (N_V < N_L: nicht symmetrisch)
    kleinbild(a1, "(a) reines Si", Z.Wg - Z.WL_Wi, 2, 2)
    doppelpfeil(a1, 0.5, 0.0, Z.Wg)
    a1.text(0.55, 0.30, "$W_g$ =\n1,12 eV", fontsize=10, ha="left", va="center")
    kleinbild(a2, "(b) n-dotiert", WFn, 7, 0)
    kleinbild(a3, "(c) p-dotiert", WFp, 0, 7)

    ax = fig.add_subplot(gs[1, :])
    pr = Z.gleichgewicht_profil()
    x = pr["x"] * 1e4
    ax.axvspan(-Z.xn0 * 1e4, Z.xp0 * 1e4, color=C_RLZ, lw=0)
    ax.fill_between(x, pr["WV"], -1.6, color=C_VOLL, lw=0)
    ax.plot(x, pr["WL"], color=C_BAND, lw=1.6)
    ax.plot(x, pr["WV"], color=C_BAND, lw=1.6)
    ax.axhline(0, color=C_GRAU, lw=1.1, ls=(0, (4, 3)))
    for xx in np.linspace(-0.44, -0.26, 6):
        elektron(ax, xx, pr["WL"][0] + 0.08 + rng.uniform(0, 0.1), r=0.011)
    for xx in np.linspace(0.26, 0.42, 6):
        loch(ax, xx, pr["WV"][-1] - 0.08 - rng.uniform(0, 0.1), r=0.012)
    doppelpfeil(ax, 0.47, pr["WL"][0], pr["WL"][-1], C_TXT, 1.1)
    ax.plot([0.25, 0.5], [pr["WL"][0], pr["WL"][0]], color=C_GRAU, lw=0.8, ls=":")
    ax.text(0.49, (pr["WL"][0] + pr["WL"][-1]) / 2, "  $e\\,U_\\mathrm{Diff}$ = 0,714 eV", fontsize=10.5, va="center")
    ax.text(-0.585, pr["WL"][0] + 0.05, "$W_L$", fontsize=10.5, va="bottom")
    ax.text(-0.585, pr["WV"][0] - 0.05, "$W_V$", fontsize=10.5, va="top")
    ax.text(-0.02, 0.04, "$W_F$", fontsize=10.5, color=C_GRAU, va="bottom", ha="center")
    ax.text(-0.42, 1.25, "n-Gebiet", ha="center", fontsize=11)
    ax.text(0.0, 1.25, "Raum-\nladungszone", ha="center", fontsize=10, va="center")
    ax.text(0.42, 1.25, "p-Gebiet", ha="center", fontsize=11)
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-1.45, 1.55)
    ax.set_xlabel("Ort $x$ in µm")
    ax.set_ylabel("Energie in eV")
    ax.xaxis.set_major_formatter(KOMMA)
    ax.yaxis.set_major_formatter(KOMMA)
    ax.set_title("(d) pn-Übergang im Gleichgewicht", fontsize=11.5, pad=6)
    speichern(fig, 1)


# ---------------------------------------------------------------- 2: Einweggleichrichter
def abb2():
    fig, (ac, aw) = plt.subplots(1, 2, figsize=(6.8, 2.9), gridspec_kw=dict(width_ratios=[1.0, 1.3], wspace=0.42))
    ac.set_xlim(-0.25, 1.35)
    ac.set_ylim(0, 1.08)
    ac.axis("off")
    ac.add_patch(Circle((0.25, 0.5), 0.12, fill=False, lw=1.3, color=C_TXT))
    tt = np.linspace(-0.075, 0.075, 30)
    ac.plot(0.25 + tt, 0.5 + 0.04 * np.sin(tt / 0.075 * math.pi), color=C_TXT, lw=1.2)
    ac.plot([0.25, 0.25, 0.48], [0.62, 0.88, 0.88], color=C_TXT, lw=1.3)
    ac.add_patch(Polygon([[0.48, 0.80], [0.48, 0.96], [0.62, 0.88]], closed=True, fc="white", ec=C_TXT, lw=1.3))
    ac.plot([0.62, 0.62], [0.80, 0.96], color=C_TXT, lw=1.6)
    ac.plot([0.62, 0.95, 0.95], [0.88, 0.88, 0.67], color=C_TXT, lw=1.3)
    ac.add_patch(Rectangle((0.895, 0.33), 0.11, 0.34, fc="white", ec=C_TXT, lw=1.3))
    ac.plot([0.95, 0.95, 0.25, 0.25], [0.33, 0.12, 0.12, 0.38], color=C_TXT, lw=1.3)
    ac.text(0.55, 1.0, "D", ha="center", va="bottom", fontsize=11)
    ac.text(0.86, 0.50, "$R$ =\n1 kΩ", ha="right", va="center", fontsize=10.5)
    pfeil(ac, (0.05, 0.72), (0.05, 0.28), C_TXT, lw=1.1, ms=10)
    ac.text(0.02, 0.50, "$u_E$", ha="right", va="center", fontsize=11)
    pfeil(ac, (1.09, 0.72), (1.09, 0.28), C_TXT, lw=1.1, ms=10)
    ac.text(1.12, 0.50, "$u_A$", ha="left", va="center", fontsize=11)
    t = np.linspace(0, 40e-3, 4001)
    uE = 10 * np.sin(2 * math.pi * 50 * t)
    uA = np.zeros_like(uE)
    for i, u in enumerate(uE):
        if u <= 0:
            uA[i] = -Z.IS * 1e3
            continue
        lo, hi = 0.0, u
        for _ in range(60):
            m = (lo + hi) / 2
            if m + Z.UT * math.log(m / 1e3 / Z.IS + 1) > u:
                hi = m
            else:
                lo = m
        uA[i] = lo
    aw.axhline(0, color="#999", lw=0.7)
    aw.plot(t * 1e3, uE, color=C_GRAU, lw=1.2, ls=(0, (5, 3)))
    aw.plot(t * 1e3, uA, color=C_E, lw=2.0)
    aw.text(15.0, -12.0, "$u_E(t)$", color=C_GRAU, fontsize=11, ha="center", va="center")
    aw.text(11.0, 4.0, "$u_A(t)$", color=C_E, fontsize=11, ha="left")
    aw.annotate("Spitze 9,3 V\nstatt 10 V", xy=(25.3, 9.30), xytext=(30.5, 6.0), fontsize=10,
                arrowprops=dict(arrowstyle="-", color=C_GRAU, lw=0.8))
    aw.set_xlim(0, 40)
    aw.set_ylim(-13, 11)
    aw.set_xlabel("$t$ in ms")
    aw.set_ylabel("$u$ in V")
    aw.set_yticks([-10, -5, 0, 5, 10])
    speichern(fig, 2)


# ---------------------------------------------------------------- 3: Leiter, Halbleiter, Isolator
def abb3():
    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    rng = np.random.default_rng(5)
    breite = 1.3
    spalten = [(1.0, "Metall\n(Kupfer)", "$8{,}5\\cdot10^{22}$ freie\nElektronen pro cm³"),
               (3.0, "Halbleiter\n(Silizium)", "je $10^{10}$ Elektronen\nund Löcher pro cm³"),
               (5.0, "Isolator\n(Siliziumdioxid)", "praktisch keine")]
    x0 = 1.0 - breite / 2
    ax.add_patch(Rectangle((x0, -2.0), breite, 3.5, color=C_VOLL, lw=0))
    ax.add_patch(Rectangle((x0, -2.0), breite, 7.0, fill=False, ec=C_BAND, lw=1.2))
    ax.plot([x0, x0 + breite], [1.5, 1.5], color=C_GRAU, lw=1.1, ls=(0, (4, 3)))
    ax.text(x0 + breite + 0.06, 1.5, "$W_F$", va="center", fontsize=10.5, color=C_GRAU)
    ax.text(1.0, 3.3, "teilweise\nbesetzt", ha="center", va="center", fontsize=10)
    for xc, wl in ((3.0, Z.Wg), (5.0, 9.0)):
        xa = xc - breite / 2
        ax.add_patch(Rectangle((xa, -2.0), breite, 2.0, color=C_VOLL, lw=0))
        ax.add_patch(Rectangle((xa, -2.0), breite, 2.0, fill=False, ec=C_BAND, lw=1.2))
        ax.add_patch(Rectangle((xa, wl), breite, 11.0 - wl if xc > 4 else 5.0 - wl, fill=False, ec=C_BAND, lw=1.2))
        doppelpfeil(ax, xc + breite / 2 + 0.12, 0.0, wl)
        ax.text(xc + breite / 2 + 0.2, wl / 2, f"$W_g$\n{str(wl).replace('.', ',')} eV" if xc < 4 else "$W_g$\n≈ 9 eV",
                fontsize=10, va="center")
        ax.text(xc, -1.0, "Valenzband\nvoll", ha="center", va="center", fontsize=9.5)
        ax.text(xc, wl + 1.3 if xc < 4 else wl + 1.0, "Leitungsband\nleer", ha="center", va="center", fontsize=9.5)
    for xx in (2.62, 3.0, 3.38):
        elektron(ax, xx + rng.uniform(-0.05, 0.05), Z.Wg + 0.22, r=0.07)
        loch(ax, xx + rng.uniform(-0.05, 0.05), -0.22, r=0.075)
    for xc, name, zahl in spalten:
        ax.text(xc, -2.45, name, ha="center", va="top", fontsize=11)
        ax.text(xc, -3.85, zahl, ha="center", va="top", fontsize=9.8, color=C_GRAU)
    ax.set_xlim(0, 6.25)
    ax.set_ylim(-5.1, 11.3)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_yticks([-2, 0, 2, 4, 6, 8, 10])
    ax.set_ylabel("Energie $W$ in eV ($W_V$ = 0)")
    ax.spines["left"].set_bounds(-2, 11)
    speichern(fig, 3)


# ---------------------------------------------------------------- 4: Kristallgitter (schematisch)
def gitter(ax, titel):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.55, 4.15)
    ax.set_ylim(-0.75, 3.0)
    ax.text(1.8, 2.95, titel, ha="center", va="top", fontsize=11)
    return [(i * 1.2, j * 1.2) for i in range(4) for j in range(2)]


def bindungen(ax, auslassen=()):
    for i in range(4):
        for j in range(2):
            x, y = i * 1.2, j * 1.2
            for (dx, dy) in ((1, 0), (0, 1)):
                if (i + dx > 3) or (j + dy > 1):
                    continue
                key = (i, j, dx, dy)
                for s in (-1, 1):
                    if (key, s) in auslassen:
                        continue
                    if dx:
                        ax.plot([x + 0.3, x + 0.9], [y + s * 0.06, y + s * 0.06], color="#444", lw=1.1)
                    else:
                        ax.plot([x + s * 0.06, x + s * 0.06], [y + 0.3, y + 0.9], color="#444", lw=1.1)


def atom(ax, x, y, text="Si", fc="white", ec="#444"):
    ax.add_patch(Circle((x, y), 0.27, fc=fc, ec=ec, lw=1.1, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=9.5, zorder=4)


def abb4():
    fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.75), gridspec_kw=dict(wspace=0.05))
    # (a) reines Si, eine aufgebrochene Bindung
    ax = axs[0]
    gitter(ax, "(a) reines Silizium")
    bindungen(ax, auslassen={((1, 0, 1, 0), 1)})
    for i in range(4):
        for j in range(2):
            atom(ax, i * 1.2, j * 1.2)
    loch(ax, 1.8, 0.06, r=0.085)
    elektron(ax, 1.95, 0.72, r=0.075)
    pfeil(ax, (1.82, 0.16), (1.92, 0.62), C_E, lw=1.0, ms=8)
    # (b) Phosphor
    ax = axs[1]
    gitter(ax, "(b) mit Phosphor")
    bindungen(ax)
    for i in range(4):
        for j in range(2):
            atom(ax, i * 1.2, j * 1.2, *(("P⁺", "#f6d5d1") if (i, j) == (1, 1) else ("Si",)))
    ax.add_patch(Circle((1.2, 1.2), 0.62, fill=False, ls=(0, (3, 2)), ec=C_GRAU, lw=0.9, zorder=2))
    elektron(ax, 2.05, 2.05, r=0.075)
    pfeil(ax, (1.66, 1.64), (1.98, 1.98), C_E, lw=1.0, ms=8)
    # (c) Bor
    ax = axs[2]
    gitter(ax, "(c) mit Bor")
    bindungen(ax, auslassen={((2, 1, 1, 0), 1)})
    for i in range(4):
        for j in range(2):
            atom(ax, i * 1.2, j * 1.2, *(("B⁻", "#d6e2f5") if (i, j) == (1, 1) else ("Si",)))
    loch(ax, 3.0, 1.26, r=0.085)
    for ax in axs:
        ax.set_ylim(-0.45, 3.0)
    speichern(fig, 4)


# ---------------------------------------------------------------- 5: Wanderung eines Lochs
def abb5():
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    ax.set_xlim(-1.5, 8.6)
    ax.set_ylim(-3.2, 1.25)
    ax.axis("off")
    for zeile, k in enumerate((1, 2, 3)):
        y = -zeile * 1.0
        ax.text(-1.45, y, f"Moment {zeile + 1}", va="center", fontsize=10.5)
        for b in range(5):
            x = b * 1.6
            ax.plot([x, x + 1.0], [y, y], color="#999", lw=1.2)
            if b == k:
                loch(ax, x + 0.5, y, r=0.11)
            else:
                elektron(ax, x + 0.5, y, r=0.095)
        if zeile < 2:
            pfeil(ax, ((k + 1) * 1.6 + 0.42, y + 0.16), (k * 1.6 + 0.6, y + 0.16), C_E, lw=1.3, ms=10, rad=0.35)
    pfeil(ax, (5.2, 0.9), (7.6, 0.9), C_FELD, lw=2.2, ms=14)
    ax.text(7.7, 0.9, "Feld $\\vec E$", color=C_FELD, va="center", fontsize=11)
    ax.text(3.7, 0.55, "ein gebundenes Elektron springt gegen das Feld in die Lücke", ha="center", fontsize=9.5, color=C_E)
    pfeil(ax, (2.2, -2.75), (5.6, -2.75), C_H, lw=2.0, ms=13)
    ax.text(5.7, -2.75, "das Loch wandert\nmit dem Feld", color=C_H, va="center", fontsize=10)
    speichern(fig, 5)


# ---------------------------------------------------------------- 6: Eigenleitungsdichte über der Temperatur
def abb6():
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    TK = np.linspace(200, 720, 600)
    ax.semilogy(TK, Z.ni_von_T(TK), color=C_E, lw=2.0)
    ax.axhline(1e16, color=C_GRAU, lw=1.0, ls=(0, (5, 3)))
    ax.text(205, 2.2e16, "Dotierung der Beispieldiode: $10^{16}\\,\\mathrm{cm^{-3}}$", fontsize=10, color=C_GRAU)
    T16 = 655
    ax.plot([T16, T16], [1e5, 1e16], color=C_GRAU, lw=0.8, ls=":")
    ax.text(T16 - 6, 1e6, "655 K", ha="right", fontsize=10, color=C_GRAU)
    ax.plot([300], [1e10], "o", color=C_E, ms=6)
    ax.annotate("300 K: $n_i = 10^{10}\\,\\mathrm{cm^{-3}}$,\n+8,3 % pro Kelvin", xy=(300, 1e10), xytext=(330, 1e8),
                fontsize=10, arrowprops=dict(arrowstyle="-", color=C_GRAU, lw=0.8))
    ax.plot([400], [float(Z.ni_von_T(400))], "o", color=C_E, ms=5)
    ax.annotate("400 K: 525-mal so viel,\nnur noch +4,7 % pro Kelvin", xy=(400, float(Z.ni_von_T(400))),
                xytext=(430, 2e11), fontsize=10, arrowprops=dict(arrowstyle="-", color=C_GRAU, lw=0.8))
    ax.set_xlim(200, 720)
    ax.set_ylim(1e5, 1e18)
    ax.set_xlabel("Temperatur $T$ in K")
    ax.set_ylabel("$n_i$ in cm$^{-3}$")
    ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
    speichern(fig, 6)


# ---------------------------------------------------------------- 7: Fermi-Verteilung
def abb7():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 3.2), gridspec_kw=dict(wspace=0.38))
    dW = np.linspace(-0.3, 0.3, 601)
    a1.plot(dW, Z.fermi(dW, 0.0), color=C_E, lw=2.0)
    a1.plot([-0.3, 0, 0, 0.3], [1, 1, 0, 0], color=C_GRAU, lw=1.0, ls=(0, (4, 3)))
    a1.plot([0], [0.5], "o", color=C_E, ms=5)
    a1.text(0.02, 0.53, "1/2 bei $W_F$", fontsize=10)
    a1.text(0.04, 0.86, "gestrichelt:\n$T$ = 0", fontsize=9.5, color=C_GRAU)
    a1.set_xlabel("$W - W_F$ in eV")
    a1.set_ylabel("Besetzung $f(W)$")
    a1.set_title("(a) linear, 300 K", fontsize=11)
    a1.xaxis.set_major_formatter(KOMMA)
    a1.yaxis.set_major_formatter(KOMMA)
    dW2 = np.linspace(0.0, 0.7, 701)
    a2.semilogy(dW2, Z.fermi(dW2, 0.0), color=C_E, lw=2.0)
    a2.semilogy(dW2, np.exp(-dW2 / Z.kT), color=C_GRAU, lw=1.0, ls=(0, (4, 3)))
    a2.text(0.03, 1e-4, "Boltzmann\n$\\exp(-(W-W_F)/k_BT)$", fontsize=9.3, color=C_GRAU)
    WLWF = Z.Wg / 2 - Z.kT / 2 * math.log(Z.NV / Z.NL)
    a2.axvline(WLWF, color=C_BAND, lw=0.9)
    a2.text(WLWF - 0.015, 3e-2, "$W_L$ in\nreinem Si", ha="right", fontsize=9.5)
    a2.plot([WLWF], [math.exp(-WLWF / Z.kT)], "o", color=C_E, ms=5)
    a2.text(WLWF - 0.02, 8e-10, "$3\\cdot10^{-10}$", ha="right", fontsize=9.5)
    a2.set_xlabel("$W - W_F$ in eV")
    a2.set_title("(b) logarithmisch", fontsize=11)
    a2.set_ylim(1e-12, 2)
    a2.set_xlim(0, 0.7)
    a2.xaxis.set_major_formatter(KOMMA)
    speichern(fig, 7)


# ---------------------------------------------------------------- 8: Bänder im dotierten Silizium
def abb8():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.9), gridspec_kw=dict(wspace=0.08))
    rng = np.random.default_rng(11)
    Wi = Z.Wg / 2 + Z.kT / 2 * math.log(Z.NV / Z.NL)
    dWF = Z.kT * math.log(Z.ND / Z.ni)
    for ax, typ in zip(axs, ("n", "p")):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.42, 1.55)
        ax.axis("off")
        ax.add_patch(Rectangle((0.05, -0.42), 0.6, 0.42, color=C_VOLL, lw=0))
        ax.plot([0.05, 0.65], [0, 0], color=C_BAND, lw=1.5)
        ax.plot([0.05, 0.65], [Z.Wg, Z.Wg], color=C_BAND, lw=1.5)
        ax.plot([0.05, 0.65], [Wi, Wi], color=C_GRAU, lw=0.9, ls=":")
        # W_F aus der Formel mit N_L bzw. N_V, wie die Beschriftung (über n_i und W_i ergäbe sich 1,6 meV mehr)
        WF = Z.Wg - Z.kT * math.log(Z.NL / Z.ND) if typ == "n" else Z.kT * math.log(Z.NV / Z.NA)
        ax.plot([0.05, 0.65], [WF, WF], color=C_TXT, lw=1.2, ls=(0, (5, 3)))
        ax.text(0.67, Z.Wg, "$W_L$", va="center", fontsize=10.5)
        ax.text(0.67, 0.0, "$W_V$", va="center", fontsize=10.5)
        ax.text(0.67, Wi, "$W_i$ (Mitte)", va="center", fontsize=10, color=C_GRAU)
        ax.text(0.67, WF, "$W_F$", va="center", fontsize=10.5)
        doppelpfeil(ax, 0.58, Wi, WF, C_TXT, 0.9)
        ax.text(0.56, (Wi + WF) / 2, "0,36 eV", ha="right", va="center", fontsize=9.5)
        if typ == "n":
            lvl = Z.Wg - Z.WD_P
            for xx in np.linspace(0.13, 0.3, 3):
                ax.plot([xx - 0.03, xx + 0.03], [lvl, lvl], color=C_GRAU, lw=1.1)
            ax.text(0.085, lvl, "$W_D$", fontsize=9.5, color=C_GRAU, va="center", ha="right")
            for xx in np.linspace(0.1, 0.6, 8):
                elektron(ax, xx + rng.uniform(-0.02, 0.02), Z.Wg + 0.05 + rng.uniform(0, 0.12), r=0.017)
            ax.text(0.35, 1.5, "n-Silizium, $N_D = 10^{16}\\,\\mathrm{cm^{-3}}$", ha="center", fontsize=10.5)
            ax.text(0.35, -0.55, "$n = 10^{16}$, $p = 10^{4}\\,\\mathrm{cm^{-3}}$", ha="center", fontsize=10)
            doppelpfeil(ax, 0.58, WF, Z.Wg, C_TXT, 0.9)
            ax.text(0.56, (WF + Z.Wg) / 2, f"{Z.kT * math.log(Z.NL / Z.ND):.2f} eV".replace(".", ","), ha="right",
                    va="center", fontsize=9.5)
        else:
            lvl = Z.WA_B
            for xx in np.linspace(0.13, 0.3, 3):
                ax.plot([xx - 0.03, xx + 0.03], [lvl, lvl], color=C_GRAU, lw=1.1)
            ax.text(0.085, lvl, "$W_A$", fontsize=9.5, color=C_GRAU, va="center", ha="right")
            for xx in np.linspace(0.1, 0.6, 8):
                loch(ax, xx + rng.uniform(-0.02, 0.02), -0.06 - rng.uniform(0, 0.12), r=0.019)
            doppelpfeil(ax, 0.58, 0.0, WF, C_TXT, 0.9)
            ax.text(0.56, WF / 2, f"{Z.kT * math.log(Z.NV / Z.NA):.2f} eV".replace(".", ","), ha="right",
                    va="center", fontsize=9.5)
            ax.text(0.35, 1.5, "p-Silizium, $N_A = 10^{16}\\,\\mathrm{cm^{-3}}$", ha="center", fontsize=10.5)
            ax.text(0.35, -0.55, "$p = 10^{16}$, $n = 10^{4}\\,\\mathrm{cm^{-3}}$", ha="center", fontsize=10)
    speichern(fig, 8)


# ---------------------------------------------------------------- 9: Entstehung der Raumladungszone
def ion(ax, x, y, vz):
    farbe = C_H if vz > 0 else C_E
    ax.add_patch(Circle((x, y), 0.17, fc="white", ec=farbe, lw=1.1, zorder=3))
    ax.text(x, y, "+" if vz > 0 else "−", ha="center", va="center", fontsize=9, color=farbe, zorder=4,
            fontweight="bold")


def abb9():
    fig, ax = plt.subplots(figsize=(6.6, 6.0))
    ax.set_xlim(-0.3, 14.1)
    ax.set_ylim(-1.3, 8.6)
    ax.axis("off")
    # (a)
    ax.text(-0.2, 8.45, "(a) vor dem Kontakt: zwei neutrale Gebiete", fontsize=10.5, va="top")
    ax.add_patch(Rectangle((0, 6.0), 6.4, 1.7, fill=False, ec="#999", lw=0.9))
    ax.add_patch(Rectangle((7.4, 6.0), 6.4, 1.7, fill=False, ec="#999", lw=0.9))
    for x in np.arange(0.5, 6.1, 0.8):
        for y in (6.45, 7.25):
            ion(ax, x, y, +1)
            elektron(ax, x + 0.3, y + 0.18, r=0.07)
    for x in np.arange(7.9, 13.5, 0.8):
        for y in (6.45, 7.25):
            ion(ax, x, y, -1)
            loch(ax, x + 0.3, y + 0.18, r=0.075)
    ax.text(3.2, 5.7, "n-Gebiet", ha="center", va="top", fontsize=10)
    ax.text(10.6, 5.7, "p-Gebiet", ha="center", va="top", fontsize=10)
    # (b)
    ax.text(-0.2, 5.05, "(b) Kontakt: Elektronen und Löcher diffundieren und rekombinieren (×)", fontsize=10.5, va="top")
    ax.add_patch(Rectangle((0, 2.6), 13.8, 1.7, fill=False, ec="#999", lw=0.9))
    ax.plot([6.9, 6.9], [2.6, 4.3], color="#999", lw=0.9, ls=(0, (4, 3)))
    for x in np.arange(0.5, 5.4, 0.8):
        for y in (3.05, 3.85):
            ion(ax, x, y, +1)
            elektron(ax, x + 0.3, y + 0.18, r=0.07)
    for x in np.arange(8.6, 13.5, 0.8):
        for y in (3.05, 3.85):
            ion(ax, x, y, -1)
            loch(ax, x + 0.3, y + 0.18, r=0.075)
    for y in (3.05, 3.85):
        ion(ax, 6.1, y, +1)
        ion(ax, 7.7, y, -1)
        ax.text(6.9, y, "×", ha="center", va="center", fontsize=12)
    pfeil(ax, (4.8, 4.55), (8.6, 4.55), C_E, lw=1.5, ms=11)
    pfeil(ax, (9.0, 2.35), (5.2, 2.35), C_H, lw=1.5, ms=11)
    ax.text(8.75, 4.55, "Elektronen", color=C_E, va="center", fontsize=9.5)
    ax.text(5.05, 2.35, "Löcher", color=C_H, va="center", ha="right", fontsize=9.5)
    # (c)
    ax.text(-0.2, 1.65, "(c) Gleichgewicht: freigelegte Rümpfe, Gegenfeld", fontsize=10.5, va="top")
    ax.add_patch(Rectangle((4.9, -0.8), 4.0, 1.7, color=C_RLZ, lw=0))
    ax.add_patch(Rectangle((0, -0.8), 13.8, 1.7, fill=False, ec="#999", lw=0.9))
    for x in np.arange(0.5, 4.6, 0.8):
        for y in (-0.35, 0.45):
            ion(ax, x, y, +1)
            elektron(ax, x + 0.3, y + 0.18, r=0.07)
    for x in np.arange(9.5, 13.5, 0.8):
        for y in (-0.35, 0.45):
            ion(ax, x, y, -1)
            loch(ax, x + 0.3, y + 0.18, r=0.075)
    for x in (5.3, 6.1):
        for y in (-0.35, 0.45):
            ion(ax, x, y, +1)
    for x in (7.7, 8.5):
        for y in (-0.35, 0.45):
            ion(ax, x, y, -1)
    pfeil(ax, (5.2, 0.05), (8.6, 0.05), C_FELD, lw=2.0, ms=13, z=2)
    ax.text(6.9, 0.05, "$\\vec E$", color=C_FELD, ha="center", va="center", fontsize=11,
            bbox=dict(fc=C_RLZ, ec="none", pad=0.6), zorder=7)
    ax.text(2.4, -1.05, "n-Gebiet, neutral", ha="center", va="top", fontsize=9.5)
    ax.text(6.9, -1.05, "Raumladungszone", ha="center", va="top", fontsize=9.5)
    ax.text(11.4, -1.05, "p-Gebiet, neutral", ha="center", va="top", fontsize=9.5)
    speichern(fig, 9)


# ---------------------------------------------------------------- 10: Profile im Gleichgewicht (Poisson numerisch)
def abb10():
    pr = Z.gleichgewicht_profil()
    x = pr["x"] * 1e4
    fig, axs = plt.subplots(5, 1, figsize=(6.0, 8.4), sharex=True, gridspec_kw=dict(hspace=0.28))
    xn, xp = Z.xn0 * 1e4, Z.xp0 * 1e4
    for ax in axs:
        ax.axvspan(-xn, xp, color=C_RLZ, lw=0)
    a = axs[0]
    a.semilogy(x, pr["n"], color=C_E, lw=1.8)
    a.semilogy(x, pr["p"], color=C_H, lw=1.8)
    a.text(-0.57, 2e14, "Elektronen $n$", color=C_E, fontsize=10)
    a.text(0.57, 2e14, "Löcher $p$", color=C_H, fontsize=10, ha="right")
    a.set_ylim(1e2, 1e17)
    a.set_yticks([1e4, 1e10, 1e16])
    a.set_ylabel("(a) Dichte\nin cm$^{-3}$", fontsize=10.5)
    a = axs[1]
    rho_dep = np.where((pr["x"] > -Z.xn0) & (pr["x"] < 0), 1.0, np.where((pr["x"] > 0) & (pr["x"] < Z.xp0), -1.0, 0.0))
    a.plot(x, rho_dep, color=C_GRAU, lw=1.0, ls=(0, (4, 3)))
    a.plot(x, pr["rho"], color=C_TXT, lw=1.6)
    a.set_ylim(-1.3, 1.3)
    a.set_yticks([-1, 0, 1])
    a.set_ylabel("(b) $\\rho/(e\\,N)$", fontsize=10.5)
    a.text(0.27, 0.55, "gestrichelt:\nVerarmungsnäherung", fontsize=9, color=C_GRAU)
    a = axs[2]
    a.plot(x, pr["E"] / 1e3, color=C_FELD, lw=1.8)
    a.set_ylim(0, 36)
    a.set_ylabel("(c) $E$ in\nkV/cm", fontsize=10.5)
    a.text(0.25, 22, "Maximum 32 kV/cm", fontsize=9.5)
    a = axs[3]
    a.plot(x, pr["phi"], color=C_TXT, lw=1.6)
    a.set_ylim(-0.1, 0.85)
    a.set_yticks([0, 0.714])
    a.set_yticklabels(["0", "0,714"])
    a.set_ylabel("(d) $\\varphi$ in V", fontsize=10.5)
    a = axs[4]
    a.fill_between(x, pr["WV"], -1.3, color=C_VOLL, lw=0)
    a.plot(x, pr["WL"], color=C_BAND, lw=1.6)
    a.plot(x, pr["WV"], color=C_BAND, lw=1.6)
    a.axhline(0, color=C_GRAU, lw=1.0, ls=(0, (4, 3)))
    a.text(-0.57, pr["WL"][0] + 0.12, "$W_L$", fontsize=10)
    a.text(-0.57, pr["WV"][0] - 0.12, "$W_V$", fontsize=10, va="top")
    a.text(0.57, 0.06, "$W_F$", fontsize=10, ha="right", color=C_GRAU)
    a.set_ylim(-1.3, 1.25)
    a.set_ylabel("(e) Energie\nin eV", fontsize=10.5)
    a.set_xlabel("Ort $x$ in µm (links n-Gebiet, rechts p-Gebiet)")
    a.set_xlim(-0.6, 0.6)
    for ax in axs:
        ax.xaxis.set_major_formatter(KOMMA)
    for ax in axs[1:]:
        ax.yaxis.set_major_formatter(KOMMA) if ax is not axs[3] else None
    speichern(fig, 10)


# ---------------------------------------------------------------- 11: hinauf und hinunter (schematisch)
def stufe(xx, hoehe):
    s = np.clip((xx - 4.3) / 1.4, 0, 1)
    return hoehe * (3 * s**2 - 2 * s**3)


def abb11():
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    rng = np.random.default_rng(7)
    kTv, Wgv, h = 0.5, 3.0, 2.0
    xx = np.linspace(0, 10, 300)
    ax.axvspan(4.3, 5.7, color=C_RLZ, lw=0)
    ax.plot(xx, stufe(xx, h), color=C_BAND, lw=2.0)
    ax.plot(xx, stufe(xx, h) - Wgv, color=C_BAND, lw=2.0)
    NE = 150
    xe, we = rng.uniform(0.3, 3.9, NE), np.minimum(rng.exponential(kTv, NE), 4.0)
    xh, wh = rng.uniform(6.1, 9.7, NE), np.minimum(rng.exponential(kTv, NE), 4.0)
    for x_, w_ in zip(xe, we):
        hoch = w_ >= h
        ax.add_patch(Circle((x_, w_), 0.07 if hoch else 0.05, color=C_E if hoch else "#9db5dd", zorder=4))
    for x_, w_ in zip(xh, wh):
        hoch = w_ >= h
        ax.add_patch(Circle((x_, h - Wgv - w_), 0.075 if hoch else 0.055, fc="white",
                            ec=C_H if hoch else "#e3a49c", lw=1.3 if hoch else 0.9, zorder=4))
    for x_, w_ in zip((6.6, 7.6, 8.5, 9.3), (0.10, 0.35, 0.18, 0.55)):
        ax.add_patch(Circle((x_, h + w_), 0.09, color=C_MIN, zorder=5))
    for x_, w_ in zip((0.8, 1.7, 2.6, 3.4), (0.12, 0.40, 0.22, 0.50)):
        ax.add_patch(Circle((x_, -Wgv - w_), 0.095, fc="white", ec=C_MIN, lw=1.6, zorder=5))
    pfeil(ax, (2.4, 2.45), (6.9, 2.85), C_E, lw=2.0, ms=13, rad=-0.25)
    ax.text(2.2, 3.55, "hinauf: Elektronen mit\ngenug Energie (Diffusion)", color=C_E, ha="center", fontsize=10)
    pfeil(ax, (6.3, 2.12), (4.7, 0.5), C_MIN, lw=2.0, ms=13, rad=-0.1)
    ax.text(5.95, 0.72, "hinunter: jedes Minoritäts-\nelektron am Rand (Drift)", color=C_MIN, fontsize=9.8)
    pfeil(ax, (7.3, -3.4), (2.9, -3.85), C_H, lw=2.0, ms=13, rad=-0.25)
    ax.text(2.3, -4.75, "Löcher mit genug Energie\ntauchen hinüber (Diffusion)", color=C_H, ha="center", fontsize=9.8)
    pfeil(ax, (3.7, -3.05), (5.3, -1.45), C_MIN, lw=2.0, ms=13, rad=-0.1)
    ax.text(3.8, -2.25, "Minoritätslöcher\n(Drift)", color=C_MIN, ha="right", fontsize=9.8)
    ax.text(10.08, h, "$W_L$", va="center", fontsize=10.5)
    ax.text(10.08, h - Wgv, "$W_V$", va="center", fontsize=10.5)
    doppelpfeil(ax, 10.75, 0, h, C_GRAU, 1.0)
    ax.text(10.82, h / 2, "$e\\,U_\\mathrm{Diff}$", va="center", fontsize=10.5)
    ax.plot([5.7, 10.75], [0, 0], color=C_GRAU, lw=0.7, ls=":")
    ax.text(2.0, -5.95, "n-Gebiet", ha="center", fontsize=10.5)
    ax.text(5.0, -5.95, "RLZ", ha="center", fontsize=10.5)
    ax.text(8.0, -5.95, "p-Gebiet", ha="center", fontsize=10.5)
    pfeil(ax, (-0.25, -2.5), (-0.25, 4.2), C_GRAU, lw=1.0, ms=10)
    ax.text(-0.38, 1.0, "Energie der Elektronen", rotation=90, va="center", ha="right", fontsize=10, color=C_GRAU)
    ax.set_xlim(-0.9, 12.2)
    ax.set_ylim(-6.2, 4.6)
    ax.axis("off")
    speichern(fig, 11)


# ---------------------------------------------------------------- 12: Bänder bei 0 V, +0,5 V, −2 V
def abb12():
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 3.7), sharey=True, gridspec_kw=dict(wspace=0.08))
    WLn = Z.WL_Wi - Z.kT * math.log(Z.ND / Z.ni)      # W_L im n-Gebiet relativ zum Fermi-Niveau
    for ax, U, titel in zip(axs, (0.0, 0.5, -2.0), ("(a) $U$ = 0\nBarriere 0,714 eV", "(b) $U$ = +0,5 V\nBarriere 0,214 eV",
                                                     "(c) $U$ = −2 V\nBarriere 2,714 eV")):
        w = Z.weite(U)
        xn = xp = w / 2
        x = np.linspace(-1.0e-4, 1.0e-4, 801)
        stufe_ = Z.UDiff - U
        phi = np.where(x < -xn, stufe_, np.where(x < 0, stufe_ - Z.e * Z.ND / (2 * Z.eps) * (x + xn)**2,
              np.where(x < xp, Z.e * Z.NA / (2 * Z.eps) * (xp - x)**2, 0.0)))
        WL = WLn + (stufe_ - phi)
        ax.axvspan(-xn * 1e4, xp * 1e4, color=C_RLZ, lw=0)
        ax.fill_between(x * 1e4, WL - Z.Wg, -1.7, color=C_VOLL, lw=0)
        ax.plot(x * 1e4, WL, color=C_BAND, lw=1.6)
        ax.plot(x * 1e4, WL - Z.Wg, color=C_BAND, lw=1.6)
        ax.set_title(titel, fontsize=11)
        doppelpfeil(ax, 0.88, WLn, WLn + stufe_, C_TXT, 1.0)
        ax.plot([-0.2, 0.92], [WLn, WLn], color=C_GRAU, lw=0.7, ls=":")
        fak = {0.0: "×1", 0.5: "×2,5·10⁸", -2.0: "×10⁻³⁴"}[U]
        if U != -2.0:
            pfeil(ax, (-0.75, WLn + 0.1), (0.45, WLn + stufe_ + 0.1), C_E, lw=1.6, ms=10, rad=-0.35)
        ax.text(-0.95, 3.35, f"hinauf {fak}", color=C_E, fontsize=9.5, va="top")
        pfeil(ax, (0.75, WLn + stufe_ + 0.05), (-0.25, WLn + 0.12), C_MIN, lw=1.6, ms=10, rad=0.25)
        ax.text(-0.95, 2.95, "hinunter ×1", color=C_MIN, fontsize=9.5, va="top")
        ax.set_xlim(-1.0, 1.0)
        ax.set_xticks([-0.5, 0, 0.5])
        ax.xaxis.set_major_formatter(KOMMA)
        ax.set_xlabel("$x$ in µm")
    axs[0].set_ylabel("Energie der Elektronen in eV")
    axs[0].set_ylim(-1.7, 3.6)
    axs[0].yaxis.set_major_formatter(KOMMA)
    speichern(fig, 12)


# ---------------------------------------------------------------- 13: Teilströme über der Spannung
def abb13():
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    U = np.linspace(-0.3, 0.72, 600)
    ax.semilogy(U, Z.IS * np.exp(U / Z.UT), color=C_E, lw=1.6, ls=(0, (6, 3)))
    ax.semilogy(U, np.full_like(U, Z.IS), color=C_MIN, lw=1.6, ls=(0, (6, 3)))
    I = np.abs(Z.strom(U))
    ax.semilogy(U[np.abs(U) > 1e-4], I[np.abs(U) > 1e-4], color=C_TXT, lw=2.2)
    ax.annotate("hinauf: $I_S\\,\\exp(U/U_T)$", xy=(-0.06, Z.IS * math.exp(-0.06 / Z.UT)), xytext=(0.08, 2.5e-16),
                fontsize=10, color=C_E, va="center", arrowprops=dict(arrowstyle="-", color=C_E, lw=0.8))
    ax.text(-0.29, 3e-14, "hinunter: $I_S$ = 15 fA", color=C_MIN, fontsize=10)
    ax.text(0.47, 1.5e-8, "Netto-Strom $|I|$\n(fast nur „hinauf“)", color=C_TXT, fontsize=10, ha="left", va="top")
    ax.plot([0.6], [float(Z.strom(0.6))], "o", color=C_TXT, ms=5)
    ax.annotate("0,6 V: 0,18 mA", xy=(0.6, float(Z.strom(0.6))), xytext=(0.30, 3e-3), fontsize=10,
                arrowprops=dict(arrowstyle="-", color=C_GRAU, lw=0.8))
    ax.text(0.36, 1e-12, "×10 je 59,5 mV", fontsize=10, color=C_GRAU)
    ax.text(-0.29, 1e-11, "Sperrrichtung:\n$I \\approx -I_S$", fontsize=10, color=C_TXT)
    ax.axvline(0, color="#999", lw=0.7)
    ax.set_xlim(-0.3, 0.72)
    ax.set_ylim(1e-16, 1e-1)
    ax.set_xlabel("Spannung $U$ in V (positiv: Durchlass)")
    ax.set_ylabel("Strom in A")
    ax.xaxis.set_major_formatter(KOMMA)
    ax.yaxis.set_major_locator(LogLocator(base=10, numticks=9))
    speichern(fig, 13)


ALLE = {1: abb1, 2: abb2, 3: abb3, 4: abb4, 5: abb5, 6: abb6, 7: abb7, 8: abb8, 9: abb9, 10: abb10, 11: abb11,
        12: abb12, 13: abb13}
for nr, f in ALLE.items():
    if not NUR or nr in NUR:
        f()
