# 🔧 Predictive Maintenance & Anomaly Detection in 6G-Integrated Smart Manufacturing

## 📌 Project Overview

This project develops a predictive maintenance framework for 6G-enabled smart manufacturing systems. The goal is to detect early-stage machine anomalies before operational efficiency degrades, enabling proactive maintenance instead of reactive repairs.

The system uses machine-specific baseline modeling and unsupervised anomaly detection to identify abnormal operational patterns in real time.

---

## 🏭 Problem Statement

Manufacturing industries face:

- Unexpected machine breakdowns  
- High maintenance and downtime costs  
- Difficulty detecting early warning signals in noisy sensor data  

Traditional rule-based thresholds fail because:

- Normal behavior varies by machine and operating mode  
- Early anomalies are subtle and multidimensional  

This project addresses these challenges using AI-driven anomaly detection.

---

## 📊 Dataset Description

The dataset contains:

- Machine operational parameters (Temperature, Vibration, Power)
- Network performance metrics (Latency, Packet Loss)
- Quality indicators (Defect Rate, Error Rate)
- Production metrics (Production Speed)
- Operational mode
- Efficiency status label

Each record represents real-time machine behavior in a smart factory environment.

---

## ⚙️ Methodology

### 1️⃣ Data Preprocessing
- Removed duplicates and inconsistencies
- Combined Date and Time into Datetime column
- Sorted data per Machine_ID

### 2️⃣ Baseline Behavior Modeling
- Rolling mean per machine
- Learned normal operational ranges

### 3️⃣ Feature Engineering
- Sensor deviation from rolling baseline
- Vibration-to-power instability ratio
- Maintenance score decay pattern
- Error escalation indicators

### 4️⃣ Anomaly Detection
- Isolation Forest algorithm used
- Unsupervised learning approach
- Each record assigned an anomaly score

### 5️⃣ Risk Classification
Anomaly scores categorized into:
- Low Risk
- Medium Risk
- High Risk

### 6️⃣ Temporal Risk Escalation Analysis
- Risk trend smoothing
- Escalation detection
- High-risk machine ranking

---

## 📈 Key Performance Indicators (KPIs)

- Anomaly Score
- Maintenance Risk Level
- High-Risk Machine Ranking
- Early Warning Lead Time
- Downtime Prevention Signals

---

## 🖥 Streamlit Dashboard Features

The deployed dashboard includes:

- Risk distribution overview
- High-risk machine count
- Machine-specific risk trend visualization
- Sensor deviation analysis
- Maintenance alert panel
- Time window selection
- Operation mode filtering
- Adjustable risk threshold slider

---

## 🚀 Deployment

The application is deployed using Streamlit Cloud.

Main files:
- `app.py`
- `final_predictive_maintenance_output.csv`
- `requirements.txt`

To run locally:

```bash
streamlit run app.py
