import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_squared_error
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

# Predicting values for 2023 based on selected variables (for validation)
predictions_2023 = model.predict(X_train_imputed)

# Calculate R^2 score
r2 = r2_score(df_2023[y_column], predictions_2023)
print(f'R^2 Score: {r2:.2f}')

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(df_2023[y_column], predictions_2023)
print(f'Mean Squared Error: {mse:.2f}')

# Chlorophyll vs Dissolved Oxygen
plt.figure(figsize=(12, 6))
plt.scatter(df_2023['Chlorophyll'], df_2023['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2023['Chlorophyll'], predictions_2023, color='red', label='Predicted', alpha=0.5)
plt.title('Chlorophyll vs Dissolved Oxygen (2023)')
plt.xlabel('Chlorophyll')
plt.ylabel('Dissolved Oxygen')
plt.legend()

# Temperature vs Dissolved Oxygen
plt.figure(figsize=(12, 6))
plt.scatter(df_2023['Temperature'], df_2023['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2023['Temperature'], predictions_2023, color='red', label='Predicted', alpha=0.5)
plt.title('Temperature vs Dissolved Oxygen (2023)')
plt.xlabel('Temperature')
plt.ylabel('Dissolved Oxygen')
plt.legend()

# Salinity vs Dissolved Oxygen
plt.figure(figsize=(12, 6))
plt.scatter(df_2023['Salinity'], df_2023['Dissolved Oxygen'], color='blue', label='Observed', alpha=0.5)
plt.scatter(df_2023['Salinity'], predictions_2023, color='red', label='Predicted', alpha=0.5)
plt.title('Salinity vs Dissolved Oxygen (2023)')
plt.xlabel('Salinity')
plt.ylabel('Dissolved Oxygen')
plt.legend()

plt.tight_layout()
plt.show()
