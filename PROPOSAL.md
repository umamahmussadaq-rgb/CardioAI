# PROJECT PROPOSAL

## CardioAI: A Quality-Aware and Explainable AI Platform for Noise-Robust ECG Arrhythmia Analysis

**Student Name:** Umamah binte Mussadaq  
**Enrollment Number:** 537450  
**Course:** AI-853 — Advanced Programming in Python  
**Project Track:** Track B — Product Development  
**Project Type:** Individual, Software-Based AI Product

### 1. Problem Statement

Electrocardiogram (ECG) recordings can contain noise and artifacts caused by movement, electrode contact and baseline wandering. These disturbances can affect the reliability of automated ECG analysis. Users also need to understand whether a signal is suitable for analysis and why an AI model produces a particular prediction.

CardioAI aims to provide an integrated software platform for ECG preprocessing, signal-quality assessment, arrhythmia classification, explainable AI and automated reporting.

### 2. Target Users and Evidence

The intended users include biomedical engineering students, biomedical signal-processing researchers and university research laboratories.

At least five potential users will be consulted before development to identify their current ECG analysis workflows, challenges and desired features. Actual feedback will be documented after conducting the interviews.

### 3. Existing Solutions and Product Gap

Three related solutions will be reviewed:

1. **ExChanGeAI:** An ECG analysis platform supporting signal analysis, model training and prediction.
2. **Cordis:** An ECG/PPG analysis platform providing signal processing, biomarkers and artifact correction.
3. **BRAVEHEART:** Open-source software for automated ECG and vectorcardiogram processing.

**Proposed product gap:** CardioAI will focus on integrating signal-quality assessment, noise-robust arrhythmia classification, prediction confidence and explainable AI into an accessible research-oriented application. Existing solutions will be evaluated to verify the specific differences.

### 4. Proposed Product and AI Components

CardioAI will be developed as an interactive Python-based web application with the following modules:

- ECG data upload using CSV and WFDB formats.
- Signal preprocessing, filtering and baseline-wander removal.
- Automated signal-quality assessment.
- Machine-learning/deep-learning-based arrhythmia classification.
- Noise-robustness evaluation under controlled noise conditions.
- Explainable AI visualizations to interpret model predictions.
- Prediction confidence and uncertainty indicators.
- Interactive ECG visualization and downloadable reports.

**Datasets:**
- MIT-BIH Arrhythmia Database.
- PTB-XL ECG Dataset.

**Technologies:** Python, Google Colab, NumPy, Pandas, SciPy, NeuroKit2, Scikit-learn, PyTorch or TensorFlow, Plotly, Streamlit and GitHub.

### 5. Success Measures

The product will be evaluated using:

- Accuracy, precision, recall, F1-score and confusion matrix.
- AUROC where appropriate.
- Signal-quality assessment performance.
- Classification performance under different noise levels.
- Changes in F1-score as noise increases.
- Prediction explanations and confidence estimates.
- Usability feedback from at least five real users.

All numerical results will be obtained through actual experiments and testing.

### 6. Development Plan

**By 4 December 2026:**
- Review existing solutions and obtain ECG datasets.
- Implement ECG data loading and preprocessing.
- Develop an initial arrhythmia classification model.
- Demonstrate a working prototype.
- Maintain regular GitHub commits.

**By 18 December 2026:**
- Integrate signal-quality assessment.
- Implement noise-robustness experiments.
- Add explainability and confidence visualization.
- Complete the Streamlit application.
- Conduct testing with at least five users.
- Prepare the final product report.

**Fallback Plan:** If the complete implementation cannot be finished, the minimum working product will include ECG upload, preprocessing, waveform visualization, a baseline classification model and a basic analysis report.

### 7. Expected Deliverable

The expected deliverable is a working software-only ECG analysis platform integrating digital signal processing, machine learning, explainable AI and interactive visualization. The final submission will include the application, GitHub repository, experimental evaluation and a 4–6 page product report.

**Scope Limitation:** CardioAI is intended for educational and research purposes and is not a clinically validated diagnostic system.
