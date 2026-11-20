# CardioAI Project Proposal

## Project Title
**CardioAI: An Explainable and Quality-Aware AI-Based ECG Analysis and Arrhythmia Classification System**

## Project Scope
CardioAI is a software-only research and product-development project. It will analyze previously recorded ECG datasets. This project phase does **not** include live ECG acquisition, physical electrodes, Raspberry Pi, patient-connected hardware, or real-time monitoring.

- **Student:** Umamah binte Mussadaq
- **Enrollment No.:** 537450
- **Course:** AI-853 — Advanced Programming in Python
- **Project Track:** Track B — Product Development
- **Development environment:** Microsoft Visual Studio IDE
- **Programming language:** Python
- **Application interface:** Streamlit
- **Primary dataset:** PTB-XL (12-lead ECG)

## 1. Abstract
CardioAI is a software platform for loading, visualizing, preprocessing, and classifying previously recorded electrocardiogram (ECG) signals. The initial implementation will focus on 12-lead recordings from the publicly available PTB-XL dataset. The proposed workflow combines per-lead signal-quality assessment, multi-lead deep-learning classification, lead-wise explainability, and robustness evaluation under missing or corrupted lead conditions. A Python-based application developed in Microsoft Visual Studio will use Streamlit as its user interface. The Streamlit application will allow users to upload supported ECG files, inspect raw and processed waveforms, review model outputs, and export analysis summaries. The system is intended for research and education and is not a clinically validated diagnostic tool.

## 2. Problem Statement
ECG classification can be affected by noisy recordings, unreliable leads, class imbalance, and limited interpretability. A model may produce a prediction when some input leads are corrupted or unavailable without communicating how signal quality affects the result. Users may also receive a class label without understanding which leads contributed to the prediction. CardioAI will investigate a quality-aware and explainable workflow and evaluate reliability under controlled signal degradation.

## 3. Aim
To develop a software-only ECG analysis platform that uses multi-lead ECG datasets to assess signal quality, classify ECG abnormalities, and evaluate prediction robustness when leads are noisy, corrupted, or missing.

## 4. Objectives
1. Load and organize 12-lead ECG recordings and diagnostic labels from PTB-XL.
2. Implement signal validation, filtering, normalization, and segmentation.
3. Develop per-lead signal-quality indicators and controlled corruption tests.
4. Establish reproducible baseline ECG classification models.
5. Develop a multi-lead deep-learning model with lead-wise attention or learned lead weighting.
6. Generate lead-wise explanations and compare them with lead-occlusion experiments.
7. Evaluate performance when selected leads are missing or synthetically degraded.
8. Build a Streamlit interface for upload, visualization, inference, and report generation.

## 5. Proposed Research Contribution
The proposed contribution is a combined evaluation framework for quality-aware, explainable, and lead-robust ECG classification.

### 5.1 Lead-quality assessment
Calculate signal-quality indicators for each lead and flag potentially unreliable segments. PTB-XL does not provide complete ground-truth quality labels for every lead and segment. Initial quality labels will therefore use transparent signal rules and/or controlled synthetic corruption. These will be treated as proxy labels, not clinical ground truth.

### 5.2 Lead-wise explainability
Use an attention or feature-weighting mechanism to estimate the contribution of individual leads to predictions. Validate explanations with lead occlusion or perturbation experiments. Attention weights are model explanations, not proof of clinical causality.

### 5.3 Missing- and corrupted-lead robustness
Train and evaluate under controlled lead dropout, noise addition, baseline drift, and other defined perturbations. Compare performance with uncorrupted inputs at multiple corruption levels.

The novelty claim will be finalized after a focused literature review and comparison with existing quality-aware, attention-based, and missing-lead ECG methods.

## 6. Dataset and Data Handling
### Primary dataset: PTB-XL
PTB-XL is a publicly available 12-lead ECG dataset. The project will use its metadata and recommended patient-level folds where applicable. Sampling frequency, label taxonomy, and selected subset will be documented before training.

### Optional secondary dataset: MIT-BIH Arrhythmia Database
MIT-BIH may be used for a separate two-channel experiment. It will not be treated as an equivalent 12-lead external test set. Any cross-dataset comparison will account for differences in lead count, acquisition, and label definitions.

### Leakage prevention
Use patient-independent data splits. Fit preprocessing and model-selection parameters on training/validation data only; reserve the held-out test set for final evaluation.

