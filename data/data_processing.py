import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
from typing import Dict, List
import logging
import json
import arff

class DataPreprocessor:
    def __init__(self):
        self.logger = self._setup_logger()
        self.label_encoders = {}
        self.scalers = {}
        self.metadata = {
            'nsl_kdd': {}
        }

    def _setup_logger(self) -> logging.Logger:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)

    def process_nsl_kdd_files(self, input_dir: str) -> Dict[str, pd.DataFrame]:
        """Process all NSL-KDD dataset files"""
        processed_dfs = {}
        
        # Define expected files
        expected_files = {
            'KDDTrain+.txt': 'train_full',
            'KDDTest+.txt': 'test_full',
            'KDDTrain+_20Percent.txt': 'train_20',
            'KDDTest-21.txt': 'test_21'
        }
        
        # Define column names for NSL-KDD dataset
        columns = [
            'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
            'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
            'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
            'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
            'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
            'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
            'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
            'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
            'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label', 'difficulty'
        ]
        
        # Process each file
        for filename, shortname in expected_files.items():
            txt_path = os.path.join(input_dir, filename)
            arff_path = os.path.join(input_dir, filename.replace('.txt', '.arff'))
            
            # Try reading ARFF first, fall back to TXT if needed
            try:
                if os.path.exists(arff_path):
                    self.logger.info(f"Processing ARFF file: {filename.replace('.txt', '.arff')}")
                    with open(arff_path) as f:
                        arff_data = arff.load(f)
                    arff_data = list(arff_data)
                    df = pd.DataFrame(arff_data['data'], columns=columns)
                elif os.path.exists(txt_path):
                    self.logger.info(f"Processing TXT file: {filename}")
                    df = pd.read_csv(txt_path, names=columns)
                else:
                    self.logger.warning(f"Neither ARFF nor TXT file found for {filename}")
                    continue
                
                # Remove difficulty column if present
                if 'difficulty' in df.columns:
                    df = df.drop('difficulty', axis=1)
                
                # Identify categorical and numerical columns
                categorical_cols = ['protocol_type', 'service', 'flag']
                numeric_cols = [col for col in df.columns if col not in categorical_cols + ['label']]
                
                # Store metadata
                self.metadata['nsl_kdd'][shortname] = {
                    'n_samples': len(df),
                    'n_features': len(df.columns) - 1,
                    'categorical_features': categorical_cols,
                    'numeric_features': numeric_cols,
                    'label_distribution': df['label'].value_counts().to_dict()
                }
                
                # Encode categorical features
                for col in categorical_cols:
                    le = LabelEncoder()
                    df[col] = le.fit_transform(df[col].astype(str))
                    self.label_encoders[f'nsl_kdd_{shortname}_{col}'] = le
                
                # Scale numerical features
                scaler = StandardScaler()
                df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
                self.scalers[f'nsl_kdd_{shortname}'] = scaler
                
                processed_dfs[shortname] = df
                
            except Exception as e:
                self.logger.error(f"Error processing {filename}: {str(e)}")
                continue
                
        return processed_dfs

    def save_processed_data(self, dfs: Dict[str, pd.DataFrame], output_dir: str, dataset_type: str):
        """Save processed DataFrames to CSV files"""
        output_path = os.path.join(output_dir, dataset_type)
        os.makedirs(output_path, exist_ok=True)
        
        for name, df in dfs.items():
            file_path = os.path.join(output_path, f"processed_{name}")
            df.to_csv(file_path, index=False)
            self.logger.info(f"Saved processed data to {file_path}")

    def save_metadata(self, output_path: str):
        """Save metadata to JSON"""
        metadata_path = os.path.join(output_path, 'metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(self.metadata, f, indent=4)
        self.logger.info(f"Saved metadata to {metadata_path}")

def main():
    # Initialize preprocessor
    preprocessor = DataPreprocessor()
    
    # Define paths
    base_path = "../../data"
    raw_data_path = os.path.join(base_path, "raw_data")
    processed_data_path = os.path.join(base_path, "processed_data")
    
    # Process NSL-KDD dataset
    nsl_kdd_path = os.path.join(raw_data_path, "NSL-KDD-Dataset-master")
    if os.path.exists(nsl_kdd_path):
        nsl_kdd_dfs = preprocessor.process_nsl_kdd_files(nsl_kdd_path)
        preprocessor.save_processed_data(nsl_kdd_dfs, processed_data_path, "nsl_kdd")
    
    # Save metadata
    preprocessor.save_metadata(processed_data_path)

if __name__ == "__main__":
    main()