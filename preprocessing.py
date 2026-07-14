import pandas as pd

# Load dataset
df = pd.read_csv("dataset/loan_prediction.csv")

# Check dataset
print("Shape:", df.shape)
print("\nInformation:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill numerical columns with mean
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].mean())
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mean())
df["ApplicantIncome"] = df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean())
df["CoapplicantIncome"] = df["CoapplicantIncome"].fillna(df["CoapplicantIncome"].mean())

# Fill categorical columns with mode
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

print("\nMissing Values After Filling:")
print(df.isnull().sum())
from sklearn.preprocessing import LabelEncoder

# Create LabelEncoder object
le = LabelEncoder()

# List of categorical columns
categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

# Apply Label Encoding
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

print("\nEncoded Dataset:")
print(df.head())
from imblearn.over_sampling import SMOTE

# Separate features (X) and target (y)
X = df.drop(["Loan_ID", "Loan_Status"], axis=1)
y = df["Loan_Status"]

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

print("\nBefore SMOTE:")
print(y.value_counts())

print("\nAfter SMOTE:")
print(y_resampled.value_counts())
from sklearn.preprocessing import StandardScaler

# Scale the features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_resampled)

# Convert back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print("\nScaled Dataset:")
print(X_scaled.head())
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_resampled,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)