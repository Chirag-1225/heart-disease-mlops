
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, recall_score

# 1. Simulate or load the UCI Heart Disease Dataset
# For testing, we generate synthetic data matching the schema
def load_data():
    np.random.seed(42)
    n_samples = 300
    data = {
        'age': np.random.randint(29, 77, n_samples),
        'sex': np.random.choice([0, 1], n_samples),
        'cp': np.random.randint(0, 4, n_samples),
        'trestbps': np.random.randint(94, 200, n_samples), # Blood Pressure
        'chol': np.random.randint(126, 564, n_samples),    # Cholesterol
        'thalach': np.random.randint(71, 202, n_samples),   # Max Heart Rate
        'target': np.random.choice([0, 1], n_samples)      # 1 = Disease, 0 = No Disease
    }
    df = pd.DataFrame(data)
    return df

print("📦 Loading dataset...")
df = load_data()

# 2. Split Features & Target
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Feature Scaling (Crucial for Logistic Regression and SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Model Exploration & Comparison
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(eval_metric='logloss', random_state=42)
}

best_model = None
best_recall = 0

print("\n🚀 Training and evaluating models...")
for name, model in models.items():
    # Train
    model.fit(X_train_scaled, y_train)
    # Predict
    preds = model.predict(X_test_scaled)
    
    # Evaluate
    acc = accuracy_score(y_test, preds)
    rec = recall_score(y_test, preds)
    
    print(f"--- {name} ---")
    print(f"Accuracy: {acc:.4f} | Recall: {rec:.4f}")
    
    # Save the model with the highest Recall
    if rec > best_recall:
        best_recall = rec
        best_model = model
        best_model_name = name

print(f"\n🏆 Best Model Selected: {best_model_name} with Recall: {best_recall:.4f}")

# 5. Save the best model and scaler artifact
with open('best_model.pkl', 'wb') as m_file:
    pickle.dump(best_model, m_file)

with open('scaler.pkl', 'wb') as s_file:
    pickle.dump(scaler, s_file)

print("💾 Artifacts saved successfully as 'best_model.pkl' and 'scaler.pkl'!")