"""Manuscript Figure 2: decisions of P7 in the probability-amount plane.
Reads figures/source/Figure_2.csv and Figure_2_summary.csv (written by the notebook)
and writes figures/Figure_2.pdf/.png. Run from the repository root: python tools/figure2_regions.py"""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
from style import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import matplotlib.patches as mpatches
F = os.path.join(ROOT, "figures", "source"); P = pd.read_csv(f"{F}/Figure_2.csv"); S = pd.read_csv(f"{F}/Figure_2_summary.csv").set_index("dataset")
C_REV, C_BLK = 10.0, 50.0
fig, axes = plt.subplots(1, 3, figsize=(W, 2.8))
for k, t in enumerate(DS):
    ax = axes[k]; d = P[P.dataset == t]; pp = np.maximum(d.p.values, 1e-4); aa = np.maximum(d.amount.values, 1e-2)
    for dec, c in [("approve", "#bdbdbd"), ("review", "#ff7f0e"), ("block", "#d62728")]:
        m0 = (d.decision.values == dec) & (d.y.values == 0); m1 = (d.decision.values == dec) & (d.y.values == 1)
        ax.scatter(pp[m0], aa[m0], s=1, c=c, alpha=.35, lw=0, rasterized=True); ax.scatter(pp[m1], aa[m1], s=7, c=c, marker="x", lw=.6, rasterized=True)
    thr = C_REV + max(S.loc[t, "gain_threshold"], 0.0); pmax = 1 - thr / C_BLK
    g = np.logspace(-4, 0, 400)[:-1]; ax.plot(g, (1 - g) * C_BLK / g, "k-", lw=.9); ok = g <= pmax; ax.plot(g[ok], thr / g[ok], "k--", lw=.9)
    if pmax > 0: ax.plot([pmax, pmax], [thr / pmax, aa.max() * 1.3], "k--", lw=.9)
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(8e-5, 1.1); ax.set_ylim(aa.min() * .8, aa.max() * 1.3)
    ax.set_xlabel("Calibrated fraud probability $p$"); ax.set_ylabel("Transaction amount $a$" if k == 0 else "")
    panel(ax, f"({'abc'[k]}) {DSN[t]}, $K$ = {MID[t]:,}", -0.3)
h = [mpatches.Patch(color=c, label=l) for l, c in [("approve", "#bdbdbd"), ("review", "#ff7f0e"), ("block", "#d62728")]]
h += [plt.Line2D([], [], color="k", marker="x", ls="", ms=4, label="fraud"), plt.Line2D([], [], color="k", ls="-", label="approve/block boundary"),
      plt.Line2D([], [], color="k", ls="--", label="review region boundary")]
fig.legend(handles=h, loc="upper center", ncol=6, bbox_to_anchor=(0.5, 1.07), frameon=False); fig.tight_layout()
out = os.path.join(ROOT, "figures", "Figure_2"); fig.savefig(out + ".pdf", bbox_inches="tight"); fig.savefig(out + ".png", dpi=600, bbox_inches="tight"); plt.close(fig); print("ok")
