# Dataset Documentation

## CICIDS2017 Dataset
- **Source:** [https://intrusion-detection.distrinet-research.be/WTMC2021/extended_doc.html](https://intrusion-detection.distrinet-research.be/WTMC2021/extended_doc.html)
- **Size:** ~1.07GB
- **Files:** 5 CSV files (one for each day: Monday-Friday)
- **Features:** 84 features including:
  - **Flow ID**
  - **Source IP/Port, Destination IP/Port**
  - **Protocol, Timestamp**
  - **Flow Duration, Flow Packets/s, Flow IAT (Mean, Std, Max, Min)**
  - **Total Fwd/Bwd Packets and Lengths, Fwd/Bwd Packet Lengths (Max, Min, Mean, Std)**
  - **Packet Length Mean, Std, Variance**
  - **Flags (FIN, SYN, RST, PSH, ACK, URG, CWE, ECE)**
  - **Down/Up Ratio, Average Packet Size, Avg Fwd/Bwd Segment Size**
  - **Subflow Fwd/Bwd Packets and Bytes**
  - **Initial Window Bytes (forward and backward)**
  - **Active/Idle Mean, Std, Max, Min**
- **Attack Types:** Includes various network attack categories such as:
  - **Brute Force**
  - **Denial of Service (DoS)**
  - **DDoS (Distributed DoS)**
  - **Heartbleed**
  - **Infiltration**
  - **Botnet**
  - **Web attacks (SQL Injection, XSS, etc.)**
  - **PortScan**

## NSL-KDD Dataset
- **Source:** [https://www.kaggle.com/datasets/hassan06/nslkdd](https://www.kaggle.com/datasets/hassan06/nslkdd)
- **Size:** ~25MB
- **Files:** 4 text files
- **Features:** 41 columns, including:
  - **Duration, Protocol Type, Service, Flag**
  - **Source and Destination Bytes**
  - **Land, Wrong Fragment, Urgent**
  - **Login Status, Number of Failed Logins, Number of Compromised Conditions**
  - **Number of Shells, Accessed Files, Outbound Commands**
  - **Host and Service Rates, Error Rates**
  - **Count, srv_count, srv_serror_rate, srv_rerror_rate**
  - **Host Connection Stats (same_srv_rate, diff_srv_rate, etc.)**
- **Attack Categories:** Four main attack categories:
  - **DoS (Denial of Service)**
  - **Probe (Surveillance and probing)**
  - **R2L (Remote to Local)**
  - **U2R (User to Root)**

## Processed Data
- **Location:** [https://drive.google.com/drive/folders/18BbTXRiLOqGWfiF4s_YNjAIsZIWQFTLV?usp=sharing](https://drive.google.com/drive/folders/18BbTXRiLOqGWfiF4s_YNjAIsZIWQFTLV?usp=sharing)
- **Processing Steps:** See `docs/data_processing.md` for detailed steps on preprocessing, feature selection, and normalization.
- **Sample Data:** A subset of processed data is available in `processed_data/samples/` for quick reference and testing.