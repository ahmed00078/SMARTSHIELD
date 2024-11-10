# Data Processing Documentation

## Overview
This document details the data preprocessing pipeline for the SmartShield project's cybersecurity datasets: CICIDS2017 and NSL-KDD.

## Datasets

### 1. CICIDS2017 Dataset
#### Raw Data Structure
- Format: CSV files (Monday through Friday)
- Size: ~50GB total
- Features: Network flow data
- Attack Types: Various cyber attacks including DoS, DDoS, Brute Force, XSS, SQL Injection, etc.

#### Processing Steps
1. **Data Cleaning**
   ```python
   # Column standardization
   df.columns = df.columns.str.strip().str.replace(' ', '_')
   
   # Handle missing/infinite values
   df = df.replace([np.inf, -np.inf], np.nan)
   df = df.dropna()
   ```

2. **Feature Processing**
   - Numerical features: StandardScaler normalization
   - Label encoding: Convert attack types to numerical values
   - Feature selection: All features retained for comprehensive analysis

3. **Quality Checks**
   - Verify no missing values
   - Confirm feature scaling ranges (-1 to 1)
   - Validate label distribution
   - Check for data leakage

### 2. NSL-KDD Dataset
#### Raw Data Structure
- Format: TXT files
- Size: ~25MB
- Features: 41 columns (network connection data)
- Attack Categories: DoS, Probe, R2L, U2R

#### Processing Steps
1. **Data Loading**
   - Support for both TXT and ARFF formats
   - Consistent column naming
   - Remove difficulty column

2. **Feature Processing**
   ```python
   # Categorical features
   categorical_cols = ['protocol_type', 'service', 'flag']
   
   # Numerical features
   numeric_cols = [col for col in df.columns 
                  if col not in categorical_cols + ['label']]
   ```

3. **Encoding**
   - Categorical features: LabelEncoder
   - Numerical features: StandardScaler
   - Labels: Encoded to numerical values

## Sample Dataset Creation
### CICIDS2017 Sample
- 1000 records per day
- Stratified sampling to maintain attack distribution
- All feature columns included

### NSL-KDD Sample
- 1000 records from each file
- Maintain original attack distribution
- All features included
