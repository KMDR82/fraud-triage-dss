"""Manuscript Table 6 (additional robustness analyses) from the notebook result files.
Run from the repository root: python tools/table6_robustness.py  -> results/table6_robustness.tex"""
import os, re
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = os.path.join(ROOT, "results", "output")
W = pd.read_csv(f"{O}/tuned_and_decomposition_wide.csv"); Wc = pd.read_csv(f"{O}/cost_model_scenarios_wide.csv")
S2 = pd.read_csv(f"{O}/prevalence_shift_summary.csv"); DS = ["ieee", "ulb", "bs"]
cell = lambda v, a, b: f"{v:.1f} ({a}/{b})"
rows = [["Thresholds of P1, P5, P6 tuned on validation$^{a}$"] + [cell(W[W.dataset == t].P7_vs_best_tuned_pct.median(),
         int((W[W.dataset == t].P7_vs_best_tuned_pct >= -1e-9).sum()), int((W.dataset == t).sum())) for t in DS]]
lab = {"recovery_0.5": "Partial recovery, $\\rho=0.5$", "recovery_0.75": "Partial recovery, $\\rho=0.75$",
       "amount_dependent_Cblk": "Amount-dependent $C_{\\mathrm{blk}}$", "amount_dependent_q": "Amount-dependent $q$ (0.95 / 0.70)"}
for sn, ln in lab.items():
    r = [ln]
    for t in DS:
        g = Wc[(Wc.dataset == t) & (Wc.scenario == sn)]; r.append(cell(g.P7_vs_best_pct.median(), int((g.P7_vs_best_pct >= -1e-9).sum()), len(g)))
    rows.append(r)
for f in [0.5, 2.0]:
    for md, ml in [("offline", "offline"), ("online_capped", "online")]:
        r = [f"Fraud prevalence $\\times{f:g}$, {ml}$^{{b}}$"]
        for t in DS:
            g = S2[(S2.dataset == t) & (S2.factor == f) & (S2["mode"] == md)].iloc[0]; r.append(f"{g.P7_vs_best_median:.1f} ({100 * g.P7_best_share:.0f}\\%)")
        rows.append(r)
body = "\n".join(re.sub(r"& -(\d)", r"& $-$\1", " & ".join(r)) + " \\\\" for r in rows)
tex = "\\begin{tabular}{lrrr}\n\\toprule\nAnalysis & IEEE-CIS & ULB & BankSim \\\\\n\\midrule\n" + body + "\n\\bottomrule\n\\end{tabular}\n"
open(os.path.join(ROOT, "results", "table6_robustness.tex"), "w").write(tex); print(tex)
