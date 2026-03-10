# MedScope X: Personal Health Analytics System

## Overview

**MedScope X** is a modular Python-based health analytics system designed to evaluate key physiological indicators, lifestyle habits, and potential disease risks. The program collects user health data, performs medical calculations, and generates a personalized health report.

The system integrates several biomedical metrics such as Body Mass Index (BMI), Basal Metabolic Rate (BMR), hydration levels, cardiovascular risk factors, and metabolic indicators to produce a comprehensive health score.

MedScope X is intended as an educational project demonstrating how computational tools can analyze health data and simulate decision-support systems used in digital health technologies.

---

## Features

### Health Metric Calculations

The system calculates several important health metrics:

* Body Mass Index (BMI)
* Basal Metabolic Rate (BMR)
* Hydration score
* Cardiovascular risk estimation
* Diabetes risk estimation

### Lifestyle Analysis

The program evaluates several lifestyle factors:

* Sleep habits
* Weekly exercise
* Stress levels
* Daily sugar intake
* Water intake

### Health Risk Modeling

Using rule-based algorithms, the system estimates potential risks for conditions such as:

* cardiovascular risk
* metabolic disorders
* hydration deficiency

### Overall Health Score

MedScope X generates a final **health score (0–100)** based on the combined results of physiological and lifestyle analysis.

### Patient History Tracking

Each health scan is stored so users can track changes in their health score across multiple sessions.

### Health Reports

The system generates a clear, structured report summarizing:

* calculated metrics
* risk indicators
* overall health score

---

## Project Structure

```
medscope_x/
│
├── main.py
├── menu.py
├── input_module.py
├── bmi_module.py
├── bmr_module.py
├── hydration_module.py
├── cardiovascular_module.py
├── metabolic_module.py
├── probability_model.py
├── health_score_engine.py
├── analytics_module.py
├── history_manager.py
├── report_generator.py
└── utils.py
```

Each module performs a specific function to keep the system organized and maintainable.

---

## How the Program Works

1. The user launches the program.
2. Basic health data is collected.
3. Lifestyle questions are asked.
4. Medical formulas calculate physiological metrics.
5. Risk models estimate disease likelihood.
6. A health score is calculated.
7. A final health report is displayed.
8. Results can optionally be saved to a history database.

---

## Example Output

```
====== MEDSCOPE X REPORT ======

Patient: Alex
BMI: 22.4
BMR: 1540 kcal/day

Hydration Score: 78
Cardiovascular Risk: Low
Diabetes Risk: Low

Overall Health Score: 86 / 100
```

---

## Technologies Used

* Python 3
* Modular programming architecture
* JSON file storage
* Rule-based health analytics

---

## Educational Purpose

This project demonstrates how computational models can simulate aspects of medical decision support systems used in healthcare technology and digital health monitoring.

---

## Disclaimer

MedScope X is designed for educational and demonstration purposes only.
It does **not provide medical diagnoses** and should not replace professional medical advice.
