# Data Processing Documentation

## Overview
This document outlines the data preprocessing implementation for the SmartShield project's cybersecurity datasets: CICIDS2017 and NSL-KDD.

## Implementation Details

### DataPreprocessor Class
```python
class DataPreprocessor:
    def __init__(self):
        self.label_encoders = {}
        self.scalers = {}
        self.metadata = {
            'cicids': {},
            'nsl_kdd': {}
        }
```

### 1. CICIDS2017 Dataset Processing

#### Raw Data Structure
- Format: CSV files (Monday through Friday)
- Files: monday.csv, tuesday.csv, wednesday.csv, thursday.csv, friday.csv

#### Processing Steps
1. **Data Cleaning**
```python
# Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Handle infinite and missing values
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()
```

2. **Feature Processing**
- Label encoding for attack types
- StandardScaler normalization for numerical features
- Metadata collection (samples, features, label distribution)

### 2. NSL-KDD Dataset Processing

#### Raw Data Structure
- Format: TXT and ARFF files
- Files: 
  - KDDTrain+.txt
  - KDDTest+.txt
  - KDDTrain+_20Percent.txt
  - KDDTest-21.txt

#### Processing Steps
1. **Data Loading**
- Support for both TXT and ARFF formats
- Predefined column names
- Removal of difficulty column if present

2. **Feature Processing**
```python
# Categorical features
categorical_cols = ['protocol_type', 'service', 'flag']

# Numerical features
numeric_cols = [col for col in df.columns 
               if col not in categorical_cols + ['label']]

# Encode categorical features
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Scale numerical features
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
```

### Metadata Collection
- Number of samples
- Number of features
- Label distribution
- Feature types (for NSL-KDD)

### Data Storage
```python
# Save processed data
output_path = os.path.join(output_dir, dataset_type)
os.makedirs(output_path, exist_ok=True)

# Save as CSV
df.to_csv(file_path, index=False)

# Save metadata as JSON
json.dump(self.metadata, f, indent=4)
```

## Usage

```python
# Initialize preprocessor
preprocessor = DataPreprocessor()

# Process CICIDS2017
cicids_dfs = preprocessor.process_cicids_files(cicids_path)
preprocessor.save_processed_data(cicids_dfs, processed_data_path, "cicids")

# Process NSL-KDD
nsl_kdd_dfs = preprocessor.process_nsl_kdd_files(nsl_kdd_path)
preprocessor.save_processed_data(nsl_kdd_dfs, processed_data_path, "nsl_kdd")

# Save metadata
preprocessor.save_metadata(processed_data_path)
```

## File Structure
```
data/
├── raw_data/
│   ├── CICIDS2017_improved/
│   └── NSL-KDD-Dataset-master/
└── processed_data/
    ├── cicids/
    ├── nsl_kdd/
```