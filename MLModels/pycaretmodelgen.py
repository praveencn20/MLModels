
from pycaret.anomaly import *
import pandas as pd

# 'dataset' is the input dataframe from Power BI

# Initialize PyCaret setup
exp_ano = setup(data=dataset, 
                normalize=True,  # Normalize numeric features
                ignore_features=['transaction_id', 'transaction_datetime', 'merchant_id', 'transaction_type', 'transaction_status'],
                session_id=123,
                silent=True,
                verbose=False)

# Create Isolation Forest model for anomaly detection
model = create_model('iforest')

# Assign anomaly labels and scores to dataset
results = assign_model(model)

# Output the dataframe with two new columns: 'Anomaly' and 'Anomaly_Score'
output = results
