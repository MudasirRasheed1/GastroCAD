# EGD-CAD-System

## Overview

The **EGD-CAD-System** is an advanced Computer-Aided Diagnosis (CAD) system designed to enhance the detection and localization of upper gastrointestinal (GI) diseases during Esophagogastroduodenoscopy (EGD) procedures. Built using artificial intelligence (AI), specifically machine learning (ML) and deep learning (DL), this system targets 28 upper GI conditions affecting the esophagus, stomach, and duodenum. Unlike existing CAD systems, it not only classifies diseases but also provides critical spatial information about abnormalities, improving diagnostic accuracy and clinical decision-making in gastroenterology.

This project leverages two datasets:
- **GastroVision**: 8,000 annotated images representing 27 diseases, published July 16, 2023.
- **GastroHun**: 8,834 images and 4,729 annotated video sequences with 22 anatomical landmarks, published January 17, 2025.

The system aims to reduce human error, support less experienced clinicians, and set new standards in patient care by integrating precise disease detection and localization into routine endoscopic evaluations.

## Features

- **Disease Classification**: Identifies 28 upper GI diseases using deep learning models.
- **Spatial Localization**: Provides precise locations of abnormalities via segmentation techniques.
- **Datasets**: Trained on GastroVision and GastroHun for robust generalization.
- **Clinical Impact**: Enhances diagnostic accuracy and treatment planning in gastroenterology.
## Directory structure
EGD-CAD-System/
├── data/                # Raw and processed datasets
├── src/                 # Source code (preprocessing, models, utils, etc.)
├── experiments/         # Logs, checkpoints, and results
├── docs/                # Documentation and references
├── tests/               # Unit tests
├── scripts/             # Workflow automation scripts
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── LICENSE              # License file
