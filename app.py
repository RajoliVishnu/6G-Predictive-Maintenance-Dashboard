import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration

st.set_page_config(
    page_title="6G Predictive Maintenance Dashboard",
    layout="wide"
)

# Professional Header Styling
st.markdown("""
<style>
div.block-container {padding-top: 1rem;}
h1, h2, h3 {color: #003366;}
</style>
""", unsafe_allow_html=True)

st.title("🔧 Predictive Maintenance & Anomaly Detection")
st.markdown("### 6G-Integrated Smart Manufacturing System")
st.markdown("Developed for Thales Group – Smart Factory Risk Monitoring Framework")


# Load Dataset

@st.cache_data
def load_data():
    return pd.read_csv("final_predictive_maintenance_output.csv", parse_dates=["Datetime"])

df = load_data()

# Sidebar Filters

st.sidebar.header("Filter Options")

machine_list = sorted(df["Machine_ID"].unique())
selected_machine = st.sidebar.selectbox("Select Machine ID", machine_list)

operation_modes = ["All"] + list(df["Operation_Mode"].unique())
selected_mode = st.sidebar.selectbox("Select Operation Mode", operation_modes)

min_date = df["Datetime"].min()
max_date = df["Datetime"].max()

selected_dates = st.sidebar.date_input(
    "Select Time Window",
    [min_date, max_date]
)

risk_threshold = st.sidebar.slider(
    "Risk Score Threshold",
    float(df["Risk_Score"].min()),
    float(df["Risk_Score"].max()),
    float(df["Risk_Score"].quantile(0.90))
)


# Apply Filters

if selected_mode != "All":
    df = df[df["Operation_Mode"] == selected_mode]

df = df[
    (df["Datetime"] >= pd.to_datetime(selected_dates[0])) &
    (df["Datetime"] <= pd.to_datetime(selected_dates[1]))
]

# KPI Overview Section

st.subheader("📊 Predictive Maintenance Overview")

total_machines = df["Machine_ID"].nunique()
high_risk_machines = df[df["Maintenance_Risk_Level"] == "High"]["Machine_ID"].nunique()

early_detection = df[
    (df["Maintenance_Risk_Level"] == "High") &
    (df["Efficiency_Status"] != "Low")
]

downtime_prevention_index = len(early_detection)

col1, col2, col3 = st.columns(3)
col1.metric("Total Machines", total_machines)
col2.metric("High Risk Machines", high_risk_machines)
col3.metric("Downtime Prevention Signals", downtime_prevention_index)

st.subheader("Risk Level Distribution")
risk_counts = df["Maintenance_Risk_Level"].value_counts()
st.bar_chart(risk_counts)

# Machine Risk Escalation Trend

st.subheader("📈 Machine Risk Escalation Trend")

machine_data = df[df["Machine_ID"] == selected_machine].copy()
machine_data = machine_data.sort_values("Datetime")

machine_data["Risk_Smoothed"] = machine_data["Risk_Score"].rolling(window=30).mean()

plt.style.use("seaborn-v0_8-whitegrid")

fig1, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(
    machine_data["Datetime"],
    machine_data["Risk_Smoothed"],
    color="#003366",
    linewidth=3,
    label="Smoothed Risk Score"
)

ax1.axhline(
    y=risk_threshold,
    color="#C62828",
    linestyle="--",
    linewidth=2,
    label="High-Risk Threshold"
)

ax1.fill_between(
    machine_data["Datetime"],
    machine_data["Risk_Smoothed"],
    risk_threshold,
    where=(machine_data["Risk_Smoothed"] >= risk_threshold),
    color="#FFCDD2",
    alpha=0.6
)

ax1.set_title(f"Machine {selected_machine} – Risk Escalation Timeline", fontsize=14, fontweight="bold")
ax1.set_xlabel("Time")
ax1.set_ylabel("Risk Score")
ax1.legend()

plt.xticks(rotation=45)
st.pyplot(fig1)

# Sensor Deviation Visualization

st.subheader("📊 Sensor Deviation Analysis")

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(
    machine_data["Datetime"],
    machine_data["Temp_Deviation"],
    color="#F57C00",
    linewidth=2,
    label="Temperature Deviation"
)

ax2.plot(
    machine_data["Datetime"],
    machine_data["Vib_Deviation"],
    color="#6A1B9A",
    linewidth=2,
    label="Vibration Deviation"
)

ax2.plot(
    machine_data["Datetime"],
    machine_data["Power_Deviation"],
    color="#00897B",
    linewidth=2,
    label="Power Deviation"
)

ax2.set_title(f"Machine {selected_machine} – Sensor Behavior Deviations", fontsize=14, fontweight="bold")
ax2.set_xlabel("Time")
ax2.set_ylabel("Deviation from Baseline")
ax2.legend()

plt.xticks(rotation=45)
st.pyplot(fig2)

# High-Risk Machine Ranking

st.subheader("🚨 High-Risk Machine Ranking")

ranking = df.groupby("Machine_ID")["Risk_Score"].mean().sort_values(ascending=False)
st.dataframe(ranking.head(10))


# Maintenance Alert Panel

st.subheader("⚠ Maintenance Alerts")

alerts = df[df["Risk_Score"] >= risk_threshold]

st.write(f"Number of Records Above Threshold: {len(alerts)}")

st.dataframe(
    alerts[["Machine_ID", "Datetime", "Risk_Score"]]
    .sort_values("Risk_Score", ascending=False)
    .head(20)
)

st.markdown("---")
st.markdown("### End of Dashboard – 6G Predictive Maintenance System")