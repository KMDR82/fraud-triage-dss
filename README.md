# Budgeted decision rules for fraud decision support

Code and results for the manuscript *"Approve, review or block: an evaluation of budgeted decision rules for fraud decision support"* (under review).

The study evaluates the decision layer that turns fraud scores into three actions (approve, send to an analyst for review, block) under a review budget. A budgeted Bayes policy (P7) is compared with six policies from the cost-sensitive, alert, reject-option and three-way decision literature on three public datasets and four scoring models (XGBoost, LightGBM, CatBoost, FT-Transformer).

## Repository structure

| Path | Content |
|---|---|
| `notebook/fraud_triage_dss_full.ipynb` | Complete pipeline: raw data → models → calibration → decision policies → statistics → every table, figure and number in the manuscript (Steps 1–27) |
| `results/output/` | All result files of the reported run (CSV), including `manuscript_numbers.csv`, the registry of every number quoted in the manuscript with its source file |
| `results/output/tables/` | Tables written by the notebook (CSV and LaTeX) |
| `figures/` | Manuscript Figures 1–7 (PDF, 600-dpi PNG) with the data of each figure (CSV) |
| `figures/source/` | Data used by `tools/figure2_regions.py` |
| `tools/` | Scripts that produce the manuscript versions of Figure 1, Figure 2 and Table 6 from the files above |
| `data/README.md` | How to obtain the three datasets (they are not redistributed here) |

## Reproducing the results

1. Create a Kaggle notebook and import `notebook/fraud_triage_dss_full.ipynb`.
2. Add the input data (see `data/README.md`): the IEEE-CIS Fraud Detection competition data and the ULB credit card fraud dataset. BankSim is downloaded by the notebook (Step 2), so the internet must be enabled.
3. Settings: GPU T4 ×2, Internet on. Run **Save Version → Save & Run All** (about 3 hours).
4. The notebook writes `/kaggle/working/paper_package.zip` with `fig/` and `output/`; its contents correspond to `results/` and `figures/` in this repository.

Gradient-boosted models are deterministic given the seed. FT-Transformer and CatBoost training on GPU is not bit-reproducible, so numbers that involve these two scorers can differ slightly between runs; the manuscript reports one complete run, whose files are in `results/`.

The manuscript-formatted artefacts not produced directly by the notebook can be regenerated from the repository root:

```bash
python tools/figure1_drawio.py figures/Figure_1.drawio   # editable diagram; export to PDF in draw.io
python tools/figure2_regions.py                          # figures/Figure_2.pdf/.png
python tools/table6_robustness.py                        # results/table6_robustness.tex
```

## Manuscript items and their sources

| Manuscript | Source |
|---|---|
| Figure 1 | `tools/figure1_drawio.py` → `figures/Figure_1.drawio` (schematic) |
| Figure 2 | `tools/figure2_regions.py` (data from notebook Step 19, `figures/source/Figure_2*.csv`) |
| Figure 3 | notebook figure `Figure_3` (policy cost over the budget) |
| Figure 4 | notebook figure `Figure_4` (cost decomposition) |
| Figure 5 | notebook figure `Figure_6` (budget enforced on arrival) |
| Figure 6 | notebook figure `Figure_7` (per-period capacity, analyst accuracy) |
| Figure 7 | notebook figure `Figure_8` (cost scale) |
| Table 1 | `results/output/tables/table1_datasets.csv` |
| Table 2 | `results/output/tables/table2_detection.csv` |
| Table 3 | `results/output/tables/table4_policy_costs.csv` |
| Table 4 | `results/output/tables/table5b_block_holm.csv` |
| Table 5 | `results/output/tables/table7_effect_sizes.csv` |
| Table 6 | `tools/table6_robustness.py` (from `tuned_and_decomposition_wide.csv`, `cost_model_scenarios_wide.csv`, `prevalence_shift_summary.csv`) |
| Numbers in the text | `results/output/manuscript_numbers.csv` (key, value, source file) |

The notebook also writes some tables and figures that are not part of the final manuscript (for example the transaction-level bootstrap table and the cost-ratio figure); their numbers are reported in the text where used.

## Requirements

Python 3 with the packages in `requirements.txt`. The reported run used the Kaggle Python GPU image of October 2026 (TensorFlow 2.20).

## Licence

Code: MIT (see `LICENSE`). The datasets are subject to the terms of their providers and are not included.
