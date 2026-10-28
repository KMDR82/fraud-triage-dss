# Data

The datasets are not redistributed in this repository. Obtain them from their providers and accept their terms of use.

| Dataset | Source | Files used | Notes |
|---|---|---|---|
| IEEE-CIS Fraud Detection | Kaggle competition `ieee-fraud-detection` (https://www.kaggle.com/competitions/ieee-fraud-detection) | `train_transaction.csv`, `train_identity.csv` | Accept the competition rules on Kaggle and add the competition data as notebook input. The unlabelled test files are not used. |
| ULB credit card fraud | Kaggle dataset `mlg-ulb/creditcardfraud` | `creditcard.csv` | Add the dataset as notebook input. |
| BankSim | Public CSV `bs140513_032310.csv` | `bs140513_032310.csv` | Downloaded automatically by notebook Step 2 from the URL in the configuration cell (`BANKSIM_URL`), or added as notebook input. |

The configuration cell finds the files anywhere under `/kaggle/input/`, so the input folder names do not matter.
