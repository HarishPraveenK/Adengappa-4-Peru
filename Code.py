import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the dataset
file_path = r"C:\Users\haris\Downloads\german_credit_data.csv"
data = pd.read_csv(file_path)

# Drop irrelevant column
data.drop(columns=['Unnamed: 0'], inplace=True)

# Handle missing values
categorical_imputer = SimpleImputer(strategy='most_frequent')
data[['Saving accounts', 'Checking account']] = categorical_imputer.fit_transform(
    data[['Saving accounts', 'Checking account']]
)

# Encode categorical variables
categorical_columns = ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose', 'Risk']
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  # Save encoders for potential inverse transformation

# Scale numerical features
numerical_columns = ['Age', 'Credit amount', 'Duration']
scaler = MinMaxScaler()
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Correlation analysis
correlation_matrix = data.corr()

# Feature selection based on correlation and domain knowledge
selected_features = ['Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration', 'Purpose']

# Extract features and target variable
X = data[selected_features]
y = data['Risk']

# Display results
print("Processed Data Sample:\n", data.head())
print("\nCorrelation Matrix:\n", correlation_matrix)
print("\nSelected Features:", selected_features)
