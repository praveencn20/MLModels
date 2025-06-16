
import pandas as pd
import numpy as np


from faker import Faker

fake = Faker()
np.random.seed(42)

num_records = 1000

data = {
    'transaction_id': [fake.uuid4() for _ in range(num_records)],
    'transaction_datetime': [fake.date_time_between(start_date='-90d', end_date='now') for _ in range(num_records)],
    'merchant_id': np.random.choice(['M001', 'M002', 'M003', 'M004', 'M005'], size=num_records),
    'transaction_type': np.random.choice(['dine_in', 'takeaway', 'delivery'], size=num_records),
    'transaction_amount': np.round(np.random.normal(loc=50, scale=30, size=num_records), 2),
    'transaction_status': np.random.choice(['completed', 'pending', 'failed'], size=num_records, p=[0.85, 0.10, 0.05])
}

df = pd.DataFrame(data)

# Fix negative or zero amounts
df['transaction_amount'] = df['transaction_amount'].apply(lambda x: x if x > 0 else np.random.uniform(1, 10))

df = df.sort_values(by='transaction_datetime').reset_index(drop=True)

# Save to CSV for import into Power BI
df.to_csv('C:\Projects\synthetic_transactions.csv', index=False)

print(df.head())
