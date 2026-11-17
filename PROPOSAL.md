# PROJECT PROPOSAL

## CardioAI: A Quality-Aware and Explainable AI Platform for Noise-Robust ECG Arrhythmia Analysis

Student Name: Umamah binte Mussadaq
Enrollment Number: 537450
**Project Track:** Track B — Product Development  
**Course:** AI-853 — Advanced Programming in Python  
**Project Type:** Individual, Software-Based AI Product

### 1. Problem

Electrocardiogram (ECG) signals are widely used to study cardiac electrical activity. However, ECG recordings can contain noise and artifacts caused by movement, electrode contact, baseline wandering and other sources. These disturbances can affect the reliability of automated ECG analysis.

Many existing ECG analysis tools provide signal processing, automated classification or visualization, but users may still face difficulties understanding signal quality, interpreting model predictions and identifying when a prediction is unreliable.

This project proposes CardioAI, a software-based platform that integrates ECG preprocessing, signal-quality assessment, arrhythmia classification, explainable artificial intelligence and automated reporting.

### 2. Target Users and Evidence

The intended users are:

- Biomedical engineering students.
- Biomedical signal-processing researchers.
- University research laboratories.
- Students and researchers working on ECG and machine-learning projects.

At least five potential users will be consulted before product development to understand their current ECG analysis workflows, difficulties and desired features.

**User feedback:** To be completed after conducting five genuine user interviews. No interview results are claimed at the proposal stage.

### 3. Existing Solutions and Identified Gap

Three related solutions will be considered:

1. **ExChanGeAI:** An open-source ECG analysis platform supporting signal analysis, model training, fine-tuning and prediction.
2. **Cordis:** An ECG/PPG analysis platform providing signal processing, heart-rate variability biomarkers, artifact correction and anomaly detection.
3. **BRAVEHEART:** Open-source software for automated ECG and vectorcardiogram processing and research measurements.

**Proposed product gap:**

CardioAI will focus on an integrated, quality-aware ECG analysis workflow that:

- Assesses signal quality before classification.
- Evaluates classification performance under controlled noise conditions.
- Combines arrhythmia classification with prediction confidence.
- Provides visual explanations of model predictions.
- Offers an accessible interface for educational and research use.

The project will implement and evaluate these features rather than claim that the existing platforms lack them entirely.

### 4. Proposed Product and AI Components

CardioAI will be developed as an interactive web application using Python.

**Main modules:**

1. **ECG Data Upload:** Accept ECG recordings in supported CSV and WFDB formats.
2. **Signal Preprocessing:** Perform filtering, baseline-wander removal, normalization and noise reduction.
3. **Signal Quality Assessment:** Estimate whether a recording is suitable for further analysis.
4. **Arrhythmia Classification:** Develop a machine-learning or deep-learning model to classify supported ECG rhythm or beat categories.
5. **Noise-Robustness Analysis:** Evaluate model performance under controlled levels of added noise.
6. **Explainable AI:** Visualize the ECG regions or signal features contributing to model predictions.
7. **Prediction Confidence:** Display confidence estimates and flag uncertain predictions.
8. **Visualization and Reporting:** Display ECG waveforms, analysis results, performance metrics and downloadable reports.

**Proposed datasets:**

- MIT-BIH Arrhythmia Database.
- PTB-XL ECG Dataset, subject to compatibility with the selected classification task.

**Proposed technologies:**

- Python
- Google Colab
- NumPy and Pandas
- SciPy and NeuroKit2
- Scikit-learn
- PyTorch or TensorFlow
- SHAP or another suitable explainability method
- Streamlit
- Plotly
- GitHub

### 5. Success Measures

The product will be evaluated using measurable criteria.

**Model performance:**
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- AUROC, where appropriate

**Signal-quality assessment:**
- Classification performance on clean and noisy recordings.
- Ability to identify unsuitable or highly corrupted signals.

**Noise robustness:**
- Compare classification performance at different controlled noise levels.
- Measure the change in F1-score as noise increases.

**Explainability and usability:**
- Display explanations for model predictions.
- Collect feedback from at least five real users.
- Measure task completion, usability feedback and user-reported usefulness.

All numerical results will be obtained from actual experiments and user testing.

### 6. Development Plan

**By 4 December 2026:**
- Complete the initial literature and existing-product review.
- Obtain and inspect the selected public ECG dataset.
- Implement ECG loading and preprocessing.
- Develop an initial arrhythmia classification model.
- Demonstrate a working prototype.
- Commit the implementation to GitHub.

**By 18 December 2026:**
- Complete the signal-quality assessment module.
- Implement noise-robustness experiments.
- Integrate explainability and confidence visualization.
- Complete the Streamlit application.
- Conduct testing with at least five potential users.
- Evaluate results and prepare the final product report.

**Fallback plan:**

If the full multi-module implementation cannot be completed, the minimum working product will support ECG upload, preprocessing, signal-quality assessment, arrhythmia classification, waveform visualization and a basic analysis report.

### 7. Expected Deliverable

A working, software-only ECG analysis application that demonstrates the integration of digital signal processing, machine learning, explainable AI and interactive visualization.

The final submission will include the application source code, GitHub repository, experimental results, user-testing evidence and a 4–6 page product report.

**Scope limitation:** CardioAI is intended for educational and research purposes. It will not be presented as a clinically validated diagnostic system.
