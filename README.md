# CardioAI

**CardioAI** is a software-only research and educational platform for multi-lead ECG dataset analysis, signal-quality assessment, explainable AI classification, and robustness testing.

## Current project scope

This development phase uses previously recorded ECG datasets only. It does **not** include Raspberry Pi, physical electrodes, live ECG acquisition, or real-time patient monitoring.

- Primary dataset: **PTB-XL** (12-lead ECG)
- Application: **Streamlit**
- Core language: **Python**
- Research focus: lead-quality assessment, lead-wise explainability, and missing/corrupted-lead robustness

See [PROPOSAL.md](PROPOSAL.md) for the updated project proposal.

## Planned software workflow

1. Upload or select a supported ECG dataset recording.
2. Validate metadata, lead count, sampling frequency, and labels.
3. Visualize raw ECG signals across the available leads.
4. Preprocess signals using documented filtering and normalization.
5. Assess signal quality for each lead.
6. Run baseline and proposed multi-lead classification models.
7. Explain predictions using lead-wise contribution visualizations and perturbation tests.
8. Evaluate robustness when selected leads are noisy, corrupted, or missing.
9. Export an analysis summary.

## Proposed research components

### 1. Lead-quality assessment
Calculate per-lead signal-quality indicators and identify potentially unreliable segments. Any proxy quality labels derived from signal rules or synthetic corruption will be clearly distinguished from clinical ground truth.

### 2. Lead-wise explainability
Use a lead-attention or learned lead-weighting mechanism and validate the resulting explanations with lead-occlusion experiments. Attention weights will not be interpreted as causal evidence.

### 3. Missing- and corrupted-lead robustness
Evaluate model performance under controlled lead dropout, noise, and baseline-drift conditions at documented severity levels.

The novelty of this combination will be assessed through a focused literature review and baseline comparisons.

## Dataset plan

- **PTB-XL:** primary 12-lead dataset.
- **MIT-BIH Arrhythmia Database:** optional separate two-channel experiment; not a directly equivalent 12-lead test set.

Use patient-independent data splits and avoid leakage between training, validation, and test sets. Follow dataset licenses and terms; do not commit restricted raw datasets to this repository.

## Technology stack

- Python, NumPy, SciPy, pandas, WFDB
- PyTorch or TensorFlow (final choice to be documented)
- scikit-learn
- Streamlit, Plotly, Matplotlib
- Git and GitHub

## Planned repository organization

```text
CardioAI/
├── README.md
├── PROPOSAL.md
├── requirements.txt
├── data/                 # dataset instructions; raw data excluded from Git
├── src/
│   └── cardioai/
│       ├── data/         # dataset loaders and metadata handling
│       ├── preprocessing/
│       ├── quality/
│       ├── models/
│       ├── explainability/
│       └── evaluation/
├── app/                  # Streamlit application
├── notebooks/            # exploration and experiments
├── tests/
└── reports/              # generated experiment summaries
```

## Evaluation

Report macro-F1, per-class precision/recall, AUROC or AUPRC where appropriate, confusion matrices, class-wise sensitivity/specificity, and robustness degradation under controlled corruptions. Document patient-level splitting and reproducibility settings.

## Safety and intended use

CardioAI is for research and education. It is not a clinically validated diagnostic device and must not be used to make medical decisions or replace professional assessment.
