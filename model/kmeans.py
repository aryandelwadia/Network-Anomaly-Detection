import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load the dataset
df_large = pd.read_csv(r"c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/Realistic_Large-Scale_Network_Traffic_Dataset.csv")

# Split features and target
X = df_large.drop(columns=['label'])
y = df_large['label']   # 0 = normal, 1 = anomaly

# Initialize label encoders dictionary
label_encoders = {}
for col in ['ip.src', 'ip.dst', 'http.request.uri']:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

# Save the label encoders for prediction
joblib.dump(label_encoders, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/label_encoders.pkl')

# Train-test split (80-20 for evaluation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle missing values by imputing with the most frequent value
imputer = SimpleImputer(strategy='most_frequent')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Save the imputer for later use
joblib.dump(imputer, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/imputer.pkl')

# Save trained column names
trained_columns = X.columns
joblib.dump(trained_columns, 'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/trained_columns.pkl')

# -------------------
# Train KMeans model
# -------------------
k = 5  # number of clusters (can tune)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_train)

# Compute distances on training set
dists_train = np.min(kmeans.transform(X_train), axis=1)

threshold = np.percentile(dists_train, 80)

# Save the trained KMeans model and threshold
joblib.dump({'kmeans': kmeans, 'threshold': threshold},
            'c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/model/kmeans_model.pkl')

# -------------------
# Predict on test data
# -------------------
dists_test = np.min(kmeans.transform(X_test), axis=1)

# Predict anomalies: 1 = anomaly, 0 = normal
y_pred = (dists_test > threshold).astype(int)

# -------------------
# Evaluate the model
# -------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"KMeans Model Accuracy: {accuracy}")
