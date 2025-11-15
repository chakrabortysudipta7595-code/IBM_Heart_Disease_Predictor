"""
Heart Disease Prediction Model Training Script
This script loads the UCI Heart Disease Dataset, trains a logistic regression model,
and saves it for use in the Flask application.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os
import warnings
warnings.filterwarnings('ignore')

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Load the dataset
print("Loading dataset...")

# Prefer a local `heart.csv` (repo root or common locations) if available
local_paths = [
    'heart.csv',
    os.path.join('data', 'heart.csv'),
    os.path.join('datasets', 'heart.csv'),
    r'c:\Users\User\Downloads\archive\heart.csv'
]

df = None
for p in local_paths:
    if os.path.exists(p):
        print(f"Found local dataset at: {p}")
        try:
            df = pd.read_csv(p)
            break
        except Exception as e:
            print(f"Failed to read {p}: {e}")

if df is None:
    # Fallback to UCI dataset URL
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
    column_names = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
    ]
    try:
        df = pd.read_csv(url, names=column_names)
    except Exception:
        # Fallback: create a sample dataset if URL fails
        print("Could not load from URL, creating sample dataset for demonstration...")
        np.random.seed(42)
        n_samples = 303
        df = pd.DataFrame({
            'age': np.random.randint(29, 77, n_samples),
            'sex': np.random.randint(0, 2, n_samples),
            'cp': np.random.randint(0, 4, n_samples),
            'trestbps': np.random.randint(94, 200, n_samples),
            'chol': np.random.randint(126, 564, n_samples),
            'fbs': np.random.randint(0, 2, n_samples),
            'restecg': np.random.randint(0, 3, n_samples),
            'thalach': np.random.randint(60, 203, n_samples),
            'exang': np.random.randint(0, 2, n_samples),
            'oldpeak': np.random.uniform(0, 6.2, n_samples),
            'slope': np.random.randint(0, 3, n_samples),
            'ca': np.random.randint(0, 5, n_samples),
            'thal': np.random.randint(0, 4, n_samples),
            'target': np.random.randint(0, 2, n_samples)
        })

print(f"Dataset shape: {df.shape}")
print(f"\nDataset info:")
print(df.head())

# Handle missing values and ensure numeric types where appropriate
df.replace('?', np.nan, inplace=True)

# If dataset doesn't have 'target' column, try to detect it
if 'target' not in df.columns:
    # Common alternative names
    alt_targets = ['heartdisease', 'heart_disease', 'HeartDisease', 'output', 'y']
    found = False
    for t in alt_targets:
        if t in df.columns:
            df = df.rename(columns={t: 'target'})
            found = True
            print(f"Renamed column '{t}' to 'target'")
            break
    if not found:
        # As a last resort, assume last column is target
        last_col = df.columns[-1]
        if last_col.lower() not in [c.lower() for c in ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]:
            print(f"Assuming last column '{last_col}' is the target column and renaming to 'target'")
            df = df.rename(columns={last_col: 'target'})

# Try to coerce numeric columns to numeric types where possible
for col in df.columns:
    # Skip object columns that are clearly categorical like 'thal' if they are numeric strings
    try:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    except Exception:
        pass

# Drop rows with NaNs introduced by coercion or original missing values
df.dropna(inplace=True)

print(f"\nDataset shape after cleaning: {df.shape}")

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Convert target to binary (0 or 1)
# In UCI dataset: 0 = no disease, 1-4 = disease present
y = (y > 0).astype(int)

print(f"\nTarget distribution:")
print(f"No Disease (0): {(y == 0).sum()}")
print(f"Disease (1): {(y == 1).sum()}")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# Feature scaling (important for logistic regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nTraining Logistic Regression model...")

# Train the logistic regression model
model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    solver='lbfgs'
)

model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Disease', 'Disease']))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the model and scaler
print("\nSaving model and scaler...")
pickle.dump(model, open('models/heart_disease_model.pkl', 'wb'))
pickle.dump(scaler, open('models/scaler.pkl', 'wb'))

# Save feature names
with open('models/feature_names.pkl', 'wb') as f:
    pickle.dump(list(X.columns), f)

print("Model saved successfully!")
print("\nProject files ready:")
print("- models/heart_disease_model.pkl")
print("- models/scaler.pkl")
print("- models/feature_names.pkl")
