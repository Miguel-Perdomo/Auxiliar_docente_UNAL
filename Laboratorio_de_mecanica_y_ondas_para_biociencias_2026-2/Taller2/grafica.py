"""
Gráfica de referencia — Taller 2, Parte B
Caída libre: h vs t², regresión lineal por mínimos cuadrados.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# DATOS

h = np.array([0.50, 1.00, 1.50, 2.00, 2.50, 3.00])        # altura [m]
t = np.array([0.312, 0.461, 0.548, 0.652, 0.703, 0.795])  # tiempo [s]
t2 = t**2                                                  # [s^2]

G_BOGOTA = 9.78          # valor aceptado [m/s^2]
DELTA_H = 0.10           # incertidumbre en altura [m]  
DELTA_T = 0.03           # incertidumbre en tiempo [s]  

# propagación:  Δ(t²) = 2·t·Δt   -> crece con t
DELTA_T2 = 2 * t * DELTA_T

fit = stats.linregress(t2, h)
m, b = fit.slope, fit.intercept
sm, sb = fit.stderr, fit.intercept_stderr
r2 = fit.rvalue**2

g_exp = 2 * m
sg_exp = 2 * sm
error_pct = abs(g_exp - G_BOGOTA) / G_BOGOTA * 100


m0 = np.sum(t2 * h) / np.sum(t2**2)
res0 = h - m0 * t2
s0 = np.sqrt(np.sum(res0**2) / (len(h) - 1))
sm0 = s0 / np.sqrt(np.sum(t2**2))
g0, sg0 = 2 * m0, 2 * sm0
error_pct0 = abs(g0 - G_BOGOTA) / G_BOGOTA * 100

plt.rcParams.update({
    "font.size": 20,
    "axes.labelsize": 24,
    "xtick.labelsize": 20,
    "ytick.labelsize": 20,
    "legend.fontsize": 19,
    "axes.linewidth": 1.6,
    "xtick.major.width": 1.6,
    "ytick.major.width": 1.6,
    "xtick.major.size": 7,
    "ytick.major.size": 7,
    "xtick.minor.size": 4,
    "ytick.minor.size": 4,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "font.family": "serif",
    "font.serif": ["cmr10", "Computer Modern Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,
    "axes.unicode_minus": False,
})

COLOR_PUNTOS = "#8B0000"   # darkred
COLOR_RECTA  = "#00008B"   # darkblue

fig, ax = plt.subplots(figsize=(10, 7.5))

ax.errorbar(t2, h,
            yerr=DELTA_H,
            xerr=DELTA_T2,
            fmt="o", markersize=8,
            color=COLOR_PUNTOS, markerfacecolor=COLOR_PUNTOS,
            markeredgecolor=COLOR_PUNTOS,
            ecolor=COLOR_PUNTOS, elinewidth=1.8,
            capsize=7, capthick=1.8,
            linestyle="none",
            label="Datos experimentales", zorder=3)

x_fit = np.linspace(0, t2.max() * 1.15, 200)
ax.plot(x_fit, m * x_fit + b, "-", linewidth=2.4, color=COLOR_RECTA,
        label="Ajuste lineal", zorder=2)

ax.set_xlabel(r"$t^{2}$  (s$^{2}$)", labelpad=12)
ax.set_ylabel(r"$h$  (m)", labelpad=12)

ax.set_xlim(0, t2.max() * 1.15)
ax.set_ylim(0.1, h.max() + 3 * DELTA_H)
ax.minorticks_on()

texto = (
    f"$h = m\\,t^{{2}} + b$\n"
    f"$m = {m:.2f} \\pm {sm:.2f}$ m/s$^2$\n"
    f"$b = {b:.3f} \\pm {sb:.3f}$ m\n"
    f"$R^{{2}} = {r2:.4f}$\n"
    f"$g = 2m = {g_exp:.2f} \\pm {sg_exp:.2f}$ m/s$^2$"
)
ax.text(0.05, 0.95, texto, transform=ax.transAxes,
        fontsize=19, va="top", ha="left", linespacing=1.5)

ax.legend(loc="lower right", frameon=False)

fig.tight_layout()
fig.savefig("grafica_taller2.png", dpi=300, bbox_inches="tight")
fig.savefig("grafica_taller2.pdf", bbox_inches="tight")
plt.show()