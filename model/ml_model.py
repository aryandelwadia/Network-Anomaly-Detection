import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, classification_report
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# ==============================
# Load the dataset
# ==============================
df_large = pd.read_csv(
    r"c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/Realistic_Large-Scale_Network_Traffic_Dataset.csv"
)

print("Initial dataset shape:", df_large.shape)

# Graph: distribution of labels before processing
sns.countplot(x=df_large['label'])
plt.title("Label Distribution (Raw)")
plt.show()

# ==============================
# Split features and target
# ==============================
X = df_large.drop(columns=['label'])
y = df_large['label']

# Graph: null values per column before preprocessing
plt.figure(figsize=(10, 5))
sns.heatmap(X.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values (Before Imputation)")
plt.show()

# ==============================
# Label Encoding
# ==============================
label_encoders = {}
for col in ['ip.src', 'ip.dst', 'http.request.uri']:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le  

# Save the encoders
joblib.dump(label_encoders, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/label_encoders.pkl')

# Graph: encoded features distributions
for col in ['ip.src', 'ip.dst', 'http.request.uri']:
    plt.figure(figsize=(8, 4))
    sns.histplot(X[col], bins=50, kde=False)
    plt.title(f"Distribution after Label Encoding: {col}")
    plt.show()

# ==============================
# Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Graph: label distribution in train/test
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
sns.countplot(x=y_train, ax=ax[0])
ax[0].set_title("Train Label Distribution")
sns.countplot(x=y_test, ax=ax[1])
ax[1].set_title("Test Label Distribution")
plt.show()

# ==============================
# Handle Missing Values
# ==============================
imputer = SimpleImputer(strategy='most_frequent')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

joblib.dump(imputer, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/imputer.pkl')

# Graph: check missing after imputation
plt.figure(figsize=(10, 5))
sns.heatmap(pd.DataFrame(X_train).isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values After Imputation (Train)")
plt.show()

# ==============================
# Save trained column names
# ==============================
trained_columns = X.columns
joblib.dump(trained_columns, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/trained_columns.pkl')

# ==============================
# Train Isolation Forest
# ==============================
clf = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.05, random_state=42)
clf.fit(X_train)

# Save model
joblib.dump(clf, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/isolation_forest_model.pkl')

# ==============================
# Predictions
# ==============================
y_pred = clf.predict(X_test)
y_pred = np.where(y_pred == -1, 1, 0)  # Convert -1 → anomaly(1), 1 → normal(0)

# Graph: prediction distribution
sns.countplot(x=y_pred)
plt.title("Predicted Anomaly Distribution (Test)")
plt.show()

# ==============================
# Evaluation
# ==============================
accuracy = accuracy_score(y_test, y_pred)
print(f"Isolation Forest Model Accuracy: {accuracy:.4f}")
