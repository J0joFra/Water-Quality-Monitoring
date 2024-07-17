import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Path to your CSV file
csv_file = r"C:\Users\JoaquimFrancalanci\Downloads\archive (20)\brisbane_water_quality.csv"

# Load data into a DataFrame
df = pd.read_csv(csv_file)

# Drop columns with quality information
df = df.drop(columns=['Dissolved Oxygen [quality]', 'Chlorophyll [quality]', 'Temperature [quality]', 
                      'Dissolved Oxygen (%Saturation) [quality]', 'pH [quality]', 'Salinity [quality]',
                      'Specific Conductance [quality]', 'Turbidity [quality]'], errors='ignore')

# Convert 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Drop rows with NaN values
df = df.dropna()

# Filter rows for the year 2023 (August to December)
df_2023 = df[(df['Timestamp'].dt.year == 2023) & (df['Timestamp'].dt.month >= 8)]

# Selecting variables for prediction
X_columns = ['Chlorophyll', 'Temperature', 'Salinity']
y_column = 'Dissolved Oxygen'

# Impute missing values in 2023 dataset
imputer = SimpleImputer(strategy='mean')
df_2023_imputed = imputer.fit_transform(df_2023[X_columns + [y_column]])

# Extract X_train_imputed and y_train_imputed from imputed data
X_train_imputed = df_2023_imputed[:, :-1]  # All columns except the last one (y_column)
y_train_imputed = df_2023_imputed[:, -1]   # Last column (y_column)

# Initializing and fitting the model
model = LinearRegression()
model.fit(X_train_imputed, y_train_imputed)

# Filter rows for the year 2024 (January to June)
df_2024 = df[(df['Timestamp'].dt.year == 2024) & (df['Timestamp'].dt.month <= 7)]

# Predicting values for 2024 based on selected variables
X_test_2024 = df_2024[X_columns]
predictions_2024 = model.predict(X_test_2024)

# Adding predictions to the 2024 DataFrame
df_2024['Predicted Dissolved Oxygen'] = predictions_2024

# Displaying predictions
print("Predicted Dissolved Oxygen for 2024:")
print(df_2024[['Timestamp', 'Chlorophyll', 'Temperature', 'Salinity', 'Predicted Dissolved Oxygen']])

# Plotting observed vs predicted values
plt.figure(figsize=(16, 12))

# Chlorophyll vs Dissolved Oxygen
plt.subplot(3, 1, 1)
plt.scatter(df_2024['Chlorophyll'], df_2024['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2024['Chlorophyll'], df_2024['Predicted Dissolved Oxygen'], color='red', label='Predicted', alpha=0.5)
plt.title('Chlorophyll vs Dissolved Oxygen')
plt.xlabel('Chlorophyll')
plt.ylabel('Dissolved Oxygen')
plt.legend()

# Temperature vs Dissolved Oxygen
plt.subplot(3, 1, 2)
plt.scatter(df_2024['Temperature'], df_2024['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2024['Temperature'], df_2024['Predicted Dissolved Oxygen'], color='red', label='Predicted', alpha=0.5)
plt.title('Temperature vs Dissolved Oxygen')
plt.xlabel('Temperature')
plt.ylabel('Dissolved Oxygen')
plt.legend()

# Salinity vs Dissolved Oxygen
plt.subplot(3, 1, 3)
plt.scatter(df_2024['Salinity'], df_2024['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2024['Salinity'], df_2024['Predicted Dissolved Oxygen'], color='red', label='Predicted', alpha=0.5)
plt.title('Salinity vs Dissolved Oxygen')
plt.xlabel('Salinity')
plt.ylabel('Dissolved Oxygen')
plt.legend()

plt.tight_layout()
plt.show()
