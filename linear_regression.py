import pandas as pd
from sklearn.linear_model import LinearRegression

# Path to your CSV file
csv_file = r"C:\Users\JoaquimFrancalanci\Downloads\archive (20)\brisbane_water_quality.csv"

# Load data into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filter rows for the year 2023 (August to December)
df_2023 = df[(df['Timestamp'].dt.year == 2023) & (df['Timestamp'].dt.month >= 8)]

# Filter rows for the year 2024 (January to June)
df_2024 = df[(df['Timestamp'].dt.year == 2024) & (df['Timestamp'].dt.month <= 6)]

# Selecting variables for prediction
X_columns = ['Chlorophyll', 'Temperature', 'Salinity']
y_column = 'Dissolved Oxygen'

# Splitting data into training and testing sets for 2023
X_train = df_2023[X_columns]
y_train = df_2023[y_column]

# Initializing and fitting the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting values for 2024 based on selected variables
X_test_2024 = df_2024[X_columns]
predictions_2024 = model.predict(X_test_2024)

# Adding predictions to the 2024 DataFrame
df_2024['Predicted Dissolved Oxygen'] = predictions_2024

# Displaying predictions
print("Predicted Dissolved Oxygen for 2024:")
print(df_2024[['Timestamp', 'Chlorophyll', 'Temperature', 'Salinity', 'Predicted Dissolved Oxygen']])
