import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "legend.fontsize": 7, "axes.grid": True, "grid.alpha": .3, "grid.linewidth": .5, "axes.linewidth": .6,
    "lines.linewidth": 1.1, "lines.markersize": 3.5, "savefig.dpi": 600, "pdf.fonttype": 42,
    "axes.axisbelow": True, "font.family": "DejaVu Sans"})
W = 7.0   # full-width figure (in); placed at \textwidth
DS = ["ieee", "ulb", "bs"]; DSN = {"ieee": "IEEE-CIS", "ulb": "ULB", "bs": "BankSim"}
MID = {"ieee": 2000, "ulb": 100, "bs": 400}
POL = ["binary_F1", "binary_bayes_amount", "topK_review", "reject_option", "threeway_fixed",
       "threeway_expected_loss", "threeway_bayes_budget"]
PN = {"binary_F1": "Binary, F1 threshold (P1)", "binary_bayes_amount": "Binary, Bayes rule (P2)",
      "topK_review": "Top-K review (P3)", "reject_option": "Reject option (P4)",
      "threeway_fixed": "Three-way, fixed (P5)", "threeway_expected_loss": "Three-way, expected loss (P6)",
      "threeway_bayes_budget": "Budgeted Bayes (P7)"}
PS = {"binary_F1": ("#7f7f7f", "s", "--"), "binary_bayes_amount": ("#8c564b", "D", "--"),
      "topK_review": ("#bcbd22", "v", ":"), "reject_option": ("#9467bd", "^", ":"),
      "threeway_fixed": ("#1f77b4", "o", "-."), "threeway_expected_loss": ("#2ca02c", "P", "-."),
      "threeway_bayes_budget": ("#d62728", "o", "-")}
SN = {"FTT_ens": "FT-Transformer", "LightGBM": "LightGBM", "XGBoost": "XGBoost", "CatBoost": "CatBoost"}
def panel(ax, s, dy=-0.18):
    ax.text(0.5, dy, s, transform=ax.transAxes, ha="center", va="top", fontsize=8, fontweight="bold")
def save(fig, name, data):
    import pandas as pd
    fig.savefig(f"out/{name}.pdf", bbox_inches="tight"); fig.savefig(f"out/{name}.png", dpi=600, bbox_inches="tight")
    pd.DataFrame(data).to_csv(f"out/{name}.csv", index=False); plt.close(fig); print("saved", name)
