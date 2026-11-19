
# CardioAI
### An Integrated AI-Powered ECG Monitoring and Arrhythmia Analysis Platform

## Project Overview

CardioAI is a biomedical engineering project designed to integrate ECG acquisition hardware with an AI-powered software platform for real-time ECG monitoring and offline ECG analysis.

The platform supports two operating modes:

1. **Real-Time ECG Monitoring:** Acquires ECG signals from connected hardware and processes them continuously.
2. **Offline ECG Analysis:** Allows users to upload ECG recordings and datasets for preprocessing, visualization, and AI-based arrhythmia classification.

Both modes utilize a shared signal-processing and AI inference pipeline to ensure consistent analysis.

## Key Features

- Real-time ECG signal acquisition.
- Offline ECG recording and dataset upload.
- ECG signal preprocessing and noise filtering.
- Baseline wander and noise assessment.
- ECG waveform visualization.
- AI-based heartbeat and arrhythmia classification.
- Signal-quality assessment.
- Prediction confidence estimation.
- Uncertain prediction rejection (selective prediction).
- Explainability and visualization of AI predictions.
- Downloadable ECG analysis reports.

## System Architecture

### Input Layer
- Live ECG hardware acquisition.
- Offline ECG file and dataset upload.

### Signal Processing Layer
- Signal validation.
- Metadata handling.
- Signal normalization.
- Noise filtering.
- Beat segmentation and detection.
- Signal-quality assessment.

### Artificial Intelligence Layer
- ECG heartbeat classification.
- Model confidence estimation.
- Quality-aware prediction rejection.

### Visualization Layer
- Real-time ECG waveform display.
- Arrhythmia classification results.
- Confidence indicators.
- Signal-quality warnings.
- Explainability visualizations.
- Analysis reports.

## Dataset

The initial development will utilize:

- MIT-BIH Arrhythmia Database.
- PTB-XL ECG Dataset (optional, for a separate compatible classification task).

Dataset labels and classification mappings will be documented according to the selected experimental methodology.

## Technology Stack

### Programming
- Python

### Signal Processing
- NumPy
- SciPy
- Pandas
- WFDB
- NeuroKit2

### Machine Learning / Deep Learning
- Scikit-learn
- TensorFlow / PyTorch

### Visualization and Interface
- Streamlit
- Plotly
- Matplotlib

### Hardware Integration
- ECG acquisition hardware
- Microcontroller-based communication interface
- USB Serial / Wi-Fi / Bluetooth (subject to hardware verification)

### Version Control
- Git
- GitHub

## Project Objectives

1. Develop an integrated ECG acquisition and analysis platform.
2. Support both real-time and offline ECG inputs.
3. Implement a unified signal-processing pipeline.
4. Develop AI-based arrhythmia classification.
5. Incorporate signal-quality assessment and prediction confidence.
6. Evaluate system performance under different noise conditions.
7. Provide interpretable and reproducible ECG analysis.

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- AUROC (where appropriate)
- Signal-quality assessment performance
- Prediction coverage and rejection performance
- Real-time processing latency

## Project Status

**Development Stage:** Proposed / In Progress

The project will be developed in phases, beginning with hardware verification and offline ECG analysis, followed by real-time hardware integration, AI implementation, and system evaluation.

## Safety Disclaimer

CardioAI is an educational and research prototype. It is not a clinically validated diagnostic system and must not be used as a replacement for professional medical assessment.

## Repository Structure

```text
CardioAI/
│
├── README.md
├── PROPOSAL.md
├── proposal/
│   └── CardioAI_Updated_Project_Proposal.pdf
│
├── data/
│   ├── raw/
│   └── processed/
│
├── hardware/
│   ├── acquisition/
│   └── communication/
│
├── preprocessing/
│
├── models/
│
├── evaluation/
│
├── visualization/
│
├── app/
│
├── requirements.txt
└── .gitignore
```

*Directory structure represents the planned organization and may be adjusted during implementation.*

## References

1. MIT-BIH Arrhythmia Database: https://physionet.org/content/mitdb/
2. PTB-XL Dataset: https://physionet.org/content/ptb-xl/
3. ExChanGeAI: https://www.jmir.org/2026/1/e81116/
4. XBeats ECG Monitoring System: https://www.mdpi.com/2624-6120/3/2/13
