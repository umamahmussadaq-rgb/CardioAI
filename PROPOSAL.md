Project Proposal
CardioAI: A Quality-Aware and Explainable AI Platform for Noise-Robust ECG Arrhythmia Analysis
Student Name: Umamah binte Mussadaq
Enrollment Number: 537450
Course: AI-853 — Advanced Programming in Python
Project Track: Track B — Product Development
1. Problem
ECG recordings can contain baseline wander, motion artifacts and other noise that reduce the reliability of automated analysis. Users also need to understand whether a recording is suitable for analysis and why an AI model produced a particular prediction. CardioAI will provide an integrated software workflow for ECG preprocessing, signal-quality assessment, arrhythmia classification, prediction explanation and reporting.
2. Target Users and Evidence
Target users include biomedical engineering students, ECG and biomedical signal-processing researchers, and university research laboratories. Before development, feedback will be collected from at least five potential users about their workflows, difficulties and desired features. Interview findings will be added after genuine interviews; no user feedback is claimed at this proposal stage.
3. Existing Solutions and Product Gap
The project will review ExChanGeAI, Cordis and BRAVEHEART as related ECG analysis solutions and compare their documented features with CardioAI. The proposed focus is an accessible integrated workflow that assesses signal quality, evaluates classification under controlled noise, displays prediction confidence and visual explanations, and produces an analysis report. The comparison will be verified during the product review rather than assuming these capabilities are absent from existing tools.
4. Product and AI Components
CardioAI will be a Python web application. Planned modules: (i) ECG upload using supported CSV/WFDB formats; (ii) filtering, baseline-wander removal and normalization; (iii) signal-quality assessment; (iv) machine-learning/deep-learning classification of selected ECG classes; (v) controlled noise-robustness experiments; (vi) explainability visualizations and prediction-confidence indicators; and (vii) waveform display and downloadable reports. Candidate datasets are MIT-BIH Arrhythmia Database and PTB-XL, subject to task and label compatibility. Planned tools include Python, NumPy, Pandas, SciPy, NeuroKit2, scikit-learn, PyTorch or TensorFlow, Plotly and Streamlit.
5. Success Measures
Classification will be evaluated using accuracy, precision, recall, F1-score, confusion matrices and AUROC where appropriate. Signal-quality assessment will be evaluated against labelled or controlled-quality examples where available. Robustness will be measured by comparing classification metrics across controlled noise levels. Usability will be assessed through task-based testing and feedback from at least five real users. All reported results will come from actual experiments and testing.
6. Plan and Fallback
By 4 December 2026: complete the product review, obtain and inspect data, implement ECG loading and preprocessing, train an initial classifier, demonstrate a working prototype and maintain GitHub commits. By 18 December 2026: integrate signal-quality assessment, noise experiments, explainability, confidence display and the Streamlit interface; test with at least five users; and complete the product report. If time or compute is limited, the fallback product will provide ECG upload, preprocessing, waveform visualization, a baseline classifier and a basic report.
7. Expected Deliverable and Scope
The deliverable will be a working software-only ECG analysis application, its GitHub source repository, experimental evaluation and a 4–6 page product report. CardioAI is for educational and research use and is not a clinically validated diagnostic device.
