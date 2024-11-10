# Dataset Documentation

This document details the cybersecurity datasets used in the SmartShield project for training and testing AI models.

## CICIDS2017 Dataset

### Overview
- **Source:** [Canadian Institute for Cybersecurity IDS 2017 Dataset](https://intrusion-detection.distrinet-research.be/WTMC2021/extended_doc.html)
- **Size:** ~1.07GB
- **Format:** 5 CSV files (Monday through Friday)
- **Description:** A comprehensive network traffic dataset containing both normal and attack traffic patterns

### Features (84 total)
#### Network Flow Basics
- Flow ID
- Source IP/Port
- Destination IP/Port
- Protocol
- Timestamp

#### Flow Statistics
- Flow Duration
- Flow Packets/s
- Flow IAT (Mean, Std, Max, Min)
- Total Forward/Backward Packets
- Packet Lengths (Max, Min, Mean, Std)
- Packet Length Statistics (Mean, Std, Variance)

#### Protocol Flags
- FIN, SYN, RST, PSH
- ACK, URG, CWE, ECE

#### Advanced Metrics
- Down/Up Ratio
- Average Packet Size
- Average Forward/Backward Segment Size
- Subflow Forward/Backward Packets and Bytes
- Initial Window Bytes (forward and backward)
- Active/Idle Statistics (Mean, Std, Max, Min)

### Attack Categories
1. **Network Attacks**
   - Brute Force
   - Denial of Service (DoS)
   - Distributed DoS (DDoS)
   - PortScan

2. **Application Attacks**
   - Web Attacks
     - SQL Injection
     - Cross-Site Scripting (XSS)
   - Heartbleed

3. **System Attacks**
   - Infiltration
   - Botnet

## NSL-KDD Dataset

### Overview
- **Source:** [NSL-KDD Dataset on Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd)
- **Size:** ~25MB
- **Format:** 4 text files
- **Description:** An improved version of the KDD99 dataset, addressing issues of redundant records and bias

### Features (41 total)
#### Basic Features
- Duration
- Protocol Type
- Service
- Flag
- Source/Destination Bytes

#### Content Features
- Land
- Wrong Fragment
- Urgent
- Login Status
- Failed Logins Count
- Compromised Conditions Count

#### System Access Features
- Number of Shells
- Accessed Files Count
- Outbound Commands

#### Statistical Features
- Host and Service Rates
- Error Rates
- Connection Statistics
  - Count
  - srv_count
  - srv_serror_rate
  - srv_rerror_rate
- Host Connection Patterns
  - same_srv_rate
  - diff_srv_rate

### Attack Categories
1. **DoS (Denial of Service)**
   - Network resource exhaustion attacks

2. **Probe**
   - Surveillance and scanning activities

3. **R2L (Remote to Local)**
   - Unauthorized access from remote machine

4. **U2R (User to Root)**
   - Privilege escalation attempts

## Processed Data

### Access and Storage
- **Google Drive Location:** [Processed Dataset](https://drive.google.com/drive/folders/18BbTXRiLOqGWfiF4s_YNjAIsZIWQFTLV?usp=sharing)
- **Local Storage:** `processed_data/samples/`

### Processing Documentation
- Detailed preprocessing steps available in `docs/data_processing.md`
- Includes information on:
  - Feature selection methodology
  - Data normalization techniques
  - Handling missing values
  - Feature engineering steps

### Sample Data
- Quick-start datasets available in `processed_data/samples/`
  - CICIDS samples: `processed_data/samples/cicids/`
  - NSL-KDD samples: `processed_data/samples/nsl_kdd/`
- Suitable for initial testing and development