## 7. Methodology
1. **Dataset ingestion:** Read waveforms and metadata; validate lead count, sampling rate, units, and labels.
2. **Exploratory analysis:** Inspect class distribution, recording duration, sampling frequency, missing values, and signal examples.
3. **Preprocessing:** Apply documented filtering and normalization; preserve raw signals and processing metadata.
4. **Quality analysis:** Compute per-lead indicators such as clipping, flatline, amplitude range, baseline drift, and high-frequency noise.
5. **Baseline modelling:** Train reproducible baseline models and establish patient-independent reference metrics.
6. **Proposed model:** Implement a multi-lead neural network with lead-wise attention or learned lead weighting.
7. **Robustness experiments:** Apply controlled lead removal and signal corruption at defined severities.
8. **Explainability:** Visualize lead contributions and validate through lead occlusion/perturbation.
9. **Application:** Build a Streamlit workflow for upload, plotting, preprocessing, prediction, warnings, and export.

## 8. Software Architecture and Tools
- **Development environment:** Microsoft Visual Studio IDE with the Python development workload
- **Programming:** Python
- **Data processing:** NumPy, SciPy, pandas, WFDB
- **Machine learning:** PyTorch or TensorFlow (one framework will be selected for the final pipeline)
- **Visualization and interface:** Matplotlib, Plotly, Streamlit
- **Development workflow:** Create, edit, run, and debug the Python project in Microsoft Visual Studio; launch the Streamlit interface from the Visual Studio terminal.
- **Evaluation:** scikit-learn and reproducible experiment scripts
- **Version control:** Git and GitHub

Microsoft Visual Studio will be used as the main integrated development environment (IDE) for creating, editing, running, and debugging the Python code. Streamlit is the application framework that renders the interactive browser-based interface; it is not a replacement for Visual Studio. The repository will separate dataset loading, preprocessing, quality assessment, model training, evaluation, explainability, and the Streamlit application. Public datasets will not be redistributed unless their terms permit it.

## 9. Evaluation Plan
Classification will be evaluated using macro-F1, per-class precision and recall, AUROC and/or AUPRC where appropriate, confusion matrices, and class-wise sensitivity and specificity. Calibration and confidence behaviour will be examined where probability outputs are available. Quality assessment will be evaluated against defined proxy labels or controlled corruption conditions, with limitations stated. Robustness will be measured by comparing clean, noisy, and missing-lead inputs at multiple corruption levels. Confidence intervals or repeated-run variability will be reported where feasible.

## 10. Expected Deliverables
1. A documented PTB-XL data-loading and preprocessing pipeline.
2. A reproducible baseline ECG classification model.
3. A quality-aware multi-lead classification model with lead-wise explanation outputs.
4. A missing/corrupted-lead robustness evaluation report.
5. A Streamlit application for ECG upload, visualization, analysis, and report export.
6. Source code, configuration files, experiment documentation, and final project report.

## 11. Proposed Timeline

| Week | Planned work |
|---|---|
| 1 | Dataset access, documentation, exploratory analysis, and label selection |
| 2 | Preprocessing pipeline, visualization, and data validation |
| 3 | Baseline model training and initial evaluation |
| 4–5 | Lead-quality assessment and attention-based model development |
| 6 | Missing/corrupted-lead experiments and explainability validation |
| 7 | Streamlit integration, reporting, and usability checks |
| 8 | Final evaluation, documentation, and report refinement |

## 12. Scope, Limitations, and Safety
This project is limited to retrospective analysis of existing ECG datasets. It does not include live patient monitoring, hardware acquisition, diagnosis, treatment recommendations, or clinical deployment. Dataset labels may be noisy or incomplete, class imbalance may affect performance, and synthetic corruption may not fully represent real-world acquisition artefacts. Outputs are research predictions, not medical advice. Future patient-facing hardware or clinical use would require separate engineering, regulatory, and clinical validation.

## 13. References
1. Wagner, P., et al. (2020). PTB-XL, a large publicly available electrocardiography dataset. *Scientific Data, 7*, 154. https://doi.org/10.1038/s41597-020-0495-6
2. Goldberger, A. L., et al. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215
3. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50.
4. Additional recent literature on ECG signal-quality assessment, multi-lead deep learning, attention-based explainability, and missing-lead robustness will be added after the focused literature review.
