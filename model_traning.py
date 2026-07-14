import pandas as pd

# Preprocessing Libraries
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

# Evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Save Model
import pickle

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/loan_prediction.csv")

# -----------------------------
# Fill Missing Values
# -----------------------------
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].mean())
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mean())
df["ApplicantIncome"] = df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean())
df["CoapplicantIncome"] = df["CoapplicantIncome"].fillna(df["CoapplicantIncome"].mean())

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

# -----------------------------
# Label Encoding
# -----------------------------
le = LabelEncoder()

columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

for col in columns:
    df[col] = le.fit_transform(df[col])

# -----------------------------
# Features and Target
# -----------------------------
X = df.drop(["Loan_ID", "Loan_Status"], axis=1)
y = df["Loan_Status"]

# -----------------------------
# SMOTE
# -----------------------------
smote = SMOTE(random_state=42)
X, y = smote.fit_resample(X, y)

# -----------------------------
# Scaling
# -----------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Dictionary of Models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss")
}

best_model = None
best_accuracy = 0

print("=" * 60)

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"\n{name}")
    print("Accuracy:", accuracy)

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, prediction))

    print("\nClassification Report")
    print(classification_report(y_test, prediction))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

print("\nBest Accuracy:", best_accuracy)

pickle.dump(best_model, open("model/model.pkl", "wb"))

print("\nModel Saved Successfully!")