import numpy as np
import pandas as pd

# Setting the seed for reproducibility
np.random.seed(0)

# Number of rows
num_rows = 2000
# Percentage of fraudulent transactions
fraud_percentage = 0.1

# Generating data
data = {
    "Transaction Amount": np.random.exponential(scale=100, size=num_rows).round(2),
    "Transaction Frequency": np.random.poisson(lam=2, size=num_rows),
    "Geographic Location": np.random.choice(["Local", "Foreign"], size=num_rows, p=[0.9, 0.1]),
    "Time of Transaction": np.random.choice(["Usual", "Unusual"], size=num_rows, p=[0.8, 0.2]),
    "Cardholder’s Purchase History": np.random.choice(["Consistent", "Inconsistent"], size=num_rows, p=[0.95, 0.05]),
    "Merchant Category": np.random.choice(["High Risk", "Low Risk"], size=num_rows, p=[0.2, 0.8]),
    "CNP Transactions": np.random.choice(["Yes", "No"], size=num_rows, p=[0.3, 0.7]),
    "Device Information": np.random.choice(["Known", "Unknown"], size=num_rows, p=[0.9, 0.1]),
    "Velocity Checks": np.random.choice(["Normal", "High"], size=num_rows, p=[0.9, 0.1]),
    "Failed Authentication Attempts": np.random.choice(["None", "Multiple"], size=num_rows, p=[0.95, 0.05]),
    "Card Expiration Date and CVV": np.random.choice(["Correct", "Incorrect"], size=num_rows, p=[0.98, 0.02]),
    "International Transactions": np.random.choice(["No", "Yes"], size=num_rows, p=[0.9, 0.1]),
    "Fraudulent": np.random.choice([False, True], size=num_rows, p=[1 - fraud_percentage, fraud_percentage])
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Adjusting some entries to better simulate fraud
fraud_indices = df[df['Fraudulent']].index

for index in fraud_indices:
    # Increase likelihood of anomalies in fraud cases
    if np.random.rand() < 0.7: df.at[index, 'Transaction Amount'] *= np.random.choice([5, 0.2])
    if np.random.rand() < 0.5: df.at[index, 'Transaction Frequency'] = np.random.randint(5, 10)
    if np.random.rand() < 0.6: df.at[index, 'Geographic Location'] = "Foreign"
    if np.random.rand() < 0.6: df.at[index, 'Time of Transaction'] = "Unusual"
    if np.random.rand() < 0.8: df.at[index, 'Cardholder’s Purchase History'] = "Inconsistent"
    if np.random.rand() < 0.6: df.at[index, 'Merchant Category'] = "High Risk"
    if np.random.rand() < 0.7: df.at[index, 'CNP Transactions'] = "Yes"
    if np.random.rand() < 0.5: df.at[index, 'Device Information'] = "Unknown"
    if np.random.rand() < 0.4: df.at[index, 'Velocity Checks'] = "High"
    if np.random.rand() < 0.3: df.at[index, 'Failed Authentication Attempts'] = "Multiple"
    if np.random.rand() < 0.2: df.at[index, 'Card Expiration Date and CVV'] = "Incorrect"
    if np.random.rand() < 0.5: df.at[index, 'International Transactions'] = "Yes"

# Display a sample of the data
df.to_csv('credit_card_fraud.csv', index=False)
