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
```
EGD-CAD-System/
├── data/
├── src/
├── experiments/
├── docs/
├── tests/
├── scripts/
├── requirements.txt
├── README.md
└── LICENSE
```

# SSS Kenshi Yao Protocol in Gastroenterology

The **SSS Kenshi Yao Protocol** in gastroenterology refers to the **Systematic Screening Protocol for the Stomach (SSS)**, developed by Dr. Kenshi Yao, a prominent Japanese gastroenterologist and expert in endoscopic diagnosis. This protocol is designed to improve the detection of early gastric cancer and other abnormalities in the stomach during upper gastrointestinal endoscopy (gastroscopy). It provides a standardized, methodical approach to ensure the entire stomach is thoroughly examined, reducing the likelihood of missing subtle lesions.

## What It Is
The SSS protocol outlines a step-by-step method for endoscopists to systematically observe the stomach’s mucosa using conventional white-light endoscopy. It emphasizes proper preparation, technique, and a structured sequence of observations to map the stomach comprehensively. The goal is to enhance the detection of early-stage gastric cancers, which can be challenging to identify because they often appear as subtle mucosal changes (e.g., gastritis-like lesions).

## Key Components of the SSS Protocol

### 1. Optimal Preparation
- Patients are given an antiperistaltic agent (e.g., hyoscine butylbromide) to reduce stomach motility, making it easier to examine the mucosa.
- Mucolytics (e.g., pronase) and defoaming agents (e.g., simethicone) may be used to clear mucus and bubbles, improving visibility.

### 2. Systematic Observation
- The protocol divides the stomach into specific regions and quadrants, ensuring all areas are inspected.
- A typical sequence involves observing the stomach in a standardized order, such as:
  - **Antrum**: Including the pylorus and surrounding areas.
  - **Body**: Lesser and greater curvatures, anterior and posterior walls.
  - **Fundus**: Viewed in retroflexion (J-maneuver) to inspect the cardia and upper stomach.
  - **Cardia**: The area around the gastroesophageal junction.
- The endoscopist takes multiple images (e.g., at least 20–40, depending on the version) to document key landmarks and any suspicious findings.

### 3. Key Signs to Look For
Dr. Yao emphasizes recognizing subtle markers of early gastric neoplasia, such as:
- **Surface changes**: Irregularities in the mucosal pattern.
- **Color changes**: Redness, pallor, or discoloration compared to surrounding tissue.
- **Light reflection**: Differences in how light reflects off abnormal areas.
- **Spontaneous bleeding**: Small areas of bleeding that may indicate a lesion.

### 4. Image Documentation
- The protocol encourages taking enough photos to cover all regions, as studies suggest that longer examination times and more images correlate with higher detection rates of abnormalities.

## Why It’s Important
- **Early Detection**: Early gastric cancer often has a good prognosis if caught before it invades deeper layers, but it’s easily missed without a systematic approach. The SSS protocol addresses this by ensuring no area is overlooked.
- **Standardization**: It provides a reproducible method that can be taught to endoscopists worldwide, improving consistency in gastric screening.
- **Adaptability**: While designed for white-light endoscopy, it can be combined with advanced techniques like chromoendoscopy or magnifying narrow-band imaging (NBI), which Dr. Yao also advocates for characterizing suspicious lesions.

## Background and Development
Dr. Kenshi Yao, based at Fukuoka University Chikushi Hospital, proposed the SSS protocol in response to limitations in existing gastric screening methods. For example:
- The Japanese Society of Gastroenterological Cancer Screening (JSGCS) protocol was detailed but complex, with too many images for practical use outside Japan.
- The European Society of Gastrointestinal Endoscopy (ESGE) protocol was simpler (only 4 images) but less thorough.

The SSS strikes a balance, offering a “minimum required standard” that is both practical and effective. It was detailed in publications like *The Endoscopic Diagnosis of Early Gastric Cancer* (Annals of Gastroenterology, 2013).

## Practical Example
During an endoscopy using the SSS protocol:
1. The endoscopist starts by clearing mucus and bubbles.
2. They advance the scope to the pylorus, then systematically move through the antrum, body, and fundus, taking images of the lesser curvature, greater curvature, anterior wall, and posterior wall in each section.
3. In retroflexion, they inspect the cardia and fundus.
4. If a subtle lesion (e.g., a slightly elevated area with irregular color) is spotted, they may switch to magnifying endoscopy or NBI for closer inspection.

## Significance in Gastroenterology
The SSS protocol is particularly valuable in regions with high gastric cancer rates, like Japan, where screening is routine. It’s also gaining attention globally as a way to improve diagnostic yield in Western countries, where gastric cancer is less common but often diagnosed at later stages. By training endoscopists in this method, it’s possible to catch abnormalities like early gastric cancer, *Helicobacter pylori*-related changes, or precancerous lesions (e.g., intestinal metaplasia) earlier.


## Summary Table

| Code | Region                            | View      |
|------|-----------------------------------|-----------|
| A1   | Anterior wall - Antrum           | Antegrade |
| A2   | Anterior wall - Lower body       | Antegrade |
| A3   | Anterior wall - Middle upper body | Antegrade |
| P1   | Posterior wall - Antrum          | Antegrade |
| P2   | Posterior wall - Lower body      | Antegrade |
| P3   | Posterior wall - Middle upper body | Antegrade |
| L1   | Lesser curvature - Antrum        | Antegrade |
| L2   | Lesser curvature - Lower body    | Antegrade |
| L3   | Lesser curvature - Middle upper body | Antegrade |
| G1   | Greater curvature - Antrum       | Antegrade |
| G2   | Greater curvature - Lower body   | Antegrade |
| G3   | Greater curvature - Middle upper body | Antegrade |
| A4   | Anterior wall - Fundus cardia    | Retroflex |
| A5   | Anterior wall - Middle upper body | Retroflex |
| A6   | Anterior wall - Incisura         | Retroflex |
| P4   | Posterior wall - Fundus cardia   | Retroflex |
| P5   | Posterior wall - Middle upper body | Retroflex |
| P6   | Posterior wall - Incisura        | Retroflex |
| L4   | Lesser curvature - Fundus cardia | Retroflex |
| L5   | Lesser curvature - Middle upper body | Retroflex |
| L6   | Lesser curvature - Incisura      | Retroflex |
| G4   | Greater curvature - Fundus cardia | Retroflex |
| NA   | Not applicable (unqualified images) | N/A       |



