import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from datetime import datetime, timedelta
from streamlit_card import card


# Data preparation
training_data = {
    'Type': [
        'normal', 'neptune', 'satan', 'ipsweep', 'DoS', 
        'smurf', 'nmap', 'guess_passwd', 'imap'
    ],
    'Count': [343, 214, 301, 110, 120, 646, 493, 956, 892]
}
df = pd.DataFrame(training_data)

st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;}  
        header {visibility: hidden;}  
        .alert-box, .alert-box2{
            position: fixed;
            top: 40px;
            right: 20px;
            background-color: #f8d7da;
            color: #721c24;
            padding: 5px 15px;
            border-radius: 15px;
            border: 1px solid #f5c6cb;
            z-index: 9999;
            align-items: center;
            display: none;
        }
        .alert-box2{
            top: 100px;
         }
        .alert-box button, .alert-box2 button{
            right: 10px;
            padding: 5px 10px;
            border: none;
            cursor: pointer;
            border-radius: 15px;
        }
        .resolve-btn {
            background-color: #4caf50;
            color: white;
        }
        .ignore-btn {
            background-color: #f44336;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

user_name = "John Doe"
user_avatar = "https://www.w3schools.com/w3images/avatar2.png"  

st.markdown(f"""
    <div style="display: flex; margin: -120px -100px; justify-content: flex-end; align-items: center; padding: 2px; background-color: #f1f1f1;">
        <p style="margin: 10px; font-weight: bold">{user_name}</p>
        <img src="{user_avatar}" alt="User Avatar" style="width: 30px; height: 30px; border-radius: 50%;margin-right: 30px;">
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='font-size: 36px; margin-top:-50px'>Cybersecurity Threat Monitoring Dashboard</h1>", unsafe_allow_html=True)
st.write("Total Threat Count: ", df['Count'].sum())
st.write("Unique Threat Types Detected: ", df['Type'].nunique())

st.write("The model has detected several anomalies in your data, categorized by type.")
threat_types = st.multiselect("Select Threat Types", df['Type'].unique(), default=df['Type'].unique())
filtered_df = df[df['Type'].isin(threat_types)]
c1, c2 = st.columns(2)
with c1:
        df3 = pd.DataFrame({
            'Count': [10, 5],
            'Type': ['Normal', 'Abnormal']
        })
        st.markdown('<h6 class="small-header">Threats Severity Distribution</h6>', unsafe_allow_html=True)
        
        # Define the colors (you can customize this)
        colors = ['#66b3ff', '#ff6666']  # Blue for Normal, Red for Abnormal

        # Create the semi-pie chart (half-pie)
        fig, ax = plt.subplots(figsize=(8, 3))
        wedges, texts, autotexts = ax.pie(df3['Count'], labels=df3['Type'], autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.4))

        # Make it a half-pie chart by setting the angle limits (i.e., 180 degrees)
        ax.set_aspect('equal')
        # Display the pie chart in Streamlit
        st.pyplot(fig)
with c2:
        st.markdown('<h6 class="small-header">Anomalies by Type</h6>', unsafe_allow_html=True)
        fig, ax = plt.subplots()
        ax.pie(df['Count'], labels=df['Type'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 
        st.pyplot(fig)

c3, c4 = st.columns(2)
with c3:
        st.markdown('<h6 class="small-header">Number of Anomalies by Type</h6>', unsafe_allow_html=True)
        plt.figure(figsize=(12, 6))
        sns.barplot(data=filtered_df, x="Type", y="Count", palette="coolwarm")
        plt.xticks(rotation=45)
        plt.title("Threat Count by Type")
        st.pyplot(plt)
with c4:
        incident_data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=10, freq='M'),
            'Incidents': [15, 30, 22, 40, 58, 25, 60, 80, 35, 45]
        })
        st.markdown('<h6 class="small-header">Historical Incident Data</h6>', unsafe_allow_html=True)

        fig, ax = plt.subplots()
        ax.plot(incident_data['Date'], incident_data['Incidents'], marker='o', linestyle='-', color='b')

        ax.set_title("Cybersecurity Incidents Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Incidents")

        plt.xticks(rotation=45)
        st.pyplot(fig)


data = {
    'Anomaly ID': [1, 2, 3, 4],
    'Date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04'],
    'Anomaly Type': ['normal', 'Phishing', 'Malware', 'DoS'],
    'Severity': ['High', 'Medium', 'High', 'Low'],
    'Model Prediction': ['True', 'False', 'True', 'True'],
    'Action Taken': ['Alert Raised', 'No Action', 'Alert Raised', 'Blocked']
}
df2 = pd.DataFrame(data)
st.markdown('<h6 class="small-header">Historical Anomalies detected by Model</h6>', unsafe_allow_html=True)
st.dataframe(df2)

# Real-time Alerts in Sidebar
alerts = pd.DataFrame({
    'Alert ID': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'Alert Type': ['DDoS', 'Malware', 'Phishing', 'SQL Injection', 'Ransomware'],
    'Severity': ['Critical', 'High', 'Medium', 'High', 'Critical'],
    'Timestamp': pd.to_datetime(['2023-10-01 12:00', '2023-10-02 14:30', '2023-10-03 15:45', 
                                 '2023-10-04 10:00', '2023-10-05 09:00'])
})

# Sidebar Alert List
st.sidebar.header("Alerts")
alert_selection = st.sidebar.selectbox("Select an Alert", alerts['Alert ID'])
selected_alert = alerts[alerts['Alert ID'] == alert_selection]

# Display alert details in the main panel
st.sidebar.subheader(f"Alert Details: {selected_alert['Alert ID'].values[0]}")
st.sidebar.write(f"**Alert Type:** {selected_alert['Alert Type'].values[0]}")
st.sidebar.write(f"**Severity:** {selected_alert['Severity'].values[0]}")
st.sidebar.write(f"**Timestamp:** {selected_alert['Timestamp'].values[0]}")
st.sidebar.write(f"**Action Taken:** {selected_alert['Alert Type'].values[0]}")

# Display action buttons
if selected_alert['Severity'].values[0] == "Critical":
    alert_message = "Critical alert detected! Immediate attention required."
    st.markdown(
        f"""
        <div id="alert" class="alert-box">
            {alert_message}
            <button class="resolve-btn" onclick="alert('Threat resolved')">Resolve</button>
            <button class="ignore-btn" onclick="alert('Threat ignored')">Ignore</button>
        </div>
        <script>
        // Display the alert for 7 seconds, then hide it
        setTimeout(function() {{
            var alertBox = document.getElementById('alert');
            if (alertBox) {{
                alertBox.style.display = 'none';
            }}
        }}, 7000);
        </script>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div id="alert" class="alert-box2">
           Anomaly detected. Would you like to resolve it, or should we assign<br> responsibility to the system for handling it?
            ( Start IN: 04:49)
            <br>
            <button class="resolve-btn" onclick="alert('Threat resolved')">YES</button>
            <button class="ignore-btn" onclick="alert('Threat ignored')">NO</button>
        </div>
        <script>
        setTimeout(function() {{
            var alertBox = document.getElementById('alert');
            if (alertBox) {{
                alertBox.style.display = 'none';
            }}
        }}, 7000);
        </script>
        """,
        unsafe_allow_html=True
    )
